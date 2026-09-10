# Schaduwbot status

- tijd: 2026-09-10 20:45:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 58 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 639/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 25040, "tokens_in_memory": 1544, "msgs": 5101040, "trades": 910025, "creates": 10131, "decode_fail": 69583, "rpc_calls": 15236, "rpc_errors": 1563, "sol_usd": 100.06852972294494, "open_positions": 89}
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
Sep 10 20:33:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:31,755 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:33:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:31,952 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:33:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:32,057 main INFO screen Bigduck pass=0 dev=0.0 ins=37.98 pro=14 1a=False 1b=False 2=True (0.3s)
Sep 10 20:33:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:38,304 main INFO screen $DEMP pass=0 dev=0.13 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 20:34:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:01,287 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:34:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:01,378 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:34:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:01,572 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 20:34:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:21,694 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:34:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:21,784 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:34:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:21,959 main INFO screen CATEPULT pass=0 dev=0.0 ins=38.26 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 10 20:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:40,764 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:40,856 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:34:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:34:41,044 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 20:35:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:00,587 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:35:00 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 20:35:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:20,139 main INFO screen STOCKDOG pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=True (2.1s)
Sep 10 20:35:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:25,743 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:35:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:25,868 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:35:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:26,122 main INFO screen CATEPULT pass=0 dev=0.0 ins=38.27 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 10 20:35:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:36,738 main INFO screen Btc pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (2.6s)
Sep 10 20:35:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:41,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:35:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:41,558 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:35:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:41,685 main INFO screen MINIJUG pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 10 20:35:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:35:54,224 main INFO screen EMOAN pass=0 dev=0.7 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 10 20:36:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:32,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:36:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:32,515 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:36:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:32,706 main INFO screen NEEGY pass=0 dev=0.0 ins=79.04 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 20:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:42,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:42,150 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:42,275 main INFO screen LONG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 20:36:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:36:59,683 main INFO screen FLIH pass=0 dev=0.06 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 10 20:37:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:37:25,771 main INFO screen Justice  pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=True (1.8s)
Sep 10 20:38:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:15,964 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:38:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:16,059 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:38:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:16,249 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.4s)
Sep 10 20:38:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:48,720 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:38:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:48,804 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:38:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:52,245 main INFO screen CEO pass=0 dev=0.0 ins=21.48 pro=14 1a=False 1b=False 2=True (3.6s)
Sep 10 20:38:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:38:55,083 main INFO screen Balls pass=1 dev=0.57 ins=0.0 pro=43 1a=False 1b=False 2=False (3.5s)
Sep 10 20:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:02,466 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 10 20:39:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:21,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:39:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:21,419 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:39:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:21,683 main INFO screen FCOIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 20:39:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:26,830 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:39:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:26,959 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:39:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:27,077 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 20:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:31,411 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:31,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:31,663 main INFO screen BINX pass=1 dev=0.0 ins=9.9 pro=12 1a=False 1b=False 2=False (0.3s)
Sep 10 20:39:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:39:59,388 main INFO screen ALBO pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 20:40:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:12,811 aiohttp.access INFO 195.182.16.23 [10/Sep/2026:20:40:12 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 10 20:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:17,377 main INFO screen window pass=0 dev=0.33 ins=0.0 pro=7 1a=False 1b=False 2=False (3.8s)
Sep 10 20:40:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:24,742 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:40:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:24,857 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:40:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:24,986 main INFO screen DREGG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 20:40:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:32,481 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:40:32 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 20:40:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:53,439 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:40:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:40:53,547 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:41:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:13,291 main INFO screen milky pass=0 dev=0.56 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 10 20:41:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:13,885 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 10 20:41:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:20,160 main INFO screen ROI pass=0 dev=0.0 ins=36.19 pro=7 1a=False 1b=False 2=True (26.8s)
Sep 10 20:41:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:21,772 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:41:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:21,897 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:41:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:22,065 main INFO screen Hedge pass=0 dev=0.0 ins=36.07 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 10 20:41:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:25,326 main INFO screen catjak pass=1 dev=0.0 ins=18.07 pro=16 1a=False 1b=False 2=False (1.9s)
Sep 10 20:41:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:47,093 main INFO screen wifout pass=0 dev=0.0 ins=15.93 pro=48 1a=False 1b=False 2=True (4.0s)
Sep 10 20:41:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:41:48,014 main INFO screen Black pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 10 20:42:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:42:30,646 main INFO screen Rocketman pass=0 dev=0.0 ins=19.55 pro=8 1a=False 1b=False 2=False (10.7s)
Sep 10 20:42:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:42:38,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:42:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:42:38,455 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:42:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:42:38,617 main INFO screen SOL CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.3s)
Sep 10 20:43:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:16,412 main INFO screen $CAJUN pass=0 dev=0.65 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 10 20:43:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:31,706 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:43:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:31,806 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:43:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:32,034 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 20:43:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:49,055 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:43:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:49,148 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:43:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:43:49,484 main INFO screen BOING pass=0 dev=0.0 ins=11.28 pro=23 1a=False 1b=False 2=True (0.5s)
Sep 10 20:44:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:44:27,942 main INFO screen MUSKRAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (3.0s)
Sep 10 20:45:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:45:06,152 main INFO screen BINX pass=1 dev=0.0 ins=12.18 pro=36 1a=False 1b=False 2=False (3.7s)
Sep 10 20:45:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:45:37,086 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:45:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
