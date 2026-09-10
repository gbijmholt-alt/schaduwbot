"""Stap C/D/E: instapsignaal op dip-vanaf-ATH, uitstapvarianten, fills met vertraging,
exacte curve-slippage en kosten. Alles virtueel; er wordt niets gestuurd."""
import json, time, logging
from dataclasses import dataclass, field
import config as C
import curve

log = logging.getLogger("sim")
VARIANTS = ["V1", "V2", "V3"]

@dataclass
class Position:
    variant: str; entry_signal_ts: float; entry_ts: float; entry_price: float
    tokens: dict                     # (size, terminal) -> tokens_raw
    entry_cost: dict                 # (size, terminal) -> kosten in SOL
    peak: float
    exit_signal_ts: float = 0.0; exit_reason: str = ""

@dataclass
class DipSim:
    dip: float
    phase: str = "waiting"           # waiting -> dipped -> pending_entry -> open -> done
    low: float = 0.0; low_ts: float = 0.0
    signal_ts: float = 0.0; signal_price: float = 0.0
    positions: dict = field(default_factory=dict)
    done: bool = False

class Simulator:
    def __init__(self, store, funnel):
        self.store = store; self.funnel = funnel

    def ensure(self, ts):
        if not ts.sims:
            for d in C.DIP_VARIANTS: ts.sims[d] = DipSim(dip=d)

    # ---------- per trade-event ----------
    def on_trade(self, ts, ev, pre, now):
        """pre = (v_sol, v_tok) vóór deze trade: de prijs die onze order zou krijgen."""
        self.ensure(ts)
        p = ts.last_price
        for sim in ts.sims.values():
            if sim.done: continue
            if sim.phase == "waiting":
                if ts.ath >= ts.launch_price * C.ATH_MIN_MULT and p <= ts.ath * (1 - sim.dip):
                    sim.phase = "dipped"; sim.low, sim.low_ts = p, now
            elif sim.phase == "dipped":
                if p >= ts.ath:                      # nieuwe top zonder instap: opnieuw wachten
                    sim.phase = "waiting"; continue
                if p < sim.low: sim.low, sim.low_ts = p, now
                rebound = p >= sim.low * (1 + C.REBOUND_PCT) or (ev.is_buy and ev.sol_amount / 1e9 >= C.REBOUND_BUY_SOL and now > sim.low_ts)
                if rebound and not ts.migrated:
                    sim.phase = "pending_entry"; sim.signal_ts, sim.signal_price = now, p
                    self.funnel(f"signal_{sim.dip:.2f}")
            elif sim.phase == "pending_entry":
                if now >= sim.signal_ts + C.FILL_DELAY_S: self._fill_entry(ts, sim, pre, now)
            elif sim.phase == "open":
                self._check_exits(ts, sim, p, now, pre, ev)

    def _fill_entry(self, ts, sim, pre, now):
        v_sol, v_tok = pre; entry_price = curve.price_sol(v_sol, v_tok)
        tokens, costs = {}, {}
        for size in C.SIZES_SOL:
            for term in C.FEE_TERMINAL:
                tok, cost = curve.buy(v_sol, v_tok, size, term); tokens[(size, term)] = tok; costs[(size, term)] = cost
        for v in VARIANTS:
            sim.positions[v] = Position(v, sim.signal_ts, now, entry_price, tokens, costs, entry_price)
        sim.phase = "open"; self.funnel("entry")

    def _check_exits(self, ts, sim, p, now, pre, ev):
        for v, pos in list(sim.positions.items()):
            if pos.exit_signal_ts:
                if now >= pos.exit_signal_ts + C.FILL_DELAY_S: self._fill_exit(ts, sim, pos, pre, now)
                continue
            if p > pos.peak: pos.peak = p
            ret = p / pos.entry_price - 1
            reason = None
            if ts.rug_ts and ts.rug_ts >= pos.entry_ts: reason = "rug"
            elif v == "V1":
                if ret <= -C.V1_STOP_MARGIN: reason = "stop"
                elif ret >= C.V1_TP: reason = "tp"
            elif v == "V2":
                if ret <= -C.V2_STOP: reason = "stop"
                elif p <= pos.peak * (1 - C.V2_TRAIL) and pos.peak > pos.entry_price: reason = "trail"
            elif v == "V3":
                if ret <= -C.V3_STOP: reason = "stop"
                elif now - pos.entry_ts >= C.V3_TIME_S: reason = "time"
            if now - pos.entry_ts >= C.MAX_HOLD_S: reason = reason or "maxhold"
            if reason: pos.exit_signal_ts, pos.exit_reason = now, reason
        if not sim.positions: sim.done = True

    def _fill_exit(self, ts, sim, pos, pre, now):
        v_sol, v_tok = pre; exit_price = curve.price_sol(v_sol, v_tok)
        pnl = {}
        for (size, term), tok in pos.tokens.items():
            sol_out, cost = curve.sell(v_sol, v_tok, tok, term)
            net = sol_out - size - C.PRIO_FEE_SOL      # koopfee zit al in size; prio van de koop apart; verkoopfees zitten in sol_out
            pnl[f"{size}_{term}"] = round(net / size, 4)
        gross = exit_price / pos.entry_price - 1
        is_rug = int(pos.exit_reason == "rug" or gross <= -0.6)
        self.store.add_sim_trade(mint=ts.mint, dip=sim.dip, variant=pos.variant, screen_pass=ts.screen_pass,
            signal_ts=pos.entry_signal_ts, entry_ts=pos.entry_ts, entry_price=pos.entry_price, exit_ts=now,
            exit_price=exit_price, exit_reason=pos.exit_reason, is_rug=is_rug, hold_s=round(now - pos.entry_ts, 1),
            pnl_json=json.dumps(pnl), gross_ret=round(gross, 4))
        self.funnel("exit"); del sim.positions[pos.variant]
        if not sim.positions: sim.done = True

    # ---------- periodiek (elke seconde) ----------
    def tick(self, ts, now):
        """Tijdsexits, en fills als er geen trade meer binnenkomt (dan geldt de huidige curveprijs)."""
        if not ts.sims: return
        pre = (ts.v_sol, ts.v_tok)
        for sim in ts.sims.values():
            if sim.done: continue
            if sim.phase == "pending_entry" and now >= sim.signal_ts + C.FILL_DELAY_S + 10:
                self._fill_entry(ts, sim, pre, now)
            elif sim.phase == "open":
                for pos in list(sim.positions.values()):
                    if pos.exit_signal_ts:
                        if now >= pos.exit_signal_ts + C.FILL_DELAY_S + 10: self._fill_exit(ts, sim, pos, pre, now)
                    else:
                        if pos.variant == "V3" and now - pos.entry_ts >= C.V3_TIME_S: pos.exit_signal_ts, pos.exit_reason = now, "time"
                        elif now - pos.entry_ts >= C.MAX_HOLD_S: pos.exit_signal_ts, pos.exit_reason = now, "maxhold"

    def on_migration(self, ts, now):
        pre = (ts.v_sol, ts.v_tok)
        for sim in ts.sims.values():
            if sim.done: continue
            if sim.phase == "open":
                for pos in list(sim.positions.values()):
                    pos.exit_reason = pos.exit_reason or "migration"; self._fill_exit(ts, sim, pos, pre, now)
            sim.done = True
