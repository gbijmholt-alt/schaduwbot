# Schaduwbot status

- tijd: 2026-09-10 17:31:56 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 hours, 44 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 582/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 13419, "tokens_in_memory": 1459, "msgs": 2377141, "trades": 444369, "creates": 5329, "decode_fail": 38982, "rpc_calls": 7408, "rpc_errors": 824, "sol_usd": 100.14590287561673, "open_positions": 46}
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
Sep 10 17:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:21:38,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:21:38,534 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:21:38,736 main INFO screen COLLECTIBLE pass=0 dev=0.0 ins=10.75 pro=16 1a=False 1b=False 2=True (0.4s)
Sep 10 17:22:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:22:19,383 main INFO screen SONELON pass=0 dev=0.39 ins=0.0 pro=4 1a=False 1b=False 2=False (10.5s)
Sep 10 17:23:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:08,574 main INFO screen Lady pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 10 17:23:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:20,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:23:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:20,306 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:23:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:25,028 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 10 17:23:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:52,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:23:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:53,118 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:23:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:23:58,373 main INFO screen iCat pass=0 dev=0.0 ins=42.4 pro=3 1a=False 1b=False 2=True (5.5s)
Sep 10 17:24:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:12,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:24:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:12,449 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:24:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:16,263 main INFO screen CHRUMP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 10 17:24:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:40,588 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:24:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:40,682 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:24:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:45,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:24:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:45,304 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:24:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:45,498 main INFO screen FGAY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.0s)
Sep 10 17:24:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:46,131 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:24:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:46,277 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:24:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:51,793 main INFO screen NOISE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 10 17:24:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:24:52,692 main INFO screen JustPepe pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.6s)
Sep 10 17:25:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:26,151 main INFO screen sol pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 10 17:25:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:27,083 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:25:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:27,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:25:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:27,341 main INFO screen Kirk pass=0 dev=0.0 ins=17.01 pro=17 1a=False 1b=False 2=True (0.3s)
Sep 10 17:25:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:44,944 main INFO screen SQUIDE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 10 17:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:58,900 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:25:58,992 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:26:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:26:03,723 main INFO screen NVIDIA6900 pass=1 dev=0.0 ins=4.3 pro=17 1a=False 1b=False 2=False (4.9s)
Sep 10 17:26:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:26:39,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:26:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:26:39,145 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:26:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:26:39,344 main INFO screen Fredrick pass=0 dev=0.0 ins=35.73 pro=15 1a=False 1b=False 2=True (0.4s)
Sep 10 17:26:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:26:40,341 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:26:40 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 17:27:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:35,277 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:27:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:35,413 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:27:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:39,420 main INFO screen suitdog pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.2s)
Sep 10 17:27:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:54,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:27:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:54,314 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:27:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:27:54,646 main INFO screen TripleS pass=0 dev=0.0 ins=16.52 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 10 17:28:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:28:02,381 main INFO screen SOLSTONK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 10 17:28:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:28:44,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:28:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:28:44,346 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:28:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:28:44,618 main INFO screen Starbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 17:28:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:28:52,807 main INFO screen bek  pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (3.2s)
Sep 10 17:29:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:03,177 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:29:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:03,309 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:29:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:03,454 main INFO screen CASHPIG pass=0 dev=0.0 ins=21.76 pro=36 1a=False 1b=False 2=True (0.3s)
Sep 10 17:29:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:10,875 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:29:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:10,964 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:29:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:12,986 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.2s)
Sep 10 17:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:29:19,942 main INFO screen C pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 10 17:30:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:30:02,077 main INFO screen $BREAD pass=0 dev=0.7 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 10 17:31:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:05,161 aiohttp.access INFO 85.11.167.132 [10/Sep/2026:17:31:05 +0000] "GET / HTTP/1.1" 404 174 "-" "-"
Sep 10 17:31:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:29,454 main INFO screen vrl pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (4.7s)
Sep 10 17:31:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:54,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:31:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:55,058 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:31:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:55,388 main INFO screen BALTZE pass=0 dev=0.0 ins=24.87 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 17:31:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:31:56,449 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:31:56 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
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
