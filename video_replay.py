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

VERSIE = "replay-v6-h4-gespreid"    # v6: regel H4 en gespreid uitstappen erbij
# De reeks loopt door tot 80%: bij 60% boog de EV nog niet af, dus het omslagpunt lag buiten beeld.
# Verder dan 80% heeft geen zin — dan zit je in rug-gebied en is er geen koers meer om op in te stappen.
DIPS = [0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]
ATH_MULT = C.ATH_MIN_MULT            # top moet minstens 2x de startkoers zijn (video: 4-5K -> 10K)
TRIGGER_MAX_AGE_S = 3600             # dip moet binnen het eerste uur vallen (zoals de live simulatie)
HOLD_S = 3600
SIZE = 0.2
# Hoe ver terug de replay kijkt. Dit stond open, en daardoor groeide hij mee met de database: op
# 15 sept ging het om 130.000 tokens en liep hij vier rondes achter elkaar vast zonder één logregel
# — het geheugen ging op aan de cache en aan de lijst met per-token uitkomsten. De lopende toets
# (H4, vastgelegd 14 sept 22:00) heeft maar twee dagen nodig. Gevolg dat je moet weten: het raster
# en de hoofdtoets in latere rapporten rusten op minder tokens dan die van 15 sept 09:38.
REPLAY_DAGEN = float(os.getenv("REPLAY_DAGEN", 2.5))
SIZES = [float(x) for x in os.getenv("REPLAY_SIZES", "0.05,0.2,1.0").split(",")]
# Winstgrenzen om te toetsen of de +45% uit de video wel gehaald wordt, en of een lagere grens beter is.
TP_LADDER = sorted({0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.45, 0.60} | {C.V1_TP})

# Regel van Gerben (13 sept): instappen na een dip van 55% vanaf de top, stop als de koers 65%
# onder die top staat, winst nemen op +30%, en zodra +20% is aangetikt de stop naar de instapprijs.
# De stop is dus een absoluut koersniveau (t.o.v. de top), niet een percentage onder de instap:
# instap op ATH x 0,45 en stop op ATH x 0,35 betekent ruim 22% ruimte onder de instap. Precies
# daarom kan deze regel werken waar de videoregel faalt: 76% van de dips zakt éérst nog 10% verder,
# en een stop van 3% onder de instap wordt daar altijd door weggeslagen.
G_STOP_VANAF_TOP = 0.65
G_STOP_EXTRA = 0.10                  # zie hieronder
G_TP = 0.30
G_BREAKEVEN = 0.20

# Regel H4 (voorstel Gerben, 14 sept): dieper instappen en niet op een vaste winst uitstappen maar
# de winst laten lopen achter een meelopende stop. Tot +15% ligt de stop op hetzelfde absolute
# niveau als bij H3 — tien procentpunt dieper dan de instap — zodat de positie ruimte heeft om
# eerst nog te zakken. Vanaf +15% loopt de stop mee op 10% onder de hoogste koers sindsdien.
# Omdat de stop pas meeloopt vanaf +15%, ligt hij dan altijd boven de instapprijs (1,15 x 0,90 =
# 1,035), dus vanaf dat moment kan de trade niet meer met verlies eindigen, afgezien van kosten.
H4_ARM = 0.15                        # vanaf deze winst gaat de trailing stop lopen
H4_TRAIL = 0.10                      # en volgt dan op zoveel onder de piek

# Gespreid uitstappen, zoals de KOL-video van 14 sept aanraadt: niet in één keer verkopen maar in
# plakjes op de weg omhoog. Dat is exact het gewogen gemiddelde van de losse winstgrenzen: elk deel
# van de positie gedraagt zich als de enkelvoudige regel met díe grens en dezelfde stop. Daarom is
# het hier uit te rekenen zonder de koersen opnieuw te doorlopen — en daarom kan het de verwachting
# ook niet redden: het gemiddelde van vier negatieve getallen is negatief. Wat het wél verandert is
# de spreiding. Aanname: de deelverkopen bewegen de koers niet, wat bij deze inzetgroottes klopt.
GESPREID = [0.10, 0.20, 0.30, 0.45]      # vier gelijke plakjes op deze winstgrenzen


