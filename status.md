# Schaduwbot status

- tijd: 2026-09-11 00:37:13 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 10 hours, 50 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 639/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 38936, "tokens_in_memory": 1339, "msgs": 7774216, "trades": 1472695, "creates": 15881, "decode_fail": 106546, "rpc_calls": 24226, "rpc_errors": 2337, "sol_usd": 98.86097824772388, "open_positions": 73}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 23:48 UTC

Gelogde schaduwtrades: **12127**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14776 | 2109 | 28 | 2109 | 185 | 4062 | 12127 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 149 | 15% | 2.0% | +38.6% | -17.3% | -8.68% | 94% |
| dip35_V1_gescreend_fail | 1215 | 25% | 3.9% | +45.6% | -25.6% | -7.50% | 100% |
| dip35_V1_alle | 1406 | 24% | 4.0% | +44.5% | -25.1% | -8.11% | 100% |
| dip35_V2_gescreend_pass | 148 | 16% | 2.7% | +29.8% | -21.8% | -13.46% | 99% |
| dip35_V2_gescreend_fail | 1222 | 24% | 4.6% | +53.2% | -28.1% | -8.97% | 100% |
| dip35_V2_alle | 1402 | 22% | 4.7% | +50.9% | -27.7% | -10.03% | 100% |
| dip35_V3_gescreend_pass | 149 | 6% | 2.7% | +132.0% | -23.5% | -14.10% | 99% |
| dip35_V3_gescreend_fail | 1226 | 11% | 6.3% | +117.8% | -29.8% | -13.23% | 100% |
| dip35_V3_alle | 1405 | 11% | 6.2% | +115.7% | -29.4% | -13.84% | 100% |
| dip40_V1_gescreend_pass | 137 | 12% | 2.9% | +43.8% | -16.8% | -9.30% | 95% |
| dip40_V1_gescreend_fail | 1181 | 25% | 4.1% | +48.5% | -25.7% | -7.38% | 100% |
| dip40_V1_alle | 1351 | 24% | 4.1% | +47.6% | -25.0% | -7.87% | 100% |
| dip40_V2_gescreend_pass | 136 | 12% | 2.9% | +47.2% | -21.3% | -13.20% | 98% |
| dip40_V2_gescreend_fail | 1187 | 24% | 4.5% | +55.0% | -27.9% | -8.39% | 100% |
| dip40_V2_alle | 1346 | 22% | 4.5% | +54.0% | -27.4% | -9.30% | 100% |
| dip40_V3_gescreend_pass | 138 | 6% | 2.9% | +116.7% | -22.3% | -13.26% | 99% |
| dip40_V3_gescreend_fail | 1193 | 11% | 6.0% | +102.7% | -29.5% | -15.29% | 100% |
| dip40_V3_alle | 1352 | 10% | 5.8% | +101.6% | -29.0% | -15.43% | 100% |
| dip45_V1_gescreend_pass | 126 | 14% | 3.2% | +50.0% | -16.2% | -6.78% | 92% |
| dip45_V1_gescreend_fail | 1139 | 26% | 3.5% | +50.4% | -25.1% | -5.32% | 100% |
| dip45_V1_alle | 1290 | 25% | 3.7% | +50.1% | -24.5% | -5.81% | 100% |
| dip45_V2_gescreend_pass | 125 | 17% | 4.0% | +39.9% | -20.6% | -10.46% | 95% |
| dip45_V2_gescreend_fail | 1142 | 24% | 4.0% | +59.7% | -27.3% | -5.99% | 100% |
| dip45_V2_alle | 1285 | 24% | 4.3% | +57.9% | -26.9% | -6.84% | 100% |
| dip45_V3_gescreend_pass | 126 | 6% | 4.0% | +179.2% | -21.5% | -8.80% | 97% |
| dip45_V3_gescreend_fail | 1148 | 12% | 5.6% | +120.3% | -29.0% | -11.14% | 100% |
| dip45_V3_alle | 1290 | 11% | 5.7% | +122.0% | -28.4% | -11.30% | 100% |

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
Sep 11 00:24:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:24:50,773 main INFO screen RAPEYOU pass=1 dev=3.43 ins=17.93 pro=76 1a=False 1b=False 2=False (7.9s)
Sep 11 00:25:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:06,184 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:25:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:06,294 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:11,670 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:11,804 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:25:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:11,848 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.8s)
Sep 11 00:25:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:18,124 main INFO screen $R6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.5s)
Sep 11 00:25:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:41,213 main INFO screen cap pass=0 dev=1.37 ins=0.0 pro=1 1a=False 1b=False 2=False (5.5s)
Sep 11 00:25:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:46,151 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:25:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:46,266 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:25:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:47,428 main INFO screen $GOOSE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 11 00:25:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:50,539 main INFO screen $RAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.5s)
Sep 11 00:25:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:54,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:25:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:25:55,100 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:26:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:00,970 main INFO screen COCKSOCK pass=0 dev=0.0 ins=22.78 pro=13 1a=False 1b=False 2=True (6.1s)
Sep 11 00:26:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:10,731 main INFO screen cap pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 00:26:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:29,431 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:26:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:29,535 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:26:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:29,753 main INFO screen MAL pass=0 dev=0.0 ins=25.46 pro=21 1a=False 1b=False 2=True (0.4s)
Sep 11 00:26:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:34,161 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:26:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:34,289 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:26:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:37,182 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:26:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:26:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:40,477 main INFO screen MAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 11 00:26:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:46,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:26:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:46,293 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:26:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:26:50,282 main INFO screen SOL CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (4.1s)
Sep 11 00:27:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:27:27,580 main INFO screen $RAT pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 11 00:28:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:12,673 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:28:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:12,760 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:28:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:18,636 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.1s)
Sep 11 00:28:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:48,523 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:28:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:48,630 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:28:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:28:48,963 main INFO screen ICM pass=0 dev=0.0 ins=20.54 pro=22 1a=False 1b=False 2=False (0.5s)
Sep 11 00:29:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:29:35,964 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:29:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:29:36,064 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:29:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:29:36,264 main INFO screen RETAIL pass=0 dev=0.0 ins=21.8 pro=34 1a=False 1b=False 2=True (0.4s)
Sep 11 00:30:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:30:02,169 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 00:30:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:30:02,500 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (8.8s)
Sep 11 00:30:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:30:03,280 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 00:31:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:06,912 main INFO screen MMM pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 00:31:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:19,011 main INFO screen btc pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (1.8s)
Sep 11 00:31:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:29,145 main INFO screen CHefQueef pass=0 dev=0.37 ins=0.0 pro=4 1a=False 1b=False 2=False (2.3s)
Sep 11 00:31:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:38,607 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:31:38 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:31:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:41,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:31:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:41,974 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:31:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:42,150 main INFO screen JUGGER67 pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 11 00:31:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:47,549 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:31:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:47,670 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:31:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:31:47,802 main INFO screen 5 pass=0 dev=0.0 ins=20.74 pro=17 1a=False 1b=False 2=True (0.3s)
Sep 11 00:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:06,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:32:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:07,045 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:32:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:07,402 main INFO screen Encore pass=0 dev=0.0 ins=5.92 pro=35 1a=False 1b=False 2=True (0.5s)
Sep 11 00:32:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:10,850 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:32:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:10,984 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:32:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:11,103 main INFO screen CVX pass=0 dev=0.0 ins=8.05 pro=33 1a=False 1b=False 2=True (0.3s)
Sep 11 00:32:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:18,455 main INFO screen CEREAL pass=1 dev=0.0 ins=6.17 pro=75 1a=False 1b=False 2=False (3.5s)
Sep 11 00:32:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:19,109 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 11 00:32:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:23,173 main INFO screen ANLS pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 11 00:32:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:26,664 main INFO screen mmrich pass=0 dev=2.22 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 00:32:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:32:31,919 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 00:33:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:03,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:33:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:03,183 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:33:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:03,375 main INFO screen GDOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 00:33:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:06,281 main INFO screen vrl pass=0 dev=3.41 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 00:33:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:28,262 main INFO screen buck pass=1 dev=0.0 ins=13.59 pro=30 1a=False 1b=False 2=False (1.9s)
Sep 11 00:33:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:56,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:33:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:56,944 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:33:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:33:57,168 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 00:34:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:29,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:34:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:29,311 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:34:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:29,650 main INFO screen VWANCEGUARD pass=0 dev=0.0 ins=21.17 pro=37 1a=False 1b=False 2=True (0.5s)
Sep 11 00:34:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:38,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:34:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:38,635 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:34:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:34:38,777 main INFO screen $LAPTOP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 00:35:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:35:44,602 main INFO screen Insider pass=0 dev=0.0 ins=16.49 pro=66 1a=False 1b=False 2=True (2.9s)
Sep 11 00:36:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:36:13,964 main INFO screen USELESS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 00:36:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:36:14,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:36:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:36:14,294 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:36:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:36:14,413 main INFO screen $PTA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 00:37:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:37:13,084 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:37:13 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
