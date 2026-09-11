#!/usr/bin/env python3
"""Wallet-analyse met terugwerkende kracht op de gelogde pump.fun-trades.

Vraag: bestaat er een selecte groep wallets die structureel wint, en valt dat te kopiëren?

 1. Posities per (wallet, token) reconstrueren uit de trades-tabel (pump-fee meegerekend).
 2. Per wallet: winkans, winst, winst zonder beste trade, houdtijd, type
    (dev / hoogfrequente bot / vroege houder / scalper / swing).
 3. Geluk-toets: de echte toppers vergeleken met toppers na willekeurig husselen van alle
    posities over wallets (max-T, corrigeert voor het testen van duizenden wallets tegelijk).
 4. Persistentie: top-20 gekozen op de eerste helft van de periode, gemeten op de tweede helft.
 5. Kopieer-simulatie: hun aankopen volgen na 0 / 2 / 10 / 60 s met 0,2 SOL en onze kosten,
    verkopen zodra zij de helft van hun positie verkopen (plus dezelfde vertraging).

Alleen standaardbibliotheek. Leest de database alleen-lezen; de bot kan gewoon doordraaien.
Uitvoer: <out>/wallets.json en <out>/wallets.md
Gebruik: python wallet_analysis.py [--db PAD] [--out MAP] [--since UNIX_TS] [--perm N] [--min-pos N]
"""
import argparse, bisect, json, math, os, random, sqlite3, statistics, sys, time
from collections import defaultdict
import config as C
import curve

CLIP_LO, CLIP_HI = -1.0, 3.0          # rendement per positie afgekapt voor de t-waarde (één moonshot domineert niet)
COPY_SIZE = 0.2
COPY_DELAYS = [0, 2, 10, 60]
TOP_K = 20


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


# ----------------------------------------------------------------- statistiek
def tstat(xs):
    n = len(xs)
    if n < 2: return 0.0
    m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    if var <= 1e-18: return 0.0 if abs(m) < 1e-12 else math.copysign(1e3, m)   # identieke uitkomsten: extreem, maar eindig
    return m / math.sqrt(var / n)


def clip(r): return max(CLIP_LO, min(CLIP_HI, r))


def pool_params(xs):
    """Gemiddelde en spreiding van alle (afgekapte) positierendementen: de 'markt' waartegen een wallet wordt gemeten."""
    n = len(xs)
    if n < 2: return 0.0, 1.0
    m = sum(xs) / n
    return m, math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)) or 1.0


def excess_z(xs, mu, sigma):
    """Hoeveel beter dan een willekeurige positie in dezelfde markt, in standaardfouten.
    Gecentreerd op het marktgemiddelde, dus een stijgende markt maakt niet iedereen 'goed'."""
    n = len(xs)
    return 0.0 if n == 0 else (sum(xs) / n - mu) / (sigma / math.sqrt(n))


def ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0.0] * len(xs); i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]: j += 1
        for k in range(i, j + 1): r[order[k]] = (i + j) / 2
        i = j + 1
    return r


def spearman(a, b):
    if len(a) < 5: return None
    ra, rb = ranks(a), ranks(b); n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = math.sqrt(sum((x - ma) ** 2 for x in ra)); vb = math.sqrt(sum((y - mb) ** 2 for y in rb))
    return round(cov / (va * vb), 3) if va and vb else None


def pct(xs, q):
    if not xs: return None
    s = sorted(xs); return s[min(len(s) - 1, max(0, int(round(q * (len(s) - 1)))))]


# ----------------------------------------------------------------- data
def open_db(path):
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=60)
    db.execute("PRAGMA query_only=1")
    return db


def load_tokens(db):
    out = {}
    for mint, creator, cts, np_ts, mig in db.execute("SELECT mint, creator, created_ts, filter_newpairs_ts, migrated_ts FROM tokens"):
        out[mint] = (creator, cts, np_ts, mig)
    return out


def iter_mints(db, since):
    cur = db.execute("SELECT mint, ts, user, is_buy, sol, tokens, v_sol, v_tok FROM trades INDEXED BY trades_mint_ts "
                     "WHERE ts >= ? ORDER BY mint, ts", (since,))
    mint, rows = None, []
    for r in cur:
        if r[0] != mint:
            if rows: yield mint, rows
            mint, rows = r[0], []
        rows.append(r)
    if rows: yield mint, rows


def sell_value(v_sol, v_tok, tok):
    """Opbrengst (SOL, na pump-fee) als `tok` raw tokens nu op de curve verkocht worden."""
    if tok <= 0 or v_tok <= 0: return 0.0
    lam = v_sol - (v_sol * v_tok) // (v_tok + int(tok))
    return lam / 1e9 * (1 - C.FEE_PUMP)


