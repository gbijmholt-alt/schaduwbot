# Schaduwbot status

- tijd: 2026-09-14 21:45:07 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 7 hours, 58 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.4G/38G | geheugen: 2218/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 141059, "tokens_in_memory": 11154, "msgs": 20212685, "trades": 4200773, "creates": 44433, "decode_fail": 370301, "rpc_calls": 119319, "rpc_errors": 7, "sol_usd": 103.28459954589314, "open_positions": 61, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 21:23:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:37,284 main INFO screen SAKE pass=0 dev=0.0 ins=1.1 pro=18 1a=False 1b=False 2=False (80.1s)
Sep 14 21:23:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:37,471 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:23:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 21:23:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:38,526 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (80.2s)
Sep 14 21:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:47,066 main INFO screen Olive pass=0 dev=0.0 ins=20.09 pro=2 1a=False 1b=False 2=False (73.2s)
Sep 14 21:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:24:47,984 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.5s)
Sep 14 21:24:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:24:56,107 main INFO screen how pass=0 dev=0.03 ins=0.0 pro=1 1a=False 1b=False 2=False (78.8s)
Sep 14 21:25:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:25:00,876 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.8s)
Sep 14 21:25:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:25:43,785 main INFO screen Lil Wig pass=0 dev=0.0 ins=15.58 pro=45 1a=False 1b=False 2=False (55.8s)
Sep 14 21:26:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:26:08,591 main INFO screen SEMIHARD pass=0 dev=0.0 ins=19.52 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 14 21:26:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:26:11,945 main INFO screen SEMI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.1s)
Sep 14 21:26:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:26:36,483 main INFO screen Pot pass=0 dev=0.0 ins=25.81 pro=83 1a=False 1b=False 2=True (52.7s)
Sep 14 21:27:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:27:11,542 main INFO screen Pot pass=0 dev=0.0 ins=20.86 pro=4 1a=False 1b=False 2=True (59.6s)
Sep 14 21:27:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:27:17,162 main INFO screen memerot pass=0 dev=0.0 ins=3.0 pro=70 1a=False 1b=False 2=False (68.6s)
Sep 14 21:27:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:27:33,863 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 14 21:27:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:27:47,482 aiohttp.access INFO 192.248.150.180 [14/Sep/2026:21:27:47 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CyberConvoyScout/1.0; +https://scout.cyberconvoy.co)"
Sep 14 21:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:28:23,561 main INFO screen PINMO pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (72.0s)
Sep 14 21:28:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:28:30,005 main INFO screen FBMB  pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (72.8s)
Sep 14 21:28:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:28:34,442 main INFO screen inu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.6s)
Sep 14 21:28:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:28:55,675 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:28:55 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 21:29:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:29:23,120 main INFO screen ACD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.6s)
Sep 14 21:29:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:29:25,470 main INFO screen alien pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.5s)
Sep 14 21:29:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:29:43,915 main INFO screen SLOP pass=0 dev=0.0 ins=23.23 pro=59 1a=False 1b=False 2=True (69.5s)
Sep 14 21:30:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:30:21,334 main INFO screen tɐɔ pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.2s)
Sep 14 21:30:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:30:33,008 main INFO screen GROKCOIN pass=0 dev=0.0 ins=20.57 pro=2 1a=False 1b=False 2=False (49.1s)
Sep 14 21:30:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:30:35,344 main INFO screen boner pass=0 dev=0.0 ins=25.39 pro=3 1a=False 1b=False 2=True (69.9s)
Sep 14 21:31:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:31:16,796 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.5s)
Sep 14 21:31:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:31:23,078 main INFO screen MENSA META pass=0 dev=0.0 ins=27.56 pro=16 1a=False 1b=False 2=True (47.7s)
Sep 14 21:31:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:31:27,816 main INFO screen META pass=0 dev=0.0 ins=19.24 pro=53 1a=False 1b=False 2=True (54.8s)
Sep 14 21:32:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:32:08,391 main INFO screen MENSA pass=0 dev=0.0 ins=21.25 pro=17 1a=False 1b=False 2=True (51.6s)
Sep 14 21:32:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:32:23,850 main INFO screen yyt pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 14 21:32:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:32:33,658 main INFO screen $EPFILES pass=0 dev=1.33 ins=0.0 pro=1 1a=False 1b=False 2=False (65.8s)
Sep 14 21:33:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:33:03,341 main INFO screen MM pass=0 dev=0.0 ins=19.76 pro=4 1a=False 1b=False 2=True (54.9s)
Sep 14 21:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:33:18,702 main INFO screen SAFFRON pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (54.8s)
Sep 14 21:33:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:33:43,872 main INFO screen ozempork pass=0 dev=0.0 ins=15.28 pro=66 1a=False 1b=False 2=False (70.2s)
Sep 14 21:34:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:34:04,286 main INFO screen WOFI pass=0 dev=0.0 ins=153.3 pro=1 1a=False 1b=False 2=True (60.9s)
Sep 14 21:34:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:34:19,540 main INFO screen DOBER pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:35:25,855 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 21:35:25 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 21:35:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:35:26,031 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:35:26 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:35:28,669 main INFO screen WH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (104.8s)
Sep 14 21:35:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:35:51,742 main INFO screen TRIKE pass=0 dev=0.0 ins=1.19 pro=22 1a=False 1b=False 2=False (107.5s)
Sep 14 21:36:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:36:07,909 main INFO screen BHS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (108.4s)
Sep 14 21:36:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:36:25,204 main INFO screen WEST pass=0 dev=0.0 ins=27.82 pro=11 1a=False 1b=False 2=True (56.5s)
Sep 14 21:36:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:36:52,500 main INFO screen 5050coin pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 14 21:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:37:06,436 main INFO screen SEMIHARD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 14 21:37:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:37:25,671 main INFO screen sperm pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (60.5s)
Sep 14 21:37:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:37:53,043 main INFO screen USD pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (60.5s)
Sep 14 21:38:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:38:13,543 main INFO screen CATE pass=0 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (67.1s)
Sep 14 21:38:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:38:33,562 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (67.9s)
Sep 14 21:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:39:02,458 main INFO screen BRADPIT pass=0 dev=0.67 ins=0.0 pro=4 1a=False 1b=False 2=False (69.4s)
Sep 14 21:39:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:39:10,918 main INFO screen ☉ pass=0 dev=0.0 ins=23.37 pro=29 1a=False 1b=False 2=True (57.4s)
Sep 14 21:39:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:39:31,134 main INFO screen BEAST pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 14 21:39:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:39:41,173 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:39:41 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:40:00,602 main INFO screen PROPUTER pass=0 dev=0.0 ins=16.45 pro=39 1a=False 1b=False 2=False (58.1s)
Sep 14 21:40:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:40:14,556 main INFO screen Callr pass=0 dev=0.0 ins=50.0 pro=49 1a=False 1b=False 2=True (63.6s)
Sep 14 21:40:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:40:32,304 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 14 21:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:40:59,899 main INFO screen PERPSPAD pass=0 dev=0.0 ins=24.44 pro=22 1a=False 1b=False 2=False (59.3s)
Sep 14 21:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:41:11,083 main INFO screen DUDE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 14 21:41:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:41:25,842 main INFO screen DONDUMP pass=0 dev=0.0 ins=77.59 pro=1 1a=False 1b=True 2=True (53.5s)
Sep 14 21:41:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:41:42,319 aiohttp.access INFO 80.66.83.43 [14/Sep/2026:21:41:42 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 14 21:42:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:42:07,493 main INFO screen GWARY pass=0 dev=0.0 ins=16.65 pro=73 1a=False 1b=False 2=True (67.6s)
Sep 14 21:42:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:42:15,961 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (64.9s)
Sep 14 21:42:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:42:19,211 main INFO screen ALONCOIN pass=0 dev=0.0 ins=31.81 pro=68 1a=False 1b=False 2=True (53.4s)
Sep 14 21:43:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:43:03,204 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (55.7s)
Sep 14 21:43:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:43:09,313 main INFO screen @BROKE pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (53.4s)
Sep 14 21:43:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:43:12,137 main INFO screen BULLS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.9s)
Sep 14 21:43:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:43:54,534 main INFO screen Apple pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (51.3s)
Sep 14 21:44:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:44:17,657 main INFO screen Callr pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (65.5s)
Sep 14 21:44:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:44:18,612 main INFO screen BANKNOTES pass=0 dev=0.0 ins=25.73 pro=3 1a=False 1b=False 2=True (69.3s)
Sep 14 21:44:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:44:50,432 main INFO screen RAVIOLI pass=0 dev=0.0 ins=33.15 pro=69 1a=False 1b=False 2=True (55.9s)
Sep 14 21:45:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:45:07,171 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:45:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T20:47:34Z
nieuwe code: a1e210f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T20:52:35Z
Running as unit: schaduwbot-wallets.service; invocation ID: 69a69562f5464aaa85ae3e414157ea6c
analyses gestart (d1af81359b25)
--- update 2026-09-14T20:57:35Z
--- update 2026-09-14T21:02:36Z
nieuwe code: 2a95007
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T21:07:54Z
--- update 2026-09-14T21:13:21Z
--- update 2026-09-14T21:18:29Z
--- update 2026-09-14T21:23:36Z
--- update 2026-09-14T21:28:54Z
--- update 2026-09-14T21:34:36Z
--- update 2026-09-14T21:39:39Z
--- update 2026-09-14T21:45:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5eee46075898481b8005cdd132a55989
analyses gestart (96a46d7e3c26)
```

## Analyses (laatste 25 regels)
```
active
21:31:52   38000 tokens, 3743377 trades, 455514 posities (259s)
21:32:05   40000 tokens, 3932772 trades, 480452 posities (272s)
21:32:20   42000 tokens, 4121390 trades, 499624 posities (286s)
21:32:33   44000 tokens, 4296406 trades, 521714 posities (299s)
21:32:47   46000 tokens, 4485463 trades, 545032 posities (313s)
21:33:01   48000 tokens, 4664503 trades, 566214 posities (328s)
21:33:16   50000 tokens, 4871126 trades, 589726 posities (342s)
21:33:30   52000 tokens, 5078167 trades, 615443 posities (357s)
21:33:45   54000 tokens, 5273459 trades, 641899 posities (372s)
21:33:59   56000 tokens, 5439920 trades, 661005 posities (385s)
21:34:15   58000 tokens, 5643555 trades, 687424 posities (401s)
21:34:28   60000 tokens, 5818611 trades, 707093 posities (415s)
21:34:45   62000 tokens, 6024213 trades, 733475 posities (432s)
21:35:02   64000 tokens, 6220746 trades, 761948 posities (448s)
21:35:20   66000 tokens, 6434588 trades, 789894 posities (466s)
21:35:36   68000 tokens, 6618972 trades, 815082 posities (483s)
21:35:52   70000 tokens, 6811620 trades, 838817 posities (499s)
21:36:08   72000 tokens, 7007378 trades, 867280 posities (515s)
21:36:24   74000 tokens, 7207555 trades, 898587 posities (531s)
21:36:28 posities: 902419 uit 7239579 trades (537s)
21:36:41 209406 wallets gerekend
21:36:41 geluk-toets
21:37:17 persistentie
21:37:20 kopieer-simulatie
21:39:47 klaar in 736s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
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
20:52:38 ijk: +0 van 0 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 9}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:52:39 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 9/43/182 | al gemeten: 229
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
