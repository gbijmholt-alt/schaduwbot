# Schaduwbot status

- tijd: 2026-09-13 01:47:00 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 12 hours, 0 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.1G/38G | geheugen: 1296/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 18793, "tokens_in_memory": 6779, "msgs": 2108048, "trades": 617979, "creates": 6779, "decode_fail": 56621, "rpc_calls": 16160, "rpc_errors": 2, "sol_usd": 102.14580124774069, "open_positions": 37, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 1696 | 188 | 0 | 199 | 29 | 351 | 1070 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 600 | 16% | 1.7% | +43.5% | -15.9% | -6.10% | 100% |
| dip35_V1_gescreend_fail | 4682 | 27% | 3.9% | +45.2% | -26.0% | -6.77% | 100% |
| dip35_V1_alle | 6192 | 26% | 4.0% | +44.5% | -25.4% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 598 | 22% | 2.3% | +41.1% | -20.2% | -6.60% | 100% |
| dip35_V2_gescreend_fail | 4753 | 25% | 4.4% | +54.8% | -28.0% | -7.03% | 100% |
| dip35_V2_alle | 6149 | 25% | 4.5% | +52.3% | -27.7% | -7.99% | 100% |
| dip35_V3_gescreend_pass | 605 | 9% | 3.0% | +261.0% | -21.9% | +4.28% | 100% |
| dip35_V3_gescreend_fail | 4876 | 14% | 6.1% | +118.2% | -29.7% | -9.41% | 100% |
| dip35_V3_alle | 6207 | 13% | 6.1% | +117.3% | -29.3% | -9.99% | 100% |
| dip40_V1_gescreend_pass | 571 | 14% | 1.8% | +44.5% | -15.4% | -6.73% | 100% |
| dip40_V1_gescreend_fail | 4603 | 26% | 3.9% | +46.8% | -25.8% | -6.66% | 100% |
| dip40_V1_alle | 5952 | 26% | 3.9% | +46.5% | -25.2% | -6.89% | 100% |
| dip40_V2_gescreend_pass | 571 | 18% | 2.1% | +43.7% | -19.5% | -8.31% | 100% |
| dip40_V2_gescreend_fail | 4649 | 25% | 4.3% | +54.7% | -27.9% | -7.04% | 100% |
| dip40_V2_alle | 5902 | 24% | 4.5% | +53.0% | -27.6% | -8.05% | 100% |
| dip40_V3_gescreend_pass | 577 | 8% | 2.6% | +253.8% | -20.9% | +1.49% | 100% |
| dip40_V3_gescreend_fail | 4760 | 13% | 5.8% | +113.8% | -29.4% | -10.34% | 100% |
| dip40_V3_alle | 5962 | 13% | 5.9% | +113.0% | -29.1% | -10.90% | 100% |
| dip45_V1_gescreend_pass | 550 | 15% | 1.6% | +47.2% | -15.2% | -6.02% | 100% |
| dip45_V1_gescreend_fail | 4519 | 27% | 3.6% | +48.2% | -25.6% | -5.53% | 100% |
| dip45_V1_alle | 5755 | 26% | 3.6% | +48.3% | -25.0% | -5.93% | 100% |
| dip45_V2_gescreend_pass | 549 | 18% | 2.0% | +42.7% | -19.5% | -8.02% | 100% |
| dip45_V2_gescreend_fail | 4558 | 25% | 4.0% | +58.4% | -27.6% | -5.86% | 100% |
| dip45_V2_alle | 5706 | 24% | 4.2% | +56.9% | -27.3% | -6.85% | 100% |
| dip45_V3_gescreend_pass | 556 | 8% | 2.2% | +286.8% | -20.2% | +4.62% | 100% |
| dip45_V3_gescreend_fail | 4651 | 14% | 5.5% | +120.8% | -29.0% | -8.04% | 100% |
| dip45_V3_alle | 5754 | 13% | 5.5% | +122.9% | -28.6% | -8.70% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 473 | 16% | 5.1% | -8.20% | -11.4% tot -5.0% | -14.3% | – | 100% |
| per_token_zonder_xlink | 145 | 23% | 0.0% | +16.09% | -11.7% tot +43.9% | -13.1% | 132% | 58% |
| gepoold_met_xlink | 3962 | 13% | 2.8% | -9.38% | -10.6% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1215 | 18% | 0.0% | +15.87% | -0.2% tot +32.0% | -14.0% | 72% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 01:11:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:11:31,200 main INFO screen 100k/Rug pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.3s)
Sep 13 01:12:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:13,711 main INFO screen Journal pass=0 dev=0.0 ins=16.36 pro=62 1a=False 1b=False 2=True (66.3s)
Sep 13 01:12:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:26,567 main INFO screen ROSHI pass=0 dev=0.01 ins=0.0 pro=4 1a=False 1b=False 2=False (64.0s)
Sep 13 01:12:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:32,577 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.4s)
Sep 13 01:13:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:13:10,332 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 13 01:14:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:14:50,285 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:14:50 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:15:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:00,867 main INFO screen sol  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (74.4s)
Sep 13 01:15:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:24,336 main INFO screen BFC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (77.0s)
Sep 13 01:15:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:26,811 main INFO screen FL pass=0 dev=0.38 ins=0.0 pro=7 1a=False 1b=False 2=False (80.3s)
Sep 13 01:16:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:16,522 main INFO screen ​ pass=0 dev=0.0 ins=34.48 pro=70 1a=False 1b=False 2=True (75.7s)
Sep 13 01:16:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:28,690 main INFO screen LioraLLM pass=0 dev=0.17 ins=48.7 pro=24 1a=False 1b=False 2=True (64.4s)
Sep 13 01:16:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:56,093 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.9s)
Sep 13 01:17:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:19,001 main INFO screen duluth pass=0 dev=1.83 ins=0.0 pro=2 1a=False 1b=False 2=False (62.5s)
Sep 13 01:17:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:40,954 main INFO screen DUCKUS pass=1 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (58.3s)
Sep 13 01:17:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:47,385 main INFO screen Flybot pass=0 dev=0.0 ins=21.92 pro=23 1a=False 1b=False 2=False (51.3s)
Sep 13 01:18:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:22,860 main INFO screen Sherwood pass=0 dev=0.0 ins=10.35 pro=58 1a=False 1b=False 2=True (63.9s)
Sep 13 01:18:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:33,502 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 13 01:18:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:46,314 main INFO screen REDSKINS pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 13 01:19:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:21,002 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 13 01:19:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:27,375 aiohttp.access INFO 47.251.185.198 [13/Sep/2026:01:19:27 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 01:19:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:27,703 aiohttp.access INFO 47.251.185.198 [13/Sep/2026:01:19:27 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 13 01:19:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:41,558 main INFO screen speed pass=1 dev=0.0 ins=2.29 pro=50 1a=False 1b=False 2=False (68.1s)
Sep 13 01:20:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:20:36,651 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:20:36 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 01:20:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:20:38,986 main INFO screen $spideyy pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 13 01:21:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:21:48,354 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.5s)
Sep 13 01:22:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:22:15,515 aiohttp.access INFO 104.248.206.108 [13/Sep/2026:01:22:15 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
Sep 13 01:23:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:05,886 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.4s)
Sep 13 01:23:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:18,954 main INFO screen FLYPAD pass=0 dev=1.0 ins=45.05 pro=66 1a=False 1b=False 2=True (73.5s)
Sep 13 01:23:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:21,312 main INFO screen $4Stock pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 13 01:23:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:58,573 main INFO screen dihcoin pass=0 dev=0.0 ins=16.96 pro=36 1a=False 1b=False 2=True (52.7s)
Sep 13 01:24:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:15,381 main INFO screen MCAT pass=0 dev=0.0 ins=78.96 pro=1 1a=True 1b=True 2=True (56.4s)
Sep 13 01:24:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:55,474 main INFO screen Pump pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (74.6s)
Sep 13 01:24:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:58,747 main INFO screen ROSHI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 13 01:25:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:25:33,589 main INFO screen Gregory pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=True (75.2s)
Sep 13 01:25:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:25:37,131 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:25:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:25:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:25:56,420 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.4s)
Sep 13 01:28:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:28:09,556 main INFO screen SEXI pass=1 dev=0.0 ins=9.16 pro=59 1a=False 1b=False 2=False (62.5s)
Sep 13 01:28:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:28:40,483 main INFO screen CATGEMINI pass=0 dev=0.38 ins=78.96 pro=6 1a=False 1b=True 2=True (57.1s)
Sep 13 01:29:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:29:12,166 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.1s)
Sep 13 01:29:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:29:52,604 main INFO screen $GOAT pass=0 dev=0.97 ins=0.0 pro=4 1a=False 1b=False 2=False (62.0s)
Sep 13 01:30:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:30:10,688 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (70.0s)
Sep 13 01:30:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:30:25,390 main INFO screen PVS pass=0 dev=0.01 ins=0.0 pro=3 1a=False 1b=False 2=False (62.9s)
Sep 13 01:30:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:30:31,126 rpc WARNING rpc getTokenLargestAccounts exc Server disconnected
Sep 13 01:30:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:30:50,583 main INFO screen CAJUN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 13 01:30:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:30:51,919 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:30:51 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:31:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:31:27,137 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.0s)
Sep 13 01:32:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:32:40,396 main INFO screen AUTO AGENT pass=0 dev=0.02 ins=0.0 pro=5 1a=False 1b=False 2=False (77.7s)
Sep 13 01:32:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:32:49,808 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.2s)
Sep 13 01:34:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:34:49,200 main INFO screen SBT pass=0 dev=0.0 ins=23.47 pro=60 1a=False 1b=False 2=True (119.5s)
Sep 13 01:36:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:36:00,933 main INFO screen Cat pass=1 dev=0.79 ins=0.0 pro=11 1a=False 1b=False 2=False (89.2s)
Sep 13 01:36:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:36:02,490 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (90.6s)
Sep 13 01:36:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:36:08,306 main INFO screen SPL pass=0 dev=0.0 ins=15.59 pro=72 1a=False 1b=False 2=True (79.1s)
Sep 13 01:36:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:36:31,780 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:36:31 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:37:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:37:13,677 main INFO screen LLM pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (71.2s)
Sep 13 01:37:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:37:14,436 main INFO screen SPL pass=0 dev=0.0 ins=40.94 pro=74 1a=False 1b=False 2=True (73.5s)
Sep 13 01:37:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:37:19,777 main INFO screen DOOYET pass=0 dev=51.51 ins=0.0 pro=14 1a=False 1b=False 2=False (71.5s)
Sep 13 01:38:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:38:20,051 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (65.6s)
Sep 13 01:38:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:38:23,163 main INFO screen XSL pass=0 dev=0.0 ins=36.16 pro=57 1a=False 1b=False 2=True (69.5s)
Sep 13 01:38:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:38:27,460 main INFO screen son pass=1 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (65.7s)
Sep 13 01:39:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:39:38,578 main INFO screen SDF pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (71.1s)
Sep 13 01:39:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:39:40,325 main INFO screen IRL pass=1 dev=0.0 ins=17.16 pro=75 1a=False 1b=False 2=False (80.3s)
Sep 13 01:39:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:39:42,503 main INFO screen Cat pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (79.3s)
Sep 13 01:40:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:40:30,394 main INFO screen PNKY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.8s)
Sep 13 01:40:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:40:34,837 main INFO screen PMARCA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 13 01:40:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:40:41,318 main INFO screen $kiyana pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.0s)
Sep 13 01:41:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:41:37,346 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:41:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:41:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:41:43,378 main INFO screen FRONT pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (73.0s)
Sep 13 01:41:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:41:46,804 main INFO screen DOOYET pass=0 dev=26.49 ins=0.0 pro=20 1a=False 1b=False 2=False (72.0s)
Sep 13 01:41:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:41:51,217 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (69.9s)
Sep 13 01:43:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:43:17,534 main INFO screen MISSILE pass=1 dev=0.0 ins=16.21 pro=54 1a=False 1b=False 2=False (67.7s)
Sep 13 01:43:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:43:39,907 main INFO screen OpenAI pass=0 dev=99.32 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 13 01:44:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:44:04,259 main INFO screen CAJUN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (64.1s)
Sep 13 01:44:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:44:07,444 main INFO screen Rolex pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.9s)
Sep 13 01:44:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:44:32,392 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (52.5s)
Sep 13 01:44:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:44:54,826 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.6s)
Sep 13 01:45:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:45:23,154 main INFO screen RobIncog pass=0 dev=0.0 ins=48.8 pro=34 1a=False 1b=False 2=True (59.1s)
Sep 13 01:45:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:45:33,451 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.1s)
Sep 13 01:46:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:46:01,497 main INFO screen FLM pass=1 dev=0.0 ins=17.92 pro=44 1a=False 1b=False 2=False (66.7s)
Sep 13 01:46:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:46:11,549 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (48.4s)
Sep 13 01:47:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:47:00,983 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:47:00 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T00:17:36Z
--- update 2026-09-13T00:22:47Z
--- update 2026-09-13T00:27:48Z
--- update 2026-09-13T00:32:51Z
--- update 2026-09-13T00:38:16Z
--- update 2026-09-13T00:43:31Z
--- update 2026-09-13T00:48:36Z
--- update 2026-09-13T00:53:44Z
--- update 2026-09-13T00:59:15Z
--- update 2026-09-13T01:04:36Z
--- update 2026-09-13T01:09:45Z
--- update 2026-09-13T01:14:49Z
--- update 2026-09-13T01:20:35Z
--- update 2026-09-13T01:25:36Z
--- update 2026-09-13T01:30:50Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1f41f3dc42b0489e96e2321b9527b30f
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T01:36:30Z
--- update 2026-09-13T01:41:36Z
--- update 2026-09-13T01:47:00Z
```

## Analyses (laatste 25 regels)
```
inactive
01:38:38   8000 tokens, 896463 trades, 154963 posities (7s)
01:38:39   10000 tokens, 1118644 trades, 190444 posities (8s)
01:38:41   12000 tokens, 1338288 trades, 228593 posities (10s)
01:38:43   14000 tokens, 1559070 trades, 261143 posities (12s)
01:38:45   16000 tokens, 1815116 trades, 309221 posities (14s)
01:38:47   18000 tokens, 2054344 trades, 353904 posities (16s)
01:38:49   20000 tokens, 2273316 trades, 387540 posities (17s)
01:38:51   22000 tokens, 2497395 trades, 423098 posities (19s)
01:38:53   24000 tokens, 2734666 trades, 464849 posities (22s)
01:38:55   26000 tokens, 2948676 trades, 499259 posities (24s)
01:38:57   28000 tokens, 3193751 trades, 544763 posities (26s)
01:38:59   30000 tokens, 3417064 trades, 581170 posities (28s)
01:39:02   32000 tokens, 3645058 trades, 619865 posities (31s)
01:39:05   34000 tokens, 3861173 trades, 655601 posities (33s)
01:39:07   36000 tokens, 4091321 trades, 695494 posities (36s)
01:39:10   38000 tokens, 4311336 trades, 733577 posities (39s)
01:39:13   40000 tokens, 4549726 trades, 777004 posities (42s)
01:39:16   42000 tokens, 4787461 trades, 819867 posities (45s)
01:39:19   44000 tokens, 5019931 trades, 871749 posities (48s)
01:39:21 posities: 893712 uit 5124941 trades (50s)
01:39:30 187794 wallets gerekend
01:39:31 geluk-toets
01:40:02 persistentie
01:40:04 kopieer-simulatie
01:40:38 klaar in 127s -> /opt/schaduwbot/reports/wallets.md
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
