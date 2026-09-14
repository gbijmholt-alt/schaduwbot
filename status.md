# Schaduwbot status

- tijd: 2026-09-14 04:43:39 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 14 hours, 56 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 1903/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 79771, "tokens_in_memory": 6829, "msgs": 10709719, "trades": 2240874, "creates": 23612, "decode_fail": 195518, "rpc_calls": 65425, "rpc_errors": 3, "sol_usd": 101.15429227219406, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 04:05:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:06,919 main INFO screen BMW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.3s)
Sep 14 04:05:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:17,708 main INFO screen TIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 14 04:05:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:44,222 main INFO screen poop pass=0 dev=0.0 ins=26.54 pro=51 1a=False 1b=False 2=True (50.2s)
Sep 14 04:06:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:06:27,279 main INFO screen Gen pass=1 dev=0.42 ins=0.0 pro=17 1a=False 1b=False 2=False (67.5s)
Sep 14 04:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:07:30,961 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:07:30 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 04:07:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:07:39,247 main INFO screen RETARD pass=0 dev=0.0 ins=25.34 pro=69 1a=False 1b=False 2=True (60.0s)
Sep 14 04:11:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:15,642 main INFO screen CTO pass=0 dev=0.0 ins=16.75 pro=71 1a=False 1b=False 2=True (63.5s)
Sep 14 04:11:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:21,878 main INFO screen TRUMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 14 04:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:43,260 main INFO screen SHATGPT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 14 04:12:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:24,934 main INFO screen EMEM pass=0 dev=0.0 ins=25.29 pro=66 1a=False 1b=False 2=True (69.3s)
Sep 14 04:12:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:34,218 main INFO screen twineACT pass=0 dev=0.18 ins=77.58 pro=17 1a=False 1b=False 2=True (72.3s)
Sep 14 04:12:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:35,583 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:12:35 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:13:07,106 main INFO screen ShanaTova pass=0 dev=0.0 ins=17.41 pro=40 1a=False 1b=False 2=True (72.5s)
Sep 14 04:14:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:06,262 main INFO screen Nike pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.0s)
Sep 14 04:14:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:22,861 main INFO screen POP pass=0 dev=0.0 ins=14.23 pro=55 1a=False 1b=False 2=True (58.7s)
Sep 14 04:14:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:32,946 main INFO screen MEMEBACK pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (59.0s)
Sep 14 04:15:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:15:56,598 main INFO screen Rotator pass=0 dev=0.0 ins=33.81 pro=80 1a=False 1b=False 2=True (62.5s)
Sep 14 04:16:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:16:34,665 main INFO screen poop pass=0 dev=0.0 ins=21.86 pro=65 1a=False 1b=False 2=True (61.0s)
Sep 14 04:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:17:37,132 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:17:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 04:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:18:23,112 main INFO screen Rotator pass=1 dev=0.0 ins=8.76 pro=49 1a=False 1b=False 2=False (60.3s)
Sep 14 04:18:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:18:40,445 main INFO screen MIKESEM pass=0 dev=34.74 ins=0.0 pro=5 1a=False 1b=False 2=True (62.3s)
Sep 14 04:19:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:19:39,878 main INFO screen Humanity pass=0 dev=0.0 ins=33.57 pro=71 1a=False 1b=False 2=True (64.4s)
Sep 14 04:20:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:20:15,653 main INFO screen $RENT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.8s)
Sep 14 04:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:20:18,240 main INFO screen GUMP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.5s)
Sep 14 04:21:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:21:25,613 main INFO screen . pass=0 dev=0.26 ins=0.0 pro=4 1a=False 1b=False 2=False (65.7s)
Sep 14 04:22:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:22:45,479 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:22:45 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:23:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:23:12,460 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (68.5s)
Sep 14 04:23:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:23:19,359 main INFO screen $JUICY pass=0 dev=0.14 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 04:24:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:24:11,372 main INFO screen とろろ pass=0 dev=0.0 ins=29.29 pro=58 1a=False 1b=False 2=True (66.4s)
Sep 14 04:24:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:24:25,289 main INFO screen bikecate pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (55.0s)
Sep 14 04:25:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:25:14,445 main INFO screen Humanity pass=0 dev=0.0 ins=3.46 pro=69 1a=False 1b=False 2=True (65.7s)
Sep 14 04:26:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:26:06,295 main INFO screen WHITETWINE pass=0 dev=0.18 ins=79.13 pro=7 1a=False 1b=True 2=True (56.4s)
Sep 14 04:26:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:26:18,700 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.6s)
Sep 14 04:26:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:26:45,080 main INFO screen Gemini AI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.2s)
Sep 14 04:27:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:27:23,907 main INFO screen OSC pass=0 dev=9.0 ins=24.2 pro=25 1a=False 1b=False 2=True (56.1s)
Sep 14 04:28:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:28:05,679 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:28:05 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:28:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:28:36,103 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (67.0s)
Sep 14 04:28:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:28:46,117 main INFO screen WTFF pass=0 dev=0.46 ins=0.0 pro=1 1a=False 1b=False 2=False (54.3s)
Sep 14 04:29:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:29:41,291 main INFO screen TEM pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (68.7s)
Sep 14 04:29:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:29:57,073 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (61.9s)
Sep 14 04:32:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:32:03,631 main INFO screen NIGGER pass=0 dev=0.0 ins=20.49 pro=53 1a=False 1b=False 2=True (55.6s)
Sep 14 04:32:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:32:15,484 main INFO screen McDonald's pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.5s)
Sep 14 04:32:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:32:50,528 main INFO screen baton pass=0 dev=0.7 ins=55.34 pro=9 1a=False 1b=True 2=True (54.2s)
Sep 14 04:33:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:33:30,405 main INFO screen Humanity pass=0 dev=0.0 ins=25.9 pro=45 1a=False 1b=False 2=True (68.7s)
Sep 14 04:33:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:33:33,071 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:33:33 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:33:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:33:42,462 main INFO screen SubSneak pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (75.0s)
Sep 14 04:33:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:33:45,914 main INFO screen Nike pass=0 dev=66.78 ins=0.0 pro=1 1a=False 1b=False 2=True (55.4s)
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:35:02,855 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 04:35:02 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 04:35:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:35:10,282 main INFO screen KOVRA pass=0 dev=13.0 ins=24.34 pro=29 1a=False 1b=True 2=False (99.9s)
Sep 14 04:35:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:35:43,955 main INFO screen Johnny  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (98.7s)
Sep 14 04:36:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:11,745 main INFO screen 🌙 pass=0 dev=0.07 ins=0.0 pro=7 1a=False 1b=False 2=False (68.8s)
Sep 14 04:36:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:56,085 main INFO screen GOAT pass=0 dev=4.32 ins=0.0 pro=4 1a=False 1b=False 2=False (69.2s)
Sep 14 04:36:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:36:58,701 main INFO screen 奶龙 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.8s)
Sep 14 04:37:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:37:51,256 main INFO screen ACTII pass=0 dev=0.0 ins=12.05 pro=67 1a=False 1b=False 2=True (62.0s)
Sep 14 04:38:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:38:35,917 main INFO screen $MD pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (68.2s)
Sep 14 04:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:38:37,073 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:38:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:39:07,132 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.4s)
Sep 14 04:39:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:39:48,406 main INFO screen PUMP pass=1 dev=0.0 ins=10.51 pro=40 1a=False 1b=False 2=False (63.1s)
Sep 14 04:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:06,003 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 14 04:40:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:21,014 main INFO screen FROGLABS pass=0 dev=8.76 ins=25.57 pro=16 1a=False 1b=False 2=False (53.4s)
Sep 14 04:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:40:39,277 main INFO screen USDF pass=0 dev=77.77 ins=1.54 pro=1 1a=False 1b=False 2=True (50.9s)
Sep 14 04:41:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:03,100 main INFO screen JWD pass=1 dev=1.74 ins=0.0 pro=45 1a=False 1b=False 2=False (57.1s)
Sep 14 04:41:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:27,294 main INFO screen pump pass=1 dev=0.21 ins=0.0 pro=10 1a=False 1b=False 2=False (66.3s)
Sep 14 04:41:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:31,289 main INFO screen plum pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (52.0s)
Sep 14 04:41:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:41:55,739 main INFO screen GPTjak pass=0 dev=0.18 ins=77.76 pro=10 1a=False 1b=True 2=True (52.6s)
Sep 14 04:42:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:42:28,495 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 14 04:42:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:42:29,917 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.6s)
Sep 14 04:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:11,659 main INFO screen Human pass=0 dev=0.0 ins=6.56 pro=52 1a=False 1b=False 2=True (65.4s)
Sep 14 04:43:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:32,498 main INFO screen human pass=0 dev=0.0 ins=25.64 pro=65 1a=False 1b=False 2=True (64.0s)
Sep 14 04:43:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:39,488 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:43:39 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T03:05:21Z
--- update 2026-09-14T03:10:24Z
--- update 2026-09-14T03:15:35Z
--- update 2026-09-14T03:20:36Z
--- update 2026-09-14T03:25:45Z
--- update 2026-09-14T03:30:49Z
--- update 2026-09-14T03:35:52Z
--- update 2026-09-14T03:40:58Z
--- update 2026-09-14T03:46:36Z
--- update 2026-09-14T03:51:35Z
--- update 2026-09-14T03:56:38Z
--- update 2026-09-14T04:02:07Z
--- update 2026-09-14T04:07:29Z
--- update 2026-09-14T04:12:34Z
--- update 2026-09-14T04:17:36Z
--- update 2026-09-14T04:22:44Z
--- update 2026-09-14T04:28:04Z
--- update 2026-09-14T04:33:32Z
--- update 2026-09-14T04:38:36Z
--- update 2026-09-14T04:43:38Z
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
