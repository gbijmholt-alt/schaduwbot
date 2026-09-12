"""SQLite-opslag. Alles wat nodig is om varianten achteraf te herberekenen."""
import sqlite3, json, os, time, threading

SCHEMA = """
CREATE TABLE IF NOT EXISTS tokens (
  mint TEXT PRIMARY KEY, name TEXT, symbol TEXT, uri TEXT, creator TEXT, bonding_curve TEXT,
  created_ts REAL, create_slot INTEGER, launch_price REAL, has_x_link INTEGER,
  first_seen_ts REAL, migrated_ts REAL, last_price REAL, ath_price REAL, ath_ts REAL,
  filter_newpairs_ts REAL, filter_fs_ts REAL, screened_ts REAL, screen_pass INTEGER, screen_json TEXT
);
CREATE TABLE IF NOT EXISTS trades (
  mint TEXT, ts REAL, slot INTEGER, sig TEXT, user TEXT, is_buy INTEGER, sol REAL, tokens INTEGER,
  v_sol INTEGER, v_tok INTEGER, r_tok INTEGER, price REAL
);
CREATE INDEX IF NOT EXISTS trades_mint_ts ON trades(mint, ts);
CREATE TABLE IF NOT EXISTS sim_trades (
  id INTEGER PRIMARY KEY AUTOINCREMENT, mint TEXT, dip REAL, variant TEXT, screen_pass INTEGER,
  signal_ts REAL, entry_ts REAL, entry_price REAL, exit_ts REAL, exit_price REAL, exit_reason TEXT,
  is_rug INTEGER, hold_s REAL, pnl_json TEXT, gross_ret REAL
);
CREATE TABLE IF NOT EXISTS amm_trades (
  mint TEXT, ts REAL, slot INTEGER, sig TEXT, user TEXT, is_buy INTEGER, sol REAL, tokens INTEGER
);
CREATE INDEX IF NOT EXISTS amm_mint_ts ON amm_trades(mint, ts);
CREATE TABLE IF NOT EXISTS funnel (day TEXT, stage TEXT, n INTEGER, PRIMARY KEY(day, stage));
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v TEXT);
"""

class Store:
    def __init__(self, path):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.execute("PRAGMA journal_mode=WAL"); self.db.execute("PRAGMA synchronous=NORMAL")
        self.db.executescript(SCHEMA); self.lock = threading.Lock()
        self._trade_buf = []; self._last_flush = time.time()
        self._amm_buf = []

    def upsert_token(self, **kw):
        cols = ",".join(kw); ph = ",".join("?" * len(kw))
        upd = ",".join(f"{k}=excluded.{k}" for k in kw if k != "mint")
        with self.lock:
            self.db.execute(f"INSERT INTO tokens({cols}) VALUES({ph}) ON CONFLICT(mint) DO UPDATE SET {upd}", list(kw.values()))

    def add_trade(self, row):
        self._trade_buf.append(row)
        if len(self._trade_buf) >= 200 or time.time() - self._last_flush > 5: self.flush()

    def add_amm_trade(self, row):
        self._amm_buf.append(row)
        if len(self._amm_buf) >= 200: self.flush()

    def flush(self):
        if not self._trade_buf and not self._amm_buf: return
        with self.lock:
            if self._trade_buf: self.db.executemany("INSERT INTO trades VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", self._trade_buf)
            if self._amm_buf: self.db.executemany("INSERT INTO amm_trades VALUES(?,?,?,?,?,?,?,?)", self._amm_buf)
            self.db.commit()
        self._trade_buf = []; self._amm_buf = []; self._last_flush = time.time()
        self._amm_buf = []

    def add_sim_trade(self, **kw):
        cols = ",".join(kw); ph = ",".join("?" * len(kw))
        with self.lock:
            self.db.execute(f"INSERT INTO sim_trades({cols}) VALUES({ph})", list(kw.values())); self.db.commit()

    def bump_funnel(self, stage, day=None):
        day = day or time.strftime("%Y-%m-%d", time.gmtime())
        with self.lock:
            self.db.execute("INSERT INTO funnel(day,stage,n) VALUES(?,?,1) ON CONFLICT(day,stage) DO UPDATE SET n=n+1", (day, stage))

    def set_meta(self, k, v):
        with self.lock:
            self.db.execute("INSERT INTO meta(k,v) VALUES(?,?) ON CONFLICT(k) DO UPDATE SET v=excluded.v", (k, json.dumps(v))); self.db.commit()

    def commit(self):
        with self.lock: self.db.commit()

    def query(self, sql, args=()):
        with self.lock:
            cur = self.db.execute(sql, args); cols = [c[0] for c in cur.description]
            return [dict(zip(cols, r)) for r in cur.fetchall()]
