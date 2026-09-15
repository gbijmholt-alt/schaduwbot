# Schaduwbot status

- tijd: 2026-09-15 02:06:44 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 12 hours, 19 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.7G/38G | geheugen: 2323/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 156756, "tokens_in_memory": 9685, "msgs": 23893608, "trades": 4784001, "creates": 51007, "decode_fail": 412480, "rpc_calls": 134827, "rpc_errors": 13, "sol_usd": 102.23442347755292, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 01:42:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:42:14,520 main INFO screen npc pass=0 dev=0.0 ins=18.35 pro=45 1a=False 1b=False 2=True (62.1s)
Sep 15 01:42:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:42:42,459 main INFO screen DATACENTER pass=0 dev=0.0 ins=12.11 pro=20 1a=False 1b=False 2=True (66.8s)
Sep 15 01:43:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:43:12,519 main INFO screen BIKE TRUMP pass=0 dev=0.0 ins=79.17 pro=2 1a=False 1b=True 2=True (61.2s)
Sep 15 01:43:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:43:13,529 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 15 01:43:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:43:40,027 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.6s)
Sep 15 01:44:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:44:10,939 main INFO screen HYPERGAMY pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (58.4s)
Sep 15 01:44:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:44:21,471 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.9s)
Sep 15 01:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:44:37,458 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (57.4s)
Sep 15 01:45:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:45:05,812 main INFO screen PCA pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (54.9s)
Sep 15 01:45:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:45:35,004 main INFO screen PONS pass=0 dev=0.0 ins=21.14 pro=76 1a=False 1b=False 2=True (73.5s)
Sep 15 01:45:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:45:36,752 main INFO screen Fonke pass=0 dev=0.0 ins=4.2 pro=31 1a=False 1b=False 2=False (59.3s)
Sep 15 01:46:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:46:02,613 main INFO screen fever pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.8s)
Sep 15 01:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:46:15,597 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:46:15 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:46:31,450 main INFO screen NYT Coin pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (54.7s)
Sep 15 01:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:46:31,514 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (56.5s)
Sep 15 01:46:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:46:52,852 main INFO screen Oiled pass=0 dev=0.0 ins=20.04 pro=52 1a=False 1b=False 2=False (50.2s)
Sep 15 01:47:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:47:17,105 main INFO screen Froge pass=0 dev=0.0 ins=20.49 pro=44 1a=False 1b=False 2=True (45.7s)
Sep 15 01:47:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:47:41,199 main INFO screen WITTY pass=0 dev=0.0 ins=35.47 pro=61 1a=False 1b=False 2=True (69.7s)
Sep 15 01:47:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:47:49,430 main INFO screen Fonke pass=0 dev=0.0 ins=6.79 pro=47 1a=False 1b=False 2=True (56.6s)
Sep 15 01:48:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:48:16,221 main INFO screen magus pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.1s)
Sep 15 01:48:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:48:41,090 main INFO screen PEAR pass=0 dev=0.0 ins=40.27 pro=24 1a=True 1b=False 2=False (59.9s)
Sep 15 01:48:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:48:50,999 main INFO screen  AI pass=0 dev=0.0 ins=21.47 pro=56 1a=False 1b=False 2=True (61.6s)
Sep 15 01:49:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:49:29,238 main INFO screen Fonke pass=0 dev=0.0 ins=5.19 pro=58 1a=False 1b=False 2=False (73.0s)
Sep 15 01:49:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:49:29,588 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (48.5s)
Sep 15 01:50:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:50:06,873 main INFO screen Windows pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (75.9s)
Sep 15 01:50:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:50:23,696 main INFO screen Pro-Human pass=0 dev=0.0 ins=25.16 pro=53 1a=False 1b=False 2=True (54.5s)
Sep 15 01:50:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:50:33,862 main INFO screen BGE pass=0 dev=0.0 ins=0.24 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 15 01:51:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:51:02,408 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.5s)
Sep 15 01:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:51:17,269 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:51:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:51:17,582 main INFO screen VOID pass=0 dev=0.0 ins=1.26 pro=10 1a=False 1b=False 2=False (53.9s)
Sep 15 01:51:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:51:26,555 main INFO screen copium pass=0 dev=0.0 ins=24.21 pro=64 1a=False 1b=False 2=True (52.7s)
Sep 15 01:52:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:52:06,710 main INFO screen SCALES pass=0 dev=0.0 ins=24.06 pro=59 1a=False 1b=False 2=True (64.3s)
Sep 15 01:52:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:52:13,475 main INFO screen copium pass=0 dev=0.0 ins=23.58 pro=15 1a=False 1b=False 2=True (46.9s)
Sep 15 01:52:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:52:13,804 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (56.2s)
Sep 15 01:52:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:52:56,036 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (49.3s)
Sep 15 01:53:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:53:15,548 main INFO screen Fun pass=0 dev=0.0 ins=28.73 pro=21 1a=True 1b=False 2=True (61.7s)
Sep 15 01:53:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:53:21,046 main INFO screen gegner pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.6s)
Sep 15 01:53:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:53:50,627 main INFO screen SLOP pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (54.6s)
Sep 15 01:54:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:54:07,759 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.2s)
Sep 15 01:54:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:54:25,412 main INFO screen WHEELBERG pass=0 dev=0.0 ins=28.61 pro=74 1a=False 1b=False 2=True (64.4s)
Sep 15 01:54:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:54:47,522 main INFO screen Holdcoin pass=0 dev=0.0 ins=6.26 pro=57 1a=False 1b=False 2=True (56.9s)
Sep 15 01:55:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:55:02,729 main INFO screen funymaz pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.0s)
Sep 15 01:55:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:55:32,557 main INFO screen ram pass=0 dev=0.0 ins=10.38 pro=74 1a=False 1b=False 2=True (67.1s)
Sep 15 01:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:55:38,113 main INFO screen SODL pass=0 dev=0.0 ins=49.53 pro=26 1a=True 1b=False 2=True (50.6s)
Sep 15 01:56:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:56:00,830 main INFO screen LMAOGIRL pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (58.1s)
Sep 15 01:56:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:56:32,472 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:56:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:56:33,792 main INFO screen ECTF pass=0 dev=0.0 ins=125.11 pro=1 1a=False 1b=False 2=True (61.2s)
Sep 15 01:56:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:56:43,775 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=False 2=True (65.7s)
Sep 15 01:57:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:57:03,101 main INFO screen AI pass=0 dev=0.0 ins=20.24 pro=69 1a=False 1b=False 2=True (62.3s)
Sep 15 01:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:57:28,273 main INFO screen Nutsack pass=0 dev=0.0 ins=17.68 pro=51 1a=False 1b=False 2=True (54.5s)
Sep 15 01:57:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:57:37,163 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.4s)
Sep 15 01:57:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:57:49,637 main INFO screen mikeandike pass=0 dev=0.0 ins=5.75 pro=20 1a=False 1b=False 2=False (46.5s)
Sep 15 01:58:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:58:34,683 main INFO screen SLOP pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (66.4s)
Sep 15 01:58:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:58:39,377 main INFO screen Bott pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (62.2s)
Sep 15 01:58:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:58:59,353 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.7s)
Sep 15 01:59:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:59:25,825 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (51.1s)
Sep 15 01:59:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:59:46,780 main INFO screen CAPY pass=0 dev=0.0 ins=46.75 pro=20 1a=False 1b=False 2=True (67.4s)
Sep 15 02:00:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:00:04,989 main INFO screen MAHOMES pass=0 dev=0.0 ins=27.14 pro=51 1a=False 1b=False 2=True (65.6s)
Sep 15 02:00:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:00:29,421 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.6s)
Sep 15 02:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:00:45,876 main INFO screen Cupsey pass=0 dev=0.0 ins=17.51 pro=73 1a=False 1b=False 2=True (59.1s)
Sep 15 02:01:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:01:03,809 main INFO screen SLOP pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (58.8s)
Sep 15 02:01:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:01:24,521 main INFO screen CHONK pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (55.1s)
Sep 15 02:01:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:01:37,389 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:01:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:01:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:01:40,860 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.0s)
Sep 15 02:02:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:02:00,006 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.2s)
Sep 15 02:02:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:02:17,411 main INFO screen urgay pass=0 dev=0.0 ins=37.95 pro=22 1a=True 1b=False 2=True (52.9s)
Sep 15 02:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:02:36,014 main INFO screen HYUNDAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 15 02:02:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:02:57,042 main INFO screen Rarri pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 15 02:03:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:03:13,207 main INFO screen grandEUR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.8s)
Sep 15 02:03:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:03:32,493 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.5s)
Sep 15 02:04:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:04:06,737 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (69.7s)
Sep 15 02:04:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:04:13,006 main INFO screen DOJARAT pass=0 dev=0.0 ins=2.58 pro=6 1a=False 1b=False 2=False (59.8s)
Sep 15 02:04:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:04:45,747 main INFO screen Carbonoid pass=0 dev=0.0 ins=25.32 pro=78 1a=False 1b=False 2=True (73.3s)
Sep 15 02:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:22,147 main INFO screen Ferrari pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (75.4s)
Sep 15 02:05:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:26,562 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.6s)
Sep 15 02:05:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:41,105 aiohttp.access INFO 172.235.40.131 [15/Sep/2026:02:05:41 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 15 02:05:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:43,175 main INFO screen DRILLNYE pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (57.4s)
Sep 15 02:06:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:35,194 main INFO screen FAR pass=0 dev=0.0 ins=18.88 pro=30 1a=False 1b=False 2=False (68.6s)
Sep 15 02:06:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:36,919 main INFO screen TWIN pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=False (74.8s)
Sep 15 02:06:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:44,162 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:06:44 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T00:38:36Z
--- update 2026-09-15T00:43:36Z
--- update 2026-09-15T00:48:48Z
--- update 2026-09-15T00:54:19Z
--- update 2026-09-15T00:59:26Z
--- update 2026-09-15T01:04:36Z
--- update 2026-09-15T01:09:36Z
--- update 2026-09-15T01:15:15Z
--- update 2026-09-15T01:20:32Z
--- update 2026-09-15T01:25:36Z
--- update 2026-09-15T01:30:37Z
--- update 2026-09-15T01:35:39Z
--- update 2026-09-15T01:40:45Z
--- update 2026-09-15T01:46:14Z
--- update 2026-09-15T01:51:16Z
Running as unit: schaduwbot-wallets.service; invocation ID: 198697cd6df2473cb461b6a874faa3b9
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T01:56:31Z
--- update 2026-09-15T02:01:36Z
--- update 2026-09-15T02:06:42Z
```

## Analyses (laatste 25 regels)
```
active
00:32:06   56000 tokens, 5365533 trades, 644406 posities (382s)
00:32:23   58000 tokens, 5562944 trades, 669075 posities (399s)
00:32:39   60000 tokens, 5746516 trades, 689739 posities (415s)
00:32:57   62000 tokens, 5955952 trades, 716730 posities (433s)
00:33:13   64000 tokens, 6142789 trades, 744367 posities (449s)
00:33:30   66000 tokens, 6356758 trades, 771423 posities (466s)
00:33:43   68000 tokens, 6541957 trades, 795263 posities (479s)
00:33:56   70000 tokens, 6731219 trades, 818210 posities (492s)
00:34:10   72000 tokens, 6922572 trades, 843202 posities (506s)
00:34:25   74000 tokens, 7133262 trades, 878980 posities (521s)
00:34:30 posities: 885811 uit 7196469 trades (529s)
00:34:43 211069 wallets gerekend
00:34:43 geluk-toets
00:35:19 persistentie
00:35:22 kopieer-simulatie
00:37:42 klaar in 721s -> /opt/schaduwbot/reports/wallets.md
01:51:17 99035 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
01:51:40   ingelezen tot rowid 10260007 (200000 rijen, 200000 bruikbaar)
01:51:45   ingelezen tot rowid 10315765 (255758 rijen, 255758 bruikbaar)
01:51:47 ingelezen: 255758 nieuwe trades, 255758 bruikbaar (30s)
01:54:40 3000 aankopen van gevolgde wallets geëvalueerd
01:55:31 vroege kopers: 270 voldoen nu, register 480, 346 tokens beoordeeld
01:56:05 grote spelers: saldo van 396 wallets opgehaald
01:56:37 herkomst: 40 posities gekoppeld
01:56:49 klaar in 333s -> /opt/schaduwbot/reports/ledger.md
```

## IJking poolkoers (laatste 12 regels)
```
01:25:42 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=77 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:25:42 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 8/40/164 | al gemeten: 372
01:30:43 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=79 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:30:43 ijk-diagnose: nieuwste migratie 1.8 min oud | migraties 15/60/240 min: 8/39/158 | al gemeten: 374
01:35:51 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=83 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:35:52 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 8/41/158 | al gemeten: 378
01:40:57 ijk: +4 van 4 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=85 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:40:57 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 10/43/158 | al gemeten: 382
01:46:21 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=86 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:46:21 ijk-diagnose: nieuwste migratie 1.5 min oud | migraties 15/60/240 min: 11/45/157 | al gemeten: 385
01:51:50 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=90 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:51:54 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 11/46/159 | al gemeten: 389
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
