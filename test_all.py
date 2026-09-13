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


def _synth_full_log(path, n_tok=60, seed=4, t_start=None, tag="Q", append=False):
    """Kleine dataset met volledige logging: helft bundelgrafiek, helft schoon; dev en sniper verkopen aan de top."""
    import random
    from store import Store
    rng = random.Random(seed); st = Store(path); T0 = t_start if t_start is not None else time.time() - 30 * 3600
    if not append:
        st.set_meta("full_trade_log_since", T0); st.set_meta("bot_starts", [T0 - 5])
    rows = []; slot = [100 + (10000 if append else 0)]
    for k in range(n_tok):
        mint = f"{tag}{k:03d}" + "m" * 40; t = T0 + k * 600; creator = f"D{tag}{k}" + "d" * 39
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


def test_on_curve():
    import ledger
    assert ledger.on_curve("BwWK17cbHxwWBKZkUYvzxLcNQ1YVyaFezduWbtm2de6s") is False     # Solscan: isOnCurve FALSE
    try:
        import base58 as _b58
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives import serialization
        for _ in range(50):
            pub = Ed25519PrivateKey.generate().public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
            assert ledger.on_curve(_b58.b58encode(pub).decode()) is True
    except ImportError:
        pass
    assert ledger.on_curve("geen-adres") is None
    print("on_curve ok")

test_on_curve()


def test_pumpswap_layout():
    """De probe mag niets vaststellen op basis van gokwerk: de offsets moeten uit de
    werkelijke bedragen in de transactie volgen, en onder de drempel schrijft hij niets."""
    import pumpswap, hashlib, tempfile
    MEME = base58.b58encode(bytes([9]) * 32).decode(); USER = base58.b58encode(bytes([8]) * 32).decode()
    POOL = base58.b58encode(bytes([6]) * 32).decode()
    WSOL = pumpswap.WSOL
    TOK, LAM = 4_321_000_000, 777_000_000

    def tx(tok=TOK, lam=LAM, bron="log", off=(16, 0, 24, 56)):
        ot, ol, om, ou = off
        body = bytearray(88)
        struct.pack_into("<Q", body, ot, tok); struct.pack_into("<Q", body, ol, lam)
        body[om:om + 32] = base58.b58decode(MEME); body[ou:ou + 32] = base58.b58decode(USER)
        blob = hashlib.sha256(b"event:BuyEvent").digest()[:8] + bytes(body)
        meta = {"preTokenBalances": [{"accountIndex": 1, "mint": MEME, "owner": USER, "uiTokenAmount": {"amount": "0"}},
                                     {"accountIndex": 3, "mint": MEME, "owner": POOL, "uiTokenAmount": {"amount": str(tok)}},
                                     {"accountIndex": 2, "mint": WSOL, "owner": POOL, "uiTokenAmount": {"amount": "0"}}],
                "postTokenBalances": [{"accountIndex": 1, "mint": MEME, "owner": USER, "uiTokenAmount": {"amount": str(tok)}},
                                      {"accountIndex": 3, "mint": MEME, "owner": POOL, "uiTokenAmount": {"amount": "0"}},
                                      {"accountIndex": 2, "mint": WSOL, "owner": POOL, "uiTokenAmount": {"amount": str(lam)}}],
                "logMessages": [], "innerInstructions": []}
        if bron in ("log", "beide"): meta["logMessages"] = ["Program data: " + base64.b64encode(blob).decode()]
        if bron in ("cpi", "beide"): meta["innerInstructions"] = [{"instructions": [{"programId": pumpswap.PUMPSWAP_PROGRAM,
                                                             "data": base58.b58encode(pumpswap.ANCHOR_CPI_EVENT + blob).decode()}]}]
        return {"meta": meta, "transaction": {"message": {"accountKeys": [USER, POOL, MEME]}}}

    w = pumpswap.waarheid_uit_tx(tx())
    assert w and w["mint"] == MEME and w["tok"] == TOK and LAM in w["lamports"] and w["eigenaar"] == USER, w
    # een derde partij op dezelfde mint (router die de order splitst) mag niet als bewijs gelden
    t3 = tx(); t3["meta"]["postTokenBalances"].append({"accountIndex": 4, "mint": MEME, "owner": "DERDE",
                                                      "uiTokenAmount": {"amount": "7"}})
    assert pumpswap.waarheid_uit_tx(t3) is None, "router-transactie moet worden uitgesloten"
    assert pumpswap.waarheid_uit_tx(t3, streng=False) is not None, "zonder streng filter wel bruikbaar"
    blobs = pumpswap.blobs_uit_tx(tx()); assert len(blobs) == 1 and blobs[0][0] == "log"
    blobs = pumpswap.blobs_uit_tx(tx(bron="cpi")); assert blobs[0][0] == "inner_cpi", blobs[0][0]
    # In de praktijk staat hetzélfde event in beide bronnen. Zonder ontdubbelen lijkt elke
    # transactie 'meerdere events van hetzelfde type' te hebben en valt alles af (fout van 12 sept 09:59).
    beide = pumpswap.blobs_uit_tx(tx(bron="beide"))
    assert len(beide) == 2 and {b for b, _ in beide} == {"log", "inner_cpi"}, beide
    assert len({bl for _, bl in beide}) == 1, "zelfde event, zelfde bytes"
    ev, tel = pumpswap.events_van_tx(tx(bron="beide"))
    assert len(ev) == 1 and list(tel.values()) == [1], (ev, tel)      # één event, niet twee
    assert ev[0][0] == ["inner_cpi", "log"], ev[0][0]
    # ook als de bytes per bron nét niet gelijk zijn, mag het geen twee events worden
    scheef = tx(bron="beide")
    scheef["meta"]["innerInstructions"] = [{"instructions": [{"programId": pumpswap.PUMPSWAP_PROGRAM,
        "data": base58.b58encode(pumpswap.ANCHOR_CPI_EVENT + base64.b64decode(
            scheef["meta"]["logMessages"][0][14:]) + b"\x00").decode()}]}]
    ev3, tel3 = pumpswap.events_van_tx(scheef)
    assert list(tel3.values()) == [1], (ev3, tel3)
    assert len(ev3) == 1 and ev3[0][0] == ["log"], ev3      # logregel is de eerste keuze
    # twee verschillende events van hetzelfde type in één transactie -> wel als 'meerdere' tellen,
    # ook als één bron er maar één van laat zien (afgekapte logs): dan kiezen we de veilige kant
    t2 = tx(bron="beide"); t2["meta"]["logMessages"].append(tx(tok=TOK + 1)["meta"]["logMessages"][0])
    ev2, tel2 = pumpswap.events_van_tx(t2)
    assert max(tel2.values()) == 2, tel2
    # afgekapte logs: dan is de binnenste instructie de bron voor het bewijs
    t4 = tx(bron="beide"); t4["meta"]["logMessages"].append("Log truncated")
    ev4, tel4 = pumpswap.events_van_tx(t4)
    assert list(tel4.values()) == [1] and ev4[0][0] == ["inner_cpi", "log"], (ev4, tel4)
    body = blobs[0][1][8:]
    assert 16 in pumpswap.zoek_offsets(body, TOK) and 0 in pumpswap.zoek_offsets(body, LAM)
    assert pumpswap.zoek_pubkey(body, MEME) == [24] and pumpswap.zoek_pubkey(body, USER) == [56]
    # twee mints zonder memecoin-onderscheid -> geen waarheid, dus geen valse offsets
    t2 = tx(); t2["meta"]["postTokenBalances"].append({"accountIndex": 3, "mint": base58.b58encode(bytes([7]) * 32).decode(),
                                                      "owner": USER, "uiTokenAmount": {"amount": "5"}})
    assert pumpswap.waarheid_uit_tx(t2) is None
    # onder de drempel: niets vastleggen
    d = hashlib.sha256(b"event:BuyEvent").digest()[:8].hex()
    laag = {"events": {d: {"naam": "BuyEvent", "bron": ["log"], "n": 10, "offset_tokens": 16, "match_tokens": 1.0,
                           "offset_lamports": 0, "match_lamports": 1.0, "offset_mint": 24, "match_mint": 1.0,
                           "offset_pool": 56, "match_pool": 1.0, "identificatie": "mint",
                           "offset_user": 56, "match_user": 1.0, "vastgesteld": False}}}
    tmp = tempfile.mkdtemp(); pumpswap.LAYOUT_PATH = os.path.join(tmp, "layout.json")
    assert pumpswap.schrijf_layout(laag) is None and not os.path.exists(pumpswap.LAYOUT_PATH)
    hoog = json.loads(json.dumps(laag)); hoog["events"][d]["vastgesteld"] = True; hoog["events"][d]["n"] = 80
    lay = pumpswap.schrijf_layout(hoog)
    assert lay and os.path.exists(pumpswap.LAYOUT_PATH) and pumpswap.layout_via_logs(lay)
    # rondrit: met de vastgestelde layout moet de decoder de bedragen terugvinden
    line = tx()["meta"]["logMessages"][0]
    got = pumpswap.decode_amm_log(line, lay)
    assert got == (MEME, USER, True, LAM / 1e9, TOK), got
    # alleen emit_cpi -> de logstream kan het niet zien
    cpi = json.loads(json.dumps(hoog)); cpi["events"][d]["bron"] = ["inner_cpi"]
    assert pumpswap.layout_via_logs(pumpswap.schrijf_layout(cpi)) is False
    # layout die de pool noemt in plaats van de mint: vastgesteld, maar de bot mag er niets mee
    pool = json.loads(json.dumps(hoog)); pool["events"][d]["identificatie"] = "pool"
    lp = pumpswap.schrijf_layout(pool)
    assert lp and lp["events"][d]["offset_mint"] is None and lp["events"][d]["offset_pool"] == 56, lp
    assert pumpswap.load_layout(pumpswap.LAYOUT_PATH) is None, "pool-layout mag de bot niet aanzetten"
    print("pumpswap layout ok")

