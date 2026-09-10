"""Stap A (final-stretch-filters) en stap B (de vier token-checks) uit het bouwplan."""
import asyncio, time, logging, statistics, aiohttp
import config as C
from curve import mcap_sol

log = logging.getLogger("screen")
IPFS_GATEWAYS = ["https://ipfs.io/ipfs/", "https://cloudflare-ipfs.com/ipfs/", "https://gateway.pinata.cloud/ipfs/"]

async def fetch_metadata(uri: str, session: aiohttp.ClientSession) -> dict:
    urls = [uri]
    if "/ipfs/" in uri:
        cid = uri.split("/ipfs/")[-1]; urls = [g + cid for g in IPFS_GATEWAYS] + [uri]
    for u in urls:
        try:
            async with session.get(u, timeout=aiohttp.ClientTimeout(total=8)) as r:
                if r.status == 200: return await r.json(content_type=None)
        except Exception: continue
    return {}

def x_link_present(meta: dict) -> int:
    blob = " ".join(str(v) for v in meta.values()).lower() if meta else ""
    return int(("x.com/" in blob) or ("twitter.com/" in blob))

async def rugcheck(mint: str, session: aiohttp.ClientSession) -> dict:
    if not C.RUGCHECK_ENABLED: return {}
    try:
        async with session.get(f"https://api.rugcheck.xyz/v1/tokens/{mint}/report", timeout=aiohttp.ClientTimeout(total=12)) as r:
            if r.status != 200: return {"http": r.status}
            j = await r.json(content_type=None)
    except Exception as e:
        return {"error": str(e)[:80]}
    out = {"score": j.get("score_normalised", j.get("score")), "risks": [x.get("name") for x in (j.get("risks") or [])][:10]}
    try:
        nets = j.get("insiderNetworks") or []
        out["insider_pct"] = round(100 * sum(n.get("tokenAmount", 0) for n in nets) / C.TOTAL_SUPPLY_RAW, 2)
    except Exception: pass
    out["mint_authority"] = j.get("mintAuthority"); out["freeze_authority"] = j.get("freezeAuthority")
    return out

async def screen_token(ts, rpc, sol_usd: float, session: aiohttp.ClientSession) -> dict:
    """Voert alle checks uit. Geeft dict met deelresultaten en 'pass'."""
    t0 = time.time(); res = {"ts": t0, "age_min": round(ts.age_s(t0) / 60, 1)}
    mcap_usd = mcap_sol(ts.v_sol, ts.v_tok) * (sol_usd or 0); res["mcap_usd"] = round(mcap_usd)

    # --- check 1a/1b: top-5 houders ---
    largest = await rpc.largest_token_accounts(ts.mint)
    accts = [a["address"] for a in largest[:20]]
    owners = await rpc.token_account_owners(accts) if accts else {}
    top = []
    for a in largest[:20]:
        o = owners.get(a["address"])
        if o and o != ts.bonding_curve and o not in [t[0] for t in top]:
            top.append((o, int(a["amount"])))
        if len(top) == 5: break
    owner_list = [o for o, _ in top]
    balances = await rpc.sol_balances(owner_list) if owner_list else {}
    bals = [balances.get(o, 0.0) for o in owner_list]
    similar = 0
    if bals:
        med = statistics.median(bals)
        similar = sum(1 for b in bals if med > 0 and abs(b - med) / med <= C.HOLDER_BAL_SIMILAR_PCT / 100 and b < C.HOLDER_BAL_SMALL_SOL)
    res["top5"] = [{"owner": o, "pct": round(100 * amt / C.TOTAL_SUPPLY_RAW, 2), "sol": round(balances.get(o, 0.0), 3)} for o, amt in top]
    res["check1a_flag"] = similar >= C.HOLDER_BAL_SIMILAR_MIN_COUNT

    fund = await asyncio.gather(*[rpc.first_funding_time(o) for o in owner_list]) if owner_list else []
    for i, f in enumerate(fund): res["top5"][i]["funded"] = f
    times = sorted(f for f in fund if f)
    cluster = 0
    for i, a in enumerate(times):
        n = sum(1 for b in times if 0 <= b - a <= C.FUNDING_WINDOW_H * 3600); cluster = max(cluster, n)
    res["check1b_flag"] = cluster >= C.FUNDING_CLUSTER_MIN_COUNT

    # --- check 2: bundle-chartpatroon ---
    res["check2"] = ts.bundle_pattern(); res["check2_flag"] = res["check2"]["flag"]

    # --- final-stretch-filters ---
    dev_raw = await rpc.token_balance_of_owner(ts.creator, ts.mint) if ts.creator else 0
    res["dev_pct"] = round(100 * dev_raw / C.TOTAL_SUPPLY_RAW, 2)
    res["insider_pct_sameslot"] = round(100 * ts.same_slot_buy_tokens / C.TOTAL_SUPPLY_RAW, 2)
    buyers = list(ts.buyers_sol)[:100]
    bb = await rpc.sol_balances(buyers) if buyers else {}
    res["unique_buyers"] = len(ts.buyers_sol)
    res["pro_traders"] = sum(1 for b in bb.values() if b >= C.PRO_TRADER_MIN_SOL)

    # --- extra: metadata (X-link) en RugCheck ---
    meta = await fetch_metadata(ts.uri, session) if ts.uri else {}
    res["has_x_link"] = x_link_present(meta)
    res["rugcheck"] = await rugcheck(ts.mint, session)
    insider_pct = max(res["insider_pct_sameslot"], res["rugcheck"].get("insider_pct", 0) or 0)
    res["insider_pct"] = insider_pct

    res["fs_rules_pass"] = (res["dev_pct"] <= C.FS_MAX_DEV_PCT and insider_pct <= C.FS_MAX_INSIDER_PCT
                            and res["pro_traders"] >= C.FS_MIN_PRO_TRADERS and res["age_min"] <= C.FS_MAX_AGE_MIN)
    res["checks_pass"] = not (res["check1a_flag"] or res["check1b_flag"] or res["check2_flag"])
    res["pass"] = bool(res["fs_rules_pass"] and res["checks_pass"])
    res["duration_s"] = round(time.time() - t0, 1)
    return res
