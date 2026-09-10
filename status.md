# Schaduwbot status

- tijd: 2026-09-10 19:38:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 hours, 51 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 614/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 20991, "tokens_in_memory": 1497, "msgs": 4023302, "trades": 735927, "creates": 8391, "decode_fail": 54931, "rpc_calls": 12259, "rpc_errors": 1283, "sol_usd": 99.82499409317802, "open_positions": 78}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 18:48 UTC

Gelogde schaduwtrades: **5438**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 7151 | 973 | 20 | 973 | 110 | 1831 | 5438 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 89 | 14% | 1.1% | +34.1% | -15.2% | -8.57% | 82% |
| dip35_V1_gescreend_fail | 521 | 26% | 4.8% | +45.4% | -26.2% | -7.26% | 100% |
| dip35_V1_alle | 633 | 25% | 4.4% | +43.8% | -25.1% | -8.02% | 100% |
| dip35_V2_gescreend_pass | 88 | 17% | 1.1% | +31.0% | -19.9% | -11.21% | 88% |
| dip35_V2_gescreend_fail | 520 | 24% | 5.2% | +55.6% | -28.0% | -8.37% | 100% |
| dip35_V2_alle | 626 | 22% | 4.8% | +51.8% | -27.3% | -9.47% | 100% |
| dip35_V3_gescreend_pass | 88 | 6% | 1.1% | +75.2% | -21.9% | -16.34% | 95% |
| dip35_V3_gescreend_fail | 530 | 12% | 6.4% | +100.3% | -29.6% | -13.67% | 100% |
| dip35_V3_alle | 634 | 12% | 5.8% | +94.8% | -28.9% | -14.67% | 100% |
| dip40_V1_gescreend_pass | 82 | 16% | 1.2% | +43.4% | -14.6% | -5.37% | 69% |
| dip40_V1_gescreend_fail | 507 | 24% | 5.5% | +50.2% | -26.7% | -8.02% | 100% |
| dip40_V1_alle | 608 | 23% | 4.9% | +48.8% | -25.3% | -8.02% | 100% |
| dip40_V2_gescreend_pass | 81 | 15% | 1.2% | +54.4% | -19.6% | -8.68% | 82% |
| dip40_V2_gescreend_fail | 508 | 23% | 5.5% | +59.2% | -28.5% | -8.13% | 100% |
| dip40_V2_alle | 603 | 22% | 5.0% | +57.9% | -27.6% | -8.73% | 100% |
| dip40_V3_gescreend_pass | 82 | 8% | 1.2% | +57.1% | -21.1% | -14.41% | 92% |
| dip40_V3_gescreend_fail | 514 | 12% | 7.0% | +97.4% | -30.4% | -14.49% | 100% |
| dip40_V3_alle | 608 | 12% | 6.2% | +91.1% | -29.4% | -14.95% | 100% |
| dip45_V1_gescreend_pass | 74 | 16% | 2.7% | +44.4% | -14.9% | -5.25% | 70% |
| dip45_V1_gescreend_fail | 488 | 25% | 4.9% | +52.2% | -26.1% | -6.22% | 100% |
| dip45_V1_alle | 578 | 24% | 4.7% | +51.1% | -25.0% | -6.54% | 100% |
| dip45_V2_gescreend_pass | 73 | 20% | 2.7% | +42.8% | -18.6% | -5.96% | 71% |
| dip45_V2_gescreend_fail | 486 | 24% | 5.1% | +64.3% | -28.1% | -5.89% | 100% |
| dip45_V2_alle | 571 | 24% | 4.9% | +61.3% | -27.2% | -6.44% | 100% |
| dip45_V3_gescreend_pass | 74 | 8% | 2.7% | +108.1% | -19.8% | -9.47% | 88% |
| dip45_V3_gescreend_fail | 493 | 14% | 6.5% | +127.9% | -29.7% | -7.32% | 100% |
| dip45_V3_alle | 577 | 13% | 6.1% | +124.9% | -28.7% | -8.18% | 100% |

