# Schaduwbot status

- tijd: 2026-09-13 07:36:45 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 17 hours, 49 minutes
- bot-service: active
- code-versie: 8a627ef
- schijf: 4.4G/38G | geheugen: 887/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 3757, "tokens_in_memory": 712, "msgs": 265852, "trades": 55001, "creates": 712, "decode_fail": 8342, "rpc_calls": 2004, "rpc_errors": 0, "sol_usd": 101.13537590254819, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 06:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:18,562 main INFO screen $MOMO pass=1 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (73.6s)
Sep 13 06:48:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:27,427 main INFO screen Nuts pass=0 dev=0.0 ins=10.34 pro=63 1a=False 1b=False 2=True (67.3s)
Sep 13 06:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:56,445 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.5s)
Sep 13 06:49:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:26,413 main INFO screen NUT pass=1 dev=0.0 ins=3.22 pro=77 1a=False 1b=False 2=False (63.9s)
Sep 13 06:49:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:30,009 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (48.4s)
Sep 13 06:49:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:37,266 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:49:37 +0000] "GET /health HTTP/1.1" 200 492 "-" "Python-urllib/3.14"
Sep 13 06:50:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:50:56,426 main INFO screen PBJT pass=1 dev=0.0 ins=6.67 pro=57 1a=False 1b=False 2=False (68.3s)
Sep 13 06:50:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:50:58,916 main INFO screen EMPIPE pass=0 dev=0.14 ins=79.2 pro=8 1a=False 1b=False 2=True (65.5s)
Sep 13 06:53:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:53:46,365 main INFO screen ponks pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (60.7s)
Sep 13 06:54:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:54:04,297 main INFO screen Nutsack pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=True (61.1s)
Sep 13 06:54:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:54:53,289 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:54:53 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 13 06:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:56:01,147 main INFO screen PUMP pass=0 dev=0.0 ins=35.85 pro=73 1a=False 1b=False 2=True (67.0s)
Sep 13 06:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:56:39,482 main INFO screen Heist pass=0 dev=0.0 ins=18.19 pro=44 1a=False 1b=False 2=True (69.4s)
Sep 13 06:57:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:57:25,324 main INFO screen dddd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.0s)
Sep 13 06:58:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:58:21,469 main INFO screen HOLDINGS pass=1 dev=0.0 ins=1.74 pro=22 1a=False 1b=False 2=False (70.4s)
Sep 13 07:00:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:06,596 main INFO screen PEPEHOUSE pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=False 2=True (78.2s)
Sep 13 07:00:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:10,045 main INFO screen agent pass=1 dev=0.0 ins=1.61 pro=66 1a=False 1b=False 2=False (86.4s)
Sep 13 07:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:23,101 main INFO screen BALI pass=1 dev=0.21 ins=0.0 pro=10 1a=False 1b=False 2=False (74.0s)
Sep 13 07:00:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:36,118 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:00:36 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 13 07:01:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:01:04,225 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 13 07:01:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:01:26,002 main INFO screen 男人 pass=0 dev=0.0 ins=27.12 pro=58 1a=False 1b=False 2=True (65.4s)
Sep 13 07:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:04,382 main INFO screen LILI pass=0 dev=0.0 ins=12.88 pro=52 1a=False 1b=False 2=True (72.4s)
Sep 13 07:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:21,225 main INFO screen mmrich pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (58.3s)
Sep 13 07:02:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:53,073 main INFO screen PRINCESSV pass=0 dev=0.06 ins=0.0 pro=6 1a=False 1b=False 2=False (70.4s)
Sep 13 07:05:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:01,206 main INFO screen ANONPUMP pass=0 dev=0.04 ins=77.96 pro=8 1a=False 1b=True 2=True (55.2s)
Sep 13 07:05:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:16,695 main INFO screen NIGER pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (48.2s)
Sep 13 07:05:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:37,160 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:05:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:06:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:06:05,253 main INFO screen SS pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=True (48.8s)
Sep 13 07:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:08:37,203 main INFO screen sirpump pass=0 dev=0.11 ins=79.2 pro=9 1a=False 1b=True 2=True (54.3s)
Sep 13 07:09:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:07,392 main INFO screen SAVPIR pass=0 dev=7.97 ins=0.0 pro=6 1a=False 1b=False 2=False (79.9s)
Sep 13 07:09:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:30,524 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (61.7s)
Sep 13 07:09:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:49,335 main INFO screen PSYCHO pass=0 dev=1.57 ins=0.0 pro=1 1a=False 1b=False 2=False (72.1s)
Sep 13 07:10:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:10:40,021 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:10:40 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:11:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:11:55,820 main INFO screen GROK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (63.0s)
Sep 13 07:12:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:12:01,057 main INFO screen ASI pass=0 dev=0.0 ins=30.95 pro=41 1a=False 1b=False 2=True (60.3s)
Sep 13 07:12:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:12:32,588 main INFO screen PFS pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (69.5s)
Sep 13 07:13:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:03,094 main INFO screen GHOSTDOG pass=0 dev=35.46 ins=0.0 pro=2 1a=False 1b=False 2=True (67.3s)
Sep 13 07:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:11,067 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.0s)
Sep 13 07:13:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:52,391 main INFO screen ASI pass=1 dev=0.0 ins=1.35 pro=73 1a=False 1b=False 2=False (79.8s)
Sep 13 07:14:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:14:56,002 main INFO screen Pepex pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.6s)
Sep 13 07:16:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:16:11,466 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:16:11 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:17:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:17:56,616 main INFO screen HALH pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 13 07:18:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:18:46,536 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.0s)
Sep 13 07:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:18:49,135 main INFO screen HOUSECAT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.7s)
Sep 13 07:19:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:19:26,200 main INFO screen LMAO pass=0 dev=0.13 ins=0.0 pro=2 1a=False 1b=False 2=False (66.3s)
Sep 13 07:21:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:21:11,741 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:21:11 +0000] "GET /health HTTP/1.1" 200 493 "-" "Python-urllib/3.14"
Sep 13 07:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:22:06,648 main INFO screen Fluffy pass=0 dev=0.0 ins=30.53 pro=62 1a=False 1b=False 2=True (61.5s)
Sep 13 07:23:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:23:50,918 main INFO screen PCAT pass=0 dev=0.0 ins=28.6 pro=43 1a=False 1b=False 2=True (63.7s)
Sep 13 07:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:24:49,210 main INFO screen JubTrump pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (54.1s)
Sep 13 07:25:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:25:30,912 main INFO screen LAMB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (64.8s)
Sep 13 07:26:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:26:26,654 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:26:26 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:26:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:26:44,586 aiohttp.access INFO 148.251.56.115 [13/Sep/2026:07:26:44 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 13 07:27:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:27:03,219 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.0s)
Sep 13 07:27:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:27:22,385 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.8s)
Sep 13 07:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:28:23,284 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (64.8s)
Sep 13 07:29:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:29:07,084 main INFO screen YIN pass=0 dev=8.8 ins=26.12 pro=19 1a=False 1b=True 2=False (64.1s)
Sep 13 07:29:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:29:25,275 main INFO screen SNZ pass=1 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (66.0s)
Sep 13 07:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:29:36,826 main INFO screen CUKE pass=0 dev=0.18 ins=77.58 pro=7 1a=False 1b=True 2=True (66.6s)
Sep 13 07:30:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:30:30,198 main INFO screen CrackyCat pass=0 dev=1.25 ins=0.0 pro=8 1a=False 1b=False 2=False (82.6s)
Sep 13 07:31:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:31:35,424 main INFO screen MONCAT pass=0 dev=35.72 ins=0.0 pro=4 1a=False 1b=False 2=True (72.3s)
Sep 13 07:31:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:31:37,148 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:31:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:31:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:31:56,620 main INFO screen Sp pass=0 dev=3.09 ins=0.0 pro=4 1a=False 1b=False 2=False (75.5s)
Sep 13 07:32:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:32:27,269 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.4s)
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:34:52,564 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:34:52,660 aiohttp.access INFO 204.76.203.49 [13/Sep/2026:07:34:52 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 13 07:34:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:34:52,660 aiohttp.access INFO 204.76.203.49 [13/Sep/2026:07:34:52 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 13 07:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:35:40,048 main INFO screen stonk pass=1 dev=0.0 ins=0.02 pro=30 1a=False 1b=False 2=False (101.9s)
Sep 13 07:35:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:35:52,939 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.2s)
Sep 13 07:36:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:36:34,313 main INFO screen TANUKI pass=0 dev=0.0 ins=14.49 pro=41 1a=False 1b=False 2=True (62.8s)
Sep 13 07:36:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:36:45,121 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:36:45 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: a7e508db89c149a5bfe6a64d43f3bf81
analyses gestart (53ca44e52d90)
--- update 2026-09-13T06:39:07Z
--- update 2026-09-13T06:44:11Z
--- update 2026-09-13T06:49:36Z
--- update 2026-09-13T06:54:52Z
--- update 2026-09-13T07:00:35Z
--- update 2026-09-13T07:05:36Z
--- update 2026-09-13T07:10:38Z
--- update 2026-09-13T07:16:10Z
--- update 2026-09-13T07:21:10Z
nieuwe code: 8a627ef
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: f9a58f01752147e09bc4fdf885328ad1
analyses gestart (a296e5df3860)
--- update 2026-09-13T07:26:25Z
--- update 2026-09-13T07:31:36Z
--- update 2026-09-13T07:36:44Z
```

## Analyses (laatste 25 regels)
```
active
06:46:56 194340 wallets gerekend
06:46:57 geluk-toets
06:47:32 persistentie
06:47:34 kopieer-simulatie
06:47:56 klaar in 121s -> /opt/schaduwbot/reports/wallets.md
07:21:12 48943 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
07:21:13   ingelezen tot rowid 5609875 (44022 rijen, 44022 bruikbaar)
07:21:14 ingelezen: 44022 nieuwe trades, 44022 bruikbaar (3s)
07:22:00 943 aankopen van gevolgde wallets geëvalueerd
07:22:12 vroege kopers: 166 voldoen nu, register 261, 0 tokens beoordeeld
07:22:24 grote spelers: saldo van 22 wallets opgehaald
07:23:43 herkomst: 40 posities gekoppeld
07:23:47 klaar in 156s -> /opt/schaduwbot/reports/ledger.md
07:24:39 S1: gezakt — toets n=4558, verkennend n=14656
07:24:39 klaar in 52s -> /opt/schaduwbot/reports/hypotheses.md
07:24:40 na-migratie: 400 paren te checken
07:30:21 na-migratie: 118 paren, 43 prijzen
07:30:25 probe: 400 transacties ophalen
07:36:16 klaar (882 rpc-calls, 656 fouten)
07:36:20   2000 nieuwe tokens doorgerekend
07:36:23   4000 nieuwe tokens doorgerekend
07:36:27   6000 nieuwe tokens doorgerekend
07:36:32   8000 nieuwe tokens doorgerekend
07:36:38   10000 nieuwe tokens doorgerekend
07:36:42   12000 nieuwe tokens doorgerekend
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
