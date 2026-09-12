# Schaduwbot status

- tijd: 2026-09-12 16:39:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 2 hours, 52 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.8G/38G | geheugen: 825/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 24417, "tokens_in_memory": 6824, "msgs": 2611034, "trades": 650714, "creates": 7432, "decode_fail": 29002, "rpc_calls": 18831, "rpc_errors": 793, "sol_usd": 101.94518852711005, "open_positions": 16, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 15042 | 2283 | 13 | 2283 | 172 | 3987 | 11945 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 567 | 17% | 1.8% | +43.6% | -16.1% | -6.25% | 100% |
| dip35_V1_gescreend_fail | 4514 | 27% | 3.9% | +45.3% | -26.0% | -6.62% | 100% |
| dip35_V1_alle | 5604 | 27% | 4.1% | +44.5% | -25.4% | -6.83% | 100% |
| dip35_V2_gescreend_pass | 564 | 23% | 2.5% | +40.8% | -20.5% | -6.56% | 100% |
| dip35_V2_gescreend_fail | 4566 | 26% | 4.4% | +55.0% | -28.1% | -6.90% | 100% |
| dip35_V2_alle | 5566 | 25% | 4.7% | +52.3% | -27.8% | -7.75% | 100% |
| dip35_V3_gescreend_pass | 565 | 9% | 2.8% | +266.5% | -22.1% | +4.50% | 100% |
| dip35_V3_gescreend_fail | 4669 | 14% | 6.1% | +110.2% | -29.8% | -10.76% | 100% |
| dip35_V3_alle | 5621 | 13% | 6.2% | +114.4% | -29.4% | -10.27% | 100% |
| dip40_V1_gescreend_pass | 535 | 14% | 1.9% | +45.9% | -15.6% | -7.09% | 100% |
| dip40_V1_gescreend_fail | 4440 | 27% | 3.9% | +46.8% | -25.9% | -6.57% | 100% |
| dip40_V1_alle | 5384 | 26% | 4.0% | +46.7% | -25.2% | -6.84% | 100% |
| dip40_V2_gescreend_pass | 533 | 17% | 2.3% | +44.0% | -19.5% | -8.45% | 100% |
| dip40_V2_gescreend_fail | 4466 | 25% | 4.3% | +54.8% | -28.0% | -6.99% | 100% |
| dip40_V2_alle | 5341 | 24% | 4.5% | +52.9% | -27.6% | -8.00% | 100% |
| dip40_V3_gescreend_pass | 535 | 8% | 2.4% | +265.1% | -20.9% | +2.05% | 100% |
| dip40_V3_gescreend_fail | 4555 | 13% | 5.9% | +105.1% | -29.6% | -11.84% | 100% |
| dip40_V3_alle | 5395 | 13% | 5.9% | +109.9% | -29.1% | -11.35% | 100% |
| dip45_V1_gescreend_pass | 515 | 14% | 1.7% | +47.5% | -15.4% | -6.33% | 100% |
| dip45_V1_gescreend_fail | 4351 | 28% | 3.5% | +48.2% | -25.7% | -5.36% | 100% |
| dip45_V1_alle | 5209 | 26% | 3.6% | +48.3% | -24.9% | -5.76% | 100% |
| dip45_V2_gescreend_pass | 512 | 18% | 2.1% | +43.0% | -19.5% | -8.03% | 100% |
| dip45_V2_gescreend_fail | 4367 | 25% | 4.1% | +57.6% | -27.7% | -6.02% | 100% |
| dip45_V2_alle | 5168 | 24% | 4.1% | +56.0% | -27.2% | -6.89% | 100% |
| dip45_V3_gescreend_pass | 515 | 8% | 2.1% | +303.1% | -20.4% | +5.39% | 100% |
| dip45_V3_gescreend_fail | 4440 | 14% | 5.5% | +112.1% | -29.1% | -9.68% | 100% |
| dip45_V3_alle | 5213 | 13% | 5.5% | +119.0% | -28.6% | -9.08% | 100% |

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
| per_token_met_xlink | 443 | 15% | 5.0% | -9.10% | -11.9% tot -6.3% | -14.3% | – | 100% |
| per_token_zonder_xlink | 127 | 20% | 0.0% | +18.90% | -12.8% tot +50.6% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3737 | 13% | 2.8% | -9.68% | -10.9% tot -8.4% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1104 | 18% | 0.0% | +17.83% | +0.1% tot +35.5% | -14.4% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 16:16:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:16:26,468 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:16:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:16:31,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:16:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:16:52,104 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:16:16:52 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 16:16:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:16:52,456 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:16:16:52 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 16:16:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:16:53,134 main INFO screen CTO pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (26.8s)
Sep 12 16:18:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:18:02,700 main INFO screen BPCATE pass=0 dev=3.42 ins=0.0 pro=2 1a=False 1b=False 2=False (11.5s)
Sep 12 16:18:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:18:07,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:18:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:18:12,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:18:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:18:18,953 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:18:18 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 16:18:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:18:34,922 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (27.6s)
Sep 12 16:19:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:19:13,927 main INFO screen EPORK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 12 16:20:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:20:53,992 main INFO screen BALL pass=0 dev=0.26 ins=0.0 pro=3 1a=False 1b=False 2=False (11.4s)
Sep 12 16:21:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:21:31,358 main INFO screen ZORP pass=0 dev=0.0 ins=22.64 pro=42 1a=False 1b=False 2=True (2.8s)
Sep 12 16:22:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:22:06,402 main INFO screen $GOAT pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (10.8s)
Sep 12 16:22:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:22:17,504 main INFO screen wind pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 12 16:22:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:22:24,180 main INFO screen FOLD pass=0 dev=1.16 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 12 16:23:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:23:16,639 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 12 16:23:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:23:21,491 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:23:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:23:33,742 main INFO screen DOOB pass=0 dev=12.49 ins=0.0 pro=5 1a=False 1b=False 2=False (12.3s)
Sep 12 16:23:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:23:37,119 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:23:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:24:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:24:39,970 main INFO screen AVN pass=1 dev=0.03 ins=0.0 pro=42 1a=False 1b=False 2=False (9.7s)
Sep 12 16:24:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:24:52,802 main INFO screen flytchua pass=0 dev=0.0 ins=29.12 pro=21 1a=False 1b=False 2=False (10.4s)
Sep 12 16:24:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:24:59,655 main INFO screen Locaton pass=0 dev=1.57 ins=24.36 pro=20 1a=False 1b=True 2=False (7.1s)
Sep 12 16:25:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:25:12,179 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:16:25:12 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 16:25:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:25:15,039 main INFO screen RTW pass=0 dev=9.66 ins=0.0 pro=5 1a=False 1b=False 2=False (9.6s)
Sep 12 16:25:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:25:16,138 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:25:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:25:21,202 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:25:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:25:39,335 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.3s)
Sep 12 16:26:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:26:29,718 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.3s)
Sep 12 16:26:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:26:35,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:26:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:26:40,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:26:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:26:55,802 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:27:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:27:01,666 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (26.1s)
Sep 12 16:27:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:27:08,508 main INFO screen LMAO pass=0 dev=0.87 ins=0.0 pro=3 1a=False 1b=False 2=True (12.8s)
Sep 12 16:28:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:28:16,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:28:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:28:21,672 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:28:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:28:39,702 main INFO screen GEMI pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (23.2s)
Sep 12 16:28:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:28:49,972 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:28:49 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:29:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:29:12,941 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:29:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:29:15,922 main INFO screen CAJUN pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=True (7.2s)
Sep 12 16:29:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:29:27,225 main INFO screen GARP pass=0 dev=6.64 ins=0.0 pro=4 1a=False 1b=False 2=False (14.4s)
Sep 12 16:29:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:29:30,175 main INFO screen JCAT pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 12 16:30:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:30:46,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:31:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:01,031 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:31:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:01,663 main INFO screen ROCK pass=0 dev=0.23 ins=0.0 pro=3 1a=False 1b=False 2=False (9.8s)
Sep 12 16:31:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:04,197 main INFO screen MDS pass=0 dev=6.64 ins=0.0 pro=5 1a=False 1b=False 2=False (17.7s)
Sep 12 16:31:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:06,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:31:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:21,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:31:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:26,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:31:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:26,712 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (25.8s)
Sep 12 16:31:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:40,544 main INFO screen Stockwork pass=0 dev=4.07 ins=29.76 pro=34 1a=False 1b=False 2=True (19.2s)
Sep 12 16:31:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:50,801 main INFO screen monster pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.1s)
Sep 12 16:31:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:31:57,565 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:32:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:32:02,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:32:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:32:15,992 main INFO screen Lemur coin pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 12 16:32:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:32:16,041 main INFO screen CRT pass=1 dev=2.75 ins=0.0 pro=33 1a=False 1b=False 2=False (10.5s)
Sep 12 16:32:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:32:23,584 main INFO screen $GOAT pass=0 dev=9.64 ins=0.0 pro=3 1a=False 1b=False 2=False (26.1s)
Sep 12 16:32:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:32:33,400 main INFO screen meme pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 12 16:34:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:34:00,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T15:09:30Z
--- update 2026-09-12T15:14:35Z
--- update 2026-09-12T15:19:36Z
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
