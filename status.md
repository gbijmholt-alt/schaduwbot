# Schaduwbot status

- tijd: 2026-09-15 02:37:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 12 hours, 50 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.7G/38G | geheugen: 2534/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 158609, "tokens_in_memory": 9372, "msgs": 24314469, "trades": 4846035, "creates": 51681, "decode_fail": 416556, "rpc_calls": 136657, "rpc_errors": 13, "sol_usd": 102.14170386767647, "open_positions": 18, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 02:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:13:11,219 main INFO screen LOS pass=0 dev=0.0 ins=30.23 pro=48 1a=False 1b=False 2=True (50.0s)
Sep 15 02:13:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:13:57,686 main INFO screen $WAGE pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (67.7s)
Sep 15 02:14:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:14:17,169 main INFO screen RA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.9s)
Sep 15 02:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:14:18,481 main INFO screen JUDE pass=0 dev=0.0 ins=11.01 pro=71 1a=False 1b=False 2=True (69.0s)
Sep 15 02:15:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:01,651 main INFO screen Clasiclux pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.0s)
Sep 15 02:15:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:31,075 main INFO screen FART pass=0 dev=1.05 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 15 02:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:35,557 main INFO screen SPAMCAT pass=0 dev=0.0 ins=28.42 pro=60 1a=False 1b=False 2=True (78.4s)
Sep 15 02:16:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:03,749 main INFO screen MEEK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.1s)
Sep 15 02:16:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:45,583 main INFO screen ISHOWSPEED pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.0s)
Sep 15 02:16:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:52,540 main INFO screen Bob pass=0 dev=0.0 ins=24.04 pro=68 1a=False 1b=False 2=True (81.5s)
Sep 15 02:17:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:17:07,563 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:17:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:17:15,191 main INFO screen WOJAKTYSON pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (71.4s)
Sep 15 02:18:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:10,801 main INFO screen BUFF pass=0 dev=0.0 ins=9.29 pro=60 1a=False 1b=False 2=False (85.2s)
Sep 15 02:18:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:16,116 main INFO screen NETO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (83.6s)
Sep 15 02:18:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:24,672 main INFO screen bundloor pass=0 dev=0.0 ins=21.1 pro=49 1a=False 1b=False 2=True (69.5s)
Sep 15 02:19:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:34,522 main INFO screen Jizz pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (78.4s)
Sep 15 02:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:38,806 main INFO screen BEARISH pass=0 dev=0.21 ins=0.0 pro=15 1a=False 1b=False 2=False (88.0s)
Sep 15 02:19:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:40,510 main INFO screen Bridge402 pass=0 dev=39.93 ins=0.0 pro=60 1a=False 1b=False 2=True (75.8s)
Sep 15 02:20:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:32,480 main INFO screen Rolex pass=0 dev=0.0 ins=175.36 pro=0 1a=False 1b=False 2=True (58.0s)
Sep 15 02:20:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:43,516 main INFO screen Museum pass=0 dev=0.0 ins=33.47 pro=27 1a=False 1b=False 2=True (63.0s)
Sep 15 02:20:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:49,004 main INFO screen SAN pass=0 dev=0.0 ins=11.61 pro=27 1a=False 1b=False 2=True (70.2s)
Sep 15 02:21:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:21:39,124 main INFO screen pumpoids pass=0 dev=0.0 ins=17.11 pro=27 1a=False 1b=False 2=True (55.6s)
Sep 15 02:21:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:21:50,849 main INFO screen JUDE pass=0 dev=0.0 ins=19.49 pro=57 1a=False 1b=False 2=False (78.4s)
Sep 15 02:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:06,930 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (77.9s)
Sep 15 02:22:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:08,135 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:22:08 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 02:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:31,222 main INFO screen Bridge402 pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (52.1s)
Sep 15 02:22:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:58,255 main INFO screen AI pass=0 dev=0.0 ins=26.01 pro=60 1a=False 1b=False 2=True (67.4s)
Sep 15 02:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:23:17,469 main INFO screen INSTAR pass=0 dev=5.0 ins=4.24 pro=51 1a=False 1b=False 2=True (70.5s)
Sep 15 02:23:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:23:45,678 main INFO screen DERP pass=0 dev=0.0 ins=46.02 pro=9 1a=False 1b=False 2=True (74.5s)
Sep 15 02:24:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:12,981 main INFO screen GS pass=0 dev=0.0 ins=23.99 pro=39 1a=False 1b=False 2=True (74.7s)
Sep 15 02:24:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:30,972 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (73.5s)
Sep 15 02:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:49,091 main INFO screen DUO pass=0 dev=0.0 ins=31.63 pro=54 1a=False 1b=True 2=True (63.4s)
Sep 15 02:25:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:25:08,435 main INFO screen tiger pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.5s)
Sep 15 02:25:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:25:29,433 main INFO screen cappykidd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 15 02:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:04,549 main INFO screen 天議論 pass=0 dev=0.0 ins=28.96 pro=64 1a=False 1b=False 2=True (75.5s)
Sep 15 02:26:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:19,351 main INFO screen Hedge pass=0 dev=0.0 ins=16.35 pro=30 1a=False 1b=False 2=True (70.9s)
Sep 15 02:26:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:34,037 main INFO screen GS pass=0 dev=0.0 ins=40.9 pro=36 1a=False 1b=False 2=True (64.6s)
Sep 15 02:27:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:11,034 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:27:11 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:27:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:20,412 main INFO screen Papoy pass=0 dev=0.0 ins=16.9 pro=44 1a=False 1b=False 2=False (75.9s)
Sep 15 02:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:41,737 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (67.7s)
Sep 15 02:27:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:44,243 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (84.9s)
Sep 15 02:28:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:17,051 main INFO screen Lanaroads pass=0 dev=0.0 ins=4.96 pro=45 1a=False 1b=False 2=False (56.6s)
Sep 15 02:28:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:41,991 main INFO screen JUDE pass=0 dev=0.0 ins=12.61 pro=56 1a=False 1b=False 2=True (60.3s)
Sep 15 02:28:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:59,378 main INFO screen QUVO pass=0 dev=0.0 ins=18.42 pro=19 1a=False 1b=False 2=True (75.1s)
Sep 15 02:29:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:29:23,595 main INFO screen Q50 coin pass=0 dev=0.04 ins=0.0 pro=4 1a=False 1b=False 2=False (66.5s)
Sep 15 02:29:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:29:45,291 main INFO screen Nbaton pass=0 dev=0.0 ins=21.51 pro=3 1a=False 1b=False 2=False (63.3s)
Sep 15 02:30:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:05,991 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.74 pro=26 1a=False 1b=False 2=True (66.6s)
Sep 15 02:30:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:18,955 main INFO screen PENIS pass=0 dev=0.0 ins=32.69 pro=25 1a=False 1b=False 2=True (55.4s)
Sep 15 02:30:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:45,624 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (60.3s)
Sep 15 02:31:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:01,293 main INFO screen JUDE pass=0 dev=0.0 ins=78.96 pro=0 1a=True 1b=True 2=True (55.3s)
Sep 15 02:31:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:10,364 main INFO screen USGR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 15 02:31:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:46,799 main INFO screen MEME pass=0 dev=0.0 ins=37.3 pro=67 1a=False 1b=False 2=True (61.2s)
Sep 15 02:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:32:14,146 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:32:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:32:14,299 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.43 pro=16 1a=False 1b=False 2=True (63.9s)
Sep 15 02:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:32:14,995 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.7s)
Sep 15 02:32:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:32:44,449 main INFO screen SRZN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 02:33:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:33:06,856 main INFO screen Gang pass=0 dev=0.0 ins=3.63 pro=35 1a=False 1b=False 2=False (52.6s)
Sep 15 02:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:33:13,993 main INFO screen pump pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 15 02:33:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:33:39,726 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.02 pro=13 1a=False 1b=False 2=True (55.3s)
Sep 15 02:33:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:33:59,529 main INFO screen 天議論 pass=0 dev=0.0 ins=38.26 pro=52 1a=False 1b=False 2=True (52.7s)
Sep 15 02:34:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:34:14,745 main INFO screen DEBATER pass=0 dev=0.0 ins=23.47 pro=67 1a=False 1b=False 2=True (60.8s)
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:35:27,301 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 02:35:27 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 02:35:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:35:30,114 main INFO screen Kirk pass=0 dev=0.0 ins=29.94 pro=45 1a=False 1b=False 2=True (110.4s)
Sep 15 02:35:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:35:48,916 main INFO screen 50SCENT pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (109.4s)
Sep 15 02:36:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:36:18,512 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (123.8s)
Sep 15 02:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:36:27,632 main INFO screen MEMEMAN pass=0 dev=0.0 ins=10.25 pro=61 1a=False 1b=False 2=True (57.5s)
Sep 15 02:36:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:36:57,926 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.05 pro=33 1a=False 1b=False 2=True (69.0s)
Sep 15 02:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:37:06,370 main INFO screen BOBBI pass=0 dev=0.0 ins=26.97 pro=21 1a=False 1b=False 2=True (47.9s)
Sep 15 02:37:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:37:22,980 main INFO screen fihdih pass=0 dev=0.0 ins=18.14 pro=28 1a=False 1b=False 2=True (55.3s)
Sep 15 02:37:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:37:37,507 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:37:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T01:09:36Z
--- update 2026-09-15T01:15:15Z
--- update 2026-09-15T01:20:32Z
--- update 2026-09-15T01:25:36Z
--- update 2026-09-15T01:30:37Z
--- update 2026-09-15T01:35:39Z
--- update 2026-09-15T01:40:45Z
--- update 2026-09-15T01:46:14Z
--- update 2026-09-15T01:51:16Z
Running as unit: schaduwbot-wallets.service; invocation ID: 198697cd6df2473cb461b6a874faa3b9
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T01:56:31Z
--- update 2026-09-15T02:01:36Z
--- update 2026-09-15T02:06:42Z
--- update 2026-09-15T02:11:49Z
--- update 2026-09-15T02:17:06Z
--- update 2026-09-15T02:22:06Z
--- update 2026-09-15T02:27:10Z
--- update 2026-09-15T02:32:12Z
--- update 2026-09-15T02:37:36Z
```

## Analyses (laatste 25 regels)
```
active
02:31:54   4000 tokens, 397218 trades, 51398 posities (30s)
02:32:07   6000 tokens, 588812 trades, 71889 posities (43s)
02:32:18   8000 tokens, 756426 trades, 86497 posities (55s)
02:32:31   10000 tokens, 946267 trades, 108636 posities (67s)
02:32:44   12000 tokens, 1140175 trades, 136894 posities (80s)
02:32:57   14000 tokens, 1343753 trades, 161497 posities (94s)
02:33:10   16000 tokens, 1535351 trades, 182780 posities (106s)
02:33:23   18000 tokens, 1725684 trades, 205187 posities (119s)
02:33:35   20000 tokens, 1901131 trades, 222752 posities (131s)
02:33:49   22000 tokens, 2119736 trades, 244980 posities (145s)
02:34:03   24000 tokens, 2317216 trades, 273969 posities (159s)
02:34:18   26000 tokens, 2531966 trades, 302109 posities (175s)
02:34:32   28000 tokens, 2712250 trades, 324473 posities (189s)
02:34:46   30000 tokens, 2898630 trades, 346942 posities (202s)
02:35:00   32000 tokens, 3097268 trades, 371520 posities (216s)
02:35:14   34000 tokens, 3278138 trades, 390675 posities (230s)
02:35:30   36000 tokens, 3481435 trades, 417851 posities (246s)
02:35:45   38000 tokens, 3672841 trades, 438922 posities (261s)
02:35:59   40000 tokens, 3868151 trades, 465286 posities (275s)
02:36:13   42000 tokens, 4050923 trades, 484626 posities (289s)
02:36:26   44000 tokens, 4229969 trades, 507070 posities (302s)
02:36:40   46000 tokens, 4404490 trades, 527503 posities (316s)
02:36:54   48000 tokens, 4583089 trades, 547292 posities (330s)
02:37:09   50000 tokens, 4783817 trades, 571729 posities (345s)
02:37:24   52000 tokens, 4998695 trades, 600377 posities (361s)
```

## IJking poolkoers (laatste 12 regels)
```
01:25:42 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=77 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:25:42 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 8/40/164 | al gemeten: 372
01:30:43 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=79 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:30:43 ijk-diagnose: nieuwste migratie 1.8 min oud | migraties 15/60/240 min: 8/39/158 | al gemeten: 374
01:35:51 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=83 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:35:52 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 8/41/158 | al gemeten: 378
01:40:57 ijk: +4 van 4 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=85 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:40:57 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 10/43/158 | al gemeten: 382
01:46:21 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=86 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:46:21 ijk-diagnose: nieuwste migratie 1.5 min oud | migraties 15/60/240 min: 11/45/157 | al gemeten: 385
01:51:50 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=90 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:51:54 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 11/46/159 | al gemeten: 389
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
