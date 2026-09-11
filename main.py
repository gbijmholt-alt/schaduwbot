"""Orchestrator: websocket-stream -> decoder -> toestand -> filters -> screening -> simulatie -> opslag.
Gebruik:  python main.py run      (24/7)
          python main.py probe    (60 s meeluisteren, decoder valideren)
          python main.py report   (rapport uit de database)"""
import asyncio, json, logging, shutil, sys, time, os
import aiohttp, websockets
import config as C
from decoder import decode_logs, TradeEvent, CreateEvent, CompleteEvent
from state import TokenState
from store import Store
from rpc import Rpc
from prices import SolPrice
from screening import screen_token
from simulator import Simulator
from health import Health
from curve import mcap_sol, progress
import report as report_mod

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"), format="%(asctime)s %(name)s %(levelname)s %(message)s")
log = logging.getLogger("main")

class Bot:
    def __init__(self):
        self.store = Store(C.DB_PATH); self.rpc = Rpc(); self.price = SolPrice()
        self.health = Health(C.HEALTH_PORT); self.sim = Simulator(self.store, self.store.bump_funnel)
        self.tokens: dict[str, TokenState] = {}; self.session = None
        self.n_msgs = 0; self.n_trades = 0; self.n_creates = 0; self.n_decode_fail = 0
        self.screen_sem = asyncio.Semaphore(3)
        self.log_all = C.LOG_ALL_TRADES; self.last_disk_check = 0.0

    # ---------- events ----------
    def on_create(self, ev: CreateEvent, slot, now):
        ts = TokenState(mint=ev.mint, name=ev.name[:64], symbol=ev.symbol[:16], uri=ev.uri[:300], creator=ev.creator or ev.user,
                        bonding_curve=ev.bonding_curve, created_ts=now, create_slot=slot)
        if ev.v_sol and ev.v_tok: ts.v_sol, ts.v_tok = ev.v_sol, ev.v_tok; ts.__post_init__()
        self.tokens[ev.mint] = ts; self.n_creates += 1; self.store.bump_funnel("created")
        self.store.upsert_token(mint=ts.mint, name=ts.name, symbol=ts.symbol, uri=ts.uri, creator=ts.creator, bonding_curve=ts.bonding_curve,
                                created_ts=now, create_slot=slot, launch_price=ts.launch_price, first_seen_ts=now)

    def on_trade(self, ev: TradeEvent, slot, sig, now):
        ts = self.tokens.get(ev.mint)
        if ts is None or ts.migrated: return
        pre = ts.apply_trade(ev, slot, now); self.n_trades += 1
        if ev.creator and not ts.creator: ts.creator = ev.creator
        tracked = bool(ts.newpairs_ts or ts.fs_ts) and not ts.sim_closed
        if not tracked and not ts.sim_closed: tracked = self._check_filters(ts, now)
        if tracked or self.log_all or ts.newpairs_ts or ts.fs_ts:     # alle trades bewaren voor de wallet-analyse (zolang er schijfruimte is)
            self.store.add_trade((ts.mint, now, slot, sig, ev.user, int(ev.is_buy), ev.sol_amount / 1e9, ev.token_amount, ev.v_sol, ev.v_tok, ev.r_tok, ts.last_price))
        if tracked:
            self.sim.on_trade(ts, ev, pre, now)

    def on_complete(self, ev: CompleteEvent, now):
        ts = self.tokens.get(ev.mint)
        if ts is None: return
        ts.migrated, ts.migrated_ts = True, now
        self.sim.on_migration(ts, now); self.store.upsert_token(mint=ts.mint, migrated_ts=now)

    def _check_filters(self, ts, now) -> bool:
        usd = self.price.usd
        if not usd: return False
        mcap = mcap_sol(ts.v_sol, ts.v_tok) * usd
        hit = False
        if not ts.newpairs_ts and mcap >= C.NEWPAIRS_MIN_MCAP_USD:
            ts.newpairs_ts = now; self.store.bump_funnel("newpairs"); hit = True
        if not ts.fs_ts and progress(ts.r_tok) >= C.FS_MIN_PROGRESS and C.FS_MIN_MCAP_USD <= mcap <= C.FS_MAX_MCAP_USD and ts.age_s(now) <= C.FS_MAX_AGE_MIN * 60:
            ts.fs_ts = now; self.store.bump_funnel("final_stretch"); hit = True
        if hit:
            self.store.upsert_token(mint=ts.mint, filter_newpairs_ts=ts.newpairs_ts or None, filter_fs_ts=ts.fs_ts or None)
            if not ts.screening_started:
                ts.screening_started = True; asyncio.create_task(self._screen(ts))
        return hit

    async def _screen(self, ts):
        async with self.screen_sem:
            try:
                res = await screen_token(ts, self.rpc, self.price.usd, self.session)
            except Exception as e:
                log.exception("screening %s mislukt: %s", ts.symbol, e); res = {"error": str(e)[:200], "pass": False}
        ts.screened_ts = time.time(); ts.screen_pass = int(bool(res.get("pass"))); ts.screen_result = res; ts.has_x_link = res.get("has_x_link")
        self.store.bump_funnel("screened")
        if ts.screen_pass: self.store.bump_funnel("screen_pass")
        self.store.upsert_token(mint=ts.mint, screened_ts=ts.screened_ts, screen_pass=ts.screen_pass, screen_json=json.dumps(res, default=str), has_x_link=ts.has_x_link)
        log.info("screen %s pass=%s dev=%s ins=%s pro=%s 1a=%s 1b=%s 2=%s (%ss)", ts.symbol, ts.screen_pass, res.get("dev_pct"), res.get("insider_pct"),
                 res.get("pro_traders"), res.get("check1a_flag"), res.get("check1b_flag"), res.get("check2_flag"), res.get("duration_s"))

    # ---------- stream ----------
    async def stream(self, probe_seconds=None):
        backoff = 1; t_end = time.time() + probe_seconds if probe_seconds else None
        while True:
            try:
                async with websockets.connect(C.RPC_WS, max_size=None, ping_interval=20, open_timeout=20) as ws:
                    await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                              "params": [{"mentions": [C.PUMP_PROGRAM]}, {"commitment": "processed"}]}))
                    log.info("verbonden met %s", C.RPC_WS.split("?")[0]); backoff = 1
                    async for raw in ws:
                        if t_end and time.time() > t_end: return
                        msg = json.loads(raw)
                        if "params" not in msg: continue
                        val = msg["params"]["result"]["value"]; slot = msg["params"]["result"]["context"]["slot"]
                        self.n_msgs += 1; now = time.time(); self.health.last_event = now
                        if val.get("err"): continue
                        evs = decode_logs(val["logs"])
                        if not evs and any(l.startswith("Program data:") for l in val["logs"]): self.n_decode_fail += 1
                        for ev in evs:
                            if isinstance(ev, CreateEvent): self.on_create(ev, slot, now)
                            elif isinstance(ev, TradeEvent): self.on_trade(ev, slot, val["signature"], now)
                            elif isinstance(ev, CompleteEvent): self.on_complete(ev, now)
            except Exception as e:
                log.warning("stream verbroken: %s — opnieuw over %ss", e, backoff)
                await asyncio.sleep(backoff); backoff = min(backoff * 2, 60)

    # ---------- onderhoud ----------
    async def ticker(self):
        last_report = 0; last_day = None
        while True:
            await asyncio.sleep(1); now = time.time()
            for ts in list(self.tokens.values()):
                if ts.sims: self.sim.tick(ts, now)
                age = ts.age_s(now)
                # Na TRACK_MAX_AGE_S doet een token niet meer mee aan de simulatie (zoals voorheen), maar we blijven
                # zijn trades loggen tot LOG_MAX_AGE_S, zodat verkopen na het eerste uur zichtbaar zijn voor de wallet-analyse.
                if not ts.sim_closed and age > C.TRACK_MAX_AGE_S and all(s.done or s.phase in ("waiting", "dipped") for s in ts.sims.values()):
                    ts.sim_closed = True
                    for s in ts.sims.values(): s.done = True
                    if ts.newpairs_ts or ts.fs_ts:
                        self.store.upsert_token(mint=ts.mint, last_price=ts.last_price, ath_price=ts.ath, ath_ts=ts.ath_ts)
                if ts.sim_closed and (age > C.LOG_MAX_AGE_S or not self.log_all):
                    del self.tokens[ts.mint]
            self.store.flush()
            if now - self.last_disk_check > 60:
                self.last_disk_check = now
                free_gb = shutil.disk_usage(os.path.dirname(os.path.abspath(C.DB_PATH))).free / 1e9
                want = C.LOG_ALL_TRADES and free_gb > C.MIN_FREE_DISK_GB
                if want != self.log_all:
                    log.warning("volledige trade-logging %s (vrije schijf %.1f GB)", "aan" if want else "UIT", free_gb); self.log_all = want
            self.health.stats = {"tokens_in_memory": len(self.tokens), "msgs": self.n_msgs, "trades": self.n_trades, "creates": self.n_creates,
                                 "decode_fail": self.n_decode_fail, "rpc_calls": self.rpc.calls, "rpc_errors": self.rpc.errors, "sol_usd": self.price.usd,
                                 "open_positions": sum(len(s.positions) for t in self.tokens.values() for s in t.sims.values()),
                                 "log_all_trades": self.log_all}
            if now - last_report > 3600:
                last_report = now
                try: report_mod.write(self.store); self.store.set_meta("last_report", now)
                except Exception as e: log.exception("rapport mislukt: %s", e)

    async def run(self):
        if self.log_all and not self.store.query("SELECT v FROM meta WHERE k = 'full_trade_log_since'"):
            self.store.set_meta("full_trade_log_since", time.time())
        # vanaf deze versie: houdercheck met herhaalpoging, terugval op de tradestroom en fail-closed
        if not self.store.query("SELECT v FROM meta WHERE k = 'screening_v2_since'"):
            self.store.set_meta("screening_v2_since", time.time())
        # starttijden bijhouden: tokens die een herstart overleven hebben een gat in hun trades
        prev = self.store.query("SELECT v FROM meta WHERE k = 'bot_starts'")
        starts = json.loads(prev[0]["v"]) if prev else []
        self.store.set_meta("bot_starts", (starts + [time.time()])[-500:])
        await self.rpc.start(); self.session = aiohttp.ClientSession()
        await self.health.start()
        await asyncio.gather(self.price.run(), self.stream(), self.ticker())

    async def probe(self, seconds=60):
        await self.rpc.start(); self.session = aiohttp.ClientSession()
        asyncio.create_task(self.price.run())
        await self.stream(probe_seconds=seconds)
        self.store.flush()
        print(json.dumps({"msgs": self.n_msgs, "creates": self.n_creates, "trades": self.n_trades, "decode_fail": self.n_decode_fail,
                          "sol_usd": self.price.usd, "tokens": len(self.tokens)}, indent=1))
        for ts in list(self.tokens.values())[:5]:
            print(f"  {ts.symbol:10s} trades={ts.n_trades:4d} launch={ts.launch_price:.3e} last={ts.last_price:.3e} ath×={ts.ath/ts.launch_price:.2f} mcapSOL={mcap_sol(ts.v_sol, ts.v_tok):.1f} prog={progress(ts.r_tok):.2f}")
        await self.rpc.close(); await self.session.close()

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    bot = Bot()
    if cmd == "run": asyncio.run(bot.run())
    elif cmd == "probe": asyncio.run(bot.probe(int(sys.argv[2]) if len(sys.argv) > 2 else 60))
    elif cmd == "report":
        rep = report_mod.write(bot.store); print(report_mod.to_markdown(rep))
    else: print(__doc__)

if __name__ == "__main__": main()
