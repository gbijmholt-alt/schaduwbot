# Schaduwbot status

- tijd: 2026-09-11 18:22:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 4 hours, 35 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.8G/38G | geheugen: 896/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 30762, "tokens_in_memory": 7703, "msgs": 3858557, "trades": 935916, "creates": 9961, "decode_fail": 67767, "rpc_calls": 17717, "rpc_errors": 1492, "sol_usd": 101.36473248297698, "open_positions": 83, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 17:49 UTC

Gelogde schaduwtrades: **28037**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 20025 | 2920 | 31 | 2920 | 211 | 5313 | 15682 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 309 | 16% | 1.9% | +42.2% | -16.3% | -6.68% | 99% |
| dip35_V1_gescreend_fail | 2833 | 27% | 3.7% | +46.2% | -25.9% | -6.51% | 100% |
| dip35_V1_alle | 3241 | 26% | 3.8% | +45.5% | -25.2% | -6.75% | 100% |
| dip35_V2_gescreend_pass | 308 | 19% | 2.6% | +45.8% | -21.3% | -8.47% | 100% |
| dip35_V2_gescreend_fail | 2837 | 25% | 4.4% | +56.3% | -28.2% | -7.39% | 100% |
| dip35_V2_alle | 3218 | 24% | 4.4% | +54.9% | -27.8% | -7.91% | 100% |
| dip35_V3_gescreend_pass | 309 | 8% | 2.9% | +121.7% | -22.8% | -11.55% | 100% |
| dip35_V3_gescreend_fail | 2876 | 13% | 6.1% | +104.3% | -29.8% | -11.99% | 100% |
| dip35_V3_alle | 3253 | 13% | 6.0% | +102.8% | -29.3% | -12.30% | 100% |
| dip40_V1_gescreend_pass | 285 | 15% | 1.8% | +47.6% | -15.5% | -6.19% | 99% |
| dip40_V1_gescreend_fail | 2752 | 26% | 3.7% | +48.0% | -25.9% | -6.42% | 100% |
| dip40_V1_alle | 3115 | 26% | 3.7% | +47.7% | -25.1% | -6.54% | 100% |
| dip40_V2_gescreend_pass | 284 | 14% | 2.5% | +52.7% | -19.9% | -9.45% | 100% |
| dip40_V2_gescreend_fail | 2749 | 25% | 4.1% | +55.2% | -28.1% | -7.53% | 100% |
| dip40_V2_alle | 3089 | 24% | 4.2% | +54.8% | -27.5% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 286 | 7% | 2.4% | +100.2% | -21.2% | -13.13% | 100% |
| dip40_V3_gescreend_fail | 2787 | 13% | 5.8% | +91.9% | -29.6% | -13.93% | 100% |
| dip40_V3_alle | 3125 | 12% | 5.7% | +90.9% | -29.0% | -14.17% | 100% |
| dip45_V1_gescreend_pass | 272 | 15% | 1.5% | +53.0% | -15.1% | -4.61% | 98% |
| dip45_V1_gescreend_fail | 2680 | 27% | 3.3% | +49.4% | -25.6% | -5.24% | 100% |
| dip45_V1_alle | 3009 | 26% | 3.3% | +49.4% | -24.8% | -5.40% | 100% |
| dip45_V2_gescreend_pass | 270 | 18% | 2.2% | +50.5% | -19.3% | -6.88% | 99% |
| dip45_V2_gescreend_fail | 2664 | 25% | 3.8% | +58.9% | -27.6% | -6.26% | 100% |
| dip45_V2_alle | 2979 | 24% | 3.8% | +58.1% | -27.0% | -6.68% | 100% |
| dip45_V3_gescreend_pass | 272 | 7% | 2.2% | +155.9% | -20.3% | -7.98% | 100% |
| dip45_V3_gescreend_fail | 2695 | 14% | 5.5% | +105.2% | -29.1% | -10.75% | 100% |
| dip45_V3_alle | 3008 | 13% | 5.4% | +106.2% | -28.5% | -10.79% | 100% |

