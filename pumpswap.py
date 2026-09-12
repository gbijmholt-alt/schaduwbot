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
import base64, hashlib, json, os, sqlite3, struct, sys, time
from collections import defaultdict

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
MIN_SAMPLES = int(os.getenv("PUMPSWAP_MIN_SAMPLES", 50))
MIN_MATCH = float(os.getenv("PUMPSWAP_MIN_MATCH", 0.95))
PROBE_TX = int(os.getenv("PUMPSWAP_PROBE_TX", 120))
KANDIDAAT_NAMEN = ["BuyEvent", "SellEvent", "CreatePoolEvent", "DepositEvent", "WithdrawEvent",
                   "CreateConfigEvent", "UpdateAdminEvent", "UpdateFeeConfigEvent", "TradeEvent",
                   "SyncUserVolumeAccumulatorEvent", "CollectCoinCreatorFeeEvent",
                   "SetCoinCreatorEvent", "ExtendAccountEvent", "DisableEvent"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS amm_pos(wallet TEXT, mint TEXT, verwacht_tok INTEGER, saldo_tok INTEGER,
  status TEXT, kostprijs_sol REAL, gecheckt_ts REAL, PRIMARY KEY(wallet, mint));
CREATE TABLE IF NOT EXISTS amm_prijs(mint TEXT PRIMARY KEY, pool TEXT, prijs_sol REAL, tok_in_pool INTEGER,
  wsol_in_pool REAL, gecheckt_ts REAL);
CREATE TABLE IF NOT EXISTS amm_layout(disc TEXT PRIMARY KEY, naam TEXT, bron TEXT, n INTEGER, json TEXT, gecheckt_ts REAL);
"""


def disc_of(name): return hashlib.sha256(f"event:{name}".encode()).digest()[:8]


def open_led():
    if not os.path.exists(LEDGER_DB): return None
    db = sqlite3.connect(LEDGER_DB)
    db.execute("PRAGMA journal_mode=WAL"); db.executescript(SCHEMA); db.commit()
    return db


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


def pool_prijs(rpc, mint):
    """Grootste tokenaccount -> eigenaar (de pool) -> WSOL-saldo van die pool. Geen aanname
    over welk programma de pool beheert; we lezen alleen twee saldi."""
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
    if tok <= 0 or wsol <= 0: return {"pool": owner, "prijs_sol": None, "tok_in_pool": tok, "wsol_in_pool": round(wsol, 4)}
    return {"pool": owner, "prijs_sol": wsol / (tok / 10**C.TOKEN_DECIMALS), "tok_in_pool": tok, "wsol_in_pool": round(wsol, 4)}


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
    mints = [r[0] for r in led.execute("""SELECT p.mint FROM amm_pos p LEFT JOIN amm_prijs q ON q.mint = p.mint
        WHERE p.status != 'verkocht' AND (q.gecheckt_ts IS NULL OR q.gecheckt_ts < ?)
        GROUP BY p.mint ORDER BY SUM(p.kostprijs_sol) DESC LIMIT ?""", (now - VERVERSEN_S, MINTS_PRIJS_PER_RUN))]
    for mint in mints:
        pp = pool_prijs(rpc, mint)
        if pp is None: continue
        led.execute("INSERT OR REPLACE INTO amm_prijs VALUES(?,?,?,?,?,?)",
                    (mint, pp["pool"], pp["prijs_sol"], pp["tok_in_pool"], pp["wsol_in_pool"], now))
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
        WHERE p.status != 'verkocht' AND q.prijs_sol IS NOT NULL""").fetchone()
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


