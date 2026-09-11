#!/usr/bin/env python3
"""Toets van de kern van de video op álle gelogde trades: instappen op een pullback van ~45% vanaf de top,
en het onderscheid tussen een bundel/pump-and-dump-grafiek en een schone grafiek.

Wat de video zegt (transcript, gecontroleerd):
 - Bundelgrafiek: token start rond 4–5K en schiet in één groene candle door naar ~10K+, zonder verkopen en zonder
   andere koersactie. Dan wordt er in kleine stukjes verkocht om echte handel na te bootsen, en daarna gedumpt.
   Controle: top-5 houders met bijna gelijke SOL-saldi en dezelfde funding-tijd.
 - Instap: bij een schone coin met community op een dip van 40–50% vanaf de all-time high ("45%").
   Claim: "daarna kopen mensen hem weer 45% omhoog, elke keer".
 - Uitstap: verkopen zodra de koers onder je instapprijs zakt.

Werkwijze
 - Alleen tokens die ontstonden nadat de bot álle trades logde, zonder herstart binnen hun logperiode, en minstens
   2 uur oud (zodat de hele houdperiode in de data zit).
 - Per token: lanceerkenmerken (max koers vóór de eerste verkoop, aandeel supply in het creatieblok en eerste 5 s),
   aanloop tot de top (kopers, verkopen, tussentijdse dips, grootste koper), en het eerste dipmoment per dipdiepte.
 - Instap 2 s na het signaal met 0,2 SOL, PumpPortal-fees, exacte curve-slippage. Drie uitstapregels.
 - Screening (houders, dev, insiders) telt alleen als die vóór het instapmoment klaar was.
 Resultaten per token worden bewaard (data/ledger.sqlite, tabel replay), dus elke run rekent alleen nieuwe tokens.
Uitvoer: reports/video_replay.md en .json
"""
import argparse, bisect, json, math, os, sqlite3, statistics, time
import config as C
import curve

VERSIE = "replay-v1"
DIPS = [0.40, 0.45, 0.50]
ATH_MULT = C.ATH_MIN_MULT            # top moet minstens 2x de startkoers zijn (video: 4-5K -> 10K)
TRIGGER_MAX_AGE_S = 3600             # dip moet binnen het eerste uur vallen (zoals de live simulatie)
HOLD_S = 3600
SIZE = 0.2
BUNDLE_CANDLE_MULT = 2.0             # video: één groene candle van 5K naar 10K zonder verkopen
PRIMARY = ("d45_direct", "video", "schoon+houders_ok")


def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None
def px(vs, vt): return vs / vt if vt else 0.0


def meta_get(db, k, default=None):
    r = db.execute("SELECT v FROM meta WHERE k = ?", (k,)).fetchone()
    return json.loads(r[0]) if r else default


