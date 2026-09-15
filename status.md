# Schaduwbot status

- tijd: 2026-09-15 19:57:35 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 6 hours, 10 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.6G/38G | geheugen: 2306/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 221007, "tokens_in_memory": 10619, "msgs": 35139357, "trades": 7022351, "creates": 74512, "decode_fail": 595782, "rpc_calls": 199387, "rpc_errors": 17, "sol_usd": 97.8341160403622, "open_positions": 58, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 19:35:40 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 19:36:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:36:24,855 main INFO screen LASER pass=0 dev=0.0 ins=38.15 pro=18 1a=False 1b=False 2=True (107.0s)
Sep 15 19:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:36:37,290 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:36:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:36:37,898 main INFO screen Clarity pass=0 dev=0.0 ins=32.83 pro=64 1a=False 1b=False 2=True (121.5s)
Sep 15 19:36:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:36:45,834 main INFO screen BULLISHCAT pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=False 2=True (125.9s)
Sep 15 19:37:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:37:15,645 main INFO screen Constantinopl pass=0 dev=0.0 ins=17.7 pro=43 1a=False 1b=False 2=True (50.8s)
Sep 15 19:37:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:37:31,878 main INFO screen Constantinopl pass=0 dev=0.0 ins=6.51 pro=14 1a=False 1b=False 2=False (54.0s)
Sep 15 19:37:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:37:55,776 main INFO screen Signor  pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (69.9s)
Sep 15 19:38:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:38:16,089 main INFO screen cap pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (60.4s)
Sep 15 19:38:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:38:39,534 main INFO screen Constatinople pass=0 dev=0.0 ins=19.15 pro=51 1a=False 1b=False 2=True (67.7s)
Sep 15 19:38:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:38:53,502 main INFO screen LUCAS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 19:39:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:39:25,647 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (69.6s)
Sep 15 19:39:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:39:50,871 main INFO screen CAPS pass=0 dev=0.04 ins=0.0 pro=82 1a=False 1b=False 2=False (71.3s)
Sep 15 19:39:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:39:55,301 main INFO screen NOPOOL2 pass=0 dev=0.0 ins=0.05 pro=3 1a=False 1b=False 2=True (61.8s)
Sep 15 19:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:40:39,077 main INFO screen ZFONE pass=0 dev=0.0 ins=79.27 pro=5 1a=False 1b=False 2=True (73.4s)
Sep 15 19:40:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:40:44,868 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (54.0s)
Sep 15 19:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:40:56,427 main INFO screen $SEND pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (61.1s)
Sep 15 19:41:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:41:46,403 main INFO screen McCannon pass=0 dev=0.0 ins=27.62 pro=63 1a=False 1b=False 2=True (67.3s)
Sep 15 19:41:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:41:56,518 main INFO screen CATE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (71.6s)
Sep 15 19:41:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:41:58,534 main INFO screen bikeconor pass=0 dev=0.0 ins=79.17 pro=3 1a=False 1b=True 2=True (62.1s)
Sep 15 19:42:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:42:04,954 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:42:04 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:42:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:42:41,965 main INFO screen CAT pass=0 dev=0.0 ins=17.7 pro=67 1a=False 1b=False 2=True (55.6s)
Sep 15 19:43:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:43:02,040 main INFO screen LARPFLEX pass=0 dev=0.0 ins=24.57 pro=35 1a=False 1b=False 2=False (65.5s)
Sep 15 19:43:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:43:04,527 main INFO screen DOG pass=0 dev=0.0 ins=9.75 pro=42 1a=False 1b=False 2=False (66.0s)
Sep 15 19:43:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:43:49,797 main INFO screen CAT pass=0 dev=0.0 ins=45.11 pro=63 1a=False 1b=False 2=True (67.8s)
Sep 15 19:43:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:43:52,857 main INFO screen OCAT pass=0 dev=0.0 ins=17.7 pro=20 1a=False 1b=False 2=True (48.3s)
Sep 15 19:43:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:43:56,335 main INFO screen Manifestoe pass=0 dev=0.0 ins=15.81 pro=1 1a=False 1b=False 2=True (54.3s)
Sep 15 19:44:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:44:57,671 main INFO screen #1 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.9s)
Sep 15 19:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:44:59,550 main INFO screen CLRTY pass=0 dev=0.0 ins=0.21 pro=15 1a=False 1b=False 2=False (66.7s)
Sep 15 19:45:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:45:00,108 main INFO screen BBC pass=0 dev=0.0 ins=166.59 pro=0 1a=False 1b=False 2=True (63.8s)
Sep 15 19:45:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:45:44,231 main INFO screen $HUG pass=0 dev=0.0 ins=0.84 pro=16 1a=False 1b=False 2=False (46.6s)
Sep 15 19:45:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:45:50,884 main INFO screen NOWORNEVER pass=0 dev=0.0 ins=33.23 pro=17 1a=False 1b=False 2=True (50.8s)
Sep 15 19:45:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:45:53,359 main INFO screen FOX pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 15 19:46:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:46:36,769 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.5s)
Sep 15 19:46:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:46:56,322 main INFO screen ZFONE pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (65.4s)
Sep 15 19:46:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:46:58,118 main INFO screen bill pass=0 dev=0.0 ins=61.52 pro=75 1a=False 1b=False 2=True (64.8s)
Sep 15 19:47:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:47:13,061 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:47:13 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:47:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:47:29,937 main INFO screen NOWORNEVER pass=0 dev=0.0 ins=20.03 pro=3 1a=False 1b=False 2=False (53.2s)
Sep 15 19:47:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:47:49,431 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.1s)
Sep 15 19:47:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:47:51,453 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 15 19:48:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:48:33,869 main INFO screen BlurCat pass=0 dev=0.0 ins=31.01 pro=38 1a=False 1b=False 2=True (63.9s)
Sep 15 19:48:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:48:42,640 main INFO screen EGGSHEERAN pass=0 dev=0.0 ins=78.46 pro=3 1a=False 1b=True 2=True (53.2s)
Sep 15 19:48:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:48:46,103 main INFO screen baton pass=0 dev=0.0 ins=91.02 pro=0 1a=False 1b=False 2=True (54.6s)
Sep 15 19:49:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:49:46,919 main INFO screen FSJAL pass=0 dev=0.0 ins=47.35 pro=21 1a=False 1b=False 2=True (73.0s)
Sep 15 19:49:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:49:49,413 main INFO screen bill pass=0 dev=0.0 ins=20.47 pro=48 1a=False 1b=False 2=True (66.8s)
Sep 15 19:49:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:49:54,917 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.8s)
Sep 15 19:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:50:07,585 aiohttp.access INFO 94.154.43.203 [15/Sep/2026:19:50:07 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0"
Sep 15 19:50:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:50:38,286 main INFO screen kitkat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.4s)
Sep 15 19:50:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:50:43,459 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.0s)
Sep 15 19:50:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:50:50,151 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 15 19:51:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:51:30,051 main INFO screen Bic pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (51.8s)
Sep 15 19:51:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:51:39,959 main INFO screen F&IC pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (49.8s)
Sep 15 19:51:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:51:47,496 main INFO screen lucidity pass=0 dev=0.0 ins=36.21 pro=70 1a=False 1b=False 2=True (64.0s)
Sep 15 19:52:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:52:26,798 main INFO screen TINY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.7s)
Sep 15 19:52:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:52:30,214 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:52:30 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:52:34,215 main INFO screen lucidity pass=0 dev=0.0 ins=15.06 pro=2 1a=False 1b=False 2=True (54.3s)
Sep 15 19:52:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:52:39,241 main INFO screen $BEERDOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 15 19:53:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:17,993 main INFO screen CPT pass=0 dev=0.0 ins=32.44 pro=30 1a=False 1b=False 2=True (51.2s)
Sep 15 19:53:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:40,640 main INFO screen ZARXU pass=0 dev=0.0 ins=10.51 pro=45 1a=False 1b=False 2=True (66.4s)
Sep 15 19:53:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:43,824 main INFO screen SIGIL pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=True (64.6s)
Sep 15 19:54:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:11,828 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (53.8s)
Sep 15 19:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:28,890 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=32.44 pro=17 1a=False 1b=False 2=True (48.2s)
Sep 15 19:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:37,288 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.5s)
Sep 15 19:55:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:16,572 main INFO screen pinkfloyd pass=0 dev=0.0 ins=17.59 pro=56 1a=False 1b=False 2=False (64.7s)
Sep 15 19:55:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:34,788 main INFO screen ber pass=0 dev=0.0 ins=37.37 pro=64 1a=False 1b=False 2=True (65.9s)
Sep 15 19:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:37,747 main INFO screen YOUR pass=0 dev=0.0 ins=27.96 pro=56 1a=False 1b=False 2=True (60.5s)
Sep 15 19:56:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:10,326 main INFO screen YOUR pass=0 dev=0.0 ins=55.79 pro=37 1a=False 1b=False 2=True (53.8s)
Sep 15 19:56:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:20,883 main INFO screen $CLICK pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (46.1s)
Sep 15 19:56:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:24,418 main INFO screen 300008 pass=0 dev=0.0 ins=20.68 pro=0 1a=False 1b=False 2=False (46.7s)
Sep 15 19:57:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:03,246 main INFO screen Signor  pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (52.9s)
Sep 15 19:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:27,799 main INFO screen batcat pass=0 dev=0.0 ins=59.63 pro=60 1a=False 1b=False 2=True (66.9s)
Sep 15 19:57:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:30,653 main INFO screen Paid pass=0 dev=0.0 ins=33.13 pro=60 1a=False 1b=False 2=True (66.2s)
Sep 15 19:57:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:35,443 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:57:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:34:36Z
--- update 2026-09-15T18:39:36Z
--- update 2026-09-15T18:44:43Z
--- update 2026-09-15T18:49:44Z
--- update 2026-09-15T18:55:20Z
--- update 2026-09-15T19:00:36Z
--- update 2026-09-15T19:05:56Z
Running as unit: schaduwbot-wallets.service; invocation ID: d4e9a4210cb94fceb933a73dcc655635
analyses gestart (84579ff37485)
--- update 2026-09-15T19:10:57Z
--- update 2026-09-15T19:15:59Z
--- update 2026-09-15T19:21:24Z
--- update 2026-09-15T19:26:28Z
--- update 2026-09-15T19:31:32Z
--- update 2026-09-15T19:36:36Z
--- update 2026-09-15T19:42:03Z
--- update 2026-09-15T19:47:11Z
--- update 2026-09-15T19:52:29Z
--- update 2026-09-15T19:57:34Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 19:05:57
19:05:58 venster 2026-09-13 07:05 UTC .. nu, 68842 tokens
19:06:46 klaar in 49s: 52628 tokens, 1902 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
19:26:58 ijk: +6 van 6 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=325 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:26:58 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 16/43/163 | al gemeten: 752
19:31:42 ijk: +2 van 2 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=326 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:31:42 ijk-diagnose: nieuwste migratie 3.4 min oud | migraties 15/60/240 min: 13/42/160 | al gemeten: 754
19:36:41 ijk: +1 van 1 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=327 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:36:41 ijk-diagnose: nieuwste migratie 0.7 min oud | migraties 15/60/240 min: 8/39/160 | al gemeten: 755
19:42:34 ijk: +6 van 6 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 2}) | verste bak n=332 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:42:34 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 8/41/164 | al gemeten: 761
19:47:31 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=335 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:47:32 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 12/41/162 | al gemeten: 765
19:52:54 ijk: +5 van 5 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=339 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:52:54 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 14/41/163 | al gemeten: 770
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
| 09-15 12:00 | 9559 | 1227 | 1135 | 5 | 0 | 75.9 min |
| 09-15 18:00 | 3487 | 0 | 0 | 0 | 0 | - |

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
