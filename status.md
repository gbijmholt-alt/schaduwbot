# Schaduwbot status

- tijd: 2026-09-11 03:29:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 13 hours, 42 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 645/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 49280, "tokens_in_memory": 1018, "msgs": 9091375, "trades": 1740344, "creates": 19211, "decode_fail": 118880, "rpc_calls": 28600, "rpc_errors": 2760, "sol_usd": 99.2121997411218, "open_positions": 35}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 02:48 UTC

Gelogde schaduwtrades: **14754**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 3510 | 408 | 0 | 409 | 43 | 792 | 2399 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 190 | 15% | 1.6% | +37.8% | -16.8% | -8.51% | 97% |
| dip35_V1_gescreend_fail | 1467 | 26% | 4.0% | +44.5% | -25.4% | -7.54% | 100% |
| dip35_V1_alle | 1710 | 25% | 4.1% | +43.2% | -24.8% | -7.98% | 100% |
| dip35_V2_gescreend_pass | 191 | 17% | 2.1% | +29.7% | -21.5% | -12.69% | 100% |
| dip35_V2_gescreend_fail | 1476 | 24% | 4.7% | +56.5% | -28.0% | -7.68% | 100% |
| dip35_V2_alle | 1704 | 23% | 4.8% | +53.5% | -27.6% | -8.73% | 100% |
| dip35_V3_gescreend_pass | 190 | 6% | 2.6% | +138.2% | -23.4% | -13.19% | 100% |
| dip35_V3_gescreend_fail | 1483 | 12% | 6.2% | +118.9% | -29.7% | -11.67% | 100% |
| dip35_V3_alle | 1708 | 12% | 6.1% | +116.4% | -29.2% | -12.27% | 100% |
| dip40_V1_gescreend_pass | 178 | 13% | 2.2% | +41.2% | -16.4% | -8.95% | 97% |
| dip40_V1_gescreend_fail | 1424 | 25% | 4.1% | +47.2% | -25.4% | -7.22% | 100% |
| dip40_V1_alle | 1641 | 24% | 4.1% | +46.0% | -24.6% | -7.60% | 100% |
| dip40_V2_gescreend_pass | 179 | 13% | 2.2% | +44.7% | -20.4% | -12.05% | 99% |
| dip40_V2_gescreend_fail | 1433 | 24% | 4.5% | +57.8% | -27.7% | -6.92% | 100% |
| dip40_V2_alle | 1637 | 23% | 4.5% | +56.5% | -27.1% | -7.88% | 100% |
| dip40_V3_gescreend_pass | 179 | 6% | 2.8% | +118.0% | -22.1% | -13.53% | 100% |
| dip40_V3_gescreend_fail | 1440 | 12% | 5.9% | +106.8% | -29.4% | -13.13% | 100% |
| dip40_V3_alle | 1642 | 11% | 5.8% | +105.3% | -28.8% | -13.51% | 100% |
| dip45_V1_gescreend_pass | 166 | 14% | 2.4% | +47.6% | -15.6% | -6.51% | 94% |
| dip45_V1_gescreend_fail | 1378 | 27% | 3.5% | +49.2% | -24.8% | -4.76% | 100% |
| dip45_V1_alle | 1572 | 26% | 3.6% | +48.7% | -24.0% | -5.17% | 100% |
| dip45_V2_gescreend_pass | 165 | 19% | 3.0% | +39.5% | -19.5% | -8.39% | 96% |
| dip45_V2_gescreend_fail | 1383 | 25% | 3.9% | +62.8% | -27.0% | -4.18% | 100% |
| dip45_V2_alle | 1567 | 25% | 4.0% | +60.4% | -26.4% | -4.99% | 100% |
| dip45_V3_gescreend_pass | 166 | 7% | 3.6% | +173.8% | -21.1% | -6.98% | 98% |
| dip45_V3_gescreend_fail | 1390 | 13% | 5.5% | +119.2% | -28.8% | -9.41% | 100% |
| dip45_V3_alle | 1573 | 12% | 5.5% | +120.8% | -28.1% | -9.48% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 11 03:13:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:13:35,759 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:13:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:13:35,860 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:13:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:13:37,108 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:13:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 03:13:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:13:40,743 main INFO screen ZORILLA pass=0 dev=0.0 ins=0.28 pro=4 1a=False 1b=False 2=True (5.1s)
Sep 11 03:13:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:13:56,954 main INFO screen MOONPUP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.2s)
Sep 11 03:14:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:31,288 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:14:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:31,412 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:14:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:34,825 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.6s)
Sep 11 03:14:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:47,270 aiohttp.access INFO 20.29.44.10 [11/Sep/2026:03:14:47 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 11 03:14:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:47,523 aiohttp.access INFO 20.29.44.10 [11/Sep/2026:03:14:47 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 11 03:14:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:57,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:14:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:14:57,384 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:15:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:02,196 main INFO screen ZORILLA pass=0 dev=0.0 ins=0.25 pro=4 1a=False 1b=False 2=True (5.0s)
Sep 11 03:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:08,050 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:08,175 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:08,530 main INFO screen Nicholas pass=0 dev=0.0 ins=7.07 pro=34 1a=False 1b=False 2=True (0.5s)
Sep 11 03:15:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:17,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:15:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:17,539 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:15:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:15:24,085 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 11 03:16:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:16:15,634 main INFO screen VEE pass=1 dev=0.01 ins=0.82 pro=35 1a=False 1b=False 2=False (2.4s)
Sep 11 03:16:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:16:36,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:16:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:16:36,800 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:16:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:16:42,262 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (5.7s)
Sep 11 03:17:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:17:32,211 main INFO screen TITS pass=0 dev=2.07 ins=0.0 pro=1 1a=False 1b=False 2=False (4.9s)
Sep 11 03:17:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:17:46,125 main INFO screen mustamp pass=0 dev=0.96 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 03:18:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:18:18,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:18:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:18:19,093 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:18:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:18:19,280 main INFO screen MOG pass=0 dev=0.0 ins=17.53 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 03:19:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:19:04,857 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:19:04 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 03:19:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:19:44,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:19:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:19:44,199 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:19:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:19:44,528 main INFO screen SMART pass=0 dev=0.0 ins=8.13 pro=16 1a=False 1b=False 2=True (0.5s)
Sep 11 03:20:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:20:13,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:20:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:20:13,726 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:20:19,916 main INFO screen thanglong pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.3s)
Sep 11 03:20:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:20:50,078 main INFO screen cap pass=0 dev=1.68 ins=0.0 pro=3 1a=False 1b=False 2=False (10.1s)
Sep 11 03:21:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:06,056 main INFO screen SHROOM pass=0 dev=0.16 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 03:21:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:19,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:21:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:19,103 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:21:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:20,947 main INFO screen BTC pass=1 dev=0.0 ins=2.7 pro=29 1a=False 1b=False 2=False (2.0s)
Sep 11 03:21:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:41,984 main INFO screen CUBEMOM pass=0 dev=6.63 ins=0.0 pro=3 1a=False 1b=False 2=False (6.8s)
Sep 11 03:21:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:21:46,883 main INFO screen Pusky pass=0 dev=1.78 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 11 03:22:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:22:05,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:22:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:22:05,599 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:22:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:22:05,950 main INFO screen Penny pass=0 dev=0.0 ins=23.24 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 11 03:22:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:22:54,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:22:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:22:54,692 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:23:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:23:00,799 main INFO screen PEPO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 03:23:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:23:53,204 main INFO screen ECHO pass=1 dev=3.82 ins=15.72 pro=52 1a=False 1b=False 2=False (6.8s)
Sep 11 03:23:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:23:57,207 main INFO screen mehemded  pass=0 dev=1.5 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 03:24:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:24:32,904 main INFO screen MEMES pass=1 dev=0.05 ins=3.35 pro=61 1a=False 1b=False 2=False (8.0s)
Sep 11 03:24:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:24:34,078 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:24:34 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 03:25:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:25:02,631 main INFO screen BAYGON pass=1 dev=0.12 ins=8.76 pro=57 1a=False 1b=False 2=False (2.9s)
Sep 11 03:25:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:25:54,453 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:25:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:25:54,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:25:58,834 main INFO screen smily pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (4.5s)
Sep 11 03:26:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:07,918 main INFO screen ch pass=0 dev=0.27 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 11 03:26:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:13,629 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:26:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:13,809 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:26:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:20,012 main INFO screen SPX59X pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 11 03:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:47,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:47,723 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:26:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:51,950 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.4s)
Sep 11 03:27:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:37,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:27:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:37,931 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:41,599 main INFO screen JUGTROLL pass=0 dev=0.0 ins=79.24 pro=6 1a=False 1b=False 2=True (3.9s)
Sep 11 03:27:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:42,940 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:27:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:43,074 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:27:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:49,898 main INFO screen dollar pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=True (7.0s)
Sep 11 03:28:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:02,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:28:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:02,697 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:28:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:03,009 main INFO screen + pass=1 dev=0.0 ins=12.8 pro=12 1a=False 1b=False 2=False (0.5s)
Sep 11 03:28:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:37,281 main INFO screen Coinfly pass=0 dev=1.61 ins=0.0 pro=4 1a=False 1b=False 2=False (8.2s)
Sep 11 03:28:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:38,043 main INFO screen vrl pass=0 dev=1.28 ins=0.0 pro=2 1a=False 1b=False 2=False (6.4s)
Sep 11 03:29:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:01,425 main INFO screen MEMECOIN pass=0 dev=0.0 ins=9.51 pro=66 1a=False 1b=False 2=True (3.2s)
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,564 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,933 main INFO screen CREIOPCS pass=0 dev=0.0 ins=0.26 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 11 03:29:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:25,628 main INFO screen BROKE pass=0 dev=0.11 ins=0.0 pro=4 1a=False 1b=False 2=False (7.5s)
Sep 11 03:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:37,096 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:29:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
