# Schaduwbot status

- tijd: 2026-09-11 08:57:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 19 hours, 10 minutes
- bot-service: active
- code-versie: 3e65967
- schijf: 2.3G/38G | geheugen: 530/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 601, "tokens_in_memory": 146, "msgs": 26070, "trades": 7120, "creates": 147, "decode_fail": 700, "rpc_calls": 258, "rpc_errors": 12, "sol_usd": 99.90542424895735, "open_positions": 25, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 08:47 UTC

Gelogde schaduwtrades: **20217**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 9843 | 1366 | 18 | 1366 | 99 | 2655 | 7862 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 241 | 15% | 1.7% | +40.4% | -16.5% | -7.74% | 98% |
| dip35_V1_gescreend_fail | 2021 | 26% | 4.0% | +46.0% | -26.4% | -7.46% | 100% |
| dip35_V1_alle | 2338 | 25% | 4.1% | +44.7% | -25.7% | -7.82% | 100% |
| dip35_V2_gescreend_pass | 242 | 18% | 2.1% | +39.3% | -21.1% | -10.35% | 100% |
| dip35_V2_gescreend_fail | 2029 | 24% | 4.6% | +55.0% | -28.7% | -8.72% | 100% |
| dip35_V2_alle | 2326 | 23% | 4.7% | +53.1% | -28.2% | -9.33% | 100% |
| dip35_V3_gescreend_pass | 242 | 7% | 2.5% | +141.2% | -23.1% | -12.22% | 100% |
| dip35_V3_gescreend_fail | 2057 | 13% | 6.5% | +111.6% | -30.4% | -12.26% | 100% |
| dip35_V3_alle | 2349 | 12% | 6.3% | +110.0% | -29.9% | -12.70% | 100% |
| dip40_V1_gescreend_pass | 223 | 13% | 1.8% | +42.7% | -15.9% | -8.26% | 98% |
| dip40_V1_gescreend_fail | 1966 | 26% | 3.9% | +47.9% | -26.3% | -6.87% | 100% |
| dip40_V1_alle | 2246 | 25% | 3.9% | +46.9% | -25.5% | -7.27% | 100% |
| dip40_V2_gescreend_pass | 224 | 13% | 1.8% | +49.8% | -19.8% | -10.50% | 100% |
| dip40_V2_gescreend_fail | 1967 | 24% | 4.3% | +55.9% | -28.5% | -7.90% | 100% |
| dip40_V2_alle | 2231 | 23% | 4.3% | +55.1% | -27.8% | -8.60% | 100% |
| dip40_V3_gescreend_pass | 224 | 6% | 2.2% | +116.7% | -21.7% | -13.64% | 100% |
| dip40_V3_gescreend_fail | 1995 | 13% | 6.1% | +103.3% | -30.2% | -13.11% | 100% |
| dip40_V3_alle | 2255 | 12% | 5.9% | +102.1% | -29.5% | -13.59% | 100% |
| dip45_V1_gescreend_pass | 212 | 15% | 1.9% | +50.6% | -15.7% | -6.02% | 96% |
| dip45_V1_gescreend_fail | 1909 | 28% | 3.4% | +49.9% | -25.9% | -5.06% | 100% |
| dip45_V1_alle | 2162 | 26% | 3.5% | +49.5% | -25.0% | -5.42% | 100% |
| dip45_V2_gescreend_pass | 212 | 19% | 2.4% | +50.3% | -19.5% | -6.37% | 97% |
| dip45_V2_gescreend_fail | 1902 | 25% | 3.8% | +59.8% | -27.9% | -5.97% | 100% |
| dip45_V2_alle | 2145 | 24% | 3.9% | +58.7% | -27.3% | -6.42% | 100% |
| dip45_V3_gescreend_pass | 212 | 7% | 2.8% | +186.5% | -20.9% | -6.20% | 99% |
| dip45_V3_gescreend_fail | 1926 | 14% | 5.9% | +111.7% | -29.6% | -10.29% | 100% |
| dip45_V3_alle | 2165 | 13% | 5.8% | +114.2% | -28.9% | -10.27% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1636 | 12% | 2.6% | -10.04% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 08:37:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:54,863 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:37:54 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 08:37:57 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:57,253 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:37:57 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,355 main INFO screen $USD pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,803 main INFO screen wind pass=0 dev=1.44 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,911 main INFO screen FYC pass=0 dev=0.0 ins=16.28 pro=52 1a=False 1b=False 2=True (8.5s)
Sep 11 08:39:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:58,237 main INFO screen PC pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (3.9s)
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,305 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,398 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,599 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,298 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,440 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:41:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:39,691 main INFO screen Lucy pass=1 dev=0.0 ins=10.58 pro=48 1a=False 1b=False 2=False (3.3s)
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,335 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,526 main INFO screen happen pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,238 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,299 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,515 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 08:42:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:30,532 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:42:30 +0000] "GET /health HTTP/1.1" 200 420 "-" "Python-urllib/3.14"
Sep 11 08:42:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:42,143 main INFO screen ch pass=0 dev=9.25 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 11 08:43:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:11,505 main INFO screen power pass=0 dev=0.34 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 08:43:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:19,405 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:43:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:19,560 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:43:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:19,720 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:43:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:32,836 main INFO screen SCRVAN pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 08:43:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:43,633 main INFO screen $RAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 11 08:43:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:52,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:43:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:52,614 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:43:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:43:52,729 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 08:44:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:20,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:44:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:20,459 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:44:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:20,681 main INFO screen KALSHE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:44:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:30,207 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:44:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:30,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:44:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:30,506 main INFO screen NIKE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 08:44:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:44:36,884 main INFO screen Lucky pass=0 dev=0.0 ins=11.57 pro=63 1a=False 1b=False 2=True (3.6s)
Sep 11 08:45:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:45:21,830 main INFO screen GOD  pass=0 dev=1.4 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 08:46:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:46:54,214 main INFO screen DOOB pass=0 dev=0.33 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 08:47:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:47:37,611 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 08:47:38 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 08:47:38 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 08:47:38 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 08:47:38 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 4min 49.569s CPU time over 1h 8min 42.095s wall clock time, 143.8M memory peak.
Sep 11 08:47:38 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 08:47:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:47:39,360 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 08:47:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:47:39,370 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:47:39 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 11 08:48:29 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:48:29,397 main INFO screen Félicette pass=0 dev=0.0 ins=17.93 pro=34 1a=False 1b=False 2=True (6.6s)
Sep 11 08:48:29 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:48:29,426 main INFO screen OSAMA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.4s)
Sep 11 08:48:32 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:48:32,241 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 08:49:17 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:17,176 main INFO screen 401k pass=0 dev=0.0 ins=24.48 pro=37 1a=False 1b=False 2=True (3.8s)
Sep 11 08:49:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:42,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:49:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:42,522 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:49:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:42,698 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 11 08:49:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:43,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:49:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:43,253 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:49:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:49:43,375 main INFO screen PUMPCAT pass=0 dev=0.0 ins=75.89 pro=5 1a=False 1b=False 2=True (0.3s)
Sep 11 08:50:52 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:50:52,193 main INFO screen wind pass=0 dev=0.57 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 08:51:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:51:04,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:51:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:51:04,664 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:51:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:51:04,825 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 08:51:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:51:41,315 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 08:52:32 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:52:32,150 main INFO screen power pass=0 dev=0.4 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 11 08:52:37 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:52:37,205 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:52:37 +0000] "GET /health HTTP/1.1" 200 434 "-" "Python-urllib/3.14"
Sep 11 08:52:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:52:46,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:52:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:52:46,403 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:52:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:52:47,422 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (1.2s)
Sep 11 08:53:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:53:47,015 main INFO screen ASTRUID pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 08:53:52 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:53:52,537 main INFO screen SAVPIR pass=0 dev=3.23 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 08:54:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:54:42,333 main INFO screen $GOAT10 pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 08:55:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:55:42,524 main INFO screen $GOAT10 pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 08:56:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:04,606 main INFO screen 🚀 pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 08:56:29 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:29,779 main INFO screen OTC pass=0 dev=0.0 ins=18.41 pro=36 1a=False 1b=False 2=True (2.2s)
Sep 11 08:56:38 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:38,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:56:38 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:38,833 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:56:38 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:38,953 main INFO screen $GOAT10 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 08:56:57 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:57,645 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:56:57 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:57,742 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:56:57 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:56:57,961 main INFO screen ZTRADE pass=0 dev=0.0 ins=79.26 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 08:57:40 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 08:57:40,561 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:57:40 +0000] "GET /health HTTP/1.1" 200 437 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
install klaar
--- update 2026-09-11T07:43:57Z
--- update 2026-09-11T07:48:58Z
--- update 2026-09-11T07:53:58Z
--- update 2026-09-11T07:59:05Z
--- update 2026-09-11T08:04:36Z
--- update 2026-09-11T08:09:59Z
--- update 2026-09-11T08:15:36Z
--- update 2026-09-11T08:20:55Z
--- update 2026-09-11T08:26:04Z
--- update 2026-09-11T08:31:36Z
--- update 2026-09-11T08:36:38Z
--- update 2026-09-11T08:42:29Z
--- update 2026-09-11T08:47:35Z
nieuwe code: 3e65967
install klaar
--- update 2026-09-11T08:52:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 277361cb46e7428ca1de36d4214ea43b
wallet-analyse gestart (e04fe8bd5728)
--- update 2026-09-11T08:57:39Z
```

## Wallet-analyse (laatste 15 regels)
```
inactive
08:52:36 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 08:52 UTC
08:52:36 24905 tokens geladen
08:52:43   2000 tokens, 587636 trades, 196383 posities (6s)
08:52:47 posities: 352960 uit 1045578 trades (11s)
08:52:52 79415 wallets gerekend
08:52:53 geluk-toets
08:53:06 persistentie
08:53:07 kopieer-simulatie
08:53:11 klaar in 34s -> /opt/schaduwbot/reports/wallets.md
```

## Bootstrap-log (laatste 60 regels)
```
Unpacking libcurl4t64:amd64 (8.18.0-1ubuntu2.5) over (8.18.0-1ubuntu2.4)…
Preparing to unpack …/08-libcurl3t64-gnutls_8.18.0-1ubuntu2.5_amd64.deb…
Unpacking libcurl3t64-gnutls:amd64 (8.18.0-1ubuntu2.5) over (8.18.0-1ubuntu2.4)…
Selecting previously unselected package python3-wheel.
Preparing to unpack …/09-python3-wheel_0.46.3-2_all.deb…
Unpacking python3-wheel (0.46.3-2)…
Selecting previously unselected package python3-pip.
Preparing to unpack …/10-python3-pip_25.1.1+dfsg-1ubuntu2_all.deb…
Unpacking python3-pip (25.1.1+dfsg-1ubuntu2)…
Selecting previously unselected package python3-pip-whl.
Preparing to unpack …/11-python3-pip-whl_25.1.1+dfsg-1ubuntu2_all.deb…
Unpacking python3-pip-whl (25.1.1+dfsg-1ubuntu2)…
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack …/12-python3-setuptools-whl_78.1.1-0.1build1_all.deb…
Unpacking python3-setuptools-whl (78.1.1-0.1build1)…
Selecting previously unselected package python3.14-venv.
Preparing to unpack …/13-python3.14-venv_3.14.4-1ubuntu0.2_amd64.deb…
Unpacking python3.14-venv (3.14.4-1ubuntu0.2)…
Selecting previously unselected package python3-venv.
Preparing to unpack …/14-python3-venv_3.14.3-0ubuntu2_amd64.deb…
Unpacking python3-venv (3.14.3-0ubuntu2)…
Setting up python3-setuptools-whl (78.1.1-0.1build1)…
Setting up libcurl4t64:amd64 (8.18.0-1ubuntu2.5)…
Setting up python3-pip-whl (25.1.1+dfsg-1ubuntu2)…
Setting up libpython3.14-minimal:amd64 (3.14.4-1ubuntu0.2)…
Setting up libcurl3t64-gnutls:amd64 (8.18.0-1ubuntu2.5)…
Setting up python3-wheel (0.46.3-2)…
Setting up python3.14-gdbm (3.14.4-1ubuntu0.2)…
Setting up python3-pip (25.1.1+dfsg-1ubuntu2)…
Setting up curl (8.18.0-1ubuntu2.5)…
Setting up python3.14-minimal (3.14.4-1ubuntu0.2)…
Setting up libpython3.14-stdlib:amd64 (3.14.4-1ubuntu0.2)…
Setting up libpython3.14:amd64 (3.14.4-1ubuntu0.2)…
Setting up python3.14 (3.14.4-1ubuntu0.2)…
Setting up python3.14-venv (3.14.4-1ubuntu0.2)…
Setting up python3-venv (3.14.3-0ubuntu2)…
Processing triggers for systemd (259.5-0ubuntu3.4)…
Processing triggers for man-db (2.13.1-1build1)…
Processing triggers for libc-bin (2.43-2ubuntu2.3)…

