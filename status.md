# Schaduwbot status

- tijd: 2026-09-14 00:52:00 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 11 hours, 5 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.2G/38G | geheugen: 1922/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 65873, "tokens_in_memory": 7948, "msgs": 8417834, "trades": 1817887, "creates": 19460, "decode_fail": 162468, "rpc_calls": 53197, "rpc_errors": 3, "sol_usd": 99.59169736654921, "open_positions": 12, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 00:20:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:20:39,211 main INFO screen DONGHORN pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 14 00:21:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:06,499 main INFO screen CUCK pass=0 dev=0.0 ins=0.04 pro=3 1a=False 1b=False 2=False (62.2s)
Sep 14 00:21:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:39,580 main INFO screen HOBL pass=0 dev=0.0 ins=23.9 pro=72 1a=False 1b=False 2=True (67.2s)
Sep 14 00:21:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:46,561 main INFO screen TWINE pass=0 dev=0.41 ins=0.0 pro=5 1a=False 1b=False 2=True (67.3s)
Sep 14 00:22:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:19,692 main INFO screen WhiteBull pass=0 dev=0.0 ins=55.63 pro=39 1a=False 1b=False 2=True (73.2s)
Sep 14 00:22:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:51,050 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.5s)
Sep 14 00:22:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:54,311 main INFO screen JANE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.7s)
Sep 14 00:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:33,604 main INFO screen Dexter pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.9s)
Sep 14 00:23:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:49,922 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 00:23:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:57,457 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.1s)
Sep 14 00:24:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:24:39,786 main INFO screen EL pass=0 dev=6.4 ins=15.94 pro=26 1a=False 1b=True 2=False (49.3s)
Sep 14 00:25:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:20,714 main INFO screen BTC pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (67.1s)
Sep 14 00:25:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:37,129 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:25:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:25:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:51,399 main INFO screen JANE pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 14 00:26:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:26:49,141 main INFO screen DOGATE pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (57.0s)
Sep 14 00:27:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:27:53,371 main INFO screen TJR pass=1 dev=0.88 ins=0.0 pro=13 1a=False 1b=False 2=False (72.1s)
Sep 14 00:28:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:28:13,687 main INFO screen UNCLE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 00:29:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:29:44,070 main INFO screen Lobster pass=0 dev=0.0 ins=12.62 pro=67 1a=False 1b=False 2=True (63.2s)
Sep 14 00:30:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:30:07,099 main INFO screen XCOINS pass=0 dev=3.42 ins=35.27 pro=78 1a=False 1b=False 2=True (61.0s)
Sep 14 00:31:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:07,862 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:31:07 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:31:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:17,816 aiohttp.access INFO 43.131.24.90 [14/Sep/2026:00:31:17 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 5.1; rv:9.0.1) Gecko/20100101 Firefox/9.0.1"
Sep 14 00:31:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:30,032 main INFO screen potato pass=0 dev=0.0 ins=29.47 pro=81 1a=False 1b=False 2=True (65.4s)
Sep 14 00:31:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:36,391 main INFO screen LOBSTER pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.7s)
Sep 14 00:32:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:32:19,917 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 14 00:32:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:32:49,280 main INFO screen taxless pass=0 dev=0.0 ins=27.42 pro=59 1a=False 1b=False 2=True (65.6s)
Sep 14 00:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:17,824 main INFO screen LaMisery pass=0 dev=0.17 ins=0.0 pro=3 1a=False 1b=False 2=False (67.6s)
Sep 14 00:33:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:55,676 main INFO screen LAUNCHPAD pass=0 dev=0.0 ins=30.0 pro=30 1a=False 1b=False 2=True (54.1s)
Sep 14 00:33:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:59,560 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:02,153 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 00:35:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:13,030 main INFO screen MINT pass=1 dev=3.42 ins=14.3 pro=50 1a=False 1b=False 2=False (113.6s)
Sep 14 00:35:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:35,105 main INFO screen KFC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (99.4s)
Sep 14 00:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:55,800 main INFO screen STONK pass=0 dev=6.46 ins=0.0 pro=1 1a=False 1b=False 2=True (53.5s)
Sep 14 00:36:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:36:12,740 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:36:12 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:36:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:36:22,958 main INFO screen BOBSOL pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (69.9s)
Sep 14 00:36:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:36:43,563 main INFO screen FALCON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.5s)
Sep 14 00:36:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:36:54,009 main INFO screen SpaceX pass=0 dev=66.64 ins=0.0 pro=1 1a=False 1b=False 2=True (58.2s)
Sep 14 00:37:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:37:23,294 main INFO screen HUMAN pass=0 dev=0.0 ins=26.05 pro=33 1a=False 1b=False 2=False (60.3s)
Sep 14 00:37:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:37:33,897 main INFO screen WhiteBull pass=0 dev=0.0 ins=44.46 pro=13 1a=False 1b=False 2=True (50.3s)
Sep 14 00:37:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:37:52,573 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.9s)
Sep 14 00:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:38:17,916 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.6s)
Sep 14 00:39:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:39:13,792 main INFO screen SAM  pass=0 dev=3.42 ins=21.04 pro=39 1a=False 1b=False 2=False (66.7s)
Sep 14 00:39:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:39:17,956 main INFO screen BGB pass=0 dev=0.59 ins=0.0 pro=1 1a=False 1b=False 2=False (61.3s)
Sep 14 00:39:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:39:20,457 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 14 00:40:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:40:22,236 main INFO screen Bulljak pass=0 dev=1.74 ins=44.0 pro=35 1a=False 1b=False 2=True (68.4s)
Sep 14 00:40:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:40:23,651 main INFO screen GOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.7s)
Sep 14 00:40:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:40:26,722 main INFO screen Jamie pass=1 dev=0.0 ins=0.0 pro=41 1a=False 1b=False 2=False (66.3s)
Sep 14 00:41:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:41:13,463 main INFO screen PVE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.8s)
Sep 14 00:41:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:41:18,914 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 14 00:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:41:30,929 main INFO screen GAMESTOP pass=0 dev=5.18 ins=0.0 pro=15 1a=False 1b=False 2=False (64.2s)
Sep 14 00:41:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:41:31,699 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:41:31 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:42:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:42:29,548 main INFO screen THE CHEAT pass=0 dev=0.72 ins=0.0 pro=5 1a=False 1b=False 2=False (70.6s)
Sep 14 00:42:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:42:31,224 main INFO screen MHGA pass=0 dev=0.0 ins=38.35 pro=53 1a=False 1b=False 2=True (77.8s)
Sep 14 00:42:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:42:37,236 main INFO screen Duck pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (66.3s)
Sep 14 00:43:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:43:35,611 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.1s)
Sep 14 00:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:43:37,054 main INFO screen CHILLCAT pass=1 dev=0.04 ins=5.86 pro=55 1a=False 1b=False 2=False (65.8s)
Sep 14 00:43:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:43:52,200 main INFO screen PUMP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (60.6s)
Sep 14 00:44:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:44:26,420 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.8s)
Sep 14 00:45:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:45:41,098 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.3s)
Sep 14 00:45:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:45:52,672 main INFO screen KOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (47.0s)
Sep 14 00:46:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:46:25,315 main INFO screen TAPE pass=1 dev=3.09 ins=0.0 pro=66 1a=False 1b=False 2=False (61.9s)
Sep 14 00:46:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:46:30,787 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.7s)
Sep 14 00:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:46:37,171 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:46:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:47:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:47:38,333 main INFO screen BITKOIN pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (61.3s)
Sep 14 00:48:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:48:09,885 main INFO screen JANE pass=0 dev=0.28 ins=0.0 pro=5 1a=False 1b=False 2=False (64.4s)
Sep 14 00:48:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:48:58,659 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.1s)
Sep 14 00:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:49:21,173 main INFO screen SOLBOT pass=0 dev=0.0 ins=23.42 pro=66 1a=False 1b=False 2=True (50.6s)
Sep 14 00:49:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:49:49,777 main INFO screen LetsRide pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (51.4s)
Sep 14 00:50:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:50:55,276 main INFO screen PANIC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.9s)
Sep 14 00:51:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:51:38,634 main INFO screen Nintendo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.4s)
Sep 14 00:52:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:00,785 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:52:00 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T23:24:17Z
--- update 2026-09-13T23:29:20Z
--- update 2026-09-13T23:34:26Z
--- update 2026-09-13T23:39:29Z
--- update 2026-09-13T23:44:32Z
--- update 2026-09-13T23:49:36Z
--- update 2026-09-13T23:54:39Z
--- update 2026-09-13T23:59:40Z
--- update 2026-09-14T00:04:46Z
--- update 2026-09-14T00:10:22Z
--- update 2026-09-14T00:15:23Z
--- update 2026-09-14T00:20:34Z
--- update 2026-09-14T00:25:36Z
--- update 2026-09-14T00:31:06Z
--- update 2026-09-14T00:36:11Z
--- update 2026-09-14T00:41:30Z
--- update 2026-09-14T00:46:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7e8a0dc2ace745d49c06fa77ab8fe773
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T00:51:59Z
```

## Analyses (laatste 25 regels)
```
active
23:14:53   44000 tokens, 4548599 trades, 621351 posities (248s)
23:15:05   46000 tokens, 4751977 trades, 646323 posities (260s)
23:15:17   48000 tokens, 4947857 trades, 676731 posities (273s)
23:15:30   50000 tokens, 5152223 trades, 704551 posities (286s)
23:15:42   52000 tokens, 5327073 trades, 727800 posities (297s)
23:15:53   54000 tokens, 5528435 trades, 756055 posities (309s)
23:16:05   56000 tokens, 5741491 trades, 787436 posities (320s)
23:16:15   58000 tokens, 5949257 trades, 815855 posities (330s)
23:16:24   60000 tokens, 6158655 trades, 848573 posities (339s)
23:16:34   62000 tokens, 6378507 trades, 891082 posities (349s)
23:16:43 posities: 913444 uit 6542295 trades (361s)
23:16:54 192830 wallets gerekend
23:16:54 geluk-toets
23:17:26 persistentie
23:17:28 kopieer-simulatie
23:19:10 klaar in 508s -> /opt/schaduwbot/reports/wallets.md
00:46:39 67722 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
00:46:59   ingelezen tot rowid 7325925 (200000 rijen, 200000 bruikbaar)
00:47:02   ingelezen tot rowid 7371776 (245851 rijen, 245851 bruikbaar)
00:47:03 ingelezen: 245851 nieuwe trades, 245851 bruikbaar (27s)
00:48:47 3000 aankopen van gevolgde wallets geëvalueerd
00:49:07 vroege kopers: 206 voldoen nu, register 357, 317 tokens beoordeeld
00:49:27 grote spelers: saldo van 482 wallets opgehaald
00:51:01 herkomst: 40 posities gekoppeld
00:51:08 klaar in 271s -> /opt/schaduwbot/reports/ledger.md
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
