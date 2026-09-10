# Schaduwbot status

- tijd: 2026-09-10 17:21:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 hours, 34 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 586/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 12800, "tokens_in_memory": 1554, "msgs": 2275483, "trades": 425392, "creates": 5122, "decode_fail": 38088, "rpc_calls": 7176, "rpc_errors": 792, "sol_usd": 99.8261536502606, "open_positions": 74}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 16:48 UTC

Gelogde schaduwtrades: **3046**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 4315 | 586 | 12 | 586 | 77 | 1040 | 3046 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 57 | 10% | 1.8% | +36.3% | -17.2% | -11.56% | 79% |
| dip35_V1_gescreend_fail | 284 | 26% | 5.6% | +47.6% | -27.7% | -8.06% | 100% |
| dip35_V1_alle | 355 | 24% | 5.1% | +46.3% | -26.4% | -9.24% | 100% |
| dip35_V2_gescreend_pass | 54 | 11% | 1.9% | +22.9% | -21.0% | -16.12% | 85% |
| dip35_V2_gescreend_fail | 284 | 22% | 6.0% | +79.1% | -29.5% | -5.82% | 100% |
| dip35_V2_alle | 350 | 20% | 5.4% | +71.9% | -28.6% | -8.25% | 100% |
| dip35_V3_gescreend_pass | 57 | 5% | 1.8% | +32.4% | -22.7% | -19.77% | 90% |
| dip35_V3_gescreend_fail | 291 | 13% | 7.9% | +128.1% | -31.2% | -10.43% | 100% |
| dip35_V3_alle | 358 | 12% | 7.0% | +115.9% | -30.3% | -12.74% | 100% |
| dip40_V1_gescreend_pass | 54 | 17% | 1.9% | +42.6% | -16.2% | -6.41% | 67% |
| dip40_V1_gescreend_fail | 277 | 24% | 6.1% | +55.7% | -27.9% | -7.36% | 100% |
| dip40_V1_alle | 343 | 23% | 5.5% | +53.9% | -26.5% | -7.77% | 100% |
| dip40_V2_gescreend_pass | 51 | 14% | 2.0% | +61.0% | -20.1% | -8.95% | 72% |
| dip40_V2_gescreend_fail | 278 | 22% | 6.1% | +84.9% | -29.7% | -5.01% | 100% |
| dip40_V2_alle | 339 | 20% | 5.6% | +80.7% | -28.6% | -6.38% | 100% |
| dip40_V3_gescreend_pass | 54 | 7% | 1.9% | +25.0% | -21.3% | -17.86% | 87% |
| dip40_V3_gescreend_fail | 281 | 14% | 8.2% | +119.3% | -31.8% | -10.80% | 100% |
| dip40_V3_alle | 343 | 13% | 7.3% | +108.2% | -30.5% | -12.67% | 100% |
| dip45_V1_gescreend_pass | 47 | 19% | 2.1% | +45.4% | -16.2% | -4.39% | 63% |
| dip45_V1_gescreend_fail | 261 | 25% | 6.1% | +56.0% | -28.4% | -7.07% | 100% |
| dip45_V1_alle | 320 | 24% | 5.6% | +54.5% | -27.2% | -7.29% | 100% |
| dip45_V2_gescreend_pass | 45 | 20% | 2.2% | +45.1% | -18.4% | -5.72% | 60% |
| dip45_V2_gescreend_fail | 263 | 23% | 6.5% | +87.6% | -29.8% | -3.01% | 100% |
| dip45_V2_alle | 318 | 22% | 6.0% | +80.5% | -28.6% | -4.29% | 100% |
| dip45_V3_gescreend_pass | 47 | 8% | 2.1% | +107.5% | -20.0% | -9.20% | 77% |
| dip45_V3_gescreend_fail | 265 | 16% | 7.9% | +122.2% | -31.3% | -7.58% | 100% |
| dip45_V3_alle | 320 | 14% | 7.2% | +118.5% | -30.1% | -8.71% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 17:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:08:37,975 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:08:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:08:42,784 main INFO screen LOWKIRK pass=0 dev=0.0 ins=13.66 pro=5 1a=False 1b=False 2=True (5.0s)
Sep 10 17:08:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:08:49,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:08:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:08:49,276 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:08:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:08:49,614 main INFO screen BREZ pass=0 dev=0.0 ins=24.87 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 17:09:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:00,246 main INFO screen DIAMAND pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (5.2s)
Sep 10 17:09:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:08,741 main INFO screen RICK pass=0 dev=1.72 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 10 17:09:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:53,927 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:09:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:54,021 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:09:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:57,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:09:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:57,718 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:09:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:09:59,418 main INFO screen ? pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.6s)
Sep 10 17:10:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:03,895 main INFO screen $POTATO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 10 17:10:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:06,589 main INFO screen 911 pass=1 dev=0.0 ins=6.7 pro=17 1a=False 1b=False 2=False (2.7s)
Sep 10 17:10:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:45,443 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:10:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:45,538 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:10:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:45,906 main INFO screen SUPERSTONK pass=0 dev=0.0 ins=19.97 pro=29 1a=False 1b=False 2=True (0.6s)
Sep 10 17:10:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:45,984 main INFO screen ASTRAL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.4s)
Sep 10 17:10:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:10:48,202 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:10:48 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 17:12:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:13,391 main INFO screen KIRK pass=1 dev=0.0 ins=7.61 pro=57 1a=False 1b=False 2=False (3.3s)
Sep 10 17:12:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:33,013 main INFO screen DOJECOIN pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 10 17:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:34,421 main INFO screen Hedgy pass=0 dev=7.68 ins=2.5 pro=28 1a=False 1b=True 2=False (5.5s)
Sep 10 17:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:34,581 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:34,695 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:12:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:39,567 main INFO screen BADDOG pass=0 dev=0.0 ins=79.24 pro=9 1a=False 1b=False 2=True (5.1s)
Sep 10 17:12:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:12:57,598 main INFO screen STOCKHOOD pass=0 dev=34.79 ins=0.0 pro=8 1a=False 1b=False 2=True (7.4s)
Sep 10 17:13:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:06,679 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:13:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:06,842 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:13:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:07,153 main INFO screen ily pass=0 dev=0.0 ins=10.85 pro=4 1a=False 1b=False 2=True (0.5s)
Sep 10 17:13:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:17,833 main INFO screen ? pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (8.4s)
Sep 10 17:13:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:24,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:13:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:24,774 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:13:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:13:28,505 main INFO screen REDCAP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 10 17:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:26,627 main INFO screen $OMT pass=0 dev=0.56 ins=0.0 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 10 17:14:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:55,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:14:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:55,684 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:14:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:57,005 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:14:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:57,152 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:14:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:14:59,418 main INFO screen STOCKS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.0s)
Sep 10 17:15:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:15:01,203 main INFO screen AI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 17:15:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:15:12,611 main INFO screen Bankcoin pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 10 17:15:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:15:38,894 main INFO screen VAGINA pass=0 dev=24.53 ins=0.0 pro=35 1a=False 1b=False 2=False (6.3s)
Sep 10 17:15:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:15:59,869 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:15:59 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 17:16:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:16:16,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:16:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:16:16,536 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:16:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:16:20,459 main INFO screen WomenPepe pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 17:16:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:16:51,342 main INFO screen GCAT pass=0 dev=5.0 ins=30.96 pro=11 1a=False 1b=True 2=True (8.1s)
Sep 10 17:17:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:02,358 main INFO screen PERC pass=1 dev=3.79 ins=13.13 pro=63 1a=False 1b=False 2=False (9.9s)
Sep 10 17:17:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:02,823 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:17:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:02,977 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:17:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:03,189 main INFO screen $POTATO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.0s)
Sep 10 17:17:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:08,482 main INFO screen ! pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 10 17:17:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:30,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:17:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:30,748 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:17:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:17:36,745 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.2s)
Sep 10 17:18:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:18:02,356 main INFO screen PepeWomen pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (8.7s)
Sep 10 17:18:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:18:11,660 main INFO screen ! pass=0 dev=0.3 ins=0.0 pro=4 1a=False 1b=False 2=False (8.7s)
Sep 10 17:19:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:19:04,080 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:19:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:19:04,177 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:19:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:19:09,702 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 10 17:19:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:19:27,943 main INFO screen HIPHOP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.6s)
Sep 10 17:19:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:19:48,564 main INFO screen Kirky pass=1 dev=0.0 ins=0.0 pro=31 1a=False 1b=False 2=False (10.4s)
Sep 10 17:20:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:05,251 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:20:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:05,253 main INFO screen $POTATO pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 10 17:20:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:05,335 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:20:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:09,718 main INFO screen MARIO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.5s)
Sep 10 17:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:19,112 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.1s)
Sep 10 17:20:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:21,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:20:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:21,828 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:20:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:29,083 main INFO screen SOLSTONK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.5s)
Sep 10 17:20:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:31,134 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:20:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:31,263 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:20:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:36,504 main INFO screen APEBATON pass=0 dev=0.0 ins=79.17 pro=8 1a=False 1b=False 2=True (5.4s)
Sep 10 17:20:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:38,191 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:20:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:38,382 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:20:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:43,324 main INFO screen SOLFROG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 10 17:20:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:48,208 main INFO screen SATH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (6.7s)
Sep 10 17:20:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:56,266 main INFO screen ! pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 10 17:20:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:20:56,578 main INFO screen GAYceX pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 10 17:21:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:21:37,206 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:21:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
