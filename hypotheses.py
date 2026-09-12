"""Hypotheseregister: elke hypothese staat hier met een oorzakelijk verhaal, een falsificeerbare
voorspelling, één primaire meetcel en een vaste registratietijd — vóórdat er data naar gekeken
wordt. Alleen tokens die ná de registratietijd zijn ontstaan tellen als toets. Wat daarvoor
ligt heet 'verkennend' en kan nooit een oordeel opleveren.

Regels (bewust hard):
- `vastgelegd_ts` wordt nooit gewijzigd. Een aangepaste hypothese is een nieuwe hypothese met een
  nieuw id en een nieuw oorzakelijk verhaal.
- Eén primaire cel per hypothese. De rest van het raster is verkennend, hoe mooi het er ook
  uitziet. Zo kan niemand achteraf de beste cel kiezen.
- Eén herkansing (zoals het bouwplan). Een oordeel 'gezakt' blijft staan in data/hypotheses_state.json.

Gebruik:  python hypotheses.py [--db ...] [--out reports]
"""
import argparse, bisect, json, math, os, sqlite3, statistics, time
from collections import defaultdict

import config as C
import curve

# --------------------------------------------------------------------------- register
HYPOTHESEN = [
    {
        "id": "S1",
        "naam": "Sniper-rang op de bonding curve",
        "vastgelegd_ts": 1789236000,        # 2026-09-12 18:00 UTC — niet wijzigen
        "oorzaak": (
            "De curve is een constant-product op virtuele reserves: elke volgende koop verhoogt de prijs "
            "deterministisch. Wie als k-de koper instapt, koopt vóór alle latere kopers en verkoopt aan hen. "
            "Het voordeel zit dus niet in selectie of vaardigheid maar in positie in de rij. De geldstroom "
            "bevestigt dat: de enige rollen met netto instroom zijn de rollen die er vóór de zichtbare "
            "koers in zitten (dev, bundel, sniper ≤ 5 s)."
        ),
        "voorspelling": (
            "EV per trade daalt monotoon met de instaprang. Voor lage rang (≤ 3) en een uitstap 'verkopen aan "
            "de volgende golf kopers' is de EV na kosten positief, óók zonder enige selectie op het token. "
            "Is de EV op rang 1–3 negatief, dan is er op de curve géén positie die winst geeft zonder "
            "informatie van vóór de creatie, en is deze lijn dood."
        ),
        "primair": {"filter": "ongefilterd", "rang": 3, "uitstap": "na_10_kopers"},
        "drempel": {"min_n": 500, "ev_min": 0.03, "winkans_min": 0.50, "rug_max": 0.05, "maxdd20_max": 0.40},
        "toets": "sniper_rang",
        "beperking": (
            "De simulatie zet ons vóór koper k zonder iemand te verdringen en zonder eigen koersimpact, tegen een "
            "vaste tip. Echt snipen is een latentieveiling: de kosten van rang k zijn niet vast en niet gemeten. "
            "Deze toets zegt of er op rang k waarde zít — of die rang haalbaar is, zegt hij niet."
        ),
    },
]

# --------------------------------------------------------------------------- S1-instellingen
RANGEN = [1, 2, 3, 5, 10, 20]
UITSTAPPEN = ["t10", "t30", "t60", "t180", "na_3_kopers", "na_10_kopers", "tp50_sl30", "trail20"]
FILTERS = ["ongefilterd", "geen_bundel", "dev_eerder_gemigreerd"]
SIZE = 0.2
TIP_SOL = float(os.getenv("SNIPE_TIP_SOL", 0.005))     # Jito-tip per kant, bovenop de prioriteitskosten
HORIZON_S = 180
RUG_S = 60
INIT_V_SOL, INIT_V_TOK = 30_000_000_000, 1_073_000_000_000_000
BUNDEL_MAX_SUPPLY = 0.05
STATE_PATH = os.getenv("HYPOTHESES_STATE", "data/hypotheses_state.json")


def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None
def price(vs, vt): return vs / vt if vt else 0.0