# ----------------------------------------------------------------- per token
def analyse_token(rows, created_ts, create_slot, creator, screened_ts):
    """rows: (ts, slot, user, is_buy, sol, tokens, v_sol, v_tok) op tijd gesorteerd. Geeft dict of None."""
    if not rows: return None
    P = [px(r[6], r[7]) for r in rows]; T = [r[0] for r in rows]
    # startkoers: na de aankopen van de dev in het creatieblok
    i0 = 0
    for i, r in enumerate(rows):
        if r[1] == create_slot and r[2] == creator and r[3]: i0 = i
        elif r[0] > created_ts + 2: break
    L0 = P[i0]
    if L0 <= 0: return None
    # lanceerkenmerken
    first_sell = next((i for i, r in enumerate(rows) if not r[3] and r[2] != creator), len(rows))
    mult_first_sell = max(P[:max(1, first_sell)]) / L0
    blok0 = sum(r[5] for r in rows if r[3] and r[1] == create_slot and r[2] != creator)
    s5 = sum(r[5] for r in rows if r[3] and r[0] <= created_ts + 5 and r[2] != creator)
    buyers_first_sell = len({r[2] for r in rows[:first_sell] if r[3] and r[2] != creator})
    feat = {"mult_voor_eerste_verkoop": round(mult_first_sell, 3), "blok0_pct": round(100 * blok0 / C.TOTAL_SUPPLY_RAW, 2),
            "eerste5s_pct": round(100 * s5 / C.TOTAL_SUPPLY_RAW, 2), "kopers_voor_eerste_verkoop": buyers_first_sell,
            "bundelgrafiek": mult_first_sell >= BUNDLE_CANDLE_MULT, "n_trades": len(rows), "max_mult": round(max(P) / L0, 3)}

    def state(t):
        i = max(0, bisect.bisect_right(T, t) - 1); return int(rows[i][6]), int(rows[i][7]), i

    out = {"feat": feat, "signalen": {}}
    for d in DIPS:
        ath, ath_i = L0, i0; trig = None
        for i in range(i0, len(rows)):
            if T[i] > created_ts + TRIGGER_MAX_AGE_S: break
            if P[i] > ath: ath, ath_i = P[i], i
            if ath >= ATH_MULT * L0 and P[i] <= ath * (1 - d): trig = i; break
        if trig is None: continue
        # aanloop tot de top
        buys = {}; n_sells = 0; pullbacks = 0; run_max = L0; in_pb = False
        for r, p in zip(rows[i0:ath_i + 1], P[i0:ath_i + 1]):
            if r[3]: buys[r[2]] = buys.get(r[2], 0.0) + r[4]
            elif r[2] != creator: n_sells += 1
            if p > run_max:
                if in_pb: pullbacks += 1; in_pb = False
                run_max = p
            elif p <= run_max * 0.85: in_pb = True
        tot_buy = sum(buys.values()) or 1.0
        sig = {"ts": T[trig], "ath_mult": round(ath / L0, 3), "tijd_tot_top_s": round(T[ath_i] - created_ts), "dip_duur_s": round(T[trig] - T[ath_i]),
               "kopers_tot_top": len(buys), "verkopen_tot_top": n_sells, "tussendips_15pct": pullbacks,
               "grootste_koper_aandeel": round(max(buys.values()) / tot_buy, 3) if buys else None,
               "gescreend_voor_signaal": bool(screened_ts and screened_ts <= T[trig])}
        # claim uit de video: na de dip kopen mensen hem weer +45% omhoog
        low = P[trig]; up45 = None; deeper10 = False
        for i in range(trig, len(rows)):
            if T[i] > T[trig] + HOLD_S: break
            if P[i] <= P[trig] * 0.90 and up45 is None: deeper10 = True
            low = min(low, P[i])
            if P[i] >= P[trig] * 1.45: up45 = round(T[i] - T[trig]); break
        sig["herstel_45_vanaf_signaal_s"] = up45; sig["eerst_10pct_dieper"] = deeper10
        # instappen: direct, of na 5% herstel vanaf het dieptepunt (zoals de live bot)
        entries = {"direct": T[trig] + C.FILL_DELAY_S}
        lo = P[trig]; conf = None
        for i in range(trig, len(rows)):
            if T[i] > T[trig] + 1800: break
            if P[i] >= ath: break
            lo = min(lo, P[i])
            if P[i] >= lo * (1 + C.REBOUND_PCT): conf = T[i] + C.FILL_DELAY_S; break
        if conf: entries["herstel5"] = conf
        res = {}
        for mode, t_fill in entries.items():
            vs, vt, fi = state(t_fill); pe = px(vs, vt)
            if pe <= 0: continue
            tok, _ = curve.buy(vs, vt, SIZE, "pp")
            for rule in ("video", "video_strikt", "trail"):
                exit_t, reason, peak, minp = t_fill + HOLD_S, "tijd", pe, pe
                for i in range(fi + 1, len(rows)):
                    if T[i] <= t_fill: continue
                    if T[i] > t_fill + HOLD_S: break
                    p = P[i]; peak = max(peak, p); minp = min(minp, p)
                    if rule == "video" and (p <= pe * (1 - C.V1_STOP_MARGIN) or p >= pe * (1 + C.V1_TP)):
                        exit_t, reason = T[i] + C.FILL_DELAY_S, "stop" if p < pe else "winst"; break
                    if rule == "video_strikt" and (p < pe * 0.995 or p >= pe * (1 + C.V1_TP)):
                        exit_t, reason = T[i] + C.FILL_DELAY_S, "stop" if p < pe else "winst"; break
                    if rule == "trail" and (p <= pe * (1 - C.V2_STOP) or (peak > pe and p <= peak * (1 - C.V2_TRAIL))):
                        exit_t, reason = T[i] + C.FILL_DELAY_S, "stop" if p < pe else "trail"; break
                if reason == "tijd" and T[-1] < t_fill + HOLD_S: reason = "data_eindigt"
                vs2, vt2, _ = state(exit_t); sol, _ = curve.sell(vs2, vt2, tok, "pp")
                res[f"{mode}|{rule}"] = {"ret": round((sol - SIZE - C.PRIO_FEE_SOL) / SIZE, 4), "reden": reason,
                                         "houd_s": round(exit_t - t_fill), "rug": minp <= pe * 0.2}
        sig["uitkomst"] = res
        out["signalen"][f"d{int(d * 100)}"] = sig
    return out


