"""Dag-/eindrapport: funnel, per variant winkans, rug-%, verwachtingswaarde, drawdown, Monte Carlo."""
import json, math, random, statistics, time, os
import config as C

def _stats(rows, key):
    """rows: sim_trades; key: pnl-sleutel bv '0.2_axiom'. Geeft dict met kerncijfers."""
    rets = []
    for r in rows:
        try: rets.append(json.loads(r["pnl_json"])[key])
        except Exception: continue
    n = len(rets)
    if n == 0: return {"n": 0}
    wins = [x for x in rets if x > 0]; losses = [x for x in rets if x <= 0]
    rugs = sum(1 for r in rows if r["is_rug"])
    ev = statistics.mean(rets)
    out = {"n": n, "winkans": round(len(wins) / n, 3), "rug_pct": round(rugs / n, 3), "gem_winst": round(statistics.mean(wins), 3) if wins else 0,
           "gem_verlies": round(statistics.mean(losses), 3) if losses else 0, "ev": round(ev, 4), "mediaan": round(statistics.median(rets), 4)}
    for size_frac in (0.05, 0.20, 0.50):
        out[f"maxdd_{int(size_frac*100)}"] = round(_max_dd(rets, size_frac), 3)
    if n >= 30: out["mc"] = _monte_carlo(rets, 0.20)
    out["ci95"] = _ci95(rets)
    out["aandeel_van_ev_uit_top3"] = _top_share(rets)
    return out


def _ci95(rets):
    """95%-marge om de EV. Zonder marge is een EV op een handvol uitschieters niet te beoordelen."""
    n = len(rets)
    if n < 2: return None
    h = 1.96 * statistics.pstdev(rets) / math.sqrt(n)
    m = statistics.mean(rets)
    return [round(m - h, 4), round(m + h, 4)]


def _top_share(rets):
    """Welk deel van de totale winst komt uit de drie beste trades? Bij een hoog getal draagt
    de EV op een paar uitschieters en zegt het gemiddelde weinig over wat je zou meemaken.
    Boven 100% betekent: de drie beste trades zijn de hele winst en de rest verliest geld."""
    tot = sum(rets)
    if tot <= 0: return None
    return round(sum(sorted(rets, reverse=True)[:3]) / tot, 3)

def _max_dd(rets, f):
    eq, peak, dd = 1.0, 1.0, 0.0
    for r in rets:
        eq *= 1 + f * r; peak = max(peak, eq); dd = max(dd, 1 - eq / peak)
    return dd

def _monte_carlo(rets, f, runs=2000, trades=2000, target=10000, ruin=0.02):
    random.seed(7); hit = ruin_n = 0
    for _ in range(runs):
        eq = 1.0
        for _ in range(trades):
            eq *= 1 + f * random.choice(rets)
            if eq >= target: hit += 1; break
            if eq <= ruin: ruin_n += 1; break
    return {"inzet": f, "kans_10000x": round(hit / runs, 3), "kans_ruine": round(ruin_n / runs, 3)}

def build(store, since_ts=0):
    rows = store.query("SELECT * FROM sim_trades WHERE exit_ts >= ?", (since_ts,))
    funnel = store.query("SELECT day, stage, n FROM funnel ORDER BY day, stage")
    rep = {"generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "sim_trades": len(rows), "funnel": {}}
    for f in funnel: rep["funnel"].setdefault(f["day"], {})[f["stage"]] = f["n"]
    rep["varianten"] = {}
    keys = [f"{s}_{t}" for s in C.SIZES_SOL for t in C.FEE_TERMINAL]
    for dip in C.DIP_VARIANTS:
        for v in ("V1", "V2", "V3"):
            for sp_label, sp in (("gescreend_pass", 1), ("gescreend_fail", 0), ("alle", None)):
                sub = [r for r in rows if r["dip"] == dip and r["variant"] == v and (sp is None or r["screen_pass"] == sp)]
                if not sub: continue
                rep["varianten"][f"dip{int(dip*100)}_{v}_{sp_label}"] = {k: _stats(sub, k) for k in keys}
    # beste variant op EV bij 0.2 SOL / PumpPortal met n>=30
    best = None
    for name, d in rep["varianten"].items():
        s = d.get("0.2_pp", {})
        if s.get("n", 0) >= 30 and (best is None or s["ev"] > best[1]["ev"]): best = (name, s)
    rep["beste_variant"] = {"naam": best[0], **best[1]} if best else None
    rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
                       "rug<=0.05": bool(best and best[1]["rug_pct"] <= 0.05), "ev>=+0.03": bool(best and best[1]["ev"] >= 0.03),
                       "maxdd20<=0.40": bool(best and best[1]["maxdd_20"] <= 0.40)} if best else None
    # Proxy voor bouwplan-regel 3 ("community-check", niet gemeten als filter, zie README):
    # heeft het token een X-link in de metadata? Alleen aan-/afwezigheid, geen echte activiteit/engagement-check.
    # Gepoold over alle dip%/exit-varianten binnen gescreend_pass, inzet 0,2 SOL / PumpPortal-fees.
    xlink = {t["mint"]: t["has_x_link"] for t in store.query("SELECT mint, has_x_link FROM tokens")}
    rep["community_proxy"] = {"_uitleg": "Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, "
                                          "niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. "
                                          "Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal "
                                          "onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) "
                                          "en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd."}
    for label, cond in (("met_xlink", 1), ("zonder_xlink", 0)):
        sub = [r for r in rows if r["screen_pass"] == 1 and xlink.get(r["mint"]) == cond]
        if not sub: continue
        rep["community_proxy"][f"gepoold_{label}"] = _stats(sub, "0.2_pp")
        rep["community_proxy"][f"per_token_{label}"] = _per_token_stats(sub, "0.2_pp")
    return rep


