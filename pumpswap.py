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
RPS = float(os.getenv("PUMPSWAP_RPS", 1.0))          # de bot heeft voorrang op dezelfde sleutel

# --- 1. na-migratie-check ---
PAREN_PER_RUN = int(os.getenv("PUMPSWAP_PAREN", 100))    # (wallet, mint)-paren waarvan we het saldo ophalen
MINTS_PRIJS_PER_RUN = int(os.getenv("PUMPSWAP_MINTS", 20))
VERVERSEN_S = 6 * 3600
VERKOCHT_DREMPEL = 0.01      # <= 1% van de gekochte tokens over = eruit
DEELS_DREMPEL = 0.80         # <= 80% over = deels verkocht

# --- 2. probe ---
PROBE_VERSIE = "probe-v4-pool-navragen"
ACCT_VOORBEELDEN = 4     # telwijze; wijzigen = alle tellers en de layout ongeldig
MIN_SAMPLES = int(os.getenv("PUMPSWAP_MIN_SAMPLES", 50))
MIN_MATCH = float(os.getenv("PUMPSWAP_MIN_MATCH", 0.95))
PROBE_TX = int(os.getenv("PUMPSWAP_PROBE_TX", 150))
KANDIDAAT_NAMEN = ["BuyEvent", "SellEvent", "CreatePoolEvent", "DepositEvent", "WithdrawEvent",
                   "CreateConfigEvent", "UpdateAdminEvent", "UpdateFeeConfigEvent", "TradeEvent",
                   "SyncUserVolumeAccumulatorEvent", "CollectCoinCreatorFeeEvent",
                   "SetCoinCreatorEvent", "ExtendAccountEvent", "DisableEvent"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS amm_pos(wallet TEXT, mint TEXT, verwacht_tok INTEGER, saldo_tok INTEGER,
  status TEXT, kostprijs_sol REAL, gecheckt_ts REAL, PRIMARY KEY(wallet, mint));
CREATE TABLE IF NOT EXISTS amm_prijs(mint TEXT PRIMARY KEY, pool TEXT, prijs_sol REAL, tok_in_pool INTEGER,
  wsol_in_pool REAL, gecheckt_ts REAL, curve_prijs REAL, factor REAL, afgekeurd TEXT, route TEXT);
CREATE TABLE IF NOT EXISTS amm_layout(disc TEXT PRIMARY KEY, naam TEXT, bron TEXT, n INTEGER, json TEXT, gecheckt_ts REAL);
CREATE TABLE IF NOT EXISTS amm_probe(disc TEXT PRIMARY KEY, tellers TEXT, bijgewerkt REAL);
CREATE TABLE IF NOT EXISTS amm_probe_meta(k TEXT PRIMARY KEY, v REAL);
CREATE TABLE IF NOT EXISTS amm_paar(pool TEXT, mint TEXT, bekeken_ts REAL, PRIMARY KEY(pool, mint));
CREATE TABLE IF NOT EXISTS amm_poolveld(offset INTEGER PRIMARY KEY, n INTEGER);
CREATE TABLE IF NOT EXISTS amm_pool(mint TEXT PRIMARY KEY, pool TEXT, route TEXT, gecheckt_ts REAL);
CREATE TABLE IF NOT EXISTS amm_prijsijk(mint TEXT PRIMARY KEY, factor REAL, minuten REAL, ts REAL,
  wsol REAL, tok INTEGER, prijs_sol REAL, curve_prijs REAL, curve_sol_netto REAL);
"""


def disc_of(name): return hashlib.sha256(f"event:{name}".encode()).digest()[:8]


def open_led():
    if not os.path.exists(LEDGER_DB): return None
    db = sqlite3.connect(LEDGER_DB)
    db.execute("PRAGMA journal_mode=WAL"); db.executescript(SCHEMA)
    have = {r[1] for r in db.execute("PRAGMA table_info(amm_prijs)")}
    for naam, typ in (("curve_prijs", "REAL"), ("factor", "REAL"), ("afgekeurd", "TEXT"), ("route", "TEXT")):
        if naam not in have: db.execute(f"ALTER TABLE amm_prijs ADD COLUMN {naam} {typ}")
    # zie lotgevallen: CREATE TABLE IF NOT EXISTS migreert een bestaande tabel niet
    have = {r[1] for r in db.execute("PRAGMA table_info(amm_prijsijk)")}
    for naam, typ in (("wsol", "REAL"), ("tok", "INTEGER"), ("prijs_sol", "REAL"),
                      ("curve_prijs", "REAL"), ("curve_sol_netto", "REAL")):
        if naam not in have: db.execute(f"ALTER TABLE amm_prijsijk ADD COLUMN {naam} {typ}")
    # Metingen zonder de losse getallen zijn niet te diagnosticeren, en een gemeten token wordt niet
    # opnieuw opgehaald. Dus die rijen weg: ze komen er volgende run mét onderdelen weer in.
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
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
    if r and r[0] == "prijs-v3-pool-uit-programma": return True
    db.execute("INSERT OR REPLACE INTO amm_meta VALUES('prijs_versie', 'prijs-v3-pool-uit-programma')")
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
POOLS_PER_RUN = int(os.getenv("PUMPSWAP_POOLS", 60))     # poolaccounts waarvan we de inhoud bekijken
# Een net gemigreerd token kan zijn koers nog niet ver bewogen hebben. Bij die tokens hoort de
# poolprijs dus gelijk te zijn aan de laatste curveprijs, en dáár is de route te ijken.
IJK_ZOEK_S = int(os.getenv("PUMPSWAP_IJK_ZOEK", 12 * 3600))   # zo ver terug zoeken we migraties
IJK_VERS_MIN = float(os.getenv("PUMPSWAP_IJK_VERS_MIN", 120))  # alleen migraties jonger dan dit ijken
IJK_MIN = int(os.getenv("PUMPSWAP_IJK_MIN", 20))         # zo veel verse migraties voor een uitspraak
IJK_MARGE = 0.25                                          # mediane afwijking mag hooguit zo groot zijn
IJK_PER_RUN = int(os.getenv("PUMPSWAP_IJK_PER_RUN", 15))
WIJDE_FACTOR = 1e6      # zelfs een geijkte route mag geen onzin doorlaten
MIGRATIE_PER_RUN = int(os.getenv("PUMPSWAP_MIGRATIE", 120))   # gemigreerde tokens die we per run prijzen
MIGRATIE_VERS_S = int(os.getenv("PUMPSWAP_MIGRATIE_VERS", 24 * 3600))  # daarna opnieuw ophalen
MIN_POOLVELD = int(os.getenv("PUMPSWAP_MIN_POOLVELD", 20))   # zo veel pools moeten het eens zijn
MIN_POOLVELD_MATCH = 0.95


def pool_prijs(rpc, mint, curve_prijs=None, stand=None, led=None, geijkt=False):
    """Koers in de AMM-pool, langs de betrouwbare weg als die er is.

    Route 1 (`pool_uit_programma`): de keten vertelt welke pool bij deze mint hoort, via het
    gemeten mint-veld in het poolaccount, en we lezen de twee vaten van die pool. Geen aanname:
    de pool bezit zijn eigen tokenaccounts.

    Route 2 (`grootste_houder`): de oude noodgreep — de grootste tokenhouder is vermoedelijk de
    pool. Die klopt vaak niet (22 van de 44 prijzen werden afgekeurd, en eerder rolde er 26.647 SOL
    restwaarde uit), dus hij wordt alleen gebruikt zolang route 1 niet vaststaat, en het rapport
    zegt per prijs welke route het was.

    In beide gevallen dezelfde controle: de prijs mag niet meer dan MAX_PRIJSFACTOR van de laatste
    curveprijs afwijken. Afgekeurde prijzen worden geteld en niet gebruikt."""
    uit = {"pool": None, "prijs_sol": None, "tok_in_pool": 0, "wsol_in_pool": 0.0,
           "curve_prijs": curve_prijs, "factor": None, "afgekeurd": None, "route": None}

    if (stand or {}).get("vastgesteld"):
        uit["route"] = "pool_uit_programma"
        pool = None
        if led is not None:
            r = led.execute("SELECT pool FROM amm_pool WHERE mint = ?", (mint,)).fetchone()
            pool = r[0] if r else None
        if pool is None:
            pool, reden = mint_naar_pool(rpc, mint, stand)
            if pool is None: uit["afgekeurd"] = reden; return uit
            if led is not None:
                led.execute("INSERT OR REPLACE INTO amm_pool VALUES(?,?,?,?)",
                            (mint, pool, "programma", time.time()))
                led.commit()
        uit["pool"] = pool
        sal = pool_saldi(rpc, pool, mint)
        if sal["mislukt"]: uit["afgekeurd"] = "geen_antwoord"; return uit
        uit["tok_in_pool"], uit["wsol_in_pool"] = sal["tok"], round(sal["wsol"], 4)
    else:
        uit["route"] = "grootste_houder"
        la = rpc.call("getTokenLargestAccounts", [mint, {"commitment": "confirmed"}])
        vals = (la or {}).get("value") or []
        if not vals: uit["afgekeurd"] = "geen_tokenhouders"; return uit
        ta = vals[0]["address"]; uit["tok_in_pool"] = int(vals[0]["amount"])
        info = rpc.call("getAccountInfo", [ta, {"encoding": "jsonParsed", "commitment": "confirmed"}])
        try: owner = info["value"]["data"]["parsed"]["info"]["owner"]
        except Exception: uit["afgekeurd"] = "eigenaar_onbekend"; return uit
        uit["pool"] = owner
        if _ledger().on_curve(owner) is True: uit["afgekeurd"] = "eigenaar_is_gewone_wallet"; return uit
        ws = rpc.call("getTokenAccountsByOwner", [owner, {"mint": WSOL},
                                                 {"encoding": "jsonParsed", "commitment": "confirmed"}])
        wsol = 0.0
        for v in (ws or {}).get("value", []):
            try: wsol += int(v["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"]) / 1e9
            except Exception: pass
        uit["wsol_in_pool"] = round(wsol, 4)

    if uit["tok_in_pool"] <= 0 or uit["wsol_in_pool"] <= 0:
        uit["afgekeurd"] = "geen_wsol_of_tokens"; return uit
    prijs = uit["wsol_in_pool"] / (uit["tok_in_pool"] / 10**C.TOKEN_DECIMALS)
    # Welke afwijking van de laatste curveprijs nog mag, hangt af van wat de grens moet vangen.
    # Bij de oude route ving hij de verkeerde pool: dan is een factor 20 al verdacht. Bij de
    # geijkte route vertelt de keten wélke pool het is, dus die foutsoort is weg — en dan gooit
    # een strenge grens échte koersbewegingen weg (14 van de 20 prijzen op 13 sept 13:34). Daar
    # hoort dus een wijde grens, en alleen als de route ook echt geijkt is.
    grens = WIJDE_FACTOR if (geijkt and uit["route"] == "pool_uit_programma") else MAX_PRIJSFACTOR
    if curve_prijs and curve_prijs > 0:
        uit["factor"] = round(prijs / curve_prijs, 5)
        if not (1 / grens <= uit["factor"] <= grens):
            uit["afgekeurd"] = "prijs_onwaarschijnlijk"; return uit
    uit["prijs_sol"] = prijs
    return uit


# ---------------------------------------------------------------- pool bij mint
# Het AMM-event noemt de pool, niet de mint. Zolang die koppeling er niet is, weet de bot niet welk
# token hij ziet en blijft de ingestie uit — en kunnen we de koers van gemigreerde tokens niet
# opvragen. De koppeling staat in het poolaccount zelf, maar op welke plek is niet bekend. Dus
# meten in plaats van aannemen: van paren (pool, mint) die we uit transacties kennen, zoeken we
# waar de 32 bytes van de mint in het poolaccount staan. Komt dat bij bijna elke pool op dezelfde
# plek uit, dan is dat het veld. Verschilt het, dan is er geen veld en gebeurt er niets.


def poolveld_stand(led):
    """Geeft (offset, n, totaal, datalengte, vastgesteld) voor het mint-veld in het poolaccount."""
    rijen = {int(o): n for o, n in led.execute("SELECT offset, n FROM amm_poolveld")}
    tot = int((led.execute("SELECT v FROM amm_probe_meta WHERE k='poolaccounts_bekeken'").fetchone() or [0])[0])
    lengte = int((led.execute("SELECT v FROM amm_probe_meta WHERE k='poolaccount_lengte'").fetchone() or [0])[0])
    if not rijen or not tot:
        return {"offset": None, "n": 0, "totaal": tot, "lengte": lengte, "vastgesteld": False,
                "reden": f"nog {max(0, MIN_POOLVELD - tot)} poolaccounts te gaan"}
    offset, n = max(rijen.items(), key=lambda kv: kv[1])
    deel = n / tot
    vast = tot >= MIN_POOLVELD and deel >= MIN_POOLVELD_MATCH and lengte > 0
    return {"offset": offset, "n": n, "totaal": tot, "deel": round(deel, 4), "lengte": lengte,
            "kandidaten": dict(sorted(rijen.items())), "vastgesteld": vast,
            "reden": None if vast else (f"nog {MIN_POOLVELD - tot} poolaccounts te gaan" if tot < MIN_POOLVELD
                                        else f"mint staat maar bij {deel:.0%} van de pools op dezelfde plek")}


def ijk_poolveld(rpc, led, per_run=POOLS_PER_RUN):
    """Bekijkt poolaccounts waarvan we de mint kennen en telt waar die mint in de data staat.

    Alleen pools die we nog niet bekeken hebben, en een mislukte call slaat niets op — anders komt
    een 429 als 'mint staat er niet in' in de tellers terecht."""
    paren = led.execute("SELECT pool, mint FROM amm_paar WHERE bekeken_ts IS NULL LIMIT ?", (per_run,)).fetchall()
    gedaan = mislukt = zonder = 0
    for pool, mint in paren:
        if rpc_dood(rpc): log("RPC geblokkeerd: poolveld-ijking afgebroken"); break
        info = rpc.call("getAccountInfo", [pool, {"encoding": "base64", "commitment": "confirmed"}])
        v = (info or {}).get("value")
        if info is None:
            mislukt += 1; continue                  # geen antwoord: niets opslaan, volgende run opnieuw
        if not v:
            led.execute("UPDATE amm_paar SET bekeken_ts=? WHERE pool=? AND mint=?", (time.time(), pool, mint))
            zonder += 1; continue                   # pool bestaat niet meer
        try: data = base64.b64decode(v["data"][0])
        except Exception:
            mislukt += 1; continue
        offsets = zoek_pubkey(data, mint)
        for i in offsets:
            led.execute("INSERT INTO amm_poolveld VALUES(?,1) ON CONFLICT(offset) DO UPDATE SET n = n + 1", (i,))
        led.execute("INSERT INTO amm_probe_meta VALUES('poolaccounts_bekeken',1) "
                    "ON CONFLICT(k) DO UPDATE SET v = v + 1")
        led.execute("INSERT OR REPLACE INTO amm_probe_meta VALUES('poolaccount_lengte',?)", (len(data),))
        led.execute("UPDATE amm_paar SET bekeken_ts=? WHERE pool=? AND mint=?", (time.time(), pool, mint))
        if not offsets: zonder += 1
        gedaan += 1
    led.commit()
    return {"bekeken": gedaan, "mislukt": mislukt, "zonder_mint": zonder, "te_gaan":
            led.execute("SELECT count(*) FROM amm_paar WHERE bekeken_ts IS NULL").fetchone()[0]}


def mint_naar_pool(rpc, mint, stand):
    """Vraagt de keten welke pool bij deze mint hoort, via het gemeten mint-veld. Geeft None als
    het veld niet is vastgesteld of als het endpoint getProgramAccounts niet serveert."""
    if not stand.get("vastgesteld"): return None, "veld_niet_vastgesteld"
    res = rpc.call("getProgramAccounts", [PUMPSWAP_PROGRAM, {
        "encoding": "base64", "dataSlice": {"offset": 0, "length": 0}, "commitment": "confirmed",
        "filters": [{"dataSize": stand["lengte"]},
                    {"memcmp": {"offset": stand["offset"], "bytes": mint}}]}])
    if res is None: return None, "geen_antwoord"
    if not res: return None, "geen_pool_gevonden"
    if len(res) > 1: return None, "meerdere_pools"          # niet gokken welke
    return res[0]["pubkey"], None


def pool_saldi(rpc, pool, mint):
    """De twee vaten van de pool, elk apart opgevraagd op mint. Geen aanname over de layout van het
    poolaccount en geen 'grootste houder' — de pool bezit zijn eigen tokenaccounts."""
    uit = {"tok": 0, "wsol": 0.0, "mislukt": False}
    for sleutel, m, deler in (("tok", mint, 1), ("wsol", WSOL, 1e9)):
        r = rpc.call("getTokenAccountsByOwner", [pool, {"mint": m},
                                                 {"encoding": "jsonParsed", "commitment": "confirmed"}])
        if r is None: uit["mislukt"] = True; return uit
        som = 0
        for a in (r or {}).get("value", []):
            try: som += int(a["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"])
            except Exception: pass
        uit[sleutel] = som if deler == 1 else som / deler
    return uit


def curve_sol_netto(led, mint):
    """Hoeveel SOL er volgens onze eigen curve-trades netto in dit token is gegaan. Bij een
    gemigreerd token hoort dat bedrag (min de migratiekosten) in de pool te zitten — een
    onafhankelijke maat voor of we het juiste WSOL-vat lezen."""
    try:
        r = led.execute("SELECT SUM(sol_in - sol_out) FROM wt WHERE mint = ?", (mint,)).fetchone()
        return round(r[0], 4) if r and r[0] is not None else None
    except sqlite3.Error:
        return None


def poolprijs_stand(led):
    """Is de geijkte route geijkt? Bij tokens die net gemigreerd zijn hoort de poolprijs gelijk te
    zijn aan de laatste curveprijs. Klopt dat bij genoeg van die tokens, dan leest de route de
    juiste vaten en mag hij ook koersen ver van de curveprijs opleveren."""
    rijen = [(f, m) for f, m in led.execute(
        "SELECT factor, minuten FROM amm_prijsijk WHERE factor IS NOT NULL AND minuten <= ?", (IJK_VERS_MIN,))]
    n = len(rijen)
    if n < IJK_MIN:
        return {"n": n, "geijkt": False,
                "reden": f"nog {IJK_MIN - n} migraties van minder dan {IJK_VERS_MIN:.0f} minuten oud te gaan"}
    afw = sorted(abs(f - 1) for f, _ in rijen)
    med = statistics.median(afw)
    return {"n": n, "mediane_afwijking": round(med, 4), "mediane_minuten": round(statistics.median(m for _, m in rijen), 1),
            "geijkt": med <= IJK_MARGE,
            "reden": None if med <= IJK_MARGE else f"mediane afwijking {med:.0%} boven {IJK_MARGE:.0%}"}


def ijk_poolprijs(led, rpc, now, stand, main=None, per_run=IJK_PER_RUN):
    """Prijst net gemigreerde tokens en legt de verhouding met de curveprijs vast.

    De migratietijd en de laatste curveprijs komen uit de bot-database, niet uit de ledger: die
    laatste rekent tokens pas door als ze twee uur oud zijn, dus daar staat een migratie van een uur
    geleden nog niet in. In de run van 13 sept 15:04 leverde dat 0 kandidaten op.

    We zoeken ruim terug (IJK_ZOEK_S) maar leggen per token vast hoeveel minuten na de migratie de
    meting is gedaan; het oordeel in poolprijs_stand gebruikt alleen de verse."""
    if not (stand or {}).get("vastgesteld"): return {"nieuw": 0, "reden": "poolveld niet vastgesteld"}
    if main is None: return {"nieuw": 0, "reden": "bot-database niet open"}
    gedaan = {m for m, in led.execute("SELECT mint FROM amm_prijsijk")}
    rijen = [(m, lp, mts) for m, lp, mts in main.execute(
        """SELECT mint, last_price, migrated_ts FROM tokens
           WHERE migrated_ts IS NOT NULL AND migrated_ts > ? AND last_price > 0
           ORDER BY migrated_ts DESC""", (now - IJK_ZOEK_S,)) if m not in gedaan]
    nieuw = 0
    for mint, cp, mts in rijen[:per_run]:
        if rpc_dood(rpc): break
        pp = pool_prijs(rpc, mint, cp, stand=stand, led=led, geijkt=True)   # wijde grens: we meten juist
        if pp.get("afgekeurd") in ("geen_antwoord", "veld_niet_vastgesteld"): continue
        # De onderdelen erbij, niet alleen de verhouding. De ijking zakte op 13 sept 17:44 met een
        # mediane afwijking van 99% — een factor rond 50, en dat is te systematisch voor koers. Of
        # de SOL in de pool klopt niet, of de curveprijs, en dat is alleen te zien door de losse
        # getallen naast elkaar te leggen. curve_sol_netto is wat er volgens onze eigen trades op de
        # curve is ingelegd: dat hoort ruwweg in de pool te zitten.
        led.execute("INSERT OR REPLACE INTO amm_prijsijk VALUES(?,?,?,?,?,?,?,?,?)",
                    (mint, pp.get("factor"), round((now - mts) / 60, 1), now,
                     pp.get("wsol_in_pool"), pp.get("tok_in_pool"), pp.get("prijs_sol"), cp,
                     curve_sol_netto(led, mint)))
        nieuw += 1
    led.commit()
    return {"nieuw": nieuw, "kandidaten": len(rijen)}


def prijs_gemigreerd(led, rpc, now, stand, geijkt, main, per_run=MIGRATIE_PER_RUN):
    """Koers van vandaag voor gemigreerde tokens, zodat de afloopanalyse ze niet hoeft over te slaan.

    Die 1081 gemigreerde tokens zijn juist de groep die het goed deed; zolang hun koers ontbreekt is
    elk cijfer over vasthouden een ondergrens. De bron is de bot-database: migrated_ts wordt daar
    direct weggeschreven en last_price staat in SOL per heel token — dezelfde eenheid als de
    poolprijs, dus de verhouding is direct te vergelijken."""
    if not (stand or {}).get("vastgesteld"): return {"gedaan": 0, "reden": "poolveld niet vastgesteld"}
    if main is None: return {"gedaan": 0, "reden": "bot-database niet open"}
    vers = {m for m, in led.execute("SELECT mint FROM amm_prijs WHERE gecheckt_ts > ?", (now - MIGRATIE_VERS_S,))}
    kand = [(m, lp) for m, lp in main.execute(
        """SELECT mint, last_price FROM tokens
           WHERE migrated_ts IS NOT NULL AND ath_price IS NOT NULL AND last_price > 0
           ORDER BY migrated_ts DESC""") if m not in vers]
    gedaan = mislukt = 0
    for mint, cp in kand[:per_run]:
        if rpc_dood(rpc): log("RPC geblokkeerd: gemigreerde prijzen afgebroken"); break
        pp = pool_prijs(rpc, mint, cp, stand=stand, led=led, geijkt=geijkt)
        if pp.get("afgekeurd") == "geen_antwoord":
            mislukt += 1; continue                    # niets opslaan: volgende run opnieuw
        led.execute("INSERT OR REPLACE INTO amm_prijs VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (mint, pp["pool"], pp["prijs_sol"], pp["tok_in_pool"], pp["wsol_in_pool"], now,
                     pp["curve_prijs"], pp["factor"], pp["afgekeurd"], pp["route"]))
        gedaan += 1
        if gedaan % 25 == 0: led.commit()
    led.commit()
    return {"gedaan": gedaan, "mislukt": mislukt, "te_gaan": max(0, len(kand) - gedaan)}


def factor_spreiding(led):
    """Verdeling van de verhouding poolprijs/curveprijs per route — als diagnose, niet als filter."""
    uit = {}
    for route, in led.execute("SELECT DISTINCT COALESCE(route,'onbekend') FROM amm_prijs"):
        fs = sorted(r[0] for r in led.execute(
            "SELECT factor FROM amm_prijs WHERE factor IS NOT NULL AND COALESCE(route,'onbekend') = ?", (route,)))
        if not fs: continue
        uit[route] = {"n": len(fs), "p10": round(fs[len(fs) // 10], 5), "mediaan": round(statistics.median(fs), 5),
                      "p90": round(fs[min(len(fs) - 1, 9 * len(fs) // 10)], 5)}
    return uit


def rpc_dood(rpc, minimaal=8):
    """True als de eerste `minimaal` calls van deze run allemaal mislukten: dan is de sleutel
    geblokkeerd (429) en heeft doorgaan geen zin — het kost alleen maar calls die de bot ook nodig heeft."""
    calls, errors = getattr(rpc, "calls", 0), getattr(rpc, "errors", 0)
    return calls >= minimaal and errors >= calls


def run_na_migratie(led, rpc, now, stand=None, geijkt=False):
    paren = kandidaat_paren(led, now, PAREN_PER_RUN)
    log(f"na-migratie: {len(paren)} paren te checken")
    gedaan = 0
    for wallet, mint, verwacht, kost, _ in paren:
        if rpc_dood(rpc): log("RPC geblokkeerd: na-migratie afgebroken"); break
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
        if rpc_dood(rpc): log("RPC geblokkeerd: prijzen afgebroken"); break
        # laatste curveprijs in SOL per heel token, als referentie voor de plausibiliteitscheck
        cp = ((v_sol / 1e9) / (v_tok / 10**C.TOKEN_DECIMALS)) if (v_sol and v_tok) else None
        pp = pool_prijs(rpc, mint, cp, stand=stand, led=led, geijkt=geijkt)
        if pp is None: continue
        led.execute("INSERT OR REPLACE INTO amm_prijs VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (mint, pp["pool"], pp["prijs_sol"], pp["tok_in_pool"], pp["wsol_in_pool"], now,
                     pp["curve_prijs"], pp["factor"], pp["afgekeurd"], pp["route"]))
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


def run_probe(rpc, n_tx=PROBE_TX, led=None, lay=None):
    sigs = rpc.call("getSignaturesForAddress", [PUMPSWAP_PROGRAM, {"limit": min(1000, n_tx * 2), "commitment": "confirmed"}]) or []
    sigs = [s["signature"] for s in sigs if not s.get("err")][:n_tx]
    log(f"probe: {len(sigs)} transacties ophalen")
    per_disc = defaultdict(lambda: {"bron": set(), "n": 0, "tok": defaultdict(int), "sol": defaultdict(int),
                                    "mint": defaultdict(int), "user": defaultdict(int), "acct": defaultdict(int),
                                    "lengtes": defaultdict(int), "afw": defaultdict(list), "acct_vb": defaultdict(list)})
    n_tx_ok = n_waarheid = n_multi = n_router = 0
    for sig in sigs:
        if rpc_dood(rpc): log("RPC geblokkeerd: probe afgebroken"); break
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
            # (pool, mint) vastleggen zodra de layout een pool-offset heeft: die paren zijn de
            # ijkpunten voor het mint-veld in het poolaccount.
            if led is not None and lay:
                e_lay = (lay.get("events") or {}).get(d)
                off = (e_lay or {}).get("offset_pool")
                if off is not None and len(body) >= off + 32:
                    pool58 = base58.b58encode(body[off:off + 32]).decode()
                    led.execute("INSERT OR IGNORE INTO amm_paar VALUES(?,?,NULL)", (pool58, w["mint"]))
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
    if led is not None: led.commit()
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
                if rpc_dood(rpc): cache[pk] = None; continue
                if pk not in cache:
                    info = rpc.call("getAccountInfo", [pk, {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0},
                                                            "commitment": "confirmed"}])
                    cache[pk] = ((info or {}).get("value") or {}).get("owner")
                eigenaars.append(cache[pk])
            k["eigenaar_programma"] = sorted({e for e in eigenaars if e})
            k["opzoekingen_mislukt"] = sum(1 for e in eigenaars if e is None)
            # Fail-closed: élke opzoeking moet gelukt zijn én het AMM-programma opleveren. In de run van
            # 19:24 (alle RPC-calls 429) werden alle zes kandidaten 'pool' omdat all() over niets True is.
            k["is_pool"] = bool(eigenaars) and all(e == PUMPSWAP_PROGRAM for e in eigenaars)
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
def lees_layout_bestand(path=None):
    """De layout zoals hij op schijf staat, ook als hij voor de bot nog niet bruikbaar is. Nodig om
    (pool, mint)-paren te kunnen verzamelen: daarvoor is alleen de pool-offset nodig."""
    try:
        with open(path or LAYOUT_PATH) as f: return json.load(f)
    except Exception:
        return None


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
    pv = rep.get("poolveld")
    if pv:
        run = pv.get("run") or {}
        L += ["## 3. Welke pool hoort bij welk token?", "",
              "Het event noemt de pool. Waar in het poolaccount de mint staat, is niet gedocumenteerd, dus meten we "
              "het: van paren (pool, mint) die uit transacties bekend zijn, zoeken we waar de 32 bytes van de mint in "
              "de accountdata staan. Komt dat bij minstens "
              f"{MIN_POOLVELD} pools op dezelfde plek uit ({MIN_POOLVELD_MATCH:.0%} van de gevallen), dan is dat het "
              "veld. Zo niet, dan gebeurt er niets — een gegokt veld levert de koers van een willekeurig token op.", ""]
        if pv.get("vastgesteld"):
            L += [f"**Veld vastgesteld op offset {pv['offset']}** ({pv['n']} van {pv['totaal']} pools, "
                  f"{pv['deel']:.0%}; accountlengte {pv['lengte']} bytes). Daarmee vraagt de analyse bij de keten op "
                  "welke pool bij een mint hoort, en leest daarna de twee vaten van die pool. Dat vervangt de oude "
                  "noodgreep 'de grootste tokenhouder is vermoedelijk de pool'.", ""]
        else:
            L += [f"**Nog niet vastgesteld**: {pv.get('reden')}. "
                  f"({pv.get('totaal', 0)} pools bekeken.) Zolang dit niet staat, wordt de koers via de oude route "
                  "bepaald en staat er per prijs bij dat het die route was.", ""]
        if pv.get("kandidaten"):
            L += ["| offset | pools waar de mint daar staat |", "|---|---|"]
            for o, n in sorted(pv["kandidaten"].items(), key=lambda kv: -kv[1])[:8]:
                L.append(f"| @{o} | {n} |")
            L.append("")
        L += [f"Deze run: {run.get('bekeken', 0)} poolaccounts bekeken, {run.get('mislukt', 0)} calls mislukt "
              f"(niet opgeslagen, volgende keer opnieuw), {run.get('zonder_mint', 0)} zonder mint in de data, "
              f"{run.get('te_gaan', 0)} paren te gaan.", ""]
        pi = rep.get("prijsijk") or {}
        if pi:
            L += ["**Is die route ook geijkt?** Een token dat net gemigreerd is kan zijn koers nog niet ver bewogen "
                  "hebben, dus daar hóórt de poolprijs gelijk te zijn aan de laatste curveprijs. Dat is de enige plek "
                  "waar deze route te controleren valt zonder AMM-trades.", ""]
            if pi.get("geijkt"):
                L += [f"**Geijkt**: bij {pi['n']} tokens die mediaan {pi.get('mediane_minuten')} minuten eerder "
                      f"migreerden wijkt de poolprijs mediaan {pi['mediane_afwijking']:.1%} van de curveprijs af "
                      f"(marge {IJK_MARGE:.0%}). Daarmee is de grens op koersbewegingen losgelaten: een gemigreerd "
                      "token mag ook 100× onder zijn curveprijs staan, want dat is dan koers en geen leesfout.", ""]
            else:
                L += [f"**Nog niet geijkt**: {pi.get('reden')} ({pi['n']} migraties jonger dan "
                      f"{IJK_VERS_MIN:.0f} minuten gemeten, {(pi.get('run') or {}).get('kandidaten', 0)} kandidaten "
                      f"in de laatste {IJK_ZOEK_S // 3600} uur). Zolang dit niet "
                      f"staat, wordt elke prijs die meer dan {MAX_PRIJSFACTOR:.0f}× van de curveprijs afwijkt "
                      "afgekeurd — streng, maar zonder ijking is er geen reden die grens te verruimen.", ""]
        db = rep.get("prijsijk_onderdelen") or []
        if db:
            L += ["", "De losse getallen van de laatste metingen, zodat te zien is welke kant er scheef staat. "
                  "`SOL in pool` is het WSOL-vat van de pool; `SOL uit curve` is wat er volgens onze eigen trades "
                  "op de curve is ingelegd — die twee horen op de migratiekosten na gelijk te zijn.", "",
                  "| min. na migratie | SOL in pool | SOL uit curve | tokens in pool | poolprijs | curveprijs | verhouding |",
                  "|---|---|---|---|---|---|---|"]
            for r in db:
                L.append(f"| {r['minuten']} | {r['wsol']} | {r['curve_sol_netto']} | "
                         f"{(r['tok'] or 0) / 1e6:,.0f} | {r['prijs_sol']} | {r['curve_prijs']} | {r['factor']} |")
            L.append("")
        fs = rep.get("factor_spreiding") or {}
        if fs:
            L += ["| route | prijzen | p10 | mediaan | p90 | (poolprijs ÷ laatste curveprijs)", "|---|---|---|---|---|---|"]
            for r, v in sorted(fs.items()):
                L.append(f"| {r} | {v['n']} | {v['p10']} | {v['mediaan']} | {v['p90']} | |")
            L.append("")
        gm = rep.get("gemigreerd_geprijsd") or {}
        if gm:
            L += [f"Koersen van gemigreerde tokens opgehaald voor de afloopanalyse: {gm.get('gedaan', 0)} deze run, "
                  f"{gm.get('te_gaan', 0)} te gaan, {gm.get('mislukt', 0)} calls mislukt"
                  + (f" — {gm['reden']}" if gm.get("reden") else "") + ".", ""]
        rt = rep.get("prijs_routes") or {}
        if rt:
            L += ["Koersen per route: " + ", ".join(f"{k}: {v}" for k, v in sorted(rt.items())), ""]
    return "\n".join(L) + "\n"


def main():
    wat = sys.argv[1] if len(sys.argv) > 1 else "alles"
    led = open_led()
    if led is None: print(f"ledger-db {LEDGER_DB} bestaat nog niet"); return
    try: main_db = sqlite3.connect(f"file:{C.DB_PATH}?mode=ro", uri=True, timeout=60)
    except Exception: main_db = None
    rpc = _ledger().RpcHttp(C.RPC_HTTP, RPS) if (C.HELIUS_API_KEY or os.getenv("RPC_HTTP")) else None
    if rpc is None: print("geen RPC ingesteld"); return
    now = time.time()
    rep = {"generated": iso(now)}
    # Volgorde met opzet: eerst de layout (die levert de pool-offset), dan de pool-mint-koppeling,
    # en pas daarna de prijzen — want die hebben die koppeling nodig om de juiste pool te vinden.
    if wat in ("alles", "probe"):
        bestaat = os.path.exists(LAYOUT_PATH)
        ruw, tellers = run_probe(rpc, led=led, lay=lees_layout_bestand())
        alles, tot = tel_op(led, ruw, tellers)
        rep["probe"] = verifieer_pool(rpc, beoordeel(alles, tot))
        rep["layout"] = schrijf_layout(rep["probe"], led, now)
        if bestaat and not rep["layout"]:
            with open(LAYOUT_PATH) as f: rep["layout"] = json.load(f)     # eerder vastgesteld: laten staan
    if wat in ("alles", "probe", "poolveld"):
        werk = ijk_poolveld(rpc, led)
        stand = poolveld_stand(led)
        rep["poolveld"] = {**stand, "run": werk}
        log(f"poolveld: {werk['bekeken']} pools bekeken, {werk['te_gaan']} te gaan -> "
            f"{'vastgesteld @' + str(stand['offset']) if stand['vastgesteld'] else stand['reden']}")
    if wat in ("alles", "probe", "poolveld"):
        # ijken vóór prijzen: de grens die een prijs afkeurt hangt ervan af of de route geijkt is
        rep["prijsijk"] = {**poolprijs_stand(led),
                           "run": ijk_poolprijs(led, rpc, now, poolveld_stand(led), main=main_db)}
        st = rep["prijsijk"]
        log(f"prijsijk: n={st['n']} -> {'geijkt' if st['geijkt'] else st.get('reden')}")
    if wat in ("alles", "na_migratie"):
        st_pool, st_prijs = poolveld_stand(led), poolprijs_stand(led)
        n, m = run_na_migratie(led, rpc, now, stand=st_pool, geijkt=st_prijs["geijkt"])
        log(f"na-migratie: {n} paren, {m} prijzen")
        rep["gemigreerd_geprijsd"] = prijs_gemigreerd(led, rpc, now, st_pool, st_prijs["geijkt"], main_db)
        g = rep["gemigreerd_geprijsd"]
        log(f"gemigreerde koersen: {g.get('gedaan', 0)} gedaan, {g.get('te_gaan', 0)} te gaan"
            + (f" ({g['reden']})" if g.get("reden") else ""))
        rep["na_migratie"] = na_migratie_report(led)
    rep["prijsijk_onderdelen"] = [
        {"minuten": m, "wsol": w, "tok": t, "prijs_sol": p, "curve_prijs": c, "curve_sol_netto": n, "factor": f}
        for m, w, t, p, c, n, f in led.execute(
            """SELECT minuten, wsol, tok, prijs_sol, curve_prijs, curve_sol_netto, factor FROM amm_prijsijk
               WHERE wsol IS NOT NULL ORDER BY minuten ASC LIMIT 10""")]
    rep["factor_spreiding"] = factor_spreiding(led)
    rep["prijs_routes"] = dict(led.execute(
        "SELECT COALESCE(route,'onbekend') || '/' || COALESCE(afgekeurd,'goedgekeurd'), COUNT(*) FROM amm_prijs GROUP BY 1"))
    rep["rpc_calls"] = rpc.calls; rep["rpc_errors"] = rpc.errors
    os.makedirs("reports", exist_ok=True)
    with open("reports/pumpswap.json", "w") as f: json.dump(rep, f, indent=1)
    with open("reports/pumpswap.md", "w") as f: f.write(to_md(rep))
    log(f"klaar ({rpc.calls} rpc-calls, {rpc.errors} fouten)")


if __name__ == "__main__":
    main()