# ----------------------------------------------------------------- samenvatten
def filt_sets(tok):
    """Welke filters haalt dit token? tok: dict met feat, screen, gescreend_voor_signaal (per signaal apart)."""
    return tok


def summarize(rets):
    if not rets: return {"n": 0}
    n = len(rets); m = sum(rets) / n
    sd = statistics.stdev(rets) if n > 1 else 0.0
    return {"n": n, "winkans": round(sum(1 for r in rets if r > 0) / n, 3), "ev": round(m, 4), "mediaan": round(statistics.median(rets), 4),
            "ev_95_laag": round(m - 1.96 * sd / math.sqrt(n), 4) if n > 1 else None, "ev_95_hoog": round(m + 1.96 * sd / math.sqrt(n), 4) if n > 1 else None}


def build_report(items, cover):
    """items: lijst van (mint, data, screen) met screen = dict(pass, fs, h_ok, h_done, x)."""
    FILTERS = {
        "alle": lambda f, s, sig: True,
        "schoon": lambda f, s, sig: not f["bundelgrafiek"],
        "bundelgrafiek": lambda f, s, sig: f["bundelgrafiek"],
        "schoon+houders_ok": lambda f, s, sig: not f["bundelgrafiek"] and sig["gescreend_voor_signaal"] and s["h_done"] and s["h_ok"],
        "schoon+houders_ok+final_stretch": lambda f, s, sig: not f["bundelgrafiek"] and sig["gescreend_voor_signaal"] and s["h_done"] and s["h_ok"] and s["fs"],
        "volledige_screening+schoon": lambda f, s, sig: not f["bundelgrafiek"] and sig["gescreend_voor_signaal"] and s["pass"],
        "volledige_screening+schoon+x_link": lambda f, s, sig: not f["bundelgrafiek"] and sig["gescreend_voor_signaal"] and s["pass"] and s["x"],
    }
    VARS = [("d40", "direct"), ("d45", "direct"), ("d50", "direct"), ("d45", "herstel5")]
    grid = {}
    for fname, fn in FILTERS.items():
        grid[fname] = {}
        for d, mode in VARS:
            for rule in ("video", "video_strikt", "trail"):
                rets = [data["signalen"][d]["uitkomst"][f"{mode}|{rule}"]["ret"] for _, data, s in items
                        if d in data["signalen"] and f"{mode}|{rule}" in data["signalen"][d]["uitkomst"] and fn(data["feat"], s, data["signalen"][d])]
                grid[fname][f"{d}_{mode}|{rule}"] = summarize(rets)
    # claim: herstel +45% na een 45%-dip
    claim = {}
    for fname in ("alle", "schoon", "bundelgrafiek", "schoon+houders_ok"):
        fn = FILTERS[fname]
        sigs = [data["signalen"]["d45"] for _, data, s in items if "d45" in data["signalen"] and fn(data["feat"], s, data["signalen"]["d45"])]
        if sigs:
            claim[fname] = {"n": len(sigs), "herstelt_45pct_binnen_60m": round(sum(1 for x in sigs if x["herstel_45_vanaf_signaal_s"] is not None) / len(sigs), 3),
                            "zakt_eerst_10pct_verder": round(sum(1 for x in sigs if x["eerst_10pct_dieper"]) / len(sigs), 3),
                            "rug_tijdens_positie": round(sum(1 for x in sigs if x["uitkomst"].get("direct|video", {}).get("rug")) / len(sigs), 3)}
    # verkennend: kenmerken van de aanloop (d45, direct, videoregel, alle tokens)
    base = [(data, s) for _, data, s in items if "d45" in data["signalen"] and "direct|video" in data["signalen"]["d45"]["uitkomst"]]
    def bucket(name, getter, edges, labels):
        out = {}
        for lab in labels: out[lab] = []
        for data, s in base:
            v = getter(data)
            if v is None: continue
            k = labels[bisect.bisect_right(edges, v)]
            out[k].append(data["signalen"]["d45"]["uitkomst"]["direct|video"]["ret"])
        return {"kenmerk": name, "groepen": {k: summarize(v) for k, v in out.items()}}
    sigf = lambda key: (lambda data: data["signalen"]["d45"].get(key))
    featf = lambda key: (lambda data: data["feat"].get(key))
    expl = [
        bucket("max koers vóór eerste verkoop (x start)", featf("mult_voor_eerste_verkoop"), [1.3, 2.0], ["< 1,3x", "1,3–2x", "≥ 2x (bundelgrafiek)"]),
        bucket("aandeel supply gekocht in creatieblok", featf("blok0_pct"), [5, 20], ["< 5%", "5–20%", "≥ 20%"]),
        bucket("top t.o.v. start", sigf("ath_mult"), [3, 6], ["2–3x", "3–6x", "≥ 6x"]),
        bucket("unieke kopers tot de top", sigf("kopers_tot_top"), [30, 100], ["< 30", "30–100", "≥ 100"]),
        bucket("tussentijdse dips ≥ 15% tot de top", sigf("tussendips_15pct"), [1, 3], ["0 (rechte lijn)", "1–2", "≥ 3 (trap)"]),
        bucket("grootste koper, aandeel koopvolume", sigf("grootste_koper_aandeel"), [0.1, 0.25], ["< 10%", "10–25%", "≥ 25%"]),
        bucket("duur van top naar dip", sigf("dip_duur_s"), [30, 180], ["< 30 s (crash)", "30 s–3 min", "≥ 3 min (langzaam)"]),
        bucket("tijd van start tot top", sigf("tijd_tot_top_s"), [120, 600], ["< 2 min", "2–10 min", "≥ 10 min"]),
    ]
    prim = grid[PRIMARY[2]][f"{PRIMARY[0]}|{PRIMARY[1]}"]
    return {"dekking": cover, "primair": {"definitie": "dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap",
                                          **prim}, "raster": grid, "claim_45_herstel": claim, "verkennend": expl}


