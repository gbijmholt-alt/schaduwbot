# Schaduwbot status

- tijd: 2026-09-10 16:23:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 hours, 36 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 563/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 9320, "tokens_in_memory": 1343, "msgs": 1487923, "trades": 302761, "creates": 3616, "decode_fail": 32770, "rpc_calls": 4871, "rpc_errors": 584, "sol_usd": 99.25387846540858, "open_positions": 53}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 15:48 UTC

Gelogde schaduwtrades: **1955**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 2829 | 392 | 9 | 392 | 51 | 673 | 1955 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 36 | 6% | 2.8% | +35.4% | -18.8% | -15.77% | 70% |
| dip35_V1_gescreend_fail | 185 | 28% | 5.9% | +47.5% | -29.0% | -7.87% | 99% |
| dip35_V1_alle | 232 | 25% | 5.6% | +46.4% | -27.6% | -9.45% | 100% |
| dip35_V2_gescreend_pass | 35 | 6% | 2.9% | +1.1% | -22.5% | -21.18% | 78% |
| dip35_V2_gescreend_fail | 176 | 25% | 6.2% | +42.0% | -31.3% | -12.96% | 100% |
| dip35_V2_alle | 221 | 22% | 5.9% | +39.0% | -30.2% | -14.83% | 100% |
| dip35_V3_gescreend_pass | 36 | 6% | 2.8% | +1.3% | -24.0% | -22.61% | 82% |
| dip35_V3_gescreend_fail | 188 | 14% | 8.0% | +110.5% | -31.5% | -11.15% | 100% |
| dip35_V3_alle | 232 | 13% | 7.3% | +96.9% | -30.9% | -13.78% | 100% |
| dip40_V1_gescreend_pass | 34 | 15% | 2.9% | +48.0% | -17.9% | -8.19% | 55% |
| dip40_V1_gescreend_fail | 181 | 25% | 6.6% | +55.8% | -28.2% | -6.86% | 98% |
| dip40_V1_alle | 224 | 24% | 6.2% | +54.6% | -27.0% | -7.31% | 99% |
| dip40_V2_gescreend_pass | 33 | 9% | 3.0% | +64.8% | -21.3% | -13.50% | 66% |
| dip40_V2_gescreend_fail | 172 | 24% | 7.0% | +46.4% | -30.9% | -12.45% | 99% |
| dip40_V2_alle | 213 | 22% | 6.6% | +46.7% | -29.6% | -13.10% | 100% |
| dip40_V3_gescreend_pass | 34 | 6% | 2.9% | +2.3% | -22.4% | -20.97% | 77% |
| dip40_V3_gescreend_fail | 184 | 16% | 8.7% | +103.7% | -31.7% | -10.39% | 100% |
| dip40_V3_alle | 224 | 14% | 8.0% | +94.5% | -30.6% | -12.77% | 100% |
| dip45_V1_gescreend_pass | 29 | 21% | 3.4% | +44.7% | -17.3% | -4.51% | 48% |
| dip45_V1_gescreend_fail | 170 | 26% | 5.9% | +55.2% | -28.5% | -6.32% | 98% |
| dip45_V1_alle | 208 | 26% | 5.8% | +53.6% | -27.4% | -6.36% | 98% |
| dip45_V2_gescreend_pass | 28 | 18% | 3.6% | +42.5% | -18.7% | -7.79% | 51% |
| dip45_V2_gescreend_fail | 160 | 26% | 6.9% | +47.9% | -30.4% | -10.35% | 99% |
| dip45_V2_alle | 196 | 24% | 6.6% | +46.4% | -29.1% | -10.60% | 99% |
| dip45_V3_gescreend_pass | 29 | 10% | 3.4% | +142.5% | -20.0% | -3.15% | 54% |
| dip45_V3_gescreend_fail | 170 | 17% | 8.2% | +115.4% | -31.2% | -6.21% | 100% |
| dip45_V3_alle | 205 | 16% | 7.8% | +114.7% | -30.0% | -6.74% | 100% |

