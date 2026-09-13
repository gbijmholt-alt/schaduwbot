#!/usr/bin/env python3
"""Wat is er van de tokens terechtgekomen?

Alle andere analyses kijken naar een raampje van hooguit een uur rond de instap. Deze kijkt naar
de afloop: welke tokens bestaan nog, welke zijn dood, welke zijn gerugd, welke zijn gemigreerd —
en of de screening uit de video dat voorspelt. Plus, voor de tokens die álle criteria haalden:
wat is hun koers nú, en wat had simpelweg kopen-en-vasthouden opgeleverd.

Twee bronnen, en het verschil is belangrijk:
 - Wat wij zagen: de bot logt trades tot ~6 uur na creatie. Daarna weten we niets meer.
 - Wat er nu is: opgehaald bij de keten. Voor tokens die nog op de curve staan is de koers af te
   leiden uit het saldo van de curve. Voor gemigreerde tokens niet: hun koers staat in een
   AMM-pool, en die layout is nog niet bevestigd. Die groep krijgt dus geen koers in plaats van
   een gegokte koers — en omdat het juist de tokens zijn die het goed deden, is alles wat hier
   over vasthouden staat een ondergrens.

De afgeleide koers wordt eerst gecontroleerd tegen wat we zelf zagen, bij tokens waar die twee
elkaar moeten overlappen. Klopt dat niet, dan wordt de koers niet gebruikt. Zonder die controle
is een prijs uit de keten net zo goed een gok als de restwaarde van 26.647 SOL van gisteren.

Gebruik:  python lotgevallen.py [--db ...] [--ledger ...] [--out reports]
"""
import argparse, json, math, os, sqlite3, statistics, time

import config as C

DOOD_NA_S = 6 * 3600            # geen trades meer sinds zoveel: dood op de curve
RUG_DALING = 0.80               # koers >= 80% onder de top: gerugd
KETEN_PER_RUN = int(os.getenv("LOT_KETEN", 400))    # tokens waarvan we de koers nú ophalen
KETEN_RPS = float(os.getenv("LOT_RPS", 2.0))
IJK_PUNTEN = 120                # dode tokens die als ijkpunt dienen; meer voegt niets toe
VERS_S = 12 * 3600              # koers van een nog actief token ouder dan dit: opnieuw ophalen
CONTROLE_MIN = 20               # minder controlepunten dan dit: koers niet gebruiken
CONTROLE_MARGE = 0.25           # afgeleide koers mag max 25% afwijken van wat we zelf zagen

# De bot slaat ath_price op in SOL per heel token; wij rekenen overal in lamports per raw token
# (v_sol/v_tok), want dat is wat in de events staat. Dat verschilt een factor 10^(9-6) = 1000.
# Dit is op 13 sept fout gegaan: de top werd met de koers van nu vergeleken zonder omrekening,
# waardoor vasthouden +60.000% leek en bijna geen token als 'gerugd' werd geteld. Één plek voor
# de omrekening, één test erop.
PRIJS_FACTOR = 10 ** (9 - C.TOKEN_DECIMALS)

# Verandert deze versie, dan worden opgeslagen ketenantwoorden weggegooid en opnieuw opgehaald.
# Nodig omdat de vorige versie mislukte calls als 'curve is weg' opsloeg: die rijen zijn niet meer
# te onderscheiden van een echt verdwenen curve, dus ze moeten er allemaal uit.
LOT_VERSIE = "lot-v2-foutonderscheid"

SCHEMA = """
CREATE TABLE IF NOT EXISTS lot(mint TEXT PRIMARY KEY, status TEXT, keten_prijs REAL, keten_bron TEXT,
  gecheckt_ts REAL, afwijking REAL, lamports INTEGER, tokens INTEGER);
"""

