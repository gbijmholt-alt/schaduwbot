# Schaduwbot status

- tijd: 2026-09-12 11:53:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 22 hours, 6 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.6G/38G | geheugen: 621/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 7277, "tokens_in_memory": 1610, "msgs": 563788, "trades": 150079, "creates": 1610, "decode_fail": 5889, "rpc_calls": 4291, "rpc_errors": 191, "sol_usd": 102.02913338496016, "open_positions": 33, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 10828 | 1662 | 8 | 1662 | 115 | 2907 | 8717 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 520 | 16% | 1.9% | +43.9% | -16.5% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 4248 | 27% | 3.8% | +45.8% | -25.8% | -6.54% | 100% |
| dip35_V1_alle | 5232 | 26% | 4.0% | +45.1% | -25.2% | -6.77% | 100% |
| dip35_V2_gescreend_pass | 516 | 22% | 2.7% | +42.6% | -20.9% | -6.75% | 100% |
| dip35_V2_gescreend_fail | 4289 | 25% | 4.3% | +56.0% | -27.9% | -6.81% | 100% |
| dip35_V2_alle | 5191 | 25% | 4.6% | +53.4% | -27.7% | -7.62% | 100% |
| dip35_V3_gescreend_pass | 517 | 9% | 3.1% | +273.0% | -22.2% | +4.59% | 100% |
| dip35_V3_gescreend_fail | 4385 | 14% | 6.0% | +115.0% | -29.6% | -10.03% | 100% |
| dip35_V3_alle | 5245 | 13% | 6.1% | +119.0% | -29.2% | -9.61% | 100% |
| dip40_V1_gescreend_pass | 488 | 14% | 2.0% | +46.1% | -15.8% | -6.83% | 100% |
| dip40_V1_gescreend_fail | 4181 | 26% | 3.7% | +47.3% | -25.7% | -6.42% | 100% |
| dip40_V1_alle | 5029 | 25% | 3.9% | +47.4% | -25.0% | -6.64% | 100% |
| dip40_V2_gescreend_pass | 486 | 18% | 2.5% | +45.4% | -19.9% | -8.18% | 100% |
| dip40_V2_gescreend_fail | 4198 | 25% | 4.2% | +55.5% | -27.9% | -6.91% | 100% |
| dip40_V2_alle | 4984 | 24% | 4.4% | +53.8% | -27.5% | -7.81% | 100% |
| dip40_V3_gescreend_pass | 488 | 8% | 2.7% | +275.2% | -21.1% | +3.17% | 100% |
| dip40_V3_gescreend_fail | 4282 | 13% | 5.8% | +109.1% | -29.4% | -11.07% | 100% |
| dip40_V3_alle | 5037 | 13% | 5.8% | +114.5% | -29.0% | -10.55% | 100% |
| dip45_V1_gescreend_pass | 469 | 15% | 1.9% | +47.8% | -15.7% | -6.20% | 100% |
| dip45_V1_gescreend_fail | 4096 | 27% | 3.3% | +48.5% | -25.4% | -5.17% | 100% |
| dip45_V1_alle | 4866 | 26% | 3.4% | +48.8% | -24.7% | -5.54% | 100% |
| dip45_V2_gescreend_pass | 465 | 19% | 2.4% | +43.0% | -19.8% | -7.78% | 100% |
| dip45_V2_gescreend_fail | 4104 | 25% | 3.8% | +58.2% | -27.5% | -5.72% | 100% |
| dip45_V2_alle | 4822 | 24% | 4.0% | +56.9% | -27.1% | -6.52% | 100% |
| dip45_V3_gescreend_pass | 469 | 8% | 2.3% | +317.5% | -20.5% | +6.85% | 100% |
| dip45_V3_gescreend_fail | 4173 | 14% | 5.4% | +113.9% | -28.9% | -8.90% | 100% |
| dip45_V3_alle | 4867 | 13% | 5.3% | +122.0% | -28.4% | -8.25% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 406 | 15% | 5.4% | -9.25% | -12.3% tot -6.2% | -14.6% | – | 100% |
| per_token_zonder_xlink | 117 | 20% | 0.0% | +20.37% | -14.0% tot +54.7% | -13.2% | 130% | 54% |
| gepoold_met_xlink | 3404 | 13% | 3.1% | -9.91% | -11.2% tot -8.6% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1014 | 19% | 0.0% | +19.84% | +0.6% tot +39.1% | -14.3% | 69% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 11:31:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:01,435 main INFO screen kikmi pass=0 dev=0.12 ins=0.0 pro=1 1a=False 1b=False 2=False (5.4s)
Sep 12 11:31:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:08,745 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:13,820 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:32,816 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:32,993 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.3s)
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,892 aiohttp.access INFO 194.187.176.92 [12/Sep/2026:11:31:37 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,924 aiohttp.access INFO 194.187.176.67 [12/Sep/2026:11:31:37 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
Sep 12 11:31:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:57,646 main INFO screen BATONUSD pass=0 dev=0.19 ins=79.12 pro=9 1a=True 1b=True 2=True (24.9s)
Sep 12 11:32:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:32:20,807 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:32:20 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:34:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:34:37,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:34:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:34:45,926 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (3.5s)
Sep 12 11:34:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:34:46,451 main INFO screen LaMisery pass=0 dev=0.46 ins=0.0 pro=1 1a=False 1b=False 2=False (8.8s)
Sep 12 11:34:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:34:57,998 main INFO screen fuelcoin pass=1 dev=0.0 ins=5.99 pro=38 1a=False 1b=False 2=False (3.0s)
Sep 12 11:36:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:36:06,185 main INFO screen peDisguys pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.6s)
Sep 12 11:36:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:36:49,424 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:36:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:36:54,491 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:37:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:37:07,768 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:37:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:37:10,427 main INFO screen COIN pass=0 dev=15.85 ins=2.79 pro=82 1a=False 1b=False 2=False (21.1s)
Sep 12 11:37:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:37:12,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:37:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:37:27,718 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.5s)
Sep 12 11:37:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:37:37,119 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:37:37 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:38:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:38:16,695 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:38:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:38:20,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:38:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:38:21,772 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:38:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:38:29,262 main INFO screen gascoin pass=0 dev=0.0 ins=11.48 pro=36 1a=False 1b=False 2=True (8.8s)
Sep 12 11:38:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:38:34,990 main INFO screen RWIF pass=0 dev=0.07 ins=79.24 pro=8 1a=False 1b=True 2=True (18.4s)
Sep 12 11:39:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:39:15,525 main INFO screen Awnım pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 12 11:39:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:39:30,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:39:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:39:35,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:39:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:39:51,705 main INFO screen gas pass=0 dev=0.0 ins=16.53 pro=61 1a=False 1b=False 2=True (21.1s)
Sep 12 11:39:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:39:58,158 main INFO screen NUTS pass=0 dev=0.0 ins=19.49 pro=45 1a=False 1b=False 2=True (1.3s)
Sep 12 11:40:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:26,142 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:31,220 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:35,323 main INFO screen Micromeme pass=1 dev=0.0 ins=9.35 pro=23 1a=False 1b=False 2=False (3.7s)
Sep 12 11:40:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:38,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:43,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:44,293 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:45,368 main INFO screen GBNHVN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (19.3s)
Sep 12 11:40:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:45,456 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:48,982 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:50,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:40:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:58,657 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 11:40:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:40:59,587 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:41:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:03,792 main INFO screen CLOUD pass=0 dev=0.0 ins=22.75 pro=36 1a=False 1b=False 2=True (20.1s)
Sep 12 11:41:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:04,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:41:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:05,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:41:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:06,667 main INFO screen pair pass=0 dev=0.0 ins=21.38 pro=66 1a=False 1b=False 2=True (21.3s)
Sep 12 11:41:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:09,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:41:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:21,213 main INFO screen WALLY pass=0 dev=0.36 ins=46.92 pro=14 1a=False 1b=True 2=True (21.7s)
Sep 12 11:41:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:41:23,659 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.9s)
Sep 12 11:42:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:42:38,006 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:42:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:42:43,034 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:42:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:42:57,437 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.5s)
Sep 12 11:43:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:43:15,178 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:11:43:15 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 11:43:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:43:21,380 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:43:21 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:46:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:05,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:46:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:05,769 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:46:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:10,227 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:46:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:10,837 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:46:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:25,871 main INFO screen werld pass=0 dev=0.0 ins=20.6 pro=33 1a=False 1b=False 2=True (20.8s)
Sep 12 11:46:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:27,540 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.8s)
Sep 12 11:46:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:46:34,327 main INFO screen PLATFORM pass=1 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=False (2.9s)
Sep 12 11:47:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:47:28,973 main INFO screen Entropy pass=0 dev=0.0 ins=19.97 pro=45 1a=False 1b=True 2=True (1.4s)
Sep 12 11:48:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:48:21,541 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:48:21 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:48:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:48:41,279 main INFO screen TOAD pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 12 11:48:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:48:57,615 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:49:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:02,643 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:49:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:08,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:49:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:13,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:49:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:16,823 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.3s)
Sep 12 11:49:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:27,627 main INFO screen FlyGPT pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (19.7s)
Sep 12 11:49:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:49:30,481 main INFO screen mmrich pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (3.5s)
Sep 12 11:51:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:51:19,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:51:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:51:24,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:51:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:51:41,511 main INFO screen . pass=0 dev=1.01 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 12 11:51:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:51:41,555 main INFO screen BFD pass=0 dev=2.08 ins=55.38 pro=19 1a=False 1b=False 2=True (22.3s)
Sep 12 11:53:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:53:19,527 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.3s)
Sep 12 11:53:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:53:20,774 main INFO screen LETSGETUP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 12 11:53:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:53:37,152 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:53:37 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T10:13:22Z
--- update 2026-09-12T10:18:22Z
--- update 2026-09-12T10:23:36Z
--- update 2026-09-12T10:29:22Z
--- update 2026-09-12T10:34:36Z
--- update 2026-09-12T10:39:55Z
--- update 2026-09-12T10:45:23Z
--- update 2026-09-12T10:50:23Z
--- update 2026-09-12T10:55:36Z
--- update 2026-09-12T11:01:03Z
--- update 2026-09-12T11:06:18Z
--- update 2026-09-12T11:11:18Z
--- update 2026-09-12T11:16:36Z
--- update 2026-09-12T11:21:57Z
--- update 2026-09-12T11:27:19Z
--- update 2026-09-12T11:32:19Z
--- update 2026-09-12T11:37:36Z
--- update 2026-09-12T11:43:20Z
--- update 2026-09-12T11:48:20Z
--- update 2026-09-12T11:53:36Z
```

## Analyses (laatste 25 regels)
```
inactive
10:06:09 klaar (813 rpc-calls, 2 fouten)
10:06:12 klaar in 2s: 16508 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
10:06:12 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 10:06 UTC
10:06:12 52895 tokens geladen
10:06:15   2000 tokens, 247058 trades, 50537 posities (3s)
10:06:18   4000 tokens, 492472 trades, 99641 posities (6s)
10:06:21   6000 tokens, 735209 trades, 145534 posities (9s)
10:06:24   8000 tokens, 976677 trades, 193839 posities (12s)
10:06:26   10000 tokens, 1228727 trades, 240802 posities (15s)
10:06:29   12000 tokens, 1497671 trades, 298929 posities (17s)
10:06:32   14000 tokens, 1735520 trades, 339333 posities (20s)
10:06:35   16000 tokens, 1986175 trades, 387978 posities (23s)
10:06:37   18000 tokens, 2228897 trades, 433810 posities (25s)
10:06:40   20000 tokens, 2503151 trades, 490567 posities (28s)
10:06:43   22000 tokens, 2748558 trades, 535570 posities (31s)
10:06:46   24000 tokens, 2992686 trades, 583437 posities (34s)
10:06:48   26000 tokens, 3220982 trades, 627232 posities (36s)
10:06:51   28000 tokens, 3479029 trades, 676463 posities (39s)
10:06:54   30000 tokens, 3729766 trades, 734645 posities (42s)
10:06:55 posities: 748220 uit 3781782 trades (43s)
10:07:06 161757 wallets gerekend
10:07:06 geluk-toets
10:07:42 persistentie
10:07:44 kopieer-simulatie
10:07:56 klaar in 105s -> /opt/schaduwbot/reports/wallets.md
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
