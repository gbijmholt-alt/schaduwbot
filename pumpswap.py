"""PumpSwap-dekking (na migratie van de bonding curve).

Twee dingen, in deze volgorde:

1. `na_migratie` — beantwoordt de vraag "wordt die open SOL nog winst?" zonder ook maar
   iets over de event-layout te hoeven weten. Voor open posities in gemigreerde tokens
   halen we het hùidige tokensaldo van de wallet op. Saldo ≈ 0 = ze zijn eruit; saldo nog
   vol = ze zitten er nog in. De pool-prijs leiden we generiek af (grootste tokenaccount
   -> eigenaar = pool -> WSOL-saldo van die pool), dus zonder aannames over het programma.

2. `probe` — verificatie van de event-layout van het AMM-programma. We raden niets: we
   zoeken de velden empirisch. Per transactie weten we uit pre/post-balansen wat er
   werkelijk van eigenaar wisselde; daarna zoeken we in de event-bytes op welke offset
   die bedragen staan. Een offset geldt pas als vastgesteld bij >= MIN_MATCH over
   >= MIN_SAMPLES transacties. Alleen dan schrijven we data/pumpswap_layout.json, en
   alleen als dat bestand bestaat gaat de bot AMM-trades inlezen (zie main.py).

Gebruik:  python pumpswap.py            (beide, schrijft reports/pumpswap.md)
          python pumpswap.py na_migratie
          python pumpswap.py probe
"""
import base64, hashlib, json, os, sqlite3, statistics, struct, sys, time
from collections import Counter, defaultdict

import base58
import config as C

# ledger.py is een zwaar analysemodule; de bot importeert pumpswap alleen voor de decoder,
# dus halen we die pas op als een analysepad het echt nodig heeft.
def _ledger():
    import ledger
    return ledger

def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None

PUMPSWAP_PROGRAM = "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"
WSOL = "So11111111111111111111111111111111111111112"
ANCHOR_CPI_EVENT = bytes.fromhex("e445a52e51cb9a1d")   # prefix bij emit_cpi!

LEDGER_DB = os.getenv("LEDGER_DB", "data/ledger.sqlite")
LAYOUT_PATH = os.getenv("PUMPSWAP_LAYOUT", "data/pumpswap_layout.json")
RPS = float(os.getenv("PUMPSWAP_RPS", 2.0))

# --- 1. na-migratie-check ---
PAREN_PER_RUN = int(os.getenv("PUMPSWAP_PAREN", 400))    # (wallet, mint)-paren waarvan we het saldo ophalen
MINTS_PRIJS_PER_RUN = int(os.getenv("PUMPSWAP_MINTS", 60))
VERVERSEN_S = 6 * 3600
VERKOCHT_DREMPEL = 0.01      # <= 1% van de gekochte tokens over = eruit
DEELS_DREMPEL = 0.80         # <= 80% over = deels verkocht

