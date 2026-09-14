# Schaduwbot status

- tijd: 2026-09-14 05:52:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 16 hours, 5 minutes
- bot-service: active
- code-versie: 4c85537
- schijf: 5.5G/38G | geheugen: 1983/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 83887, "tokens_in_memory": 6118, "msgs": 11171424, "trades": 2319134, "creates": 24314, "decode_fail": 201993, "rpc_calls": 68184, "rpc_errors": 4, "sol_usd": 100.91156631972619, "open_positions": 8, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 05:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:16:33,094 main INFO screen PXL pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=True (83.9s)
Sep 14 05:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:16:53,920 main INFO screen EAGLEF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.0s)
Sep 14 05:17:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:17:09,967 main INFO screen KIBA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 14 05:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:17:52,861 main INFO screen BAAN-KUN pass=0 dev=0.0 ins=19.99 pro=66 1a=False 1b=False 2=True (79.8s)
Sep 14 05:19:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:21,414 main INFO screen dog pass=0 dev=0.0 ins=9.26 pro=57 1a=False 1b=False 2=True (69.8s)
Sep 14 05:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:22,969 main INFO screen LaMisery pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (71.8s)
Sep 14 05:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:35,614 main INFO screen FYPM pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.1s)
Sep 14 05:19:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:59,619 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:19:59 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 05:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:20:16,668 main INFO screen SCT pass=0 dev=8.16 ins=28.4 pro=17 1a=False 1b=False 2=False (55.3s)
Sep 14 05:22:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:22:49,152 main INFO screen BEER pass=0 dev=0.0 ins=37.17 pro=76 1a=False 1b=False 2=True (67.7s)
Sep 14 05:22:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:22:51,466 main INFO screen MadisonBeer pass=0 dev=0.0 ins=39.93 pro=76 1a=False 1b=False 2=True (64.2s)
Sep 14 05:23:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:23:54,668 main INFO screen flyhouse pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (57.3s)
Sep 14 05:24:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:24:48,334 main INFO screen AI pass=0 dev=0.0 ins=23.04 pro=61 1a=False 1b=False 2=True (66.8s)
Sep 14 05:24:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:24:52,350 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 14 05:25:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:25:15,762 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:25:15 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:26:04,788 main INFO screen DOXA pass=0 dev=9.0 ins=41.9 pro=26 1a=False 1b=True 2=True (55.5s)
Sep 14 05:26:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:26:25,200 main INFO screen CATESZN pass=0 dev=1.05 ins=78.26 pro=2 1a=False 1b=True 2=True (55.5s)
Sep 14 05:26:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:26:30,764 main INFO screen 奶龙 pass=0 dev=78.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
Sep 14 05:26:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:26:42,481 aiohttp.access INFO 167.172.165.251 [14/Sep/2026:05:26:42 +0000] "GET /login HTTP/1.1" 404 193 "-" "Go-http-client/1.1"
Sep 14 05:27:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:27:02,128 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.3s)
Sep 14 05:27:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:27:49,516 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 14 05:28:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:28:22,571 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 14 05:28:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:28:43,399 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (69.6s)
Sep 14 05:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:29:36,264 main INFO screen EAGLEF pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.0s)
Sep 14 05:30:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:30:03,010 main INFO screen FakeTaxi pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (71.2s)
Sep 14 05:30:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:30:07,773 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.2s)
Sep 14 05:30:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:30:37,596 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:30:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 05:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:30:48,939 main INFO screen EAGLEF pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.7s)
Sep 14 05:31:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:31:10,517 main INFO screen FakeTaxi pass=1 dev=0.0 ins=0.0 pro=29 1a=False 1b=False 2=False (67.5s)
Sep 14 05:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:32:14,163 main INFO screen . pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (53.7s)
Sep 14 05:33:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:33:32,576 main INFO screen FakeTaxi pass=1 dev=0.0 ins=0.24 pro=16 1a=False 1b=False 2=False (65.5s)
Sep 14 05:33:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:33:57,854 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:35:08,310 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 05:35:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:35:08,424 rpc WARNING rpc getSignaturesForAddress exc
Sep 14 05:35:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:35:17,321 main INFO screen FakeTaxi pass=0 dev=67.25 ins=0.0 pro=55 1a=False 1b=True 2=False (110.6s)
Sep 14 05:35:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:35:56,499 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:35:56 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:36:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:36:00,340 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.0s)
Sep 14 05:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:36:27,736 main INFO screen 245 pass=0 dev=4.11 ins=0.0 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 14 05:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:36:37,659 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.8s)
Sep 14 05:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:37:06,893 main INFO screen HUMAN pass=0 dev=1.84 ins=0.0 pro=7 1a=False 1b=False 2=False (66.3s)
Sep 14 05:37:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:37:25,812 main INFO screen PUMPDUMP pass=0 dev=0.02 ins=0.0 pro=3 1a=False 1b=False 2=False (58.1s)
Sep 14 05:38:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:38:13,425 main INFO screen tothemoon pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (70.1s)
Sep 14 05:38:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:38:14,393 main INFO screen . pass=0 dev=0.15 ins=0.0 pro=3 1a=False 1b=False 2=False (67.5s)
Sep 14 05:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:39:02,600 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.9s)
Sep 14 05:39:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:39:18,649 main INFO screen NABU pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (50.7s)
Sep 14 05:40:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:40:15,390 main INFO screen MC pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (51.0s)
Sep 14 05:41:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:41:16,977 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:41:16 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 05:41:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:41:53,371 main INFO screen PUMPCAT pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (60.3s)
Sep 14 05:42:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:42:17,033 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.8s)
Sep 14 05:42:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:42:19,933 main INFO screen woods pass=1 dev=1.34 ins=2.64 pro=50 1a=False 1b=False 2=False (68.1s)
Sep 14 05:42:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:42:44,130 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 14 05:42:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:42:51,567 aiohttp.access INFO 45.63.4.69 [14/Sep/2026:05:42:51 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CyberConvoyScout/1.0; +https://scout.cyberconvoy.co)"
Sep 14 05:44:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:44:06,787 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (61.7s)
Sep 14 05:44:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:44:12,008 main INFO screen FakeTaxi pass=0 dev=67.25 ins=0.0 pro=44 1a=False 1b=False 2=False (69.2s)
Sep 14 05:44:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:44:26,397 aiohttp.access INFO 3.129.187.38 [14/Sep/2026:05:44:26 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 14 05:44:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:44:49,263 main INFO screen Anthropic pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 14 05:45:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:45:06,071 main INFO screen REJ pass=0 dev=3.43 ins=0.0 pro=3 1a=False 1b=False 2=False (59.3s)
Sep 14 05:45:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:45:38,699 main INFO screen tothemoon pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (62.0s)
Sep 14 05:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:46:37,436 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:46:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 05:47:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:47:30,821 aiohttp.access INFO 3.129.187.38 [14/Sep/2026:05:47:30 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 14 05:48:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:48:00,118 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 14 05:48:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:48:50,169 main INFO screen BHS DOGE pass=0 dev=0.02 ins=0.0 pro=6 1a=False 1b=False 2=False (64.5s)
Sep 14 05:49:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:49:10,272 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.0s)
Sep 14 05:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:49:19,783 main INFO screen Humanity pass=0 dev=79.05 ins=0.26 pro=2 1a=False 1b=False 2=True (62.9s)
Sep 14 05:49:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:49:42,007 main INFO screen ZALIEN pass=0 dev=0.04 ins=77.78 pro=9 1a=False 1b=True 2=True (51.8s)
Sep 14 05:50:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:50:18,162 main INFO screen . pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 14 05:50:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:50:25,881 main INFO screen ZENITH pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=True (66.1s)
Sep 14 05:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:50:48,207 main INFO screen $BABYCAT pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (66.2s)
Sep 14 05:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:52:14,972 main INFO screen COZY pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.4s)
Sep 14 05:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:52:15,104 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:52:15 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T04:43:38Z
--- update 2026-09-14T04:48:49Z
--- update 2026-09-14T04:53:59Z
Running as unit: schaduwbot-wallets.service; invocation ID: f736891630a542c892110e5793ff0a8a
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T04:59:09Z
--- update 2026-09-14T05:04:31Z
--- update 2026-09-14T05:09:35Z
--- update 2026-09-14T05:14:36Z
--- update 2026-09-14T05:19:58Z
--- update 2026-09-14T05:25:14Z
--- update 2026-09-14T05:30:36Z
--- update 2026-09-14T05:35:54Z
--- update 2026-09-14T05:41:15Z
nieuwe code: 4c85537
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 50bde54a4fe34817a194febaf1a38587
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T05:46:36Z
--- update 2026-09-14T05:52:13Z
```

## Analyses (laatste 25 regels)
```
active
05:26:47   48000 tokens, 4836646 trades, 616368 posities (303s)
05:26:59   50000 tokens, 5034828 trades, 637262 posities (316s)
05:27:12   52000 tokens, 5210108 trades, 658636 posities (328s)
05:27:25   54000 tokens, 5410943 trades, 684943 posities (342s)
05:27:38   56000 tokens, 5591190 trades, 706352 posities (355s)
05:27:53   58000 tokens, 5793492 trades, 734369 posities (370s)
05:28:07   60000 tokens, 5975822 trades, 759301 posities (384s)
05:28:22   62000 tokens, 6197512 trades, 790087 posities (398s)
05:28:35   64000 tokens, 6398608 trades, 815506 posities (412s)
05:28:50   66000 tokens, 6604999 trades, 847264 posities (427s)
05:29:03   68000 tokens, 6801133 trades, 882109 posities (440s)
05:29:11 posities: 898489 uit 6928702 trades (452s)
05:29:24 194290 wallets gerekend
05:29:24 geluk-toets
05:29:59 persistentie
05:30:02 kopieer-simulatie
05:31:56 klaar in 617s -> /opt/schaduwbot/reports/wallets.md
05:41:20 72572 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
05:41:29   ingelezen tot rowid 7875753 (55635 rijen, 55635 bruikbaar)
05:41:30 ingelezen: 55635 nieuwe trades, 55635 bruikbaar (14s)
05:43:32 3000 aankopen van gevolgde wallets geëvalueerd
05:43:53 vroege kopers: 222 voldoen nu, register 383, 66 tokens beoordeeld
05:44:14 grote spelers: saldo van 11 wallets opgehaald
05:45:06 herkomst: 40 posities gekoppeld
05:45:15 klaar in 239s -> /opt/schaduwbot/reports/ledger.md
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
