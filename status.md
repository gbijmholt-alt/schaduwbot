# Schaduwbot status

- tijd: 2026-09-15 06:15:39 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 16 hours, 28 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2352/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 171691, "tokens_in_memory": 7278, "msgs": 25997980, "trades": 5199508, "creates": 55620, "decode_fail": 442743, "rpc_calls": 149701, "rpc_errors": 13, "sol_usd": 101.31645935681783, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 5572 | 625 | 10 | 635 | 107 | 1125 | 3395 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 617 | 17% | 1.6% | +43.2% | -15.9% | -5.99% | 100% |
| dip35_V1_gescreend_fail | 4728 | 27% | 4.0% | +45.1% | -25.9% | -6.78% | 100% |
| dip35_V1_alle | 6456 | 26% | 4.0% | +44.4% | -25.5% | -7.05% | 100% |
| dip35_V2_gescreend_pass | 616 | 23% | 2.3% | +40.7% | -20.1% | -6.31% | 100% |
| dip35_V2_gescreend_fail | 4810 | 25% | 4.4% | +54.6% | -27.9% | -7.05% | 100% |
| dip35_V2_alle | 6416 | 25% | 4.5% | +52.3% | -27.8% | -7.95% | 100% |
| dip35_V3_gescreend_pass | 625 | 9% | 3.2% | +253.7% | -21.9% | +3.65% | 100% |
| dip35_V3_gescreend_fail | 4943 | 14% | 6.1% | +119.4% | -29.6% | -9.19% | 100% |
| dip35_V3_alle | 6472 | 13% | 6.1% | +116.5% | -29.4% | -10.33% | 100% |
| dip40_V1_gescreend_pass | 588 | 15% | 1.7% | +43.7% | -15.4% | -6.70% | 100% |
| dip40_V1_gescreend_fail | 4653 | 26% | 3.9% | +46.6% | -25.7% | -6.64% | 100% |
| dip40_V1_alle | 6210 | 26% | 3.9% | +46.4% | -25.3% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 589 | 18% | 2.0% | +43.0% | -19.4% | -7.95% | 100% |
| dip40_V2_gescreend_fail | 4712 | 25% | 4.3% | +54.6% | -27.8% | -6.97% | 100% |
| dip40_V2_alle | 6164 | 24% | 4.4% | +53.3% | -27.6% | -7.94% | 100% |
| dip40_V3_gescreend_pass | 598 | 8% | 2.8% | +251.7% | -21.0% | +1.83% | 100% |
| dip40_V3_gescreend_fail | 4828 | 13% | 5.8% | +115.5% | -29.3% | -9.97% | 100% |
| dip40_V3_alle | 6220 | 13% | 5.9% | +113.2% | -29.1% | -11.05% | 100% |
| dip45_V1_gescreend_pass | 568 | 15% | 1.6% | +46.7% | -15.1% | -5.90% | 100% |
| dip45_V1_gescreend_fail | 4570 | 27% | 3.6% | +48.0% | -25.5% | -5.53% | 100% |
| dip45_V1_alle | 6003 | 26% | 3.6% | +48.1% | -25.1% | -6.06% | 100% |
| dip45_V2_gescreend_pass | 567 | 19% | 1.9% | +42.4% | -19.4% | -7.86% | 100% |
| dip45_V2_gescreend_fail | 4621 | 25% | 4.0% | +58.3% | -27.5% | -5.83% | 100% |
| dip45_V2_alle | 5957 | 24% | 4.1% | +56.9% | -27.3% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 578 | 8% | 2.4% | +276.6% | -20.3% | +3.82% | 100% |
| dip45_V3_gescreend_fail | 4723 | 14% | 5.4% | +121.9% | -28.9% | -7.66% | 100% |
| dip45_V3_alle | 6006 | 13% | 5.5% | +121.6% | -28.7% | -8.97% | 100% |

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
| per_token_met_xlink | 488 | 16% | 5.3% | -8.21% | -11.3% tot -5.1% | -14.3% | – | 100% |
| per_token_zonder_xlink | 154 | 23% | 0.0% | +18.49% | -8.6% tot +45.6% | -13.1% | 119% | 58% |
| gepoold_met_xlink | 4066 | 14% | 2.9% | -9.32% | -10.5% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1280 | 18% | 0.0% | +15.22% | -0.1% tot +30.5% | -14.3% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 15 05:52:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:52:05,286 main INFO screen PweaseBul pass=0 dev=0.0 ins=55.92 pro=14 1a=False 1b=False 2=True (58.7s)
Sep 15 05:52:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:52:36,958 main INFO screen HYPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (52.3s)
Sep 15 05:52:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:52:50,551 main INFO screen zazu pass=0 dev=0.0 ins=2.2 pro=65 1a=False 1b=False 2=False (66.7s)
Sep 15 05:53:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:53:04,019 aiohttp.access INFO 204.76.203.92 [15/Sep/2026:05:53:04 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 05:53:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:53:08,420 main INFO screen SMILE pass=0 dev=0.0 ins=28.34 pro=57 1a=False 1b=False 2=True (63.1s)
Sep 15 05:53:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:53:35,864 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.9s)
Sep 15 05:54:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:01,769 main INFO screen CHILLBULL pass=0 dev=0.0 ins=55.81 pro=67 1a=False 1b=False 2=True (71.2s)
Sep 15 05:54:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:08,532 main INFO screen stockless pass=0 dev=0.0 ins=25.98 pro=70 1a=False 1b=False 2=True (60.1s)
Sep 15 05:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:13,913 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:13 +0000] "GET /actuator/env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:13,986 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:13 +0000] "GET /env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,060 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /actuator/env.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,133 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /management/env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,207 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /.env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,281 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /.env.production HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,356 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /.env.local HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,430 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /.env.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,504 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /application.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:14,578 aiohttp.access INFO 178.16.55.205 [15/Sep/2026:05:54:14 +0000] "GET /application.properties HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 05:54:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:54:33,451 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 05:55:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:55:13,646 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.9s)
Sep 15 05:55:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:55:14,041 main INFO screen AIBUBBLE pass=0 dev=0.0 ins=23.56 pro=44 1a=False 1b=False 2=False (65.5s)
Sep 15 05:55:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:55:32,357 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:55:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:55:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:55:45,266 main INFO screen zazu pass=0 dev=0.0 ins=17.69 pro=72 1a=False 1b=False 2=True (71.8s)
Sep 15 05:56:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:56:28,105 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (74.5s)
Sep 15 05:56:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:56:34,350 main INFO screen bSOL pass=0 dev=0.0 ins=0.32 pro=72 1a=False 1b=False 2=False (80.3s)
Sep 15 05:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:56:50,814 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (65.5s)
Sep 15 05:57:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:57:17,522 main INFO screen HYPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.4s)
Sep 15 05:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:57:28,883 main INFO screen BetOnBlak pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (54.5s)
Sep 15 05:57:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:57:55,746 main INFO screen SOLCAT pass=0 dev=0.0 ins=9.21 pro=61 1a=False 1b=False 2=False (64.9s)
Sep 15 05:58:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:58:06,748 main INFO screen HUHCAT pass=0 dev=0.0 ins=35.63 pro=25 1a=False 1b=False 2=True (49.2s)
Sep 15 05:58:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:58:33,126 main INFO screen PEPE pass=0 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=False (64.2s)
Sep 15 05:59:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:59:01,167 main INFO screen HUHCAT pass=0 dev=0.0 ins=18.4 pro=61 1a=False 1b=False 2=False (65.4s)
Sep 15 05:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:59:06,620 main INFO screen ECTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.9s)
Sep 15 05:59:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:59:26,779 main INFO screen Google pass=0 dev=0.0 ins=163.6 pro=0 1a=False 1b=False 2=True (53.7s)
Sep 15 06:00:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:00:05,444 main INFO screen SOLCAT pass=0 dev=0.0 ins=9.64 pro=68 1a=False 1b=False 2=False (64.3s)
Sep 15 06:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:00:15,015 main INFO screen Cat pass=0 dev=0.0 ins=21.1 pro=36 1a=False 1b=False 2=False (68.4s)
Sep 15 06:00:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:00:32,969 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:00:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:00:37,109 main INFO screen Bytes pass=0 dev=0.0 ins=10.63 pro=52 1a=False 1b=False 2=False (70.3s)
Sep 15 06:01:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:01:02,676 main INFO screen gMS-α pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.2s)
Sep 15 06:01:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:01:11,891 main INFO screen OpenAI pass=0 dev=0.0 ins=286.07 pro=0 1a=False 1b=False 2=True (56.9s)
Sep 15 06:01:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:01:34,285 main INFO screen SOLCAT pass=0 dev=0.0 ins=7.17 pro=71 1a=False 1b=False 2=False (57.2s)
Sep 15 06:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:02:04,602 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.9s)
Sep 15 06:02:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:02:07,102 main INFO screen HYPE pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.2s)
Sep 15 06:02:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:02:38,228 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.9s)
Sep 15 06:03:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:03:18,469 main INFO screen HashFly pass=0 dev=0.0 ins=15.43 pro=74 1a=False 1b=False 2=True (71.4s)
Sep 15 06:03:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:03:24,670 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (80.1s)
Sep 15 06:03:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:03:44,668 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.4s)
Sep 15 06:04:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:04:20,853 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.4s)
Sep 15 06:04:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:04:39,343 main INFO screen Samoyed pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=False (74.7s)
Sep 15 06:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:04:46,417 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.7s)
Sep 15 06:05:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:05:20,886 main INFO screen Wombat pass=0 dev=0.0 ins=37.26 pro=66 1a=False 1b=False 2=True (60.0s)
Sep 15 06:05:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:05:32,093 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:05:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:05:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:05:45,223 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.9s)
Sep 15 06:05:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:05:52,911 main INFO screen Cocacola pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 15 06:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:06:29,423 main INFO screen SQLana pass=0 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=True (68.5s)
Sep 15 06:07:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:07:11,377 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (78.5s)
Sep 15 06:07:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:07:11,759 main INFO screen larpcat pass=0 dev=0.0 ins=19.44 pro=54 1a=False 1b=False 2=False (86.5s)
Sep 15 06:07:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:07:38,016 main INFO screen 21CABBAGE pass=0 dev=0.0 ins=6.64 pro=36 1a=False 1b=False 2=False (68.6s)
Sep 15 06:08:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:08:26,380 main INFO screen snoopy pass=0 dev=0.0 ins=25.49 pro=74 1a=False 1b=False 2=True (75.0s)
Sep 15 06:08:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:08:28,041 main INFO screen bowl cut pass=0 dev=0.03 ins=0.0 pro=9 1a=False 1b=False 2=False (76.3s)
Sep 15 06:08:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:08:50,012 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.0s)
Sep 15 06:09:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:09:30,858 main INFO screen HUHCAT pass=0 dev=0.11 ins=120.14 pro=1 1a=False 1b=False 2=True (64.5s)
Sep 15 06:09:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:09:41,682 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (73.6s)
Sep 15 06:10:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:10:01,146 main INFO screen NFT pass=0 dev=0.0 ins=9.04 pro=67 1a=False 1b=False 2=False (71.1s)
Sep 15 06:10:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:10:33,669 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.8s)
Sep 15 06:10:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:10:37,652 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:10:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:10:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:10:46,001 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.3s)
Sep 15 06:11:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:11:10,236 main INFO screen Cocacola pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (69.1s)
Sep 15 06:11:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:11:39,946 main INFO screen SOLANADON pass=0 dev=0.0 ins=22.34 pro=42 1a=False 1b=False 2=False (66.3s)
Sep 15 06:11:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:11:59,637 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (73.6s)
Sep 15 06:12:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:12:24,297 main INFO screen BOTTLENECK pass=0 dev=0.0 ins=12.36 pro=69 1a=False 1b=False 2=True (74.1s)
Sep 15 06:12:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:12:50,755 main INFO screen NFT pass=0 dev=0.0 ins=12.6 pro=60 1a=False 1b=False 2=True (70.8s)
Sep 15 06:13:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:13:08,381 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.7s)
Sep 15 06:13:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:13:50,026 main INFO screen LSD pass=0 dev=0.0 ins=17.64 pro=61 1a=False 1b=False 2=False (85.7s)
Sep 15 06:14:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:14:02,644 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.9s)
Sep 15 06:14:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:14:16,876 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.5s)
Sep 15 06:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:14:51,138 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.1s)
Sep 15 06:15:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:15:07,705 main INFO screen UkaUka pass=0 dev=0.0 ins=11.25 pro=67 1a=False 1b=False 2=True (65.1s)
Sep 15 06:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:15:37,399 main INFO screen SMASH  pass=0 dev=0.35 ins=0.0 pro=11 1a=False 1b=False 2=False (80.5s)
Sep 15 06:15:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:15:39,654 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:15:39 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T04:59:49Z
--- update 2026-09-15T05:04:49Z
--- update 2026-09-15T05:09:51Z
--- update 2026-09-15T05:14:50Z
--- update 2026-09-15T05:19:57Z
--- update 2026-09-15T05:25:00Z
--- update 2026-09-15T05:30:09Z
--- update 2026-09-15T05:35:11Z
--- update 2026-09-15T05:40:15Z
nieuwe code: 8878e1e
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: f5672219e09449dfbd4cf05bf897dc12
analyses gestart (ef01904db983)
--- update 2026-09-15T05:45:17Z
--- update 2026-09-15T05:50:30Z
--- update 2026-09-15T05:55:30Z
--- update 2026-09-15T06:00:31Z
--- update 2026-09-15T06:05:31Z
--- update 2026-09-15T06:10:36Z
--- update 2026-09-15T06:15:38Z
```

## Analyses (laatste 25 regels)
```
active
04:42:13   74000 tokens, 7115774 trades, 877324 posities (525s)
04:42:25 posities: 894047 uit 7257996 trades (542s)
04:42:37 208926 wallets gerekend
04:42:38 geluk-toets
04:43:12 persistentie
04:43:15 kopieer-simulatie
04:45:48 klaar in 745s -> /opt/schaduwbot/reports/wallets.md
05:40:17 103493 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
05:40:38   ingelezen tot rowid 10715293 (181256 rijen, 181256 bruikbaar)
05:40:41 ingelezen: 181256 nieuwe trades, 181256 bruikbaar (25s)
05:43:45 3000 aankopen van gevolgde wallets geëvalueerd
05:44:19 vroege kopers: 281 voldoen nu, register 500, 271 tokens beoordeeld
05:44:51 grote spelers: saldo van 39 wallets opgehaald
05:45:40 herkomst: 40 posities gekoppeld
05:45:55 klaar in 338s -> /opt/schaduwbot/reports/ledger.md
06:00:45 S1: gezakt — toets n=31349, verkennend n=14656
06:00:45 klaar in 890s -> /opt/schaduwbot/reports/hypotheses.md
06:00:45 probe: 150 transacties ophalen
06:04:15 poolveld: 17 pools bekeken, 0 te gaan -> vastgesteld @43
06:05:29 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
06:05:29 prijsijk: n=177 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:05:36 na-migratie: 100 paren te checken
06:07:15 na-migratie: 69 paren, 0 prijzen
06:10:50 gemigreerde koersen: 78 gedaan, 1908 te gaan
06:10:59 klaar (589 rpc-calls, 87 fouten)
```

## IJking poolkoers (laatste 12 regels)
```
05:15:05 ijk: +5 van 5 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=155 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:15:06 ijk-diagnose: nieuwste migratie 1.0 min oud | migraties 15/60/240 min: 9/32/153 | al gemeten: 489
05:20:16 ijk: +6 van 7 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=160 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:20:16 ijk-diagnose: nieuwste migratie 0.7 min oud | migraties 15/60/240 min: 13/37/156 | al gemeten: 495
05:25:18 ijk: +6 van 7 kandidaten (18 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=166 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:25:18 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 18/38/160 | al gemeten: 501
05:30:18 ijk: +3 van 3 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 12}) | verste bak n=168 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:30:19 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 15/39/160 | al gemeten: 504
05:35:17 ijk: +2 van 2 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=170 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:35:17 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 10/39/159 | al gemeten: 506
05:40:40 ijk: +2 van 2 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=172 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:40:41 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 6/39/156 | al gemeten: 508
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
