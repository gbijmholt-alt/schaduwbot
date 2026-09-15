# Schaduwbot status

- tijd: 2026-09-15 16:33:26 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 2 hours, 46 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.3G/38G | geheugen: 3622/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 208758, "tokens_in_memory": 8543, "msgs": 30675400, "trades": 6434459, "creates": 68526, "decode_fail": 547071, "rpc_calls": 186984, "rpc_errors": 15, "sol_usd": 99.1345480617948, "open_positions": 82, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 16:09:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:04,053 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (56.9s)
Sep 15 16:09:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:32,773 main INFO screen MIGHTFLY pass=0 dev=0.0 ins=52.29 pro=16 1a=True 1b=False 2=True (54.2s)
Sep 15 16:09:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:47,124 main INFO screen PONK pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (57.7s)
Sep 15 16:09:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:51,261 main INFO screen MIGHTFLY pass=0 dev=0.0 ins=24.16 pro=1 1a=False 1b=False 2=False (47.2s)
Sep 15 16:10:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:28,510 main INFO screen PONS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 16:10:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:41,182 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (54.1s)
Sep 15 16:10:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:44,083 main INFO screen DIP pass=0 dev=0.0 ins=34.81 pro=13 1a=False 1b=False 2=True (52.8s)
Sep 15 16:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:37,774 main INFO screen Neuro pass=0 dev=0.0 ins=10.26 pro=64 1a=False 1b=False 2=False (69.3s)
Sep 15 16:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:43,679 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (59.6s)
Sep 15 16:11:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:46,758 main INFO screen Neuro pass=0 dev=0.0 ins=17.72 pro=49 1a=False 1b=False 2=False (65.6s)
Sep 15 16:12:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:33,291 main INFO screen ORCA pass=0 dev=0.0 ins=48.56 pro=6 1a=False 1b=False 2=True (55.5s)
Sep 15 16:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:46,147 main INFO screen PricedIn pass=0 dev=0.0 ins=18.74 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 15 16:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:49,271 main INFO screen taxless pass=0 dev=0.0 ins=45.07 pro=24 1a=False 1b=False 2=True (65.6s)
Sep 15 16:13:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:13:21,795 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:13:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:13:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:13:27,017 main INFO screen GM pass=0 dev=0.0 ins=40.0 pro=6 1a=False 1b=False 2=True (53.7s)
Sep 15 16:13:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:13:39,077 main INFO screen XPXGOLD pass=0 dev=0.0 ins=135.23 pro=1 1a=False 1b=False 2=True (52.9s)
Sep 15 16:13:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:13:52,695 main INFO screen HAMSTER pass=0 dev=0.0 ins=29.75 pro=69 1a=False 1b=False 2=True (63.4s)
Sep 15 16:14:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:14:14,856 main INFO screen taxless pass=0 dev=0.0 ins=18.62 pro=12 1a=False 1b=False 2=False (47.8s)
Sep 15 16:14:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:14:38,577 main INFO screen JENSENHUH pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (59.5s)
Sep 15 16:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:14:51,497 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (58.8s)
Sep 15 16:15:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:15:04,779 main INFO screen taxless pass=0 dev=0.0 ins=22.7 pro=31 1a=False 1b=False 2=True (49.9s)
Sep 15 16:15:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:15:38,530 main INFO screen DIAMOND pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.0s)
Sep 15 16:15:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:15:46,413 main INFO screen PETIFY pass=0 dev=0.0 ins=47.53 pro=12 1a=False 1b=False 2=True (54.9s)
Sep 15 16:15:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:15:59,484 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 15 16:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:16:33,123 main INFO screen FATPEPE pass=0 dev=0.0 ins=34.81 pro=31 1a=False 1b=False 2=True (54.6s)
Sep 15 16:16:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:16:55,093 main INFO screen SENGI pass=0 dev=0.0 ins=69.33 pro=67 1a=False 1b=False 2=True (68.7s)
Sep 15 16:17:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:17:01,822 main INFO screen Pepecap! pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (62.3s)
Sep 15 16:17:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:17:41,950 main INFO screen lol pass=0 dev=0.0 ins=56.59 pro=21 1a=False 1b=False 2=True (68.8s)
Sep 15 16:17:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:17:50,683 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.6s)
Sep 15 16:18:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:18:11,342 main INFO screen Dodge pass=0 dev=0.0 ins=37.24 pro=37 1a=False 1b=False 2=True (69.5s)
Sep 15 16:18:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:18:22,858 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:18:22 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:18:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:18:30,600 main INFO screen Brud pass=0 dev=0.0 ins=27.55 pro=48 1a=False 1b=False 2=True (48.6s)
Sep 15 16:18:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:18:48,810 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (58.1s)
Sep 15 16:19:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:19:16,687 main INFO screen osc pass=0 dev=0.0 ins=0.24 pro=25 1a=False 1b=False 2=False (65.3s)
Sep 15 16:19:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:19:24,152 main INFO screen TRENCHROT pass=0 dev=0.0 ins=28.53 pro=53 1a=False 1b=False 2=True (53.6s)
Sep 15 16:19:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:19:44,634 main INFO screen FLY pass=0 dev=0.0 ins=37.58 pro=16 1a=True 1b=False 2=True (55.8s)
Sep 15 16:20:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:20:15,861 main INFO screen Dodge pass=0 dev=0.0 ins=28.12 pro=15 1a=True 1b=False 2=True (59.2s)
Sep 15 16:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:20:18,229 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.1s)
Sep 15 16:20:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:20:37,982 main INFO screen 4D pass=0 dev=0.0 ins=37.23 pro=28 1a=False 1b=False 2=True (53.3s)
Sep 15 16:21:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:21:04,086 main INFO screen Bread pass=0 dev=0.0 ins=42.36 pro=38 1a=False 1b=False 2=True (45.9s)
Sep 15 16:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:21:10,733 main INFO screen MEMESCOPE pass=0 dev=0.0 ins=47.68 pro=19 1a=False 1b=False 2=True (54.9s)
Sep 15 16:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:21:34,893 main INFO screen wind pass=0 dev=2.15 ins=0.0 pro=1 1a=False 1b=False 2=False (56.9s)
Sep 15 16:22:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:22:14,028 main INFO screen FART pass=0 dev=0.0 ins=0.0 pro=57 1a=False 1b=False 2=False (69.9s)
Sep 15 16:22:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:22:18,291 main INFO screen DOGMOB pass=0 dev=0.0 ins=33.77 pro=16 1a=False 1b=False 2=True (67.6s)
Sep 15 16:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:22:31,821 main INFO screen pen pass=0 dev=0.0 ins=18.91 pro=1 1a=False 1b=False 2=False (56.9s)
Sep 15 16:23:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:23:18,830 main INFO screen ratcoin pass=0 dev=0.0 ins=12.44 pro=69 1a=False 1b=False 2=False (64.8s)
Sep 15 16:23:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:23:22,712 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:23:22 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:23:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:23:26,698 main INFO screen STAMPYDOG pass=0 dev=0.0 ins=7.13 pro=55 1a=False 1b=False 2=False (68.4s)
Sep 15 16:23:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:23:32,761 main INFO screen $FROCKET pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=True (60.9s)
Sep 15 16:24:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:24:13,380 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.5s)
Sep 15 16:24:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:24:13,575 main INFO screen Credit pass=0 dev=0.0 ins=19.67 pro=7 1a=False 1b=False 2=False (46.9s)
Sep 15 16:24:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:24:27,520 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.8s)
Sep 15 16:25:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:25:20,503 main INFO screen Gadsden pass=0 dev=0.0 ins=37.6 pro=60 1a=False 1b=False 2=True (67.1s)
Sep 15 16:25:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:25:26,606 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.0s)
Sep 15 16:25:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:25:41,326 main INFO screen LEAFYWIF pass=0 dev=0.04 ins=0.0 pro=46 1a=False 1b=False 2=False (73.8s)
Sep 15 16:26:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:26:18,415 main INFO screen Xo1o pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.9s)
Sep 15 16:26:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:26:20,058 main INFO screen RACCOONGPT pass=0 dev=0.0 ins=39.35 pro=2 1a=False 1b=False 2=True (53.5s)
Sep 15 16:26:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:26:51,028 main INFO screen SMS pass=0 dev=0.58 ins=35.44 pro=48 1a=False 1b=False 2=True (69.7s)
Sep 15 16:27:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:27:26,849 main INFO screen superdark pass=0 dev=0.0 ins=17.91 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 15 16:27:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:27:32,249 main INFO screen CHAD pass=0 dev=0.0 ins=0.88 pro=6 1a=False 1b=False 2=False (73.8s)
Sep 15 16:27:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:27:55,615 main INFO screen FOOL pass=0 dev=0.0 ins=24.17 pro=68 1a=False 1b=False 2=True (64.6s)
Sep 15 16:28:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:28:00,616 aiohttp.access INFO 200.34.244.43 [15/Sep/2026:16:28:00 +0000] "UNKNOWN / HTTP/1.0" 400 229 "-" "-"
Sep 15 16:28:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:28:24,540 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:28:24 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:28:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:28:38,902 main INFO screen AEYE pass=0 dev=0.0 ins=20.66 pro=5 1a=False 1b=False 2=False (66.7s)
Sep 15 16:28:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:28:47,733 main INFO screen Gadsden pass=0 dev=0.0 ins=37.23 pro=46 1a=False 1b=False 2=True (80.9s)
Sep 15 16:28:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:28:56,117 main INFO screen PepeCap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.5s)
Sep 15 16:29:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:29:40,505 main INFO screen HAMM pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (61.6s)
Sep 15 16:29:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:29:42,958 main INFO screen Floor pass=0 dev=0.0 ins=45.29 pro=24 1a=False 1b=False 2=True (55.2s)
Sep 15 16:29:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:29:53,316 main INFO screen Floor pass=0 dev=0.0 ins=59.91 pro=15 1a=True 1b=False 2=True (57.2s)
Sep 15 16:30:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:30:34,477 main INFO screen FF pass=0 dev=0.0 ins=17.17 pro=17 1a=False 1b=False 2=True (51.5s)
Sep 15 16:30:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:30:46,545 main INFO screen STAMPYCAT pass=0 dev=0.0 ins=0.0 pro=54 1a=False 1b=False 2=False (66.0s)
Sep 15 16:31:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:31:06,071 main INFO screen CHAD pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.8s)
Sep 15 16:31:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:31:24,037 main INFO screen Launchpad pass=0 dev=0.0 ins=34.42 pro=43 1a=False 1b=False 2=True (49.6s)
Sep 15 16:31:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:31:41,827 main INFO screen err0r pass=0 dev=0.0 ins=28.65 pro=6 1a=False 1b=False 2=True (55.3s)
Sep 15 16:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:32:05,627 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.6s)
Sep 15 16:32:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:32:21,274 main INFO screen CHAD pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (57.2s)
Sep 15 16:32:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:32:37,855 main INFO screen UP pass=0 dev=0.0 ins=48.45 pro=25 1a=False 1b=False 2=True (56.0s)
Sep 15 16:33:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:33:02,692 main INFO screen Moolah pass=0 dev=0.0 ins=56.89 pro=26 1a=False 1b=False 2=True (57.1s)
Sep 15 16:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:33:17,065 main INFO screen OIL2 pass=0 dev=5.09 ins=0.0 pro=15 1a=False 1b=False 2=False (55.8s)
Sep 15 16:33:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:33:26,124 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:33:26 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T15:07:36Z
--- update 2026-09-15T15:12:37Z
--- update 2026-09-15T15:17:36Z
--- update 2026-09-15T15:22:38Z
--- update 2026-09-15T15:27:40Z
--- update 2026-09-15T15:32:40Z
--- update 2026-09-15T15:37:40Z
--- update 2026-09-15T15:42:42Z
--- update 2026-09-15T15:47:43Z
--- update 2026-09-15T15:52:44Z
--- update 2026-09-15T15:57:45Z
--- update 2026-09-15T16:03:18Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1702f0d8babc48c590b11e6b42957c29
analyses gestart (0f687558a2d6)
--- update 2026-09-15T16:08:19Z
--- update 2026-09-15T16:13:20Z
--- update 2026-09-15T16:18:21Z
--- update 2026-09-15T16:23:21Z
--- update 2026-09-15T16:28:23Z
--- update 2026-09-15T16:33:24Z
```

## Analyses (laatste 40 regels)
```
active
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
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
--- /opt/schaduwbot/vamp.py 13:01:37
13:01:37 tokens lezen
13:01:41 135941 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
13:13:51 6879 lopers, 19 niet-onderscheidende woorden
13:14:53   500/6879 lopers, 4294 koppelingen
13:15:46   1000/6879 lopers, 7299 koppelingen
13:16:30   1500/6879 lopers, 11181 koppelingen
13:17:20   2000/6879 lopers, 15724 koppelingen
13:18:02   2500/6879 lopers, 18375 koppelingen
13:18:35   3000/6879 lopers, 21263 koppelingen
13:19:25   3500/6879 lopers, 25366 koppelingen
13:19:59   4000/6879 lopers, 28115 koppelingen
13:20:55   4500/6879 lopers, 31747 koppelingen
13:21:39   5000/6879 lopers, 34889 koppelingen
13:22:16   5500/6879 lopers, 37799 koppelingen
13:23:41   6000/6879 lopers, 44142 koppelingen
13:24:27   6500/6879 lopers, 47629 koppelingen
13:24:50 uitkomsten uit de trades halen
13:38:33 69698 tokens met een instapkoers
13:38:34 klaar in 2217s: 6879 lopers, 27676 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 13:38:34
--- /opt/schaduwbot/video_replay.py 14:02:16
--- /opt/schaduwbot/video_replay.py 15:02:36
--- /opt/schaduwbot/video_replay.py 16:03:19
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
14:02:52 ijk: +6 van 14 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=238 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
14:02:53 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 14/45/160 | al gemeten: 637
15:03:01 ijk: +4 van 4 kandidaten (4 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=240 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
15:03:02 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 4/34/158 | al gemeten: 641
16:03:54 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=246 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
16:03:55 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 12/35/164 | al gemeten: 647
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