def _per_token_stats(rows, key):
    """Elk token één keer: eerst het gemiddelde over zijn varianten, dan de statistiek daarover.
    Zo kan één token met een uitschieter niet vijf keer meetellen."""
    per = {}
    for r in rows:
        try: v = json.loads(r["pnl_json"])[key]
        except Exception: continue
        a = per.setdefault(r["mint"], [0.0, 0, 0])
        a[0] += v; a[1] += 1; a[2] = max(a[2], int(r["is_rug"] or 0))
    if not per: return {"n": 0}
    rets = [a[0] / a[1] for a in per.values()]
    wins = [x for x in rets if x > 0]
    n = len(rets)
    return {"n": n, "winkans": round(len(wins) / n, 3), "rug_pct": round(sum(a[2] for a in per.values()) / n, 3),
            "ev": round(statistics.mean(rets), 4), "mediaan": round(statistics.median(rets), 4),
            "ci95": _ci95(rets), "aandeel_van_ev_uit_top3": _top_share(rets),
            "maxdd_20": round(_max_dd(rets, 0.20), 3)}

def to_markdown(rep):
    L = [f"# Schaduwbot rapport — {rep['generated']}", "", f"Gelogde schaduwtrades: **{rep['sim_trades']}**", "", "## Funnel per dag", ""]
    stages = ["created", "newpairs", "final_stretch", "screened", "screen_pass", "entry", "exit"]
    L.append("| dag | " + " | ".join(stages) + " |"); L.append("|" + "---|" * (len(stages) + 1))
    for day, d in sorted(rep["funnel"].items()):
        L.append(f"| {day} | " + " | ".join(str(d.get(s, 0)) for s in stages) + " |")
    L += ["", "## Varianten (inzet 0,2 SOL, PumpPortal-fees)", "", "| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |", "|---|---|---|---|---|---|---|---|"]
    for name, d in rep["varianten"].items():
        s = d.get("0.2_pp", {})
        if s.get("n", 0) == 0: continue
        L.append(f"| {name} | {s['n']} | {s['winkans']:.0%} | {s['rug_pct']:.1%} | {s['gem_winst']:+.1%} | {s['gem_verlies']:+.1%} | {s['ev']:+.2%} | {s['maxdd_20']:.0%} |")
    if rep.get("beste_variant"):
        b = rep["beste_variant"]; L += ["", f"## Beste variant: {b['naam']}", ""]
        for k, v in rep["drempels"].items(): L.append(f"- {k}: {'✅' if v else '❌'}")
        if b.get("mc"): L.append(f"- Monte Carlo (20% inzet): kans 10.000× {b['mc']['kans_10000x']:.1%}, kans ruïne {b['mc']['kans_ruine']:.1%}")
    else:
        L += ["", "_Nog geen variant met ≥ 30 trades._"]
    cp = rep.get("community_proxy") or {}
    if any(k.endswith("xlink") for k in cp):
        L += ["", "## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)", "", cp["_uitleg"], "",
              "| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |",
              "|---|---|---|---|---|---|---|---|---|"]
        for label in ("per_token_met_xlink", "per_token_zonder_xlink", "gepoold_met_xlink", "gepoold_zonder_xlink"):
            st = cp.get(label)
            if not (st and st.get("n", 0) > 0): continue
            ci = f"{st['ci95'][0]:+.1%} tot {st['ci95'][1]:+.1%}" if st.get("ci95") else "–"
            top = f"{st['aandeel_van_ev_uit_top3']:.0%}" if st.get("aandeel_van_ev_uit_top3") is not None else "–"
            L.append(f"| {label} | {st['n']} | {st['winkans']:.0%} | {st['rug_pct']:.1%} | {st['ev']:+.2%} | {ci} | "
                     f"{st['mediaan']:+.1%} | {top} | {st['maxdd_20']:.0%} |")
        L += ["", "Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een "
                  "verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden."]
    return "\n".join(L) + "\n"

def write(store, outdir=C.REPORT_DIR):
    os.makedirs(outdir, exist_ok=True)
    rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
    with open(os.path.join(outdir, f"{day}.json"), "w") as f: json.dump(rep, f, indent=1)
    md = to_markdown(rep)
    with open(os.path.join(outdir, f"{day}.md"), "w") as f: f.write(md)
    with open(os.path.join(outdir, "latest.md"), "w") as f: f.write(md)
    return rep
