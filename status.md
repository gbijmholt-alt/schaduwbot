# Schaduwbot status

- tijd: 2026-09-12 00:02:55 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 10 hours, 15 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.1G/38G | geheugen: 941/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 15767, "tokens_in_memory": 5961, "msgs": 3791067, "trades": 670197, "creates": 5961, "decode_fail": 37352, "rpc_calls": 22581, "rpc_errors": 867, "sol_usd": 102.45440488404238, "open_positions": 98, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 23:40 UTC

Gelogde schaduwtrades: **36036**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28017 | 4378 | 41 | 4376 | 367 | 8031 | 23681 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 420 | 17% | 2.4% | +44.7% | -17.2% | -6.61% | 100% |
| dip35_V1_gescreend_fail | 3472 | 27% | 3.7% | +45.7% | -26.0% | -6.87% | 100% |
| dip35_V1_alle | 4172 | 26% | 3.7% | +44.6% | -25.3% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 417 | 22% | 3.4% | +46.2% | -21.8% | -7.08% | 100% |
| dip35_V2_gescreend_fail | 3481 | 25% | 4.3% | +56.5% | -28.2% | -7.34% | 100% |
| dip35_V2_alle | 4130 | 24% | 4.4% | +54.3% | -27.8% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 417 | 9% | 3.8% | +331.7% | -23.0% | +8.45% | 100% |
| dip35_V3_gescreend_fail | 3561 | 13% | 5.9% | +118.6% | -29.7% | -9.86% | 100% |
| dip35_V3_alle | 4180 | 13% | 5.8% | +127.1% | -29.3% | -8.73% | 100% |
| dip40_V1_gescreend_pass | 390 | 15% | 2.6% | +47.3% | -16.5% | -6.86% | 100% |
| dip40_V1_gescreend_fail | 3401 | 26% | 3.7% | +47.4% | -25.9% | -6.72% | 100% |
| dip40_V1_alle | 4007 | 25% | 3.7% | +47.1% | -25.2% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 388 | 17% | 3.1% | +50.1% | -20.4% | -8.40% | 100% |
| dip40_V2_gescreend_fail | 3392 | 25% | 4.2% | +55.5% | -28.1% | -7.55% | 100% |
| dip40_V2_alle | 3959 | 24% | 4.2% | +54.2% | -27.6% | -8.11% | 100% |
| dip40_V3_gescreend_pass | 391 | 8% | 3.3% | +343.8% | -21.5% | +6.53% | 100% |
| dip40_V3_gescreend_fail | 3469 | 13% | 5.6% | +113.5% | -29.5% | -10.94% | 100% |
| dip40_V3_alle | 4015 | 13% | 5.6% | +122.7% | -29.0% | -9.85% | 100% |
| dip45_V1_gescreend_pass | 374 | 16% | 2.4% | +48.8% | -16.4% | -5.75% | 100% |
| dip45_V1_gescreend_fail | 3322 | 27% | 3.2% | +47.8% | -25.6% | -5.55% | 100% |
| dip45_V1_alle | 3873 | 26% | 3.3% | +47.7% | -25.0% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 371 | 19% | 3.0% | +48.3% | -20.2% | -7.12% | 100% |
| dip45_V2_gescreend_fail | 3305 | 25% | 3.8% | +57.6% | -27.7% | -6.37% | 100% |
| dip45_V2_alle | 3826 | 24% | 3.9% | +56.0% | -27.2% | -6.97% | 100% |
| dip45_V3_gescreend_pass | 375 | 8% | 2.9% | +392.1% | -20.8% | +11.14% | 100% |
| dip45_V3_gescreend_fail | 3369 | 14% | 5.3% | +120.2% | -29.0% | -8.15% | 100% |
| dip45_V3_alle | 3874 | 13% | 5.2% | +132.0% | -28.4% | -6.94% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.6%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2718 | 13% | 3.9% | -9.99% | 100% |
| zonder_xlink | 825 | 19% | 0.0% | +25.41% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 23:52:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:09,734 main INFO screen co1n9 pass=0 dev=0.0 ins=19.0 pro=44 1a=False 1b=False 2=True (20.9s)
Sep 11 23:52:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:35,056 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 23:52:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:36,892 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:52:36 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 23:52:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:37,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:52:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:46,926 main INFO screen GRL pass=0 dev=0.0 ins=17.42 pro=56 1a=False 1b=False 2=True (9.1s)
Sep 11 23:52:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:51,075 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:52:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:52:56,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:02,521 main INFO screen sendorjohnson pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 23:53:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:08,572 main INFO screen $QAIS pass=0 dev=2.75 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 11 23:53:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:10,389 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.4s)
Sep 11 23:53:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:20,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:23,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:25,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:28,879 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:29,513 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:34,581 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:53:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:40,509 main INFO screen SENDIT pass=0 dev=3.46 ins=37.76 pro=29 1a=False 1b=False 2=True (20.4s)
Sep 11 23:53:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:43,464 main INFO screen WOFI pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 11 23:53:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:53:48,838 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.4s)
Sep 11 23:54:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:17,857 main INFO screen DOGE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 23:54:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:28,596 main INFO screen $MEOWX pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 11 23:54:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:42,286 main INFO screen NUTS pass=0 dev=0.0 ins=19.11 pro=70 1a=False 1b=False 2=True (3.8s)
Sep 11 23:54:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:46,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:54:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:48,146 main INFO screen BALLS pass=1 dev=0.88 ins=0.56 pro=31 1a=False 1b=False 2=False (3.7s)
Sep 11 23:54:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:54:53,675 main INFO screen CRISPE pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 23:55:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:55:05,507 main INFO screen trumpog pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 11 23:55:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:55:28,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:55:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:55:33,244 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:55:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:55:44,967 main INFO screen $CAJUN pass=0 dev=0.83 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 23:55:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:55:48,802 main INFO screen SCAT pass=0 dev=0.0 ins=8.54 pro=73 1a=False 1b=False 2=True (20.7s)
Sep 11 23:56:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:02,051 main INFO screen CRISPE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 23:56:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:13,975 main INFO screen N pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 11 23:56:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:29,950 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 11 23:56:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:30,830 main INFO screen     $ASTG pass=0 dev=0.31 ins=0.0 pro=1 1a=False 1b=False 2=False (5.0s)
Sep 11 23:56:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:39,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:56:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:56:46,625 main INFO screen biggerball pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.1s)
Sep 11 23:57:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:57:26,169 aiohttp.access INFO 94.154.43.126 [11/Sep/2026:23:57:26 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 23:57:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:57:37,152 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:57:37 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 23:57:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:57:51,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:57:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:57:58,838 main INFO screen FLYSTONKS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 11 23:57:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:57:58,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:58:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:03,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:58:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:07,861 main INFO screen ROBINFLY pass=0 dev=0.0 ins=28.71 pro=21 1a=False 1b=False 2=False (2.8s)
Sep 11 23:58:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:10,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:58:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:20,718 main INFO screen anorchia pass=0 dev=0.0 ins=17.56 pro=60 1a=False 1b=False 2=True (10.7s)
Sep 11 23:58:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:21,810 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (23.1s)
Sep 11 23:58:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:23,778 main INFO screen Bricko pass=0 dev=0.06 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 23:58:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:31,096 main INFO screen RIPIT pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 23:58:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:32,499 main INFO screen PEPE pass=0 dev=0.0 ins=14.99 pro=38 1a=False 1b=False 2=True (5.4s)
Sep 11 23:58:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:50,443 aiohttp.access INFO 40.124.178.49 [11/Sep/2026:23:58:50 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 11 23:58:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:58:50,684 aiohttp.access INFO 40.124.178.49 [11/Sep/2026:23:58:50 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 11 23:59:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:04,598 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:59:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:08,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:59:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:09,666 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,388 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "UNKNOWN / HTTP/1.0" 400 218 "-" "-"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,447 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,503 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,555 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,618 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,674 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,750 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 23:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:10,806 aiohttp.access INFO 2.57.122.103 [11/Sep/2026:23:59:10 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 23:59:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:13,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:59:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:22,932 main INFO screen ZFLY pass=0 dev=0.0 ins=22.02 pro=44 1a=False 1b=False 2=True (18.4s)
Sep 11 23:59:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:27,873 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 11 23:59:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:59:43,483 main INFO screen $CAJUN pass=0 dev=0.48 ins=0.0 pro=2 1a=False 1b=False 2=True (2.5s)
Sep 12 00:00:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:09,314 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:00:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:14,382 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:00:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:26,468 main INFO screen PWO pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 12 00:00:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:27,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:00:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:32,484 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:00:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:33,924 main INFO screen BUBBLE pass=0 dev=0.0 ins=17.61 pro=60 1a=False 1b=False 2=True (24.7s)
Sep 12 00:00:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:42,246 main INFO screen STONKSCAT pass=1 dev=0.02 ins=0.0 pro=51 1a=False 1b=False 2=False (8.4s)
Sep 12 00:00:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:51,811 main INFO screen COPYCAT pass=0 dev=0.64 ins=16.37 pro=20 1a=False 1b=False 2=True (10.9s)
Sep 12 00:00:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:54,651 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=2 1a=False 1b=False 2=True (27.7s)
Sep 12 00:00:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:00:55,015 main INFO screen ZCUMBER pass=0 dev=1.22 ins=30.6 pro=17 1a=False 1b=True 2=True (9.5s)
Sep 12 00:01:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:01:54,797 main INFO screen Milestones pass=0 dev=0.86 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 12 00:02:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:02:39,019 main INFO screen LUMIO pass=0 dev=0.0 ins=21.07 pro=70 1a=False 1b=False 2=True (10.8s)
Sep 12 00:02:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:02:40,191 main INFO screen Inkyy pass=0 dev=0.0 ins=16.32 pro=28 1a=False 1b=True 2=True (10.0s)
Sep 12 00:02:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:02:55,661 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:02:55 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T22:35:46Z
--- update 2026-09-11T22:40:58Z
--- update 2026-09-11T22:45:58Z
--- update 2026-09-11T22:51:07Z
--- update 2026-09-11T22:56:09Z
--- update 2026-09-11T23:01:22Z
--- update 2026-09-11T23:06:34Z
--- update 2026-09-11T23:11:35Z
--- update 2026-09-11T23:16:36Z
--- update 2026-09-11T23:22:10Z
--- update 2026-09-11T23:27:17Z
--- update 2026-09-11T23:32:26Z
--- update 2026-09-11T23:37:30Z
--- update 2026-09-11T23:42:35Z
--- update 2026-09-11T23:47:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: b162cdb09d844c599f2691bd2f42382f
analyses gestart (8746aefc73b4)
--- update 2026-09-11T23:52:35Z
--- update 2026-09-11T23:57:36Z
--- update 2026-09-12T00:02:54Z
```

## Analyses (laatste 25 regels)
```
inactive
23:47:43 ingelezen: 322040 nieuwe trades, 322040 bruikbaar (7s)
23:48:00 2429 aankopen van gevolgde wallets geëvalueerd
23:48:06 grote spelers: saldo van 404 wallets opgehaald
23:49:10 herkomst: 40 posities gekoppeld
23:49:11 klaar in 95s -> /opt/schaduwbot/reports/ledger.md
23:49:13   2000 nieuwe tokens doorgerekend
23:49:14 klaar in 4s: 8512 tokens, 2651 nieuw -> /opt/schaduwbot/reports/video_replay.md
23:49:15 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 23:49 UTC
23:49:15 43238 tokens geladen
23:49:17   2000 tokens, 267586 trades, 60734 posities (3s)
23:49:20   4000 tokens, 532423 trades, 117776 posities (5s)
23:49:22   6000 tokens, 799668 trades, 174921 posities (7s)
23:49:24   8000 tokens, 1110246 trades, 245252 posities (10s)
23:49:26   10000 tokens, 1366401 trades, 294918 posities (12s)
23:49:29   12000 tokens, 1641516 trades, 355008 posities (14s)
23:49:31   14000 tokens, 1922876 trades, 417966 posities (16s)
23:49:34   16000 tokens, 2201914 trades, 478052 posities (19s)
23:49:36   18000 tokens, 2446968 trades, 532110 posities (22s)
23:49:39   20000 tokens, 2731719 trades, 594313 posities (24s)
23:49:40 posities: 627709 uit 2860518 trades (26s)
23:49:48 141754 wallets gerekend
23:49:49 geluk-toets
23:50:14 persistentie
23:50:15 kopieer-simulatie
23:50:24 klaar in 70s -> /opt/schaduwbot/reports/wallets.md
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
