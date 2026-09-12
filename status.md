# Schaduwbot status

- tijd: 2026-09-12 14:10:13 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 23 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 739/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 15472, "tokens_in_memory": 3676, "msgs": 1323882, "trades": 370166, "creates": 3676, "decode_fail": 16532, "rpc_calls": 11162, "rpc_errors": 489, "sol_usd": 102.00220761168669, "open_positions": 36, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 12582 | 1937 | 11 | 1937 | 142 | 3392 | 10150 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 542 | 16% | 1.8% | +43.7% | -16.3% | -6.47% | 100% |
| dip35_V1_gescreend_fail | 4364 | 27% | 3.8% | +45.5% | -25.9% | -6.59% | 100% |
| dip35_V1_alle | 5401 | 26% | 4.0% | +44.7% | -25.3% | -6.83% | 100% |
| dip35_V2_gescreend_pass | 539 | 22% | 2.6% | +41.9% | -20.7% | -6.74% | 100% |
| dip35_V2_gescreend_fail | 4405 | 25% | 4.4% | +55.3% | -28.0% | -6.92% | 100% |
| dip35_V2_alle | 5358 | 25% | 4.6% | +52.7% | -27.7% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 540 | 9% | 3.0% | +273.8% | -22.2% | +5.19% | 100% |
| dip35_V3_gescreend_fail | 4503 | 14% | 6.1% | +113.1% | -29.7% | -10.40% | 100% |
| dip35_V3_alle | 5413 | 13% | 6.1% | +117.4% | -29.3% | -9.88% | 100% |
| dip40_V1_gescreend_pass | 510 | 14% | 2.0% | +45.8% | -15.7% | -6.87% | 100% |
| dip40_V1_gescreend_fail | 4294 | 26% | 3.8% | +47.0% | -25.8% | -6.61% | 100% |
| dip40_V1_alle | 5188 | 25% | 3.9% | +46.9% | -25.1% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 507 | 18% | 2.4% | +45.1% | -19.7% | -8.35% | 100% |
| dip40_V2_gescreend_fail | 4308 | 25% | 4.3% | +54.8% | -28.0% | -7.15% | 100% |
| dip40_V2_alle | 5137 | 24% | 4.5% | +53.1% | -27.5% | -8.08% | 100% |
| dip40_V3_gescreend_pass | 510 | 8% | 2.5% | +271.0% | -21.1% | +2.95% | 100% |
| dip40_V3_gescreend_fail | 4395 | 13% | 5.9% | +107.4% | -29.5% | -11.48% | 100% |
| dip40_V3_alle | 5194 | 13% | 5.9% | +112.5% | -29.0% | -10.94% | 100% |
| dip45_V1_gescreend_pass | 490 | 15% | 1.8% | +47.6% | -15.6% | -6.29% | 100% |
| dip45_V1_gescreend_fail | 4208 | 27% | 3.4% | +48.2% | -25.6% | -5.42% | 100% |
| dip45_V1_alle | 5021 | 26% | 3.5% | +48.4% | -24.9% | -5.78% | 100% |
| dip45_V2_gescreend_pass | 486 | 18% | 2.3% | +43.1% | -19.7% | -8.05% | 100% |
| dip45_V2_gescreend_fail | 4213 | 25% | 4.0% | +57.5% | -27.6% | -6.03% | 100% |
| dip45_V2_alle | 4972 | 24% | 4.1% | +56.1% | -27.2% | -6.86% | 100% |
| dip45_V3_gescreend_pass | 490 | 8% | 2.2% | +315.7% | -20.5% | +6.22% | 100% |
| dip45_V3_gescreend_fail | 4287 | 14% | 5.5% | +112.7% | -29.0% | -9.30% | 100% |
| dip45_V3_alle | 5022 | 13% | 5.4% | +120.3% | -28.4% | -8.67% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 421 | 15% | 5.2% | -9.16% | -12.1% tot -6.2% | -14.6% | – | 100% |
| per_token_zonder_xlink | 124 | 21% | 0.0% | +19.71% | -12.7% tot +52.1% | -13.2% | 126% | 54% |
| gepoold_met_xlink | 3537 | 13% | 3.0% | -9.78% | -11.1% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1077 | 18% | 0.0% | +18.64% | +0.5% tot +36.8% | -14.3% | 69% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 13:55:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:57,620 main INFO screen Pele pass=1 dev=0.0 ins=12.69 pro=53 1a=False 1b=False 2=False (3.7s)
Sep 12 13:56:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:56:02,606 main INFO screen Bull pass=0 dev=0.0 ins=12.09 pro=70 1a=False 1b=False 2=True (24.4s)
Sep 12 13:56:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:56:07,068 main INFO screen ANW pass=0 dev=0.62 ins=17.29 pro=60 1a=False 1b=False 2=True (4.6s)
Sep 12 13:56:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:56:07,784 main INFO screen $OIL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (11.7s)
Sep 12 13:56:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:56:10,367 main INFO screen PUSSY pass=0 dev=0.38 ins=0.0 pro=1 1a=False 1b=False 2=False (4.1s)
Sep 12 13:57:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:57:48,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:57:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:57:53,576 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:02,049 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:02,913 main INFO screen BPCATE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 12 13:58:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:07,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:07,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:09,490 main INFO screen Doggos pass=1 dev=0.0 ins=17.03 pro=78 1a=False 1b=False 2=False (21.1s)
Sep 12 13:58:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:12,222 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:16,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:58:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:23,930 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=3 1a=False 1b=False 2=True (22.0s)
Sep 12 13:58:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:25,981 main INFO screen HORACE pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 12 13:58:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:26,116 main INFO screen DATADOG pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (19.5s)
Sep 12 13:58:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:32,259 main INFO screen USDTCAT pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 12 13:58:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:55,656 main INFO screen UFC pass=0 dev=0.1 ins=0.0 pro=4 1a=False 1b=False 2=False (4.6s)
Sep 12 13:58:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:58:56,254 main INFO screen HEDGEHOG pass=1 dev=0.0 ins=17.85 pro=43 1a=False 1b=False 2=False (4.4s)
Sep 12 13:59:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:59:37,126 main INFO screen JN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 12 13:59:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:59:48,361 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:59:48 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:00:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:06,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:00:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:12,067 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:00:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:19,618 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 12 14:00:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:20,735 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 14:00:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:30,757 main INFO screen HOT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (23.8s)
Sep 12 14:00:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:38,518 main INFO screen BUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.7s)
Sep 12 14:00:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:00:54,607 main INFO screen SCRVAN pass=0 dev=0.06 ins=0.0 pro=5 1a=False 1b=False 2=False (7.7s)
Sep 12 14:01:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:11,600 main INFO screen dai pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 12 14:01:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:29,498 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:01:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:40,798 main INFO screen BUCK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 12 14:01:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:41,421 main INFO screen ✈️ pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (12.0s)
Sep 12 14:01:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:51,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:01:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:53,933 main INFO screen Simple pass=1 dev=3.47 ins=0.0 pro=30 1a=False 1b=False 2=False (9.3s)
Sep 12 14:01:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:01:56,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:02:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:10,890 main INFO screen SAKADUNG CAT pass=0 dev=0.0 ins=18.37 pro=59 1a=False 1b=False 2=True (19.9s)
Sep 12 14:02:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:15,270 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:02:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:20,294 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:02:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:23,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:02:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:28,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:02:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:41,949 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.8s)
Sep 12 14:02:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:02:49,863 main INFO screen HOT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (26.5s)
Sep 12 14:03:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:02,249 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:03:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:07,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:03:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:14,398 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 12 14:03:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:16,174 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:03:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:25,618 main INFO screen Degenerates pass=0 dev=0.0 ins=14.11 pro=61 1a=False 1b=False 2=True (23.4s)
Sep 12 14:03:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:25,688 main INFO screen POKEMON pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 12 14:03:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:32,267 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (16.1s)
Sep 12 14:03:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:42,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:03:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:03:54,792 main INFO screen pmp pass=0 dev=0.09 ins=0.0 pro=1 1a=False 1b=False 2=False (12.0s)
Sep 12 14:04:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:04:27,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:04:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:04:32,383 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:04:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:04:35,446 main INFO screen lol pass=0 dev=0.53 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 12 14:04:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:04:52,077 main INFO screen Jakgpt pass=0 dev=0.35 ins=78.3 pro=8 1a=False 1b=True 2=True (25.2s)
Sep 12 14:05:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:05:00,484 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:05:00 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:05:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:05:14,807 main INFO screen PEPEHOUSE pass=0 dev=5.22 ins=3.83 pro=47 1a=False 1b=False 2=False (7.5s)
Sep 12 14:05:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:05:48,682 main INFO screen Doggy pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.9s)
Sep 12 14:06:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:06:01,495 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.2s)
Sep 12 14:06:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:06:40,531 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (11.5s)
Sep 12 14:06:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:06:41,289 main INFO screen beer pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (12.3s)
Sep 12 14:06:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:06:48,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:06:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:06:53,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:07:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:07:13,414 main INFO screen FLYEMBER pass=0 dev=0.35 ins=78.76 pro=6 1a=False 1b=True 2=True (25.2s)
Sep 12 14:07:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:07:51,128 main INFO screen $VOID pass=0 dev=1.39 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 12 14:08:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:11,560 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:08:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:16,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:08:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:16,741 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:08:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:21,222 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:08:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:24,999 main INFO screen DERP pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 12 14:08:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:25,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:08:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:33,998 main INFO screen caton pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (22.5s)
Sep 12 14:08:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:41,659 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (15.7s)
Sep 12 14:08:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:43,673 main INFO screen Life pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (27.6s)
Sep 12 14:08:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:08:55,878 main INFO screen $CAJUN pass=0 dev=0.53 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 12 14:09:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:09:35,156 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:09:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:09:40,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:10:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:00,468 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.4s)
Sep 12 14:10:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:13,086 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:10:13 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (83a2a6960268)
--- update 2026-09-12T13:08:11Z
--- update 2026-09-12T13:13:29Z
--- update 2026-09-12T13:18:36Z
--- update 2026-09-12T13:23:41Z
--- update 2026-09-12T13:28:54Z
--- update 2026-09-12T13:34:09Z
--- update 2026-09-12T13:39:09Z
--- update 2026-09-12T13:44:26Z
--- update 2026-09-12T13:49:36Z
--- update 2026-09-12T13:54:38Z
--- update 2026-09-12T13:59:47Z
--- update 2026-09-12T14:04:59Z
nieuwe code: 9a7e741
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 367f286af9504770be86685502142335
analyses gestart (6b9b2315b322)
--- update 2026-09-12T14:10:11Z
nieuwe code: f76b0ba
alleen analyses/documentatie gewijzigd: geen herstart
```

## Analyses (laatste 25 regels)
```
active
13:13:06   16000 tokens, 1964033 trades, 376676 posities (17s)
13:13:08   18000 tokens, 2217916 trades, 427570 posities (20s)
13:13:10   20000 tokens, 2455968 trades, 473450 posities (22s)
13:13:12   22000 tokens, 2717056 trades, 523961 posities (23s)
13:13:14   24000 tokens, 2956310 trades, 567769 posities (25s)
13:13:16   26000 tokens, 3200796 trades, 614853 posities (27s)
13:13:18   28000 tokens, 3423421 trades, 657040 posities (29s)
13:13:20   30000 tokens, 3683712 trades, 705965 posities (31s)
13:13:22   32000 tokens, 3941796 trades, 764610 posities (33s)
13:13:22 posities: 788267 uit 4042689 trades (34s)
13:13:32 166368 wallets gerekend
13:13:33 geluk-toets
13:14:04 persistentie
13:14:06 kopieer-simulatie
13:14:17 klaar in 89s -> /opt/schaduwbot/reports/wallets.md
14:05:00 31470 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
14:05:03   ingelezen tot rowid 4130519 (104556 rijen, 104556 bruikbaar)
14:05:03 ingelezen: 104556 nieuwe trades, 104556 bruikbaar (4s)
14:05:34 1023 aankopen van gevolgde wallets geëvalueerd
14:05:42 vroege kopers: 142 voldoen nu, register 194, 152 tokens beoordeeld
14:05:50 grote spelers: saldo van 81 wallets opgehaald
14:07:07 herkomst: 40 posities gekoppeld
14:07:10 klaar in 130s -> /opt/schaduwbot/reports/ledger.md
14:07:10 telwijze -> probe-v3-uniek-tellen: tellers en layout gewist, opnieuw opbouwen
14:07:11 na-migratie: 400 paren te checken
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