# CREATE TABLE IF NOT EXISTS laat een bestaande tabel ongemoeid, ook als het schema is uitgebreid.
# Dat is in dit project nu drie keer misgegaan (ledger, pumpswap, en hier op 13 sept 09:09 met
# "no such column: lamports"). Vandaar deze helper: na executescript altijd langs zorg_kolommen.
KOLOMMEN = {"lot": [("keten_prijs", "REAL"), ("keten_bron", "TEXT"), ("gecheckt_ts", "REAL"),
                    ("afwijking", "REAL"), ("lamports", "INTEGER"), ("tokens", "INTEGER")]}


def wis_bij_nieuwe_versie(db, versie=LOT_VERSIE):
    """Gooit opgehaalde ketenantwoorden weg als de versie is veranderd. Geen 'waarschijnlijk nog
    goed' — een antwoord uit een versie met een bekende fout is geen antwoord."""
    db.execute("CREATE TABLE IF NOT EXISTS lot_versie(k TEXT PRIMARY KEY, v TEXT)")
    r = db.execute("SELECT v FROM lot_versie WHERE k='keten'").fetchone()
    if r and r[0] == versie: return 0
    n = db.execute("SELECT count(*) FROM lot").fetchone()[0]
    db.execute("DELETE FROM lot")
    db.execute("INSERT OR REPLACE INTO lot_versie VALUES('keten',?)", (versie,))
    db.commit()
    return n


def zorg_kolommen(db, kolommen=None):
    """Voegt ontbrekende kolommen toe aan bestaande tabellen. Veilig om altijd te draaien."""
    for tabel, cols in (kolommen or KOLOMMEN).items():
        have = {r[1] for r in db.execute(f"PRAGMA table_info({tabel})")}
        if not have: continue                     # tabel bestaat nog niet: executescript maakt hem
        for naam, typ in cols:
            if naam not in have: db.execute(f"ALTER TABLE {tabel} ADD COLUMN {naam} {typ}")
    db.commit()


def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None
def prijs(vs, vt): return (vs / vt) if vt else 0.0


def ci95(xs):
    n = len(xs)
    if n < 2: return None
    m = sum(xs) / n; h = 1.96 * statistics.pstdev(xs) / math.sqrt(n)
    return [round(m - h, 4), round(m + h, 4)]


def samenvat(xs, naam="rendement"):
    if not xs: return {"n": 0}
    return {"n": len(xs), "mediaan": round(statistics.median(xs), 4), "gemiddeld": round(sum(xs) / len(xs), 4),
            "ci95": ci95(xs), "aandeel_positief": round(sum(1 for x in xs if x > 0) / len(xs), 3),
            "aandeel_min90": round(sum(1 for x in xs if x <= -0.9) / len(xs), 3)}


# --------------------------------------------------------------------------- 1. status per token
def lees_tokens(main, led, now):
    """Geeft per token: creatie, screeningniveau, laatste waargenomen koers en top, status."""
    scr = {}
    for m, created, mig, sp, sj, xl, bc in main.execute(
            "SELECT mint, created_ts, migrated_ts, screen_pass, screen_json, has_x_link, bonding_curve FROM tokens WHERE created_ts IS NOT NULL"):
        j = {}
        try: j = json.loads(sj) if sj else {}
        except Exception: pass
        scr[m] = {"created_ts": created, "migrated_ts": mig, "screen_pass": sp, "bonding_curve": bc,
                  "gescreend": sj is not None,
                  "houders_ok": bool(j.get("houders_gecheckt")) and not (j.get("check1a_flag") or j.get("check1b_flag")),
                  "fs": bool(j.get("fs")), "x": xl}
    uit = {}
    for m, created, mig, last_ts, vs, vt, n_tr, gap in led.execute(
            "SELECT mint, created_ts, migrated_ts, last_ts, v_sol, v_tok, n_trades, gap FROM token WHERE created_ts IS NOT NULL"):
        s = scr.get(m)
        if s is None or gap: continue
        p_nu = prijs(vs or 0, vt or 0)
        uit[m] = {**s, "mint": m, "migrated_ts": mig or s["migrated_ts"], "last_ts": last_ts, "n_trades": n_tr,
                  "v_sol": vs, "v_tok": vt, "laatste_prijs": p_nu}
    return uit


