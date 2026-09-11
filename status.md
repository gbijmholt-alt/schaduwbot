# Schaduwbot status

- tijd: 2026-09-11 21:11:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 7 hours, 24 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 654/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 5458, "tokens_in_memory": 1774, "msgs": 1105449, "trades": 221946, "creates": 1774, "decode_fail": 16489, "rpc_calls": 7017, "rpc_errors": 307, "sol_usd": 102.72240914013432, "open_positions": 91, "log_all_trades": true}
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
Sep 11 20:59:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:59:45,762 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:59:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:59:52,568 main INFO screen marcat pass=0 dev=1.09 ins=7.09 pro=18 1a=False 1b=False 2=True (6.9s)
Sep 11 21:00:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:00:19,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:00:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:00:24,825 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:00:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:00:41,386 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:00:41 +0000] "GET /health HTTP/1.1" 200 448 "-" "Python-urllib/3.14"
Sep 11 21:00:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:00:43,060 main INFO screen Martingale pass=0 dev=1.0 ins=20.4 pro=76 1a=False 1b=False 2=True (6.1s)
Sep 11 21:00:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:00:47,657 main INFO screen GOBLIN pass=0 dev=0.44 ins=49.51 pro=24 1a=False 1b=False 2=True (28.0s)
Sep 11 21:01:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:01:18,763 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:01:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:01:32,201 main INFO screen $SC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (13.5s)
Sep 11 21:01:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:01:42,159 main INFO screen SEPE pass=1 dev=0.0 ins=8.61 pro=17 1a=False 1b=False 2=False (5.9s)
Sep 11 21:01:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:01:51,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:01:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:01:56,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:02:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:11,773 main INFO screen BALLIN pass=0 dev=0.0 ins=17.31 pro=73 1a=False 1b=False 2=True (20.6s)
Sep 11 21:02:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:19,795 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:02:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:24,868 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:02:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:26,396 main INFO screen frens pass=0 dev=0.0 ins=19.22 pro=38 1a=False 1b=False 2=True (8.1s)
Sep 11 21:02:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:30,405 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:02:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:35,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:02:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:35,742 main INFO screen VENOM pass=0 dev=0.49 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 11 21:02:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:46,933 main INFO screen PORNHUB pass=0 dev=97.73 ins=0.0 pro=1 1a=False 1b=False 2=True (27.6s)
Sep 11 21:02:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:53,396 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 21:02:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:54,525 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 21:02:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:02:54,786 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.0s)
Sep 11 21:03:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:22,704 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:31,233 main INFO screen CHUNLI2.0 pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 11 21:03:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:32,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:33,901 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:37,264 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:38,972 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:44,208 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:49,269 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:03:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:03:51,754 main INFO screen INU pass=0 dev=0.0 ins=9.26 pro=76 1a=False 1b=False 2=True (19.6s)
Sep 11 21:04:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:01,315 main INFO screen HAPPY pass=0 dev=0.0 ins=20.07 pro=38 1a=False 1b=False 2=True (27.5s)
Sep 11 21:04:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:01,802 main INFO screen $CAJUN pass=0 dev=1.19 ins=0.0 pro=3 1a=False 1b=False 2=False (10.0s)
Sep 11 21:04:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:10,198 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.1s)
Sep 11 21:04:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:24,505 main INFO screen RICK pass=0 dev=0.69 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 11 21:04:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:27,936 main INFO screen its pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 11 21:04:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:04:31,411 main INFO screen JIMPUS pass=0 dev=0.88 ins=35.79 pro=12 1a=False 1b=True 2=True (7.3s)
Sep 11 21:05:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:03,414 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:05:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:09,203 main INFO screen HALH pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.4s)
Sep 11 21:05:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:11,160 main INFO screen SQUEEZE pass=0 dev=0.0 ins=16.51 pro=36 1a=False 1b=False 2=True (7.9s)
Sep 11 21:05:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:26,381 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:05:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:31,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:05:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:40,512 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:05:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:44,369 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:05:44 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 21:05:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:45,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:05:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:05:47,957 main INFO screen WIFJUG pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (21.7s)
Sep 11 21:06:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:06,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:06:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:08,049 main INFO screen ROBIN pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (27.6s)
Sep 11 21:06:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:17,662 main INFO screen La Peace pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (11.6s)
Sep 11 21:06:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:23,210 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:06:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:28,279 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:06:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:30,332 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:06:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:35,405 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:06:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:49,592 main INFO screen $GOAT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (26.5s)
Sep 11 21:06:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:06:54,802 main INFO screen SIZE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (24.6s)
Sep 11 21:07:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:19,491 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:07:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:24,562 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:07:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:40,868 main INFO screen ALLINU pass=0 dev=0.0 ins=0.27 pro=42 1a=False 1b=False 2=False (7.4s)
Sep 11 21:07:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:42,161 main INFO screen $SLUMP pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=True (22.8s)
Sep 11 21:07:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:53,950 main INFO screen BALLS pass=1 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (9.4s)
Sep 11 21:07:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:07:56,567 main INFO screen GRADELESS pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (12.5s)
Sep 11 21:08:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:08:13,401 main INFO screen ALLINU pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (7.0s)
Sep 11 21:08:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:08:22,907 main INFO screen APPLECAT pass=0 dev=0.79 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 11 21:08:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:08:28,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:08:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:08:41,068 main INFO screen $SC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (12.3s)
Sep 11 21:08:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:08:56,951 main INFO screen $CAJUN pass=0 dev=0.78 ins=0.0 pro=4 1a=False 1b=False 2=False (6.4s)
Sep 11 21:09:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:09:08,682 main INFO screen VAYNE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 21:09:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:09:10,045 main INFO screen OG pass=1 dev=3.42 ins=0.0 pro=23 1a=False 1b=False 2=False (10.9s)
Sep 11 21:09:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:09:11,570 main INFO screen MUSKRAT pass=1 dev=0.0 ins=11.95 pro=21 1a=False 1b=False 2=False (11.1s)
Sep 11 21:09:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:09:33,444 main INFO screen DEREK pass=1 dev=0.0 ins=4.21 pro=45 1a=False 1b=False 2=False (3.2s)
Sep 11 21:09:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:09:59,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:10:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:13,446 main INFO screen Pleb pass=0 dev=0.0 ins=20.32 pro=47 1a=False 1b=False 2=True (14.0s)
Sep 11 21:10:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:26,408 main INFO screen flynsa pass=0 dev=0.0 ins=27.57 pro=15 1a=False 1b=False 2=False (9.6s)
Sep 11 21:10:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:49,393 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 11 21:10:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:50,196 main INFO screen ALLAPE pass=1 dev=0.0 ins=2.61 pro=54 1a=False 1b=False 2=False (12.5s)
Sep 11 21:10:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:55,063 main INFO screen DEREK pass=1 dev=0.0 ins=16.39 pro=44 1a=False 1b=False 2=False (3.0s)
Sep 11 21:10:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:10:55,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:11:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:11:00,450 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:11:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:11:06,949 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:11:06 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 670a5941fedf41389993862a94844cc9
analyses gestart (8746aefc73b4)
--- update 2026-09-11T19:45:08Z
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
