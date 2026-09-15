# Schaduwbot status

- tijd: 2026-09-15 04:19:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 14 hours, 32 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.8G/38G | geheugen: 2230/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 164714, "tokens_in_memory": 8326, "msgs": 25221754, "trades": 5021466, "creates": 53780, "decode_fail": 428597, "rpc_calls": 142829, "rpc_errors": 13, "sol_usd": 101.48619697568243, "open_positions": 55, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 03:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:13,673 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:54:13 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:54:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:41,333 main INFO screen Ape pass=0 dev=0.59 ins=35.9 pro=64 1a=False 1b=False 2=True (64.4s)
Sep 15 03:54:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:47,276 main INFO screen fomo pass=0 dev=0.0 ins=153.84 pro=0 1a=False 1b=False 2=True (57.9s)
Sep 15 03:54:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:54:50,809 main INFO screen Breadguy pass=0 dev=0.0 ins=29.28 pro=53 1a=False 1b=False 2=True (63.8s)
Sep 15 03:55:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:51,494 main INFO screen COTE pass=0 dev=0.87 ins=233.52 pro=1 1a=False 1b=False 2=True (64.2s)
Sep 15 03:55:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:52,006 main INFO screen DANCE pass=0 dev=0.6 ins=0.0 pro=7 1a=False 1b=False 2=False (70.7s)
Sep 15 03:55:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:55:54,538 main INFO screen Snoop Doge pass=0 dev=0.07 ins=0.0 pro=5 1a=False 1b=False 2=False (63.7s)
Sep 15 03:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:26,781 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:26 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,857 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "POST /mcp HTTP/1.1" 404 174 "-" "python-httpx/0.28.1"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,883 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "GET /sse HTTP/1.1" 404 174 "-" "python-httpx/0.28.1"
Sep 15 03:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:56:48,947 aiohttp.access INFO 45.156.128.66 [15/Sep/2026:03:56:48 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 03:57:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:08,277 main INFO screen Lanaroads pass=0 dev=0.0 ins=5.72 pro=55 1a=False 1b=False 2=False (76.8s)
Sep 15 03:57:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:11,481 main INFO screen bag pass=0 dev=0.0 ins=29.44 pro=75 1a=False 1b=False 2=True (79.5s)
Sep 15 03:57:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:57:11,726 main INFO screen MHRD pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=True (77.2s)
Sep 15 03:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:18,365 main INFO screen Cented pass=0 dev=0.0 ins=28.69 pro=11 1a=False 1b=False 2=True (66.9s)
Sep 15 03:58:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:19,261 main INFO screen RCHAT pass=0 dev=0.0 ins=12.09 pro=46 1a=False 1b=True 2=False (71.0s)
Sep 15 03:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:58:20,577 main INFO screen WIGGABUTT pass=0 dev=0.0 ins=0.0 pro=67 1a=False 1b=False 2=False (68.9s)
Sep 15 03:59:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:59:14,351 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:59:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:59:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:59:36,629 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (78.3s)
Sep 15 03:59:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:59:38,573 main INFO screen Cupsey pass=0 dev=0.0 ins=12.62 pro=68 1a=False 1b=False 2=True (79.3s)
Sep 15 03:59:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:59:40,424 main INFO screen CURRY pass=0 dev=0.0 ins=4.54 pro=40 1a=False 1b=False 2=False (79.8s)
Sep 15 04:00:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:00:38,515 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (61.9s)
Sep 15 04:00:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:00:51,602 main INFO screen testies pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (71.2s)
Sep 15 04:00:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:00:53,083 main INFO screen NAKAMOTO pass=0 dev=0.0 ins=17.17 pro=41 1a=False 1b=False 2=True (74.5s)
Sep 15 04:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:01:30,912 main INFO screen Spidey pass=0 dev=0.44 ins=0.0 pro=16 1a=False 1b=False 2=False (52.4s)
Sep 15 04:01:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:01:47,373 main INFO screen pump pass=0 dev=0.0 ins=4.52 pro=48 1a=False 1b=False 2=False (55.8s)
Sep 15 04:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:02:04,830 main INFO screen Mindless pass=0 dev=0.0 ins=0.07 pro=51 1a=False 1b=False 2=False (71.7s)
Sep 15 04:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:02:37,141 main INFO screen DJordan pass=0 dev=0.0 ins=19.64 pro=64 1a=False 1b=False 2=True (66.2s)
Sep 15 04:03:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:03:02,601 main INFO screen KIBA pass=0 dev=3.97 ins=116.61 pro=1 1a=False 1b=False 2=True (57.8s)
Sep 15 04:03:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:03:02,702 main INFO screen AbdiCenat pass=0 dev=0.0 ins=0.0 pro=53 1a=False 1b=False 2=False (75.3s)
Sep 15 04:03:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:03:34,881 main INFO screen GS pass=0 dev=0.0 ins=15.31 pro=15 1a=False 1b=False 2=True (57.7s)
Sep 15 04:03:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:03:56,385 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (53.8s)
Sep 15 04:04:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:04:06,105 main INFO screen Dior pass=0 dev=0.0 ins=13.68 pro=57 1a=False 1b=False 2=True (63.4s)
Sep 15 04:04:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:04:17,370 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:04:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:04:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:04:31,786 main INFO screen TSLA pass=0 dev=0.0 ins=19.88 pro=1 1a=False 1b=False 2=True (56.9s)
Sep 15 04:05:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:05:05,672 main INFO screen GME pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (69.3s)
Sep 15 04:05:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:05:18,694 main INFO screen Mandarin A pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (72.6s)
Sep 15 04:05:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:05:39,305 main INFO screen Mdudass pass=0 dev=0.0 ins=8.13 pro=46 1a=False 1b=False 2=False (67.5s)
Sep 15 04:06:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:06:05,011 main INFO screen BONX pass=0 dev=0.95 ins=0.0 pro=12 1a=False 1b=False 2=False (59.3s)
Sep 15 04:06:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:06:17,201 main INFO screen TripleX pass=0 dev=0.0 ins=22.26 pro=45 1a=False 1b=False 2=True (58.5s)
Sep 15 04:06:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:06:35,358 main INFO screen SOL Meme pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (56.1s)
Sep 15 04:07:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:07:14,732 main INFO screen VPN pass=0 dev=0.0 ins=18.67 pro=16 1a=False 1b=False 2=True (69.7s)
Sep 15 04:07:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:07:24,727 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (67.5s)
Sep 15 04:07:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:07:29,920 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.6s)
Sep 15 04:08:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:08:15,155 main INFO screen weave pass=0 dev=0.0 ins=23.36 pro=62 1a=False 1b=False 2=True (60.4s)
Sep 15 04:08:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:08:41,742 main INFO screen Sink pass=0 dev=0.0 ins=14.32 pro=60 1a=False 1b=False 2=True (77.0s)
Sep 15 04:08:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:08:45,211 main INFO screen KIMCHI pass=0 dev=0.0 ins=9.55 pro=71 1a=False 1b=False 2=True (75.3s)
Sep 15 04:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:09:17,603 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:09:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:09:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:09:21,873 main INFO screen $CATINBOX pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (66.7s)
Sep 15 04:09:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:09:40,384 main INFO screen grow pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=True (58.6s)
Sep 15 04:09:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:09:51,814 main INFO screen OPTIONS pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.6s)
Sep 15 04:10:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:10:18,661 main INFO screen MIKEANSON pass=0 dev=0.0 ins=32.42 pro=26 1a=False 1b=False 2=True (56.8s)
Sep 15 04:10:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:10:35,571 main INFO screen Snoop Doge pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (55.2s)
Sep 15 04:10:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:10:42,630 main INFO screen SURVIVE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.8s)
Sep 15 04:11:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:11:12,024 main INFO screen Microsoft pass=0 dev=0.0 ins=176.66 pro=0 1a=False 1b=False 2=True (53.4s)
Sep 15 04:11:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:11:24,908 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.3s)
Sep 15 04:11:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:11:52,502 main INFO screen HILL pass=0 dev=3.06 ins=8.04 pro=48 1a=False 1b=False 2=True (69.9s)
Sep 15 04:12:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:12:17,824 main INFO screen WOLF pass=0 dev=0.0 ins=26.25 pro=62 1a=False 1b=False 2=True (65.8s)
Sep 15 04:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:12:20,579 main INFO screen MIKEANSON pass=0 dev=0.0 ins=31.3 pro=19 1a=False 1b=False 2=True (55.7s)
Sep 15 04:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:12:46,722 main INFO screen SNOOT pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 15 04:13:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:13:28,839 main INFO screen SWIFT pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (71.0s)
Sep 15 04:13:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:13:30,529 main INFO screen MIKEANSON pass=0 dev=0.0 ins=32.54 pro=28 1a=False 1b=False 2=True (69.9s)
Sep 15 04:13:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:13:44,065 main INFO screen BOLT pass=0 dev=0.0 ins=23.32 pro=42 1a=False 1b=False 2=True (57.3s)
Sep 15 04:14:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:14:20,635 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:14:20 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:14:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:14:36,916 main INFO screen MagicJohnson pass=0 dev=0.0 ins=6.68 pro=65 1a=False 1b=False 2=True (68.1s)
Sep 15 04:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:14:37,967 main INFO screen FTFS pass=0 dev=41.2 ins=0.0 pro=3 1a=False 1b=False 2=True (67.4s)
Sep 15 04:14:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:14:41,240 main INFO screen PROFITABLE pass=0 dev=0.0 ins=18.06 pro=47 1a=False 1b=False 2=True (57.2s)
Sep 15 04:15:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:42,832 main INFO screen MIKEANSON pass=0 dev=0.0 ins=32.09 pro=48 1a=False 1b=False 2=True (65.9s)
Sep 15 04:15:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:44,900 main INFO screen QUANT pass=0 dev=0.0 ins=19.21 pro=17 1a=False 1b=False 2=True (66.9s)
Sep 15 04:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:47,248 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.0s)
Sep 15 04:16:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:47,225 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (62.3s)
Sep 15 04:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:53,767 main INFO screen KIMCHI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.5s)
Sep 15 04:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:54,630 main INFO screen HILL pass=0 dev=0.0 ins=4.38 pro=36 1a=False 1b=False 2=False (71.8s)
Sep 15 04:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:17:38,590 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.4s)
Sep 15 04:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:00,892 main INFO screen RAIN pass=0 dev=0.0 ins=19.31 pro=55 1a=False 1b=False 2=True (66.3s)
Sep 15 04:18:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:05,285 main INFO screen MIKEANSON pass=0 dev=0.0 ins=31.77 pro=43 1a=False 1b=False 2=True (71.5s)
Sep 15 04:18:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:38,831 main INFO screen JIGG pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.2s)
Sep 15 04:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:56,681 main INFO screen SOLANA pass=0 dev=0.0 ins=10.33 pro=31 1a=False 1b=False 2=True (51.4s)
Sep 15 04:18:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:57,379 main INFO screen battwine pass=0 dev=0.0 ins=78.05 pro=18 1a=False 1b=True 2=True (56.5s)
Sep 15 04:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:19:22,028 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:19:22 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T02:53:20Z
--- update 2026-09-15T02:58:21Z
--- update 2026-09-15T03:03:23Z
--- update 2026-09-15T03:08:36Z
--- update 2026-09-15T03:13:43Z
--- update 2026-09-15T03:18:46Z
--- update 2026-09-15T03:23:46Z
--- update 2026-09-15T03:29:04Z
--- update 2026-09-15T03:34:05Z
--- update 2026-09-15T03:39:07Z
--- update 2026-09-15T03:44:09Z
--- update 2026-09-15T03:49:12Z
--- update 2026-09-15T03:54:12Z
Running as unit: schaduwbot-wallets.service; invocation ID: c556852febb7497c926f7c233c44f1d1
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T03:59:12Z
--- update 2026-09-15T04:04:15Z
--- update 2026-09-15T04:09:16Z
--- update 2026-09-15T04:14:19Z
--- update 2026-09-15T04:19:20Z
```

## Analyses (laatste 25 regels)
```
active
02:38:55   64000 tokens, 6127099 trades, 744134 posities (451s)
02:39:11   66000 tokens, 6324136 trades, 768998 posities (467s)
02:39:27   68000 tokens, 6521044 trades, 794258 posities (483s)
02:39:43   70000 tokens, 6709770 trades, 817423 posities (499s)
02:39:58   72000 tokens, 6901181 trades, 840177 posities (514s)
02:40:16   74000 tokens, 7111581 trades, 876955 posities (532s)
02:40:26 posities: 888948 uit 7226958 trades (548s)
02:40:38 209899 wallets gerekend
02:40:39 geluk-toets
02:41:13 persistentie
02:41:16 kopieer-simulatie
02:43:47 klaar in 749s -> /opt/schaduwbot/reports/wallets.md
03:54:13 101653 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
03:54:38   ingelezen tot rowid 10515765 (200000 rijen, 200000 bruikbaar)
03:54:40   ingelezen tot rowid 10534037 (218272 rijen, 218272 bruikbaar)
03:54:42 ingelezen: 218272 nieuwe trades, 218272 bruikbaar (29s)
03:57:47 3000 aankopen van gevolgde wallets geëvalueerd
03:58:20 vroege kopers: 278 voldoen nu, register 491, 311 tokens beoordeeld
03:58:55 grote spelers: saldo van 490 wallets opgehaald
03:59:42 herkomst: 40 posities gekoppeld
03:59:55 klaar in 342s -> /opt/schaduwbot/reports/ledger.md
04:14:44 S1: gezakt — toets n=30298, verkennend n=14656
04:14:44 klaar in 888s -> /opt/schaduwbot/reports/hypotheses.md
04:14:44 probe: 150 transacties ophalen
04:18:09 poolveld: 16 pools bekeken, 0 te gaan -> vastgesteld @43
```

## IJking poolkoers (laatste 12 regels)
```
03:29:10 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=118 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:29:10 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 9/38/154 | al gemeten: 436
03:34:11 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=120 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:34:11 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 7/37/155 | al gemeten: 438
03:39:20 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=124 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:39:20 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 8/37/155 | al gemeten: 442
03:44:15 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=126 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:44:15 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 8/36/155 | al gemeten: 444
03:49:22 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=129 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:49:22 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 10/37/155 | al gemeten: 447
03:54:48 ijk: +6 van 6 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=133 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:54:52 ijk-diagnose: nieuwste migratie -0.3 min oud | migraties 15/60/240 min: 13/42/159 | al gemeten: 453
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
