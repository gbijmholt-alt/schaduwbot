# Schaduwbot status

- tijd: 2026-09-12 03:03:03 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 13 hours, 16 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1084/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 26575, "tokens_in_memory": 7787, "msgs": 5272034, "trades": 998103, "creates": 9397, "decode_fail": 53695, "rpc_calls": 33624, "rpc_errors": 1352, "sol_usd": 101.6736069666947, "open_positions": 30, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **39337**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 3089 | 511 | 3 | 510 | 29 | 905 | 2781 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 448 | 17% | 2.2% | +44.4% | -16.9% | -6.46% | 100% |
| dip35_V1_gescreend_fail | 3748 | 27% | 3.7% | +45.6% | -25.9% | -6.79% | 100% |
| dip35_V1_alle | 4548 | 26% | 3.8% | +44.7% | -25.2% | -6.89% | 100% |
| dip35_V2_gescreend_pass | 445 | 22% | 3.1% | +43.5% | -21.4% | -7.14% | 100% |
| dip35_V2_gescreend_fail | 3781 | 25% | 4.3% | +56.5% | -27.9% | -7.17% | 100% |
| dip35_V2_alle | 4516 | 24% | 4.4% | +54.0% | -27.6% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 447 | 8% | 3.6% | +323.1% | -22.7% | +6.69% | 100% |
| dip35_V3_gescreend_fail | 3854 | 13% | 5.9% | +117.5% | -29.6% | -9.99% | 100% |
| dip35_V3_alle | 4560 | 13% | 5.9% | +124.0% | -29.2% | -9.14% | 100% |
| dip40_V1_gescreend_pass | 418 | 15% | 2.4% | +47.1% | -16.2% | -6.64% | 100% |
| dip40_V1_gescreend_fail | 3681 | 26% | 3.8% | +47.5% | -25.8% | -6.60% | 100% |
| dip40_V1_alle | 4370 | 25% | 3.8% | +47.4% | -25.1% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 416 | 18% | 2.9% | +46.1% | -20.1% | -8.33% | 100% |
| dip40_V2_gescreend_fail | 3693 | 25% | 4.3% | +55.5% | -27.9% | -7.24% | 100% |
| dip40_V2_alle | 4332 | 24% | 4.4% | +53.8% | -27.4% | -7.91% | 100% |
| dip40_V3_gescreend_pass | 419 | 7% | 3.1% | +332.9% | -21.3% | +4.87% | 100% |
| dip40_V3_gescreend_fail | 3761 | 13% | 5.8% | +115.7% | -29.4% | -10.49% | 100% |
| dip40_V3_alle | 4378 | 13% | 5.8% | +122.6% | -28.9% | -9.72% | 100% |
| dip45_V1_gescreend_pass | 402 | 16% | 2.2% | +48.7% | -16.1% | -5.78% | 100% |
| dip45_V1_gescreend_fail | 3596 | 27% | 3.3% | +48.4% | -25.5% | -5.29% | 100% |
| dip45_V1_alle | 4223 | 26% | 3.4% | +48.4% | -24.8% | -5.60% | 100% |
| dip45_V2_gescreend_pass | 399 | 19% | 2.8% | +45.1% | -20.0% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 3598 | 25% | 3.9% | +58.0% | -27.5% | -6.06% | 100% |
| dip45_V2_alle | 4185 | 24% | 4.0% | +56.1% | -27.1% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 402 | 7% | 2.7% | +392.1% | -20.7% | +9.12% | 100% |
| dip45_V3_gescreend_fail | 3656 | 14% | 5.5% | +121.3% | -29.0% | -7.99% | 100% |
| dip45_V3_alle | 4225 | 13% | 5.5% | +131.2% | -28.5% | -7.14% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2926 | 13% | 3.6% | -10.08% | 100% |
| zonder_xlink | 870 | 19% | 0.0% | +23.66% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 02:48:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:45,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:48:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:45,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:48:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:48,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:48:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:49,549 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:02:48:49 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 02:48:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:52,323 main INFO screen sortout pass=0 dev=0.84 ins=0.0 pro=3 1a=False 1b=False 2=False (7.0s)
Sep 12 02:48:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:48:53,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:49:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:49:00,807 main INFO screen Dog pass=0 dev=0.0 ins=7.93 pro=55 1a=False 1b=False 2=True (20.5s)
Sep 12 02:49:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:49:07,101 main INFO screen PEPEBRAIN pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 12 02:49:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:49:44,437 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:49:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:49:49,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:50:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:50:05,156 main INFO screen IPO pass=0 dev=0.0 ins=12.11 pro=61 1a=False 1b=False 2=True (20.8s)
Sep 12 02:50:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:50:46,197 main INFO screen Usdtd pass=0 dev=0.39 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 12 02:50:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:50:58,371 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:50:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:50:59,659 main INFO screen Apple pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 02:51:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:03,990 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:06,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:06,820 main INFO screen HAPPYWHEELS pass=0 dev=0.0 ins=7.44 pro=49 1a=False 1b=False 2=True (3.9s)
Sep 12 02:51:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:11,286 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:19,085 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (21.5s)
Sep 12 02:51:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:26,480 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:26,728 main INFO screen WhiteBull pass=0 dev=1.74 ins=55.11 pro=18 1a=False 1b=False 2=True (20.9s)
Sep 12 02:51:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:31,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:36,265 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:41,338 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:51:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:46,087 main INFO screen jewmong pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (19.8s)
Sep 12 02:51:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:51:56,188 main INFO screen ANSEM pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 02:52:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:01,975 main INFO screen Pepotamus pass=0 dev=2.12 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 12 02:52:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:07,349 main INFO screen CIP pass=1 dev=3.81 ins=10.89 pro=40 1a=False 1b=False 2=False (3.2s)
Sep 12 02:52:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:24,939 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:52:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:25,357 main INFO screen WCT pass=0 dev=0.0 ins=30.85 pro=21 1a=False 1b=True 2=True (1.9s)
Sep 12 02:52:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:32,121 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 12 02:52:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:54,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:52:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:52:56,000 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:52:55 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:53:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:53:02,814 main INFO screen CPU pass=0 dev=0.0 ins=11.25 pro=68 1a=False 1b=False 2=True (8.1s)
Sep 12 02:55:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:02,441 main INFO screen $CAJUN pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 02:55:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:08,820 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:09,151 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:14,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:17,137 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 12 02:55:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:17,516 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:17,921 main INFO screen SAVWAR pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 12 02:55:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:22,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:28,902 main INFO screen CAY pass=0 dev=0.0 ins=17.89 pro=42 1a=False 1b=False 2=True (19.8s)
Sep 12 02:55:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:31,449 main INFO screen skipoo pass=0 dev=0.35 ins=0.0 pro=7 1a=False 1b=False 2=False (4.1s)
Sep 12 02:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:37,113 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.0s)
Sep 12 02:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:37,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:43,000 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:55:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:55:57,791 main INFO screen CHILLBULL pass=0 dev=0.0 ins=41.08 pro=12 1a=False 1b=False 2=True (19.9s)
Sep 12 02:56:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:56:01,343 main INFO screen jewmong pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 12 02:56:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:56:03,143 main INFO screen MEMEFi pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 12 02:56:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:56:42,322 main INFO screen 🍌 pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 12 02:57:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:57:28,276 main INFO screen skipoo pass=0 dev=1.02 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 02:57:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:57:43,891 main INFO screen PVE pass=1 dev=0.0 ins=16.04 pro=20 1a=False 1b=False 2=False (4.3s)
Sep 12 02:57:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:57:52,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:57:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:57:57,439 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:58:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:02,335 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:58:02 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:58:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:13,225 main INFO screen CHILLBULL pass=0 dev=1.39 ins=41.08 pro=16 1a=False 1b=False 2=True (20.9s)
Sep 12 02:58:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:19,674 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 12 02:58:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:23,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:58:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:28,960 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:58:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:43,936 main INFO screen marcat pass=0 dev=5.2 ins=17.61 pro=26 1a=False 1b=False 2=True (20.1s)
Sep 12 02:58:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:58:59,953 main INFO screen $CAJUN pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 12 02:59:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:05,093 main INFO screen skipoo pass=0 dev=0.95 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 12 02:59:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:05,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:10,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:59:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:25,057 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 02:59:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:38,067 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:59:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:43,138 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:59:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:50,165 main INFO screen MMM pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 12 02:59:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:59:57,796 main INFO screen ROBIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 03:00:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:00:38,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:00:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:00:43,118 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:01:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:01:05,389 main INFO screen Bulljak pass=0 dev=1.39 ins=41.08 pro=17 1a=False 1b=False 2=True (27.4s)
Sep 12 03:01:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:01:21,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:01:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:01:26,884 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:01:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:01:46,804 main INFO screen Tesla pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.1s)
Sep 12 03:02:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:02:00,896 main INFO screen skipoo pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (7.1s)
Sep 12 03:02:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:02:09,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:02:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:02:24,400 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (14.6s)
Sep 12 03:03:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:03:03,378 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:03:03 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T01:37:15Z
--- update 2026-09-12T01:42:15Z
--- update 2026-09-12T01:47:19Z
--- update 2026-09-12T01:52:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 39f959b4ea4249ad9802ce16bcd55516
analyses gestart (8746aefc73b4)
--- update 2026-09-12T01:57:21Z
--- update 2026-09-12T02:02:22Z
--- update 2026-09-12T02:07:22Z
--- update 2026-09-12T02:12:26Z
--- update 2026-09-12T02:17:29Z
--- update 2026-09-12T02:22:33Z
--- update 2026-09-12T02:27:33Z
--- update 2026-09-12T02:32:33Z
--- update 2026-09-12T02:37:36Z
--- update 2026-09-12T02:42:48Z
--- update 2026-09-12T02:47:52Z
--- update 2026-09-12T02:52:55Z
--- update 2026-09-12T02:58:01Z
--- update 2026-09-12T03:03:02Z
```

## Analyses (laatste 25 regels)
```
inactive
01:52:48 3000 aankopen van gevolgde wallets geëvalueerd
01:53:00 grote spelers: saldo van 1359 wallets opgehaald
01:53:57 herkomst: 40 posities gekoppeld
01:53:58 klaar in 97s -> /opt/schaduwbot/reports/ledger.md
01:54:00   2000 nieuwe tokens doorgerekend
01:54:02 klaar in 4s: 11080 tokens, 2981 nieuw -> /opt/schaduwbot/reports/video_replay.md
01:54:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 01:54 UTC
01:54:02 45856 tokens geladen
01:54:04   2000 tokens, 253102 trades, 54428 posities (2s)
01:54:07   4000 tokens, 520825 trades, 111725 posities (5s)
01:54:09   6000 tokens, 782379 trades, 167557 posities (7s)
01:54:11   8000 tokens, 1054119 trades, 222555 posities (9s)
01:54:13   10000 tokens, 1329211 trades, 281413 posities (11s)
01:54:16   12000 tokens, 1594580 trades, 333921 posities (13s)
01:54:18   14000 tokens, 1836819 trades, 382990 posities (15s)
01:54:20   16000 tokens, 2119459 trades, 446339 posities (18s)
01:54:22   18000 tokens, 2395048 trades, 502642 posities (20s)
01:54:24   20000 tokens, 2629029 trades, 552671 posities (22s)
01:54:27   22000 tokens, 2903307 trades, 608372 posities (24s)
01:54:29 posities: 660394 uit 3108846 trades (26s)
01:54:37 148332 wallets gerekend
01:54:38 geluk-toets
01:55:03 persistentie
01:55:05 kopieer-simulatie
01:55:14 klaar in 72s -> /opt/schaduwbot/reports/wallets.md
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
