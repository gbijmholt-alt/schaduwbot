# Schaduwbot status

- tijd: 2026-09-15 20:59:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 7 hours, 12 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.6G/38G | geheugen: 2341/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 224699, "tokens_in_memory": 10788, "msgs": 36123814, "trades": 7196755, "creates": 76261, "decode_fail": 607577, "rpc_calls": 203351, "rpc_errors": 17, "sol_usd": 97.34928788717875, "open_positions": 88, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:35:38,501 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (110.5s)
Sep 15 20:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:01,860 main INFO screen BC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (106.3s)
Sep 15 20:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:01,871 main INFO screen Lokas pass=0 dev=0.0 ins=9.81 pro=52 1a=False 1b=False 2=False (129.0s)
Sep 15 20:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:36,656 main INFO screen motion pass=0 dev=0.0 ins=25.01 pro=34 1a=False 1b=False 2=True (58.1s)
Sep 15 20:36:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:53,904 main INFO screen ALLCAT pass=0 dev=0.0 ins=75.89 pro=0 1a=True 1b=True 2=True (52.0s)
Sep 15 20:36:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:54,006 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (52.1s)
Sep 15 20:37:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:26,767 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.1s)
Sep 15 20:37:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:44,508 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (50.6s)
Sep 15 20:37:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:49,163 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.2s)
Sep 15 20:38:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:38:26,776 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:38:26 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:38:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:38:30,683 main INFO screen Memecoin pass=0 dev=0.0 ins=39.35 pro=65 1a=False 1b=False 2=True (63.9s)
Sep 15 20:38:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:38:52,223 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.7s)
Sep 15 20:38:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:38:53,665 main INFO screen HNKL pass=0 dev=3.23 ins=0.0 pro=17 1a=False 1b=False 2=False (64.5s)
Sep 15 20:39:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:39:37,546 main INFO screen Lummis pass=0 dev=0.0 ins=30.87 pro=28 1a=False 1b=False 2=True (66.9s)
Sep 15 20:39:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:39:59,115 main INFO screen Memecoin pass=0 dev=0.0 ins=24.45 pro=60 1a=False 1b=False 2=True (66.9s)
Sep 15 20:40:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:40:01,114 main INFO screen HCAT pass=0 dev=0.0 ins=31.39 pro=57 1a=False 1b=False 2=True (67.4s)
Sep 15 20:40:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:40:44,982 main INFO screen DOG pass=0 dev=0.0 ins=17.88 pro=53 1a=False 1b=False 2=False (67.4s)
Sep 15 20:41:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:41:08,295 main INFO screen Vectra pass=0 dev=0.0 ins=49.08 pro=12 1a=False 1b=False 2=True (67.2s)
Sep 15 20:41:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:41:09,505 main INFO screen Loaf pass=0 dev=0.02 ins=0.0 pro=6 1a=False 1b=False 2=False (70.4s)
Sep 15 20:41:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:41:45,158 main INFO screen THEGLOCK pass=0 dev=0.0 ins=26.9 pro=3 1a=False 1b=False 2=True (60.2s)
Sep 15 20:42:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:42:15,275 main INFO screen UTILITY pass=0 dev=0.0 ins=21.12 pro=1 1a=False 1b=False 2=True (67.0s)
Sep 15 20:42:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:42:16,773 main INFO screen TEAMWINS pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (67.3s)
Sep 15 20:42:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:42:40,856 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (55.7s)
Sep 15 20:43:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:43:09,616 main INFO screen BDOG pass=0 dev=0.0 ins=46.62 pro=45 1a=False 1b=False 2=True (54.3s)
Sep 15 20:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:43:11,415 main INFO screen calm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.6s)
Sep 15 20:43:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:43:32,357 main INFO screen RENTOPOLY pass=0 dev=0.0 ins=48.32 pro=32 1a=False 1b=False 2=True (51.5s)
Sep 15 20:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:43:37,288 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:43:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:44:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:44:04,164 main INFO screen PEPE pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=True (54.5s)
Sep 15 20:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:44:19,595 main INFO screen $BARK pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (68.2s)
Sep 15 20:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:44:28,364 main INFO screen DOOMTARD pass=0 dev=0.0 ins=25.51 pro=0 1a=False 1b=False 2=False (56.0s)
Sep 15 20:45:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:45:18,312 main INFO screen Thanks pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (74.1s)
Sep 15 20:45:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:45:27,275 main INFO screen MEME pass=0 dev=0.0 ins=4.62 pro=55 1a=False 1b=False 2=True (67.7s)
Sep 15 20:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:45:30,427 main INFO screen MEME pass=0 dev=0.0 ins=13.13 pro=26 1a=False 1b=False 2=True (62.1s)
Sep 15 20:46:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:46:27,454 main INFO screen Higher pass=0 dev=0.0 ins=20.32 pro=16 1a=False 1b=False 2=False (69.1s)
Sep 15 20:46:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:46:30,883 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.6s)
Sep 15 20:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:46:35,365 main INFO screen MEME COIN pass=0 dev=0.0 ins=29.21 pro=57 1a=False 1b=False 2=True (64.9s)
Sep 15 20:47:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:47:18,740 main INFO screen INSANITY pass=0 dev=0.0 ins=28.46 pro=11 1a=False 1b=False 2=True (47.9s)
Sep 15 20:47:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:47:20,769 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 15 20:47:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:47:38,061 main INFO screen MemeCoin pass=0 dev=0.0 ins=15.17 pro=64 1a=False 1b=False 2=True (62.7s)
Sep 15 20:48:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:48:26,020 aiohttp.access INFO 45.156.128.127 [15/Sep/2026:20:48:26 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 20:48:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:48:29,789 main INFO screen XPXGOLD pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (69.0s)
Sep 15 20:48:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:48:30,655 main INFO screen Higher pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (71.9s)
Sep 15 20:48:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:48:53,520 main INFO screen dodge pass=0 dev=0.0 ins=28.84 pro=61 1a=False 1b=False 2=True (75.5s)
Sep 15 20:48:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:48:54,820 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:48:54 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 20:49:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:49:18,124 main INFO screen MEME pass=0 dev=0.0 ins=36.49 pro=32 1a=False 1b=False 2=True (48.3s)
Sep 15 20:49:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:49:23,179 main INFO screen Meme pass=0 dev=0.0 ins=18.93 pro=9 1a=False 1b=False 2=False (52.5s)
Sep 15 20:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:49:56,681 main INFO screen Memecoin pass=0 dev=0.0 ins=35.93 pro=65 1a=False 1b=False 2=True (63.2s)
Sep 15 20:50:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:50:10,745 main INFO screen KARY pass=0 dev=0.0 ins=77.89 pro=2 1a=False 1b=True 2=True (52.6s)
Sep 15 20:50:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:50:19,452 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.3s)
Sep 15 20:50:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:50:50,933 main INFO screen WOFI pass=0 dev=0.0 ins=125.49 pro=0 1a=False 1b=False 2=True (54.3s)
Sep 15 20:51:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:51:15,146 main INFO screen Meme coin pass=0 dev=0.0 ins=39.78 pro=8 1a=False 1b=False 2=True (55.7s)
Sep 15 20:51:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:51:24,160 main INFO screen MEMECOIN pass=0 dev=0.0 ins=34.73 pro=79 1a=False 1b=False 2=True (73.4s)
Sep 15 20:51:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:51:50,835 main INFO screen MY pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (59.9s)
Sep 15 20:52:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:52:27,476 main INFO screen NAHDOG pass=0 dev=0.0 ins=19.45 pro=70 1a=False 1b=True 2=False (72.3s)
Sep 15 20:52:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:52:29,288 main INFO screen NUT pass=0 dev=0.0 ins=19.54 pro=38 1a=False 1b=False 2=True (65.1s)
Sep 15 20:53:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:53:04,461 main INFO screen Joke pass=0 dev=0.0 ins=26.16 pro=63 1a=False 1b=False 2=True (73.6s)
Sep 15 20:53:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:53:21,367 main INFO screen ALTCOIN pass=0 dev=0.0 ins=24.53 pro=12 1a=False 1b=False 2=True (53.9s)
Sep 15 20:53:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:53:42,867 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (73.6s)
Sep 15 20:54:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:54:02,885 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:54:02 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 20:54:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:54:04,010 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (59.5s)
Sep 15 20:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:54:28,108 main INFO screen MICROSCOPE pass=0 dev=0.0 ins=12.92 pro=29 1a=False 1b=False 2=True (66.7s)
Sep 15 20:54:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:54:40,019 main INFO screen $GOLDPIG pass=0 dev=0.0 ins=1.04 pro=18 1a=False 1b=False 2=False (57.2s)
Sep 15 20:55:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:55:09,914 main INFO screen CLAWINU pass=0 dev=0.0 ins=24.33 pro=3 1a=False 1b=False 2=True (65.9s)
Sep 15 20:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:55:37,612 main INFO screen MICROSCOPE pass=0 dev=0.0 ins=17.61 pro=51 1a=False 1b=False 2=True (69.5s)
Sep 15 20:55:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:55:47,755 main INFO screen BALL pass=0 dev=0.0 ins=24.45 pro=72 1a=False 1b=False 2=True (67.7s)
Sep 15 20:55:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:55:59,786 main INFO screen Xo1o pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (49.9s)
Sep 15 20:56:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:56:41,287 main INFO screen Regulated pass=0 dev=0.0 ins=47.25 pro=71 1a=False 1b=False 2=True (63.7s)
Sep 15 20:56:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:56:58,805 main INFO screen ELUSSA pass=0 dev=0.0 ins=29.47 pro=70 1a=False 1b=False 2=True (71.0s)
Sep 15 20:57:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:57:02,152 main INFO screen Over pass=0 dev=0.0 ins=12.62 pro=77 1a=False 1b=False 2=False (62.4s)
Sep 15 20:57:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:57:47,493 main INFO screen Altcoin pass=0 dev=0.0 ins=33.25 pro=76 1a=False 1b=False 2=True (66.2s)
Sep 15 20:58:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:58:04,021 main INFO screen CRYPTO pass=0 dev=0.0 ins=35.49 pro=53 1a=False 1b=False 2=True (65.2s)
Sep 15 20:58:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:58:06,992 main INFO screen LESHIT pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.8s)
Sep 15 20:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:58:54,876 main INFO screen Paws pass=0 dev=0.0 ins=15.18 pro=17 1a=False 1b=False 2=False (50.9s)
Sep 15 20:59:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:59:00,259 main INFO screen Confused pass=0 dev=0.0 ins=15.72 pro=72 1a=False 1b=False 2=False (72.8s)
Sep 15 20:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:59:06,762 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:59:06 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T19:31:32Z
--- update 2026-09-15T19:36:36Z
--- update 2026-09-15T19:42:03Z
--- update 2026-09-15T19:47:11Z
--- update 2026-09-15T19:52:29Z
--- update 2026-09-15T19:57:34Z
--- update 2026-09-15T20:02:36Z
--- update 2026-09-15T20:07:43Z
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
```

## Analyses (laatste 40 regels)
```
inactive
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
20:28:39 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=359 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:28:40 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 11/40/164 | al gemeten: 794
20:33:35 ijk: +2 van 2 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=361 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:33:35 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 11/42/160 | al gemeten: 796
20:38:50 ijk: +5 van 5 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=365 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:38:50 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 9/46/165 | al gemeten: 801
20:43:46 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=366 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:43:46 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/42/161 | al gemeten: 803
20:49:23 ijk: +6 van 7 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=372 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:49:23 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 14/43/165 | al gemeten: 809
20:54:25 ijk: +5 van 5 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=375 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:54:25 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 12/44/166 | al gemeten: 814
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 4224 | 425 | 421 | 0 | 97 | 3.8 min |
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
| 09-15 18:00 | 5236 | 150 | 143 | 146 | 0 | 133.3 min |

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
