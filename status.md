# Schaduwbot status

- tijd: 2026-09-10 20:09:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 22 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 634/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 22861, "tokens_in_memory": 1579, "msgs": 4547747, "trades": 817677, "creates": 9224, "decode_fail": 63099, "rpc_calls": 13808, "rpc_errors": 1436, "sol_usd": 99.88244271803259, "open_positions": 96}
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
Sep 10 20:04:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:16,028 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:04:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:16,116 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:04:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:19,448 main INFO screen COTE pass=0 dev=0.0 ins=38.28 pro=6 1a=False 1b=False 2=True (3.5s)
Sep 10 20:04:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:28,763 main INFO screen MERUMP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 10 20:04:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:31,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:04:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:31,944 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:04:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:32,143 main INFO screen cashback pass=0 dev=0.0 ins=6.59 pro=25 1a=False 1b=False 2=True (0.4s)
Sep 10 20:04:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:38,312 main INFO screen CCAT pass=1 dev=0.0 ins=14.3 pro=34 1a=False 1b=False 2=False (3.6s)
Sep 10 20:04:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:40,811 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:04:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:40,941 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:04:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:04:46,648 main INFO screen DOLLY pass=0 dev=0.0 ins=36.24 pro=8 1a=False 1b=False 2=True (5.9s)
Sep 10 20:05:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:05:03,031 main INFO screen $NP pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (8.4s)
Sep 10 20:05:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:05:16,163 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:05:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:05:16,286 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:05:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:05:16,604 main INFO screen SEX pass=0 dev=0.0 ins=15.2 pro=42 1a=False 1b=False 2=True (0.5s)
Sep 10 20:05:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:05:33,715 main INFO screen $CAJUN pass=0 dev=0.51 ins=0.0 pro=3 1a=False 1b=False 2=False (7.0s)
Sep 10 20:06:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:21,052 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:06:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:21,160 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:06:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:24,642 main INFO screen TAYFA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.7s)
Sep 10 20:06:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:29,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:06:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:29,319 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:06:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:29,714 main INFO screen Tugi pass=0 dev=0.0 ins=11.66 pro=48 1a=False 1b=False 2=True (0.6s)
Sep 10 20:06:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:46,883 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:06:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:46,983 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:06:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:06:50,492 main INFO screen Tugi pass=0 dev=0.0 ins=36.1 pro=8 1a=False 1b=False 2=True (3.7s)
Sep 10 20:07:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:24,155 main INFO screen SBUS pass=0 dev=2.25 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 10 20:07:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:33,860 main INFO screen STW pass=1 dev=0.0 ins=19.24 pro=19 1a=False 1b=False 2=False (4.9s)
Sep 10 20:07:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:39,361 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:07:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:39,448 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:07:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:39,724 main INFO screen BACONAI pass=0 dev=0.0 ins=37.5 pro=5 1a=False 1b=False 2=True (0.5s)
Sep 10 20:07:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:41,033 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:07:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:41,181 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:07:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:41,588 main INFO screen DoGe pass=0 dev=0.0 ins=10.35 pro=20 1a=False 1b=False 2=True (0.6s)
Sep 10 20:07:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:46,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:07:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:47,060 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:07:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:07:51,371 main INFO screen $VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.5s)
Sep 10 20:08:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:05,661 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:08:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:05,746 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:08:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:08,237 main INFO screen PIXI pass=0 dev=0.18 ins=34.43 pro=6 1a=False 1b=False 2=True (9.3s)
Sep 10 20:08:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:10,090 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.5s)
Sep 10 20:08:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:17,274 main INFO screen SPY pass=1 dev=0.0 ins=0.0 pro=39 1a=False 1b=False 2=False (9.0s)
Sep 10 20:08:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:23,238 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:08:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:23,403 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:08:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:27,859 main INFO screen WOBBLE pass=0 dev=0.0 ins=37.98 pro=10 1a=False 1b=False 2=True (4.7s)
Sep 10 20:08:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:46,075 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:08:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:46,193 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:08:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:47,863 main INFO screen ORT pass=0 dev=8.47 ins=0.0 pro=4 1a=False 1b=False 2=False (6.0s)
Sep 10 20:08:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:48,609 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:08:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:48,729 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:08:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:50,829 main INFO screen HORACE pass=0 dev=0.0 ins=20.56 pro=11 1a=False 1b=False 2=True (4.8s)
Sep 10 20:08:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:08:54,136 main INFO screen HAT pass=0 dev=0.0 ins=77.81 pro=8 1a=False 1b=False 2=True (5.6s)
Sep 10 20:09:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:09:18,779 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:09:18 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
