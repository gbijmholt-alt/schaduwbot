# Schaduwbot status

- tijd: 2026-09-15 09:50:32 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 20 hours, 3 minutes
- bot-service: active
- code-versie: 1146874
- schijf: 7.0G/38G | geheugen: 2917/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 184584, "tokens_in_memory": 5973, "msgs": 27034300, "trades": 5534520, "creates": 59174, "decode_fail": 462273, "rpc_calls": 162693, "rpc_errors": 14, "sol_usd": 100.8571857923723, "open_positions": 52, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 09:39:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:39:58,989 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (71.4s)
Sep 15 09:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:40:00,955 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.4s)
Sep 15 09:40:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:40:01,425 main INFO screen bruh pass=0 dev=0.0 ins=1.93 pro=59 1a=False 1b=False 2=True (71.5s)
Sep 15 09:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:40:56,603 main INFO screen RPIG pass=0 dev=0.0 ins=79.24 pro=3 1a=False 1b=True 2=True (57.6s)
Sep 15 09:41:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:41:07,969 main INFO screen SpaceX pass=0 dev=0.0 ins=136.32 pro=1 1a=False 1b=False 2=True (66.5s)
Sep 15 09:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:41:11,616 main INFO screen pupper pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (70.7s)
Sep 15 09:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:41:51,212 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.6s)
Sep 15 09:42:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:42:03,660 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 09:42:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:42:07,296 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.7s)
Sep 15 09:42:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:42:54,819 main INFO screen robinsol pass=0 dev=0.0 ins=77.41 pro=9 1a=False 1b=False 2=True (51.2s)
Sep 15 09:42:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:42:56,386 main INFO screen AI pass=0 dev=0.0 ins=18.04 pro=29 1a=False 1b=False 2=True (65.2s)
Sep 15 09:43:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:43:15,658 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (68.4s)
Sep 15 09:43:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:43:50,771 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (54.4s)
Sep 15 09:43:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:43:58,779 main INFO screen QUMIS pass=0 dev=0.0 ins=13.14 pro=53 1a=False 1b=False 2=True (64.0s)
Sep 15 09:44:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:44:07,335 main INFO screen Porsche pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.7s)
Sep 15 09:44:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:44:45,294 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.5s)
Sep 15 09:45:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:45:03,928 main INFO screen WOHUHCAT pass=0 dev=0.0 ins=75.77 pro=18 1a=False 1b=False 2=True (65.1s)
Sep 15 09:45:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:45:07,911 main INFO screen SOLROCKET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.6s)
Sep 15 09:45:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:45:20,694 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:45:20 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 09:45:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:45:37,346 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.0s)
Sep 15 09:45:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:45:57,244 main INFO screen ASH pass=0 dev=0.0 ins=0.57 pro=17 1a=False 1b=False 2=False (53.3s)
Sep 15 09:46:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:46:01,194 main INFO screen Porsche pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.3s)
Sep 15 09:46:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:46:40,959 main INFO screen TGB pass=0 dev=0.0 ins=25.54 pro=68 1a=False 1b=False 2=True (63.6s)
Sep 15 09:46:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:46:44,976 main INFO screen ASH pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (47.7s)
Sep 15 09:46:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:46:50,499 main INFO screen jets  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.3s)
Sep 15 09:47:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:47:28,612 main INFO screen ASH pass=0 dev=0.0 ins=0.26 pro=18 1a=False 1b=False 2=False (47.7s)
Sep 15 09:47:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:47:31,836 main INFO screen SOLANA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (46.9s)
Sep 15 09:47:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:47:41,540 main INFO screen $BUY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.0s)
Sep 15 09:48:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:48:36,311 main INFO screen GEEKBAR pass=0 dev=0.0 ins=26.75 pro=39 1a=False 1b=False 2=True (67.7s)
Sep 15 09:48:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:48:37,774 main INFO screen POKXMR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 15 09:48:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:48:52,843 main INFO screen bling pass=0 dev=0.7 ins=0.0 pro=21 1a=False 1b=False 2=False (71.3s)
Sep 15 09:49:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:49:30,445 main INFO screen ANSEM pass=0 dev=0.0 ins=166.84 pro=0 1a=False 1b=False 2=True (54.1s)
Sep 15 09:49:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:49:32,438 main INFO screen NVDA pass=0 dev=0.0 ins=161.19 pro=1 1a=False 1b=False 2=True (54.7s)
Sep 15 09:49:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:49:46,702 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 15 09:50:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 09:50:32,652 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:09:50:32 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-15T09:45:19Z
--- update 2026-09-15T09:50:31Z
```

## Analyses (laatste 40 regels)
```
active
09:40:56   8000 tokens, 755977 trades, 89163 posities (55s)
09:41:07   10000 tokens, 943799 trades, 110527 posities (66s)
09:41:20   12000 tokens, 1149594 trades, 141016 posities (79s)
09:41:33   14000 tokens, 1353076 trades, 165919 posities (92s)
09:41:46   16000 tokens, 1545724 trades, 186698 posities (105s)
09:42:00   18000 tokens, 1744310 trades, 211096 posities (118s)
09:42:12   20000 tokens, 1930494 trades, 231267 posities (130s)
09:42:24   22000 tokens, 2117298 trades, 250847 posities (143s)
09:42:38   24000 tokens, 2339818 trades, 281298 posities (157s)
09:42:52   26000 tokens, 2553382 trades, 309360 posities (170s)
09:43:06   28000 tokens, 2742877 trades, 334422 posities (184s)
09:43:18   30000 tokens, 2923620 trades, 356460 posities (197s)
09:43:31   32000 tokens, 3122998 trades, 382161 posities (210s)
09:43:44   34000 tokens, 3306769 trades, 402614 posities (223s)
09:43:59   36000 tokens, 3493571 trades, 424580 posities (237s)
09:44:13   38000 tokens, 3697888 trades, 450391 posities (252s)
09:44:27   40000 tokens, 3900334 trades, 475051 posities (265s)
09:44:40   42000 tokens, 4082676 trades, 498480 posities (279s)
09:44:55   44000 tokens, 4267583 trades, 519384 posities (293s)
09:45:07   46000 tokens, 4445286 trades, 541079 posities (306s)
09:45:20   48000 tokens, 4625749 trades, 562677 posities (318s)
09:45:34   50000 tokens, 4813554 trades, 585505 posities (332s)
09:45:49   52000 tokens, 5034036 trades, 615083 posities (347s)
09:46:03   54000 tokens, 5222179 trades, 638754 posities (361s)
09:46:18   56000 tokens, 5420893 trades, 666757 posities (377s)
09:46:31   58000 tokens, 5587511 trades, 684159 posities (390s)
09:46:47   60000 tokens, 5783930 trades, 710882 posities (405s)
09:47:01   62000 tokens, 5973435 trades, 733938 posities (420s)
09:47:15   64000 tokens, 6172546 trades, 762658 posities (433s)
09:47:29   66000 tokens, 6368136 trades, 786022 posities (447s)
09:47:44   68000 tokens, 6558130 trades, 811760 posities (463s)
09:47:59   70000 tokens, 6738863 trades, 833010 posities (477s)
09:48:14   72000 tokens, 6940230 trades, 857491 posities (492s)
09:48:30   74000 tokens, 7140514 trades, 889117 posities (508s)
09:48:44   76000 tokens, 7316833 trades, 913068 posities (522s)
09:48:45 posities: 913473 uit 7325165 trades (529s)
09:48:58 210371 wallets gerekend
09:48:58 geluk-toets
09:49:35 persistentie
09:49:38 kopieer-simulatie
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