def ci95(xs):
    n = len(xs)
    if n < 2: return None
    m = sum(xs) / n; h = 1.96 * statistics.pstdev(xs) / math.sqrt(n)
    return [round(m - h, 4), round(m + h, 4)]


def max_dd(rets, f=0.20):
    eq = piek = 1.0; dd = 0.0
    for r in rets:
        eq *= 1 + f * r; piek = max(piek, eq); dd = max(dd, 1 - eq / piek)
    return dd


# --------------------------------------------------------------------------- S1: sniper-rang
def _uitstap_index(rows, idx, regel, p0):
    """Geeft de index in rows waar we verkopen, volgens `regel`. rows[idx] is de koop van koper k;
    wij zitten er net vóór. Verkopen gebeurt op de toestand ná rows[j]."""
    t0 = rows[idx][0]; laatste = idx
    if regel[0] == "t" and regel[1:].isdigit():
        grens = t0 + int(regel[1:])
        for j in range(idx, len(rows)):
            if rows[j][0] > grens: break
            laatste = j
        return laatste
    if regel.startswith("na_"):
        n_doel = int(regel.split("_")[1]); geteld = 0
        for j in range(idx, len(rows)):
            if rows[j][0] > t0 + HORIZON_S: break
            laatste = j
            if rows[j][2]: geteld += 1
            if geteld >= n_doel: return j
        return laatste
    if regel == "tp50_sl30":
        for j in range(idx, len(rows)):
            if rows[j][0] > t0 + HORIZON_S: break
            laatste = j; m = price(rows[j][4], rows[j][5]) / p0
            if m >= 1.5 or m <= 0.7: return j
        return laatste
    if regel == "trail20":
        piek = 1.0
        for j in range(idx, len(rows)):
            if rows[j][0] > t0 + HORIZON_S: break
            laatste = j; m = price(rows[j][4], rows[j][5]) / p0; piek = max(piek, m)
            if m <= 0.75 or (piek > 1 and m <= piek * 0.8): return j
        return laatste
    raise ValueError(regel)


def eval_token(rows, tok):
    """rows: [(ts, user, is_buy, tokens, v_sol, v_tok)] gesorteerd. tok: dict met creator, created_ts,
    create_slot, geen_bundel, dev_eerder_gemigreerd. Geeft {rang: {"latentie": s, "rug": bool, uitstap: ret}}."""
    creator = tok["creator"]
    kopers = [i for i, r in enumerate(rows) if r[2] and r[1] != creator]
    if not kopers: return {}
    # rug: dev verkoopt ≥ 50% van zijn bezit binnen RUG_S, of koers -80% t.o.v. eerste koop binnen RUG_S
    dev_gekocht = sum(r[3] for r in rows if r[2] and r[1] == creator and r[0] <= tok["created_ts"] + RUG_S)
    dev_verkocht = sum(r[3] for r in rows if not r[2] and r[1] == creator and r[0] <= tok["created_ts"] + RUG_S)
    rug_dev = dev_gekocht > 0 and dev_verkocht >= 0.5 * dev_gekocht
    out = {}
    for k in RANGEN:
        if len(kopers) < k: break
        idx = kopers[k - 1]
        vs, vt = (rows[idx - 1][4], rows[idx - 1][5]) if idx > 0 else (INIT_V_SOL, INIT_V_TOK)
        p0 = price(vs, vt)
        if p0 <= 0: continue
        tok_raw, _ = curve.buy(vs, vt, SIZE, "pp")
        p_rug = min((price(r[4], r[5]) for r in rows[idx:] if r[0] <= rows[idx][0] + RUG_S), default=p0)
        res = {"latentie": round(rows[idx][0] - tok["created_ts"], 3), "rug": bool(rug_dev or p_rug <= 0.2 * p0)}
        for regel in UITSTAPPEN:
            j = _uitstap_index(rows, idx, regel, p0)
            uit, _ = curve.sell(rows[j][4], rows[j][5], tok_raw, "pp")
            res[regel] = round((uit - TIP_SOL - SIZE - TIP_SOL) / SIZE, 4)
        out[k] = res
    return out


