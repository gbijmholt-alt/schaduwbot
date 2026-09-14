# Schaduwbot status

- tijd: 2026-09-14 23:14:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 9 hours, 27 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.5G/38G | geheugen: 2206/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 146429, "tokens_in_memory": 11282, "msgs": 21425313, "trades": 4416063, "creates": 47075, "decode_fail": 391605, "rpc_calls": 124776, "rpc_errors": 12, "sol_usd": 102.74865314348966, "open_positions": 93, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 22:50:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:50:21,410 main INFO screen emilyblunt pass=0 dev=0.0 ins=4.2 pro=74 1a=False 1b=False 2=True (64.9s)
Sep 14 22:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:50:46,935 main INFO screen FUSION pass=0 dev=0.0 ins=44.26 pro=12 1a=False 1b=True 2=False (55.6s)
Sep 14 22:51:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:51:02,375 main INFO screen VEST pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.0s)
Sep 14 22:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:51:13,744 main INFO screen GILF pass=0 dev=0.0 ins=24.99 pro=60 1a=False 1b=False 2=False (52.3s)
Sep 14 22:51:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:51:38,575 main INFO screen gay$ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 14 22:52:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:52:07,893 main INFO screen Dihval pass=0 dev=0.0 ins=33.87 pro=63 1a=False 1b=False 2=True (65.5s)
Sep 14 22:52:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:52:11,615 main INFO screen USGR pass=0 dev=0.0 ins=130.85 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 14 22:52:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:52:33,022 main INFO screen Orangie pass=0 dev=0.0 ins=14.35 pro=71 1a=False 1b=False 2=False (54.4s)
Sep 14 22:52:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:52:57,730 main INFO screen IPO pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (49.8s)
Sep 14 22:53:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:53:13,790 main INFO screen GAKE pass=0 dev=0.0 ins=4.45 pro=20 1a=False 1b=False 2=False (62.2s)
Sep 14 22:53:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:53:31,939 main INFO screen Gondola pass=0 dev=0.0 ins=11.71 pro=3 1a=False 1b=False 2=False (58.9s)
Sep 14 22:53:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:53:44,259 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:53:44 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:53:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:53:51,446 main INFO screen Stewart pass=0 dev=0.0 ins=45.16 pro=24 1a=False 1b=False 2=True (53.7s)
Sep 14 22:54:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:54:19,648 main INFO screen biketroll pass=0 dev=0.0 ins=46.69 pro=20 1a=False 1b=False 2=True (65.9s)
Sep 14 22:54:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:54:21,076 main INFO screen VEST pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (49.1s)
Sep 14 22:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:54:55,877 main INFO screen MVP pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (64.4s)
Sep 14 22:55:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:55:06,924 main INFO screen WOFI pass=0 dev=0.79 ins=37.51 pro=1 1a=False 1b=False 2=True (47.3s)
Sep 14 22:55:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:55:14,944 main INFO screen rasmr pass=0 dev=0.0 ins=22.15 pro=53 1a=False 1b=False 2=True (53.9s)
Sep 14 22:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:55:43,014 main INFO screen Hoax pass=0 dev=0.0 ins=36.6 pro=9 1a=False 1b=False 2=True (47.1s)
Sep 14 22:56:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:56:00,757 main INFO screen ROCKET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 14 22:56:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:56:15,597 main INFO screen DAH pass=0 dev=0.0 ins=18.89 pro=58 1a=False 1b=False 2=True (60.7s)
Sep 14 22:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:56:33,979 main INFO screen Dihli pass=0 dev=0.0 ins=15.32 pro=58 1a=False 1b=False 2=False (51.0s)
Sep 14 22:56:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:56:55,538 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.8s)
Sep 14 22:57:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:57:07,706 main INFO screen Toebiden pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (52.1s)
Sep 14 22:57:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:57:29,641 main INFO screen FUSION pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 14 22:57:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:57:46,052 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.5s)
Sep 14 22:58:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:58:02,599 main INFO screen frogrogan pass=0 dev=0.0 ins=15.32 pro=61 1a=False 1b=False 2=False (54.9s)
Sep 14 22:58:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:58:21,210 main INFO screen PEPTOSHI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (51.6s)
Sep 14 22:58:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:58:37,292 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.2s)
Sep 14 22:58:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:58:55,024 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.4s)
Sep 14 22:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:59:06,354 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:59:06 +0000] "GET /health HTTP/1.1" 200 511 "-" "Python-urllib/3.14"
Sep 14 22:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:59:16,143 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.9s)
Sep 14 22:59:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:59:27,579 main INFO screen FARM pass=0 dev=0.0 ins=38.64 pro=55 1a=False 1b=False 2=True (50.3s)
Sep 14 22:59:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:59:48,602 main INFO screen toely pass=0 dev=0.0 ins=40.92 pro=77 1a=False 1b=False 2=True (53.6s)
Sep 14 23:00:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:00:16,142 main INFO screen ANDREW pass=0 dev=0.0 ins=50.05 pro=12 1a=False 1b=False 2=True (60.0s)
Sep 14 23:00:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:00:32,737 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.2s)
Sep 14 23:00:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:00:43,014 main INFO screen WOFI pass=0 dev=0.0 ins=123.97 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 14 23:01:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:01:23,470 main INFO screen spork pass=0 dev=0.0 ins=36.86 pro=56 1a=False 1b=False 2=True (67.3s)
Sep 14 23:01:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:01:33,594 main INFO screen FROG pass=0 dev=0.0 ins=0.0 pro=53 1a=False 1b=False 2=False (60.9s)
Sep 14 23:01:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:01:40,693 main INFO screen GRUMBLE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 14 23:02:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:02:20,754 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.3s)
Sep 14 23:02:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:02:31,866 main INFO screen VOID pass=0 dev=0.0 ins=0.01 pro=10 1a=False 1b=False 2=True (58.3s)
Sep 14 23:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:02:50,536 main INFO screen DUDE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.8s)
Sep 14 23:03:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:03:21,053 main INFO screen MANGO⁠ pass=0 dev=0.0 ins=10.35 pro=6 1a=False 1b=False 2=False (60.3s)
Sep 14 23:03:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:03:30,049 main INFO screen SEMIHARD pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (58.2s)
Sep 14 23:03:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:03:41,810 main INFO screen spork pass=0 dev=0.0 ins=36.86 pro=68 1a=False 1b=False 2=True (51.3s)
Sep 14 23:04:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:04:18,472 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:04:18 +0000] "GET /health HTTP/1.1" 200 511 "-" "Python-urllib/3.14"
Sep 14 23:04:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:04:25,610 main INFO screen Toerogan pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (55.6s)
Sep 14 23:04:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:04:34,443 main INFO screen pepetide pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.6s)
Sep 14 23:04:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:04:34,835 main INFO screen CODO pass=0 dev=54.77 ins=0.0 pro=15 1a=False 1b=False 2=False (73.8s)
Sep 14 23:05:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:05:21,642 main INFO screen SEMIHARD pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (47.2s)
Sep 14 23:05:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:05:21,670 main INFO screen spork pass=0 dev=0.0 ins=31.27 pro=16 1a=False 1b=False 2=True (56.1s)
Sep 14 23:05:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:05:43,069 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (68.2s)
Sep 14 23:06:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:06:19,973 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 14 23:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:06:29,580 main INFO screen TRUCE pass=0 dev=0.0 ins=26.85 pro=25 1a=False 1b=False 2=True (67.9s)
Sep 14 23:06:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:06:58,936 main INFO screen BIFROST pass=0 dev=0.0 ins=50.35 pro=61 1a=False 1b=False 2=True (75.9s)
Sep 14 23:07:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:07:26,132 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.2s)
Sep 14 23:07:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:07:35,442 main INFO screen Nirvana pass=0 dev=0.0 ins=16.67 pro=34 1a=False 1b=False 2=True (65.9s)
Sep 14 23:08:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:08:08,465 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (69.5s)
Sep 14 23:08:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:08:21,824 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.7s)
Sep 14 23:08:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:08:48,212 main INFO screen Khalifas  pass=0 dev=0.0 ins=6.22 pro=37 1a=False 1b=False 2=False (72.8s)
Sep 14 23:09:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:09:18,464 main INFO screen DRAKE pass=0 dev=0.0 ins=22.36 pro=41 1a=False 1b=False 2=False (70.0s)
Sep 14 23:09:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:09:22,046 main INFO screen SEMIHARD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.2s)
Sep 14 23:09:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:09:28,490 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:09:28 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 23:09:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:09:57,067 main INFO screen Nirvana pass=0 dev=0.0 ins=10.12 pro=1 1a=False 1b=False 2=False (68.9s)
Sep 14 23:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:10:16,276 main INFO screen NTDA pass=0 dev=0.0 ins=431.73 pro=1 1a=False 1b=False 2=True (57.8s)
Sep 14 23:10:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:10:21,989 main INFO screen BMW pass=0 dev=0.0 ins=140.75 pro=0 1a=False 1b=False 2=True (59.9s)
Sep 14 23:10:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:10:54,922 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.9s)
Sep 14 23:11:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:11:10,290 main INFO screen €OUPS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.0s)
Sep 14 23:11:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:11:14,205 main INFO screen toeken pass=0 dev=0.0 ins=19.57 pro=27 1a=False 1b=False 2=True (52.2s)
Sep 14 23:11:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:11:41,139 main INFO screen SEMIHARD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (46.2s)
Sep 14 23:12:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:12:09,993 main INFO screen HAGE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.7s)
Sep 14 23:12:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:12:21,923 main INFO screen DICAPY pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (67.7s)
Sep 14 23:12:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:12:38,236 main INFO screen KINU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.1s)
Sep 14 23:13:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:13:06,416 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (56.4s)
Sep 14 23:13:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:13:18,554 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 14 23:13:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:13:44,544 main INFO screen fun pass=0 dev=0.0 ins=16.11 pro=21 1a=False 1b=False 2=False (66.3s)
Sep 14 23:14:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:14:09,384 main INFO screen BIFROST pass=0 dev=0.0 ins=43.98 pro=1 1a=False 1b=False 2=True (63.0s)
Sep 14 23:14:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:14:16,495 main INFO screen AdamSandr pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=False 2=True (57.9s)
Sep 14 23:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:14:37,283 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:14:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T21:45:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5eee46075898481b8005cdd132a55989
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T21:50:36Z
--- update 2026-09-14T21:55:44Z
--- update 2026-09-14T22:01:30Z
--- update 2026-09-14T22:06:35Z
--- update 2026-09-14T22:11:36Z
--- update 2026-09-14T22:16:38Z
--- update 2026-09-14T22:22:15Z
--- update 2026-09-14T22:27:36Z
--- update 2026-09-14T22:32:54Z
--- update 2026-09-14T22:37:58Z
--- update 2026-09-14T22:43:01Z
--- update 2026-09-14T22:48:36Z
--- update 2026-09-14T22:53:43Z
--- update 2026-09-14T22:59:05Z
--- update 2026-09-14T23:04:17Z
--- update 2026-09-14T23:09:27Z
--- update 2026-09-14T23:14:36Z
```

## Analyses (laatste 25 regels)
```
inactive
22:22:35   38000 tokens, 3709788 trades, 448598 posities (250s)
22:22:50   40000 tokens, 3900481 trades, 473390 posities (264s)
22:23:04   42000 tokens, 4086379 trades, 492462 posities (278s)
22:23:17   44000 tokens, 4260028 trades, 515191 posities (291s)
22:23:30   46000 tokens, 4445005 trades, 537426 posities (305s)
22:23:44   48000 tokens, 4620265 trades, 558280 posities (319s)
22:23:59   50000 tokens, 4822700 trades, 580896 posities (334s)
22:24:14   52000 tokens, 5032898 trades, 607308 posities (349s)
22:24:28   54000 tokens, 5221391 trades, 629728 posities (363s)
22:24:42   56000 tokens, 5390312 trades, 650213 posities (377s)
22:24:58   58000 tokens, 5581326 trades, 674058 posities (393s)
22:25:12   60000 tokens, 5766236 trades, 695878 posities (407s)
22:25:27   62000 tokens, 5971487 trades, 721683 posities (422s)
22:25:40   64000 tokens, 6162947 trades, 750238 posities (435s)
22:25:55   66000 tokens, 6381573 trades, 779020 posities (450s)
22:26:08   68000 tokens, 6564687 trades, 802231 posities (463s)
22:26:23   70000 tokens, 6758719 trades, 827352 posities (478s)
22:26:37   72000 tokens, 6950951 trades, 853949 posities (492s)
22:26:52   74000 tokens, 7146187 trades, 885103 posities (506s)
22:26:56 posities: 891065 uit 7198322 trades (512s)
22:27:09 209874 wallets gerekend
22:27:10 geluk-toets
22:27:44 persistentie
22:27:47 kopieer-simulatie
22:30:19 klaar in 715s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
22:43:02 ijk: +0 van 0 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=14 -> nog 1 metingen binnen 5 minuten na de migratie te gaan
22:43:02 ijk-diagnose: nieuwste migratie 6.1 min oud | migraties 15/60/240 min: 8/38/180 | al gemeten: 277
22:48:54 ijk: +6 van 7 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=18 -> mediane afwijking 96% boven 25% binnen 5 minuten na de migratie
22:48:54 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 13/41/182 | al gemeten: 283
22:53:54 ijk: +4 van 4 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=21 -> mediane afwijking 97% boven 25% binnen 5 minuten na de migratie
22:53:55 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 10/40/184 | al gemeten: 287
22:59:17 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=25 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
22:59:17 ijk-diagnose: nieuwste migratie 2.1 min oud | migraties 15/60/240 min: 11/43/182 | al gemeten: 291
23:04:26 ijk: +3 van 3 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=27 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:04:26 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 10/45/179 | al gemeten: 294
23:09:33 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=29 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:09:33 ijk-diagnose: nieuwste migratie 4.2 min oud | migraties 15/60/240 min: 9/44/177 | al gemeten: 296
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
