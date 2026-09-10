"""Bonding-curve rekenwerk (constant product op virtuele reserves) en kosten."""
from . import config as C

LAMPORTS = 1_000_000_000

def price_sol(v_sol: int, v_tok: int) -> float:
    """Prijs in SOL per token (1 token = 10^6 raw)."""
    if v_tok <= 0: return 0.0
    return (v_sol / LAMPORTS) / (v_tok / 10**C.TOKEN_DECIMALS)

def mcap_sol(v_sol: int, v_tok: int) -> float:
    return price_sol(v_sol, v_tok) * (C.TOTAL_SUPPLY_RAW / 10**C.TOKEN_DECIMALS)

def progress(r_tok: int) -> float:
    return max(0.0, min(1.0, 1 - r_tok / C.INITIAL_REAL_TOKEN_RESERVES))

def buy(v_sol: int, v_tok: int, sol_in: float, terminal: str):
    """Simuleer een koop van sol_in SOL. Geeft (tokens_raw, kosten_sol)."""
    fee_pct = C.FEE_PUMP + C.FEE_TERMINAL[terminal]
    sol_net = sol_in * (1 - fee_pct)
    lam = int(sol_net * LAMPORTS)
    tok_out = v_tok - (v_sol * v_tok) // (v_sol + lam)
    cost = sol_in * fee_pct + C.PRIO_FEE_SOL
    return tok_out, cost

def sell(v_sol: int, v_tok: int, tok_in: int, terminal: str):
    """Simuleer verkoop van tok_in raw tokens. Geeft (sol_netto, kosten_sol)."""
    fee_pct = C.FEE_PUMP + C.FEE_TERMINAL[terminal]
    lam_out = v_sol - (v_sol * v_tok) // (v_tok + tok_in)
    gross = lam_out / LAMPORTS
    cost = gross * fee_pct + C.PRIO_FEE_SOL
    return gross - cost, cost
