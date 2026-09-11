# Schaduwbot status

- tijd: 2026-09-11 16:03:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 2 hours, 16 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 823/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 22432, "tokens_in_memory": 6344, "msgs": 2489626, "trades": 581628, "creates": 6539, "decode_fail": 46518, "rpc_calls": 10149, "rpc_errors": 964, "sol_usd": 102.02891078867302, "open_positions": 47, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 15:49 UTC

Gelogde schaduwtrades: **25464**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 17033 | 2392 | 26 | 2392 | 164 | 4446 | 13109 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 286 | 16% | 1.7% | +41.5% | -16.2% | -7.10% | 99% |
| dip35_V1_gescreend_fail | 2573 | 26% | 3.8% | +45.5% | -25.9% | -7.06% | 100% |
| dip35_V1_alle | 2946 | 26% | 3.9% | +44.5% | -25.2% | -7.35% | 100% |
| dip35_V2_gescreend_pass | 283 | 18% | 2.5% | +41.9% | -21.2% | -9.84% | 100% |
| dip35_V2_gescreend_fail | 2575 | 24% | 4.5% | +55.4% | -28.3% | -7.79% | 100% |
| dip35_V2_alle | 2922 | 24% | 4.6% | +53.8% | -27.9% | -8.42% | 100% |
| dip35_V3_gescreend_pass | 286 | 7% | 2.4% | +133.4% | -22.6% | -11.70% | 100% |
| dip35_V3_gescreend_fail | 2612 | 13% | 6.2% | +107.3% | -29.9% | -11.70% | 100% |
| dip35_V3_alle | 2957 | 13% | 6.1% | +106.0% | -29.4% | -12.12% | 100% |
| dip40_V1_gescreend_pass | 262 | 14% | 1.5% | +42.7% | -15.4% | -7.46% | 99% |
| dip40_V1_gescreend_fail | 2502 | 26% | 3.8% | +47.9% | -25.9% | -6.60% | 100% |
| dip40_V1_alle | 2829 | 25% | 3.8% | +47.1% | -25.1% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 260 | 14% | 2.3% | +50.8% | -20.0% | -10.47% | 100% |
| dip40_V2_gescreend_fail | 2497 | 25% | 4.2% | +55.0% | -28.1% | -7.64% | 100% |
| dip40_V2_alle | 2804 | 24% | 4.3% | +54.4% | -27.6% | -8.31% | 100% |
| dip40_V3_gescreend_pass | 263 | 6% | 2.3% | +112.1% | -21.4% | -13.74% | 100% |
| dip40_V3_gescreend_fail | 2534 | 13% | 5.8% | +96.5% | -29.6% | -13.33% | 100% |
| dip40_V3_alle | 2840 | 12% | 5.7% | +95.7% | -29.0% | -13.74% | 100% |
| dip45_V1_gescreend_pass | 251 | 14% | 1.6% | +48.9% | -15.4% | -6.18% | 98% |
| dip45_V1_gescreend_fail | 2431 | 27% | 3.3% | +49.6% | -25.5% | -5.06% | 100% |
| dip45_V1_alle | 2730 | 26% | 3.4% | +49.2% | -24.7% | -5.44% | 100% |
| dip45_V2_gescreend_pass | 248 | 18% | 2.4% | +50.0% | -19.7% | -7.32% | 99% |
| dip45_V2_gescreend_fail | 2416 | 25% | 3.7% | +58.7% | -27.6% | -6.05% | 100% |
| dip45_V2_alle | 2702 | 24% | 3.8% | +57.8% | -27.1% | -6.54% | 100% |
| dip45_V3_gescreend_pass | 251 | 6% | 2.4% | +180.2% | -20.6% | -7.80% | 100% |
| dip45_V3_gescreend_fail | 2449 | 14% | 5.5% | +109.6% | -29.2% | -10.05% | 100% |
| dip45_V3_alle | 2734 | 13% | 5.4% | +111.4% | -28.5% | -10.19% | 100% |

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
| met_xlink | 1931 | 12% | 2.6% | -9.83% | 100% |
| zonder_xlink | 459 | 13% | 0.0% | -6.08% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 15:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:15,845 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:15,977 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:52:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:27,524 main INFO screen hailmary pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 15:52:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:42,469 main INFO screen $CAJUN pass=0 dev=1.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 15:53:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:02,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:53:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:03,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:53:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:03,223 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 15:53:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:30,924 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:53:30 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:53:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:32,609 main INFO screen wind pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 11 15:54:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:54:17,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:54:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:54:17,147 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:54:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:54:17,359 main INFO screen hailmary pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 15:54:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:54:38,554 main INFO screen USMS pass=0 dev=0.0 ins=0.34 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 11 15:55:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:55:27,362 main INFO screen 9TTTLL1 pass=0 dev=2.15 ins=0.0 pro=2 1a=False 1b=False 2=False (13.6s)
Sep 11 15:55:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:55:31,255 main INFO screen Stonkmart pass=0 dev=5.38 ins=0.0 pro=49 1a=False 1b=False 2=False (11.0s)
Sep 11 15:55:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:55:49,129 main INFO screen go pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 15:55:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:55:59,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:56:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:00,321 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:56:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:00,816 main INFO screen Olaf pass=0 dev=0.0 ins=4.45 pro=5 1a=False 1b=False 2=True (1.3s)
Sep 11 15:56:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:01,179 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:56:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:01,437 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:56:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:01,579 main INFO screen stocklana pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (3.6s)
Sep 11 15:56:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:56:01,846 main INFO screen HUH pass=0 dev=0.0 ins=40.07 pro=13 1a=False 1b=False 2=True (0.7s)
Sep 11 15:57:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:13,974 main INFO screen HANSEM pass=0 dev=4.81 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 15:57:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:46,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:57:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:46,559 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:57:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:46,763 main INFO screen TWIN pass=0 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=True (0.6s)
Sep 11 15:57:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:50,243 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:57:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:50,360 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:57:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:57:50,542 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:58:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:58:02,759 main INFO screen DERP pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 11 15:58:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:58:35,289 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:58:35 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:58:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:58:37,525 main INFO screen dontdoit pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 15:58:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:58:53,830 main INFO screen BRD pass=0 dev=22.37 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 15:59:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:16,001 main INFO screen Neko pass=0 dev=7.9 ins=5.63 pro=25 1a=False 1b=False 2=False (2.5s)
Sep 11 15:59:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:24,346 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:59:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:24,407 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:59:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:24,604 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 11 15:59:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:24,998 main INFO screen $PTA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 15:59:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:51,793 main INFO screen $RAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 15:59:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:57,775 main INFO screen iRobMore pass=0 dev=2.46 ins=0.0 pro=2 1a=False 1b=False 2=False (4.6s)
Sep 11 15:59:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:59:58,444 main INFO screen $CAJUN pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (4.8s)
Sep 11 16:00:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:18,078 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:00:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:18,177 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:00:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:20,457 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:00:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:20,582 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:00:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:22,916 main INFO screen BONKAT pass=0 dev=0.0 ins=79.24 pro=2 1a=False 1b=False 2=True (4.9s)
Sep 11 16:00:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:24,222 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 11 16:00:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:28,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:00:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:28,953 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:00:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:30,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:00:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:30,221 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:00:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:30,416 main INFO screen ANXIETYDOG pass=0 dev=0.0 ins=28.71 pro=14 1a=False 1b=False 2=True (0.4s)
Sep 11 16:00:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:00:33,305 main INFO screen WARREN pass=1 dev=0.0 ins=3.44 pro=32 1a=False 1b=False 2=False (4.6s)
Sep 11 16:01:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:01:11,793 main INFO screen ANICOIN pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 11 16:01:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:01:19,404 main INFO screen VRFOMOAPE pass=0 dev=37.84 ins=0.0 pro=5 1a=False 1b=False 2=True (8.3s)
Sep 11 16:02:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:01,059 main INFO screen solanaszn pass=1 dev=0.0 ins=19.3 pro=22 1a=False 1b=False 2=False (5.9s)
Sep 11 16:02:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:09,299 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:02:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:09,440 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:02:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:10,790 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:02:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:10,931 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:02:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:13,687 main INFO screen GAYLANA pass=0 dev=0.0 ins=29.89 pro=12 1a=False 1b=False 2=True (4.5s)
Sep 11 16:02:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:17,692 main INFO screen solbaton pass=0 dev=0.0 ins=77.53 pro=5 1a=False 1b=False 2=True (7.0s)
Sep 11 16:02:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:18,088 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (6.4s)
Sep 11 16:02:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:22,542 main INFO screen GAYCAT pass=0 dev=16.45 ins=0.0 pro=18 1a=False 1b=False 2=False (5.7s)
Sep 11 16:02:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:33,772 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:02:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:33,862 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:02:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:35,523 main INFO screen CEO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.3s)
Sep 11 16:02:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:37,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:02:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:37,349 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:02:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:38,894 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 11 16:02:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:02:41,509 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.4s)
Sep 11 16:03:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:00,347 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:03:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:00,837 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:03:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:08,603 main INFO screen KIRKOWEEN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (8.7s)
Sep 11 16:03:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:08,713 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (10.1s)
Sep 11 16:03:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:09,411 main INFO screen FERSPE pass=0 dev=5.17 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 11 16:03:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:31,046 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:03:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:31,095 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:03:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:37,299 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:03:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T14:34:22Z
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
--- update 2026-09-11T14:49:38Z
--- update 2026-09-11T14:54:48Z
--- update 2026-09-11T15:00:22Z
--- update 2026-09-11T15:05:25Z
--- update 2026-09-11T15:10:36Z
--- update 2026-09-11T15:15:48Z
--- update 2026-09-11T15:21:20Z
--- update 2026-09-11T15:26:33Z
--- update 2026-09-11T15:31:36Z
--- update 2026-09-11T15:37:24Z
--- update 2026-09-11T15:42:36Z
--- update 2026-09-11T15:48:24Z
--- update 2026-09-11T15:53:29Z
--- update 2026-09-11T15:58:34Z
--- update 2026-09-11T16:03:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: bf2f0fbff9834af3ad8812a9ec61480b
analyses gestart (8213ec5e675e)
```

## Analyses (laatste 25 regels)
```
active
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
14:02:53 5048 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
14:02:56   ingelezen tot rowid 1452718 (196794 rijen, 196794 bruikbaar)
14:02:56 ingelezen: 196794 nieuwe trades, 196794 bruikbaar (3s)
14:02:59 klaar in 6s -> /opt/schaduwbot/reports/ledger.md
14:03:01 klaar in 2s: 1642 tokens, 1877 nieuw -> /opt/schaduwbot/reports/video_replay.md
14:03:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 14:03 UTC
14:03:01 29885 tokens geladen
14:03:05   2000 tokens, 356777 trades, 100453 posities (4s)
14:03:09   4000 tokens, 700400 trades, 193583 posities (7s)
14:03:12   6000 tokens, 1047800 trades, 291369 posities (11s)
14:03:16   8000 tokens, 1402251 trades, 394081 posities (15s)
14:03:16 posities: 409300 uit 1453102 trades (15s)
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
16:03:36 7475 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
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
