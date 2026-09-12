# Schaduwbot status

- tijd: 2026-09-12 14:47:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 1 hour, 0 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 731/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 17716, "tokens_in_memory": 4435, "msgs": 1545183, "trades": 432116, "creates": 4435, "decode_fail": 18909, "rpc_calls": 13420, "rpc_errors": 584, "sol_usd": 102.02396335595701, "open_positions": 40, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 14:35:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:35:13,987 main INFO screen $CAJUN pass=0 dev=0.6 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 14:35:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:35:52,512 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:35:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:35:53,246 main INFO screen CHAROC pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=True (2.6s)
Sep 12 14:36:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:00,376 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.18 pro=10 1a=False 1b=False 2=True (8.1s)
Sep 12 14:36:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:04,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:36:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:12,115 main INFO screen da pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 12 14:36:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:24,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:36:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:31,208 main INFO screen Horse pass=0 dev=1.67 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 12 14:36:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:36,654 main INFO screen $CAJUN pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=True (2.5s)
Sep 12 14:36:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:51,954 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:36:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:36:57,029 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:37:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:37:10,284 main INFO screen FRONTIER pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (18.4s)
Sep 12 14:37:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:37:11,563 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:37:11 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:37:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:37:17,270 main INFO screen spida pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 12 14:37:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:37:42,461 main INFO screen DOGGPT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 14:37:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:37:53,904 main INFO screen spida pass=0 dev=1.78 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 12 14:38:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:00,444 main INFO screen HATS pass=0 dev=9.64 ins=0.0 pro=28 1a=False 1b=False 2=False (2.1s)
Sep 12 14:38:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:08,021 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:13,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:17,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:17,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:22,603 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:22,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:27,563 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.69 pro=18 1a=False 1b=False 2=True (19.6s)
Sep 12 14:38:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:28,882 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:33,951 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:37,928 main INFO screen batonfly pass=0 dev=0.35 ins=78.76 pro=6 1a=False 1b=True 2=True (20.3s)
Sep 12 14:38:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:38,463 main INFO screen GOAP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.0s)
Sep 12 14:38:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:48,154 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.3s)
Sep 12 14:38:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:57,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:38:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:58,112 main INFO screen TRANS pass=0 dev=0.8 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 14:38:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:38:58,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:39:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:02,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:39:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:07,158 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.67 pro=12 1a=False 1b=False 2=True (8.5s)
Sep 12 14:39:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:19,773 main INFO screen STONKOOR pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=True (22.1s)
Sep 12 14:39:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:20,882 main INFO screen da pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 12 14:39:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:41,438 main INFO screen Stonkoor pass=1 dev=0.0 ins=16.26 pro=26 1a=False 1b=False 2=False (4.0s)
Sep 12 14:39:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:47,021 main INFO screen DOOB pass=0 dev=1.33 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 12 14:40:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:16,711 main INFO screen BINGO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 12 14:40:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:38,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:39,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:44,487 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:46,848 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=14 1a=False 1b=False 2=True (8.8s)
Sep 12 14:40:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:59,047 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.1s)
Sep 12 14:41:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:13,146 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 12 14:41:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:37,102 main INFO screen spida pass=0 dev=4.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:41:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:58,252 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:03,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:10,973 main INFO screen Doge pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 12 14:42:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:11,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:16,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:16,691 main INFO screen MEME50 pass=0 dev=0.17 ins=50.82 pro=21 1a=False 1b=False 2=True (18.6s)
Sep 12 14:42:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:26,381 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:27,148 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:42:27 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:42:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:31,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:31,825 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=16 1a=False 1b=False 2=True (20.8s)
Sep 12 14:42:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:45,911 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 14:43:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:08,251 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:16,095 main INFO screen Tradcat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 14:43:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:41,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:46,552 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:56,600 main INFO screen spida pass=0 dev=4.26 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:44:01,117 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (19.7s)
Sep 12 14:45:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:13,079 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:45:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:18,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:45:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:32,317 main INFO screen $AURA pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (19.3s)
Sep 12 14:45:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:54,104 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,238 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /@vite/client HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,468 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /nonexistent-lane-control-cf9x2 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,652 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /__nextjs_source-map?filename=file:///nonexistent-lane-cf9x2 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,949 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /vite.svg HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,232 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.tsx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,487 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.ts HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,699 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.jsx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,887 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,171 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.mts HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,390 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.vue HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,594 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.svelte HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:47:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:15,718 main INFO screen FAG pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 12 14:47:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:37,126 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:47:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T14:15:36Z
--- update 2026-09-12T14:21:31Z
Running as unit: schaduwbot-wallets.service; invocation ID: 231ef89f1987467a9f6d8d397018c1e2
analyses gestart (02faa7a55c91)
--- update 2026-09-12T14:26:36Z
--- update 2026-09-12T14:31:58Z
--- update 2026-09-12T14:37:10Z
--- update 2026-09-12T14:42:26Z
--- update 2026-09-12T14:47:36Z
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
