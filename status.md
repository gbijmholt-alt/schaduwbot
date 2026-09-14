# Schaduwbot status

- tijd: 2026-09-14 20:27:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 6 hours, 40 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.3G/38G | geheugen: 2122/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 136393, "tokens_in_memory": 10267, "msgs": 19068524, "trades": 3997311, "creates": 41942, "decode_fail": 350783, "rpc_calls": 114856, "rpc_errors": 7, "sol_usd": 104.56437441516547, "open_positions": 48, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 20:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:04,684 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:02:04 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:02:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:22,971 main INFO screen Kirk pass=0 dev=0.0 ins=40.2 pro=2 1a=False 1b=False 2=True (46.5s)
Sep 14 20:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:50,989 main INFO screen cashcat pass=0 dev=0.0 ins=31.29 pro=33 1a=False 1b=False 2=True (47.1s)
Sep 14 20:02:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:54,313 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.4s)
Sep 14 20:03:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:03:15,761 main INFO screen cashcat pass=0 dev=0.0 ins=40.37 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 14 20:03:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:03:39,834 main INFO screen cashcat pass=0 dev=0.0 ins=40.31 pro=2 1a=False 1b=False 2=True (48.8s)
Sep 14 20:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:04,009 main INFO screen DOM pass=0 dev=0.0 ins=17.0 pro=73 1a=False 1b=False 2=True (69.7s)
Sep 14 20:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:04,684 main INFO screen FINE pass=0 dev=0.0 ins=40.56 pro=1 1a=False 1b=False 2=True (48.9s)
Sep 14 20:04:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:49,223 main INFO screen FINE pass=0 dev=0.0 ins=18.52 pro=56 1a=False 1b=False 2=False (45.2s)
Sep 14 20:04:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:49,288 main INFO screen glob pass=0 dev=0.0 ins=50.52 pro=21 1a=False 1b=False 2=True (69.5s)
Sep 14 20:04:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:55,059 main INFO screen FINE pass=0 dev=0.0 ins=40.28 pro=0 1a=False 1b=False 2=True (50.4s)
Sep 14 20:05:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:05:57,757 main INFO screen     NWN pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.5s)
Sep 14 20:05:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:05:59,699 main INFO screen WOFI pass=0 dev=0.78 ins=139.38 pro=1 1a=False 1b=False 2=True (64.6s)
Sep 14 20:06:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:06:00,588 main INFO screen pumpcat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.3s)
Sep 14 20:06:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:06:49,884 main INFO screen taxcat pass=0 dev=0.0 ins=39.98 pro=2 1a=False 1b=False 2=True (50.2s)
Sep 14 20:07:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:05,111 main INFO screen PVE pass=0 dev=0.0 ins=79.98 pro=67 1a=False 1b=False 2=False (67.4s)
Sep 14 20:07:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:07,606 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:07:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:07:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:08,179 main INFO screen Pumploo pass=0 dev=0.0 ins=11.38 pro=51 1a=False 1b=False 2=False (67.6s)
Sep 14 20:07:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:48,539 main INFO screen Dividend pass=0 dev=0.0 ins=41.73 pro=1 1a=False 1b=False 2=True (58.7s)
Sep 14 20:07:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:56,974 main INFO screen FAIR pass=0 dev=0.0 ins=78.92 pro=1 1a=False 1b=False 2=True (51.9s)
Sep 14 20:08:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:08:04,655 main INFO screen RKL pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (56.5s)
Sep 14 20:08:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:08:41,804 main INFO screen GTA 6 Coin pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 14 20:08:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:08:56,393 main INFO screen income pass=0 dev=0.0 ins=12.0 pro=55 1a=False 1b=False 2=True (59.4s)
Sep 14 20:09:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:09:00,469 main INFO screen Niggio pass=0 dev=0.0 ins=39.27 pro=0 1a=False 1b=False 2=True (55.8s)
Sep 14 20:09:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:09:33,982 main INFO screen FOUR pass=0 dev=0.0 ins=9.97 pro=76 1a=False 1b=False 2=False (52.2s)
Sep 14 20:09:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:09:54,606 main INFO screen LARP pass=0 dev=0.0 ins=40.06 pro=3 1a=False 1b=False 2=True (54.1s)
Sep 14 20:10:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:10:06,283 main INFO screen NINGEN pass=0 dev=0.0 ins=14.74 pro=77 1a=False 1b=False 2=True (69.9s)
Sep 14 20:10:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:10:27,194 main INFO screen ROBOELON pass=0 dev=0.0 ins=40.78 pro=0 1a=False 1b=False 2=True (53.2s)
Sep 14 20:11:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:11:06,655 main INFO screen FEE pass=0 dev=0.07 ins=0.0 pro=70 1a=False 1b=False 2=False (72.0s)
Sep 14 20:11:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:11:08,292 main INFO screen RSI pass=0 dev=0.0 ins=39.45 pro=1 1a=False 1b=False 2=True (62.0s)
Sep 14 20:11:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:11:25,407 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.2s)
Sep 14 20:12:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:12:03,623 main INFO screen Cody pass=0 dev=0.0 ins=20.01 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 14 20:12:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:12:07,888 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:12:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:12:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:12:08,408 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.1s)
Sep 14 20:12:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:12:26,448 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.0s)
Sep 14 20:13:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:13:03,612 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.0s)
Sep 14 20:13:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:13:08,411 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.0s)
Sep 14 20:13:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:13:27,944 main INFO screen HEAVES pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (61.5s)
Sep 14 20:14:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:14:01,039 main INFO screen niketyson pass=0 dev=0.0 ins=35.44 pro=50 1a=True 1b=True 2=True (57.4s)
Sep 14 20:14:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:14:10,143 main INFO screen RALPH pass=0 dev=0.0 ins=12.65 pro=46 1a=False 1b=False 2=False (61.7s)
Sep 14 20:14:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:14:26,261 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.3s)
Sep 14 20:15:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:15:10,202 main INFO screen shitrat pass=0 dev=0.0 ins=35.52 pro=65 1a=False 1b=False 2=True (69.2s)
Sep 14 20:15:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:15:20,431 main INFO screen STONKSBAT pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (70.3s)
Sep 14 20:15:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:15:26,674 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.4s)
Sep 14 20:16:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:16:09,004 main INFO screen BBC pass=0 dev=0.0 ins=117.02 pro=1 1a=False 1b=False 2=True (58.8s)
Sep 14 20:16:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:16:22,912 main INFO screen NYT Coin pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (62.5s)
Sep 14 20:16:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:16:42,983 main INFO screen CHOGE pass=0 dev=0.0 ins=20.73 pro=2 1a=False 1b=False 2=False (76.3s)
Sep 14 20:17:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:17:07,985 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:17:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:17:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:17:17,085 main INFO screen pump pass=0 dev=0.0 ins=60.65 pro=15 1a=False 1b=False 2=True (54.2s)
Sep 14 20:17:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:17:22,758 main INFO screen Lobster pass=0 dev=0.0 ins=39.75 pro=69 1a=False 1b=False 2=True (73.8s)
Sep 14 20:17:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:17:54,627 main INFO screen batonpump pass=0 dev=0.0 ins=20.1 pro=2 1a=False 1b=False 2=False (71.6s)
Sep 14 20:18:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:18:37,588 main INFO screen CHIC pass=0 dev=0.0 ins=11.65 pro=54 1a=False 1b=False 2=True (74.8s)
Sep 14 20:18:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:18:39,088 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (82.0s)
Sep 14 20:18:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:18:58,850 main INFO screen OXINDR pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (64.2s)
Sep 14 20:19:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:19:57,071 main INFO screen KOALYPT pass=0 dev=0.0 ins=49.24 pro=25 1a=False 1b=False 2=True (79.5s)
Sep 14 20:19:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:19:59,247 main INFO screen $INU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (80.2s)
Sep 14 20:20:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:20:05,745 main INFO screen wagie pass=0 dev=0.0 ins=47.11 pro=24 1a=False 1b=False 2=True (66.9s)
Sep 14 20:20:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:20:52,719 main INFO screen GOAT pass=0 dev=0.0 ins=1.72 pro=43 1a=False 1b=False 2=True (55.6s)
Sep 14 20:21:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:21:05,506 main INFO screen OMNI pass=0 dev=0.0 ins=10.27 pro=61 1a=False 1b=False 2=False (66.3s)
Sep 14 20:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:21:13,327 main INFO screen taxcat pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=False 2=True (67.6s)
Sep 14 20:21:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:21:49,741 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 14 20:22:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:22:02,388 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 14 20:22:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:22:16,929 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:22:16 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:22:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:22:18,110 main INFO screen XREV pass=0 dev=2.12 ins=19.76 pro=66 1a=False 1b=False 2=True (64.8s)
Sep 14 20:22:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:22:44,299 main INFO screen ADAMITY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.6s)
Sep 14 20:22:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:22:51,247 main INFO screen AIZEN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (48.9s)
Sep 14 20:23:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:23:30,328 main INFO screen BUNNY pass=0 dev=0.0 ins=28.53 pro=62 1a=False 1b=False 2=True (72.2s)
Sep 14 20:23:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:23:42,632 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.3s)
Sep 14 20:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:23:47,779 main INFO screen zidek pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.5s)
Sep 14 20:24:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:24:29,267 main INFO screen $BLK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 20:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:24:47,113 main INFO screen PepethePP pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (59.3s)
Sep 14 20:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:24:49,332 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.7s)
Sep 14 20:25:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:25:19,408 main INFO screen $DOGGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.1s)
Sep 14 20:25:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:25:54,085 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.8s)
Sep 14 20:25:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:25:57,835 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (70.7s)
Sep 14 20:26:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:26:18,330 main INFO screen charley pass=0 dev=0.0 ins=15.33 pro=16 1a=False 1b=False 2=True (58.9s)
Sep 14 20:26:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:26:47,299 main INFO screen CDUDE pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (53.2s)
Sep 14 20:27:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:27:05,041 main INFO screen taxcat pass=0 dev=0.0 ins=17.0 pro=2 1a=False 1b=False 2=True (67.2s)
Sep 14 20:27:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:27:16,733 main INFO screen Trader pass=0 dev=0.0 ins=17.49 pro=1 1a=False 1b=False 2=False (58.4s)
Sep 14 20:27:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:27:20,984 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:27:20 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T19:01:07Z
--- update 2026-09-14T19:06:12Z
--- update 2026-09-14T19:11:15Z
--- update 2026-09-14T19:16:28Z
--- update 2026-09-14T19:21:34Z
--- update 2026-09-14T19:26:36Z
--- update 2026-09-14T19:31:43Z
--- update 2026-09-14T19:36:46Z
--- update 2026-09-14T19:41:50Z
--- update 2026-09-14T19:46:52Z
--- update 2026-09-14T19:51:52Z
--- update 2026-09-14T19:56:58Z
--- update 2026-09-14T20:02:03Z
Running as unit: schaduwbot-wallets.service; invocation ID: 14498679f71340f08b872ad37a3b0138
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T20:07:06Z
--- update 2026-09-14T20:12:06Z
--- update 2026-09-14T20:17:06Z
--- update 2026-09-14T20:22:15Z
--- update 2026-09-14T20:27:19Z
```

## Analyses (laatste 25 regels)
```
active
18:44:48   70000 tokens, 6958343 trades, 869440 posities (446s)
18:45:00   72000 tokens, 7152236 trades, 898391 posities (458s)
18:45:02 posities: 902239 uit 7182626 trades (464s)
18:45:16 202478 wallets gerekend
18:45:16 geluk-toets
18:45:52 persistentie
18:45:55 kopieer-simulatie
18:48:01 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
20:02:04 89494 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
20:02:30   ingelezen tot rowid 9373289 (200000 rijen, 200000 bruikbaar)
20:02:39   ingelezen tot rowid 9499553 (326264 rijen, 326264 bruikbaar)
20:02:40 ingelezen: 326264 nieuwe trades, 326264 bruikbaar (36s)
20:05:17 3000 aankopen van gevolgde wallets geëvalueerd
20:06:08 vroege kopers: 256 voldoen nu, register 449, 443 tokens beoordeeld
20:06:39 grote spelers: saldo van 479 wallets opgehaald
20:07:06 herkomst: 40 posities gekoppeld
20:07:18 klaar in 314s -> /opt/schaduwbot/reports/ledger.md
20:19:15 S1: gezakt — toets n=24393, verkennend n=14656
20:19:15 klaar in 717s -> /opt/schaduwbot/reports/hypotheses.md
20:19:17 probe: 150 transacties ophalen
20:22:39 poolveld: 14 pools bekeken, 0 te gaan -> vastgesteld @43
20:23:49 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
20:23:49 prijsijk: n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:23:51 na-migratie: 100 paren te checken
20:25:50 na-migratie: 66 paren, 9 prijzen
```

## IJking poolkoers (laatste 12 regels)
```
19:31:44 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:36:47 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:41:51 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:46:53 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:51:53 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:56:59 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:02:04 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:07:10 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:12:10 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:17:10 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:22:19 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:27:20 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
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
