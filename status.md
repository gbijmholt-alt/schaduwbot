# Schaduwbot status

- tijd: 2026-09-12 14:21:32 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 34 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 738/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 16152, "tokens_in_memory": 3869, "msgs": 1403312, "trades": 388828, "creates": 3869, "decode_fail": 17195, "rpc_calls": 11890, "rpc_errors": 518, "sol_usd": 101.9620592845741, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 14:10:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:19,753 main INFO screen $CAJUN pass=0 dev=0.62 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 12 14:10:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:24,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:10:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:25,788 main INFO screen 100k/Rug pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.5s)
Sep 12 14:10:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:34,481 main INFO screen LaMisery pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (9.9s)
Sep 12 14:10:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:39,194 main INFO screen FLYWHEEL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 14:10:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:10:56,231 main INFO screen Frontier pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:11:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:11:17,242 main INFO screen SXSN pass=0 dev=0.61 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 14:11:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:11:27,293 main INFO screen 🍓 pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 12 14:11:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:11:50,313 main INFO screen HORACE pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 14:12:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:01,206 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:12:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:06,276 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:12:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:14,754 main INFO screen Remember pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 12 14:12:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:24,409 main INFO screen ROBINSTUNK pass=0 dev=0.07 ins=77.41 pro=8 1a=False 1b=True 2=True (23.2s)
Sep 12 14:12:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:32,623 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:12:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:32,645 main INFO screen KRES pass=0 dev=16.45 ins=0.0 pro=22 1a=False 1b=False 2=False (8.8s)
Sep 12 14:12:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:37,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:12:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:12:59,430 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (26.8s)
Sep 12 14:13:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:13:32,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:13:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:13:37,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:13:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:13:58,429 main INFO screen DANGR pass=0 dev=97.07 ins=0.0 pro=1 1a=False 1b=True 2=True (26.1s)
Sep 12 14:14:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:14:09,240 main INFO screen PTF pass=1 dev=0.0 ins=13.69 pro=30 1a=False 1b=False 2=False (3.9s)
Sep 12 14:14:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:14:47,956 main INFO screen $CAJUN pass=0 dev=0.49 ins=0.0 pro=4 1a=False 1b=False 2=False (8.6s)
Sep 12 14:15:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:15:27,935 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 12 14:15:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:15:29,066 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 14:15:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:15:37,088 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:15:37 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 14:15:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:15:49,779 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:15:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:15:54,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:03,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:09,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:16,209 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (26.5s)
Sep 12 14:16:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:22,498 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:27,571 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:28,075 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.3s)
Sep 12 14:16:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:44,308 main INFO screen HUMANITY pass=0 dev=0.0 ins=17.05 pro=70 1a=False 1b=False 2=True (22.6s)
Sep 12 14:16:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:45,774 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:16:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:46,722 main INFO screen $CAJUN pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 12 14:16:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:16:50,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:17:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:17:07,918 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (22.2s)
Sep 12 14:17:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:17:12,884 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:17:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:17:17,999 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:17:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:17:38,958 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.1s)
Sep 12 14:17:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:17:45,349 main INFO screen NEED pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 14:18:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:01,572 main INFO screen HORACE pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 12 14:18:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:03,834 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:18:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:08,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:18:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:12,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:18:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:14,518 main INFO screen BPCATE pass=0 dev=0.68 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 12 14:18:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:18,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:18:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:24,757 main INFO screen Degenerates pass=0 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=True (21.0s)
Sep 12 14:18:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:34,231 main INFO screen HEDGEHOG pass=0 dev=0.0 ins=23.26 pro=38 1a=False 1b=False 2=True (21.3s)
Sep 12 14:18:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:35,786 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:18:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:18:40,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:19:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:00,149 main INFO screen K-Train pass=0 dev=5.7 ins=28.94 pro=69 1a=False 1b=False 2=True (24.4s)
Sep 12 14:19:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:13,749 main INFO screen PTF pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (3.8s)
Sep 12 14:19:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:26,233 main INFO screen LaMisery pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (9.4s)
Sep 12 14:19:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:41,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:19:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:42,922 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 12 14:19:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:19:46,212 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:20:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:05,897 main INFO screen FOMOGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (24.8s)
Sep 12 14:20:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:09,600 main INFO screen gold pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 12 14:20:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:16,066 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:20:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:21,098 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:20:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:28,987 main INFO screen Frontier pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 14:20:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:20:40,210 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.2s)
Sep 12 14:21:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:21:04,702 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:21:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:21:13,654 main INFO screen HUMANITY pass=0 dev=0.0 ins=15.18 pro=23 1a=False 1b=False 2=True (9.2s)
Sep 12 14:21:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:21:27,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:21:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:21:32,289 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:21:32 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T14:15:36Z
--- update 2026-09-12T14:21:31Z
Running as unit: schaduwbot-wallets.service; invocation ID: 231ef89f1987467a9f6d8d397018c1e2
analyses gestart (02faa7a55c91)
```

## Analyses (laatste 25 regels)
```
active
14:13:56 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 14:13 UTC
14:13:56 56462 tokens geladen
14:13:59   2000 tokens, 250869 trades, 49721 posities (3s)
14:14:02   4000 tokens, 496962 trades, 96458 posities (6s)
14:14:05   6000 tokens, 727430 trades, 139630 posities (8s)
14:14:07   8000 tokens, 958130 trades, 181193 posities (11s)
14:14:10   10000 tokens, 1192071 trades, 225932 posities (14s)
14:14:13   12000 tokens, 1464544 trades, 280776 posities (16s)
14:14:15   14000 tokens, 1721171 trades, 332440 posities (19s)
14:14:18   16000 tokens, 1949466 trades, 370903 posities (21s)
14:14:21   18000 tokens, 2207875 trades, 421304 posities (24s)
14:14:23   20000 tokens, 2437481 trades, 463507 posities (27s)
14:14:26   22000 tokens, 2711250 trades, 521128 posities (29s)
14:14:28   24000 tokens, 2954125 trades, 564538 posities (32s)
14:14:30   26000 tokens, 3191397 trades, 606694 posities (34s)
14:14:32   28000 tokens, 3419253 trades, 650567 posities (36s)
14:14:35   30000 tokens, 3665909 trades, 698549 posities (38s)
14:14:37   32000 tokens, 3923754 trades, 748685 posities (41s)
14:14:39 posities: 802052 uit 4144083 trades (43s)
14:14:49 168023 wallets gerekend
14:14:50 geluk-toets
14:15:25 persistentie
14:15:28 kopieer-simulatie
14:15:42 klaar in 106s -> /opt/schaduwbot/reports/wallets.md
14:21:32 31764 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
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
