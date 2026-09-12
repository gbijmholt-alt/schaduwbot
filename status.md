# Schaduwbot status

- tijd: 2026-09-12 03:55:09 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 14 hours, 8 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1138/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 29701, "tokens_in_memory": 7310, "msgs": 5930024, "trades": 1080343, "creates": 10265, "decode_fail": 56330, "rpc_calls": 36571, "rpc_errors": 1493, "sol_usd": 101.56014171158513, "open_positions": 34, "log_all_trades": true}
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
Sep 12 03:40:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:40:57,136 main INFO screen Pepizzuh pass=0 dev=2.22 ins=0.0 pro=9 1a=False 1b=False 2=False (3.7s)
Sep 12 03:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:04,246 main INFO screen skipoo pass=0 dev=3.43 ins=0.0 pro=1 1a=False 1b=False 2=True (2.0s)
Sep 12 03:41:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:26,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:41:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:31,267 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:41:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:46,386 main INFO screen primed pass=0 dev=0.0 ins=20.35 pro=42 1a=False 1b=False 2=True (20.2s)
Sep 12 03:41:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:50,949 main INFO screen ANTHROJEW pass=0 dev=0.0 ins=35.14 pro=21 1a=True 1b=False 2=True (3.2s)
Sep 12 03:41:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:57,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:41:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:41:59,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:42:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:42:04,895 main INFO screen DERP pass=0 dev=1.69 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 12 03:42:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:42:07,868 main INFO screen STEEL pass=0 dev=1.92 ins=16.37 pro=35 1a=False 1b=False 2=True (8.6s)
Sep 12 03:42:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:42:13,685 main INFO screen skipoo pass=0 dev=2.42 ins=0.0 pro=1 1a=False 1b=False 2=True (1.9s)
Sep 12 03:42:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:42:32,845 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.9s)
Sep 12 03:42:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:42:47,126 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 03:43:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:43:12,385 main INFO screen Pepizza pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 12 03:43:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:43:56,826 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:44:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:02,978 main INFO screen MIMI pass=1 dev=0.0 ins=4.01 pro=22 1a=False 1b=False 2=False (1.8s)
Sep 12 03:44:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:04,024 main INFO screen popdog pass=0 dev=6.63 ins=21.59 pro=17 1a=False 1b=False 2=False (7.3s)
Sep 12 03:44:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:09,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:44:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:15,632 main INFO screen beer pass=0 dev=1.75 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 12 03:44:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:25,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:44:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:30,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:44:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:44,069 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:44:44 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 03:44:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:44:44,997 main INFO screen SBF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 03:45:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:45:11,478 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:45:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:45:16,550 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:45:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:45:31,458 main INFO screen commodity pass=0 dev=0.0 ins=13.96 pro=68 1a=False 1b=False 2=True (20.1s)
Sep 12 03:46:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:00,123 main INFO screen luvpeeza pass=0 dev=3.73 ins=0.0 pro=8 1a=False 1b=False 2=False (2.9s)
Sep 12 03:46:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:18,075 main INFO screen CATSOL pass=0 dev=0.7 ins=30.74 pro=21 1a=False 1b=True 2=True (2.1s)
Sep 12 03:46:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:20,439 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:46:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:46:25,508 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T02:27:33Z
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
```

## Analyses (laatste 25 regels)
```
active
01:53:00 grote spelers: saldo van 1359 wallets opgehaald
01:53:57 herkomst: 40 posities gekoppeld
01:53:58 klaar in 97s -> /opt/schaduwbot/reports/ledger.md
01:54:00   2000 nieuwe tokens doorgerekend
01:54:02 klaar in 4s: 11080 tokens, 2981 nieuw -> /opt/schaduwbot/reports/video_replay.md
01:54:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 01:54 UTC
01:54:02 45856 tokens geladen
01:54:04   2000 tokens, 253102 trades, 54428 posities (2s)
01:54:07   4000 tokens, 520825 trades, 111725 posities (5s)
01:54:09   6000 tokens, 782379 trades, 167557 posities (7s)
01:54:11   8000 tokens, 1054119 trades, 222555 posities (9s)
01:54:13   10000 tokens, 1329211 trades, 281413 posities (11s)
01:54:16   12000 tokens, 1594580 trades, 333921 posities (13s)
01:54:18   14000 tokens, 1836819 trades, 382990 posities (15s)
01:54:20   16000 tokens, 2119459 trades, 446339 posities (18s)
01:54:22   18000 tokens, 2395048 trades, 502642 posities (20s)
01:54:24   20000 tokens, 2629029 trades, 552671 posities (22s)
01:54:27   22000 tokens, 2903307 trades, 608372 posities (24s)
01:54:29 posities: 660394 uit 3108846 trades (26s)
01:54:37 148332 wallets gerekend
01:54:38 geluk-toets
01:55:03 persistentie
01:55:05 kopieer-simulatie
01:55:14 klaar in 72s -> /opt/schaduwbot/reports/wallets.md
03:55:09 23030 tokens sinds start volledige logging, waarvan 5134 met een gat door herstart
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
