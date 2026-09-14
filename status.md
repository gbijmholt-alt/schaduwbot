# Schaduwbot status

- tijd: 2026-09-14 16:25:19 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 2 hours, 38 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.9G/38G | geheugen: 2008/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 121871, "tokens_in_memory": 6540, "msgs": 15273634, "trades": 3344207, "creates": 34270, "decode_fail": 284142, "rpc_calls": 100421, "rpc_errors": 7, "sol_usd": 102.69728228962693, "open_positions": 119, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 15:59:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:59:35,811 main INFO screen bikebaton pass=0 dev=0.46 ins=73.17 pro=8 1a=False 1b=True 2=True (54.3s)
Sep 14 15:59:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:59:37,520 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:15:59:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 15:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:59:59,140 main INFO screen TEST pass=1 dev=0.0 ins=11.6 pro=83 1a=False 1b=False 2=False (65.0s)
Sep 14 15:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 15:59:59,705 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.3s)
Sep 14 16:00:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:00:36,001 main INFO screen HAI pass=0 dev=0.0 ins=47.08 pro=51 1a=False 1b=False 2=True (60.2s)
Sep 14 16:01:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:01:07,922 main INFO screen TH3000 pass=0 dev=0.0 ins=19.69 pro=48 1a=False 1b=False 2=True (68.2s)
Sep 14 16:01:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:01:13,532 main INFO screen MARLEY pass=0 dev=4.45 ins=0.0 pro=9 1a=False 1b=False 2=False (74.4s)
Sep 14 16:01:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:01:51,678 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (75.7s)
Sep 14 16:02:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:02:07,381 main INFO screen buywhy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 14 16:02:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:02:20,108 main INFO screen fone pass=0 dev=0.0 ins=30.39 pro=64 1a=False 1b=False 2=True (66.6s)
Sep 14 16:02:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:02:49,818 main INFO screen BIKESEM pass=0 dev=17.84 ins=16.26 pro=18 1a=False 1b=True 2=False (58.1s)
Sep 14 16:03:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:03:05,869 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 14 16:03:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:03:18,135 main INFO screen OMG pass=0 dev=0.0 ins=26.6 pro=30 1a=False 1b=True 2=True (58.0s)
Sep 14 16:03:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:03:46,696 main INFO screen HAI pass=0 dev=0.0 ins=20.11 pro=7 1a=False 1b=False 2=False (56.9s)
Sep 14 16:03:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:03:54,915 main INFO screen fone pass=0 dev=0.0 ins=20.59 pro=25 1a=False 1b=False 2=False (49.0s)
Sep 14 16:04:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:04:14,203 main INFO screen TTWIN pass=0 dev=0.0 ins=9.45 pro=56 1a=False 1b=False 2=True (56.1s)
Sep 14 16:04:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:04:36,528 main INFO screen WHEEL TYSON pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (49.8s)
Sep 14 16:04:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:04:43,047 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:04:43 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 16:04:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:04:47,764 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.8s)
Sep 14 16:05:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:05:19,815 main INFO screen LuxoBench pass=1 dev=0.0 ins=18.99 pro=33 1a=False 1b=False 2=False (65.6s)
Sep 14 16:05:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:05:28,733 main INFO screen Tripad pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 14 16:05:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:05:38,758 main INFO screen Samsung pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (51.0s)
Sep 14 16:06:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:06:11,978 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.2s)
Sep 14 16:06:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:06:19,095 main INFO screen survive pass=0 dev=0.0 ins=50.18 pro=17 1a=False 1b=False 2=True (50.4s)
Sep 14 16:06:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:06:30,474 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 16:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:07:19,893 main INFO screen RISE pass=0 dev=53.0 ins=0.94 pro=5 1a=False 1b=False 2=True (67.9s)
Sep 14 16:07:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:07:24,513 main INFO screen TWIN pass=1 dev=0.0 ins=2.54 pro=53 1a=False 1b=False 2=False (65.4s)
Sep 14 16:07:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:07:44,101 main INFO screen TRAVIS pass=0 dev=0.0 ins=19.38 pro=67 1a=False 1b=False 2=True (73.6s)
Sep 14 16:08:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:08:13,596 main INFO screen BIKESEM pass=0 dev=0.0 ins=37.17 pro=32 1a=False 1b=False 2=True (53.7s)
Sep 14 16:08:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:08:26,289 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 14 16:08:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:08:47,256 main INFO screen TRICAT pass=1 dev=0.0 ins=10.39 pro=75 1a=False 1b=False 2=False (63.2s)
Sep 14 16:09:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:09:19,741 main INFO screen $GOAT pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.1s)
Sep 14 16:09:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:09:30,745 main INFO screen SPOOK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.5s)
Sep 14 16:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:09:44,818 main INFO screen LEAGUE pass=1 dev=0.47 ins=0.0 pro=23 1a=False 1b=False 2=False (57.6s)
Sep 14 16:09:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:09:47,630 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:09:47 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 16:10:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:10:17,610 main INFO screen random pass=0 dev=0.0 ins=35.3 pro=54 1a=False 1b=False 2=True (57.9s)
Sep 14 16:10:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:10:25,013 main INFO screen $DONALD pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (54.3s)
Sep 14 16:10:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:10:38,681 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 14 16:11:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:11:12,286 main INFO screen XuBo pass=0 dev=0.0 ins=24.25 pro=65 1a=False 1b=False 2=True (54.7s)
Sep 14 16:11:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:11:33,736 main INFO screen Aware pass=1 dev=3.79 ins=12.08 pro=33 1a=False 1b=False 2=False (68.7s)
Sep 14 16:11:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:11:39,110 main INFO screen TWIN pass=1 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (60.4s)
Sep 14 16:12:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:12:19,360 main INFO screen FRITZ pass=0 dev=0.0 ins=16.9 pro=8 1a=False 1b=False 2=True (67.1s)
Sep 14 16:12:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:12:30,988 main INFO screen XuBo pass=1 dev=0.0 ins=19.44 pro=22 1a=False 1b=False 2=False (51.9s)
Sep 14 16:12:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:12:33,341 main INFO screen Black Pearl pass=0 dev=0.0 ins=12.54 pro=40 1a=False 1b=False 2=True (59.6s)
Sep 14 16:13:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:13:16,684 main INFO screen SLOPNET pass=0 dev=0.0 ins=47.66 pro=13 1a=False 1b=False 2=True (57.3s)
Sep 14 16:13:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:13:24,128 main INFO screen Twin pass=0 dev=0.0 ins=18.76 pro=24 1a=False 1b=False 2=True (53.1s)
Sep 14 16:13:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:13:30,259 main INFO screen Supercycle pass=0 dev=0.0 ins=31.93 pro=44 1a=False 1b=False 2=True (56.9s)
Sep 14 16:14:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:14:17,293 main INFO screen $GTA6 pass=1 dev=0.0 ins=1.04 pro=11 1a=False 1b=False 2=False (60.6s)
Sep 14 16:14:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:14:34,331 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.1s)
Sep 14 16:14:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:14:36,308 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.2s)
Sep 14 16:14:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:14:47,524 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:14:47 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 16:15:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:15:24,778 main INFO screen Sibai pass=0 dev=0.0 ins=29.09 pro=63 1a=False 1b=False 2=True (67.5s)
Sep 14 16:15:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:15:52,987 main INFO screen Orangutan pass=0 dev=0.0 ins=20.7 pro=45 1a=False 1b=False 2=True (76.7s)
Sep 14 16:15:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:15:54,161 main INFO screen dd pass=0 dev=0.22 ins=0.0 pro=4 1a=False 1b=False 2=False (79.8s)
Sep 14 16:16:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:16:40,574 main INFO screen HedgeHog pass=1 dev=0.0 ins=19.89 pro=22 1a=False 1b=False 2=False (75.8s)
Sep 14 16:16:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:16:49,325 main INFO screen PauseAI pass=0 dev=0.0 ins=39.72 pro=45 1a=False 1b=False 2=True (55.2s)
Sep 14 16:17:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:17:04,917 main INFO screen bradpit pass=1 dev=0.0 ins=14.84 pro=62 1a=False 1b=False 2=False (71.9s)
Sep 14 16:17:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:17:51,094 main INFO screen Orangutan pass=0 dev=0.0 ins=13.19 pro=56 1a=False 1b=False 2=True (70.5s)
Sep 14 16:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:18:00,182 main INFO screen Duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.3s)
Sep 14 16:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:18:00,551 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 14 16:19:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:05,392 main INFO screen $GOLD pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (74.3s)
Sep 14 16:19:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:06,933 main INFO screen KERALAM pass=0 dev=0.0 ins=42.35 pro=38 1a=False 1b=False 2=True (66.8s)
Sep 14 16:19:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:14,763 main INFO screen /what_if pass=0 dev=0.0 ins=27.13 pro=64 1a=False 1b=False 2=True (74.2s)
Sep 14 16:19:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:51,183 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:19:51 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 16:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:55,304 main INFO screen /what_if pass=0 dev=0.0 ins=39.22 pro=18 1a=False 1b=False 2=True (48.4s)
Sep 14 16:20:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:04,441 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 14 16:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:16,069 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.3s)
Sep 14 16:20:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:46,584 main INFO screen BMW pass=0 dev=0.0 ins=138.39 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 14 16:20:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:57,781 main INFO screen Cody pass=1 dev=0.0 ins=19.84 pro=21 1a=False 1b=False 2=False (53.3s)
Sep 14 16:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:21:20,777 main INFO screen Sage pass=0 dev=0.0 ins=8.13 pro=63 1a=False 1b=False 2=True (64.7s)
Sep 14 16:22:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:01,355 main INFO screen BIGTITYCO pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.8s)
Sep 14 16:22:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:14,127 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.3s)
Sep 14 16:22:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:25,156 main INFO screen chrisbrocc pass=0 dev=0.07 ins=79.2 pro=1 1a=False 1b=True 2=True (64.4s)
Sep 14 16:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:17,338 main INFO screen Cody pass=0 dev=0.0 ins=20.1 pro=28 1a=False 1b=False 2=True (76.0s)
Sep 14 16:23:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:21,228 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.1s)
Sep 14 16:23:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:24,170 main INFO screen Emil pass=0 dev=0.0 ins=18.32 pro=28 1a=False 1b=False 2=True (59.0s)
Sep 14 16:24:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:16,897 main INFO screen HOGEY pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (59.6s)
Sep 14 16:24:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:22,757 main INFO screen GOLDGOOSE pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (61.5s)
Sep 14 16:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:35,895 main INFO screen FOMO pass=0 dev=79.31 ins=79.31 pro=0 1a=False 1b=False 2=True (71.7s)
Sep 14 16:25:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:25:19,111 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:25:19 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T14:57:10Z
--- update 2026-09-14T15:02:12Z
--- update 2026-09-14T15:07:12Z
--- update 2026-09-14T15:12:26Z
--- update 2026-09-14T15:17:27Z
--- update 2026-09-14T15:22:36Z
--- update 2026-09-14T15:28:10Z
--- update 2026-09-14T15:33:36Z
--- update 2026-09-14T15:38:40Z
--- update 2026-09-14T15:43:41Z
--- update 2026-09-14T15:48:53Z
--- update 2026-09-14T15:54:27Z
Running as unit: schaduwbot-wallets.service; invocation ID: bb9b36ab53964518996f9300eff1d4cf
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T15:59:36Z
--- update 2026-09-14T16:04:41Z
--- update 2026-09-14T16:09:46Z
--- update 2026-09-14T16:14:46Z
--- update 2026-09-14T16:19:50Z
--- update 2026-09-14T16:25:17Z
```

## Analyses (laatste 25 regels)
```
active
14:30:42 posities: 898781 uit 7156509 trades (444s)
14:30:55 201106 wallets gerekend
14:30:56 geluk-toets
14:31:33 persistentie
14:31:36 kopieer-simulatie
14:33:43 klaar in 625s -> /opt/schaduwbot/reports/wallets.md
15:54:28 81889 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
15:54:52   ingelezen tot rowid 8775292 (200000 rijen, 200000 bruikbaar)
15:54:57   ingelezen tot rowid 8835965 (260673 rijen, 260673 bruikbaar)
15:54:58 ingelezen: 260673 nieuwe trades, 260673 bruikbaar (31s)
15:57:22 3000 aankopen van gevolgde wallets geëvalueerd
15:57:49 vroege kopers: 246 voldoen nu, register 428, 392 tokens beoordeeld
15:58:23 grote spelers: saldo van 1231 wallets opgehaald
15:58:49 herkomst: 40 posities gekoppeld
15:58:59 klaar in 272s -> /opt/schaduwbot/reports/ledger.md
16:08:57 S1: gezakt — toets n=20912, verkennend n=14656
16:08:57 klaar in 598s -> /opt/schaduwbot/reports/hypotheses.md
16:08:58 probe: 150 transacties ophalen
16:12:18 poolveld: 11 pools bekeken, 0 te gaan -> vastgesteld @43
16:13:31 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
16:13:31 prijsijk: n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:13:32 na-migratie: 100 paren te checken
16:15:44 na-migratie: 86 paren, 19 prijzen
16:20:56 gemigreerde koersen: 106 gedaan, 1417 te gaan
16:20:57 klaar (715 rpc-calls, 34 fouten)
```

## IJking poolkoers (laatste 12 regels)
```
sqlite3.OperationalError: database is locked
Traceback (most recent call last):
  File "/opt/schaduwbot/pumpswap.py", line 1183, in <module>
    main()
    ~~~~^^
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
16:19:51 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
