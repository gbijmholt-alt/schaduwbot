import base64, struct, os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["DB_PATH"] = "/tmp/schaduwbot_test.sqlite"
if os.path.exists(os.environ["DB_PATH"]): os.remove(os.environ["DB_PATH"])
import base58
import config as C, curve
from decoder import decode_program_data, D_TRADE, D_CREATE, D_COMPLETE, TradeEvent, CreateEvent, CompleteEvent
from state import TokenState
from store import Store
from simulator import Simulator
import report

def pk(seed): return base58.b58encode(bytes([seed]) * 32).decode()
def enc_pk(seed): return bytes([seed]) * 32
def s(x): b = x.encode(); return struct.pack("<I", len(b)) + b

def test_decoder():
    body = enc_pk(1) + struct.pack("<QQ?", 5_000_000_000, 123_456_789_000, True) + enc_pk(2) + struct.pack("<q", 1700000000) \
           + struct.pack("<QQQQ", 35_000_000_000, 900_000_000_000_000, 5_000_000_000, 600_000_000_000_000) \
           + enc_pk(3) + struct.pack("<QQ", 95, 4750000) + enc_pk(4) + struct.pack("<QQ", 30, 1500000)
    line = "Program data: " + base64.b64encode(D_TRADE + body).decode()
    ev = decode_program_data(line); assert isinstance(ev, TradeEvent), ev
    assert ev.mint == pk(1) and ev.sol_amount == 5_000_000_000 and ev.is_buy and ev.user == pk(2) and ev.v_sol == 35_000_000_000 and ev.creator == pk(4)
    body = s("Naam") + s("SYM") + s("https://ipfs.io/ipfs/abc") + enc_pk(5) + enc_pk(6) + enc_pk(7) + enc_pk(8) + struct.pack("<q", 1700000000) + struct.pack("<QQQQ", 1_073_000_000_000_000, 30_000_000_000, 793_100_000_000_000, 1_000_000_000_000_000)
    ev = decode_program_data("Program data: " + base64.b64encode(D_CREATE + body).decode()); assert isinstance(ev, CreateEvent)
    assert ev.symbol == "SYM" and ev.mint == pk(5) and ev.bonding_curve == pk(6) and ev.creator == pk(8) and ev.v_sol == 30_000_000_000
    # oude versie zonder staart
    ev = decode_program_data("Program data: " + base64.b64encode(D_CREATE + s("N") + s("S") + s("u") + enc_pk(5) + enc_pk(6) + enc_pk(7)).decode()); assert ev.creator is None
    ev = decode_program_data("Program data: " + base64.b64encode(D_COMPLETE + enc_pk(1) + enc_pk(2) + enc_pk(3) + struct.pack("<q", 1)).decode()); assert isinstance(ev, CompleteEvent)
    assert decode_program_data("Program log: Instruction: Buy") is None
    assert decode_program_data("Program data: " + base64.b64encode(b"\x00" * 8 + b"x").decode()) is None
    print("decoder ok")

def test_curve():
    v_sol, v_tok = 30_000_000_000, 1_073_000_000_000_000
    assert abs(curve.mcap_sol(v_sol, v_tok) - 27.96) < 0.05, curve.mcap_sol(v_sol, v_tok)
    tok, cost = curve.buy(v_sol, v_tok, 1.0, "pp")
    # nieuwe reserves na onze koop
    lam = int(1.0 * (1 - C.FEE_PUMP - C.FEE_TERMINAL["pp"]) * 1e9); v_sol2, v_tok2 = v_sol + lam, v_tok - tok
    sol_back, _ = curve.sell(v_sol2, v_tok2, tok, "pp")
    loss = 1 - sol_back
    assert 0.03 < loss < 0.045, loss     # ~2x1.75% + 2x prio
    assert curve.progress(C.INITIAL_REAL_TOKEN_RESERVES) == 0 and curve.progress(0) == 1
    print(f"curve ok (rondje kost {loss:.2%})")

