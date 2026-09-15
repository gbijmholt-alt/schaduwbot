#!/usr/bin/env python3
"""Zijn afgeleide tokens van een lopend token beter dan willekeurige nieuwe tokens?

Aanleiding: een KOL-video van 14 sept beschrijft de 'vamp'. Er loopt een token (hij noemt Joe op
$500k), iemand ontdekt dat er een fout in zit — verkeerde naam, verkeerde ticker, verkeerde foto —
en lanceert de gecorrigeerde versie (Bella). Die afgeleide zou de plek van het origineel overnemen.
Hij toont één winnende trade en geen enkel basisgetal.

Wat hier gemeten wordt is de zwakkere, mechanische versie van die claim: presteren tokens die kort
na het doorbreken van een ander token met een sterk lijkende naam of ticker worden gelanceerd, beter
dan tokens die in dezelfde uren zijn gelanceerd? 'Er zit een fout in de naam en die corrigeer ik' is
een oordeel en geen meting; dat deel kan een bot niet vaststellen. Valt de zwakke versie negatief
uit, dan is daarmee niet bewezen dat de scherpe versie ook niet werkt — wel dat het effect dan
volledig in dat oordeel moet zitten, en niet in het verschijnsel 'afgeleide van een loper'.

Deze analyse is verkennend: hij kijkt naar data die er al ligt. Komt er iets uit, dan moet het
vooraf vastgelegd en op nieuwe tokens getoetst worden, net als H2, H3 en H4.

Gebruik:  python vamp.py [--db ...] [--out reports]
"""
import argparse, difflib, json, math, os, re, sqlite3, statistics, time
from collections import Counter, defaultdict

import config as C

VENSTER_S = int(os.getenv("VAMP_VENSTER", 2 * 3600))   # afgeleide moet zo snel na de loper komen
LOPER_DEEL = float(os.getenv("VAMP_LOPER", 0.5))       # loper = koers boven dit deel van de voltooiingsprijs
GELIJKENIS = float(os.getenv("VAMP_GELIJK", 0.80))     # naamgelijkenis vanaf hier telt als afgeleide
MIN_TEKENS = 3                                          # tickers korter dan dit geven toevalstreffers
GENERIEK_VANAF = int(os.getenv("VAMP_GENERIEK", 200))  # ticker die zo vaak voorkomt is geen identiteit
TWEE_X = 2.0
TIEN_X = 10.0


def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None


def voltooiingsprijs():
    """De koers waarop een token de curve verlaat, in SOL per heel token. Zie pumpswap.py: dit is
    geen meting maar een constante, en hij komt tot tien cijfers overeen met wat de bot waarneemt."""
    v_tok_start = C.TOTAL_SUPPLY_RAW * 1073 // 1000
    v_tok_eind = v_tok_start - C.INITIAL_REAL_TOKEN_RESERVES
    v_sol_eind = 30 * 10**9 * v_tok_start // v_tok_eind
    return (v_sol_eind / 1e9) / (v_tok_eind / 10**C.TOKEN_DECIMALS)


VOLTOOIINGSPRIJS = voltooiingsprijs()


# ------------------------------------------------------------------ 1. namen vergelijken
def norm(s):
    """Kleine letters, alleen letters en cijfers. '$BELLA ' en 'bella' worden hetzelfde."""
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def woorden(s):
    return [w for w in re.split(r"[^a-z0-9]+", (s or "").lower()) if w]