def iter_tokens(db, since):
    cur = db.execute("SELECT mint, ts, user, is_buy, tokens, v_sol, v_tok FROM trades INDEXED BY trades_mint_ts "
                     "WHERE ts >= ? ORDER BY mint, ts", (since,))
    mint, rows = None, []
    for r in cur:
        if r[0] != mint:
            if rows: yield mint, rows
            mint, rows = r[0], []
        rows.append((r[1], r[2], int(r[3]), int(r[4] or 0), int(r[5]), int(r[6])))
    if rows: yield mint, rows


def laad_tokens(db, since, starts):
    """Zoals ledger.py: tokens met een herstart binnen 2 uur na creatie vallen af (gat in de data)."""
    toks = {}
    gemigreerd_door = defaultdict(list)
    for m, creator, created, slot, mig in db.execute(
            "SELECT mint, creator, created_ts, create_slot, migrated_ts FROM tokens WHERE created_ts >= ?", (since,)):
        gap = any(created < s < created + 7200 for s in starts)
        toks[m] = {"creator": creator, "created_ts": created, "create_slot": slot, "gap": gap, "migrated_ts": mig}
        if mig: gemigreerd_door[creator].append(created)
    for m, t in toks.items():
        t["dev_eerder_gemigreerd"] = any(c < t["created_ts"] for c in gemigreerd_door.get(t["creator"], []))
    return toks


def sniper_rang(db, since, starts, hyp, now):
    toks = laad_tokens(db, since, starts)
    vast = hyp["vastgelegd_ts"]
    agg = {"toets": defaultdict(list), "verkennend": defaultdict(list)}      # (filter, rang, uitstap) -> [ret]
    rugs = {"toets": defaultdict(list), "verkennend": defaultdict(list)}
    lat = {"toets": defaultdict(list), "verkennend": defaultdict(list)}
    n_tok = {"toets": 0, "verkennend": 0}; n_skip = 0
    for mint, rows in iter_tokens(db, since):
        t = toks.get(mint)
        if t is None or t["gap"] or t["created_ts"] > now - HORIZON_S - 120: n_skip += 1; continue
        # bundel: in het creatieblok gekocht (door wie dan ook) > 5% van de supply
        in_blok = sum(r[3] for r in rows if r[2] and r[0] <= t["created_ts"] + 1.0)
        t["geen_bundel"] = in_blok <= BUNDEL_MAX_SUPPLY * C.TOTAL_SUPPLY_RAW
        groep = "toets" if t["created_ts"] >= vast else "verkennend"
        n_tok[groep] += 1
        per_rang = eval_token(rows, t)
        for f in FILTERS:
            if f == "geen_bundel" and not t["geen_bundel"]: continue
            if f == "dev_eerder_gemigreerd" and not t["dev_eerder_gemigreerd"]: continue
            for k, res in per_rang.items():
                lat[groep][(f, k)].append(res["latentie"])
                rugs[groep][(f, k)].append(res["rug"])
                for regel in UITSTAPPEN:
                    agg[groep][(f, k, regel)].append(res[regel])
    def cel(groep, f, k, regel):
        xs = agg[groep].get((f, k, regel)) or []
        if not xs: return {"n": 0}
        rg = rugs[groep].get((f, k)) or []
        return {"n": len(xs), "ev": round(sum(xs) / len(xs), 4), "ci95": ci95(xs), "mediaan": round(statistics.median(xs), 4),
                "winkans": round(sum(1 for x in xs if x > 0) / len(xs), 3), "rug_pct": round(sum(rg) / len(rg), 3) if rg else None,
                "maxdd_20": round(max_dd(xs), 3), "latentie_mediaan_s": round(statistics.median(lat[groep][(f, k)]), 2)}
    out = {"tokens": n_tok, "overgeslagen": n_skip, "instellingen": {"size_sol": SIZE, "tip_sol": TIP_SOL, "horizon_s": HORIZON_S,
                                                                      "rangen": RANGEN, "uitstappen": UITSTAPPEN, "filters": FILTERS}}
    for groep in ("toets", "verkennend"):
        out[groep] = {f: {k: {regel: cel(groep, f, k, regel) for regel in UITSTAPPEN} for k in RANGEN} for f in FILTERS}
    p = hyp["primair"]
    out["primair"] = {"cel": p, "toets": cel("toets", p["filter"], p["rang"], p["uitstap"]),
                      "verkennend": cel("verkennend", p["filter"], p["rang"], p["uitstap"])}
    return out


