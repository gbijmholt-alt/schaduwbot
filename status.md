# Schaduwbot status

- tijd: 2026-09-14 17:58:54 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 4 hours, 11 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.0G/38G | geheugen: 1934/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 127487, "tokens_in_memory": 8283, "msgs": 17014026, "trades": 3607436, "creates": 37392, "decode_fail": 312040, "rpc_calls": 106178, "rpc_errors": 7, "sol_usd": 103.1035022571464, "open_positions": 98, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 17:35:20 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 17:35:20 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 17:35:20 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 17:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:35:28,570 main INFO screen NUT pass=0 dev=0.0 ins=43.65 pro=45 1a=False 1b=False 2=True (113.3s)
Sep 14 17:35:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:35:30,056 main INFO screen JERK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (113.3s)
Sep 14 17:36:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:36:07,948 main INFO screen PEPEFU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (106.8s)
Sep 14 17:36:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:36:32,675 main INFO screen Z500 pass=0 dev=0.0 ins=14.51 pro=21 1a=False 1b=False 2=True (64.1s)
Sep 14 17:36:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:36:33,305 main INFO screen AI pass=0 dev=0.0 ins=12.64 pro=72 1a=False 1b=False 2=True (63.2s)
Sep 14 17:37:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:37:11,177 main INFO screen ELON pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (63.2s)
Sep 14 17:37:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:37:31,638 main INFO screen NIGGA pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (59.0s)
Sep 14 17:37:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:37:46,091 main INFO screen NIGGA pass=0 dev=0.0 ins=15.02 pro=75 1a=False 1b=False 2=True (72.8s)
Sep 14 17:38:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:38:04,822 main INFO screen NIGGA pass=0 dev=0.0 ins=8.49 pro=16 1a=False 1b=False 2=False (53.6s)
Sep 14 17:38:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:38:35,858 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:38:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:38:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:38:39,367 main INFO screen NIGGA pass=0 dev=0.0 ins=12.49 pro=8 1a=False 1b=False 2=False (53.3s)
Sep 14 17:38:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:38:45,729 main INFO screen SORT pass=0 dev=0.0 ins=0.11 pro=2 1a=False 1b=False 2=True (74.1s)
Sep 14 17:39:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:39:00,619 main INFO screen NIGGA pass=0 dev=0.0 ins=12.54 pro=27 1a=False 1b=False 2=True (55.8s)
Sep 14 17:39:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:39:33,027 main INFO screen MIC pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=False (53.7s)
Sep 14 17:39:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:39:43,205 main INFO screen NIGGA pass=0 dev=0.0 ins=9.15 pro=5 1a=False 1b=False 2=False (57.5s)
Sep 14 17:40:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:40:03,379 main INFO screen PSTR pass=0 dev=0.0 ins=19.33 pro=52 1a=False 1b=False 2=True (62.8s)
Sep 14 17:40:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:40:27,298 main INFO screen venuscoin pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (54.3s)
Sep 14 17:40:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:40:50,434 main INFO screen BASKAT pass=1 dev=0.0 ins=12.29 pro=81 1a=False 1b=False 2=False (67.2s)
Sep 14 17:41:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:41:13,367 main INFO screen LPG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (70.0s)
Sep 14 17:41:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:41:22,632 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.3s)
Sep 14 17:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:41:51,358 main INFO screen basket pass=0 dev=0.0 ins=20.9 pro=45 1a=False 1b=False 2=True (60.9s)
Sep 14 17:42:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:42:00,231 main INFO screen TRUMP pass=0 dev=0.0 ins=30.11 pro=18 1a=False 1b=False 2=True (46.9s)
Sep 14 17:42:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:42:20,720 main INFO screen Bananaut pass=0 dev=0.0 ins=19.77 pro=10 1a=False 1b=False 2=True (58.1s)
Sep 14 17:42:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:42:45,192 main INFO screen Z500 pass=0 dev=0.0 ins=13.88 pro=7 1a=False 1b=False 2=False (53.8s)
Sep 14 17:42:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:42:53,498 main INFO screen PEG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.3s)
Sep 14 17:43:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:43:13,862 main INFO screen PSOL pass=0 dev=1.41 ins=8.05 pro=54 1a=False 1b=True 2=False (53.1s)
Sep 14 17:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:43:37,360 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:43:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:43:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:43:50,123 main INFO screen RWA pass=0 dev=0.0 ins=47.92 pro=41 1a=False 1b=False 2=True (64.9s)
Sep 14 17:43:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:43:56,489 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 14 17:44:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:44:04,262 main INFO screen PUMPFOLIO pass=0 dev=0.0 ins=4.78 pro=19 1a=False 1b=False 2=True (50.4s)
Sep 14 17:44:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:44:41,696 main INFO screen meganfox pass=0 dev=0.0 ins=79.24 pro=4 1a=False 1b=True 2=True (51.6s)
Sep 14 17:44:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:44:49,513 main INFO screen Claude pass=0 dev=0.08 ins=125.53 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 14 17:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:45:12,590 main INFO screen PUMPFOLIO pass=0 dev=0.0 ins=17.79 pro=56 1a=False 1b=False 2=True (68.3s)
Sep 14 17:45:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:45:35,685 main INFO screen Gemini AI pass=0 dev=0.39 ins=78.92 pro=1 1a=False 1b=False 2=True (54.0s)
Sep 14 17:45:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:45:42,855 main INFO screen NEIL pass=0 dev=0.0 ins=19.0 pro=6 1a=False 1b=False 2=False (53.3s)
Sep 14 17:46:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:46:03,637 main INFO screen PVE pass=0 dev=0.0 ins=17.82 pro=24 1a=False 1b=False 2=True (51.0s)
Sep 14 17:46:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:46:25,521 main INFO screen IBM pass=0 dev=0.0 ins=15.94 pro=21 1a=False 1b=False 2=True (49.8s)
Sep 14 17:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:46:35,203 main INFO screen moonstock pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (52.3s)
Sep 14 17:46:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:46:56,201 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.6s)
Sep 14 17:47:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:47:18,934 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.4s)
Sep 14 17:47:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:47:24,915 main INFO screen CUPSEY pass=0 dev=0.0 ins=49.19 pro=24 1a=False 1b=False 2=True (49.7s)
Sep 14 17:47:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:47:59,503 main INFO screen Muck pass=0 dev=0.0 ins=1.65 pro=62 1a=False 1b=False 2=False (63.3s)
Sep 14 17:48:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:48:09,223 main INFO screen VPN pass=0 dev=0.0 ins=18.42 pro=15 1a=False 1b=False 2=True (50.3s)
Sep 14 17:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:48:18,557 main INFO screen OAIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 14 17:48:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:48:40,146 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:48:40 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 17:48:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:48:52,211 main INFO screen QUVO pass=0 dev=0.0 ins=19.47 pro=4 1a=False 1b=False 2=False (52.7s)
Sep 14 17:49:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:49:17,128 main INFO screen COOKEDCAT pass=0 dev=0.0 ins=32.69 pro=73 1a=False 1b=False 2=True (67.9s)
Sep 14 17:49:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:49:24,333 main INFO screen GULPCAT pass=0 dev=0.0 ins=34.96 pro=79 1a=False 1b=False 2=True (65.8s)
Sep 14 17:50:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:00,910 main INFO screen GULP pass=0 dev=0.0 ins=31.14 pro=42 1a=False 1b=False 2=True (68.7s)
Sep 14 17:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:07,789 main INFO screen TOMI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.7s)
Sep 14 17:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:26,913 main INFO screen COOKED pass=0 dev=0.0 ins=20.81 pro=4 1a=False 1b=False 2=True (62.6s)
Sep 14 17:51:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:06,171 main INFO screen COOKED pass=0 dev=0.0 ins=21.38 pro=5 1a=False 1b=False 2=True (65.3s)
Sep 14 17:51:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:10,576 main INFO screen HOE pass=1 dev=0.0 ins=0.0 pro=52 1a=False 1b=False 2=False (62.8s)
Sep 14 17:51:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:27,248 main INFO screen UH OH pass=0 dev=0.0 ins=18.03 pro=5 1a=False 1b=False 2=True (60.3s)
Sep 14 17:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:58,086 main INFO screen POKEBALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.9s)
Sep 14 17:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:52:04,664 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.1s)
Sep 14 17:52:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:52:18,254 main INFO screen POKEBALL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (51.0s)
Sep 14 17:53:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:06,451 main INFO screen VANS pass=0 dev=0.0 ins=11.0 pro=48 1a=False 1b=False 2=True (68.4s)
Sep 14 17:53:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:07,961 main INFO screen NABU  pass=0 dev=0.02 ins=0.0 pro=5 1a=False 1b=False 2=False (63.3s)
Sep 14 17:53:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:27,593 main INFO screen PEDALON pass=0 dev=0.0 ins=40.69 pro=61 1a=False 1b=False 2=True (69.3s)
Sep 14 17:53:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:43,825 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:53:43 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:54:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:15,654 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.2s)
Sep 14 17:54:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:17,272 main INFO screen BRAIN pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (69.3s)
Sep 14 17:54:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:22,832 main INFO screen BIKEUNC pass=0 dev=0.0 ins=78.96 pro=5 1a=False 1b=True 2=True (55.2s)
Sep 14 17:55:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:21,430 main INFO screen BASKET pass=1 dev=0.0 ins=16.87 pro=18 1a=False 1b=False 2=False (64.2s)
Sep 14 17:55:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:23,337 main INFO screen DUMB pass=0 dev=0.0 ins=15.21 pro=25 1a=False 1b=False 2=True (60.5s)
Sep 14 17:55:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:23,728 main INFO screen MEME1921 pass=0 dev=0.0 ins=1.32 pro=28 1a=False 1b=False 2=False (68.1s)
Sep 14 17:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:35,332 main INFO screen HAIRLINES pass=0 dev=0.0 ins=34.96 pro=16 1a=False 1b=False 2=True (71.6s)
Sep 14 17:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:38,225 aiohttp.access INFO 94.154.43.223 [14/Sep/2026:17:56:38 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 17:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:39,603 main INFO screen WT pass=1 dev=0.0 ins=0.21 pro=13 1a=False 1b=False 2=False (78.2s)
Sep 14 17:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:39,660 main INFO screen cooked pass=1 dev=0.0 ins=10.41 pro=40 1a=False 1b=False 2=False (76.3s)
Sep 14 17:57:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:42,698 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.0s)
Sep 14 17:57:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:54,899 main INFO screen PURRNACE pass=0 dev=0.0 ins=77.57 pro=0 1a=False 1b=False 2=True (75.3s)
Sep 14 17:57:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:56,327 main INFO screen FATPANDA pass=1 dev=0.0 ins=19.78 pro=28 1a=False 1b=False 2=False (81.0s)
Sep 14 17:58:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:46,571 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.9s)
Sep 14 17:58:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:51,432 main INFO screen Pp AI pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 14 17:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:54,960 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:58:54 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T16:30:36Z
--- update 2026-09-14T16:36:15Z
--- update 2026-09-14T16:41:21Z
--- update 2026-09-14T16:46:36Z
--- update 2026-09-14T16:52:04Z
--- update 2026-09-14T16:57:04Z
--- update 2026-09-14T17:02:05Z
--- update 2026-09-14T17:07:34Z
--- update 2026-09-14T17:12:36Z
--- update 2026-09-14T17:17:39Z
--- update 2026-09-14T17:22:47Z
--- update 2026-09-14T17:28:07Z
--- update 2026-09-14T17:33:20Z
--- update 2026-09-14T17:38:34Z
--- update 2026-09-14T17:43:36Z
--- update 2026-09-14T17:48:39Z
--- update 2026-09-14T17:53:42Z
--- update 2026-09-14T17:58:53Z
Running as unit: schaduwbot-wallets.service; invocation ID: 9f16fe299e444a8da42e4530eb930f0d
analyses gestart (61d1b06b5cec)
```

## Analyses (laatste 25 regels)
```
active
16:33:38   34000 tokens, 3432567 trades, 425634 posities (227s)
16:33:53   36000 tokens, 3644007 trades, 450026 posities (242s)
16:34:08   38000 tokens, 3848659 trades, 478377 posities (256s)
16:34:22   40000 tokens, 4046955 trades, 500997 posities (271s)
16:34:35   42000 tokens, 4222952 trades, 519780 posities (283s)
16:34:47   44000 tokens, 4418580 trades, 544143 posities (295s)
16:34:58   46000 tokens, 4610884 trades, 567679 posities (307s)
16:35:10   48000 tokens, 4822586 trades, 593054 posities (319s)
16:35:22   50000 tokens, 5034610 trades, 619442 posities (330s)
16:35:33   52000 tokens, 5213503 trades, 638616 posities (341s)
16:35:45   54000 tokens, 5392064 trades, 660041 posities (353s)
16:35:58   56000 tokens, 5596181 trades, 686230 posities (366s)
16:36:09   58000 tokens, 5774359 trades, 706776 posities (378s)
16:36:23   60000 tokens, 6000078 trades, 737951 posities (392s)
16:36:36   62000 tokens, 6182781 trades, 763126 posities (404s)
16:36:50   64000 tokens, 6399806 trades, 792698 posities (419s)
16:37:03   66000 tokens, 6596383 trades, 817546 posities (432s)
16:37:16   68000 tokens, 6798262 trades, 845064 posities (445s)
16:37:30   70000 tokens, 7001931 trades, 881382 posities (458s)
16:37:40 posities: 900358 uit 7154599 trades (470s)
16:37:52 200540 wallets gerekend
16:37:52 geluk-toets
16:38:27 persistentie
16:38:29 kopieer-simulatie
16:40:34 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
17:02:06 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:07:34 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:12:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:17:40 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:22:48 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:28:07 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:33:20 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:38:35 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:43:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:48:39 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:53:43 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:58:54 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
