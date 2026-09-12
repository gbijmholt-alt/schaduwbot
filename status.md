# Schaduwbot status

- tijd: 2026-09-12 16:28:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 2 hours, 41 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.8G/38G | geheugen: 860/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 23789, "tokens_in_memory": 6760, "msgs": 2549603, "trades": 631906, "creates": 7187, "decode_fail": 27773, "rpc_calls": 18379, "rpc_errors": 776, "sol_usd": 101.95267886316525, "open_positions": 30, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 16:01:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:01:19,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:01:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:01:27,243 main INFO screen $AIKNOW pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (14.0s)
Sep 12 16:01:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:01:30,194 main INFO screen CASHCAT pass=0 dev=8.57 ins=0.0 pro=1 1a=False 1b=False 2=True (11.2s)
Sep 12 16:01:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:01:30,282 main INFO screen Lazycoin pass=0 dev=0.0 ins=15.95 pro=20 1a=False 1b=False 2=True (27.2s)
Sep 12 16:02:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:02:17,952 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:02:17 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:03:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:03:38,497 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:03:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:03:43,567 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:04:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:04:02,784 main INFO screen MILLI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (24.4s)
Sep 12 16:04:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:04:55,744 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:05:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:05:00,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:05:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:05:18,419 main INFO screen CASHCAT pass=0 dev=10.8 ins=0.0 pro=1 1a=False 1b=False 2=True (7.1s)
Sep 12 16:05:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:05:21,685 main INFO screen CHICK pass=0 dev=0.17 ins=48.6 pro=19 1a=False 1b=False 2=True (26.0s)
Sep 12 16:05:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:05:52,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:05:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:05:57,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:06:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:06:09,743 main INFO screen tick pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.4s)
Sep 12 16:06:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:06:12,621 main INFO screen GEMI pass=0 dev=6.58 ins=0.0 pro=57 1a=False 1b=False 2=True (20.4s)
Sep 12 16:06:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:06:17,940 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:06:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:06:22,999 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:06:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:06:42,236 main INFO screen LARPY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (24.3s)
Sep 12 16:07:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:07:37,107 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:07:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:07:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:07:50,949 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:07:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:07:56,314 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 12 16:08:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:08:06,136 main INFO screen horse pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (15.3s)
Sep 12 16:08:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:08:28,454 main INFO screen lifetimecomeb pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.2s)
Sep 12 16:10:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:10:24,282 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:10:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:10:29,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:10:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:10:46,207 main INFO screen のび子 pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (22.0s)
Sep 12 16:10:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:10:56,275 main INFO screen PAPI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.8s)
Sep 12 16:12:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:12:02,723 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 12 16:12:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:12:06,015 main INFO screen HORIZON IA pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (9.4s)
Sep 12 16:13:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:02,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:13:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:07,275 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:13:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:18,534 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:16:13:18 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 16:13:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:26,831 main INFO screen BJ pass=1 dev=0.81 ins=0.95 pro=19 1a=False 1b=False 2=False (6.3s)
Sep 12 16:13:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:27,824 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.7s)
Sep 12 16:13:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:54,508 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:13:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:13:59,575 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:14:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:14:10,259 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 12 16:14:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:14:19,410 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (25.0s)
Sep 12 16:14:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:14:52,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:14:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:14:57,708 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:15:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:15:14,148 main INFO screen BERD pass=0 dev=0.17 ins=48.67 pro=21 1a=False 1b=False 2=True (21.6s)
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
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T15:57:16Z
--- update 2026-09-12T16:02:16Z
--- update 2026-09-12T16:07:36Z
--- update 2026-09-12T16:13:17Z
--- update 2026-09-12T16:18:17Z
--- update 2026-09-12T16:23:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 734fe7fd71e047c5827569b33cc14ab3
analyses gestart (02faa7a55c91)
--- update 2026-09-12T16:28:48Z
```

## Analyses (laatste 25 regels)
```
active
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
16:23:37 34918 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
16:23:42   ingelezen tot rowid 4357872 (200000 rijen, 200000 bruikbaar)
16:23:43   ingelezen tot rowid 4392526 (234654 rijen, 234654 bruikbaar)
16:23:43 ingelezen: 234654 nieuwe trades, 234654 bruikbaar (7s)
16:24:17 2866 aankopen van gevolgde wallets geëvalueerd
16:24:26 vroege kopers: 154 voldoen nu, register 216, 331 tokens beoordeeld
16:24:42 grote spelers: saldo van 1467 wallets opgehaald
16:25:49 herkomst: 40 posities gekoppeld
16:25:52 klaar in 136s -> /opt/schaduwbot/reports/ledger.md
16:25:52 na-migratie: 400 paren te checken
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