# --------------------------------------------------------------------------- oordeel en toestand
def laad_state():
    try:
        with open(STATE_PATH) as f: return json.load(f)
    except Exception: return {}


def bewaar_state(st):
    os.makedirs(os.path.dirname(STATE_PATH) or ".", exist_ok=True)
    with open(STATE_PATH, "w") as f: json.dump(st, f, indent=1)


def oordeel(hyp, cel, state, now):
    """Alleen de primaire cel, alleen op toetsdata. Een eindoordeel blijft staan."""
    d = hyp["drempel"]; st = state.setdefault(hyp["id"], {"oordelen": []})
    if st.get("eind"): return st["eind"]
    if cel.get("n", 0) < d["min_n"]:
        return {"status": "te vroeg", "n": cel.get("n", 0), "nodig": d["min_n"]}
    checks = {"n>=min_n": True, "ev>=ev_min": cel["ev"] >= d["ev_min"], "winkans>=min": cel["winkans"] >= d["winkans_min"],
              "rug<=max": (cel["rug_pct"] or 0) <= d["rug_max"], "maxdd20<=max": cel["maxdd_20"] <= d["maxdd20_max"]}
    gehaald = all(checks.values())
    o = {"status": "gehaald" if gehaald else "gezakt", "ts": now, "n": cel["n"], "ev": cel["ev"], "ci95": cel["ci95"], "checks": checks}
    st["oordelen"].append(o)
    if gehaald or len(st["oordelen"]) > hyp.get("herkansingen", 1):
        st["eind"] = {**o, "definitief": True}
    return st.get("eind") or {**o, "herkansing_over": hyp.get("herkansingen", 1) - len(st["oordelen"]) + 1}


# --------------------------------------------------------------------------- rapport
def fmt_cel(c):
    if not c.get("n"): return "–"
    ci = f" ({c['ci95'][0]:+.0%}…{c['ci95'][1]:+.0%})" if c.get("ci95") else ""
    return f"{c['ev']:+.1%}{ci} n={c['n']}"