## Beste variant: dip45_V1_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2058 | 13% | 2.8% | -9.55% | 100% |
| zonder_xlink | 537 | 16% | 0.0% | -3.85% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 18:10:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:10:55,886 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:11:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:00,169 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 11 18:11:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:02,042 main INFO screen VOID pass=0 dev=0.0 ins=77.48 pro=8 1a=False 1b=False 2=True (6.4s)
Sep 11 18:11:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:06,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:11:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:06,949 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:11:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:12,466 main INFO screen LQX pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 18:11:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:35,523 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:11:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:35,626 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:11:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:41,950 main INFO screen $TRUMPMOON pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (5.6s)
Sep 11 18:11:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:42,001 main INFO screen SNAPCAT pass=1 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (6.6s)
Sep 11 18:11:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:42,186 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:11:42 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 18:11:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:11:54,235 main INFO screen FRUITPAD pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (9.6s)
Sep 11 18:12:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:38,371 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:12:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:38,458 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:12:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:45,786 main INFO screen Stunk pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (7.5s)
Sep 11 18:12:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:55,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:12:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:55,642 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:12:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:12:56,809 main INFO screen MEMES pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (1.4s)
Sep 11 18:13:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:03,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:13:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:03,595 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:13:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:03,937 aiohttp.access INFO 147.185.132.114 [11/Sep/2026:18:13:03 +0000] "GET / HTTP/1.0" 404 174 "-" "Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity"
Sep 11 18:13:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:04,146 main INFO screen MEMESTOCK pass=0 dev=0.0 ins=17.54 pro=7 1a=False 1b=False 2=True (1.1s)
Sep 11 18:13:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:12,136 main INFO screen vrl pass=0 dev=2.31 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 11 18:13:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:15,312 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.3s)
Sep 11 18:13:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:18,546 main INFO screen Cap pass=0 dev=0.22 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 18:13:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:24,879 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:13:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:25,008 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:13:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:29,295 main INFO screen FRUITPAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.1s)
Sep 11 18:13:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:31,717 main INFO screen MEMESTOCK pass=0 dev=0.0 ins=12.7 pro=5 1a=False 1b=False 2=True (6.9s)
Sep 11 18:13:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:40,159 main INFO screen hamster pass=0 dev=2.2 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 11 18:13:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:43,623 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:13:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:43,807 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:13:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:44,105 main INFO screen MEMESTOCK pass=0 dev=0.0 ins=17.05 pro=17 1a=False 1b=False 2=True (0.5s)
Sep 11 18:13:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:45,185 main INFO screen beer pass=0 dev=1.22 ins=0.0 pro=4 1a=False 1b=False 2=False (8.7s)
Sep 11 18:13:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:51,244 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:13:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:51,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:13:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:51,723 main INFO screen MEMESTOCK pass=0 dev=0.0 ins=8.14 pro=10 1a=False 1b=False 2=True (0.6s)
Sep 11 18:13:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:53,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:13:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:54,067 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:13:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:57,900 main INFO screen WCCF pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 11 18:13:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:13:59,604 main INFO screen TWENTowers pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 18:14:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:14:53,733 main INFO screen beer pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 18:15:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:02,463 main INFO screen snap pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 18:15:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:34,858 main INFO screen Vmaxsolana pass=0 dev=1.77 ins=23.39 pro=35 1a=False 1b=True 2=False (8.7s)
Sep 11 18:15:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:46,039 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:15:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:46,089 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:15:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:51,989 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.1s)
Sep 11 18:15:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:15:57,805 main INFO screen 100 pass=0 dev=9.66 ins=0.0 pro=2 1a=False 1b=False 2=True (7.6s)
Sep 11 18:16:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:16:37,842 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:16:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:16:38,020 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:16:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:16:38,156 main INFO screen NASDOG pass=0 dev=0.0 ins=12.4 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 18:16:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:16:40,062 main INFO screen embercat pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 11 18:16:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:16:53,221 main INFO screen SWH pass=1 dev=0.04 ins=0.0 pro=10 1a=False 1b=False 2=False (6.1s)
Sep 11 18:17:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:21,363 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:17:21 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 18:17:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:25,246 main INFO screen NPC pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (5.4s)
Sep 11 18:17:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:32,202 main INFO screen hamster pass=0 dev=3.8 ins=0.0 pro=3 1a=False 1b=False 2=False (11.2s)
Sep 11 18:17:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:34,472 main INFO screen CHAROC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (11.0s)
Sep 11 18:17:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:39,104 main INFO screen SIXSEVEN pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 11 18:17:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:17:45,729 main INFO screen APPLECAT pass=0 dev=0.71 ins=0.0 pro=4 1a=False 1b=False 2=False (6.5s)
Sep 11 18:18:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:05,423 main INFO screen FRUIT pass=0 dev=15.17 ins=0.0 pro=9 1a=False 1b=False 2=False (9.2s)
Sep 11 18:18:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:18,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:18:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:18,216 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:18:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:18,365 main INFO screen POPWIF pass=0 dev=0.0 ins=12.41 pro=28 1a=False 1b=False 2=True (0.3s)
Sep 11 18:18:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:29,326 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:18:18:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 18:18:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:18:29,675 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:18:18:29 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 18:19:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:19:19,490 main INFO screen ClickBait pass=0 dev=5.3 ins=1.63 pro=31 1a=False 1b=False 2=False (10.3s)
Sep 11 18:19:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:19:39,218 main INFO screen RWA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.9s)
Sep 11 18:19:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:19:44,271 main INFO screen APPLECAT pass=0 dev=0.63 ins=0.0 pro=3 1a=False 1b=False 2=False (9.2s)
Sep 11 18:20:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:20:21,227 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (7.5s)
Sep 11 18:20:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:20:47,150 main INFO screen MIPEP pass=0 dev=0.4 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 11 18:20:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:20:49,621 main INFO screen $CAJUN pass=0 dev=0.99 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 18:21:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:25,611 main INFO screen BIB pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 18:21:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:40,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:21:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:40,578 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:21:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:45,898 main INFO screen FISTER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.5s)
Sep 11 18:21:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:49,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:21:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:49,991 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:21:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:50,604 main INFO screen APPLECAT pass=0 dev=0.52 ins=0.0 pro=4 1a=False 1b=False 2=False (8.5s)
Sep 11 18:21:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:21:54,385 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.5s)
Sep 11 18:22:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:22:27,160 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:22:27 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T16:55:36Z
--- update 2026-09-11T17:00:58Z
--- update 2026-09-11T17:06:10Z
--- update 2026-09-11T17:11:21Z
--- update 2026-09-11T17:16:23Z
--- update 2026-09-11T17:21:29Z
--- update 2026-09-11T17:26:32Z
--- update 2026-09-11T17:31:32Z
--- update 2026-09-11T17:36:36Z
--- update 2026-09-11T17:41:37Z
--- update 2026-09-11T17:46:37Z
--- update 2026-09-11T17:51:39Z
--- update 2026-09-11T17:56:40Z
--- update 2026-09-11T18:01:40Z
--- update 2026-09-11T18:06:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: f4240d03c1404a3aa0fe2959269b0656
analyses gestart (8213ec5e675e)
--- update 2026-09-11T18:11:40Z
--- update 2026-09-11T18:17:20Z
--- update 2026-09-11T18:22:26Z
```

## Analyses (laatste 25 regels)
```
inactive
16:04:29 persistentie
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
18:06:41 10533 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
18:06:45   ingelezen tot rowid 1884078 (200000 rijen, 200000 bruikbaar)
18:06:47   ingelezen tot rowid 1995665 (311587 rijen, 311587 bruikbaar)
18:06:47 ingelezen: 311587 nieuwe trades, 311587 bruikbaar (6s)
18:06:58 820 aankopen van groeiers geëvalueerd
18:06:59 klaar in 18s -> /opt/schaduwbot/reports/ledger.md
18:07:01   2000 nieuwe tokens doorgerekend
18:07:02 klaar in 3s: 5471 tokens, 2456 nieuw -> /opt/schaduwbot/reports/video_replay.md
18:07:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 18:07 UTC
18:07:02 35379 tokens geladen
18:07:05   2000 tokens, 288862 trades, 71888 posities (3s)
18:07:08   4000 tokens, 576736 trades, 138871 posities (6s)
18:07:12   6000 tokens, 890562 trades, 213603 posities (9s)
18:07:14   8000 tokens, 1176630 trades, 283011 posities (12s)
18:07:18   10000 tokens, 1485942 trades, 359232 posities (16s)
18:07:21   12000 tokens, 1771256 trades, 428551 posities (19s)
18:07:24 posities: 488514 uit 1996386 trades (22s)
18:07:31 115882 wallets gerekend
18:07:31 geluk-toets
18:07:51 persistentie
18:07:53 kopieer-simulatie
18:08:00 klaar in 58s -> /opt/schaduwbot/reports/wallets.md
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
