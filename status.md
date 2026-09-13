# Schaduwbot status

- tijd: 2026-09-13 21:21:10 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 7 hours, 34 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.0G/38G | geheugen: 1802/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 53222, "tokens_in_memory": 7752, "msgs": 6215377, "trades": 1391761, "creates": 14912, "decode_fail": 131677, "rpc_calls": 40843, "rpc_errors": 2, "sol_usd": 101.40332937415009, "open_positions": 29, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 20:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:53:54,121 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.1s)
Sep 13 20:53:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:53:55,614 main INFO screen BILLION pass=0 dev=0.0 ins=10.89 pro=78 1a=False 1b=False 2=True (75.9s)
Sep 13 20:53:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:53:59,586 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.9s)
Sep 13 20:54:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:54:16,566 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:54:16 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:55:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:55:12,536 main INFO screen egg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (78.4s)
Sep 13 20:55:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:55:13,440 main INFO screen ILANDS pass=0 dev=0.0 ins=30.39 pro=83 1a=False 1b=False 2=True (77.8s)
Sep 13 20:55:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:55:14,901 main INFO screen NIGGAMODE pass=0 dev=26.58 ins=1.0 pro=21 1a=False 1b=False 2=False (75.3s)
Sep 13 20:56:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:56:19,834 main INFO screen ALLSTATE pass=1 dev=2.37 ins=0.0 pro=14 1a=False 1b=False 2=False (64.9s)
Sep 13 20:56:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:56:21,667 main INFO screen MILLI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.1s)
Sep 13 20:56:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:56:22,168 main INFO screen PUMPPONS pass=0 dev=0.0 ins=23.75 pro=12 1a=False 1b=False 2=False (68.7s)
Sep 13 20:57:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:57:26,014 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (63.8s)
Sep 13 20:57:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:57:26,114 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.4s)
Sep 13 20:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:57:27,979 main INFO screen BMS pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (68.1s)
Sep 13 20:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:58:18,298 main INFO screen STOCKNINA pass=0 dev=0.7 ins=78.61 pro=3 1a=False 1b=True 2=True (52.3s)
Sep 13 20:58:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:58:28,294 main INFO screen BetOnBlak pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 13 20:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:58:29,850 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.9s)
Sep 13 20:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:59:06,140 main INFO screen FOMO pass=0 dev=37.14 ins=0.0 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 13 20:59:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:59:31,750 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=4 1a=False 1b=True 2=False (61.9s)
Sep 13 20:59:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:59:33,209 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.9s)
Sep 13 20:59:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:59:37,472 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:59:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:00:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:00:09,458 main INFO screen VELOC pass=0 dev=0.0 ins=28.09 pro=71 1a=False 1b=False 2=True (63.3s)
Sep 13 21:00:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:00:29,318 main INFO screen SEND pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.6s)
Sep 13 21:00:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:00:32,508 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.3s)
Sep 13 21:01:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:01:18,943 main INFO screen TICKER pass=1 dev=1.57 ins=0.0 pro=40 1a=False 1b=False 2=False (69.5s)
Sep 13 21:01:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:01:43,366 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (74.0s)
Sep 13 21:01:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:01:44,410 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (71.9s)
Sep 13 21:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:02:21,035 main INFO screen HBANK pass=0 dev=0.0 ins=26.31 pro=62 1a=False 1b=False 2=True (62.1s)
Sep 13 21:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:02:36,690 main INFO screen LCB pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.3s)
Sep 13 21:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:02:37,651 main INFO screen TikTok pass=0 dev=28.92 ins=20.94 pro=1 1a=False 1b=False 2=True (54.3s)
Sep 13 21:03:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:03:27,335 main INFO screen SEND pass=0 dev=0.27 ins=0.0 pro=3 1a=False 1b=False 2=False (66.3s)
Sep 13 21:03:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:03:48,045 main INFO screen BIGTITTY  pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (70.4s)
Sep 13 21:03:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:03:48,351 main INFO screen Big Tts pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (71.7s)
Sep 13 21:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:04:38,643 main INFO screen fg pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (71.3s)
Sep 13 21:04:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:04:59,898 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:04:59 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:05:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:05:30,741 main INFO screen BIGTITTY  pass=0 dev=0.12 ins=0.0 pro=5 1a=False 1b=False 2=False (67.8s)
Sep 13 21:06:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:06:11,338 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.4s)
Sep 13 21:06:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:06:22,556 main INFO screen ILLEGAL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (67.6s)
Sep 13 21:07:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:07:18,532 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:21:07:18 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 21:07:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:07:23,067 main INFO screen LVL pass=0 dev=0.0 ins=24.73 pro=66 1a=False 1b=False 2=True (71.7s)
Sep 13 21:07:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:07:24,550 main INFO screen V12 pass=0 dev=1.75 ins=0.0 pro=4 1a=False 1b=False 2=False (74.3s)
Sep 13 21:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:07:30,930 main INFO screen SMACK pass=0 dev=3.42 ins=0.0 pro=4 1a=False 1b=False 2=False (68.4s)
Sep 13 21:08:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:08:14,769 main INFO screen KK3000 pass=0 dev=0.0 ins=34.92 pro=33 1a=False 1b=False 2=True (51.7s)
Sep 13 21:08:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:08:31,072 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.5s)
Sep 13 21:08:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:08:33,283 main INFO screen Big Tts pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 13 21:09:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:09:47,844 main INFO screen FUSION pass=0 dev=0.0 ins=25.24 pro=51 1a=False 1b=False 2=True (76.2s)
Sep 13 21:09:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:09:52,097 main INFO screen GLORILLA pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (78.8s)
Sep 13 21:09:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:09:53,798 main INFO screen VOID pass=0 dev=42.53 ins=0.01 pro=6 1a=False 1b=False 2=False (82.5s)
Sep 13 21:10:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:10:37,085 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:10:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:10:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:10:42,308 main INFO screen homo pass=0 dev=4.95 ins=23.39 pro=33 1a=False 1b=False 2=True (54.5s)
Sep 13 21:10:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:10:46,335 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.2s)
Sep 13 21:11:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:11:00,050 main INFO screen BLYAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.3s)
Sep 13 21:11:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:11:54,736 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.4s)
Sep 13 21:11:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:11:57,074 main INFO screen SCRVAN pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (70.7s)
Sep 13 21:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:12:20,597 main INFO screen ENDAI pass=0 dev=0.0 ins=78.96 pro=0 1a=True 1b=True 2=True (60.0s)
Sep 13 21:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:13:07,495 main INFO screen JAKE pass=0 dev=0.01 ins=0.0 pro=6 1a=False 1b=False 2=False (68.0s)
Sep 13 21:13:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:13:29,098 main INFO screen Big Tts pass=0 dev=0.0 ins=0.21 pro=8 1a=False 1b=False 2=False (73.3s)
Sep 13 21:13:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:13:31,766 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.5s)
Sep 13 21:14:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:14:23,244 main INFO screen RETARD pass=0 dev=0.0 ins=17.37 pro=45 1a=False 1b=False 2=True (55.3s)
Sep 13 21:14:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:14:45,488 main INFO screen ALI pass=0 dev=3.75 ins=0.0 pro=7 1a=False 1b=False 2=False (74.9s)
Sep 13 21:15:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:37,888 main INFO screen att pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (75.0s)
Sep 13 21:15:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:39,123 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:15:39 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:15:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:44,735 main INFO screen Motion pass=0 dev=0.15 ins=36.49 pro=64 1a=False 1b=False 2=True (68.0s)
Sep 13 21:15:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:15:56,378 main INFO screen SOL pass=0 dev=0.0 ins=36.86 pro=79 1a=False 1b=False 2=True (63.9s)
Sep 13 21:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:31,893 main INFO screen Longdog pass=1 dev=0.0 ins=8.29 pro=24 1a=False 1b=False 2=False (54.0s)
Sep 13 21:16:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:45,878 aiohttp.access INFO 195.182.16.23 [13/Sep/2026:21:16:45 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 13 21:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:54,335 aiohttp.access INFO 34.222.185.251 [13/Sep/2026:21:16:54 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
Sep 13 21:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:54,346 main INFO screen TWINS pass=0 dev=0.0 ins=23.79 pro=47 1a=False 1b=False 2=False (69.6s)
Sep 13 21:16:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:16:59,077 main INFO screen ALI pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=True (62.7s)
Sep 13 21:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:17:28,259 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.4s)
Sep 13 21:17:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:17:50,757 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 13 21:18:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:04,711 main INFO screen NOCAP pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 13 21:18:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:22,901 main INFO screen ALGO pass=0 dev=3.98 ins=22.83 pro=64 1a=False 1b=True 2=True (54.6s)
Sep 13 21:18:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:42,400 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 13 21:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:18:56,295 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.6s)
Sep 13 21:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:22,216 main INFO screen cry pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.3s)
Sep 13 21:19:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:31,286 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.9s)
Sep 13 21:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:19:55,870 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.6s)
Sep 13 21:20:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:20:28,330 main INFO screen savemeeee pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (66.1s)
Sep 13 21:20:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:20:36,263 main INFO screen WOFI pass=0 dev=61.29 ins=0.0 pro=1 1a=False 1b=False 2=True (65.0s)
Sep 13 21:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:21:10,266 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:21:10 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (87dd80a5c10e)
--- update 2026-09-13T20:07:10Z
nieuwe code: 69b3f7f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T20:12:26Z
--- update 2026-09-13T20:17:36Z
--- update 2026-09-13T20:22:59Z
--- update 2026-09-13T20:28:22Z
--- update 2026-09-13T20:33:36Z
--- update 2026-09-13T20:38:57Z
Running as unit: schaduwbot-wallets.service; invocation ID: 301ce98199ac46cc8bdea3ab53015d56
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T20:44:08Z
--- update 2026-09-13T20:49:14Z
--- update 2026-09-13T20:54:15Z
--- update 2026-09-13T20:59:36Z
--- update 2026-09-13T21:04:58Z
--- update 2026-09-13T21:10:36Z
--- update 2026-09-13T21:15:38Z
--- update 2026-09-13T21:21:09Z
```

## Analyses (laatste 25 regels)
```
inactive
20:58:24   24000 tokens, 2539115 trades, 362670 posities (122s)
20:58:34   26000 tokens, 2749363 trades, 392838 posities (132s)
20:58:44   28000 tokens, 2951661 trades, 418764 posities (143s)
20:58:55   30000 tokens, 3167138 trades, 449939 posities (153s)
20:59:06   32000 tokens, 3395846 trades, 485427 posities (164s)
20:59:16   34000 tokens, 3598592 trades, 514118 posities (174s)
20:59:27   36000 tokens, 3791936 trades, 538973 posities (185s)
20:59:38   38000 tokens, 4009130 trades, 571221 posities (196s)
20:59:50   40000 tokens, 4217529 trades, 602889 posities (208s)
21:00:01   42000 tokens, 4419767 trades, 629224 posities (219s)
21:00:11   44000 tokens, 4617797 trades, 654225 posities (229s)
21:00:22   46000 tokens, 4814574 trades, 683467 posities (240s)
21:00:34   48000 tokens, 5035877 trades, 716964 posities (253s)
21:00:45   50000 tokens, 5214248 trades, 742397 posities (263s)
21:00:57   52000 tokens, 5426165 trades, 774722 posities (275s)
21:01:10   54000 tokens, 5649674 trades, 809593 posities (289s)
21:01:23   56000 tokens, 5861579 trades, 840319 posities (301s)
21:01:36   58000 tokens, 6086009 trades, 875935 posities (315s)
21:01:48   60000 tokens, 6302939 trades, 921314 posities (327s)
21:01:55 posities: 941185 uit 6436124 trades (336s)
21:02:09 199194 wallets gerekend
21:02:10 geluk-toets
21:02:45 persistentie
21:02:48 kopieer-simulatie
21:04:24 klaar in 485s -> /opt/schaduwbot/reports/wallets.md
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
