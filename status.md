# Schaduwbot status

- tijd: 2026-09-14 03:40:59 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 13 hours, 54 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 1907/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 76011, "tokens_in_memory": 7258, "msgs": 10293831, "trades": 2157513, "creates": 22736, "decode_fail": 187143, "rpc_calls": 62950, "rpc_errors": 3, "sol_usd": 100.84479120335683, "open_positions": 40, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 03:13:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:02,070 main INFO screen TESSERACT pass=1 dev=0.0 ins=3.01 pro=16 1a=False 1b=False 2=False (81.9s)
Sep 14 03:13:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:33,539 main INFO screen BRAINMUSK pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (64.6s)
Sep 14 03:13:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:53,425 main INFO screen STRAWDOG pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (76.2s)
Sep 14 03:14:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:14:12,494 main INFO screen Bank pass=0 dev=0.0 ins=27.83 pro=50 1a=False 1b=False 2=True (70.4s)
Sep 14 03:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:14:51,356 main INFO screen MWG pass=1 dev=0.0 ins=7.58 pro=62 1a=False 1b=False 2=False (77.8s)
Sep 14 03:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:13,932 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (80.5s)
Sep 14 03:15:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:17,414 main INFO screen $tOp pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.9s)
Sep 14 03:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:36,351 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:15:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:01,315 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (70.0s)
Sep 14 03:16:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:11,879 main INFO screen SOLLADY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 14 03:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:18,908 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.5s)
Sep 14 03:17:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:14,081 main INFO screen vrl pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (72.8s)
Sep 14 03:17:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:26,544 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (74.7s)
Sep 14 03:17:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:33,007 main INFO screen BOB pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (74.1s)
Sep 14 03:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:23,353 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (69.3s)
Sep 14 03:18:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:26,734 main INFO screen Trump pass=0 dev=50.78 ins=0.0 pro=1 1a=False 1b=False 2=True (60.2s)
Sep 14 03:18:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:29,081 main INFO screen ECTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.1s)
Sep 14 03:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:35,927 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=33 1a=False 1b=False 2=False (72.6s)
Sep 14 03:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:35,933 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.2s)
Sep 14 03:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:38,709 main INFO screen FASTER. PU pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (69.6s)
Sep 14 03:20:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:20:37,572 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:20:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:20:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:20:49,714 main INFO screen nothing pass=0 dev=0.0 ins=33.35 pro=72 1a=False 1b=False 2=True (73.8s)
Sep 14 03:20:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:20:51,101 main INFO screen STRAWDOG pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=True 2=True (75.2s)
Sep 14 03:20:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:20:53,860 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (75.1s)
Sep 14 03:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:21:13,227 aiohttp.access INFO 2.27.248.13 [14/Sep/2026:03:21:13 +0000] "GET /login HTTP/1.1" 404 193 "-" "Go-http-client/1.1"
Sep 14 03:22:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:22:00,023 main INFO screen wind pass=0 dev=0.81 ins=0.0 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 14 03:22:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:22:02,459 main INFO screen UberChad pass=0 dev=0.0 ins=18.5 pro=81 1a=False 1b=False 2=True (72.7s)
Sep 14 03:22:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:22:05,361 main INFO screen POON pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (71.5s)
Sep 14 03:23:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:23:09,048 main INFO screen MEOWALD pass=0 dev=0.0 ins=30.13 pro=30 1a=False 1b=False 2=True (63.7s)
Sep 14 03:23:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:23:09,854 main INFO screen Rolex pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (67.4s)
Sep 14 03:23:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:23:13,448 main INFO screen TESSERACT pass=0 dev=31.92 ins=0.24 pro=70 1a=False 1b=False 2=False (73.4s)
Sep 14 03:24:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:24:04,392 main INFO screen STRAWDOG pass=0 dev=35.47 ins=0.0 pro=30 1a=False 1b=True 2=False (55.3s)
Sep 14 03:24:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:24:04,563 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.5s)
Sep 14 03:25:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:25:39,935 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.9s)
Sep 14 03:25:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:25:46,590 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:25:46 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 03:26:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:26:48,544 main INFO screen cap pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (67.4s)
Sep 14 03:26:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:26:49,696 main INFO screen BULLSEM pass=0 dev=0.13 ins=0.0 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 14 03:27:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:27:07,487 main INFO screen hardcock pass=0 dev=3.12 ins=16.32 pro=71 1a=False 1b=False 2=True (71.5s)
Sep 14 03:28:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:28:26,317 main INFO screen OGANT pass=1 dev=0.0 ins=4.6 pro=81 1a=False 1b=False 2=False (67.4s)
Sep 14 03:28:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:28:27,293 main INFO screen ETAC pass=1 dev=0.0 ins=0.21 pro=14 1a=False 1b=False 2=False (72.4s)
Sep 14 03:29:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:29:21,880 main INFO screen Bulljak pass=0 dev=0.35 ins=77.91 pro=8 1a=False 1b=False 2=True (79.1s)
Sep 14 03:30:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:30:12,997 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.9s)
Sep 14 03:30:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:30:25,265 main INFO screen FROBERT pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (56.5s)
Sep 14 03:30:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:30:50,429 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:30:50 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:32:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:32:26,563 main INFO screen FERSPE pass=0 dev=9.85 ins=0.0 pro=2 1a=False 1b=False 2=False (67.3s)
Sep 14 03:33:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:33:08,264 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:03:33:08 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 03:33:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:33:15,281 main INFO screen Mage pass=1 dev=3.42 ins=0.0 pro=18 1a=False 1b=False 2=False (72.2s)
Sep 14 03:33:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:33:31,847 main INFO screen sh4vwty pass=0 dev=0.0 ins=18.71 pro=56 1a=False 1b=False 2=True (58.1s)
Sep 14 03:33:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:33:48,831 main INFO screen beer pass=0 dev=0.07 ins=0.0 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 14 03:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:34:08,307 main INFO screen ZGPT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:35:05,589 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 03:35:05 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 03:35:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:35:31,848 main INFO screen Og pass=1 dev=2.42 ins=6.8 pro=27 1a=False 1b=False 2=False (120.0s)
Sep 14 03:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:35:40,664 main INFO screen kittylick pass=0 dev=0.74 ins=0.0 pro=2 1a=False 1b=False 2=False (111.8s)
Sep 14 03:35:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:35:52,418 main INFO screen TRUMP pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (104.1s)
Sep 14 03:35:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:35:53,777 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:35:53 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:36:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:36:30,451 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.6s)
Sep 14 03:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:36:37,468 main INFO screen MEME pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.8s)
Sep 14 03:37:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:37:02,783 main INFO screen CatDamon pass=0 dev=8.13 ins=0.0 pro=48 1a=False 1b=False 2=False (70.4s)
Sep 14 03:37:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:37:28,950 main INFO screen ECTF pass=0 dev=98.26 ins=0.0 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 14 03:37:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:37:52,046 main INFO screen PICK AUTO pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.6s)
Sep 14 03:38:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:38:13,367 main INFO screen BOWL pass=1 dev=0.0 ins=2.22 pro=78 1a=False 1b=False 2=False (70.6s)
Sep 14 03:38:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:38:34,517 main INFO screen LOS pass=1 dev=0.0 ins=13.55 pro=36 1a=False 1b=False 2=False (65.6s)
Sep 14 03:39:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:39:00,015 main INFO screen tacocat pass=0 dev=0.0 ins=9.75 pro=71 1a=False 1b=False 2=True (68.0s)
Sep 14 03:39:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:39:18,296 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (64.9s)
Sep 14 03:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:39:35,374 main INFO screen enof pass=0 dev=0.0 ins=13.18 pro=66 1a=False 1b=False 2=True (60.9s)
Sep 14 03:39:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:39:50,208 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (50.2s)
Sep 14 03:40:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:29,249 main INFO screen SCRVAN pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (71.0s)
Sep 14 03:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:39,696 main INFO screen . pass=1 dev=0.42 ins=0.0 pro=12 1a=False 1b=False 2=False (64.3s)
Sep 14 03:40:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:45,699 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.5s)
Sep 14 03:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:59,139 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:40:59 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T03:05:21Z
--- update 2026-09-14T03:10:24Z
--- update 2026-09-14T03:15:35Z
--- update 2026-09-14T03:20:36Z
--- update 2026-09-14T03:25:45Z
--- update 2026-09-14T03:30:49Z
--- update 2026-09-14T03:35:52Z
--- update 2026-09-14T03:40:58Z
```

## Analyses (laatste 25 regels)
```
inactive
03:21:51   32000 tokens, 3238043 trades, 422854 posities (177s)
03:22:04   34000 tokens, 3461147 trades, 451926 posities (191s)
03:22:17   36000 tokens, 3662732 trades, 479673 posities (204s)
03:22:31   38000 tokens, 3865753 trades, 505063 posities (218s)
03:22:43   40000 tokens, 4045000 trades, 525732 posities (230s)
03:22:57   42000 tokens, 4249962 trades, 552995 posities (244s)
03:23:10   44000 tokens, 4446595 trades, 578153 posities (257s)
03:23:24   46000 tokens, 4659194 trades, 606292 posities (270s)
03:23:36   48000 tokens, 4854158 trades, 628527 posities (283s)
03:23:48   50000 tokens, 5042947 trades, 653903 posities (295s)
03:24:00   52000 tokens, 5230122 trades, 676078 posities (307s)
03:24:11   54000 tokens, 5422843 trades, 703819 posities (318s)
03:24:23   56000 tokens, 5615846 trades, 727463 posities (330s)
03:24:35   58000 tokens, 5810050 trades, 754947 posities (341s)
03:24:47   60000 tokens, 6031857 trades, 786254 posities (354s)
03:24:57   62000 tokens, 6234325 trades, 813935 posities (364s)
03:25:07   64000 tokens, 6430429 trades, 840854 posities (374s)
03:25:18   66000 tokens, 6647572 trades, 880931 posities (385s)
03:25:28   68000 tokens, 6828531 trades, 905157 posities (394s)
03:25:28 posities: 907715 uit 6836758 trades (398s)
03:25:40 194054 wallets gerekend
03:25:40 geluk-toets
03:26:14 persistentie
03:26:17 kopieer-simulatie
03:28:13 klaar in 563s -> /opt/schaduwbot/reports/wallets.md
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