def to_md(rep):
    L = []; add = L.append; c = rep["dekking"]
    add(f"# Videostrategie op alle trades — {rep['gegenereerd']}\n")
    add(f"Tokens sinds {c['sinds']}: {c['tokens_geschikt']} geschikt (≥ 2 uur oud, geen herstart), {c['met_trades']} met trades, "
        f"{c['top_2x']} haalden 2x de startkoers, {c['met_d45']} kregen een 45%-dip binnen het eerste uur. "
        f"Bundelgrafiek (≥ 2x vóór de eerste verkoop): {c['bundelgrafieken']} tokens. "
        f"Houdercheck echt uitgevoerd bij {pct(c['houdercheck_uitgevoerd'])} van de gescreende tokens.\n")
    p = rep["primair"]
    add("## Hoofdtoets (vooraf vastgelegd)\n")
    add(f"{p['definitie']}.\n")
    if p.get("n"):
        add(f"**n = {p['n']}, winkans {p['winkans']:.0%}, EV per trade {p['ev']:+.1%} (95%-marge {p['ev_95_laag']:+.1%} tot {p['ev_95_hoog']:+.1%}), mediaan {p['mediaan']:+.1%}.** "
            "Drempel uit het bouwplan: EV ≥ +3% bij ≥ 500 trades.\n" if p.get("ev_95_laag") is not None else f"n = {p['n']}, EV {p['ev']:+.1%}.\n")
    else:
        add("Nog geen trades die aan alle voorwaarden voldoen.\n")
    add("## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?\n")
    add("| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |"); add("|---|---|---|---|---|")
    for k, v in rep["claim_45_herstel"].items():
        add(f"| {k} | {v['n']} | {v['herstelt_45pct_binnen_60m']:.0%} | {v['zakt_eerst_10pct_verder']:.0%} | {v['rug_tijdens_positie']:.0%} |")
    add("\n## Raster: EV per trade (n) — videoregel\n")
    cols = ["d40_direct", "d45_direct", "d50_direct", "d45_herstel5"]
    add("| filter | " + " | ".join(cols) + " |"); add("|---|" + "---|" * len(cols))
    for fname, g in rep["raster"].items():
        add(f"| {fname} | " + " | ".join(fmt_cell(g[f"{c_}|video"]) for c_ in cols) + " |")
    add("\n## Uitstapregels vergeleken (dip 45%, direct)\n")
    add("| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) |"); add("|---|---|---|---|")
    for fname, g in rep["raster"].items():
        add(f"| {fname} | {fmt_cell(g['d45_direct|video'])} | {fmt_cell(g['d45_direct|video_strikt'])} | {fmt_cell(g['d45_direct|trail'])} |")
    add("\n## Verkennend: kenmerken van het koersverloop tot de dip (dip 45%, direct, videoregel, alle tokens)\n")
    add("Niet gebruiken als nieuwe regel zonder aparte toets op nieuwe data: met veel indelingen vind je altijd wel een groep die toevallig goed uitvalt.\n")
    for e in rep["verkennend"]:
        add(f"**{e['kenmerk']}:** " + "; ".join(f"{k}: {fmt_cell(v)}" for k, v in e["groepen"].items()) + "\n")
    add("## Beperkingen\n")
    for b in rep["beperkingen"]: add(f"- {b}")
    return "\n".join(L) + "\n"