# ----------------------------------------------------------------- stap 1: posities
class Pos:
    __slots__ = ("open_ts", "invested", "proceeds", "held", "bought", "sold", "max_held", "n_tr", "exit_sig_ts")
    def __init__(self, ts):
        self.open_ts = ts; self.invested = self.proceeds = 0.0; self.held = self.bought = self.sold = self.max_held = 0
        self.n_tr = 0; self.exit_sig_ts = None


def build_positions(db, tokens, since):
    """Geeft (positions, wallets, mints, prewin, early_agg, cover). Alleen posities vanaf >= $7k als tuple:
    position-tuple: (wid, mid, open_ts, close_ts|None, exit_sig_ts|None, invested, pnl, ret, closed, early, creator, age_s, entry_mcap_sol)"""
    wid_of, wallets, mid_of, mints = {}, [], {}, []
    positions = []
    prewin = defaultdict(lambda: [0, 0.0])     # wid -> [aantal verkopen zonder waargenomen aankoop, SOL-opbrengst]
    early_agg = defaultdict(lambda: [0, 0.0])  # wid -> [posities geopend vóór $7k, winst daarop]
    n_rows = n_mints = 0; tmin, tmax = float("inf"), 0.0; t0 = time.time()

    def wid(u):
        i = wid_of.get(u)
        if i is None: i = wid_of[u] = len(wallets); wallets.append(u)
        return i

    def finish(w, mid, p, close_ts, closed, dust_value, creator, created_ts, np_ts, entry_mcap):
        value = p.proceeds + dust_value
        pnl = value - p.invested
        ret = pnl / p.invested if p.invested > 0 else 0.0
        early = bool(np_ts is None or p.open_ts < np_ts - 0.5)
        if early:                                    # alleen totalen bewaren: dit zijn er met volledige logging heel veel
            e = early_agg[w]; e[0] += 1; e[1] += pnl; return
        age = (p.open_ts - created_ts) if created_ts else None
        positions.append((w, mid, p.open_ts, close_ts, p.exit_sig_ts, p.invested, pnl, ret, closed, early,
                          creator == wallets[w], age, entry_mcap))

    for mint, rows in iter_mints(db, since):
        n_mints += 1; n_rows += len(rows)
        tmin = min(tmin, rows[0][1]); tmax = max(tmax, rows[-1][1])
        creator, created_ts, np_ts, _mig = tokens.get(mint, (None, None, None, None))
        mid = mid_of[mint] = len(mints); mints.append(mint)
        open_pos, entry_mcap = {}, {}
        for (_m, ts, user, is_buy, sol, tok, vs, vt) in rows:
            w = wid(user); p = open_pos.get(w)
            if is_buy:
                if p is None:
                    p = open_pos[w] = Pos(ts)
                    entry_mcap[w] = curve.mcap_sol(vs, vt)
                p.invested += sol * (1 + C.FEE_PUMP); p.held += tok; p.bought += tok; p.n_tr += 1
                if p.held > p.max_held: p.max_held = p.held
            else:
                if p is None or p.held <= 0:
                    prewin[w][0] += 1; prewin[w][1] += sol * (1 - C.FEE_PUMP); continue
                s = min(tok, p.held); frac = s / tok if tok else 1.0
                p.proceeds += sol * (1 - C.FEE_PUMP) * frac
                if frac < 1.0:
                    prewin[w][0] += 1; prewin[w][1] += sol * (1 - C.FEE_PUMP) * (1 - frac)
                p.held -= s; p.sold += s; p.n_tr += 1
                if p.exit_sig_ts is None and p.sold >= 0.5 * p.bought: p.exit_sig_ts = ts
                if p.held <= 0.01 * p.max_held:
                    finish(w, mid, p, ts, True, sell_value(vs, vt, p.held), creator, created_ts, np_ts, entry_mcap.pop(w))
                    del open_pos[w]
        lv, lt = rows[-1][6], rows[-1][7]
        for w, p in open_pos.items():                 # niet gesloten binnen de data: waarderen op laatste curvestand
            finish(w, mid, p, None, False, sell_value(lv, lt, p.held), creator, created_ts, np_ts, entry_mcap.get(w))
        if n_mints % 2000 == 0: log(f"  {n_mints} tokens, {n_rows} trades, {len(positions)} posities ({time.time()-t0:.0f}s)")
    n_early = sum(e[0] for e in early_agg.values())
    cover = {"trades": n_rows, "tokens": n_mints, "wallets": len(wallets), "posities": len(positions) + n_early,
             "posities_in_venster": len(positions), "posities_vroeg": n_early,
             "van_ts": tmin if n_rows else None, "tot_ts": tmax if n_rows else None}
    return positions, wallets, mints, prewin, early_agg, cover


# ----------------------------------------------------------------- stap 1b: overrendement t.o.v. vergelijkbare posities
AGE_EDGES = [60, 300, 900]            # s na creatie: <1 min, 1-5 min, 5-15 min, >15 min
MCAP_EDGES = [60, 120, 250]           # marketcap in SOL bij instap


