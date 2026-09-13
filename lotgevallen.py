#!/usr/bin/env python3
"""Wat is er van de tokens terechtgekomen?

Alle andere analyses kijken naar een raampje van hooguit een uur rond de instap. Deze kijkt naar
de afloop: welke tokens bestaan nog, welke zijn dood, welke zijn gerugd, welke zijn gemigreerd —
en of de screening uit de video dat voorspelt. Plus, voor de tokens die álle criteria haalden:
wat is hun koers nú, en wat had simpelweg kopen-en-vasthouden opgeleverd.

Twee bronnen, en het verschil is belangrijk:
 - Wat wij zagen: de bot logt trades tot ~6 uur na creatie. Daarna weten we niets meer.
 - Wat er nu is: opgehaald bij de keten. Voor tokens die nog op de curve staan is de koers af te
   leiden uit het saldo van de curve; voor gemigreerde tokens uit de pool.

De afgeleide koers wordt eerst gecontroleerd tegen wat we zelf zagen, bij tokens waar die twee
elkaar moeten overlappen. Klopt dat niet, dan wordt de koers niet gebruikt. Zonder die controle
is een prijs uit de keten net zo goed een gok als de restwaarde van 26.647 SOL van gisteren.

Gebruik:  python lotgevallen.py [--db ...] [--ledger ...] [--out reports]
"""
import argparse, json, math, os, sqlite3, statistics, time

import config as C

DOOD_NA_S = 6 * 3600            # geen trades meer sinds zoveel: dood op de curve
RUG_DALING = 0.80               # koers >= 80% onder de top: gerugd
KETEN_PER_RUN = int(os.getenv("LOT_KETEN", 120))    # tokens waarvan we de koers nú ophalen
KETEN_RPS = float(os.getenv("LOT_RPS", 1.0))
CONTROLE_MIN = 20               # minder controlepunten dan dit: koers niet gebruiken
CONTROLE_MARGE = 0.25           # afgeleide koers mag max 25% afwijken van wat we zelf zagen

SCHEMA = """
CREATE TABLE IF NOT EXISTS lot(mint TEXT PRIMARY KEY, status TEXT, keten_prijs REAL, keten_bron TEXT,
  gecheckt_ts REAL, afwijking REAL);
"""


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
    for m, created, mig, sp, sj, xl in main.execute(
            "SELECT mint, created_ts, migrated_ts, screen_pass, screen_json, has_x_link FROM tokens WHERE created_ts IS NOT NULL"):
        j = {}
        try: j = json.loads(sj) if sj else {}
        except Exception: pass
        scr[m] = {"created_ts": created, "migrated_ts": mig, "screen_pass": sp,
                  "houders_ok": bool(j.get("houders_gecheckt")) and not (j.get("check1a_flag") or j.get("check1b_flag")),
                  "fs": bool(j.get("fs")), "x": xl}
    uit = {}
    for m, created, mig, last_ts, vs, vt, n_tr, gap in led.execute(
            "SELECT mint, created_ts, migrated_ts, last_ts, v_sol, v_tok, n_trades, gap FROM token WHERE created_ts IS NOT NULL"):
        s = scr.get(m)
        if s is None or gap: continue
        p_nu = prijs(vs or 0, vt or 0)
        uit[m] = {**s, "migrated_ts": mig or s["migrated_ts"], "last_ts": last_ts, "n_trades": n_tr,
                  "v_sol": vs, "v_tok": vt, "laatste_prijs": p_nu}
    return uit


def status_van(t, ath, now):
    """gemigreerd / gerugd / dood / nog_actief — in die volgorde, want ze sluiten elkaar uit."""
    if t["migrated_ts"]: return "gemigreerd"
    p = t["laatste_prijs"]
    if ath and p and p <= ath * (1 - RUG_DALING): return "gerugd"
    if t["last_ts"] and t["last_ts"] < now - DOOD_NA_S: return "dood_op_curve"
    return "nog_actief"


def tops(led, mints=None):
    """Hoogste koers per token uit de wt-tabel is er niet; we halen hem uit de replay-tabel als die
    er is, anders uit de tokens-tabel van de bot."""
    return {}


