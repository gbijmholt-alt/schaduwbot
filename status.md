# Schaduwbot status

- tijd: 2026-09-10 19:53:48 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 6 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 629/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 21931, "tokens_in_memory": 1546, "msgs": 4326221, "trades": 780967, "creates": 8809, "decode_fail": 59700, "rpc_calls": 13098, "rpc_errors": 1373, "sol_usd": 99.65589969549339, "open_positions": 108}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 19:48 UTC

Gelogde schaduwtrades: **6731**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 8656 | 1215 | 26 | 1215 | 123 | 2270 | 6731 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 101 | 13% | 1.0% | +34.6% | -15.7% | -9.22% | 86% |
| dip35_V1_gescreend_fail | 654 | 26% | 4.1% | +45.1% | -26.2% | -7.75% | 100% |
| dip35_V1_alle | 784 | 24% | 4.0% | +43.3% | -25.2% | -8.48% | 100% |
| dip35_V2_gescreend_pass | 100 | 15% | 1.0% | +31.0% | -20.6% | -12.85% | 94% |
| dip35_V2_gescreend_fail | 652 | 24% | 4.8% | +55.6% | -28.0% | -8.37% | 100% |
| dip35_V2_alle | 775 | 22% | 4.5% | +52.3% | -27.4% | -9.61% | 100% |
| dip35_V3_gescreend_pass | 101 | 5% | 1.0% | +75.2% | -22.2% | -17.36% | 98% |
| dip35_V3_gescreend_fail | 664 | 13% | 5.7% | +91.4% | -29.4% | -14.14% | 100% |
| dip35_V3_alle | 786 | 12% | 5.3% | +87.0% | -28.8% | -15.12% | 100% |
| dip40_V1_gescreend_pass | 92 | 15% | 1.1% | +43.2% | -14.3% | -5.54% | 73% |
| dip40_V1_gescreend_fail | 642 | 25% | 4.7% | +49.0% | -26.4% | -7.41% | 100% |
| dip40_V1_alle | 755 | 24% | 4.2% | +47.5% | -25.2% | -7.45% | 100% |
| dip40_V2_gescreend_pass | 91 | 13% | 1.1% | +54.4% | -19.6% | -9.88% | 88% |
| dip40_V2_gescreend_fail | 639 | 24% | 5.0% | +58.5% | -28.6% | -7.64% | 100% |
| dip40_V2_alle | 745 | 23% | 4.6% | +57.2% | -27.7% | -8.32% | 100% |
| dip40_V3_gescreend_pass | 92 | 8% | 1.1% | +57.1% | -21.1% | -15.15% | 95% |
| dip40_V3_gescreend_fail | 651 | 13% | 6.1% | +89.9% | -30.2% | -14.66% | 100% |
| dip40_V3_alle | 756 | 12% | 5.6% | +84.9% | -29.3% | -15.06% | 100% |
| dip45_V1_gescreend_pass | 82 | 15% | 2.4% | +44.4% | -14.8% | -6.12% | 76% |
| dip45_V1_gescreend_fail | 615 | 26% | 4.2% | +51.2% | -26.3% | -5.98% | 100% |
| dip45_V1_alle | 714 | 25% | 4.1% | +50.2% | -25.1% | -6.34% | 100% |
| dip45_V2_gescreend_pass | 81 | 18% | 2.5% | +42.8% | -18.6% | -7.27% | 79% |
| dip45_V2_gescreend_fail | 611 | 25% | 4.6% | +66.5% | -28.2% | -4.61% | 100% |
| dip45_V2_alle | 705 | 24% | 4.4% | +63.6% | -27.3% | -5.36% | 100% |
| dip45_V3_gescreend_pass | 82 | 7% | 2.4% | +108.1% | -19.8% | -10.41% | 91% |
| dip45_V3_gescreend_fail | 618 | 14% | 5.7% | +118.4% | -29.5% | -8.94% | 100% |
| dip45_V3_alle | 711 | 13% | 5.3% | +115.4% | -28.6% | -9.53% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 19:46:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:46:58,774 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:46:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:46:58,871 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:46:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:46:59,161 main INFO screen SEXI pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (0.5s)
Sep 10 19:47:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:04,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:47:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:04,759 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:05,067 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 10 19:47:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:08,029 main INFO screen APEZCAT pass=0 dev=22.55 ins=1.63 pro=43 1a=False 1b=False 2=False (3.7s)
Sep 10 19:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:51,329 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:51,585 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:51,785 main INFO screen Influencer pass=0 dev=0.0 ins=26.02 pro=46 1a=False 1b=False 2=True (0.7s)
Sep 10 19:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:51,999 main INFO screen CHAROC pass=0 dev=3.39 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 10 19:47:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:47:59,922 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:48:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:48:00,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:48:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:48:00,178 main INFO screen PULLIT pass=0 dev=0.0 ins=0.07 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 19:49:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:02,595 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:49:02 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:49:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:08,527 main INFO screen grower pass=0 dev=0.0 ins=13.42 pro=75 1a=False 1b=False 2=True (6.0s)
Sep 10 19:49:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:09,680 main INFO screen CCOM pass=1 dev=3.46 ins=15.83 pro=18 1a=False 1b=False 2=False (6.8s)
Sep 10 19:49:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:09,878 main INFO screen COMMODITY pass=0 dev=0.0 ins=8.91 pro=71 1a=False 1b=False 2=True (7.3s)
Sep 10 19:49:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:11,281 main INFO screen ROBIN pass=0 dev=0.18 ins=78.49 pro=8 1a=False 1b=True 2=True (2.8s)
Sep 10 19:49:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:18,058 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 10 19:49:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:18,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:18,801 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:19,442 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 10 19:49:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:20,850 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (11.0s)
Sep 10 19:49:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:21,662 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:21,831 main INFO screen S&P500 pass=0 dev=0.0 ins=33.93 pro=40 1a=False 1b=False 2=True (12.2s)
Sep 10 19:49:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:21,946 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:22,074 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:22,193 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:22,307 main INFO screen Rasmr pass=0 dev=0.0 ins=33.91 pro=0 1a=False 1b=False 2=True (0.8s)
Sep 10 19:49:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:22,509 main INFO screen PULLIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.9s)
Sep 10 19:49:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:28,352 main INFO screen 🚀 pass=0 dev=0.48 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 10 19:49:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:33,870 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:33,946 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:34,106 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 19:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:42,010 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:42,140 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:42,290 main INFO screen JUGSEM pass=0 dev=0.0 ins=79.04 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 10 19:49:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:43,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:49:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:43,982 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:49:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:44,179 main INFO screen lam pass=0 dev=0.0 ins=20.65 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 19:49:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:49:44,528 main INFO screen PUMPY pass=0 dev=0.0 ins=24.67 pro=20 1a=False 1b=False 2=False (1.8s)
Sep 10 19:50:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:02,506 main INFO screen $PENGU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 10 19:50:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:33,395 main INFO screen CNUT pass=0 dev=0.0 ins=24.51 pro=16 1a=False 1b=False 2=False (1.5s)
Sep 10 19:50:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:34,587 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:50:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:34,757 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:50:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:34,958 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 19:50:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:37,324 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:50:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:37,489 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:50:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:37,615 main INFO screen CNUT pass=0 dev=0.0 ins=20.59 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 10 19:50:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:40,999 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:50:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:41,120 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:50:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:41,440 main INFO screen CNUT pass=0 dev=0.0 ins=20.13 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 10 19:50:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:50:48,823 main INFO screen BUGS pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=True (2.2s)
Sep 10 19:51:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:05,958 main INFO screen HALH pass=0 dev=6.56 ins=0.0 pro=2 1a=False 1b=False 2=True (1.9s)
Sep 10 19:51:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:21,444 main INFO screen WthCoin pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 10 19:51:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:40,245 main INFO screen 🚀 pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 19:51:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:44,236 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:51:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:44,354 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:51:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:45,635 main INFO screen invest pass=0 dev=0.0 ins=18.92 pro=13 1a=False 1b=False 2=True (1.5s)
Sep 10 19:51:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:57,424 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:51:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:57,804 main INFO screen OKGO pass=0 dev=0.34 ins=0.0 pro=3 1a=False 1b=False 2=False (4.4s)
Sep 10 19:51:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:58,033 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:51:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:58,596 main INFO screen OTC pass=0 dev=0.0 ins=21.16 pro=20 1a=False 1b=False 2=True (1.9s)
Sep 10 19:51:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:51:59,481 main INFO screen VYNE pass=0 dev=0.11 ins=0.0 pro=46 1a=False 1b=False 2=True (5.1s)
Sep 10 19:52:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:52:19,484 main INFO screen 34% pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 10 19:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:12,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:12,337 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:12,573 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 10 19:53:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:14,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:53:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:14,560 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:53:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:14,696 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:53:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:39,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:53:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:39,742 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:53:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:39,928 main INFO screen CNUT pass=0 dev=0.0 ins=20.62 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 10 19:53:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:40,487 main INFO screen SSF pass=0 dev=20.1 ins=0.0 pro=11 1a=False 1b=True 2=False (2.4s)
Sep 10 19:53:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:42,052 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:53:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:42,179 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:53:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:42,322 main INFO screen MEWZ pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:53:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:53:48,444 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:53:48 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
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
