# Schaduwbot status

- tijd: 2026-09-15 18:55:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 5 hours, 8 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.5G/38G | geheugen: 2263/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 217273, "tokens_in_memory": 9959, "msgs": 33633696, "trades": 6840093, "creates": 72567, "decode_fail": 582227, "rpc_calls": 195421, "rpc_errors": 17, "sol_usd": 97.74394304214218, "open_positions": 69, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 18:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:33:21,588 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (75.8s)
Sep 15 18:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:08,587 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (65.1s)
Sep 15 18:34:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:24,394 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.8s)
Sep 15 18:34:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:24,986 main INFO screen $ROCKET pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (63.7s)
Sep 15 18:34:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:37,294 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:34:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:35:37,285 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:35:37,397 rpc WARNING rpc getTokenLargestAccounts exc
Sep 15 18:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:35:55,769 main INFO screen DCS pass=0 dev=0.0 ins=0.31 pro=3 1a=False 1b=False 2=False (107.2s)
Sep 15 18:36:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:36:17,938 main INFO screen WHEEL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (113.5s)
Sep 15 18:36:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:36:24,743 main INFO screen werld pass=0 dev=0.0 ins=48.18 pro=20 1a=False 1b=False 2=True (119.8s)
Sep 15 18:37:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:37:08,625 main INFO screen BTAI pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (72.9s)
Sep 15 18:37:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:37:26,291 main INFO screen Traincat pass=0 dev=0.0 ins=24.11 pro=69 1a=False 1b=False 2=True (68.4s)
Sep 15 18:37:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:37:29,771 main INFO screen CLART pass=0 dev=0.0 ins=9.33 pro=54 1a=False 1b=False 2=True (65.0s)
Sep 15 18:38:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:38:02,276 main INFO screen CBO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 15 18:38:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:38:26,250 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 15 18:38:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:38:30,935 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (61.2s)
Sep 15 18:39:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:39:00,588 main INFO screen $ROCKET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.3s)
Sep 15 18:39:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:39:21,642 main INFO screen MOGE pass=0 dev=0.0 ins=19.76 pro=45 1a=False 1b=False 2=True (55.4s)
Sep 15 18:39:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:39:25,572 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (54.6s)
Sep 15 18:39:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:39:37,144 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:39:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:40:06,881 main INFO screen TUSK pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (66.3s)
Sep 15 18:40:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:40:24,564 main INFO screen FAZE pass=0 dev=0.0 ins=13.74 pro=12 1a=False 1b=False 2=False (59.0s)
Sep 15 18:40:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:40:30,572 main INFO screen PEPEFU pass=0 dev=0.0 ins=79.17 pro=4 1a=False 1b=True 2=True (68.9s)
Sep 15 18:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:41:05,415 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (58.5s)
Sep 15 18:41:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:41:18,605 main INFO screen SpaceX pass=0 dev=0.0 ins=147.49 pro=0 1a=False 1b=False 2=True (54.0s)
Sep 15 18:41:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:41:36,738 main INFO screen ROBBIN pass=0 dev=0.0 ins=24.45 pro=72 1a=False 1b=False 2=True (66.2s)
Sep 15 18:42:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:42:05,333 main INFO screen HAMMER pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (59.9s)
Sep 15 18:42:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:42:12,949 main INFO screen ROBBIN pass=0 dev=0.0 ins=38.57 pro=37 1a=False 1b=False 2=True (54.3s)
Sep 15 18:42:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:42:27,906 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.2s)
Sep 15 18:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:42:52,154 main INFO screen dih pass=0 dev=0.0 ins=56.98 pro=25 1a=False 1b=False 2=True (46.8s)
Sep 15 18:43:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:43:21,614 main INFO screen PEA pass=0 dev=2.79 ins=0.43 pro=70 1a=False 1b=False 2=False (68.7s)
Sep 15 18:43:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:43:34,641 main INFO screen ROBBIN pass=0 dev=0.0 ins=28.81 pro=69 1a=False 1b=False 2=True (66.7s)
Sep 15 18:43:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:43:45,620 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.5s)
Sep 15 18:44:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:44:18,173 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 15 18:44:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:44:43,803 main INFO screen ANON pass=0 dev=0.0 ins=43.57 pro=56 1a=False 1b=False 2=True (69.2s)
Sep 15 18:44:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:44:44,186 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:44:44 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:44:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:44:54,248 main INFO screen $Omt pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (68.6s)
Sep 15 18:45:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:45:27,614 main INFO screen NUT pass=0 dev=0.0 ins=31.66 pro=75 1a=False 1b=False 2=True (69.4s)
Sep 15 18:45:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:45:52,791 main INFO screen Rob pass=0 dev=0.0 ins=18.55 pro=52 1a=False 1b=False 2=True (69.0s)
Sep 15 18:45:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:45:58,519 main INFO screen escobar pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 15 18:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:46:35,340 main INFO screen CRIMECAT pass=0 dev=0.0 ins=38.58 pro=77 1a=False 1b=False 2=True (67.7s)
Sep 15 18:46:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:46:49,310 main INFO screen SEI pass=0 dev=0.0 ins=24.76 pro=30 1a=False 1b=False 2=True (50.8s)
Sep 15 18:46:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:46:49,619 main INFO screen IQD pass=0 dev=42.92 ins=0.0 pro=2 1a=False 1b=False 2=True (56.8s)
Sep 15 18:47:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:47:38,220 main INFO screen ROBBIN pass=0 dev=0.0 ins=35.59 pro=16 1a=False 1b=False 2=True (48.9s)
Sep 15 18:47:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:47:40,662 main INFO screen lowcap pass=0 dev=0.0 ins=29.55 pro=42 1a=False 1b=False 2=True (65.3s)
Sep 15 18:47:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:47:42,825 main INFO screen ROBBIN pass=0 dev=0.0 ins=28.79 pro=13 1a=False 1b=False 2=True (53.2s)
Sep 15 18:48:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:48:32,587 main INFO screen ROBBIN pass=0 dev=0.0 ins=34.67 pro=78 1a=False 1b=False 2=True (54.4s)
Sep 15 18:48:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:48:42,334 main INFO screen BLURRY pass=0 dev=0.06 ins=0.0 pro=4 1a=False 1b=False 2=False (61.7s)
Sep 15 18:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:48:47,038 main INFO screen SM pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (64.2s)
Sep 15 18:49:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:49:45,545 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:49:45 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:49:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:49:54,560 main INFO screen Doohnibor pass=0 dev=0.0 ins=35.47 pro=36 1a=False 1b=False 2=True (82.0s)
Sep 15 18:49:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:49:57,435 main INFO screen Perrito pass=0 dev=0.0 ins=26.87 pro=74 1a=False 1b=False 2=True (75.1s)
Sep 15 18:50:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:50:02,146 main INFO screen DAVE pass=0 dev=0.0 ins=36.86 pro=42 1a=False 1b=False 2=True (75.1s)
Sep 15 18:50:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:50:29,961 aiohttp.access INFO 200.168.117.238 [15/Sep/2026:18:50:29 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 15 18:50:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:50:49,299 main INFO screen Perrito pass=0 dev=0.0 ins=23.92 pro=1 1a=False 1b=False 2=True (54.7s)
Sep 15 18:51:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:51:01,886 main INFO screen ROAM pass=0 dev=0.0 ins=3.46 pro=42 1a=False 1b=False 2=False (64.4s)
Sep 15 18:51:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:51:12,755 main INFO screen KASHCAT pass=0 dev=0.0 ins=8.04 pro=66 1a=False 1b=False 2=False (70.6s)
Sep 15 18:52:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:52:02,606 main INFO screen beandiesel pass=0 dev=0.0 ins=59.56 pro=10 1a=False 1b=False 2=True (73.3s)
Sep 15 18:52:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:52:06,929 main INFO screen ROAR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.0s)
Sep 15 18:52:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:52:38,370 main INFO screen Blaze pass=0 dev=0.0 ins=13.28 pro=70 1a=False 1b=False 2=True (85.6s)
Sep 15 18:53:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:53:02,962 main INFO screen ANON pass=0 dev=0.0 ins=41.74 pro=47 1a=False 1b=False 2=True (56.0s)
Sep 15 18:53:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:53:14,954 main INFO screen CAI pass=0 dev=0.0 ins=20.3 pro=66 1a=False 1b=False 2=False (72.3s)
Sep 15 18:53:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:53:32,191 main INFO screen USMS pass=0 dev=0.76 ins=0.0 pro=4 1a=False 1b=False 2=False (53.8s)
Sep 15 18:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:53:54,771 main INFO screen GayCat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.8s)
Sep 15 18:54:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:54:06,262 main INFO screen ROAR pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.3s)
Sep 15 18:54:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:54:20,384 main INFO screen Blaze pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.2s)
Sep 15 18:54:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:54:47,171 main INFO screen EMPTY pass=0 dev=0.0 ins=55.51 pro=63 1a=False 1b=False 2=True (52.4s)
Sep 15 18:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:54:55,123 main INFO screen HUHCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.9s)
Sep 15 18:55:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:55:05,696 main INFO screen Blaze pass=0 dev=0.0 ins=19.97 pro=13 1a=False 1b=False 2=False (45.3s)
Sep 15 18:55:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:55:21,588 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:55:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T17:48:54Z
--- update 2026-09-15T17:54:07Z
--- update 2026-09-15T17:59:11Z
--- update 2026-09-15T18:04:11Z
Running as unit: schaduwbot-wallets.service; invocation ID: e462df6ecd2e4a138f160f044589f580
analyses gestart (84579ff37485)
--- update 2026-09-15T18:09:12Z
--- update 2026-09-15T18:14:13Z
--- update 2026-09-15T18:19:17Z
nieuwe code: 03bcc03
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:24:20Z
--- update 2026-09-15T18:29:34Z
nieuwe code: 85d446e
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:34:36Z
--- update 2026-09-15T18:39:36Z
--- update 2026-09-15T18:44:43Z
--- update 2026-09-15T18:49:44Z
--- update 2026-09-15T18:55:20Z
```

## Analyses (laatste 40 regels)
```
inactive
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
--- /opt/schaduwbot/vamp.py 13:01:37
13:01:37 tokens lezen
13:01:41 135941 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
13:13:51 6879 lopers, 19 niet-onderscheidende woorden
13:14:53   500/6879 lopers, 4294 koppelingen
13:15:46   1000/6879 lopers, 7299 koppelingen
13:16:30   1500/6879 lopers, 11181 koppelingen
13:17:20   2000/6879 lopers, 15724 koppelingen
13:18:02   2500/6879 lopers, 18375 koppelingen
13:18:35   3000/6879 lopers, 21263 koppelingen
13:19:25   3500/6879 lopers, 25366 koppelingen
13:19:59   4000/6879 lopers, 28115 koppelingen
13:20:55   4500/6879 lopers, 31747 koppelingen
13:21:39   5000/6879 lopers, 34889 koppelingen
13:22:16   5500/6879 lopers, 37799 koppelingen
13:23:41   6000/6879 lopers, 44142 koppelingen
13:24:27   6500/6879 lopers, 47629 koppelingen
13:24:50 uitkomsten uit de trades halen
13:38:33 69698 tokens met een instapkoers
13:38:34 klaar in 2217s: 6879 lopers, 27676 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 13:38:34
--- /opt/schaduwbot/video_replay.py 14:02:16
--- /opt/schaduwbot/video_replay.py 15:02:36
--- /opt/schaduwbot/video_replay.py 16:03:19
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 18:04:11
18:04:12 venster 2026-09-13 06:04 UTC .. nu, 67852 tokens
18:05:01 klaar in 50s: 51584 tokens, 1905 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
18:24:38 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=289 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:24:39 ijk-diagnose: nieuwste migratie 1.9 min oud | migraties 15/60/240 min: 9/42/150 | al gemeten: 710
18:29:35 ijk: +0 van 0 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=289 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:29:35 ijk-diagnose: nieuwste migratie 7.1 min oud | migraties 15/60/240 min: 6/38/146 | al gemeten: 710
18:35:06 ijk: +6 van 6 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=295 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:35:06 ijk-diagnose: nieuwste migratie 1.8 min oud | migraties 15/60/240 min: 10/40/149 | al gemeten: 716
18:39:40 ijk: +1 van 1 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=296 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:39:41 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 7/39/145 | al gemeten: 717
18:45:16 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=301 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:45:16 ijk-diagnose: nieuwste migratie 1.3 min oud | migraties 15/60/240 min: 13/37/149 | al gemeten: 723
18:50:06 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=305 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:50:07 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 12/38/151 | al gemeten: 727
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 4861 | 494 | 486 | 0 | 118 | 3.7 min |
| 09-13 00:00 | 5995 | 675 | 658 | 0 | 295 | 2.3 min |
| 09-13 06:00 | 4301 | 538 | 534 | 0 | 282 | 2.4 min |
| 09-13 12:00 | 6600 | 754 | 741 | 0 | 286 | 2.6 min |
| 09-13 18:00 | 8021 | 920 | 889 | 0 | 118 | 4.0 min |
| 09-14 00:00 | 6068 | 752 | 743 | 0 | 275 | 2.6 min |
| 09-14 06:00 | 4709 | 692 | 683 | 0 | 323 | 2.3 min |
| 09-14 12:00 | 8320 | 1156 | 1091 | 0 | 36 | 16.9 min |
| 09-14 18:00 | 10622 | 1266 | 1153 | 266 | 0 | 94.8 min |
| 09-15 00:00 | 7337 | 881 | 827 | 81 | 0 | 112.5 min |
| 09-15 06:00 | 6072 | 909 | 853 | 1 | 0 | 73.3 min |
| 09-15 12:00 | 9559 | 1051 | 971 | 2 | 0 | 69.3 min |
| 09-15 18:00 | 1542 | 0 | 0 | 0 | 0 | - |

'pas na 2u05' = gescreend nadat de replay het token al had vastgelegd; die tellen nooit mee.


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
