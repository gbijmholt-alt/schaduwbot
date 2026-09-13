# Schaduwbot status

- tijd: 2026-09-13 19:09:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 5 hours, 22 minutes
- bot-service: active
- code-versie: 3997123
- schijf: 4.9G/38G | geheugen: 1654/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 45329, "tokens_in_memory": 7160, "msgs": 4991005, "trades": 1113324, "creates": 11867, "decode_fail": 111354, "rpc_calls": 33224, "rpc_errors": 2, "sol_usd": 101.14101136094645, "open_positions": 30, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 18:54:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:17,151 main INFO screen UNDA pass=1 dev=1.97 ins=0.0 pro=58 1a=False 1b=False 2=False (65.0s)
Sep 13 18:54:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:34,270 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 13 18:54:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:36,162 main INFO screen BLACK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.0s)
Sep 13 18:54:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:41,800 aiohttp.access INFO 71.6.135.131 [13/Sep/2026:18:54:41 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
Sep 13 18:54:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:54:42,744 aiohttp.access INFO 71.6.135.131 [13/Sep/2026:18:54:42 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
Sep 13 18:55:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:55:10,154 main INFO screen Tiger pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.0s)
Sep 13 18:55:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:55:20,448 main INFO screen gek pass=0 dev=0.0 ins=43.65 pro=37 1a=False 1b=False 2=True (46.2s)
Sep 13 18:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:55:43,066 main INFO screen kaki pass=1 dev=3.37 ins=4.8 pro=54 1a=False 1b=False 2=False (66.9s)
Sep 13 18:56:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:56:07,235 main INFO screen JELLO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.1s)
Sep 13 18:56:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:56:23,695 main INFO screen BATONTRUMP pass=0 dev=0.05 ins=79.26 pro=9 1a=False 1b=True 2=True (63.2s)
Sep 13 18:56:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:56:31,697 main INFO screen PINGO pass=0 dev=0.0 ins=0.14 pro=2 1a=False 1b=False 2=True (48.6s)
Sep 13 18:56:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:56:54,477 main INFO screen COCA COLA pass=0 dev=0.0 ins=155.34 pro=1 1a=False 1b=False 2=True (47.2s)
Sep 13 18:57:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:57:36,534 main INFO screen ZGIGA pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=False 2=True (72.8s)
Sep 13 18:57:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:57:38,448 main INFO screen $OMT pass=0 dev=2.75 ins=0.0 pro=9 1a=False 1b=False 2=False (66.8s)
Sep 13 18:57:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:57:50,024 main INFO screen Silkie  pass=0 dev=0.0 ins=22.11 pro=66 1a=False 1b=False 2=True (55.5s)
Sep 13 18:58:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:58:45,553 main INFO screen HEAVEN pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (69.0s)
Sep 13 18:58:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:58:47,048 main INFO screen Saturween pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (68.6s)
Sep 13 18:58:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:58:52,128 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.1s)
Sep 13 18:59:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:59:25,229 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:59:25 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 18:59:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:59:34,740 aiohttp.access INFO 45.135.193.198 [13/Sep/2026:18:59:34 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 18:59:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:59:34,767 aiohttp.access INFO 45.135.193.198 [13/Sep/2026:18:59:34 +0000] "GET / HTTP/1.0" 404 174 "-" "0day"
Sep 13 19:00:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:00:02,422 main INFO screen ‎  pass=0 dev=0.0 ins=26.47 pro=74 1a=False 1b=False 2=True (76.9s)
Sep 13 19:00:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:00:10,114 main INFO screen wtf pass=0 dev=0.0 ins=21.58 pro=72 1a=False 1b=False 2=True (83.1s)
Sep 13 19:00:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:00:10,672 main INFO screen $CATO pass=1 dev=1.26 ins=0.0 pro=39 1a=False 1b=False 2=False (78.5s)
Sep 13 19:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:01:01,331 main INFO screen pisscoin pass=0 dev=13.0 ins=4.0 pro=35 1a=False 1b=False 2=False (58.9s)
Sep 13 19:01:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:01:20,172 main INFO screen 🧔🏿‍ pass=0 dev=0.0 ins=14.21 pro=42 1a=False 1b=False 2=True (69.5s)
Sep 13 19:01:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:01:21,307 main INFO screen CCBKB pass=0 dev=0.0 ins=0.33 pro=2 1a=False 1b=False 2=False (71.2s)
Sep 13 19:01:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:01:57,494 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (56.2s)
Sep 13 19:02:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:02:28,557 main INFO screen MSI pass=0 dev=0.0 ins=44.72 pro=41 1a=False 1b=False 2=True (68.4s)
Sep 13 19:02:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:02:29,750 main INFO screen PAYPAW pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (68.4s)
Sep 13 19:02:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:02:58,616 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (61.1s)
Sep 13 19:03:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:03:35,489 main INFO screen Tiger pass=0 dev=0.06 ins=0.0 pro=6 1a=False 1b=False 2=False (65.7s)
Sep 13 19:03:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:03:38,209 main INFO screen MELANIA pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (69.7s)
Sep 13 19:03:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:03:51,124 main INFO screen BLAST AI pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 13 19:04:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:04:27,161 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:19:04:27 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 19:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:04:46,735 main INFO screen Life pass=0 dev=0.0 ins=15.85 pro=64 1a=False 1b=False 2=True (71.2s)
Sep 13 19:04:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:04:48,888 main INFO screen FFN pass=0 dev=0.01 ins=0.0 pro=9 1a=False 1b=False 2=False (70.7s)
Sep 13 19:04:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:04:55,447 main INFO screen SOLCAT pass=0 dev=0.0 ins=28.6 pro=63 1a=False 1b=False 2=True (64.3s)
Sep 13 19:05:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:05:45,783 main INFO screen HAALAND pass=0 dev=0.0 ins=32.16 pro=14 1a=False 1b=False 2=True (50.3s)
Sep 13 19:05:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:05:58,469 main INFO screen $SLEEP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.6s)
Sep 13 19:06:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:06:01,038 main INFO screen COOKED pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (74.3s)
Sep 13 19:06:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:06:58,945 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.2s)
Sep 13 19:07:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:07:07,772 main INFO screen $SLEEP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.3s)
Sep 13 19:07:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:07:10,778 main INFO screen Tiger pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (69.7s)
Sep 13 19:08:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:08:07,915 main INFO screen fries pass=0 dev=0.0 ins=50.19 pro=45 1a=False 1b=False 2=True (69.0s)
Sep 13 19:08:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:08:11,178 main INFO screen Bibendum pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (63.4s)
Sep 13 19:08:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:08:13,832 main INFO screen XLK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (63.1s)
Sep 13 19:08:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:08:57,166 main INFO screen $BHSL pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (49.3s)
Sep 13 19:09:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:09:19,575 main INFO screen DERP pass=0 dev=1.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.7s)
Sep 13 19:09:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:09:20,129 main INFO screen balloon pass=1 dev=4.46 ins=0.0 pro=47 1a=False 1b=False 2=False (69.0s)
Sep 13 19:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 19:09:36,720 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:19:09:36 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-13T18:59:24Z
--- update 2026-09-13T19:04:26Z
--- update 2026-09-13T19:09:35Z
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
