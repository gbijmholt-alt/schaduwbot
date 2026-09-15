# Schaduwbot status

- tijd: 2026-09-15 04:59:50 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 15 hours, 12 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.8G/38G | geheugen: 2240/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 167142, "tokens_in_memory": 7756, "msgs": 25596237, "trades": 5093488, "creates": 54469, "decode_fail": 434415, "rpc_calls": 145142, "rpc_errors": 13, "sol_usd": 101.29417669366741, "open_positions": 59, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:28,567 main INFO screen KET pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (108.0s)
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:28,658 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:35:28 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 04:35:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:44,717 main INFO screen MDOR pass=0 dev=0.0 ins=19.58 pro=1 1a=False 1b=False 2=True (104.8s)
Sep 15 04:35:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:46,373 main INFO screen CATE pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (110.3s)
Sep 15 04:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:27,985 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 15 04:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:37,001 main INFO screen DogC pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (52.3s)
Sep 15 04:36:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:45,918 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 15 04:37:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:17,754 main INFO screen SOLdiers pass=0 dev=0.0 ins=22.07 pro=36 1a=False 1b=False 2=True (49.8s)
Sep 15 04:37:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:34,019 main INFO screen WOFI pass=0 dev=1.81 ins=118.36 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 15 04:37:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:59,086 main INFO screen STUMP pass=0 dev=10.3 ins=0.0 pro=23 1a=False 1b=False 2=False (73.2s)
Sep 15 04:38:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:16,207 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (58.5s)
Sep 15 04:38:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:29,140 main INFO screen Toely pass=0 dev=0.0 ins=36.06 pro=43 1a=False 1b=False 2=True (55.1s)
Sep 15 04:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:55,963 main INFO screen HIPPLEX pass=0 dev=0.0 ins=78.91 pro=18 1a=False 1b=True 2=True (56.9s)
Sep 15 04:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:05,741 main INFO screen 4096 pass=0 dev=0.0 ins=36.55 pro=69 1a=False 1b=False 2=True (49.5s)
Sep 15 04:39:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:38,226 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:39:38 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:39:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:41,387 main INFO screen Zucker pass=0 dev=0.0 ins=0.0 pro=43 1a=False 1b=False 2=False (72.2s)
Sep 15 04:39:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:57,105 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.1s)
Sep 15 04:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:40:02,488 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 15 04:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:40:56,442 main INFO screen KING pass=0 dev=0.0 ins=19.01 pro=64 1a=False 1b=False 2=True (75.1s)
Sep 15 04:41:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:41:13,163 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.1s)
Sep 15 04:41:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:41:14,938 main INFO screen BIKEROBI pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=False 2=True (72.4s)
Sep 15 04:41:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:41:56,766 main INFO screen Lobster pass=0 dev=0.0 ins=41.21 pro=70 1a=False 1b=False 2=True (60.3s)
Sep 15 04:42:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:42:20,904 main INFO screen SCALES pass=0 dev=0.0 ins=5.01 pro=47 1a=False 1b=False 2=False (67.7s)
Sep 15 04:42:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:42:23,381 main INFO screen GOKU pass=0 dev=0.0 ins=30.95 pro=54 1a=False 1b=False 2=True (68.4s)
Sep 15 04:42:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:42:54,645 main INFO screen CHAWIZ pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.9s)
Sep 15 04:43:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:43:21,358 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 15 04:43:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:43:21,376 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 15 04:44:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:44:07,856 main INFO screen faucat pass=0 dev=0.0 ins=12.04 pro=57 1a=False 1b=False 2=True (73.2s)
Sep 15 04:44:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:44:27,919 main INFO screen WOFI pass=0 dev=0.0 ins=19.72 pro=0 1a=False 1b=False 2=True (66.5s)
Sep 15 04:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:44:37,217 main INFO screen PRAWN pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (75.9s)
Sep 15 04:44:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:44:39,277 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:44:39 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:45:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:45:06,265 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.4s)
Sep 15 04:45:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:45:26,628 main INFO screen CMAX pass=0 dev=0.0 ins=0.21 pro=6 1a=False 1b=False 2=False (58.7s)
Sep 15 04:45:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:45:35,568 main INFO screen Unc pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.3s)
Sep 15 04:46:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:46:11,835 main INFO screen SOLANAGOMEZ pass=0 dev=0.0 ins=23.46 pro=54 1a=False 1b=False 2=True (65.6s)
Sep 15 04:46:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:46:24,040 main INFO screen BOOGERS  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.4s)
Sep 15 04:46:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:46:33,760 main INFO screen LELD pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (58.2s)
Sep 15 04:47:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:47:19,011 main INFO screen LELD pass=0 dev=0.0 ins=0.16 pro=21 1a=False 1b=False 2=False (55.0s)
Sep 15 04:47:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:47:21,082 main INFO screen Cumsey pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (69.2s)
Sep 15 04:47:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:47:37,606 main INFO screen kevinheart pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (63.8s)
Sep 15 04:48:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:48:24,550 main INFO screen MCD pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (63.5s)
Sep 15 04:48:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:48:30,005 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (71.0s)
Sep 15 04:48:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:48:33,547 main INFO screen CHAWIZ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.9s)
Sep 15 04:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:49:33,355 main INFO screen RAIN pass=0 dev=0.0 ins=29.47 pro=58 1a=False 1b=False 2=True (68.8s)
Sep 15 04:49:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:49:36,860 main INFO screen Cocacola pass=0 dev=18.07 ins=0.0 pro=17 1a=False 1b=False 2=False (66.9s)
Sep 15 04:49:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:49:39,706 main INFO screen LELD pass=0 dev=0.0 ins=0.34 pro=44 1a=False 1b=False 2=False (66.2s)
Sep 15 04:49:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:49:41,453 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:49:41 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:50:46,451 main INFO screen oldspice pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.6s)
Sep 15 04:50:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:50:47,548 main INFO screen LELD pass=0 dev=0.0 ins=0.0 pro=44 1a=False 1b=False 2=False (74.2s)
Sep 15 04:50:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:50:51,169 main INFO screen KIRKYAHU pass=0 dev=0.0 ins=3.96 pro=64 1a=False 1b=False 2=False (71.5s)
Sep 15 04:51:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:51:43,065 main INFO screen SMUDGE pass=0 dev=0.0 ins=79.12 pro=4 1a=False 1b=True 2=True (55.5s)
Sep 15 04:51:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:51:55,524 main INFO screen Perfected pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.1s)
Sep 15 04:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:51:56,532 main INFO screen BREAST pass=0 dev=0.0 ins=40.15 pro=23 1a=False 1b=False 2=True (65.4s)
Sep 15 04:52:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:52:48,487 main INFO screen Horse pass=0 dev=0.0 ins=17.55 pro=52 1a=False 1b=False 2=False (65.4s)
Sep 15 04:52:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:52:51,803 main INFO screen CR7 pass=0 dev=0.08 ins=126.18 pro=1 1a=False 1b=False 2=True (56.3s)
Sep 15 04:52:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:52:56,816 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (60.3s)
Sep 15 04:53:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:53:40,116 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.6s)
Sep 15 04:53:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:53:57,120 main INFO screen Horse pass=0 dev=0.0 ins=29.83 pro=63 1a=False 1b=False 2=True (65.3s)
Sep 15 04:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:00,609 main INFO screen NTDA pass=0 dev=0.0 ins=19.93 pro=1 1a=False 1b=False 2=True (63.8s)
Sep 15 04:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:37,215 main INFO screen INSTAR pass=0 dev=0.0 ins=20.28 pro=64 1a=False 1b=False 2=True (57.1s)
Sep 15 04:54:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:46,494 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:54:46 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:54:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:53,730 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.6s)
Sep 15 04:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:55,718 main INFO screen OPTIONS pass=0 dev=0.0 ins=56.41 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 15 04:55:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:29,296 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.1s)
Sep 15 04:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:48,840 main INFO screen WHITETYSON pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (55.1s)
Sep 15 04:55:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:50,253 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.5s)
Sep 15 04:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:26,791 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 15 04:56:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:45,478 main INFO screen NVDA pass=0 dev=0.0 ins=135.65 pro=0 1a=False 1b=False 2=True (56.6s)
Sep 15 04:56:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:56,489 main INFO screen LELD pass=0 dev=0.41 ins=0.15 pro=70 1a=False 1b=False 2=False (66.2s)
Sep 15 04:57:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:32,200 main INFO screen Bean pass=0 dev=0.0 ins=8.15 pro=28 1a=False 1b=False 2=False (65.4s)
Sep 15 04:57:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:52,569 main INFO screen MOon pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 15 04:57:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:57,108 main INFO screen Cocacola pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.6s)
Sep 15 04:58:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:58:31,203 main INFO screen HOT pass=0 dev=0.0 ins=36.85 pro=68 1a=False 1b=False 2=True (59.0s)
Sep 15 04:59:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:09,635 main INFO screen BABYSLING pass=0 dev=0.01 ins=2.36 pro=48 1a=False 1b=False 2=False (72.5s)
Sep 15 04:59:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:10,966 main INFO screen INf pass=0 dev=135.96 ins=0.0 pro=15 1a=False 1b=False 2=False (78.4s)
Sep 15 04:59:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:32,756 main INFO screen CREW pass=0 dev=0.0 ins=8.55 pro=30 1a=False 1b=False 2=False (61.6s)
Sep 15 04:59:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:50,429 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:59:50 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T03:34:05Z
--- update 2026-09-15T03:39:07Z
--- update 2026-09-15T03:44:09Z
--- update 2026-09-15T03:49:12Z
--- update 2026-09-15T03:54:12Z
Running as unit: schaduwbot-wallets.service; invocation ID: c556852febb7497c926f7c233c44f1d1
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T03:59:12Z
--- update 2026-09-15T04:04:15Z
--- update 2026-09-15T04:09:16Z
--- update 2026-09-15T04:14:19Z
--- update 2026-09-15T04:19:20Z
--- update 2026-09-15T04:24:32Z
--- update 2026-09-15T04:29:35Z
--- update 2026-09-15T04:34:36Z
--- update 2026-09-15T04:39:36Z
--- update 2026-09-15T04:44:37Z
--- update 2026-09-15T04:49:40Z
--- update 2026-09-15T04:54:45Z
--- update 2026-09-15T04:59:49Z
```

## Analyses (laatste 25 regels)
```
inactive
04:37:40   38000 tokens, 3669904 trades, 439287 posities (251s)
04:37:56   40000 tokens, 3869261 trades, 465053 posities (267s)
04:38:12   42000 tokens, 4053581 trades, 487112 posities (283s)
04:38:27   44000 tokens, 4238786 trades, 509220 posities (299s)
04:38:42   46000 tokens, 4415347 trades, 529333 posities (314s)
04:38:58   48000 tokens, 4589550 trades, 549788 posities (329s)
04:39:15   50000 tokens, 4787116 trades, 574764 posities (347s)
04:39:32   52000 tokens, 4994455 trades, 600510 posities (363s)
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
```

## IJking poolkoers (laatste 12 regels)
```
03:39:20 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=124 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:39:20 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 8/37/155 | al gemeten: 442
03:44:15 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=126 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:44:15 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 8/36/155 | al gemeten: 444
03:49:22 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=129 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:49:22 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 10/37/155 | al gemeten: 447
03:54:48 ijk: +6 van 6 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=133 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:54:52 ijk-diagnose: nieuwste migratie -0.3 min oud | migraties 15/60/240 min: 13/42/159 | al gemeten: 453
04:50:02 ijk: +6 van 7 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=140 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
04:50:02 ijk-diagnose: nieuwste migratie 3.3 min oud | migraties 15/60/240 min: 7/42/162 | al gemeten: 474
04:54:54 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=143 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
04:54:54 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 477
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