test_pumpswap_layout()


def test_uitstapregels_en_vroeg():
    """Uitstapregels op één koerspad, en de vooruit-werking van het register van vroege kopers."""
    import tempfile, subprocess, json as _json, sys as _sys, sqlite3, importlib
    import ledger
    importlib.reload(ledger)
    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); led = os.path.join(d, "l.sqlite"); out = os.path.join(d, "out")

    # --- 1. uitstapregels op een gemaakt koerspad: eerst +40%, dan instorten ---
    from store import Store
    st = Store(db); T = time.time() - 7200
    st.set_meta("full_trade_log_since", T - 10); st.set_meta("bot_starts", [T - 20])
    mint = "P" + "p" * 43; vs, vt = 30_000_000_000, 1_073_000_000_000_000; K = vs * vt
    rows = []
    for i, factor in enumerate([1.0, 1.15, 1.40, 1.45, 1.10, 0.55, 0.40]):
        vs2 = int((K * factor) ** 0.5); vt2 = K // vs2
        rows.append((mint, T + i * 20, 100 + i, "s", "W" + "w" * 43, 1, 0.1, 1000, vs2, vt2, 0, vs2 / vt2))
    st._trade_buf = rows; st.flush()
    main_db = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    r = ledger.eval_entry(main_db, mint, T)
    assert r is not None
    assert r["ret_tp20"] > 0 and r["ret_video"] > 0, (r["ret_tp20"], r["ret_video"])   # de stijging wordt gepakt
    assert r["ret_tp50"] < -0.1, r["ret_tp50"]          # +50% komt nooit, dus uit op de stop
    assert r["ret_t180"] < -0.4, r["ret_t180"]          # na 3 min is de koers weg
    assert r["ret_trail"] > r["ret_t180"], (r["ret_trail"], r["ret_t180"])      # trailing pakt de top mee
    assert r["ret_t15"] < r["ret_t30"], (r["ret_t15"], r["ret_t30"])            # koers stijgt in de eerste 30 s
    assert -1.0 <= min(r[k] for k in r if k.startswith("ret_")) , r
    main_db.close()

    # --- 2. register van vroege kopers werkt alleen vooruit ---
    db2 = os.path.join(d, "m2.sqlite")
    T0 = time.time() - 30 * 3600
    _synth_full_log(db2, n_tok=60, t_start=T0)
    def draai(nu=None):
        cmd = [_sys.executable, "ledger.py", "--db", db2, "--ledger", led, "--out", out] + (["--now", str(nu)] if nu else [])
        rr = subprocess.run(cmd, capture_output=True, text=True)
        assert rr.returncode == 0, rr.stdout + rr.stderr
        return _json.load(open(os.path.join(out, "ledger.json")))

    peil = T0 + 11 * 3600
    L1 = draai(peil)
    reg1 = L1["vroege_kopers"]["register_grootte"]
    assert reg1 >= 1, L1["vroege_kopers"]
    assert not L1["vroege_kopers"]["per_bucket"], "tokens van vóór het register mogen niet meetellen"
    # nieuwe tokens ná het peilmoment: nu mag de tokentoets wel iets zeggen
    _synth_full_log(db2, n_tok=20, t_start=peil + 3600, tag="Z", append=True)
    L15 = draai(T0 + 16 * 3600)
    assert L15["groeiers"], "sniper had inmiddels groeier moeten zijn"
    # en pas tokens ná opname op de groeierslijst geven een vooruit-toets met uitstapregels
    _synth_full_log(db2, n_tok=20, t_start=T0 + 17 * 3600, tag="Y", append=True)
    L2 = draai()
    bk = L2["vroege_kopers"]["per_bucket"]
    assert bk, L2["vroege_kopers"]
    # elke bucket moet een marge hebben, anders is niet te zien of een verschil ruis is
    for label, v in bk.items():
        assert "tp30_ci95" in v, (label, v)
        if v["tokens"] > 1:
            assert v["tp30_ci95"] and v["tp30_ci95"][0] <= v["tp30"] <= v["tp30_ci95"][1], (label, v)
    md2 = open(os.path.join(out, "ledger.md")).read()
    assert "95%-marge daarop" in md2, "marge ontbreekt in het rapport"
    assert sum(v["tokens"] for v in bk.values()) <= 20 + 60, bk
    u = L2["uitstapregels"]
    assert u, "uitstapregels ontbreken"
    for k in ("ret_video", "ret_tp30", "ret_t15", "ret_trail"):
        assert k in u and u[k]["n"] > 0, (k, u.get(k))
        assert u[k]["ci95"] is None or u[k]["ci95"][0] <= u[k]["ev"] <= u[k]["ci95"][1], u[k]
    assert os.path.exists(os.path.join(out, "ledger.md"))
    md = open(os.path.join(out, "ledger.md")).read()
    assert "Uitstapregels op dezelfde aankopen" in md and "Register van vroege kopers" in md
    print("uitstapregels ok:", {k: u[k]["ev"] for k in ("ret_video", "ret_tp30", "ret_t15", "ret_trail")},
          "| register:", reg1, "buckets:", {k: v["tokens"] for k, v in bk.items()})

