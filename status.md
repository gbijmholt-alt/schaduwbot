# Schaduwbot status

- tijd: 2026-09-12 04:00:12 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 14 hours, 13 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1095/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 30004, "tokens_in_memory": 7268, "msgs": 5988343, "trades": 1088179, "creates": 10344, "decode_fail": 56570, "rpc_calls": 36876, "rpc_errors": 1507, "sol_usd": 101.63563704633128, "open_positions": 32, "log_all_trades": true}
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
Sep 12 03:46:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:41,639 main INFO screen KING pass=0 dev=98.38 ins=0.0 pro=1 1a=False 1b=False 2=True (21.3s)
Sep 12 03:46:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:44,136 main INFO screen Cat pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (5.6s)
Sep 12 03:47:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:07,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:47:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:13,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:47:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:27,316 main INFO screen catcern pass=0 dev=4.71 ins=0.0 pro=3 1a=False 1b=False 2=False (19.4s)
Sep 12 03:47:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:42,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:47:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:48,831 main INFO screen Fly pass=1 dev=0.0 ins=3.91 pro=42 1a=False 1b=False 2=False (5.1s)
Sep 12 03:47:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:52,280 main INFO screen Toad pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 12 03:47:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:55,756 main INFO screen bundloor pass=1 dev=0.0 ins=7.63 pro=67 1a=False 1b=False 2=False (13.0s)
Sep 12 03:47:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:47:55,924 main INFO screen FLY pass=0 dev=6.63 ins=22.12 pro=30 1a=False 1b=False 2=False (1.6s)
Sep 12 03:48:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:48:09,862 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:48:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:48:15,259 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:48:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:48:16,695 main INFO screen $U pass=0 dev=1.31 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 12 03:48:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:48:29,640 main INFO screen CCT pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (19.8s)
Sep 12 03:48:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:48:59,998 aiohttp.access INFO 216.218.206.69 [12/Sep/2026:03:48:59 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
Sep 12 03:49:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:49:29,339 main INFO screen satanpawn pass=0 dev=0.46 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 12 03:49:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:49:43,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:49:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:49:48,702 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:49:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:49:58,481 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:49:58 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 03:50:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:50:00,473 main INFO screen NIKE pass=0 dev=0.0 ins=15.81 pro=59 1a=False 1b=False 2=True (3.8s)
Sep 12 03:50:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:50:01,893 main INFO screen CHADGPT pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (18.3s)
Sep 12 03:50:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:50:49,706 main INFO screen MIMI pass=0 dev=4.29 ins=4.65 pro=29 1a=False 1b=True 2=False (1.3s)
Sep 12 03:50:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:50:53,699 main INFO screen NIKE pass=0 dev=0.0 ins=20.35 pro=32 1a=False 1b=False 2=False (1.2s)
Sep 12 03:51:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:51:13,055 main INFO screen . pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 12 03:51:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:51:13,721 aiohttp.access INFO 216.218.206.73 [12/Sep/2026:03:51:13 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
Sep 12 03:51:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:51:24,140 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:51:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:51:29,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:51:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:51:43,721 main INFO screen Mewania pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 03:52:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:52:00,017 main INFO screen $CAJUN pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=True (3.4s)
Sep 12 03:52:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:52:54,474 main INFO screen skipoo pass=0 dev=1.7 ins=0.0 pro=1 1a=False 1b=False 2=True (2.1s)
Sep 12 03:52:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:52:59,340 aiohttp.access INFO 216.218.206.109 [12/Sep/2026:03:52:59 +0000] "GET /?format=json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 12 03:53:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:10,721 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:53:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:15,789 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:53:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:18,100 aiohttp.access INFO 216.218.206.121 [12/Sep/2026:03:53:18 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 12 03:53:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:30,583 main INFO screen CANDLE pass=0 dev=0.0 ins=24.92 pro=36 1a=False 1b=False 2=True (20.0s)
Sep 12 03:53:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:38,547 aiohttp.access INFO 216.218.206.69 [12/Sep/2026:03:53:38 +0000] "GET /geoserver/web/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 12 03:53:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:43,966 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:53:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:53:49,039 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:54:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:03,630 main INFO screen FINDER pass=0 dev=0.0 ins=23.1 pro=62 1a=False 1b=False 2=True (19.7s)
Sep 12 03:54:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:10,369 main INFO screen $CAJUN pass=0 dev=0.69 ins=0.0 pro=2 1a=False 1b=False 2=True (1.9s)
Sep 12 03:54:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:14,943 main INFO screen SONJI pass=0 dev=0.0 ins=30.92 pro=19 1a=False 1b=True 2=True (2.3s)
Sep 12 03:54:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:28,559 main INFO screen puh  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 12 03:54:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:31,651 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:54:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:36,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:54:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:43,489 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:54:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:48,556 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:54:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:54:52,028 main INFO screen duve pass=0 dev=0.0 ins=24.79 pro=24 1a=False 1b=False 2=True (20.4s)
Sep 12 03:55:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:01,738 main INFO screen FCHUMP pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (18.3s)
Sep 12 03:55:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:08,562 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:55:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:09,996 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:55:09 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 03:55:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:15,910 main INFO screen CP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 12 03:55:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:31,830 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:55:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:55:38,096 main INFO screen duve pass=0 dev=6.63 ins=23.58 pro=24 1a=False 1b=False 2=True (6.4s)
Sep 12 03:56:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:07,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:09,000 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:12,553 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:14,070 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:28,200 main INFO screen popdog pass=0 dev=0.0 ins=16.93 pro=30 1a=False 1b=False 2=True (20.8s)
Sep 12 03:56:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:30,086 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.2s)
Sep 12 03:56:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:31,099 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:36,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:39,515 main INFO screen LMAO pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 12 03:56:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:39,606 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:56:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:44,702 main INFO screen TAGTEAM pass=0 dev=2.09 ins=0.0 pro=4 1a=False 1b=False 2=False (11.9s)
Sep 12 03:56:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:51,592 main INFO screen Chudette pass=0 dev=0.0 ins=15.88 pro=73 1a=False 1b=False 2=True (12.1s)
Sep 12 03:56:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:56:54,937 main INFO screen popdog pass=0 dev=0.0 ins=24.82 pro=32 1a=False 1b=False 2=True (23.9s)
Sep 12 03:57:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:57:03,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:57:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:57:11,691 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 03:57:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:57:40,925 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:57:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:57:48,179 main INFO screen 2centrust pass=0 dev=2.14 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 12 03:58:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:58:42,900 main INFO screen UPS pass=0 dev=0.0 ins=16.92 pro=44 1a=False 1b=False 2=True (2.9s)
Sep 12 03:59:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:02,243 main INFO screen STABLEB pass=0 dev=31.62 ins=0.0 pro=8 1a=False 1b=False 2=True (1.3s)
Sep 12 03:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:10,136 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (3.7s)
Sep 12 03:59:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:20,465 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:59:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:20,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:59:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:25,500 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:59:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:25,800 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:59:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:39,007 main INFO screen PENIS pass=0 dev=1.66 ins=24.79 pro=22 1a=False 1b=False 2=True (18.6s)
Sep 12 03:59:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:59:41,188 main INFO screen MIMI pass=0 dev=0.0 ins=20.9 pro=30 1a=False 1b=True 2=True (20.5s)
Sep 12 04:00:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:00:12,607 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:00:12 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T02:32:33Z
--- update 2026-09-12T02:37:36Z
--- update 2026-09-12T02:42:48Z
--- update 2026-09-12T02:47:52Z
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
