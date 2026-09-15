# Schaduwbot status

- tijd: 2026-09-15 23:55:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 10 hours, 8 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.9G/38G | geheugen: 2455/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 235302, "tokens_in_memory": 11486, "msgs": 41583786, "trades": 7794249, "creates": 82405, "decode_fail": 643435, "rpc_calls": 214233, "rpc_errors": 19, "sol_usd": 96.91168100505458, "open_positions": 64, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 23:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:36:36,969 main INFO screen FLY HIGH pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (127.6s)
Sep 15 23:37:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:09,451 main INFO screen sol pass=0 dev=0.0 ins=24.3 pro=5 1a=False 1b=False 2=True (69.5s)
Sep 15 23:37:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:43,463 main INFO screen URMOM pass=0 dev=0.0 ins=8.47 pro=70 1a=False 1b=False 2=True (66.5s)
Sep 15 23:37:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:46,075 main INFO screen compute pass=0 dev=0.0 ins=18.79 pro=5 1a=False 1b=False 2=True (70.5s)
Sep 15 23:38:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:03,479 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.0s)
Sep 15 23:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:46,313 main INFO screen Mafia pass=0 dev=0.0 ins=4.85 pro=55 1a=False 1b=False 2=True (60.2s)
Sep 15 23:38:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:48,230 main INFO screen LMEOW pass=0 dev=0.0 ins=35.3 pro=25 1a=False 1b=False 2=True (64.8s)
Sep 15 23:39:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:06,841 main INFO screen OnlyFlies pass=0 dev=0.0 ins=14.58 pro=56 1a=False 1b=False 2=False (63.4s)
Sep 15 23:39:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:52,629 main INFO screen CATNIS  pass=0 dev=0.02 ins=0.0 pro=3 1a=False 1b=False 2=False (64.4s)
Sep 15 23:39:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:54,354 main INFO screen NVDA pass=0 dev=0.0 ins=25.1 pro=0 1a=False 1b=False 2=True (68.0s)
Sep 15 23:39:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:58,532 main INFO screen AUTONOMOUS pass=0 dev=0.0 ins=6.53 pro=48 1a=False 1b=False 2=False (51.7s)
Sep 15 23:40:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:40:32,073 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:40:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:40:56,220 main INFO screen BUFFO pass=0 dev=0.0 ins=79.13 pro=2 1a=False 1b=True 2=True (61.9s)
Sep 15 23:40:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:40:57,466 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.8s)
Sep 15 23:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:40:59,500 aiohttp.access INFO 66.132.195.46 [15/Sep/2026:23:40:59 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 23:41:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:01,815 aiohttp.access INFO 66.132.195.46 [15/Sep/2026:23:41:01 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:05,077 main INFO screen € pass=0 dev=0.0 ins=19.63 pro=2 1a=False 1b=False 2=True (66.5s)
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:05,230 aiohttp.server ERROR Error handling request from 66.132.195.46
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/.venv/lib/python3.14/site-packages/aiohttp/web_protocol.py", line 433, in data_received
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:     messages, upgraded, tail = self._parser.feed_data(data)
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:     raise ex
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:   Pause on PRI/Upgrade:
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:     b'\x00\x00\x18\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x04\x00\x00Bh\x00\x06\x00\x04\x00\x00\x00\x03\x00\x00\x00\n'
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]:       ^
Sep 15 23:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:05,233 aiohttp.access INFO 66.132.195.46 [15/Sep/2026:23:41:05 +0000] "UNKNOWN / HTTP/1.0" 400 321 "-" "-"
Sep 15 23:41:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:40,456 aiohttp.access INFO 66.132.195.46 [15/Sep/2026:23:41:40 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 23:41:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:41:41,746 aiohttp.access INFO 66.132.195.46 [15/Sep/2026:23:41:41 +0000] "GET /login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 15 23:42:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:42:00,805 main INFO screen ASPIRIN pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (63.3s)
Sep 15 23:42:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:42:02,309 main INFO screen COVID26 pass=0 dev=0.0 ins=20.08 pro=1 1a=False 1b=False 2=False (66.1s)
Sep 15 23:42:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:42:05,305 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.2s)
Sep 15 23:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:42:52,108 main INFO screen FGTV pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.8s)
Sep 15 23:43:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:43:05,680 main INFO screen Cadillac pass=0 dev=0.0 ins=161.48 pro=0 1a=False 1b=False 2=True (60.4s)
Sep 15 23:43:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:43:07,217 main INFO screen eyes pass=0 dev=0.0 ins=7.31 pro=69 1a=False 1b=False 2=False (66.4s)
Sep 15 23:43:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:43:45,602 main INFO screen R1CH pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (53.5s)
Sep 15 23:44:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:44:11,210 main INFO screen NTFS pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (64.0s)
Sep 15 23:44:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:44:12,612 main INFO screen SARS-COV-2 pass=0 dev=0.0 ins=27.95 pro=65 1a=False 1b=False 2=True (66.9s)
Sep 15 23:44:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:44:40,046 main INFO screen FLY HIGH pass=0 dev=0.0 ins=1.64 pro=54 1a=False 1b=False 2=False (54.4s)
Sep 15 23:45:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:45:02,232 main INFO screen FSD pass=0 dev=0.0 ins=23.89 pro=4 1a=False 1b=False 2=False (51.0s)
Sep 15 23:45:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:45:05,629 main INFO screen Covid-26 pass=0 dev=0.0 ins=37.33 pro=60 1a=False 1b=False 2=True (53.0s)
Sep 15 23:45:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:45:29,688 main INFO screen CATNIS  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.6s)
Sep 15 23:45:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:45:37,200 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:45:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:46:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:46:04,375 main INFO screen BRZ pass=0 dev=0.0 ins=25.95 pro=39 1a=False 1b=False 2=True (58.7s)
Sep 15 23:46:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:46:05,881 main INFO screen OpenPerps pass=0 dev=0.0 ins=49.5 pro=22 1a=False 1b=False 2=True (63.6s)
Sep 15 23:46:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:46:36,986 main INFO screen LMEOW pass=0 dev=0.0 ins=35.3 pro=13 1a=False 1b=False 2=True (67.3s)
Sep 15 23:47:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:47:11,088 main INFO screen Covid-26 pass=0 dev=0.0 ins=12.62 pro=30 1a=False 1b=False 2=False (66.7s)
Sep 15 23:47:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:47:12,581 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (66.7s)
Sep 15 23:47:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:47:41,788 main INFO screen cap pass=0 dev=0.0 ins=39.53 pro=69 1a=False 1b=False 2=True (64.8s)
Sep 15 23:48:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:48:09,342 main INFO screen $CTO pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (58.3s)
Sep 15 23:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:48:18,284 main INFO screen otis pass=0 dev=0.0 ins=35.26 pro=79 1a=False 1b=False 2=True (65.7s)
Sep 15 23:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:48:31,871 main INFO screen BRZ pass=0 dev=0.0 ins=25.94 pro=64 1a=False 1b=False 2=True (50.1s)
Sep 15 23:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:49:13,613 main INFO screen DEBTPOOL pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=True (64.3s)
Sep 15 23:49:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:49:18,138 main INFO screen MARS pass=0 dev=0.0 ins=12.23 pro=57 1a=False 1b=False 2=False (59.9s)
Sep 15 23:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:49:19,657 main INFO screen SARS-CoV-2 pass=0 dev=0.0 ins=29.11 pro=34 1a=False 1b=False 2=True (47.8s)
Sep 15 23:50:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:50:03,960 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (50.3s)
Sep 15 23:50:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:50:05,433 main INFO screen batCoV pass=0 dev=0.0 ins=34.89 pro=30 1a=False 1b=False 2=True (47.3s)
Sep 15 23:50:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:50:11,466 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.8s)
Sep 15 23:50:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:50:41,415 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:50:41 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:50:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:50:59,101 main INFO screen WTEAMINU pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (55.1s)
Sep 15 23:51:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:51:01,991 main INFO screen bdjdjjd pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (56.6s)
Sep 15 23:51:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:51:09,370 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 15 23:51:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:51:59,575 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.5s)
Sep 15 23:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:15,493 main INFO screen otis pass=0 dev=0.0 ins=30.65 pro=61 1a=False 1b=False 2=True (73.5s)
Sep 15 23:52:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:17,240 main INFO screen beer pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 15 23:52:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:59,017 main INFO screen cbBTC pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (59.4s)
Sep 15 23:53:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:25,042 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.5s)
Sep 15 23:53:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:30,833 main INFO screen Rich pass=0 dev=0.0 ins=19.31 pro=0 1a=False 1b=False 2=False (73.6s)
Sep 15 23:53:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:55,513 main INFO screen XPXGOLD pass=0 dev=0.0 ins=2.08 pro=0 1a=False 1b=False 2=True (56.5s)
Sep 15 23:54:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:22,319 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.3s)
Sep 15 23:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:28,053 main INFO screen DUBS pass=0 dev=0.0 ins=25.79 pro=1 1a=False 1b=False 2=False (57.2s)
Sep 15 23:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:54,144 main INFO screen YBR pass=0 dev=0.55 ins=0.0 pro=4 1a=False 1b=False 2=False (58.6s)
Sep 15 23:55:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:29,317 main INFO screen att pass=0 dev=0.21 ins=10.99 pro=9 1a=False 1b=False 2=False (67.0s)
Sep 15 23:55:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:30,755 main INFO screen parsa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.7s)
Sep 15 23:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:38,100 aiohttp.access INFO 143.198.60.223 [15/Sep/2026:23:55:38 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
Sep 15 23:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:38,426 aiohttp.access INFO 143.198.60.223 [15/Sep/2026:23:55:38 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "http://167.233.49.49:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
Sep 15 23:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:43,275 main INFO screen NTDA pass=0 dev=0.0 ins=146.38 pro=1 1a=False 1b=False 2=True (49.1s)
Sep 15 23:55:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:49,741 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:55:49 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T22:26:45Z
--- update 2026-09-15T22:31:47Z
--- update 2026-09-15T22:37:16Z
--- update 2026-09-15T22:42:34Z
--- update 2026-09-15T22:47:36Z
--- update 2026-09-15T22:52:48Z
--- update 2026-09-15T22:58:28Z
--- update 2026-09-15T23:03:36Z
--- update 2026-09-15T23:09:15Z
--- update 2026-09-15T23:14:26Z
Running as unit: schaduwbot-wallets.service; invocation ID: 28b70ef890d5475a9c6286045b142940
analyses gestart (84579ff37485)
--- update 2026-09-15T23:19:31Z
--- update 2026-09-15T23:24:33Z
--- update 2026-09-15T23:29:36Z
--- update 2026-09-15T23:35:22Z
--- update 2026-09-15T23:40:30Z
--- update 2026-09-15T23:45:36Z
--- update 2026-09-15T23:50:40Z
--- update 2026-09-15T23:55:48Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 20:07:44
20:07:45 venster 2026-09-13 08:07 UTC .. nu, 70021 tokens
20:08:37 klaar in 53s: 53536 tokens, 1839 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 21:09:36
21:09:36 venster 2026-09-13 09:09 UTC .. nu, 71175 tokens
21:10:29 klaar in 53s: 54456 tokens, 1720 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 22:11:40
22:11:40 venster 2026-09-13 10:11 UTC .. nu, 72419 tokens
22:12:33 klaar in 54s: 55545 tokens, 1912 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 23:14:26
23:14:27 venster 2026-09-13 11:14 UTC .. nu, 73409 tokens
23:15:28 klaar in 61s: 56398 tokens, 1848 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
23:24:43 ijk: +2 van 2 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=442 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:24:44 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 13/48/192 | al gemeten: 902
23:29:49 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=444 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:29:49 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 9/47/192 | al gemeten: 905
23:35:32 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=446 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:35:32 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 7/45/194 | al gemeten: 907
23:40:55 ijk: +5 van 5 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=450 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:40:56 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 11/46/197 | al gemeten: 912
23:46:02 ijk: +5 van 5 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=453 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:46:02 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 13/46/195 | al gemeten: 917
23:50:45 ijk: +1 van 1 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=453 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:50:46 ijk-diagnose: nieuwste migratie 4.9 min oud | migraties 15/60/240 min: 10/42/192 | al gemeten: 918
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 82 | 11 | 11 | 0 | 0 | 5.3 min |
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
| 09-15 12:00 | 9559 | 1252 | 1159 | 12 | 0 | 76.9 min |
| 09-15 18:00 | 11380 | 642 | 592 | 638 | 0 | 158.2 min |

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
