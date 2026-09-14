# Schaduwbot status

- tijd: 2026-09-14 08:51:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 19 hours, 4 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.5G/38G | geheugen: 1912/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 94661, "tokens_in_memory": 4475, "msgs": 11739125, "trades": 2544314, "creates": 26395, "decode_fail": 217646, "rpc_calls": 75174, "rpc_errors": 6, "sol_usd": 101.32283005339112, "open_positions": 23, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 08:22:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:22:52,313 main INFO screen cashcaton pass=0 dev=0.11 ins=79.2 pro=9 1a=False 1b=True 2=True (54.1s)
Sep 14 08:23:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:23:23,792 main INFO screen INU pass=0 dev=0.0 ins=16.44 pro=39 1a=False 1b=False 2=True (54.3s)
Sep 14 08:23:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:23:44,758 main INFO screen danlarson pass=1 dev=0.0 ins=0.87 pro=13 1a=False 1b=False 2=False (48.8s)
Sep 14 08:24:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:24:25,578 main INFO screen danlarson pass=0 dev=0.0 ins=0.82 pro=5 1a=False 1b=False 2=False (49.0s)
Sep 14 08:25:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:25:35,020 main INFO screen danlarson pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (48.3s)
Sep 14 08:26:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:26:05,340 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:26:05 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:26:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:26:35,515 main INFO screen Los pass=0 dev=0.0 ins=17.53 pro=57 1a=False 1b=False 2=True (54.0s)
Sep 14 08:26:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:26:44,179 main INFO screen TRUMP2028 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.9s)
Sep 14 08:26:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:26:54,774 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.3s)
Sep 14 08:28:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:28:26,706 main INFO screen danlarson pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (49.2s)
Sep 14 08:28:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:28:50,282 main INFO screen Topblast pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (62.2s)
Sep 14 08:29:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:29:29,248 main INFO screen danlarson pass=1 dev=0.0 ins=0.87 pro=10 1a=False 1b=False 2=False (63.3s)
Sep 14 08:29:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:29:50,724 main INFO screen Los pass=0 dev=0.0 ins=7.71 pro=33 1a=False 1b=False 2=True (61.9s)
Sep 14 08:30:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:30:01,322 main INFO screen BATONGUY pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (55.6s)
Sep 14 08:31:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:31:08,460 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:31:08 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 08:31:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:31:13,489 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.4s)
Sep 14 08:33:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:33:03,523 main INFO screen CHAROC pass=0 dev=0.17 ins=0.0 pro=5 1a=False 1b=False 2=False (66.1s)
Sep 14 08:33:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:33:07,287 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.5s)
Sep 14 08:33:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:33:16,919 main INFO screen Los pass=0 dev=0.0 ins=29.76 pro=53 1a=False 1b=False 2=True (58.0s)
Sep 14 08:33:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:33:56,809 main INFO screen MrBeast pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 14 08:34:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:34:05,085 main INFO screen TAXCAT pass=0 dev=0.0 ins=30.07 pro=47 1a=False 1b=True 2=True (57.7s)
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:35:20,824 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 08:35:20 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 08:36:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:36:09,666 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:36:09 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:36:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:36:12,615 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 14 08:37:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:37:04,854 main INFO screen NUT pass=0 dev=0.0 ins=19.92 pro=72 1a=False 1b=False 2=True (57.8s)
Sep 14 08:37:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:37:36,557 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (52.5s)
Sep 14 08:38:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:38:00,298 main INFO screen DARWIN pass=0 dev=0.0 ins=13.27 pro=47 1a=False 1b=False 2=True (65.2s)
Sep 14 08:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:38:37,641 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 14 08:38:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:38:45,487 main INFO screen DeepSeek pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.1s)
Sep 14 08:38:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:38:54,911 main INFO screen Nasdaq6900 pass=0 dev=6.11 ins=72.68 pro=1 1a=False 1b=True 2=True (54.6s)
Sep 14 08:39:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:39:42,940 main INFO screen Los pass=0 dev=0.0 ins=18.62 pro=58 1a=False 1b=False 2=True (65.3s)
Sep 14 08:39:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:39:50,261 main INFO screen CHILLBIKE pass=0 dev=0.06 ins=77.91 pro=8 1a=False 1b=False 2=True (64.8s)
Sep 14 08:40:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:40:48,145 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.1s)
Sep 14 08:41:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:41:09,818 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.7s)
Sep 14 08:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:41:11,122 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:41:11 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:43:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:43:25,822 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.4s)
Sep 14 08:43:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:43:40,359 main INFO screen beer pass=0 dev=1.21 ins=0.0 pro=2 1a=False 1b=False 2=False (49.9s)
Sep 14 08:43:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:43:56,734 main INFO screen retire  pass=1 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (59.9s)
Sep 14 08:44:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:44:50,960 main INFO screen 肥嘟嘟 pass=0 dev=0.14 ins=79.2 pro=9 1a=False 1b=True 2=True (48.8s)
Sep 14 08:45:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:45:25,892 main INFO screen CATEUS pass=0 dev=0.7 ins=78.61 pro=2 1a=False 1b=True 2=True (51.7s)
Sep 14 08:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:45:33,882 main INFO screen tenn pass=0 dev=1.84 ins=0.0 pro=1 1a=False 1b=False 2=False (55.6s)
Sep 14 08:46:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:10,930 main INFO screen DD pass=0 dev=0.0 ins=18.93 pro=55 1a=False 1b=False 2=True (62.3s)
Sep 14 08:46:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:16,109 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:16 +0000] "UNKNOWN / HTTP/1.0" 400 447 "-" "-"
Sep 14 08:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:17,478 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:17 +0000] "UNKNOWN / HTTP/1.0" 400 447 "-" "-"
Sep 14 08:46:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:19,849 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:19 +0000] "UNKNOWN / HTTP/1.0" 400 447 "-" "-"
Sep 14 08:46:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:30,402 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:30 +0000] "GET / HTTP/1.1" 404 174 "-" "rawgrab"
Sep 14 08:46:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:30,772 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:30 +0000] "GET /raw HTTP/1.1" 404 174 "-" "rawgrab"
Sep 14 08:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:31,142 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:31 +0000] "GET /ws HTTP/1.1" 404 174 "-" "rawgrab"
Sep 14 08:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:31,518 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:31 +0000] "GET /socket.io/?EIO=4&transport=websocket HTTP/1.1" 404 174 "-" "rawgrab"
Sep 14 08:46:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:31,887 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:31 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:32,256 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:32 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:32,625 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:32 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:32,993 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:32 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:33,362 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:33 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:33,730 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:33 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:46:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:34,100 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:34 +0000] "GET /v1/vector/collections/describe HTTP/1.1" 404 174 "-" "-"
Sep 14 08:46:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:34,469 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:34 +0000] "GET /v1 HTTP/1.1" 404 174 "-" "-"
Sep 14 08:46:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:34,838 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:34 +0000] "GET / HTTP/1.1" 404 174 "-" "-"
Sep 14 08:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:35,286 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:35 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
Sep 14 08:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:35,669 aiohttp.access INFO 156.225.1.41 [14/Sep/2026:08:46:35 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "http://167.233.49.49:8080" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
Sep 14 08:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:46:37,159 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:46:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:48:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:48:12,983 main INFO screen QUANT pass=0 dev=0.0 ins=15.19 pro=58 1a=False 1b=False 2=True (64.3s)
Sep 14 08:48:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:48:20,655 main INFO screen NAMI pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (53.9s)
Sep 14 08:48:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:48:30,696 main INFO screen RICK pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (65.6s)
Sep 14 08:49:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:49:05,484 main INFO screen Gemini AI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 14 08:49:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:49:40,159 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 14 08:50:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:50:03,710 main INFO screen NTDA pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 14 08:50:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:50:13,229 main INFO screen meep pass=0 dev=1.0 ins=24.29 pro=63 1a=False 1b=False 2=True (64.6s)
Sep 14 08:50:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:50:31,809 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 14 08:51:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:51:49,540 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:51:49 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T07:22:16Z
--- update 2026-09-14T07:27:36Z
--- update 2026-09-14T07:32:56Z
--- update 2026-09-14T07:38:22Z
--- update 2026-09-14T07:43:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 70fffb71339a4c6280f71f7916117380
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T07:48:53Z
--- update 2026-09-14T07:54:36Z
--- update 2026-09-14T07:59:58Z
--- update 2026-09-14T08:05:13Z
--- update 2026-09-14T08:10:30Z
--- update 2026-09-14T08:15:36Z
--- update 2026-09-14T08:21:00Z
--- update 2026-09-14T08:26:04Z
--- update 2026-09-14T08:31:07Z
--- update 2026-09-14T08:36:08Z
--- update 2026-09-14T08:41:09Z
--- update 2026-09-14T08:46:36Z
--- update 2026-09-14T08:51:48Z
```

## Analyses (laatste 25 regels)
```
inactive
08:14:10   34000 tokens, 3437170 trades, 430248 posities (171s)
08:14:20   36000 tokens, 3647193 trades, 455311 posities (182s)
08:14:31   38000 tokens, 3851106 trades, 483245 posities (192s)
08:14:41   40000 tokens, 4036193 trades, 502424 posities (202s)
08:14:50   42000 tokens, 4215521 trades, 523353 posities (211s)
08:15:01   44000 tokens, 4423683 trades, 550075 posities (222s)
08:15:11   46000 tokens, 4625464 trades, 576790 posities (232s)
08:15:20   48000 tokens, 4826560 trades, 601404 posities (242s)
08:15:30   50000 tokens, 5027322 trades, 623297 posities (252s)
08:15:41   52000 tokens, 5209033 trades, 644607 posities (262s)
08:15:52   54000 tokens, 5386597 trades, 663148 posities (273s)
08:16:02   56000 tokens, 5579519 trades, 689954 posities (284s)
08:16:14   58000 tokens, 5769730 trades, 711633 posities (295s)
08:16:26   60000 tokens, 5968117 trades, 740459 posities (307s)
08:16:38   62000 tokens, 6171692 trades, 766550 posities (320s)
08:16:50   64000 tokens, 6380049 trades, 795543 posities (332s)
08:17:02   66000 tokens, 6573751 trades, 819478 posities (343s)
08:17:14   68000 tokens, 6767562 trades, 850720 posities (355s)
08:17:27   70000 tokens, 6978354 trades, 884198 posities (368s)
08:17:32 posities: 893588 uit 7039798 trades (377s)
08:17:46 196188 wallets gerekend
08:17:46 geluk-toets
08:18:26 persistentie
08:18:29 kopieer-simulatie
08:20:28 klaar in 553s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
08:05:14 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:10:35 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:15:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:21:04 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:26:05 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:31:08 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:36:09 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:41:10 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:46:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:51:49 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
