# Schaduwbot status

- tijd: 2026-09-15 13:46:54 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 23 hours, 59 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.2G/38G | geheugen: 3568/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 198766, "tokens_in_memory": 6631, "msgs": 28417272, "trades": 5970042, "creates": 63675, "decode_fail": 495609, "rpc_calls": 176855, "rpc_errors": 15, "sol_usd": 100.02615452577955, "open_positions": 50, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 13:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:24:35,183 main INFO screen LOL pass=0 dev=0.0 ins=2.42 pro=2 1a=False 1b=False 2=False (70.0s)
Sep 15 13:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:24:35,881 main INFO screen MOVEMENT pass=0 dev=0.0 ins=22.81 pro=2 1a=False 1b=False 2=True (67.2s)
Sep 15 13:25:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:25:25,015 main INFO screen Zap pass=0 dev=5.51 ins=0.0 pro=14 1a=False 1b=False 2=False (70.7s)
Sep 15 13:25:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:25:39,443 main INFO screen Foreskin pass=0 dev=0.0 ins=25.31 pro=66 1a=False 1b=False 2=True (63.6s)
Sep 15 13:25:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:25:43,202 main INFO screen WOTF pass=0 dev=0.79 ins=122.32 pro=1 1a=False 1b=False 2=True (68.0s)
Sep 15 13:25:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:25:47,444 aiohttp.access INFO 213.209.159.91 [15/Sep/2026:13:25:47 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 15 13:26:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:26:21,084 main INFO screen ZIX pass=0 dev=0.0 ins=0.21 pro=3 1a=False 1b=False 2=False (56.1s)
Sep 15 13:26:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:26:39,878 main INFO screen chud  pass=0 dev=0.0 ins=3.76 pro=2 1a=False 1b=False 2=False (60.4s)
Sep 15 13:26:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:26:47,476 main INFO screen KOA pass=0 dev=0.0 ins=17.66 pro=38 1a=False 1b=False 2=False (64.3s)
Sep 15 13:26:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:26:53,015 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:26:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:27:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:27:14,676 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.6s)
Sep 15 13:27:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:27:32,754 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (52.9s)
Sep 15 13:27:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:27:43,907 main INFO screen Goblin pass=0 dev=0.0 ins=23.9 pro=1 1a=False 1b=False 2=True (56.4s)
Sep 15 13:28:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:28:10,130 main INFO screen ALI pass=0 dev=0.0 ins=1.74 pro=2 1a=False 1b=False 2=False (55.5s)
Sep 15 13:28:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:28:28,938 main INFO screen DGONS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.2s)
Sep 15 13:28:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:28:39,585 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.7s)
Sep 15 13:29:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:29:08,764 main INFO screen OBANANA pass=0 dev=0.0 ins=70.95 pro=32 1a=False 1b=True 2=True (58.6s)
Sep 15 13:29:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:29:26,440 main INFO screen ddd pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.5s)
Sep 15 13:29:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:29:38,140 main INFO screen ILONBIKE pass=0 dev=0.0 ins=79.26 pro=3 1a=False 1b=True 2=True (58.6s)
Sep 15 13:30:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:30:20,260 main INFO screen WNB pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (71.5s)
Sep 15 13:30:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:30:22,968 main INFO screen Sig pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (56.5s)
Sep 15 13:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:30:48,063 main INFO screen Biggie pass=0 dev=0.0 ins=42.44 pro=27 1a=False 1b=False 2=True (69.9s)
Sep 15 13:31:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:31:19,576 main INFO screen Coca pass=0 dev=0.0 ins=160.85 pro=0 1a=False 1b=False 2=True (56.6s)
Sep 15 13:31:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:31:30,580 main INFO screen Obama pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (70.3s)
Sep 15 13:31:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:31:46,836 main INFO screen Sandwich pass=0 dev=0.0 ins=79.13 pro=5 1a=False 1b=True 2=True (58.8s)
Sep 15 13:31:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:31:53,313 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:31:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:32:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:32:17,588 main INFO screen Sig pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (58.0s)
Sep 15 13:32:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:32:29,934 main INFO screen Hope pass=0 dev=0.09 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 15 13:32:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:32:45,502 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.7s)
Sep 15 13:33:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:33:25,347 main INFO screen Normie pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (67.8s)
Sep 15 13:33:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:33:32,447 main INFO screen FOMO pass=0 dev=0.0 ins=21.01 pro=26 1a=False 1b=False 2=False (62.5s)
Sep 15 13:33:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:33:55,668 main INFO screen FART pass=0 dev=0.0 ins=23.62 pro=66 1a=False 1b=False 2=True (70.2s)
Sep 15 13:34:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:34:37,994 main INFO screen OIIA pass=0 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (72.6s)
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:35:41,408 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 13:35:41 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 13:35:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:35:50,520 main INFO screen DRILLPIG pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=False (138.1s)
Sep 15 13:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:35:55,852 main INFO screen fgg pass=0 dev=0.07 ins=0.0 pro=1 1a=False 1b=False 2=False (120.2s)
Sep 15 13:36:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:36:48,292 main INFO screen APEWIF pass=0 dev=0.0 ins=76.85 pro=17 1a=False 1b=False 2=True (130.3s)
Sep 15 13:36:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:36:53,299 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:36:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:37:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:37:00,497 main INFO screen MESSI pass=0 dev=0.07 ins=0.0 pro=7 1a=False 1b=False 2=False (70.0s)
Sep 15 13:37:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:37:05,535 main INFO screen PreStocks pass=0 dev=0.0 ins=9.23 pro=81 1a=False 1b=False 2=True (69.7s)
Sep 15 13:38:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:38:04,851 main INFO screen MONTY pass=0 dev=0.0 ins=24.65 pro=0 1a=False 1b=False 2=True (76.6s)
Sep 15 13:38:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:38:08,284 main INFO screen Remus pass=0 dev=0.0 ins=10.37 pro=65 1a=False 1b=False 2=False (62.7s)
Sep 15 13:38:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:38:14,059 main INFO screen Puter pass=0 dev=0.0 ins=19.91 pro=8 1a=False 1b=False 2=False (73.6s)
Sep 15 13:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:39:02,687 main INFO screen RST pass=0 dev=0.0 ins=265.53 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 15 13:39:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:39:13,030 main INFO screen 67 pass=0 dev=0.0 ins=0.68 pro=37 1a=False 1b=False 2=False (68.2s)
Sep 15 13:39:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:39:28,706 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (74.6s)
Sep 15 13:39:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:39:55,965 aiohttp.access INFO 195.182.16.23 [15/Sep/2026:13:39:55 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 15 13:40:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:40:01,227 main INFO screen TITIS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 15 13:40:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:40:18,317 main INFO screen Amir pass=0 dev=0.0 ins=14.49 pro=62 1a=False 1b=False 2=True (65.3s)
Sep 15 13:40:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:40:29,559 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.9s)
Sep 15 13:41:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:41:02,280 main INFO screen $PUZZ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.1s)
Sep 15 13:41:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:41:20,964 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.6s)
Sep 15 13:41:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:41:27,095 main INFO screen ALI pass=0 dev=0.0 ins=0.88 pro=9 1a=False 1b=False 2=False (57.5s)
Sep 15 13:41:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:41:53,977 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:41:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:42:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:42:07,363 main INFO screen MESSI pass=0 dev=0.42 ins=0.0 pro=12 1a=False 1b=False 2=False (65.1s)
Sep 15 13:42:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:42:13,242 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 15 13:42:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:42:19,257 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (52.2s)
Sep 15 13:42:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:42:59,626 main INFO screen HODL pass=0 dev=0.0 ins=23.63 pro=25 1a=False 1b=False 2=False (52.3s)
Sep 15 13:43:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:43:05,044 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.8s)
Sep 15 13:43:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:43:20,044 main INFO screen INVESCOW pass=0 dev=0.0 ins=24.6 pro=33 1a=False 1b=False 2=True (60.8s)
Sep 15 13:43:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:43:58,869 main INFO screen MESSI pass=0 dev=0.14 ins=0.0 pro=7 1a=False 1b=False 2=False (59.2s)
Sep 15 13:44:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:44:07,639 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (62.6s)
Sep 15 13:44:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:44:25,434 main INFO screen Park pass=0 dev=0.0 ins=4.37 pro=66 1a=False 1b=False 2=False (65.4s)
Sep 15 13:44:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:44:53,562 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=True (54.7s)
Sep 15 13:45:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:45:02,551 main INFO screen CUPPY pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (54.9s)
Sep 15 13:45:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:45:16,328 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 15 13:46:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:46:03,447 main INFO screen SOUNDCAT pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (69.9s)
Sep 15 13:46:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:46:08,896 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (66.3s)
Sep 15 13:46:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:46:09,739 main INFO screen Family pass=0 dev=0.0 ins=7.86 pro=73 1a=False 1b=False 2=False (53.4s)
Sep 15 13:46:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:46:54,648 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:46:54 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T12:31:11Z
--- update 2026-09-15T12:36:11Z
--- update 2026-09-15T12:41:11Z
--- update 2026-09-15T12:46:11Z
--- update 2026-09-15T12:51:12Z
--- update 2026-09-15T12:56:12Z
--- update 2026-09-15T13:01:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7ff017f4c1e54aaebf060b943fa4342a
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T13:06:35Z
--- update 2026-09-15T13:11:36Z
--- update 2026-09-15T13:16:44Z
nieuwe code: caa47fa
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T13:21:52Z
--- update 2026-09-15T13:26:51Z
--- update 2026-09-15T13:31:52Z
--- update 2026-09-15T13:36:51Z
--- update 2026-09-15T13:41:52Z
--- update 2026-09-15T13:46:53Z
```

## Analyses (laatste 40 regels)
```
active
12:01:13 134689 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
12:13:27 6807 lopers, 18 niet-onderscheidende woorden
12:14:29   500/6807 lopers, 4334 koppelingen
12:15:21   1000/6807 lopers, 7353 koppelingen
12:16:07   1500/6807 lopers, 11262 koppelingen
12:16:58   2000/6807 lopers, 15841 koppelingen
12:17:42   2500/6807 lopers, 18547 koppelingen
12:18:20   3000/6807 lopers, 21453 koppelingen
12:19:14   3500/6807 lopers, 25603 koppelingen
12:19:50   4000/6807 lopers, 28395 koppelingen
12:20:45   4500/6807 lopers, 32066 koppelingen
12:21:33   5000/6807 lopers, 35311 koppelingen
12:22:13   5500/6807 lopers, 38244 koppelingen
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
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
