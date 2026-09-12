# Schaduwbot status

- tijd: 2026-09-12 15:51:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 2 hours, 4 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 790/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 21556, "tokens_in_memory": 5790, "msgs": 2164439, "trades": 554043, "creates": 5790, "decode_fail": 23870, "rpc_calls": 17143, "rpc_errors": 726, "sol_usd": 101.97410102891595, "open_positions": 37, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 15:35:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:10,684 main INFO screen FART pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 12 15:35:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:37,092 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:35:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:35:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:45,984 main INFO screen anorchia pass=0 dev=0.0 ins=19.77 pro=59 1a=False 1b=False 2=True (3.9s)
Sep 12 15:35:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:51,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:35:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:53,595 main INFO screen TITSLA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 12 15:35:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:58,510 main INFO screen TITSLA pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 15:36:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:05,244 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:10,023 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:10,314 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:18,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:18,791 main INFO screen TWC pass=0 dev=0.08 ins=0.0 pro=2 1a=False 1b=False 2=False (8.8s)
Sep 12 15:36:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:18,832 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:23,383 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:23,625 main INFO screen TCM pass=0 dev=0.17 ins=48.7 pro=15 1a=False 1b=False 2=True (18.4s)
Sep 12 15:36:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:23,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:36:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:25,934 main INFO screen BATON pass=0 dev=0.11 ins=0.35 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 12 15:36:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:41,489 main INFO screen dc pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=True (6.9s)
Sep 12 15:36:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:42,747 main INFO screen SOLFLY pass=1 dev=0.0 ins=5.61 pro=12 1a=False 1b=False 2=False (25.3s)
Sep 12 15:36:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:42,945 main INFO screen XDAO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.2s)
Sep 12 15:36:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:36:58,807 main INFO screen PPT pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 12 15:37:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:37:04,499 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:37:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:37:09,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:37:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:37:24,895 main INFO screen SOLFLY pass=0 dev=0.0 ins=29.15 pro=72 1a=False 1b=False 2=True (20.5s)
Sep 12 15:37:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:37:57,470 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:38:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:38:02,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:38:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:38:17,486 main INFO screen baton pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=True 2=True (20.1s)
Sep 12 15:38:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:38:24,399 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 15:39:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:39:21,289 main INFO screen TITSLA pass=0 dev=0.41 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 12 15:39:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:39:28,795 main INFO screen NOCAP pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 15:39:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:39:41,224 main INFO screen ALXA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 12 15:40:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:40:35,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:40:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:40:40,505 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:40:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:40:45,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:40:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:40:50,780 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:40:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:40:54,767 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.4s)
Sep 12 15:41:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:41:05,214 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:41:05 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:41:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:41:05,367 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 15:41:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:41:42,303 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 12 15:41:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:41:51,942 main INFO screen Migration pass=1 dev=3.47 ins=4.45 pro=44 1a=False 1b=False 2=False (3.4s)
Sep 12 15:42:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:42:14,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:42:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:42:19,575 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:42:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:42:26,320 main INFO screen LARP pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 12 15:42:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:42:33,793 main INFO screen GTA 6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.4s)
Sep 12 15:43:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:43:55,198 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:44:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:02,723 main INFO screen CASHLESS pass=1 dev=0.0 ins=16.06 pro=33 1a=False 1b=False 2=False (7.6s)
Sep 12 15:44:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:07,059 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:44:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:11,757 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:44:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:14,606 main INFO screen LARP pass=0 dev=6.64 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 12 15:44:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:17,999 main INFO screen Pleb pass=0 dev=5.05 ins=11.65 pro=17 1a=False 1b=False 2=True (6.3s)
Sep 12 15:44:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:32,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:44:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:44:40,995 main INFO screen Pumployed pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 12 15:45:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:45:07,580 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:45:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:45:12,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:45:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:45:16,146 main INFO screen BLACK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 15:45:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:45:27,264 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (19.8s)
Sep 12 15:45:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:45:39,025 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 12 15:46:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:46:17,079 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:46:17 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:46:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:46:56,996 main INFO screen CHAINWARS pass=0 dev=2.79 ins=1.76 pro=41 1a=False 1b=True 2=False (1.8s)
Sep 12 15:48:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:01,399 main INFO screen YT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 15:48:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:05,919 main INFO screen LOL pass=1 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (3.9s)
Sep 12 15:48:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:07,637 main INFO screen fg pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 12 15:48:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:21,181 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:48:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:26,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:48:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:29,266 main INFO screen BAH pass=0 dev=0.0 ins=9.55 pro=42 1a=False 1b=False 2=True (3.9s)
Sep 12 15:48:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:41,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:48:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:41,762 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.6s)
Sep 12 15:48:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:48:46,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:49:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:00,699 main INFO screen IF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 15:49:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:14,468 main INFO screen $20 pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 12 15:49:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:22,862 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 12 15:49:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:32,090 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:49:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:37,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:49:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:51,320 main INFO screen BlindCat pass=0 dev=3.26 ins=0.0 pro=64 1a=False 1b=False 2=True (4.2s)
Sep 12 15:49:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:49:51,344 main INFO screen EXIT pass=0 dev=0.17 ins=48.61 pro=17 1a=False 1b=False 2=True (19.3s)
Sep 12 15:50:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:50:36,388 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:50:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:50:44,599 main INFO screen Dihvidend pass=0 dev=0.0 ins=9.55 pro=33 1a=False 1b=False 2=True (8.3s)
Sep 12 15:50:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:50:49,116 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:50:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:50:54,178 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:51:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:51:08,971 main INFO screen faucat pass=0 dev=0.0 ins=21.65 pro=45 1a=False 1b=False 2=True (19.9s)
Sep 12 15:51:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:51:37,129 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:51:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T15:25:28Z
--- update 2026-09-12T15:30:35Z
--- update 2026-09-12T15:35:36Z
--- update 2026-09-12T15:41:04Z
--- update 2026-09-12T15:46:16Z
--- update 2026-09-12T15:51:36Z
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
