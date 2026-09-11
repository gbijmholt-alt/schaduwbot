#!/usr/bin/env python3
"""Geldstroom per wallet, bijgehouden over de tijd: waar gaat het geld naartoe, en welke wallets groeien gestaag?

Werking
 - Leest nieuwe trades incrementeel (op rowid) uit de bot-database en telt per wallet per token op hoeveel SOL erin
   ging (aankopen, inclusief pump-fee) en hoeveel er terugkwam (verkopen, na pump-fee). Netto = wat er echt in de
   wallet landt min wat eruit ging. Geen waarderingen, geen aannames.
 - Alleen tokens die ontstonden nadat de bot álle trades ging loggen, en die geen herstart van de bot overlapten.
   Alleen dan is de hele geschiedenis van dat token bekend.
 - Schrijft naar een eigen database (data/ledger.sqlite), zodat de bot er geen last van heeft en alles bewaard blijft.

Uitvoer (reports/ledger.md en .json)
 1. Waar gaat het geld naartoe: per rol (dev, bundel in het creatieblok, sniper ≤ 5 s, vroeg < $7k, laat ≥ $7k).
 2. Hoe geconcentreerd de winst is, en de top 25 op netto instroom.
 3. Groeiers: wallets die volgens vooraf vastgelegde criteria zelden verliezen en gestaag groeien.
    Eenmaal op de lijst blijven ze gevolgd (momentopname per run).
 4. Vooruit-toets: wat gebeurt er met de koers nadat een groeier koopt, gemeten op aankopen ná opname in de lijst.
"""
import argparse, bisect, json, math, os, sqlite3, statistics, time
from collections import defaultdict
import config as C
import curve

