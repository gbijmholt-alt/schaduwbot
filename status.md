# Schaduwbot status

- tijd: 2026-09-12 10:23:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 20 hours, 36 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.5G/38G | geheugen: 556/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 1877, "tokens_in_memory": 364, "msgs": 116117, "trades": 29619, "creates": 364, "decode_fail": 1225, "rpc_calls": 1058, "rpc_errors": 46, "sol_usd": 102.04679609815321, "open_positions": 13, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 9229 | 1453 | 6 | 1453 | 96 | 2547 | 7662 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 505 | 16% | 2.0% | +44.2% | -16.6% | -6.84% | 100% |
| dip35_V1_gescreend_fail | 4166 | 27% | 3.8% | +45.6% | -25.8% | -6.59% | 100% |
| dip35_V1_alle | 5110 | 26% | 3.9% | +44.9% | -25.3% | -6.89% | 100% |
| dip35_V2_gescreend_pass | 502 | 21% | 2.8% | +42.9% | -20.9% | -7.40% | 100% |
| dip35_V2_gescreend_fail | 4201 | 25% | 4.3% | +55.9% | -27.9% | -6.94% | 100% |
| dip35_V2_alle | 5073 | 24% | 4.6% | +53.4% | -27.6% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 503 | 8% | 3.2% | +297.3% | -22.3% | +4.39% | 100% |
| dip35_V3_gescreend_fail | 4290 | 13% | 5.9% | +116.4% | -29.6% | -10.09% | 100% |
| dip35_V3_alle | 5123 | 13% | 6.0% | +120.7% | -29.2% | -9.65% | 100% |
| dip40_V1_gescreend_pass | 475 | 14% | 2.1% | +46.9% | -16.0% | -6.97% | 100% |
| dip40_V1_gescreend_fail | 4095 | 26% | 3.7% | +47.2% | -25.7% | -6.51% | 100% |
| dip40_V1_alle | 4910 | 25% | 3.8% | +47.3% | -25.1% | -6.75% | 100% |
| dip40_V2_gescreend_pass | 473 | 17% | 2.5% | +45.9% | -19.8% | -8.41% | 100% |
| dip40_V2_gescreend_fail | 4108 | 25% | 4.2% | +55.3% | -27.8% | -7.05% | 100% |
| dip40_V2_alle | 4868 | 24% | 4.4% | +53.8% | -27.4% | -7.93% | 100% |
| dip40_V3_gescreend_pass | 475 | 8% | 2.7% | +294.2% | -21.1% | +2.81% | 100% |
| dip40_V3_gescreend_fail | 4187 | 13% | 5.7% | +110.4% | -29.4% | -10.99% | 100% |
| dip40_V3_alle | 4918 | 13% | 5.8% | +116.1% | -28.9% | -10.51% | 100% |
| dip45_V1_gescreend_pass | 456 | 15% | 2.0% | +48.7% | -15.8% | -6.31% | 100% |
| dip45_V1_gescreend_fail | 4011 | 27% | 3.3% | +48.4% | -25.4% | -5.21% | 100% |
| dip45_V1_alle | 4752 | 26% | 3.4% | +48.8% | -24.7% | -5.60% | 100% |
| dip45_V2_gescreend_pass | 453 | 19% | 2.4% | +43.3% | -19.8% | -7.94% | 100% |
| dip45_V2_gescreend_fail | 4018 | 25% | 3.8% | +58.1% | -27.4% | -5.84% | 100% |
| dip45_V2_alle | 4711 | 24% | 4.0% | +56.9% | -27.0% | -6.62% | 100% |
| dip45_V3_gescreend_pass | 456 | 7% | 2.4% | +352.6% | -20.5% | +6.50% | 100% |
| dip45_V3_gescreend_fail | 4083 | 14% | 5.4% | +115.4% | -28.9% | -8.86% | 100% |
| dip45_V3_alle | 4753 | 13% | 5.4% | +124.1% | -28.4% | -8.25% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 396 | 15% | 5.6% | -9.61% | -12.7% tot -6.6% | -14.6% | – | 100% |
| per_token_zonder_xlink | 112 | 19% | 0.0% | +20.98% | -14.9% tot +56.8% | -13.3% | 131% | 54% |
| gepoold_met_xlink | 3320 | 13% | 3.2% | -10.29% | -11.6% tot -9.0% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 978 | 18% | 0.0% | +20.19% | +0.2% tot +40.1% | -14.6% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 09:58:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:24,856 main INFO screen eyecoin pass=0 dev=0.0 ins=20.02 pro=42 1a=False 1b=False 2=True (1.4s)
Sep 12 09:58:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:26,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:31,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:46,708 main INFO screen RST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.6s)
Sep 12 09:59:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:21,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:59:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:26,533 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:59:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:42,338 main INFO screen primed pass=0 dev=0.0 ins=8.53 pro=62 1a=False 1b=False 2=True (20.9s)
Sep 12 10:00:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:31,620 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:00:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:41,147 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (7.4s)
Sep 12 10:00:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:41,810 main INFO screen Pochita  pass=0 dev=0.0 ins=21.9 pro=53 1a=False 1b=False 2=True (10.3s)
Sep 12 10:02:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:02:37,095 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:02:37 +0000] "GET /health HTTP/1.1" 200 490 "-" "Python-urllib/3.14"
Sep 12 10:02:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:02:57,576 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:03:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:03:01,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:03:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:03:02,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:03:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:03:06,686 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:03:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:03:23,837 main INFO screen ポチタ pass=0 dev=0.0 ins=49.04 pro=37 1a=False 1b=False 2=True (26.3s)
Sep 12 10:03:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:03:26,175 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.7s)
Sep 12 10:04:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:04:21,993 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:04:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:04:27,063 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:04:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:04:44,534 main INFO screen BMW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (22.6s)
Sep 12 10:05:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:27,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:05:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:32,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:05:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:41,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:05:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:42,084 main INFO screen LaMisery pass=0 dev=0.33 ins=0.0 pro=7 1a=False 1b=False 2=False (8.4s)
Sep 12 10:05:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:46,444 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:05:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:05:51,788 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.9s)
Sep 12 10:06:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:06:10,139 main INFO screen Dickbutt pass=0 dev=0.0 ins=49.57 pro=31 1a=False 1b=True 2=True (28.9s)
Sep 12 10:06:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:06:31,635 main INFO screen ANGRYWA pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (8.8s)
Sep 12 10:07:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:07:01,427 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (7.1s)
Sep 12 10:07:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:07:58,174 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:07:58 +0000] "GET /health HTTP/1.1" 200 491 "-" "Python-urllib/3.14"
Sep 12 10:08:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:08:17,802 main INFO screen SHHHH pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (9.6s)
Sep 12 10:09:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:09:12,031 main INFO screen Tantan pass=0 dev=0.0 ins=19.22 pro=62 1a=False 1b=False 2=True (3.8s)
Sep 12 10:09:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:09:15,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:09:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:09:20,554 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:09:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:09:39,877 main INFO screen EMBPONS pass=0 dev=0.19 ins=79.12 pro=8 1a=True 1b=True 2=True (24.4s)
Sep 12 10:10:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:03,666 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:10:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:08,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:10:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:23,095 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:10:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:28,163 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:10:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:28,666 main INFO screen BTCC pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (25.2s)
Sep 12 10:10:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:10:46,383 main INFO screen Tantan pass=0 dev=0.0 ins=49.79 pro=25 1a=False 1b=False 2=True (23.5s)
Sep 12 10:11:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:11:25,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:11:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:11:30,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:11:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:11:53,534 main INFO screen SOL4EX pass=0 dev=6.63 ins=4.37 pro=39 1a=False 1b=False 2=False (11.4s)
Sep 12 10:11:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:11:54,320 main INFO screen Flork pass=0 dev=0.0 ins=49.57 pro=32 1a=False 1b=False 2=True (28.6s)
Sep 12 10:11:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:11:56,878 main INFO screen ALEXI-AI pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 10:12:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:12:24,100 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 12 10:12:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:12:54,114 main INFO screen falling  pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 12 10:13:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:13:23,171 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:13:23 +0000] "GET /health HTTP/1.1" 200 492 "-" "Python-urllib/3.14"
Sep 12 10:13:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:13:53,917 main INFO screen commotitty pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=True (2.3s)
Sep 12 10:14:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:14:53,059 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.6s)
Sep 12 10:15:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:20,245 main INFO screen shi pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (9.4s)
Sep 12 10:15:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:34,621 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:15:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:37,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:15:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:39,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:15:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:45,689 main INFO screen Hustle pass=0 dev=1.59 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 12 10:15:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:50,457 main INFO screen SSDD pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (12.5s)
Sep 12 10:15:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:15:56,587 main INFO screen ROBINBATON pass=0 dev=0.07 ins=79.24 pro=8 1a=False 1b=True 2=True (22.1s)
Sep 12 10:16:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:16:47,501 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=5 1a=False 1b=False 2=False (9.0s)
Sep 12 10:17:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:17:20,006 main INFO screen PADCAT pass=1 dev=0.36 ins=0.0 pro=34 1a=False 1b=False 2=False (9.6s)
Sep 12 10:18:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:18:23,378 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:18:23 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 12 10:19:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:09,134 main INFO screen $FOMOMAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 12 10:19:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:11,363 main INFO screen commotitty pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=True (1.6s)
Sep 12 10:19:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:23,576 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (10.0s)
Sep 12 10:19:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:34,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:19:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:39,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:19:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:19:54,480 main INFO screen HORACE pass=0 dev=0.0 ins=26.11 pro=65 1a=False 1b=False 2=True (20.4s)
Sep 12 10:20:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:12,128 aiohttp.access INFO 94.154.43.223 [12/Sep/2026:10:20:12 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 12 10:20:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:18,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:20:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:23,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:20:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:32,846 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:20:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:37,875 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:20:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:41,684 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.9s)
Sep 12 10:20:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:43,347 main INFO screen HORACE pass=0 dev=8.3 ins=20.44 pro=12 1a=False 1b=False 2=False (24.8s)
Sep 12 10:20:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:20:58,309 main INFO screen HORACE pass=0 dev=0.0 ins=48.81 pro=64 1a=False 1b=False 2=True (26.0s)
Sep 12 10:22:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:22:51,034 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:22:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:22:56,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:23:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:23:00,811 main INFO screen Launchpad pass=0 dev=0.0 ins=5.49 pro=39 1a=False 1b=False 2=True (3.1s)
Sep 12 10:23:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:23:20,192 main INFO screen Duo pass=0 dev=0.0 ins=48.82 pro=27 1a=False 1b=True 2=True (29.3s)
Sep 12 10:23:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:23:37,179 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:23:37 +0000] "GET /health HTTP/1.1" 200 496 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T09:20:36Z
--- update 2026-09-12T09:26:16Z
--- update 2026-09-12T09:31:18Z
--- update 2026-09-12T09:36:36Z
--- update 2026-09-12T09:41:47Z
--- update 2026-09-12T09:47:04Z
Running as unit: schaduwbot-wallets.service; invocation ID: 59ae4466605a4369ba7d98991ca62d2e
analyses gestart (571ea883d7b8)
--- update 2026-09-12T09:52:16Z
nieuwe code: 49e15c7
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T09:57:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 571283a9195f4501a57b6cd9bbbe5e84
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T10:02:36Z
--- update 2026-09-12T10:07:56Z
--- update 2026-09-12T10:13:22Z
--- update 2026-09-12T10:18:22Z
--- update 2026-09-12T10:23:36Z
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
