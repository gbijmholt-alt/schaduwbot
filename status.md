# Schaduwbot status

- tijd: 2026-09-12 15:57:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 2 hours, 10 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 812/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 21897, "tokens_in_memory": 5928, "msgs": 2234265, "trades": 565254, "creates": 5981, "decode_fail": 24671, "rpc_calls": 17372, "rpc_errors": 732, "sol_usd": 102.09129632180563, "open_positions": 37, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 15:52:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:52:14,551 main INFO screen Pajeet pass=1 dev=0.0 ins=6.56 pro=68 1a=False 1b=False 2=False (3.2s)
Sep 12 15:52:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:52:18,128 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 12 15:52:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:52:19,263 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 15:53:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:53:11,519 main INFO screen のび子 pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (2.7s)
Sep 12 15:53:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:53:11,857 main INFO screen FOLDapple pass=0 dev=1.72 ins=0.0 pro=6 1a=False 1b=False 2=False (3.3s)
Sep 12 15:53:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:53:22,245 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:53:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:53:31,905 main INFO screen LMAO pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (9.7s)
Sep 12 15:53:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:53:35,245 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 12 15:55:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:55:16,498 main INFO screen BMS pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 15:55:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:55:43,314 main INFO screen RC pass=0 dev=0.13 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 12 15:55:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:55:48,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:55:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:55:56,148 main INFO screen TRANS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 15:56:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:01,777 main INFO screen $20 pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 15:56:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:24,481 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:56:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:29,511 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:56:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:36,499 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:56:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:41,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:56:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:44,013 main INFO screen GPTGUY pass=0 dev=0.18 ins=50.47 pro=7 1a=False 1b=False 2=True (19.6s)
Sep 12 15:56:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:56,007 main INFO screen BetOnBlak pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.9s)
Sep 12 15:56:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:56:57,897 main INFO screen Pokex pass=0 dev=0.0 ins=47.56 pro=16 1a=False 1b=False 2=True (21.5s)
Sep 12 15:57:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:57:17,943 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:57:17 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T15:57:16Z
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
