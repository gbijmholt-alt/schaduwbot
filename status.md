# Schaduwbot status

- tijd: 2026-09-15 12:31:12 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 22 hours, 44 minutes
- bot-service: active
- code-versie: 8b410ac
- schijf: 7.1G/38G | geheugen: 2359/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 194224, "tokens_in_memory": 6216, "msgs": 27865204, "trades": 5801663, "creates": 62063, "decode_fail": 480613, "rpc_calls": 172197, "rpc_errors": 15, "sol_usd": 101.02931747497273, "open_positions": 35, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 12:06:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:06:08,899 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:06:08 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:06:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:06:10,110 main INFO screen Bulljak pass=0 dev=0.0 ins=54.75 pro=5 1a=False 1b=False 2=True (50.2s)
Sep 15 12:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:06:56,314 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.9s)
Sep 15 12:07:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:07:18,499 main INFO screen CARDS pass=0 dev=0.0 ins=16.83 pro=8 1a=False 1b=False 2=False (68.4s)
Sep 15 12:07:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:07:21,749 main INFO screen OneBull pass=0 dev=0.0 ins=55.77 pro=27 1a=True 1b=False 2=True (74.9s)
Sep 15 12:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:07:30,443 aiohttp.access INFO 179.43.134.114 [15/Sep/2026:12:07:30 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 15 12:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:07:30,512 aiohttp.access INFO 179.43.134.114 [15/Sep/2026:12:07:30 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 15 12:07:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:07:59,352 main INFO screen KevinChart pass=0 dev=0.0 ins=53.08 pro=28 1a=False 1b=False 2=True (63.0s)
Sep 15 12:08:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:08:19,102 main INFO screen BBC pass=0 dev=0.0 ins=162.39 pro=0 1a=False 1b=False 2=True (60.6s)
Sep 15 12:08:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:08:36,261 main INFO screen Megan pass=0 dev=0.0 ins=4.25 pro=40 1a=False 1b=False 2=False (74.5s)
Sep 15 12:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:09:17,554 main INFO screen SALO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (78.2s)
Sep 15 12:09:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:09:25,565 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 15 12:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:09:36,848 main INFO screen EGGSHEERAN pass=0 dev=0.0 ins=79.26 pro=2 1a=False 1b=True 2=True (60.6s)
Sep 15 12:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:10:16,721 main INFO screen KevinChart pass=0 dev=0.0 ins=53.75 pro=32 1a=False 1b=False 2=True (59.2s)
Sep 15 12:10:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:10:40,612 main INFO screen OnlyFlies pass=0 dev=0.0 ins=9.15 pro=72 1a=False 1b=False 2=True (75.0s)
Sep 15 12:10:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:10:51,507 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.7s)
Sep 15 12:11:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:11:09,404 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:11:09 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:11:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:11:23,518 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 15 12:11:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:11:38,255 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 15 12:11:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:11:51,378 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.9s)
Sep 15 12:12:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:12:23,673 main INFO screen 屁屁 pass=0 dev=0.0 ins=79.13 pro=2 1a=False 1b=True 2=True (60.2s)
Sep 15 12:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:12:49,348 main INFO screen FSG pass=0 dev=0.0 ins=24.0 pro=77 1a=False 1b=False 2=False (71.1s)
Sep 15 12:13:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:13:00,681 main INFO screen DonaldTrumpet pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=False 2=True (69.3s)
Sep 15 12:13:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:13:23,495 main INFO screen PRISM pass=0 dev=0.0 ins=30.5 pro=11 1a=False 1b=False 2=True (59.8s)
Sep 15 12:13:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:13:45,136 main INFO screen SALO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.8s)
Sep 15 12:14:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:14:03,649 main INFO screen RAYGUN pass=0 dev=0.0 ins=22.59 pro=52 1a=False 1b=False 2=True (63.0s)
Sep 15 12:14:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:14:16,678 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 15 12:14:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:14:56,081 main INFO screen KevinChart pass=0 dev=0.0 ins=53.05 pro=47 1a=False 1b=False 2=True (70.9s)
Sep 15 12:14:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:14:59,752 main INFO screen snake pass=0 dev=0.0 ins=12.82 pro=64 1a=False 1b=True 2=False (56.1s)
Sep 15 12:15:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:15:29,230 main INFO screen GOYBEAM pass=0 dev=0.0 ins=4.91 pro=65 1a=False 1b=False 2=False (72.5s)
Sep 15 12:16:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:16:09,331 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:16:09 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:16:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:16:12,617 main INFO screen SCAN pass=0 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (76.5s)
Sep 15 12:16:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:16:12,953 main INFO screen SCRIBEDOG pass=0 dev=2.09 ins=0.0 pro=12 1a=False 1b=False 2=False (73.2s)
Sep 15 12:16:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:16:43,463 main INFO screen Obama  pass=0 dev=0.0 ins=4.13 pro=52 1a=False 1b=False 2=False (74.2s)
Sep 15 12:17:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:17:11,976 aiohttp.access INFO 94.154.43.250 [15/Sep/2026:12:17:11 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 12:17:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:17:16,323 main INFO screen Curie pass=0 dev=0.0 ins=13.25 pro=57 1a=False 1b=False 2=True (63.7s)
Sep 15 12:17:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:17:24,337 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.4s)
Sep 15 12:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:17:40,564 main INFO screen LadyGarag pass=0 dev=0.0 ins=67.1 pro=17 1a=False 1b=True 2=True (57.1s)
Sep 15 12:18:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:18:12,169 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.8s)
Sep 15 12:18:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:18:22,111 main INFO screen BOOM pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (57.8s)
Sep 15 12:18:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:18:36,295 main INFO screen KIRKY pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (55.7s)
Sep 15 12:19:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:19:08,846 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.7s)
Sep 15 12:19:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:19:16,388 main INFO screen TNT pass=0 dev=0.01 ins=125.05 pro=1 1a=False 1b=False 2=True (54.3s)
Sep 15 12:19:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:19:33,659 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.4s)
Sep 15 12:20:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:20:17,753 main INFO screen pepevoice pass=0 dev=0.0 ins=29.37 pro=61 1a=False 1b=False 2=True (68.9s)
Sep 15 12:20:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:20:21,090 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.7s)
Sep 15 12:20:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:20:28,035 main INFO screen HERMES pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (54.4s)
Sep 15 12:21:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:21:09,433 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (51.7s)
Sep 15 12:21:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:21:12,597 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:21:12 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:21:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:21:27,919 main INFO screen MUSKRAT pass=0 dev=0.0 ins=5.64 pro=72 1a=False 1b=False 2=False (66.8s)
Sep 15 12:21:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:21:32,257 main INFO screen Cat pass=0 dev=0.0 ins=59.77 pro=64 1a=False 1b=False 2=True (64.2s)
Sep 15 12:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:22:06,853 main INFO screen OneBull pass=0 dev=0.0 ins=55.38 pro=11 1a=False 1b=False 2=True (57.4s)
Sep 15 12:22:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:22:23,133 main INFO screen 🎺 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.2s)
Sep 15 12:22:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:22:27,409 main INFO screen NIKOCAKE pass=0 dev=0.0 ins=79.26 pro=3 1a=False 1b=True 2=True (55.1s)
Sep 15 12:23:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:23:02,861 main INFO screen fomo pass=0 dev=0.0 ins=142.92 pro=0 1a=False 1b=False 2=True (56.0s)
Sep 15 12:23:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:23:30,447 main INFO screen assets pass=0 dev=0.0 ins=0.21 pro=4 1a=False 1b=False 2=False (63.0s)
Sep 15 12:23:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:23:36,955 main INFO screen $CLACT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.8s)
Sep 15 12:24:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:24:02,352 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.5s)
Sep 15 12:24:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:24:24,571 main INFO screen EYES pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.1s)
Sep 15 12:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:24:44,668 main INFO screen Distra pass=0 dev=0.0 ins=10.4 pro=54 1a=False 1b=False 2=False (67.7s)
Sep 15 12:25:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:25:04,358 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.0s)
Sep 15 12:25:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:25:24,468 main INFO screen CardiBtc pass=0 dev=0.0 ins=53.05 pro=49 1a=False 1b=False 2=True (59.9s)
Sep 15 12:25:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:25:45,283 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (60.6s)
Sep 15 12:26:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:26:12,452 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:26:12 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:26:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:26:17,977 main INFO screen pepevoice pass=0 dev=0.0 ins=30.82 pro=61 1a=False 1b=False 2=True (73.6s)
Sep 15 12:26:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:26:30,438 main INFO screen Rambo pass=0 dev=0.0 ins=42.26 pro=29 1a=False 1b=False 2=True (66.0s)
Sep 15 12:27:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:27:03,023 main INFO screen CASHCATA pass=0 dev=0.0 ins=77.29 pro=10 1a=False 1b=False 2=True (77.7s)
Sep 15 12:27:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:27:16,097 main INFO screen BALD pass=0 dev=0.0 ins=54.75 pro=20 1a=False 1b=False 2=True (58.1s)
Sep 15 12:27:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:27:20,168 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:12:27:20 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 12:27:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:27:40,960 main INFO screen Ape pass=0 dev=0.0 ins=32.65 pro=68 1a=False 1b=False 2=True (70.5s)
Sep 15 12:28:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:28:02,139 main INFO screen BRAINROT pass=0 dev=0.0 ins=23.85 pro=26 1a=False 1b=False 2=True (59.1s)
Sep 15 12:28:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:28:21,513 main INFO screen AMEOW pass=0 dev=0.0 ins=77.47 pro=2 1a=False 1b=True 2=True (65.4s)
Sep 15 12:28:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:28:37,747 main INFO screen ChillBike pass=0 dev=0.0 ins=68.53 pro=29 1a=False 1b=True 2=True (56.8s)
Sep 15 12:29:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:29:13,593 main INFO screen Gravity  pass=0 dev=0.02 ins=0.0 pro=6 1a=False 1b=False 2=False (71.5s)
Sep 15 12:29:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:29:32,549 main INFO screen BALD pass=0 dev=0.0 ins=58.64 pro=44 1a=False 1b=False 2=True (71.0s)
Sep 15 12:29:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:29:42,971 main INFO screen SOUNDPAD pass=0 dev=0.0 ins=31.81 pro=57 1a=False 1b=False 2=True (65.2s)
Sep 15 12:30:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:30:21,565 main INFO screen Trump pass=0 dev=0.0 ins=17.69 pro=57 1a=False 1b=False 2=False (68.0s)
Sep 15 12:30:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:30:31,361 main INFO screen RIRI pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (58.8s)
Sep 15 12:30:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:30:34,609 main INFO screen WOTF pass=0 dev=0.01 ins=120.06 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 15 12:31:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:31:12,400 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:31:12 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T11:15:54Z
--- update 2026-09-15T11:20:58Z
--- update 2026-09-15T11:25:58Z
--- update 2026-09-15T11:30:58Z
--- update 2026-09-15T11:35:58Z
--- update 2026-09-15T11:40:59Z
--- update 2026-09-15T11:45:59Z
--- update 2026-09-15T11:51:00Z
--- update 2026-09-15T11:56:01Z
nieuwe code: 8b410ac
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T12:01:07Z
Running as unit: schaduwbot-wallets.service; invocation ID: acccd1e31aaa474a8eb1e19774a93cf5
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T12:06:07Z
--- update 2026-09-15T12:11:07Z
--- update 2026-09-15T12:16:08Z
--- update 2026-09-15T12:21:11Z
--- update 2026-09-15T12:26:11Z
--- update 2026-09-15T12:31:11Z
```

## Analyses (laatste 40 regels)
```
active
10:21:52 klaar in 1276s: 6700 lopers, 40017 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/vamp.py 11:00:50
11:00:50 tokens lezen
11:00:55 133728 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
11:12:30 6749 lopers, 18 niet-onderscheidende woorden
11:13:34   500/6749 lopers, 4334 koppelingen
11:14:27   1000/6749 lopers, 7353 koppelingen
11:15:10   1500/6749 lopers, 11262 koppelingen
11:16:04   2000/6749 lopers, 15841 koppelingen
11:16:46   2500/6749 lopers, 18547 koppelingen
11:17:20   3000/6749 lopers, 21453 koppelingen
11:18:10   3500/6749 lopers, 25603 koppelingen
11:18:45   4000/6749 lopers, 28395 koppelingen
11:19:40   4500/6749 lopers, 32066 koppelingen
11:20:29   5000/6749 lopers, 35311 koppelingen
11:21:10   5500/6749 lopers, 38244 koppelingen
11:22:29   6000/6749 lopers, 44729 koppelingen
11:23:19   6500/6749 lopers, 48371 koppelingen
11:23:34 uitkomsten uit de trades halen
11:37:02 68207 tokens met een instapkoers
11:37:02 klaar in 2172s: 6749 lopers, 27371 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 11:37:02
--- /opt/schaduwbot/vamp.py 12:01:08
12:01:09 tokens lezen
12:01:13 134689 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
12:13:27 6807 lopers, 18 niet-onderscheidende woorden
12:14:29   500/6807 lopers, 4334 koppelingen
12:15:21   1000/6807 lopers, 7353 koppelingen
12:16:07   1500/6807 lopers, 11262 koppelingen
12:16:58   2000/6807 lopers, 15841 koppelingen
12:17:42   2500/6807 lopers, 18547 koppelingen
12:18:20   3000/6807 lopers, 21453 koppelingen
12:19:14   3500/6807 lopers, 25603 koppelingen
12:19:50   4000/6807 lopers, 28395 koppelingen
12:20:45   4500/6807 lopers, 32066 koppelingen
12:21:33   5000/6807 lopers, 35311 koppelingen
12:22:13   5500/6807 lopers, 38244 koppelingen
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
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