# --- 2. probe ---
PROBE_VERSIE = "probe-v4-pool-navragen"
ACCT_VOORBEELDEN = 4     # telwijze; wijzigen = alle tellers en de layout ongeldig
MIN_SAMPLES = int(os.getenv("PUMPSWAP_MIN_SAMPLES", 50))
MIN_MATCH = float(os.getenv("PUMPSWAP_MIN_MATCH", 0.95))
PROBE_TX = int(os.getenv("PUMPSWAP_PROBE_TX", 400))
KANDIDAAT_NAMEN = ["BuyEvent", "SellEvent", "CreatePoolEvent", "DepositEvent", "WithdrawEvent",
                   "CreateConfigEvent", "UpdateAdminEvent", "UpdateFeeConfigEvent", "TradeEvent",
                   "SyncUserVolumeAccumulatorEvent", "CollectCoinCreatorFeeEvent",
                   "SetCoinCreatorEvent", "ExtendAccountEvent", "DisableEvent"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS amm_pos(wallet TEXT, mint TEXT, verwacht_tok INTEGER, saldo_tok INTEGER,
  status TEXT, kostprijs_sol REAL, gecheckt_ts REAL, PRIMARY KEY(wallet, mint));
CREATE TABLE IF NOT EXISTS amm_prijs(mint TEXT PRIMARY KEY, pool TEXT, prijs_sol REAL, tok_in_pool INTEGER,
  wsol_in_pool REAL, gecheckt_ts REAL, curve_prijs REAL, factor REAL, afgekeurd TEXT);
CREATE TABLE IF NOT EXISTS amm_layout(disc TEXT PRIMARY KEY, naam TEXT, bron TEXT, n INTEGER, json TEXT, gecheckt_ts REAL);
CREATE TABLE IF NOT EXISTS amm_probe(disc TEXT PRIMARY KEY, tellers TEXT, bijgewerkt REAL);
CREATE TABLE IF NOT EXISTS amm_probe_meta(k TEXT PRIMARY KEY, v REAL);
"""


def disc_of(name): return hashlib.sha256(f"event:{name}".encode()).digest()[:8]


def open_led():
    if not os.path.exists(LEDGER_DB): return None
    db = sqlite3.connect(LEDGER_DB)
    db.execute("PRAGMA journal_mode=WAL"); db.executescript(SCHEMA)
    have = {r[1] for r in db.execute("PRAGMA table_info(amm_prijs)")}
    for naam, typ in (("curve_prijs", "REAL"), ("factor", "REAL"), ("afgekeurd", "TEXT")):
        if naam not in have: db.execute(f"ALTER TABLE amm_prijs ADD COLUMN {naam} {typ}")
    # prijzen van vóór de plausibiliteitscheck opnieuw ophalen
    if not meta_prijs_ok(db): db.execute("DELETE FROM amm_prijs")
    # tellers van vóór deze telwijze weggooien: ze zijn opgeblazen, en een layout die eruit
    # volgde is niet bewezen
    if not meta_probe_ok(db):
        db.execute("DELETE FROM amm_probe"); db.execute("DELETE FROM amm_probe_meta")
        db.execute("DELETE FROM amm_layout")
        try: os.remove(LAYOUT_PATH)
        except OSError: pass
        log(f"telwijze -> {PROBE_VERSIE}: tellers en layout gewist, opnieuw opbouwen")
    db.commit()
    return db


def meta_probe_ok(db):
    db.execute("CREATE TABLE IF NOT EXISTS amm_meta(k TEXT PRIMARY KEY, v TEXT)")
    r = db.execute("SELECT v FROM amm_meta WHERE k = 'probe_versie'").fetchone()
    if r and r[0] == PROBE_VERSIE: return True
    db.execute("INSERT OR REPLACE INTO amm_meta VALUES('probe_versie', ?)", (PROBE_VERSIE,))
    return False


def meta_prijs_ok(db):
    db.execute("CREATE TABLE IF NOT EXISTS amm_meta(k TEXT PRIMARY KEY, v TEXT)")
    r = db.execute("SELECT v FROM amm_meta WHERE k = 'prijs_versie'").fetchone()
    if r and r[0] == "prijs-v2-controle": return True
    db.execute("INSERT OR REPLACE INTO amm_meta VALUES('prijs_versie', 'prijs-v2-controle')")
    return False


# ================================================================ 1. na migratie
def kandidaat_paren(led, now, limit):
    """Open posities in gemigreerde tokens. Eerst de gevolgde wallets, dan de grootste bedragen."""
    CLOSED_SQL = _ledger().CLOSED_SQL
    q = f"""SELECT w.wallet, w.mint, w.tok_buy - w.tok_sell, w.sol_out - w.sol_in,
                   CASE WHEN wa.wallet IS NULL THEN 1 ELSE 0 END AS niet_gevolgd
            FROM wt w JOIN token t ON t.mint = w.mint
            LEFT JOIN watch wa ON wa.wallet = w.wallet
            LEFT JOIN amm_pos p ON p.wallet = w.wallet AND p.mint = w.mint
            WHERE t.migrated_ts IS NOT NULL AND t.gap = 0 AND NOT {CLOSED_SQL}
              AND w.tok_buy - w.tok_sell > 0 AND w.sol_out - w.sol_in > 0.05
              AND (p.gecheckt_ts IS NULL OR p.gecheckt_ts < ?)
            ORDER BY niet_gevolgd, (w.sol_out - w.sol_in) DESC LIMIT ?"""
    return led.execute(q, (now - VERVERSEN_S, limit)).fetchall()


def saldo_van(rpc, wallet, mint):
    res = rpc.call("getTokenAccountsByOwner", [wallet, {"mint": mint}, {"encoding": "jsonParsed", "commitment": "confirmed"}])
    if res is None: return None
    tot = 0
    for v in (res or {}).get("value", []):
        try: tot += int(v["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"])
        except Exception: pass
    return tot


MAX_PRIJSFACTOR = float(os.getenv("PUMPSWAP_MAX_PRIJSFACTOR", 20))   # t.o.v. de laatste curveprijs


def pool_prijs(rpc, mint, curve_prijs=None):
    """Grootste tokenaccount -> eigenaar (de pool) -> WSOL-saldo van die pool. Geen aanname over
    welk programma de pool beheert; we lezen alleen twee saldi.

    Met controles, want de grootste tokenhouder hoeft niet de pool te zijn. Is het een gewone
    wallet met veel WSOL en weinig tokens, dan rolt daar een absurde prijs uit. Eisen: de eigenaar
    is geen normale wallet (een pool is een PDA, dus niet op de curve), hij houdt zelf WSOL aan,
    en de prijs wijkt niet meer dan MAX_PRIJSFACTOR af van de laatste curveprijs. Alles wat afvalt
    wordt geteld en niet gebruikt, niet stilletjes meegerekend."""
    la = rpc.call("getTokenLargestAccounts", [mint, {"commitment": "confirmed"}])
    vals = (la or {}).get("value") or []
    if not vals: return None
    ta = vals[0]["address"]; tok = int(vals[0]["amount"])
    info = rpc.call("getAccountInfo", [ta, {"encoding": "jsonParsed", "commitment": "confirmed"}])
    try: owner = info["value"]["data"]["parsed"]["info"]["owner"]
    except Exception: return None
    ws = rpc.call("getTokenAccountsByOwner", [owner, {"mint": WSOL}, {"encoding": "jsonParsed", "commitment": "confirmed"}])
    wsol = 0.0
    for v in (ws or {}).get("value", []):
        try: wsol += int(v["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"]) / 1e9
        except Exception: pass
    uit = {"pool": owner, "prijs_sol": None, "tok_in_pool": tok, "wsol_in_pool": round(wsol, 4),
           "curve_prijs": curve_prijs, "factor": None, "afgekeurd": None}
    if tok <= 0 or wsol <= 0: uit["afgekeurd"] = "geen_wsol_of_tokens"; return uit
    op_curve = _ledger().on_curve(owner)
    if op_curve is True: uit["afgekeurd"] = "eigenaar_is_gewone_wallet"; return uit
    prijs = wsol / (tok / 10**C.TOKEN_DECIMALS)
    if curve_prijs and curve_prijs > 0:
        uit["factor"] = round(prijs / curve_prijs, 3)
        if not (1 / MAX_PRIJSFACTOR <= uit["factor"] <= MAX_PRIJSFACTOR):
            uit["afgekeurd"] = "prijs_onwaarschijnlijk"; return uit
    uit["prijs_sol"] = prijs
    return uit


def run_na_migratie(led, rpc, now):
    paren = kandidaat_paren(led, now, PAREN_PER_RUN)
    log(f"na-migratie: {len(paren)} paren te checken")
    gedaan = 0
    for wallet, mint, verwacht, kost, _ in paren:
        saldo = saldo_van(rpc, wallet, mint)
        if saldo is None: continue
        frac = saldo / verwacht if verwacht > 0 else 0.0
        status = "verkocht" if frac <= VERKOCHT_DREMPEL else ("deels_verkocht" if frac <= DEELS_DREMPEL else "nog_in_bezit")
        led.execute("INSERT OR REPLACE INTO amm_pos VALUES(?,?,?,?,?,?,?)", (wallet, mint, verwacht, saldo, status, kost, now))
        gedaan += 1
        if gedaan % 50 == 0: led.commit()
    led.commit()
    # prijzen voor de mints waar nog tokens in zitten
    mints = led.execute("""SELECT p.mint, t.v_sol, t.v_tok FROM amm_pos p JOIN token t ON t.mint = p.mint
        LEFT JOIN amm_prijs q ON q.mint = p.mint
        WHERE p.status != 'verkocht' AND (q.gecheckt_ts IS NULL OR q.gecheckt_ts < ?)
        GROUP BY p.mint ORDER BY SUM(p.kostprijs_sol) DESC LIMIT ?""", (now - VERVERSEN_S, MINTS_PRIJS_PER_RUN)).fetchall()
    for mint, v_sol, v_tok in mints:
        # laatste curveprijs in SOL per heel token, als referentie voor de plausibiliteitscheck
        cp = ((v_sol / 1e9) / (v_tok / 10**C.TOKEN_DECIMALS)) if (v_sol and v_tok) else None
        pp = pool_prijs(rpc, mint, cp)
        if pp is None: continue
        led.execute("INSERT OR REPLACE INTO amm_prijs VALUES(?,?,?,?,?,?,?,?,?)",
                    (mint, pp["pool"], pp["prijs_sol"], pp["tok_in_pool"], pp["wsol_in_pool"], now,
                     pp["curve_prijs"], pp["factor"], pp["afgekeurd"]))
    led.commit()
    return gedaan, len(mints)


def na_migratie_report(led):
    CLOSED_SQL = _ledger().CLOSED_SQL
    tot = led.execute(f"""SELECT COALESCE(SUM(w.sol_out - w.sol_in), 0), COUNT(*) FROM wt w JOIN token t ON t.mint = w.mint
        WHERE t.migrated_ts IS NOT NULL AND t.gap = 0 AND NOT {CLOSED_SQL} AND w.sol_out - w.sol_in > 0""").fetchone()
    rows = led.execute("""SELECT status, COUNT(*), SUM(kostprijs_sol) FROM amm_pos GROUP BY status""").fetchall()
    per = {s: {"posities": n, "kostprijs_sol": round(k or 0, 2)} for s, n, k in rows}
    gecheckt_kost = sum(v["kostprijs_sol"] for v in per.values())
    # restwaarde van wat nog in bezit is, tegen de afgeleide poolprijs
    rest = led.execute("""SELECT COALESCE(SUM(p.saldo_tok / 1e6 * q.prijs_sol), 0), COUNT(*), COALESCE(SUM(p.kostprijs_sol), 0)
        FROM amm_pos p JOIN amm_prijs q ON q.mint = p.mint
        WHERE p.status != 'verkocht' AND q.prijs_sol IS NOT NULL AND q.afgekeurd IS NULL""").fetchone()
    prijs_status = dict(led.execute("""SELECT COALESCE(afgekeurd, 'goedgekeurd'), COUNT(*) FROM amm_prijs GROUP BY 1"""))
    facts = [r[0] for r in led.execute("SELECT factor FROM amm_prijs WHERE factor IS NOT NULL AND afgekeurd IS NULL")]
    per_rol = led.execute("""SELECT CASE WHEN wa.wallet IS NULL THEN 'niet_gevolgd' ELSE 'gevolgd' END,
        p.status, COUNT(*), SUM(p.kostprijs_sol) FROM amm_pos p LEFT JOIN watch wa ON wa.wallet = p.wallet
        GROUP BY 1, 2""").fetchall()
    groepen = defaultdict(dict)
    for grp, status, n, k in per_rol: groepen[grp][status] = {"posities": n, "kostprijs_sol": round(k or 0, 2)}
    return {
        "open_totaal_sol": round(tot[0], 2), "open_posities_totaal": tot[1],
        "gecheckt_posities": sum(v["posities"] for v in per.values()), "gecheckt_kostprijs_sol": round(gecheckt_kost, 2),
        "per_status": per, "per_groep": dict(groepen),
        "restwaarde_nog_in_bezit_sol": round(rest[0], 2), "restwaarde_posities": rest[1], "restwaarde_kostprijs_sol": round(rest[2], 2),
        "prijs_status": prijs_status, "mediane_factor_vs_curve": round(statistics.median(facts), 2) if facts else None,
        "_uitleg": "kostprijs_sol = SOL erin min SOL eruit op de curve, dus wat er nog 'open' stond. "
                   "'verkocht' betekent: het tokensaldo van de wallet is nu leeg, dus er is ná migratie verkocht — "
                   "voor welk bedrag weten we niet, daarvoor is de trade-ingestie nodig. Restwaarde is tegen de "
                   "huidige poolprijs en overschat, want niet iedereen kan tegen die prijs verkopen.",
    }


# ================================================================ 2. layout-probe
def blobs_uit_tx(tx):
    """Geeft [(bron, payload_bytes)] voor alle kandidaat-eventdata in de transactie."""
    out = []
    meta = tx.get("meta") or {}
    for line in (meta.get("logMessages") or []):
        if line.startswith("Program data: "):
            try: out.append(("log", base64.b64decode(line[14:])))
            except Exception: pass
    for grp in (meta.get("innerInstructions") or []):
        for ins in grp.get("instructions") or []:
            if ins.get("programId") != PUMPSWAP_PROGRAM: continue
            d = ins.get("data")
            if not d: continue
            try: raw = base58.b58decode(d)
            except Exception: continue
            if raw[:8] == ANCHOR_CPI_EVENT: out.append(("inner_cpi", raw[8:]))
            else: out.append(("inner", raw))
    return out


def account_keys(tx):
    return [k if isinstance(k, str) else k.get("pubkey") for k in
            ((tx.get("transaction") or {}).get("message") or {}).get("accountKeys") or []]


def waarheid_uit_tx(tx, streng=True):
    """Wat wisselde er werkelijk van eigenaar? Geeft een dict of None.

    `streng` sluit transacties uit waarin het bedrag per event niet gelijk kan zijn aan het
    netto saldoverschil van de transactie: routers (Jupiter) splitsen één order over meerdere
    legs, en dan telt de balans iets anders dan één event. Zonder dat filter vergelijk je
    appels met peren en zakt de match omlaag zonder dat de layout fout is."""
    meta = tx.get("meta") or {}
    pre = {(b["accountIndex"]): b for b in (meta.get("preTokenBalances") or [])}
    post = {(b["accountIndex"]): b for b in (meta.get("postTokenBalances") or [])}
    per_mint = defaultdict(lambda: defaultdict(int))     # mint -> owner -> delta raw
    for idx in set(pre) | set(post):
        b = post.get(idx) or pre.get(idx); mint = b.get("mint"); owner = b.get("owner")
        a0 = int((pre.get(idx) or {}).get("uiTokenAmount", {}).get("amount", 0) or 0)
        a1 = int((post.get(idx) or {}).get("uiTokenAmount", {}).get("amount", 0) or 0)
        if a1 != a0: per_mint[mint][owner] += a1 - a0
    memes = [m for m in per_mint if m != WSOL]
    if len(memes) != 1: return None
    mint = memes[0]
    eig = per_mint[mint]
    # precies twee partijen (pool en handelaar) -> het bedrag van de transactie is het bedrag van het event
    if streng and len(eig) != 2: return None
    kand = sorted(eig.items(), key=lambda kv: -abs(kv[1]))
    if not kand: return None
    eigenaar, tok_delta = kand[0]
    lams = []
    if WSOL in per_mint:
        lams = [abs(v) for v in sorted(per_mint[WSOL].values(), key=lambda v: -abs(v))]
    if not lams:      # geen WSOL-account: native saldoverandering van de ondertekenaar
        pb, qb = meta.get("preBalances") or [], meta.get("postBalances") or []
        if account_keys(tx) and pb and qb: lams = [abs((qb[0] - pb[0]) + (meta.get("fee") or 0))]
    lams = [x for x in lams if x > 0]
    if abs(tok_delta) == 0 or not lams: return None
    # meerdere WSOL-kandidaten: het event noemt bruto of netto, dus we accepteren elk van beide
    return {"mint": mint, "tok": abs(tok_delta), "lamports": lams, "eigenaar": eigenaar,
            "keys": [k for k in account_keys(tx) if k]}


BRON_VOORKEUR = ("log", "inner_cpi", "inner")


def events_van_tx(tx):
    """Geeft ([(bronnen, blob)], aantal echte events per discriminator).

    Eén event staat in de transactie twee keer: als logregel én als binnenste instructie
    (`emit_cpi!`). Zonder dat te verrekenen lijkt élke transactie 'meerdere events van hetzelfde
    type' te hebben en valt alles af — dat ging op 12 sept 09:59 mis.

    We tellen daarom per bron apart en nemen per discriminator het hóógste aantal: staat hetzelfde
    event in twee bronnen, dan blijft de telling 1, en mist een bron events (Solana kapt lange logs
    af) dan kiezen we de voorzichtige kant en sluiten we de transactie uit. Dit werkt ook als de
    bytes per bron niet exact gelijk zijn, en op die aanname wilde ik niet leunen. Voor het bewijs
    gebruiken we per discriminator één bron, met de logregel als eerste keuze omdat dat is wat de
    bot kan meelezen — tenzij de logs zijn afgekapt."""
    per_bron = defaultdict(list)
    for bron, bl in blobs_uit_tx(tx):
        if len(bl) >= 16: per_bron[bron].append(bl)
    tel_per_bron = {b: Counter(bl[:8].hex() for bl in v) for b, v in per_bron.items()}
    discs = set().union(*(set(c) for c in tel_per_bron.values())) if tel_per_bron else set()
    tel = {d: max(c[d] for c in tel_per_bron.values() if d in c) for d in discs}
    bronnen = defaultdict(set)
    for bron, v in per_bron.items():
        for bl in v: bronnen[bl].add(bron)
    afgekapt = any("truncated" in l.lower() for l in ((tx.get("meta") or {}).get("logMessages") or []))
    voorkeur = BRON_VOORKEUR[1:] + ("log",) if afgekapt else BRON_VOORKEUR
    keuze = {}
    for d in discs:
        for b in voorkeur:
            if d in tel_per_bron.get(b, {}): keuze[d] = b; break
    blobs = []
    for bron, v in per_bron.items():
        for bl in v:
            if keuze.get(bl[:8].hex()) == bron: blobs.append((sorted(bronnen[bl]), bl))
    return blobs, tel


def zoek_offsets(blob, waarde):
    """Alle offsets waar `waarde` als little-endian u64 in blob staat."""
    out = []
    for i in range(0, max(0, len(blob) - 7)):
        if struct.unpack_from("<Q", blob, i)[0] == waarde: out.append(i)
    return out


def zoek_pubkey(blob, key58):
    try: raw = base58.b58decode(key58)
    except Exception: return []
    if len(raw) != 32: return []
    out, start = [], 0
    while (i := blob.find(raw, start)) != -1: out.append(i); start = i + 1
    return out


def run_probe(rpc, n_tx=PROBE_TX):
    sigs = rpc.call("getSignaturesForAddress", [PUMPSWAP_PROGRAM, {"limit": min(1000, n_tx * 2), "commitment": "confirmed"}]) or []
    sigs = [s["signature"] for s in sigs if not s.get("err")][:n_tx]
    log(f"probe: {len(sigs)} transacties ophalen")
    per_disc = defaultdict(lambda: {"bron": set(), "n": 0, "tok": defaultdict(int), "sol": defaultdict(int),
                                    "mint": defaultdict(int), "user": defaultdict(int), "acct": defaultdict(int),
                                    "lengtes": defaultdict(int), "afw": defaultdict(list), "acct_vb": defaultdict(list)})
    n_tx_ok = n_waarheid = n_multi = n_router = 0
    for sig in sigs:
        tx = rpc.call("getTransaction", [sig, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0, "commitment": "confirmed"}])
        if not tx: continue
        n_tx_ok += 1
        w = waarheid_uit_tx(tx)
        if w is None:
            if waarheid_uit_tx(tx, streng=False) is not None: n_router += 1
            continue
        blobs, tel = events_van_tx(tx)
        multi = any(v > 1 for v in tel.values())
        if multi: n_multi += 1
        n_waarheid += 1
        for bron_lijst, blob in blobs:
            d = blob[:8].hex(); body = blob[8:]
            e = per_disc[d]; e["bron"].update(bron_lijst)
            if tel[d] > 1: continue                  # meerdere events van dit type: niet als bewijs gebruiken
            e["n"] += 1; e["lengtes"][len(body)] += 1
            # Per voorbeeld mag een offset maar één keer meetellen. Zonder de set() hieronder
            # telde een offset dubbel zodra twee kandidaatbedragen (bruto en netto WSOL) op
            # dezelfde plek uitkwamen, en dan komt er een 'match' van boven 100% uit — precies
            # wat SellEvent op 12 sept 13:05 liet zien (@376, 142%). Zo'n percentage is geen
            # match maar een telfout.
            hit_t = set(zoek_offsets(body, w["tok"]))
            for i in hit_t: e["tok"][i] += 1
            hit_s = set()
            for lam in w["lamports"]: hit_s.update(zoek_offsets(body, lam))
            for i in hit_s: e["sol"][i] += 1
            for i in set(zoek_pubkey(body, w["mint"])): e["mint"][i] += 1
            for i in set(zoek_pubkey(body, w["eigenaar"])): e["user"][i] += 1
            # welke offsets bevatten überhaupt een account uit deze transactie? Zo vinden we de
            # pool, want het event noemt vermoedelijk de pool en niet de mint.
            hit_a = set()
            for k in set(w["keys"]): hit_a.update(zoek_pubkey(body, k))
            for i in hit_a:
                e["acct"][i] += 1
                if len(e["acct_vb"][i]) < ACCT_VOORBEELDEN:
                    e["acct_vb"][i].append(base58.b58encode(body[i:i + 32]).decode())
            # diagnose: als de tokens niet matchen, hoe ver zit het ernaast?
            if not hit_t and len(body) >= 16:
                kand = [struct.unpack_from("<Q", body, i)[0] for i in range(0, len(body) - 7, 8)]
                dichtbij = [abs(v - w["tok"]) / w["tok"] for v in kand if v and 0.5 < v / w["tok"] < 2.0]
                if dichtbij: e["afw"]["tokens"].append(round(min(dichtbij), 5))
    ruw = {}
    for d, e in per_disc.items():
        ruw[d] = {"bron": sorted(e["bron"]), "n": e["n"], "lengtes": {str(k): v for k, v in e["lengtes"].items()},
                  "afw": list(e["afw"]["tokens"]), "acct_vb": {str(k): v for k, v in e["acct_vb"].items()},
                  **{veld: {str(k): v for k, v in e[veld].items()} for veld in ("tok", "sol", "mint", "user", "acct")}}
    tellers = {"transacties_opgehaald": n_tx_ok, "transacties_met_waarheid": n_waarheid,
               "transacties_meerdere_events": n_multi, "transacties_router_of_meerdere_partijen": n_router}
    return ruw, tellers


def tel_op(led, ruw, tellers):
    """Tel de tellers van deze run op bij eerdere runs. Met het strenge filter blijven er per run
    weinig bruikbare transacties over; zonder optellen halen we de eis van 50 voorbeelden nooit."""
    for d, e in ruw.items():
        oud = led.execute("SELECT tellers FROM amm_probe WHERE disc = ?", (d,)).fetchone()
        samen = json.loads(oud[0]) if oud else {"bron": [], "n": 0, "lengtes": {}, "afw": [], "acct_vb": {},
                                                "tok": {}, "sol": {}, "mint": {}, "user": {}, "acct": {}}
        samen["bron"] = sorted(set(samen.get("bron", [])) | set(e["bron"]))
        samen["n"] = samen.get("n", 0) + e["n"]
        samen["afw"] = (samen.get("afw") or [])[-500:] + e["afw"]
        for veld in ("lengtes", "tok", "sol", "mint", "user", "acct"):
            bij = samen.setdefault(veld, {})
            for k, v in e[veld].items(): bij[k] = bij.get(k, 0) + v
        vb = samen.setdefault("acct_vb", {})
        for k, v in (e.get("acct_vb") or {}).items():
            vb[k] = list(dict.fromkeys((vb.get(k) or []) + v))[:ACCT_VOORBEELDEN]
        led.execute("INSERT OR REPLACE INTO amm_probe VALUES(?,?,?)", (d, json.dumps(samen), time.time()))
    for k, v in tellers.items():
        led.execute("INSERT INTO amm_probe_meta VALUES(?,?) ON CONFLICT(k) DO UPDATE SET v = v + excluded.v", (k, v))
    led.commit()
    alles = {d: json.loads(t) for d, t in led.execute("SELECT disc, tellers FROM amm_probe")}
    tot = {k: v for k, v in led.execute("SELECT k, v FROM amm_probe_meta")}
    return alles, tot


def beoordeel(alles, tot):
    naam_van = {disc_of(n).hex(): n for n in KANDIDAAT_NAMEN}
    res = {"programma": PUMPSWAP_PROGRAM, "eisen": {"min_samples": MIN_SAMPLES, "min_match": MIN_MATCH},
           "transacties_opgehaald": int(tot.get("transacties_opgehaald", 0)),
           "transacties_met_waarheid": int(tot.get("transacties_met_waarheid", 0)),
           "transacties_meerdere_events": int(tot.get("transacties_meerdere_events", 0)),
           "transacties_router_of_meerdere_partijen": int(tot.get("transacties_router_of_meerdere_partijen", 0)),
           "events": {}}
    for d, e in sorted(alles.items(), key=lambda kv: -kv[1].get("n", 0)):
        e = {**e, **{veld: {int(k): v for k, v in (e.get(veld) or {}).items()} for veld in ("lengtes", "tok", "sol", "mint", "user", "acct")}}
        e["acct_vb"] = {int(k): v for k, v in (e.get("acct_vb") or {}).items()}
        e["afw"] = {"tokens": e.get("afw") or []}
        n = e["n"]
        best = lambda dd: (max(dd.items(), key=lambda kv: kv[1]) if dd else (None, 0))
        ot, ct = best(e["tok"]); os_, cs = best(e["sol"]); om, cm = best(e["mint"]); ou, cu = best(e["user"])
        # De pool: een offset met een account uit de transactie, maar niet de mint- of user-offset.
        # Let op: in één event staan meerdere accounts, dus meerdere offsets halen 100%. De hoogste
        # eruit pakken is willekeurig — daarom geven we álle kandidaten terug en laten we ze
        # narekenen bij de keten (een pool is eigendom van het AMM-programma, een wallet niet).
        acct = {i: c for i, c in e["acct"].items() if i not in (om, ou)}
        f = lambda c: (c / n) if n else 0
        kandidaten = sorted((i for i, c in acct.items() if f(c) >= MIN_MATCH), key=lambda i: (-acct[i], i))
        op, cp = (kandidaten[0], acct[kandidaten[0]]) if kandidaten else best(acct)
        # vastgesteld mag ook met een pool in plaats van een mint; de bot kan zo'n layout nog niet
        # gebruiken (hij kent de pool niet), maar dan weten we wel dat de layout klopt
        via_mint = f(cm) >= MIN_MATCH
        via_pool = False    # wordt pas waar als verifieer_pool() een offset bevestigt
        vast = n >= MIN_SAMPLES and f(ct) >= MIN_MATCH and f(cs) >= MIN_MATCH and (via_mint or via_pool)
        afw = e["afw"]["tokens"]
        telfout = [veld for veld, dd in (("tokens", e["tok"]), ("lamports", e["sol"]), ("mint", e["mint"]),
                                        ("pool", e["acct"]), ("user", e["user"])) if dd and max(dd.values()) > n]
        if telfout: vast = False
        res["events"][d] = {"naam": naam_van.get(d), "bron": sorted(e.get("bron") or []), "n": n,
                            "telfout": telfout or None,
                            "body_lengtes": dict(sorted(e["lengtes"].items(), key=lambda kv: -kv[1])[:4]),
                            "offset_tokens": ot, "match_tokens": round(f(ct), 3),
                            "offset_lamports": os_, "match_lamports": round(f(cs), 3),
                            "offset_mint": om, "match_mint": round(f(cm), 3),
                            "offset_pool": op, "match_pool": round(f(cp), 3),
                            "pool_kandidaten": [{"offset": i, "match": round(f(acct[i]), 3),
                                                 "voorbeelden": (e.get("acct_vb") or {}).get(i) or []} for i in kandidaten],
                            "offset_user": ou, "match_user": round(f(cu), 3),
                            "identificatie": "mint" if via_mint else ("pool" if via_pool else None),
                            "mediane_afwijking_tokens": round(statistics.median(afw), 5) if afw else None,
                            "vastgesteld": bool(vast)}
    return res


def verifieer_pool(rpc, res):
    """Welke kandidaat-offset bevat écht de pool? Een pool is eigendom van het AMM-programma;
    een wallet is eigendom van het systeemprogramma en een tokenaccount van het tokenprogramma.
    Dat vragen we na bij de keten in plaats van de hoogste match te geloven — meerdere offsets
    halen 100% omdat in één event meerdere accounts staan, en dan is 'de hoogste' willekeurig."""
    cache = {}
    for d, v in res["events"].items():
        gekozen = None
        for k in v.get("pool_kandidaten") or []:
            eigenaars = []
            for pk in k["voorbeelden"]:
                if pk not in cache:
                    info = rpc.call("getAccountInfo", [pk, {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0},
                                                            "commitment": "confirmed"}])
                    cache[pk] = ((info or {}).get("value") or {}).get("owner")
                eigenaars.append(cache[pk])
            k["eigenaar_programma"] = sorted({e for e in eigenaars if e})
            k["is_pool"] = bool(eigenaars) and all(e == PUMPSWAP_PROGRAM for e in eigenaars if e)
            if k["is_pool"] and gekozen is None: gekozen = k
        if gekozen is not None:
            v["offset_pool"] = gekozen["offset"]; v["match_pool"] = gekozen["match"]
            v["identificatie"] = "mint" if v.get("identificatie") == "mint" else "pool"
            if v["identificatie"] == "pool":
                v["vastgesteld"] = bool(v["n"] >= MIN_SAMPLES and v["match_tokens"] >= MIN_MATCH
                                        and v["match_lamports"] >= MIN_MATCH and not v.get("telfout"))
        elif v.get("pool_kandidaten"):
            v["pool_onbevestigd"] = True
    return res


def schrijf_layout(res, led=None, now=None):
    """Schrijft data/pumpswap_layout.json alleen voor events die de eis halen. De bot leest
    dit bestand; bestaat het niet, dan leest hij geen AMM-trades in."""
    vast = {d: v for d, v in res["events"].items() if v["vastgesteld"]}
    if not vast:
        return None
    # koop of verkoop: uit de naam als die matcht, anders onbekend -> dan schrijven we niets
    layout = {"programma": PUMPSWAP_PROGRAM, "vastgesteld_ts": time.time(), "bron": sorted({b for v in vast.values() for b in v["bron"]}),
              "events": {}}
    for d, v in vast.items():
        naam = v["naam"]
        if naam not in ("BuyEvent", "SellEvent"): continue
        ident = v.get("identificatie")
        layout["events"][d] = {"naam": naam, "is_buy": naam == "BuyEvent", "bron": v["bron"], "n": v["n"],
                               "offset_tokens": v["offset_tokens"], "offset_lamports": v["offset_lamports"],
                               "offset_mint": v["offset_mint"] if ident == "mint" else None,
                               "offset_pool": v.get("offset_pool") if ident == "pool" else None,
                               "identificatie": ident, "offset_user": v["offset_user"],
                               "match": min(v["match_tokens"], v["match_lamports"],
                                            v["match_mint"] if ident == "mint" else v.get("match_pool", 0))}
    if not layout["events"]: return None
    os.makedirs(os.path.dirname(LAYOUT_PATH) or ".", exist_ok=True)
    with open(LAYOUT_PATH, "w") as f: json.dump(layout, f, indent=1)
    if led is not None:
        for d, v in layout["events"].items():
            led.execute("INSERT OR REPLACE INTO amm_layout VALUES(?,?,?,?,?,?)",
                        (d, v["naam"], ",".join(v["bron"]), v["n"], json.dumps(v), now or time.time()))
        led.commit()
    return layout


# ================================================================ 3. decoder voor de bot
def load_layout(path=None):
    """Geeft de vastgestelde layout of None. Zonder dit bestand leest de bot geen AMM-trades in."""
    try:
        with open(path or LAYOUT_PATH) as f: lay = json.load(f)
    except Exception:
        return None
    ev = lay.get("events") or {}
    if not ev: return None
    for v in ev.values():
        if v.get("offset_tokens") is None or v.get("offset_lamports") is None: return None
        # De bot kan alleen ingesteld worden op een layout die de mint zélf noemt. Noemt het event
        # de pool, dan is de layout wel vastgesteld maar nog niet bruikbaar: de bot weet niet welke
        # pool bij welk token hoort. Dan blijft de ingestie uit tot dat is opgelost.
        if v.get("offset_mint") is None: return None
    return lay


def layout_via_logs(lay):
    """True als minstens één vastgesteld event in de logregels staat; alleen dan kan de
    logstream van de websocket de bedragen zien."""
    return bool(lay) and any("log" in (v.get("bron") or []) for v in lay["events"].values())


def decode_amm_log(line, lay):
    """Geeft (mint, user, is_buy, sol, tokens_raw) uit een 'Program data:'-regel, of None."""
    if not line.startswith("Program data: "): return None
    try: raw = base64.b64decode(line[14:])
    except Exception: return None
    if len(raw) < 16: return None
    e = (lay.get("events") or {}).get(raw[:8].hex())
    if e is None: return None
    body = raw[8:]
    try:
        tok = struct.unpack_from("<Q", body, e["offset_tokens"])[0]
        lam = struct.unpack_from("<Q", body, e["offset_lamports"])[0]
        om = e["offset_mint"]; mint = base58.b58encode(body[om:om + 32]).decode()
        ou = e.get("offset_user"); user = base58.b58encode(body[ou:ou + 32]).decode() if ou is not None else None
    except (struct.error, IndexError, ValueError):
        return None
    if len(mint) < 32 or tok == 0: return None
    return mint, user, bool(e["is_buy"]), lam / 1e9, tok


# ================================================================ rapport
def to_md(rep):
    L = [f"# PumpSwap-dekking — {rep['generated']}", "",
         "Twee vragen: wat gebeurt er met de open SOL ná migratie, en kunnen we de AMM-trades "
         "überhaupt betrouwbaar inlezen. De tweede is een voorwaarde voor de eerste in bedragen.", ""]
    nm = rep.get("na_migratie")
    if nm:
        L += ["## 1. Open posities in gemigreerde tokens", "",
              f"Totaal open (SOL erin min eruit op de curve): **{nm['open_totaal_sol']:.0f} SOL** over {nm['open_posities_totaal']} posities. "
              f"Hiervan gecheckt: {nm['gecheckt_posities']} posities ({nm['gecheckt_kostprijs_sol']:.0f} SOL).", "",
              "| status nu | posities | open SOL |", "|---|---|---|"]
        for s in ("verkocht", "deels_verkocht", "nog_in_bezit"):
            v = nm["per_status"].get(s)
            if v: L.append(f"| {s} | {v['posities']} | {v['kostprijs_sol']:.1f} |")
        L += ["", f"Restwaarde van wat nog in bezit is, tegen de huidige poolprijs: **{nm['restwaarde_nog_in_bezit_sol']:.1f} SOL** "
                  f"tegen {nm['restwaarde_kostprijs_sol']:.1f} SOL kostprijs ({nm['restwaarde_posities']} posities met een goedgekeurde prijs).", ""]
        ps = nm.get("prijs_status") or {}
        if ps:
            L += ["Poolprijzen: " + ", ".join(f"{k}: {v}" for k, v in sorted(ps.items())) +
                  (f". Mediane verhouding met de laatste curveprijs: {nm['mediane_factor_vs_curve']}×."
                   if nm.get("mediane_factor_vs_curve") else "") +
                  " Afgekeurde prijzen tellen niet mee in de restwaarde: de grootste tokenhouder is niet altijd de pool, "
                  "en bij een gewone wallet met veel WSOL rolt er een onzinprijs uit.", ""]
        if nm.get("per_groep"):
            L += ["| groep | status | posities | open SOL |", "|---|---|---|---|"]
            for grp, d in sorted(nm["per_groep"].items()):
                for s, v in sorted(d.items()): L.append(f"| {grp} | {s} | {v['posities']} | {v['kostprijs_sol']:.1f} |")
            L.append("")
        L += [nm["_uitleg"], ""]
    pr = rep.get("probe")
    if pr:
        L += ["## 2. Layout-verificatie van het AMM-programma", "",
              f"Programma `{pr['programma']}`. {pr['transacties_opgehaald']} transacties opgehaald, "
              f"{pr['transacties_met_waarheid']} bruikbaar (één memecoin-mint, bedragen uit pre/post-balansen af te leiden). "
              f"Eis om een layout vast te stellen: match ≥ {pr['eisen']['min_match']:.0%} over ≥ {pr['eisen']['min_samples']} voorbeelden.", "",
              "| discriminator | naam | waar | n | tokens | lamports | mint | pool | user | herkenning | vastgesteld |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for d, v in pr["events"].items():
            f = lambda o, m: "–" if o is None else f"@{o} ({m:.0%})"
            L.append(f"| `{d}` | {v['naam'] or '?'} | {'+'.join(v['bron'])} | {v['n']} | {f(v['offset_tokens'], v['match_tokens'])} | "
                     f"{f(v['offset_lamports'], v['match_lamports'])} | {f(v['offset_mint'], v['match_mint'])} | "
                     f"{f(v.get('offset_pool'), v.get('match_pool', 0))} | {f(v['offset_user'], v['match_user'])} | "
                     f"{v.get('identificatie') or '–'} | {'ja' if v['vastgesteld'] else ('TELFOUT: ' + ','.join(v['telfout']) if v.get('telfout') else 'nee')} |")
        L += ["", "`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). "
                  "Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen "
                  "niet in de logs en is een andere bron nodig.",
              f"Uitgesloten als bewijs: {pr.get('transacties_router_of_meerdere_partijen', 0)} transacties met meer dan twee "
              f"partijen (routers splitsen één order over meerdere legs), en per discriminator de transacties met meer dan "
              f"één event van dat type ({pr.get('transacties_meerdere_events', 0)} transacties). In die gevallen is het netto "
              f"saldoverschil van de transactie niet het bedrag van één event; ze meenemen verlaagt de match zonder dat de "
              f"layout fout is.", ""]
        kand = [(v["naam"] or d, v.get("pool_kandidaten") or []) for d, v in pr["events"].items() if v.get("pool_kandidaten")]
        if kand:
            L += ["**Welke offset is de pool?** In één event staan meerdere accounts, dus meerdere offsets halen 100%. "
                  "De hoogste eruit pakken is willekeurig, dus vragen we bij de keten na wie de eigenaar van het account is: "
                  "een pool is eigendom van het AMM-programma, een wallet van het systeemprogramma.", "",
                  "| event | offset | match | eigenaar-programma | pool |", "|---|---|---|---|---|"]
            for naam, ks in kand:
                for k in ks:
                    eig = ", ".join(e[:8] + "…" for e in (k.get("eigenaar_programma") or [])) or "onbekend"
                    L.append(f"| {naam} | @{k['offset']} | {k['match']:.0%} | {eig} | {'ja' if k.get('is_pool') else 'nee'} |")
            L.append("")
        afw = {v["naam"] or d: v["mediane_afwijking_tokens"] for d, v in pr["events"].items() if v.get("mediane_afwijking_tokens")}
        if afw:
            L += ["Waar de tokens niet matchen, zit de dichtstbijzijnde waarde er mediaan " +
                  ", ".join(f"{n}: {x:.2%}" for n, x in afw.items()) +
                  " naast. Een klein percentage wijst op kosten die het event anders rekent dan de balans; "
                  "een groot percentage op een verkeerd veld.", ""]
        if rep.get("layout"):
            ev = rep["layout"]["events"]
            L += [f"**Layout vastgelegd** in `{LAYOUT_PATH}`: " +
                  ", ".join(f"{v['naam']} (match {v['match']:.0%}, n={v['n']}, herkenning via {v.get('identificatie')})" for v in ev.values()), ""]
            if any(v.get("identificatie") == "pool" for v in ev.values()):
                L += ["De layout klopt, maar het event noemt de **pool** en niet de mint. De bot weet niet welke pool bij "
                      "welk token hoort, dus de ingestie blijft uit tot die koppeling er is. Dat is een volgende stap, "
                      "geen fout in de layout.", ""]
            else:
                L += ["De bot begint AMM-trades in te lezen zodra hij dit bestand ziet.", ""]
        else:
            L += ["**Geen layout vastgelegd**: de eis is niet gehaald. De bot leest dus géén AMM-trades in. "
                  "Dat is opzet: liever geen data dan verkeerd gedecodeerde data.", ""]
    return "\n".join(L) + "\n"


def main():
    wat = sys.argv[1] if len(sys.argv) > 1 else "alles"
    led = open_led()
    if led is None: print(f"ledger-db {LEDGER_DB} bestaat nog niet"); return
    rpc = _ledger().RpcHttp(C.RPC_HTTP, RPS) if (C.HELIUS_API_KEY or os.getenv("RPC_HTTP")) else None
    if rpc is None: print("geen RPC ingesteld"); return
    now = time.time()
    rep = {"generated": iso(now)}
    if wat in ("alles", "na_migratie"):
        n, m = run_na_migratie(led, rpc, now)
        log(f"na-migratie: {n} paren, {m} prijzen")
        rep["na_migratie"] = na_migratie_report(led)
    if wat in ("alles", "probe"):
        bestaat = os.path.exists(LAYOUT_PATH)
        ruw, tellers = run_probe(rpc)
        alles, tot = tel_op(led, ruw, tellers)
        rep["probe"] = verifieer_pool(rpc, beoordeel(alles, tot))
        rep["layout"] = schrijf_layout(rep["probe"], led, now)
        if bestaat and not rep["layout"]:
            with open(LAYOUT_PATH) as f: rep["layout"] = json.load(f)     # eerder vastgesteld: laten staan
    rep["rpc_calls"] = rpc.calls; rep["rpc_errors"] = rpc.errors
    os.makedirs("reports", exist_ok=True)
    with open("reports/pumpswap.json", "w") as f: json.dump(rep, f, indent=1)
    with open("reports/pumpswap.md", "w") as f: f.write(to_md(rep))
    log(f"klaar ({rpc.calls} rpc-calls, {rpc.errors} fouten)")


if __name__ == "__main__":
    main()
