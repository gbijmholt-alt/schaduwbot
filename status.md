# Schaduwbot status

- tijd: 2026-09-12 16:55:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 3 hours, 8 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.8G/38G | geheugen: 860/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 25378, "tokens_in_memory": 6923, "msgs": 2717102, "trades": 681971, "creates": 7761, "decode_fail": 30620, "rpc_calls": 19531, "rpc_errors": 813, "sol_usd": 102.04558648337843, "open_positions": 26, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 16945 | 2396 | 14 | 2395 | 178 | 4220 | 12642 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 574 | 17% | 1.7% | +43.6% | -16.1% | -6.22% | 100% |
| dip35_V1_gescreend_fail | 4584 | 27% | 3.9% | +45.4% | -26.1% | -6.60% | 100% |
| dip35_V1_alle | 5690 | 26% | 4.1% | +44.7% | -25.4% | -6.85% | 100% |
| dip35_V2_gescreend_pass | 570 | 22% | 2.5% | +40.8% | -20.4% | -6.62% | 100% |
| dip35_V2_gescreend_fail | 4633 | 25% | 4.4% | +55.0% | -28.1% | -6.97% | 100% |
| dip35_V2_alle | 5648 | 25% | 4.6% | +52.3% | -27.8% | -7.83% | 100% |
| dip35_V3_gescreend_pass | 571 | 9% | 2.8% | +266.5% | -22.0% | +4.28% | 100% |
| dip35_V3_gescreend_fail | 4734 | 14% | 6.1% | +110.9% | -29.8% | -10.71% | 100% |
| dip35_V3_alle | 5701 | 13% | 6.1% | +114.9% | -29.4% | -10.27% | 100% |
| dip40_V1_gescreend_pass | 542 | 14% | 1.8% | +46.0% | -15.6% | -6.93% | 100% |
| dip40_V1_gescreend_fail | 4504 | 27% | 3.9% | +46.9% | -25.9% | -6.55% | 100% |
| dip40_V1_alle | 5464 | 26% | 4.0% | +46.8% | -25.2% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 539 | 17% | 2.2% | +43.6% | -19.5% | -8.49% | 100% |
| dip40_V2_gescreend_fail | 4529 | 25% | 4.3% | +54.8% | -28.1% | -7.02% | 100% |
| dip40_V2_alle | 5419 | 24% | 4.5% | +52.8% | -27.6% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 541 | 8% | 2.4% | +265.1% | -20.9% | +1.84% | 100% |
| dip40_V3_gescreend_fail | 4614 | 13% | 5.9% | +105.9% | -29.6% | -11.74% | 100% |
| dip40_V3_alle | 5469 | 13% | 5.9% | +110.5% | -29.1% | -11.31% | 100% |
| dip45_V1_gescreend_pass | 520 | 15% | 1.7% | +47.5% | -15.4% | -6.19% | 100% |
| dip45_V1_gescreend_fail | 4415 | 28% | 3.6% | +48.3% | -25.7% | -5.37% | 100% |
| dip45_V1_alle | 5285 | 26% | 3.6% | +48.3% | -25.0% | -5.80% | 100% |
| dip45_V2_gescreend_pass | 516 | 18% | 2.1% | +42.7% | -19.5% | -8.04% | 100% |
| dip45_V2_gescreend_fail | 4428 | 25% | 4.1% | +57.5% | -27.7% | -6.11% | 100% |
| dip45_V2_alle | 5240 | 24% | 4.1% | +55.9% | -27.3% | -6.99% | 100% |
| dip45_V3_gescreend_pass | 519 | 8% | 2.1% | +303.1% | -20.3% | +5.22% | 100% |
| dip45_V3_gescreend_fail | 4498 | 14% | 5.5% | +111.2% | -29.2% | -9.84% | 100% |
| dip45_V3_alle | 5282 | 13% | 5.5% | +118.1% | -28.6% | -9.26% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 448 | 15% | 4.9% | -9.04% | -11.8% tot -6.2% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3773 | 13% | 2.8% | -9.69% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 16:34:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:01,194 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:34:01 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:34:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:03,411 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 12 16:34:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:04,783 main INFO screen $GOAT pass=0 dev=12.49 ins=0.0 pro=3 1a=False 1b=False 2=False (4.9s)
Sep 12 16:34:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:05,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:34:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:07,225 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:34:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:15,319 main INFO screen PUMPCAT pass=0 dev=0.13 ins=0.0 pro=19 1a=False 1b=True 2=False (8.2s)
Sep 12 16:34:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:20,043 main INFO screen Lara pass=0 dev=0.0 ins=29.19 pro=36 1a=False 1b=False 2=True (19.8s)
Sep 12 16:34:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:47,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:34:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:52,102 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:35:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:35:05,413 main INFO screen faucat pass=0 dev=6.63 ins=72.68 pro=0 1a=False 1b=True 2=True (18.5s)
Sep 12 16:35:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:35:29,117 main INFO screen LAHA pass=0 dev=6.64 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 16:35:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:35:38,497 main INFO screen GPTGUY pass=0 dev=0.49 ins=0.0 pro=5 1a=False 1b=False 2=False (3.0s)
Sep 12 16:37:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:37:20,781 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:37:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:37:27,948 main INFO screen BIRDKICKS pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 12 16:38:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:38:31,227 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:38:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:38:36,297 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:38:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:38:52,136 main INFO screen $GOAT pass=0 dev=20.1 ins=0.0 pro=6 1a=False 1b=False 2=False (21.0s)
Sep 12 16:38:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:38:53,523 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:39:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:01,550 main INFO screen ︀ pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 12 16:39:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:01,751 main INFO screen sol pass=0 dev=1.43 ins=0.0 pro=3 1a=False 1b=False 2=False (4.8s)
Sep 12 16:39:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:18,103 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:39:18 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:39:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:34,464 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:39:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:38,444 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 16:39:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:41,977 main INFO screen $CAT pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 12 16:39:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:39:42,913 main INFO screen GOOSE pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 12 16:40:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:40:24,184 main INFO screen USMS pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 12 16:40:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:40:57,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:40:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:40:59,703 main INFO screen delusional pass=0 dev=0.0 ins=33.43 pro=30 1a=False 1b=False 2=True (3.6s)
Sep 12 16:41:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:41:02,677 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:41:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:41:17,544 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.3s)
Sep 12 16:42:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:42:45,957 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:42:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:42:52,639 main INFO screen CRT pass=0 dev=0.68 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 12 16:42:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:42:53,811 aiohttp.access INFO 94.154.43.31 [12/Sep/2026:16:42:53 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0"
Sep 12 16:44:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:10,407 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:44:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:15,480 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:44:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:18,172 main INFO screen PRCA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 12 16:44:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:22,036 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:44:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:27,106 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:44:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:29,706 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.4s)
Sep 12 16:44:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:37,058 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:44:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:44:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:44:44,021 main INFO screen DEBANK pass=0 dev=0.0 ins=51.17 pro=18 1a=False 1b=False 2=True (22.0s)
Sep 12 16:45:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:45:36,522 main INFO screen USMS pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.3s)
Sep 12 16:45:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:45:40,484 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:45:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:45:45,540 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:46:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:46:01,492 main INFO screen EYES pass=0 dev=0.0 ins=48.52 pro=19 1a=False 1b=False 2=True (21.0s)
Sep 12 16:46:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:46:03,411 main INFO screen DOOB pass=0 dev=8.46 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 12 16:46:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:46:47,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:46:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:46:54,645 main INFO screen BALL pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=True (7.1s)
Sep 12 16:47:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:47:21,216 main INFO screen LMAO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 12 16:47:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:47:23,552 main INFO screen Bagueton pass=0 dev=0.0 ins=29.11 pro=23 1a=False 1b=True 2=False (3.0s)
Sep 12 16:47:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:47:50,019 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:47:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:47:55,091 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:48:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:07,614 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:48:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:09,788 main INFO screen GEMI pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (19.8s)
Sep 12 16:48:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:10,913 main INFO screen $GTA6 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 12 16:48:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:11,038 main INFO screen delusional pass=0 dev=0.0 ins=34.51 pro=27 1a=False 1b=False 2=True (1.2s)
Sep 12 16:48:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:14,648 main INFO screen PUSSY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 12 16:48:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:48:59,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:49:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:49:04,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:49:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:49:17,741 main INFO screen BRAIN pass=0 dev=0.17 ins=48.04 pro=21 1a=False 1b=False 2=True (18.4s)
Sep 12 16:50:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:50:11,859 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:50:11 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:50:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:50:29,588 main INFO screen SIRIUSCHUM pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (5.2s)
Sep 12 16:50:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:50:30,519 main INFO screen BMS pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 12 16:51:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:51:13,488 main INFO screen BALL pass=0 dev=1.02 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 12 16:51:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:51:33,891 main INFO screen $GTA6 pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 12 16:52:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:52:07,275 main INFO screen LOLA pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 16:52:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:52:14,978 main INFO screen HERD pass=1 dev=0.0 ins=15.22 pro=24 1a=False 1b=False 2=False (4.2s)
Sep 12 16:52:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:52:17,261 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:52:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:52:22,335 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:53:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:53:18,229 main INFO screen BALL pass=0 dev=1.76 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 12 16:53:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:53:18,234 main INFO screen GS pass=0 dev=0.0 ins=17.11 pro=66 1a=False 1b=False 2=True (61.0s)
Sep 12 16:53:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:53:18,503 main INFO screen NASA pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=True 2=True (8.4s)
Sep 12 16:53:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:53:34,813 main INFO screen ALL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 16:53:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:53:52,206 main INFO screen HNKL pass=0 dev=0.73 ins=0.0 pro=6 1a=False 1b=False 2=False (2.4s)
Sep 12 16:54:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:54:02,502 main INFO screen Hedgehog pass=0 dev=0.0 ins=19.87 pro=57 1a=False 1b=False 2=True (3.7s)
Sep 12 16:54:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:54:29,939 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:54:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:54:35,028 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:54:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:54:50,345 main INFO screen PDT pass=0 dev=8.0 ins=36.25 pro=10 1a=False 1b=False 2=True (20.5s)
Sep 12 16:54:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:54:54,045 main INFO screen BALL pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (3.9s)
Sep 12 16:55:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:55:18,620 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:55:18 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T15:25:28Z
--- update 2026-09-12T15:30:35Z
--- update 2026-09-12T15:35:36Z
--- update 2026-09-12T15:41:04Z
--- update 2026-09-12T15:46:16Z
--- update 2026-09-12T15:51:36Z
--- update 2026-09-12T15:57:16Z
--- update 2026-09-12T16:02:16Z
--- update 2026-09-12T16:07:36Z
--- update 2026-09-12T16:13:17Z
--- update 2026-09-12T16:18:17Z
--- update 2026-09-12T16:23:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 734fe7fd71e047c5827569b33cc14ab3
analyses gestart (02faa7a55c91)
--- update 2026-09-12T16:28:48Z
--- update 2026-09-12T16:34:00Z
--- update 2026-09-12T16:39:17Z
--- update 2026-09-12T16:44:36Z
--- update 2026-09-12T16:50:10Z
--- update 2026-09-12T16:55:17Z
```

## Analyses (laatste 25 regels)
```
inactive
16:32:40 60027 tokens geladen
16:32:42   2000 tokens, 242311 trades, 44385 posities (2s)
16:32:44   4000 tokens, 480659 trades, 89480 posities (4s)
16:32:46   6000 tokens, 691725 trades, 129237 posities (6s)
16:32:48   8000 tokens, 930063 trades, 171480 posities (8s)
16:32:50   10000 tokens, 1158013 trades, 214886 posities (10s)
16:32:52   12000 tokens, 1397951 trades, 256831 posities (12s)
16:32:54   14000 tokens, 1652982 trades, 307793 posities (15s)
16:32:56   16000 tokens, 1890382 trades, 350350 posities (17s)
16:32:58   18000 tokens, 2118735 trades, 389193 posities (18s)
16:33:00   20000 tokens, 2363976 trades, 436311 posities (21s)
16:33:02   22000 tokens, 2582686 trades, 474654 posities (23s)
16:33:05   24000 tokens, 2844904 trades, 527964 posities (25s)
16:33:07   26000 tokens, 3086184 trades, 570567 posities (28s)
16:33:09   28000 tokens, 3312079 trades, 611146 posities (30s)
16:33:11   30000 tokens, 3535303 trades, 651231 posities (31s)
16:33:13   32000 tokens, 3763932 trades, 694079 posities (33s)
16:33:16   34000 tokens, 4017731 trades, 742207 posities (36s)
16:33:18   36000 tokens, 4259150 trades, 795214 posities (38s)
16:33:19 posities: 829213 uit 4407533 trades (40s)
16:33:29 172443 wallets gerekend
16:33:30 geluk-toets
16:34:03 persistentie
16:34:05 kopieer-simulatie
16:34:23 klaar in 103s -> /opt/schaduwbot/reports/wallets.md
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
