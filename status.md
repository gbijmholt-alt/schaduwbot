# Schaduwbot status

- tijd: 2026-09-14 05:14:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 15 hours, 27 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 1916/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 81629, "tokens_in_memory": 6489, "msgs": 10986884, "trades": 2282582, "creates": 23948, "decode_fail": 198418, "rpc_calls": 66749, "rpc_errors": 3, "sol_usd": 101.15280740912006, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 04:35:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:35:10,282 main INFO screen KOVRA pass=0 dev=13.0 ins=24.34 pro=29 1a=False 1b=True 2=False (99.9s)
Sep 14 04:35:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:35:43,955 main INFO screen Johnny  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (98.7s)
Sep 14 04:36:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:11,745 main INFO screen 🌙 pass=0 dev=0.07 ins=0.0 pro=7 1a=False 1b=False 2=False (68.8s)
Sep 14 04:36:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:56,085 main INFO screen GOAT pass=0 dev=4.32 ins=0.0 pro=4 1a=False 1b=False 2=False (69.2s)
Sep 14 04:36:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:58,701 main INFO screen 奶龙 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.8s)
Sep 14 04:37:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:37:51,256 main INFO screen ACTII pass=0 dev=0.0 ins=12.05 pro=67 1a=False 1b=False 2=True (62.0s)
Sep 14 04:38:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:38:35,917 main INFO screen $MD pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (68.2s)
Sep 14 04:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:38:37,073 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:38:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:39:07,132 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.4s)
Sep 14 04:39:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:39:48,406 main INFO screen PUMP pass=1 dev=0.0 ins=10.51 pro=40 1a=False 1b=False 2=False (63.1s)
Sep 14 04:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:06,003 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 14 04:40:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:21,014 main INFO screen FROGLABS pass=0 dev=8.76 ins=25.57 pro=16 1a=False 1b=False 2=False (53.4s)
Sep 14 04:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:39,277 main INFO screen USDF pass=0 dev=77.77 ins=1.54 pro=1 1a=False 1b=False 2=True (50.9s)
Sep 14 04:41:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:03,100 main INFO screen JWD pass=1 dev=1.74 ins=0.0 pro=45 1a=False 1b=False 2=False (57.1s)
Sep 14 04:41:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:27,294 main INFO screen pump pass=1 dev=0.21 ins=0.0 pro=10 1a=False 1b=False 2=False (66.3s)
Sep 14 04:41:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:31,289 main INFO screen plum pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (52.0s)
Sep 14 04:41:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:55,739 main INFO screen GPTjak pass=0 dev=0.18 ins=77.76 pro=10 1a=False 1b=True 2=True (52.6s)
Sep 14 04:42:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:42:28,495 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 14 04:42:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:42:29,917 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.6s)
Sep 14 04:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:11,659 main INFO screen Human pass=0 dev=0.0 ins=6.56 pro=52 1a=False 1b=False 2=True (65.4s)
Sep 14 04:43:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:32,498 main INFO screen human pass=0 dev=0.0 ins=25.64 pro=65 1a=False 1b=False 2=True (64.0s)
Sep 14 04:43:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:39,488 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:43:39 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:43:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:48,340 main INFO screen JAKE pass=1 dev=0.04 ins=0.0 pro=13 1a=False 1b=False 2=False (66.6s)
Sep 14 04:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:44:19,145 main INFO screen Is pass=0 dev=0.0 ins=27.32 pro=59 1a=False 1b=False 2=True (67.5s)
Sep 14 04:45:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:45:38,040 main INFO screen TEIZA pass=0 dev=10.0 ins=28.42 pro=18 1a=False 1b=True 2=False (53.2s)
Sep 14 04:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:15,353 main INFO screen Humanity pass=1 dev=0.0 ins=4.23 pro=59 1a=False 1b=False 2=False (79.4s)
Sep 14 04:46:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:16,445 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=5 1a=False 1b=False 2=False (77.4s)
Sep 14 04:46:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:58,743 main INFO screen Humanity pass=0 dev=0.0 ins=11.81 pro=50 1a=False 1b=False 2=True (80.7s)
Sep 14 04:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:47:10,416 main INFO screen BikeTyson pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.1s)
Sep 14 04:47:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:47:35,230 main INFO screen Sloth pass=1 dev=0.0 ins=9.26 pro=56 1a=False 1b=False 2=False (72.4s)
Sep 14 04:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:48:31,018 main INFO screen SpaceX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 14 04:48:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:48:50,515 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:48:50 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:49:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:49:01,443 main INFO screen ZAP pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 14 04:49:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:49:45,876 main INFO screen ocs pass=0 dev=9.38 ins=24.34 pro=21 1a=False 1b=False 2=False (48.4s)
Sep 14 04:50:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:50:45,394 main INFO screen Jerry pass=1 dev=0.0 ins=19.41 pro=44 1a=False 1b=False 2=False (53.0s)
Sep 14 04:51:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:33,396 main INFO screen mictyson pass=0 dev=1.74 ins=77.57 pro=2 1a=False 1b=False 2=True (68.4s)
Sep 14 04:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:35,283 main INFO screen USDF pass=0 dev=71.24 ins=0.0 pro=10 1a=False 1b=False 2=True (70.9s)
Sep 14 04:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:56,440 main INFO screen FOMO pass=0 dev=0.0 ins=15.35 pro=62 1a=False 1b=False 2=True (71.0s)
Sep 14 04:52:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:52:42,389 main INFO screen Rotator pass=0 dev=0.0 ins=38.08 pro=76 1a=False 1b=False 2=True (69.0s)
Sep 14 04:52:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:52:43,681 main INFO screen INBRED pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (68.4s)
Sep 14 04:53:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:01,339 main INFO screen FakeTaxi pass=1 dev=0.0 ins=0.24 pro=32 1a=False 1b=False 2=False (64.9s)
Sep 14 04:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:54,808 main INFO screen Fork pass=0 dev=0.0 ins=42.27 pro=67 1a=False 1b=False 2=True (71.1s)
Sep 14 04:53:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:56,137 main INFO screen HI pass=0 dev=0.0 ins=34.37 pro=70 1a=False 1b=False 2=True (73.7s)
Sep 14 04:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:54:00,493 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:54:00 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:54:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:54:05,584 main INFO screen FakeTaxi pass=0 dev=55.95 ins=0.0 pro=59 1a=False 1b=True 2=False (64.2s)
Sep 14 04:55:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:55:33,651 main INFO screen SHELL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.9s)
Sep 14 04:57:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:57:48,001 main INFO screen Human pass=0 dev=0.0 ins=25.9 pro=68 1a=False 1b=False 2=True (61.7s)
Sep 14 04:58:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:05,146 main INFO screen Basilisk pass=0 dev=0.0 ins=29.82 pro=74 1a=False 1b=False 2=True (59.5s)
Sep 14 04:58:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:22,753 main INFO screen SubSneak pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (67.7s)
Sep 14 04:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:54,230 main INFO screen Luddites pass=1 dev=0.0 ins=4.79 pro=38 1a=False 1b=False 2=False (66.2s)
Sep 14 04:58:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:57,215 main INFO screen NINA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.1s)
Sep 14 04:59:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:59:10,783 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:59:10 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:59:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:59:56,967 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 14 05:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:00:45,636 main INFO screen SHROOMS pass=0 dev=0.7 ins=55.34 pro=11 1a=False 1b=True 2=True (55.6s)
Sep 14 05:00:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:00:57,091 main INFO screen trumpndmp pass=0 dev=8.06 ins=0.0 pro=11 1a=False 1b=False 2=False (64.7s)
Sep 14 05:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:01:01,724 main INFO screen LMAO pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (64.3s)
Sep 14 05:01:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:01:58,562 main INFO screen BPCATE pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (72.9s)
Sep 14 05:02:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:02:03,352 main INFO screen PONSLv pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=False 2=True (66.3s)
Sep 14 05:02:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:02:32,689 main INFO screen REVPEPE pass=0 dev=0.07 ins=0.0 pro=4 1a=False 1b=False 2=False (68.9s)
Sep 14 05:03:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:03:17,470 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.1s)
Sep 14 05:03:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:03:38,352 main INFO screen HYPILL pass=0 dev=0.0 ins=21.35 pro=65 1a=False 1b=False 2=True (61.1s)
Sep 14 05:04:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:04:32,553 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:04:32 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:04:38,913 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=5 1a=False 1b=False 2=False (68.3s)
Sep 14 05:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:05:22,443 main INFO screen TWICE pass=0 dev=5.01 ins=0.0 pro=54 1a=False 1b=False 2=False (66.8s)
Sep 14 05:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:07:04,675 main INFO screen Sloth pass=0 dev=0.0 ins=14.64 pro=64 1a=False 1b=False 2=True (63.3s)
Sep 14 05:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:07:19,910 main INFO screen AI pass=0 dev=0.0 ins=9.55 pro=34 1a=False 1b=False 2=True (67.8s)
Sep 14 05:08:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:08:25,848 main INFO screen PETIX pass=0 dev=10.0 ins=23.63 pro=18 1a=False 1b=False 2=False (73.7s)
Sep 14 05:09:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:24,134 main INFO screen NFA pass=0 dev=0.0 ins=36.86 pro=65 1a=False 1b=False 2=True (76.1s)
Sep 14 05:09:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:26,959 main INFO screen $AURA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (79.0s)
Sep 14 05:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:36,564 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:09:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:09:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:37,411 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (70.9s)
Sep 14 05:10:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:24,183 main INFO screen BLAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (60.0s)
Sep 14 05:10:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:51,316 main INFO screen MTC pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (84.4s)
Sep 14 05:10:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:59,854 main INFO screen GS pass=0 dev=0.0 ins=27.71 pro=73 1a=False 1b=False 2=True (82.4s)
Sep 14 05:11:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:11:29,673 main INFO screen FYPM pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 14 05:12:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:12:39,634 main INFO screen ANTIAI pass=0 dev=0.0 ins=28.72 pro=29 1a=False 1b=False 2=False (75.3s)
Sep 14 05:13:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:13:51,175 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (56.5s)
Sep 14 05:14:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:01,197 main INFO screen Rabbitson pass=0 dev=0.7 ins=55.23 pro=14 1a=False 1b=True 2=True (55.6s)
Sep 14 05:14:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:11,041 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 14 05:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:37,044 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:14:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T03:46:36Z
--- update 2026-09-14T03:51:35Z
--- update 2026-09-14T03:56:38Z
--- update 2026-09-14T04:02:07Z
--- update 2026-09-14T04:07:29Z
--- update 2026-09-14T04:12:34Z
--- update 2026-09-14T04:17:36Z
--- update 2026-09-14T04:22:44Z
--- update 2026-09-14T04:28:04Z
--- update 2026-09-14T04:33:32Z
--- update 2026-09-14T04:38:36Z
--- update 2026-09-14T04:43:38Z
--- update 2026-09-14T04:48:49Z
--- update 2026-09-14T04:53:59Z
Running as unit: schaduwbot-wallets.service; invocation ID: f736891630a542c892110e5793ff0a8a
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T04:59:09Z
--- update 2026-09-14T05:04:31Z
--- update 2026-09-14T05:09:35Z
--- update 2026-09-14T05:14:36Z
```

## Analyses (laatste 25 regels)
```
active
03:25:07   64000 tokens, 6430429 trades, 840854 posities (374s)
03:25:18   66000 tokens, 6647572 trades, 880931 posities (385s)
03:25:28   68000 tokens, 6828531 trades, 905157 posities (394s)
03:25:28 posities: 907715 uit 6836758 trades (398s)
03:25:40 194054 wallets gerekend
03:25:40 geluk-toets
03:26:14 persistentie
03:26:17 kopieer-simulatie
03:28:13 klaar in 563s -> /opt/schaduwbot/reports/wallets.md
04:54:04 72107 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
04:54:23   ingelezen tot rowid 7820118 (192283 rijen, 192283 bruikbaar)
04:54:24 ingelezen: 192283 nieuwe trades, 192283 bruikbaar (25s)
04:56:21 3000 aankopen van gevolgde wallets geëvalueerd
04:56:43 vroege kopers: 220 voldoen nu, register 381, 305 tokens beoordeeld
04:57:05 grote spelers: saldo van 345 wallets opgehaald
04:57:44 herkomst: 40 posities gekoppeld
04:57:52 klaar in 232s -> /opt/schaduwbot/reports/ledger.md
05:05:28 S1: gezakt — toets n=15473, verkennend n=14656
05:05:28 klaar in 456s -> /opt/schaduwbot/reports/hypotheses.md
05:05:29 probe: 150 transacties ophalen
05:08:59 poolveld: 21 pools bekeken, 0 te gaan -> vastgesteld @43
05:10:13 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
05:10:13 prijsijk: n=104 -> mediane afwijking 100% boven 25%
05:10:14 na-migratie: 100 paren te checken
05:12:33 na-migratie: 78 paren, 20 prijzen
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