test_uitstapregels_en_vroeg()


def test_community_proxy():
    """Poolen over varianten telt hetzelfde token meerdere keren. De per-token-variant moet
    dat wegnemen, en een EV die op één uitschieter drijft moet als zodanig zichtbaar zijn."""
    import report as R
    rows = []
    for mint, rets in (("A" * 44, [5.0, 5.0, 5.0, 5.0]), ("B" * 44, [-0.3, -0.3]), ("C" * 44, [-0.2, -0.2]),
                       ("D" * 44, [-0.25, -0.25]), ("E" * 44, [-0.1, -0.1])):
        for v in rets: rows.append({"mint": mint, "is_rug": 0, "pnl_json": json.dumps({"0.2_pp": v})})
    gep = R._stats(rows, "0.2_pp"); pt = R._per_token_stats(rows, "0.2_pp")
    assert gep["n"] == 12 and pt["n"] == 5, (gep["n"], pt["n"])          # 12 waarnemingen, 5 tokens
    assert gep["ev"] > pt["ev"], (gep["ev"], pt["ev"])                    # poolen overweegt de uitschieter
    assert pt["aandeel_van_ev_uit_top3"] >= 1.0, pt["aandeel_van_ev_uit_top3"]   # alle winst uit de top (>100% = de rest verliest)
    assert pt["ci95"][0] < 0 < pt["ci95"][1], pt["ci95"]                 # marge loopt door nul: geen bewijs
    assert R._ci95([0.1]) is None and R._top_share([-0.1, -0.2]) is None
    md = R.to_markdown({"generated": "x", "sim_trades": 0, "funnel": {}, "varianten": {}, "beste_variant": None,
                        "drempels": None, "community_proxy": {"_uitleg": "u", "per_token_zonder_xlink": pt, "gepoold_zonder_xlink": gep}})
    assert "95%-marge" in md and "per_token_zonder_xlink" in md
    print("community-proxy ok: gepoold EV", gep["ev"], "per token EV", pt["ev"], "marge", pt["ci95"])

test_community_proxy()


def test_pumpswap_optellen():
    """Met het strenge filter blijven er per run weinig voorbeelden over; de tellers moeten
    dus over runs optellen, anders halen we de eis van 50 voorbeelden nooit."""
    import pumpswap, sqlite3, tempfile
    d = tempfile.mkdtemp(); path = os.path.join(d, "l.sqlite")
    led = sqlite3.connect(path); led.executescript(pumpswap.SCHEMA)
    disc = "ab" * 8
    ruw = {disc: {"bron": ["log"], "n": 30, "lengtes": {"88": 30}, "afw": [0.0125],
                  "tok": {"8": 29}, "sol": {"96": 30}, "mint": {}, "user": {"144": 20}, "acct": {"40": 30, "144": 20}}}
    tel = {"transacties_opgehaald": 400, "transacties_met_waarheid": 30, "transacties_meerdere_events": 5,
           "transacties_router_of_meerdere_partijen": 120}
    alles, tot = pumpswap.tel_op(led, ruw, tel)
    r1 = pumpswap.beoordeel(alles, tot)[ "events"][disc]
    assert r1["n"] == 30 and r1["vastgesteld"] is False, r1          # nog te weinig voorbeelden
    alles, tot = pumpswap.tel_op(led, ruw, tel)                       # tweede run
    r2 = pumpswap.beoordeel(alles, tot)["events"][disc]
    assert r2["n"] == 60, r2["n"]
    assert tot["transacties_opgehaald"] == 800, tot
    assert r2["offset_tokens"] == 8 and r2["offset_lamports"] == 96, r2
    assert r2["offset_pool"] == 40 and r2["pool_kandidaten"], r2
    # beoordeel() mag de pool niet zelf goedkeuren: dat moet de keten uitwijzen
    assert r2["identificatie"] is None and r2["vastgesteld"] is False, r2
    assert r2["mediane_afwijking_tokens"] == 0.0125, r2
    print("pumpswap optellen ok: n", r1["n"], "->", r2["n"], "herkenning", r2["identificatie"])

test_pumpswap_optellen()


def test_pumpswap_prijs():
    """De grootste tokenhouder hoeft niet de pool te zijn. Een gewone wallet met veel WSOL gaf
    op 12 sept 09:59 een restwaarde van 26.647 SOL tegen 605 SOL kostprijs; die controle hoort
    hier te zitten."""
    import pumpswap
    POOL_PDA = "BwWK17cbHxwWBKZkUYvzxLcNQ1YVyaFezduWbtm2de6s"      # niet op de curve
    MINT = base58.b58encode(bytes([9]) * 32).decode()

    class FakeRpc:
        def __init__(self, owner, wsol, tok): self.owner, self.wsol, self.tok = owner, wsol, tok
        def call(self, method, params):
            if method == "getTokenLargestAccounts": return {"value": [{"address": "TA", "amount": str(self.tok)}]}
            if method == "getAccountInfo": return {"value": {"data": {"parsed": {"info": {"owner": self.owner}}}}}
            if method == "getTokenAccountsByOwner":
                return {"value": [{"account": {"data": {"parsed": {"info": {"tokenAmount": {"amount": str(self.wsol)}}}}}}]}
            return None

    # 1e-7 SOL per token op de curve; pool met plausibele prijs
    curve = 1e-7
    tok = 200_000_000 * 10**6; wsol = int(tok / 10**6 * curve * 1.5 * 1e9)
    r = pumpswap.pool_prijs(FakeRpc(POOL_PDA, wsol, tok), MINT, curve)
    assert r["afgekeurd"] is None and abs(r["factor"] - 1.5) < 0.01, r
    # gewone wallet als 'pool' -> afkeuren
    import base58 as _b58
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives import serialization
        pub = Ed25519PrivateKey.generate().public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        r = pumpswap.pool_prijs(FakeRpc(_b58.b58encode(pub).decode(), wsol, tok), MINT, curve)
        assert r["afgekeurd"] == "eigenaar_is_gewone_wallet", r
    except ImportError:
        pass
    # absurde prijs (veel WSOL, weinig tokens) -> afkeuren, ook bij een PDA
    r = pumpswap.pool_prijs(FakeRpc(POOL_PDA, wsol * 100, tok), MINT, curve)
    assert r["afgekeurd"] == "prijs_onwaarschijnlijk" and r["prijs_sol"] is None, r
    # geen WSOL -> geen prijs
    r = pumpswap.pool_prijs(FakeRpc(POOL_PDA, 0, tok), MINT, curve)
    assert r["afgekeurd"] == "geen_wsol_of_tokens", r
    print("pumpswap prijs ok: factor", 1.5, "afkeuringen werken")