def waarheid_uit_tx(tx):
    """Wat wisselde er werkelijk van eigenaar? Geeft (mint, tok_delta_raw, lamports, eigenaar) of None."""
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
    # de handelaar: grootste absolute tokenverandering die niet de pool is (pool heeft tegengesteld teken bij WSOL)
    kand = sorted(per_mint[mint].items(), key=lambda kv: -abs(kv[1]))
    if not kand: return None
    eigenaar, tok_delta = kand[0]
    lam = 0
    if WSOL in per_mint:
        w = sorted(per_mint[WSOL].items(), key=lambda kv: -abs(kv[1]))
        lam = abs(w[0][1]) if w else 0
    if lam == 0:      # geen WSOL-account: native saldoverandering van de ondertekenaar
        keys = [k if isinstance(k, str) else k.get("pubkey") for k in
                ((tx.get("transaction") or {}).get("message") or {}).get("accountKeys") or []]
        pb, qb = meta.get("preBalances") or [], meta.get("postBalances") or []
        if keys and pb and qb: lam = abs((qb[0] - pb[0]) + (meta.get("fee") or 0))
    if abs(tok_delta) == 0 or lam == 0: return None
    return mint, abs(tok_delta), lam, eigenaar


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
                                    "mint": defaultdict(int), "user": defaultdict(int), "lengtes": defaultdict(int)})
    n_tx_ok = n_waarheid = 0
    for sig in sigs:
        tx = rpc.call("getTransaction", [sig, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0, "commitment": "confirmed"}])
        if not tx: continue
        n_tx_ok += 1
        w = waarheid_uit_tx(tx)
        if w is None: continue
        n_waarheid += 1
        mint, tok, lam, eigenaar = w
        for bron, blob in blobs_uit_tx(tx):
            if len(blob) < 16: continue
            d = blob[:8].hex(); body = blob[8:]
            e = per_disc[d]; e["bron"].add(bron); e["n"] += 1; e["lengtes"][len(body)] += 1
            for i in zoek_offsets(body, tok): e["tok"][i] += 1
            for i in zoek_offsets(body, lam): e["sol"][i] += 1
            for i in zoek_pubkey(body, mint): e["mint"][i] += 1
            for i in zoek_pubkey(body, eigenaar): e["user"][i] += 1
    naam_van = {disc_of(n).hex(): n for n in KANDIDAAT_NAMEN}
    res = {"transacties_opgehaald": n_tx_ok, "transacties_met_waarheid": n_waarheid, "programma": PUMPSWAP_PROGRAM,
           "eisen": {"min_samples": MIN_SAMPLES, "min_match": MIN_MATCH}, "events": {}}
    for d, e in sorted(per_disc.items(), key=lambda kv: -kv[1]["n"]):
        n = e["n"]
        best = lambda dd: (max(dd.items(), key=lambda kv: kv[1]) if dd else (None, 0))
        ot, ct = best(e["tok"]); os_, cs = best(e["sol"]); om, cm = best(e["mint"]); ou, cu = best(e["user"])
        vast = (n >= MIN_SAMPLES and ct / n >= MIN_MATCH and cs / n >= MIN_MATCH and cm / n >= MIN_MATCH)
        res["events"][d] = {"naam": naam_van.get(d), "bron": sorted(e["bron"]), "n": n,
                            "body_lengtes": dict(sorted(e["lengtes"].items(), key=lambda kv: -kv[1])[:4]),
                            "offset_tokens": ot, "match_tokens": round(ct / n, 3) if n else 0,
                            "offset_lamports": os_, "match_lamports": round(cs / n, 3) if n else 0,
                            "offset_mint": om, "match_mint": round(cm / n, 3) if n else 0,
                            "offset_user": ou, "match_user": round(cu / n, 3) if n else 0,
                            "vastgesteld": bool(vast)}
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
        layout["events"][d] = {"naam": naam, "is_buy": naam == "BuyEvent", "bron": v["bron"], "n": v["n"],
                               "offset_tokens": v["offset_tokens"], "offset_lamports": v["offset_lamports"],
                               "offset_mint": v["offset_mint"], "offset_user": v["offset_user"],
                               "match": min(v["match_tokens"], v["match_lamports"], v["match_mint"])}
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
        if v.get("offset_tokens") is None or v.get("offset_lamports") is None or v.get("offset_mint") is None: return None
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
                  f"tegen {nm['restwaarde_kostprijs_sol']:.1f} SOL kostprijs ({nm['restwaarde_posities']} posities met prijs).", ""]
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
              "| discriminator | naam | waar | n | tokens | lamports | mint | user | vastgesteld |", "|---|---|---|---|---|---|---|---|---|"]
        for d, v in pr["events"].items():
            f = lambda o, m: "–" if o is None else f"@{o} ({m:.0%})"
            L.append(f"| `{d}` | {v['naam'] or '?'} | {'+'.join(v['bron'])} | {v['n']} | {f(v['offset_tokens'], v['match_tokens'])} | "
                     f"{f(v['offset_lamports'], v['match_lamports'])} | {f(v['offset_mint'], v['match_mint'])} | "
                     f"{f(v['offset_user'], v['match_user'])} | {'ja' if v['vastgesteld'] else 'nee'} |")
        L += ["", "`waar` = log (`Program data:`) of inner_cpi (`emit_cpi!`, in een binnenste instructie). "
                  "Dat verschil bepaalt of de bot dit via de logstream kan meelezen: bij inner_cpi staan de bedragen "
                  "niet in de logs en is een andere bron nodig.", ""]
        if rep.get("layout"):
            L += [f"**Layout vastgelegd** in `{LAYOUT_PATH}`: " +
                  ", ".join(f"{v['naam']} (match {v['match']:.0%}, n={v['n']})" for v in rep["layout"]["events"].values()) +
                  ". De bot begint AMM-trades in te lezen zodra hij dit bestand ziet.", ""]
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
        rep["probe"] = run_probe(rpc)
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
