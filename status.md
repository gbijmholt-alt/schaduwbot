# Schaduwbot status

- tijd: 2026-09-12 13:59:48 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 12 minutes
- bot-service: active
- code-versie: 1f31a46
- schijf: 3.6G/38G | geheugen: 678/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 14848, "tokens_in_memory": 3496, "msgs": 1266834, "trades": 352023, "creates": 3496, "decode_fail": 15968, "rpc_calls": 10499, "rpc_errors": 465, "sol_usd": 101.92962916528221, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 13:43:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:48,892 main INFO screen Sherwood pass=1 dev=0.0 ins=16.46 pro=24 1a=False 1b=False 2=False (3.9s)
Sep 12 13:43:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:57,383 main INFO screen KDAY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 12 13:44:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:05,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:44:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:10,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:44:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:25,508 main INFO screen SOL pass=0 dev=0.0 ins=21.99 pro=57 1a=False 1b=False 2=True (20.5s)
Sep 12 13:44:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:27,144 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:44:27 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 13:45:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:26,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:45:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:35,924 main INFO screen Celebrity pass=0 dev=0.0 ins=20.97 pro=60 1a=False 1b=False 2=False (9.5s)
Sep 12 13:45:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:36,133 main INFO screen PAPERBAG pass=0 dev=0.0 ins=21.4 pro=33 1a=False 1b=False 2=True (2.5s)
Sep 12 13:47:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:35,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:47:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:40,249 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:47:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:53,510 main INFO screen anonwjak pass=0 dev=0.07 ins=79.24 pro=9 1a=False 1b=True 2=True (18.4s)
Sep 12 13:48:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:48:03,986 main INFO screen Celebrity pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 12 13:49:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:26,992 main INFO screen fg pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 12 13:49:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:37,153 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:49:37 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 13:49:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:42,131 main INFO screen rekt pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 12 13:49:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:56,508 main INFO screen $CAJUN pass=0 dev=0.62 ins=0.0 pro=3 1a=False 1b=False 2=False (3.7s)
Sep 12 13:50:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:50:51,603 main INFO screen bundloor pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 12 13:51:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:19,099 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:51:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:24,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:51:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:39,910 main INFO screen GachaPad pass=0 dev=0.0 ins=4.65 pro=64 1a=False 1b=False 2=True (20.9s)
Sep 12 13:51:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:42,103 main INFO screen Celebrity pass=1 dev=0.0 ins=16.78 pro=38 1a=False 1b=False 2=False (2.9s)
Sep 12 13:51:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:48,856 main INFO screen cap pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (5.3s)
Sep 12 13:51:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:51,354 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 12 13:51:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:51:53,542 main INFO screen HORACE pass=0 dev=0.0 ins=20.15 pro=44 1a=False 1b=False 2=True (2.5s)
Sep 12 13:52:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:52:22,499 main INFO screen PUSSY pass=0 dev=0.21 ins=0.04 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 12 13:53:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:10,198 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:53:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:13,260 main INFO screen PEPEGROK pass=0 dev=0.18 ins=77.58 pro=9 1a=False 1b=True 2=True (3.5s)
Sep 12 13:53:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:15,435 main INFO screen VPEPE pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (5.7s)
Sep 12 13:53:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:18,756 main INFO screen 1coins pass=0 dev=0.25 ins=0.0 pro=4 1a=False 1b=False 2=False (5.5s)
Sep 12 13:53:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:19,264 main INFO screen BRANDON pass=0 dev=74.7 ins=0.0 pro=13 1a=False 1b=False 2=True (9.3s)
Sep 12 13:53:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:20,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:53:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:28,290 main INFO screen 💵 pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 12 13:53:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:42,013 main INFO screen LaMisery pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 12 13:53:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:48,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:53:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:53,759 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:53:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:55,256 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:53:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:57,685 aiohttp.access INFO 89.42.231.200 [12/Sep/2026:13:53:57 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 13:53:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:53:57,931 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:13:53:57 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 13:54:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:02,363 main INFO screen hellobaby pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.2s)
Sep 12 13:54:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:08,313 main INFO screen HORACE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (19.6s)
Sep 12 13:54:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:12,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:15,213 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:17,710 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:17,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:20,271 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:22,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:54:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:32,091 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.5s)
Sep 12 13:54:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:36,378 main INFO screen GMEx pass=0 dev=0.0 ins=49.51 pro=66 1a=True 1b=True 2=True (21.2s)
Sep 12 13:54:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:37,203 main INFO screen Peedy pass=0 dev=0.17 ins=48.65 pro=11 1a=False 1b=False 2=True (19.4s)
Sep 12 13:54:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:39,151 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:54:39 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 13:54:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:54:45,204 main INFO screen RDJ pass=1 dev=0.86 ins=0.0 pro=46 1a=False 1b=False 2=False (3.9s)
Sep 12 13:55:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:02,175 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 12 13:55:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:21,183 main INFO screen Remember pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 12 13:55:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:34,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:55:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:38,227 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:55:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:42,249 main INFO screen $CAT pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 13:55:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:55:43,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T12:41:36Z
--- update 2026-09-12T12:47:05Z
--- update 2026-09-12T12:52:10Z
--- update 2026-09-12T12:57:36Z
--- update 2026-09-12T13:02:55Z
nieuwe code: 1f31a46
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 88310e2f16cc42c39aad06b1953b4bf1
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
```

## Analyses (laatste 25 regels)
```
inactive
13:12:48 klaar in 2s: 17367 tokens, 891 nieuw -> /opt/schaduwbot/reports/video_replay.md
13:12:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 13:12 UTC
13:12:48 55478 tokens geladen
13:12:51   2000 tokens, 249962 trades, 50569 posities (2s)
13:12:53   4000 tokens, 493968 trades, 97416 posities (4s)
13:12:55   6000 tokens, 732147 trades, 142845 posities (6s)
13:12:57   8000 tokens, 964228 trades, 186079 posities (8s)
13:12:58   10000 tokens, 1201571 trades, 229531 posities (10s)
13:13:01   12000 tokens, 1476021 trades, 287458 posities (13s)
13:13:04   14000 tokens, 1723248 trades, 333950 posities (15s)
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