def status_van(t, ath, now):
    """gemigreerd / dood op de curve / nog actief — en die drie sluiten elkaar uit.

    'Gerugd' zat hier eerst tússen, en dat was fout op twee manieren: een token dat zowel gerugd
    als stil is werd alleen als gerugd geteld (waardoor 'dood op de curve' van 82% naar 44% zakte
    zonder dat er iets veranderd was), en de gerugde tokens vielen buiten de koersberekening omdat
    die op de status 'dood' keek. Gerugd is geen afloop maar een eigenschap van de koers, dus het
    is nu een aparte, overlappende kolom."""
    if t["migrated_ts"]: return "gemigreerd"
    if t["last_ts"] and t["last_ts"] < now - DOOD_NA_S: return "dood_op_curve"
    return "nog_actief"


def is_gerugd(t, ath):
    p = t["laatste_prijs"]
    return bool(ath and p and p <= ath * (1 - RUG_DALING))


# --------------------------------------------------------------------------- 2. koers nu, met controle
# Een mislukte call en een leeg account zijn twee verschillende dingen. Dat stond eerst op één
# hoop (beide None), waardoor 35 van de 296 mislukte calls als 'curve is weg' in de database
# belandden — en daar nooit meer uit kwamen, want een weggeschreven antwoord wordt niet opnieuw
# opgehaald. Vandaar dit onderscheid.
FOUT = object()


class Rpc:
    def __init__(self, url, rps, pogingen=2):
        self.url, self.gap, self.last, self.calls, self.errors = url, 1.0 / rps, 0.0, 0, 0
        self.pogingen = pogingen

    def call(self, method, params):
        import urllib.request
        body = json.dumps({"jsonrpc": "2.0", "id": self.calls + 1, "method": method, "params": params}).encode()
        for poging in range(self.pogingen):
            w = self.last + self.gap - time.time()
            if w > 0: time.sleep(w)
            self.last = time.time(); self.calls += 1
            try:
                req = urllib.request.Request(self.url, data=body, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=20) as r: j = json.loads(r.read().decode())
                if "error" not in j: return j.get("result")
            except Exception:
                pass
            self.errors += 1
            if poging + 1 < self.pogingen: time.sleep(1.0)      # publiek endpoint begrenst hard
        return FOUT


def curve_staat(rpc, mint, bonding_curve):
    """Hoeveel SOL en hoeveel tokens houdt de bonding curve nú aan?

    Twee basismethodes die het publieke endpoint wél serveert — de bot doet er duizenden per uur
    met bijna geen fouten. `getTokenLargestAccounts` werkt er niet (8 van 8 mislukt op 13 sept
    08:17), dus die route is verlaten.

    Geeft None als het curve-account weg is (doorgaans: gemigreerd) en FOUT als de keten geen
    antwoord gaf. Dat tweede mag niet als antwoord worden opgeslagen."""
    acc = rpc.call("getAccountInfo", [bonding_curve, {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0},
                                                      "commitment": "confirmed"}])
    if acc is FOUT: return FOUT
    v = (acc or {}).get("value")
    if not v: return None
    lam = v.get("lamports", 0)
    res = rpc.call("getTokenAccountsByOwner", [bonding_curve, {"mint": mint},
                                               {"encoding": "jsonParsed", "commitment": "confirmed"}])
    if res is FOUT: return FOUT
    tok = 0
    for a in (res or {}).get("value", []):
        try: tok += int(a["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"])
        except Exception: pass
    if tok <= 0: return None
    return {"lamports": lam, "tokens": tok}


