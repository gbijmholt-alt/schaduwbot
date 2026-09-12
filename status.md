# Schaduwbot status

- tijd: 2026-09-12 02:32:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 12 hours, 45 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.2G/38G | geheugen: 1064/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 24746, "tokens_in_memory": 7842, "msgs": 5024311, "trades": 950013, "creates": 8867, "decode_fail": 52368, "rpc_calls": 32028, "rpc_errors": 1279, "sol_usd": 101.7467373762461, "open_positions": 48, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **38446**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 2011 | 344 | 0 | 344 | 21 | 634 | 1890 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 438 | 17% | 2.3% | +44.5% | -17.0% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 3678 | 27% | 3.7% | +45.6% | -25.9% | -6.85% | 100% |
| dip35_V1_alle | 4446 | 26% | 3.8% | +44.8% | -25.3% | -6.90% | 100% |
| dip35_V2_gescreend_pass | 435 | 22% | 3.2% | +44.2% | -21.6% | -7.21% | 100% |
| dip35_V2_gescreend_fail | 3702 | 25% | 4.3% | +56.4% | -28.1% | -7.23% | 100% |
| dip35_V2_alle | 4408 | 24% | 4.4% | +54.1% | -27.7% | -7.78% | 100% |
| dip35_V3_gescreend_pass | 438 | 8% | 3.7% | +331.7% | -22.8% | +7.15% | 100% |
| dip35_V3_gescreend_fail | 3785 | 13% | 5.9% | +117.9% | -29.7% | -9.94% | 100% |
| dip35_V3_alle | 4464 | 13% | 5.9% | +124.9% | -29.2% | -9.01% | 100% |
| dip40_V1_gescreend_pass | 409 | 15% | 2.4% | +47.3% | -16.3% | -6.81% | 100% |
| dip40_V1_gescreend_fail | 3609 | 26% | 3.8% | +47.4% | -25.9% | -6.72% | 100% |
| dip40_V1_alle | 4271 | 25% | 3.8% | +47.4% | -25.1% | -6.74% | 100% |
| dip40_V2_gescreend_pass | 406 | 18% | 3.0% | +47.1% | -20.2% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 3612 | 25% | 4.3% | +55.5% | -28.1% | -7.39% | 100% |
| dip40_V2_alle | 4224 | 24% | 4.4% | +54.0% | -27.5% | -7.99% | 100% |
| dip40_V3_gescreend_pass | 410 | 7% | 3.2% | +343.8% | -21.4% | +5.30% | 100% |
| dip40_V3_gescreend_fail | 3693 | 13% | 5.9% | +114.9% | -29.5% | -10.70% | 100% |
| dip40_V3_alle | 4285 | 13% | 5.8% | +122.5% | -29.0% | -9.82% | 100% |
| dip45_V1_gescreend_pass | 393 | 16% | 2.3% | +48.8% | -16.2% | -5.79% | 100% |
| dip45_V1_gescreend_fail | 3526 | 27% | 3.3% | +47.9% | -25.6% | -5.54% | 100% |
| dip45_V1_alle | 4129 | 26% | 3.4% | +48.1% | -24.9% | -5.76% | 100% |
| dip45_V2_gescreend_pass | 389 | 19% | 2.8% | +46.0% | -20.1% | -7.37% | 100% |
| dip45_V2_gescreend_fail | 3520 | 25% | 3.9% | +58.0% | -27.6% | -6.24% | 100% |
| dip45_V2_alle | 4083 | 24% | 4.0% | +56.2% | -27.2% | -6.91% | 100% |
| dip45_V3_gescreend_pass | 393 | 7% | 2.8% | +392.1% | -20.8% | +9.71% | 100% |
| dip45_V3_gescreend_fail | 3589 | 14% | 5.5% | +121.6% | -29.0% | -8.11% | 100% |
| dip45_V3_alle | 4136 | 13% | 5.4% | +132.0% | -28.5% | -7.12% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2841 | 13% | 3.7% | -10.15% | 100% |
| zonder_xlink | 870 | 19% | 0.0% | +23.66% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 02:15:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:15:50,689 main INFO screen WOTF pass=0 dev=99.0 ins=0.0 pro=1 1a=False 1b=False 2=True (24.1s)
Sep 12 02:16:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:16:24,877 main INFO screen pepe  pass=0 dev=0.1 ins=0.0 pro=4 1a=False 1b=False 2=False (7.4s)
Sep 12 02:16:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:16:52,196 main INFO screen YONI pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (10.0s)
Sep 12 02:17:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:08,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:17:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:11,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:17:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:13,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:17:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:26,606 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (14.7s)
Sep 12 02:17:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:30,600 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:17:30 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:17:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:32,479 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.3s)
Sep 12 02:17:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:48,083 main INFO screen OIL pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 12 02:17:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:17:51,203 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:18:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:03,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:18:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:04,293 main INFO screen fast pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (13.2s)
Sep 12 02:18:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:08,213 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:18:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:22,568 main INFO screen FBS99c pass=0 dev=1.51 ins=0.0 pro=3 1a=False 1b=False 2=False (6.1s)
Sep 12 02:18:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:29,055 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 12 02:18:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:38,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:18:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:18:43,299 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:19:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:19:01,225 main INFO screen flywifhat pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (23.1s)
Sep 12 02:19:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:19:05,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:19:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:19:09,794 main INFO screen PEELARCHY pass=0 dev=0.28 ins=0.0 pro=5 1a=False 1b=False 2=False (9.5s)
Sep 12 02:19:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:19:10,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:19:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:19:31,868 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.4s)
Sep 12 02:20:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:20:01,606 main INFO screen Coke pass=0 dev=0.0 ins=16.91 pro=49 1a=False 1b=False 2=True (3.0s)
Sep 12 02:20:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:20:48,079 main INFO screen 911 pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 12 02:21:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:21:20,975 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:21:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:21:26,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:21:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:21:44,996 main INFO screen DOGE pass=0 dev=0.0 ins=25.58 pro=20 1a=False 1b=False 2=True (24.1s)
Sep 12 02:22:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:22:34,260 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:22:34 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:22:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:22:41,230 main INFO screen CSWS pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (8.4s)
Sep 12 02:22:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:22:56,558 main INFO screen fast pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (12.0s)
Sep 12 02:22:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:22:56,647 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:23:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:23:01,706 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:23:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:23:22,997 main INFO screen DOGE-1 pass=0 dev=6.63 ins=19.7 pro=46 1a=False 1b=False 2=True (26.4s)
Sep 12 02:23:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:23:34,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:23:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:23:39,169 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:23:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:23:56,179 main INFO screen AWIFPIG pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (22.2s)
Sep 12 02:24:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:24:34,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:24:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:24:40,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:25:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:25:02,154 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.3s)
Sep 12 02:25:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:25:54,821 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:25:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:25:55,940 main INFO screen piscat pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (10.8s)
Sep 12 02:26:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:01,711 main INFO screen air pass=0 dev=0.0 ins=15.89 pro=37 1a=False 1b=False 2=True (7.2s)
Sep 12 02:26:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:02,591 main INFO screen RAM pass=0 dev=0.0 ins=16.61 pro=39 1a=False 1b=True 2=True (7.9s)
Sep 12 02:26:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:17,601 main INFO screen Kwit pass=0 dev=1.46 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 02:26:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:20,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:25,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:34,676 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:39,746 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:44,379 main INFO screen ALLDOG pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (24.1s)
Sep 12 02:26:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:56,658 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:59,462 main INFO screen SBF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.8s)
Sep 12 02:27:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:01,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:27:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:23,845 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.2s)
Sep 12 02:27:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:34,971 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:27:34 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:27:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:51,206 main INFO screen TRUMP pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 12 02:28:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:42,777 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:02:28:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 02:28:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:43,135 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:02:28:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 02:28:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:49,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:28:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:54,280 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:13,637 main INFO screen NUT pass=0 dev=6.63 ins=18.32 pro=42 1a=False 1b=False 2=False (5.4s)
Sep 12 02:29:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:15,366 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.2s)
Sep 12 02:29:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:18,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:23,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:37,212 main INFO screen catfis pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (6.4s)
Sep 12 02:29:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:41,147 main INFO screen UP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.8s)
Sep 12 02:29:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:57,649 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:02,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:14,698 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:20,135 main INFO screen LOOM pass=0 dev=7.55 ins=23.35 pro=33 1a=False 1b=False 2=True (22.6s)
Sep 12 02:30:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:27,093 main INFO screen utility pass=0 dev=0.0 ins=19.43 pro=64 1a=False 1b=False 2=True (12.5s)
Sep 12 02:30:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:31,327 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:36,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:55,567 main INFO screen utility pass=0 dev=0.0 ins=18.32 pro=42 1a=False 1b=False 2=True (24.3s)
Sep 12 02:31:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:15,611 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:20,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:35,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:42,289 main INFO screen Predator pass=0 dev=0.0 ins=42.65 pro=56 1a=False 1b=False 2=True (26.8s)
Sep 12 02:31:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:48,347 main INFO screen VOIDHODL pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (13.8s)
Sep 12 02:32:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:32:34,837 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:32:34 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T01:06:31Z
--- update 2026-09-12T01:11:36Z
--- update 2026-09-12T01:16:55Z
--- update 2026-09-12T01:22:03Z
--- update 2026-09-12T01:27:11Z
--- update 2026-09-12T01:32:13Z
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
