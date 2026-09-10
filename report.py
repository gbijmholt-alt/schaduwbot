"""Dag-/eindrapport: funnel, per variant winkans, rug-%, verwachtingswaarde, drawdown, Monte Carlo."""
import json, random, statistics, time, os
from . import config as C

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
    return out

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
    return rep

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
    return "\n".join(L) + "\n"

def write(store, outdir=C.REPORT_DIR):
    os.makedirs(outdir, exist_ok=True)
    rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
    with open(os.path.join(outdir, f"{day}.json"), "w") as f: json.dump(rep, f, indent=1)
    md = to_markdown(rep)
    with open(os.path.join(outdir, f"{day}.md"), "w") as f: f.write(md)
    with open(os.path.join(outdir, "latest.md"), "w") as f: f.write(md)
    return rep
