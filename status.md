# Schaduwbot status

- tijd: 2026-09-15 13:16:46 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 23 hours, 29 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.2G/38G | geheugen: 2327/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 196958, "tokens_in_memory": 6460, "msgs": 28189638, "trades": 5903344, "creates": 63048, "decode_fail": 490647, "rpc_calls": 175052, "rpc_errors": 15, "sol_usd": 101.01908068270208, "open_positions": 39, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 12:51:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:51:26,046 main INFO screen CLARITY pass=0 dev=0.0 ins=43.01 pro=5 1a=False 1b=False 2=True (45.7s)
Sep 15 12:52:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:52:21,883 main INFO screen DOSE pass=0 dev=0.0 ins=14.58 pro=65 1a=False 1b=False 2=False (73.9s)
Sep 15 12:52:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:52:26,496 main INFO screen MAX pass=0 dev=0.0 ins=21.47 pro=72 1a=False 1b=False 2=True (68.9s)
Sep 15 12:52:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:52:29,423 main INFO screen IVKA pass=0 dev=41.19 ins=0.15 pro=2 1a=False 1b=False 2=False (63.4s)
Sep 15 12:53:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:53:15,873 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.0s)
Sep 15 12:53:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:53:29,660 main INFO screen Beyond  pass=0 dev=8.01 ins=0.0 pro=18 1a=False 1b=False 2=False (63.2s)
Sep 15 12:53:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:53:30,836 main INFO screen bitch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.4s)
Sep 15 12:54:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:54:12,638 main INFO screen Jackhammer pass=0 dev=0.0 ins=68.76 pro=19 1a=False 1b=True 2=True (56.8s)
Sep 15 12:54:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:54:38,428 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (67.6s)
Sep 15 12:54:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:54:40,300 main INFO screen O'SEAL pass=0 dev=28.21 ins=0.0 pro=18 1a=False 1b=False 2=False (70.6s)
Sep 15 12:55:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:55:08,020 main INFO screen BIKEW pass=0 dev=0.0 ins=79.26 pro=2 1a=False 1b=True 2=True (55.4s)
Sep 15 12:55:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:55:42,342 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.9s)
Sep 15 12:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:55:43,684 main INFO screen SOUNDPAD pass=0 dev=0.0 ins=35.0 pro=63 1a=False 1b=False 2=True (63.4s)
Sep 15 12:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:56:01,848 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (53.8s)
Sep 15 12:56:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:56:13,952 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:12:56:13 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 12:56:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:56:45,711 main INFO screen Value pass=0 dev=0.0 ins=20.36 pro=2 1a=False 1b=False 2=True (62.0s)
Sep 15 12:56:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:56:47,166 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.8s)
Sep 15 12:56:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:56:53,938 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.1s)
Sep 15 12:57:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:57:34,180 aiohttp.access INFO 94.154.43.250 [15/Sep/2026:12:57:34 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 12:57:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:57:49,511 main INFO screen NITROGOD pass=0 dev=0.0 ins=0.88 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 15 12:57:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:57:51,006 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (65.3s)
Sep 15 12:57:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:57:54,078 main INFO screen WOTF pass=0 dev=0.04 ins=43.73 pro=1 1a=False 1b=False 2=True (60.1s)
Sep 15 12:58:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:58:43,765 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 15 12:58:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:58:58,516 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (64.4s)
Sep 15 12:59:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:59:00,251 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.7s)
Sep 15 12:59:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 12:59:44,206 main INFO screen ☉ pass=0 dev=0.0 ins=20.09 pro=3 1a=False 1b=False 2=False (60.4s)
Sep 15 13:00:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:00:07,483 main INFO screen HOUSEHOLD pass=0 dev=0.0 ins=9.36 pro=78 1a=False 1b=False 2=True (69.0s)
Sep 15 13:00:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:00:10,346 main INFO screen SCRIBE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.1s)
Sep 15 13:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:00:50,927 main INFO screen GRIMACE pass=0 dev=0.0 ins=20.87 pro=6 1a=False 1b=False 2=True (66.7s)
Sep 15 13:01:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:01:12,662 main INFO screen INU BOT pass=0 dev=0.16 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 15 13:01:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:01:14,591 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (67.1s)
Sep 15 13:01:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:01:37,627 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:01:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:01:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:01:42,407 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.5s)
Sep 15 13:02:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:02:19,959 main INFO screen bracat pass=0 dev=0.0 ins=0.0 pro=54 1a=False 1b=False 2=False (65.4s)
Sep 15 13:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:02:21,930 main INFO screen ELON pass=0 dev=0.0 ins=19.61 pro=3 1a=False 1b=False 2=False (69.3s)
Sep 15 13:02:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:02:46,556 main INFO screen max pass=0 dev=0.0 ins=22.72 pro=62 1a=False 1b=False 2=False (64.1s)
Sep 15 13:03:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:03:13,140 main INFO screen SCRIBECAT pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (53.2s)
Sep 15 13:03:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:03:24,702 main INFO screen SOUNDPAD pass=0 dev=0.0 ins=40.46 pro=68 1a=False 1b=False 2=True (62.8s)
Sep 15 13:03:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:03:44,343 main INFO screen Jeetless pass=0 dev=0.0 ins=28.75 pro=59 1a=False 1b=False 2=True (57.8s)
Sep 15 13:04:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:04:20,945 main INFO screen reaction pass=0 dev=0.0 ins=3.09 pro=36 1a=False 1b=False 2=False (67.8s)
Sep 15 13:04:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:04:28,966 main INFO screen bulltrack pass=0 dev=0.0 ins=0.0 pro=52 1a=False 1b=False 2=False (64.3s)
Sep 15 13:04:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:04:52,118 main INFO screen PEPE27 pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (67.8s)
Sep 15 13:05:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:05:19,775 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (58.8s)
Sep 15 13:05:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:05:28,816 main INFO screen weave pass=0 dev=0.0 ins=28.09 pro=60 1a=False 1b=False 2=True (59.8s)
Sep 15 13:05:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:05:45,474 main INFO screen MASK pass=0 dev=0.0 ins=0.24 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 15 13:06:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:06:18,811 main INFO screen WBG pass=0 dev=0.0 ins=26.61 pro=30 1a=False 1b=False 2=False (50.0s)
Sep 15 13:06:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:06:22,878 main INFO screen Boombox pass=0 dev=0.0 ins=26.29 pro=66 1a=False 1b=False 2=True (63.1s)
Sep 15 13:06:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:06:32,466 main INFO screen Google pass=0 dev=0.0 ins=141.34 pro=1 1a=False 1b=False 2=True (47.0s)
Sep 15 13:06:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:06:37,138 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:06:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:07:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:07:07,959 main INFO screen YOUTUBALE pass=0 dev=0.0 ins=79.26 pro=3 1a=False 1b=True 2=True (49.1s)
Sep 15 13:07:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:07:26,965 main INFO screen Flycat pass=0 dev=0.0 ins=14.58 pro=57 1a=False 1b=False 2=False (64.1s)
Sep 15 13:07:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:07:36,017 main INFO screen BOOM pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=False 2=True (63.5s)
Sep 15 13:07:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:07:58,948 main INFO screen RST pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (51.0s)
Sep 15 13:08:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:08:36,654 main INFO screen River pass=0 dev=0.0 ins=35.77 pro=77 1a=False 1b=False 2=True (69.7s)
Sep 15 13:08:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:08:38,117 main INFO screen RACECAR pass=0 dev=0.0 ins=21.62 pro=3 1a=False 1b=False 2=True (62.1s)
Sep 15 13:08:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:08:53,416 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.5s)
Sep 15 13:09:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:09:31,577 main INFO screen WBG pass=0 dev=0.0 ins=21.28 pro=81 1a=False 1b=False 2=True (53.5s)
Sep 15 13:09:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:09:41,115 main INFO screen DOOB pass=0 dev=0.04 ins=0.0 pro=6 1a=False 1b=False 2=False (64.5s)
Sep 15 13:09:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:09:43,552 main INFO screen korn pass=0 dev=4.05 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 15 13:10:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:10:22,904 main INFO screen LIMES pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (51.3s)
Sep 15 13:10:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:10:40,793 main INFO screen CATANA pass=0 dev=0.0 ins=0.47 pro=21 1a=False 1b=False 2=False (57.2s)
Sep 15 13:10:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:10:50,394 main INFO screen PUGY pass=0 dev=0.25 ins=0.0 pro=14 1a=False 1b=False 2=False (69.3s)
Sep 15 13:11:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:11:18,755 main INFO screen CHONK pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (55.8s)
Sep 15 13:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:11:37,197 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:11:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:11:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:11:51,922 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (71.1s)
Sep 15 13:11:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:11:55,244 main INFO screen KIBA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (64.8s)
Sep 15 13:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:12:20,489 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (61.7s)
Sep 15 13:13:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:13:03,432 main INFO screen LEBULL pass=0 dev=56.08 ins=0.0 pro=17 1a=False 1b=False 2=False (71.5s)
Sep 15 13:13:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:13:04,031 main INFO screen ROBOELON pass=0 dev=0.0 ins=20.83 pro=12 1a=False 1b=False 2=False (68.8s)
Sep 15 13:13:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:13:15,490 main INFO screen CharliCork pass=0 dev=0.0 ins=68.51 pro=12 1a=False 1b=True 2=True (55.0s)
Sep 15 13:14:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:14:15,340 main INFO screen CCOIN pass=0 dev=0.0 ins=27.85 pro=70 1a=False 1b=False 2=True (71.3s)
Sep 15 13:14:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:14:20,928 main INFO screen DOOB pass=0 dev=0.35 ins=0.0 pro=13 1a=False 1b=False 2=False (77.5s)
Sep 15 13:14:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:14:25,836 main INFO screen PepeCoin pass=0 dev=0.0 ins=20.08 pro=7 1a=False 1b=False 2=True (70.3s)
Sep 15 13:15:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:15:29,122 main INFO screen HedgeHog pass=0 dev=0.0 ins=20.75 pro=3 1a=False 1b=False 2=False (73.8s)
Sep 15 13:15:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:15:32,432 main INFO screen CLASH pass=0 dev=0.0 ins=46.81 pro=70 1a=False 1b=False 2=True (71.5s)
Sep 15 13:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:15:37,064 main INFO screen XRPP pass=0 dev=39.4 ins=0.01 pro=6 1a=False 1b=False 2=False (71.2s)
Sep 15 13:16:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:16:15,483 main INFO screen STAR pass=0 dev=0.0 ins=0.17 pro=2 1a=False 1b=False 2=False (46.4s)
Sep 15 13:16:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:16:25,419 main INFO screen HEDGIE pass=0 dev=0.0 ins=19.23 pro=4 1a=False 1b=False 2=False (53.0s)
Sep 15 13:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:16:29,366 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (52.3s)
Sep 15 13:16:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:16:46,079 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:16:46 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T12:06:07Z
--- update 2026-09-15T12:11:07Z
--- update 2026-09-15T12:16:08Z
--- update 2026-09-15T12:21:11Z
--- update 2026-09-15T12:26:11Z
--- update 2026-09-15T12:31:11Z
--- update 2026-09-15T12:36:11Z
--- update 2026-09-15T12:41:11Z
--- update 2026-09-15T12:46:11Z
--- update 2026-09-15T12:51:12Z
--- update 2026-09-15T12:56:12Z
--- update 2026-09-15T13:01:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7ff017f4c1e54aaebf060b943fa4342a
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T13:06:35Z
--- update 2026-09-15T13:11:36Z
--- update 2026-09-15T13:16:44Z
nieuwe code: caa47fa
alleen analyses/documentatie gewijzigd: geen herstart
```

## Analyses (laatste 40 regels)
```
active
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
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
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
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
