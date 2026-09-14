# Schaduwbot status

- tijd: 2026-09-14 08:31:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 18 hours, 44 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.5G/38G | geheugen: 1908/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 93420, "tokens_in_memory": 4729, "msgs": 11657320, "trades": 2520476, "creates": 26111, "decode_fail": 213887, "rpc_calls": 74495, "rpc_errors": 6, "sol_usd": 101.387317041593, "open_positions": 45, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]:   Pause on PRI/Upgrade:
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]:     b'\x00\x00\x18\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x04\x00\x00Bh\x00\x06\x00\x04\x00\x00\x00\x03\x00\x00\x00\n'
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]:       ^
Sep 14 07:52:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:52:01,131 aiohttp.access INFO 66.132.195.104 [14/Sep/2026:07:52:01 +0000] "UNKNOWN / HTTP/1.0" 400 321 "-" "-"
Sep 14 07:52:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:52:12,898 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 14 07:52:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:52:20,076 aiohttp.access INFO 66.132.195.104 [14/Sep/2026:07:52:20 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 07:52:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:52:20,329 aiohttp.access INFO 66.132.195.104 [14/Sep/2026:07:52:20 +0000] "GET /ads.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)"
Sep 14 07:53:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:53:50,776 main INFO screen Spurdo pass=0 dev=0.0 ins=15.27 pro=51 1a=False 1b=False 2=True (51.8s)
Sep 14 07:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:54:37,429 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:54:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:55:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:55:28,230 main INFO screen BPCATE pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (63.9s)
Sep 14 07:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:56:26,759 main INFO screen PSA pass=1 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (66.6s)
Sep 14 07:56:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:56:46,665 main INFO screen OTC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.0s)
Sep 14 07:57:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:57:59,215 main INFO screen Heist pass=0 dev=0.0 ins=20.37 pro=66 1a=False 1b=False 2=True (69.1s)
Sep 14 07:58:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:58:00,807 main INFO screen CHADSTER pass=1 dev=0.24 ins=0.0 pro=10 1a=False 1b=False 2=False (68.7s)
Sep 14 07:58:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:58:38,838 main INFO screen SOL pass=0 dev=0.0 ins=33.73 pro=47 1a=False 1b=False 2=True (72.4s)
Sep 14 07:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:58:54,114 main INFO screen TST pass=0 dev=0.0 ins=0.0 pro=21 1a=True 1b=False 2=False (54.9s)
Sep 14 07:59:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:59:07,191 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.7s)
Sep 14 07:59:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:59:46,423 main INFO screen mimi pass=1 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (67.6s)
Sep 14 07:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:59:59,800 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:59:59 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 08:00:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:00:08,862 main INFO screen World Wate pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.4s)
Sep 14 08:01:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:01:23,949 main INFO screen RHAWK pass=0 dev=0.06 ins=79.26 pro=8 1a=False 1b=True 2=True (53.0s)
Sep 14 08:02:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:02:38,979 main INFO screen tosho pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.5s)
Sep 14 08:03:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:03:11,402 main INFO screen WOFI pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (73.4s)
Sep 14 08:03:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:03:31,276 main INFO screen DRPEPPER pass=0 dev=0.25 ins=0.0 pro=9 1a=False 1b=False 2=False (69.6s)
Sep 14 08:04:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:04:12,201 main INFO screen Heist pass=1 dev=0.0 ins=9.74 pro=63 1a=False 1b=False 2=False (66.1s)
Sep 14 08:04:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:04:18,091 aiohttp.access INFO 130.12.180.89 [14/Sep/2026:08:04:18 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 14 08:05:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:05:15,259 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:05:15 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:05:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:05:44,290 main INFO screen copium pass=0 dev=0.0 ins=16.44 pro=59 1a=False 1b=False 2=True (64.3s)
Sep 14 08:07:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:07:24,507 main INFO screen 奶龙 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 14 08:07:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:07:34,232 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (54.8s)
Sep 14 08:10:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:10:31,590 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:10:31 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:11:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:11:36,594 main INFO screen $CVD pass=1 dev=0.41 ins=0.0 pro=10 1a=False 1b=False 2=False (70.5s)
Sep 14 08:11:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:11:42,420 main INFO screen Og pass=1 dev=3.43 ins=13.9 pro=35 1a=False 1b=False 2=False (69.0s)
Sep 14 08:11:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:11:47,992 main INFO screen LOGE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.3s)
Sep 14 08:12:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:12:45,709 main INFO screen ZABUBU pass=0 dev=0.0 ins=19.34 pro=45 1a=False 1b=False 2=True (69.1s)
Sep 14 08:14:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:14:13,935 main INFO screen tobby pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (55.4s)
Sep 14 08:14:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:14:32,143 main INFO screen INU pass=1 dev=0.0 ins=9.43 pro=55 1a=False 1b=False 2=False (68.7s)
Sep 14 08:14:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:14:42,330 main INFO screen TEST pass=1 dev=0.0 ins=0.0 pro=93 1a=False 1b=False 2=False (71.3s)
Sep 14 08:15:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:15:29,155 main INFO screen $STONK pass=0 dev=0.35 ins=0.0 pro=7 1a=False 1b=False 2=False (75.2s)
Sep 14 08:15:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:15:32,384 main INFO screen King pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.2s)
Sep 14 08:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:15:37,546 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:15:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:15:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:15:50,024 main INFO screen STONK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.9s)
Sep 14 08:16:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:16:39,367 main INFO screen werld pass=0 dev=0.0 ins=18.01 pro=39 1a=False 1b=False 2=True (54.7s)
Sep 14 08:17:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:17:09,655 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.3s)
Sep 14 08:17:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:17:12,605 main INFO screen $STONK pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (76.3s)
Sep 14 08:17:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:17:48,351 main INFO screen Lab pass=0 dev=0.0 ins=21.47 pro=26 1a=False 1b=False 2=True (69.0s)
Sep 14 08:18:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:18:33,814 main INFO screen tk  pass=0 dev=0.93 ins=0.0 pro=3 1a=False 1b=False 2=True (74.6s)
Sep 14 08:18:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:18:40,233 main INFO screen danlarson pass=0 dev=0.0 ins=1.62 pro=5 1a=False 1b=False 2=False (67.0s)
Sep 14 08:18:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:18:57,690 main INFO screen CAD pass=0 dev=0.0 ins=18.77 pro=53 1a=False 1b=False 2=True (63.7s)
Sep 14 08:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:19:30,830 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.0s)
Sep 14 08:19:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:19:49,853 main INFO screen BeachBull pass=0 dev=1.74 ins=55.58 pro=43 1a=False 1b=False 2=True (69.6s)
Sep 14 08:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:19:55,222 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.5s)
Sep 14 08:20:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:20:37,702 main INFO screen Lobster pass=0 dev=0.0 ins=30.76 pro=80 1a=False 1b=False 2=True (66.9s)
Sep 14 08:20:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:20:47,030 main INFO screen PSNAKE pass=0 dev=0.06 ins=79.26 pro=8 1a=False 1b=True 2=True (57.2s)
Sep 14 08:20:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:20:48,498 main INFO screen danlarson pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (53.3s)
Sep 14 08:21:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:02,202 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:08:21:02 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 08:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:29,424 aiohttp.access INFO 45.135.193.198 [14/Sep/2026:08:21:29 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 08:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:29,457 aiohttp.access INFO 45.135.193.198 [14/Sep/2026:08:21:29 +0000] "GET / HTTP/1.0" 404 174 "-" "0day"
Sep 14 08:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:34,435 main INFO screen Rolex pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 14 08:21:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:44,398 main INFO screen danlarson pass=0 dev=0.0 ins=0.82 pro=6 1a=False 1b=False 2=False (57.4s)
Sep 14 08:21:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:21:58,235 main INFO screen PVE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (69.7s)
Sep 14 08:22:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:22:29,457 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.0s)
Sep 14 08:22:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 08:22:39,583 main INFO screen CASHCAT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T07:01:08Z
--- update 2026-09-14T07:06:23Z
--- update 2026-09-14T07:11:29Z
--- update 2026-09-14T07:16:36Z
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
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
08:05:14 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:10:35 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:15:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:21:04 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:26:05 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
08:31:08 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