test_pumpswap_prijs()


def test_pumpswap_telfout():
    """Een match boven 100% is onmogelijk en betekende op 12 sept 13:05 dat een offset dubbel
    werd geteld (bruto én netto WSOL op dezelfde plek). Zo'n event mag niet 'vastgesteld' heten."""
    import pumpswap, sqlite3, tempfile
    d = tempfile.mkdtemp(); pumpswap.LEDGER_DB = os.path.join(d, "l.sqlite")
    led = sqlite3.connect(pumpswap.LEDGER_DB); led.executescript(pumpswap.SCHEMA)
    disc = "cd" * 8
    # tellers die hoger zijn dan het aantal voorbeelden: kan alleen door dubbel tellen
    ruw = {disc: {"bron": ["log"], "n": 60, "lengtes": {"400": 60}, "afw": [],
                  "tok": {"8": 59}, "sol": {"376": 85}, "mint": {}, "user": {"144": 59},
                  "acct": {"208": 60}}}
    alles, tot = pumpswap.tel_op(led, ruw, {"transacties_opgehaald": 400, "transacties_met_waarheid": 60,
                                            "transacties_meerdere_events": 0, "transacties_router_of_meerdere_partijen": 0})
    r = pumpswap.beoordeel(alles, tot)["events"][disc]
    assert r["telfout"] == ["lamports"], r["telfout"]
    assert r["vastgesteld"] is False, "een telfout mag nooit 'vastgesteld' opleveren"
    assert pumpswap.schrijf_layout({"events": {disc: r}}) is None
    # en met eerlijke tellers wel
    led.execute("DELETE FROM amm_probe"); led.execute("DELETE FROM amm_probe_meta"); led.commit()
    ruw[disc]["sol"] = {"96": 59}
    alles, tot = pumpswap.tel_op(led, ruw, {"transacties_opgehaald": 400, "transacties_met_waarheid": 60,
                                            "transacties_meerdere_events": 0, "transacties_router_of_meerdere_partijen": 0})
    r2 = pumpswap.beoordeel(alles, tot)["events"][disc]
    assert r2["telfout"] is None, r2
    # met eerlijke tellers én een pool die de keten bevestigt, wordt het wel vastgesteld
    r2["pool_kandidaten"] = [{"offset": 208, "match": 1.0, "voorbeelden": ["POOLX"]}]

    class Rpc:
        def call(self, m, p): return {"value": {"owner": pumpswap.PUMPSWAP_PROGRAM}}

    na = pumpswap.verifieer_pool(Rpc(), {"events": {disc: r2}})["events"][disc]
    assert na["vastgesteld"] is True and na["identificatie"] == "pool", na
    print("pumpswap telfout ok: >100% wordt afgekeurd, eerlijke tellers plus bevestigde pool wel vastgesteld")

test_pumpswap_telfout()


def test_pumpswap_pool_navragen():
    """Meerdere offsets halen 100% omdat in één event meerdere accounts staan. 'De hoogste' is
    dan willekeurig — dat zag je aan de pool-offset die per run verschoof (@112 -> @353). De keten
    moet het uitwijzen: een pool is eigendom van het AMM-programma, een wallet niet."""
    import pumpswap
    SYS = "11111111111111111111111111111111"
    res = {"events": {"aa" * 8: {
        "naam": "BuyEvent", "n": 300, "match_tokens": 0.97, "match_lamports": 0.97, "match_mint": 0.0,
        "offset_pool": 112, "match_pool": 1.0, "identificatie": None, "vastgesteld": False, "telfout": None,
        "pool_kandidaten": [{"offset": 112, "match": 1.0, "voorbeelden": ["WALLET1", "WALLET2"]},
                            {"offset": 353, "match": 1.0, "voorbeelden": ["POOL1", "POOL2"]}]}}}

    class FakeRpc:
        calls = 0
        def call(self, method, params):
            FakeRpc.calls += 1
            pk = params[0]
            owner = pumpswap.PUMPSWAP_PROGRAM if pk.startswith("POOL") else SYS
            return {"value": {"owner": owner}}

    out = pumpswap.verifieer_pool(FakeRpc(), res)
    ev = out["events"]["aa" * 8]
    assert ev["offset_pool"] == 353, ev["offset_pool"]          # niet de eerste/hoogste, maar de echte
    assert ev["identificatie"] == "pool" and ev["vastgesteld"] is True, ev
    assert ev["pool_kandidaten"][0]["is_pool"] is False and ev["pool_kandidaten"][1]["is_pool"] is True
    # geen enkele kandidaat is een pool -> niets vaststellen
    res2 = {"events": {"bb" * 8: {
        "naam": "SellEvent", "n": 300, "match_tokens": 0.97, "match_lamports": 0.97, "match_mint": 0.0,
        "offset_pool": 240, "match_pool": 1.0, "identificatie": None, "vastgesteld": False, "telfout": None,
        "pool_kandidaten": [{"offset": 240, "match": 1.0, "voorbeelden": ["WALLET3"]}]}}}
    ev2 = pumpswap.verifieer_pool(FakeRpc(), res2)["events"]["bb" * 8]
    assert ev2["vastgesteld"] is False and ev2.get("pool_onbevestigd") is True, ev2
    # RPC dood (alle opzoekingen None): dan mag NIETS pool heten — op 12 sept 19:24 werden alle zes
    # kandidaten 'pool' omdat all() over een lege reeks True is
    class DodeRpc:
        calls = errors = 0
        def call(self, m, p): self.calls += 1; self.errors += 1; return None
    res3 = json.loads(json.dumps(res)); res3["events"]["aa" * 8]["vastgesteld"] = False
    ev3 = pumpswap.verifieer_pool(DodeRpc(), res3)["events"]["aa" * 8]
    assert all(k["is_pool"] is False for k in ev3["pool_kandidaten"]), ev3["pool_kandidaten"]
    assert ev3["vastgesteld"] is False and ev3.get("pool_onbevestigd") is True, ev3
    # stroomonderbreker: na 8 mislukte calls stopt de probe
    d8 = DodeRpc()
    for _ in range(8): d8.call("x", [])
    assert pumpswap.rpc_dood(d8) is True and pumpswap.rpc_dood(DodeRpc()) is False
    print("pumpswap pool navragen ok: offset", ev["offset_pool"], "bevestigd via de eigenaar")

test_pumpswap_pool_navragen()


