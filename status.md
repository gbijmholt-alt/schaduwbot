# Schaduwbot status

- tijd: 2026-09-12 04:20:54 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 14 hours, 33 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1091/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 31246, "tokens_in_memory": 7053, "msgs": 6155806, "trades": 1116984, "creates": 10646, "decode_fail": 57402, "rpc_calls": 37982, "rpc_errors": 1547, "sol_usd": 101.57116811497049, "open_positions": 35, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **40074**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 4122 | 672 | 3 | 672 | 43 | 1150 | 3518 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 459 | 17% | 2.2% | +44.4% | -16.8% | -6.63% | 100% |
| dip35_V1_gescreend_fail | 3803 | 27% | 3.8% | +45.8% | -25.9% | -6.72% | 100% |
| dip35_V1_alle | 4636 | 26% | 3.9% | +45.0% | -25.2% | -6.81% | 100% |
| dip35_V2_gescreend_pass | 456 | 22% | 3.1% | +42.9% | -21.3% | -7.23% | 100% |
| dip35_V2_gescreend_fail | 3838 | 25% | 4.4% | +56.6% | -28.0% | -7.07% | 100% |
| dip35_V2_alle | 4603 | 24% | 4.5% | +54.0% | -27.6% | -7.68% | 100% |
| dip35_V3_gescreend_pass | 458 | 8% | 3.5% | +315.4% | -22.6% | +6.18% | 100% |
| dip35_V3_gescreend_fail | 3914 | 13% | 6.0% | +117.7% | -29.6% | -9.92% | 100% |
| dip35_V3_alle | 4648 | 13% | 6.0% | +123.4% | -29.2% | -9.13% | 100% |
| dip40_V1_gescreend_pass | 428 | 15% | 2.3% | +47.1% | -16.1% | -6.79% | 100% |
| dip40_V1_gescreend_fail | 3731 | 26% | 3.8% | +47.6% | -25.7% | -6.53% | 100% |
| dip40_V1_alle | 4448 | 25% | 3.8% | +47.7% | -25.0% | -6.56% | 100% |
| dip40_V2_gescreend_pass | 426 | 18% | 2.8% | +45.2% | -20.1% | -8.41% | 100% |
| dip40_V2_gescreend_fail | 3746 | 25% | 4.3% | +56.2% | -27.9% | -7.04% | 100% |
| dip40_V2_alle | 4410 | 24% | 4.4% | +54.4% | -27.4% | -7.73% | 100% |
| dip40_V3_gescreend_pass | 429 | 8% | 3.0% | +323.1% | -21.3% | +4.39% | 100% |
| dip40_V3_gescreend_fail | 3819 | 13% | 5.8% | +115.9% | -29.4% | -10.42% | 100% |
| dip40_V3_alle | 4459 | 13% | 5.8% | +122.2% | -28.9% | -9.69% | 100% |
| dip45_V1_gescreend_pass | 411 | 16% | 2.2% | +48.7% | -16.0% | -5.95% | 100% |
| dip45_V1_gescreend_fail | 3652 | 27% | 3.3% | +48.6% | -25.4% | -5.19% | 100% |
| dip45_V1_alle | 4302 | 26% | 3.4% | +48.8% | -24.8% | -5.49% | 100% |
| dip45_V2_gescreend_pass | 408 | 19% | 2.7% | +44.3% | -19.9% | -7.48% | 100% |
| dip45_V2_gescreend_fail | 3659 | 25% | 3.9% | +58.6% | -27.4% | -5.79% | 100% |
| dip45_V2_alle | 4264 | 24% | 4.0% | +56.6% | -27.0% | -6.61% | 100% |
| dip45_V3_gescreend_pass | 411 | 7% | 2.7% | +379.8% | -20.6% | +8.62% | 100% |
| dip45_V3_gescreend_fail | 3717 | 14% | 5.5% | +121.2% | -29.0% | -7.96% | 100% |
| dip45_V3_alle | 4304 | 13% | 5.5% | +130.6% | -28.4% | -7.15% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2998 | 13% | 3.5% | -10.11% | 100% |
| zonder_xlink | 888 | 18% | 0.0% | +22.78% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 04:04:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:04:20,297 main INFO screen ‎ pass=0 dev=0.0 ins=17.51 pro=42 1a=False 1b=False 2=True (1.9s)
Sep 12 04:04:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:04:44,612 main INFO screen skipoo pass=0 dev=2.32 ins=0.0 pro=1 1a=False 1b=False 2=False (9.5s)
Sep 12 04:05:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:05:03,233 main INFO screen Peproto pass=0 dev=2.44 ins=0.0 pro=7 1a=False 1b=False 2=False (6.8s)
Sep 12 04:05:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:05:14,792 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:05:14 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 04:06:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:06:02,839 main INFO screen MemeLand pass=0 dev=0.53 ins=0.35 pro=8 1a=True 1b=True 2=False (4.8s)
Sep 12 04:06:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:06:30,360 main INFO screen robotdih pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 12 04:07:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:01,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:06,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:06,667 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:11,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:15,373 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:20,543 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:07:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:24,581 main INFO screen CASH pass=0 dev=0.83 ins=23.58 pro=39 1a=False 1b=False 2=True (18.4s)
Sep 12 04:07:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:26,552 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.1s)
Sep 12 04:07:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:26,627 main INFO screen Micromeme pass=1 dev=0.0 ins=9.35 pro=67 1a=False 1b=False 2=False (2.0s)
Sep 12 04:07:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:31,928 main INFO screen Nom pass=0 dev=0.0 ins=17.44 pro=43 1a=False 1b=False 2=True (5.4s)
Sep 12 04:07:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:39,924 main INFO screen CRINGE pass=0 dev=0.12 ins=0.0 pro=3 1a=False 1b=False 2=False (12.2s)
Sep 12 04:07:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:42,091 main INFO screen wind pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (9.7s)
Sep 12 04:07:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:43,121 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.8s)
Sep 12 04:07:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:07:59,600 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:08:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:04,670 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:08:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:24,045 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.5s)
Sep 12 04:08:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:25,946 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (8.1s)
Sep 12 04:08:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:38,298 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:08:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:43,250 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:08:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:43,364 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:08:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:08:48,320 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:09:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:00,034 main INFO screen memecoin pass=0 dev=0.0 ins=22.34 pro=73 1a=False 1b=False 2=True (21.8s)
Sep 12 04:09:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:06,396 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.2s)
Sep 12 04:09:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:28,453 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.8s)
Sep 12 04:09:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:29,226 main INFO screen Bihcoin pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 12 04:09:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:39,769 aiohttp.access INFO 87.236.176.120 [12/Sep/2026:04:09:39 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; InternetMeasurement/1.0; +https://internet-measurement.com/)"
Sep 12 04:09:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:09:41,430 main INFO screen mayham pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 12 04:10:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:10:17,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:10:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:10:22,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:10:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:10:37,223 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:10:37 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:10:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:10:42,062 main INFO screen wojakgpt pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (24.9s)
Sep 12 04:10:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:10:48,514 main INFO screen LILY pass=1 dev=0.0 ins=8.05 pro=54 1a=False 1b=False 2=False (3.9s)
Sep 12 04:11:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:11:57,279 main INFO screen skipoo pass=0 dev=2.51 ins=0.0 pro=3 1a=False 1b=False 2=False (8.2s)
Sep 12 04:12:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:12:13,073 main INFO screen Gamble pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 12 04:12:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:12:52,880 main INFO screen RAM pass=1 dev=0.56 ins=0.0 pro=48 1a=False 1b=False 2=False (6.8s)
Sep 12 04:12:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:12:54,597 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:13:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:13:02,110 main INFO screen west pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 04:13:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:13:50,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:13:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:13:55,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:14:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:12,430 main INFO screen CATSOLANA pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (22.2s)
Sep 12 04:14:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:18,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:14:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:23,616 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:14:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:37,087 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:14:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:39,347 main INFO screen $CAJUN pass=0 dev=0.85 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 12 04:14:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:42,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:14:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:43,849 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (25.3s)
Sep 12 04:14:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:14:57,546 main INFO screen HTML pass=0 dev=0.0 ins=26.68 pro=67 1a=False 1b=False 2=True (20.7s)
Sep 12 04:15:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:14,754 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:15:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:21,562 main INFO screen diddy pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 12 04:15:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:25,007 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:15:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:30,078 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:15:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:31,109 main INFO screen $AURA pass=0 dev=0.51 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 12 04:15:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:34,141 main INFO screen FRC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (11.1s)
Sep 12 04:15:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:48,155 main INFO screen x pass=0 dev=0.0 ins=10.48 pro=31 1a=False 1b=True 2=False (1.5s)
Sep 12 04:15:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:48,338 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:15:48 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:15:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:50,040 main INFO screen DELL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.6s)
Sep 12 04:15:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:15:54,883 main INFO screen DD pass=0 dev=0.0 ins=24.1 pro=61 1a=False 1b=False 2=True (3.9s)
Sep 12 04:16:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:16:56,446 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 12 04:17:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:17:17,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:17:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:17:22,301 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:17:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:17:42,897 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.7s)
Sep 12 04:18:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:18:32,828 main INFO screen skipoo pass=0 dev=1.95 ins=0.0 pro=1 1a=False 1b=False 2=True (8.8s)
Sep 12 04:18:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:18:44,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:18:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:18:50,054 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:19:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:04,338 main INFO screen NICE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.5s)
Sep 12 04:19:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:18,524 main INFO screen TOAD pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 04:19:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:40,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:19:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:45,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:00,863 main INFO screen PUMP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 04:20:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:32,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:38,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:44,395 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 04:20:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:53,598 main INFO screen Dellphin pass=0 dev=0.0 ins=10.39 pro=64 1a=False 1b=False 2=True (20.8s)
Sep 12 04:20:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:54,697 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:20:54 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T02:52:55Z
--- update 2026-09-12T02:58:01Z
--- update 2026-09-12T03:03:02Z
--- update 2026-09-12T03:08:04Z
--- update 2026-09-12T03:13:08Z
--- update 2026-09-12T03:18:29Z
--- update 2026-09-12T03:23:36Z
--- update 2026-09-12T03:28:37Z
--- update 2026-09-12T03:33:53Z
--- update 2026-09-12T03:39:36Z
--- update 2026-09-12T03:44:43Z
--- update 2026-09-12T03:49:57Z
--- update 2026-09-12T03:55:08Z
Running as unit: schaduwbot-wallets.service; invocation ID: 65c97d0888f44ae1a8047aba8afd8a37
analyses gestart (8746aefc73b4)
--- update 2026-09-12T04:00:11Z
--- update 2026-09-12T04:05:13Z
--- update 2026-09-12T04:10:36Z
--- update 2026-09-12T04:15:47Z
--- update 2026-09-12T04:20:53Z
```

## Analyses (laatste 25 regels)
```
inactive
03:55:46 grote spelers: saldo van 418 wallets opgehaald
03:56:54 herkomst: 40 posities gekoppeld
03:56:57 klaar in 108s -> /opt/schaduwbot/reports/ledger.md
03:56:59   2000 nieuwe tokens doorgerekend
03:57:01 klaar in 4s: 13363 tokens, 2580 nieuw -> /opt/schaduwbot/reports/video_replay.md
03:57:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 03:57 UTC
03:57:01 47900 tokens geladen
03:57:04   2000 tokens, 246053 trades, 52081 posities (3s)
03:57:07   4000 tokens, 503264 trades, 107812 posities (6s)
03:57:09   6000 tokens, 764215 trades, 157570 posities (8s)
03:57:12   8000 tokens, 1014522 trades, 208740 posities (11s)
03:57:15   10000 tokens, 1313518 trades, 277037 posities (14s)
03:57:17   12000 tokens, 1549954 trades, 317998 posities (16s)
03:57:20   14000 tokens, 1819922 trades, 373769 posities (19s)
03:57:23   16000 tokens, 2091269 trades, 432443 posities (22s)
03:57:25   18000 tokens, 2350661 trades, 485256 posities (24s)
03:57:28   20000 tokens, 2609433 trades, 537071 posities (27s)
03:57:30   22000 tokens, 2847285 trades, 586776 posities (29s)
03:57:32   24000 tokens, 3117299 trades, 640240 posities (31s)
03:57:34 posities: 689428 uit 3308619 trades (33s)
03:57:43 153508 wallets gerekend
03:57:44 geluk-toets
03:58:14 persistentie
03:58:16 kopieer-simulatie
03:58:26 klaar in 85s -> /opt/schaduwbot/reports/wallets.md
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
