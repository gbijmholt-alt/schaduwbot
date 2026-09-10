# Schaduwbot status

- tijd: 2026-09-10 20:35:00 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 48 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 635/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 24403, "tokens_in_memory": 1579, "msgs": 5012278, "trades": 887480, "creates": 9885, "decode_fail": 67871, "rpc_calls": 14844, "rpc_errors": 1533, "sol_usd": 100.02661899321235, "open_positions": 109}
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
Sep 10 20:25:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:24,701 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:25:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:28,854 main INFO screen CATEPULT pass=0 dev=0.0 ins=38.28 pro=5 1a=False 1b=False 2=True (4.3s)
Sep 10 20:25:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:43,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:25:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:43,977 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:25:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:44,417 main INFO screen MEME pass=0 dev=0.0 ins=16.22 pro=27 1a=False 1b=False 2=True (0.6s)
Sep 10 20:25:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:44,468 main INFO screen $PINT pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 10 20:25:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:44,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:25:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:45,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:25:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:25:51,717 main INFO screen CATEPULT pass=0 dev=0.0 ins=48.86 pro=18 1a=False 1b=False 2=True (6.9s)
Sep 10 20:26:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:16,137 main INFO screen mert pass=1 dev=0.0 ins=17.4 pro=13 1a=False 1b=False 2=False (5.3s)
Sep 10 20:26:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:24,057 main INFO screen Emerald pass=0 dev=0.96 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 10 20:26:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:45,174 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:26:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:45,272 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:26:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:45,656 main INFO screen WENDY pass=0 dev=0.0 ins=15.12 pro=19 1a=False 1b=False 2=True (0.6s)
Sep 10 20:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:47,827 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:20:26:47 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 20:26:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:26:59,656 main INFO screen mert pass=1 dev=0.0 ins=18.85 pro=10 1a=False 1b=False 2=False (4.5s)
Sep 10 20:27:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:00,906 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 10 20:27:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:13,573 main INFO screen FIX6900 pass=0 dev=0.0 ins=13.1 pro=69 1a=False 1b=False 2=True (4.5s)
Sep 10 20:27:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:15,692 main INFO screen BATON pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 10 20:27:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:22,289 main INFO screen $CAJUN pass=0 dev=0.95 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 10 20:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:41,887 main INFO screen RECRUIT pass=1 dev=0.18 ins=0.0 pro=25 1a=False 1b=False 2=False (9.4s)
Sep 10 20:27:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:44,948 main INFO screen HODL pass=0 dev=0.15 ins=10.98 pro=21 1a=False 1b=False 2=True (6.1s)
Sep 10 20:27:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:59,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:27:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:27:59,693 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:28:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:00,073 main INFO screen Bracat pass=1 dev=0.0 ins=10.14 pro=20 1a=False 1b=False 2=False (0.6s)
Sep 10 20:28:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:10,905 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:28:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:11,034 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:28:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:11,329 main INFO screen WENDY pass=0 dev=0.0 ins=16.83 pro=18 1a=False 1b=False 2=True (0.5s)
Sep 10 20:28:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:39,781 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:28:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:39,821 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:28:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:40,061 main INFO screen WENDY pass=1 dev=0.0 ins=0.37 pro=29 1a=False 1b=False 2=False (0.4s)
Sep 10 20:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:46,762 main INFO screen ACate pass=0 dev=0.96 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 20:28:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:28:49,539 main INFO screen trigg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 10 20:29:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:05,710 main INFO screen Bracat pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 10 20:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:37,213 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:37,311 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:37,816 main INFO screen Memefactory pass=0 dev=0.0 ins=13.27 pro=17 1a=False 1b=False 2=True (0.7s)
Sep 10 20:29:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:38,409 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:29:38 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 20:29:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:40,698 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:29:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:40,812 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:29:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:40,978 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 20:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:44,872 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:29:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:45,000 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:29:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:45,129 main INFO screen 9/11 pass=0 dev=0.0 ins=35.6 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 10 20:29:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:59,670 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:29:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:59,801 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:29:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:29:59,921 main INFO screen XRP pass=0 dev=0.0 ins=18.24 pro=20 1a=False 1b=False 2=True (0.3s)
Sep 10 20:30:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:30:01,717 main INFO screen $AURA pass=0 dev=6.73 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 10 20:30:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:30:10,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:30:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:30:10,290 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:30:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:30:10,419 main INFO screen MASTERCOIN pass=1 dev=0.0 ins=14.67 pro=21 1a=False 1b=False 2=False (0.3s)
Sep 10 20:30:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:30:38,137 main INFO screen MASTERCOIN pass=0 dev=6.63 ins=16.83 pro=19 1a=False 1b=False 2=False (1.3s)
Sep 10 20:31:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:31:17,710 main INFO screen MOP pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (1.8s)
Sep 10 20:31:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:31:40,872 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:31:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:31:41,084 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:31:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:31:41,220 main INFO screen $Pengu pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 20:32:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:32:32,774 main INFO screen OPEC pass=0 dev=17.7 ins=0.0 pro=10 1a=False 1b=False 2=False (2.6s)
Sep 10 20:32:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:32:40,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:32:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:32:40,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:32:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:32:40,388 main INFO screen ALBO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 20:32:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:32:51,596 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 10 20:33:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:02,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:33:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:02,843 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:33:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:02,985 main INFO screen 9/11 pass=0 dev=0.0 ins=36.06 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 10 20:33:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:07,955 main INFO screen Bracat pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 10 20:33:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:33:24,960 main INFO screen STOCKDOG pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
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
