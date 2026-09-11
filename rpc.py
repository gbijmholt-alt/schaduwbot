"""Async JSON-RPC-client met rate-limiter (Helius free: 10 req/s)."""
import asyncio, time, logging
import aiohttp
import config as C

log = logging.getLogger("rpc")

class RateLimiter:
    def __init__(self, rps: float):
        self.interval = 1.0 / rps; self.next = 0.0; self.lock = asyncio.Lock()
    async def wait(self):
        async with self.lock:
            now = time.monotonic()
            if now < self.next: await asyncio.sleep(self.next - now)
            self.next = max(now, self.next) + self.interval

class Rpc:
    def __init__(self, url=C.RPC_HTTP, rps=C.RPC_RPS):
        self.url = url; self.rl = RateLimiter(rps); self.session = None; self._id = 0
        self.calls = 0; self.errors = 0
    async def start(self):
        self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=20))
    async def close(self):
        if self.session: await self.session.close()
    async def call(self, method, params, retries=3):
        for attempt in range(retries):
            await self.rl.wait(); self._id += 1; self.calls += 1
            try:
                async with self.session.post(self.url, json={"jsonrpc": "2.0", "id": self._id, "method": method, "params": params}) as r:
                    if r.status == 429:
                        await asyncio.sleep(1.5 * (attempt + 1)); continue
                    j = await r.json()
                    if "error" in j:
                        self.errors += 1; log.warning("rpc %s error %s", method, j["error"]); return None
                    return j.get("result")
            except Exception as e:
                self.errors += 1; log.warning("rpc %s exc %s", method, e); await asyncio.sleep(0.5)
        return None

    async def largest_token_accounts(self, mint):
        res = await self.call("getTokenLargestAccounts", [mint, {"commitment": "confirmed"}])
        return (res or {}).get("value", [])   # [{address, amount, decimals, uiAmount}]

    async def multiple_accounts(self, pubkeys, parsed=True):
        out = []
        for i in range(0, len(pubkeys), 100):
            chunk = pubkeys[i:i+100]
            enc = {"encoding": "jsonParsed"} if parsed else {"encoding": "base64"}
            res = await self.call("getMultipleAccounts", [chunk, {"commitment": "confirmed", **enc}])
            vals = (res or {}).get("value") or [None] * len(chunk)
            out.extend(vals)
        return out

    async def sol_balances(self, owners):
        accs = await self.multiple_accounts(owners, parsed=False)
        return {o: ((a or {}).get("lamports", 0) / 1e9) for o, a in zip(owners, accs)}

    async def token_account_owners(self, token_accounts):
        accs = await self.multiple_accounts(token_accounts, parsed=True)
        owners = {}
        for ta, a in zip(token_accounts, accs):
            try: owners[ta] = a["data"]["parsed"]["info"]["owner"]
            except Exception: owners[ta] = None
        return owners

    async def first_funding_time(self, wallet, max_pages=C.FUNDING_MAX_PAGES):
        """Blocktime van de oudste transactie van een wallet. None = ouder dan max_pages*1000 tx."""
        before = None; oldest = None
        for _ in range(max_pages):
            params = [wallet, {"limit": 1000, "commitment": "confirmed", **({"before": before} if before else {})}]
            res = await self.call("getSignaturesForAddress", params)
            if not res: break
            oldest = res[-1]; before = oldest["signature"]
            if len(res) < 1000: return oldest.get("blockTime")
        return None   # cap bereikt: oude, actieve wallet

    async def token_balance_of_owner(self, owner, mint):
        res = await self.call("getTokenAccountsByOwner", [owner, {"mint": mint}, {"encoding": "jsonParsed", "commitment": "confirmed"}])
        if res is None: return None          # RPC-fout: onbekend, niet 'nul'
        total = 0
        for v in (res or {}).get("value", []):
            try: total += int(v["account"]["data"]["parsed"]["info"]["tokenAmount"]["amount"])
            except Exception: pass
        return total