# --------------------------------------------------------------------------- 2. koers nu, met controle
class Rpc:
    def __init__(self, url, rps):
        self.url, self.gap, self.last, self.calls, self.errors = url, 1.0 / rps, 0.0, 0, 0
    def call(self, method, params):
        import urllib.request
        w = self.last + self.gap - time.time()
        if w > 0: time.sleep(w)
        self.last = time.time(); self.calls += 1
        body = json.dumps({"jsonrpc": "2.0", "id": self.calls, "method": method, "params": params}).encode()
        try:
            req = urllib.request.Request(self.url, data=body, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r: j = json.loads(r.read().decode())
            if "error" in j: self.errors += 1; return None
            return j.get("result")
        except Exception:
            self.errors += 1; return None


def keten_prijs(rpc, mint):
    """Koers nu, zonder aannames over het programma: grootste tokenaccount -> eigenaar -> diens
    SOL- of WSOL-saldo, gedeeld door de tokens die hij aanhoudt. Werkt voor de bonding curve
    (SOL in lamports) én voor een AMM-pool (WSOL in een tokenaccount)."""
    la = rpc.call("getTokenLargestAccounts", [mint, {"commitment": "confirmed"}])
    vals = (la or {}).get("value") or []
    if not vals: return None
    ta = vals[0]["address"]; tok = int(vals[0]["amount"])
    if tok <= 0: return None
    info = rpc.call("getAccountInfo", [ta, {"encoding": "jsonParsed", "commitment": "confirmed"}])
    try: eig = info["value"]["data"]["parsed"]["info"]["owner"]
    except Exception: return None
    acc = rpc.call("getAccountInfo", [eig, {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0}, "commitment": "confirmed"}])
    lam = ((acc or {}).get("value") or {}).get("lamports", 0)
    bron = "curve"
    if lam < 10_000_000:      # nauwelijks SOL: waarschijnlijk een pool die WSOL aanhoudt
        ws = rpc.call("getTokenAccountsByOwner", [eig, {"mint": "So11111111111111111111111111111111111111112"},
                                                  {"encoding": "jsonParsed", "commitment": "confirmed"}])
        for v in (ws or {}).get("value", []):
            try: lam += int(v["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"])
            except Exception: pass
        bron = "pool"
    if lam <= 0: return None
    return {"prijs": (lam / 1e9) / (tok / 10 ** C.TOKEN_DECIMALS), "bron": bron, "eigenaar": eig, "tokens": tok}


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


# --------------------------------------------------------------------------- 3. rapport
NIVEAUS = [
    ("alle tokens", lambda t: True),
    ("schoon (houders gecheckt en ok)", lambda t: t["houders_ok"]),
    ("final stretch gehaald", lambda t: t["fs"]),
    ("volledige screening", lambda t: t["screen_pass"] == 1),
    ("volledige screening + X-link", lambda t: t["screen_pass"] == 1 and t["x"]),
]
STATUSSEN = ["gemigreerd", "nog_actief", "dood_op_curve", "gerugd"]


def bouw(main, led, lot, rpc, now, ath_van):
    toks = lees_tokens(main, led, now)
    for m, t in toks.items():
        t["ath"] = ath_van.get(m)
        t["status"] = status_van(t, t["ath"], now)
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
        rep["per_niveau"][naam] = rij

    # --- koers nu, voor de strengste groep plus een controlegroep ---
    gescreend = [m for m, t in toks.items() if t["screen_pass"] == 1]
    controle = [m for m, t in toks.items() if t["screen_pass"] != 1 and t["status"] == "dood_op_curve"]
    te_doen = []
    gedaan = {m: (p, b) for m, p, b in lot.execute("SELECT mint, keten_prijs, keten_bron FROM lot WHERE keten_prijs IS NOT NULL")}
    for m in gescreend + controle[:KETEN_PER_RUN]:
        if m not in gedaan: te_doen.append(m)
    te_doen = te_doen[:KETEN_PER_RUN]
    if rpc is not None:
        for i, m in enumerate(te_doen):
            if rpc.calls >= 8 and rpc.errors >= rpc.calls:
                log("keten onbereikbaar, gestopt"); break
            kp = keten_prijs(rpc, m)
            if kp is None: continue
            t = toks.get(m) or {}
            afw = (kp["prijs"] / t["laatste_prijs"] - 1) if t.get("laatste_prijs") else None
            lot.execute("INSERT OR REPLACE INTO lot VALUES(?,?,?,?,?,?)",
                        (m, t.get("status"), kp["prijs"], kp["bron"], now, round(afw, 4) if afw is not None else None))
            if i % 20 == 0: lot.commit()
        lot.commit()
    gedaan = {m: (p, b) for m, p, b in lot.execute("SELECT mint, keten_prijs, keten_bron FROM lot WHERE keten_prijs IS NOT NULL")}

    # --- de controle: bij dode curve-tokens mag de koers niet meer bewogen zijn ---
    paren = [(toks[m]["laatste_prijs"], gedaan[m][0]) for m in gedaan
             if m in toks and toks[m]["status"] == "dood_op_curve" and toks[m]["laatste_prijs"]]
    rep["koerscontrole"] = controleer(paren)

    # --- wat had vasthouden opgeleverd? ---
    rep["vasthouden"] = {}
    bruikbaar = rep["koerscontrole"].get("bruikbaar")
    for naam, fn in NIVEAUS:
        sub = [(m, t) for m, t in toks.items() if fn(t) and m in gedaan and t.get("ath")]
        if not sub: continue
        vanaf_top, vanaf_dip = [], []
        for m, t in sub:
            nu = gedaan[m][0]
            if not bruikbaar: nu = t["laatste_prijs"]      # dan alleen wat we zelf zagen
            if t["ath"]: vanaf_top.append(nu / t["ath"] - 1)
            dip = t["ath"] * 0.55 if t["ath"] else None    # instap op een 45%-dip
            if dip: vanaf_dip.append(nu / dip - 1)
        rep["vasthouden"][naam] = {"vanaf_de_top": samenvat(vanaf_top), "vanaf_45pct_dip": samenvat(vanaf_dip),
                                   "koers_uit": "keten" if bruikbaar else "laatste waarneming"}
    rep["keten"] = {"opgehaald": len(gedaan), "deze_run": len(te_doen),
                    "rpc_calls": getattr(rpc, "calls", 0), "rpc_fouten": getattr(rpc, "errors", 0)}
    return rep, toks