def ijk_virtueel(paren):
    """De koers op de curve rekent met vìrtuele reserves: v_sol = vaste startwaarde + de SOL die
    er echt in zit. Die startwaarde gokken we niet — we meten hem.

    Bij een token dat dood op de curve staat is er sinds onze laatste waarneming niet meer
    gehandeld. De v_sol die wij toen in het event zagen hoort dan exact gelijk te zijn aan
    startwaarde + de lamports die er nu in zitten. Het verschil is dus de startwaarde, en als die
    bij alle tokens hetzelfde is, klopt het model. Varieert hij, dan deugt de aanname niet en
    gebruiken we de koers niet.

    paren: [(v_sol_toen, lamports_nu)]. Geeft de gemeten startwaarde en of hij bruikbaar is."""
    offsets = [vs - lam for vs, lam in paren if vs and lam is not None]
    if len(offsets) < CONTROLE_MIN:
        return {"n": len(offsets), "bruikbaar": False, "reden": f"minder dan {CONTROLE_MIN} controlepunten"}
    med = statistics.median(offsets)
    if med <= 0: return {"n": len(offsets), "bruikbaar": False, "reden": "gemeten startwaarde is niet positief"}
    afw = [abs(o / med - 1) for o in offsets]
    spreiding = statistics.median(afw)
    return {"n": len(offsets), "virtuele_sol": round(med / 1e9, 4), "mediane_spreiding": round(spreiding, 4),
            "bruikbaar": spreiding <= 0.02,
            "reden": None if spreiding <= 0.02 else f"startwaarde varieert ({spreiding:.1%}), model klopt niet"}


def prijs_uit_curve(staat, virtuele_sol_lam, v_tok_start):
    """Koers nu, in dezelfde eenheid als wat we zelf zagen: lamports per raw token, dus v_sol/v_tok.

    De eerste versie gaf SOL per heel token en dat is een factor 1000 anders. De controle ving dat
    op — hij weigerde de koers — maar een controle is geen excuus voor een verkeerde eenheid."""
    v_sol = virtuele_sol_lam + staat["lamports"]
    v_tok = v_tok_start - (C.INITIAL_REAL_TOKEN_RESERVES - staat["tokens"])
    if v_tok <= 0: return None
    return v_sol / v_tok


def controleer(paren):
    """paren: [(waargenomen, afgeleid)] voor tokens waar beide horen te kloppen (dood op de curve,
    dus de koers kan sinds onze laatste waarneming niet meer bewogen zijn). Geeft de mediane
    afwijking en of de afgeleide koers bruikbaar is."""
    afw = [abs(a / w - 1) for w, a in paren if w and a and w > 0]
    if len(afw) < CONTROLE_MIN:
        return {"n": len(afw), "bruikbaar": False, "reden": f"minder dan {CONTROLE_MIN} controlepunten"}
    med = statistics.median(afw)
    return {"n": len(afw), "mediane_afwijking": round(med, 4), "bruikbaar": med <= CONTROLE_MARGE,
            "reden": None if med <= CONTROLE_MARGE else f"mediane afwijking {med:.0%} boven {CONTROLE_MARGE:.0%}"}


def koers_nu(t, prijzen, bruikbaar):
    """De koers van vandaag, of niets — met de reden erbij. Nooit stilzwijgend terugvallen op een
    oude waarneming: voor een nog actief token is die simpelweg geen koers van nu."""
    if not bruikbaar: return None, "nog_niet_opgehaald"
    if t["status"] == "gemigreerd": return None, "gemigreerd_geen_koers"
    p = prijzen.get(t["mint"])
    if p: return p, "keten"
    # Stil op de curve: er is sinds onze laatste waarneming niet gehandeld, dus die waarneming ís de
    # koers van nu. Dit keek eerst op de status 'dood_op_curve', en toen 'gerugd' die status
    # overschreef vielen 1617 tokens hier stilletjes uit.
    if t["status"] == "dood_op_curve" and t.get("laatste_prijs"): return t["laatste_prijs"], "stil_onveranderd"
    return None, "nog_niet_opgehaald"


