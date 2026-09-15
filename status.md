# Schaduwbot status

- tijd: 2026-09-15 21:30:05 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 7 hours, 43 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.7G/38G | geheugen: 2381/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 226558, "tokens_in_memory": 10878, "msgs": 36899068, "trades": 7298774, "creates": 77275, "decode_fail": 613353, "rpc_calls": 205380, "rpc_errors": 17, "sol_usd": 96.66230250600462, "open_positions": 132, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 21:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:05:22,165 main INFO screen IYKYK pass=0 dev=0.0 ins=25.02 pro=64 1a=False 1b=False 2=True (70.7s)
Sep 15 21:05:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:05:46,562 main INFO screen LV pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (54.5s)
Sep 15 21:06:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:06:25,514 main INFO screen CLARITY pass=0 dev=0.0 ins=20.96 pro=60 1a=False 1b=False 2=True (63.3s)
Sep 15 21:06:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:06:26,895 main INFO screen CRYING pass=0 dev=0.0 ins=24.18 pro=3 1a=False 1b=False 2=False (66.1s)
Sep 15 21:06:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:06:49,070 main INFO screen mem pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (62.5s)
Sep 15 21:07:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:07:15,153 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (49.6s)
Sep 15 21:07:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:07:31,771 main INFO screen $MOOD pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (64.9s)
Sep 15 21:07:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:07:36,971 main INFO screen CLARITY pass=0 dev=0.0 ins=34.97 pro=52 1a=False 1b=False 2=True (47.9s)
Sep 15 21:08:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:08:22,937 main INFO screen NAY pass=0 dev=0.0 ins=26.98 pro=62 1a=False 1b=False 2=True (67.8s)
Sep 15 21:08:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:08:43,068 main INFO screen COIN pass=0 dev=0.0 ins=27.75 pro=70 1a=False 1b=False 2=True (71.3s)
Sep 15 21:08:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:08:44,505 main INFO screen SOB pass=0 dev=0.0 ins=20.68 pro=57 1a=False 1b=False 2=True (67.5s)
Sep 15 21:09:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:09:19,185 main INFO screen Solana pass=0 dev=5.43 ins=0.0 pro=8 1a=False 1b=False 2=False (56.2s)
Sep 15 21:09:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:09:31,198 main INFO screen YEA pass=0 dev=0.0 ins=28.92 pro=37 1a=False 1b=False 2=True (46.7s)
Sep 15 21:09:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:09:35,208 main INFO screen NAY pass=0 dev=0.0 ins=36.12 pro=38 1a=False 1b=False 2=True (52.1s)
Sep 15 21:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:09:36,694 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:09:36 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:10:16,729 main INFO screen KETO pass=0 dev=0.0 ins=31.84 pro=21 1a=False 1b=False 2=True (57.5s)
Sep 15 21:10:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:10:37,016 main INFO screen Sol pass=0 dev=0.0 ins=24.42 pro=1 1a=False 1b=False 2=True (65.8s)
Sep 15 21:10:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:10:41,396 main INFO screen v1be pass=0 dev=0.0 ins=61.49 pro=52 1a=False 1b=False 2=True (66.2s)
Sep 15 21:11:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:11:22,981 main INFO screen Over pass=0 dev=0.0 ins=21.15 pro=24 1a=False 1b=False 2=False (66.2s)
Sep 15 21:11:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:11:48,062 main INFO screen CCOIN pass=0 dev=0.0 ins=38.96 pro=81 1a=False 1b=False 2=True (66.7s)
Sep 15 21:11:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:11:52,732 main INFO screen WORTHLESS pass=0 dev=0.0 ins=2.87 pro=68 1a=False 1b=False 2=True (75.7s)
Sep 15 21:12:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:12:27,298 main INFO screen STUMP pass=0 dev=0.0 ins=77.57 pro=3 1a=False 1b=True 2=True (64.3s)
Sep 15 21:12:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:12:45,602 main INFO screen LION pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.5s)
Sep 15 21:12:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:12:51,862 main INFO screen CCOIN pass=0 dev=0.0 ins=40.9 pro=70 1a=False 1b=False 2=True (59.1s)
Sep 15 21:13:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:13:15,639 main INFO screen CCOIN pass=0 dev=0.0 ins=34.71 pro=57 1a=False 1b=False 2=True (48.3s)
Sep 15 21:13:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:13:41,473 main INFO screen Fire  pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.9s)
Sep 15 21:13:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:13:58,087 main INFO screen DOOM pass=0 dev=0.0 ins=53.81 pro=49 1a=False 1b=False 2=True (66.2s)
Sep 15 21:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:14:27,084 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (71.4s)
Sep 15 21:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:14:37,449 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:14:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:14:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:14:58,050 main INFO screen NOTHING pass=0 dev=0.0 ins=16.62 pro=53 1a=False 1b=False 2=True (76.6s)
Sep 15 21:14:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:14:58,291 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.2s)
Sep 15 21:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:15:37,397 main INFO screen feralfox pass=0 dev=0.0 ins=24.37 pro=43 1a=False 1b=False 2=True (70.3s)
Sep 15 21:16:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:16:03,685 main INFO screen page pass=0 dev=0.0 ins=9.78 pro=53 1a=False 1b=False 2=False (65.6s)
Sep 15 21:16:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:16:05,252 main INFO screen NEH pass=0 dev=0.0 ins=26.3 pro=43 1a=False 1b=False 2=True (67.0s)
Sep 15 21:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:16:31,079 main INFO screen GOLDENARRO pass=0 dev=0.0 ins=136.23 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 15 21:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:17:15,096 main INFO screen CRYPTO pass=0 dev=0.0 ins=32.33 pro=73 1a=False 1b=False 2=True (71.4s)
Sep 15 21:17:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:17:18,998 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.7s)
Sep 15 21:17:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:17:23,626 main INFO screen CRYPTO pass=0 dev=0.0 ins=22.59 pro=63 1a=False 1b=False 2=True (52.5s)
Sep 15 21:17:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:17:55,900 aiohttp.access INFO 216.126.239.185 [15/Sep/2026:21:17:55 +0000] "GET / HTTP/1.0" 404 174 "-" "zern-scanner (+https://zern.io)"
Sep 15 21:18:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:18:02,868 main INFO screen confused pass=0 dev=0.0 ins=38.16 pro=16 1a=False 1b=False 2=True (47.8s)
Sep 15 21:18:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:18:04,531 aiohttp.access INFO 216.126.239.185 [15/Sep/2026:21:18:04 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 21:18:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:18:12,970 main INFO screen CRYPTO pass=0 dev=0.0 ins=30.39 pro=32 1a=False 1b=False 2=True (54.0s)
Sep 15 21:18:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:18:32,389 main INFO screen ALLSMALL pass=0 dev=3.42 ins=17.08 pro=65 1a=False 1b=False 2=True (68.8s)
Sep 15 21:19:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:19:00,571 main INFO screen ber pass=0 dev=0.0 ins=29.61 pro=22 1a=False 1b=False 2=True (47.6s)
Sep 15 21:19:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:19:01,957 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.1s)
Sep 15 21:19:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:19:37,316 main INFO screen Back pass=0 dev=0.0 ins=17.88 pro=51 1a=False 1b=False 2=True (64.9s)
Sep 15 21:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:19:38,576 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:19:38 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 21:20:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:20:05,335 main INFO screen HUHDOG pass=0 dev=0.0 ins=36.25 pro=22 1a=False 1b=False 2=True (63.4s)
Sep 15 21:20:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:20:06,773 main INFO screen DIP pass=0 dev=0.0 ins=18.43 pro=55 1a=False 1b=False 2=True (66.2s)
Sep 15 21:20:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:20:35,783 main INFO screen CCCOIN pass=0 dev=0.0 ins=4.35 pro=28 1a=False 1b=False 2=False (58.5s)
Sep 15 21:21:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:21:19,332 main INFO screen $100X pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (74.0s)
Sep 15 21:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:21:20,601 main INFO screen KIP pass=0 dev=0.0 ins=31.74 pro=64 1a=False 1b=False 2=True (73.8s)
Sep 15 21:21:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:21:25,214 aiohttp.access INFO 62.171.146.116 [15/Sep/2026:21:21:25 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 21:21:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:21:28,183 main INFO screen WOFI pass=0 dev=0.0 ins=128.66 pro=1 1a=False 1b=False 2=True (52.4s)
Sep 15 21:22:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:22:09,550 main INFO screen Clarity pass=0 dev=0.0 ins=27.43 pro=47 1a=False 1b=False 2=True (50.2s)
Sep 15 21:22:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:22:27,036 main INFO screen DOnPlump pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.4s)
Sep 15 21:22:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:22:30,592 main INFO screen WAGIE pass=0 dev=0.0 ins=8.87 pro=37 1a=False 1b=False 2=True (62.4s)
Sep 15 21:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:23:17,473 main INFO screen FYOUWARREN pass=0 dev=0.0 ins=37.34 pro=69 1a=False 1b=False 2=True (67.9s)
Sep 15 21:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:23:33,625 main INFO screen FYOUWARREN pass=0 dev=0.0 ins=24.2 pro=2 1a=False 1b=False 2=False (66.6s)
Sep 15 21:23:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:23:34,956 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=24.45 pro=74 1a=False 1b=False 2=True (64.4s)
Sep 15 21:24:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:24:24,607 main INFO screen CROWN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.0s)
Sep 15 21:24:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:24:29,385 main INFO screen FINE pass=0 dev=0.0 ins=46.96 pro=69 1a=False 1b=False 2=True (71.9s)
Sep 15 21:24:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:24:39,506 main INFO screen STABLE pass=0 dev=0.0 ins=1.13 pro=16 1a=False 1b=False 2=False (64.5s)
Sep 15 21:25:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:25:03,701 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:25:03 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:25:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:25:34,211 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.6s)
Sep 15 21:25:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:25:35,727 main INFO screen DOGE2 pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (66.3s)
Sep 15 21:25:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:25:41,098 main INFO screen $MOONCOIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.6s)
Sep 15 21:26:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:26:24,188 main INFO screen SpaceTortious pass=0 dev=0.0 ins=35.91 pro=28 1a=False 1b=False 2=True (48.5s)
Sep 15 21:26:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:26:26,571 main INFO screen STRATEGY pass=0 dev=0.0 ins=13.19 pro=57 1a=False 1b=False 2=False (52.4s)
Sep 15 21:26:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:26:45,129 main INFO screen SpaceTortoise pass=0 dev=0.0 ins=12.62 pro=43 1a=False 1b=False 2=True (64.0s)
Sep 15 21:27:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:27:17,586 main INFO screen GCAPY pass=0 dev=1.44 ins=0.0 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 15 21:27:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:27:27,098 main INFO screen SpaceTortious pass=0 dev=0.0 ins=24.51 pro=0 1a=False 1b=False 2=False (60.5s)
Sep 15 21:27:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:27:33,233 main INFO screen RED pass=0 dev=0.0 ins=34.95 pro=25 1a=False 1b=False 2=True (48.1s)
Sep 15 21:28:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:28:08,798 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.2s)
Sep 15 21:28:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:28:31,384 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.3s)
Sep 15 21:28:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:28:33,330 main INFO screen OVER pass=0 dev=0.0 ins=34.88 pro=55 1a=False 1b=False 2=True (60.1s)
Sep 15 21:29:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:29:11,293 main INFO screen 𝓟𝓛 pass=0 dev=0.0 ins=15.1 pro=12 1a=False 1b=False 2=False (62.5s)
Sep 15 21:29:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:29:41,487 main INFO screen Psyopcat pass=0 dev=0.0 ins=31.18 pro=69 1a=False 1b=False 2=True (68.2s)
Sep 15 21:29:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:29:42,794 main INFO screen katie pass=0 dev=0.0 ins=36.01 pro=36 1a=False 1b=False 2=True (71.4s)
Sep 15 21:30:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:30:05,705 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:30:05 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 5a26243331f64387869dcc88488d69a0
analyses gestart (84579ff37485)
--- update 2026-09-15T20:13:08Z
--- update 2026-09-15T20:18:13Z
--- update 2026-09-15T20:23:16Z
--- update 2026-09-15T20:28:20Z
--- update 2026-09-15T20:33:25Z
--- update 2026-09-15T20:38:25Z
--- update 2026-09-15T20:43:36Z
--- update 2026-09-15T20:48:53Z
--- update 2026-09-15T20:54:01Z
--- update 2026-09-15T20:59:05Z
--- update 2026-09-15T21:04:26Z
--- update 2026-09-15T21:09:35Z
Running as unit: schaduwbot-wallets.service; invocation ID: 816305a7ccbb460db17cb3d4a36ce786
analyses gestart (84579ff37485)
--- update 2026-09-15T21:14:36Z
--- update 2026-09-15T21:19:37Z
--- update 2026-09-15T21:25:02Z
--- update 2026-09-15T21:30:04Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 18:04:11
18:04:12 venster 2026-09-13 06:04 UTC .. nu, 67852 tokens
18:05:01 klaar in 50s: 51584 tokens, 1905 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 19:05:57
19:05:58 venster 2026-09-13 07:05 UTC .. nu, 68842 tokens
19:06:46 klaar in 49s: 52628 tokens, 1902 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 20:07:44
20:07:45 venster 2026-09-13 08:07 UTC .. nu, 70021 tokens
20:08:37 klaar in 53s: 53536 tokens, 1839 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 21:09:36
21:09:36 venster 2026-09-13 09:09 UTC .. nu, 71175 tokens
21:10:29 klaar in 53s: 54456 tokens, 1720 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
20:59:10 ijk: +1 van 1 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=376 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:59:10 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 13/38/165 | al gemeten: 815
21:04:40 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=378 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:04:41 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 8/36/163 | al gemeten: 818
21:10:10 ijk: +6 van 7 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=382 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:10:13 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 11/43/166 | al gemeten: 824
21:15:08 ijk: +6 van 8 kandidaten (16 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=387 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:15:08 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 17/50/173 | al gemeten: 830
21:20:02 ijk: +5 van 5 kandidaten (17 migraties in het venster, overgeslagen: {'al_gemeten': 12}) | verste bak n=389 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:20:02 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 18/48/172 | al gemeten: 835
21:25:17 ijk: +3 van 3 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 10}) | verste bak n=391 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:25:17 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 14/46/171 | al gemeten: 838
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 3408 | 353 | 349 | 0 | 71 | 4.0 min |
| 09-13 00:00 | 5995 | 675 | 658 | 0 | 295 | 2.3 min |
| 09-13 06:00 | 4301 | 538 | 534 | 0 | 282 | 2.4 min |
| 09-13 12:00 | 6600 | 754 | 741 | 0 | 286 | 2.6 min |
| 09-13 18:00 | 8021 | 920 | 889 | 0 | 118 | 4.0 min |
| 09-14 00:00 | 6068 | 752 | 743 | 0 | 275 | 2.6 min |
| 09-14 06:00 | 4709 | 692 | 683 | 0 | 323 | 2.3 min |
| 09-14 12:00 | 8320 | 1156 | 1091 | 0 | 36 | 16.9 min |
| 09-14 18:00 | 10622 | 1266 | 1153 | 266 | 0 | 94.8 min |
| 09-15 00:00 | 7337 | 881 | 827 | 81 | 0 | 112.5 min |
| 09-15 06:00 | 6072 | 909 | 853 | 1 | 0 | 73.3 min |
| 09-15 12:00 | 9559 | 1252 | 1159 | 12 | 0 | 76.9 min |
| 09-15 18:00 | 6250 | 240 | 225 | 236 | 0 | 137.6 min |

'pas na 2u05' = gescreend nadat de replay het token al had vastgelegd; die tellen nooit mee.


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