def test_hypotheses_register():
    """Het register mag alleen tokens ná de registratietijd als toets tellen, moet de primaire cel
    vastpinnen, en moet een oordeel pas geven bij voldoende n — en dat oordeel daarna laten staan."""
    import tempfile, subprocess, json as _json, sys as _sys
    import hypotheses as H
    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); out = os.path.join(d, "out"); st = os.path.join(d, "state.json")
    vast = H.HYPOTHESEN[0]["vastgelegd_ts"]
    # 1. alleen tokens van vóór de registratie -> alles verkennend, oordeel 'te vroeg'
    _synth_full_log(db, n_tok=40, t_start=vast - 40 * 600 - 3600)
    r = subprocess.run([_sys.executable, "hypotheses.py", "--db", db, "--out", out, "--state", st, "--now", str(vast + 7200)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    J = _json.load(open(os.path.join(out, "hypotheses.json")))
    h = J["hypothesen"][0]
    assert h["id"] == "S1" and h["oordeel"]["status"] == "te vroeg", h["oordeel"]
    assert h["resultaat"]["tokens"]["toets"] == 0 and h["resultaat"]["tokens"]["verkennend"] == 40, h["resultaat"]["tokens"]
    # in de gemaakte data koopt SNIPER als eerste na de dev en verkoopt aan de top: rang 1 moet beter zijn dan rang 20
    v = h["resultaat"]["verkennend"]["ongefilterd"]
    assert v["1"]["na_10_kopers"]["ev"] > v["20"]["na_10_kopers"]["ev"], (v["1"]["na_10_kopers"], v["20"]["na_10_kopers"])
    assert v["1"]["na_10_kopers"]["latentie_mediaan_s"] < v["5"]["na_10_kopers"]["latentie_mediaan_s"]
    # 2. tokens ná de registratie -> toets vult zich; drempel min_n verlagen voor de test via een kopie van de hypothese
    _synth_full_log(db, n_tok=30, t_start=vast + 60, tag="N", append=True)
    r = subprocess.run([_sys.executable, "hypotheses.py", "--db", db, "--out", out, "--state", st, "--now", str(vast + 30 * 600 + 7200)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    J2 = _json.load(open(os.path.join(out, "hypotheses.json")))
    h2 = J2["hypothesen"][0]
    assert h2["resultaat"]["tokens"]["toets"] == 30, h2["resultaat"]["tokens"]
    assert h2["oordeel"]["status"] == "te vroeg" and h2["oordeel"]["n"] == 30, h2["oordeel"]     # 30 < 500
    md = open(os.path.join(out, "hypotheses.md")).read()
    assert "Toets (ná registratie)" in md and "niet gebruiken als bewijs" in md and "Primaire cel" in md
    # 3. oordeel-logica los: gezakt + herkansing, daarna definitief
    hyp = {**H.HYPOTHESEN[0], "drempel": {**H.HYPOTHESEN[0]["drempel"], "min_n": 10}}
    state = {}
    slecht = {"n": 50, "ev": -0.2, "ci95": [-0.3, -0.1], "winkans": 0.2, "rug_pct": 0.1, "maxdd_20": 0.9}
    o1 = H.oordeel(hyp, slecht, state, 1.0)
    assert o1["status"] == "gezakt" and not o1.get("definitief") and o1["herkansing_over"] == 1, o1
    o2 = H.oordeel(hyp, slecht, state, 2.0)
    assert o2["status"] == "gezakt" and o2.get("definitief"), o2
    goed = {"n": 50, "ev": 0.2, "ci95": [0.1, 0.3], "winkans": 0.7, "rug_pct": 0.0, "maxdd_20": 0.1}
    o3 = H.oordeel(hyp, goed, state, 3.0)
    assert o3["status"] == "gezakt", "een definitief oordeel mag niet meer veranderen, ook niet bij mooie cijfers"
    print("hypotheses ok: verkennend", h["resultaat"]["tokens"]["verkennend"], "toets", h2["resultaat"]["tokens"]["toets"],
          "| rang1", v["1"]["na_10_kopers"]["ev"], "rang20", v["20"]["na_10_kopers"]["ev"])

test_hypotheses_register()


def test_rpc_endpoint_bestand():
    """Van aanbieder wisselen moet via de repo kunnen (geen serverconsole nodig), maar een sleutel
    in .env op de server moet altijd winnen — die repo is openbaar."""
    import tempfile
    import config as C
    d = tempfile.mkdtemp(); pad = os.path.join(d, "rpc_endpoint.txt")
    with open(pad, "w") as f:
        f.write("# commentaar\nhttp=https://voorbeeld/rpc   # achteraan commentaar\n\nws=wss://voorbeeld/ws\nrps=3\nleeg=\n")
    ep = C.lees_endpoint(pad)
    assert ep == {"http": "https://voorbeeld/rpc", "ws": "wss://voorbeeld/ws", "rps": "3"}, ep
    assert C.lees_endpoint(os.path.join(d, "bestaat-niet.txt")) == {}          # ontbreken mag nooit crashen
    k = C.kies_endpoint
    assert k("env", "bestand", "helius", "publiek") == "env"                   # .env wint (geheimen)
    assert k(None, "bestand", "helius", "publiek") == "bestand"                # dan de repo
    assert k(None, None, "helius", "publiek") == "helius"
    assert k(None, None, None, "publiek") == "publiek"
    # het meegeleverde bestand moet geen sleutel bevatten: de repo is openbaar
    echt = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rpc_endpoint.txt")
    if os.path.exists(echt):
        waarden = " ".join(C.lees_endpoint(echt).values()).lower()      # alleen de waarden, niet het commentaar
        for verdacht in ("api-key", "api_key", "dkey", "apikey", "token="):
            assert verdacht not in waarden, f"sleutel in een openbaar bestand: {verdacht}"
    print("rpc-endpoint ok:", C.RPC_HTTP, "| rps", C.RPC_RPS)

test_rpc_endpoint_bestand()


def test_beste_variant_over_alle_cellen():
    """Het bouwplan schrijft drie inzetgroottes en twee terminals voor. De drempeltoets keek tot
    13 sept alleen naar 0,2 SOL / PumpPortal — dus naar één van de zes cellen."""
    import report as R
    def cel(n, ev, win, rug, dd):
        return {"n": n, "ev": ev, "winkans": win, "rug_pct": rug, "maxdd_20": dd}
    rep = {"varianten": {
        "dipA": {"0.2_pp": cel(600, -0.05, 0.2, 0.02, 1.0), "0.05_pp": cel(600, 0.09, 0.55, 0.02, 0.3)},
        "dipB": {"0.2_pp": cel(600, 0.01, 0.3, 0.02, 0.9)}}}
    keys = ["0.05_axiom", "0.05_pp", "0.2_axiom", "0.2_pp", "1.0_axiom", "1.0_pp"]
    best = None
    for name, d in rep["varianten"].items():
        for k in keys:
            s = d.get(k, {})
            if s.get("n", 0) >= 30 and (best is None or s["ev"] > best[2]["ev"]): best = (name, k, s)
    assert best[0] == "dipA" and best[1] == "0.05_pp", best   # niet 0.2_pp, en niet dipB
    haalt = [(n, k) for n, d in rep["varianten"].items() for k in keys
             if (s := d.get(k, {})).get("n") and s["n"] >= 500 and s["winkans"] >= 0.5
             and s["rug_pct"] <= 0.05 and s["ev"] >= 0.03 and s["maxdd_20"] <= 0.40]
    assert haalt == [("dipA", "0.05_pp")], haalt
    # en de echte code moet hetzelfde doen
    import inspect
    bron = inspect.getsource(R.build)
    assert "for k in keys" in bron, "beste_variant kijkt nog steeds naar één cel"
    assert "haalt_alle_drempels" in bron
    print("beste-variant ok: beste cel", best[1], "i.p.v. vast 0.2_pp")

test_beste_variant_over_alle_cellen()


def test_replay_dieptes():
    """De dipreeks moet 50% en 55% bevatten: dat was de vraag van Gerben, en 55% was nooit getoetst."""
    import video_replay as V
    for d in (0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80):
        assert d in V.DIPS, (d, V.DIPS)
    assert max(V.DIPS) <= 0.80, "dieper dan 80% is rug-gebied, geen instapmoment"
    assert V.VERSIE.startswith("replay-v5"), V.VERSIE   # versie moet bumpen, anders blijven oude rijen staan
    assert len(V.SIZES) == 3 and 0.05 in V.SIZES and 1.0 in V.SIZES, V.SIZES
    print("replay-dieptes ok:", V.DIPS, "| inzet", V.SIZES, "| versie", V.VERSIE)

test_replay_dieptes()


def test_winstgrenzen():
    """De kernvraag van Gerben: haalt de koers na de dip de +45%, en helpt een lagere grens?
    Een grens die pas ná de stop geraakt wordt is niet te pakken; dat onderscheid moet erin zitten."""
    import video_replay as V
    for tp in (0.10, 0.20, 0.30, 0.35, 0.45):
        assert tp in V.TP_LADDER, (tp, V.TP_LADDER)
    assert V.C.V1_TP in V.TP_LADDER, "de videogrens zelf moet in de ladder zitten"
    assert V.VERSIE.startswith("replay-v"), V.VERSIE
    import inspect
    bron = inspect.getsource(V.analyse_token)
    assert "voor_stop" in bron and "max_stijging" in bron
    assert "t_stop is None or t_tp[tp] <= t_stop" in bron, "voor_stop moet echt met de stop vergelijken"
    rap = inspect.getsource(V.to_md)
    assert "haalt vóór stop" in rap and "Wordt die +45% na de dip wel gehaald?" in rap
    print("winstgrenzen ok:", [f"+{int(t*100)}%" for t in V.TP_LADDER])

test_winstgrenzen()


def test_regel_gerben():
    """De regel exact zoals gesteld: instap na 55%-dip, stop als de koers 65% onder de TOP staat
    (dus ~22% onder de instap, niet 65% onder de instap), winst op +30%, en bij +20% stop naar
    instapprijs. Op een gemaakt koerspad moet elk van de drie uitgangen precies één keer kloppen."""
    import video_replay as V
    assert V.G_STOP_VANAF_TOP == 0.65 and V.G_TP == 0.30 and V.G_BREAKEVEN == 0.20
    h3 = [h for h in V.HYPOTHESEN if h["id"] == "H3"]
    assert h3 and h3[0]["variant"] == "d55" and h3[0]["sleutel"] == "direct|gerben", h3
    assert h3[0]["vastgelegd_ts"] > 1789279199, "H3 moet vooruit gelden, niet met terugwerkende kracht"
    assert 0.55 in V.DIPS

    # rekenvoorbeeld: top = 100, instap op 45 (dip 55%), stop op 35 (65% onder de top)
    ath, pe = 100.0, 45.0
    assert abs(V.g_stop_niveau_van(ath, 0.55) - 35.0) < 1e-9, "bij 55% moet het exact Gerbens 65% zijn"
    # bij diepere instappen moet de stop meebewegen, anders ligt hij bóven de instapprijs
    for d in V.DIPS:
        instap = ath * (1 - d); stop = V.g_stop_niveau_van(ath, d)
        assert stop < instap, (d, stop, instap)
    assert abs(V.g_stop_niveau_van(ath, 0.70) - 20.0) < 1e-9, V.g_stop_niveau_van(ath, 0.70)
    assert abs(ath * (1 - V.G_STOP_VANAF_TOP) - 35.0) < 1e-9
    assert abs((35.0 / pe - 1) + 0.2222) < 0.001, "stop hoort ~22% onder de instap te liggen"
    # winst nemen op 45 * 1,30 = 58,5 ; breakeven wordt gewapend op 45 * 1,20 = 54
    assert abs(pe * (1 + V.G_TP) - 58.5) < 1e-9 and abs(pe * (1 + V.G_BREAKEVEN) - 54.0) < 1e-9

    def loop(pad):
        """Bootst de lus uit analyse_token na en geeft (reden, koers bij uitstap)."""
        t_g = None; reden = "tijd"; be = False; uit = None
        for p in pad:
            if t_g is not None: break
            if not be and p >= pe * (1 + V.G_BREAKEVEN): be = True
            niveau = pe if be else ath * (1 - V.G_STOP_VANAF_TOP)
            if p >= pe * (1 + V.G_TP): t_g, reden, uit = 1, "winst", p
            elif p <= niveau: t_g, reden, uit = 1, "breakeven" if be else "stop", p
        return reden, uit

    # 1. zakt door naar 34 -> stop (en een tussentijdse dip naar 40 mag hem NIET raken)
    assert loop([44, 40, 38, 34, 60]) == ("stop", 34), loop([44, 40, 38, 34, 60])
    # 2. stijgt door naar 59 -> winst op +30%
    assert loop([46, 50, 59])[0] == "winst"
    # 3. tikt 54 aan (+20%), zakt daarna terug naar 45 -> breakeven, niet de 35-stop
    assert loop([54, 50, 45])[0] == "breakeven", loop([54, 50, 45])
    # 4. tikt 54 aan en gaat daarna door naar 59 -> winst gaat vóór breakeven
    assert loop([54, 56, 59])[0] == "winst"
    print("regel-gerben ok: stop 35 (=-22% onder instap), winst 58,5, breakeven gewapend op 54")

test_regel_gerben()


def test_lotgevallen():
    """Afloop per token, en vooral: de koers uit de keten mag pas gebruikt worden als hij is
    gecontroleerd tegen wat we zelf zagen. Zonder die controle is het weer de 26.647-SOL-fout."""
    import tempfile, subprocess, sys as _sys, json as _json, sqlite3
    import lotgevallen as LG
    import config as C

    # --- status-logica ---
    now = 1_800_000_000
    t = {"migrated_ts": now - 100, "laatste_prijs": 1e-7, "last_ts": now - 10}
    assert LG.status_van(t, 1e-6, now) == "gemigreerd"          # migratie gaat vóór alles
    t = {"migrated_ts": None, "laatste_prijs": 1e-7, "last_ts": now - 10}
    assert LG.status_van(t, 1e-6, now) == "nog_actief"          # gerugd is geen afloop maar een kolom
    assert LG.is_gerugd(t, 1e-6) is True                        # 90% onder de top
    assert LG.is_gerugd({"laatste_prijs": 5e-7}, 1e-6) is False  # 50% onder de top is geen rug
    t = {"migrated_ts": None, "laatste_prijs": 9e-7, "last_ts": now - 10 * 3600}
    assert LG.status_van(t, 1e-6, now) == "dood_op_curve"
    t = {"migrated_ts": None, "laatste_prijs": 9e-7, "last_ts": now - 60}
    assert LG.status_van(t, 1e-6, now) == "nog_actief"

    # --- de ijking van de virtuele startwaarde ---
    # v_sol(toen) - lamports(nu) moet bij elk dood token dezelfde startwaarde geven
    vast = 30_000_000_000
    goed = [(vast + lam, lam) for lam in range(1_000_000, 1_000_000 + 30 * 250_000, 250_000)]
    r = LG.ijk_virtueel(goed)
    assert r["bruikbaar"] and abs(r["virtuele_sol"] - 30.0) < 0.01, r
    # varieert de startwaarde, dan deugt het model niet en mag er niets berekend worden
    import random as _rnd
    _rnd.seed(1)
    slecht = [(vast + lam + _rnd.randint(0, 40_000_000_000), lam) for lam in range(1_000_000, 1_000_000 + 30 * 250_000, 250_000)]
    r = LG.ijk_virtueel(slecht)
    assert r["bruikbaar"] is False and "varieert" in r["reden"], r
    assert LG.ijk_virtueel([(vast, 0)] * 5)["bruikbaar"] is False      # te weinig punten

    # --- eenheden: de afgeleide koers moet in dezelfde eenheid staan als wat we zelf zagen
    # (v_sol/v_tok, lamports per raw token). De eerste versie gaf SOL per heel token: factor 1000.
    V_TOK_START = C.TOTAL_SUPPLY_RAW * 1073 // 1000
    v_tok = 1_000_000_000_000_000
    held = v_tok - V_TOK_START + C.INITIAL_REAL_TOKEN_RESERVES
    lam = 5_000_000_000
    afgeleid = LG.prijs_uit_curve({"lamports": lam, "tokens": held}, vast, V_TOK_START)
    gezien = (vast + lam) / v_tok
    assert abs(afgeleid / gezien - 1) < 1e-9, (afgeleid, gezien)

    # --- de koerscontrole ---
    goed = [(1.0, 1.02)] * 30
    r = LG.controleer(goed); assert r["bruikbaar"] and r["mediane_afwijking"] < 0.03, r
    slecht = [(1.0, 44.0)] * 30                                  # de fout van gisteren, 44x ernaast
    r = LG.controleer(slecht); assert r["bruikbaar"] is False and "afwijking" in r["reden"], r
    weinig = [(1.0, 1.0)] * 5
    r = LG.controleer(weinig); assert r["bruikbaar"] is False and "controlepunten" in r["reden"], r

    # --- eind tot eind op gemaakte data, zonder keten ---
    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); led = os.path.join(d, "l.sqlite"); out = os.path.join(d, "out")
    _synth_full_log(db, n_tok=40)
    r = subprocess.run([_sys.executable, "ledger.py", "--db", db, "--ledger", led, "--out", out], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    r = subprocess.run([_sys.executable, "lotgevallen.py", "--db", db, "--ledger", led, "--out", out, "--geen-rpc"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    J = _json.load(open(os.path.join(out, "lotgevallen.json")))
    assert J["tokens"] > 0, J
    assert "alle tokens" in J["per_niveau"], J["per_niveau"]
    rij = J["per_niveau"]["alle tokens"]
    som = sum(rij[s]["aandeel"] for s in LG.STATUSSEN)
    assert abs(som - 1.0) < 0.001, (som, rij)                    # de statussen moeten optellen tot 100%
    assert J["koerscontrole"]["bruikbaar"] is False              # zonder keten geen koers
    md = open(os.path.join(out, "lotgevallen.md")).read()
    assert "wordt niet gebruikt" in md and "Afloop per screeningniveau" in md
    print("lotgevallen ok:", J["tokens"], "tokens |",
          {s: rij[s]["aandeel"] for s in LG.STATUSSEN})

test_lotgevallen()


def test_lot_eenheid_top():
    """De top staat in de bot-database in SOL per heel token; de koers waar wij mee rekenen in
    lamports per raw token. Dat is een factor 1000. Op 13 sept 09:30 stond daardoor in het rapport
    dat vasthouden +60.325% opleverde en werd bijna geen token als 'gerugd' geteld. Deze test
    rekent één token met de hand door en controleert allebei de gevolgen."""
    import tempfile, subprocess, sys as _sys, json as _json, sqlite3
    import lotgevallen as LG
    import config as C
    import curve as CV

    assert LG.PRIJS_FACTOR == 1000, LG.PRIJS_FACTOR

    # Eén token: top bij v_sol/v_tok, nu 1/3 daarvan. In SOL per heel token is de top duizend keer
    # kleiner. Zonder omrekening lijkt de koers van nu 333x de top in plaats van een derde.
    v_sol, v_tok = 40_000_000_000, 900_000_000_000_000
    top_lamports_per_raw = v_sol / v_tok
    top_sol_per_token = CV.price_sol(v_sol, v_tok)
    assert abs(top_sol_per_token * LG.PRIJS_FACTOR / top_lamports_per_raw - 1) < 1e-9
    nu = top_lamports_per_raw / 3

    # gevolg 1: de rug-indeling. Een derde van de top is geen rug (drempel is 80% eronder), maar
    # met de niet-omgerekende top lijkt de koers ver bóven de top te staan en valt hij er ook buiten.
    t = {"migrated_ts": None, "laatste_prijs": nu, "last_ts": 1_800_000_000 - 60}
    assert LG.is_gerugd(t, top_lamports_per_raw) is False       # een derde van de top is geen rug
    t2 = {"migrated_ts": None, "laatste_prijs": top_lamports_per_raw * 0.1, "last_ts": 1_800_000_000 - 60}
    assert LG.is_gerugd(t2, top_lamports_per_raw) is True
    assert LG.is_gerugd(t2, top_sol_per_token) is False, "zonder omrekening wordt geen rug gezien"

    # gevolg 2: het rendement van vasthouden vanaf een 45%-dip. Nu op een derde van de top betekent
    # een derde gedeeld door 0,55 = -39%, niet +60.000%.
    echt = nu / (top_lamports_per_raw * 0.55) - 1
    assert -0.40 < echt < -0.38, echt
    fout = nu / (top_sol_per_token * 0.55) - 1
    assert fout > 500, fout                                   # dit stond er gisteren

    # --- koers_nu: nooit stilzwijgend een oude waarneming als 'koers van nu' doorgeven ---
    act = {"mint": "A", "status": "nog_actief", "laatste_prijs": 5.0}
    mig = {"mint": "B", "status": "gemigreerd", "laatste_prijs": 5.0}
    doo = {"mint": "C", "status": "dood_op_curve", "laatste_prijs": 5.0}
    assert LG.koers_nu(act, {}, True) == (None, "nog_niet_opgehaald")     # actief zonder keten: geen koers
    assert LG.koers_nu(act, {"A": 7.0}, True) == (7.0, "keten")
    assert LG.koers_nu(mig, {"B": 7.0}, True)[0] is None                  # pool lezen we nog niet
    assert LG.koers_nu(mig, {}, True)[1] == "gemigreerd_geen_koers"
    assert LG.koers_nu(doo, {}, True) == (5.0, "stil_onveranderd")        # stil: onveranderd, dus geldig
    assert LG.koers_nu(doo, {}, False)[0] is None                         # ijking gezakt: niets

    # --- eind tot eind: met een top in de database mag er geen rendement van 600x uitkomen ---
    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); led = os.path.join(d, "l.sqlite"); out = os.path.join(d, "out")
    _synth_full_log(db, n_tok=40)
    c = sqlite3.connect(db)
    rijen = c.execute("SELECT mint FROM tokens").fetchall()
    for (m,) in rijen:
        c.execute("UPDATE tokens SET ath_price=? WHERE mint=?", (top_sol_per_token, m))
    c.commit(); c.close()
    r = subprocess.run([_sys.executable, "ledger.py", "--db", db, "--ledger", led, "--out", out], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    r = subprocess.run([_sys.executable, "lotgevallen.py", "--db", db, "--ledger", led, "--out", out, "--geen-rpc"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    J = _json.load(open(os.path.join(out, "lotgevallen.json")))
    for naam, v in (J.get("vasthouden") or {}).items():
        med = v["vanaf_45pct_dip"].get("mediaan")
        assert med is None or -1.0 <= med <= 10.0, (naam, med)   # 600x betekent een eenheidsfout
    print("lot-eenheid ok: top omgerekend, -39% i.p.v. +60.000%")

test_lot_eenheid_top()


def test_lot_rug_en_rpcfout():
    """Twee fouten uit de run van 13 sept 12:23, beide met hetzelfde gevolg: tokens die stilletjes
    uit de cijfers vielen.

    1. 'Gerugd' was een status en overschreef 'dood op de curve'. Daardoor zakte dood op de curve
       van 82% naar 44%, en vielen 1617 tokens uit de koersberekening omdat die op die status keek.
    2. Een mislukte RPC-call werd als 'curve is weg' opgeslagen, en opgeslagen antwoorden worden
       niet opnieuw opgehaald. 35 van de 296 calls verdwenen zo permanent."""
    import tempfile, sqlite3, json as _json, subprocess, sys as _sys
    import lotgevallen as LG
    now = 1_800_000_000

    # 1. een token dat zowel gerugd als stil is telt in beide, en houdt zijn koers
    stil_gerugd = {"mint": "R", "migrated_ts": None, "laatste_prijs": 1e-7, "last_ts": now - 10 * 3600}
    assert LG.status_van(stil_gerugd, 1e-6, now) == "dood_op_curve"
    assert LG.is_gerugd(stil_gerugd, 1e-6) is True
    stil_gerugd["status"] = "dood_op_curve"
    assert LG.koers_nu(stil_gerugd, {}, True) == (1e-7, "stil_onveranderd"), "gerugd mag geen koers kosten"
    assert set(LG.STATUSSEN) == {"gemigreerd", "nog_actief", "dood_op_curve"}, LG.STATUSSEN

    # 2. een dode keten mag niets opslaan — anders staat 'curve weg' er voor altijd in
    class DodeRpc:
        calls = 0; errors = 0; pogingen = 1
        def call(self, m, p):
            DodeRpc.calls += 1; DodeRpc.errors += 1; return LG.FOUT
    r = LG.curve_staat(DodeRpc(), "M", "BC")
    assert r is LG.FOUT, r
    assert r is not None, "FOUT mag niet als 'account weg' gelezen worden"

    d = tempfile.mkdtemp(); db = os.path.join(d, "m.sqlite"); led = os.path.join(d, "l.sqlite"); out = os.path.join(d, "out")
    _synth_full_log(db, n_tok=30)
    r = subprocess.run([_sys.executable, "ledger.py", "--db", db, "--ledger", led, "--out", out], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    import lotgevallen as LG2
    main_db = sqlite3.connect(f"file:{db}?mode=ro", uri=True); l = sqlite3.connect(led)
    l.executescript(LG2.SCHEMA); LG2.zorg_kolommen(l)
    ath = {m: a * LG2.PRIJS_FACTOR for m, a in main_db.execute("SELECT mint, 1.0 FROM tokens")}
    rep, _ = LG2.bouw(main_db, l, l, DodeRpc(), now, ath)
    assert l.execute("SELECT count(*) FROM lot").fetchone()[0] == 0, "mislukte calls zijn opgeslagen"
    assert rep["ijking"]["bruikbaar"] is False
    for naam, rij in rep["per_niveau"].items():
        som = sum(rij[st]["aandeel"] for st in LG2.STATUSSEN)
        assert abs(som - 1.0) < 0.001, (naam, som)              # de drie statussen tellen op tot 100%
        assert "gerugd" in rij                                  # en gerugd staat er los naast
    # 3. een versiewissel gooit oude ketenantwoorden weg; de rijen uit de foute versie zijn niet
    #    van een echt verdwenen curve te onderscheiden, dus ze moeten er allemaal uit
    l.execute("INSERT INTO lot VALUES('X','dood_op_curve',NULL,'curve_weg',1,NULL,NULL,NULL)"); l.commit()
    assert LG2.wis_bij_nieuwe_versie(l, "lot-vtest") == 1
    assert l.execute("SELECT count(*) FROM lot").fetchone()[0] == 0
    assert LG2.wis_bij_nieuwe_versie(l, "lot-vtest") == 0        # zelfde versie: niets weggooien
    print("lot rug/rpcfout ok: gerugd is een kolom, mislukte calls worden niet opgeslagen, versiewissel wist")

test_lot_rug_en_rpcfout()


def test_lot_schema_migratie():
    """CREATE TABLE IF NOT EXISTS laat een bestaande tabel ongemoeid. Op 13 sept 09:09 crashte
    lotgevallen daarop met 'no such column: lamports' — de derde keer in dit project. Deze test
    maakt eerst de oude tabel en controleert dan dat de nieuwe kolommen erbij komen."""
    import tempfile, sqlite3
    import lotgevallen as LG
    d = tempfile.mkdtemp(); pad = os.path.join(d, "oud.sqlite")
    db = sqlite3.connect(pad)
    db.execute("CREATE TABLE lot(mint TEXT PRIMARY KEY, status TEXT)")      # het oude schema
    db.execute("INSERT INTO lot VALUES('M1','dood_op_curve')"); db.commit()
    db.executescript(LG.SCHEMA)                                             # doet niets aan de tabel
    have = {r[1] for r in db.execute("PRAGMA table_info(lot)")}
    assert "lamports" not in have, "opzet van de test klopt niet"
    LG.zorg_kolommen(db)
    have = {r[1] for r in db.execute("PRAGMA table_info(lot)")}
    for k in ("keten_prijs", "keten_bron", "gecheckt_ts", "afwijking", "lamports", "tokens"):
        assert k in have, (k, have)
    assert db.execute("SELECT status FROM lot WHERE mint='M1'").fetchone()[0] == "dood_op_curve"  # data blijft
    LG.zorg_kolommen(db)                                                    # nog eens: mag niet stukgaan
    q = "SELECT mint, keten_prijs, keten_bron, lamports, tokens FROM lot WHERE lamports IS NOT NULL"
    assert db.execute(q).fetchall() == []
    print("lot-schema ok: kolommen bijgezet, data behouden")

test_lot_schema_migratie()