def _bucket(x, edges):
    if x is None: return -1
    for i, e in enumerate(edges):
        if x < e: return i
    return len(edges)


def add_excess(positions):
    """Voegt per positie toe: [13] overrendement, [14] voorzichtige winst, [15] voorzichtig rendement.
    Voorzichtig = een positie zonder verkoop telt verlies volledig mee, maar papieren winst niet (die is niet gerealiseerd
    en de waardering op de laatste curveprijs is onbetrouwbaar). Overrendement = afgekapt voorzichtig rendement min het
    gemiddelde van posities in hetzelfde uur, op vergelijkbare tokenleeftijd en marketcap. Zo telt 'vroeg zijn in een
    stijgende markt' niet als talent."""
    fine, coarse = defaultdict(lambda: [0, 0.0]), defaultdict(lambda: [0, 0.0])
    keys = []
    for p in positions:
        c2 = (_bucket(p[11], AGE_EDGES), _bucket(p[12], MCAP_EDGES)); c1 = (int(p[2] // 3600),) + c2
        r = clip(cons_ret(p)); fine[c1][0] += 1; fine[c1][1] += r; coarse[c2][0] += 1; coarse[c2][1] += r
        keys.append((c1, c2))
    out = []
    for p, (c1, c2) in zip(positions, keys):
        cell = fine[c1] if fine[c1][0] >= 30 else coarse[c2]
        out.append(p + (clip(cons_ret(p)) - cell[1] / cell[0], cons_pnl(p), cons_ret(p)))
    return out


def cons_ret(p): return p[7] if p[8] else min(p[7], 0.0)
def cons_pnl(p): return p[6] if p[8] else min(p[6], 0.0)


# ----------------------------------------------------------------- stap 2: wallet-statistiek
MIN_FULL_STATS = 5      # wallets met minder posities krijgen alleen kerncijfers (geheugen) en type 'incidenteel'


def wallet_table(positions, prewin, early_agg, mid_ts):
    by_w = defaultdict(list)
    for p in positions: by_w[p[0]].append(p)
    for w in early_agg: by_w.setdefault(w, [])
    table = {}
    for w, ps_in in by_w.items():                      # alle tuples zijn posities geopend vanaf >= $7k
        e = early_agg.get(w, (0, 0.0))
        base = {"n_early": e[0], "winst_vroeg": e[1], "prewin_sells": prewin[w][0], "prewin_sol": prewin[w][1]}
        if len(ps_in) >= MIN_FULL_STATS:
            s = stats_for(ps_in, mid_ts); s.update(base); s["type"] = classify(s)
        else:
            s = {"n": len(ps_in), "winst_sol": sum(p[6] for p in ps_in), "winst_gesloten": sum(p[6] for p in ps_in if p[8]),
                 "winst_voorzichtig": sum(p[14] for p in ps_in),
                 "creator_aandeel": (sum(1 for p in ps_in if p[10]) / len(ps_in)) if ps_in else 0.0, **base}
            s["type"] = ("dev" if s["creator_aandeel"] >= 0.2 else
                         "vroege_houder" if s["prewin_sells"] >= max(5, s["n"]) else "incidenteel")
        table[w] = s
    for w, pw in prewin.items():
        if w not in table:
            table[w] = {"n": 0, "winst_sol": 0.0, "winst_gesloten": 0.0, "winst_voorzichtig": 0.0, "creator_aandeel": 0.0, "n_early": 0, "winst_vroeg": 0.0,
                        "prewin_sells": pw[0], "prewin_sol": pw[1], "type": "vroege_houder"}
    return table


def stats_for(ps, mid_ts):
    """Alle prestatiecijfers op voorzichtige waarden ([14]/[15]); 'winst_sol' is inclusief papieren winst."""
    n = len(ps); pnls = [p[14] for p in ps]; rets = [p[15] for p in ps]
    closed = [p for p in ps if p[8]]
    holds = [p[3] - p[2] for p in closed]
    inv = sum(p[5] for p in ps); pnl = sum(pnls); pnl_marked = sum(p[6] for p in ps)
    wins = [x for x in pnls if x > 0]; losses = [x for x in pnls if x <= 0]
    best = max(pnls)
    hours = {int(p[2] // 3600) for p in ps}
    a = [p for p in ps if p[2] < mid_ts]; b = [p for p in ps if p[2] >= mid_ts]
    ages = [p[11] for p in ps if p[11] is not None]
    return {
        "n": n, "n_closed": len(closed), "n_open": n - len(closed), "n_tokens": len({p[1] for p in ps}),
        "winst_gesloten": round(sum(p[6] for p in closed), 3),
        "med_instap_mcap_sol": round(statistics.median([p[12] for p in ps if p[12] is not None]), 1) if any(p[12] is not None for p in ps) else None,
        "winkans": round(len(wins) / n, 3), "winst_voorzichtig": round(pnl, 3), "winst_sol": round(pnl_marked, 3), "ingezet_sol": round(inv, 3),
        "roi": round(pnl / inv, 4) if inv > 0 else 0.0,
        "gem_rend": round(sum(rets) / n, 4), "med_rend": round(statistics.median(rets), 4),
        "gem_overrendement": round(sum(p[13] for p in ps) / n, 4), "t": None,
        "beste_trade_sol": round(best, 3), "winst_zonder_beste": round(pnl - best, 3),
        "profit_factor": round(sum(wins) / -sum(losses), 2) if losses and sum(losses) < 0 else None,
        "med_houdtijd_s": round(statistics.median(holds), 1) if holds else None,
        "med_inzet_sol": round(statistics.median([p[5] for p in ps]), 3),
        "med_leeftijd_bij_instap_s": round(statistics.median(ages)) if ages else None,
        "pos_per_actief_uur": round(n / max(1, len(hours)), 1),
        "creator_aandeel": round(sum(1 for p in ps if p[10]) / n, 3),
        "n_A": len(a), "winst_A": round(sum(p[14] for p in a), 3),
        "n_B": len(b), "winst_B": round(sum(p[14] for p in b), 3),
    }


def classify(s):
    if s["creator_aandeel"] >= 0.2: return "dev"
    if (s["med_houdtijd_s"] is not None and s["med_houdtijd_s"] < 15) or s["pos_per_actief_uur"] >= 20: return "bot_hf"
    if s["prewin_sells"] >= max(5, s["n"]): return "vroege_houder"
    if s["med_houdtijd_s"] is not None and s["med_houdtijd_s"] >= 600: return "swing"
    return "scalper"


# ----------------------------------------------------------------- stap 3: geluk-toets (max-T)
def luck_test(positions, table, min_pos, n_perm, seed=7):
    pop = [w for w, s in table.items() if s["n"] >= min_pos and s["type"] != "dev"]
    if len(pop) < TOP_K: return {"populatie_wallets": len(pop), "opmerking": "te weinig wallets voor de toets"}
    popset = set(pop)
    rets_by_w = defaultdict(list)
    for p in positions:
        if not p[9] and p[0] in popset: rets_by_w[p[0]].append(p[13])
    counts = [len(rets_by_w[w]) for w in pop]
    pool = [r for w in pop for r in rets_by_w[w]]
    mu, sigma = pool_params(pool)
    real_by_w = {w: excess_z(rets_by_w[w], mu, sigma) for w in pop}
    real = sorted(real_by_w.values(), reverse=True)
    n_perm = max(20, min(n_perm, int(4e7 / max(1, len(pool)))))
    rng = random.Random(seed); tops = {1: [], 10: [], 20: []}
    for i in range(n_perm):
        rng.shuffle(pool); k = 0; ts_ = []
        for c in counts:
            ts_.append(excess_z(pool[k:k + c], mu, sigma)); k += c
        ts_.sort(reverse=True)
        for r in tops: tops[r].append(ts_[r - 1])
    grens = pct(tops[1], 0.95)
    return {
        "populatie_wallets": len(pop), "populatie_posities": len(pool), "husselrondes": n_perm,
        "echt_t": {f"#{r}": round(real[r - 1], 2) for r in tops},
        "geluk_t_mediaan": {f"#{r}": round(pct(tops[r], 0.5), 2) for r in tops},
        "geluk_t_95pct": {f"#{r}": round(pct(tops[r], 0.95), 2) for r in tops},
        "max_t_grens_95pct": round(grens, 2),
        "wallets_boven_grens": sum(1 for t in real if t > grens),
        "significant": [w for w in pop if real_by_w[w] > grens],
    }


# ----------------------------------------------------------------- stap 4: persistentie A -> B
def persistence(positions, table, mid_ts, seed=11):
    a_by, b_by = defaultdict(list), defaultdict(list)
    for p in positions:
        if p[9] or table.get(p[0], {}).get("type") == "dev": continue
        (a_by if p[2] < mid_ts else b_by)[p[0]].append(p)
    elig = [w for w, ps in a_by.items() if len(ps) >= 10]
    if len(elig) < TOP_K: return {"opmerking": f"te weinig wallets met >= 10 posities in helft A ({len(elig)})"}, [], []

    mu_a, sd_a = pool_params([p[13] for w in elig for p in a_by[w]])
    def score_t(w): return excess_z([p[13] for p in a_by[w]], mu_a, sd_a)
    def score_pnl(w): return sum(p[14] for p in a_by[w])

    def measure(ws):
        ps = [p for w in ws for p in b_by.get(w, [])]
        active = sum(1 for w in ws if b_by.get(w))
        if not ps: return {"actief_in_B": active, "n": 0}
        rets = [p[15] for p in ps]
        return {"actief_in_B": active, "n": len(ps), "winkans": round(sum(1 for p in ps if p[14] > 0) / len(ps), 3),
                "gem_rend": round(sum(rets) / len(rets), 4), "med_rend": round(statistics.median(rets), 4),
                "winst_sol": round(sum(p[14] for p in ps), 3),
                "wallets_winstgevend_in_B": sum(1 for w in ws if b_by.get(w) and sum(p[14] for p in b_by[w]) > 0)}

    top_t = sorted(elig, key=score_t, reverse=True)[:TOP_K]
    top_pnl = sorted(elig, key=score_pnl, reverse=True)[:TOP_K]
    all_b = [p for ps in b_by.values() for p in ps]
    rng = random.Random(seed); rand_rets = []
    for _ in range(200):
        m = measure(rng.sample(elig, TOP_K))
        if m.get("n"): rand_rets.append(m["gem_rend"])
    both = [w for w in elig if len(b_by.get(w, [])) >= 10]
    rho = spearman([sum(p[13] for p in a_by[w]) / len(a_by[w]) for w in both],
                   [sum(p[13] for p in b_by[w]) / len(b_by[w]) for w in both])
    res = {
        "wallets_gekozen_uit": len(elig),
        "top20_op_t_in_A__gemeten_in_B": measure(top_t),
        "top20_op_winst_in_A__gemeten_in_B": measure(top_pnl),
        "alle_posities_in_B": {"n": len(all_b), "gem_rend": round(sum(p[15] for p in all_b) / len(all_b), 4) if all_b else None,
                               "winkans": round(sum(1 for p in all_b if p[14] > 0) / len(all_b), 3) if all_b else None},
        "willekeurige_20_uit_A__gem_rend_in_B": {"mediaan": round(pct(rand_rets, 0.5), 4) if rand_rets else None,
                                                  "p95": round(pct(rand_rets, 0.95), 4) if rand_rets else None},
        "spearman_rend_A_vs_B": {"wallets": len(both), "rho": rho},
    }
    return res, top_t, top_pnl


# ----------------------------------------------------------------- stap 5: kopieer-simulatie
def copy_sim(db, positions, mints, groups, mid_ts):
    """groups: naam -> (set(wid), alleen_helft_B: bool). Geeft per groep per vertraging EV/winkans."""
    wanted = defaultdict(list)
    for p in positions:
        if p[9]: continue
        for name, (ws, only_b) in groups.items():
            if p[0] in ws and (not only_b or p[2] >= mid_ts): wanted[p[1]].append((name, p))
    out = {name: {d: [] for d in COPY_DELAYS} for name in groups}
    marked = {name: 0 for name in groups}
    for mid, items in wanted.items():
        rows = db.execute("SELECT ts, v_sol, v_tok FROM trades INDEXED BY trades_mint_ts WHERE mint = ? ORDER BY ts", (mints[mid],)).fetchall()
        if not rows: continue
        tsa = [r[0] for r in rows]
        def state(t):
            i = bisect.bisect_right(tsa, t) - 1
            r = rows[max(0, i)]; return int(r[1]), int(r[2])
        for name, p in items:
            if p[4] is None: marked[name] += 1
            for d in COPY_DELAYS:
                vs, vt = state(p[2] + d)
                tok, _ = curve.buy(vs, vt, COPY_SIZE, "pp")
                vs2, vt2 = state(p[4] + d) if p[4] is not None else (int(rows[-1][1]), int(rows[-1][2]))
                sol_out, _ = curve.sell(vs2, vt2, tok, "pp")
                r = (sol_out - COPY_SIZE - C.PRIO_FEE_SOL) / COPY_SIZE
                out[name][d].append(r if p[4] is not None else min(r, 0.0))
    res = {}
    for name, per_d in out.items():
        res[name] = {"posities_zonder_verkoopsignaal": marked[name]}
        for d, rets in per_d.items():
            if not rets: res[name][f"{d}s"] = {"n": 0}; continue
            res[name][f"{d}s"] = {"n": len(rets), "winkans": round(sum(1 for r in rets if r > 0) / len(rets), 3),
                                  "ev": round(sum(rets) / len(rets), 4), "mediaan": round(statistics.median(rets), 4),
                                  "winst_sol_bij_0.2": round(sum(rets) * COPY_SIZE, 3)}
    return res


# ----------------------------------------------------------------- wie wint het geld
def money_flow(table):
    keys = ("winst_gesloten", "winst_voorzichtig", "winst_sol", "winst_vroeg", "prewin_sol")
    agg = defaultdict(lambda: {"wallets": 0, "posities": 0, "posities_vroeg": 0, **{k: 0.0 for k in keys}})
    for s in table.values():
        a = agg[s["type"]]; a["wallets"] += 1; a["posities"] += s["n"]; a["posities_vroeg"] += s["n_early"]
        for k in keys: a[k] += s.get(k, 0.0)
    for a in agg.values():
        for k in keys: a[k] = round(a[k], 2)
    act = [s for s in table.values() if s["n"] >= 10]
    pos_pnl = sorted((s["winst_gesloten"] for s in table.values() if s["n"] and s["winst_gesloten"] > 0), reverse=True)
    top1 = pos_pnl[:max(1, len(pos_pnl) // 100)]
    return {"per_type": dict(agg),
            "wallets_met_10plus_posities": len(act),
            "aandeel_daarvan_winstgevend": round(sum(1 for s in act if s["winst_voorzichtig"] > 0) / len(act), 3) if act else None,
            "som_gesloten_posities_sol": round(sum(s.get("winst_gesloten", 0.0) for s in table.values()), 2),
            "aandeel_winst_bij_top_1pct_winnaars": round(sum(top1) / sum(pos_pnl), 3) if pos_pnl else None}


# ----------------------------------------------------------------- rapport
def row_for(wallets, table, w, rank):
    s = table[w]; a = wallets[w]
    return {"rang": rank, "wallet": a, "type": s["type"], "posities": s["n"], "open": s["n_open"], "tokens": s["n_tokens"], "winkans": s["winkans"],
            "med_instap_mcap_sol": s["med_instap_mcap_sol"], "gem_overrendement": s["gem_overrendement"],
            "winst_sol": s["winst_voorzichtig"], "winst_incl_papier": s["winst_sol"], "winst_zonder_beste": s["winst_zonder_beste"], "roi": s["roi"], "t": s["t"],
            "med_houdtijd_s": s["med_houdtijd_s"], "med_inzet_sol": s["med_inzet_sol"], "med_leeftijd_bij_instap_s": s["med_leeftijd_bij_instap_s"],
            "winst_A": s["winst_A"], "winst_B": s["winst_B"]}


def to_md(rep):
    L = []; add = L.append
    c = rep["dekking"]
    add(f"# Wallet-analyse pump.fun — {rep['gegenereerd']}\n")
    add("## Kort antwoord\n")
    for line in rep["conclusies"]: add(f"- {line}")
    add("\n## Dekking van de data\n")
    add(f"- Periode: {c.get('van')} → {c.get('tot')} ({c.get('uren')} uur), helft A/B-grens: {c.get('grens_AB')}")
    add(f"- {c['trades']} trades, {c['tokens']} tokens, {c['wallets']} wallets, {c['posities']} posities "
        f"({c['posities_in_venster']} geopend vanaf ≥ $7k, {c['posities_vroeg']} eerder)")
    add(f"- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): {c['posities_open_gewaardeerd']}")
    add(f"- Alle trades (ook onder $7k) gelogd sinds: {c.get('volledige_logging_sinds') or 'nog niet — alleen trades vanaf $7k'}")
    mf = rep["wie_wint"]
    add("\n## Wie wint het geld (posities vanaf ≥ $7k)\n")
    add("| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |")
    add("|---|---|---|---|---|---|---|---|---|")
    for t, a in sorted(mf["per_type"].items(), key=lambda kv: -kv[1]["winst_voorzichtig"]):
        add(f"| {t} | {a['wallets']} | {a['posities']} | {a['winst_gesloten']:+.2f} | {a['winst_voorzichtig']:+.2f} | {a['winst_sol']:+.2f} | {a['prewin_sol']:.2f} | {a['posities_vroeg']} | {a['winst_vroeg']:+.2f} |")
    add(f"\nWallets met ≥ 10 posities: {mf['wallets_met_10plus_posities']}, waarvan winstgevend: {fmt_pct(mf['aandeel_daarvan_winstgevend'])}. "
        f"De top 1% winnaars pakt {fmt_pct(mf['aandeel_winst_bij_top_1pct_winnaars'])} van alle winst op gesloten posities. "
        f"Som over alle gesloten posities (na pump-fee): {mf['som_gesloten_posities_sol']:+.2f} SOL.")
    add("\nTypes: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; "
        "vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; "
        "incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.")
    for key, title, note in (("top_beste", "Top 20 beste traders (streng gefilterd)",
                              f"Filters: ≥ {rep['instellingen']['min_pos']} posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert."),
                             ("top_winst", "Top 20 op winst (zonder filters, ter vergelijking)", "Zo werken de meeste 'smart money'-lijsten.")):
        add(f"\n## {title}\n\n{note} Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.\n")
        add("| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |")
        add("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rep[key]:
            w = r["wallet"]
            add(f"| {r['rang']} | [{w[:4]}…{w[-4:]}](https://solscan.io/account/{w}) | {r['type']} | {r['posities']} ({r['open']}) | {r['winkans']:.0%} | "
                f"{r['winst_sol']:+.2f} | {r['winst_zonder_beste']:+.2f} | {r['roi']:+.0%} | {r['t']} | {'ja' if r['significant_na_geluktoets'] else 'nee'} | {fmt_s(r['med_houdtijd_s'])} | {r['winst_A']:+.2f} / {r['winst_B']:+.2f} |")
        if not rep[key]: add("| – | geen wallets die aan de filters voldoen | | | | | | | | | | |")
    lt = rep["geluk_toets"]
    add("\n## Geluk-toets\n")
    if "echt_t" in lt:
        add(f"Populatie: {lt['populatie_wallets']} wallets met ≥ {rep['instellingen']['min_pos']} posities, {lt['husselrondes']} husselrondes.\n")
        add("| rang | echte t | geluk mediaan | geluk 95% |"); add("|---|---|---|---|")
        for r in ("#1", "#10", "#20"):
            add(f"| {r} | {lt['echt_t'][r]} | {lt['geluk_t_mediaan'][r]} | {lt['geluk_t_95pct'][r]} |")
        add(f"\nWallets boven de 95%-grens van de beste 'geluks-wallet' (t > {lt['max_t_grens_95pct']}): **{lt['wallets_boven_grens']}**. "
            "Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; "
            "hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.")
    else: add(lt.get("opmerking", ""))
    ps = rep["persistentie"]
    add("\n## Persistentie: gekozen op helft A, gemeten op helft B\n")
    if "top20_op_t_in_A__gemeten_in_B" in ps:
        add("| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |"); add("|---|---|---|---|---|---|---|")
        for k, lab in (("top20_op_t_in_A__gemeten_in_B", "top 20 op t (A)"), ("top20_op_winst_in_A__gemeten_in_B", "top 20 op winst (A)")):
            m = ps[k]
            if m.get("n"): add(f"| {lab} | {m['actief_in_B']}/20 | {m['n']} | {m['winkans']:.0%} | {m['gem_rend']:+.1%} | {m['med_rend']:+.1%} | {m['winst_sol']:+.2f} |")
            else: add(f"| {lab} | {m['actief_in_B']}/20 | 0 | – | – | – | – |")
        ab = ps["alle_posities_in_B"]; rr = ps["willekeurige_20_uit_A__gem_rend_in_B"]
        if ab["n"]: add(f"| alle wallets | – | {ab['n']} | {ab['winkans']:.0%} | {ab['gem_rend']:+.1%} | – | – |")
        if rr["mediaan"] is not None: add(f"| willekeurige 20 (mediaan / p95) | – | – | – | {rr['mediaan']:+.1%} / {rr['p95']:+.1%} | – | – |")
        sp = ps["spearman_rend_A_vs_B"]
        add(f"\nRangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: {sp['wallets']}): ρ = {sp['rho']}. "
            "Rond 0 betekent: goed in A zegt niets over B.")
    else: add(ps.get("opmerking", ""))
    add("\n## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)\n")
    for name, res in rep["kopieer_simulatie"].items():
        add(f"**{name}** — posities zonder verkoopsignaal binnen de data: {res['posities_zonder_verkoopsignaal']}\n")
        add("| vertraging | n | winkans | EV per trade | mediaan | winst SOL |"); add("|---|---|---|---|---|---|")
        for d in COPY_DELAYS:
            m = res[f"{d}s"]
            if m["n"]: add(f"| {d} s | {m['n']} | {m['winkans']:.0%} | {m['ev']:+.1%} | {m['mediaan']:+.1%} | {m['winst_sol_bij_0.2']:+.2f} |")
            else: add(f"| {d} s | 0 | – | – | – | – |")
        add("")
    add("## Beperkingen\n")
    for b in rep["beperkingen"]: add(f"- {b}")
    return "\n".join(L) + "\n"


def fmt_pct(x): return "–" if x is None else f"{x:.0%}"
def fmt_s(x):
    if x is None: return "–"
    return f"{x:.0f} s" if x < 120 else f"{x/60:.0f} min"


def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None


def conclusions(rep):
    out = []; lt = rep["geluk_toets"]; ps = rep["persistentie"]; cs = rep["kopieer_simulatie"]
    if "wallets_boven_grens" in lt:
        out.append(f"Geluk-toets: {lt['wallets_boven_grens']} van {lt['populatie_wallets']} wallets scoren beter dan de beste wallet in een wereld van puur geluk "
                   f"(echte #1 t={lt['echt_t']['#1']}, geluk-grens {lt['max_t_grens_95pct']}).")
    m = ps.get("top20_op_t_in_A__gemeten_in_B")
    if m and m.get("n"):
        base = ps["alle_posities_in_B"]["gem_rend"]
        out.append(f"Persistentie: de top 20 uit helft A haalde in helft B gemiddeld {m['gem_rend']:+.1%} per positie "
                   f"(alle wallets: {base:+.1%}; {m['wallets_winstgevend_in_B']} van {m['actief_in_B']} actieve toppers bleven winstgevend).")
    o = cs.get("buiten steekproef: top 20 uit A, gekopieerd in B", {})
    if o.get("2s", {}).get("n"):
        out.append("Kopiëren buiten de steekproef, EV per trade na onze kosten: " +
                   ", ".join(f"{d} s: {o[f'{d}s']['ev']:+.1%}" for d in COPY_DELAYS if o[f'{d}s']['n']) +
                   f" (drempel uit het bouwplan: +3%).")
    if not out: out.append("Nog te weinig data voor conclusies; zie de secties hieronder.")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH); ap.add_argument("--out", default=C.REPORT_DIR)
    ap.add_argument("--since", type=float, default=None, help="unix-tijd; standaard: laatste --hours uur")
    ap.add_argument("--hours", type=float, default=72.0, help="venster als --since ontbreekt (0 = alles)")
    ap.add_argument("--perm", type=int, default=100)
    ap.add_argument("--min-pos", type=int, default=20)
    args = ap.parse_args()
    args.min_pos = max(args.min_pos, MIN_FULL_STATS)
    if args.since is None: args.since = 0.0 if not args.hours else time.time() - args.hours * 3600
    t0 = time.time(); log("wallet-analyse start", args.db, "since", iso(args.since) or "begin")
    db = open_db(args.db)
    tokens = load_tokens(db); log(f"{len(tokens)} tokens geladen")
    try:
        r = db.execute("SELECT v FROM meta WHERE k = 'full_trade_log_since'").fetchone()
        full_since = float(json.loads(r[0])) if r else None
    except sqlite3.Error:
        full_since = None
    positions, wallets, mints, prewin, early_agg, cover = build_positions(db, tokens, args.since)
    log(f"posities: {len(positions)} uit {cover['trades']} trades ({time.time()-t0:.0f}s)")
    positions = add_excess(positions)
    if not positions:
        rep = {"gegenereerd": iso(time.time()), "opmerking": "geen trades gevonden"}
        os.makedirs(args.out, exist_ok=True)
        json.dump(rep, open(os.path.join(args.out, "wallets.json"), "w"), indent=1); return
    mid_ts = (cover["van_ts"] + cover["tot_ts"]) / 2
    table = wallet_table(positions, prewin, early_agg, mid_ts); log(f"{len(table)} wallets gerekend")
    mu, sigma = pool_params([p[13] for p in positions])
    for s in table.values():
        if "gem_overrendement" in s:
            s["t"] = round((s["gem_overrendement"] - mu) / (sigma / math.sqrt(s["n"])), 2)

    beste = [w for w, s in table.items() if s["n"] >= args.min_pos and s["type"] != "dev"
             and s["winst_A"] > 0 and s["winst_B"] > 0 and s["winst_zonder_beste"] > 0]
    beste = sorted(beste, key=lambda w: table[w]["t"], reverse=True)[:TOP_K]
    top_winst = sorted([w for w, s in table.items() if s["n"] >= MIN_FULL_STATS], key=lambda w: table[w]["winst_voorzichtig"], reverse=True)[:TOP_K]

    log("geluk-toets"); lt = luck_test(positions, table, args.min_pos, args.perm)
    sig = set(lt.pop("significant", []))
    log("persistentie"); ps, top_t_a, _ = persistence(positions, table, mid_ts)
    log("kopieer-simulatie")
    groups = {}
    if top_t_a: groups["buiten steekproef: top 20 uit A, gekopieerd in B"] = (set(top_t_a), True)
    if beste: groups["binnen steekproef: top 20 beste traders, hele periode (optimistisch)"] = (set(beste), False)
    if top_winst: groups["binnen steekproef: top 20 op winst, hele periode (optimistisch)"] = (set(top_winst), False)
    cs = copy_sim(db, positions, mints, groups, mid_ts) if groups else {}

    rep = {
        "gegenereerd": iso(time.time()), "looptijd_s": None,
        "instellingen": {"min_pos": args.min_pos, "since": args.since, "copy_size_sol": COPY_SIZE, "fee_pump": C.FEE_PUMP},
        "dekking": {**cover, "van": iso(cover["van_ts"]), "tot": iso(cover["tot_ts"]), "grens_AB": iso(mid_ts),
                    "uren": round((cover["tot_ts"] - cover["van_ts"]) / 3600, 1),
                    "posities_open_gewaardeerd": sum(1 for p in positions if not p[8]),
                    "volledige_logging_sinds": iso(full_since)},
        "wie_wint": money_flow(table),
        "top_beste": [dict(row_for(wallets, table, w, i + 1), significant_na_geluktoets=w in sig) for i, w in enumerate(beste)],
        "top_winst": [dict(row_for(wallets, table, w, i + 1), significant_na_geluktoets=w in sig) for i, w in enumerate(top_winst)],
        "geluk_toets": lt, "persistentie": ps, "kopieer_simulatie": cs,
        "beperkingen": [
            "Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.",
            "Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').",
            "Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.",
            "Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.",
            "Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.",
            "De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.",
        ],
    }
    rep["conclusies"] = conclusions(rep); rep["looptijd_s"] = round(time.time() - t0)
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "wallets.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "wallets.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {rep['looptijd_s']}s -> {args.out}/wallets.md")


if __name__ == "__main__":
    main()
