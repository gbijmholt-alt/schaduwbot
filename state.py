"""In-memory toestand per token (alleen tokens waarvan we de CreateEvent zagen)."""
import time
from collections import deque
from dataclasses import dataclass, field
from . import config as C
from .curve import price_sol

@dataclass
class TokenState:
    mint: str; name: str = ""; symbol: str = ""; uri: str = ""; creator: str = ""; bonding_curve: str = ""
    created_ts: float = 0.0; create_slot: int = 0
    v_sol: int = 30_000_000_000; v_tok: int = 1_073_000_000_000_000; r_tok: int = C.INITIAL_REAL_TOKEN_RESERVES
    launch_price: float = 0.0; last_price: float = 0.0; last_ts: float = 0.0
    ath: float = 0.0; ath_ts: float = 0.0
    migrated: bool = False; migrated_ts: float = 0.0
    n_trades: int = 0
    buyers_sol: dict = field(default_factory=dict)        # user -> totaal gekochte SOL (cap)
    creator_net_tokens: int = 0
    same_slot_buy_tokens: int = 0                          # kopen in het creatie-slot, niet door creator
    early_buy_tokens: int = 0                              # kopen binnen BUNDLE_WINDOW_S
    first60_sells: int = 0; first60_max_price: float = 0.0
    price_window: deque = field(default_factory=lambda: deque(maxlen=400))   # (ts, price) voor rug-detectie
    rug_ts: float = 0.0
    newpairs_ts: float = 0.0; fs_ts: float = 0.0
    screening_started: bool = False; screened_ts: float = 0.0; screen_pass: int = None; screen_result: dict = None
    has_x_link: int = None
    sims: dict = field(default_factory=dict)              # dip -> DipSim

    def __post_init__(self):
        self.launch_price = price_sol(self.v_sol, self.v_tok); self.last_price = self.launch_price
        self.ath = self.launch_price

    def age_s(self, now=None): return (now or time.time()) - self.created_ts

    def apply_trade(self, ev, slot: int, now: float):
        """Werk reserves en statistieken bij. Geeft (pre_v_sol, pre_v_tok) terug: de prijs die een
        order die net vóór deze trade landde zou hebben gekregen."""
        pre = (self.v_sol, self.v_tok)
        self.v_sol, self.v_tok, self.r_tok = ev.v_sol, ev.v_tok, ev.r_tok
        p = price_sol(self.v_sol, self.v_tok); self.last_price = p; self.last_ts = now; self.n_trades += 1
        if p > self.ath: self.ath, self.ath_ts = p, now
        age = self.age_s(now)
        if ev.is_buy:
            if len(self.buyers_sol) < 500 or ev.user in self.buyers_sol:
                self.buyers_sol[ev.user] = self.buyers_sol.get(ev.user, 0.0) + ev.sol_amount / 1e9
            if ev.user == self.creator: self.creator_net_tokens += ev.token_amount
            else:
                if slot == self.create_slot: self.same_slot_buy_tokens += ev.token_amount
                if age <= C.BUNDLE_WINDOW_S: self.early_buy_tokens += ev.token_amount
        else:
            if ev.user == self.creator: self.creator_net_tokens -= ev.token_amount
            if age <= 60: self.first60_sells += 1
        if age <= 60 and p > self.first60_max_price: self.first60_max_price = p
        # rug-detectie: prijs <= (1-RUG_DROP) x prijs van <= RUG_WINDOW_S geleden
        self.price_window.append((now, p))
        if not self.rug_ts:
            for ts, old in self.price_window:
                if now - ts <= C.RUG_WINDOW_S and old > 0 and p <= old * (1 - C.RUG_DROP_PCT):
                    self.rug_ts = now; break
        return pre

    def bundle_pattern(self) -> dict:
        """Check 2 uit de video: 'één grote groene candle' vanaf launch."""
        early_pct = 100 * self.early_buy_tokens / C.TOTAL_SUPPLY_RAW
        first60_mult = (self.first60_max_price / self.launch_price) if self.launch_price else 0
        flag = early_pct >= C.BUNDLE_SUPPLY_PCT or (first60_mult >= C.BUNDLE_FIRST60_MULT and self.first60_sells < C.BUNDLE_FIRST60_MIN_SELLS)
        return {"early_buy_pct": round(early_pct, 2), "first60_mult": round(first60_mult, 2), "first60_sells": self.first60_sells, "flag": bool(flag)}