def test_simulator():
    store = Store(os.environ["DB_PATH"]); sim = Simulator(store, store.bump_funnel)
    ts = TokenState(mint="M", symbol="T", creator=pk(9), bonding_curve=pk(10), created_ts=1000.0, create_slot=1)
    ts.newpairs_ts = 1001; ts.screen_pass = 1
    v_sol, v_tok = ts.v_sol, ts.v_tok
    def trade(t, sol, buy=True, user=pk(11)):
        nonlocal v_sol, v_tok
        if buy:
            lam = int(sol * 1e9); tok = v_tok - (v_sol * v_tok) // (v_sol + lam); v_sol += lam; v_tok -= tok
        else:
            tok = int(sol); lam = v_sol - (v_sol * v_tok) // (v_tok + tok); v_sol -= lam; v_tok += tok
        ev = TradeEvent("M", lam, tok, buy, user, int(t), v_sol, v_tok, 0, C.INITIAL_REAL_TOKEN_RESERVES - (C.TOTAL_SUPPLY_RAW - v_tok) )
        pre = ts.apply_trade(ev, 5, t); sim.on_trade(ts, ev, pre, t); return ts.last_price
    t = 1010.0
    for i in range(30): trade(t := t + 1, 1.5)               # pump: ATH ver boven 2x launch
    p_ath = ts.ath; assert p_ath / ts.launch_price > 2
    # dump tot -47%
    while ts.last_price > p_ath * 0.53: trade(t := t + 0.2, v_tok * 0.02, buy=False)
    assert all(s.phase == "dipped" for s in ts.sims.values()), {d: s.phase for d, s in ts.sims.items()}
    low = ts.last_price
    while ts.last_price < low * 1.06: trade(t := t + 0.5, 0.5)     # herstel 6% -> signaal
    assert all(s.phase == "pending_entry" for s in ts.sims.values())
    trade(t := t + 3, 0.3)                                        # eerste trade na 2 s -> fill
    assert all(s.phase == "open" and len(s.positions) == 3 for s in ts.sims.values())
    entry = next(iter(ts.sims.values())).positions["V1"].entry_price
    while ts.last_price < entry * 1.5: trade(t := t + 1, 1.0)     # +50%: V1 tp, V2 blijft (trail), V3 blijft
    trade(t := t + 3, 0.1)                                         # fill van V1-exit
    rows = store.query("SELECT variant, exit_reason, gross_ret, pnl_json FROM sim_trades")
    assert len(rows) == 3 and all(r["variant"] == "V1" and r["exit_reason"] == "tp" for r in rows), rows
    pnl = json.loads(rows[0]["pnl_json"]); assert 0.25 < pnl["0.2_pp"] < 0.5, pnl
    # daarna -25% vanaf piek -> V2 trail; V3 stop
    while ts.last_price > entry * 1.5 * 0.7: trade(t := t + 0.5, v_tok * 0.01, buy=False)
    trade(t := t + 3, 0.1)
    rows = store.query("SELECT variant, exit_reason, gross_ret FROM sim_trades ORDER BY id")
    reasons = {(r["variant"], r["exit_reason"]) for r in rows}
    assert ("V2", "trail") in reasons, reasons
    # V3: tijdsexit via tick
    sim.tick(ts, t + 2000); sim.tick(ts, t + 2020)
    rows = store.query("SELECT variant, exit_reason FROM sim_trades ORDER BY id")
    assert any(r["variant"] == "V3" and r["exit_reason"] in ("time", "maxhold") for r in rows), rows
    assert all(s.done for s in ts.sims.values())
    rep = report.build(store); md = report.to_markdown(rep); assert "dip35_V1" in md
    print("simulator ok:", sorted(reasons))
    # rug-detectie
    ts2 = TokenState(mint="R", created_ts=0.0); ts2.price_window.append((100.0, 1e-7))
    ev = TradeEvent("R", 0, 0, False, pk(1), 100, 1_000_000_000, 1_000_000_000_000_000, 0, 0)  # prijs 1e-9? v_sol/v_tok -> 1e-6 SOL / 1e9 tok
    ts2.apply_trade(ev, 1, 100.5); assert ts2.rug_ts == 100.5
    print("rug-detectie ok")

test_decoder(); test_curve(); test_simulator()
