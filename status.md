# Schaduwbot status

- tijd: 2026-09-10 19:27:41 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 hours, 40 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 614/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 20364, "tokens_in_memory": 1470, "msgs": 3933354, "trades": 706255, "creates": 8109, "decode_fail": 52466, "rpc_calls": 11787, "rpc_errors": 1233, "sol_usd": 99.95047528339174, "open_positions": 64}
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
Sep 10 19:17:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:18,628 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:17:18 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:17:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:21,153 main INFO screen Chester pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.8s)
Sep 10 19:17:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:46,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:17:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:46,330 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:17:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:51,581 main INFO screen lam pass=0 dev=0.0 ins=38.23 pro=3 1a=False 1b=False 2=True (5.4s)
Sep 10 19:18:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:00,735 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:18:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:00,812 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:18:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:08,169 main INFO screen BTCBST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.5s)
Sep 10 19:18:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:12,942 main INFO screen head pass=0 dev=0.41 ins=0.0 pro=2 1a=False 1b=False 2=True (6.0s)
Sep 10 19:18:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:16,876 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:18:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:17,001 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:18:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:20,508 main INFO screen DayTrader pass=0 dev=0.0 ins=43.42 pro=4 1a=False 1b=False 2=True (3.7s)
Sep 10 19:18:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:35,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:18:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:35,249 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:18:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:41,059 main INFO screen worker pass=0 dev=0.0 ins=78.23 pro=9 1a=False 1b=False 2=True (6.0s)
Sep 10 19:18:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:41,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:18:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:41,725 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:18:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:42,248 main INFO screen goldfish pass=0 dev=0.0 ins=16.69 pro=10 1a=False 1b=False 2=True (0.7s)
Sep 10 19:18:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:18:44,748 main INFO screen SHILL pass=1 dev=0.0 ins=18.74 pro=17 1a=False 1b=False 2=False (5.9s)
Sep 10 19:19:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:19:08,989 main INFO screen VOLVAN pass=0 dev=1.76 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 10 19:20:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:31,231 main INFO screen STRCOIN pass=0 dev=2.15 ins=0.0 pro=7 1a=False 1b=False 2=False (9.2s)
Sep 10 19:20:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:39,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:20:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:40,041 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:20:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:40,251 main INFO screen Mangos pass=0 dev=0.0 ins=26.86 pro=56 1a=False 1b=False 2=True (0.4s)
Sep 10 19:20:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:47,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:20:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:47,967 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:20:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:51,323 main INFO screen SONIC pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (3.6s)
Sep 10 19:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:58,316 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:20:58,453 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:21:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:21:03,646 main INFO screen Arata pass=0 dev=0.0 ins=43.97 pro=5 1a=False 1b=False 2=True (5.4s)
Sep 10 19:21:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:21:21,312 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:21:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:21:21,385 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:21:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:21:21,749 main INFO screen OpenStreet pass=0 dev=0.0 ins=16.22 pro=19 1a=False 1b=False 2=True (0.6s)
Sep 10 19:21:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:21:57,279 main INFO screen BLOCKFIELD pass=1 dev=5.0 ins=4.64 pro=13 1a=False 1b=False 2=False (6.4s)
Sep 10 19:22:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:01,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:22:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:01,244 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:22:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:08,220 main INFO screen VANGOGE pass=0 dev=0.0 ins=37.77 pro=10 1a=False 1b=False 2=True (7.2s)
Sep 10 19:22:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:13,396 main INFO screen piggy pass=0 dev=0.0 ins=24.89 pro=19 1a=False 1b=False 2=False (6.3s)
Sep 10 19:22:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:18,119 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:22:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:18,290 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:22:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:24,396 main INFO screen Apple pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 10 19:22:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:22:37,044 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:22:37 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:23:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:02,307 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:23:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:02,410 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:23:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:05,830 main INFO screen イイヨ pass=1 dev=0.0 ins=1.19 pro=28 1a=False 1b=False 2=False (3.6s)
Sep 10 19:23:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:09,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:23:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:09,704 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:23:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:13,570 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 10 19:23:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:21,971 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:23:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:22,139 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:23:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:23:28,099 main INFO screen GAE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (6.2s)
Sep 10 19:24:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:07,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:24:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:07,871 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:24:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:08,007 main INFO screen イイヨ pass=0 dev=0.0 ins=24.02 pro=9 1a=False 1b=False 2=True (0.5s)
Sep 10 19:24:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:21,556 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:24:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:21,681 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:24:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:27,448 main INFO screen ROBINDOG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 10 19:24:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:37,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:24:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:37,646 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:24:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:37,945 main INFO screen イイヨ pass=0 dev=0.0 ins=16.66 pro=27 1a=False 1b=False 2=True (0.5s)
Sep 10 19:24:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:24:52,626 main INFO screen MOON67 pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (8.9s)
Sep 10 19:25:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:03,252 main INFO screen Space Boy pass=0 dev=0.2 ins=0.0 pro=4 1a=False 1b=False 2=False (8.8s)
Sep 10 19:25:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:16,783 main INFO screen SAPIENS pass=0 dev=0.35 ins=31.85 pro=17 1a=False 1b=False 2=True (10.5s)
Sep 10 19:25:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:22,524 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.6s)
Sep 10 19:25:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:32,678 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:25:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:32,756 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:25:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:32,918 main INFO screen stockdog pass=0 dev=0.0 ins=31.11 pro=15 1a=False 1b=False 2=True (0.4s)
Sep 10 19:25:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:25:51,946 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 10 19:26:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:07,656 main INFO screen Minik pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 10 19:26:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:25,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:26:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:25,588 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:26:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:29,559 main INFO screen GIGAORC pass=0 dev=0.0 ins=37.56 pro=1 1a=False 1b=False 2=True (4.2s)
Sep 10 19:26:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:32,453 main INFO screen WELL pass=0 dev=10.0 ins=17.45 pro=20 1a=False 1b=False 2=False (1.5s)
Sep 10 19:26:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:40,462 main INFO screen FROG pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 10 19:26:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:54,388 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:26:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:26:54,439 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:27:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:27:00,006 main INFO screen bullton pass=0 dev=0.0 ins=45.88 pro=5 1a=False 1b=False 2=True (5.7s)
Sep 10 19:27:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:27:39,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:27:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:27:40,009 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:27:41,191 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:27:41 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
