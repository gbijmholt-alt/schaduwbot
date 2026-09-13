# Schaduwbot status

- tijd: 2026-09-13 18:54:16 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 5 hours, 7 minutes
- bot-service: active
- code-versie: 3997123
- schijf: 4.9G/38G | geheugen: 1635/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 44408, "tokens_in_memory": 7075, "msgs": 4845633, "trades": 1085407, "creates": 11551, "decode_fail": 109252, "rpc_calls": 32259, "rpc_errors": 2, "sol_usd": 101.24809612276952, "open_positions": 40, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 18:34:59 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 18:35:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:35:41,896 main INFO screen CORGI pass=0 dev=0.0 ins=45.31 pro=41 1a=False 1b=False 2=True (108.2s)
Sep 13 18:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:36:01,343 main INFO screen nubillions pass=1 dev=0.0 ins=7.27 pro=40 1a=False 1b=False 2=False (113.5s)
Sep 13 18:36:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:36:02,696 main INFO screen BULLSON pass=0 dev=10.23 ins=31.3 pro=24 1a=True 1b=False 2=True (115.1s)
Sep 13 18:36:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:36:59,470 main INFO screen Nono pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (77.6s)
Sep 13 18:37:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:37:04,879 main INFO screen ANONWIFCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.5s)
Sep 13 18:37:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:37:08,006 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.3s)
Sep 13 18:37:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:37:50,289 main INFO screen 牛来SOL pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 13 18:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:38:10,335 main INFO screen OpenAI pass=0 dev=0.0 ins=155.01 pro=1 1a=False 1b=False 2=True (62.3s)
Sep 13 18:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:38:10,701 main INFO screen KOON-SAN pass=0 dev=0.0 ins=26.16 pro=40 1a=False 1b=False 2=True (65.8s)
Sep 13 18:38:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:38:27,422 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:38:27 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 18:38:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:38:59,554 main INFO screen DOWNGPT pass=0 dev=0.04 ins=78.25 pro=7 1a=False 1b=False 2=True (69.3s)
Sep 13 18:39:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:39:19,295 main INFO screen BSMITH pass=0 dev=0.0 ins=0.16 pro=9 1a=False 1b=False 2=True (69.0s)
Sep 13 18:39:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:39:20,748 main INFO screen Shift pass=1 dev=0.0 ins=3.96 pro=32 1a=False 1b=False 2=False (70.0s)
Sep 13 18:40:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:40:10,776 main INFO screen CLAUDE pass=0 dev=0.0 ins=0.04 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 13 18:40:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:40:12,610 main INFO screen JubWhale pass=0 dev=0.75 ins=79.26 pro=7 1a=False 1b=True 2=True (53.3s)
Sep 13 18:40:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:40:17,698 main INFO screen PRINT pass=0 dev=0.0 ins=47.08 pro=46 1a=False 1b=False 2=True (56.9s)
Sep 13 18:41:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:41:22,105 main INFO screen pearl pass=0 dev=0.0 ins=33.66 pro=59 1a=False 1b=False 2=True (71.3s)
Sep 13 18:41:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:41:23,461 main INFO screen BlackPearl pass=1 dev=0.0 ins=16.9 pro=57 1a=False 1b=False 2=False (70.9s)
Sep 13 18:41:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:41:26,516 main INFO screen GRAPE pass=0 dev=0.0 ins=27.36 pro=69 1a=False 1b=False 2=True (68.8s)
Sep 13 18:42:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:42:35,660 main INFO screen NUT pass=0 dev=0.0 ins=23.94 pro=78 1a=False 1b=False 2=True (72.2s)
Sep 13 18:42:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:42:37,165 main INFO screen $LLAMA pass=1 dev=0.35 ins=0.0 pro=14 1a=False 1b=False 2=False (75.1s)
Sep 13 18:42:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:42:40,198 main INFO screen SWAMIS pass=0 dev=0.0 ins=21.47 pro=61 1a=False 1b=False 2=True (73.7s)
Sep 13 18:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:43:37,146 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:43:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 18:43:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:43:46,653 main INFO screen Moon pass=0 dev=0.0 ins=15.98 pro=66 1a=False 1b=False 2=True (69.5s)
Sep 13 18:43:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:43:49,553 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.4s)
Sep 13 18:43:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:43:50,151 main INFO screen Moon pass=0 dev=0.0 ins=17.2 pro=64 1a=False 1b=False 2=True (74.5s)
Sep 13 18:44:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:44:33,703 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.0s)
Sep 13 18:44:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:44:54,328 main INFO screen Silverback pass=0 dev=0.07 ins=20.78 pro=65 1a=False 1b=False 2=True (64.2s)
Sep 13 18:44:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:44:55,856 main INFO screen Tiger pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.3s)
Sep 13 18:45:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:45:27,529 main INFO screen PUNk pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 13 18:46:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:46:00,616 main INFO screen GTA6 pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (66.3s)
Sep 13 18:46:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:46:02,066 main INFO screen TEXAS pass=0 dev=0.0 ins=21.64 pro=66 1a=False 1b=False 2=True (66.2s)
Sep 13 18:46:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:46:24,162 main INFO screen HALH pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 13 18:47:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:47:06,818 main INFO screen MEMESCOPE pass=0 dev=0.0 ins=49.1 pro=53 1a=False 1b=False 2=True (64.8s)
Sep 13 18:47:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:47:09,361 main INFO screen FALCON9 pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (68.7s)
Sep 13 18:47:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:47:30,871 main INFO screen Chihuahua pass=0 dev=0.0 ins=23.9 pro=68 1a=False 1b=False 2=True (66.7s)
Sep 13 18:48:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:48:11,631 main INFO screen Tiger pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 13 18:48:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:48:13,554 main INFO screen Records pass=1 dev=0.0 ins=17.32 pro=63 1a=False 1b=False 2=False (66.7s)
Sep 13 18:48:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:48:21,062 main INFO screen pepsolq pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (50.2s)
Sep 13 18:49:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:49:02,931 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:49:02 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 18:49:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:49:03,493 main INFO screen CatGPT pass=0 dev=0.72 ins=72.68 pro=0 1a=True 1b=True 2=True (51.9s)
Sep 13 18:49:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:49:17,114 main INFO screen SMC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.6s)
Sep 13 18:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:49:21,577 main INFO screen $SLEEP pass=0 dev=40.35 ins=0.0 pro=1 1a=False 1b=False 2=True (60.5s)
Sep 13 18:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:49:56,038 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.5s)
Sep 13 18:50:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:50:09,955 main INFO screen JOINT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.8s)
Sep 13 18:50:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:50:10,362 main INFO screen FAIR pass=0 dev=97.21 ins=0.0 pro=1 1a=False 1b=False 2=True (48.8s)
Sep 13 18:51:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:04,652 main INFO screen NOVAN pass=1 dev=0.0 ins=1.72 pro=12 1a=False 1b=False 2=False (68.6s)
Sep 13 18:51:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:08,876 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:08 +0000] "GET / HTTP/1.1" 404 174 "-" "-"
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:13,021 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:13 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:13,602 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:13 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:13,809 aiohttp.server ERROR Error handling request from 167.94.146.52
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/.venv/lib/python3.14/site-packages/aiohttp/web_protocol.py", line 433, in data_received
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:     messages, upgraded, tail = self._parser.feed_data(data)
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:   Pause on PRI/Upgrade:
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:     b'\x00\x00\x18\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x04\x00\x00Bh\x00\x06\x00\x04\x00\x00\x00\x03\x00\x00\x00\n'
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]:       ^
Sep 13 18:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:13,811 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:13 +0000] "UNKNOWN / HTTP/1.0" 400 321 "-" "-"
Sep 13 18:51:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:15,576 main INFO screen CHONAN pass=0 dev=0.0 ins=18.38 pro=18 1a=False 1b=False 2=True (65.6s)
Sep 13 18:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:17,081 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:17 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 18:51:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:17,107 aiohttp.access INFO 167.94.146.52 [13/Sep/2026:18:51:17 +0000] "GET /.well-known/security.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 18:51:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:51:19,372 main INFO screen Moon pass=1 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (69.0s)
Sep 13 18:52:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:52:20,221 main INFO screen STICKY pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (75.6s)
Sep 13 18:52:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:52:24,178 main INFO screen Moon pass=0 dev=0.0 ins=9.22 pro=57 1a=False 1b=False 2=True (68.6s)
Sep 13 18:52:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:52:28,659 main INFO screen SWEET pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=False (69.3s)
Sep 13 18:53:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:53:12,128 main INFO screen Door dash  pass=0 dev=0.2 ins=0.0 pro=1 1a=False 1b=False 2=False (51.9s)
Sep 13 18:53:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:53:26,128 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.9s)
Sep 13 18:53:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:53:31,230 main INFO screen LSSK pass=0 dev=0.35 ins=78.96 pro=9 1a=False 1b=False 2=True (62.6s)
Sep 13 18:54:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:16,385 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:54:16 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T17:34:49Z
--- update 2026-09-13T17:40:05Z
--- update 2026-09-13T17:45:17Z
--- update 2026-09-13T17:50:26Z
--- update 2026-09-13T17:55:36Z
--- update 2026-09-13T18:00:58Z
nieuwe code: 3997123
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 277a60b2a54543f3adc6304d0d8680f0
analyses gestart (87dd80a5c10e)
--- update 2026-09-13T18:06:06Z
--- update 2026-09-13T18:11:19Z
--- update 2026-09-13T18:16:36Z
--- update 2026-09-13T18:21:59Z
--- update 2026-09-13T18:27:36Z
--- update 2026-09-13T18:33:15Z
--- update 2026-09-13T18:38:26Z
--- update 2026-09-13T18:43:36Z
--- update 2026-09-13T18:49:01Z
--- update 2026-09-13T18:54:15Z
```

## Analyses (laatste 25 regels)
```
inactive
18:24:03   22000 tokens, 2379816 trades, 358635 posities (98s)
18:24:12   24000 tokens, 2605389 trades, 394418 posities (107s)
18:24:21   26000 tokens, 2807825 trades, 420330 posities (116s)
18:24:30   28000 tokens, 3010134 trades, 449840 posities (125s)
18:24:40   30000 tokens, 3245462 trades, 483434 posities (134s)
18:24:48   32000 tokens, 3461736 trades, 518331 posities (142s)
18:24:56   34000 tokens, 3665018 trades, 546460 posities (151s)
18:25:04   36000 tokens, 3884834 trades, 581386 posities (159s)
18:25:12   38000 tokens, 4099273 trades, 614735 posities (167s)
18:25:20   40000 tokens, 4302730 trades, 642941 posities (175s)
18:25:29   42000 tokens, 4515773 trades, 671872 posities (184s)
18:25:37   44000 tokens, 4713499 trades, 702489 posities (192s)
18:25:47   46000 tokens, 4943381 trades, 740198 posities (202s)
18:25:56   48000 tokens, 5130329 trades, 768122 posities (210s)
18:26:05   50000 tokens, 5347610 trades, 802737 posities (220s)
18:26:15   52000 tokens, 5575428 trades, 837726 posities (230s)
18:26:26   54000 tokens, 5801341 trades, 873712 posities (240s)
18:26:35   56000 tokens, 6017713 trades, 911880 posities (250s)
18:26:44   58000 tokens, 6223270 trades, 953012 posities (259s)
18:26:47 posities: 967684 uit 6293738 trades (262s)
18:27:00 201693 wallets gerekend
18:27:01 geluk-toets
18:27:36 persistentie
18:27:39 kopieer-simulatie
18:29:09 klaar in 405s -> /opt/schaduwbot/reports/wallets.md
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
