# Schaduwbot status

- tijd: 2026-09-14 15:33:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 1 hour, 46 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.9G/38G | geheugen: 1909/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 118769, "tokens_in_memory": 6077, "msgs": 14542452, "trades": 3220657, "creates": 33059, "decode_fail": 270972, "rpc_calls": 97268, "rpc_errors": 7, "sol_usd": 101.93559558075614, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 15:07:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:07:53,040 main INFO screen COINBASE pass=1 dev=0.0 ins=1.14 pro=30 1a=False 1b=False 2=False (69.3s)
Sep 14 15:08:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:08:30,924 main INFO screen CLANKER pass=0 dev=0.0 ins=32.79 pro=41 1a=False 1b=False 2=True (58.3s)
Sep 14 15:08:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:08:45,831 main INFO screen HUMANIST pass=0 dev=0.0 ins=1.04 pro=49 1a=False 1b=False 2=True (57.7s)
Sep 14 15:08:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:08:48,927 main INFO screen Rolex pass=0 dev=0.0 ins=97.42 pro=1 1a=False 1b=False 2=True (55.9s)
Sep 14 15:09:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:09:31,153 main INFO screen UOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.2s)
Sep 14 15:09:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:09:56,231 main INFO screen Claude pass=0 dev=0.0 ins=95.36 pro=1 1a=False 1b=False 2=True (67.3s)
Sep 14 15:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:09:58,474 main INFO screen Cupsey pass=0 dev=0.0 ins=20.61 pro=74 1a=False 1b=False 2=True (72.6s)
Sep 14 15:10:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:10:32,325 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (61.2s)
Sep 14 15:10:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:10:53,514 main INFO screen Cupsey pass=0 dev=0.0 ins=0.84 pro=10 1a=False 1b=False 2=False (55.0s)
Sep 14 15:11:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:11:15,912 main INFO screen JUAN pass=0 dev=81.24 ins=0.0 pro=19 1a=False 1b=False 2=False (79.7s)
Sep 14 15:11:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:11:31,561 main INFO screen HEY pass=0 dev=0.0 ins=28.9 pro=26 1a=False 1b=False 2=True (59.2s)
Sep 14 15:11:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:11:56,819 main INFO screen WAH pass=0 dev=0.0 ins=32.84 pro=43 1a=False 1b=False 2=True (63.3s)
Sep 14 15:12:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:12:26,997 main INFO screen LIFE pass=0 dev=0.0 ins=31.82 pro=64 1a=False 1b=False 2=True (71.1s)
Sep 14 15:12:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:12:27,205 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:12:27 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 15:12:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:12:38,653 main INFO screen HUMAN pass=0 dev=0.0 ins=33.34 pro=47 1a=False 1b=False 2=True (67.1s)
Sep 14 15:13:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:13:01,112 main INFO screen Cooked pass=0 dev=0.0 ins=40.58 pro=80 1a=False 1b=False 2=True (64.3s)
Sep 14 15:13:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:13:29,040 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (62.0s)
Sep 14 15:13:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:13:37,417 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 14 15:13:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:13:58,222 main INFO screen Schwab pass=0 dev=0.0 ins=20.79 pro=36 1a=False 1b=False 2=False (57.1s)
Sep 14 15:14:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:14:25,537 main INFO screen COW pass=0 dev=0.0 ins=56.0 pro=14 1a=False 1b=False 2=True (56.5s)
Sep 14 15:14:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:14:36,435 main INFO screen $BIKECAT pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (59.0s)
Sep 14 15:15:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:15:07,130 main INFO screen SDOG pass=0 dev=0.0 ins=15.28 pro=64 1a=False 1b=False 2=True (68.9s)
Sep 14 15:15:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:15:19,900 main INFO screen MVN pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (54.4s)
Sep 14 15:15:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:15:48,299 main INFO screen sol pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (71.9s)
Sep 14 15:16:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:16:03,749 main INFO screen FAIR pass=0 dev=0.01 ins=130.42 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 14 15:16:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:16:28,774 main INFO screen DID pass=0 dev=0.0 ins=28.9 pro=27 1a=False 1b=False 2=True (68.9s)
Sep 14 15:16:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:16:48,336 main INFO screen BALD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 14 15:17:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:17:18,844 main INFO screen MUM pass=1 dev=2.97 ins=0.0 pro=13 1a=False 1b=False 2=False (75.1s)
Sep 14 15:17:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:17:22,970 main INFO screen bikecate pass=0 dev=0.0 ins=78.26 pro=0 1a=False 1b=True 2=True (54.2s)
Sep 14 15:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:17:28,269 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:17:28 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 15:17:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:17:47,535 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.2s)
Sep 14 15:18:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:18:17,915 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.9s)
Sep 14 15:18:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:18:18,675 main INFO screen HOBL pass=0 dev=0.0 ins=23.58 pro=19 1a=False 1b=False 2=True (59.8s)
Sep 14 15:18:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:18:55,568 main INFO screen TIMELESS pass=1 dev=0.85 ins=0.0 pro=46 1a=False 1b=False 2=False (68.0s)
Sep 14 15:19:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:19:15,503 main INFO screen Datavault  pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (57.6s)
Sep 14 15:19:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:19:18,807 main INFO screen $AURA pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (60.1s)
Sep 14 15:19:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:19:19,013 aiohttp.access INFO 103.253.145.18 [14/Sep/2026:15:19:19 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 15:19:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:19:54,599 main INFO screen FLY pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (59.0s)
Sep 14 15:20:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:20:23,087 main INFO screen Pro-Human pass=0 dev=0.0 ins=31.49 pro=54 1a=False 1b=False 2=True (67.6s)
Sep 14 15:20:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:20:31,952 main INFO screen JEFF pass=1 dev=0.0 ins=18.6 pro=29 1a=False 1b=False 2=False (73.1s)
Sep 14 15:21:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:21:00,868 main INFO screen NS pass=0 dev=0.0 ins=25.14 pro=74 1a=False 1b=False 2=True (66.3s)
Sep 14 15:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:21:20,455 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.4s)
Sep 14 15:21:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:21:32,373 main INFO screen rollindrit pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (60.4s)
Sep 14 15:22:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:22:00,485 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.6s)
Sep 14 15:22:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:22:34,993 main INFO screen fine pass=0 dev=0.0 ins=31.68 pro=63 1a=False 1b=False 2=True (74.5s)
Sep 14 15:22:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:22:37,205 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:22:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 15:22:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:22:45,185 main INFO screen SolLama pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (72.8s)
Sep 14 15:22:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:22:56,611 main INFO screen IQ pass=0 dev=0.02 ins=13.34 pro=75 1a=False 1b=False 2=True (56.1s)
Sep 14 15:23:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:23:35,536 main INFO screen MIND pass=0 dev=0.0 ins=27.11 pro=19 1a=False 1b=False 2=False (60.5s)
Sep 14 15:23:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:23:45,947 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 14 15:23:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:23:52,388 main INFO screen McMuffin pass=0 dev=0.0 ins=20.38 pro=54 1a=False 1b=False 2=True (55.8s)
Sep 14 15:24:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:24:46,908 main INFO screen Obsidian pass=1 dev=0.0 ins=11.38 pro=48 1a=False 1b=False 2=False (71.4s)
Sep 14 15:24:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:24:57,958 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.0s)
Sep 14 15:25:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:25:06,973 main INFO screen McMuffin pass=0 dev=0.0 ins=25.15 pro=66 1a=False 1b=False 2=True (74.6s)
Sep 14 15:25:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:25:48,269 main INFO screen TRASH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.4s)
Sep 14 15:26:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:26:05,332 main INFO screen CAD pass=0 dev=0.0 ins=11.51 pro=38 1a=False 1b=False 2=True (67.4s)
Sep 14 15:26:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:26:10,792 main INFO screen BIKESEM pass=0 dev=0.0 ins=38.45 pro=28 1a=False 1b=False 2=True (63.8s)
Sep 14 15:26:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:26:43,491 main INFO screen TREY pass=0 dev=0.0 ins=9.76 pro=22 1a=False 1b=False 2=True (55.2s)
Sep 14 15:27:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:27:05,345 main INFO screen GOOGINK pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (60.0s)
Sep 14 15:27:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:27:22,900 main INFO screen ☉ pass=1 dev=0.0 ins=17.84 pro=25 1a=False 1b=False 2=False (72.1s)
Sep 14 15:28:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:28:01,315 main INFO screen Grandpa pass=1 dev=0.0 ins=1.44 pro=41 1a=False 1b=False 2=False (77.8s)
Sep 14 15:28:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:28:10,724 main INFO screen PACMAN pass=0 dev=0.0 ins=20.38 pro=56 1a=False 1b=False 2=True (65.4s)
Sep 14 15:28:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:28:11,844 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:28:11 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 15:28:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:28:27,371 main INFO screen Eldonfuck pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.5s)
Sep 14 15:28:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:28:53,530 main INFO screen CORINE pass=0 dev=0.0 ins=42.97 pro=4 1a=False 1b=False 2=True (52.2s)
Sep 14 15:29:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:29:22,582 main INFO screen Dpump pass=1 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (71.9s)
Sep 14 15:29:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:29:27,342 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.0s)
Sep 14 15:29:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:29:51,986 main INFO screen BMW pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 14 15:30:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:30:33,169 main INFO screen NOVO pass=1 dev=0.0 ins=2.94 pro=43 1a=False 1b=False 2=False (70.6s)
Sep 14 15:30:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:30:40,051 main INFO screen CITYBOY pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (72.7s)
Sep 14 15:31:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:31:04,411 main INFO screen HABIBI pass=0 dev=3.2 ins=70.54 pro=9 1a=False 1b=False 2=True (72.4s)
Sep 14 15:31:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:31:17,362 aiohttp.access INFO 129.212.227.207 [14/Sep/2026:15:31:17 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 15:31:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:31:24,335 main INFO screen LOFIGIRL pass=0 dev=0.0 ins=15.72 pro=17 1a=False 1b=False 2=True (51.2s)
Sep 14 15:31:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:31:38,581 main INFO screen LOFI pass=0 dev=0.0 ins=38.71 pro=70 1a=False 1b=True 2=True (58.5s)
Sep 14 15:32:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:32:01,872 main INFO screen GOOSE pass=0 dev=0.0 ins=35.79 pro=27 1a=False 1b=False 2=True (57.5s)
Sep 14 15:32:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:32:20,644 main INFO screen DVLT pass=0 dev=0.0 ins=142.27 pro=1 1a=False 1b=False 2=True (56.3s)
Sep 14 15:32:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:32:36,378 main INFO screen OYXS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.8s)
Sep 14 15:32:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:32:59,373 main INFO screen ANAI pass=0 dev=6.63 ins=72.68 pro=1 1a=False 1b=True 2=True (57.5s)
Sep 14 15:33:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:33:16,474 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.8s)
Sep 14 15:33:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:33:37,220 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:33:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T13:55:06Z
--- update 2026-09-14T14:00:15Z
--- update 2026-09-14T14:05:29Z
--- update 2026-09-14T14:10:36Z
--- update 2026-09-14T14:15:44Z
--- update 2026-09-14T14:20:58Z
--- update 2026-09-14T14:26:20Z
--- update 2026-09-14T14:31:36Z
--- update 2026-09-14T14:36:47Z
--- update 2026-09-14T14:41:57Z
--- update 2026-09-14T14:46:58Z
--- update 2026-09-14T14:52:05Z
--- update 2026-09-14T14:57:10Z
--- update 2026-09-14T15:02:12Z
--- update 2026-09-14T15:07:12Z
--- update 2026-09-14T15:12:26Z
--- update 2026-09-14T15:17:27Z
--- update 2026-09-14T15:22:36Z
--- update 2026-09-14T15:28:10Z
--- update 2026-09-14T15:33:36Z
```

## Analyses (laatste 25 regels)
```
inactive
14:26:46   34000 tokens, 3433257 trades, 422988 posities (204s)
14:26:59   36000 tokens, 3651216 trades, 449494 posities (217s)
14:27:11   38000 tokens, 3855373 trades, 477025 posities (229s)
14:27:22   40000 tokens, 4058288 trades, 500003 posities (240s)
14:27:32   42000 tokens, 4231179 trades, 518624 posities (250s)
14:27:44   44000 tokens, 4431591 trades, 543117 posities (262s)
14:27:55   46000 tokens, 4628449 trades, 569121 posities (273s)
14:28:08   48000 tokens, 4835951 trades, 592426 posities (286s)
14:28:21   50000 tokens, 5042483 trades, 617257 posities (299s)
14:28:34   52000 tokens, 5232943 trades, 639976 posities (312s)
14:28:45   54000 tokens, 5400820 trades, 656278 posities (323s)
14:28:58   56000 tokens, 5607778 trades, 682670 posities (336s)
14:29:10   58000 tokens, 5779171 trades, 702483 posities (348s)
14:29:25   60000 tokens, 5995263 trades, 731299 posities (363s)
14:29:38   62000 tokens, 6195128 trades, 760023 posities (376s)
14:29:52   64000 tokens, 6409063 trades, 789743 posities (390s)
14:30:05   66000 tokens, 6613290 trades, 815749 posities (403s)
14:30:18   68000 tokens, 6815336 trades, 844682 posities (416s)
14:30:32   70000 tokens, 7014350 trades, 880257 posities (430s)
14:30:42 posities: 898781 uit 7156509 trades (444s)
14:30:55 201106 wallets gerekend
14:30:56 geluk-toets
14:31:33 persistentie
14:31:36 kopieer-simulatie
14:33:43 klaar in 625s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
14:36:51 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:41:57 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:46:58 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:52:09 ijk: +1 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:57:11 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
15:02:13 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
15:07:12 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
15:12:29 ijk: +1 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
15:17:27 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
15:22:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
15:28:11 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
15:33:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
