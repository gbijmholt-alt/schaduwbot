# Schaduwbot status

- tijd: 2026-09-13 05:20:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 15 hours, 33 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.2G/38G | geheugen: 1405/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 31625, "tokens_in_memory": 6302, "msgs": 3238649, "trades": 940743, "creates": 10255, "decode_fail": 100658, "rpc_calls": 25508, "rpc_errors": 6, "sol_usd": 101.80858233123199, "open_positions": 35, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 4691 | 531 | 8 | 541 | 90 | 967 | 2918 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 614 | 17% | 1.6% | +43.2% | -15.8% | -5.93% | 100% |
| dip35_V1_gescreend_fail | 4719 | 27% | 3.9% | +45.1% | -25.9% | -6.74% | 100% |
| dip35_V1_alle | 6403 | 26% | 3.9% | +44.4% | -25.4% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 612 | 23% | 2.3% | +40.8% | -20.1% | -6.29% | 100% |
| dip35_V2_gescreend_fail | 4798 | 25% | 4.4% | +54.7% | -27.9% | -7.01% | 100% |
| dip35_V2_alle | 6360 | 25% | 4.5% | +52.0% | -27.7% | -7.98% | 100% |
| dip35_V3_gescreend_pass | 620 | 9% | 3.2% | +257.9% | -22.0% | +3.76% | 100% |
| dip35_V3_gescreend_fail | 4931 | 14% | 6.1% | +119.4% | -29.6% | -9.24% | 100% |
| dip35_V3_alle | 6418 | 13% | 6.1% | +117.0% | -29.4% | -10.25% | 100% |
| dip40_V1_gescreend_pass | 585 | 15% | 1.7% | +43.7% | -15.4% | -6.63% | 100% |
| dip40_V1_gescreend_fail | 4646 | 26% | 3.9% | +46.7% | -25.7% | -6.62% | 100% |
| dip40_V1_alle | 6159 | 26% | 3.9% | +46.4% | -25.3% | -6.96% | 100% |
| dip40_V2_gescreend_pass | 585 | 18% | 2.1% | +43.2% | -19.4% | -7.94% | 100% |
| dip40_V2_gescreend_fail | 4700 | 25% | 4.3% | +54.7% | -27.8% | -6.97% | 100% |
| dip40_V2_alle | 6109 | 24% | 4.4% | +53.1% | -27.6% | -8.01% | 100% |
| dip40_V3_gescreend_pass | 593 | 8% | 2.9% | +256.5% | -21.0% | +1.94% | 100% |
| dip40_V3_gescreend_fail | 4816 | 13% | 5.8% | +115.4% | -29.3% | -10.03% | 100% |
| dip40_V3_alle | 6168 | 13% | 5.8% | +113.6% | -29.1% | -10.98% | 100% |
| dip45_V1_gescreend_pass | 564 | 15% | 1.6% | +46.7% | -15.2% | -5.84% | 100% |
| dip45_V1_gescreend_fail | 4562 | 27% | 3.6% | +48.1% | -25.5% | -5.50% | 100% |
| dip45_V1_alle | 5952 | 26% | 3.6% | +48.2% | -25.0% | -6.02% | 100% |
| dip45_V2_gescreend_pass | 563 | 19% | 2.0% | +42.6% | -19.4% | -7.85% | 100% |
| dip45_V2_gescreend_fail | 4608 | 25% | 4.0% | +58.3% | -27.5% | -5.81% | 100% |
| dip45_V2_alle | 5904 | 24% | 4.1% | +56.7% | -27.3% | -6.89% | 100% |
| dip45_V3_gescreend_pass | 572 | 8% | 2.4% | +282.3% | -20.4% | +3.97% | 100% |
| dip45_V3_gescreend_fail | 4710 | 14% | 5.4% | +121.8% | -28.9% | -7.72% | 100% |
| dip45_V3_alle | 5954 | 13% | 5.5% | +122.3% | -28.6% | -8.90% | 100% |

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
| per_token_met_xlink | 485 | 16% | 5.4% | -8.13% | -11.2% tot -5.0% | -14.3% | – | 100% |
| per_token_zonder_xlink | 152 | 23% | 0.0% | +18.92% | -8.5% tot +46.4% | -13.1% | 118% | 58% |
| gepoold_met_xlink | 4040 | 14% | 2.9% | -9.32% | -10.6% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1268 | 18% | 0.0% | +15.52% | +0.1% tot +31.0% | -14.3% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 04:39:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:39:57,423 main INFO screen baton pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (53.1s)
Sep 13 04:40:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:40:11,481 main INFO screen CHAROC pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (64.2s)
Sep 13 04:40:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:40:21,034 main INFO screen HolyChett pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.5s)
Sep 13 04:41:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:41:09,354 main INFO screen $harley pass=0 dev=1.95 ins=0.0 pro=3 1a=False 1b=False 2=False (50.2s)
Sep 13 04:41:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:41:38,495 main INFO screen PTRK pass=0 dev=3.42 ins=0.0 pro=1 1a=False 1b=False 2=False (50.8s)
Sep 13 04:43:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:43:15,503 main INFO screen STL pass=0 dev=63.74 ins=0.0 pro=4 1a=False 1b=False 2=True (62.1s)
Sep 13 04:43:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:43:20,971 main INFO screen CROCGPT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 13 04:43:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:43:30,502 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.9s)
Sep 13 04:44:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:44:08,053 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:44:08 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 04:44:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:44:17,465 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.9s)
Sep 13 04:46:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:46:16,582 main INFO screen OTTERGPT pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (73.2s)
Sep 13 04:47:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:47:33,343 main INFO screen sol pass=0 dev=0.29 ins=0.0 pro=2 1a=False 1b=False 2=False (71.1s)
Sep 13 04:47:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:47:34,335 main INFO screen WTF pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (78.6s)
Sep 13 04:47:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:47:37,510 main INFO screen WIF2 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.2s)
Sep 13 04:48:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:48:45,139 main INFO screen stonksman pass=0 dev=0.18 ins=77.58 pro=8 1a=False 1b=True 2=True (70.8s)
Sep 13 04:48:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:48:46,985 main INFO screen fg pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (73.6s)
Sep 13 04:49:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:49:22,125 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:49:22 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:49:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:49:30,990 main INFO screen WTF pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (75.9s)
Sep 13 04:49:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:49:51,624 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 13 04:50:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:50:25,383 main INFO screen HolyChett pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (74.6s)
Sep 13 04:50:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:50:35,436 main INFO screen WTF pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.4s)
Sep 13 04:50:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:50:40,948 main INFO screen DoCa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.3s)
Sep 13 04:51:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:51:26,607 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.4s)
Sep 13 04:52:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:52:13,770 main INFO screen CATHOUSE pass=0 dev=0.88 ins=0.0 pro=4 1a=False 1b=False 2=False (60.6s)
Sep 13 04:52:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:52:46,357 main INFO screen WTF pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 13 04:53:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:53:45,848 main INFO screen foff pass=0 dev=0.12 ins=0.0 pro=3 1a=False 1b=False 2=False (56.2s)
Sep 13 04:53:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:53:57,905 aiohttp.access INFO 18.215.152.242 [13/Sep/2026:04:53:57 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
Sep 13 04:54:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:54:06,996 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.3s)
Sep 13 04:54:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:54:27,207 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:54:27 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:55:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:55:56,154 main INFO screen scat pass=0 dev=0.25 ins=0.04 pro=1 1a=False 1b=False 2=False (67.5s)
Sep 13 04:56:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:56:05,257 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 13 04:56:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:56:49,424 main INFO screen TESSERACT pass=1 dev=0.0 ins=1.87 pro=31 1a=False 1b=False 2=False (73.4s)
Sep 13 04:57:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:57:26,465 main INFO screen dung pass=0 dev=0.0 ins=51.09 pro=24 1a=False 1b=False 2=True (76.1s)
Sep 13 04:57:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:57:31,108 main INFO screen 6AM pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.6s)
Sep 13 04:58:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:58:01,647 main INFO screen FLAPPY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.2s)
Sep 13 04:59:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:59:22,515 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (67.2s)
Sep 13 04:59:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:59:31,939 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.8s)
Sep 13 04:59:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:59:37,022 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:59:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 05:00:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:00:17,599 main INFO screen TINA pass=0 dev=0.0 ins=31.11 pro=29 1a=False 1b=False 2=True (71.2s)
Sep 13 05:00:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:00:21,195 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.7s)
Sep 13 05:01:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:01:22,859 main INFO screen TESSERACT pass=0 dev=26.6 ins=0.0 pro=42 1a=False 1b=False 2=False (70.0s)
Sep 13 05:01:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:01:28,918 main INFO screen Medusa pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (66.4s)
Sep 13 05:02:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:02:00,730 main INFO screen foff pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.0s)
Sep 13 05:02:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:02:29,348 main INFO screen ZBUNNY pass=0 dev=0.07 ins=79.24 pro=7 1a=False 1b=True 2=True (55.6s)
Sep 13 05:03:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:03:07,016 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.8s)
Sep 13 05:03:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:03:38,484 main INFO screen TESSERACT pass=0 dev=35.47 ins=0.0 pro=34 1a=False 1b=False 2=False (69.4s)
Sep 13 05:03:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:03:44,511 main INFO screen CHILLCENTER pass=0 dev=0.0 ins=27.96 pro=40 1a=False 1b=False 2=True (55.1s)
Sep 13 05:04:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:04:16,498 main INFO screen Tradition pass=0 dev=0.0 ins=36.94 pro=66 1a=False 1b=False 2=True (68.1s)
Sep 13 05:04:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:04:42,622 main INFO screen KEYCAT pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (56.2s)
Sep 13 05:05:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:05:02,929 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:05:02 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 13 05:05:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:05:13,312 main INFO screen FLAPPY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 13 05:05:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:05:29,674 main INFO screen cap pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 13 05:06:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:06:30,338 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 13 05:07:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:07:40,725 main INFO screen PORNHUB pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (49.4s)
Sep 13 05:08:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:08:12,363 main INFO screen foff pass=0 dev=0.16 ins=0.0 pro=4 1a=False 1b=False 2=False (75.3s)
Sep 13 05:08:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:08:12,526 main INFO screen $OCT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.2s)
Sep 13 05:08:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:08:35,973 main INFO screen Tesla pass=0 dev=52.71 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
Sep 13 05:09:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:09:24,091 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=29 1a=False 1b=False 2=False (71.7s)
Sep 13 05:09:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:09:44,507 main INFO screen PUMPHero pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (61.2s)
Sep 13 05:09:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:09:56,639 main INFO screen ZCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.6s)
Sep 13 05:10:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:10:37,149 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:10:37 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 13 05:10:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:10:39,007 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.9s)
Sep 13 05:10:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:10:41,554 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.0s)
Sep 13 05:11:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:11:10,957 main INFO screen DISBELIEF pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (74.3s)
Sep 13 05:11:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:11:49,355 main INFO screen jubjub pass=1 dev=0.0 ins=1.74 pro=51 1a=False 1b=False 2=False (70.3s)
Sep 13 05:11:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:11:50,517 main INFO screen MACROCAT pass=0 dev=0.0 ins=21.23 pro=35 1a=False 1b=False 2=True (69.0s)
Sep 13 05:12:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:12:27,291 main INFO screen KINURA pass=0 dev=0.0 ins=31.11 pro=9 1a=False 1b=False 2=True (76.3s)
Sep 13 05:13:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:13:15,389 main INFO screen ZDOG pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (86.0s)
Sep 13 05:13:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:13:16,008 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.71 pro=50 1a=False 1b=False 2=False (85.5s)
Sep 13 05:14:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:14:23,328 main INFO screen KYCS pass=1 dev=1.72 ins=0.0 pro=20 1a=False 1b=False 2=False (61.7s)
Sep 13 05:14:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:14:44,398 main INFO screen anorchia pass=0 dev=0.0 ins=15.56 pro=46 1a=False 1b=False 2=True (67.8s)
Sep 13 05:15:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:15:03,261 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.32 pro=23 1a=False 1b=False 2=False (73.3s)
Sep 13 05:15:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:15:32,070 main INFO screen Crook pass=0 dev=0.0 ins=2.83 pro=54 1a=False 1b=True 2=True (65.5s)
Sep 13 05:15:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:15:42,928 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:15:42 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 13 05:16:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:16:21,988 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.16 pro=23 1a=False 1b=False 2=False (76.6s)
Sep 13 05:17:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:17:50,973 main INFO screen TESSERACT pass=0 dev=35.47 ins=0.0 pro=43 1a=False 1b=False 2=False (71.4s)
Sep 13 05:18:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:18:21,525 main INFO screen Zbaton pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (56.8s)
Sep 13 05:18:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:18:38,500 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.7s)
Sep 13 05:20:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:20:24,355 main INFO screen foff pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.9s)
Sep 13 05:20:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:20:53,562 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:20:53 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T03:41:36Z
--- update 2026-09-13T03:47:19Z
--- update 2026-09-13T03:52:26Z
--- update 2026-09-13T03:57:36Z
--- update 2026-09-13T04:03:06Z
--- update 2026-09-13T04:08:13Z
--- update 2026-09-13T04:13:32Z
--- update 2026-09-13T04:18:34Z
--- update 2026-09-13T04:23:34Z
--- update 2026-09-13T04:28:36Z
--- update 2026-09-13T04:33:47Z
--- update 2026-09-13T04:38:57Z
--- update 2026-09-13T04:44:07Z
--- update 2026-09-13T04:49:21Z
--- update 2026-09-13T04:54:26Z
--- update 2026-09-13T04:59:36Z
--- update 2026-09-13T05:05:01Z
--- update 2026-09-13T05:10:36Z
--- update 2026-09-13T05:15:41Z
--- update 2026-09-13T05:20:52Z
```

## Analyses (laatste 25 regels)
```
inactive
03:46:34   10000 tokens, 1119139 trades, 186212 posities (9s)
03:46:36   12000 tokens, 1334024 trades, 220569 posities (12s)
03:46:38   14000 tokens, 1552125 trades, 254897 posities (14s)
03:46:41   16000 tokens, 1798887 trades, 299037 posities (17s)
03:46:45   18000 tokens, 2044898 trades, 345751 posities (21s)
03:46:48   20000 tokens, 2269436 trades, 381126 posities (24s)
03:46:51   22000 tokens, 2474809 trades, 412711 posities (27s)
03:46:55   24000 tokens, 2716778 trades, 453809 posities (30s)
03:46:59   26000 tokens, 2933582 trades, 489092 posities (34s)
03:47:03   28000 tokens, 3146779 trades, 522947 posities (38s)
03:47:08   30000 tokens, 3397653 trades, 570494 posities (44s)
03:47:13   32000 tokens, 3622591 trades, 605594 posities (49s)
03:47:18   34000 tokens, 3841397 trades, 639128 posities (53s)
03:47:24   36000 tokens, 4070267 trades, 678218 posities (59s)
03:47:29   38000 tokens, 4285222 trades, 715485 posities (65s)
03:47:34   40000 tokens, 4503457 trades, 753083 posities (70s)
03:47:40   42000 tokens, 4744163 trades, 796233 posities (76s)
03:47:46   44000 tokens, 4977416 trades, 836360 posities (82s)
03:47:52   46000 tokens, 5213776 trades, 889236 posities (88s)
03:47:55 posities: 909801 uit 5314228 trades (91s)
03:48:07 190892 wallets gerekend
03:48:07 geluk-toets
03:48:38 persistentie
03:48:41 kopieer-simulatie
03:49:41 klaar in 197s -> /opt/schaduwbot/reports/wallets.md
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