CRITERIA_VERSIE = "groeiers-v1"
CRITERIA = {                      # vooraf vastgelegd; wijzigen = nieuwe versie
    "min_tokens_afgerond": 20,    # gesloten of doodgebloede posities
    "min_winkans_tokens": 0.60,
    "min_netto_sol": 0.0,
    "max_drawdown_van_piek": 0.25,
    "min_aandeel_positieve_6u_blokken": 0.75,
    "min_actieve_6u_blokken": 3,
    "max_dev_aandeel": 0.10,
    "max_bundel_aandeel": 0.20,
}
GAP_WINDOW_S = 2 * 3600           # herstart binnen 2 uur na creatie = gat; daarna gebeurt er nog maar weinig met een token
DEAD_AFTER_S = 2 * 3600           # geen trades meer sinds 2 uur en niet gemigreerd: resterende tokens tellen als verloren
COPY_SIZE = 0.2
SIGNAL_WINDOW_S = 3600
FEE = C.FEE_PUMP

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE IF NOT EXISTS token(mint TEXT PRIMARY KEY, created_ts REAL, create_slot INTEGER, creator TEXT,
  np_ts REAL, migrated_ts REAL, last_ts REAL, v_sol INTEGER, v_tok INTEGER, n_trades INTEGER DEFAULT 0, gap INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS wt(wallet TEXT, mint TEXT, first_ts REAL, last_ts REAL, sol_out REAL, sol_in REAL,
  tok_buy INTEGER, tok_sell INTEGER, n_buy INTEGER, n_sell INTEGER, first_buy_ts REAL, first_buy_slot INTEGER,
  PRIMARY KEY(wallet, mint));
CREATE INDEX IF NOT EXISTS wt_mint ON wt(mint);
CREATE TABLE IF NOT EXISTS wh(wallet TEXT, hour INTEGER, sol_out REAL, sol_in REAL, PRIMARY KEY(wallet, hour));
CREATE TABLE IF NOT EXISTS watch(wallet TEXT PRIMARY KEY, added_ts REAL, versie TEXT, stats TEXT);
CREATE TABLE IF NOT EXISTS watch_snap(wallet TEXT, ts REAL, netto REAL, afgerond INTEGER, winkans REAL, PRIMARY KEY(wallet, ts));
CREATE TABLE IF NOT EXISTS signal(wallet TEXT, mint TEXT, buy_ts REAL, na_opname INTEGER, r1 REAL, r5 REAL, r15 REAL, r60 REAL,
  max15 REAL, ret_volg REAL, ret_video REAL, opmerking TEXT, PRIMARY KEY(wallet, mint));
CREATE TABLE IF NOT EXISTS herkomst(wallet TEXT, mint TEXT, afzender TEXT, tx_ts REAL, notitie TEXT, gecheckt_ts REAL, PRIMARY KEY(wallet, mint));
CREATE TABLE IF NOT EXISTS wallet_info(wallet TEXT PRIMARY KEY, sol_saldo REAL, eigenaar TEXT, op_curve INTEGER, gecheckt_ts REAL);
"""
GROOT_KANDIDATEN = 2000          # meest actieve wallets (volume in de meetperiode) waarvan we het SOL-saldo ophalen
GROOT_SALDO_SOL = 100.0          # 'groot' = minstens zoveel SOL in de wallet ...
GROOT_VOLUME_SOL = 100.0         # ... of minstens zoveel SOL verhandeld op de curve in de meetperiode
GROOT_MIN_TOKENS = 10
SALDO_VERVERSEN_S = 6 * 3600
MANUAL = "handmatig"
HERKOMST_PER_RUN = 40            # 'zonder koop'-posities per run koppelen aan de wallet waar de tokens vandaan kwamen
HERKOMST_MIN_SOL = 0.5
HERKOMST_RPS = 2.0               # laag houden: de bot gebruikt dezelfde Helius-sleutel


def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def iso(ts): return time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(ts)) if ts else None


def meta_get(db, k, default=None):
    r = db.execute("SELECT v FROM meta WHERE k = ?", (k,)).fetchone()
    return json.loads(r[0]) if r else default


def meta_set(db, k, v):
    db.execute("INSERT INTO meta(k, v) VALUES(?, ?) ON CONFLICT(k) DO UPDATE SET v = excluded.v", (k, json.dumps(v)))


# ----------------------------------------------------------------- 1. incrementeel inlezen
def load_tokens(main, start_ts, starts):
    """Tokens die ontstonden na de start van volledige logging. gap=1 als de bot binnen 2 uur na hun creatie
    herstartte: dan ontbreekt het drukste deel van hun trades en tellen ze niet mee. (Eerder was dit 6 uur, maar
    dan kostte elke herstart zes uur aan tokens, terwijl na 2 uur vrijwel alle handel voorbij is.)"""
    out = {}
    later = sorted(s for s in starts if s > start_ts + 60)
    for mint, cts, slot, creator, np_ts, mig in main.execute(
            "SELECT mint, created_ts, create_slot, creator, filter_newpairs_ts, migrated_ts FROM tokens WHERE created_ts >= ?", (start_ts,)):
        i = bisect.bisect_left(later, cts)
        gap = int(i < len(later) and later[i] < cts + GAP_WINDOW_S)
        out[mint] = (cts, slot, creator, np_ts, mig, gap)
    return out


def ingest(main, led, toks, max_rowid, batch=200_000):
    """max_rowid is vastgelegd vóór het laden van de tokens: elke trade tot die rij hoort bij een token dat we kennen."""
    last = meta_get(led, "last_rowid", 0); n_rows = n_used = 0
    while last < max_rowid:
        rows = main.execute("SELECT rowid, mint, ts, slot, user, is_buy, sol, tokens, v_sol, v_tok FROM trades WHERE rowid > ? AND rowid <= ? ORDER BY rowid LIMIT ?",
                            (last, max_rowid, batch)).fetchall()
        if not rows: break
        wt, wh, tk = {}, defaultdict(lambda: [0.0, 0.0]), {}
        for rid, mint, ts, slot, user, is_buy, sol, tok, vs, vt in rows:
            last = rid; n_rows += 1
            if mint not in toks: continue
            n_used += 1
            key = (user, mint); r = wt.get(key)
            if r is None: r = wt[key] = [ts, ts, 0.0, 0.0, 0, 0, 0, 0, None, None]
            r[1] = ts
            if is_buy:
                cost = sol * (1 + FEE); r[2] += cost; r[4] += tok; r[6] += 1
                if r[8] is None: r[8], r[9] = ts, slot
                wh[(user, int(ts // 3600))][0] += cost
            else:
                got = sol * (1 - FEE); r[3] += got; r[5] += tok; r[7] += 1
                wh[(user, int(ts // 3600))][1] += got
            t = tk.get(mint)
            if t is None: t = tk[mint] = [ts, vs, vt, 0]
            t[0], t[1], t[2] = ts, vs, vt; t[3] += 1
        led.executemany("""INSERT INTO wt VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(wallet, mint) DO UPDATE SET
            last_ts = max(last_ts, excluded.last_ts), sol_out = sol_out + excluded.sol_out, sol_in = sol_in + excluded.sol_in,
            tok_buy = tok_buy + excluded.tok_buy, tok_sell = tok_sell + excluded.tok_sell, n_buy = n_buy + excluded.n_buy,
            n_sell = n_sell + excluded.n_sell, first_buy_ts = coalesce(first_buy_ts, excluded.first_buy_ts),
            first_buy_slot = coalesce(first_buy_slot, excluded.first_buy_slot)""",
                        [(u, m, *v) for (u, m), v in wt.items()])
        led.executemany("""INSERT INTO wh VALUES(?,?,?,?) ON CONFLICT(wallet, hour) DO UPDATE SET
            sol_out = sol_out + excluded.sol_out, sol_in = sol_in + excluded.sol_in""", [(u, h, a, b) for (u, h), (a, b) in wh.items()])
        led.executemany("""INSERT INTO token(mint, last_ts, v_sol, v_tok, n_trades) VALUES(?,?,?,?,?) ON CONFLICT(mint) DO UPDATE SET
            last_ts = excluded.last_ts, v_sol = excluded.v_sol, v_tok = excluded.v_tok, n_trades = n_trades + excluded.n_trades""",
                        [(m, *v) for m, v in tk.items()])
        meta_set(led, "last_rowid", last); led.commit()
        log(f"  ingelezen tot rowid {last} ({n_rows} rijen, {n_used} bruikbaar)")
    # tokeninformatie bijwerken (migratie en $7k-moment komen later binnen)
    led.executemany("""INSERT INTO token(mint, created_ts, create_slot, creator, np_ts, migrated_ts, gap) VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(mint) DO UPDATE SET created_ts = excluded.created_ts, create_slot = excluded.create_slot, creator = excluded.creator,
        np_ts = excluded.np_ts, migrated_ts = excluded.migrated_ts, gap = excluded.gap""", [(m, *v) for m, v in toks.items()])
    led.commit()
    return n_rows, n_used


# ----------------------------------------------------------------- 2. analyse
ROLE_SQL = """CASE
  WHEN t.creator = w.wallet THEN 'dev'
  WHEN w.first_buy_ts IS NULL THEN 'zonder_koop'
  WHEN w.first_buy_slot = t.create_slot THEN 'bundel_creatieblok'
  WHEN w.first_buy_ts - t.created_ts <= 5 THEN 'sniper_5s'
  WHEN t.np_ts IS NULL OR w.first_buy_ts < t.np_ts THEN 'vroeg_onder_7k'
  ELSE 'laat_vanaf_7k' END"""
CLOSED_SQL = "(w.tok_buy > 0 AND w.tok_sell >= 0.99 * w.tok_buy)"


def money_flow(led, now):
    dead = f"(NOT {CLOSED_SQL} AND t.migrated_ts IS NULL AND t.last_ts < {now - DEAD_AFTER_S})"
    rows = led.execute(f"""SELECT {ROLE_SQL} AS rol, COUNT(*), COUNT(DISTINCT w.wallet), SUM(w.sol_out), SUM(w.sol_in),
        SUM(CASE WHEN w.sol_in > w.sol_out THEN 1 ELSE 0 END),
        SUM(CASE WHEN {CLOSED_SQL} OR {dead} THEN 1 ELSE 0 END),
        SUM(CASE WHEN ({CLOSED_SQL} OR {dead}) AND w.sol_in > w.sol_out THEN 1 ELSE 0 END)
        FROM wt w JOIN token t ON t.mint = w.mint WHERE t.created_ts IS NOT NULL AND t.gap = 0 GROUP BY rol""").fetchall()
    per = {}
    for rol, n, nw, so, si, npos, nfin, nfinwin in rows:
        per[rol] = {"posities": n, "wallets": nw, "sol_erin": round(so or 0, 2), "sol_eruit": round(si or 0, 2),
                    "netto": round((si or 0) - (so or 0), 2), "aandeel_posities_met_winst": round(npos / n, 3) if n else None,
                    "afgerond": nfin, "winkans_afgerond": round(nfinwin / nfin, 3) if nfin else None}
    tot_in = sum(p["sol_erin"] for p in per.values()); tot_out = sum(p["sol_eruit"] for p in per.values())
    mig_open = led.execute(f"""SELECT COALESCE(SUM(w.sol_out - w.sol_in), 0) FROM wt w JOIN token t ON t.mint = w.mint
        WHERE t.migrated_ts IS NOT NULL AND t.gap = 0 AND NOT {CLOSED_SQL}""").fetchone()[0]
    nets = [r[0] for r in led.execute("""SELECT SUM(w.sol_in) - SUM(w.sol_out) FROM wt w JOIN token t ON t.mint = w.mint
        WHERE t.created_ts IS NOT NULL AND t.gap = 0 GROUP BY w.wallet""")]
    pos = sorted((x for x in nets if x > 0), reverse=True); neg = [x for x in nets if x < 0]
    share = lambda k: round(sum(pos[:k]) / sum(pos), 3) if pos else None
    return {
        "per_rol": per, "totaal_sol_in_aankopen": round(tot_in, 2), "totaal_sol_uit_verkopen": round(tot_out, 2),
        "pump_fee_geschat": round((tot_in / (1 + FEE)) * FEE + (tot_out / (1 - FEE)) * FEE, 2),
        "open_in_gemigreerde_tokens": round(mig_open, 2),
        "wallets": len(nets), "wallets_netto_plus": len(pos), "som_plus": round(sum(pos), 2),
        "wallets_netto_min": len(neg), "som_min": round(sum(neg), 2),
        "aandeel_winst_top10": share(10), "aandeel_winst_top100": share(100),
        "aandeel_winst_top_1pct": share(max(1, len(pos) // 100)),
    }


def wallet_stats(led, now, wallets=None, having="", order="", limit=None):
    dead = f"(NOT {CLOSED_SQL} AND t.migrated_ts IS NULL AND t.last_ts < {now - DEAD_AFTER_S})"
    where = "WHERE t.created_ts IS NOT NULL AND t.gap = 0"; args = ()
    if wallets is not None:
        if not wallets: return {}
        where += f" AND w.wallet IN ({','.join('?' * len(wallets))})"; args = tuple(wallets)
    q = f"""SELECT w.wallet, COUNT(*) n, SUM(w.sol_out) so, SUM(w.sol_in) si,
        SUM(CASE WHEN {CLOSED_SQL} OR {dead} THEN 1 ELSE 0 END) nfin,
        SUM(CASE WHEN ({CLOSED_SQL} OR {dead}) AND w.sol_in > w.sol_out THEN 1 ELSE 0 END) nwin,
        SUM(CASE WHEN t.creator = w.wallet THEN 1 ELSE 0 END),
        SUM(CASE WHEN w.first_buy_slot = t.create_slot AND t.creator != w.wallet THEN 1 ELSE 0 END),
        SUM(CASE WHEN w.first_buy_ts - t.created_ts <= 5 AND t.creator != w.wallet AND w.first_buy_slot != t.create_slot THEN 1 ELSE 0 END),
        SUM(CASE WHEN w.first_buy_ts IS NULL THEN 1 ELSE 0 END),
        SUM(CASE WHEN t.migrated_ts IS NOT NULL AND NOT {CLOSED_SQL} THEN 1 ELSE 0 END),
        MIN(w.first_ts), MAX(w.last_ts)
        FROM wt w JOIN token t ON t.mint = w.mint {where} GROUP BY w.wallet {having} {order} {'LIMIT ' + str(int(limit)) if limit else ''}"""
    out = {}
    for (w, n, so, si, nfin, nwin, ndev, nbun, nsnip, nnobuy, nmig, f0, f1) in led.execute(q, args):
        out[w] = {"tokens": n, "sol_erin": round(so, 3), "sol_eruit": round(si, 3), "netto": round(si - so, 3),
                  "afgerond": nfin, "winkans": round(nwin / nfin, 3) if nfin else None,
                  "dev_aandeel": round(ndev / n, 3), "bundel_aandeel": round(nbun / n, 3), "sniper_aandeel": round(nsnip / n, 3),
                  "zonder_koop_aandeel": round(nnobuy / n, 3), "open_gemigreerd": nmig, "actief_van": f0, "actief_tot": f1}
    return out


def growth(led, wallet):
    rows = led.execute("SELECT hour, sol_in - sol_out FROM wh WHERE wallet = ? ORDER BY hour", (wallet,)).fetchall()
    cum = peak = dd = 0.0; blocks = defaultdict(float)
    for h, net in rows:
        cum += net; peak = max(peak, cum); dd = max(dd, peak - cum); blocks[h // 6] += net
    pos_blocks = sum(1 for v in blocks.values() if v > 0)
    return {"piek": round(peak, 3), "max_drawdown_sol": round(dd, 3), "drawdown_van_piek": round(dd / peak, 3) if peak > 0 else None,
            "actieve_6u_blokken": len(blocks), "aandeel_positieve_6u_blokken": round(pos_blocks / len(blocks), 3) if blocks else None}


def qualifies(s, g):
    c = CRITERIA
    return (s["afgerond"] >= c["min_tokens_afgerond"] and (s["winkans"] or 0) >= c["min_winkans_tokens"] and s["netto"] > c["min_netto_sol"]
            and g["drawdown_van_piek"] is not None and g["drawdown_van_piek"] <= c["max_drawdown_van_piek"]
            and g["actieve_6u_blokken"] >= c["min_actieve_6u_blokken"]
            and (g["aandeel_positieve_6u_blokken"] or 0) >= c["min_aandeel_positieve_6u_blokken"]
            and s["dev_aandeel"] <= c["max_dev_aandeel"] and s["bundel_aandeel"] <= c["max_bundel_aandeel"])


# ----------------------------------------------------------------- 3. vooruit-toets op aankopen van groeiers
def price(vs, vt): return vs / vt if vt else 0.0


def eval_signal(main, mint, wallet, buy_ts):
    rows = main.execute("SELECT ts, user, is_buy, tokens, v_sol, v_tok FROM trades INDEXED BY trades_mint_ts WHERE mint = ? AND ts >= ? AND ts <= ? ORDER BY ts",
                        (mint, buy_ts - 1, buy_ts + SIGNAL_WINDOW_S + 120)).fetchall()
    if not rows: return None
    tsa = [r[0] for r in rows]
    def st(t):
        i = max(0, bisect.bisect_right(tsa, t) - 1); return int(rows[i][4]), int(rows[i][5])
    vs, vt = st(buy_ts + 2); p0 = price(vs, vt)
    if p0 <= 0: return None
    tok, _ = curve.buy(vs, vt, COPY_SIZE, "pp")
    note = []
    def ret_at(t):
        if t > tsa[-1] + 1 and tsa[-1] < buy_ts + SIGNAL_WINDOW_S: note.append("data_eindigt")
        v2, t2 = st(t); return price(v2, t2) / p0 - 1
    r = {k: round(ret_at(buy_ts + 2 + s), 4) for k, s in (("r1", 60), ("r5", 300), ("r15", 900), ("r60", 3600))}
    r["max15"] = round(max(price(int(x[4]), int(x[5])) for x in rows if buy_ts + 2 <= x[0] <= buy_ts + 902) / p0 - 1, 4) if any(buy_ts + 2 <= x[0] <= buy_ts + 902 for x in rows) else 0.0
    def sell_ret(t):
        v2, t2 = st(t); out, _ = curve.sell(v2, t2, tok, "pp"); return round((out - COPY_SIZE - C.PRIO_FEE_SOL) / COPY_SIZE, 4)
    # volgen: verkopen 2 s nadat de wallet de helft van zijn tokens heeft verkocht, anders na 60 min
    bought = sold = 0; exit_t = buy_ts + SIGNAL_WINDOW_S
    for ts, user, is_buy, tk, _, _ in rows:
        if user != wallet: continue
        if is_buy: bought += tk
        else:
            sold += tk
            if bought and sold >= 0.5 * bought: exit_t = ts + 2; break
    r["ret_volg"] = sell_ret(exit_t)
    # videoregel: uit zodra de koers onder de instapprijs zakt (-3% marge), winst nemen op +45%, max 60 min
    exit_t = buy_ts + SIGNAL_WINDOW_S
    for ts, _, _, _, a, b in rows:
        if ts <= buy_ts + 2: continue
        p = price(int(a), int(b)) / p0 - 1
        if p <= -C.V1_STOP_MARGIN or p >= C.V1_TP: exit_t = ts + 2; break
    r["ret_video"] = sell_ret(exit_t)
    r["opmerking"] = ",".join(sorted(set(note)))
    return r


def run_signals(main, led, now, max_new=3000):
    todo = led.execute(f"""SELECT w.wallet, w.mint, w.first_buy_ts, wa.added_ts FROM wt w JOIN watch wa ON wa.wallet = w.wallet
        JOIN token t ON t.mint = w.mint AND t.gap = 0
        LEFT JOIN signal s ON s.wallet = w.wallet AND s.mint = w.mint
        WHERE s.wallet IS NULL AND w.first_buy_ts IS NOT NULL AND w.first_buy_ts < ? ORDER BY w.first_buy_ts LIMIT ?""",
                       (now - SIGNAL_WINDOW_S - 300, max_new)).fetchall()
    for wallet, mint, buy_ts, added in todo:
        r = eval_signal(main, mint, wallet, buy_ts)
        if r is None: continue
        led.execute("INSERT OR REPLACE INTO signal VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (wallet, mint, buy_ts, int(buy_ts >= added), r["r1"], r["r5"], r["r15"], r["r60"], r["max15"], r["ret_volg"], r["ret_video"], r["opmerking"]))
    led.commit()
    return len(todo)


def signal_per_wallet(led):
    rows = led.execute("""SELECT wallet, COUNT(*), AVG(r15), AVG(max15), AVG(ret_volg), AVG(ret_video),
        AVG(CASE WHEN ret_volg > 0 THEN 1.0 ELSE 0 END) FROM signal WHERE na_opname = 1 GROUP BY wallet ORDER BY COUNT(*) DESC LIMIT 40""").fetchall()
    return [{"wallet": w, "n": n, "koers_+15m": round(a, 4), "max_binnen_15m": round(b, 4), "kopie_volgen": round(c, 4),
             "kopie_videoregel": round(d, 4), "aandeel_kopie_volgen_plus": round(e, 3)} for w, n, a, b, c, d, e in rows]


def signal_summary(led, handmatig=False):
    out = {}
    op = "=" if handmatig else "!="
    for label, cond in (("vooruit (na opname in lijst)", 1), ("terugkijkend (vóór opname, optimistisch)", 0)):
        rows = led.execute(f"""SELECT s.r1, s.r5, s.r15, s.r60, s.max15, s.ret_volg, s.ret_video FROM signal s JOIN watch w ON w.wallet = s.wallet
            WHERE s.na_opname = ? AND w.versie {op} ?""", (cond, MANUAL)).fetchall()
        if not rows: out[label] = {"n": 0}; continue
        col = lambda i: [r[i] for r in rows if r[i] is not None]
        def summ(xs):
            return {"gem": round(sum(xs) / len(xs), 4), "mediaan": round(statistics.median(xs), 4), "aandeel_plus": round(sum(1 for x in xs if x > 0) / len(xs), 3)} if xs else None
        out[label] = {"n": len(rows), "koers_+1m": summ(col(0)), "koers_+5m": summ(col(1)), "koers_+15m": summ(col(2)), "koers_+60m": summ(col(3)),
                      "max_binnen_15m": summ(col(4)), "kopie_volgen": summ(col(5)), "kopie_videoregel": summ(col(6))}
    return out


# ----------------------------------------------------------------- 4. handmatig gevolgde wallets
def load_manual(path):
    """volg_wallets.txt: één adres per regel, optioneel '# notitie'. Te bewerken via GitHub."""
    out = {}
    if not os.path.exists(path): return out
    for line in open(path, encoding="utf-8"):
        addr, _, note = line.partition("#"); addr = addr.strip()
        if 32 <= len(addr) <= 44: out[addr] = note.strip()
    return out


def trend(led, wallet):
    rows = led.execute("SELECT ts, netto, afgerond, winkans FROM watch_snap WHERE wallet = ? ORDER BY ts", (wallet,)).fetchall()
    if not rows: return None
    return {"eerste_meting": iso(rows[0][0]), "netto_toen": rows[0][1], "metingen": len(rows),
            "reeks": [{"ts": iso(t), "netto": n} for t, n, _, _ in rows[-12:]]}


# ----------------------------------------------------------------- 5. herkomst van 'zonder koop'-tokens
class RpcHttp:
    def __init__(self, url, rps):
        self.url, self.gap, self.last, self.calls, self.errors = url, 1.0 / rps, 0.0, 0, 0
    def call(self, method, params):
        import urllib.request
        wait = self.last + self.gap - time.time()
        if wait > 0: time.sleep(wait)
        self.last = time.time(); self.calls += 1
        body = json.dumps({"jsonrpc": "2.0", "id": self.calls, "method": method, "params": params}).encode()
        try:
            req = urllib.request.Request(self.url, data=body, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                j = json.loads(r.read().decode())
            if "error" in j: self.errors += 1; return None
            return j.get("result")
        except Exception:
            self.errors += 1; return None


def token_deltas(tx, mint):
    meta = (tx or {}).get("meta") or {}
    d = {}
    for sign, key in ((-1, "preTokenBalances"), (1, "postTokenBalances")):
        for b in meta.get(key) or []:
            if b.get("mint") != mint or not b.get("owner"): continue
            amt = int((b.get("uiTokenAmount") or {}).get("amount") or 0)
            d[b["owner"]] = d.get(b["owner"], 0) + sign * amt
    return d


def find_sender(rpc, wallet, mint, created_ts, first_sell_ts, curve, max_pages=3, max_tx=15):
    """Zoekt de transactie waarin 'wallet' tokens van 'mint' ontving zonder ze op de curve te kopen."""
    before, cands = None, []
    for _ in range(max_pages):
        opts = {"limit": 1000, "commitment": "confirmed"}
        if before: opts["before"] = before
        page = rpc.call("getSignaturesForAddress", [wallet, opts])
        if not page: break
        for p in page:
            bt = p.get("blockTime") or 0
            if created_ts - 60 <= bt <= first_sell_ts + 5 and not p.get("err"): cands.append((bt, p["signature"]))
        before = page[-1]["signature"]
        if (page[-1].get("blockTime") or 0) < created_ts - 60 or len(page) < 1000: break
    for bt, sig in sorted(cands)[:max_tx]:
        tx = rpc.call("getTransaction", [sig, {"encoding": "jsonParsed", "maxSupportedTransactionVersion": 0, "commitment": "confirmed"}])
        d = token_deltas(tx, mint)
        if d.get(wallet, 0) <= 0: continue
        senders = sorted((v, o) for o, v in d.items() if v < 0 and o != wallet and o != curve)
        if senders: return senders[0][1], bt, "overdracht"
        keys = ((tx.get("transaction") or {}).get("message") or {}).get("accountKeys") or []
        payer = keys[0].get("pubkey") if keys and isinstance(keys[0], dict) else (keys[0] if keys else None)
        if payer and payer != wallet: return payer, bt, "gekocht door ander in dezelfde transactie"
        return None, bt, "ontvangen, afzender onduidelijk"
    return None, None, "niet gevonden" if cands else "geen transacties in venster"


def run_herkomst(main, led, now, rpc):
    curves = {}
    todo = led.execute("""SELECT w.wallet, w.mint, t.created_ts, w.first_ts, w.sol_in FROM wt w JOIN token t ON t.mint = w.mint AND t.gap = 0
        LEFT JOIN herkomst h ON h.wallet = w.wallet AND h.mint = w.mint
        WHERE w.first_buy_ts IS NULL AND w.sol_in >= ? AND h.wallet IS NULL ORDER BY w.sol_in DESC LIMIT ?""",
                       (HERKOMST_MIN_SOL, HERKOMST_PER_RUN)).fetchall()
    for wallet, mint, cts, first_ts, _ in todo:
        if mint not in curves:
            r = main.execute("SELECT bonding_curve FROM tokens WHERE mint = ?", (mint,)).fetchone(); curves[mint] = r[0] if r else None
        try:
            afz, bt, note = find_sender(rpc, wallet, mint, cts, first_ts, curves[mint])
        except Exception as e:
            afz, bt, note = None, None, f"fout: {str(e)[:60]}"
        led.execute("INSERT OR REPLACE INTO herkomst VALUES(?,?,?,?,?,?)", (wallet, mint, afz, bt, note, now)); led.commit()
    return len(todo)


def herkomst_report(led):
    rows = led.execute("""SELECT h.afzender, COUNT(DISTINCT h.wallet), COUNT(DISTINCT h.mint), SUM(w.sol_in),
        GROUP_CONCAT(DISTINCT h.mint) FROM herkomst h JOIN wt w ON w.wallet = h.wallet AND w.mint = h.mint
        WHERE h.afzender IS NOT NULL GROUP BY h.afzender ORDER BY SUM(w.sol_in) DESC LIMIT 15""").fetchall()
    out = []
    for afz, n_w, n_m, fed_in, mints in rows:
        ml = mints.split(",")
        own = led.execute(f"""SELECT COALESCE(SUM(w.sol_out), 0), COALESCE(SUM(w.sol_in), 0), SUM(CASE WHEN t.creator = w.wallet THEN 1 ELSE 0 END),
            SUM(CASE WHEN w.first_buy_slot = t.create_slot THEN 1 ELSE 0 END) FROM wt w JOIN token t ON t.mint = w.mint
            WHERE w.wallet = ? AND w.mint IN ({','.join('?' * len(ml))})""", (afz, *ml)).fetchone()
        out.append({"afzender": afz, "doorstuur_wallets": n_w, "tokens": n_m, "opbrengst_doorstuurwallets": round(fed_in, 2),
                    "afzender_erin": round(own[0], 2), "afzender_eruit": round(own[1], 2),
                    "cluster_netto": round(fed_in + own[1] - own[0], 2), "afzender_is_dev_op": own[2] or 0, "afzender_kocht_in_creatieblok_op": own[3] or 0})
    stats = dict(led.execute("SELECT notitie, COUNT(*) FROM herkomst GROUP BY notitie").fetchall())
    return {"clusters": out, "status": stats}


# ----------------------------------------------------------------- 6. grote spelers
_P = 2**255 - 19
_D = (-121665 * pow(121666, _P - 2, _P)) % _P
_I = pow(2, (_P - 1) // 4, _P)


def on_curve(addr):
    """True = gewoon adres met privésleutel; False = programma-adres (PDA), bv. een kluis van een botplatform.
    Zelfde toets als Solana's isOnCurve (ed25519-decompressie)."""
    import base58
    try: b = base58.b58decode(addr)
    except Exception: return None
    if len(b) != 32: return None
    y = int.from_bytes(b, "little") & ((1 << 255) - 1); sign = b[31] >> 7
    if y >= _P: return False
    u = (y * y - 1) % _P; v = (_D * y * y + 1) % _P
    x2 = u * pow(v, _P - 2, _P) % _P
    if x2 == 0: return sign == 0
    x = pow(x2, (_P + 3) // 8, _P)
    if (x * x - x2) % _P != 0:
        x = x * _I % _P
        if (x * x - x2) % _P != 0: return False
    return True


def refresh_wallet_info(led, rpc, wallets, now):
    todo = [w for w in wallets if not (r := led.execute("SELECT gecheckt_ts FROM wallet_info WHERE wallet = ?", (w,)).fetchone()) or r[0] < now - SALDO_VERVERSEN_S]
    for i in range(0, len(todo), 100):
        chunk = todo[i:i + 100]
        res = rpc.call("getMultipleAccounts", [chunk, {"encoding": "base64", "dataSlice": {"offset": 0, "length": 0}, "commitment": "confirmed"}])
        if res is None: continue
        for w, acc in zip(chunk, res.get("value") or [None] * len(chunk)):
            led.execute("INSERT OR REPLACE INTO wallet_info VALUES(?,?,?,?,?)",
                        (w, (acc or {}).get("lamports", 0) / 1e9, (acc or {}).get("owner"), None if (oc := on_curve(w)) is None else int(oc), now))
        led.commit()
    return len(todo)


def profile(s, med_hold):
    if s["dev_aandeel"] >= 0.10 or s["bundel_aandeel"] >= 0.20 or s["zonder_koop_aandeel"] >= 0.20: return "insider (dev/bundel/doorstuur)"
    if s["sniper_aandeel"] >= 0.50: return "sniper (≤ 5 s)"
    if med_hold is not None and med_hold < 60: return "snelle scalper (< 1 min)"
    if med_hold is not None and med_hold < 600: return "scalper (1–10 min)"
    return "swing (≥ 10 min)"


def ranks_of(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0.0] * len(xs)
    for pos, i in enumerate(order): r[i] = pos
    return r


def spearman(a, b):
    n = len(a)
    if n < 8: return None
    ra, rb = ranks_of(a), ranks_of(b); ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = math.sqrt(sum((x - ma) ** 2 for x in ra)); vb = math.sqrt(sum((y - mb) ** 2 for y in rb))
    return round(cov / (va * vb), 3) if va and vb else None


def big_players(led, now, rpc):
    top = wallet_stats(led, now, order="ORDER BY so + si DESC", limit=GROOT_KANDIDATEN)
    if rpc is not None:
        n = refresh_wallet_info(led, rpc, list(top), now); log(f"grote spelers: saldo van {n} wallets opgehaald")
    info = {w: (bal, own, oc) for w, bal, own, oc in led.execute("SELECT wallet, sol_saldo, eigenaar, op_curve FROM wallet_info")}
    big, rest = [], []
    for w, s in top.items():
        if s["tokens"] < GROOT_MIN_TOKENS: continue
        bal, own, oc = info.get(w, (None, None, None))
        is_big = (bal or 0) >= GROOT_SALDO_SOL or (s["sol_erin"] + s["sol_eruit"]) >= GROOT_VOLUME_SOL
        (big if is_big else rest).append((w, s, bal, own, oc))
    if not big: return {"n_groot": 0, "kandidaten": len(top), "saldo_bekend": len(info)}
    holds = defaultdict(list)
    ws = [w for w, *_ in big]
    for i in range(0, len(ws), 500):
        chunk = ws[i:i + 500]
        for w, h in led.execute(f"""SELECT wallet, last_ts - first_buy_ts FROM wt WHERE wallet IN ({','.join('?' * len(chunk))})
                                    AND first_buy_ts IS NOT NULL AND tok_buy > 0 AND tok_sell >= 0.99 * tok_buy""", chunk):
            holds[w].append(h)
    rows = []
    for w, s, bal, own, oc in big:
        mh = statistics.median(holds[w]) if holds.get(w) else None
        roi = s["netto"] / s["sol_erin"] if s["sol_erin"] > 0 else None
        g = growth(led, w)
        kind = "onbekend" if oc is None else ("gewone wallet" if oc else "programma-adres (PDA)")
        if own and own != "11111111111111111111111111111111": kind += f", eigenaar {own[:4]}…"
        rows.append({"wallet": w, "sol_saldo": round(bal, 1) if bal is not None else None, "adres_type": kind, "profiel": profile(s, mh),
                     "roi": round(roi, 4) if roi is not None else None, "med_houdtijd_s": round(mh) if mh is not None else None, **s, **g})
    per = defaultdict(list)
    for r in rows: per[r["profiel"]].append(r)
    def agg(rs):
        rois = [r["roi"] for r in rs if r["roi"] is not None]
        return {"wallets": len(rs), "aandeel_netto_plus": round(sum(1 for r in rs if r["netto"] > 0) / len(rs), 3),
                "som_netto": round(sum(r["netto"] for r in rs), 2), "mediaan_roi": round(statistics.median(rois), 4) if rois else None,
                "mediaan_winkans": round(statistics.median([r["winkans"] for r in rs if r["winkans"] is not None]), 3) if any(r["winkans"] is not None for r in rs) else None}
    rest_rows = [s for _, s, *_ in rest]
    rest_rois = [s["netto"] / s["sol_erin"] for s in rest_rows if s["sol_erin"] > 0]
    with_bal = [r for r in rows if r["sol_saldo"] is not None and r["roi"] is not None]
    return {
        "kandidaten": len(top), "n_groot": len(rows), "n_pda": sum(1 for r in rows if "PDA" in r["adres_type"]),
        "drempels": {"saldo_sol": GROOT_SALDO_SOL, "volume_sol": GROOT_VOLUME_SOL, "min_tokens": GROOT_MIN_TOKENS},
        "per_profiel": {k: agg(v) for k, v in sorted(per.items())},
        "groot_vs_rest": {"groot": agg(rows), "rest_actief": {"wallets": len(rest_rows),
                          "aandeel_netto_plus": round(sum(1 for s in rest_rows if s["netto"] > 0) / len(rest_rows), 3) if rest_rows else None,
                          "mediaan_roi": round(statistics.median(rest_rois), 4) if rest_rois else None}},
        "spearman_saldo_roi": spearman([r["sol_saldo"] for r in with_bal], [r["roi"] for r in with_bal]),
        "spearman_volume_roi": spearman([r["sol_erin"] + r["sol_eruit"] for r in rows if r["roi"] is not None], [r["roi"] for r in rows if r["roi"] is not None]),
        "top": sorted(rows, key=lambda r: -r["netto"])[:25],
        "top_roi_min20": sorted([r for r in rows if r["afgerond"] >= 20 and r["roi"] is not None], key=lambda r: -r["roi"])[:15],
    }


# ----------------------------------------------------------------- rapport
def to_md(rep):
    L = []; add = L.append
    add(f"# Geldstroom per wallet — {rep['gegenereerd']}\n")
    d = rep["dekking"]
    add(f"Gemeten sinds {d['sinds']} ({d['uren']} uur). {d['tokens']} tokens met volledige geschiedenis, {d['wallets']} wallets, "
        f"{d['posities']} wallet-token-posities ({d['tokens_met_gat']} tokens overgeslagen door een herstart). Bedragen in SOL, inclusief pump-fee, zonder waardering van tokens die nog in bezit zijn.\n")
    mf = rep["geldstroom"]
    add("## Waar gaat het geld naartoe\n")
    add("| rol (eerste aankoop) | posities | wallets | SOL erin | SOL eruit | netto | posities met winst | winkans afgerond |")
    add("|---|---|---|---|---|---|---|---|")
    order = ["dev", "bundel_creatieblok", "sniper_5s", "vroeg_onder_7k", "laat_vanaf_7k", "zonder_koop"]
    for rol in order:
        p = mf["per_rol"].get(rol)
        if not p: continue
        add(f"| {rol} | {p['posities']} | {p['wallets']} | {p['sol_erin']:.2f} | {p['sol_eruit']:.2f} | {p['netto']:+.2f} | "
            f"{pct(p['aandeel_posities_met_winst'])} | {pct(p['winkans_afgerond'])} |")
    add(f"\nTotaal in aankopen {mf['totaal_sol_in_aankopen']:.2f} SOL, uit verkopen {mf['totaal_sol_uit_verkopen']:.2f} SOL. "
        f"Pump-fee ongeveer {mf['pump_fee_geschat']:.2f} SOL. Nog open in tokens die naar PumpSwap migreerden: {mf['open_in_gemigreerde_tokens']:.2f} SOL "
        "(daar handelen we niet mee, dus die uitkomst zien we niet).")
    add(f"\n{mf['wallets_netto_plus']} wallets staan netto in de plus (samen {mf['som_plus']:+.2f} SOL), {mf['wallets_netto_min']} in de min "
        f"({mf['som_min']:+.2f} SOL). De top 10 pakt {pct(mf['aandeel_winst_top10'])} van alle plus, de top 100 {pct(mf['aandeel_winst_top100'])}, "
        f"de top 1% {pct(mf['aandeel_winst_top_1pct'])}.")
    add("\nRollen: dev = maakte het token; bundel_creatieblok = kocht in hetzelfde blok als de creatie; sniper_5s = kocht binnen 5 seconden; "
        "vroeg_onder_7k = kocht voordat het token $7k haalde; laat_vanaf_7k = kocht daarna; zonder_koop = verkocht tokens die hij niet op de curve kocht "
        "(doorgestuurd vanuit een andere wallet, typisch voor bundels). 'Winkans afgerond' telt alleen posities die verkocht zijn of waarvan het token dood is.")
    add("\n## Top 25 op netto instroom (zonder filters)\n")
    add("| # | wallet | netto | erin | eruit | tokens | afgerond | winkans | dev | bundel | sniper | zonder koop |")
    add("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rep["top_netto"], 1):
        add(f"| {i} | {link(r['wallet'])} | {r['netto']:+.2f} | {r['sol_erin']:.2f} | {r['sol_eruit']:.2f} | {r['tokens']} | {r['afgerond']} | {pct(r['winkans'])} | "
            f"{pct(r['dev_aandeel'])} | {pct(r['bundel_aandeel'])} | {pct(r['sniper_aandeel'])} | {pct(r['zonder_koop_aandeel'])} |")
    add("\n## Groeiers (vooraf vastgelegde criteria, " + CRITERIA_VERSIE + ")\n")
    add("Criteria: " + ", ".join(f"{k} = {v}" for k, v in CRITERIA.items()) + ".\n")
    if rep["groeiers"]:
        add("| wallet | op lijst sinds | netto | afgerond | winkans | drawdown van piek | positieve 6u-blokken | sniper | kandidaat nu |")
        add("|---|---|---|---|---|---|---|---|---|")
        for r in rep["groeiers"]:
            add(f"| {link(r['wallet'])} | {r['op_lijst_sinds']} | {r['netto']:+.2f} | {r['afgerond']} | {pct(r['winkans'])} | {pct(r['drawdown_van_piek'])} | "
                f"{pct(r['aandeel_positieve_6u_blokken'])} ({r['actieve_6u_blokken']}) | {pct(r['sniper_aandeel'])} | {'ja' if r['voldoet_nu'] else 'nee'} |")
    else:
        add("Nog geen wallets die aan alle criteria voldoen.\n")
    if rep["bijna"]:
        add(f"\n### Bijna-groeiers (≥ {CRITERIA['min_tokens_afgerond']} afgerond en netto plus, maar niet alle criteria)\n")
        add("| wallet | netto | afgerond | winkans | drawdown van piek | positieve 6u-blokken | dev | bundel | sniper | faalt op |")
        add("|---|---|---|---|---|---|---|---|---|---|")
        for r in rep["bijna"]:
            add(f"| {link(r['wallet'])} | {r['netto']:+.2f} | {r['afgerond']} | {pct(r['winkans'])} | {pct(r['drawdown_van_piek'])} | "
                f"{pct(r['aandeel_positieve_6u_blokken'])} ({r['actieve_6u_blokken']}) | {pct(r['dev_aandeel'])} | {pct(r['bundel_aandeel'])} | {pct(r['sniper_aandeel'])} | {r['faalt_op']} |")
    if rep.get("handmatig"):
        add("\n## Handmatig gevolgde wallets (volg_wallets.txt)\n")
        add("Alleen tokens met volledige geschiedenis tellen mee. Netto = SOL uit verkopen min SOL in aankopen op de pump.fun-curve; "
            "het totale walletsaldo zegt daar niets over.\n")
        add("| wallet | notitie | sinds | netto | erin | tokens | afgerond | winkans | sniper | bundel | drawdown van piek | netto bij eerste meting | groeier-criteria |")
        add("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rep["handmatig"]:
            if not r.get("tokens"):
                add(f"| {link(r['wallet'])} | {r['notitie']} | {r['op_lijst_sinds']} | nog geen trades gezien | | | | | | | | | |"); continue
            t = r.get("trend") or {}
            add(f"| {link(r['wallet'])} | {r['notitie']} | {r['op_lijst_sinds']} | {r['netto']:+.2f} | {r['sol_erin']:.2f} | {r['tokens']} | {r['afgerond']} | "
                f"{pct(r['winkans'])} | {pct(r['sniper_aandeel'])} | {pct(r['bundel_aandeel'])} | {pct(r['drawdown_van_piek'])} | "
                f"{t.get('netto_toen', 0):+.2f} ({t.get('eerste_meting', '–')}) | {'ja' if r.get('voldoet_aan_groeiers_criteria') else 'nee'} |")
        vh = rep.get("vooruit_toets_handmatig", {})
        for label, sm in vh.items():
            if sm.get("n"):
                add(f"\n**{label}, handmatig gevolgd** — {sm['n']} aankopen: koers +15 min gem. {sm['koers_+15m']['gem']:+.1%}, "
                    f"kopie volgen gem. {sm['kopie_volgen']['gem']:+.1%} ({sm['kopie_volgen']['aandeel_plus']:.0%} positief), "
                    f"videoregel gem. {sm['kopie_videoregel']['gem']:+.1%}.")
    gp = rep.get("grote_spelers") or {}
    add("\n## Grote spelers: patronen bij grote en actieve wallets\n")
    if gp.get("n_groot"):
        d_ = gp["drempels"]
        add(f"Van de {gp['kandidaten']} meest actieve wallets zijn er {gp['n_groot']} 'groot' (≥ {d_['saldo_sol']:.0f} SOL saldo of ≥ {d_['volume_sol']:.0f} SOL "
            f"verhandeld, en ≥ {d_['min_tokens']} tokens). {gp['n_pda']} daarvan zijn programma-adressen (PDA): kluizen van platforms of operators, geen losse personen.\n")
        add("| profiel | wallets | netto plus | som netto | mediaan ROI | mediaan winkans |"); add("|---|---|---|---|---|---|")
        for k, v in gp["per_profiel"].items():
            add(f"| {k} | {v['wallets']} | {pct(v['aandeel_netto_plus'])} | {v['som_netto']:+.2f} | {('–' if v['mediaan_roi'] is None else format(v['mediaan_roi'], '+.1%'))} | {pct(v['mediaan_winkans'])} |")
        g_, r_ = gp["groot_vs_rest"]["groot"], gp["groot_vs_rest"]["rest_actief"]
        add(f"\nGroot versus de overige actieve wallets: netto plus {pct(g_['aandeel_netto_plus'])} tegen {pct(r_['aandeel_netto_plus'])}, "
            f"mediaan ROI {('–' if g_['mediaan_roi'] is None else format(g_['mediaan_roi'], '+.1%'))} tegen {('–' if r_['mediaan_roi'] is None else format(r_['mediaan_roi'], '+.1%'))}. "
            f"Rangcorrelatie saldo ↔ ROI: {gp['spearman_saldo_roi']}; volume ↔ ROI: {gp['spearman_volume_roi']} (rond 0 = geen verband).\n")
        for key, title in (("top", "Top 25 grote spelers op netto"), ("top_roi_min20", "Hoogste ROI bij grote spelers (≥ 20 afgeronde tokens)")):
            add(f"**{title}**\n")
            add("| wallet | saldo SOL | adres | profiel | netto | erin | ROI | tokens | afgerond | winkans | sniper | med. houdtijd | positieve 6u-blokken |")
            add("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
            for r in gp[key]:
                add(f"| {link(r['wallet'])} | {('–' if r['sol_saldo'] is None else format(r['sol_saldo'], ',.0f'))} | {r['adres_type']} | {r['profiel']} | {r['netto']:+.2f} | {r['sol_erin']:.1f} | "
                    f"{('–' if r['roi'] is None else format(r['roi'], '+.1%'))} | {r['tokens']} | {r['afgerond']} | {pct(r['winkans'])} | {pct(r['sniper_aandeel'])} | "
                    f"{('–' if r['med_houdtijd_s'] is None else str(r['med_houdtijd_s']) + ' s')} | {pct(r['aandeel_positieve_6u_blokken'])} ({r['actieve_6u_blokken']}) |")
            add("")
    else:
        add("Nog geen grote spelers gevonden in de meetperiode.\n")
    hk = rep.get("herkomst") or {}
    add("\n## Herkomst van 'zonder koop'-winst: wie stuurde de tokens door?\n")
    add("Wallets die tokens verkopen zonder ze op de curve te kopen, kregen ze van een andere wallet. Per 'zonder koop'-positie zoeken we de "
        "transactie waarin de tokens binnenkwamen. Zo worden bundel-clusters zichtbaar: de koper in het creatieblok plus zijn doorstuurwallets.\n")
    if hk.get("clusters"):
        add("| afzender | doorstuurwallets | tokens | opbrengst doorstuurwallets | afzender erin | afzender eruit | cluster netto | afzender dev op | afzender kocht in creatieblok op |")
        add("|---|---|---|---|---|---|---|---|---|")
        for c in hk["clusters"]:
            add(f"| {link(c['afzender'])} | {c['doorstuur_wallets']} | {c['tokens']} | {c['opbrengst_doorstuurwallets']:.2f} | {c['afzender_erin']:.2f} | "
                f"{c['afzender_eruit']:.2f} | {c['cluster_netto']:+.2f} | {c['afzender_is_dev_op']} | {c['afzender_kocht_in_creatieblok_op']} |")
    add(f"\nStatus van de koppeling: {', '.join(f'{k}: {v}' for k, v in (hk.get('status') or {}).items()) or 'nog niets gecontroleerd'}.")
    add("\n## Vooruit-toets: wat gebeurt er nadat een groeier koopt\n")
    add("Instap 2 s na hun aankoop met 0,2 SOL. 'Volgen' = verkopen 2 s nadat zij de helft verkochten (anders na 60 min). "
        "'Videoregel' = uit bij -3% onder instap of +45% winst, max 60 min. Alleen aankopen waarvan het uur erna voorbij is.\n")
    for label, s in rep["vooruit_toets"].items():
        if not s.get("n"): add(f"- {label}: nog geen aankopen"); continue
        add(f"**{label}** — {s['n']} aankopen\n")
        add("| maatstaf | gemiddeld | mediaan | aandeel positief |"); add("|---|---|---|---|")
        for k in ("koers_+1m", "koers_+5m", "koers_+15m", "koers_+60m", "max_binnen_15m", "kopie_volgen", "kopie_videoregel"):
            v = s.get(k)
            if v: add(f"| {k} | {v['gem']:+.1%} | {v['mediaan']:+.1%} | {v['aandeel_plus']:.0%} |")
        add("")
    if rep.get("vooruit_per_wallet"):
        add("**Per groeier (alleen aankopen na opname)**\n")
        add("| wallet | aankopen | koers +15m | max binnen 15m | kopie volgen | kopie videoregel | kopie volgen plus |"); add("|---|---|---|---|---|---|---|")
        for r in rep["vooruit_per_wallet"]:
            add(f"| {link(r['wallet'])} | {r['n']} | {r['koers_+15m']:+.1%} | {r['max_binnen_15m']:+.1%} | {r['kopie_volgen']:+.1%} | {r['kopie_videoregel']:+.1%} | {pct(r['aandeel_kopie_volgen_plus'])} |")
        add("")
    add("## Beperkingen\n")
    for b in rep["beperkingen"]: add(f"- {b}")
    return "\n".join(L) + "\n"


def pct(x): return "–" if x is None else f"{x:.0%}"
def link(w): return f"[{w[:4]}…{w[-4:]}](https://solscan.io/account/{w})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=C.DB_PATH)
    ap.add_argument("--ledger", default=os.path.join(os.path.dirname(C.DB_PATH) or ".", "ledger.sqlite"))
    ap.add_argument("--out", default=C.REPORT_DIR)
    ap.add_argument("--now", type=float, default=None, help="alleen voor tests")
    ap.add_argument("--volg", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "volg_wallets.txt"))
    args = ap.parse_args()
    now = args.now or time.time(); t0 = time.time()
    main_db = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True, timeout=60)
    start = meta_get(main_db, "full_trade_log_since")
    os.makedirs(args.out, exist_ok=True)
    if not start:
        log("volledige logging nog niet actief; niets te doen")
        with open(os.path.join(args.out, "ledger.md"), "w") as f: f.write("# Geldstroom per wallet\n\nVolledige trade-logging is nog niet actief.\n")
        return
    starts = meta_get(main_db, "bot_starts", [])
    led = sqlite3.connect(args.ledger, timeout=60); led.executescript(SCHEMA)
    max_rowid = main_db.execute("SELECT MAX(rowid) FROM trades").fetchone()[0] or 0
    toks = load_tokens(main_db, start, starts)
    log(f"{len(toks)} tokens sinds start volledige logging, waarvan {sum(1 for v in toks.values() if v[5])} met een gat door herstart")
    n_rows, n_used = ingest(main_db, led, toks, max_rowid)
    log(f"ingelezen: {n_rows} nieuwe trades, {n_used} bruikbaar ({time.time()-t0:.0f}s)")

    mf = money_flow(led, now)
    top_netto = list(wallet_stats(led, now, order="ORDER BY si - so DESC", limit=25).items())

    # handmatig gevolgde wallets eerst, zodat ze altijd als 'handmatig' geregistreerd staan
    manual = load_manual(args.volg)
    for w, note in manual.items():
        led.execute("""INSERT INTO watch VALUES(?,?,?,?) ON CONFLICT(wallet) DO UPDATE SET versie = excluded.versie, stats = excluded.stats""",
                    (w, now, MANUAL, json.dumps({"notitie": note})))
    led.commit()

    # groeiers
    cands = wallet_stats(led, now, having=f"HAVING nfin >= {CRITERIA['min_tokens_afgerond']} AND si > so")
    evals = []
    for w, s in cands.items():
        g = growth(led, w); ok = qualifies(s, g); evals.append((w, s, g, ok))
        if ok and not led.execute("SELECT 1 FROM watch WHERE wallet = ?", (w,)).fetchone():
            led.execute("INSERT INTO watch VALUES(?,?,?,?)", (w, now, CRITERIA_VERSIE, json.dumps({**s, **g})))
    led.commit()
    watch = {w: (added, versie, st) for w, added, versie, st in led.execute("SELECT wallet, added_ts, versie, stats FROM watch")}
    wstats = wallet_stats(led, now, list(watch)) if watch else {}
    groeiers, handmatig = [], []
    for w, (added, versie, st) in watch.items():
        s = wstats.get(w)
        if versie == MANUAL:
            note = (json.loads(st or "{}") or {}).get("notitie", "")
            if not s:
                handmatig.append({"wallet": w, "notitie": note, "op_lijst_sinds": iso(added), "tokens": 0}); continue
            g = growth(led, w)
            led.execute("INSERT OR REPLACE INTO watch_snap VALUES(?,?,?,?,?)", (w, now, s["netto"], s["afgerond"], s["winkans"]))
            handmatig.append({"wallet": w, "notitie": note, "op_lijst_sinds": iso(added), **s, **g, "trend": trend(led, w),
                              "voldoet_aan_groeiers_criteria": qualifies(s, g)})
            continue
        if not s: continue
        g = growth(led, w)
        led.execute("INSERT OR REPLACE INTO watch_snap VALUES(?,?,?,?,?)", (w, now, s["netto"], s["afgerond"], s["winkans"]))
        groeiers.append({"wallet": w, "op_lijst_sinds": iso(added), **s, **g, "voldoet_nu": qualifies(s, g)})
    led.commit()
    groeiers.sort(key=lambda r: -r["netto"])

    def fails(s, g):
        c = CRITERIA; f = []
        if (s["winkans"] or 0) < c["min_winkans_tokens"]: f.append("winkans")
        if g["drawdown_van_piek"] is None or g["drawdown_van_piek"] > c["max_drawdown_van_piek"]: f.append("drawdown")
        if g["actieve_6u_blokken"] < c["min_actieve_6u_blokken"]: f.append("te kort actief")
        elif (g["aandeel_positieve_6u_blokken"] or 0) < c["min_aandeel_positieve_6u_blokken"]: f.append("niet elk blok plus")
        if s["dev_aandeel"] > c["max_dev_aandeel"]: f.append("dev")
        if s["bundel_aandeel"] > c["max_bundel_aandeel"]: f.append("bundel")
        return ", ".join(f)
    bijna = [dict(wallet=w, **s, **g, faalt_op=fails(s, g)) for w, s, g, ok in evals if not ok]
    bijna.sort(key=lambda r: (-(r["winkans"] or 0), -r["netto"])); bijna = bijna[:15]

    n_sig = run_signals(main_db, led, now) if watch else 0
    if n_sig: log(f"{n_sig} aankopen van gevolgde wallets geëvalueerd")

    rpc = RpcHttp(C.RPC_HTTP, HERKOMST_RPS) if (C.HELIUS_API_KEY or os.getenv("RPC_HTTP")) else None
    try:
        gp = big_players(led, now, rpc)
    except Exception as e:
        log(f"grote spelers mislukt: {e}"); gp = {"n_groot": 0, "fout": str(e)[:200]}
    try:
        if rpc is not None:
            n_h = run_herkomst(main_db, led, now, rpc); log(f"herkomst: {n_h} posities gekoppeld")
    except Exception as e:
        log(f"herkomst mislukt: {e}")
    herk = herkomst_report(led)

    span = led.execute("""SELECT MIN(w.first_ts), MAX(w.last_ts), COUNT(DISTINCT w.wallet), COUNT(*) FROM wt w
        JOIN token t ON t.mint = w.mint WHERE t.gap = 0 AND t.created_ts IS NOT NULL""").fetchone()
    rep = {
        "gegenereerd": iso(now), "criteria_versie": CRITERIA_VERSIE, "criteria": CRITERIA,
        "dekking": {"sinds": iso(span[0] or start), "uren": round(((span[1] or now) - (span[0] or start)) / 3600, 1),
                    "tokens": sum(1 for v in toks.values() if not v[5]),
                    "wallets": span[2], "posities": span[3], "herstarts_sinds_start": sum(1 for x in starts if x > start + 60),
                    "tokens_met_gat": sum(1 for v in toks.values() if v[5])},
        "geldstroom": mf,
        "top_netto": [dict(wallet=w, **s) for w, s in top_netto],
        "groeiers": groeiers, "bijna": bijna, "handmatig": handmatig, "herkomst": herk, "grote_spelers": gp,
        "vooruit_toets": signal_summary(led), "vooruit_toets_handmatig": signal_summary(led, handmatig=True),
        "vooruit_per_wallet": signal_per_wallet(led),
        "beperkingen": [
            "Alleen handel op de pump.fun-curve. Na migratie naar PumpSwap zien we niets meer; posities in gemigreerde tokens staan apart.",
            "Trades worden tot 6 uur na creatie gelogd. Wie later verkoopt, lijkt verlies te hebben op dat token.",
            "Tokens waarbij de bot binnen 2 uur na creatie herstartte, worden overgeslagen. Late verkopen (na een herstart later dan 2 uur) kunnen ontbreken.",
            "Creator-fees die pump.fun aan devs uitbetaalt en eventuele terminal-, prioriteits- en Jito-kosten zijn niet zichtbaar.",
            "Eén partij kan veel wallets gebruiken (bundels sturen tokens door naar andere wallets). Die groep lijkt dan klein per wallet maar is samen groot.",
            "Groeiers-criteria zijn vooraf vastgelegd. Een wallet die er achteraf op past, is pas bewezen als de vooruit-toets positief uitvalt.",
        ],
        "looptijd_s": round(time.time() - t0),
    }
    with open(os.path.join(args.out, "ledger.json"), "w") as f: json.dump(rep, f, indent=1)
    with open(os.path.join(args.out, "ledger.md"), "w") as f: f.write(to_md(rep))
    log(f"klaar in {rep['looptijd_s']}s -> {args.out}/ledger.md")


if __name__ == "__main__":
    main()
