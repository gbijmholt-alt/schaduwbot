# Schaduwbot status

- tijd: 2026-09-15 07:01:47 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 17 hours, 14 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2240/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 174459, "tokens_in_memory": 6891, "msgs": 26186594, "trades": 5276790, "creates": 56319, "decode_fail": 447185, "rpc_calls": 152518, "rpc_errors": 13, "sol_usd": 100.89593663920428, "open_positions": 54, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 06:37:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:37:49,787 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (71.0s)
Sep 15 06:38:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:38:12,840 main INFO screen Bender pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.1s)
Sep 15 06:38:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:38:25,350 main INFO screen boost pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.6s)
Sep 15 06:38:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:38:41,003 main INFO screen GOAF pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (51.2s)
Sep 15 06:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:39:02,532 main INFO screen Lil Yatchy pass=0 dev=0.0 ins=24.45 pro=60 1a=False 1b=False 2=True (49.7s)
Sep 15 06:39:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:39:18,083 main INFO screen ZCHUD pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=True 2=True (52.7s)
Sep 15 06:39:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:39:34,490 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.5s)
Sep 15 06:40:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:40:11,378 main INFO screen Asian dog pass=0 dev=0.0 ins=0.8 pro=57 1a=False 1b=False 2=False (53.3s)
Sep 15 06:40:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:40:13,350 main INFO screen boost pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (70.8s)
Sep 15 06:40:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:40:34,253 main INFO screen dͨoͣgͭ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.8s)
Sep 15 06:41:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:41:07,203 main INFO screen SWAIFU pass=0 dev=0.0 ins=79.12 pro=4 1a=False 1b=True 2=True (55.8s)
Sep 15 06:41:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:41:16,022 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:41:16 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:41:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:41:21,617 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.3s)
Sep 15 06:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:41:30,265 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (56.0s)
Sep 15 06:42:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:42:10,245 main INFO screen Zoidberg pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (63.0s)
Sep 15 06:42:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:42:27,236 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 15 06:42:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:42:29,204 main INFO screen Samsung pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.9s)
Sep 15 06:43:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:43:02,944 main INFO screen momo pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.7s)
Sep 15 06:43:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:43:13,496 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (46.3s)
Sep 15 06:43:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:43:35,159 main INFO screen Threadguy pass=0 dev=0.0 ins=15.54 pro=62 1a=False 1b=False 2=False (66.0s)
Sep 15 06:44:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:44:06,304 main INFO screen Frosty pass=0 dev=0.0 ins=31.16 pro=37 1a=False 1b=False 2=True (52.8s)
Sep 15 06:44:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:44:09,303 main INFO screen BLACKJACK pass=0 dev=0.0 ins=22.15 pro=39 1a=False 1b=False 2=False (66.4s)
Sep 15 06:44:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:44:25,871 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (50.7s)
Sep 15 06:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:45:10,614 main INFO screen ASh pass=0 dev=0.0 ins=0.38 pro=21 1a=False 1b=False 2=False (61.3s)
Sep 15 06:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:45:12,182 main INFO screen ASTER  pass=0 dev=34.97 ins=0.0 pro=13 1a=False 1b=False 2=False (65.9s)
Sep 15 06:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:45:31,003 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (65.1s)
Sep 15 06:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:46:15,980 main INFO screen Mayhem  pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.8s)
Sep 15 06:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:46:17,314 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:46:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:46:17,888 main INFO screen AMC pass=0 dev=0.0 ins=20.6 pro=64 1a=False 1b=False 2=True (67.3s)
Sep 15 06:46:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:46:34,468 main INFO screen $BULL pass=0 dev=0.0 ins=0.28 pro=1 1a=False 1b=False 2=False (63.5s)
Sep 15 06:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:47:27,607 main INFO screen asscoin pass=0 dev=0.0 ins=13.26 pro=73 1a=False 1b=False 2=True (71.6s)
Sep 15 06:47:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:47:29,597 main INFO screen Clemente pass=0 dev=0.0 ins=20.04 pro=54 1a=False 1b=False 2=True (55.1s)
Sep 15 06:47:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:47:30,106 main INFO screen 404 pass=0 dev=0.0 ins=17.19 pro=54 1a=False 1b=False 2=True (72.2s)
Sep 15 06:48:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:48:14,417 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (46.8s)
Sep 15 06:48:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:48:32,960 main INFO screen 猫王 pass=0 dev=0.2 ins=72.33 pro=16 1a=False 1b=False 2=False (63.4s)
Sep 15 06:48:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:48:35,073 main INFO screen buttcoin pass=0 dev=0.0 ins=0.0 pro=39 1a=False 1b=False 2=False (65.0s)
Sep 15 06:49:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:49:22,683 main INFO screen FLY pass=0 dev=0.0 ins=4.45 pro=72 1a=False 1b=False 2=True (68.3s)
Sep 15 06:49:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:49:24,828 main INFO screen awd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (49.8s)
Sep 15 06:49:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:49:27,289 main INFO screen fomo pass=0 dev=0.0 ins=146.16 pro=1 1a=False 1b=False 2=True (54.3s)
Sep 15 06:50:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:50:28,498 main INFO screen Inscribe pass=0 dev=0.14 ins=0.0 pro=68 1a=False 1b=False 2=True (65.8s)
Sep 15 06:50:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:50:30,572 main INFO screen awd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.7s)
Sep 15 06:50:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:50:30,884 main INFO screen Benz pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (63.6s)
Sep 15 06:50:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:50:54,059 aiohttp.access INFO 65.49.1.122 [15/Sep/2026:06:50:54 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 06:51:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:51:15,265 main INFO screen WILL FERAL pass=0 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (46.8s)
Sep 15 06:51:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:51:16,681 main INFO screen dawd pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (46.1s)
Sep 15 06:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:51:35,834 main INFO screen SQLana pass=0 dev=0.0 ins=8.24 pro=65 1a=False 1b=False 2=False (64.9s)
Sep 15 06:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:51:35,976 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:51:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 06:52:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:52:10,652 main INFO screen awd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.4s)
Sep 15 06:52:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:52:19,234 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (62.6s)
Sep 15 06:52:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:52:25,414 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.6s)
Sep 15 06:53:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:53:00,188 main INFO screen MAYHEM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.5s)
Sep 15 06:53:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:53:23,298 main INFO screen TERRYCREWSHIP pass=0 dev=0.0 ins=24.62 pro=38 1a=False 1b=False 2=False (64.1s)
Sep 15 06:53:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:53:28,108 main INFO screen asscoin pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (62.7s)
Sep 15 06:53:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:53:55,440 main INFO screen cartyson pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (55.2s)
Sep 15 06:54:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:54:30,055 main INFO screen orangie pass=0 dev=0.0 ins=6.82 pro=15 1a=False 1b=False 2=False (66.8s)
Sep 15 06:54:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:54:31,546 main INFO screen ACC pass=0 dev=0.0 ins=77.08 pro=14 1a=False 1b=False 2=True (63.4s)
Sep 15 06:54:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:54:50,673 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 15 06:55:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:55:21,354 main INFO screen HUHDOG pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (51.3s)
Sep 15 06:55:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:55:25,349 main INFO screen EGGWHITE pass=0 dev=0.0 ins=2.01 pro=27 1a=False 1b=False 2=False (53.8s)
Sep 15 06:55:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:55:40,265 main INFO screen EGGWHITE pass=0 dev=0.0 ins=1.85 pro=35 1a=False 1b=False 2=False (49.6s)
Sep 15 06:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:56:33,618 main INFO screen SPED pass=0 dev=0.0 ins=12.72 pro=46 1a=False 1b=False 2=False (68.3s)
Sep 15 06:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:56:35,526 main INFO screen FLY pass=0 dev=0.0 ins=17.05 pro=57 1a=False 1b=False 2=False (74.2s)
Sep 15 06:56:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:56:37,277 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:06:56:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 06:56:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:56:41,447 main INFO screen ALCAPP pass=0 dev=0.0 ins=79.12 pro=3 1a=False 1b=True 2=True (61.2s)
Sep 15 06:57:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:57:22,241 main INFO screen Google pass=0 dev=0.0 ins=117.77 pro=1 1a=False 1b=False 2=True (48.6s)
Sep 15 06:57:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:57:39,793 main INFO screen DANGR pass=0 dev=0.0 ins=136.14 pro=1 1a=False 1b=False 2=True (58.3s)
Sep 15 06:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:57:41,842 main INFO screen PUSSY pass=0 dev=0.0 ins=3.39 pro=64 1a=False 1b=False 2=False (66.3s)
Sep 15 06:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:58:29,579 main INFO screen ROCKET pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (67.3s)
Sep 15 06:58:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:58:30,457 main INFO screen AREF pass=0 dev=0.0 ins=158.72 pro=1 1a=False 1b=False 2=True (50.7s)
Sep 15 06:58:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:58:36,016 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.2s)
Sep 15 06:59:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:59:41,355 main INFO screen FLYCHAD pass=0 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (70.9s)
Sep 15 06:59:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:59:44,278 main INFO screen BikeApe pass=0 dev=0.0 ins=75.56 pro=10 1a=False 1b=False 2=True (74.7s)
Sep 15 06:59:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 06:59:45,803 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (69.8s)
Sep 15 07:00:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:00:29,573 main INFO screen MESA pass=0 dev=0.0 ins=19.48 pro=45 1a=False 1b=False 2=False (48.2s)
Sep 15 07:00:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:00:41,753 main INFO screen NENEM pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (55.9s)
Sep 15 07:00:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:00:48,280 main INFO screen POKEMON pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (64.0s)
Sep 15 07:01:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:01:26,480 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (56.9s)
Sep 15 07:01:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:01:35,373 main INFO screen ALMOND pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (53.6s)
Sep 15 07:01:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:01:43,743 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (55.5s)
Sep 15 07:01:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:01:47,350 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:01:47 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: 8878e1e
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: f5672219e09449dfbd4cf05bf897dc12
analyses gestart (ef01904db983)
--- update 2026-09-15T05:45:17Z
--- update 2026-09-15T05:50:30Z
--- update 2026-09-15T05:55:30Z
--- update 2026-09-15T06:00:31Z
--- update 2026-09-15T06:05:31Z
--- update 2026-09-15T06:10:36Z
--- update 2026-09-15T06:15:38Z
--- update 2026-09-15T06:20:58Z
--- update 2026-09-15T06:26:02Z
--- update 2026-09-15T06:31:06Z
--- update 2026-09-15T06:36:14Z
--- update 2026-09-15T06:41:14Z
--- update 2026-09-15T06:46:16Z
--- update 2026-09-15T06:51:34Z
--- update 2026-09-15T06:56:36Z
--- update 2026-09-15T07:01:46Z
```

## Analyses (laatste 25 regels)
```
inactive
06:28:28   38000 tokens, 3681003 trades, 443940 posities (248s)
06:28:42   40000 tokens, 3878402 trades, 468824 posities (262s)
06:28:55   42000 tokens, 4065280 trades, 492092 posities (275s)
06:29:07   44000 tokens, 4243961 trades, 512326 posities (287s)
06:29:19   46000 tokens, 4422263 trades, 532650 posities (299s)
06:29:33   48000 tokens, 4597419 trades, 553807 posities (312s)
06:29:46   50000 tokens, 4788806 trades, 577841 posities (326s)
06:30:00   52000 tokens, 4999896 trades, 603952 posities (339s)
06:30:12   54000 tokens, 5196535 trades, 629071 posities (352s)
06:30:26   56000 tokens, 5386638 trades, 656411 posities (366s)
06:30:39   58000 tokens, 5556442 trades, 675632 posities (379s)
06:30:53   60000 tokens, 5747120 trades, 700684 posities (393s)
06:31:08   62000 tokens, 5938035 trades, 722696 posities (407s)
06:31:20   64000 tokens, 6133797 trades, 751257 posities (420s)
06:31:32   66000 tokens, 6333181 trades, 775959 posities (431s)
06:31:44   68000 tokens, 6522980 trades, 801090 posities (443s)
06:31:56   70000 tokens, 6699942 trades, 821373 posities (456s)
06:32:08   72000 tokens, 6901917 trades, 845358 posities (467s)
06:32:21   74000 tokens, 7110225 trades, 878785 posities (480s)
06:32:31 posities: 896682 uit 7257573 trades (496s)
06:32:47 209065 wallets gerekend
06:32:47 geluk-toets
06:33:30 persistentie
06:33:34 kopieer-simulatie
06:35:45 klaar in 690s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
05:40:40 ijk: +2 van 2 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=172 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:40:41 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 6/39/156 | al gemeten: 508
06:36:36 ijk: +6 van 13 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=183 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:36:36 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 13/42/163 | al gemeten: 529
06:41:32 ijk: +6 van 7 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=185 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:41:33 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 13/43/162 | al gemeten: 535
06:46:31 ijk: +5 van 5 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 10}) | verste bak n=190 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:46:31 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 15/46/163 | al gemeten: 540
06:51:45 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=192 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:51:45 ijk-diagnose: nieuwste migratie 1.5 min oud | migraties 15/60/240 min: 11/45/164 | al gemeten: 543
06:56:42 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=194 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:56:42 ijk-diagnose: nieuwste migratie 2.5 min oud | migraties 15/60/240 min: 9/43/165 | al gemeten: 545
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
