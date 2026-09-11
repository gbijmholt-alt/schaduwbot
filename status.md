# Schaduwbot status

- tijd: 2026-09-11 01:33:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 11 hours, 46 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 653/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 42321, "tokens_in_memory": 1448, "msgs": 8213233, "trades": 1581093, "creates": 17247, "decode_fail": 111493, "rpc_calls": 25807, "rpc_errors": 2481, "sol_usd": 98.90539992312381, "open_positions": 46}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 00:48 UTC

Gelogde schaduwtrades: **13207**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 1153 | 134 | 0 | 135 | 13 | 286 | 852 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 162 | 15% | 1.9% | +37.5% | -17.3% | -8.81% | 96% |
| dip35_V1_gescreend_fail | 1320 | 25% | 4.2% | +44.8% | -25.8% | -7.86% | 100% |
| dip35_V1_alle | 1529 | 24% | 4.3% | +43.5% | -25.2% | -8.37% | 100% |
| dip35_V2_gescreend_pass | 161 | 16% | 2.5% | +31.2% | -21.8% | -13.23% | 99% |
| dip35_V2_gescreend_fail | 1328 | 23% | 4.9% | +52.0% | -28.2% | -9.54% | 100% |
| dip35_V2_alle | 1523 | 22% | 5.0% | +49.9% | -27.9% | -10.45% | 100% |
| dip35_V3_gescreend_pass | 163 | 6% | 2.5% | +143.0% | -23.3% | -13.07% | 99% |
| dip35_V3_gescreend_fail | 1337 | 12% | 6.5% | +125.8% | -30.0% | -11.93% | 100% |
| dip35_V3_alle | 1532 | 11% | 6.4% | +123.6% | -29.5% | -12.56% | 100% |
| dip40_V1_gescreend_pass | 151 | 12% | 2.6% | +43.2% | -16.7% | -9.56% | 96% |
| dip40_V1_gescreend_fail | 1282 | 25% | 4.4% | +48.1% | -25.9% | -7.72% | 100% |
| dip40_V1_alle | 1470 | 24% | 4.5% | +47.0% | -25.1% | -8.16% | 100% |
| dip40_V2_gescreend_pass | 150 | 12% | 2.7% | +43.6% | -21.0% | -13.26% | 99% |
| dip40_V2_gescreend_fail | 1291 | 24% | 4.8% | +53.8% | -28.1% | -8.78% | 100% |
| dip40_V2_alle | 1465 | 22% | 4.8% | +52.8% | -27.5% | -9.66% | 100% |
| dip40_V3_gescreend_pass | 152 | 6% | 2.6% | +116.7% | -22.0% | -13.78% | 99% |
| dip40_V3_gescreend_fail | 1302 | 11% | 6.3% | +112.0% | -29.7% | -13.49% | 100% |
| dip40_V3_alle | 1476 | 11% | 6.2% | +110.3% | -29.1% | -13.90% | 100% |
| dip45_V1_gescreend_pass | 140 | 14% | 2.9% | +49.0% | -16.0% | -7.17% | 93% |
| dip45_V1_gescreend_fail | 1239 | 27% | 3.7% | +49.9% | -25.3% | -5.12% | 100% |
| dip45_V1_alle | 1405 | 26% | 3.8% | +49.6% | -24.5% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 138 | 17% | 3.6% | +39.8% | -20.3% | -9.80% | 96% |
| dip45_V2_gescreend_fail | 1242 | 25% | 4.2% | +59.0% | -27.4% | -5.79% | 100% |
| dip45_V2_alle | 1398 | 24% | 4.4% | +57.3% | -26.9% | -6.57% | 100% |
| dip45_V3_gescreend_pass | 140 | 7% | 3.6% | +183.9% | -21.2% | -6.54% | 97% |
| dip45_V3_gescreend_fail | 1253 | 12% | 5.8% | +126.5% | -29.1% | -9.72% | 100% |
| dip45_V3_alle | 1409 | 12% | 5.8% | +128.5% | -28.5% | -9.77% | 100% |

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
Sep 11 01:15:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:15:52,642 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:15:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:15:57,259 main INFO screen PUMPSTOCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.8s)
Sep 11 01:15:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:15:57,677 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:15:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:15:57,761 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:16:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:16:04,667 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.1s)
Sep 11 01:16:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:16:35,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:16:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:16:36,076 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:16:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:16:36,359 main INFO screen harold pass=0 dev=0.0 ins=28.69 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 11 01:17:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:17:19,691 main INFO screen BTCPRIUS pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (7.4s)
Sep 11 01:17:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:17:30,911 main INFO screen HOTLINE pass=0 dev=10.08 ins=0.71 pro=11 1a=False 1b=True 2=False (8.3s)
Sep 11 01:18:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:18:04,465 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:18:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:18:04,522 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:18:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:18:08,522 main INFO screen $OMT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.2s)
Sep 11 01:18:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:18:30,890 main INFO screen Retire pass=1 dev=0.0 ins=9.45 pro=33 1a=False 1b=False 2=False (3.3s)
Sep 11 01:18:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:18:36,388 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:18:36 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:19:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:00,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:19:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:00,283 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:06,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:06,279 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:06,960 main INFO screen MESSI pass=0 dev=0.0 ins=31.26 pro=5 1a=False 1b=False 2=True (6.9s)
Sep 11 01:19:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:12,431 main INFO screen Coca Cola pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 01:19:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:19:33,403 main INFO screen H2E pass=1 dev=1.05 ins=0.0 pro=77 1a=False 1b=False 2=False (9.4s)
Sep 11 01:21:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:21:04,701 main INFO screen pgpt pass=0 dev=0.0 ins=0.0 pro=80 1a=False 1b=False 2=True (7.4s)
Sep 11 01:21:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:21:17,519 main INFO screen waltervit pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.2s)
Sep 11 01:21:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:21:20,537 main INFO screen AMD pass=0 dev=35.19 ins=0.0 pro=10 1a=False 1b=False 2=False (9.0s)
Sep 11 01:21:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:21:20,950 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (12.5s)
Sep 11 01:21:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:21:35,381 main INFO screen SHLM pass=0 dev=0.38 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 11 01:22:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:01,382 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:22:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:01,505 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:22:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:04,918 main INFO screen Bros pass=1 dev=0.0 ins=16.84 pro=43 1a=False 1b=False 2=False (9.4s)
Sep 11 01:22:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:07,675 main INFO screen UBC pass=0 dev=0.0 ins=55.31 pro=6 1a=False 1b=False 2=True (6.4s)
Sep 11 01:22:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:21,304 main INFO screen Pippo pass=0 dev=0.01 ins=21.79 pro=55 1a=False 1b=False 2=True (3.3s)
Sep 11 01:22:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:42,998 main INFO screen Cicada3301 pass=0 dev=26.58 ins=0.0 pro=7 1a=False 1b=False 2=True (7.6s)
Sep 11 01:22:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:48,856 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:22:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:48,979 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:22:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:22:52,781 main INFO screen meme pass=0 dev=0.0 ins=23.5 pro=16 1a=False 1b=False 2=True (4.0s)
Sep 11 01:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:23:18,999 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:23:19,102 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:23:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:23:23,573 main INFO screen STONKAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 11 01:23:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:23:36,780 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:23:36 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:24:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:24:10,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:24:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:24:10,875 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:24:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:24:11,061 main INFO screen harold pass=0 dev=0.0 ins=11.45 pro=15 1a=False 1b=False 2=True (0.4s)
Sep 11 01:24:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:24:55,251 main INFO screen SCRVAN pass=0 dev=0.46 ins=0.0 pro=5 1a=False 1b=False 2=False (8.2s)
Sep 11 01:25:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:25:54,005 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:25:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:25:54,097 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:25:58,139 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.2s)
Sep 11 01:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:25:58,770 main INFO screen LAPTOP pass=1 dev=0.0 ins=10.5 pro=57 1a=False 1b=False 2=False (2.1s)
Sep 11 01:26:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:26:46,382 main INFO screen 🇩🇪 pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 11 01:26:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:26:57,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:26:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:26:57,972 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:27:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:27:05,259 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.5s)
Sep 11 01:27:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:27:05,874 main INFO screen GAYPAL pass=0 dev=0.38 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 11 01:27:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:27:05,939 main INFO screen us pass=0 dev=1.95 ins=23.51 pro=40 1a=False 1b=False 2=True (6.7s)
Sep 11 01:27:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:27:38,740 main INFO screen Diddy pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 11 01:28:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:01,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:28:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:01,873 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:28:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:06,647 main INFO screen MetaMask pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.0s)
Sep 11 01:28:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:08,326 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:28:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:08,449 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:28:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:11,653 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.4s)
Sep 11 01:28:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:29,305 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:28:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 01:28:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:29,648 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:28:29 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 01:28:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:28:37,030 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:28:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:29:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:00,898 main INFO screen LMAO pass=0 dev=1.72 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 11 01:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:37,735 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 01:29:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:43,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:44,079 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:44,398 main INFO screen Eugene pass=0 dev=0.0 ins=7.4 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 11 01:29:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:29:45,381 main INFO screen FROGC pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 11 01:31:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:24,104 main INFO screen FROGC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.4s)
Sep 11 01:31:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:24,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:31:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:24,679 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:31:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:24,907 main INFO screen ARB pass=0 dev=0.0 ins=41.74 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 01:31:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:36,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:31:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:36,657 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:31:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:31:36,781 main INFO screen MISTAKE pass=0 dev=0.0 ins=62.17 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 11 01:33:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:14,391 aiohttp.access INFO 138.197.16.14 [11/Sep/2026:01:33:14 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/70.0"
Sep 11 01:33:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:14,578 aiohttp.access INFO 138.197.16.14 [11/Sep/2026:01:33:14 +0000] "UNKNOWN / HTTP/1.0" 400 407 "-" "-"
Sep 11 01:33:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:38,058 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:33:38 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
