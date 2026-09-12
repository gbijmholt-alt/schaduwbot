# Schaduwbot status

- tijd: 2026-09-12 15:19:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 1 hour, 32 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 754/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 19637, "tokens_in_memory": 5078, "msgs": 1833654, "trades": 487881, "creates": 5078, "decode_fail": 21048, "rpc_calls": 15253, "rpc_errors": 657, "sol_usd": 102.11028564182442, "open_positions": 34, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 13772 | 2124 | 13 | 2122 | 154 | 3717 | 11131 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 554 | 17% | 1.8% | +43.7% | -16.3% | -6.30% | 100% |
| dip35_V1_gescreend_fail | 4444 | 27% | 3.9% | +45.3% | -26.0% | -6.57% | 100% |
| dip35_V1_alle | 5510 | 26% | 4.1% | +44.6% | -25.4% | -6.83% | 100% |
| dip35_V2_gescreend_pass | 551 | 23% | 2.5% | +41.4% | -20.6% | -6.51% | 100% |
| dip35_V2_gescreend_fail | 4489 | 25% | 4.4% | +55.0% | -28.0% | -6.96% | 100% |
| dip35_V2_alle | 5468 | 25% | 4.7% | +52.4% | -27.8% | -7.81% | 100% |
| dip35_V3_gescreend_pass | 551 | 9% | 2.9% | +273.8% | -22.1% | +4.74% | 100% |
| dip35_V3_gescreend_fail | 4591 | 14% | 6.2% | +111.5% | -29.7% | -10.68% | 100% |
| dip35_V3_alle | 5524 | 13% | 6.2% | +115.8% | -29.4% | -10.19% | 100% |
| dip40_V1_gescreend_pass | 522 | 14% | 1.9% | +45.9% | -15.7% | -6.93% | 100% |
| dip40_V1_gescreend_fail | 4374 | 26% | 3.8% | +47.0% | -25.8% | -6.53% | 100% |
| dip40_V1_alle | 5295 | 26% | 4.0% | +46.9% | -25.2% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 520 | 18% | 2.3% | +44.3% | -19.7% | -8.34% | 100% |
| dip40_V2_gescreend_fail | 4393 | 25% | 4.3% | +55.0% | -28.0% | -7.03% | 100% |
| dip40_V2_alle | 5248 | 24% | 4.5% | +53.1% | -27.6% | -8.03% | 100% |
| dip40_V3_gescreend_pass | 521 | 8% | 2.5% | +265.1% | -21.0% | +2.57% | 100% |
| dip40_V3_gescreend_fail | 4481 | 13% | 6.0% | +106.1% | -29.6% | -11.73% | 100% |
| dip40_V3_alle | 5303 | 13% | 6.0% | +110.9% | -29.1% | -11.22% | 100% |
| dip45_V1_gescreend_pass | 501 | 15% | 1.8% | +47.7% | -15.5% | -6.29% | 100% |
| dip45_V1_gescreend_fail | 4290 | 27% | 3.5% | +48.3% | -25.6% | -5.34% | 100% |
| dip45_V1_alle | 5127 | 26% | 3.5% | +48.5% | -24.9% | -5.77% | 100% |
| dip45_V2_gescreend_pass | 498 | 18% | 2.2% | +43.2% | -19.6% | -8.13% | 100% |
| dip45_V2_gescreend_fail | 4301 | 25% | 4.0% | +57.7% | -27.7% | -6.02% | 100% |
| dip45_V2_alle | 5083 | 24% | 4.1% | +56.2% | -27.2% | -6.92% | 100% |
| dip45_V3_gescreend_pass | 501 | 8% | 2.2% | +308.2% | -20.5% | +5.75% | 100% |
| dip45_V3_gescreend_fail | 4372 | 14% | 5.5% | +112.9% | -29.1% | -9.51% | 100% |
| dip45_V3_alle | 5129 | 13% | 5.5% | +120.0% | -28.6% | -8.93% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 431 | 15% | 5.1% | -9.12% | -12.0% tot -6.2% | -14.3% | – | 100% |
| per_token_zonder_xlink | 126 | 21% | 0.0% | +19.17% | -12.8% tot +51.1% | -13.2% | 128% | 54% |
| gepoold_met_xlink | 3624 | 13% | 2.9% | -9.71% | -11.0% tot -8.4% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1095 | 18% | 0.0% | +18.09% | +0.2% tot +35.9% | -14.4% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 15:01:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:01:44,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:01:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:01:49,528 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:02:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:02:08,015 main INFO screen GOAP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (23.7s)
Sep 12 15:02:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:02:26,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:02:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:02:35,141 main INFO screen HUMANITY pass=0 dev=0.0 ins=17.39 pro=55 1a=False 1b=False 2=True (9.1s)
Sep 12 15:03:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:03:22,446 main INFO screen PAPI pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 12 15:03:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:03:37,114 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:03:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:04:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:00,587 main INFO screen FRONTIER pass=1 dev=0.1 ins=2.63 pro=41 1a=False 1b=False 2=False (7.2s)
Sep 12 15:04:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:16,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:04:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:33,808 main INFO screen BILLY pass=1 dev=0.0 ins=14.34 pro=21 1a=False 1b=False 2=False (7.6s)
Sep 12 15:04:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:34,274 main INFO screen IQ pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (18.2s)
Sep 12 15:04:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:46,378 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:04:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:04:51,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:05:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:09,103 main INFO screen INU pass=0 dev=0.0 ins=25.28 pro=29 1a=False 1b=False 2=True (22.8s)
Sep 12 15:05:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:10,414 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:05:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:14,939 main INFO screen Baton pass=0 dev=0.08 ins=0.35 pro=2 1a=False 1b=False 2=False (10.8s)
Sep 12 15:05:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:17,629 main INFO screen BILLY pass=0 dev=0.36 ins=0.0 pro=3 1a=False 1b=False 2=False (7.3s)
Sep 12 15:05:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:18,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:05:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:23,393 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:05:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:41,375 main INFO screen Prospect pass=0 dev=0.0 ins=39.75 pro=44 1a=False 1b=False 2=True (23.1s)
Sep 12 15:05:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:05:48,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:06:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:02,769 main INFO screen DOOB pass=0 dev=7.51 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 12 15:06:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:03,571 main INFO screen Baton pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (15.6s)
Sep 12 15:06:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:17,310 aiohttp.access INFO 194.88.98.87 [12/Sep/2026:15:06:17 +0000] "GET /zc?action=getInfo HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,024 aiohttp.access INFO 69.5.169.20 [12/Sep/2026:15:06:25 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,068 aiohttp.access INFO 69.5.169.93 [12/Sep/2026:15:06:25 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,082 aiohttp.access INFO 69.5.169.120 [12/Sep/2026:15:06:25 +0000] "GET /mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,083 aiohttp.access INFO 69.5.169.38 [12/Sep/2026:15:06:25 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,084 aiohttp.access INFO 69.5.169.110 [12/Sep/2026:15:06:25 +0000] "GET /mcp/ HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,085 aiohttp.access INFO 69.5.169.61 [12/Sep/2026:15:06:25 +0000] "GET /api/mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:25,098 aiohttp.access INFO 69.5.169.80 [12/Sep/2026:15:06:25 +0000] "GET /sse HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 15:06:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:06:57,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:07:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:07:02,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:07:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:07:20,858 main INFO screen PONYX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (23.6s)
Sep 12 15:07:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:07:37,233 main INFO screen WAGARI pass=0 dev=2.42 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 12 15:07:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:07:50,270 main INFO screen Paperhands pass=1 dev=0.0 ins=0.58 pro=58 1a=False 1b=False 2=False (3.3s)
Sep 12 15:08:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:08:32,516 main INFO screen PIGEON pass=0 dev=1.1 ins=0.0 pro=2 1a=False 1b=False 2=False (6.0s)
Sep 12 15:09:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:01,198 main INFO screen ALL pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 12 15:09:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:06,389 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (10.1s)
Sep 12 15:09:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:30,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:09:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:31,595 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:09:31 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:09:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:35,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:09:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:54,866 main INFO screen sentryrun pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 12 15:09:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:09:57,198 main INFO screen EDWARD pass=0 dev=0.0 ins=48.2 pro=45 1a=False 1b=False 2=True (26.9s)
Sep 12 15:10:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:10:48,591 main INFO screen HGI pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 12 15:11:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:11:23,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:11:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:11:37,637 main INFO screen sentryrun pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (14.4s)
Sep 12 15:11:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:11:48,087 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:11:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:11:52,698 main INFO screen Clanker pass=1 dev=0.0 ins=0.0 pro=54 1a=False 1b=False 2=False (3.5s)
Sep 12 15:11:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:11:53,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:12:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:12:12,689 main INFO screen FOMOBRAIN pass=0 dev=0.0 ins=79.31 pro=5 1a=False 1b=True 2=True (24.7s)
Sep 12 15:13:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:13:24,402 main INFO screen fone pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 12 15:14:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:14:35,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:14:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:14:36,379 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:14:36 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 15:14:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:14:40,139 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:14:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:14:43,336 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:15:14:43 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 15:14:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:14:43,686 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:15:14:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 15:15:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:00,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:15:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:00,963 main INFO screen Trafigura pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 12 15:15:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:05,986 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:15:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:26,391 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (25.5s)
Sep 12 15:15:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:27,248 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:15:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:32,276 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:15:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:45,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:15:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:50,323 main INFO screen ROBIN pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=True 2=True (23.1s)
Sep 12 15:15:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:55,004 main INFO screen Human pass=0 dev=0.0 ins=10.31 pro=56 1a=False 1b=False 2=True (9.4s)
Sep 12 15:15:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:15:59,806 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:16:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:16:04,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:16:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:16:25,938 main INFO screen trenchcat pass=0 dev=0.0 ins=49.24 pro=32 1a=False 1b=False 2=True (26.2s)
Sep 12 15:16:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:16:28,536 main INFO screen YFF pass=0 dev=2.08 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 12 15:16:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:16:39,185 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:16:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:16:44,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:17:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:17:05,791 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.7s)
Sep 12 15:17:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:17:58,545 main INFO screen CHUMP pass=0 dev=0.42 ins=0.0 pro=6 1a=False 1b=False 2=False (3.1s)
Sep 12 15:18:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:18:27,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:18:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:18:32,765 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:18:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:18:48,428 main INFO screen zVeil pass=0 dev=0.0 ins=19.6 pro=32 1a=False 1b=False 2=True (5.9s)
Sep 12 15:18:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:18:49,711 main INFO screen BINGUS pass=0 dev=5.05 ins=11.65 pro=34 1a=False 1b=False 2=False (3.1s)
Sep 12 15:18:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:18:50,931 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (23.3s)
Sep 12 15:19:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:19:37,157 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:19:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 367f286af9504770be86685502142335
analyses gestart (6b9b2315b322)
--- update 2026-09-12T14:10:11Z
nieuwe code: f76b0ba
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-12T14:15:36Z
--- update 2026-09-12T14:21:31Z
Running as unit: schaduwbot-wallets.service; invocation ID: 231ef89f1987467a9f6d8d397018c1e2
analyses gestart (02faa7a55c91)
--- update 2026-09-12T14:26:36Z
--- update 2026-09-12T14:31:58Z
--- update 2026-09-12T14:37:10Z
--- update 2026-09-12T14:42:26Z
--- update 2026-09-12T14:47:36Z
--- update 2026-09-12T14:53:12Z
--- update 2026-09-12T14:58:35Z
--- update 2026-09-12T15:03:36Z
--- update 2026-09-12T15:09:30Z
--- update 2026-09-12T15:14:35Z
--- update 2026-09-12T15:19:36Z
```

## Analyses (laatste 25 regels)
```
inactive
14:30:30 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 14:30 UTC
14:30:31 56838 tokens geladen
14:30:33   2000 tokens, 252349 trades, 49514 posities (2s)
14:30:35   4000 tokens, 494608 trades, 94985 posities (5s)
14:30:37   6000 tokens, 722751 trades, 137824 posities (7s)
14:30:39   8000 tokens, 957929 trades, 180570 posities (9s)
14:30:41   10000 tokens, 1190181 trades, 224203 posities (11s)
14:30:44   12000 tokens, 1452487 trades, 275238 posities (13s)
14:30:46   14000 tokens, 1716989 trades, 330574 posities (15s)
14:30:48   16000 tokens, 1938904 trades, 366489 posities (17s)
14:30:50   18000 tokens, 2198218 trades, 418143 posities (20s)
14:30:52   20000 tokens, 2430685 trades, 460461 posities (22s)
14:30:55   22000 tokens, 2695330 trades, 514894 posities (24s)
14:30:57   24000 tokens, 2940087 trades, 559865 posities (26s)
14:30:59   26000 tokens, 3170067 trades, 601122 posities (28s)
14:31:01   28000 tokens, 3403030 trades, 644659 posities (30s)
14:31:03   30000 tokens, 3646890 trades, 692146 posities (33s)
14:31:05   32000 tokens, 3903989 trades, 741913 posities (35s)
14:31:07   34000 tokens, 4145830 trades, 798529 posities (37s)
14:31:08 posities: 805880 uit 4173971 trades (37s)
14:31:18 168398 wallets gerekend
14:31:18 geluk-toets
14:31:51 persistentie
14:31:54 kopieer-simulatie
14:32:06 klaar in 95s -> /opt/schaduwbot/reports/wallets.md
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
