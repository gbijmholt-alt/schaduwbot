# Schaduwbot status

- tijd: 2026-09-13 06:03:09 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 16 hours, 16 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.2G/38G | geheugen: 1420/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 34161, "tokens_in_memory": 5992, "msgs": 3390326, "trades": 999127, "creates": 10920, "decode_fail": 107830, "rpc_calls": 27022, "rpc_errors": 6, "sol_usd": 101.78112662641158, "open_positions": 44, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 05:21:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:21:19,606 main INFO screen 6AM pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (79.5s)
Sep 13 05:21:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:21:59,604 main INFO screen UBERLYN pass=0 dev=4.82 ins=0.0 pro=6 1a=False 1b=False 2=False (79.9s)
Sep 13 05:22:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:22:17,560 main INFO screen FWHALES pass=1 dev=1.4 ins=0.0 pro=14 1a=False 1b=False 2=False (81.4s)
Sep 13 05:22:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:22:43,844 main INFO screen RCHUMP pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (71.8s)
Sep 13 05:23:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:23:29,966 main INFO screen foff pass=0 dev=0.11 ins=0.0 pro=8 1a=False 1b=False 2=False (81.7s)
Sep 13 05:23:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:23:33,635 main INFO screen FTFS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 13 05:24:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:24:05,108 main INFO screen 6AM pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (78.4s)
Sep 13 05:26:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:26:05,831 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:26:05 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:29:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:29:09,610 main INFO screen BAITW pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.7s)
Sep 13 05:31:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:31:19,102 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.7s)
Sep 13 05:31:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:31:37,067 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:31:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:33:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:33:07,105 main INFO screen donni pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.7s)
Sep 13 05:35:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:35:08,428 main INFO screen nrnr pass=0 dev=0.07 ins=79.24 pro=9 1a=False 1b=True 2=True (102.3s)
Sep 13 05:35:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:35:11,699 main INFO screen HASHCAT pass=0 dev=0.36 ins=0.0 pro=1 1a=False 1b=False 2=False (110.4s)
Sep 13 05:35:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:35:37,468 aiohttp.access INFO 18.218.118.203 [13/Sep/2026:05:35:37 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 13 05:36:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:36:15,569 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 13 05:36:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:36:19,600 aiohttp.access INFO 18.218.118.203 [13/Sep/2026:05:36:19 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 13 05:36:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:36:29,335 main INFO screen ACTGPT pass=0 dev=0.18 ins=77.58 pro=8 1a=False 1b=True 2=True (61.8s)
Sep 13 05:36:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:36:56,801 main INFO screen MonkeyGPT pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (53.4s)
Sep 13 05:36:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:36:58,003 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:36:58 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:37:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:37:36,100 main INFO screen USWS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.9s)
Sep 13 05:37:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:37:42,162 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (53.5s)
Sep 13 05:37:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:37:56,275 aiohttp.access INFO 18.218.118.203 [13/Sep/2026:05:37:56 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 05:38:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:38:34,524 main INFO screen Crook pass=1 dev=0.0 ins=2.55 pro=37 1a=False 1b=False 2=False (53.9s)
Sep 13 05:40:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:40:27,008 aiohttp.access INFO 18.218.118.203 [13/Sep/2026:05:40:27 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 05:41:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:41:09,836 main INFO screen Amazon pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.1s)
Sep 13 05:41:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:41:26,417 main INFO screen SSD pass=0 dev=0.0 ins=17.66 pro=70 1a=False 1b=False 2=True (75.3s)
Sep 13 05:41:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:41:43,061 main INFO screen baton pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.5s)
Sep 13 05:42:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:42:11,646 main INFO screen CUCK pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 13 05:42:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:42:12,816 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:42:12 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:42:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:42:26,786 main INFO screen MICHAEL pass=1 dev=1.86 ins=0.0 pro=30 1a=False 1b=False 2=False (60.4s)
Sep 13 05:42:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:42:44,009 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.8s)
Sep 13 05:45:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:45:14,138 main INFO screen DOOB pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (62.3s)
Sep 13 05:45:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:45:19,090 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (49.3s)
Sep 13 05:46:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:46:53,596 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.2s)
Sep 13 05:47:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:47:37,094 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:47:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:47:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:47:43,804 main INFO screen MORON pass=0 dev=1.24 ins=27.72 pro=59 1a=False 1b=False 2=True (67.9s)
Sep 13 05:47:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:47:51,908 main INFO screen ALLSTATE pass=0 dev=0.01 ins=0.0 pro=5 1a=False 1b=False 2=False (70.2s)
Sep 13 05:47:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:47:58,749 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (65.2s)
Sep 13 05:48:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:48:45,277 main INFO screen TRUMPBATON pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (50.5s)
Sep 13 05:49:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:49:42,771 main INFO screen foff pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 13 05:50:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:50:53,310 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.6s)
Sep 13 05:50:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:50:58,125 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (70.4s)
Sep 13 05:51:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:51:23,357 main INFO screen ALLSTATE pass=0 dev=0.03 ins=0.0 pro=7 1a=False 1b=False 2=False (54.3s)
Sep 13 05:51:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:51:47,085 main INFO screen ROBINCAT pass=0 dev=0.07 ins=77.39 pro=7 1a=False 1b=True 2=True (53.8s)
Sep 13 05:51:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:51:55,514 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.4s)
Sep 13 05:52:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:52:35,375 main INFO screen CILLPP pass=0 dev=0.0 ins=0.21 pro=5 1a=False 1b=False 2=False (72.0s)
Sep 13 05:52:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:52:50,948 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:52:50 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:53:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:53:14,922 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (73.5s)
Sep 13 05:53:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:53:19,914 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.2s)
Sep 13 05:53:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:53:30,651 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.3s)
Sep 13 05:54:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:54:10,493 main INFO screen BULLHOUSE pass=0 dev=0.07 ins=79.19 pro=6 1a=False 1b=True 2=True (55.6s)
Sep 13 05:54:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:54:25,803 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.2s)
Sep 13 05:55:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:55:09,097 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 13 05:55:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:55:32,528 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.4s)
Sep 13 05:55:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:55:54,523 main INFO screen CryptoKitties pass=0 dev=0.0 ins=16.69 pro=81 1a=False 1b=False 2=True (69.2s)
Sep 13 05:56:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:56:20,103 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.8s)
Sep 13 05:56:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:56:32,255 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.7s)
Sep 13 05:56:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:56:51,736 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (57.2s)
Sep 13 05:57:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:57:19,888 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.8s)
Sep 13 05:57:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:57:34,214 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.0s)
Sep 13 05:57:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:57:49,781 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 13 05:57:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:57:56,848 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:05:57:56 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 05:58:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:58:22,531 main INFO screen foff pass=0 dev=0.09 ins=0.0 pro=5 1a=False 1b=False 2=False (62.6s)
Sep 13 05:58:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:58:44,052 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.8s)
Sep 13 05:58:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:58:49,879 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.1s)
Sep 13 05:59:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:59:24,686 main INFO screen $richpump pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 13 05:59:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 05:59:47,601 main INFO screen TRUCE pass=0 dev=0.0 ins=27.46 pro=42 1a=False 1b=False 2=True (63.5s)
Sep 13 06:00:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:00:00,131 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.3s)
Sep 13 06:00:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:00:45,331 main INFO screen BBP pass=0 dev=0.04 ins=0.0 pro=6 1a=False 1b=False 2=False (80.6s)
Sep 13 06:00:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:00:58,733 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.1s)
Sep 13 06:01:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:01:08,016 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 13 06:01:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:01:42,778 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.4s)
Sep 13 06:02:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:02:03,905 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.2s)
Sep 13 06:02:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:02:05,861 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.8s)
Sep 13 06:02:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:02:13,654 aiohttp.access INFO 144.91.106.106 [13/Sep/2026:06:02:13 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0"
Sep 13 06:02:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:02:34,342 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (51.6s)
Sep 13 06:03:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:03:01,477 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.6s)
Sep 13 06:03:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:03:07,720 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.9s)
Sep 13 06:03:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:03:09,112 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:03:09 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T04:33:47Z
--- update 2026-09-13T04:38:57Z
--- update 2026-09-13T04:44:07Z
--- update 2026-09-13T04:49:21Z
--- update 2026-09-13T04:54:26Z
--- update 2026-09-13T04:59:36Z
--- update 2026-09-13T05:05:01Z
--- update 2026-09-13T05:10:36Z
--- update 2026-09-13T05:15:41Z
--- update 2026-09-13T05:20:52Z
--- update 2026-09-13T05:26:04Z
--- update 2026-09-13T05:31:36Z
--- update 2026-09-13T05:36:56Z
Running as unit: schaduwbot-wallets.service; invocation ID: 8bfe45551dd4468d8f62fa306c9c7338
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T05:42:11Z
--- update 2026-09-13T05:47:36Z
--- update 2026-09-13T05:52:49Z
--- update 2026-09-13T05:57:55Z
--- update 2026-09-13T06:03:08Z
```

## Analyses (laatste 25 regels)
```
inactive
05:48:02   12000 tokens, 1336948 trades, 216744 posities (18s)
05:48:06   14000 tokens, 1560087 trades, 251036 posities (22s)
05:48:10   16000 tokens, 1788150 trades, 289575 posities (25s)
05:48:13   18000 tokens, 2040718 trades, 336928 posities (29s)
05:48:17   20000 tokens, 2271282 trades, 376490 posities (33s)
05:48:21   22000 tokens, 2482011 trades, 407061 posities (37s)
05:48:25   24000 tokens, 2703818 trades, 442089 posities (40s)
05:48:30   26000 tokens, 2938717 trades, 481962 posities (46s)
05:48:36   28000 tokens, 3156878 trades, 515239 posities (51s)
05:48:41   30000 tokens, 3394537 trades, 555510 posities (57s)
05:48:48   32000 tokens, 3627590 trades, 595731 posities (64s)
05:48:55   34000 tokens, 3848204 trades, 630517 posities (70s)
05:49:02   36000 tokens, 4062597 trades, 663700 posities (78s)
05:49:09   38000 tokens, 4302243 trades, 705695 posities (85s)
05:49:15   40000 tokens, 4501664 trades, 737577 posities (90s)
05:49:19   42000 tokens, 4725136 trades, 777320 posities (95s)
05:49:24   44000 tokens, 4962765 trades, 815814 posities (99s)
05:49:29   46000 tokens, 5209556 trades, 859079 posities (105s)
05:49:33   48000 tokens, 5418709 trades, 905742 posities (109s)
05:49:34 posities: 923066 uit 5497133 trades (110s)
05:49:46 193401 wallets gerekend
05:49:47 geluk-toets
05:50:19 persistentie
05:50:21 kopieer-simulatie
05:51:13 klaar in 208s -> /opt/schaduwbot/reports/wallets.md
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