# --------------------------------------------------------------------------- 3. rapport
# De niveaus zijn genest: alles onder 'gescreend' is een deelverzameling daarvan. Dat is met opzet.
# 'Alle tokens' bevat ook de tienduizenden die nooit de $7k haalden en dus nooit gescreend zijn;
# die vergelijken met een gescreende groep meet vooral dat filter, niet de checks uit de video.
# De eerlijke vergelijking is 'houdercheck ok' tegen 'houdercheck gezakt', beide binnen 'gescreend'.
NIVEAUS = [
    ("alle tokens", lambda t: True),
    ("gescreend (ongeacht uitkomst)", lambda t: t["gescreend"]),
    ("gescreend, houdercheck ok", lambda t: t["gescreend"] and t["houders_ok"]),
    ("gescreend, houdercheck gezakt", lambda t: t["gescreend"] and not t["houders_ok"]),
    ("volledige screening gehaald", lambda t: t["screen_pass"] == 1),
    ("volledige screening gezakt", lambda t: t["gescreend"] and t["screen_pass"] != 1),
    ("volledige screening + X-link", lambda t: t["screen_pass"] == 1 and t["x"]),
]
STATUSSEN = ["gemigreerd", "nog_actief", "dood_op_curve"]


def bouw(main, led, lot, rpc, now, ath_van):
    toks = lees_tokens(main, led, now)
    for m, t in toks.items():
        t["ath"] = ath_van.get(m)
        t["status"] = status_van(t, t["ath"], now)
        t["gerugd"] = is_gerugd(t, t["ath"])
    rep = {"gegenereerd": iso(now), "tokens": len(toks), "per_niveau": {}}

    # --- verdeling van de afloop per screeningniveau ---
    for naam, fn in NIVEAUS:
        sub = [t for t in toks.values() if fn(t)]
        if not sub: continue
        n = len(sub)
        rij = {"tokens": n}
        for st in STATUSSEN:
            k = sum(1 for t in sub if t["status"] == st)
            rij[st] = {"n": k, "aandeel": round(k / n, 4)}
        # overlappend met de statussen hierboven, met opzet: een token kan gerugd én stil zijn
        g = sum(1 for t in sub if t["gerugd"])
        rij["gerugd"] = {"n": g, "aandeel": round(g / n, 4)}
        rep["per_niveau"][naam] = rij

    # --- staat van de curve nu: eerst ijken op dode tokens, dan pas prijzen ---
    # Volgorde met opzet. Eerst de dode tokens: daar weten we wat eruit moet komen, dus daar is het
    # model te ijken. Daarna de tokens waar de koers wél bewogen kan zijn sinds onze laatste
    # waarneming — en daarvan eerst die de volledige screening haalden, want dat is de groep
    # waarover de vraag gaat. Gemigreerde tokens vragen we niet op: hun curve is leeg en hun koers
    # staat in een AMM-pool die we nog niet betrouwbaar kunnen uitlezen.
    dood = [m for m, t in toks.items() if t["status"] == "dood_op_curve" and t.get("bonding_curve") and t.get("v_sol")]
    actief = [m for m, t in toks.items() if t["status"] == "nog_actief" and t.get("bonding_curve") and t.get("ath")]
    # gerugde tokens zitten hier gewoon in of niet, afhankelijk van of er nog gehandeld wordt; de
    # rug-kolom bepaalt dat niet meer
    volgorde = dood[:IJK_PUNTEN] + [m for m in actief if toks[m]["screen_pass"] == 1] \
                                 + [m for m in actief if toks[m]["screen_pass"] != 1]
    # Een eerder opgehaalde koers blijft geldig zolang er niet gehandeld kan zijn. Bij een dood
    # token is dat altijd; bij een nog actief token maar een beperkte tijd, anders noemen we een
    # koers van twee dagen oud 'de koers van nu'.
    gecheckt = {m: ts for m, ts in lot.execute("SELECT mint, gecheckt_ts FROM lot WHERE gecheckt_ts IS NOT NULL")}

    def vers(m):
        ts = gecheckt.get(m)
        if ts is None: return False
        if toks.get(m, {}).get("status") == "nog_actief": return (now - ts) <= VERS_S
        return True

    te_doen = [m for m in volgorde if not vers(m)][:KETEN_PER_RUN]
    mislukt = 0
    if rpc is not None:
        for i, m in enumerate(te_doen):
            if rpc.calls >= 8 and rpc.errors >= rpc.calls:
                log("keten onbereikbaar, gestopt"); break
            st = curve_staat(rpc, m, toks[m]["bonding_curve"])
            if st is FOUT:
                mislukt += 1; continue            # niets opslaan: volgende run opnieuw proberen
            rij = (m, toks[m]["status"], None, "curve_weg", now, None, None, None) if st is None else \
                  (m, toks[m]["status"], None, "curve", now, None, st["lamports"], st["tokens"])
            lot.execute("INSERT OR REPLACE INTO lot VALUES(?,?,?,?,?,?,?,?)", rij)
            gecheckt[m] = now
            if i % 20 == 0: lot.commit()
        lot.commit()
    gedaan = {m: (lm, tk) for m, lm, tk in
              lot.execute("SELECT mint, lamports, tokens FROM lot WHERE lamports IS NOT NULL")}

    # --- ijking: bij dode tokens moet v_sol(toen) - lamports(nu) een vaste startwaarde geven ---
    paren = [(toks[m]["v_sol"], gedaan[m][0]) for m in gedaan
             if m in toks and toks[m]["status"] == "dood_op_curve" and toks[m].get("v_sol")]
    rep["ijking"] = ijk_virtueel(paren)
    prijzen, verouderd = {}, 0
    if rep["ijking"].get("bruikbaar"):
        vlam = int(rep["ijking"]["virtuele_sol"] * 1e9)
        v_tok_start = C.TOTAL_SUPPLY_RAW * 1073 // 1000        # virtuele tokenreserve bij start
        for m, (lam, tk) in gedaan.items():
            if lam is None or tk is None: continue
            if not vers(m): verouderd += 1; continue           # koers te oud voor een actief token
            p = prijs_uit_curve({"lamports": lam, "tokens": tk}, vlam, v_tok_start)
            if p: prijzen[m] = p
        # tweede controle: bij dode tokens moet de afgeleide koers gelijk zijn aan wat we zagen
        rep["koerscontrole"] = controleer([(toks[m]["laatste_prijs"], prijzen[m]) for m in prijzen
                                           if toks[m]["status"] == "dood_op_curve" and toks[m]["laatste_prijs"]])
    else:
        rep["koerscontrole"] = {"n": 0, "bruikbaar": False, "reden": "ijking mislukt: " + str(rep["ijking"].get("reden"))}

    # --- wat had vasthouden opgeleverd? ---
    # Drie soorten tokens, en ze verdienen geen gemeenschappelijk getal:
    #  - gemigreerd: curve leeg, koers in een AMM-pool die we nog niet betrouwbaar uitlezen. Geen
    #    koers. Dat zijn juist de tokens die het goed deden, dus wat hieronder staat mist de
    #    winnaars en is daarmee een ondergrens, geen schatting.
    #  - nog actief: koers moet uit de keten komen, want er is sindsdien gehandeld.
    #  - dood op de curve: er is niets meer gehandeld, dus onze laatste waarneming ís de koers van
    #    nu. Dat is geen aanname: de ijking meet bij deze tokens dat het SOL-saldo van de curve
    #    onveranderd is.
    rep["vasthouden"] = {}
    bruikbaar = rep["koerscontrole"].get("bruikbaar")
    for naam, fn in NIVEAUS:
        sub = [t for t in toks.values() if fn(t) and t.get("ath")]
        if not sub: continue
        vanaf_top, vanaf_dip, bron = [], [], {"keten": 0, "stil_onveranderd": 0,
                                              "gemigreerd_geen_koers": 0, "nog_niet_opgehaald": 0}
        for t in sub:
            nu, b = koers_nu(t, prijzen, bruikbaar)
            bron[b] += 1
            if nu is None: continue
            vanaf_top.append(nu / t["ath"] - 1)
            vanaf_dip.append(nu / (t["ath"] * (1 - 0.45)) - 1)     # instap op een 45%-dip
        rep["vasthouden"][naam] = {"met_ath": len(sub), "bronnen": bron,
                                   "vanaf_de_top": samenvat(vanaf_top), "vanaf_45pct_dip": samenvat(vanaf_dip)}
    rep["keten"] = {"opgehaald": len(gedaan), "deze_run": len(te_doen), "geprijsd": len(prijzen),
                    "mislukt": mislukt,
                    "verouderd": verouderd, "nog_te_doen": sum(1 for m in volgorde if not vers(m)),
                    "rpc_calls": getattr(rpc, "calls", 0), "rpc_fouten": getattr(rpc, "errors", 0)}
    return rep, toks


