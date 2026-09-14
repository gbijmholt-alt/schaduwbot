# Schaduwbot status

- tijd: 2026-09-14 00:36:12 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 10 hours, 49 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.2G/38G | geheugen: 1906/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 64925, "tokens_in_memory": 7941, "msgs": 8331349, "trades": 1790430, "creates": 19118, "decode_fail": 160541, "rpc_calls": 52410, "rpc_errors": 3, "sol_usd": 99.49055393831661, "open_positions": 14, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 00:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:09:44,267 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 14 00:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:16,587 main INFO screen HvS pass=0 dev=0.0 ins=0.54 pro=1 1a=False 1b=False 2=False (76.0s)
Sep 14 00:10:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:20,970 main INFO screen PIG pass=0 dev=0.0 ins=43.21 pro=71 1a=False 1b=False 2=True (76.6s)
Sep 14 00:10:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:23,976 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:10:23 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:10:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:46,971 main INFO screen SpotifyFN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.7s)
Sep 14 00:11:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:11:17,650 main INFO screen CUCK pass=0 dev=0.06 ins=0.0 pro=3 1a=False 1b=False 2=False (61.1s)
Sep 14 00:11:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:11:30,304 main INFO screen DIHVIDENDS pass=1 dev=0.0 ins=18.14 pro=53 1a=False 1b=False 2=False (69.3s)
Sep 14 00:11:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:11:44,573 main INFO screen bullcat pass=0 dev=0.0 ins=12.97 pro=62 1a=False 1b=False 2=True (57.6s)
Sep 14 00:12:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:12:11,776 main INFO screen COIN pass=0 dev=0.0 ins=20.79 pro=76 1a=False 1b=False 2=True (54.1s)
Sep 14 00:12:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:12:23,960 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 14 00:12:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:12:39,774 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.2s)
Sep 14 00:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:13:07,107 main INFO screen MARIO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 14 00:13:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:13:24,169 aiohttp.access INFO 121.200.216.4 [14/Sep/2026:00:13:24 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 00:13:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:13:29,721 main INFO screen ANT pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (65.8s)
Sep 14 00:13:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:13:42,697 main INFO screen CTR pass=0 dev=0.0 ins=18.49 pro=58 1a=False 1b=False 2=True (62.9s)
Sep 14 00:14:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:14:04,992 main INFO screen STOCKP2 pass=0 dev=5.12 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 14 00:14:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:14:26,610 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.9s)
Sep 14 00:14:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:14:50,515 main INFO screen Nap pass=1 dev=0.0 ins=1.04 pro=75 1a=False 1b=False 2=False (67.8s)
Sep 14 00:15:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:15:10,830 main INFO screen CTR pass=1 dev=0.0 ins=12.62 pro=59 1a=False 1b=False 2=False (65.8s)
Sep 14 00:15:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:15:24,290 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:15:24 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 14 00:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:15:35,037 main INFO screen CTR pass=0 dev=0.0 ins=3.12 pro=79 1a=False 1b=False 2=True (68.4s)
Sep 14 00:16:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:16:04,442 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (73.9s)
Sep 14 00:16:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:16:09,829 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 14 00:16:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:16:47,805 main INFO screen Trygrok pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.8s)
Sep 14 00:17:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:17:02,099 main INFO screen PTWINE pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (57.7s)
Sep 14 00:17:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:17:17,794 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (68.0s)
Sep 14 00:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:17:34,504 aiohttp.access INFO 179.43.134.114 [14/Sep/2026:00:17:34 +0000] "CONNECT  HTTP/1.1" 404 193 "-" "-"
Sep 14 00:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:17:34,555 aiohttp.access INFO 179.43.134.114 [14/Sep/2026:00:17:34 +0000] "CONNECT  HTTP/1.1" 404 193 "-" "-"
Sep 14 00:18:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:18:06,321 main INFO screen UPTOOMUCH pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (78.5s)
Sep 14 00:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:18:19,197 main INFO screen 狗狗币 pass=0 dev=0.0 ins=28.2 pro=72 1a=False 1b=False 2=True (77.1s)
Sep 14 00:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:18:23,861 main INFO screen SAVPIR pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (66.1s)
Sep 14 00:19:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:19:03,737 main INFO screen SelfDRiv pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 14 00:19:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:19:28,460 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.3s)
Sep 14 00:19:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:19:29,928 main INFO screen d/acc pass=0 dev=77.25 ins=0.0 pro=1 1a=False 1b=False 2=True (66.1s)
Sep 14 00:20:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:20:04,273 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 14 00:20:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:20:32,379 main INFO screen JANE pass=0 dev=0.0 ins=12.56 pro=74 1a=False 1b=False 2=True (63.9s)
Sep 14 00:20:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:20:35,473 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:20:35 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:20:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:20:39,211 main INFO screen DONGHORN pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 14 00:21:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:06,499 main INFO screen CUCK pass=0 dev=0.0 ins=0.04 pro=3 1a=False 1b=False 2=False (62.2s)
Sep 14 00:21:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:39,580 main INFO screen HOBL pass=0 dev=0.0 ins=23.9 pro=72 1a=False 1b=False 2=True (67.2s)
Sep 14 00:21:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:21:46,561 main INFO screen TWINE pass=0 dev=0.41 ins=0.0 pro=5 1a=False 1b=False 2=True (67.3s)
Sep 14 00:22:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:19,692 main INFO screen WhiteBull pass=0 dev=0.0 ins=55.63 pro=39 1a=False 1b=False 2=True (73.2s)
Sep 14 00:22:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:51,050 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.5s)
Sep 14 00:22:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:22:54,311 main INFO screen JANE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.7s)
Sep 14 00:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:33,604 main INFO screen Dexter pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.9s)
Sep 14 00:23:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:49,922 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 00:23:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:23:57,457 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.1s)
Sep 14 00:24:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:24:39,786 main INFO screen EL pass=0 dev=6.4 ins=15.94 pro=26 1a=False 1b=True 2=False (49.3s)
Sep 14 00:25:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:20,714 main INFO screen BTC pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (67.1s)
Sep 14 00:25:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:37,129 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:25:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:25:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:25:51,399 main INFO screen JANE pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 14 00:26:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:26:49,141 main INFO screen DOGATE pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (57.0s)
Sep 14 00:27:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:27:53,371 main INFO screen TJR pass=1 dev=0.88 ins=0.0 pro=13 1a=False 1b=False 2=False (72.1s)
Sep 14 00:28:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:28:13,687 main INFO screen UNCLE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 00:29:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:29:44,070 main INFO screen Lobster pass=0 dev=0.0 ins=12.62 pro=67 1a=False 1b=False 2=True (63.2s)
Sep 14 00:30:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:30:07,099 main INFO screen XCOINS pass=0 dev=3.42 ins=35.27 pro=78 1a=False 1b=False 2=True (61.0s)
Sep 14 00:31:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:07,862 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:31:07 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:31:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:17,816 aiohttp.access INFO 43.131.24.90 [14/Sep/2026:00:31:17 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 5.1; rv:9.0.1) Gecko/20100101 Firefox/9.0.1"
Sep 14 00:31:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:30,032 main INFO screen potato pass=0 dev=0.0 ins=29.47 pro=81 1a=False 1b=False 2=True (65.4s)
Sep 14 00:31:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:31:36,391 main INFO screen LOBSTER pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.7s)
Sep 14 00:32:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:32:19,917 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 14 00:32:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:32:49,280 main INFO screen taxless pass=0 dev=0.0 ins=27.42 pro=59 1a=False 1b=False 2=True (65.6s)
Sep 14 00:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:17,824 main INFO screen LaMisery pass=0 dev=0.17 ins=0.0 pro=3 1a=False 1b=False 2=False (67.6s)
Sep 14 00:33:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:55,676 main INFO screen LAUNCHPAD pass=0 dev=0.0 ins=30.0 pro=30 1a=False 1b=False 2=True (54.1s)
Sep 14 00:33:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:33:59,560 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:02,153 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 00:35:02 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 00:35:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:13,030 main INFO screen MINT pass=1 dev=3.42 ins=14.3 pro=50 1a=False 1b=False 2=False (113.6s)
Sep 14 00:35:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:35,105 main INFO screen KFC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (99.4s)
Sep 14 00:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:35:55,800 main INFO screen STONK pass=0 dev=6.46 ins=0.0 pro=1 1a=False 1b=False 2=True (53.5s)
Sep 14 00:36:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:36:12,740 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:36:12 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T22:58:32Z
--- update 2026-09-13T23:03:34Z
--- update 2026-09-13T23:08:36Z
--- update 2026-09-13T23:13:55Z
--- update 2026-09-13T23:19:11Z
--- update 2026-09-13T23:24:17Z
--- update 2026-09-13T23:29:20Z
--- update 2026-09-13T23:34:26Z
--- update 2026-09-13T23:39:29Z
--- update 2026-09-13T23:44:32Z
--- update 2026-09-13T23:49:36Z
--- update 2026-09-13T23:54:39Z
--- update 2026-09-13T23:59:40Z
--- update 2026-09-14T00:04:46Z
--- update 2026-09-14T00:10:22Z
--- update 2026-09-14T00:15:23Z
--- update 2026-09-14T00:20:34Z
--- update 2026-09-14T00:25:36Z
--- update 2026-09-14T00:31:06Z
--- update 2026-09-14T00:36:11Z
```

## Analyses (laatste 25 regels)
```
inactive
23:13:05   26000 tokens, 2714180 trades, 375056 posities (140s)
23:13:17   28000 tokens, 2910347 trades, 398449 posities (152s)
23:13:28   30000 tokens, 3111752 trades, 425877 posities (163s)
23:13:41   32000 tokens, 3340745 trades, 458038 posities (176s)
23:13:53   34000 tokens, 3553363 trades, 489464 posities (188s)
23:14:05   36000 tokens, 3751673 trades, 513567 posities (200s)
23:14:16   38000 tokens, 3925965 trades, 534663 posities (212s)
23:14:30   40000 tokens, 4152994 trades, 570806 posities (226s)
23:14:42   42000 tokens, 4348336 trades, 595664 posities (237s)
23:14:53   44000 tokens, 4548599 trades, 621351 posities (248s)
23:15:05   46000 tokens, 4751977 trades, 646323 posities (260s)
23:15:17   48000 tokens, 4947857 trades, 676731 posities (273s)
23:15:30   50000 tokens, 5152223 trades, 704551 posities (286s)
23:15:42   52000 tokens, 5327073 trades, 727800 posities (297s)
23:15:53   54000 tokens, 5528435 trades, 756055 posities (309s)
23:16:05   56000 tokens, 5741491 trades, 787436 posities (320s)
23:16:15   58000 tokens, 5949257 trades, 815855 posities (330s)
23:16:24   60000 tokens, 6158655 trades, 848573 posities (339s)
23:16:34   62000 tokens, 6378507 trades, 891082 posities (349s)
23:16:43 posities: 913444 uit 6542295 trades (361s)
23:16:54 192830 wallets gerekend
23:16:54 geluk-toets
23:17:26 persistentie
23:17:28 kopieer-simulatie
23:19:10 klaar in 508s -> /opt/schaduwbot/reports/wallets.md
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