def to_md(rep):
    L = [f"# Wat is er van de tokens geworden? — {rep['gegenereerd']}", "",
         f"{rep['tokens']} tokens met een volledige logperiode. Alle andere analyses kijken naar een uur rond de "
         "instap; deze kijkt naar de afloop. 'Gerugd' = koers ≥ 80% onder de top. 'Dood op de curve' = geen trades "
         f"meer sinds ≥ {DOOD_NA_S // 3600} uur en niet gemigreerd. 'Gemigreerd' = de curve is volgelopen en het "
         "token handelt verder op een AMM — dat is wat de video als doel beschrijft.", "",
         "## Afloop per screeningniveau", "",
         "| niveau | tokens | gemigreerd | nog actief | dood op curve | gerugd |", "|---|---|---|---|---|---|"]
    for naam, rij in rep["per_niveau"].items():
        L.append(f"| {naam} | {rij['tokens']} | " + " | ".join(
            f"{rij[st]['aandeel']:.1%} ({rij[st]['n']})" for st in STATUSSEN) + " |")
    kc = rep.get("koerscontrole") or {}
    L += ["", "## Controle op de koers uit de keten", ""]
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
              "Niet scalpen maar houden, tot nu. Twee instapmomenten: op de top (het slechtst denkbare moment) en "
              "op een dip van 45% vanaf die top — het moment uit de video.", "",
              "| niveau | n | vanaf 45%-dip, mediaan | gemiddeld | 95%-marge | aandeel positief | aandeel ≤ −90% |",
              "|---|---|---|---|---|---|---|"]
        for naam, v in vh.items():
            d = v["vanaf_45pct_dip"]
            if not d.get("n"): continue
            ci = f"{d['ci95'][0]:+.0%} tot {d['ci95'][1]:+.0%}" if d.get("ci95") else "–"
            L.append(f"| {naam} | {d['n']} | {d['mediaan']:+.1%} | {d['gemiddeld']:+.1%} | {ci} | "
                     f"{d['aandeel_positief']:.0%} | {d['aandeel_min90']:.0%} |")
        L += ["", f"Koersbron: {next(iter(vh.values()))['koers_uit']}."]
    k = rep.get("keten") or {}
    L += ["", f"Koersen uit de keten opgehaald voor {k.get('opgehaald', 0)} tokens "
              f"({k.get('deze_run', 0)} deze run, {k.get('rpc_calls', 0)} calls, {k.get('rpc_fouten', 0)} fouten).", ""]
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
    led = sqlite3.connect(args.ledger, timeout=60); led.executescript(SCHEMA); led.commit()
    # hoogste koers per token: uit de replay-tabel als die er is, anders uit de bot-tabel
    ath = {}
    try:
        for m, d in led.execute("SELECT mint, data FROM replay"):
            j = json.loads(d); a = (j.get("feat") or {}).get("ath")
            if a: ath[m] = a
    except Exception: pass
    for m, a in main_db.execute("SELECT mint, ath_price FROM tokens WHERE ath_price IS NOT NULL"):
        ath.setdefault(m, a)
    rpc = None if args.geen_rpc else Rpc(C.RPC_HTTP, KETEN_RPS)
    rep, _ = bouw(main_db, led, led, rpc, now, ath)
    with open(os.path.join(args.out, "lotgevallen.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "lotgevallen.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {time.time() - t0:.0f}s -> {args.out}/lotgevallen.md")


if __name__ == "__main__":
    main()
