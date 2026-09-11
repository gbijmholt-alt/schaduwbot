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


def test_wallet_analysis():
    """Geplante 'slimme' wallets (kopen vlak voor een koopgolf) moeten bovenaan staan en de geluk-toets halen;
    willekeurige wallets niet."""
    import random, tempfile, json, subprocess, sys as _sys
    from store import Store
    rng = random.Random(3); d = tempfile.mkdtemp(); path = os.path.join(d, "w.sqlite"); st = Store(path)
    T0 = time.time() - 30 * 3600; rows = []
    smart = [f"SMART{i}" + "x" * 38 for i in range(2)]; rand = [f"R{i:03d}" + "y" * 40 for i in range(60)]
    for k in range(80):
        mint = f"M{k:03d}" + "m" * 40; t = T0 + k * 1300; vs, vt = 30_000_000_000, 1_073_000_000_000_000; K = vs * vt
        st.upsert_token(mint=mint, creator="C" + "c" * 43, created_ts=t, filter_newpairs_ts=t + 60); held = {}; ev = []
        burst = t + rng.uniform(600, 1800)
        for u in rng.sample(rand, 30):
            tb = t + rng.uniform(61, 2500); ev += [(tb, u, 1, rng.uniform(0.1, 1)), (tb + rng.uniform(20, 600), u, 0, 0)]
        for u in smart: ev += [(burst - rng.uniform(5, 50), u, 1, 0.5), (burst + 40, u, 0, 0)]
        ev += [(burst + j, f"F{k}_{j}" + "f" * 38, 1, 1.0) for j in range(25)]
        for tt, u, b, sol in sorted(ev):
            if b:
                nvs = vs + int(sol * 1e9); nvt = K // nvs; tok = vt - nvt; held[u] = held.get(u, 0) + tok
            else:
                tok = held.get(u, 0)
                if tok <= 0: continue
                nvt = vt + tok; nvs = K // nvt; sol = (vs - nvs) / 1e9; held[u] = 0
            vs, vt = nvs, nvt; rows.append((mint, tt, 0, "s", u, b, sol, tok, vs, vt, 0, vs / vt))
    st._trade_buf = rows; st.flush()
    out = os.path.join(d, "out")
    r = subprocess.run([_sys.executable, "wallet_analysis.py", "--db", path, "--out", out, "--hours", "0", "--perm", "30"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    rep = json.load(open(os.path.join(out, "wallets.json")))
    top2 = {x["wallet"] for x in rep["top_beste"][:2]}
    assert top2 == set(smart), rep["top_beste"][:3]
    assert rep["geluk_toets"]["wallets_boven_grens"] == 2, rep["geluk_toets"]
    oos = rep["kopieer_simulatie"]["buiten steekproef: top 20 uit A, gekopieerd in B"]
    assert oos["0s"]["n"] > 0
    assert os.path.exists(os.path.join(out, "wallets.md"))
    print("wallet-analyse ok: slimme wallets gevonden, geluk-toets", rep["geluk_toets"]["wallets_boven_grens"], "| kopie 2s EV", oos["2s"]["ev"])
test_wallet_analysis()


def _synth_full_log(path, n_tok=60, seed=4):
    """Kleine dataset met volledige logging: helft bundelgrafiek, helft schoon; dev en sniper verkopen aan de top."""
    import random
    from store import Store
    rng = random.Random(seed); st = Store(path); T0 = time.time() - 30 * 3600
    st.set_meta("full_trade_log_since", T0); st.set_meta("bot_starts", [T0 - 5])
    rows = []; slot = [100]
    for k in range(n_tok):
        mint = f"Q{k:03d}" + "m" * 40; t = T0 + k * 600; creator = f"D{k}" + "d" * 40
        s = {"vs": 30_000_000_000, "vt": 1_073_000_000_000_000}; K = s["vs"] * s["vt"]; held = {}
        def tr(ts, u, buy, sol=0.0, tok=0, sl=None):
            if buy: nvs = s["vs"] + int(sol * 1e9); nvt = K // nvs; tok = s["vt"] - nvt
            else:
                tok = min(tok, held.get(u, 0))
                if tok <= 0: return
                nvt = s["vt"] + tok; nvs = K // nvt
            sol = abs(nvs - s["vs"]) / 1e9; s["vs"], s["vt"] = nvs, nvt; held[u] = held.get(u, 0) + (tok if buy else -tok); slot[0] += 1
            rows.append((mint, ts, sl or slot[0], "s", u, int(buy), sol, tok, s["vs"], s["vt"], 0, s["vs"] / s["vt"]))
        cs = slot[0] + 1; st.upsert_token(mint=mint, creator=creator, created_ts=t, create_slot=cs)
        tr(t, creator, True, 0.5, sl=cs); tr(t + 2, "SNIPER" + "s" * 38, True, 0.5); tt = t + 3
        if k % 2 == 0:
            for j in range(12): tt += 0.5; tr(tt, f"B{k}_{j}" + "b" * 36, True, 3.0)
        else:
            for j in range(24):
                tt += 10; tr(tt, f"O{k}_{j}" + "o" * 36, True, 2.0)
                if j % 3 == 2: tr(tt + 2, f"O{k}_{j-1}" + "o" * 36, False, tok=10**18)
        tt += 5; tr(tt, creator, False, tok=10**18); tr(tt + 1, "SNIPER" + "s" * 38, False, tok=10**18)
        for u, h in sorted(held.items(), key=lambda kv: -kv[1])[:6]: tt += 3; tr(tt, u, False, tok=h)
        st.upsert_token(mint=mint, filter_newpairs_ts=t + 4)
    st._trade_buf = rows; st.flush()


def test_ledger_and_replay():
    import tempfile, subprocess, json as _json, sys as _sys
    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); led = os.path.join(d, "l.sqlite"); out = os.path.join(d, "out")
    _synth_full_log(db)
    for script in ("ledger.py", "video_replay.py"):
        r = subprocess.run([_sys.executable, script, "--db", db, "--ledger", led, "--out", out], capture_output=True, text=True)
        assert r.returncode == 0, script + r.stdout + r.stderr
    L = _json.load(open(os.path.join(out, "ledger.json")))
    per = L["geldstroom"]["per_rol"]
    assert per["dev"]["netto"] > 0 and per["sniper_5s"]["netto"] > 0, per
    assert L["top_netto"][0]["wallet"].startswith("SNIPER"), L["top_netto"][0]
    R = _json.load(open(os.path.join(out, "video_replay.json")))
    assert R["dekking"]["bundelgrafieken"] == 30, R["dekking"]
    # ledger opnieuw draaien mag niets dubbel tellen
    r = subprocess.run([_sys.executable, "ledger.py", "--db", db, "--ledger", led, "--out", out], capture_output=True, text=True)
    L2 = _json.load(open(os.path.join(out, "ledger.json")))
    assert L2["geldstroom"]["per_rol"]["dev"]["netto"] == per["dev"]["netto"]
    print("ledger ok: dev", per["dev"]["netto"], "sniper", per["sniper_5s"]["netto"], "| replay ok: bundelgrafieken", R["dekking"]["bundelgrafieken"])

test_ledger_and_replay()