## Beste variant: dip45_V3_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 16:11:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:30,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:11:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:30,828 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:11:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:34,334 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 10 16:11:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:36,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:11:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:36,205 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:11:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:11:43,251 main INFO screen ZRETARD pass=0 dev=0.0 ins=79.1 pro=8 1a=False 1b=False 2=True (7.2s)
Sep 10 16:12:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:12:37,146 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:12:37 +0000] "GET /health HTTP/1.1" 200 423 "-" "Python-urllib/3.14"
Sep 10 16:12:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:12:47,669 main INFO screen Pipi pass=1 dev=0.0 ins=11.38 pro=25 1a=False 1b=False 2=False (4.0s)
Sep 10 16:13:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:27,432 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:13:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:27,517 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:13:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:28,318 main INFO screen Moolah pass=0 dev=0.0 ins=11.83 pro=21 1a=False 1b=False 2=True (1.0s)
Sep 10 16:13:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:37,549 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:13:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:37,672 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:13:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:38,004 main INFO screen Moolah pass=0 dev=0.0 ins=9.16 pro=26 1a=False 1b=False 2=True (0.5s)
Sep 10 16:13:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:42,819 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:13:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:42,910 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:13:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:13:49,513 main INFO screen GOAF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 10 16:14:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:08,074 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (10.8s)
Sep 10 16:14:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:09,417 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (11.5s)
Sep 10 16:14:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:25,299 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:14:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:25,389 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:14:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:32,533 main INFO screen ND4 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 10 16:14:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:14:36,150 main INFO screen GAYNET pass=0 dev=13.43 ins=0.0 pro=19 1a=False 1b=False 2=False (8.8s)
Sep 10 16:15:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:15:22,325 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:15:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:15:22,419 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:15:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:15:22,750 main INFO screen Moolah pass=0 dev=0.0 ins=11.85 pro=19 1a=False 1b=False 2=True (0.6s)
Sep 10 16:15:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:15:59,955 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:16:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:00,071 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:16:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:00,383 main INFO screen Moolah pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 10 16:16:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:06,443 main INFO screen LMAO pass=0 dev=6.28 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 10 16:16:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:27,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:16:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:27,192 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:16:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:27,549 main INFO screen Moolah pass=0 dev=0.0 ins=11.47 pro=18 1a=False 1b=False 2=True (0.6s)
Sep 10 16:16:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:38,652 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:16:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:38,823 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:16:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:43,722 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:16:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:43,848 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:16:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:44,106 main INFO screen PXL pass=0 dev=0.0 ins=69.08 pro=5 1a=False 1b=False 2=True (5.5s)
Sep 10 16:16:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:16:50,337 main INFO screen JUGGERNAUT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 10 16:17:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:17:35,864 main INFO screen ELON pass=1 dev=0.0 ins=17.54 pro=17 1a=False 1b=False 2=False (7.7s)
Sep 10 16:17:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:17:40,350 main INFO screen RISE pass=0 dev=39.07 ins=0.0 pro=6 1a=False 1b=False 2=True (8.0s)
Sep 10 16:17:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:17:53,463 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:17:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:17:53,565 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:17:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:17:53,949 main INFO screen Solana pass=0 dev=0.0 ins=21.53 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 16:18:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:18:09,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:18:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:18:09,523 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:18:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:18:16,958 main INFO screen MELONTON pass=0 dev=0.0 ins=77.54 pro=7 1a=False 1b=False 2=True (7.6s)
Sep 10 16:18:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:18:18,354 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:18:18 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 16:19:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:19:10,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:19:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:19:10,810 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:19:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:19:16,285 main INFO screen AEON pass=0 dev=0.0 ins=21.19 pro=11 1a=False 1b=False 2=False (5.6s)
Sep 10 16:20:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:24,892 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:20:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:24,988 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:20:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:30,350 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:20:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:30,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:20:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:31,253 main INFO screen job pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 10 16:20:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:34,349 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 16:20:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:37,365 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:20:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:37,487 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:20:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:42,481 main INFO screen monki pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 10 16:20:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:54,671 main INFO screen FAGNET pass=1 dev=3.43 ins=5.75 pro=43 1a=False 1b=False 2=False (8.8s)
Sep 10 16:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:58,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:58,962 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:20:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:20:59,892 main INFO screen Finney pass=0 dev=0.0 ins=15.58 pro=24 1a=False 1b=False 2=True (2.2s)
Sep 10 16:21:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:21:06,039 main INFO screen Gayless pass=0 dev=0.0 ins=20.45 pro=55 1a=False 1b=False 2=False (9.3s)
Sep 10 16:21:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:21:39,343 main INFO screen PHO pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 10 16:21:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:21:52,710 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:21:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:21:52,810 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:22:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:22:00,279 main INFO screen STITCH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.7s)
Sep 10 16:22:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:22:23,966 main INFO screen DOOB pass=0 dev=6.56 ins=0.0 pro=3 1a=False 1b=False 2=True (7.3s)
Sep 10 16:22:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:22:38,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:22:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:22:38,625 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:22:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:22:38,965 main INFO screen Democratism pass=0 dev=0.0 ins=11.49 pro=39 1a=False 1b=False 2=True (0.5s)
Sep 10 16:23:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:08,956 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:23:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:09,045 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:23:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:15,345 main INFO screen ROBIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 10 16:23:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:34,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:23:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:34,595 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:23:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:35,574 main INFO screen CRYPTOPHASIA pass=1 dev=0.0 ins=11.81 pro=21 1a=False 1b=False 2=False (1.2s)
Sep 10 16:23:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:23:37,161 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:23:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
