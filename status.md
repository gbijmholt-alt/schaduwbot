# Schaduwbot status

- tijd: 2026-09-14 03:00:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 13 hours, 13 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.3G/38G | geheugen: 1961/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 73572, "tokens_in_memory": 7648, "msgs": 9884936, "trades": 2080264, "creates": 22078, "decode_fail": 181005, "rpc_calls": 60704, "rpc_errors": 3, "sol_usd": 100.94393378552442, "open_positions": 44, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 02:34:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:34:06,485 main INFO screen LILPUMP pass=0 dev=0.0 ins=25.96 pro=56 1a=False 1b=False 2=True (56.5s)
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:34:58,954 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 02:34:58 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 02:35:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:35:00,444 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:35:00 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:35:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:35:22,362 main INFO screen BuLL pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (112.3s)
Sep 14 02:35:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:35:32,387 main INFO screen $FEE pass=0 dev=0.83 ins=0.0 pro=7 1a=False 1b=False 2=False (108.9s)
Sep 14 02:35:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:35:58,378 main INFO screen wind pass=0 dev=29.4 ins=0.0 pro=9 1a=False 1b=False 2=False (111.9s)
Sep 14 02:36:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:36:35,349 main INFO screen Community pass=0 dev=0.0 ins=23.91 pro=55 1a=False 1b=False 2=True (73.0s)
Sep 14 02:36:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:36:46,995 main INFO screen STUPID pass=0 dev=2.96 ins=29.88 pro=43 1a=False 1b=False 2=True (74.6s)
Sep 14 02:37:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:37:00,914 main INFO screen Coinage pass=0 dev=0.0 ins=33.48 pro=31 1a=False 1b=False 2=True (62.5s)
Sep 14 02:37:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:37:27,940 main INFO screen Hunter pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.6s)
Sep 14 02:38:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:38:01,499 main INFO screen Bush pass=1 dev=0.0 ins=9.41 pro=55 1a=False 1b=False 2=False (74.5s)
Sep 14 02:38:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:38:08,927 main INFO screen Duluth pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (68.0s)
Sep 14 02:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:38:37,149 main INFO screen MDYSON pass=1 dev=1.85 ins=0.0 pro=43 1a=False 1b=False 2=False (69.2s)
Sep 14 02:39:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:39:11,308 main INFO screen MYTHOS pass=0 dev=0.0 ins=8.13 pro=71 1a=False 1b=False 2=True (69.8s)
Sep 14 02:39:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:39:12,707 main INFO screen GS pass=0 dev=0.0 ins=15.52 pro=55 1a=False 1b=False 2=True (63.8s)
Sep 14 02:39:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:39:34,785 main INFO screen squig pass=1 dev=0.0 ins=4.95 pro=12 1a=False 1b=False 2=False (57.6s)
Sep 14 02:40:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:40:07,047 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:40:07 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:40:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:40:18,602 main INFO screen FROBERT pass=0 dev=1.25 ins=0.0 pro=3 1a=False 1b=False 2=False (65.9s)
Sep 14 02:40:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:40:19,803 main INFO screen Jonathan pass=0 dev=0.0 ins=29.87 pro=48 1a=False 1b=False 2=True (68.5s)
Sep 14 02:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:40:39,495 main INFO screen KIMCHI pass=1 dev=0.0 ins=13.72 pro=67 1a=False 1b=False 2=False (64.7s)
Sep 14 02:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:41:11,166 main INFO screen SEYONGPARK pass=0 dev=0.0 ins=0.0 pro=62 1a=True 1b=False 2=True (52.6s)
Sep 14 02:41:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:41:12,578 main INFO screen Benz pass=0 dev=0.39 ins=0.0 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 14 02:41:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:41:45,406 main INFO screen AXSOLHODL pass=0 dev=0.0 ins=35.6 pro=52 1a=False 1b=False 2=True (65.9s)
Sep 14 02:42:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:42:24,862 main INFO screen Sydney pass=0 dev=0.0 ins=32.38 pro=58 1a=False 1b=False 2=True (72.3s)
Sep 14 02:42:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:42:25,992 main INFO screen SIGMA pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (74.8s)
Sep 14 02:42:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:42:44,240 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 14 02:43:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:43:32,834 main INFO screen ShillPump pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (66.8s)
Sep 14 02:43:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:43:35,800 main INFO screen UNICORN pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (70.9s)
Sep 14 02:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:43:55,966 main INFO screen Toely pass=0 dev=0.0 ins=19.11 pro=61 1a=False 1b=False 2=True (71.7s)
Sep 14 02:44:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:44:26,638 main INFO screen STRAWDOG pass=0 dev=31.36 ins=0.51 pro=32 1a=False 1b=True 2=False (53.8s)
Sep 14 02:44:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:44:29,056 main INFO screen AdamSandr pass=0 dev=1.74 ins=77.57 pro=1 1a=False 1b=True 2=True (53.3s)
Sep 14 02:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:44:59,284 main INFO screen VPN pass=0 dev=0.0 ins=20.72 pro=71 1a=False 1b=False 2=True (63.3s)
Sep 14 02:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:45:10,208 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:45:10 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:45:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:45:22,333 main INFO screen ShillPump pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.7s)
Sep 14 02:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:45:30,843 main INFO screen jamal pass=0 dev=0.0 ins=25.73 pro=38 1a=False 1b=False 2=True (61.8s)
Sep 14 02:45:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:45:50,921 main INFO screen AYE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.6s)
Sep 14 02:46:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:46:13,566 main INFO screen TURPIL pass=0 dev=2.48 ins=0.0 pro=1 1a=False 1b=False 2=False (51.2s)
Sep 14 02:46:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:46:21,015 main INFO screen SQUIG pass=0 dev=53.49 ins=0.56 pro=3 1a=False 1b=False 2=True (50.2s)
Sep 14 02:46:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:46:43,498 main INFO screen GPTMOTHY pass=0 dev=0.18 ins=78.49 pro=9 1a=False 1b=True 2=True (52.6s)
Sep 14 02:47:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:47:29,333 main INFO screen rasmr pass=0 dev=0.0 ins=23.47 pro=73 1a=False 1b=False 2=True (68.1s)
Sep 14 02:47:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:47:59,899 main INFO screen Cupsea pass=0 dev=0.0 ins=30.41 pro=68 1a=False 1b=False 2=True (69.1s)
Sep 14 02:48:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:48:01,084 main INFO screen Toely pass=0 dev=0.0 ins=28.54 pro=33 1a=False 1b=False 2=True (66.0s)
Sep 14 02:48:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:48:40,103 main INFO screen GrokSolver pass=0 dev=0.0 ins=35.88 pro=13 1a=True 1b=False 2=True (55.5s)
Sep 14 02:49:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:46,832 main INFO screen KYC pass=0 dev=0.0 ins=29.85 pro=27 1a=False 1b=False 2=True (83.2s)
Sep 14 02:49:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:51,370 main INFO screen DOOB pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (77.1s)
Sep 14 02:49:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:55,899 main INFO screen orangie pass=0 dev=0.0 ins=15.01 pro=56 1a=False 1b=False 2=True (75.8s)
Sep 14 02:50:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:50:19,131 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:50:19 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:50:46,198 main INFO screen seed pass=0 dev=0.0 ins=27.85 pro=16 1a=True 1b=False 2=True (59.4s)
Sep 14 02:51:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:51:03,941 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 14 02:51:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:51:42,440 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 14 02:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:14,906 main INFO screen PSYOPZ pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=False 2=True (71.0s)
Sep 14 02:52:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:16,858 main INFO screen ShibaShil pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (89.9s)
Sep 14 02:52:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:58,494 main INFO screen Saturween pass=0 dev=6.3 ins=0.0 pro=34 1a=False 1b=False 2=False (76.1s)
Sep 14 02:53:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:53:11,976 main INFO screen STAQ pass=0 dev=0.0 ins=38.92 pro=16 1a=True 1b=False 2=False (57.1s)
Sep 14 02:53:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:53:12,496 main INFO screen 奶龙 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.6s)
Sep 14 02:54:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:54:20,868 main INFO screen $AO pass=0 dev=40.13 ins=11.57 pro=10 1a=False 1b=False 2=False (58.3s)
Sep 14 02:55:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:06,845 main INFO screen EPIKGPT pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (60.3s)
Sep 14 02:55:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:20,640 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:55:20 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:55:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:25,359 main INFO screen USMS pass=0 dev=19.77 ins=0.0 pro=11 1a=False 1b=False 2=False (72.8s)
Sep 14 02:55:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:31,257 main INFO screen pubic pass=0 dev=0.0 ins=30.66 pro=37 1a=False 1b=False 2=True (70.4s)
Sep 14 02:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:26,219 main INFO screen TYTHON pass=1 dev=1.92 ins=6.32 pro=59 1a=False 1b=False 2=False (79.4s)
Sep 14 02:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:35,742 main INFO screen TWINEAURA pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=False 2=True (70.4s)
Sep 14 02:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:38,678 main INFO screen FROBERT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.4s)
Sep 14 02:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:57:41,409 main INFO screen USMS pass=0 dev=6.06 ins=0.0 pro=2 1a=False 1b=False 2=False (53.7s)
Sep 14 02:57:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:57:53,371 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.7s)
Sep 14 02:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:58:29,520 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (51.8s)
Sep 14 02:58:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:58:58,786 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.5s)
Sep 14 02:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:59:16,692 main INFO screen MONTY pass=0 dev=0.0 ins=18.92 pro=50 1a=False 1b=False 2=True (52.8s)
Sep 14 02:59:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:59:36,779 main INFO screen Banks pass=0 dev=0.0 ins=21.47 pro=60 1a=False 1b=False 2=True (63.4s)
Sep 14 03:00:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:00:20,516 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:00:20 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T01:33:36Z
--- update 2026-09-14T01:38:47Z
--- update 2026-09-14T01:44:10Z
--- update 2026-09-14T01:49:20Z
--- update 2026-09-14T01:54:26Z
--- update 2026-09-14T01:59:32Z
--- update 2026-09-14T02:04:36Z
--- update 2026-09-14T02:09:37Z
--- update 2026-09-14T02:14:44Z
--- update 2026-09-14T02:19:48Z
--- update 2026-09-14T02:24:49Z
--- update 2026-09-14T02:29:58Z
--- update 2026-09-14T02:34:59Z
--- update 2026-09-14T02:40:05Z
--- update 2026-09-14T02:45:08Z
--- update 2026-09-14T02:50:18Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5c723321a25a43918dd7f5917cca7869
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T02:55:19Z
--- update 2026-09-14T03:00:19Z
```

## Analyses (laatste 25 regels)
```
active
01:20:45   46000 tokens, 4702106 trades, 624669 posities (270s)
01:20:58   48000 tokens, 4900381 trades, 650745 posities (283s)
01:21:11   50000 tokens, 5090194 trades, 674603 posities (296s)
01:21:23   52000 tokens, 5279569 trades, 701217 posities (308s)
01:21:36   54000 tokens, 5472054 trades, 724710 posities (320s)
01:21:48   56000 tokens, 5666068 trades, 752606 posities (333s)
01:22:02   58000 tokens, 5879279 trades, 782376 posities (346s)
01:22:13   60000 tokens, 6079352 trades, 809473 posities (357s)
01:22:23   62000 tokens, 6287006 trades, 840673 posities (368s)
01:22:34   64000 tokens, 6500356 trades, 880050 posities (379s)
01:22:42 posities: 902414 uit 6662391 trades (391s)
01:22:55 192331 wallets gerekend
01:22:55 geluk-toets
01:23:30 persistentie
01:23:33 kopieer-simulatie
01:25:22 klaar in 551s -> /opt/schaduwbot/reports/wallets.md
02:50:22 70263 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
02:50:43   ingelezen tot rowid 7571776 (200000 rijen, 200000 bruikbaar)
02:50:47   ingelezen tot rowid 7627835 (256059 rijen, 256059 bruikbaar)
02:50:47 ingelezen: 256059 nieuwe trades, 256059 bruikbaar (29s)
02:52:38 3000 aankopen van gevolgde wallets geëvalueerd
02:52:58 vroege kopers: 216 voldoen nu, register 368, 276 tokens beoordeeld
02:53:30 grote spelers: saldo van 1254 wallets opgehaald
02:55:23 herkomst: 40 posities gekoppeld
02:55:31 klaar in 312s -> /opt/schaduwbot/reports/ledger.md
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
