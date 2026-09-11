# Schaduwbot status

- tijd: 2026-09-11 00:21:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 10 hours, 34 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 643/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 37984, "tokens_in_memory": 1259, "msgs": 7651335, "trades": 1436576, "creates": 15420, "decode_fail": 104580, "rpc_calls": 23795, "rpc_errors": 2291, "sol_usd": 98.7796252710855, "open_positions": 70}
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
Sep 11 00:07:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:07:59,492 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:08:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:02,834 main INFO screen UNSTABLE pass=0 dev=0.0 ins=78.83 pro=6 1a=False 1b=False 2=True (3.5s)
Sep 11 00:08:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:02,887 main INFO screen BERTHA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.2s)
Sep 11 00:08:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:31,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:08:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:31,652 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:37,937 main INFO screen Trumpbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 11 00:08:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:08:46,843 main INFO screen titty pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 11 00:09:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:09:23,346 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 11 00:10:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:20,684 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:10:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:20,779 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:10:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:21,044 main INFO screen Riley pass=0 dev=0.0 ins=22.84 pro=9 1a=False 1b=False 2=True (0.5s)
Sep 11 00:10:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:37,154 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:10:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:10:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:39,573 main INFO screen SLK pass=0 dev=1.27 ins=0.0 pro=4 1a=False 1b=False 2=False (7.9s)
Sep 11 00:10:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:10:51,415 main INFO screen FROBERT pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 11 00:11:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:11:23,675 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:11:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:11:23,817 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:11:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:11:29,632 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.0s)
Sep 11 00:11:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:11:43,699 main INFO screen USMS pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (8.0s)
Sep 11 00:12:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:12:58,945 main INFO screen Twilight pass=1 dev=0.0 ins=13.56 pro=43 1a=False 1b=False 2=False (2.3s)
Sep 11 00:13:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:00,130 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:13:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:00,247 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:13:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:04,132 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.1s)
Sep 11 00:13:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:04,736 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:13:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:04,853 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:13:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:08,986 main INFO screen ApeOnFone pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.3s)
Sep 11 00:13:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:15,003 main INFO screen JUPCAT pass=0 dev=9.64 ins=11.48 pro=31 1a=False 1b=False 2=False (5.3s)
Sep 11 00:13:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:15,036 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:13:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:15,195 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:13:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:20,735 main INFO screen MOUSE pass=0 dev=0.0 ins=35.89 pro=5 1a=False 1b=False 2=True (5.7s)
Sep 11 00:13:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:32,425 main INFO screen SOLCAT pass=1 dev=0.0 ins=14.16 pro=30 1a=False 1b=False 2=False (3.0s)
Sep 11 00:13:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:38,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:13:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:38,118 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:13:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:13:38,259 main INFO screen MOLLY pass=0 dev=0.0 ins=0.53 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 11 00:14:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:00,929 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:14:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:01,057 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:14:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:03,533 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (8.4s)
Sep 11 00:14:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:04,648 main INFO screen 10M pass=1 dev=0.0 ins=4.49 pro=19 1a=False 1b=False 2=False (3.8s)
Sep 11 00:14:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:11,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:14:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:11,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:14:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:11,786 main INFO screen MOLLY pass=0 dev=0.0 ins=13.93 pro=19 1a=False 1b=False 2=True (0.5s)
Sep 11 00:14:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:31,015 main INFO screen COINWORK pass=0 dev=3.42 ins=13.03 pro=41 1a=False 1b=False 2=True (3.3s)
Sep 11 00:14:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:31,062 main INFO screen MOLLY pass=1 dev=0.0 ins=13.53 pro=39 1a=False 1b=False 2=False (5.1s)
Sep 11 00:14:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:43,182 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:14:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:43,320 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:14:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:14:43,604 main INFO screen MARILYN pass=0 dev=0.0 ins=10.01 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 11 00:15:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:01,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:15:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:01,445 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:15:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:06,853 main INFO screen WTC pass=1 dev=0.0 ins=8.94 pro=17 1a=False 1b=False 2=False (5.6s)
Sep 11 00:15:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:33,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:15:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:33,430 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:15:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:40,371 main INFO screen 10M pass=0 dev=0.0 ins=17.18 pro=11 1a=False 1b=False 2=True (7.1s)
Sep 11 00:15:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:40,812 main INFO screen SOLDOG pass=0 dev=0.0 ins=6.19 pro=74 1a=False 1b=False 2=True (2.9s)
Sep 11 00:15:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:41,926 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:15:41 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:15:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:15:50,141 main INFO screen 911 pass=0 dev=0.43 ins=0.0 pro=1 1a=False 1b=False 2=False (5.8s)
Sep 11 00:16:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:07,336 main INFO screen CashCat pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 11 00:16:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:10,887 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:16:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:11,004 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:16:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:14,534 main INFO screen SPLASHY pass=0 dev=0.0 ins=25.38 pro=30 1a=False 1b=False 2=True (3.7s)
Sep 11 00:16:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:49,635 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:16:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:49,874 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:16:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:50,001 main INFO screen MOLLY pass=0 dev=0.0 ins=17.78 pro=24 1a=False 1b=False 2=True (0.5s)
Sep 11 00:16:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:16:57,142 main INFO screen Molly pass=0 dev=0.0 ins=11.47 pro=26 1a=False 1b=False 2=True (2.9s)
Sep 11 00:17:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:05,812 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:17:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:05,966 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:17:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:12,447 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.7s)
Sep 11 00:17:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:19,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:17:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:19,798 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:17:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:17:25,475 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 00:18:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:18:51,685 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:18:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:18:51,783 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:18:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:18:58,652 main INFO screen JUPCAT pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=True (7.1s)
Sep 11 00:19:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:05,759 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.5s)
Sep 11 00:19:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:13,198 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:19:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:13,324 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:19:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:13,648 main INFO screen Molly pass=0 dev=0.0 ins=25.81 pro=18 1a=False 1b=False 2=True (0.5s)
Sep 11 00:19:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:40,346 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:19:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:40,439 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:19:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:19:40,780 main INFO screen Molly pass=0 dev=0.0 ins=20.54 pro=28 1a=False 1b=False 2=True (0.5s)
Sep 11 00:20:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:20:53,569 main INFO screen Chinacat pass=0 dev=0.22 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 11 00:21:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:21:21,656 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:21:21 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
