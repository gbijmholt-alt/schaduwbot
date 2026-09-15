# Schaduwbot status

- tijd: 2026-09-15 06:00:32 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 16 hours, 13 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2374/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 170785, "tokens_in_memory": 7333, "msgs": 25918157, "trades": 5178212, "creates": 55401, "decode_fail": 440751, "rpc_calls": 148790, "rpc_errors": 13, "sol_usd": 101.37531671399994, "open_positions": 26, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 05:39:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:39:25,808 main INFO screen HUHCAT pass=0 dev=0.0 ins=9.13 pro=38 1a=False 1b=False 2=True (59.1s)
Sep 15 05:39:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:39:26,880 main INFO screen TAJRIA pass=0 dev=0.0 ins=18.45 pro=63 1a=False 1b=False 2=False (63.5s)
Sep 15 05:39:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:39:32,959 main INFO screen HUHCAT pass=0 dev=0.0 ins=26.47 pro=86 1a=False 1b=False 2=True (75.1s)
Sep 15 05:40:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:40:17,163 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:40:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:40:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:40:24,591 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.17 pro=12 1a=False 1b=False 2=True (58.8s)
Sep 15 05:40:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:40:25,266 main INFO screen DISNEY pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.4s)
Sep 15 05:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:40:35,211 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (62.3s)
Sep 15 05:41:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:41:34,021 main INFO screen Hergajera pass=0 dev=0.0 ins=22.67 pro=76 1a=False 1b=False 2=True (69.4s)
Sep 15 05:41:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:41:42,049 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.8s)
Sep 15 05:41:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:41:47,912 main INFO screen TOE pass=0 dev=0.0 ins=30.48 pro=45 1a=False 1b=False 2=True (72.7s)
Sep 15 05:42:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:42:24,842 main INFO screen TAJRIA pass=0 dev=0.0 ins=25.54 pro=66 1a=False 1b=False 2=True (50.8s)
Sep 15 05:42:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:42:35,182 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (53.1s)
Sep 15 05:42:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:42:54,488 main INFO screen HUHCAT pass=0 dev=0.0 ins=5.06 pro=74 1a=False 1b=False 2=True (66.6s)
Sep 15 05:43:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:43:21,886 main INFO screen HUHCAT pass=0 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=True (57.0s)
Sep 15 05:43:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:43:27,380 main INFO screen ACTB pass=0 dev=0.0 ins=56.24 pro=18 1a=False 1b=False 2=True (52.2s)
Sep 15 05:43:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:43:44,157 main INFO screen USDF pass=0 dev=0.0 ins=125.81 pro=1 1a=False 1b=False 2=True (49.7s)
Sep 15 05:44:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:44:31,128 main INFO screen VISH pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (69.2s)
Sep 15 05:44:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:44:34,034 main INFO screen Samoyed pass=0 dev=0.0 ins=25.77 pro=46 1a=False 1b=False 2=True (66.7s)
Sep 15 05:44:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:44:39,605 main INFO screen HUHCAT pass=0 dev=0.0 ins=9.75 pro=46 1a=False 1b=False 2=True (55.4s)
Sep 15 05:45:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:45:17,272 main INFO screen GLOVER pass=0 dev=0.0 ins=30.0 pro=21 1a=False 1b=False 2=True (46.1s)
Sep 15 05:45:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:45:18,836 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:45:18 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 05:45:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:45:23,078 main INFO screen BBC pass=0 dev=0.0 ins=176.42 pro=0 1a=False 1b=False 2=True (49.0s)
Sep 15 05:45:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:45:39,255 main INFO screen HUHCAT pass=0 dev=0.0 ins=5.58 pro=39 1a=False 1b=False 2=True (59.6s)
Sep 15 05:46:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:46:10,073 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (52.8s)
Sep 15 05:46:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:46:11,656 main INFO screen HUHCAT pass=0 dev=0.0 ins=40.25 pro=24 1a=False 1b=False 2=True (48.6s)
Sep 15 05:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:46:31,308 main INFO screen PweaseBul pass=0 dev=0.0 ins=56.23 pro=14 1a=False 1b=False 2=True (52.1s)
Sep 15 05:47:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:47:20,653 main INFO screen HUHCAT pass=0 dev=0.0 ins=11.41 pro=85 1a=False 1b=False 2=False (69.0s)
Sep 15 05:47:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:47:21,087 main INFO screen SOLCAT pass=0 dev=0.0 ins=0.0 pro=81 1a=False 1b=False 2=True (71.0s)
Sep 15 05:47:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:47:43,517 main INFO screen HUHDOG pass=0 dev=0.0 ins=12.64 pro=70 1a=False 1b=False 2=False (72.2s)
Sep 15 05:48:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:48:16,545 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (55.5s)
Sep 15 05:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:48:18,065 main INFO screen tacocat pass=0 dev=0.0 ins=28.22 pro=60 1a=False 1b=False 2=True (57.4s)
Sep 15 05:48:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:48:27,988 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:05:48:27 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 05:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:48:31,025 main INFO screen HUHCAT pass=0 dev=0.0 ins=15.33 pro=14 1a=False 1b=False 2=True (47.5s)
Sep 15 05:49:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:49:22,937 main INFO screen Family pass=0 dev=0.0 ins=0.16 pro=57 1a=False 1b=False 2=True (64.9s)
Sep 15 05:49:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:49:23,420 main INFO screen guccimorty pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.9s)
Sep 15 05:49:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:49:29,870 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.8s)
Sep 15 05:50:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:50:09,196 main INFO screen HUHCAT pass=0 dev=0.0 ins=5.06 pro=9 1a=False 1b=False 2=False (46.3s)
Sep 15 05:50:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:50:32,023 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:50:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:50:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:50:32,226 main INFO screen HUHCAT pass=0 dev=0.0 ins=11.41 pro=25 1a=False 1b=False 2=True (68.8s)
Sep 15 05:50:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:50:36,837 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (67.0s)
Sep 15 05:51:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:51:06,585 main INFO screen PEPE pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (57.4s)
Sep 15 05:51:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:51:43,864 main INFO screen RX-78-2 pass=0 dev=0.05 ins=0.0 pro=21 1a=False 1b=False 2=False (71.6s)
Sep 15 05:51:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:51:44,642 main INFO screen NINAFONE pass=0 dev=0.0 ins=79.0 pro=15 1a=False 1b=False 2=True (67.8s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T04:44:37Z
--- update 2026-09-15T04:49:40Z
--- update 2026-09-15T04:54:45Z
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
```

## Analyses (laatste 25 regels)
```
active
04:39:46   54000 tokens, 5189287 trades, 624841 posities (378s)
04:40:00   56000 tokens, 5378072 trades, 652073 posities (392s)
04:40:14   58000 tokens, 5550259 trades, 672012 posities (405s)
04:40:27   60000 tokens, 5738205 trades, 695471 posities (419s)
04:40:42   62000 tokens, 5931456 trades, 717016 posities (433s)
04:40:56   64000 tokens, 6129963 trades, 746298 posities (448s)
04:41:11   66000 tokens, 6326343 trades, 770851 posities (462s)
04:41:26   68000 tokens, 6514137 trades, 794918 posities (478s)
04:41:42   70000 tokens, 6698016 trades, 817607 posities (493s)
04:41:57   72000 tokens, 6907408 trades, 843122 posities (509s)
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
