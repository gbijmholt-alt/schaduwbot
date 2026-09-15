# Schaduwbot status

- tijd: 2026-09-15 09:39:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 19 hours, 52 minutes
- bot-service: active
- code-versie: 1146874
- schijf: 7.0G/38G | geheugen: 3584/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 183930, "tokens_in_memory": 6012, "msgs": 26951545, "trades": 5515846, "creates": 58953, "decode_fail": 461233, "rpc_calls": 162020, "rpc_errors": 14, "sol_usd": 100.74280777846008, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 09:16:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:16:39,865 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (77.7s)
Sep 15 09:16:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:16:42,528 main INFO screen SOLY pass=0 dev=0.0 ins=29.14 pro=61 1a=False 1b=False 2=True (67.2s)
Sep 15 09:16:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:16:45,067 main INFO screen Max pass=0 dev=0.0 ins=18.57 pro=41 1a=False 1b=False 2=False (70.1s)
Sep 15 09:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:17:40,261 main INFO screen kimchi pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.7s)
Sep 15 09:17:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:17:42,768 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (62.9s)
Sep 15 09:17:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:17:53,452 main INFO screen $ROCKET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 15 09:18:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:18:44,407 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:18:44 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 09:18:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:18:52,272 main INFO screen kimchi pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.5s)
Sep 15 09:18:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:18:53,944 main INFO screen ISG pass=0 dev=0.0 ins=19.24 pro=49 1a=False 1b=False 2=False (73.7s)
Sep 15 09:18:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:18:55,475 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (62.0s)
Sep 15 09:19:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:19:56,581 main INFO screen Supercycle pass=0 dev=0.0 ins=24.52 pro=40 1a=False 1b=False 2=True (61.1s)
Sep 15 09:20:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:20:08,331 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (74.4s)
Sep 15 09:20:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:20:09,240 main INFO screen POOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (77.0s)
Sep 15 09:21:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:21:00,034 main INFO screen $RISKCOIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.4s)
Sep 15 09:21:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:21:08,310 main INFO screen 34% pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (59.1s)
Sep 15 09:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:21:10,874 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.5s)
Sep 15 09:22:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:22:09,063 main INFO screen SOL pass=0 dev=0.0 ins=14.64 pro=69 1a=False 1b=False 2=True (69.0s)
Sep 15 09:22:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:22:19,592 main INFO screen Q50 pass=0 dev=0.0 ins=15.04 pro=62 1a=False 1b=False 2=False (71.3s)
Sep 15 09:22:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:22:23,147 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.3s)
Sep 15 09:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:23:17,366 main INFO screen Millie pass=0 dev=0.0 ins=30.43 pro=65 1a=False 1b=False 2=True (68.3s)
Sep 15 09:23:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:23:30,185 main INFO screen Dumocrat pass=0 dev=0.0 ins=23.99 pro=67 1a=False 1b=False 2=True (67.0s)
Sep 15 09:23:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:23:30,804 main INFO screen STARFALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.2s)
Sep 15 09:24:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:24:10,111 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:24:10 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 09:24:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:24:16,142 main INFO screen PETE pass=0 dev=0.0 ins=20.94 pro=34 1a=False 1b=False 2=False (58.8s)
Sep 15 09:24:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:24:37,536 main INFO screen Shark pass=0 dev=0.0 ins=19.04 pro=42 1a=False 1b=False 2=True (67.3s)
Sep 15 09:24:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:24:38,476 main INFO screen CLARITYN pass=0 dev=0.0 ins=14.44 pro=38 1a=False 1b=False 2=False (67.7s)
Sep 15 09:25:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:25:14,690 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 15 09:25:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:25:33,472 main INFO screen CRACK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.9s)
Sep 15 09:25:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:25:38,086 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.6s)
Sep 15 09:26:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:26:13,911 main INFO screen Mayhem pass=0 dev=0.02 ins=0.0 pro=6 1a=False 1b=False 2=False (59.2s)
Sep 15 09:26:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:26:27,767 main INFO screen $MIZO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 15 09:26:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:26:32,713 main INFO screen PANDA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.6s)
Sep 15 09:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:27:00,695 main INFO screen CODEBARA pass=0 dev=0.0 ins=15.1 pro=42 1a=False 1b=False 2=True (46.8s)
Sep 15 09:27:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:27:37,386 main INFO screen FOREVER pass=0 dev=0.0 ins=26.0 pro=32 1a=False 1b=False 2=True (69.6s)
Sep 15 09:27:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:27:40,236 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (67.5s)
Sep 15 09:28:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:28:11,047 main INFO screen BSC pass=0 dev=0.0 ins=32.31 pro=61 1a=False 1b=False 2=True (70.4s)
Sep 15 09:28:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:28:39,481 main INFO screen bikehuh pass=0 dev=0.0 ins=78.91 pro=3 1a=False 1b=True 2=True (62.1s)
Sep 15 09:28:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:28:40,628 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (60.4s)
Sep 15 09:29:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:29:16,966 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:29:16 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 09:29:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:29:20,204 main INFO screen COIN pass=0 dev=2.9 ins=0.0 pro=4 1a=False 1b=False 2=False (69.2s)
Sep 15 09:29:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:29:38,153 main INFO screen fomobros pass=0 dev=0.0 ins=79.16 pro=4 1a=False 1b=True 2=True (57.5s)
Sep 15 09:29:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:29:38,805 main INFO screen high pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.3s)
Sep 15 09:30:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:30:19,563 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.4s)
Sep 15 09:30:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:30:31,432 main INFO screen Meowero2 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 15 09:30:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:30:38,684 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.9s)
Sep 15 09:31:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:31:18,302 main INFO screen WHOOPTY pass=0 dev=0.0 ins=31.76 pro=40 1a=False 1b=False 2=True (58.7s)
Sep 15 09:31:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:31:29,489 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (58.1s)
Sep 15 09:31:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:31:34,126 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.4s)
Sep 15 09:32:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:32:16,724 main INFO screen $WAR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.4s)
Sep 15 09:32:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:32:25,223 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.02 pro=4 1a=False 1b=False 2=False (55.7s)
Sep 15 09:32:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:32:29,569 main INFO screen MEOWERO1 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.4s)
Sep 15 09:33:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:33:14,177 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (57.5s)
Sep 15 09:33:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:33:32,568 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.3s)
Sep 15 09:33:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:33:45,700 main INFO screen werld pass=0 dev=0.0 ins=20.54 pro=25 1a=False 1b=False 2=True (76.1s)
Sep 15 09:34:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:34:18,122 main INFO screen Dogcoin pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=True 2=True (63.9s)
Sep 15 09:34:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:34:27,683 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:34:27 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:35:30,830 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 09:35:30 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 09:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:35:37,071 main INFO screen MONEY pass=0 dev=1.45 ins=0.0 pro=2 1a=False 1b=False 2=False (124.5s)
Sep 15 09:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:35:38,370 main INFO screen MaY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (112.7s)
Sep 15 09:36:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:36:02,580 main INFO screen .family pass=0 dev=0.0 ins=10.76 pro=54 1a=False 1b=False 2=False (104.5s)
Sep 15 09:36:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:36:43,686 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.6s)
Sep 15 09:36:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:36:43,909 main INFO screen BHS pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (65.5s)
Sep 15 09:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:37:06,448 main INFO screen WAGMI pass=0 dev=0.0 ins=17.46 pro=69 1a=False 1b=False 2=True (63.9s)
Sep 15 09:37:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:37:40,955 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (57.3s)
Sep 15 09:37:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:37:42,450 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.5s)
Sep 15 09:38:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:38:09,162 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (62.7s)
Sep 15 09:38:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:38:47,596 main INFO screen Jeetless pass=0 dev=0.0 ins=34.32 pro=60 1a=False 1b=False 2=True (66.6s)
Sep 15 09:38:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:38:49,928 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.5s)
Sep 15 09:38:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:38:59,590 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (50.4s)
Sep 15 09:39:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:39:37,765 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:39:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: 03656c3
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T08:41:07Z
Running as unit: schaduwbot-wallets.service; invocation ID: fbbefad4940a4854a92f58face2550ce
analyses gestart (f5eb6a3d8915)
--- update 2026-09-15T08:46:36Z
--- update 2026-09-15T08:52:13Z
nieuwe code: 6952951
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T08:57:36Z
--- update 2026-09-15T09:03:03Z
--- update 2026-09-15T09:08:20Z
--- update 2026-09-15T09:13:36Z
--- update 2026-09-15T09:18:43Z
--- update 2026-09-15T09:24:08Z
--- update 2026-09-15T09:29:15Z
--- update 2026-09-15T09:34:26Z
nieuwe code: 1146874
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T09:39:36Z
```

## Analyses (laatste 40 regels)
```
active
08:35:16   74000 tokens, 7132074 trades, 882785 posities (497s)
08:35:30 posities: 905040 uit 7299848 trades (516s)
08:35:43 209933 wallets gerekend
08:35:43 geluk-toets
08:36:18 persistentie
08:36:22 kopieer-simulatie
08:38:47 klaar in 714s -> /opt/schaduwbot/reports/wallets.md
08:41:12 106376 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
08:41:25   ingelezen tot rowid 10998740 (90133 rijen, 90133 bruikbaar)
08:41:27 ingelezen: 90133 nieuwe trades, 90133 bruikbaar (20s)
08:44:45 3000 aankopen van gevolgde wallets geëvalueerd
08:45:33 vroege kopers: 297 voldoen nu, register 522, 150 tokens beoordeeld
08:46:20 grote spelers: saldo van 380 wallets opgehaald
08:46:51 herkomst: 40 posities gekoppeld
08:47:06 klaar in 359s -> /opt/schaduwbot/reports/ledger.md
09:02:17 S1: gezakt — toets n=33199, verkennend n=14656
09:02:17 klaar in 911s -> /opt/schaduwbot/reports/hypotheses.md
09:02:18 probe: 150 transacties ophalen
09:05:37 poolveld: 10 pools bekeken, 0 te gaan -> vastgesteld @43
09:07:17 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
09:07:17 prijsijk: n=224 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:07:19 na-migratie: 100 paren te checken
09:09:26 na-migratie: 35 paren, 19 prijzen
09:12:03 gemigreerde koersen: 34 gedaan, 2000 te gaan
09:12:05 klaar (585 rpc-calls, 170 fouten)
09:17:10 klaar in 304s -> /opt/schaduwbot/reports/lotgevallen.md
09:30:23   500/6654 lopers, 14233 koppelingen
09:31:09   1000/6654 lopers, 27609 koppelingen
09:31:44   1500/6654 lopers, 35674 koppelingen
09:32:28   2000/6654 lopers, 46613 koppelingen
09:33:05   2500/6654 lopers, 55002 koppelingen
09:33:34   3000/6654 lopers, 62231 koppelingen
09:34:16   3500/6654 lopers, 71433 koppelingen
09:34:44   4000/6654 lopers, 77748 koppelingen
09:35:30   4500/6654 lopers, 85514 koppelingen
09:36:11   5000/6654 lopers, 93093 koppelingen
09:36:42   5500/6654 lopers, 99227 koppelingen
09:37:54   6000/6654 lopers, 110982 koppelingen
09:38:38   6500/6654 lopers, 117630 koppelingen
09:38:44 klaar in 1294s: 6654 lopers, 39751 afgeleiden -> /opt/schaduwbot/reports/vamp.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
07:23:19 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=208 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:23:19 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/40/161 | al gemeten: 561
07:28:25 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=210 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:28:25 ijk-diagnose: nieuwste migratie 3.4 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 563
07:33:31 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=211 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:33:31 ijk-diagnose: nieuwste migratie 4.8 min oud | migraties 15/60/240 min: 6/37/159 | al gemeten: 564
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
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
