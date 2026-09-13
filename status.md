# Schaduwbot status

- tijd: 2026-09-13 04:54:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 15 hours, 7 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.2G/38G | geheugen: 1408/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 30039, "tokens_in_memory": 6474, "msgs": 3123675, "trades": 901375, "creates": 9885, "decode_fail": 94625, "rpc_calls": 24348, "rpc_errors": 6, "sol_usd": 101.67514395666062, "open_positions": 36, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 04:13:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:13:47,727 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (61.7s)
Sep 13 04:14:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:14:22,226 main INFO screen Solly pass=0 dev=0.0 ins=25.55 pro=41 1a=False 1b=False 2=True (71.3s)
Sep 13 04:15:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:15:30,509 main INFO screen samo pass=1 dev=3.43 ins=0.0 pro=54 1a=False 1b=False 2=False (68.9s)
Sep 13 04:15:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:15:39,306 main INFO screen SOL❤️ pass=0 dev=0.08 ins=0.0 pro=9 1a=False 1b=False 2=False (65.5s)
Sep 13 04:16:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:16:14,759 main INFO screen Flytown pass=0 dev=6.13 ins=0.8 pro=19 1a=False 1b=True 2=False (65.3s)
Sep 13 04:16:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:16:45,461 main INFO screen 5:10 pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (75.0s)
Sep 13 04:16:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:16:46,594 main INFO screen PAPERBAG pass=1 dev=0.0 ins=15.04 pro=29 1a=False 1b=False 2=False (67.3s)
Sep 13 04:17:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:17:25,397 main INFO screen Peccy pass=0 dev=0.0 ins=20.85 pro=41 1a=False 1b=False 2=True (70.6s)
Sep 13 04:17:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:17:59,685 main INFO screen COMGPT pass=0 dev=0.17 ins=79.13 pro=7 1a=False 1b=False 2=True (73.1s)
Sep 13 04:18:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:18:01,272 main INFO screen FML pass=1 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (75.8s)
Sep 13 04:18:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:18:28,540 main INFO screen addy pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.1s)
Sep 13 04:18:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:18:35,227 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:18:35 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 04:19:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:19:10,229 main INFO screen LORE pass=1 dev=3.43 ins=0.0 pro=54 1a=False 1b=False 2=False (69.0s)
Sep 13 04:19:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:19:13,156 main INFO screen foff pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.5s)
Sep 13 04:19:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:19:29,136 main INFO screen DOGGPT pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (59.3s)
Sep 13 04:20:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:20:04,010 main INFO screen GPT-67 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.8s)
Sep 13 04:20:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:20:25,698 main INFO screen consolidating pass=1 dev=0.0 ins=1.77 pro=60 1a=False 1b=False 2=False (64.6s)
Sep 13 04:21:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:21:31,125 main INFO screen Marvin pass=0 dev=0.0 ins=70.26 pro=1 1a=False 1b=False 2=True (50.6s)
Sep 13 04:22:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:22:49,030 main INFO screen APU pass=0 dev=0.0 ins=35.03 pro=50 1a=False 1b=False 2=True (62.5s)
Sep 13 04:22:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:22:53,564 rpc WARNING rpc getTokenLargestAccounts exc Server disconnected
Sep 13 04:23:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:23:35,927 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:23:35 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:23:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:23:46,666 main INFO screen fomo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 13 04:24:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:24:05,898 main INFO screen INDIAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 13 04:24:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:24:24,011 main INFO screen BMW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.0s)
Sep 13 04:25:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:25:21,840 main INFO screen Flytown pass=0 dev=0.0 ins=28.25 pro=52 1a=False 1b=False 2=True (78.2s)
Sep 13 04:26:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:26:23,288 main INFO screen FLYTOWN pass=0 dev=5.22 ins=10.74 pro=39 1a=False 1b=False 2=False (72.4s)
Sep 13 04:27:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:27:07,547 main INFO screen FML pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 13 04:27:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:27:48,962 main INFO screen PYKLIS pass=0 dev=0.0 ins=31.65 pro=32 1a=False 1b=True 2=True (57.7s)
Sep 13 04:28:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:28:24,863 main INFO screen AI pass=0 dev=0.0 ins=12.74 pro=33 1a=False 1b=False 2=True (55.6s)
Sep 13 04:28:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:28:37,188 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:28:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:28:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:28:52,361 main INFO screen FML pass=0 dev=0.01 ins=0.0 pro=8 1a=False 1b=False 2=False (64.0s)
Sep 13 04:30:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:30:30,997 main INFO screen Flytown pass=1 dev=0.0 ins=12.3 pro=38 1a=False 1b=False 2=False (60.7s)
Sep 13 04:31:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:31:31,649 main INFO screen ANONBATON pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (58.8s)
Sep 13 04:32:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:32:14,810 main INFO screen NASA pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (70.9s)
Sep 13 04:32:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:32:20,170 main INFO screen CATGPT pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (71.7s)
Sep 13 04:33:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:33:12,429 main INFO screen Cabal pass=0 dev=0.0 ins=33.74 pro=32 1a=True 1b=False 2=True (51.6s)
Sep 13 04:33:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:33:48,504 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:33:48 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:34:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:34:59,827 main INFO screen HolyChett pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (94.1s)
Sep 13 04:35:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:35:24,258 main INFO screen TRUMPETS pass=1 dev=1.05 ins=0.0 pro=15 1a=False 1b=False 2=False (112.9s)
Sep 13 04:35:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:35:37,715 main INFO screen Pufcat pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (58.2s)
Sep 13 04:35:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:35:57,399 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 13 04:36:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:36:35,584 main INFO screen HIJKLMN pass=1 dev=0.0 ins=14.9 pro=36 1a=False 1b=False 2=False (66.6s)
Sep 13 04:36:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:36:55,683 main INFO screen DeepSeek pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 13 04:37:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:37:18,149 main INFO screen SC07 pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (73.4s)
Sep 13 04:37:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:37:38,561 main INFO screen FML pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.1s)
Sep 13 04:37:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:37:55,273 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.6s)
Sep 13 04:38:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:38:23,132 main INFO screen SAMO pass=1 dev=0.0 ins=16.45 pro=72 1a=False 1b=False 2=False (65.0s)
Sep 13 04:38:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:38:30,744 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 13 04:38:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:38:59,147 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:04:38:59 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 04:39:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:39:03,374 main INFO screen $GOAT pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (68.1s)
Sep 13 04:39:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 04:39:10,721 main INFO screen FML pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (47.6s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T03:25:36Z
--- update 2026-09-13T03:30:35Z
--- update 2026-09-13T03:36:11Z
Running as unit: schaduwbot-wallets.service; invocation ID: 19b30d28839c4560ad0bcf4c5e040823
analyses gestart (f08e7b8a0e22)
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