def to_md(rep):
    L = [f"# Wat is er van de tokens geworden? — {rep['gegenereerd']}", "",
         f"{rep['tokens']} tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de "
         "instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades "
         f"meer sinds ≥ {DOOD_NA_S // 3600} uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het "
         "token handelt verder op een AMM — dat is wat de video als doel beschrijft.", "",
         "## Afloop per screeningniveau", "",
         "De eerste drie kolommen sluiten elkaar uit en tellen op tot 100%. 'Gerugd' staat daar los van: "
         "een token kan zowel gerugd als stil zijn, en die twee door elkaar halen verlaagde eerder het "
         "aandeel 'dood op de curve' van 82% naar 44% zonder dat er iets veranderd was.", "",
         "| niveau | tokens | gemigreerd | nog actief | dood op curve | waarvan gerugd |", "|---|---|---|---|---|---|"]
    for naam, rij in rep["per_niveau"].items():
        L.append(f"| {naam} | {rij['tokens']} | " + " | ".join(
            f"{rij[st]['aandeel']:.1%} ({rij[st]['n']})" for st in STATUSSEN)
            + f" | {rij['gerugd']['aandeel']:.1%} ({rij['gerugd']['n']}) |")
    ij = rep.get("ijking") or {}
    L += ["", "## Controle op de koers uit de keten", ""]
    if ij.get("n"):
        if ij.get("bruikbaar"):
            L.append(f"**IJking geslaagd.** Bij {ij['n']} dode curve-tokens is gemeten hoeveel virtuele SOL de curve "
                     f"bij de start meetelt: **{ij['virtuele_sol']:.2f} SOL**, met een spreiding van "
                     f"{ij['mediane_spreiding']:.1%} tussen tokens. Die waarde is dus niet aangenomen maar gemeten, "
                     "en omdat hij bij alle tokens hetzelfde uitkomt klopt het model.")
        else:
            L.append(f"**IJking mislukt** ({ij['n']} punten): {ij.get('reden')}. De koers van vandaag wordt daarom "
                     "niet berekend.")
        L.append("")
    kc = rep.get("koerscontrole") or {}
    if kc.get("bruikbaar"):
        L.append(f"Bij {kc['n']} dode curve-tokens — waar de koers sinds onze laatste waarneming niet meer bewogen "
                 f"kán zijn — wijkt de uit de keten afgeleide koers mediaan **{kc['mediane_afwijking']:.1%}** af. "
                 f"Binnen de marge van {CONTROLE_MARGE:.0%}, dus de koers wordt gebruikt.")
    else:
        L.append(f"**De koers uit de keten wordt niet gebruikt**: {kc.get('reden', 'onbekend')} "
                 f"({kc.get('n', 0)} controlepunten). De cijfers hieronder gebruiken de laatste koers die wij zelf "
                 "zagen, en dat is hooguit 6 uur na creatie — dus geen uitspraak over vandaag.")
    vh = rep.get("vasthouden") or {}
    if vh:
        L += ["", "## Wat had kopen-en-vasthouden opgeleverd?", "",
              "Niet scalpen maar houden, tot vandaag. Instap op een dip van 45% vanaf de top — het moment uit de "
              "video — en nooit verkopen. De koers van vandaag komt uit de keten; bij tokens die dood op de curve "
              "staan is onze laatste waarneming de koers van nu, want het SOL-saldo van de curve is onveranderd.",
              "",
              "**Gemigreerde tokens zitten er niet in.** Hun curve is leeg en hun koers staat in een AMM-pool die we "
              "nog niet betrouwbaar uitlezen. Dat is juist de groep die het goed deed, dus deze cijfers zijn een "
              "ondergrens en geen schatting van wat vasthouden opbrengt.", "",
              "| niveau | tokens met top | koers bekend | gemigreerd (geen koers) | nog op te halen | mediaan vanaf 45%-dip | mediaan vanaf de top | aandeel positief | aandeel ≤ −90% |",
              "|---|---|---|---|---|---|---|---|---|"]
        for naam, v in vh.items():
            d, tp, b = v["vanaf_45pct_dip"], v["vanaf_de_top"], v["bronnen"]
            if not d.get("n"):
                L.append(f"| {naam} | {v['met_ath']} | 0 | {b['gemigreerd_geen_koers']} | "
                         f"{b['nog_niet_opgehaald']} | – | – | – | – |")
                continue
            L.append(f"| {naam} | {v['met_ath']} | {d['n']} | {b['gemigreerd_geen_koers']} | "
                     f"{b['nog_niet_opgehaald']} | {d['mediaan']:+.1%} | {tp['mediaan']:+.1%} | "
                     f"{d['aandeel_positief']:.0%} | {d['aandeel_min90']:.0%} |")
        L += ["", "'Tokens met top' is kleiner dan het aantal tokens in de tabel hierboven: de bot legt een "
                  "hoogste koers alleen vast voor tokens die hij actief volgde."]
    k = rep.get("keten") or {}
    L += ["", f"Koersen uit de keten: {k.get('geprijsd', 0)} bruikbaar, {k.get('opgehaald', 0)} opgehaald, "
              f"{k.get('nog_te_doen', 0)} nog te gaan ({k.get('deze_run', 0)} deze run, "
              f"{k.get('rpc_calls', 0)} calls, {k.get('rpc_fouten', 0)} mislukte calls, "
              f"{k.get('mislukt', 0)} tokens overgeslagen en volgende keer opnieuw). De analyse draait elke 2 uur.", ""]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH)
    ap.add_argument("--ledger", default=os.path.join(os.path.dirname(C.DB_PATH) or ".", "ledger.sqlite"))
    ap.add_argument("--out", default=C.REPORT_DIR); ap.add_argument("--now", type=float, default=None)
    ap.add_argument("--geen-rpc", action="store_true")
    args = ap.parse_args()
    now = args.now or time.time(); t0 = time.time()
    os.makedirs(args.out, exist_ok=True)
    if not os.path.exists(args.ledger):
        with open(os.path.join(args.out, "lotgevallen.md"), "w") as f: f.write("# Afloop van de tokens\n\nLedger bestaat nog niet.\n")
        return
    main_db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=60)
    led = sqlite3.connect(args.ledger, timeout=60); led.executescript(SCHEMA); zorg_kolommen(led)
    gewist = wis_bij_nieuwe_versie(led)
    if gewist: log(f"nieuwe versie {LOT_VERSIE}: {gewist} opgeslagen ketenantwoorden weggegooid")
    # hoogste koers per token: uit de replay-tabel als die er is, anders uit de bot-tabel
    # Eén bron voor de top, en dus één eenheid. De replay-tabel bevat geen ath (alleen ath_mult),
    # dus die route leverde nooit iets op en zou bij hergebruik een tweede eenheid binnenhalen.
    ath = {}
    for m, a in main_db.execute("SELECT mint, ath_price FROM tokens WHERE ath_price IS NOT NULL"):
        ath.setdefault(m, a * PRIJS_FACTOR)      # SOL per heel token -> lamports per raw token
    rpc = None if args.geen_rpc else Rpc(C.RPC_HTTP, KETEN_RPS)
    rep, _ = bouw(main_db, led, led, rpc, now, ath)
    with open(os.path.join(args.out, "lotgevallen.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "lotgevallen.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s -> {args.out}/lotgevallen.md")


if __name__ == "__main__":
    main()