def fmt_cell(s): return "–" if not s or not s.get("n") else f"{s['ev']:+.1%} ({s['n']}, {s['winkans']:.0%} win)"
def pct(x): return "–" if x is None else f"{x:.0%}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH)
    ap.add_argument("--ledger", default=os.path.join(os.path.dirname(C.DB_PATH) or ".", "ledger.sqlite"))
    ap.add_argument("--out", default=C.REPORT_DIR)
    ap.add_argument("--now", type=float, default=None)
    args = ap.parse_args()
    now = args.now or time.time(); t0 = time.time()
    db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=60)
    start = meta_get(db, "full_trade_log_since"); os.makedirs(args.out, exist_ok=True)
    if not start:
        with open(os.path.join(args.out, "video_replay.md"), "w") as f: f.write("# Videostrategie\n\nVolledige trade-logging is nog niet actief.\n")
        return
    starts = sorted(s for s in meta_get(db, "bot_starts", []) if s > start + 60)
    led = sqlite3.connect(args.ledger, timeout=60)
    led.execute("CREATE TABLE IF NOT EXISTS replay(mint TEXT PRIMARY KEY, versie TEXT, data TEXT)")
    toks = db.execute("""SELECT mint, created_ts, create_slot, creator, screened_ts, screen_pass, screen_json, has_x_link FROM tokens
                         WHERE created_ts >= ? AND created_ts <= ?""", (start, now - 2 * 3600 - 300)).fetchall()
    cached = {m: json.loads(d) for m, v, d in led.execute("SELECT mint, versie, data FROM replay") if v == VERSIE}
    items = []; n_new = n_gap = n_trades = 0; screened = h_done = 0
    for mint, cts, slot, creator, scr_ts, spass, sjson, xl in toks:
        i = bisect.bisect_left(starts, cts)
        if i < len(starts) and starts[i] < cts + C.LOG_MAX_AGE_S: n_gap += 1; continue
        if mint in cached: data = cached[mint]
        else:
            rows = db.execute("SELECT ts, slot, user, is_buy, sol, tokens, v_sol, v_tok FROM trades INDEXED BY trades_mint_ts WHERE mint = ? ORDER BY ts",
                              (mint,)).fetchall()
            data = analyse_token(rows, cts, slot, creator, scr_ts) or {"feat": None, "signalen": {}}
            led.execute("INSERT OR REPLACE INTO replay VALUES(?,?,?)", (mint, VERSIE, json.dumps(data))); n_new += 1
            if n_new % 2000 == 0: led.commit(); log(f"  {n_new} nieuwe tokens doorgerekend")
        if not data.get("feat"): continue
        n_trades += 1
        sj = json.loads(sjson) if sjson else {}
        if sjson: screened += 1
        done = bool(sj.get("top5"))
        if sjson and done: h_done += 1
        screen = {"pass": bool(spass), "fs": bool(sj.get("fs_rules_pass")), "h_done": done,
                  "h_ok": done and not sj.get("check1a_flag") and not sj.get("check1b_flag"), "x": bool(xl)}
        items.append((mint, data, screen))
    led.commit()
    cover = {"sinds": iso(start), "tokens_geschikt": len(toks) - n_gap, "overgeslagen_herstart": n_gap, "met_trades": n_trades,
             "top_2x": sum(1 for _, d, _ in items if d["feat"]["max_mult"] >= ATH_MULT),
             "met_d45": sum(1 for _, d, _ in items if "d45" in d["signalen"]),
             "bundelgrafieken": sum(1 for _, d, _ in items if d["feat"]["bundelgrafiek"]),
             "houdercheck_uitgevoerd": round(h_done / screened, 3) if screened else None, "nieuw_doorgerekend": n_new}
    rep = build_report(items, cover)
    rep["gegenereerd"] = iso(now); rep["versie"] = VERSIE
    rep["beperkingen"] = [
        "De community-check uit de video (CA in bio, vastgepinde post, echte activiteit op X) wordt niet gemeten; alleen of er een X-link is.",
        "'Bundelgrafiek' is hier: ≥ 2x de startkoers vóór de eerste verkoop door iemand anders dan de dev. Dat is de letterlijke omschrijving uit de video, maar een benadering.",
        "De houdercheck (gelijke saldi, zelfde funding-tijd) mislukt bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'.",
        "Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.",
        "Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.",
    ]
    with open(os.path.join(args.out, "video_replay.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "video_replay.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s: {len(items)} tokens, {n_new} nieuw -> {args.out}/video_replay.md")


if __name__ == "__main__":
    main()
