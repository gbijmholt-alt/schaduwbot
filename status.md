# Schaduwbot status

- tijd: 2026-09-10 23:54:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 10 hours, 7 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 640/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 36363, "tokens_in_memory": 1320, "msgs": 7427405, "trades": 1380638, "creates": 14883, "decode_fail": 102357, "rpc_calls": 22846, "rpc_errors": 2203, "sol_usd": 98.7986899440522, "open_positions": 62}
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
Sep 10 23:38:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:24,989 main INFO screen Cluck pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (3.2s)
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,368 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,424 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,653 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 23:39:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:00,425 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:39:00 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 23:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:02,302 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,127 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,239 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.0s)
Sep 10 23:39:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:15,897 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:39:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:16,031 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:39:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:16,151 main INFO screen Lulu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 23:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:33,443 main INFO screen dog pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (3.3s)
Sep 10 23:40:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:40:58,926 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 23:41:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:02,820 main INFO screen SLIPPAGE pass=0 dev=0.16 ins=0.0 pro=3 1a=False 1b=False 2=False (4.5s)
Sep 10 23:41:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:03,987 main INFO screen CHUMP pass=0 dev=1.65 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 23:41:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:10,672 main INFO screen TALIS!! pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,638 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,782 main INFO screen Kirkaversa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 23:41:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:19,308 main INFO screen PDFSURX pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 10 23:41:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:41,544 main INFO screen STONK pass=0 dev=10.22 ins=5.22 pro=46 1a=False 1b=False 2=False (3.3s)
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,445 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,567 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 10 23:41:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:57,528 main INFO screen Messi pass=0 dev=0.12 ins=0.0 pro=2 1a=False 1b=False 2=False (1.6s)
Sep 10 23:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:53,683 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:53,775 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:42:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:54,297 main INFO screen CRACKSKI pass=0 dev=0.0 ins=29.78 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 10 23:43:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:28,735 main INFO screen SOLCAT pass=0 dev=0.05 ins=16.55 pro=67 1a=False 1b=False 2=True (3.4s)
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,799 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 23:44:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:02,203 main INFO screen pumplive pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,488 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,605 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,864 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 23:44:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:07,781 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:44:07 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 23:44:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:09,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:44:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:09,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:44:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:09,752 main INFO screen wifjugger pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 10 23:44:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:32,494 main INFO screen DGS pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 23:44:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:53,071 main INFO screen $DONK pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 10 23:45:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:04,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:45:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:04,783 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:45:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:05,139 main INFO screen HEDGIE pass=0 dev=0.0 ins=28.21 pro=12 1a=False 1b=False 2=False (0.5s)
Sep 10 23:45:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:11,971 main INFO screen lululemon pass=0 dev=0.0 ins=14.42 pro=50 1a=False 1b=False 2=True (3.9s)
Sep 10 23:45:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:49,914 main INFO screen FROBERT pass=0 dev=0.14 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 10 23:45:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:55,676 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:45:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:55,807 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:45:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:55,942 main INFO screen CAI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 23:45:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:56,876 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:45:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:57,006 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:45:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:45:57,324 main INFO screen GRANDMASKI pass=0 dev=0.0 ins=16.66 pro=14 1a=False 1b=False 2=True (0.5s)
Sep 10 23:46:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:46:32,588 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:46:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:46:32,718 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:46:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:46:32,909 main INFO screen RD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.4s)
Sep 10 23:47:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:47:50,967 main INFO screen FUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.0s)
Sep 10 23:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:47:51,530 main INFO screen CRISPE pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (4.3s)
Sep 10 23:49:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:00,022 main INFO screen NUTS pass=0 dev=0.0 ins=20.54 pro=44 1a=False 1b=False 2=False (2.8s)
Sep 10 23:49:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:00,952 main INFO screen Sept11 pass=0 dev=0.07 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 10 23:49:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:20,225 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:49:20 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 23:49:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:25,844 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:49:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:25,900 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:49:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:26,122 main INFO screen FUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 23:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:42,473 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:42,527 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:49:42,752 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 23:50:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:50:57,758 main INFO screen grumpycat pass=0 dev=0.0 ins=3.39 pro=65 1a=False 1b=False 2=True (3.0s)
Sep 10 23:51:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:51:36,904 main INFO screen $GOAT pass=0 dev=2.08 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 10 23:51:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:51:48,080 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 10 23:52:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:52:11,425 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:52:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:52:11,465 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:52:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:52:11,687 main INFO screen FLS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 23:52:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:52:15,267 main INFO screen GCAT pass=0 dev=3.09 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 10 23:53:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:53:00,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:53:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:53:00,410 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:53:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:53:00,602 main INFO screen FUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 23:53:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:53:08,237 main INFO screen SOLCAT pass=0 dev=6.63 ins=22.8 pro=29 1a=False 1b=False 2=False (1.4s)
Sep 10 23:54:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:54:20,399 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:54:20 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
