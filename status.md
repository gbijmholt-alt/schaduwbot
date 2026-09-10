# Schaduwbot status

- tijd: 2026-09-10 20:04:09 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 17 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 620/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 22552, "tokens_in_memory": 1566, "msgs": 4460195, "trades": 803188, "creates": 9097, "decode_fail": 62271, "rpc_calls": 13590, "rpc_errors": 1408, "sol_usd": 99.6550230357704, "open_positions": 103}
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
Sep 10 19:54:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:07,601 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:54:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:07,695 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:54:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:07,882 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 19:54:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:21,284 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 10 19:54:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:21,661 main INFO screen $CAJUN pass=0 dev=0.3 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 10 19:54:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:25,087 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:54:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:25,442 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:54:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:25,671 main INFO screen BUGS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.0s)
Sep 10 19:54:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:54:25,970 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 10 19:55:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:08,128 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:55:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:08,670 main INFO screen Ty pass=0 dev=3.43 ins=0.0 pro=3 1a=False 1b=False 2=True (0.7s)
Sep 10 19:55:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:08,745 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 10 19:55:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:45,527 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:55:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:45,904 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:55:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:46,352 main INFO screen TURBO pass=0 dev=0.0 ins=26.78 pro=24 1a=False 1b=False 2=True (1.0s)
Sep 10 19:55:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:48,411 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 10 19:55:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:49,405 main INFO screen LMAO pass=0 dev=2.09 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 10 19:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:53,590 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:53,726 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:55:53,849 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:56:30,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:56:30,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:56:30,867 main INFO screen MOODY pass=0 dev=0.0 ins=37.77 pro=13 1a=False 1b=False 2=True (0.8s)
Sep 10 19:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:56:30,950 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 19:57:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:05,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:57:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:05,555 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:57:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:05,830 main INFO screen CooK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 10 19:57:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:12,548 main INFO screen TripleD pass=1 dev=0.0 ins=17.78 pro=10 1a=False 1b=False 2=False (1.4s)
Sep 10 19:57:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:18,560 main INFO screen ELAWN pass=0 dev=1.05 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 10 19:57:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:34,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:57:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:34,562 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:57:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:34,752 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 19:57:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:44,055 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:57:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:44,173 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:57:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:44,374 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 19:57:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:50,238 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:57:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:50,329 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:57:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:50,482 main INFO screen TSLA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 19:57:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:53,201 main INFO screen BUGS pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 10 19:57:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:57:59,267 main INFO screen CODEXAI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 10 19:58:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:02,647 main INFO screen $FXTS KI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 10 19:58:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:03,651 main INFO screen $CAJUN pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 10 19:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:12,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:12,205 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:12,337 main INFO screen JOLT pass=0 dev=0.0 ins=20.47 pro=5 1a=False 1b=False 2=True (0.3s)
Sep 10 19:58:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:20,964 main INFO screen GXT pass=0 dev=5.05 ins=0.79 pro=8 1a=False 1b=False 2=False (2.1s)
Sep 10 19:58:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:25,370 main INFO screen CODEXAI pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 10 19:58:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:40,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:58:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:40,154 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:58:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:40,278 main INFO screen GS pass=0 dev=0.0 ins=21.35 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 10 19:58:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:50,263 main INFO screen CooK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 19:58:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:56,580 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:58:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:56,704 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:58:57,708 main INFO screen Easy  pass=0 dev=0.0 ins=55.0 pro=4 1a=False 1b=False 2=True (1.2s)
Sep 10 19:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:59:02,416 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:59:02 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 10 19:59:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:59:13,234 main INFO screen RISE pass=0 dev=36.91 ins=0.0 pro=13 1a=False 1b=False 2=False (2.0s)
Sep 10 19:59:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:59:41,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:59:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:59:41,800 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:59:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:59:41,996 main INFO screen CARRY pass=1 dev=0.0 ins=0.73 pro=21 1a=False 1b=False 2=False (0.4s)
Sep 10 20:00:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:00:28,766 main INFO screen ELAWN pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=True (5.7s)
Sep 10 20:00:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:00:45,092 main INFO screen Harvest pass=0 dev=0.0 ins=31.85 pro=15 1a=False 1b=False 2=True (10.0s)
Sep 10 20:01:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:01:07,664 main INFO screen 15911 pass=1 dev=0.53 ins=0.0 pro=47 1a=False 1b=False 2=False (7.3s)
Sep 10 20:01:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:01:36,286 main INFO screen up pass=0 dev=0.31 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 10 20:01:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:01:58,192 main INFO screen $HORMUZ pass=0 dev=3.42 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 10 20:02:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:02:04,038 main INFO screen HM pass=0 dev=0.0 ins=17.35 pro=68 1a=False 1b=False 2=True (7.0s)
Sep 10 20:03:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:05,905 main INFO screen 3M pass=0 dev=0.0 ins=25.71 pro=24 1a=False 1b=False 2=False (1.7s)
Sep 10 20:03:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:20,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:03:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:20,283 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:03:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:22,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:03:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:22,484 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:03:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:27,354 main INFO screen lam pass=0 dev=6.63 ins=18.91 pro=25 1a=False 1b=False 2=False (8.4s)
Sep 10 20:03:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:27,394 main INFO screen COTE pass=0 dev=0.0 ins=40.12 pro=7 1a=False 1b=False 2=True (7.7s)
Sep 10 20:03:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:28,709 main INFO screen LGBTQ pass=0 dev=0.0 ins=19.01 pro=17 1a=False 1b=False 2=True (6.4s)
Sep 10 20:03:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:45,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:03:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:45,248 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:03:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:45,604 main INFO screen CbCat pass=0 dev=0.0 ins=18.06 pro=11 1a=False 1b=False 2=True (0.6s)
Sep 10 20:03:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:51,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:03:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:51,765 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:03:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:03:52,053 main INFO screen SEXI pass=0 dev=0.0 ins=13.93 pro=18 1a=False 1b=False 2=True (0.5s)
Sep 10 20:04:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:09,102 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:04:09 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
