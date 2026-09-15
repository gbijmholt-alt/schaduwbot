# Schaduwbot status

- tijd: 2026-09-15 00:54:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 11 hours, 7 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.6G/38G | geheugen: 2232/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 152412, "tokens_in_memory": 10033, "msgs": 22839812, "trades": 4630777, "creates": 49127, "decode_fail": 402451, "rpc_calls": 130564, "rpc_errors": 13, "sol_usd": 102.61900006836807, "open_positions": 42, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 00:32:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:32:10,483 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (71.3s)
Sep 15 00:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:13,591 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:33:13 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:13,810 main INFO screen NUT pass=0 dev=0.0 ins=36.89 pro=72 1a=False 1b=False 2=True (72.1s)
Sep 15 00:33:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:24,065 main INFO screen MALONE pass=0 dev=0.0 ins=0.06 pro=47 1a=False 1b=False 2=False (74.7s)
Sep 15 00:33:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:25,086 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.6s)
Sep 15 00:34:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:14,000 main INFO screen fropy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.2s)
Sep 15 00:34:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:18,691 main INFO screen INTIUITION pass=0 dev=0.0 ins=23.58 pro=8 1a=False 1b=False 2=True (53.6s)
Sep 15 00:34:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:27,981 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.9s)
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:35:23,679 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 00:36:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:04,064 main INFO screen Clam pass=0 dev=0.0 ins=54.57 pro=72 1a=False 1b=False 2=True (110.1s)
Sep 15 00:36:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:25,775 main INFO screen DFC pass=0 dev=0.0 ins=19.61 pro=1 1a=False 1b=False 2=False (117.8s)
Sep 15 00:36:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:30,500 main INFO screen nobrain pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (131.8s)
Sep 15 00:37:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:12,016 main INFO screen werld pass=0 dev=0.0 ins=20.89 pro=44 1a=False 1b=False 2=True (68.0s)
Sep 15 00:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:24,863 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.1s)
Sep 15 00:37:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:44,823 main INFO screen LSTP pass=0 dev=0.16 ins=0.0 pro=70 1a=False 1b=False 2=False (74.3s)
Sep 15 00:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:10,770 main INFO screen CHARGE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (58.8s)
Sep 15 00:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:17,016 main INFO screen INTIUITION pass=0 dev=0.0 ins=19.47 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 15 00:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:37,675 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:38:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:46,315 main INFO screen HALH pass=0 dev=0.02 ins=0.0 pro=1 1a=False 1b=False 2=False (61.5s)
Sep 15 00:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:39:07,412 main INFO screen PEPEKING pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 15 00:39:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:39:16,136 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (59.1s)
Sep 15 00:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:39:35,721 main INFO screen brain pass=0 dev=0.0 ins=32.15 pro=21 1a=True 1b=False 2=True (49.4s)
Sep 15 00:40:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:40:07,613 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.2s)
Sep 15 00:40:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:40:12,495 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 15 00:40:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:40:33,313 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 00:40:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:40:50,057 aiohttp.access INFO 45.79.207.111 [15/Sep/2026:00:40:50 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 15 00:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:40:59,197 main INFO screen Vest pass=0 dev=0.0 ins=27.48 pro=53 1a=False 1b=False 2=True (51.6s)
Sep 15 00:41:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:41:02,872 main INFO screen KANYEVEST pass=0 dev=0.0 ins=18.35 pro=8 1a=False 1b=False 2=True (50.4s)
Sep 15 00:41:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:41:27,950 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.6s)
Sep 15 00:41:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:41:48,934 main INFO screen DiCabrio pass=0 dev=0.0 ins=42.13 pro=66 1a=False 1b=False 2=True (49.7s)
Sep 15 00:42:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:42:06,698 main INFO screen M$  pass=0 dev=48.72 ins=0.0 pro=16 1a=False 1b=False 2=False (63.8s)
Sep 15 00:42:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:42:18,018 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.1s)
Sep 15 00:42:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:42:38,991 aiohttp.access INFO 202.53.68.18 [15/Sep/2026:00:42:38 +0000] "POST /goform/formPing HTTP/1.1" 404 193 "http://167.233.49.49:8080/" "-"
Sep 15 00:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:42:52,002 main INFO screen Topless pass=0 dev=1.57 ins=38.5 pro=46 1a=False 1b=False 2=True (63.1s)
Sep 15 00:42:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:42:59,536 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.8s)
Sep 15 00:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:43:11,502 main INFO screen buy pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.5s)
Sep 15 00:43:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:43:38,044 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:43:38 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:43:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:43:57,842 main INFO screen LIONel pass=0 dev=0.0 ins=15.34 pro=55 1a=False 1b=False 2=False (65.8s)
Sep 15 00:43:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:43:58,061 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 15 00:44:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:44:06,868 main INFO screen dih pass=0 dev=0.0 ins=20.25 pro=36 1a=False 1b=False 2=True (55.4s)
Sep 15 00:45:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:00,729 main INFO screen DripCat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.9s)
Sep 15 00:45:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:02,377 main INFO screen BATON pass=0 dev=0.0 ins=9.9 pro=64 1a=False 1b=False 2=True (64.3s)
Sep 15 00:45:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:05,288 main INFO screen $HUGFACE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.4s)
Sep 15 00:45:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:49,876 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (47.5s)
Sep 15 00:45:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:52,831 main INFO screen NVIDIA6900 pass=0 dev=0.0 ins=6.53 pro=18 1a=False 1b=False 2=True (47.5s)
Sep 15 00:45:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:45:54,956 main INFO screen BRADPIT pass=0 dev=0.0 ins=0.03 pro=40 1a=False 1b=False 2=True (54.2s)
Sep 15 00:47:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:47:02,599 main INFO screen Dinky pass=0 dev=0.0 ins=22.26 pro=69 1a=False 1b=False 2=True (72.7s)
Sep 15 00:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:47:07,689 main INFO screen NACHOMAN pass=0 dev=0.0 ins=6.27 pro=63 1a=False 1b=False 2=False (74.9s)
Sep 15 00:47:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:47:08,538 main INFO screen DripCat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.6s)
Sep 15 00:48:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:48:10,936 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.3s)
Sep 15 00:48:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:48:14,260 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.6s)
Sep 15 00:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:48:15,070 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 15 00:48:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:48:49,486 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:48:49 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:49:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:49:02,866 main INFO screen BI6900 pass=0 dev=0.0 ins=19.87 pro=7 1a=False 1b=False 2=True (51.9s)
Sep 15 00:49:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:49:18,123 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.1s)
Sep 15 00:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:49:19,326 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.1s)
Sep 15 00:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:49:56,564 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.7s)
Sep 15 00:50:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:50:17,000 main INFO screen Pumpers pass=0 dev=0.0 ins=4.03 pro=67 1a=False 1b=False 2=True (58.9s)
Sep 15 00:50:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:50:19,482 main INFO screen michi pass=0 dev=0.0 ins=18.66 pro=62 1a=False 1b=False 2=False (60.2s)
Sep 15 00:50:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:50:52,806 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 15 00:51:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:51:15,322 main INFO screen chud pass=0 dev=0.0 ins=18.6 pro=15 1a=False 1b=False 2=True (58.3s)
Sep 15 00:51:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:51:28,478 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 15 00:51:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:51:51,984 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.2s)
Sep 15 00:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:52:14,767 main INFO screen DRMSCMTR pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.4s)
Sep 15 00:52:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:52:26,017 main INFO screen PIGEON pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.5s)
Sep 15 00:52:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:52:49,218 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.2s)
Sep 15 00:53:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:53:28,014 main INFO screen nugget pass=0 dev=0.0 ins=16.86 pro=5 1a=False 1b=False 2=False (73.2s)
Sep 15 00:53:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:53:31,726 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.7s)
Sep 15 00:53:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:53:49,113 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.9s)
Sep 15 00:54:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:54:20,644 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:54:20 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T23:24:58Z
--- update 2026-09-14T23:30:00Z
--- update 2026-09-14T23:35:20Z
--- update 2026-09-14T23:40:36Z
--- update 2026-09-14T23:46:20Z
Running as unit: schaduwbot-wallets.service; invocation ID: dc6a5a650126498b923bda7a46c6b0de
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T23:51:32Z
--- update 2026-09-14T23:56:36Z
--- update 2026-09-15T00:01:52Z
--- update 2026-09-15T00:07:23Z
--- update 2026-09-15T00:12:34Z
--- update 2026-09-15T00:17:36Z
--- update 2026-09-15T00:22:46Z
--- update 2026-09-15T00:28:02Z
--- update 2026-09-15T00:33:12Z
--- update 2026-09-15T00:38:36Z
--- update 2026-09-15T00:43:36Z
--- update 2026-09-15T00:48:48Z
--- update 2026-09-15T00:54:19Z
```

## Analyses (laatste 25 regels)
```
inactive
00:29:52   38000 tokens, 3688000 trades, 442370 posities (248s)
00:30:05   40000 tokens, 3882064 trades, 469159 posities (261s)
00:30:19   42000 tokens, 4065709 trades, 486855 posities (274s)
00:30:33   44000 tokens, 4245991 trades, 510852 posities (289s)
00:30:47   46000 tokens, 4420440 trades, 531350 posities (303s)
00:31:02   48000 tokens, 4598102 trades, 550760 posities (318s)
00:31:19   50000 tokens, 4799757 trades, 574399 posities (335s)
00:31:36   52000 tokens, 5016691 trades, 603626 posities (352s)
00:31:52   54000 tokens, 5200426 trades, 625224 posities (367s)
00:32:06   56000 tokens, 5365533 trades, 644406 posities (382s)
00:32:23   58000 tokens, 5562944 trades, 669075 posities (399s)
00:32:39   60000 tokens, 5746516 trades, 689739 posities (415s)
00:32:57   62000 tokens, 5955952 trades, 716730 posities (433s)
00:33:13   64000 tokens, 6142789 trades, 744367 posities (449s)
00:33:30   66000 tokens, 6356758 trades, 771423 posities (466s)
00:33:43   68000 tokens, 6541957 trades, 795263 posities (479s)
00:33:56   70000 tokens, 6731219 trades, 818210 posities (492s)
00:34:10   72000 tokens, 6922572 trades, 843202 posities (506s)
00:34:25   74000 tokens, 7133262 trades, 878980 posities (521s)
00:34:30 posities: 885811 uit 7196469 trades (529s)
00:34:43 211069 wallets gerekend
00:34:43 geluk-toets
00:35:19 persistentie
00:35:22 kopieer-simulatie
00:37:42 klaar in 721s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
23:35:28 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=42 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:35:29 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 12/42/171 | al gemeten: 312
23:40:44 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=44 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:40:45 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/38/168 | al gemeten: 315
23:46:54 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=46 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:46:55 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 9/38/167 | al gemeten: 318
00:38:57 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=52 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:38:58 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 9/39/161 | al gemeten: 339
00:43:37 ijk: +0 van 0 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=52 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:43:37 ijk-diagnose: nieuwste migratie 6.1 min oud | migraties 15/60/240 min: 6/37/156 | al gemeten: 339
00:48:54 ijk: +2 van 2 kandidaten (4 migraties in het venster, overgeslagen: {'al_gemeten': 2}) | verste bak n=54 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:48:54 ijk-diagnose: nieuwste migratie 1.9 min oud | migraties 15/60/240 min: 4/35/157 | al gemeten: 341
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
