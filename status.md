# Schaduwbot status

- tijd: 2026-09-13 08:50:26 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 19 hours, 3 minutes
- bot-service: active
- code-versie: 07fffe0
- schijf: 4.4G/38G | geheugen: 697/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 8179, "tokens_in_memory": 1468, "msgs": 451068, "trades": 119375, "creates": 1468, "decode_fail": 17469, "rpc_calls": 4099, "rpc_errors": 1, "sol_usd": 100.0517128976131, "open_positions": 16, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 08:18:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:18:44,787 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:18:44 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 08:19:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:19:42,591 main INFO screen COCA COLA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.1s)
Sep 13 08:21:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:21:52,254 main INFO screen $KB pass=0 dev=0.0 ins=0.21 pro=3 1a=False 1b=False 2=False (70.3s)
Sep 13 08:23:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:23:35,332 main INFO screen BMW pass=0 dev=1.4 ins=0.0 pro=5 1a=False 1b=False 2=False (67.2s)
Sep 13 08:23:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:23:38,088 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 13 08:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:23:47,352 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:23:47 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 08:25:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:25:26,785 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=77.86 pro=18 1a=False 1b=True 2=True (55.6s)
Sep 13 08:25:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:25:56,699 main INFO screen Crypto-Bros pass=0 dev=0.0 ins=28.79 pro=47 1a=False 1b=False 2=True (65.4s)
Sep 13 08:25:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:25:59,492 main INFO screen Fortnite pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (72.2s)
Sep 13 08:26:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:26:47,728 main INFO screen foff pass=0 dev=0.11 ins=0.0 pro=6 1a=False 1b=False 2=False (80.9s)
Sep 13 08:26:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:26:54,561 main INFO screen BABYPUMP pass=0 dev=40.28 ins=0.0 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 13 08:27:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:27:34,029 main INFO screen KŁAK pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (77.0s)
Sep 13 08:27:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:27:57,862 main INFO screen 蛙奶 pass=0 dev=37.46 ins=0.0 pro=5 1a=False 1b=False 2=True (70.1s)
Sep 13 08:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:28:23,219 aiohttp.access INFO 165.154.135.211 [13/Sep/2026:08:28:23 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
Sep 13 08:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:28:23,560 aiohttp.access INFO 165.154.135.211 [13/Sep/2026:08:28:23 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
Sep 13 08:28:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:28:39,915 main INFO screen GIGACAT pass=1 dev=0.0 ins=18.23 pro=51 1a=False 1b=False 2=False (74.8s)
Sep 13 08:28:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:28:56,679 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:28:56 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 13 08:29:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:29:20,213 aiohttp.access INFO 165.154.135.211 [13/Sep/2026:08:29:20 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
Sep 13 08:29:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:29:37,410 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (76.3s)
Sep 13 08:31:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:31:28,388 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 13 08:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:33:21,102 aiohttp.access INFO 107.150.101.107 [13/Sep/2026:08:33:21 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"
Sep 13 08:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:33:21,453 aiohttp.access INFO 107.150.101.107 [13/Sep/2026:08:33:21 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"
Sep 13 08:33:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:33:53,442 main INFO screen WGC pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (79.1s)
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:34:54,384 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:34:54,552 aiohttp.access INFO 107.150.101.107 [13/Sep/2026:08:34:54 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
Sep 13 08:34:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:34:54,553 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:34:54 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 08:35:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:35:51,530 main INFO screen BWC pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (124.7s)
Sep 13 08:35:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:35:58,484 main INFO screen MIZO pass=0 dev=7.86 ins=7.07 pro=60 1a=False 1b=False 2=False (118.1s)
Sep 13 08:35:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:35:58,919 main INFO screen GS pass=0 dev=0.0 ins=17.89 pro=36 1a=False 1b=False 2=True (118.3s)
Sep 13 08:36:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:36:38,346 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.8s)
Sep 13 08:36:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:36:50,790 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.3s)
Sep 13 08:37:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:37:03,155 main INFO screen ROBINCOIN pass=0 dev=0.59 ins=0.0 pro=8 1a=False 1b=False 2=False (63.7s)
Sep 13 08:37:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:37:26,926 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.6s)
Sep 13 08:37:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:37:59,238 main INFO screen GTA 6 pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (46.0s)
Sep 13 08:39:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:39:37,007 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:39:37 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 08:40:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:31,058 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:31 +0000] "GET / HTTP/1.1" 404 174 "-" "-"
Sep 13 08:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:35,667 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:35 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 08:40:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:36,726 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:36 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:37,520 aiohttp.server ERROR Error handling request from 199.45.155.48
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/.venv/lib/python3.14/site-packages/aiohttp/web_protocol.py", line 433, in data_received
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:     messages, upgraded, tail = self._parser.feed_data(data)
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:   Pause on PRI/Upgrade:
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:     b'\x00\x00\x18\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x04\x00\x00Bh\x00\x06\x00\x04\x00\x00\x00\x03\x00\x00\x00\n'
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]:       ^
Sep 13 08:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:37,525 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:37 +0000] "UNKNOWN / HTTP/1.0" 400 321 "-" "-"
Sep 13 08:40:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:48,717 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:48 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 08:40:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:40:49,890 aiohttp.access INFO 199.45.155.48 [13/Sep/2026:08:40:49 +0000] "GET /ads.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 08:41:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:41:14,135 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.5s)
Sep 13 08:41:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:41:22,312 main INFO screen AMERICA pass=0 dev=0.0 ins=30.42 pro=31 1a=False 1b=False 2=True (47.0s)
Sep 13 08:41:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:41:57,860 main INFO screen KFC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.8s)
Sep 13 08:42:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:42:13,413 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.1s)
Sep 13 08:44:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:44:04,200 main INFO screen ROMAN pass=0 dev=0.0 ins=19.78 pro=44 1a=False 1b=False 2=True (61.7s)
Sep 13 08:44:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:44:07,377 main INFO screen EMBER pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (47.6s)
Sep 13 08:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:44:37,470 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:44:37 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 08:44:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:44:50,080 main INFO screen MIZO pass=0 dev=0.0 ins=57.29 pro=6 1a=True 1b=True 2=True (50.5s)
Sep 13 08:45:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:15,507 main INFO screen ROBINCAT pass=0 dev=0.16 ins=0.0 pro=4 1a=False 1b=False 2=False (66.0s)
Sep 13 08:45:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:47,868 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:45:47 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
Sep 13 08:45:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:48,208 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:45:48 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
Sep 13 08:46:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:46:20,370 main INFO screen ONLY CATS pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (62.4s)
Sep 13 08:46:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:46:41,073 main INFO screen stonk pass=1 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (59.5s)
Sep 13 08:47:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:47:03,224 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:47:03 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
Sep 13 08:48:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:48:45,298 main INFO screen stonk pass=1 dev=0.0 ins=0.05 pro=23 1a=False 1b=False 2=False (56.8s)
Sep 13 08:49:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:11,443 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=77.83 pro=16 1a=False 1b=True 2=True (53.3s)
Sep 13 08:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:20,899 rpc WARNING rpc getTokenLargestAccounts exc Server disconnected
Sep 13 08:49:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:34,712 main INFO screen CATGPTCOIN pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (52.8s)
Sep 13 08:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:50:26,900 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:50:26 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T07:31:36Z
--- update 2026-09-13T07:36:44Z
--- update 2026-09-13T07:41:52Z
--- update 2026-09-13T07:47:15Z
--- update 2026-09-13T07:52:32Z
--- update 2026-09-13T07:57:36Z
--- update 2026-09-13T08:03:13Z
--- update 2026-09-13T08:08:31Z
nieuwe code: 07fffe0
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T08:13:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: b4b7c9968a0b4737b409c444043a32eb
analyses gestart (1bfbb7483d38)
--- update 2026-09-13T08:18:43Z
--- update 2026-09-13T08:23:46Z
--- update 2026-09-13T08:28:55Z
--- update 2026-09-13T08:34:36Z
--- update 2026-09-13T08:39:35Z
--- update 2026-09-13T08:44:36Z
--- update 2026-09-13T08:50:25Z
```

## Analyses (laatste 25 regels)
```
inactive
08:25:22   14000 tokens, 1549605 trades, 247130 posities (14s)
08:25:24   16000 tokens, 1757279 trades, 277445 posities (16s)
08:25:26   18000 tokens, 2004003 trades, 322993 posities (19s)
08:25:28   20000 tokens, 2234751 trades, 364761 posities (21s)
08:25:30   22000 tokens, 2460758 trades, 399176 posities (23s)
08:25:32   24000 tokens, 2665257 trades, 429618 posities (24s)
08:25:34   26000 tokens, 2912541 trades, 470802 posities (26s)
08:25:36   28000 tokens, 3130628 trades, 506085 posities (28s)
08:25:38   30000 tokens, 3342675 trades, 538677 posities (30s)
08:25:40   32000 tokens, 3593261 trades, 584916 posities (32s)
08:25:42   34000 tokens, 3804322 trades, 614565 posities (34s)
08:25:44   36000 tokens, 4028980 trades, 652010 posities (36s)
08:25:46   38000 tokens, 4232437 trades, 683408 posities (38s)
08:25:48   40000 tokens, 4463353 trades, 722688 posities (41s)
08:25:50   42000 tokens, 4682973 trades, 758406 posities (42s)
08:25:52   44000 tokens, 4899790 trades, 796612 posities (45s)
08:25:54   46000 tokens, 5133220 trades, 832981 posities (47s)
08:25:57   48000 tokens, 5373431 trades, 876583 posities (49s)
08:25:58   50000 tokens, 5581346 trades, 921795 posities (51s)
08:25:59 posities: 939120 uit 5660548 trades (52s)
08:26:11 195681 wallets gerekend
08:26:12 geluk-toets
08:26:46 persistentie
08:26:49 kopieer-simulatie
08:27:16 klaar in 128s -> /opt/schaduwbot/reports/wallets.md
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
