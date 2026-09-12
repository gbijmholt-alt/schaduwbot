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
    print("pumpswap pool navragen ok: offset", ev["offset_pool"], "bevestigd via de eigenaar")

test_pumpswap_pool_navragen()