def to_md(rep):
    L = [f"# Hypotheseregister — {rep['gegenereerd']}", "",
         "Elke hypothese hier is vastgelegd vóórdat er naar de data gekeken werd: oorzakelijk verhaal, voorspelling, "
         "één primaire meetcel en de drempels. Alleen tokens van ná de registratietijd tellen als toets; alles daarvoor "
         "is verkennend en levert nooit een oordeel op. Eén herkansing, daarna staat het oordeel vast.", ""]
    for h in rep["hypothesen"]:
        L += [f"## {h['id']} — {h['naam']}", "", f"Vastgelegd: {iso(h['vastgelegd_ts'])}.", "",
              f"**Oorzaak.** {h['oorzaak']}", "", f"**Voorspelling.** {h['voorspelling']}", "",
              f"**Primaire cel.** filter `{h['primair']['filter']}`, rang {h['primair']['rang']}, uitstap `{h['primair']['uitstap']}`. "
              f"Drempels: n ≥ {h['drempel']['min_n']}, EV ≥ {h['drempel']['ev_min']:+.0%}, winkans ≥ {h['drempel']['winkans_min']:.0%}, "
              f"rug ≤ {h['drempel']['rug_max']:.0%}, maxDD@20% ≤ {h['drempel']['maxdd20_max']:.0%}.", ""]
        o = h["oordeel"]
        if o["status"] == "te vroeg":
            L += [f"**Oordeel: te vroeg** — {o['n']} van de {o['nodig']} benodigde tokens in de toets.", ""]
        else:
            L += [f"**Oordeel: {o['status'].upper()}**" + (" (definitief)" if o.get("definitief") else f" (herkansingen over: {o.get('herkansing_over', 0)})") +
                  f" — n={o['n']}, EV {o['ev']:+.1%}" + (f", marge {o['ci95'][0]:+.1%} tot {o['ci95'][1]:+.1%}" if o.get("ci95") else "") + ".",
                  "", "| drempel | gehaald |", "|---|---|"] + [f"| {k} | {'✅' if v else '❌'} |" for k, v in o["checks"].items()] + [""]
        r = h["resultaat"]
        L += [f"Toetsdata: {r['tokens']['toets']} tokens ná registratie; verkennend: {r['tokens']['verkennend']} tokens ervoor "
              f"({r['overgeslagen']} overgeslagen wegens herstart of te jong). Inzet {r['instellingen']['size_sol']} SOL, "
              f"tip {r['instellingen']['tip_sol']} SOL per kant, horizon {r['instellingen']['horizon_s']} s.", ""]
        pc = r["primair"]
        L += ["| primaire cel | toets (telt) | verkennend (telt niet) |", "|---|---|---|",
              f"| rang {pc['cel']['rang']}, {pc['cel']['uitstap']}, {pc['cel']['filter']} | {fmt_cel(pc['toets'])} | {fmt_cel(pc['verkennend'])} |", ""]
        for groep, kop in (("toets", "Toets (ná registratie)"), ("verkennend", "Verkennend (vóór registratie — niet gebruiken als bewijs)")):
            L += [f"### {kop}", ""]
            for f in r["instellingen"]["filters"]:
                blok = r[groep][f]
                if not any(blok[k][u].get("n") for k in blok for u in blok[k]): continue
                L += [f"**filter `{f}`** — EV per trade (95%-marge) n", "",
                      "| rang | latentie (mediaan) | rug | " + " | ".join(r["instellingen"]["uitstappen"]) + " |",
                      "|---|---|---|" + "---|" * len(r["instellingen"]["uitstappen"])]
                for k, per_u in blok.items():
                    eerste = next((per_u[u] for u in per_u if per_u[u].get("n")), None)
                    if not eerste: continue
                    L.append(f"| {k} | {eerste['latentie_mediaan_s']} s | {eerste['rug_pct']:.0%} | " +
                             " | ".join(fmt_cel(per_u[u]) for u in r["instellingen"]["uitstappen"]) + " |")
                L.append("")
        L += ["**Beperking.** " + h["beperking"], ""]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH); ap.add_argument("--out", default=C.REPORT_DIR)
    ap.add_argument("--now", type=float, default=None); ap.add_argument("--state", default=None)
    args = ap.parse_args()
    global STATE_PATH
    if args.state: STATE_PATH = args.state
    now = args.now or time.time(); t0 = time.time()
    db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=60)
    meta = dict(db.execute("SELECT k, v FROM meta"))
    since = json.loads(meta.get("full_trade_log_since", "0") or "0")
    starts = json.loads(meta.get("bot_starts", "[]") or "[]")
    os.makedirs(args.out, exist_ok=True)
    if not since:
        with open(os.path.join(args.out, "hypotheses.md"), "w") as f: f.write("# Hypotheseregister\n\nVolledige logging nog niet actief.\n")
        return
    state = laad_state()
    rep = {"gegenereerd": iso(now), "hypothesen": []}
    for h in HYPOTHESEN:
        res = globals()[h["toets"]](db, since, starts, h, now)
        o = oordeel(h, res["primair"]["toets"], state, now)
        rep["hypothesen"].append({**h, "resultaat": res, "oordeel": o})
        log(f"{h['id']}: {o['status']} — toets n={res['primair']['toets'].get('n', 0)}, verkennend n={res['primair']['verkennend'].get('n', 0)}")
    bewaar_state(state)
    with open(os.path.join(args.out, "hypotheses.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "hypotheses.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s -> {args.out}/hypotheses.md")


if __name__ == "__main__":
    main()