def lijkt(loper, kandidaat):
    """Is `kandidaat` een afgeleide van `loper`? Geeft de reden, of None.

    Drie mechanische regels, in volgorde van hardheid. Bewust géén losse substring-match: 'bel' in
    'bella' zou half de dataset koppelen. De ticker moet minstens MIN_TEKENS lang zijn, anders
    matcht 'AI' op alles."""
    lt, kt = norm(loper["symbol"]), norm(kandidaat["symbol"])
    ln, kn = norm(loper["name"]), norm(kandidaat["name"])
    if len(lt) >= MIN_TEKENS and lt == kt: return "zelfde_ticker"
    # naam van de een als heel woord in de ander
    lw, kw = set(woorden(loper["name"])), set(woorden(kandidaat["name"]))
    gedeeld = {w for w in lw & kw if len(w) >= MIN_TEKENS}
    if gedeeld: return "gedeeld_woord"
    if len(lt) >= MIN_TEKENS and (lt in kw or kt in lw): return "ticker_in_naam"
    if len(ln) >= MIN_TEKENS and len(kn) >= MIN_TEKENS:
        if difflib.SequenceMatcher(None, ln, kn).ratio() >= GELIJKENIS: return "gelijkende_naam"
    return None


# ------------------------------------------------------------------ 2. lopers en afgeleiden
def lees_tokens(db):
    uit = {}
    for m, naam, sym, cre, mig, ath, launch, last in db.execute(
            """SELECT mint, name, symbol, created_ts, migrated_ts, ath_price, launch_price, last_price
               FROM tokens WHERE created_ts IS NOT NULL"""):
        uit[m] = {"mint": m, "name": naam or "", "symbol": sym or "", "created_ts": cre,
                  "migrated_ts": mig, "ath": ath, "launch": launch, "last": last}
    return uit


def loper_momenten(db, toks, drempel):
    """Wanneer werd een token zichtbaar groot? Het eerste moment dat de koers boven de drempel komt,
    of het moment van migratie als dat eerder is.

    Grens die je moet kennen: boven de curve zien we niets meer. Een token dat op de AMM naar $500k
    loopt — het geval uit de video — is voor ons alleen zichtbaar tot het de curve verlaat, rond
    410 SOL marktkap. We meten dus 'afgeleide van een token dat de top van de curve haalde', niet
    'afgeleide van een token op $500k'."""
    eerste = {}
    for m, ts in db.execute("SELECT mint, MIN(ts) FROM trades WHERE price >= ? GROUP BY mint", (drempel,)):
        if ts: eerste[m] = ts
    uit = {}
    for m, t in toks.items():
        kand = [x for x in (eerste.get(m), t.get("migrated_ts")) if x]
        if kand: uit[m] = min(kand)
    return uit


def generieke_tickers(toks):
    """Een ticker die honderden keren voorkomt is geen identiteit maar een woord. Die uitsluiten,
    anders koppelt hij de halve dataset aan zichzelf."""
    telling = Counter(norm(t["symbol"]) for t in toks.values() if len(norm(t["symbol"])) >= MIN_TEKENS)
    return {k for k, n in telling.items() if n >= GENERIEK_VANAF}


def zoek_afgeleiden(toks, lopers, generiek, venster=VENSTER_S):
    """Per loper: welke tokens zijn binnen het venster gelanceerd en lijken erop?"""
    op_tijd = sorted((t["created_ts"], m) for m, t in toks.items() if t["created_ts"])
    tijden = [x[0] for x in op_tijd]
    import bisect
    paren = []
    gedaan = 0
    for lm, lts in lopers.items():
        gedaan += 1
        if gedaan % 500 == 0: log(f"  {gedaan}/{len(lopers)} lopers, {len(paren)} koppelingen")
        loper = toks.get(lm)
        if loper is None or norm(loper["symbol"]) in generiek: continue
        i = bisect.bisect_right(tijden, lts)
        j = bisect.bisect_right(tijden, lts + venster)
        for _, km in op_tijd[i:j]:
            if km == lm: continue
            reden = lijkt(loper, toks[km])
            if reden:
                paren.append({"loper": lm, "afgeleide": km, "reden": reden, "loper_ts": lts,
                              "na_s": round(toks[km]["created_ts"] - lts),
                              "zelfde_maker": None,
                              "loper_gemigreerd": bool(loper.get("migrated_ts"))})
    return paren


# ------------------------------------------------------------------ 3. uitkomsten
def uitkomst(t):
    """Wat deed dit token? Hoogste veelvoud van de startkoers, en of het de curve haalde."""
    if not t.get("launch") or t["launch"] <= 0 or not t.get("ath"): return None
    return {"mult": t["ath"] / t["launch"], "gemigreerd": bool(t.get("migrated_ts"))}