Running kernel seems to be up-to-date.

Restarting services...
 systemctl restart packagekit.service

Service restarts being deferred:
 systemctl restart cloud-init-main.service
 systemctl restart networkd-dispatcher.service
 systemctl restart unattended-upgrades.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
Created symlink '/etc/systemd/system/multi-user.target.wants/schaduwbot.service' → '/etc/systemd/system/schaduwbot.service'.
install klaar
status.md -> 200 
report.json -> 201 
===== bootstrap klaar 2026-09-10T13:48:49Z =====
```

## cloud-init (laatste 25 regels)
```
|.BoBoB.          |
|  o.. +E         |
| .   .. S .      |
|.    . o =       |
| .  . + + .      |
| .+o . . o       |
| .**.            |
+----[SHA256]-----+
Generating public/private ed25519 key pair.
Your identification has been saved in /etc/ssh/ssh_host_ed25519_key
Your public key has been saved in /etc/ssh/ssh_host_ed25519_key.pub
The key fingerprint is:
SHA256:w2XLkdz/wp4oYdhzAWpZtAWfv0pFj8xAggp36PYfUQQ root@ubuntu-4gb-fsn1-1
The key's randomart image is:
+--[ED25519 256]--+
|       . oE++    |
|    . o o.oO..   |
|     + o +Bo= .  |
|      +.++.o.B o |
|     . oSoo. .B .|
|        o.* .o o |
|         o =. + .|
|          o. + o |
|           .o o  |
+----[SHA256]-----+
```
