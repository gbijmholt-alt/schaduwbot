# Schaduwbot status

- tijd: 2026-09-12 12:04:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 22 hours, 17 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.6G/38G | geheugen: 646/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 7934, "tokens_in_memory": 1762, "msgs": 613374, "trades": 166370, "creates": 1762, "decode_fail": 6478, "rpc_calls": 4916, "rpc_errors": 222, "sol_usd": 102.13258763951593, "open_positions": 33, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 11:54:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:54:31,692 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:54:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:54:36,760 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:54:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:54:50,330 main INFO screen Oracle pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (18.7s)
Sep 12 11:55:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:55:07,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:55:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:55:12,651 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:55:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:55:26,952 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.5s)
Sep 12 11:55:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:55:40,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:55:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:55:47,204 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 12 11:56:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:56:02,742 main INFO screen SAVPIR pass=0 dev=0.27 ins=0.0 pro=6 1a=False 1b=False 2=False (3.7s)
Sep 12 11:56:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:56:04,821 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:56:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:56:05,063 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 11:56:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:56:09,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:56:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:56:24,479 main INFO screen retard pass=0 dev=0.0 ins=21.99 pro=28 1a=False 1b=False 2=True (19.8s)
Sep 12 11:57:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:23,547 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:30,463 main INFO screen TOAD pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 12 11:57:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:45,692 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:47,747 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:50,762 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:52,816 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:54,671 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:57:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:57:59,749 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:58:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:06,065 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (20.5s)
Sep 12 11:58:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:06,263 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:58:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:06,380 main INFO screen PINS pass=0 dev=0.07 ins=79.24 pro=7 1a=False 1b=True 2=True (18.7s)
Sep 12 11:58:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:11,333 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:58:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:12,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:58:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:14,250 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.6s)
Sep 12 11:58:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:20,734 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 12 11:58:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:24,152 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=3 1a=False 1b=False 2=False (18.1s)
Sep 12 11:58:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:49,178 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:58:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:58:54,249 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:59:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:01,684 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:59:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:06,942 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:59:06 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:59:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:07,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:59:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:10,469 main INFO screen 冲鸭 pass=0 dev=25.41 ins=0.18 pro=32 1a=False 1b=False 2=False (5.5s)
Sep 12 11:59:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:11,137 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.1s)
Sep 12 11:59:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:22,881 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (21.3s)
Sep 12 11:59:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:32,986 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:59:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:38,017 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:59:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:47,033 main INFO screen ANT-1 pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 12 11:59:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:59:53,795 main INFO screen ZAN pass=0 dev=42.49 ins=0.0 pro=6 1a=False 1b=False 2=False (20.9s)
Sep 12 12:00:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:00:12,358 main INFO screen deliverINU pass=1 dev=0.0 ins=0.87 pro=48 1a=False 1b=False 2=False (8.1s)
Sep 12 12:00:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:00:31,150 main INFO screen ORGE pass=0 dev=0.0 ins=25.3 pro=61 1a=False 1b=False 2=True (7.3s)
Sep 12 12:02:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:04,064 main INFO screen MOM pass=1 dev=0.0 ins=11.17 pro=42 1a=False 1b=False 2=False (16.2s)
Sep 12 12:02:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:05,620 main INFO screen $CAJUN pass=0 dev=0.31 ins=0.0 pro=7 1a=False 1b=False 2=False (17.4s)
Sep 12 12:02:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:08,032 main INFO screen CANDLE pass=0 dev=20.66 ins=2.29 pro=30 1a=False 1b=False 2=False (17.3s)
Sep 12 12:02:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:08,838 main INFO screen Won pass=1 dev=0.0 ins=9.51 pro=48 1a=False 1b=False 2=False (4.8s)
Sep 12 12:02:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:36,627 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:02:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:51,387 main INFO screen stocklana pass=0 dev=0.36 ins=0.0 pro=3 1a=False 1b=False 2=False (14.9s)
Sep 12 12:02:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:53,123 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:02:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:02:58,185 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:11,250 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:16,412 main INFO screen Maple pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (23.4s)
Sep 12 12:03:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:16,472 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:19,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:22,353 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 12 12:03:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:32,258 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:32,523 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (13.0s)
Sep 12 12:03:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:36,538 main INFO screen OnlyCats pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (25.8s)
Sep 12 12:03:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:37,336 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:03:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:03:57,070 main INFO screen ZAN pass=0 dev=42.49 ins=0.0 pro=5 1a=False 1b=False 2=True (24.9s)
Sep 12 12:04:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:04:14,458 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (10.5s)
Sep 12 12:04:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:04:34,215 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:04:34 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T11:59:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 67d32d30228c414781697fb76280fa59
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T12:04:33Z
```

## Analyses (laatste 25 regels)
```
active
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
11:59:06 29585 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
11:59:10   ingelezen tot rowid 3927057 (155562 rijen, 155562 bruikbaar)
11:59:10 ingelezen: 155562 nieuwe trades, 155562 bruikbaar (4s)
11:59:43 3000 aankopen van gevolgde wallets geëvalueerd
11:59:51 vroege kopers: 137 voldoen nu, register 182, 109 tokens beoordeeld
12:00:01 grote spelers: saldo van 477 wallets opgehaald
12:01:28 herkomst: 40 posities gekoppeld
12:01:31 klaar in 145s -> /opt/schaduwbot/reports/ledger.md
12:01:32 na-migratie: 400 paren te checken
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
