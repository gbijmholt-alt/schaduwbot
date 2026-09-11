# Schaduwbot status

- tijd: 2026-09-11 21:37:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 7 hours, 50 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 697/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 7032, "tokens_in_memory": 2432, "msgs": 1458556, "trades": 290749, "creates": 2432, "decode_fail": 21795, "rpc_calls": 9204, "rpc_errors": 389, "sol_usd": 102.67082839327198, "open_positions": 135, "log_all_trades": true}
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
Sep 11 21:26:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:45,185 main INFO screen LINES pass=0 dev=0.18 ins=0.0 pro=81 1a=False 1b=True 2=True (26.9s)
Sep 11 21:26:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:26:46,832 main INFO screen TOAD pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 21:27:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:27:05,876 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:27:05 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 21:27:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:27:21,526 main INFO screen $GOAT pass=0 dev=1.69 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 11 21:27:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:27:36,837 main INFO screen 2neegys pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 11 21:28:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:28:06,803 main INFO screen 789 pass=1 dev=3.92 ins=3.17 pro=43 1a=False 1b=False 2=False (8.6s)
Sep 11 21:28:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:28:49,003 main INFO screen cash cat pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 21:29:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:11,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:29:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:16,093 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:29:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:17,464 main INFO screen ICEMAN pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (10.7s)
Sep 11 21:29:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:31,032 main INFO screen flynsem pass=0 dev=0.0 ins=27.57 pro=22 1a=False 1b=False 2=False (9.5s)
Sep 11 21:29:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:34,244 main INFO screen HAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (23.3s)
Sep 11 21:29:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:34,282 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:29:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:39,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:29:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:29:57,647 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:30:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:00,193 main INFO screen DOOYET pass=0 dev=0.17 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 11 21:30:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:02,722 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:30:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:04,849 main INFO screen FROGGO pass=0 dev=0.47 ins=53.74 pro=32 1a=False 1b=False 2=True (30.6s)
Sep 11 21:30:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:13,036 main INFO screen B-ALL-IN pass=1 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=False (10.2s)
Sep 11 21:30:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:22,576 main INFO screen Bullunk pass=0 dev=0.14 ins=75.6 pro=15 1a=False 1b=True 2=True (25.7s)
Sep 11 21:30:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:30,539 main INFO screen AllFrog pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (10.1s)
Sep 11 21:30:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:42,971 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:30:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:48,047 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:30:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:30:48,091 main INFO screen wind pass=0 dev=2.65 ins=0.0 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 11 21:31:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:03,275 main INFO screen allin pass=0 dev=0.0 ins=35.82 pro=66 1a=False 1b=False 2=True (20.4s)
Sep 11 21:31:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:06,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:09,962 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:11,758 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:12,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:15,033 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:16,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:26,928 main INFO screen Greed pass=0 dev=0.0 ins=13.26 pro=78 1a=False 1b=False 2=True (20.0s)
Sep 11 21:31:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:29,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:31,252 main INFO screen BONKA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (21.4s)
Sep 11 21:31:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:32,792 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.1s)
Sep 11 21:31:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:36,020 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:31:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:36,586 main INFO screen Fleece pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 11 21:31:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:40,360 main INFO screen AllFrog pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (2.6s)
Sep 11 21:31:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:31:42,660 main INFO screen TrumpCoin pass=0 dev=0.44 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 11 21:32:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:32:12,963 main INFO screen cap pass=0 dev=0.65 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 11 21:32:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:32:14,217 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:32:14 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 21:32:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:32:22,191 main INFO screen LaMisery pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 21:32:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:32:30,697 main INFO screen Dr. E pass=1 dev=0.0 ins=10.7 pro=19 1a=False 1b=False 2=False (1.6s)
Sep 11 21:32:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:32:51,625 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:33:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:00,076 main INFO screen KING pass=0 dev=0.0 ins=9.19 pro=29 1a=False 1b=True 2=True (8.5s)
Sep 11 21:33:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:00,245 main INFO screen $CAJUN pass=0 dev=0.45 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 11 21:33:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:14,547 main INFO screen RODENT pass=0 dev=0.0 ins=16.12 pro=43 1a=False 1b=False 2=True (3.9s)
Sep 11 21:33:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:16,936 main INFO screen SOLANA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 21:33:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:20,919 main INFO screen JASON pass=1 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (3.5s)
Sep 11 21:33:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:49,575 main INFO screen Bank pass=0 dev=0.0 ins=14.56 pro=78 1a=False 1b=False 2=True (3.1s)
Sep 11 21:33:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:55,267 main INFO screen Matrix pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 21:33:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:56,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:01,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:02,199 main INFO screen Greed pass=1 dev=0.0 ins=7.51 pro=19 1a=False 1b=False 2=False (2.3s)
Sep 11 21:34:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:05,312 main INFO screen Stick pass=0 dev=0.0 ins=19.53 pro=67 1a=False 1b=False 2=True (9.3s)
Sep 11 21:34:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:06,879 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:12,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:17,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:21,533 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 11 21:34:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:31,856 main INFO screen POSES pass=1 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (4.5s)
Sep 11 21:34:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:32,954 main INFO screen ElonWifHat pass=0 dev=78.8 ins=0.0 pro=4 1a=False 1b=False 2=True (20.5s)
Sep 11 21:34:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:45,024 main INFO screen 100 pass=0 dev=4.41 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 21:34:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:53,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:57,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:58,416 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:02,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:09,868 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.1s)
Sep 11 21:35:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:12,905 main INFO screen TOKABU pass=0 dev=0.0 ins=15.68 pro=57 1a=False 1b=False 2=True (19.6s)
Sep 11 21:35:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:16,506 main INFO screen LMC pass=0 dev=0.0 ins=18.34 pro=37 1a=False 1b=False 2=True (19.0s)
Sep 11 21:35:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:36,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:43,225 main INFO screen KIRK pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 21:35:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:43,795 main INFO screen YOTSUBA pass=0 dev=0.18 ins=0.0 pro=36 1a=False 1b=True 2=False (7.6s)
Sep 11 21:35:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:51,256 main INFO screen HALH pass=0 dev=0.94 ins=0.0 pro=4 1a=False 1b=False 2=False (2.7s)
Sep 11 21:35:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:55,124 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:36:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:03,645 main INFO screen BRAINS pass=0 dev=13.58 ins=0.0 pro=30 1a=False 1b=False 2=False (4.4s)
Sep 11 21:36:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:04,284 main INFO screen ice man pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 21:36:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:24,470 main INFO screen ATH pass=1 dev=1.74 ins=12.96 pro=53 1a=False 1b=False 2=False (6.0s)
Sep 11 21:36:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:38,815 main INFO screen SUPERSTONK pass=0 dev=0.0 ins=18.48 pro=68 1a=False 1b=False 2=True (3.8s)
Sep 11 21:37:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:21,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:37:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:21,292 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:37:21 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
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
