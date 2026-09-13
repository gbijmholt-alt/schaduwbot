# Schaduwbot status

- tijd: 2026-09-13 23:03:35 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 9 hours, 16 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.1G/38G | geheugen: 1925/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 59367, "tokens_in_memory": 8275, "msgs": 7469749, "trades": 1610094, "creates": 17251, "decode_fail": 147134, "rpc_calls": 47276, "rpc_errors": 2, "sol_usd": 99.9365774653433, "open_positions": 45, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 22:38:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:38:01,509 main INFO screen CATDOG pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.8s)
Sep 13 22:38:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:38:04,434 main INFO screen $speed pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (71.1s)
Sep 13 22:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:38:17,626 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:38:17 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 22:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:39:05,526 main INFO screen PVP pass=0 dev=0.0 ins=34.64 pro=73 1a=False 1b=False 2=True (70.0s)
Sep 13 22:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:39:05,544 main INFO screen mochi pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.0s)
Sep 13 22:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:39:07,648 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.2s)
Sep 13 22:39:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:39:58,636 main INFO screen FOMO pass=0 dev=0.0 ins=149.96 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 13 22:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:40:02,005 main INFO screen ROTATOOR pass=0 dev=0.01 ins=99.12 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 22:40:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:40:19,497 main INFO screen Glonk pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (71.8s)
Sep 13 22:41:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:41:08,209 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.6s)
Sep 13 22:41:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:41:14,201 main INFO screen AdamSandr pass=1 dev=0.0 ins=2.1 pro=64 1a=False 1b=False 2=False (72.2s)
Sep 13 22:41:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:41:28,571 main INFO screen copycat pass=0 dev=0.0 ins=5.51 pro=58 1a=False 1b=False 2=True (69.1s)
Sep 13 22:42:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:42:18,789 main INFO screen SOL pass=0 dev=0.0 ins=37.52 pro=69 1a=False 1b=False 2=True (70.6s)
Sep 13 22:42:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:42:21,050 main INFO screen PARABALLIC pass=0 dev=0.0 ins=20.24 pro=62 1a=False 1b=False 2=True (66.8s)
Sep 13 22:42:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:42:29,134 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.6s)
Sep 13 22:43:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:43:13,419 main INFO screen TROLLGPT pass=0 dev=0.35 ins=78.78 pro=6 1a=False 1b=True 2=True (52.4s)
Sep 13 22:43:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:43:14,976 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 13 22:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:43:18,287 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:43:18 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 22:43:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:43:21,657 main INFO screen FOMOLIFE pass=1 dev=0.0 ins=17.37 pro=28 1a=False 1b=False 2=False (52.5s)
Sep 13 22:44:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:44:29,645 main INFO screen GS pass=0 dev=0.0 ins=16.25 pro=57 1a=False 1b=False 2=True (76.2s)
Sep 13 22:44:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:44:30,357 main INFO screen ELON TAXI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.4s)
Sep 13 22:44:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:44:33,047 main INFO screen OIL pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=True (71.4s)
Sep 13 22:45:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:45:38,448 aiohttp.access INFO 20.118.36.85 [13/Sep/2026:22:45:38 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 13 22:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:45:45,324 main INFO screen VOID pass=0 dev=44.96 ins=0.0 pro=5 1a=False 1b=False 2=True (72.3s)
Sep 13 22:45:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:45:46,101 main INFO screen ELMA pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (75.7s)
Sep 13 22:45:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:45:46,236 main INFO screen TWIX pass=0 dev=0.0 ins=41.21 pro=70 1a=False 1b=False 2=True (76.6s)
Sep 13 22:47:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:02,287 main INFO screen TESTICLES pass=0 dev=0.0 ins=24.81 pro=81 1a=False 1b=False 2=True (76.2s)
Sep 13 22:47:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:04,261 main INFO screen PARABALLIC pass=1 dev=0.0 ins=19.61 pro=56 1a=False 1b=False 2=False (78.9s)
Sep 13 22:47:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:05,915 aiohttp.access INFO 152.32.234.39 [13/Sep/2026:22:47:05 +0000] "GET / HTTP/1.1" 404 174 "-" "curl/7.29.0"
Sep 13 22:47:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:06,819 aiohttp.access INFO 152.32.234.39 [13/Sep/2026:22:47:06 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 22:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:07,244 aiohttp.access INFO 152.32.234.39 [13/Sep/2026:22:47:07 +0000] "UNKNOWN / HTTP/1.0" 400 231 "-" "-"
Sep 13 22:47:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:47:08,956 main INFO screen copycat pass=0 dev=0.0 ins=10.41 pro=52 1a=False 1b=False 2=True (82.7s)
Sep 13 22:48:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:48:19,700 main INFO screen GVP pass=1 dev=0.0 ins=12.77 pro=10 1a=False 1b=False 2=False (77.4s)
Sep 13 22:48:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:48:20,623 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:48:20 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 22:48:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:48:23,130 main INFO screen HOE pass=1 dev=0.07 ins=0.0 pro=58 1a=False 1b=False 2=False (78.9s)
Sep 13 22:48:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:48:33,142 main INFO screen jinex pass=0 dev=0.0 ins=0.7 pro=7 1a=False 1b=False 2=False (84.2s)
Sep 13 22:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:49:33,562 main INFO screen TITTIES pass=0 dev=0.0 ins=16.61 pro=76 1a=False 1b=False 2=True (70.4s)
Sep 13 22:49:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:49:36,367 main INFO screen COPYCAT pass=0 dev=0.0 ins=0.0 pro=78 1a=False 1b=False 2=True (76.7s)
Sep 13 22:49:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:49:42,954 main INFO screen $CAT pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (69.8s)
Sep 13 22:50:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:50:23,653 main INFO screen MIZO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 13 22:50:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:50:25,621 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.3s)
Sep 13 22:50:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:50:47,405 main INFO screen BOOBS pass=0 dev=0.0 ins=11.9 pro=64 1a=False 1b=False 2=True (64.5s)
Sep 13 22:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:51:17,626 main INFO screen OpenAI pass=0 dev=99.29 ins=0.0 pro=1 1a=False 1b=False 2=True (54.0s)
Sep 13 22:51:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:51:34,447 main INFO screen TITTIES pass=0 dev=0.0 ins=24.76 pro=58 1a=False 1b=False 2=True (68.8s)
Sep 13 22:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:51:35,915 main INFO screen BUTTHOLE pass=0 dev=0.0 ins=5.51 pro=43 1a=False 1b=False 2=False (48.5s)
Sep 13 22:52:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:52:24,396 main INFO screen TITTIES pass=0 dev=0.0 ins=28.87 pro=6 1a=False 1b=False 2=False (49.9s)
Sep 13 22:52:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:52:31,658 main INFO screen TITTIES pass=1 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (74.0s)
Sep 13 22:52:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:52:41,297 main INFO screen organic pass=0 dev=0.0 ins=10.48 pro=59 1a=False 1b=False 2=True (65.4s)
Sep 13 22:53:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:53:32,391 main INFO screen BIKE CONOR pass=0 dev=0.0 ins=79.1 pro=12 1a=False 1b=False 2=True (68.0s)
Sep 13 22:53:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:53:32,820 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:53:32 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 22:53:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:53:35,153 main INFO screen fruit pass=0 dev=0.0 ins=24.94 pro=42 1a=False 1b=False 2=True (63.5s)
Sep 13 22:53:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:53:35,582 main INFO screen Pear pass=0 dev=0.0 ins=17.14 pro=14 1a=False 1b=False 2=True (54.3s)
Sep 13 22:54:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:54:44,297 main INFO screen COMPUTE pass=1 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=False (68.7s)
Sep 13 22:54:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:54:45,729 main INFO screen SOL pass=0 dev=0.0 ins=57.99 pro=86 1a=False 1b=False 2=True (73.3s)
Sep 13 22:54:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:54:47,208 main INFO screen fruit pass=0 dev=5.35 ins=26.15 pro=61 1a=False 1b=False 2=False (72.1s)
Sep 13 22:55:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:55:35,154 main INFO screen LLM pass=0 dev=0.0 ins=12.65 pro=10 1a=False 1b=False 2=False (47.9s)
Sep 13 22:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:55:38,034 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 13 22:55:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:55:40,393 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 13 22:56:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:56:22,497 main INFO screen TITTIES pass=0 dev=0.0 ins=28.78 pro=5 1a=False 1b=False 2=False (47.3s)
Sep 13 22:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:56:33,846 main INFO screen TITTIES pass=0 dev=0.0 ins=44.55 pro=37 1a=False 1b=False 2=True (53.5s)
Sep 13 22:56:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:56:43,895 main INFO screen SOL pass=0 dev=0.0 ins=41.66 pro=79 1a=False 1b=False 2=True (65.9s)
Sep 13 22:57:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:57:18,887 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (56.4s)
Sep 13 22:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:57:41,510 main INFO screen iFOLD pass=0 dev=1.59 ins=20.37 pro=66 1a=False 1b=False 2=True (67.7s)
Sep 13 22:57:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:57:58,697 main INFO screen TITTIES pass=0 dev=0.0 ins=45.35 pro=82 1a=False 1b=False 2=True (74.8s)
Sep 13 22:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:58:20,434 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (61.5s)
Sep 13 22:58:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:58:33,883 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:58:33 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 22:58:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:58:52,600 main INFO screen 2FAST pass=1 dev=0.0 ins=1.67 pro=56 1a=False 1b=False 2=False (71.1s)
Sep 13 22:58:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:58:56,598 main INFO screen PUMP pass=0 dev=79.31 ins=160.23 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 13 22:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:59:16,847 main INFO screen TITTIES pass=0 dev=0.0 ins=45.35 pro=32 1a=False 1b=False 2=True (56.4s)
Sep 13 23:00:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:00:04,543 main INFO screen COPYCAT pass=0 dev=0.0 ins=14.4 pro=71 1a=False 1b=False 2=True (71.9s)
Sep 13 23:00:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:00:07,358 main INFO screen PONSBER pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=False 2=True (70.8s)
Sep 13 23:00:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:00:12,254 main INFO screen MILLI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.4s)
Sep 13 23:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:01:01,239 main INFO screen RR pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 13 23:01:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:01:14,545 main INFO screen BPCATE pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (70.0s)
Sep 13 23:01:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:01:18,380 main INFO screen SOL pass=0 dev=0.0 ins=12.49 pro=60 1a=False 1b=False 2=False (66.1s)
Sep 13 23:01:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:01:59,738 main INFO screen DUDE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 13 23:02:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:02:26,669 main INFO screen GVP pass=0 dev=0.0 ins=17.2 pro=20 1a=False 1b=False 2=True (68.3s)
Sep 13 23:02:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:02:27,222 main INFO screen RISE pass=0 dev=42.67 ins=0.0 pro=3 1a=False 1b=False 2=False (72.7s)
Sep 13 23:03:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:03:07,358 main INFO screen BIKE BULL pass=0 dev=0.11 ins=77.74 pro=7 1a=False 1b=True 2=True (67.6s)
Sep 13 23:03:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:03:35,412 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:03:35 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T21:36:35Z
--- update 2026-09-13T21:41:36Z
--- update 2026-09-13T21:47:07Z
--- update 2026-09-13T21:52:16Z
--- update 2026-09-13T21:57:31Z
--- update 2026-09-13T22:02:36Z
--- update 2026-09-13T22:07:38Z
--- update 2026-09-13T22:12:49Z
--- update 2026-09-13T22:18:02Z
--- update 2026-09-13T22:23:04Z
--- update 2026-09-13T22:28:11Z
--- update 2026-09-13T22:33:12Z
--- update 2026-09-13T22:38:16Z
--- update 2026-09-13T22:43:17Z
Running as unit: schaduwbot-wallets.service; invocation ID: bacba8bde01940a1872493ea161ca641
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T22:48:19Z
--- update 2026-09-13T22:53:31Z
--- update 2026-09-13T22:58:32Z
--- update 2026-09-13T23:03:34Z
```

## Analyses (laatste 25 regels)
```
active
21:01:36   58000 tokens, 6086009 trades, 875935 posities (315s)
21:01:48   60000 tokens, 6302939 trades, 921314 posities (327s)
21:01:55 posities: 941185 uit 6436124 trades (336s)
21:02:09 199194 wallets gerekend
21:02:10 geluk-toets
21:02:45 persistentie
21:02:48 kopieer-simulatie
21:04:24 klaar in 485s -> /opt/schaduwbot/reports/wallets.md
22:43:20 65147 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
22:43:40   ingelezen tot rowid 7068112 (200000 rijen, 200000 bruikbaar)
22:43:44   ingelezen tot rowid 7125925 (257813 rijen, 257813 bruikbaar)
22:43:45 ingelezen: 257813 nieuwe trades, 257813 bruikbaar (27s)
22:45:20 3000 aankopen van gevolgde wallets geëvalueerd
22:45:38 vroege kopers: 201 voldoen nu, register 345, 317 tokens beoordeeld
22:45:59 grote spelers: saldo van 327 wallets opgehaald
22:47:07 herkomst: 40 posities gekoppeld
22:47:14 klaar in 236s -> /opt/schaduwbot/reports/ledger.md
22:52:57 S1: gezakt — toets n=12129, verkennend n=14656
22:52:58 klaar in 344s -> /opt/schaduwbot/reports/hypotheses.md
22:52:58 probe: 150 transacties ophalen
22:56:23 poolveld: 14 pools bekeken, 0 te gaan -> vastgesteld @43
22:57:34 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
22:57:34 prijsijk: n=59 -> mediane afwijking 100% boven 25%
22:57:35 na-migratie: 100 paren te checken
22:59:15 na-migratie: 26 paren, 1 prijzen
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