def samenvat(mults, migs, naam=""):
    n = len(mults)
    if not n: return {"n": 0}
    p2 = sum(1 for x in mults if x >= TWEE_X) / n
    p10 = sum(1 for x in mults if x >= TIEN_X) / n
    pm = sum(migs) / n
    return {"n": n, "mediaan_mult": round(statistics.median(mults), 3),
            "aandeel_2x": round(p2, 4), "aandeel_10x": round(p10, 4), "aandeel_gemigreerd": round(pm, 4)}


def verschil(a, b, veld):
    """Verschil in een aandeel tussen twee groepen, met 95%-marge (normale benadering).
    Loopt de marge door nul, dan is er geen verschil aangetoond."""
    if not a.get("n") or not b.get("n"): return None
    pa, pb, na, nb = a[veld], b[veld], a["n"], b["n"]
    se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    d = pa - pb
    return {"verschil": round(d, 4), "ci95": [round(d - 1.96 * se, 4), round(d + 1.96 * se, 4)],
            "significant": bool(abs(d) > 1.96 * se)}


def bouw(db, now):
    toks = lees_tokens(db)
    drempel = LOPER_DEEL * VOLTOOIINGSPRIJS
    lopers = loper_momenten(db, toks, drempel)
    generiek = generieke_tickers(toks)
    paren = zoek_afgeleiden(toks, lopers, generiek)
    for p in paren:
        p["zelfde_maker"] = None
    afg = {p["afgeleide"]: p for p in paren}        # één token telt één keer, ook bij meerdere lopers

    rep = {"gegenereerd": iso(now), "tokens": len(toks), "lopers": len(lopers),
           "drempel_sol_per_token": drempel, "drempel_marktkap_sol": round(drempel * (C.TOTAL_SUPPLY_RAW / 10**C.TOKEN_DECIMALS), 1),
           "generieke_tickers": len(generiek), "koppelingen": len(paren), "afgeleiden": len(afg),
           "venster_min": VENSTER_S // 60}

    # de eerlijke vergelijking: tokens uit dezelfde uren, want het aanbod komt in golven
    uren = Counter()
    for m in afg:
        t = toks[m]
        if t["created_ts"]: uren[int(t["created_ts"] // 3600)] += 1
    basis_mints = [m for m, t in toks.items()
                   if m not in afg and t["created_ts"] and int(t["created_ts"] // 3600) in uren]

    def groep(mints):
        mults, migs = [], []
        for m in mints:
            u = uitkomst(toks[m])
            if u is None: continue
            mults.append(u["mult"]); migs.append(1 if u["gemigreerd"] else 0)
        return samenvat(mults, migs)

    rep["afgeleiden_totaal"] = groep(list(afg))
    rep["basis_zelfde_uren"] = groep(basis_mints)
    rep["basis_alles"] = groep([m for m in toks if m not in afg])
    rep["verschil"] = {v: verschil(rep["afgeleiden_totaal"], rep["basis_zelfde_uren"], v)
                       for v in ("aandeel_2x", "aandeel_10x", "aandeel_gemigreerd")}

    # uitsplitsingen: welke soort koppeling, en maakt het uit of de loper al gemigreerd was
    rep["per_reden"] = {}
    for reden in sorted({p["reden"] for p in paren}):
        rep["per_reden"][reden] = groep([m for m, p in afg.items() if p["reden"] == reden])
    rep["per_loperstatus"] = {
        "loper_gemigreerd": groep([m for m, p in afg.items() if p["loper_gemigreerd"]]),
        "loper_op_curve": groep([m for m, p in afg.items() if not p["loper_gemigreerd"]]),
    }
    # hoe snel na de loper: eerder zou beter moeten zijn als het verschijnsel echt bestaat
    bakken = [(0, 600), (600, 1800), (1800, 3600), (3600, VENSTER_S)]
    rep["per_vertraging"] = {}
    for lo, hi in bakken:
        rep["per_vertraging"][f"{lo // 60}-{hi // 60} min"] = groep(
            [m for m, p in afg.items() if lo <= p["na_s"] < hi])

    # hoeveel gevallen per dag: zonder aantallen is het geen strategie
    per_dag = Counter()
    for m in afg:
        t = toks[m]
        if t["created_ts"]: per_dag[time.strftime("%Y-%m-%d", time.gmtime(t["created_ts"]))] += 1
    rep["per_dag"] = dict(sorted(per_dag.items()))
    rep["voorbeelden"] = [
        {"loper": f"{toks[p['loper']]['symbol']} ({toks[p['loper']]['name'][:24]})",
         "afgeleide": f"{toks[p['afgeleide']]['symbol']} ({toks[p['afgeleide']]['name'][:24]})",
         "reden": p["reden"], "na_min": round(p["na_s"] / 60, 1),
         "mult": round((uitkomst(toks[p["afgeleide"]]) or {}).get("mult", 0), 2)}
        for p in sorted(paren, key=lambda x: -((uitkomst(toks[x["afgeleide"]]) or {}).get("mult", 0)))[:10]]
    return rep


# ------------------------------------------------------------------ 4. rapport
def to_md(r):
    L = [f"# Afgeleide tokens ('vamps') — {r['gegenereerd']}", "",
         "De claim uit de KOL-video van 14 sept: als er een token loopt en iemand lanceert een "
         "gecorrigeerde versie ervan, neemt die afgeleide de plek over. Daar hoort een basisgetal bij en dat gaf de "
         "video niet. Hier staat het.", "",
         f"**Wat 'loper' hier betekent**: een token waarvan de koers boven {LOPER_DEEL:.0%} van de voltooiingsprijs "
         f"kwam (marktkap ≈ {r['drempel_marktkap_sol']:.0f} SOL) of dat migreerde. Boven de curve zien we niets meer, "
         "dus een token dat op de AMM naar $500k loopt — het geval uit de video — meten we alleen tot het de curve "
         "verlaat.", "",
         f"**Wat 'afgeleide' hier betekent**: een token gelanceerd binnen {r['venster_min']} minuten na dat moment, "
         "met dezelfde ticker, een gedeeld woord van minstens drie letters in de naam, de ticker als woord in de naam, "
         f"of een naamgelijkenis van {GELIJKENIS:.0%} of hoger. De 'fout in de naam' uit de video is een oordeel en "
         "zit hier niet in.", "",
         f"{r['tokens']} tokens, {r['lopers']} lopers, {r['koppelingen']} koppelingen, **{r['afgeleiden']} unieke "
         f"afgeleiden**. {r['generieke_tickers']} tickers uitgesloten omdat ze bij {GENERIEK_VANAF}+ tokens voorkomen "
         "en dus geen identiteit zijn.", ""]
    if not r["afgeleiden_totaal"].get("n"):
        L += ["**Geen afgeleiden gevonden met een bruikbare uitkomst.** Daarmee is de regel niet weerlegd, "
              "alleen niet meetbaar op deze data.", ""]
        return "\n".join(L) + "\n"
    L += ["## Doen afgeleiden het beter?", "",
          "| groep | n | mediaan hoogste veelvoud | ≥2x | ≥10x | gemigreerd |", "|---|---|---|---|---|---|"]
    for naam, sleutel in (("afgeleiden", "afgeleiden_totaal"), ("alle andere tokens uit dezelfde uren", "basis_zelfde_uren"),
                          ("alle andere tokens", "basis_alles")):
        g = r[sleutel]
        if not g.get("n"): continue
        L.append(f"| {naam} | {g['n']} | {g['mediaan_mult']:.2f}x | {g['aandeel_2x']:.1%} | "
                 f"{g['aandeel_10x']:.1%} | {g['aandeel_gemigreerd']:.1%} |")
    L += ["", "Verschil met tokens uit dezelfde uren, met 95%-marge. Loopt de marge door nul, dan is er geen "
              "verschil aangetoond.", "", "| maat | verschil | 95%-marge | aangetoond |", "|---|---|---|---|"]
    for v, d in (r.get("verschil") or {}).items():
        if not d: continue
        L.append(f"| {v.replace('aandeel_', '')} | {d['verschil']:+.1%} | {d['ci95'][0]:+.1%} tot {d['ci95'][1]:+.1%} | "
                 f"{'ja' if d['significant'] else 'nee'} |")
    for titel, sleutel in (("Per soort koppeling", "per_reden"), ("Was de loper al gemigreerd?", "per_loperstatus"),
                           ("Hoe snel na de loper", "per_vertraging")):
        blok = r.get(sleutel) or {}
        rijen = [(k, v) for k, v in blok.items() if v.get("n")]
        if not rijen: continue
        L += ["", f"## {titel}", "", "| groep | n | mediaan veelvoud | ≥2x | ≥10x | gemigreerd |", "|---|---|---|---|---|---|"]
        for k, g in rijen:
            L.append(f"| {k} | {g['n']} | {g['mediaan_mult']:.2f}x | {g['aandeel_2x']:.1%} | "
                     f"{g['aandeel_10x']:.1%} | {g['aandeel_gemigreerd']:.1%} |")
    if r.get("per_dag"):
        L += ["", "## Hoeveel gevallen per dag", "",
              "Zonder aantallen is het geen strategie maar een hobby.", "",
              "| dag | afgeleiden |", "|---|---|"]
        for d, n in r["per_dag"].items(): L.append(f"| {d} | {n} |")
    if r.get("voorbeelden"):
        L += ["", "## De tien grootste afgeleiden", "",
              "Let op: dit zijn de uitschieters, geselecteerd op uitkomst. Ze zeggen niets over de verwachting — "
              "ze staan er om te kunnen controleren of de koppelingen inhoudelijk kloppen.", "",
              "| loper | afgeleide | reden | na (min) | hoogste veelvoud |", "|---|---|---|---|---|"]
        for v in r["voorbeelden"]:
            L.append(f"| {v['loper']} | {v['afgeleide']} | {v['reden']} | {v['na_min']} | {v['mult']:.2f}x |")
    L += ["", "**Verkennend.** Deze analyse kijkt naar data die er al lag; elke uitkomst hier is een hypothese, "
              "geen toets. Komt er iets uit, dan moet het vooraf vastgelegd en op nieuwe tokens gemeten worden.", ""]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH)
    ap.add_argument("--out", default=C.REPORT_DIR)
    ap.add_argument("--now", type=float, default=None)
    args = ap.parse_args()
    now = args.now or time.time(); t0 = time.time()
    os.makedirs(args.out, exist_ok=True)
    db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=60)
    # Een analyse die stukloopt hoort dat te zéggen, niet te verdwijnen. Op 15 sept draaide deze
    # wel maar verscheen er geen rapport, en het logboek was toen al overschreven door de analyses
    # die erna kwamen. Daarom schrijft hij bij een fout een rapport mét de fout erin.
    try:
        rep = bouw(db, now)
    except Exception as e:
        import traceback
        fout = traceback.format_exc()
        with open(os.path.join(args.out, "vamp.md"), "w") as f:
            f.write(f"# Afgeleide tokens ('vamps') — {iso(now)}\n\n**Deze analyse is vastgelopen.** "
                    f"Er staan dus geen cijfers in; dat is geen uitkomst maar een storing.\n\n```\n{fout}\n```\n")
        with open(os.path.join(args.out, "vamp.json"), "w") as f:
            json.dump({"gegenereerd": iso(now), "fout": str(e)[:300]}, f, indent=1)
        log("vamp vastgelopen:", e)
        raise
    with open(os.path.join(args.out, "vamp.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "vamp.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s: {rep['lopers']} lopers, {rep['afgeleiden']} afgeleiden "
        f"-> {args.out}/vamp.md")


if __name__ == "__main__":
    main()
