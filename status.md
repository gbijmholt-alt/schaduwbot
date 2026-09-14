# Schaduwbot status

- tijd: 2026-09-14 10:05:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 20 hours, 18 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.6G/38G | geheugen: 1899/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 99073, "tokens_in_memory": 4346, "msgs": 12030754, "trades": 2638307, "creates": 27422, "decode_fail": 223439, "rpc_calls": 78209, "rpc_errors": 6, "sol_usd": 101.88472437213055, "open_positions": 46, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 09:35:18 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 09:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:35:19,033 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:35:19 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:35:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:35:24,712 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (125.2s)
Sep 14 09:35:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:35:48,048 main INFO screen spitty pass=0 dev=0.03 ins=79.27 pro=3 1a=False 1b=True 2=True (110.8s)
Sep 14 09:36:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:36:05,089 main INFO screen snoopdogg pass=0 dev=0.0 ins=53.12 pro=51 1a=False 1b=False 2=True (110.2s)
Sep 14 09:36:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:36:31,366 main INFO screen luigi pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (66.7s)
Sep 14 09:36:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:36:54,558 main INFO screen BeachBull pass=0 dev=0.0 ins=55.58 pro=14 1a=False 1b=False 2=True (66.5s)
Sep 14 09:37:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:37:01,749 main INFO screen FLYTROLL pass=0 dev=0.05 ins=79.26 pro=7 1a=False 1b=True 2=True (56.7s)
Sep 14 09:37:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:37:30,287 main INFO screen $CatB pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (58.9s)
Sep 14 09:37:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:37:47,956 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 14 09:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:38:10,009 main INFO screen luigi pass=0 dev=0.09 ins=0.0 pro=6 1a=False 1b=False 2=False (68.3s)
Sep 14 09:38:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:38:22,459 main INFO screen Pepper pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 14 09:38:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:38:59,332 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:09:38:59 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 09:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:39:02,184 main INFO screen Amazon pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.2s)
Sep 14 09:39:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:39:03,123 main INFO screen GOAT pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (75.2s)
Sep 14 09:39:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:39:30,370 main INFO screen cummies pass=0 dev=0.0 ins=25.32 pro=69 1a=False 1b=False 2=True (67.9s)
Sep 14 09:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:39:35,136 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:39:35 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:40:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:40:08,179 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.1s)
Sep 14 09:40:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:40:09,641 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.5s)
Sep 14 09:40:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:40:26,809 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 14 09:40:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:40:58,894 main INFO screen AZI pass=0 dev=0.0 ins=78.66 pro=22 1a=False 1b=True 2=True (50.7s)
Sep 14 09:41:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:41:28,029 main INFO screen CAT06 pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (67.1s)
Sep 14 09:41:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:41:39,742 main INFO screen Neocloud pass=1 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=False (67.4s)
Sep 14 09:41:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:41:50,032 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (49.2s)
Sep 14 09:42:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:42:23,753 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.7s)
Sep 14 09:43:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:43:12,460 main INFO screen LOL pass=0 dev=0.0 ins=22.72 pro=40 1a=False 1b=False 2=False (70.2s)
Sep 14 09:43:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:43:17,144 main INFO screen Supercycle pass=0 dev=0.0 ins=31.4 pro=66 1a=False 1b=False 2=True (66.4s)
Sep 14 09:43:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:43:22,898 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (56.3s)
Sep 14 09:44:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:44:24,687 main INFO screen Loom pass=0 dev=0.0 ins=21.59 pro=66 1a=False 1b=False 2=False (72.2s)
Sep 14 09:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:44:28,740 main INFO screen GOBLIN pass=0 dev=0.04 ins=0.0 pro=6 1a=False 1b=False 2=False (71.6s)
Sep 14 09:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:44:37,457 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:44:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:44:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:44:38,125 main INFO screen BABITA pass=1 dev=0.86 ins=9.27 pro=64 1a=False 1b=False 2=False (75.2s)
Sep 14 09:45:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:45:29,549 main INFO screen Bikejak pass=0 dev=0.25 ins=79.06 pro=3 1a=False 1b=True 2=True (60.8s)
Sep 14 09:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:45:33,496 main INFO screen heon pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (68.8s)
Sep 14 09:45:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:45:37,497 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 14 09:46:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:46:20,574 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.0s)
Sep 14 09:46:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:46:32,401 main INFO screen beer pass=0 dev=0.07 ins=0.0 pro=1 1a=False 1b=False 2=False (58.9s)
Sep 14 09:47:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:47:23,011 aiohttp.access INFO 64.62.156.66 [14/Sep/2026:09:47:23 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 09:47:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:47:48,859 main INFO screen 🧌 pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (49.9s)
Sep 14 09:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:48:56,650 main INFO screen JUB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.4s)
Sep 14 09:49:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:49:06,170 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.1s)
Sep 14 09:49:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:49:36,942 main INFO screen retard pass=0 dev=0.0 ins=32.56 pro=61 1a=False 1b=False 2=True (64.9s)
Sep 14 09:49:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:49:38,015 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:49:38 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:49:59,915 main INFO screen weene pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (63.3s)
Sep 14 09:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:50:46,421 main INFO screen NVDA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.1s)
Sep 14 09:51:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:51:07,500 main INFO screen moin pass=0 dev=0.0 ins=23.44 pro=46 1a=False 1b=False 2=True (65.5s)
Sep 14 09:51:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:51:08,744 main INFO screen $Cat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.3s)
Sep 14 09:51:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:51:53,750 main INFO screen . pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (67.3s)
Sep 14 09:51:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:51:59,100 main INFO screen founder pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.6s)
Sep 14 09:52:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:52:21,753 main INFO screen $SOLDUCK pass=0 dev=0.44 ins=0.0 pro=7 1a=False 1b=False 2=False (54.9s)
Sep 14 09:52:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:52:42,872 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.1s)
Sep 14 09:53:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:53:10,039 main INFO screen MARIO pass=0 dev=0.0 ins=31.68 pro=71 1a=False 1b=False 2=True (62.2s)
Sep 14 09:53:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:53:19,455 main INFO screen NVDA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (50.7s)
Sep 14 09:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:53:47,713 main INFO screen Celing pass=1 dev=4.1 ins=0.0 pro=51 1a=False 1b=False 2=False (64.8s)
Sep 14 09:54:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:54:03,642 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 14 09:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:54:28,833 main INFO screen TSLA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.0s)
Sep 14 09:54:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:54:38,445 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:54:38 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:54:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:54:48,816 main INFO screen SNIСKERS pass=0 dev=0.04 ins=77.78 pro=7 1a=False 1b=True 2=True (49.7s)
Sep 14 09:56:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:56:13,502 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.9s)
Sep 14 09:56:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:56:55,871 main INFO screen StunkGPT pass=0 dev=0.19 ins=79.12 pro=10 1a=False 1b=True 2=True (53.4s)
Sep 14 09:58:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:58:02,980 main INFO screen NVDA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.4s)
Sep 14 09:58:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:58:03,421 main INFO screen GIGAFLY pass=0 dev=0.05 ins=79.26 pro=9 1a=False 1b=True 2=True (69.8s)
Sep 14 09:58:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:58:30,174 main INFO screen disapel pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.0s)
Sep 14 09:58:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:58:55,222 main INFO screen NVDA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 14 09:59:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:59:19,017 main INFO screen RISE pass=0 dev=0.0 ins=0.51 pro=5 1a=False 1b=False 2=False (72.1s)
Sep 14 09:59:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:59:32,008 main INFO screen CHBU pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 14 09:59:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:59:42,839 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:09:59:42 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 09:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 09:59:59,561 main INFO screen rest pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.0s)
Sep 14 10:01:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:01:34,715 main INFO screen NVDA pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (58.3s)
Sep 14 10:01:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:01:48,027 main INFO screen ANSEMBATON pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=True 2=True (68.1s)
Sep 14 10:02:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:02:02,503 main INFO screen znap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 14 10:03:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:03:08,664 main INFO screen TORA pass=0 dev=0.0 ins=21.63 pro=61 1a=False 1b=False 2=True (58.7s)
Sep 14 10:04:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:04:55,141 main INFO screen ☠️ pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (79.0s)
Sep 14 10:05:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:05:20,026 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (55.6s)
Sep 14 10:05:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:05:21,516 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:10:05:21 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T08:36:08Z
--- update 2026-09-14T08:41:09Z
--- update 2026-09-14T08:46:36Z
--- update 2026-09-14T08:51:48Z
--- update 2026-09-14T08:56:53Z
--- update 2026-09-14T09:02:07Z
--- update 2026-09-14T09:07:21Z
--- update 2026-09-14T09:12:36Z
--- update 2026-09-14T09:18:23Z
--- update 2026-09-14T09:23:36Z
--- update 2026-09-14T09:28:56Z
--- update 2026-09-14T09:34:27Z
--- update 2026-09-14T09:39:33Z
--- update 2026-09-14T09:44:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 980b8aeb5eca48cf8ad4d8ca2b0c2103
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T09:49:36Z
--- update 2026-09-14T09:54:37Z
--- update 2026-09-14T09:59:41Z
--- update 2026-09-14T10:05:20Z
```

## Analyses (laatste 25 regels)
```
active
08:17:02   66000 tokens, 6573751 trades, 819478 posities (343s)
08:17:14   68000 tokens, 6767562 trades, 850720 posities (355s)
08:17:27   70000 tokens, 6978354 trades, 884198 posities (368s)
08:17:32 posities: 893588 uit 7039798 trades (377s)
08:17:46 196188 wallets gerekend
08:17:46 geluk-toets
08:18:26 persistentie
08:18:29 kopieer-simulatie
08:20:28 klaar in 553s -> /opt/schaduwbot/reports/wallets.md
09:44:37 75510 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
09:44:53   ingelezen tot rowid 8175826 (152909 rijen, 152909 bruikbaar)
09:44:54 ingelezen: 152909 nieuwe trades, 152909 bruikbaar (18s)
09:47:07 3000 aankopen van gevolgde wallets geëvalueerd
09:47:30 vroege kopers: 222 voldoen nu, register 391, 186 tokens beoordeeld
09:47:59 grote spelers: saldo van 1233 wallets opgehaald
09:48:46 herkomst: 40 posities gekoppeld
09:48:56 klaar in 260s -> /opt/schaduwbot/reports/ledger.md
09:57:24 S1: gezakt — toets n=17396, verkennend n=14656
09:57:24 klaar in 507s -> /opt/schaduwbot/reports/hypotheses.md
09:57:25 probe: 150 transacties ophalen
10:01:02 poolveld: 26 pools bekeken, 0 te gaan -> vastgesteld @43
10:02:14 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
10:02:14 prijsijk: n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:02:16 na-migratie: 100 paren te checken
10:04:33 na-migratie: 84 paren, 19 prijzen
```

## IJking poolkoers (laatste 12 regels)
```
09:54:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
Traceback (most recent call last):
  File "/opt/schaduwbot/pumpswap.py", line 1183, in <module>
    main()
    ~~~~^^
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
10:05:21 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
