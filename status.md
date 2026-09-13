# Schaduwbot status

- tijd: 2026-09-13 14:00:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 13 minutes
- bot-service: active
- code-versie: 6977315
- schijf: 4.6G/38G | geheugen: 1053/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 26789, "tokens_in_memory": 4636, "msgs": 1762494, "trades": 511019, "creates": 5629, "decode_fail": 62684, "rpc_calls": 16492, "rpc_errors": 1, "sol_usd": 100.07801028671632, "open_positions": 40, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 13:34:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:34:54,272 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:34:54 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:35:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:35:14,194 main INFO screen Cap pass=0 dev=0.0 ins=28.4 pro=63 1a=False 1b=False 2=True (107.5s)
Sep 13 13:36:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:36:11,492 main INFO screen KURP pass=0 dev=0.0 ins=78.87 pro=10 1a=False 1b=False 2=True (77.2s)
Sep 13 13:36:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:36:11,824 main INFO screen cap pass=1 dev=4.03 ins=0.0 pro=14 1a=False 1b=False 2=False (77.6s)
Sep 13 13:37:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:37:22,510 main INFO screen TALPY pass=0 dev=0.0 ins=31.83 pro=33 1a=False 1b=True 2=True (50.6s)
Sep 13 13:37:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:37:39,985 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.6s)
Sep 13 13:39:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:39:03,479 main INFO screen LAMBO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.2s)
Sep 13 13:39:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:39:27,085 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:39:27 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:39:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:39:27,360 main INFO screen FORTSOL pass=0 dev=0.02 ins=17.18 pro=57 1a=False 1b=False 2=True (65.7s)
Sep 13 13:39:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:39:46,946 main INFO screen Cap pass=0 dev=0.0 ins=0.3 pro=64 1a=False 1b=False 2=True (69.1s)
Sep 13 13:39:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:39:57,303 main INFO screen FADD pass=0 dev=0.0 ins=17.03 pro=17 1a=False 1b=False 2=True (53.8s)
Sep 13 13:40:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:40:36,019 main INFO screen CATCENTER pass=0 dev=0.0 ins=17.48 pro=68 1a=False 1b=False 2=True (68.7s)
Sep 13 13:40:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:40:51,823 main INFO screen cap pass=1 dev=0.0 ins=0.88 pro=14 1a=False 1b=False 2=False (64.9s)
Sep 13 13:41:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:41:28,447 main INFO screen kittylick pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (72.9s)
Sep 13 13:41:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:41:44,175 main INFO screen UK pass=0 dev=0.0 ins=39.76 pro=19 1a=False 1b=False 2=True (51.9s)
Sep 13 13:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:41:51,593 main INFO screen Bcat pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (53.8s)
Sep 13 13:43:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:43:29,888 main INFO screen bullc2 pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (67.4s)
Sep 13 13:43:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:43:33,565 main INFO screen UK pass=0 dev=0.0 ins=24.94 pro=74 1a=False 1b=False 2=True (66.7s)
Sep 13 13:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:43:55,594 main INFO screen SK pass=0 dev=0.0 ins=29.12 pro=49 1a=False 1b=False 2=False (75.5s)
Sep 13 13:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:44:37,355 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:44:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:44:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:44:40,518 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (70.6s)
Sep 13 13:44:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:44:43,964 main INFO screen NABU pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (70.4s)
Sep 13 13:45:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:45:03,853 main INFO screen VOID  pass=0 dev=42.6 ins=0.0 pro=5 1a=False 1b=False 2=False (68.3s)
Sep 13 13:45:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:45:36,983 main INFO screen DK pass=0 dev=0.0 ins=23.99 pro=26 1a=False 1b=False 2=True (53.0s)
Sep 13 13:45:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:45:47,878 main INFO screen DK pass=0 dev=0.0 ins=25.81 pro=70 1a=False 1b=False 2=True (67.4s)
Sep 13 13:45:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:45:49,925 main INFO screen DK pass=0 dev=0.0 ins=29.17 pro=14 1a=False 1b=False 2=True (46.1s)
Sep 13 13:46:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:46:25,030 main INFO screen Whats pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (48.0s)
Sep 13 13:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:46:35,557 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.7s)
Sep 13 13:46:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:46:56,176 main INFO screen cokecat pass=1 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=False (66.2s)
Sep 13 13:47:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:47:20,004 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.0s)
Sep 13 13:47:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:47:42,366 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.8s)
Sep 13 13:47:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:47:50,306 main INFO screen Pump pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.1s)
Sep 13 13:48:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:07,518 main INFO screen SAMULO pass=0 dev=0.0 ins=31.94 pro=17 1a=False 1b=False 2=True (47.5s)
Sep 13 13:48:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:49,109 main INFO screen $Pumpty pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.7s)
Sep 13 13:48:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:53,627 aiohttp.access INFO 204.76.203.49 [13/Sep/2026:13:48:53 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 13 13:48:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:53,650 aiohttp.access INFO 204.76.203.49 [13/Sep/2026:13:48:53 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 13 13:48:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:54,564 main INFO screen OrcaBall pass=0 dev=0.0 ins=56.12 pro=54 1a=False 1b=False 2=True (64.3s)
Sep 13 13:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:48:56,092 main INFO screen chat pass=0 dev=74.05 ins=16.17 pro=1 1a=False 1b=False 2=True (48.6s)
Sep 13 13:49:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:49:55,264 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:49:55 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:49:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:49:57,592 main INFO screen PLEUNTJE pass=0 dev=0.0 ins=30.11 pro=76 1a=False 1b=False 2=True (68.5s)
Sep 13 13:50:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:50:00,481 main INFO screen CAJUN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.9s)
Sep 13 13:50:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:50:01,530 main INFO screen beer pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (65.4s)
Sep 13 13:50:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:50:49,325 main INFO screen Gigalon pass=0 dev=0.0 ins=24.3 pro=48 1a=False 1b=False 2=False (51.7s)
Sep 13 13:51:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:51:06,846 main INFO screen Pump pass=1 dev=1.08 ins=0.0 pro=14 1a=False 1b=False 2=False (66.4s)
Sep 13 13:51:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:51:09,848 main INFO screen snek pass=1 dev=0.0 ins=9.51 pro=77 1a=False 1b=False 2=False (68.3s)
Sep 13 13:52:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:52:03,750 main INFO screen PLEUNTJE pass=0 dev=0.0 ins=13.42 pro=21 1a=False 1b=False 2=True (53.9s)
Sep 13 13:52:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:52:05,260 main INFO screen Pleun pass=0 dev=0.0 ins=36.45 pro=77 1a=False 1b=False 2=True (75.9s)
Sep 13 13:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:52:14,546 main INFO screen $SHAG pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (67.7s)
Sep 13 13:53:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:53:01,032 main INFO screen England pass=0 dev=0.0 ins=26.82 pro=71 1a=False 1b=False 2=True (57.3s)
Sep 13 13:53:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:53:13,398 main INFO screen NIP pass=0 dev=0.0 ins=31.94 pro=45 1a=False 1b=False 2=True (68.1s)
Sep 13 13:53:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:53:21,076 main INFO screen Pleun pass=0 dev=0.0 ins=16.14 pro=38 1a=False 1b=False 2=True (66.5s)
Sep 13 13:53:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:53:49,680 main INFO screen OpenAI pass=0 dev=0.39 ins=78.92 pro=1 1a=False 1b=False 2=True (48.6s)
Sep 13 13:54:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:54:21,776 main INFO screen CAJUN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.4s)
Sep 13 13:54:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:54:24,750 main INFO screen $SNACK pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (63.7s)
Sep 13 13:54:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:54:57,451 main INFO screen XXHuskii pass=1 dev=0.0 ins=5.0 pro=11 1a=False 1b=False 2=False (67.8s)
Sep 13 13:55:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:55:14,018 main INFO screen highs pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.2s)
Sep 13 13:55:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:55:16,616 main INFO screen PLEUNTJE pass=0 dev=0.0 ins=22.68 pro=54 1a=False 1b=False 2=True (51.9s)
Sep 13 13:55:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:55:17,743 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:55:17 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 13:55:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:55:47,223 main INFO screen 黃阿瑪 pass=0 dev=0.0 ins=78.96 pro=1 1a=True 1b=True 2=True (49.8s)
Sep 13 13:56:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:56:05,082 main INFO screen DONGLE pass=0 dev=0.0 ins=78.87 pro=6 1a=False 1b=False 2=True (51.1s)
Sep 13 13:56:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:56:29,757 main INFO screen WHEEL pass=0 dev=0.0 ins=22.89 pro=73 1a=False 1b=False 2=True (59.4s)
Sep 13 13:56:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:56:40,533 main INFO screen DOGE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 13 13:57:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:57:12,134 main INFO screen LaMisery pass=0 dev=1.51 ins=0.0 pro=4 1a=False 1b=False 2=False (67.1s)
Sep 13 13:57:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:57:36,458 main INFO screen OOmarley pass=0 dev=0.07 ins=0.0 pro=5 1a=False 1b=False 2=False (66.7s)
Sep 13 13:57:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:57:53,289 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.0s)
Sep 13 13:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:58:18,486 main INFO screen MALF pass=0 dev=57.2 ins=0.0 pro=4 1a=False 1b=False 2=False (66.4s)
Sep 13 13:59:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:59:23,144 main INFO screen RISE pass=0 dev=40.35 ins=0.0 pro=4 1a=False 1b=False 2=False (64.9s)
Sep 13 13:59:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:59:42,500 main INFO screen OrcaBall pass=0 dev=0.0 ins=55.86 pro=16 1a=False 1b=False 2=True (63.5s)
Sep 13 13:59:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:59:44,840 main INFO screen ch pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (66.5s)
Sep 13 14:00:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:00:21,646 main INFO screen $SANDY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 13 14:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:00:37,052 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:00:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T13:02:27Z
nieuwe code: 4a93173
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: be001e47867c4d53bf64f959d70cd386
analyses gestart (00feb5de9af9)
--- update 2026-09-13T13:07:36Z
--- update 2026-09-13T13:13:13Z
--- update 2026-09-13T13:18:29Z
nieuwe code: 6977315
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T13:23:36Z
--- update 2026-09-13T13:28:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: 6b131609667c446db5ee762a2a7e18b8
analyses gestart (29fd1f8386bc)
--- update 2026-09-13T13:34:14Z
--- update 2026-09-13T13:39:26Z
--- update 2026-09-13T13:44:36Z
--- update 2026-09-13T13:49:54Z
--- update 2026-09-13T13:55:16Z
--- update 2026-09-13T14:00:36Z
```

## Analyses (laatste 25 regels)
```
inactive
13:41:36   18000 tokens, 1992302 trades, 315006 posities (40s)
13:41:40   20000 tokens, 2242016 trades, 359976 posities (44s)
13:41:43   22000 tokens, 2468190 trades, 398884 posities (47s)
13:41:46   24000 tokens, 2677289 trades, 427131 posities (50s)
13:41:50   26000 tokens, 2885097 trades, 458151 posities (55s)
13:41:55   28000 tokens, 3135235 trades, 498111 posities (60s)
13:41:59   30000 tokens, 3352579 trades, 533256 posities (63s)
13:42:03   32000 tokens, 3566493 trades, 566685 posities (67s)
13:42:07   34000 tokens, 3808036 trades, 608599 posities (71s)
13:42:10   36000 tokens, 4018245 trades, 641638 posities (74s)
13:42:14   38000 tokens, 4245156 trades, 676512 posities (78s)
13:42:17   40000 tokens, 4454863 trades, 709179 posities (81s)
13:42:20   42000 tokens, 4677372 trades, 744608 posities (84s)
13:42:22   44000 tokens, 4881237 trades, 778747 posities (86s)
13:42:25   46000 tokens, 5104329 trades, 815066 posities (90s)
13:42:30   48000 tokens, 5336125 trades, 853347 posities (94s)
13:42:34   50000 tokens, 5563743 trades, 890112 posities (99s)
13:42:38   52000 tokens, 5789931 trades, 932064 posities (102s)
13:42:41   54000 tokens, 5990533 trades, 973580 posities (105s)
13:42:41 posities: 986877 uit 6042752 trades (106s)
13:42:55 202358 wallets gerekend
13:42:55 geluk-toets
13:43:28 persistentie
13:43:31 kopieer-simulatie
13:44:11 klaar in 196s -> /opt/schaduwbot/reports/wallets.md
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
