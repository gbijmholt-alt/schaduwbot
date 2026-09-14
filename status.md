# Schaduwbot status

- tijd: 2026-09-14 12:52:28 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 23 hours, 5 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.7G/38G | geheugen: 1905/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 109100, "tokens_in_memory": 4809, "msgs": 12823300, "trades": 2890433, "creates": 29841, "decode_fail": 239805, "rpc_calls": 87500, "rpc_errors": 7, "sol_usd": 101.39489780684913, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 12:30:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:30:55,142 aiohttp.access INFO 95.97.101.226 [14/Sep/2026:12:30:55 +0000] "GET /dvr/brief.xml HTTP/1.1" 404 193 "-" "-"
Sep 14 12:31:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:31:21,657 main INFO screen inim pass=0 dev=0.19 ins=78.65 pro=22 1a=False 1b=True 2=True (60.8s)
Sep 14 12:31:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:31:37,678 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:31:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 12:31:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:31:45,035 main INFO screen PumpTyson pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 12:31:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:31:45,816 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 14 12:32:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:32:31,404 main INFO screen bob pass=1 dev=0.0 ins=11.09 pro=40 1a=False 1b=False 2=False (69.7s)
Sep 14 12:32:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:32:51,394 main INFO screen att pass=0 dev=0.03 ins=0.0 pro=3 1a=False 1b=False 2=False (65.6s)
Sep 14 12:32:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:32:53,611 main INFO screen AI pass=0 dev=0.0 ins=24.38 pro=45 1a=False 1b=False 2=True (68.6s)
Sep 14 12:33:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:33:27,402 main INFO screen ANSEMHOOD pass=0 dev=0.0 ins=45.31 pro=40 1a=False 1b=True 2=True (56.0s)
Sep 14 12:33:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:33:46,916 main INFO screen MCDUCK pass=0 dev=0.0 ins=0.06 pro=3 1a=False 1b=False 2=True (53.3s)
Sep 14 12:33:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:33:48,653 main INFO screen HedgeHog pass=1 dev=0.0 ins=19.89 pro=43 1a=False 1b=False 2=False (57.3s)
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:35:16,905 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 12:35:16 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 12:35:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:35:27,199 main INFO screen leaves pass=1 dev=0.0 ins=6.56 pro=72 1a=False 1b=False 2=False (119.8s)
Sep 14 12:35:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:35:49,203 main INFO screen CART pass=1 dev=1.1 ins=0.0 pro=51 1a=False 1b=False 2=False (122.3s)
Sep 14 12:35:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:35:49,534 main INFO screen FREEHM pass=0 dev=1.24 ins=0.0 pro=6 1a=False 1b=False 2=False (120.9s)
Sep 14 12:36:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:36:25,372 main INFO screen PASY pass=0 dev=0.18 ins=79.13 pro=5 1a=False 1b=True 2=True (58.2s)
Sep 14 12:36:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:36:41,900 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:36:41 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 12:36:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:36:47,711 main INFO screen TITYSON pass=0 dev=0.06 ins=79.26 pro=9 1a=False 1b=True 2=True (58.2s)
Sep 14 12:36:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:36:47,811 main INFO screen Niggio pass=0 dev=0.0 ins=17.43 pro=28 1a=False 1b=False 2=True (58.6s)
Sep 14 12:37:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:37:23,664 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 14 12:37:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:37:43,618 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (55.9s)
Sep 14 12:37:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:37:45,161 main INFO screen VPN pass=0 dev=0.0 ins=25.91 pro=45 1a=False 1b=False 2=True (57.3s)
Sep 14 12:38:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:38:19,237 main INFO screen LMAO pass=0 dev=3.42 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 14 12:38:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:38:43,310 main INFO screen WOFI pass=0 dev=0.01 ins=79.43 pro=1 1a=False 1b=False 2=True (58.1s)
Sep 14 12:38:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:38:43,885 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 14 12:39:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:39:11,238 main INFO screen SALLY pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (52.0s)
Sep 14 12:39:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:39:38,017 main INFO screen Bananaut pass=1 dev=0.0 ins=18.75 pro=25 1a=False 1b=False 2=False (54.1s)
Sep 14 12:39:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:39:38,619 main INFO screen MC pass=0 dev=0.7 ins=0.0 pro=5 1a=False 1b=False 2=False (55.3s)
Sep 14 12:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:40:00,217 main INFO screen fihdih pass=1 dev=0.0 ins=0.0 pro=65 1a=False 1b=False 2=False (49.0s)
Sep 14 12:40:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:40:27,810 main INFO screen BULL pass=0 dev=0.0 ins=35.66 pro=13 1a=False 1b=True 2=True (49.8s)
Sep 14 12:40:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:40:40,030 main INFO screen NABU pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (61.4s)
Sep 14 12:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:40:46,579 main INFO screen ily pass=0 dev=0.0 ins=22.62 pro=4 1a=False 1b=False 2=False (46.4s)
Sep 14 12:41:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:41:17,844 main INFO screen ILY pass=0 dev=0.0 ins=25.82 pro=26 1a=False 1b=False 2=True (50.0s)
Sep 14 12:41:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:41:38,232 main INFO screen NABU pass=0 dev=0.03 ins=0.0 pro=2 1a=False 1b=False 2=False (58.2s)
Sep 14 12:41:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:41:40,144 main INFO screen CATE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 14 12:41:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:41:55,580 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:41:55 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 12:42:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:42:09,370 main INFO screen Hamster pass=0 dev=0.0 ins=26.49 pro=47 1a=False 1b=False 2=True (51.5s)
Sep 14 12:42:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:42:30,954 main INFO screen BEMJAK pass=0 dev=0.35 ins=78.96 pro=5 1a=False 1b=True 2=True (50.8s)
Sep 14 12:42:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:42:33,384 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.2s)
Sep 14 12:43:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:43:03,959 main INFO screen QUVO pass=0 dev=0.0 ins=18.75 pro=69 1a=False 1b=False 2=True (54.6s)
Sep 14 12:43:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:43:25,126 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 14 12:43:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:43:32,800 main INFO screen Loom pass=0 dev=0.0 ins=20.88 pro=2 1a=False 1b=False 2=True (59.4s)
Sep 14 12:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:43:55,796 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.8s)
Sep 14 12:44:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:44:27,890 main INFO screen USMS pass=0 dev=0.76 ins=0.0 pro=1 1a=False 1b=False 2=False (62.8s)
Sep 14 12:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:44:28,371 aiohttp.access INFO 94.154.43.31 [14/Sep/2026:12:44:28 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0"
Sep 14 12:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:45:12,474 main INFO screen Burkat pass=0 dev=0.0 ins=17.7 pro=56 1a=False 1b=False 2=True (69.7s)
Sep 14 12:45:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:45:23,220 main INFO screen FOMO pass=1 dev=0.0 ins=16.72 pro=53 1a=False 1b=False 2=False (60.8s)
Sep 14 12:45:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:45:35,242 main INFO screen Coca-Cola pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 14 12:46:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:46:04,213 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 12:46:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:46:27,846 main INFO screen Danny pass=0 dev=0.0 ins=0.88 pro=1 1a=False 1b=False 2=False (64.6s)
Sep 14 12:46:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:46:50,934 main INFO screen $FEE pass=0 dev=0.0 ins=0.22 pro=1 1a=False 1b=False 2=False (62.0s)
Sep 14 12:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:47:07,982 main INFO screen FLY777 pass=0 dev=0.0 ins=36.99 pro=76 1a=False 1b=False 2=True (63.8s)
Sep 14 12:47:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:47:09,426 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:47:09 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 12:47:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:47:32,159 main INFO screen PvP pass=0 dev=0.0 ins=19.08 pro=68 1a=False 1b=False 2=True (64.3s)
Sep 14 12:47:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:47:54,237 main INFO screen HEEHAW pass=1 dev=0.0 ins=19.5 pro=21 1a=False 1b=False 2=False (63.3s)
Sep 14 12:47:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:47:59,174 main INFO screen NEIL pass=1 dev=0.0 ins=19.83 pro=30 1a=False 1b=False 2=False (51.2s)
Sep 14 12:48:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:48:22,913 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (50.8s)
Sep 14 12:49:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:49:05,603 main INFO screen SHERWOOD pass=1 dev=0.0 ins=0.76 pro=48 1a=False 1b=False 2=False (71.4s)
Sep 14 12:49:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:49:07,514 main INFO screen cummies pass=0 dev=0.0 ins=21.51 pro=19 1a=False 1b=False 2=True (68.3s)
Sep 14 12:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:49:33,184 main INFO screen Parker pass=0 dev=0.0 ins=22.38 pro=69 1a=False 1b=False 2=True (70.3s)
Sep 14 12:50:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:50:01,786 main INFO screen Chihuahua pass=0 dev=0.0 ins=27.17 pro=40 1a=False 1b=False 2=True (54.3s)
Sep 14 12:50:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:50:11,232 main INFO screen jj pass=0 dev=0.64 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 14 12:50:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:50:23,290 main INFO screen SONK pass=0 dev=6.63 ins=72.68 pro=1 1a=False 1b=True 2=True (50.1s)
Sep 14 12:50:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:50:52,464 main INFO screen EMBRC pass=0 dev=0.0 ins=28.68 pro=9 1a=False 1b=True 2=False (50.7s)
Sep 14 12:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:51:17,544 main INFO screen PepeCoin pass=0 dev=0.0 ins=18.02 pro=32 1a=False 1b=False 2=True (66.3s)
Sep 14 12:51:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:51:23,656 main INFO screen STRAIT pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (60.4s)
Sep 14 12:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:51:56,214 main INFO screen dd pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (63.7s)
Sep 14 12:52:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:52:02,840 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (45.3s)
Sep 14 12:52:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:52:16,903 main INFO screen BULL pass=0 dev=2.2 ins=37.26 pro=34 1a=False 1b=False 2=True (53.2s)
Sep 14 12:52:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:52:28,339 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:52:28 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T11:23:05Z
--- update 2026-09-14T11:28:36Z
--- update 2026-09-14T11:33:42Z
--- update 2026-09-14T11:39:15Z
--- update 2026-09-14T11:44:18Z
--- update 2026-09-14T11:49:34Z
Running as unit: schaduwbot-wallets.service; invocation ID: 26c0b13a204d4f3ea8d30078009f924a
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T11:54:36Z
--- update 2026-09-14T11:59:52Z
--- update 2026-09-14T12:04:53Z
--- update 2026-09-14T12:09:58Z
--- update 2026-09-14T12:15:25Z
--- update 2026-09-14T12:20:36Z
--- update 2026-09-14T12:26:18Z
--- update 2026-09-14T12:31:36Z
--- update 2026-09-14T12:36:40Z
--- update 2026-09-14T12:41:54Z
--- update 2026-09-14T12:47:08Z
--- update 2026-09-14T12:52:27Z
```

## Analyses (laatste 25 regels)
```
inactive
12:24:10   34000 tokens, 3435601 trades, 426342 posities (209s)
12:24:25   36000 tokens, 3657840 trades, 454829 posities (224s)
12:24:39   38000 tokens, 3859925 trades, 481486 posities (238s)
12:24:53   40000 tokens, 4059765 trades, 504756 posities (252s)
12:25:05   42000 tokens, 4234354 trades, 524489 posities (264s)
12:25:18   44000 tokens, 4431985 trades, 548318 posities (277s)
12:25:32   46000 tokens, 4626357 trades, 574418 posities (291s)
12:25:46   48000 tokens, 4835116 trades, 597599 posities (305s)
12:25:59   50000 tokens, 5038874 trades, 622075 posities (318s)
12:26:12   52000 tokens, 5223412 trades, 643069 posities (331s)
12:26:25   54000 tokens, 5397845 trades, 660920 posities (344s)
12:26:38   56000 tokens, 5602394 trades, 687587 posities (357s)
12:26:49   58000 tokens, 5776662 trades, 706640 posities (368s)
12:27:01   60000 tokens, 5985201 trades, 736365 posities (380s)
12:27:13   62000 tokens, 6183196 trades, 764072 posities (392s)
12:27:25   64000 tokens, 6394266 trades, 791990 posities (404s)
12:27:37   66000 tokens, 6593931 trades, 817825 posities (416s)
12:27:50   68000 tokens, 6794379 trades, 846287 posities (429s)
12:28:02   70000 tokens, 6990170 trades, 880107 posities (441s)
12:28:09 posities: 896544 uit 7116580 trades (449s)
12:28:22 198620 wallets gerekend
12:28:23 geluk-toets
12:29:00 persistentie
12:29:03 kopieer-simulatie
12:31:05 klaar in 624s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
12:20:38 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:26:20 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:31:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:36:41 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:41:55 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:47:09 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:52:28 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
