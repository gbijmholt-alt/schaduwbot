# Schaduwbot status

- tijd: 2026-09-15 03:59:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 14 hours, 12 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 7.0G/38G | geheugen: 2279/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.4, "uptime_s": 163506, "tokens_in_memory": 8492, "msgs": 24928658, "trades": 4978262, "creates": 53373, "decode_fail": 426012, "rpc_calls": 141555, "rpc_errors": 13, "sol_usd": 101.50665400718917, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 03:35:25 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 03:35:25 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 03:35:25 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 03:35:25 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 03:35:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:35:26,588 main INFO screen flm pass=0 dev=0.0 ins=34.13 pro=42 1a=False 1b=False 2=True (125.5s)
Sep 15 03:35:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:35:33,881 main INFO screen KANYEVEST pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (118.5s)
Sep 15 03:35:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:35:36,381 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (108.7s)
Sep 15 03:36:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:36:40,299 main INFO screen fuelcoin pass=0 dev=0.0 ins=16.68 pro=32 1a=False 1b=False 2=True (73.7s)
Sep 15 03:36:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:36:40,819 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 15 03:36:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:36:44,599 main INFO screen SPOON pass=0 dev=0.0 ins=48.99 pro=38 1a=False 1b=False 2=True (68.2s)
Sep 15 03:37:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:37:51,872 main INFO screen Tusk pass=0 dev=0.0 ins=33.85 pro=70 1a=False 1b=False 2=True (71.6s)
Sep 15 03:37:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:37:53,389 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.6s)
Sep 15 03:37:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:37:56,617 main INFO screen MEGANFOX pass=0 dev=0.0 ins=22.33 pro=64 1a=False 1b=False 2=False (72.0s)
Sep 15 03:39:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:39:03,981 main INFO screen TOELY pass=0 dev=0.0 ins=27.42 pro=69 1a=False 1b=False 2=True (72.1s)
Sep 15 03:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:39:08,548 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.2s)
Sep 15 03:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:39:08,605 main INFO screen time pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.0s)
Sep 15 03:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:39:08,764 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:39:08 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:40:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:40:18,878 main INFO screen DISNEY pass=0 dev=0.0 ins=88.3 pro=0 1a=False 1b=False 2=True (70.3s)
Sep 15 03:40:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:40:20,864 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.3s)
Sep 15 03:40:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:40:22,551 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (78.6s)
Sep 15 03:41:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:41:22,373 main INFO screen brongains pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (63.5s)
Sep 15 03:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:41:30,515 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (69.6s)
Sep 15 03:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:41:30,663 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.1s)
Sep 15 03:42:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:42:14,374 main INFO screen icecube pass=0 dev=0.0 ins=23.45 pro=38 1a=False 1b=False 2=True (52.0s)
Sep 15 03:42:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:42:30,445 main INFO screen QUEST pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (59.9s)
Sep 15 03:42:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:42:33,952 main INFO screen criptoe pass=0 dev=0.0 ins=26.96 pro=55 1a=False 1b=False 2=True (63.3s)
Sep 15 03:43:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:43:05,642 main INFO screen Melon pass=0 dev=0.0 ins=5.44 pro=69 1a=False 1b=False 2=True (51.3s)
Sep 15 03:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:43:37,207 main INFO screen Cuck pass=0 dev=0.0 ins=29.39 pro=67 1a=False 1b=False 2=True (63.3s)
Sep 15 03:43:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:43:38,658 main INFO screen Scented pass=0 dev=0.0 ins=34.8 pro=65 1a=False 1b=False 2=True (68.2s)
Sep 15 03:44:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:44:02,358 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.7s)
Sep 15 03:44:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:44:10,719 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:44:10 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:44:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:44:30,944 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 15 03:44:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:44:39,898 main INFO screen kraken pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (61.2s)
Sep 15 03:44:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:44:52,021 main INFO screen BTC pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (49.7s)
Sep 15 03:45:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:45:21,298 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.4s)
Sep 15 03:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:45:31,222 main INFO screen COCW pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.3s)
Sep 15 03:45:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:45:42,724 main INFO screen jdvans pass=0 dev=0.0 ins=16.68 pro=57 1a=False 1b=False 2=False (50.7s)
Sep 15 03:46:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:46:09,965 main INFO screen Tesla pass=0 dev=0.0 ins=178.16 pro=0 1a=False 1b=False 2=True (48.7s)
Sep 15 03:46:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:46:29,139 main INFO screen criptoe pass=0 dev=0.0 ins=9.55 pro=73 1a=False 1b=False 2=True (57.9s)
Sep 15 03:46:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:46:49,573 main INFO screen Wick pass=0 dev=0.0 ins=29.36 pro=61 1a=False 1b=False 2=True (66.8s)
Sep 15 03:47:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:47:19,097 main INFO screen PVECAT pass=0 dev=0.02 ins=17.58 pro=57 1a=False 1b=False 2=False (69.1s)
Sep 15 03:47:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:47:26,688 main INFO screen UNPAID pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.5s)
Sep 15 03:47:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:47:47,058 main INFO screen PVE pass=0 dev=3.65 ins=110.03 pro=1 1a=False 1b=False 2=True (57.5s)
Sep 15 03:48:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:48:17,034 main INFO screen Megan pass=0 dev=0.0 ins=4.38 pro=30 1a=False 1b=False 2=False (57.9s)
Sep 15 03:48:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:48:20,282 main INFO screen USGR pass=0 dev=3.97 ins=172.52 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 15 03:48:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:48:46,651 main INFO screen SPEARS pass=0 dev=0.0 ins=31.86 pro=50 1a=False 1b=False 2=True (59.6s)
Sep 15 03:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:49:13,685 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:49:13 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 03:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:49:33,631 main INFO screen THREAD pass=0 dev=0.0 ins=25.81 pro=59 1a=False 1b=False 2=True (76.6s)
Sep 15 03:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:49:33,910 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (73.6s)
Sep 15 03:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:49:59,852 main INFO screen jackSON pass=0 dev=0.0 ins=12.47 pro=43 1a=False 1b=False 2=False (73.2s)
Sep 15 03:50:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:50:44,741 main INFO screen PEPEROYAL pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (70.8s)
Sep 15 03:50:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:50:45,155 main INFO screen JACKCHAIN pass=0 dev=0.0 ins=0.99 pro=63 1a=False 1b=False 2=False (71.5s)
Sep 15 03:50:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:50:54,124 main INFO screen CATE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (54.3s)
Sep 15 03:51:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:51:50,015 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.9s)
Sep 15 03:51:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:51:52,941 main INFO screen BLUNT pass=0 dev=0.0 ins=7.29 pro=71 1a=False 1b=False 2=False (68.2s)
Sep 15 03:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:51:58,343 main INFO screen SOL pass=0 dev=0.0 ins=9.55 pro=60 1a=False 1b=False 2=False (64.2s)
Sep 15 03:52:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:52:44,187 main INFO screen DECLINED pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (54.2s)
Sep 15 03:52:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:52:54,731 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.8s)
Sep 15 03:52:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:52:56,181 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.8s)
Sep 15 03:53:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:53:36,954 main INFO screen ha pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.8s)
Sep 15 03:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:53:47,055 main INFO screen Noiz pass=0 dev=1.9 ins=117.83 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 15 03:53:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:53:49,412 main INFO screen PEPEK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.2s)
Sep 15 03:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:13,673 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:54:13 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:54:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:41,333 main INFO screen Ape pass=0 dev=0.59 ins=35.9 pro=64 1a=False 1b=False 2=True (64.4s)
Sep 15 03:54:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:47,276 main INFO screen fomo pass=0 dev=0.0 ins=153.84 pro=0 1a=False 1b=False 2=True (57.9s)
Sep 15 03:54:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:50,809 main INFO screen Breadguy pass=0 dev=0.0 ins=29.28 pro=53 1a=False 1b=False 2=True (63.8s)
Sep 15 03:55:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:51,494 main INFO screen COTE pass=0 dev=0.87 ins=233.52 pro=1 1a=False 1b=False 2=True (64.2s)
Sep 15 03:55:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:52,006 main INFO screen DANCE pass=0 dev=0.6 ins=0.0 pro=7 1a=False 1b=False 2=False (70.7s)
Sep 15 03:55:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:54,538 main INFO screen Snoop Doge pass=0 dev=0.07 ins=0.0 pro=5 1a=False 1b=False 2=False (63.7s)
Sep 15 03:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:26,781 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:26 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,857 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "POST /mcp HTTP/1.1" 404 174 "-" "python-httpx/0.28.1"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,883 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "GET /sse HTTP/1.1" 404 174 "-" "python-httpx/0.28.1"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,947 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 03:57:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:08,277 main INFO screen Lanaroads pass=0 dev=0.0 ins=5.72 pro=55 1a=False 1b=False 2=False (76.8s)
Sep 15 03:57:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:11,481 main INFO screen bag pass=0 dev=0.0 ins=29.44 pro=75 1a=False 1b=False 2=True (79.5s)
Sep 15 03:57:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:11,726 main INFO screen MHRD pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=True (77.2s)
Sep 15 03:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:18,365 main INFO screen Cented pass=0 dev=0.0 ins=28.69 pro=11 1a=False 1b=False 2=True (66.9s)
Sep 15 03:58:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:19,261 main INFO screen RCHAT pass=0 dev=0.0 ins=12.09 pro=46 1a=False 1b=True 2=False (71.0s)
Sep 15 03:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:20,577 main INFO screen WIGGABUTT pass=0 dev=0.0 ins=0.0 pro=67 1a=False 1b=False 2=False (68.9s)
Sep 15 03:59:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:59:14,351 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:59:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T02:32:12Z
--- update 2026-09-15T02:37:36Z
--- update 2026-09-15T02:42:48Z
--- update 2026-09-15T02:48:18Z
--- update 2026-09-15T02:53:20Z
--- update 2026-09-15T02:58:21Z
--- update 2026-09-15T03:03:23Z
--- update 2026-09-15T03:08:36Z
--- update 2026-09-15T03:13:43Z
--- update 2026-09-15T03:18:46Z
--- update 2026-09-15T03:23:46Z
--- update 2026-09-15T03:29:04Z
--- update 2026-09-15T03:34:05Z
--- update 2026-09-15T03:39:07Z
--- update 2026-09-15T03:44:09Z
--- update 2026-09-15T03:49:12Z
--- update 2026-09-15T03:54:12Z
Running as unit: schaduwbot-wallets.service; invocation ID: c556852febb7497c926f7c233c44f1d1
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T03:59:12Z
```

## Analyses (laatste 25 regels)
```
active
02:37:24   52000 tokens, 4998695 trades, 600377 posities (361s)
02:37:39   54000 tokens, 5185471 trades, 621613 posities (375s)
02:37:55   56000 tokens, 5369938 trades, 647871 posities (391s)
02:38:09   58000 tokens, 5548035 trades, 669634 posities (406s)
02:38:24   60000 tokens, 5729093 trades, 691244 posities (420s)
02:38:39   62000 tokens, 5928987 trades, 715455 posities (436s)
02:38:55   64000 tokens, 6127099 trades, 744134 posities (451s)
02:39:11   66000 tokens, 6324136 trades, 768998 posities (467s)
02:39:27   68000 tokens, 6521044 trades, 794258 posities (483s)
02:39:43   70000 tokens, 6709770 trades, 817423 posities (499s)
02:39:58   72000 tokens, 6901181 trades, 840177 posities (514s)
02:40:16   74000 tokens, 7111581 trades, 876955 posities (532s)
02:40:26 posities: 888948 uit 7226958 trades (548s)
02:40:38 209899 wallets gerekend
02:40:39 geluk-toets
02:41:13 persistentie
02:41:16 kopieer-simulatie
02:43:47 klaar in 749s -> /opt/schaduwbot/reports/wallets.md
03:54:13 101653 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
03:54:38   ingelezen tot rowid 10515765 (200000 rijen, 200000 bruikbaar)
03:54:40   ingelezen tot rowid 10534037 (218272 rijen, 218272 bruikbaar)
03:54:42 ingelezen: 218272 nieuwe trades, 218272 bruikbaar (29s)
03:57:47 3000 aankopen van gevolgde wallets geëvalueerd
03:58:20 vroege kopers: 278 voldoen nu, register 491, 311 tokens beoordeeld
03:58:55 grote spelers: saldo van 490 wallets opgehaald
```

## IJking poolkoers (laatste 12 regels)
```
03:29:10 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=118 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:29:10 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 9/38/154 | al gemeten: 436
03:34:11 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=120 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:34:11 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 7/37/155 | al gemeten: 438
03:39:20 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=124 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:39:20 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 8/37/155 | al gemeten: 442
03:44:15 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=126 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:44:15 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 8/36/155 | al gemeten: 444
03:49:22 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=129 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:49:22 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 10/37/155 | al gemeten: 447
03:54:48 ijk: +6 van 6 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=133 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:54:52 ijk-diagnose: nieuwste migratie -0.3 min oud | migraties 15/60/240 min: 13/42/159 | al gemeten: 453
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
