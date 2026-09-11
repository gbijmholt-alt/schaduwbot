# Schaduwbot status

- tijd: 2026-09-11 07:33:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 17 hours, 46 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 543/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 1863, "tokens_in_memory": 559, "msgs": 166142, "trades": 36676, "creates": 559, "decode_fail": 1917, "rpc_calls": 726, "rpc_errors": 96, "sol_usd": 99.73439404548982, "open_positions": 26}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 07:02 UTC

Gelogde schaduwtrades: **18616**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 7750 | 1036 | 13 | 1036 | 88 | 2094 | 6261 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 232 | 15% | 1.7% | +41.5% | -16.4% | -7.63% | 98% |
| dip35_V1_gescreend_fail | 1851 | 27% | 3.8% | +45.9% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 2152 | 26% | 3.9% | +44.7% | -25.3% | -7.34% | 100% |
| dip35_V2_gescreend_pass | 233 | 17% | 2.1% | +41.5% | -21.0% | -10.30% | 100% |
| dip35_V2_gescreend_fail | 1864 | 24% | 4.5% | +54.8% | -28.4% | -7.98% | 100% |
| dip35_V2_alle | 2146 | 24% | 4.6% | +52.9% | -27.9% | -8.70% | 100% |
| dip35_V3_gescreend_pass | 233 | 7% | 2.6% | +141.2% | -23.1% | -11.83% | 100% |
| dip35_V3_gescreend_fail | 1877 | 13% | 6.3% | +113.7% | -30.2% | -11.73% | 100% |
| dip35_V3_alle | 2155 | 12% | 6.2% | +112.1% | -29.7% | -12.19% | 100% |
| dip40_V1_gescreend_pass | 216 | 12% | 1.9% | +43.7% | -15.9% | -8.42% | 98% |
| dip40_V1_gescreend_fail | 1804 | 26% | 3.7% | +47.9% | -25.9% | -6.37% | 100% |
| dip40_V1_alle | 2070 | 25% | 3.8% | +46.9% | -25.1% | -6.89% | 100% |
| dip40_V2_gescreend_pass | 217 | 13% | 1.8% | +48.9% | -19.8% | -10.95% | 100% |
| dip40_V2_gescreend_fail | 1813 | 25% | 4.1% | +55.4% | -28.1% | -7.26% | 100% |
| dip40_V2_alle | 2064 | 24% | 4.2% | +54.5% | -27.4% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 217 | 6% | 2.3% | +116.7% | -21.8% | -13.46% | 100% |
| dip40_V3_gescreend_fail | 1824 | 13% | 5.9% | +102.8% | -29.9% | -13.06% | 100% |
| dip40_V3_alle | 2072 | 12% | 5.7% | +102.0% | -29.2% | -13.52% | 100% |
| dip45_V1_gescreend_pass | 205 | 15% | 2.0% | +52.2% | -15.6% | -5.70% | 95% |
| dip45_V1_gescreend_fail | 1750 | 28% | 3.3% | +49.7% | -25.6% | -4.55% | 100% |
| dip45_V1_alle | 1989 | 27% | 3.3% | +49.5% | -24.7% | -4.96% | 100% |
| dip45_V2_gescreend_pass | 205 | 18% | 2.4% | +52.0% | -19.5% | -6.24% | 97% |
| dip45_V2_gescreend_fail | 1751 | 26% | 3.7% | +59.5% | -27.5% | -5.22% | 100% |
| dip45_V2_alle | 1981 | 25% | 3.8% | +58.6% | -26.9% | -5.69% | 100% |
| dip45_V3_gescreend_pass | 205 | 7% | 2.9% | +198.9% | -20.8% | -5.81% | 99% |
| dip45_V3_gescreend_fail | 1760 | 14% | 5.6% | +112.0% | -29.3% | -10.17% | 100% |
| dip45_V3_alle | 1987 | 13% | 5.5% | +115.5% | -28.6% | -10.08% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 11 07:19:40 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:19:40,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:19:40 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:19:40,762 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:19:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:19:47,710 main INFO screen THECAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.1s)
Sep 11 07:20:00 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:20:00,901 main INFO screen poki pass=0 dev=0.72 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 11 07:20:13 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:20:13,231 main INFO screen $AURA pass=0 dev=5.44 ins=0.0 pro=4 1a=False 1b=False 2=False (6.7s)
Sep 11 07:20:38 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:20:38,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:20:38 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:20:38,612 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:20:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:20:45,508 main INFO screen CLAPATHON pass=0 dev=0.0 ins=49.49 pro=16 1a=False 1b=False 2=True (7.1s)
Sep 11 07:21:22 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:22,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:21:22 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:22,465 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:21:27 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:27,756 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.5s)
Sep 11 07:21:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:46,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:21:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:46,423 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:21:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:21:46,772 main INFO screen NASDOG pass=0 dev=0.0 ins=6.65 pro=36 1a=False 1b=False 2=True (0.5s)
Sep 11 07:22:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:22:10,856 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:22:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:22:10,944 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:22:17 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:22:17,207 main INFO screen Casinu pass=0 dev=0.0 ins=49.65 pro=19 1a=False 1b=False 2=True (6.5s)
Sep 11 07:22:20 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:22:20,364 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 07:22:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:22:45,511 main INFO screen RISE pass=0 dev=36.92 ins=0.0 pro=10 1a=False 1b=False 2=True (8.4s)
Sep 11 07:23:15 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:15,058 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:23:15 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:15,115 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:23:16 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:16,327 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:23:16 +0000] "GET /health HTTP/1.1" 200 417 "-" "Python-urllib/3.14"
Sep 11 07:23:19 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:19,093 main INFO screen faucat pass=0 dev=0.0 ins=49.04 pro=18 1a=False 1b=False 2=True (4.1s)
Sep 11 07:23:53 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:53,850 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:23:53 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:53,942 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:23:54 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:23:54,140 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:24:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:24:41,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:24:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:24:41,224 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:24:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:24:41,463 main INFO screen ASD pass=0 dev=0.0 ins=0.28 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 11 07:25:11 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:11,986 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 11 07:25:23 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:23,598 main INFO screen Invictus pass=0 dev=13.0 ins=5.82 pro=12 1a=False 1b=False 2=False (7.1s)
Sep 11 07:25:30 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:30,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:25:30 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:30,721 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:25:30 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:30,908 main INFO screen ASD pass=0 dev=0.0 ins=0.28 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 11 07:25:34 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:34,245 main INFO screen whale pass=0 dev=0.72 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 11 07:25:49 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:25:49,820 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.4s)
Sep 11 07:26:11 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:26:11,144 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 11 07:26:32 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:26:32,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:26:32 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:26:32,928 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:26:33 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:26:33,115 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:27:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:27:28,076 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:07:27:28 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 07:27:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:27:28,423 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:07:27:28 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 07:28:22 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:22,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:28:22 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:22,832 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:28:26 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:26,820 main INFO screen retail pass=0 dev=0.0 ins=15.22 pro=58 1a=False 1b=False 2=True (9.2s)
Sep 11 07:28:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:28,756 main INFO screen Kirkmas pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.1s)
Sep 11 07:28:37 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:37,136 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:28:37 +0000] "GET /health HTTP/1.1" 200 417 "-" "Python-urllib/3.14"
Sep 11 07:28:42 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:42,123 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:28:42 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:42,214 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:28:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:28:45,755 main INFO screen NIVI pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 11 07:29:26 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:26,517 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:29:26 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:26,611 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:29:32 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:32,185 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.8s)
Sep 11 07:29:39 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:39,480 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:29:39 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:39,606 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:29:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:41,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:29:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:41,554 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:29:42 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:42,928 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:29:43 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:43,055 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:29:43 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:43,345 main INFO screen period  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 11 07:29:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:47,144 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.8s)
Sep 11 07:29:48 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:29:48,227 main INFO screen computer pass=0 dev=0.0 ins=0.02 pro=1 1a=False 1b=False 2=True (5.4s)
Sep 11 07:30:02 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:02,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:30:02 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:02,222 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:30:02 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:02,487 main INFO screen Unfazed pass=0 dev=0.0 ins=4.45 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 07:30:06 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:06,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:30:07 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:07,107 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:30:12 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:12,833 main INFO screen $GOBLIN99 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 07:30:15 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:30:15,251 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (6.3s)
Sep 11 07:31:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:31:28,533 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:31:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:31:28,628 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:31:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:31:28,959 main INFO screen BATTERM pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 11 07:32:04 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:04,986 aiohttp.access INFO 20.150.211.201 [11/Sep/2026:07:32:04 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 11 07:32:07 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:07,193 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:32:07 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:07,291 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:32:07 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:07,482 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:32:21 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:21,747 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:32:21 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:21,871 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:32:22 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:32:22,033 main INFO screen $CALI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 07:33:53 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:33:53,632 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:33:53 +0000] "GET /health HTTP/1.1" 200 417 "-" "Python-urllib/3.14"
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
