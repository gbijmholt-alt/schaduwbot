# Schaduwbot status

- tijd: 2026-09-14 19:36:47 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 5 hours, 49 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.2G/38G | geheugen: 2052/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 133360, "tokens_in_memory": 9791, "msgs": 18338018, "trades": 3857575, "creates": 40347, "decode_fail": 333455, "rpc_calls": 111821, "rpc_errors": 7, "sol_usd": 103.17466525118788, "open_positions": 48, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 19:13:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:13:24,624 main INFO screen 单车泰森 pass=0 dev=0.0 ins=51.91 pro=37 1a=False 1b=False 2=True (63.6s)
Sep 14 19:13:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:13:57,130 main INFO screen FAVEO pass=0 dev=3.0 ins=0.0 pro=68 1a=False 1b=False 2=False (67.8s)
Sep 14 19:14:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:14:08,777 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.5s)
Sep 14 19:14:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:14:24,863 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 14 19:15:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:15:09,483 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (72.4s)
Sep 14 19:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:15:13,268 main INFO screen AICOIN pass=0 dev=0.0 ins=2.86 pro=66 1a=False 1b=False 2=False (64.5s)
Sep 14 19:15:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:15:25,498 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.6s)
Sep 14 19:16:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:16:12,169 main INFO screen EW pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (62.7s)
Sep 14 19:16:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:16:22,937 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.7s)
Sep 14 19:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:16:29,748 main INFO screen slarf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.2s)
Sep 14 19:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:16:29,791 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:16:29 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:17:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:17:22,896 main INFO screen 21e8 pass=0 dev=0.0 ins=43.53 pro=19 1a=False 1b=False 2=True (70.7s)
Sep 14 19:17:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:17:39,232 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (76.3s)
Sep 14 19:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:17:40,534 main INFO screen bigfoot pass=0 dev=0.0 ins=43.05 pro=51 1a=False 1b=False 2=True (70.8s)
Sep 14 19:18:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:18:15,304 main INFO screen CINEMA pass=0 dev=0.0 ins=37.43 pro=19 1a=False 1b=False 2=True (52.4s)
Sep 14 19:18:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:18:28,977 main INFO screen SOLHOUSE pass=0 dev=0.0 ins=36.43 pro=23 1a=False 1b=False 2=True (48.4s)
Sep 14 19:18:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:18:39,514 main INFO screen UNEMP pass=0 dev=0.0 ins=0.8 pro=38 1a=False 1b=False 2=False (60.3s)
Sep 14 19:19:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:19:12,688 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.4s)
Sep 14 19:19:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:19:27,459 main INFO screen MNRSE pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (58.5s)
Sep 14 19:19:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:19:41,553 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.0s)
Sep 14 19:20:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:20:03,177 main INFO screen BEE pass=0 dev=0.0 ins=28.79 pro=27 1a=False 1b=False 2=True (50.5s)
Sep 14 19:20:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:20:43,435 main INFO screen PVE pass=0 dev=0.0 ins=18.18 pro=70 1a=False 1b=False 2=True (76.0s)
Sep 14 19:20:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:20:47,659 main INFO screen STONKTARDS pass=0 dev=0.0 ins=8.14 pro=55 1a=False 1b=False 2=False (66.1s)
Sep 14 19:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:21:20,022 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (76.8s)
Sep 14 19:21:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:21:35,245 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:21:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:21:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:21:47,725 main INFO screen CATLESS pass=0 dev=2.47 ins=0.0 pro=6 1a=False 1b=False 2=False (64.3s)
Sep 14 19:21:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:21:51,471 main INFO screen BEEHIVE pass=0 dev=0.0 ins=15.18 pro=38 1a=False 1b=False 2=True (63.8s)
Sep 14 19:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:22:31,348 main INFO screen Beelana pass=0 dev=0.0 ins=12.17 pro=44 1a=False 1b=False 2=False (71.3s)
Sep 14 19:22:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:22:45,303 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.6s)
Sep 14 19:22:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:22:46,069 aiohttp.access INFO 20.115.64.61 [14/Sep/2026:19:22:46 +0000] "GET /manager/text/list HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 14 19:22:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:22:59,881 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 14 19:23:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:23:28,287 main INFO screen chip pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 14 19:23:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:23:35,155 main INFO screen One pass=0 dev=0.0 ins=22.59 pro=42 1a=False 1b=False 2=True (49.9s)
Sep 14 19:23:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:23:45,973 main INFO screen INTERNET pass=0 dev=0.0 ins=34.89 pro=17 1a=False 1b=False 2=True (46.1s)
Sep 14 19:24:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:24:18,156 main INFO screen EARLY pass=0 dev=0.0 ins=38.56 pro=11 1a=False 1b=False 2=True (49.9s)
Sep 14 19:24:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:24:33,314 main INFO screen CHAIRIANA pass=0 dev=0.0 ins=0.0 pro=58 1a=False 1b=True 2=True (58.2s)
Sep 14 19:24:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:24:43,876 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.9s)
Sep 14 19:25:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:25:29,321 main INFO screen PROHUMAN pass=0 dev=0.0 ins=13.67 pro=46 1a=False 1b=False 2=True (71.2s)
Sep 14 19:25:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:25:53,024 main INFO screen NINU pass=0 dev=0.0 ins=0.7 pro=6 1a=False 1b=False 2=False (79.7s)
Sep 14 19:25:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:25:56,536 main INFO screen FLUNDLE pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (72.7s)
Sep 14 19:26:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:26:37,191 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:26:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:26:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:26:42,658 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.3s)
Sep 14 19:26:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:26:55,298 main INFO screen PROHUMAN pass=0 dev=0.0 ins=8.63 pro=29 1a=False 1b=False 2=True (62.3s)
Sep 14 19:27:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:27:12,254 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.7s)
Sep 14 19:28:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:28:04,563 main INFO screen pica pass=0 dev=0.19 ins=62.61 pro=61 1a=False 1b=False 2=True (81.9s)
Sep 14 19:28:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:28:19,540 main INFO screen Gary pass=0 dev=0.0 ins=9.75 pro=65 1a=False 1b=False 2=True (67.3s)
Sep 14 19:28:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:28:22,042 main INFO screen Duvet pass=0 dev=0.0 ins=0.77 pro=10 1a=False 1b=False 2=False (86.7s)
Sep 14 19:29:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:29:31,691 main INFO screen WEST pass=0 dev=0.0 ins=53.75 pro=56 1a=False 1b=False 2=True (87.1s)
Sep 14 19:29:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:29:35,721 main INFO screen BIKEGIGA pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (76.2s)
Sep 14 19:29:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:29:39,332 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (77.3s)
Sep 14 19:30:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:30:28,142 main INFO screen chip pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 14 19:30:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:30:43,916 main INFO screen pothead pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.2s)
Sep 14 19:30:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:30:46,912 main INFO screen WEST pass=0 dev=0.0 ins=41.68 pro=43 1a=False 1b=False 2=False (67.6s)
Sep 14 19:31:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:31:41,535 main INFO screen NINU pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (73.4s)
Sep 14 19:31:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:31:44,810 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:31:44 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:31:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:31:46,372 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.5s)
Sep 14 19:31:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:31:49,676 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.8s)
Sep 14 19:32:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:32:52,158 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.8s)
Sep 14 19:32:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:32:55,017 main INFO screen Claude pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (65.3s)
Sep 14 19:32:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:32:55,336 main INFO screen Kabosu pass=0 dev=0.0 ins=14.29 pro=48 1a=False 1b=False 2=True (73.8s)
Sep 14 19:34:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:34:06,864 main INFO screen Gary pass=0 dev=0.0 ins=49.19 pro=24 1a=False 1b=False 2=True (74.7s)
Sep 14 19:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:34:08,628 main INFO screen Liberland pass=0 dev=0.0 ins=9.99 pro=81 1a=False 1b=False 2=True (73.6s)
Sep 14 19:34:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:34:11,827 main INFO screen WEST pass=0 dev=0.0 ins=53.96 pro=56 1a=False 1b=False 2=True (76.5s)
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:35:22,985 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 19:35:22 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 19:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:35:23,159 aiohttp.access INFO 94.154.43.223 [14/Sep/2026:19:35:23 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 19:35:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:35:49,606 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (102.7s)
Sep 14 19:36:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:36:00,684 main INFO screen PRINT pass=0 dev=0.0 ins=5.52 pro=33 1a=False 1b=False 2=False (112.1s)
Sep 14 19:36:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:36:09,938 main INFO screen FINE pass=0 dev=0.0 ins=5.7 pro=63 1a=False 1b=False 2=False (118.1s)
Sep 14 19:36:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:36:44,210 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.6s)
Sep 14 19:36:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:36:47,880 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:36:47 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T18:04:03Z
--- update 2026-09-14T18:09:27Z
--- update 2026-09-14T18:14:36Z
--- update 2026-09-14T18:19:53Z
--- update 2026-09-14T18:25:09Z
--- update 2026-09-14T18:30:25Z
--- update 2026-09-14T18:35:36Z
--- update 2026-09-14T18:40:39Z
--- update 2026-09-14T18:45:49Z
--- update 2026-09-14T18:50:57Z
--- update 2026-09-14T18:56:05Z
--- update 2026-09-14T19:01:07Z
--- update 2026-09-14T19:06:12Z
--- update 2026-09-14T19:11:15Z
--- update 2026-09-14T19:16:28Z
--- update 2026-09-14T19:21:34Z
--- update 2026-09-14T19:26:36Z
--- update 2026-09-14T19:31:43Z
--- update 2026-09-14T19:36:46Z
```

## Analyses (laatste 25 regels)
```
inactive
18:41:17   36000 tokens, 3638093 trades, 448810 posities (235s)
18:41:30   38000 tokens, 3833313 trades, 474800 posities (248s)
18:41:44   40000 tokens, 4028615 trades, 498777 posities (262s)
18:41:57   42000 tokens, 4216542 trades, 518531 posities (275s)
18:42:10   44000 tokens, 4401553 trades, 541372 posities (288s)
18:42:22   46000 tokens, 4584158 trades, 563643 posities (300s)
18:42:34   48000 tokens, 4783790 trades, 585472 posities (312s)
18:42:47   50000 tokens, 5003074 trades, 615099 posities (325s)
18:42:59   52000 tokens, 5192448 trades, 634508 posities (337s)
18:43:09   54000 tokens, 5369608 trades, 656921 posities (347s)
18:43:21   56000 tokens, 5562048 trades, 679857 posities (359s)
18:43:32   58000 tokens, 5748838 trades, 703454 posities (370s)
18:43:45   60000 tokens, 5965794 trades, 730891 posities (383s)
18:43:57   62000 tokens, 6163332 trades, 760633 posities (395s)
18:44:10   64000 tokens, 6381264 trades, 789533 posities (408s)
18:44:22   66000 tokens, 6567294 trades, 814088 posities (420s)
18:44:35   68000 tokens, 6764874 trades, 841267 posities (433s)
18:44:48   70000 tokens, 6958343 trades, 869440 posities (446s)
18:45:00   72000 tokens, 7152236 trades, 898391 posities (458s)
18:45:02 posities: 902239 uit 7182626 trades (464s)
18:45:16 202478 wallets gerekend
18:45:16 geluk-toets
18:45:52 persistentie
18:45:55 kopieer-simulatie
18:48:01 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
18:40:42 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:45:54 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:51:01 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:56:06 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:01:08 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:06:13 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:11:16 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:16:29 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:21:34 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:26:36 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:31:44 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:36:47 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
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
