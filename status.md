# Schaduwbot status

- tijd: 2026-09-11 21:27:05 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 7 hours, 40 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 670/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 6417, "tokens_in_memory": 2147, "msgs": 1283380, "trades": 261346, "creates": 2147, "decode_fail": 20323, "rpc_calls": 8181, "rpc_errors": 361, "sol_usd": 102.8339772840259, "open_positions": 108, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 20:40 UTC

Gelogde schaduwtrades: **32081**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 23762 | 3627 | 39 | 3626 | 279 | 6708 | 19726 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 360 | 17% | 2.2% | +44.3% | -16.8% | -6.27% | 100% |
| dip35_V1_gescreend_fail | 3168 | 27% | 3.8% | +46.1% | -26.2% | -6.88% | 100% |
| dip35_V1_alle | 3714 | 26% | 3.8% | +45.2% | -25.5% | -7.01% | 100% |
| dip35_V2_gescreend_pass | 357 | 21% | 3.1% | +45.5% | -21.5% | -7.25% | 100% |
| dip35_V2_gescreend_fail | 3171 | 25% | 4.4% | +56.8% | -28.5% | -7.29% | 100% |
| dip35_V2_alle | 3677 | 24% | 4.4% | +55.1% | -28.0% | -7.72% | 100% |
| dip35_V3_gescreend_pass | 358 | 9% | 3.6% | +374.3% | -23.0% | +11.45% | 100% |
| dip35_V3_gescreend_fail | 3231 | 13% | 6.1% | +119.2% | -29.9% | -10.19% | 100% |
| dip35_V3_alle | 3725 | 13% | 6.0% | +130.9% | -29.4% | -8.63% | 100% |
| dip40_V1_gescreend_pass | 333 | 15% | 2.1% | +47.5% | -15.7% | -6.05% | 99% |
| dip40_V1_gescreend_fail | 3089 | 26% | 3.8% | +48.0% | -26.1% | -6.60% | 100% |
| dip40_V1_alle | 3570 | 26% | 3.7% | +47.9% | -25.3% | -6.57% | 100% |
| dip40_V2_gescreend_pass | 330 | 17% | 2.7% | +49.8% | -20.2% | -8.30% | 100% |
| dip40_V2_gescreend_fail | 3081 | 25% | 4.3% | +56.3% | -28.4% | -7.22% | 100% |
| dip40_V2_alle | 3527 | 24% | 4.3% | +55.5% | -27.8% | -7.72% | 100% |
| dip40_V3_gescreend_pass | 333 | 7% | 3.0% | +439.0% | -21.3% | +10.46% | 100% |
| dip40_V3_gescreend_fail | 3140 | 13% | 5.8% | +113.7% | -29.7% | -11.34% | 100% |
| dip40_V3_alle | 3578 | 12% | 5.7% | +127.8% | -29.1% | -9.81% | 100% |
| dip45_V1_gescreend_pass | 318 | 16% | 1.9% | +51.3% | -15.6% | -4.63% | 98% |
| dip45_V1_gescreend_fail | 3010 | 27% | 3.3% | +48.5% | -25.8% | -5.44% | 100% |
| dip45_V1_alle | 3446 | 26% | 3.3% | +48.6% | -25.1% | -5.57% | 100% |
| dip45_V2_gescreend_pass | 314 | 19% | 2.5% | +49.1% | -19.8% | -6.41% | 100% |
| dip45_V2_gescreend_fail | 2989 | 25% | 3.9% | +59.1% | -28.0% | -6.07% | 100% |
| dip45_V2_alle | 3400 | 24% | 3.9% | +58.0% | -27.5% | -6.58% | 100% |
| dip45_V3_gescreend_pass | 316 | 7% | 2.5% | +485.0% | -20.4% | +16.35% | 100% |
| dip45_V3_gescreend_fail | 3041 | 14% | 5.5% | +121.6% | -29.3% | -8.57% | 100% |
| dip45_V3_alle | 3444 | 13% | 5.3% | +138.2% | -28.6% | -6.84% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 2.0%, kans ruïne 97.5%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2374 | 13% | 3.4% | -9.88% | 100% |
| zonder_xlink | 645 | 21% | 0.0% | +35.85% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 21:16:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:16:18,182 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:16:18 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 21:16:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:16:19,603 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 21:16:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:16:19,858 main INFO screen PEE pass=0 dev=0.0 ins=17.27 pro=42 1a=False 1b=False 2=True (20.7s)
Sep 11 21:16:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:16:46,121 main INFO screen PRL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 11 21:16:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:16:54,258 main INFO screen Pokecoin  pass=0 dev=6.64 ins=1.47 pro=13 1a=False 1b=False 2=False (8.7s)
Sep 11 21:17:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:17:09,893 main INFO screen $ALLDOG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 21:17:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:17:32,419 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:17:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:17:42,993 main INFO screen mmrich pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (10.7s)
Sep 11 21:17:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:17:56,625 main INFO screen Trumpz2 pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 21:18:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:04,862 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:18:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:09,931 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:18:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:19,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:18:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:30,774 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 11 21:18:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:31,937 main INFO screen $LANA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (12.3s)
Sep 11 21:18:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:32,023 main INFO screen Rocky pass=1 dev=0.0 ins=7.06 pro=18 1a=False 1b=False 2=False (1.6s)
Sep 11 21:18:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:37,743 main INFO screen $CAJUN pass=0 dev=0.8 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 11 21:18:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:43,569 main INFO screen $GOAT pass=0 dev=0.76 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 11 21:18:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:18:56,450 main INFO screen ALL IN pass=1 dev=0.0 ins=0.98 pro=30 1a=False 1b=False 2=False (5.7s)
Sep 11 21:19:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:03,880 main INFO screen RIPALON pass=1 dev=1.71 ins=0.0 pro=53 1a=False 1b=False 2=False (6.9s)
Sep 11 21:19:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:04,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:19:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:08,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:19:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:09,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:19:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:22,973 main INFO screen MEME pass=0 dev=0.0 ins=18.0 pro=29 1a=False 1b=False 2=True (14.7s)
Sep 11 21:19:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:24,849 main INFO screen Rocky pass=1 dev=0.0 ins=7.73 pro=23 1a=False 1b=False 2=False (3.1s)
Sep 11 21:19:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:31,150 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.9s)
Sep 11 21:19:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:41,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:19:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:45,328 main INFO screen CPI pass=1 dev=0.0 ins=9.11 pro=23 1a=False 1b=False 2=False (5.5s)
Sep 11 21:19:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:45,548 main INFO screen CHEESEBURGER pass=0 dev=0.0 ins=9.45 pro=23 1a=False 1b=False 2=True (7.6s)
Sep 11 21:19:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:19:48,406 main INFO screen Piss pass=0 dev=0.0 ins=14.91 pro=40 1a=False 1b=False 2=True (6.9s)
Sep 11 21:20:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:20:07,864 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:20:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:20:20,624 main INFO screen $MOON pass=0 dev=0.24 ins=0.0 pro=4 1a=False 1b=False 2=False (12.9s)
Sep 11 21:20:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:20:20,720 main INFO screen WCOI pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 11 21:20:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:20:54,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:20:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:20:59,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:21:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:06,313 main INFO screen PAIR pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (10.0s)
Sep 11 21:21:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:20,833 main INFO screen ALLINU pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.5s)
Sep 11 21:21:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:31,991 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:21:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:37,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:21:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:37,207 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:21:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 21:21:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:21:52,576 main INFO screen TNT pass=0 dev=0.0 ins=0.07 pro=19 1a=False 1b=False 2=True (20.7s)
Sep 11 21:22:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:12,827 main INFO screen BASEDNIBBA pass=0 dev=21.25 ins=1.36 pro=28 1a=False 1b=False 2=False (7.3s)
Sep 11 21:22:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:22,227 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:22:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:25,003 main INFO screen FLYTON pass=1 dev=0.0 ins=0.4 pro=14 1a=False 1b=False 2=False (10.6s)
Sep 11 21:22:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:25,140 main INFO screen MMKY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (10.5s)
Sep 11 21:22:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:29,106 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:22:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:35,415 main INFO screen ALLDOG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (13.3s)
Sep 11 21:22:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:37,661 main INFO screen FOLD pass=0 dev=0.0 ins=17.53 pro=61 1a=False 1b=False 2=True (8.6s)
Sep 11 21:22:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:22:54,552 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:23:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:06,534 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (12.1s)
Sep 11 21:23:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:08,896 main INFO screen BELIEVE pass=1 dev=0.0 ins=12.26 pro=53 1a=False 1b=False 2=False (7.6s)
Sep 11 21:23:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:18,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:23:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:27,868 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:23:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:32,110 main INFO screen PSTR pass=1 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (14.0s)
Sep 11 21:23:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:42,509 main INFO screen CELESTE pass=0 dev=0.7 ins=36.82 pro=11 1a=False 1b=True 2=True (14.7s)
Sep 11 21:23:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:43,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:23:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:47,534 main INFO screen WCOI pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 11 21:23:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:23:48,245 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:24:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:03,032 main INFO screen Puppeth pass=0 dev=0.0 ins=7.61 pro=35 1a=False 1b=False 2=True (19.9s)
Sep 11 21:24:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:16,293 main INFO screen ALL/IN pass=1 dev=0.35 ins=4.05 pro=33 1a=False 1b=False 2=False (9.1s)
Sep 11 21:24:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:40,097 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:24:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:42,189 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:24:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:45,131 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:24:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:54,815 main INFO screen TrumpCoin pass=0 dev=0.39 ins=0.0 pro=1 1a=False 1b=False 2=False (12.7s)
Sep 11 21:24:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:54,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:24:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:24:55,594 main INFO screen ALLOUT pass=1 dev=0.2 ins=1.17 pro=58 1a=False 1b=False 2=False (10.0s)
Sep 11 21:25:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:03,188 main INFO screen YEET pass=0 dev=0.0 ins=12.9 pro=69 1a=False 1b=False 2=True (8.4s)
Sep 11 21:25:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:06,282 aiohttp.access INFO 147.185.132.51 [11/Sep/2026:21:25:06 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 21:25:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:06,310 main INFO screen ice man pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (26.3s)
Sep 11 21:25:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:06,489 aiohttp.access INFO 147.185.132.51 [11/Sep/2026:21:25:06 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 21:25:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:15,039 main INFO screen Beast pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 21:25:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:27,591 main INFO screen WCOI pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 11 21:25:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:33,870 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:21:25:33 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 21:25:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:34,219 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:21:25:34 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 21:25:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:25:39,749 main INFO screen YEET pass=1 dev=0.0 ins=11.33 pro=27 1a=False 1b=False 2=False (5.0s)
Sep 11 21:26:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:13,942 main INFO screen FERSPE pass=0 dev=0.42 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 21:26:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:18,375 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:26:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:23,446 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:26:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:45,185 main INFO screen LINES pass=0 dev=0.18 ins=0.0 pro=81 1a=False 1b=True 2=True (26.9s)
Sep 11 21:26:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:46,832 main INFO screen TOAD pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 21:27:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:27:05,876 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:27:05 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T19:50:11Z
--- update 2026-09-11T19:55:12Z
--- update 2026-09-11T20:00:15Z
--- update 2026-09-11T20:05:16Z
--- update 2026-09-11T20:10:18Z
--- update 2026-09-11T20:15:22Z
--- update 2026-09-11T20:20:26Z
--- update 2026-09-11T20:25:28Z
--- update 2026-09-11T20:30:28Z
--- update 2026-09-11T20:35:28Z
--- update 2026-09-11T20:40:31Z
--- update 2026-09-11T20:45:33Z
--- update 2026-09-11T20:50:36Z
--- update 2026-09-11T20:55:37Z
--- update 2026-09-11T21:00:40Z
--- update 2026-09-11T21:05:43Z
--- update 2026-09-11T21:11:05Z
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
```

## Analyses (laatste 25 regels)
```
inactive
18:40:27 kopieer-simulatie
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
19:40:08 12765 tokens sinds start volledige logging, waarvan 3627 met een gat door herstart
19:40:11   ingelezen tot rowid 2225120 (145387 rijen, 145387 bruikbaar)
19:40:11 ingelezen: 145387 nieuwe trades, 145387 bruikbaar (3s)
19:40:22 177 aankopen van gevolgde wallets geëvalueerd
19:40:34 grote spelers: saldo van 2000 wallets opgehaald
19:41:46 herkomst: 40 posities gekoppeld
19:41:47 klaar in 99s -> /opt/schaduwbot/reports/ledger.md
19:41:49 klaar in 1s: 6168 tokens, 1142 nieuw -> /opt/schaduwbot/reports/video_replay.md
19:41:49 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 19:41 UTC
19:41:49 37636 tokens geladen
19:41:51   2000 tokens, 281880 trades, 68228 posities (2s)
19:41:53   4000 tokens, 562091 trades, 134424 posities (4s)
19:41:56   6000 tokens, 870184 trades, 206311 posities (7s)
19:41:58   8000 tokens, 1149114 trades, 266897 posities (9s)
19:42:01   10000 tokens, 1443511 trades, 336633 posities (12s)
19:42:03   12000 tokens, 1716836 trades, 400450 posities (14s)
19:42:06   14000 tokens, 1988268 trades, 462617 posities (17s)
19:42:08 posities: 523618 uit 2226699 trades (19s)
19:42:14 123108 wallets gerekend
19:42:14 geluk-toets
19:42:33 persistentie
19:42:34 kopieer-simulatie
19:42:39 klaar in 51s -> /opt/schaduwbot/reports/wallets.md
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
