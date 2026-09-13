# Schaduwbot status

- tijd: 2026-09-13 21:36:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 7 hours, 49 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.0G/38G | geheugen: 1826/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 54148, "tokens_in_memory": 7932, "msgs": 6320007, "trades": 1425703, "creates": 15357, "decode_fail": 134211, "rpc_calls": 41750, "rpc_errors": 2, "sol_usd": 101.48655917512582, "open_positions": 77, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 21:14:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:14:45,488 main INFO screen ALI pass=0 dev=3.75 ins=0.0 pro=7 1a=False 1b=False 2=False (74.9s)
Sep 13 21:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:37,888 main INFO screen att pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (75.0s)
Sep 13 21:15:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:39,123 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:15:39 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:15:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:44,735 main INFO screen Motion pass=0 dev=0.15 ins=36.49 pro=64 1a=False 1b=False 2=True (68.0s)
Sep 13 21:15:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:56,378 main INFO screen SOL pass=0 dev=0.0 ins=36.86 pro=79 1a=False 1b=False 2=True (63.9s)
Sep 13 21:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:31,893 main INFO screen Longdog pass=1 dev=0.0 ins=8.29 pro=24 1a=False 1b=False 2=False (54.0s)
Sep 13 21:16:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:45,878 aiohttp.access INFO 195.182.16.23 [13/Sep/2026:21:16:45 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 13 21:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:54,335 aiohttp.access INFO 34.222.185.251 [13/Sep/2026:21:16:54 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
Sep 13 21:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:54,346 main INFO screen TWINS pass=0 dev=0.0 ins=23.79 pro=47 1a=False 1b=False 2=False (69.6s)
Sep 13 21:16:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:59,077 main INFO screen ALI pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=True (62.7s)
Sep 13 21:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:17:28,259 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.4s)
Sep 13 21:17:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:17:50,757 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 13 21:18:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:04,711 main INFO screen NOCAP pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 13 21:18:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:22,901 main INFO screen ALGO pass=0 dev=3.98 ins=22.83 pro=64 1a=False 1b=True 2=True (54.6s)
Sep 13 21:18:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:42,400 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 13 21:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:56,295 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 13 21:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:22,216 main INFO screen cry pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.3s)
Sep 13 21:19:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:31,286 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.9s)
Sep 13 21:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:55,870 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.6s)
Sep 13 21:20:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:20:28,330 main INFO screen savemeeee pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (66.1s)
Sep 13 21:20:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:20:36,263 main INFO screen WOFI pass=0 dev=61.29 ins=0.0 pro=1 1a=False 1b=False 2=True (65.0s)
Sep 13 21:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:21:10,266 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:21:10 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:21:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:21:11,354 main INFO screen FOMOxDRAKE pass=1 dev=0.21 ins=0.0 pro=13 1a=False 1b=False 2=False (75.5s)
Sep 13 21:21:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:21:36,792 main INFO screen WANKER pass=0 dev=0.0 ins=25.18 pro=59 1a=False 1b=False 2=True (68.5s)
Sep 13 21:21:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:21:41,848 main INFO screen POKEMON pass=0 dev=0.0 ins=24.23 pro=1 1a=False 1b=False 2=True (65.6s)
Sep 13 21:22:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:22:04,380 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (53.0s)
Sep 13 21:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:22:42,578 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (60.7s)
Sep 13 21:22:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:22:48,608 main INFO screen $speed pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (71.8s)
Sep 13 21:23:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:23:14,026 main INFO screen JAKE pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (69.6s)
Sep 13 21:23:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:23:36,632 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.1s)
Sep 13 21:23:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:23:39,365 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (50.8s)
Sep 13 21:24:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:24:19,546 main INFO screen CHUB pass=0 dev=0.0 ins=49.03 pro=17 1a=False 1b=False 2=True (65.5s)
Sep 13 21:24:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:24:28,488 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (51.9s)
Sep 13 21:24:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:24:36,971 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.6s)
Sep 13 21:25:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:25:17,189 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.6s)
Sep 13 21:25:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:25:24,668 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (47.7s)
Sep 13 21:25:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:25:26,650 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.2s)
Sep 13 21:26:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:26:11,995 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (54.8s)
Sep 13 21:26:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:26:23,377 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:26:23 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:26:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:26:29,101 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.4s)
Sep 13 21:26:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:26:31,692 main INFO screen HUMAN pass=0 dev=0.0 ins=42.95 pro=78 1a=False 1b=False 2=True (65.0s)
Sep 13 21:27:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:27:11,069 main INFO screen MSTR pass=0 dev=0.0 ins=23.11 pro=58 1a=False 1b=False 2=True (59.1s)
Sep 13 21:27:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:27:35,710 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.0s)
Sep 13 21:27:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:27:36,715 main INFO screen TWINU pass=0 dev=0.0 ins=23.77 pro=70 1a=False 1b=False 2=True (67.6s)
Sep 13 21:28:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:28:13,734 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.7s)
Sep 13 21:28:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:28:43,122 main INFO screen OpenAI pass=0 dev=0.0 ins=149.06 pro=1 1a=False 1b=False 2=True (66.4s)
Sep 13 21:28:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:28:43,443 main INFO screen Pumpty pass=0 dev=0.02 ins=0.0 pro=6 1a=False 1b=False 2=False (67.7s)
Sep 13 21:29:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:29:06,535 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 13 21:29:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:29:34,004 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (50.9s)
Sep 13 21:29:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:29:39,571 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.1s)
Sep 13 21:29:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:29:56,731 main INFO screen TOAD pass=0 dev=0.29 ins=0.0 pro=1 1a=False 1b=False 2=False (50.2s)
Sep 13 21:30:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:30:45,754 main INFO screen WRANGLER pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (71.7s)
Sep 13 21:30:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:30:47,907 main INFO screen Cat pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (68.3s)
Sep 13 21:30:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:30:52,209 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.5s)
Sep 13 21:31:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:31:25,124 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:31:25 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:31:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:31:52,524 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 13 21:31:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:31:53,961 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 13 21:31:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:31:56,465 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (68.6s)
Sep 13 21:32:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:32:48,360 main INFO screen NASDARQ pass=0 dev=0.0 ins=48.51 pro=47 1a=False 1b=False 2=True (55.8s)
Sep 13 21:33:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:33:00,842 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (66.9s)
Sep 13 21:33:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:33:02,499 main INFO screen Million pass=1 dev=0.0 ins=8.79 pro=63 1a=False 1b=False 2=False (66.0s)
Sep 13 21:33:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:33:43,517 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.2s)
Sep 13 21:34:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:34:12,739 main INFO screen AIDEGE pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (70.2s)
Sep 13 21:34:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:34:13,166 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.3s)
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:34:57,931 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 21:34:57 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 21:35:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:35:15,941 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (92.4s)
Sep 13 21:35:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:35:54,328 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (101.2s)
Sep 13 21:36:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:36:04,564 main INFO screen myth pass=0 dev=0.0 ins=52.83 pro=11 1a=False 1b=False 2=True (111.8s)
Sep 13 21:36:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:36:06,107 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (50.2s)
Sep 13 21:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:36:36,346 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:36:36 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T20:12:26Z
--- update 2026-09-13T20:17:36Z
--- update 2026-09-13T20:22:59Z
--- update 2026-09-13T20:28:22Z
--- update 2026-09-13T20:33:36Z
--- update 2026-09-13T20:38:57Z
Running as unit: schaduwbot-wallets.service; invocation ID: 301ce98199ac46cc8bdea3ab53015d56
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T20:44:08Z
--- update 2026-09-13T20:49:14Z
--- update 2026-09-13T20:54:15Z
--- update 2026-09-13T20:59:36Z
--- update 2026-09-13T21:04:58Z
--- update 2026-09-13T21:10:36Z
--- update 2026-09-13T21:15:38Z
--- update 2026-09-13T21:21:09Z
--- update 2026-09-13T21:26:22Z
--- update 2026-09-13T21:31:24Z
--- update 2026-09-13T21:36:35Z
```

## Analyses (laatste 25 regels)
```
inactive
20:58:24   24000 tokens, 2539115 trades, 362670 posities (122s)
20:58:34   26000 tokens, 2749363 trades, 392838 posities (132s)
20:58:44   28000 tokens, 2951661 trades, 418764 posities (143s)
20:58:55   30000 tokens, 3167138 trades, 449939 posities (153s)
20:59:06   32000 tokens, 3395846 trades, 485427 posities (164s)
20:59:16   34000 tokens, 3598592 trades, 514118 posities (174s)
20:59:27   36000 tokens, 3791936 trades, 538973 posities (185s)
20:59:38   38000 tokens, 4009130 trades, 571221 posities (196s)
20:59:50   40000 tokens, 4217529 trades, 602889 posities (208s)
21:00:01   42000 tokens, 4419767 trades, 629224 posities (219s)
21:00:11   44000 tokens, 4617797 trades, 654225 posities (229s)
21:00:22   46000 tokens, 4814574 trades, 683467 posities (240s)
21:00:34   48000 tokens, 5035877 trades, 716964 posities (253s)
21:00:45   50000 tokens, 5214248 trades, 742397 posities (263s)
21:00:57   52000 tokens, 5426165 trades, 774722 posities (275s)
21:01:10   54000 tokens, 5649674 trades, 809593 posities (289s)
21:01:23   56000 tokens, 5861579 trades, 840319 posities (301s)
21:01:36   58000 tokens, 6086009 trades, 875935 posities (315s)
21:01:48   60000 tokens, 6302939 trades, 921314 posities (327s)
21:01:55 posities: 941185 uit 6436124 trades (336s)
21:02:09 199194 wallets gerekend
21:02:10 geluk-toets
21:02:45 persistentie
21:02:48 kopieer-simulatie
21:04:24 klaar in 485s -> /opt/schaduwbot/reports/wallets.md
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
