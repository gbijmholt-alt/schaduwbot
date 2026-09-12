# Schaduwbot status

- tijd: 2026-09-12 14:37:11 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 50 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 727/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 17091, "tokens_in_memory": 4217, "msgs": 1503321, "trades": 416037, "creates": 4217, "decode_fail": 18292, "rpc_calls": 12836, "rpc_errors": 559, "sol_usd": 102.00012861367597, "open_positions": 47, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 14:24:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:24:06,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:24:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:24:14,216 main INFO screen COOK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 14:24:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:24:26,368 main INFO screen VOID pass=0 dev=39.93 ins=0.0 pro=4 1a=False 1b=False 2=True (24.9s)
Sep 12 14:24:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:24:46,613 main INFO screen DANTE pass=1 dev=0.0 ins=0.65 pro=49 1a=False 1b=False 2=False (7.4s)
Sep 12 14:25:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:03,198 main INFO screen GTA pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 12 14:25:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:05,103 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:25:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:10,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:25:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:31,786 main INFO screen ANIMALS pass=0 dev=0.0 ins=49.68 pro=17 1a=True 1b=True 2=True (26.8s)
Sep 12 14:25:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:57,755 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:25:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:25:59,777 main INFO screen $CAJUN pass=0 dev=0.53 ins=0.0 pro=3 1a=False 1b=False 2=False (6.5s)
Sep 12 14:26:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:02,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:26:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:11,006 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:26:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:16,538 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:26:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:22,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:26:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:23,169 main INFO screen GTA pass=0 dev=0.58 ins=0.0 pro=2 1a=False 1b=False 2=False (25.5s)
Sep 12 14:26:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:27,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:26:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:37,130 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:26:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:26:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:37,842 main INFO screen earless pass=0 dev=0.0 ins=30.4 pro=25 1a=False 1b=False 2=True (26.9s)
Sep 12 14:26:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:42,403 main INFO screen att pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 12 14:26:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:26:49,899 main INFO screen Jacob pass=0 dev=0.0 ins=18.11 pro=60 1a=False 1b=True 2=True (27.4s)
Sep 12 14:27:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:27:21,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:27:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:27:26,275 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:27:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:27:46,131 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.68 pro=17 1a=False 1b=False 2=True (25.1s)
Sep 12 14:27:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:27:48,292 main INFO screen PYR pass=1 dev=0.1 ins=0.0 pro=34 1a=False 1b=False 2=False (6.1s)
Sep 12 14:28:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:01,037 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:02,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:04,159 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:06,108 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:07,080 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:09,188 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:28:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:24,863 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (23.9s)
Sep 12 14:28:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:27,148 main INFO screen pipecat pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (25.2s)
Sep 12 14:28:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:30,434 main INFO screen Pickles pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (26.3s)
Sep 12 14:28:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:28:59,554 main INFO screen GTA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (6.9s)
Sep 12 14:29:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:29:55,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:29:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:29:58,679 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:00,201 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:03,757 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:04,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:17,158 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (13.0s)
Sep 12 14:30:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:21,070 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.72 pro=20 1a=True 1b=False 2=True (26.0s)
Sep 12 14:30:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:21,677 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.1s)
Sep 12 14:30:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:27,028 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:32,099 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:30:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:49,201 main INFO screen SAMGPT pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (22.2s)
Sep 12 14:30:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:30:59,038 main INFO screen GTA pass=0 dev=0.16 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 12 14:31:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:03,364 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:31:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:08,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:31:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:27,975 main INFO screen DOGBRAIN pass=0 dev=0.07 ins=79.24 pro=10 1a=False 1b=True 2=True (24.7s)
Sep 12 14:31:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:33,298 main INFO screen degenrex pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 12 14:31:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:58,098 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:31:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:31:59,265 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:31:59 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:32:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:11,258 main INFO screen stonk pass=0 dev=32.16 ins=2.02 pro=6 1a=False 1b=False 2=False (10.7s)
Sep 12 14:32:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:11,300 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:32:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:16,371 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:32:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:16,374 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.76 pro=16 1a=False 1b=False 2=True (18.4s)
Sep 12 14:32:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:17,014 main INFO screen Swiftie pass=1 dev=3.43 ins=4.12 pro=33 1a=False 1b=False 2=False (14.0s)
Sep 12 14:32:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:23,942 main INFO screen GTA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 14:32:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:37,631 main INFO screen GREED4 pass=0 dev=0.0 ins=0.0 pro=27 1a=False 1b=False 2=True (26.4s)
Sep 12 14:32:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:32:45,553 main INFO screen Puppeth pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 12 14:33:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:33:06,981 main INFO screen cap pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 12 14:33:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:33:20,662 main INFO screen ZPRIV pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (1.5s)
Sep 12 14:33:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:33:26,842 main INFO screen POPSPER pass=1 dev=0.0 ins=1.9 pro=69 1a=False 1b=False 2=False (3.9s)
Sep 12 14:34:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:34:12,301 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:34:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:34:19,106 main INFO screen GTA pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 12 14:34:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:34:32,802 main INFO screen TACZ pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 12 14:34:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:34:54,074 main INFO screen QLO pass=0 dev=0.26 ins=0.0 pro=45 1a=False 1b=False 2=False (3.0s)
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
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T14:15:36Z
--- update 2026-09-12T14:21:31Z
Running as unit: schaduwbot-wallets.service; invocation ID: 231ef89f1987467a9f6d8d397018c1e2
analyses gestart (02faa7a55c91)
--- update 2026-09-12T14:26:36Z
--- update 2026-09-12T14:31:58Z
--- update 2026-09-12T14:37:10Z
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
