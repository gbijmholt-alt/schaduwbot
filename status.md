# Schaduwbot status

- tijd: 2026-09-11 01:53:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 12 hours, 6 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 644/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 43536, "tokens_in_memory": 1353, "msgs": 8356963, "trades": 1608326, "creates": 17615, "decode_fail": 113176, "rpc_calls": 26213, "rpc_errors": 2517, "sol_usd": 99.33729567957872, "open_positions": 29}
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
Sep 11 01:33:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:14,578 aiohttp.access INFO 138.197.16.14 [11/Sep/2026:01:33:14 +0000] "UNKNOWN / HTTP/1.0" 400 407 "-" "-"
Sep 11 01:33:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:38,058 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:33:38 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:33:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:49,351 main INFO screen GIAB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 01:33:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:33:54,435 main INFO screen DREAM pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 11 01:34:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:04,247 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:34:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:04,342 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:34:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:04,700 main INFO screen BEAST pass=0 dev=0.0 ins=17.01 pro=25 1a=False 1b=False 2=True (0.5s)
Sep 11 01:34:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:10,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:34:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:11,123 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:34:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:34:11,270 main INFO screen GIAB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 01:35:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:35:57,161 main INFO screen KIRKVERSE pass=0 dev=8.46 ins=0.89 pro=30 1a=False 1b=False 2=False (2.0s)
Sep 11 01:36:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:25,593 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:36:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:25,693 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:36:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:25,877 main INFO screen $RIP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 01:36:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:53,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:36:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:53,118 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:36:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:36:53,307 main INFO screen $RIP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:37:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:37:15,957 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.0s)
Sep 11 01:37:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:37:28,103 main INFO screen TIKTOK pass=0 dev=4.82 ins=24.06 pro=45 1a=False 1b=False 2=True (3.5s)
Sep 11 01:38:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:38:15,537 main INFO screen TIKTOK pass=0 dev=0.0 ins=2.5 pro=63 1a=False 1b=False 2=True (3.4s)
Sep 11 01:38:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:38:26,224 main INFO screen $PTA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 01:38:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:38:39,608 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:38:39 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:39:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:39:22,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:39:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:39:22,917 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:39:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:39:23,094 main INFO screen TRUMP pass=0 dev=0.0 ins=79.24 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 01:40:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:40:35,567 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:40:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:40:35,663 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:40:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:40:36,021 main INFO screen Fartcoin pass=0 dev=0.0 ins=8.13 pro=17 1a=False 1b=False 2=True (0.5s)
Sep 11 01:41:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:41:32,883 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:41:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:41:33,011 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:41:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:41:33,188 main INFO screen RCASH pass=0 dev=0.0 ins=43.86 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 01:42:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:42:12,910 main INFO screen ORANG pass=0 dev=0.0 ins=20.16 pro=72 1a=False 1b=False 2=True (3.6s)
Sep 11 01:43:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:43:50,269 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:43:50 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:43:57,263 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:43:57,348 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:43:57,555 main INFO screen brokr pass=0 dev=0.0 ins=35.74 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 01:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:44:15,425 main INFO screen garry pass=1 dev=0.15 ins=0.66 pro=26 1a=False 1b=False 2=False (3.4s)
Sep 11 01:44:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:44:20,928 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:44:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:44:21,054 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:44:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:44:21,391 main INFO screen BURST pass=0 dev=0.0 ins=19.52 pro=21 1a=False 1b=False 2=True (0.5s)
Sep 11 01:44:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:44:35,726 main INFO screen ORANG pass=0 dev=0.0 ins=8.37 pro=70 1a=False 1b=False 2=True (3.5s)
Sep 11 01:45:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:09,633 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:45:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:09,769 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:45:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:10,092 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 01:45:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:57,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:45:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:57,168 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:45:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:45:57,353 main INFO screen brokr pass=0 dev=0.0 ins=21.38 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 01:46:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:46:33,721 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:46:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:46:33,819 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:46:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:46:33,998 main INFO screen BIZ pass=0 dev=0.0 ins=34.96 pro=14 1a=False 1b=False 2=True (0.4s)
Sep 11 01:47:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:47:00,419 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:47:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:47:00,511 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:47:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:47:00,762 main INFO screen brokr pass=0 dev=0.0 ins=21.43 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 01:47:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:47:42,927 main INFO screen MAYE pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 01:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:48:59,432 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:48:59 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:04,392 main INFO screen Draft pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (4.9s)
Sep 11 01:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:04,577 main INFO screen WTRMLN pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (5.2s)
Sep 11 01:49:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:55,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:49:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:55,877 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:49:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:56,115 main INFO screen GAYMER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 01:49:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:58,188 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:49:58 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 01:49:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:49:58,552 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:49:58 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 01:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:26,425 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:26,486 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:26,713 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:50:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:33,868 main INFO screen PLAY pass=1 dev=3.94 ins=16.44 pro=62 1a=False 1b=False 2=False (1.2s)
Sep 11 01:50:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:51,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:50:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:52,009 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:50:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:52,182 main INFO screen ZAZU pass=0 dev=0.0 ins=50.0 pro=4 1a=False 1b=False 2=True (0.7s)
Sep 11 01:50:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:50:52,940 main INFO screen BOING pass=0 dev=0.0 ins=12.99 pro=45 1a=False 1b=True 2=False (2.2s)
Sep 11 01:51:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:51:06,696 main INFO screen RCASH pass=1 dev=3.46 ins=17.82 pro=25 1a=False 1b=False 2=False (1.2s)
Sep 11 01:51:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:51:48,448 main INFO screen flashGirl pass=1 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=False (3.3s)
Sep 11 01:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:52:12,972 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:52:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:52:13,074 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:52:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:52:13,437 main INFO screen FLYBRAIN pass=0 dev=0.0 ins=15.2 pro=29 1a=False 1b=False 2=True (0.6s)
Sep 11 01:52:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:52:28,898 main INFO screen YIK pass=0 dev=0.59 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 01:53:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:53:03,865 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:53:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:53:03,967 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:53:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:53:04,156 main INFO screen APE pass=0 dev=0.0 ins=28.33 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 01:53:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:53:53,752 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:53:53 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
