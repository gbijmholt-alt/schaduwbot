# Schaduwbot status

- tijd: 2026-09-11 13:37:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 23 hours, 50 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 672/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 13654, "tokens_in_memory": 3638, "msgs": 1180290, "trades": 316078, "creates": 3638, "decode_fail": 26552, "rpc_calls": 5579, "rpc_errors": 506, "sol_usd": 100.72677815988853, "open_positions": 85, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 12:49 UTC

Gelogde schaduwtrades: **22644**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 13510 | 1846 | 23 | 1846 | 119 | 3508 | 10289 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 255 | 15% | 1.6% | +41.0% | -16.1% | -7.57% | 99% |
| dip35_V1_gescreend_fail | 2281 | 26% | 3.8% | +46.1% | -26.0% | -6.93% | 100% |
| dip35_V1_alle | 2618 | 26% | 3.9% | +45.0% | -25.4% | -7.30% | 100% |
| dip35_V2_gescreend_pass | 253 | 18% | 2.0% | +39.4% | -21.0% | -10.24% | 100% |
| dip35_V2_gescreend_fail | 2285 | 24% | 4.4% | +56.4% | -28.4% | -7.63% | 100% |
| dip35_V2_alle | 2597 | 24% | 4.5% | +54.5% | -28.0% | -8.34% | 100% |
| dip35_V3_gescreend_pass | 256 | 7% | 2.3% | +137.5% | -22.7% | -12.07% | 100% |
| dip35_V3_gescreend_fail | 2324 | 13% | 6.2% | +114.1% | -30.1% | -10.97% | 100% |
| dip35_V3_alle | 2634 | 13% | 6.2% | +112.1% | -29.6% | -11.54% | 100% |
| dip40_V1_gescreend_pass | 235 | 14% | 1.7% | +43.1% | -15.6% | -7.58% | 98% |
| dip40_V1_gescreend_fail | 2221 | 26% | 3.7% | +47.9% | -26.0% | -6.51% | 100% |
| dip40_V1_alle | 2517 | 25% | 3.8% | +47.0% | -25.2% | -6.86% | 100% |
| dip40_V2_gescreend_pass | 233 | 14% | 2.1% | +49.8% | -20.1% | -10.46% | 100% |
| dip40_V2_gescreend_fail | 2217 | 25% | 4.1% | +56.2% | -28.2% | -7.25% | 100% |
| dip40_V2_alle | 2493 | 24% | 4.2% | +55.5% | -27.7% | -7.99% | 100% |
| dip40_V3_gescreend_pass | 236 | 6% | 2.5% | +114.0% | -21.7% | -13.69% | 100% |
| dip40_V3_gescreend_fail | 2257 | 13% | 5.8% | +102.3% | -29.8% | -12.45% | 100% |
| dip40_V3_alle | 2532 | 12% | 5.8% | +101.0% | -29.2% | -12.98% | 100% |
| dip45_V1_gescreend_pass | 224 | 14% | 1.8% | +50.1% | -15.5% | -6.14% | 97% |
| dip45_V1_gescreend_fail | 2158 | 28% | 3.3% | +49.4% | -25.6% | -4.84% | 100% |
| dip45_V1_alle | 2426 | 26% | 3.4% | +49.0% | -24.8% | -5.24% | 100% |
| dip45_V2_gescreend_pass | 221 | 19% | 2.3% | +49.7% | -19.7% | -6.80% | 98% |
| dip45_V2_gescreend_fail | 2143 | 26% | 3.7% | +59.1% | -27.7% | -5.52% | 100% |
| dip45_V2_alle | 2398 | 25% | 3.8% | +58.1% | -27.2% | -6.04% | 100% |
| dip45_V3_gescreend_pass | 224 | 7% | 2.7% | +186.5% | -20.9% | -7.01% | 99% |
| dip45_V3_gescreend_fail | 2175 | 14% | 5.7% | +109.0% | -29.3% | -10.01% | 100% |
| dip45_V3_alle | 2429 | 13% | 5.6% | +111.0% | -28.7% | -10.10% | 100% |

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
| met_xlink | 1732 | 12% | 2.6% | -9.97% | 100% |
| zonder_xlink | 405 | 14% | 0.0% | -5.52% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 13:24:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:24:53,932 main INFO screen IBM pass=0 dev=0.0 ins=9.87 pro=4 1a=False 1b=True 2=False (7.4s)
Sep 11 13:25:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:15,950 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:25:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:16,046 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:25:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:21,546 main INFO screen NEIL pass=0 dev=0.0 ins=50.85 pro=2 1a=False 1b=False 2=True (5.7s)
Sep 11 13:25:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:22,985 main INFO screen Unfazed pass=0 dev=0.0 ins=14.78 pro=31 1a=False 1b=False 2=True (6.9s)
Sep 11 13:25:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:49,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:25:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:49,530 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:25:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:53,230 main INFO screen 2001 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 13:25:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:53,384 main INFO screen 13602061 pass=0 dev=0.0 ins=52.02 pro=5 1a=False 1b=False 2=True (4.1s)
Sep 11 13:25:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:57,016 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:25:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:57,213 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:25:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:25:57,538 main INFO screen Handle pass=0 dev=0.0 ins=7.33 pro=5 1a=False 1b=False 2=True (0.6s)
Sep 11 13:26:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:08,953 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:26:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:09,077 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:26:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:13,549 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 11 13:26:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:15,053 main INFO screen S&P500 pass=1 dev=0.0 ins=19.89 pro=18 1a=False 1b=False 2=False (4.8s)
Sep 11 13:26:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:45,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:26:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:45,428 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:26:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:49,749 main INFO screen flyjak pass=0 dev=0.0 ins=77.53 pro=9 1a=False 1b=False 2=True (4.6s)
Sep 11 13:26:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:26:54,760 main INFO screen eeee pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 11 13:27:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:05,737 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:27:05 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 13:27:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:09,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:27:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:09,739 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:27:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:12,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:27:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:12,967 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:27:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:14,758 main INFO screen 2001 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.2s)
Sep 11 13:27:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:19,472 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 11 13:27:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:25,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:27:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:25,930 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:27:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:26,477 main INFO screen Riley pass=0 dev=0.0 ins=22.87 pro=8 1a=False 1b=False 2=True (0.7s)
Sep 11 13:27:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:27:50,056 main INFO screen fg pass=0 dev=0.08 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 11 13:28:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:28:47,834 main INFO screen Gorilla pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 13:29:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:05,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:29:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:05,862 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:29:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:09,895 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.1s)
Sep 11 13:29:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:11,856 main INFO screen FLIES pass=1 dev=0.0 ins=19.41 pro=23 1a=False 1b=False 2=False (7.6s)
Sep 11 13:29:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:36,618 main INFO screen TOAD pass=0 dev=4.39 ins=0.0 pro=2 1a=False 1b=False 2=False (6.0s)
Sep 11 13:29:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:42,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:29:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:42,489 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:29:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:29:42,723 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 11 13:30:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:30:00,774 main INFO screen STOCKLANA pass=0 dev=0.0 ins=24.97 pro=15 1a=False 1b=False 2=True (7.3s)
Sep 11 13:30:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:30:15,041 main INFO screen wPARADISE pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 13:30:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:30:33,459 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:30:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:30:33,560 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:30:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:30:39,878 main INFO screen GTAVI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 11 13:32:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:05,257 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:32:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:05,355 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:32:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:05,569 main INFO screen BLN pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 13:32:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:05,703 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:32:05 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 13:32:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:58,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:32:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:58,707 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:32:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:32:58,892 main INFO screen $NEVER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:33:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:33:23,877 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.6s)
Sep 11 13:33:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:33:25,088 main INFO screen stocklana pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 11 13:33:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:33:53,973 main INFO screen BOP pass=0 dev=0.53 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 13:34:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:34:23,996 main INFO screen ZWHALE pass=0 dev=1.05 ins=32.64 pro=4 1a=False 1b=True 2=True (1.3s)
Sep 11 13:34:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:34:41,760 main INFO screen HOGGO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 13:34:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:34:48,794 main INFO screen $GOAT pass=0 dev=1.93 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 13:35:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:01,045 main INFO screen eeee pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.1s)
Sep 11 13:35:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:48,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:35:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:48,242 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:35:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:48,516 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:35:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:54,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:35:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:54,852 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:35:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:35:54,992 main INFO screen Cody pass=0 dev=0.0 ins=21.62 pro=5 1a=False 1b=False 2=True (0.3s)
Sep 11 13:36:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:36:09,359 main INFO screen WOMEN pass=0 dev=0.44 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 13:36:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:36:36,282 main INFO screen catcook pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 13:36:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:36:59,029 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:36:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:36:59,122 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:36:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:36:59,305 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:37:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:03,514 main INFO screen TOAD pass=0 dev=0.57 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 13:37:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:05,928 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:37:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:06,555 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:37:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:06,931 main INFO screen S911 pass=0 dev=0.0 ins=78.9 pro=6 1a=False 1b=False 2=True (1.4s)
Sep 11 13:37:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:08,183 main INFO screen POTUSEXPOS pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 13:37:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:09,200 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 11 13:37:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:13,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:37:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:13,731 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:37:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:13,863 main INFO screen $STOCKLANA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 13:37:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:37:18,519 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:37:18 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (8213ec5e675e)
--- update 2026-09-11T12:05:15Z
--- update 2026-09-11T12:10:30Z
--- update 2026-09-11T12:15:36Z
--- update 2026-09-11T12:20:40Z
--- update 2026-09-11T12:26:02Z
--- update 2026-09-11T12:31:19Z
--- update 2026-09-11T12:36:32Z
--- update 2026-09-11T12:41:33Z
--- update 2026-09-11T12:46:36Z
--- update 2026-09-11T12:51:41Z
--- update 2026-09-11T12:56:44Z
--- update 2026-09-11T13:01:44Z
--- update 2026-09-11T13:06:49Z
--- update 2026-09-11T13:11:58Z
--- update 2026-09-11T13:16:59Z
--- update 2026-09-11T13:22:01Z
--- update 2026-09-11T13:27:04Z
--- update 2026-09-11T13:32:04Z
--- update 2026-09-11T13:37:17Z
```

## Analyses (laatste 25 regels)
```
inactive
09:54:59 25844 tokens geladen
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
11:59:36 2892 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
11:59:39   ingelezen tot rowid 1255924 (151022 rijen, 151022 bruikbaar)
11:59:39 ingelezen: 151022 nieuwe trades, 151022 bruikbaar (2s)
11:59:40 klaar in 4s -> /opt/schaduwbot/reports/ledger.md
11:59:40 klaar in 0s: 59 tokens, 67 nieuw -> /opt/schaduwbot/reports/video_replay.md
11:59:40 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 11:59 UTC
11:59:40 27728 tokens geladen
11:59:44   2000 tokens, 398779 trades, 119472 posities (4s)
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
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