def g_stop_niveau_van(ath, d):
    """Stopniveau bij een instap op dipdiepte `d`.

    Gerben gaf de regel voor één diepte: instap op 55%, stop op 65% vanaf de top — tien
    procentpunt dieper. Bij het doorzoeken van álle dieptes moet die verhouding meebewegen,
    anders ligt de stop bij een instap dieper dan 65% bóven de instapprijs en word je meteen
    uitgestopt. Daarom: stop altijd 10 procentpunt dieper dan de instap. Bij d = 0,55 komt dat
    exact uit op de 65% die hij noemde; H3 is op die diepte vastgelegd en verandert dus niet.

    Gevolg dat je moet weten: de stop wordt in relatieve zin ruimer naarmate je dieper instapt.
    Bij 55% ligt hij 22% onder de instap, bij 70% al 33%. Diepere cellen nemen dus meer risico
    per trade; de EV's zijn daardoor niet één op één vergelijkbaar."""
    return ath * (1 - min(0.95, d + G_STOP_EXTRA))
BUNDLE_CANDLE_MULT = 2.0             # video: één groene candle van 5K naar 10K zonder verkopen
PRIMARY = ("d45_direct", "video", "schoon+houders_ok")
# Hypothesen die later zijn vastgelegd, na het zien van eerdere resultaten. Ze tellen alleen op tokens die ná het
# vastleggen ontstonden; alles daarvoor zou de hypothese bevestigen met de data waaruit ze komt.
HYPOTHESEN = [
    {"id": "H2", "vastgelegd_ts": 1789138800, "vastgelegd": "2026-09-11 15:00 UTC",
     "definitie": "dip 45% vanaf top, direct instappen, trailing stop (-10% onder instap of 20% onder de piek), schone grafiek",
     "variant": "d45", "sleutel": "direct|trail", "filter": "schoon",
     "aanleiding": "+8,6% EV op 135 trades in de run van 11 sept 14:02 UTC, één van 84 combinaties"},
    {"id": "H3", "vastgelegd_ts": 1789279200, "vastgelegd": "2026-09-13 06:00 UTC",
     "definitie": "instap na een dip van 55% vanaf de top, stop als de koers 65% onder die top staat, "
                  "winst nemen op +30%, en bij +20% de stop naar de instapprijs — volledige screening",
     "variant": "d55", "sleutel": "direct|gerben", "filter": "volledige_screening+schoon",
     "aanleiding": "voorstel van Gerben, 13 sept. Oorzakelijk: de videoregel faalt niet op het doel maar op de stop — "
                   "76% van de dips zakt eerst nog 10% verder, en een stop 3% onder de instap wordt daar altijd door "
                   "geraakt. Deze regel geeft de positie ruim 22% ruimte onder de instap en neemt eerder winst."},
    {"id": "H4", "vastgelegd_ts": 1789423200, "vastgelegd": "2026-09-14 22:00 UTC",
     "definitie": "instap na een dip van 65% vanaf de top; stop op 75% onder de top zolang de winst onder +15% blijft; "
                  "vanaf +15% een meelopende stop op 10% onder de hoogste koers; schone grafiek en houdercheck in orde",
     "variant": "d65", "sleutel": "direct|h4", "filter": "schoon+houders_ok",
     "aanleiding": "voorstel van Gerben, 14 sept. Combineert de twee hefbomen die los gemeten het minst slecht waren: "
                   "dieper instappen (d65-d70 gaf -3,8% tot -4,7% tegen -6,9% bij d45) en eerder winst vastleggen "
                   "(+10% gaf -5,4% tegen -6,9% bij +45%), maar dan met een meelopende stop zodat een uitschieter niet "
                   "wordt afgekapt. Filter is 'schoon+houders_ok' en niet de volledige screening, omdat die screening "
                   "in drie onafhankelijke metingen averechts werkt. Verwachting vooraf, zodat die toetsbaar is: "
                   "rond -3%, dus nog steeds negatief."},
]


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
            # Eén keer door het venster, en daaruit volgt álles: wanneer raakt de koers elke
            # winstgrens, wanneer de stop, en hoe hoog komt hij maximaal. Zo is te zien of de
            # +45% uit de video überhaupt gehaald wordt, en of dat gebeurt vóórdat de stop je
            # eruit gooit — dat laatste is wat telt, want de stop ligt maar 3% onder de instap.
            t_stop = t_strikt = t_trail = None; t_tp = {}; peak = minp = pe
            g_stop_niveau = g_stop_niveau_van(ath, d)          # 10 procentpunt dieper dan de instap
            t_g = None; g_reden = "tijd"; g_be = False        # g_be: stop staat op de instapprijs
            t_h4 = None; h4_reden = "tijd"; h4_aan = False    # h4_aan: de trailing stop loopt
            for i in range(fi + 1, len(rows)):
                if T[i] <= t_fill: continue
                if T[i] > t_fill + HOLD_S: break
                p = P[i]; peak = max(peak, p); minp = min(minp, p)
                if t_stop is None and p <= pe * (1 - C.V1_STOP_MARGIN): t_stop = T[i]
                if t_strikt is None and p < pe * 0.995: t_strikt = T[i]
                if t_trail is None and (p <= pe * (1 - C.V2_STOP) or (peak > pe and p <= peak * (1 - C.V2_TRAIL))): t_trail = T[i]
                for tp in TP_LADDER:
                    if tp not in t_tp and p >= pe * (1 + tp): t_tp[tp] = T[i]
                if t_g is None:
                    if not g_be and p >= pe * (1 + G_BREAKEVEN): g_be = True    # stop verschuift naar instap
                    niveau = pe if g_be else g_stop_niveau
                    if p >= pe * (1 + G_TP): t_g, g_reden = T[i], "winst"
                    elif p <= niveau: t_g, g_reden = T[i], "breakeven" if g_be else "stop"
                if t_h4 is None:
                    if not h4_aan and p >= pe * (1 + H4_ARM): h4_aan = True
                    niveau4 = peak * (1 - H4_TRAIL) if h4_aan else g_stop_niveau
                    if p <= niveau4: t_h4, h4_reden = T[i], "trail" if h4_aan else "stop"
            sig.setdefault("max_stijging", {})[mode] = round(peak / pe - 1, 4)
            # haalt hij de winstgrens, en haalt hij hem vóór de stop?
            sig.setdefault("haalt", {})[mode] = {
                f"tp{int(tp * 100)}": {"ooit": tp in t_tp,
                                       "voor_stop": tp in t_tp and (t_stop is None or t_tp[tp] <= t_stop)}
                for tp in TP_LADDER}

            def sluit(t_uit, reden, met_per_inzet=False):
                exit_t = (t_uit + C.FILL_DELAY_S) if t_uit is not None else t_fill + HOLD_S
                if t_uit is None and T[-1] < t_fill + HOLD_S: reden = "data_eindigt"
                vs2, vt2, _ = state(exit_t)
                sol, _ = curve.sell(vs2, vt2, tok, "pp")
                d_ = {"ret": round((sol - SIZE - C.PRIO_FEE_SOL) / SIZE, 4), "reden": reden,
                      "houd_s": round(exit_t - t_fill), "rug": minp <= pe * 0.2}
                if met_per_inzet:
                    # Bouwplan §2 stap E: drie inzetgroottes, twee terminals. Alleen voor de videoregel,
                    # want dat is de cel waarop het oordeel rust; overal doen is nodeloos zwaar.
                    per = {}
                    for sz in SIZES:
                        for term in C.FEE_TERMINAL:
                            tk, _ = curve.buy(vs, vt, sz, term)
                            uit, _ = curve.sell(vs2, vt2, tk, term)
                            per[f"{sz}_{term}"] = round((uit - sz - C.PRIO_FEE_SOL) / sz, 4)
                    d_["per_inzet"] = per
                return d_

            def eerste(*kandidaten):
                """Vroegste moment dat telt, met de reden die erbij hoort."""
                geldig = [(t, r) for t, r in kandidaten if t is not None]
                return min(geldig, key=lambda x: x[0]) if geldig else (None, "tijd")

            t, r = eerste((t_stop, "stop"), (t_tp.get(C.V1_TP), "winst"))
            res[f"{mode}|video"] = sluit(t, r, met_per_inzet=True)
            t, r = eerste((t_strikt, "stop"), (t_tp.get(C.V1_TP), "winst"))
            res[f"{mode}|video_strikt"] = sluit(t, r)
            res[f"{mode}|trail"] = sluit(t_trail, "trail" if t_trail is not None else "tijd")
            res[f"{mode}|gerben"] = sluit(t_g, g_reden)
            res[f"{mode}|h4"] = sluit(t_h4, h4_reden)
            # winst nemen op een lagere grens, met dezelfde stop als de video
            for tp in TP_LADDER:
                t, r = eerste((t_stop, "stop"), (t_tp.get(tp), "winst"))
                res[f"{mode}|tp{int(tp * 100)}"] = sluit(t, r)
            # gespreid: vier gelijke plakjes op vier grenzen, allemaal met dezelfde stop
            delen = [res[f"{mode}|tp{int(tp * 100)}"] for tp in GESPREID if f"{mode}|tp{int(tp * 100)}" in res]
            if len(delen) == len(GESPREID):
                res[f"{mode}|gespreid"] = {"ret": round(sum(d["ret"] for d in delen) / len(delen), 4),
                                           "reden": "gespreid", "houd_s": max(d["houd_s"] for d in delen),
                                           "rug": delen[0]["rug"]}
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
    VARS = [(f"d{int(d * 100)}", "direct") for d in DIPS] + [("d45", "herstel5")]
    grid = {}
    for fname, fn in FILTERS.items():
        grid[fname] = {}
        for d, mode in VARS:
            for rule in ("video", "video_strikt", "trail", "gerben", "h4", "gespreid"):
                rets = [data["signalen"][d]["uitkomst"][f"{mode}|{rule}"]["ret"] for _, data, s in items
                        if d in data["signalen"] and f"{mode}|{rule}" in data["signalen"][d]["uitkomst"] and fn(data["feat"], s, data["signalen"][d])]
                grid[fname][f"{d}_{mode}|{rule}"] = summarize(rets)
    # De kernvraag: haalt de koers na de dip die +45% wel? En zo nee, helpt een lagere winstgrens?
    # 'ooit' = de grens wordt binnen het uur geraakt. 'voor_stop' = geraakt vóórdat de koers 3%
    # onder de instap zakte, want dan pas kun je hem ook echt pakken — dat is het verschil tussen
    # een mooie claim en een uitvoerbare regel.
    grenzen = {}
    for fname in ("volledige_screening+schoon", "schoon+houders_ok", "alle"):
        fn = FILTERS[fname]; grenzen[fname] = {}
        for d, mode in VARS:
            sigs = [data["signalen"][d] for _, data, s in items
                    if d in data["signalen"] and fn(data["feat"], s, data["signalen"][d])
                    and mode in (data["signalen"][d].get("haalt") or {})]
            if not sigs: continue
            rij = {"n": len(sigs),
                   "max_stijging_mediaan": round(statistics.median([x["max_stijging"][mode] for x in sigs]), 4)}
            for tp in TP_LADDER:
                k = f"tp{int(tp * 100)}"
                ooit = sum(1 for x in sigs if x["haalt"][mode][k]["ooit"])
                voor = sum(1 for x in sigs if x["haalt"][mode][k]["voor_stop"])
                rets = [x["uitkomst"][f"{mode}|{k}"]["ret"] for x in sigs if f"{mode}|{k}" in x["uitkomst"]]
                rij[k] = {"ooit": round(ooit / len(sigs), 3), "voor_stop": round(voor / len(sigs), 3),
                          **(summarize(rets) if rets else {"n": 0})}
            grenzen[fname][f"{d}_{mode}"] = rij

    # Alle inzetgroottes x terminals voor de filters die er voor het oordeel toe doen. Het bouwplan
    # schrijft dit voor; tot 13 sept werd alleen 0,2 SOL / PumpPortal getoond.
    per_inzet = {}
    for fname in ("volledige_screening+schoon", "schoon+houders_ok", "alle"):
        fn = FILTERS[fname]; per_inzet[fname] = {}
        for d, mode in VARS:
            sleutel = f"{mode}|video"
            uitk = [data["signalen"][d]["uitkomst"][sleutel] for _, data, s in items
                    if d in data["signalen"] and sleutel in data["signalen"][d]["uitkomst"] and fn(data["feat"], s, data["signalen"][d])]
            if not uitk: continue
            cel = {}
            for sz in SIZES:
                for term in C.FEE_TERMINAL:
                    k = f"{sz}_{term}"
                    rets = [u["per_inzet"][k] for u in uitk if "per_inzet" in u and k in u["per_inzet"]]
                    if rets: cel[k] = summarize(rets)
            if cel: per_inzet[fname][f"{d}_{mode}"] = cel

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
    hyp = []
    for h in HYPOTHESEN:
        fn = FILTERS[h["filter"]]
        rets = [data["signalen"][h["variant"]]["uitkomst"][h["sleutel"]]["ret"] for _, data, s in items
                if s.get("created_ts", 0) >= h["vastgelegd_ts"] and h["variant"] in data["signalen"]
                and h["sleutel"] in data["signalen"][h["variant"]]["uitkomst"] and fn(data["feat"], s, data["signalen"][h["variant"]])]
        hyp.append({**{k: v for k, v in h.items() if k != "vastgelegd_ts"}, **summarize(rets)})
    return {"dekking": cover, "primair": {"definitie": "dip 45% vanaf top, direct instappen, uit bij -3% onder instap of +45%, schone grafiek en houdercheck uitgevoerd en in orde vóór instap",
                                          **prim}, "hypothesen": hyp, "raster": grid, "per_inzet": per_inzet, "winstgrenzen": grenzen, "claim_45_herstel": claim, "verkennend": expl}


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
    add("## Later vastgelegde hypothesen (alleen tokens van ná het vastleggen)\n")
    for h in rep.get("hypothesen", []):
        res = (f"n = {h['n']}, winkans {h['winkans']:.0%}, EV {h['ev']:+.1%}" + (f" (95%-marge {h['ev_95_laag']:+.1%} tot {h['ev_95_hoog']:+.1%})" if h.get("ev_95_laag") is not None else "")
               if h.get("n") else "nog geen trades")
        add(f"- **{h['id']}** ({h['vastgelegd']}): {h['definitie']}. Aanleiding: {h['aanleiding']}. Resultaat: {res}.")
    add("")
    add("## Klopt de claim 'na 45% dip gaat hij weer 45% omhoog, elke keer'?\n")
    add("| groep | 45%-dips | herstelt +45% binnen 60 min | zakt eerst nog 10% verder | rug tijdens positie |"); add("|---|---|---|---|---|")
    for k, v in rep["claim_45_herstel"].items():
        add(f"| {k} | {v['n']} | {v['herstelt_45pct_binnen_60m']:.0%} | {v['zakt_eerst_10pct_verder']:.0%} | {v['rug_tijdens_positie']:.0%} |")
    add("\n## Raster: EV per trade (n) — videoregel, dipdiepte 30% t/m 60%\n")
    cols = [f"d{int(d * 100)}_direct" for d in DIPS] + ["d45_herstel5"]
    add("| filter | " + " | ".join(cols) + " |"); add("|---|" + "---|" * len(cols))
    for fname, g in rep["raster"].items():
        add(f"| {fname} | " + " | ".join(fmt_cell(g.get(f"{c_}|video")) for c_ in cols) + " |")
    add("\n## Regel van Gerben: dip 55%, stop op 65% vanaf de top, winst op +30%, breakeven bij +20%\n")
    add(f"De stop is een koersniveau t.o.v. de top, niet een percentage onder de instap: altijd "
        f"{G_STOP_EXTRA:.0%}-punt dieper dan de instap. Bij de 55%-instap is dat de 65% die Gerben noemde, ruim 22% "
        f"onder de instapprijs — waar de videoregel maar 3% ruimte geeft. Zodra +{G_BREAKEVEN:.0%} is aangetikt "
        f"schuift de stop naar de instapprijs, winst op +{G_TP:.0%}.\n")
    add("| instapdip | stop vanaf top | stop onder instap |"); add("|---|---|---|")
    for d in DIPS:
        add(f"| {d:.0%} | {min(0.95, d + G_STOP_EXTRA):.0%} | {(1 - min(0.95, d + G_STOP_EXTRA)) / (1 - d) - 1:+.0%} |")
    add("\nDieper instappen betekent dus ook meer risico per trade; de EV's hieronder zijn niet één op één "
        "vergelijkbaar. **Vooraf vastgelegd als H3 op de 55%-variant met volledige screening; de rest is verkennend.**\n")
    cols_g = [f"d{int(d * 100)}_direct" for d in DIPS]
    add("| filter | " + " | ".join(cols_g) + " |"); add("|---|" + "---|" * len(cols_g))
    for fname, g in rep["raster"].items():
        add(f"| {fname} | " + " | ".join(fmt_cell(g.get(f"{c_}|gerben")) for c_ in cols_g) + " |")
    add("")
    add(f"\n## Regel H4: dip 65%, trailing stop vanaf +{H4_ARM:.0%} op {H4_TRAIL:.0%} onder de piek\n")
    add(f"Tot +{H4_ARM:.0%} ligt de stop op hetzelfde niveau als bij de vorige regel — {G_STOP_EXTRA:.0%}-punt dieper "
        f"dan de instap — zodat de positie eerst nog kan zakken. Vanaf +{H4_ARM:.0%} loopt de stop mee op "
        f"{H4_TRAIL:.0%} onder de hoogste koers, en ligt daarmee altijd boven de instapprijs. Geen vaste winstgrens: "
        "een uitschieter wordt niet afgekapt.\n")
    add("**Vooraf vastgelegd als H4 op d65 met filter schoon+houders_ok; de rest van deze regel is verkennend.**\n")
    add("| filter | " + " | ".join(cols_g) + " |"); add("|---|" + "---|" * len(cols_g))
    for fname, g in rep["raster"].items():
        add(f"| {fname} | " + " | ".join(fmt_cell(g.get(f"{c_}|h4")) for c_ in cols_g) + " |")
    add("")
    add("\n## Verkennend: winstgrens tegen dipdiepte\n")
    add("Elke winstgrens bij elke instapdiepte, filter `schoon+houders_ok`, stop als in de video. Dit is het raster "
        f"waar {len(TP_LADDER)} grenzen x {len(DIPS)} dieptes = {len(TP_LADDER) * len(DIPS)} cellen uit komen. Bij zoveel "
        "cellen zit er door toeval altijd een goede tussen, dus **hier telt geen enkele cel als bewijs** — het is "
        "bedoeld om te zien of er ergens een gebied is dat consequent beter is, niet om de beste cel te kiezen.\n")
    gz = (rep.get("winstgrenzen") or {}).get("schoon+houders_ok") or {}
    if gz:
        kolommen = [f"d{int(d * 100)}_direct" for d in DIPS if f"d{int(d * 100)}_direct" in gz]
        add("| winstgrens | " + " | ".join(k.replace("_direct", "") for k in kolommen) + " |")
        add("|---|" + "---|" * len(kolommen))
        for tp in TP_LADDER:
            k = f"tp{int(tp * 100)}"
            rij = []
            for kol in kolommen:
                cel = (gz.get(kol) or {}).get(k) or {}
                rij.append(f"{cel['ev']:+.1%} ({cel['n']})" if cel.get("n") else "–")
            add(f"| +{tp:.0%} | " + " | ".join(rij) + " |")
        add("")
    add("\n## Wordt die +45% na de dip wel gehaald?\n")
    add("De claim uit de video is dat de koers na de dip weer 45% stijgt. Twee kolommen per winstgrens: "
        "**ooit** = de grens wordt binnen het uur geraakt; **vóór stop** = geraakt vóórdat de koers 3% onder de "
        "instap zakte. Alleen die tweede is te pakken — bij de eerste ben je al uitgestopt voordat de stijging komt. "
        "Daarachter de EV als je op die grens winst neemt, met dezelfde stop als de video.\n")
    for fname, per_var in (rep.get("winstgrenzen") or {}).items():
        var = f"d{int(C.DIP_VARIANTS[-1] * 100)}_direct" if f"d{int(C.DIP_VARIANTS[-1] * 100)}_direct" in per_var else None
        var = var or ("d45_direct" if "d45_direct" in per_var else next(iter(per_var), None))
        if not var: continue
        rij = per_var[var]
        add(f"**filter `{fname}`** — variant `{var}`, {rij['n']} instappen, mediane hoogste stijging "
            f"{rij['max_stijging_mediaan']:+.1%}\n")
        add("| winstgrens | haalt ooit | haalt vóór stop | EV met die grens | winkans |"); add("|---|---|---|---|---|")
        for tp in TP_LADDER:
            k = f"tp{int(tp * 100)}"; c = rij.get(k)
            if not c: continue
            ev = f"{c['ev']:+.1%}" if c.get("n") else "–"
            wk = f"{c['winkans']:.0%}" if c.get("n") else "–"
            add(f"| +{int(tp * 100)}% | {c['ooit']:.0%} | {c['voor_stop']:.0%} | {ev} | {wk} |")
        add("")
    add("\n## Alle inzetgroottes en beide terminals (videoregel)\n")
    add("Het bouwplan (§2, stap E) schrijft 0,05 / 0,2 / 1 SOL voor en beide terminals. Die werden berekend "
        "maar tot 13 sept nooit getoond, en het oordeel rustte op één van de zes cellen. Hier staan ze alle zes. "
        "Kleiner inzetten verlaagt de slippage maar laat de vaste prioriteitsfee zwaarder wegen.\n")
    kolommen = [f"{sz}_{t}" for sz in SIZES for t in C.FEE_TERMINAL]
    for fname, per_d in (rep.get("per_inzet") or {}).items():
        if not per_d: continue
        add(f"**filter `{fname}`**\n")
        add("| variant | " + " | ".join(kolommen) + " |"); add("|---|" + "---|" * len(kolommen))
        for var, cel in per_d.items():
            add(f"| {var} | " + " | ".join(fmt_cell(cel.get(k)) for k in kolommen) + " |")
        add("")
    # Kostengevoeligheid. De KOL-video van 14 sept gebruikt een tip van 0,02 SOL per transactie,
    # plus 0,001 prioriteitsfee. Wij rekenen met 0,001. Dat verschil is geen detail: een vaste fee
    # werkt lineair door in het rendement — elke extra T SOL per kant verlaagt het rendement met
    # precies 2T/inzet — dus het is exact uit te rekenen zonder iets opnieuw te simuleren.
    pi = (rep.get("per_inzet") or {}).get("schoon+houders_ok") or {}
    basis = pi.get(f"d{int(C.DIP_VARIANTS[-1] * 100)}_direct") or (pi.get("d45_direct") or {})
    if basis:
        add("\n## Wat kost de uitvoering echt?\n")
        add(f"Wij rekenen met {C.PRIO_FEE_SOL} SOL vaste kosten per transactie. De video van 14 sept gebruikt een "
            "tip van 0,02 SOL plus 0,001 prioriteitsfee — twintig keer zoveel. Een vaste fee werkt lineair door: "
            "elke extra T SOL per kant verlaagt het rendement met 2T gedeeld door de inzet. Onderstaande EV's zijn "
            "daarmee exact doorgerekend, niet opnieuw gesimuleerd. Filter `schoon+houders_ok`, videoregel, "
            "PumpPortal.\n")
        add("| extra vaste fee per transactie | " + " | ".join(f"inzet {sz} SOL" for sz in SIZES) + " |")
        add("|---|" + "---|" * len(SIZES))
        for extra in (0.0, 0.005, 0.01, 0.02):
            rij = []
            for sz in SIZES:
                cel = basis.get(f"{sz}_pp")
                rij.append(f"{cel['ev'] - 2 * extra / sz:+.1%}" if cel and cel.get("n") else "–")
            add(f"| +{extra} SOL | " + " | ".join(rij) + " |")
        add("\nBij 0,05 SOL inzet eet een tip van 0,02 SOL per kant 84% van de positie op. Een strategie met een "
            "randje van een paar procent bestaat bij die instellingen simpelweg niet; bij 1 SOL kost hij 4,2%. "
            "Dit verandert onze conclusie niet — de EV was al negatief — maar het laat zien dat kleine inzetten "
            "bij deze uitvoering sowieso kansloos zijn, en dat onze eigen cijfers aan de gunstige kant staan.\n")
    if True:
        add("")
    add("\n## Uitstapregels vergeleken (dip 45%, direct)\n")
    add(f"'Gespreid' is vier gelijke plakjes op +{GESPREID[0]:.0%}, +{GESPREID[1]:.0%}, +{GESPREID[2]:.0%} en "
        f"+{GESPREID[3]:.0%}, allemaal met dezelfde stop — het advies uit de KOL-video om niet in één keer te "
        "verkopen. Dat is rekenkundig het gewogen gemiddelde van de vier losse grenzen, dus het kan de verwachting "
        "niet redden; het verandert alleen de spreiding.\n")
    add("| filter | video (-3% / +45%) | strikt (onder instap / +45%) | trail (-10%, 20% vanaf piek) | gespreid |")
    add("|---|---|---|---|---|")
    for fname, g in rep["raster"].items():
        add(f"| {fname} | {fmt_cell(g['d45_direct|video'])} | {fmt_cell(g['d45_direct|video_strikt'])} | "
            f"{fmt_cell(g['d45_direct|trail'])} | {fmt_cell(g.get('d45_direct|gespreid'))} |")
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
    start = max(start, now - REPLAY_DAGEN * 86400)
    led = sqlite3.connect(args.ledger, timeout=60)
    led.execute("PRAGMA busy_timeout=60000")
    led.execute("CREATE TABLE IF NOT EXISTS replay(mint TEXT PRIMARY KEY, versie TEXT, data TEXT)")
    toks = db.execute("""SELECT mint, created_ts, create_slot, creator, screened_ts, screen_pass, screen_json, has_x_link FROM tokens
                         WHERE created_ts >= ? AND created_ts <= ?""", (start, now - 2 * 3600 - 300)).fetchall()
    log(f"venster {iso(start)} .. nu, {len(toks)} tokens")

    def uit_cache(mint):
        """Eén rij tegelijk opzoeken in plaats van de hele tabel inlezen. De oude versie parste
        álle 130.000 opgeslagen tokens naar Python-objecten vóór er iets berekend werd, ook de
        tokens die buiten het venster vielen. Dat was het geheugen."""
        r = led.execute("SELECT versie, data FROM replay WHERE mint = ?", (mint,)).fetchone()
        return json.loads(r[1]) if r and r[0] == VERSIE else None
    items = []; n_new = n_gap = n_trades = 0; screened = h_done = 0
    for mint, cts, slot, creator, scr_ts, spass, sjson, xl in toks:
        i = bisect.bisect_left(starts, cts)
        if i < len(starts) and starts[i] < cts + 2 * 3600: n_gap += 1; continue      # instap ≤ 1 u + houdtijd ≤ 1 u
        data = uit_cache(mint)
        if data is None:
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
        screen = {"pass": bool(spass), "fs": bool(sj.get("fs_rules_pass")), "h_done": done, "created_ts": cts,
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
        "Tot 11 sept ~15:00 UTC mislukte de houdercheck bij een deel van de tokens door een RPC-fout; die tokens tellen niet als 'houders ok'. Daarna probeert de bot het opnieuw en valt hij terug op de eigen tradestroom.",
        "Instap- en uitstapprijzen zijn berekend op de curve 2 s na het signaal. Mislukte transacties, MEV en andere kopers die tegelijk instappen zitten er niet in; de werkelijkheid is eerder slechter.",
        "Na migratie naar PumpSwap stopt de data; zo'n positie wordt gesloten op de laatste curveprijs.",
    ]
    with open(os.path.join(args.out, "video_replay.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "video_replay.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s: {len(items)} tokens, {n_new} nieuw -> {args.out}/video_replay.md")


if __name__ == "__main__":
    main()
