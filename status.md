# Schaduwbot status

- tijd: 2026-09-14 20:52:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 7 hours, 5 minutes
- bot-service: active
- code-versie: a1e210f
- schijf: 6.3G/38G | geheugen: 2145/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 137908, "tokens_in_memory": 10645, "msgs": 19441994, "trades": 4063824, "creates": 42868, "decode_fail": 358476, "rpc_calls": 116239, "rpc_errors": 7, "sol_usd": 104.4428554252597, "open_positions": 67, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 20:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:30:48,421 main INFO screen chud pass=0 dev=0.0 ins=48.51 pro=23 1a=False 1b=False 2=True (54.5s)
Sep 14 20:31:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:31:20,388 main INFO screen HOMO pass=0 dev=0.0 ins=20.99 pro=3 1a=False 1b=False 2=False (71.6s)
Sep 14 20:31:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:31:43,324 aiohttp.access INFO 47.254.245.239 [14/Sep/2026:20:31:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 20:31:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:31:43,663 aiohttp.access INFO 47.254.245.239 [14/Sep/2026:20:31:43 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 14 20:32:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:32:01,075 main INFO screen $HOLD pass=0 dev=34.35 ins=44.96 pro=0 1a=False 1b=True 2=True (72.7s)
Sep 14 20:32:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:32:08,518 main INFO screen SM pass=0 dev=0.11 ins=0.0 pro=6 1a=False 1b=False 2=False (81.6s)
Sep 14 20:32:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:32:23,432 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:32:23 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:32:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:32:34,348 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (74.0s)
Sep 14 20:32:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:32:58,694 main INFO screen PIKACHU pass=0 dev=0.0 ins=160.53 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 14 20:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:33:17,744 main INFO screen INU pass=0 dev=0.0 ins=50.72 pro=37 1a=False 1b=False 2=True (69.2s)
Sep 14 20:33:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:33:27,871 main INFO screen BTC pass=0 dev=0.0 ins=18.18 pro=7 1a=False 1b=False 2=True (53.5s)
Sep 14 20:34:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:34:01,481 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.8s)
Sep 14 20:34:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:34:21,781 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.0s)
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:35:18,967 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 20:35:18 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 20:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:35:19,668 main INFO screen Value pass=0 dev=0.0 ins=18.42 pro=5 1a=False 1b=False 2=True (111.8s)
Sep 14 20:35:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:35:46,604 main INFO screen lol pass=0 dev=0.0 ins=55.79 pro=27 1a=False 1b=False 2=True (105.1s)
Sep 14 20:36:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:36:05,914 aiohttp.access INFO 94.154.43.254 [14/Sep/2026:20:36:05 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 20:36:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:36:08,524 main INFO screen FAIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (106.7s)
Sep 14 20:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:36:27,575 main INFO screen Octop pass=0 dev=0.0 ins=11.48 pro=39 1a=False 1b=False 2=False (67.9s)
Sep 14 20:36:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:36:50,840 main INFO screen Hamster pass=0 dev=0.0 ins=22.03 pro=11 1a=False 1b=False 2=True (64.2s)
Sep 14 20:37:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:37:09,966 main INFO screen DILLOTON pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (61.4s)
Sep 14 20:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:37:24,411 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:37:24 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 20:37:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:37:42,214 main INFO screen ZSDC pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (74.6s)
Sep 14 20:37:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:37:58,791 main INFO screen Puter pass=0 dev=0.0 ins=19.16 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 14 20:38:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:38:35,631 main INFO screen $BBCAT pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (85.7s)
Sep 14 20:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:38:55,421 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.2s)
Sep 14 20:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:39:05,575 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 14 20:39:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:39:40,954 main INFO screen wonke pass=0 dev=0.0 ins=3.43 pro=15 1a=False 1b=False 2=False (65.3s)
Sep 14 20:39:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:39:56,649 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.2s)
Sep 14 20:40:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:40:11,979 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (66.4s)
Sep 14 20:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:40:46,934 main INFO screen STONKS pass=0 dev=0.0 ins=19.59 pro=2 1a=False 1b=False 2=True (66.0s)
Sep 14 20:40:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:40:52,809 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 14 20:41:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:41:15,002 main INFO screen AT pass=0 dev=0.0 ins=40.99 pro=4 1a=False 1b=False 2=True (63.0s)
Sep 14 20:41:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:41:54,213 main INFO screen SCOOT pass=0 dev=0.0 ins=1.72 pro=6 1a=False 1b=False 2=False (61.4s)
Sep 14 20:41:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:41:55,332 main INFO screen STONKS pass=0 dev=0.0 ins=20.57 pro=5 1a=False 1b=False 2=True (68.4s)
Sep 14 20:42:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:42:03,259 main INFO screen WOFI pass=0 dev=0.0 ins=127.11 pro=0 1a=False 1b=False 2=True (48.3s)
Sep 14 20:42:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:42:35,726 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:42:35 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:42:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:42:42,436 main INFO screen HD pass=0 dev=0.0 ins=0.88 pro=8 1a=False 1b=False 2=False (48.2s)
Sep 14 20:42:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:42:42,794 main INFO screen PAMP pass=0 dev=0.0 ins=39.18 pro=4 1a=False 1b=False 2=True (47.5s)
Sep 14 20:42:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:42:51,684 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.4s)
Sep 14 20:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:43:53,129 main INFO screen PROPHET pass=0 dev=0.0 ins=16.27 pro=74 1a=False 1b=False 2=True (70.3s)
Sep 14 20:43:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:43:54,646 main INFO screen wheeliam pass=0 dev=1.23 ins=0.0 pro=29 1a=False 1b=False 2=False (72.2s)
Sep 14 20:43:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:43:59,600 main INFO screen hard pass=0 dev=0.0 ins=18.59 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 14 20:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:44:59,958 main INFO screen HEAVES pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.3s)
Sep 14 20:45:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:45:01,504 main INFO screen Goblin pass=0 dev=0.0 ins=52.11 pro=29 1a=False 1b=False 2=True (68.4s)
Sep 14 20:45:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:45:03,151 main INFO screen Face pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 14 20:45:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:45:51,539 main INFO screen PROPHET pass=0 dev=0.0 ins=40.39 pro=2 1a=False 1b=False 2=True (51.6s)
Sep 14 20:45:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:45:57,666 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.2s)
Sep 14 20:46:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:46:01,951 main INFO screen $roket pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.8s)
Sep 14 20:46:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:46:47,496 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (56.0s)
Sep 14 20:46:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:46:57,481 main INFO screen DripCat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.8s)
Sep 14 20:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:47:10,948 main INFO screen llamar pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=True (69.0s)
Sep 14 20:47:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:47:36,244 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:47:36 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:47:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:47:42,876 main INFO screen GCC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.4s)
Sep 14 20:47:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:47:58,130 main INFO screen Agentic pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (60.6s)
Sep 14 20:48:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:48:11,210 main INFO screen Sunny pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (60.3s)
Sep 14 20:48:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:48:39,524 main INFO screen CHILLBIKE pass=0 dev=0.0 ins=77.59 pro=2 1a=False 1b=True 2=True (56.6s)
Sep 14 20:48:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:48:55,387 main INFO screen GCP pass=0 dev=0.0 ins=20.06 pro=5 1a=False 1b=False 2=True (57.3s)
Sep 14 20:49:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:49:07,406 main INFO screen pumpoids pass=0 dev=0.0 ins=51.95 pro=20 1a=False 1b=False 2=True (56.2s)
Sep 14 20:49:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:49:32,817 main INFO screen fone pass=0 dev=0.0 ins=138.52 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 14 20:50:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:50:12,545 main INFO screen FOID pass=0 dev=0.09 ins=6.35 pro=50 1a=False 1b=False 2=False (77.2s)
Sep 14 20:50:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:50:14,469 main INFO screen SOLCAT pass=0 dev=0.0 ins=103.38 pro=0 1a=False 1b=False 2=True (67.1s)
Sep 14 20:50:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:50:36,064 main INFO screen pumpoids pass=0 dev=0.0 ins=24.49 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 14 20:51:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:51:11,693 main INFO screen ZIKETYSON pass=0 dev=0.0 ins=30.68 pro=8 1a=False 1b=False 2=True (57.2s)
Sep 14 20:51:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:51:21,094 main INFO screen Unicoin pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.5s)
Sep 14 20:51:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:51:37,284 main INFO screen birdy pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.2s)
Sep 14 20:52:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:52:06,425 main INFO screen $DRM pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.7s)
Sep 14 20:52:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:52:13,362 main INFO screen punch pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (52.3s)
Sep 14 20:52:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:52:22,529 main INFO screen Rabbit pass=0 dev=0.0 ins=5.11 pro=29 1a=False 1b=False 2=False (45.2s)
Sep 14 20:52:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:52:36,609 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:52:36 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T19:56:58Z
--- update 2026-09-14T20:02:03Z
Running as unit: schaduwbot-wallets.service; invocation ID: 14498679f71340f08b872ad37a3b0138
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T20:07:06Z
--- update 2026-09-14T20:12:06Z
--- update 2026-09-14T20:17:06Z
--- update 2026-09-14T20:22:15Z
--- update 2026-09-14T20:27:19Z
--- update 2026-09-14T20:32:22Z
--- update 2026-09-14T20:37:22Z
nieuwe code: a8c6844
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T20:42:34Z
--- update 2026-09-14T20:47:34Z
nieuwe code: a1e210f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T20:52:35Z
Running as unit: schaduwbot-wallets.service; invocation ID: 69a69562f5464aaa85ae3e414157ea6c
analyses gestart (d1af81359b25)
```

## Analyses (laatste 25 regels)
```
active
20:44:55   36000 tokens, 3568860 trades, 437102 posities (232s)
20:45:09   38000 tokens, 3781949 trades, 464087 posities (246s)
20:45:21   40000 tokens, 3967385 trades, 486231 posities (258s)
20:45:34   42000 tokens, 4157662 trades, 507282 posities (271s)
20:45:45   44000 tokens, 4322636 trades, 527168 posities (282s)
20:45:58   46000 tokens, 4522383 trades, 552373 posities (295s)
20:46:11   48000 tokens, 4704635 trades, 572813 posities (308s)
20:46:25   50000 tokens, 4914694 trades, 597995 posities (322s)
20:46:39   52000 tokens, 5120602 trades, 621791 posities (336s)
20:46:53   54000 tokens, 5304872 trades, 644984 posities (350s)
20:47:06   56000 tokens, 5478249 trades, 663537 posities (363s)
20:47:20   58000 tokens, 5682727 trades, 691085 posities (377s)
20:47:32   60000 tokens, 5866102 trades, 712320 posities (389s)
20:47:48   62000 tokens, 6069191 trades, 740329 posities (405s)
20:48:03   64000 tokens, 6272962 trades, 767558 posities (420s)
20:48:18   66000 tokens, 6478018 trades, 796166 posities (435s)
20:48:33   68000 tokens, 6666150 trades, 819968 posities (450s)
20:48:47   70000 tokens, 6869168 trades, 845817 posities (465s)
20:49:04   72000 tokens, 7083937 trades, 885573 posities (481s)
20:49:16 posities: 901948 uit 7229176 trades (497s)
20:49:29 206737 wallets gerekend
20:49:29 geluk-toets
20:50:05 persistentie
20:50:09 kopieer-simulatie
20:52:32 klaar in 693s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
20:37:27 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:37:27 ijk-diagnose: nieuwste migratie 3.1 min oud | migraties 15/60/240 min: 13/46/185 | al gemeten: 229
20:42:38 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:42:38 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 16/48/184 | al gemeten: 229
20:47:38 ijk: +0 van 0 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 11}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:47:39 ijk-diagnose: nieuwste migratie 3.5 min oud | migraties 15/60/240 min: 11/45/183 | al gemeten: 229
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
