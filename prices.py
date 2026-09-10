"""SOL/USD-koers, elke 60 s ververst. Jupiter eerst, CoinGecko als fallback."""
import asyncio, time, logging, aiohttp
log = logging.getLogger("prices")
SOL_MINT = "So11111111111111111111111111111111111111112"

class SolPrice:
    def __init__(self): self.usd = None; self.ts = 0
    async def run(self):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as s:
            while True:
                try:
                    async with s.get(f"https://lite-api.jup.ag/price/v3?ids={SOL_MINT}") as r:
                        j = await r.json(); self.usd = float(j[SOL_MINT]["usdPrice"]); self.ts = time.time()
                except Exception as e:
                    try:
                        async with s.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd") as r:
                            j = await r.json(); self.usd = float(j["solana"]["usd"]); self.ts = time.time()
                    except Exception as e2:
                        log.warning("SOL-koers niet opgehaald: %s / %s", e, e2)
                await asyncio.sleep(60)
