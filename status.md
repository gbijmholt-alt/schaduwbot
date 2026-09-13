# Schaduwbot status

- tijd: 2026-09-13 02:12:59 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 12 hours, 26 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.1G/38G | geheugen: 1350/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 20351, "tokens_in_memory": 7246, "msgs": 2256255, "trades": 661516, "creates": 7246, "decode_fail": 60668, "rpc_calls": 17577, "rpc_errors": 2, "sol_usd": 102.09178169956478, "open_positions": 10, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 1696 | 188 | 0 | 199 | 29 | 351 | 1070 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 600 | 16% | 1.7% | +43.5% | -15.9% | -6.10% | 100% |
| dip35_V1_gescreend_fail | 4682 | 27% | 3.9% | +45.2% | -26.0% | -6.77% | 100% |
| dip35_V1_alle | 6192 | 26% | 4.0% | +44.5% | -25.4% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 598 | 22% | 2.3% | +41.1% | -20.2% | -6.60% | 100% |
| dip35_V2_gescreend_fail | 4753 | 25% | 4.4% | +54.8% | -28.0% | -7.03% | 100% |
| dip35_V2_alle | 6149 | 25% | 4.5% | +52.3% | -27.7% | -7.99% | 100% |
| dip35_V3_gescreend_pass | 605 | 9% | 3.0% | +261.0% | -21.9% | +4.28% | 100% |
| dip35_V3_gescreend_fail | 4876 | 14% | 6.1% | +118.2% | -29.7% | -9.41% | 100% |
| dip35_V3_alle | 6207 | 13% | 6.1% | +117.3% | -29.3% | -9.99% | 100% |
| dip40_V1_gescreend_pass | 571 | 14% | 1.8% | +44.5% | -15.4% | -6.73% | 100% |
| dip40_V1_gescreend_fail | 4603 | 26% | 3.9% | +46.8% | -25.8% | -6.66% | 100% |
| dip40_V1_alle | 5952 | 26% | 3.9% | +46.5% | -25.2% | -6.89% | 100% |
| dip40_V2_gescreend_pass | 571 | 18% | 2.1% | +43.7% | -19.5% | -8.31% | 100% |
| dip40_V2_gescreend_fail | 4649 | 25% | 4.3% | +54.7% | -27.9% | -7.04% | 100% |
| dip40_V2_alle | 5902 | 24% | 4.5% | +53.0% | -27.6% | -8.05% | 100% |
| dip40_V3_gescreend_pass | 577 | 8% | 2.6% | +253.8% | -20.9% | +1.49% | 100% |
| dip40_V3_gescreend_fail | 4760 | 13% | 5.8% | +113.8% | -29.4% | -10.34% | 100% |
| dip40_V3_alle | 5962 | 13% | 5.9% | +113.0% | -29.1% | -10.90% | 100% |
| dip45_V1_gescreend_pass | 550 | 15% | 1.6% | +47.2% | -15.2% | -6.02% | 100% |
| dip45_V1_gescreend_fail | 4519 | 27% | 3.6% | +48.2% | -25.6% | -5.53% | 100% |
| dip45_V1_alle | 5755 | 26% | 3.6% | +48.3% | -25.0% | -5.93% | 100% |
| dip45_V2_gescreend_pass | 549 | 18% | 2.0% | +42.7% | -19.5% | -8.02% | 100% |
| dip45_V2_gescreend_fail | 4558 | 25% | 4.0% | +58.4% | -27.6% | -5.86% | 100% |
| dip45_V2_alle | 5706 | 24% | 4.2% | +56.9% | -27.3% | -6.85% | 100% |
| dip45_V3_gescreend_pass | 556 | 8% | 2.2% | +286.8% | -20.2% | +4.62% | 100% |
| dip45_V3_gescreend_fail | 4651 | 14% | 5.5% | +120.8% | -29.0% | -8.04% | 100% |
| dip45_V3_alle | 5754 | 13% | 5.5% | +122.9% | -28.6% | -8.70% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 473 | 16% | 5.1% | -8.20% | -11.4% tot -5.0% | -14.3% | – | 100% |
| per_token_zonder_xlink | 145 | 23% | 0.0% | +16.09% | -11.7% tot +43.9% | -13.1% | 132% | 58% |
| gepoold_met_xlink | 3962 | 13% | 2.8% | -9.38% | -10.6% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1215 | 18% | 0.0% | +15.87% | -0.2% tot +32.0% | -14.0% | 72% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 01:45:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:45:33,451 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.1s)
Sep 13 01:46:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:46:01,497 main INFO screen FLM pass=1 dev=0.0 ins=17.92 pro=44 1a=False 1b=False 2=False (66.7s)
Sep 13 01:46:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:46:11,549 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (48.4s)
Sep 13 01:47:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:47:00,983 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:47:00 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:47:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:47:25,806 main INFO screen $BOOBIES pass=0 dev=2.56 ins=0.0 pro=2 1a=False 1b=False 2=False (62.6s)
Sep 13 01:48:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:48:15,080 main INFO screen PumpRot pass=1 dev=0.0 ins=13.33 pro=37 1a=False 1b=False 2=False (52.9s)
Sep 13 01:48:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:48:29,584 main INFO screen Friendsai pass=0 dev=0.18 ins=79.13 pro=10 1a=False 1b=False 2=True (61.5s)
Sep 13 01:49:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:49:41,232 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.2s)
Sep 13 01:50:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:50:17,552 main INFO screen PUMPCHAN pass=0 dev=5.6 ins=72.68 pro=0 1a=False 1b=False 2=True (49.9s)
Sep 13 01:50:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:50:44,077 main INFO screen Buttplug pass=1 dev=0.57 ins=0.0 pro=35 1a=False 1b=False 2=False (69.0s)
Sep 13 01:50:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:50:46,048 main INFO screen $GOAT pass=1 dev=0.21 ins=0.0 pro=12 1a=False 1b=False 2=False (62.7s)
Sep 13 01:52:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:52:04,355 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:52:04 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:52:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:52:16,313 main INFO screen ROSHI pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (62.2s)
Sep 13 01:52:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:52:56,090 main INFO screen NOOT pass=1 dev=0.0 ins=11.45 pro=25 1a=False 1b=False 2=False (63.4s)
Sep 13 01:53:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:02,298 main INFO screen OpenPerps pass=0 dev=0.17 ins=48.52 pro=20 1a=False 1b=False 2=True (62.0s)
Sep 13 01:53:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:11,567 main INFO screen TIRED pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 13 01:53:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:19,830 aiohttp.access INFO 66.132.186.161 [13/Sep/2026:01:53:19 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 01:53:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:25,574 aiohttp.access INFO 66.132.186.161 [13/Sep/2026:01:53:25 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:33,075 aiohttp.server ERROR Error handling request from 66.132.186.161
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]: Traceback (most recent call last):
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:   File "/opt/schaduwbot/.venv/lib/python3.14/site-packages/aiohttp/web_protocol.py", line 433, in data_received
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:     messages, upgraded, tail = self._parser.feed_data(data)
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:   Pause on PRI/Upgrade:
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:     b'\x00\x00\x18\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x04\x00\x00Bh\x00\x06\x00\x04\x00\x00\x00\x03\x00\x00\x00\n'
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]:       ^
Sep 13 01:53:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:33,081 aiohttp.access INFO 66.132.186.161 [13/Sep/2026:01:53:33 +0000] "UNKNOWN / HTTP/1.0" 400 321 "-" "-"
Sep 13 01:53:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:47,150 main INFO screen PNC pass=0 dev=0.67 ins=0.0 pro=2 1a=False 1b=False 2=False (51.1s)
Sep 13 01:53:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:53:55,324 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.0s)
Sep 13 01:54:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:54:17,041 main INFO screen Normie pass=1 dev=0.0 ins=13.95 pro=70 1a=False 1b=False 2=False (65.5s)
Sep 13 01:54:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:54:40,644 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.5s)
Sep 13 01:54:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:54:44,902 aiohttp.access INFO 66.132.186.161 [13/Sep/2026:01:54:44 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 01:54:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:54:46,467 aiohttp.access INFO 66.132.186.161 [13/Sep/2026:01:54:46 +0000] "GET /sellers.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 13 01:54:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:54:47,590 main INFO screen GPTStunk pass=0 dev=0.39 ins=78.96 pro=6 1a=False 1b=True 2=True (52.3s)
Sep 13 01:55:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:55:07,782 main INFO screen OKBY pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (50.7s)
Sep 13 01:55:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:55:32,861 main INFO screen ROSHI pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 13 01:55:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:55:51,413 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.8s)
Sep 13 01:56:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:56:14,965 main INFO screen SOLCHAN pass=0 dev=0.0 ins=27.64 pro=53 1a=False 1b=False 2=True (67.2s)
Sep 13 01:56:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:56:23,632 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 13 01:56:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:56:46,369 main INFO screen BANKIN pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (55.0s)
Sep 13 01:57:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:57:13,934 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:57:13 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:57:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:57:23,000 main INFO screen $BSTC pass=0 dev=1.84 ins=0.0 pro=1 1a=False 1b=False 2=False (68.0s)
Sep 13 01:57:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:57:23,259 main INFO screen STONK10 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.6s)
Sep 13 01:57:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:57:40,352 main INFO screen STONK10 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.0s)
Sep 13 01:58:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:58:12,590 main INFO screen SFD pass=0 dev=79.3 ins=0.0 pro=1 1a=False 1b=False 2=True (49.6s)
Sep 13 01:58:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:58:16,549 main INFO screen STONK10 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.3s)
Sep 13 01:58:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:58:28,141 main INFO screen SAOF pass=0 dev=0.01 ins=125.37 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 13 01:59:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:59:02,330 main INFO screen STONK10 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.7s)
Sep 13 01:59:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:59:13,354 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.8s)
Sep 13 01:59:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:59:33,061 main INFO screen NI pass=0 dev=0.0 ins=8.9 pro=48 1a=False 1b=False 2=True (64.9s)
Sep 13 02:00:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:00:11,177 main INFO screen Emi pass=1 dev=0.0 ins=0.56 pro=69 1a=False 1b=False 2=False (68.8s)
Sep 13 02:00:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:00:22,008 main INFO screen DOGE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 13 02:00:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:00:25,742 main INFO screen SBN pass=0 dev=0.0 ins=24.98 pro=15 1a=False 1b=False 2=True (52.7s)
Sep 13 02:01:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:01:31,953 main INFO screen SCRVAN pass=0 dev=14.9 ins=0.0 pro=6 1a=False 1b=False 2=False (69.6s)
Sep 13 02:02:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:02:13,617 main INFO screen DOGE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 13 02:02:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:02:33,197 main INFO screen MOOOOMO pass=0 dev=0.34 ins=0.0 pro=4 1a=False 1b=False 2=False (63.6s)
Sep 13 02:02:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:02:37,086 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:02:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:03:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:03:16,202 main INFO screen NOOT pass=0 dev=0.0 ins=8.27 pro=68 1a=False 1b=False 2=True (64.5s)
Sep 13 02:04:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:04:03,656 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=True (55.7s)
Sep 13 02:04:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:04:40,213 main INFO screen GIGACAT pass=1 dev=0.0 ins=8.62 pro=61 1a=False 1b=False 2=False (72.0s)
Sep 13 02:05:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:09,333 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (63.9s)
Sep 13 02:05:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:09,886 main INFO screen GAW pass=0 dev=0.43 ins=0.0 pro=6 1a=False 1b=False 2=False (75.0s)
Sep 13 02:05:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:56,808 main INFO screen kittylick pass=0 dev=68.34 ins=0.0 pro=19 1a=False 1b=False 2=False (76.6s)
Sep 13 02:06:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:11,210 main INFO screen USFR pass=0 dev=0.01 ins=125.68 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 13 02:06:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:22,291 main INFO screen FTF pass=0 dev=0.02 ins=19.02 pro=74 1a=False 1b=False 2=True (73.0s)
Sep 13 02:06:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:59,029 main INFO screen CS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 13 02:07:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:23,679 main INFO screen MOWMOW pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 13 02:07:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:30,148 main INFO screen stomp pass=0 dev=0.18 ins=77.58 pro=8 1a=False 1b=True 2=True (66.7s)
Sep 13 02:07:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:46,375 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:07:46 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:08:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:08,352 main INFO screen BetOnBlak pass=1 dev=4.36 ins=0.0 pro=10 1a=False 1b=False 2=False (69.3s)
Sep 13 02:08:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:23,742 main INFO screen MOWMOW pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.1s)
Sep 13 02:08:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:36,318 main INFO screen $GOAT pass=0 dev=79.87 ins=0.0 pro=14 1a=False 1b=False 2=False (66.2s)
Sep 13 02:10:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:10:10,879 main INFO screen Stacy pass=0 dev=0.0 ins=19.43 pro=61 1a=False 1b=False 2=True (62.4s)
Sep 13 02:11:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:11:03,875 main INFO screen $AURA pass=0 dev=3.03 ins=0.0 pro=7 1a=False 1b=False 2=False (74.7s)
Sep 13 02:11:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:11:50,044 main INFO screen BetOnBlak pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (59.6s)
Sep 13 02:12:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:07,706 main INFO screen Him pass=0 dev=0.0 ins=5.14 pro=42 1a=False 1b=False 2=True (69.4s)
Sep 13 02:12:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:11,193 main INFO screen ROSHI pass=0 dev=0.0 ins=0.21 pro=6 1a=False 1b=False 2=False (64.8s)
Sep 13 02:12:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:59,406 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:12:59 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T00:43:31Z
--- update 2026-09-13T00:48:36Z
--- update 2026-09-13T00:53:44Z
--- update 2026-09-13T00:59:15Z
--- update 2026-09-13T01:04:36Z
--- update 2026-09-13T01:09:45Z
--- update 2026-09-13T01:14:49Z
--- update 2026-09-13T01:20:35Z
--- update 2026-09-13T01:25:36Z
--- update 2026-09-13T01:30:50Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1f41f3dc42b0489e96e2321b9527b30f
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T01:36:30Z
--- update 2026-09-13T01:41:36Z
--- update 2026-09-13T01:47:00Z
--- update 2026-09-13T01:52:03Z
--- update 2026-09-13T01:57:12Z
--- update 2026-09-13T02:02:36Z
--- update 2026-09-13T02:07:45Z
--- update 2026-09-13T02:12:58Z
```

## Analyses (laatste 25 regels)
```
inactive
01:38:38   8000 tokens, 896463 trades, 154963 posities (7s)
01:38:39   10000 tokens, 1118644 trades, 190444 posities (8s)
01:38:41   12000 tokens, 1338288 trades, 228593 posities (10s)
01:38:43   14000 tokens, 1559070 trades, 261143 posities (12s)
01:38:45   16000 tokens, 1815116 trades, 309221 posities (14s)
01:38:47   18000 tokens, 2054344 trades, 353904 posities (16s)
01:38:49   20000 tokens, 2273316 trades, 387540 posities (17s)
01:38:51   22000 tokens, 2497395 trades, 423098 posities (19s)
01:38:53   24000 tokens, 2734666 trades, 464849 posities (22s)
01:38:55   26000 tokens, 2948676 trades, 499259 posities (24s)
01:38:57   28000 tokens, 3193751 trades, 544763 posities (26s)
01:38:59   30000 tokens, 3417064 trades, 581170 posities (28s)
01:39:02   32000 tokens, 3645058 trades, 619865 posities (31s)
01:39:05   34000 tokens, 3861173 trades, 655601 posities (33s)
01:39:07   36000 tokens, 4091321 trades, 695494 posities (36s)
01:39:10   38000 tokens, 4311336 trades, 733577 posities (39s)
01:39:13   40000 tokens, 4549726 trades, 777004 posities (42s)
01:39:16   42000 tokens, 4787461 trades, 819867 posities (45s)
01:39:19   44000 tokens, 5019931 trades, 871749 posities (48s)
01:39:21 posities: 893712 uit 5124941 trades (50s)
01:39:30 187794 wallets gerekend
01:39:31 geluk-toets
01:40:02 persistentie
01:40:04 kopieer-simulatie
01:40:38 klaar in 127s -> /opt/schaduwbot/reports/wallets.md
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
