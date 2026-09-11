"""Alle instelbare parameters. Waarden komen uit omgevingsvariabelen (.env) met de
defaults uit het bouwplan (Fase1_Schaduwbot_Bouwplan.docx, §2)."""
import os

def _f(name, default): return float(os.getenv(name, default))
def _i(name, default): return int(os.getenv(name, default))

PUMP_PROGRAM = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
TOKEN_DECIMALS = 6
TOTAL_SUPPLY_RAW = 1_000_000_000 * 10**TOKEN_DECIMALS
INITIAL_REAL_TOKEN_RESERVES = 793_100_000 * 10**TOKEN_DECIMALS   # curve is "vol" als dit 0 is

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY", "")
RPC_HTTP = os.getenv("RPC_HTTP") or (f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}" if HELIUS_API_KEY else "https://api.mainnet-beta.solana.com")
RPC_WS = os.getenv("RPC_WS") or (f"wss://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}" if HELIUS_API_KEY else "wss://api.mainnet-beta.solana.com")
RPC_RPS = _f("RPC_RPS", 8)            # Helius free = 10 req/s; marge houden
DB_PATH = os.getenv("DB_PATH", "data/schaduwbot.sqlite")
REPORT_DIR = os.getenv("REPORT_DIR", "reports")
HEALTH_PORT = _i("HEALTH_PORT", 8080)
RUGCHECK_ENABLED = os.getenv("RUGCHECK_ENABLED", "1") == "1"
LOG_ALL_TRADES = os.getenv("LOG_ALL_TRADES", "1") == "1"     # ook trades onder $7k bewaren (wallet-analyse)
MIN_FREE_DISK_GB = _f("MIN_FREE_DISK_GB", 5)                 # daaronder alleen nog trades van gevolgde tokens

# --- Stap A: filters ---
NEWPAIRS_MIN_MCAP_USD = _f("NEWPAIRS_MIN_MCAP_USD", 7000)
FS_MIN_PROGRESS = _f("FS_MIN_PROGRESS", 0.70)          # "final stretch" benadering
FS_MAX_AGE_MIN = _f("FS_MAX_AGE_MIN", 40)
FS_MAX_DEV_PCT = _f("FS_MAX_DEV_PCT", 5)
FS_MAX_INSIDER_PCT = _f("FS_MAX_INSIDER_PCT", 20)
FS_MIN_PRO_TRADERS = _i("FS_MIN_PRO_TRADERS", 10)       # proxy: unieke kopers met >= PRO_TRADER_MIN_SOL
PRO_TRADER_MIN_SOL = _f("PRO_TRADER_MIN_SOL", 1.0)
FS_MIN_MCAP_USD = _f("FS_MIN_MCAP_USD", 8000)
FS_MAX_MCAP_USD = _f("FS_MAX_MCAP_USD", 30000)          # "onderste 4 van final stretch"

# --- Stap B: token-checks ---
HOLDER_BAL_SIMILAR_PCT = _f("HOLDER_BAL_SIMILAR_PCT", 20)   # ±20%
HOLDER_BAL_SIMILAR_MIN_COUNT = _i("HOLDER_BAL_SIMILAR_MIN_COUNT", 4)
HOLDER_BAL_SMALL_SOL = _f("HOLDER_BAL_SMALL_SOL", 0.5)
FUNDING_WINDOW_H = _f("FUNDING_WINDOW_H", 2)
FUNDING_CLUSTER_MIN_COUNT = _i("FUNDING_CLUSTER_MIN_COUNT", 3)
FUNDING_MAX_PAGES = _i("FUNDING_MAX_PAGES", 5)             # >5000 tx = "oude wallet", niet vers
BUNDLE_WINDOW_S = _f("BUNDLE_WINDOW_S", 5)
BUNDLE_SUPPLY_PCT = _f("BUNDLE_SUPPLY_PCT", 30)
BUNDLE_FIRST60_MULT = _f("BUNDLE_FIRST60_MULT", 2.0)
BUNDLE_FIRST60_MIN_SELLS = _i("BUNDLE_FIRST60_MIN_SELLS", 3)

# --- Stap C/D: instap en uitstap ---
DIP_VARIANTS = [float(x) for x in os.getenv("DIP_VARIANTS", "0.35,0.40,0.45").split(",")]
ATH_MIN_MULT = _f("ATH_MIN_MULT", 2.0)                     # ATH >= 2x launchprijs
REBOUND_PCT = _f("REBOUND_PCT", 0.05)
REBOUND_BUY_SOL = _f("REBOUND_BUY_SOL", 0.5)
FILL_DELAY_S = _f("FILL_DELAY_S", 2.0)
V1_STOP_MARGIN = _f("V1_STOP_MARGIN", 0.03)
V1_TP = _f("V1_TP", 0.45)
V2_STOP = _f("V2_STOP", 0.10)
V2_TRAIL = _f("V2_TRAIL", 0.20)
V3_STOP = _f("V3_STOP", 0.10)
V3_TIME_S = _f("V3_TIME_S", 900)
MAX_HOLD_S = _f("MAX_HOLD_S", 3600)                        # noodrem: na 1 uur altijd sluiten
RUG_DROP_PCT = _f("RUG_DROP_PCT", 0.80)
RUG_WINDOW_S = _f("RUG_WINDOW_S", 1.0)

# --- Stap E: kosten ---
SIZES_SOL = [float(x) for x in os.getenv("SIZES_SOL", "0.05,0.2,1.0").split(",")]
FEE_PUMP = _f("FEE_PUMP", 0.0125)
FEE_TERMINAL = {"axiom": _f("FEE_AXIOM", 0.00855), "pp": _f("FEE_PP", 0.005)}
PRIO_FEE_SOL = _f("PRIO_FEE_SOL", 0.001)

TRACK_MAX_AGE_S = _f("TRACK_MAX_AGE_S", 3600)              # tokens ouder dan 1 uur uit geheugen
