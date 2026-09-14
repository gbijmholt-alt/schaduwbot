# Schaduwbot status

- tijd: 2026-09-14 22:43:02 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 8 hours, 56 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.5G/38G | geheugen: 2204/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 144534, "tokens_in_memory": 11439, "msgs": 20965589, "trades": 4340345, "creates": 46195, "decode_fail": 385541, "rpc_calls": 122750, "rpc_errors": 12, "sol_usd": 103.07701556654604, "open_positions": 68, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 22:21:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:27,735 main INFO screen ROGE pass=0 dev=0.0 ins=9.81 pro=1 1a=False 1b=False 2=False (74.5s)
Sep 14 22:21:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:28,942 main INFO screen Kongal pass=0 dev=0.0 ins=10.28 pro=5 1a=False 1b=False 2=False (74.8s)
Sep 14 22:21:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:49,882 main INFO screen LASER pass=0 dev=0.0 ins=29.94 pro=51 1a=False 1b=False 2=True (71.6s)
Sep 14 22:22:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:16,916 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:22:16 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:22:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:35,115 main INFO screen VIVET pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (67.4s)
Sep 14 22:22:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:44,099 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.2s)
Sep 14 22:22:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:50,414 main INFO screen MOONTICKET pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (60.5s)
Sep 14 22:23:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:35,290 main INFO screen DOWN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 14 22:23:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:44,793 main INFO screen Raven pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 14 22:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:47,767 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (57.4s)
Sep 14 22:24:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:31,820 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 14 22:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:44,301 main INFO screen DOGE pass=0 dev=0.0 ins=44.01 pro=41 1a=False 1b=True 2=True (59.5s)
Sep 14 22:24:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:53,533 main INFO screen INU pass=0 dev=3.65 ins=0.0 pro=4 1a=False 1b=False 2=False (65.8s)
Sep 14 22:25:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:47,342 main INFO screen DTK pass=0 dev=0.18 ins=0.0 pro=7 1a=False 1b=False 2=False (75.5s)
Sep 14 22:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:52,554 main INFO screen PoCat pass=0 dev=0.0 ins=3.39 pro=3 1a=False 1b=False 2=False (68.3s)
Sep 14 22:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:52,981 main INFO screen BIKEWOJAK pass=0 dev=0.0 ins=0.25 pro=5 1a=False 1b=False 2=False (59.4s)
Sep 14 22:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:00,064 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.5s)
Sep 14 22:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:00,240 main INFO screen LION KING pass=0 dev=0.0 ins=2.51 pro=24 1a=False 1b=False 2=False (72.9s)
Sep 14 22:27:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:03,303 main INFO screen BJS pass=0 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=True (70.3s)
Sep 14 22:27:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:37,633 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:27:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:27:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:57,792 main INFO screen BIKEWOJAK pass=0 dev=0.0 ins=44.28 pro=3 1a=False 1b=True 2=True (57.7s)
Sep 14 22:28:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:28:09,911 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.7s)
Sep 14 22:28:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:28:12,035 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 14 22:28:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:28:53,285 main INFO screen ZYNQ pass=0 dev=27.7 ins=0.0 pro=13 1a=False 1b=False 2=False (55.5s)
Sep 14 22:29:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:29:13,963 main INFO screen BobCoin pass=0 dev=0.0 ins=14.37 pro=68 1a=False 1b=False 2=True (61.9s)
Sep 14 22:29:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:29:28,517 main INFO screen SOLROCKET pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (78.6s)
Sep 14 22:29:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:29:53,582 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 14 22:30:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:30:26,957 main INFO screen BUZZ pass=0 dev=0.0 ins=32.79 pro=34 1a=False 1b=False 2=True (73.0s)
Sep 14 22:30:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:30:57,793 main INFO screen DARK pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (89.3s)
Sep 14 22:31:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:31:01,963 main INFO screen Phytos pass=0 dev=0.0 ins=11.38 pro=42 1a=False 1b=False 2=False (68.4s)
Sep 14 22:31:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:31:25,910 aiohttp.access INFO 172.236.228.222 [14/Sep/2026:22:31:25 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 22:31:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:31:26,234 aiohttp.access INFO 172.236.228.222 [14/Sep/2026:22:31:26 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 22:31:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:31:28,949 main INFO screen Raven pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.0s)
Sep 14 22:32:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:32:09,370 main INFO screen bafi pass=0 dev=4.8 ins=0.0 pro=1 1a=False 1b=False 2=False (71.6s)
Sep 14 22:32:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:32:09,785 main INFO screen EATME pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (67.8s)
Sep 14 22:32:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:32:26,734 main INFO screen Ferrari pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (57.8s)
Sep 14 22:32:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:32:55,869 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:32:55 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 22:33:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:33:07,333 main INFO screen TNT pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (58.0s)
Sep 14 22:33:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:33:07,905 main INFO screen Tired pass=0 dev=0.0 ins=11.04 pro=3 1a=False 1b=False 2=True (58.1s)
Sep 14 22:33:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:33:26,839 main INFO screen KIKE pass=0 dev=0.0 ins=23.2 pro=51 1a=False 1b=False 2=False (60.1s)
Sep 14 22:34:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:34:09,691 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (62.4s)
Sep 14 22:34:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:34:17,295 main INFO screen pomp pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.4s)
Sep 14 22:34:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:34:26,579 main INFO screen Bank pass=0 dev=0.0 ins=35.44 pro=58 1a=True 1b=False 2=True (59.7s)
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:35:23,243 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 22:35:23 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 22:36:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:36:04,417 main INFO screen OLIVIA pass=0 dev=0.0 ins=12.81 pro=3 1a=False 1b=False 2=True (114.7s)
Sep 14 22:36:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:36:14,038 main INFO screen TOEROGAN pass=0 dev=0.0 ins=9.64 pro=66 1a=False 1b=False 2=True (116.7s)
Sep 14 22:36:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:36:23,081 main INFO screen Raven pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (116.5s)
Sep 14 22:36:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:36:52,536 main INFO screen taxless pass=0 dev=0.0 ins=19.71 pro=18 1a=False 1b=False 2=True (48.1s)
Sep 14 22:37:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:37:00,091 main INFO screen SLOP pass=0 dev=0.0 ins=30.23 pro=9 1a=False 1b=False 2=True (46.1s)
Sep 14 22:37:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:37:12,966 main INFO screen FUSION pass=0 dev=0.0 ins=26.89 pro=74 1a=False 1b=False 2=True (49.9s)
Sep 14 22:37:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:37:41,848 main INFO screen cwoin pass=0 dev=0.0 ins=40.23 pro=9 1a=False 1b=False 2=True (49.3s)
Sep 14 22:37:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:37:47,363 main INFO screen Rogan pass=0 dev=0.0 ins=5.75 pro=30 1a=False 1b=False 2=True (47.3s)
Sep 14 22:37:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:37:59,547 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:37:59 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:38:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:38:15,355 main INFO screen INU pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (62.4s)
Sep 14 22:38:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:38:53,275 main INFO screen BeggingMouse pass=0 dev=0.0 ins=9.48 pro=3 1a=False 1b=False 2=False (65.9s)
Sep 14 22:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:38:55,703 main INFO screen Raven pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (73.9s)
Sep 14 22:39:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:39:11,526 main INFO screen 🔪 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.2s)
Sep 14 22:39:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:39:56,814 main INFO screen Rogan pass=0 dev=0.0 ins=10.75 pro=2 1a=False 1b=False 2=True (61.1s)
Sep 14 22:39:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:39:58,705 main INFO screen TOEROGAN pass=0 dev=0.0 ins=10.04 pro=2 1a=False 1b=False 2=True (65.4s)
Sep 14 22:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:40:06,271 main INFO screen SolLama pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.7s)
Sep 14 22:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:40:46,868 main INFO screen אַלוֹן pass=0 dev=0.0 ins=22.58 pro=38 1a=False 1b=False 2=True (48.2s)
Sep 14 22:40:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:40:51,019 main INFO screen lightwork pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 14 22:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:40:59,554 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 14 22:41:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:41:38,743 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.9s)
Sep 14 22:41:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:41:42,185 main INFO screen SlopCycle pass=0 dev=0.0 ins=31.28 pro=15 1a=False 1b=False 2=True (51.2s)
Sep 14 22:41:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:41:47,230 main INFO screen SpaceX pass=0 dev=0.0 ins=174.59 pro=0 1a=False 1b=False 2=True (47.7s)
Sep 14 22:42:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:42:30,892 main INFO screen FLY pass=0 dev=0.0 ins=30.11 pro=67 1a=False 1b=False 2=True (52.1s)
Sep 14 22:42:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:42:36,744 main INFO screen FLY pass=0 dev=0.0 ins=31.94 pro=21 1a=False 1b=False 2=True (49.5s)
Sep 14 22:42:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:42:46,709 main INFO screen ROCKET pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (64.5s)
Sep 14 22:43:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:43:02,592 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:43:02 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T21:13:21Z
--- update 2026-09-14T21:18:29Z
--- update 2026-09-14T21:23:36Z
--- update 2026-09-14T21:28:54Z
--- update 2026-09-14T21:34:36Z
--- update 2026-09-14T21:39:39Z
--- update 2026-09-14T21:45:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5eee46075898481b8005cdd132a55989
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T21:50:36Z
--- update 2026-09-14T21:55:44Z
--- update 2026-09-14T22:01:30Z
--- update 2026-09-14T22:06:35Z
--- update 2026-09-14T22:11:36Z
--- update 2026-09-14T22:16:38Z
--- update 2026-09-14T22:22:15Z
--- update 2026-09-14T22:27:36Z
--- update 2026-09-14T22:32:54Z
--- update 2026-09-14T22:37:58Z
--- update 2026-09-14T22:43:01Z
```

## Analyses (laatste 25 regels)
```
inactive
22:22:35   38000 tokens, 3709788 trades, 448598 posities (250s)
22:22:50   40000 tokens, 3900481 trades, 473390 posities (264s)
22:23:04   42000 tokens, 4086379 trades, 492462 posities (278s)
22:23:17   44000 tokens, 4260028 trades, 515191 posities (291s)
22:23:30   46000 tokens, 4445005 trades, 537426 posities (305s)
22:23:44   48000 tokens, 4620265 trades, 558280 posities (319s)
22:23:59   50000 tokens, 4822700 trades, 580896 posities (334s)
22:24:14   52000 tokens, 5032898 trades, 607308 posities (349s)
22:24:28   54000 tokens, 5221391 trades, 629728 posities (363s)
22:24:42   56000 tokens, 5390312 trades, 650213 posities (377s)
22:24:58   58000 tokens, 5581326 trades, 674058 posities (393s)
22:25:12   60000 tokens, 5766236 trades, 695878 posities (407s)
22:25:27   62000 tokens, 5971487 trades, 721683 posities (422s)
22:25:40   64000 tokens, 6162947 trades, 750238 posities (435s)
22:25:55   66000 tokens, 6381573 trades, 779020 posities (450s)
22:26:08   68000 tokens, 6564687 trades, 802231 posities (463s)
22:26:23   70000 tokens, 6758719 trades, 827352 posities (478s)
22:26:37   72000 tokens, 6950951 trades, 853949 posities (492s)
22:26:52   74000 tokens, 7146187 trades, 885103 posities (506s)
22:26:56 posities: 891065 uit 7198322 trades (512s)
22:27:09 209874 wallets gerekend
22:27:10 geluk-toets
22:27:44 persistentie
22:27:47 kopieer-simulatie
22:30:19 klaar in 715s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
20:47:38 ijk: +0 van 0 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 11}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:47:39 ijk-diagnose: nieuwste migratie 3.5 min oud | migraties 15/60/240 min: 11/45/183 | al gemeten: 229
20:52:38 ijk: +0 van 0 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 9}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:52:39 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 9/43/182 | al gemeten: 229
21:45:44 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=7 -> nog 8 metingen binnen 5 minuten na de migratie te gaan
21:45:46 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 12/43/183 | al gemeten: 250
22:33:15 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=9 -> nog 6 metingen binnen 5 minuten na de migratie te gaan
22:33:15 ijk-diagnose: nieuwste migratie 2.6 min oud | migraties 15/60/240 min: 12/40/179 | al gemeten: 271
22:38:16 ijk: +6 van 7 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=14 -> nog 1 metingen binnen 5 minuten na de migratie te gaan
22:38:16 ijk-diagnose: nieuwste migratie 1.0 min oud | migraties 15/60/240 min: 13/42/184 | al gemeten: 277
22:43:02 ijk: +0 van 0 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=14 -> nog 1 metingen binnen 5 minuten na de migratie te gaan
22:43:02 ijk-diagnose: nieuwste migratie 6.1 min oud | migraties 15/60/240 min: 8/38/180 | al gemeten: 277
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