## Beste variant: dip45_V1_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 19:30:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:01,143 main INFO screen Elon pass=0 dev=0.0 ins=37.98 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 19:30:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:01,633 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:30:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:01,766 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:30:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:01,994 main INFO screen bullton pass=0 dev=0.0 ins=45.4 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 10 19:30:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:12,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:30:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:12,950 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:30:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:13,707 main INFO screen TSLA pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (2.2s)
Sep 10 19:30:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:16,353 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.4s)
Sep 10 19:30:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:16,837 main INFO screen FROG pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.2s)
Sep 10 19:30:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:23,645 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:30:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:23,812 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:30:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:30:23,975 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 19:31:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:10,359 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:31:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:10,441 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:31:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:10,961 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 10 19:31:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:20,945 main INFO screen Wokeflix pass=1 dev=0.0 ins=1.1 pro=51 1a=False 1b=False 2=False (3.3s)
Sep 10 19:31:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:41,833 main INFO screen FAG pass=0 dev=5.2 ins=0.68 pro=40 1a=False 1b=False 2=False (5.4s)
Sep 10 19:31:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:42,452 main INFO screen STOCK pass=0 dev=5.05 ins=4.51 pro=20 1a=False 1b=False 2=False (5.1s)
Sep 10 19:31:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:55,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:31:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:55,172 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:31:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:55,309 main INFO screen babe pass=0 dev=0.0 ins=39.94 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:31:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:31:58,236 main INFO screen CNS pass=0 dev=6.49 ins=1.08 pro=51 1a=False 1b=False 2=False (2.8s)
Sep 10 19:33:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:02,847 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:02,945 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:03,283 main INFO screen Vortex pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (0.5s)
Sep 10 19:33:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:04,106 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:33:04 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:33:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:22,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:22,790 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:22,973 main INFO screen Orus pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 19:33:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:23,049 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:23,138 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:23,306 main INFO screen MAGACOIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:33:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:26,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:26,646 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:26,815 main INFO screen chilljug pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 19:33:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:33,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:33,633 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:33,757 main INFO screen bullton pass=0 dev=0.0 ins=45.32 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 10 19:33:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:55,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:33:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:55,260 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:33:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:33:55,654 main INFO screen OCTOPUS pass=0 dev=0.0 ins=13.27 pro=14 1a=False 1b=False 2=True (0.6s)
Sep 10 19:34:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:34:31,050 main INFO screen DINO pass=0 dev=0.82 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 19:34:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:34:32,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:34:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:34:33,106 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:34:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:34:37,996 main INFO screen GSTAR pass=0 dev=1.76 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 10 19:34:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:34:38,521 main INFO screen AI pass=0 dev=0.0 ins=44.92 pro=2 1a=False 1b=False 2=True (5.6s)
Sep 10 19:35:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:00,826 main INFO screen USMS pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 19:35:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:13,886 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:35:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:13,971 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:35:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:14,187 main INFO screen WOLVERINE pass=0 dev=0.0 ins=78.65 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 19:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:23,692 main INFO screen NMU pass=1 dev=0.05 ins=0.35 pro=49 1a=False 1b=False 2=False (2.5s)
Sep 10 19:35:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:34,086 main INFO screen RSR pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 10 19:35:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:35,600 main INFO screen wind pass=0 dev=1.43 ins=0.0 pro=2 1a=False 1b=False 2=False (4.0s)
Sep 10 19:35:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:46,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:35:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:46,544 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:35:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:46,804 main INFO screen JUGGERNAUT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 19:35:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:46,972 main INFO screen Do Not Bu pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 10 19:35:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:54,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:35:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:55,016 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:35:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:35:55,140 main INFO screen VIBE pass=0 dev=0.0 ins=40.29 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:36:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:19,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:36:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:19,923 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:36:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:20,115 main INFO screen COLLECTIBLE pass=0 dev=0.0 ins=19.56 pro=22 1a=False 1b=False 2=True (0.4s)
Sep 10 19:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:26,567 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:26,840 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:36:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:27,316 main INFO screen XCAT pass=0 dev=0.0 ins=59.67 pro=1 1a=False 1b=False 2=True (1.1s)
Sep 10 19:36:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:28,322 main INFO screen DILLYS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 10 19:36:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:55,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:36:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:55,315 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:36:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:36:55,533 main INFO screen bullton pass=0 dev=0.0 ins=45.24 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 10 19:37:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:03,660 main INFO screen BTITS pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 10 19:37:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:21,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:37:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:21,144 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:37:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:21,311 main INFO screen DOOVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 10 19:37:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:32,099 main INFO screen OS pass=0 dev=13.27 ins=0.0 pro=8 1a=False 1b=False 2=False (1.9s)
Sep 10 19:37:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:49,676 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:37:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:49,755 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:37:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:37:49,967 main INFO screen ND4 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 19:38:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:38:03,995 main INFO screen Tiana pass=1 dev=0.0 ins=19.54 pro=20 1a=False 1b=False 2=False (1.4s)
Sep 10 19:38:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:38:08,583 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:38:08 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
