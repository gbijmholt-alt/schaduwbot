# Schaduwbot status

- tijd: 2026-09-14 18:14:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 4 hours, 27 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.1G/38G | geheugen: 2041/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.4, "uptime_s": 128430, "tokens_in_memory": 8658, "msgs": 17202895, "trades": 3643484, "creates": 37957, "decode_fail": 315605, "rpc_calls": 107094, "rpc_errors": 7, "sol_usd": 103.06840732937549, "open_positions": 57, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 17:50:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:00,910 main INFO screen GULP pass=0 dev=0.0 ins=31.14 pro=42 1a=False 1b=False 2=True (68.7s)
Sep 14 17:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:07,789 main INFO screen TOMI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.7s)
Sep 14 17:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:50:26,913 main INFO screen COOKED pass=0 dev=0.0 ins=20.81 pro=4 1a=False 1b=False 2=True (62.6s)
Sep 14 17:51:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:06,171 main INFO screen COOKED pass=0 dev=0.0 ins=21.38 pro=5 1a=False 1b=False 2=True (65.3s)
Sep 14 17:51:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:10,576 main INFO screen HOE pass=1 dev=0.0 ins=0.0 pro=52 1a=False 1b=False 2=False (62.8s)
Sep 14 17:51:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:27,248 main INFO screen UH OH pass=0 dev=0.0 ins=18.03 pro=5 1a=False 1b=False 2=True (60.3s)
Sep 14 17:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:51:58,086 main INFO screen POKEBALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.9s)
Sep 14 17:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:52:04,664 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.1s)
Sep 14 17:52:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:52:18,254 main INFO screen POKEBALL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (51.0s)
Sep 14 17:53:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:06,451 main INFO screen VANS pass=0 dev=0.0 ins=11.0 pro=48 1a=False 1b=False 2=True (68.4s)
Sep 14 17:53:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:07,961 main INFO screen NABU  pass=0 dev=0.02 ins=0.0 pro=5 1a=False 1b=False 2=False (63.3s)
Sep 14 17:53:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:27,593 main INFO screen PEDALON pass=0 dev=0.0 ins=40.69 pro=61 1a=False 1b=False 2=True (69.3s)
Sep 14 17:53:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:53:43,825 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:53:43 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:54:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:15,654 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.2s)
Sep 14 17:54:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:17,272 main INFO screen BRAIN pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (69.3s)
Sep 14 17:54:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:54:22,832 main INFO screen BIKEUNC pass=0 dev=0.0 ins=78.96 pro=5 1a=False 1b=True 2=True (55.2s)
Sep 14 17:55:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:21,430 main INFO screen BASKET pass=1 dev=0.0 ins=16.87 pro=18 1a=False 1b=False 2=False (64.2s)
Sep 14 17:55:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:23,337 main INFO screen DUMB pass=0 dev=0.0 ins=15.21 pro=25 1a=False 1b=False 2=True (60.5s)
Sep 14 17:55:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:55:23,728 main INFO screen MEME1921 pass=0 dev=0.0 ins=1.32 pro=28 1a=False 1b=False 2=False (68.1s)
Sep 14 17:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:35,332 main INFO screen HAIRLINES pass=0 dev=0.0 ins=34.96 pro=16 1a=False 1b=False 2=True (71.6s)
Sep 14 17:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:38,225 aiohttp.access INFO 94.154.43.223 [14/Sep/2026:17:56:38 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 17:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:39,603 main INFO screen WT pass=1 dev=0.0 ins=0.21 pro=13 1a=False 1b=False 2=False (78.2s)
Sep 14 17:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:56:39,660 main INFO screen cooked pass=1 dev=0.0 ins=10.41 pro=40 1a=False 1b=False 2=False (76.3s)
Sep 14 17:57:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:42,698 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.0s)
Sep 14 17:57:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:54,899 main INFO screen PURRNACE pass=0 dev=0.0 ins=77.57 pro=0 1a=False 1b=False 2=True (75.3s)
Sep 14 17:57:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:57:56,327 main INFO screen FATPANDA pass=1 dev=0.0 ins=19.78 pro=28 1a=False 1b=False 2=False (81.0s)
Sep 14 17:58:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:46,571 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.9s)
Sep 14 17:58:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:51,432 main INFO screen Pp AI pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 14 17:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:58:54,960 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:58:54 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 17:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:59:04,869 main INFO screen RUSH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.5s)
Sep 14 17:59:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:59:37,476 aiohttp.access INFO 94.154.43.250 [14/Sep/2026:17:59:37 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 18:00:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:00:06,690 main INFO screen Meta pass=1 dev=0.0 ins=5.37 pro=43 1a=False 1b=False 2=False (80.1s)
Sep 14 18:00:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:00:07,128 main INFO screen DARK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.7s)
Sep 14 18:00:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:00:19,881 main INFO screen moncat pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (75.0s)
Sep 14 18:01:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:01:05,129 main INFO screen WOTF pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 14 18:01:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:01:06,402 main INFO screen pempfen pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.7s)
Sep 14 18:01:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:01:15,814 main INFO screen TRUMPET pass=0 dev=0.0 ins=79.27 pro=0 1a=True 1b=True 2=True (55.9s)
Sep 14 18:02:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:02:17,505 main INFO screen orangie pass=0 dev=0.0 ins=24.88 pro=19 1a=False 1b=False 2=True (72.4s)
Sep 14 18:02:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:02:20,464 main INFO screen FAIR pass=0 dev=0.01 ins=135.64 pro=1 1a=False 1b=False 2=True (64.6s)
Sep 14 18:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:02:21,342 main INFO screen FORGE pass=1 dev=0.0 ins=0.0 pro=46 1a=False 1b=False 2=False (74.9s)
Sep 14 18:03:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:03:27,625 main INFO screen pbot pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.2s)
Sep 14 18:03:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:03:27,984 main INFO screen QUAKEIII pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (70.5s)
Sep 14 18:03:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:03:29,933 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.6s)
Sep 14 18:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:04:04,569 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:04:04 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:04:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:04:33,783 main INFO screen SATS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.2s)
Sep 14 18:04:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:04:36,291 main INFO screen ARE cat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.3s)
Sep 14 18:04:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:04:37,010 main INFO screen Sat pass=0 dev=0.0 ins=48.15 pro=47 1a=False 1b=False 2=True (67.1s)
Sep 14 18:05:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:05:23,940 main INFO screen FAIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (50.2s)
Sep 14 18:05:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:05:38,806 main INFO screen ZORAH pass=0 dev=0.0 ins=32.24 pro=68 1a=False 1b=False 2=True (61.8s)
Sep 14 18:05:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:05:40,996 main INFO screen Enthusiasts pass=0 dev=0.0 ins=20.45 pro=7 1a=False 1b=False 2=False (64.7s)
Sep 14 18:06:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:06:17,899 main INFO screen SpaceX pass=0 dev=0.0 ins=158.21 pro=0 1a=False 1b=False 2=True (54.0s)
Sep 14 18:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:06:29,974 main INFO screen ZORAH pass=0 dev=0.0 ins=55.52 pro=26 1a=False 1b=False 2=True (51.2s)
Sep 14 18:06:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:06:52,609 main INFO screen MARS pass=0 dev=0.0 ins=14.92 pro=46 1a=False 1b=False 2=False (71.6s)
Sep 14 18:07:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:07:16,796 main INFO screen HoneyCc pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.9s)
Sep 14 18:07:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:07:43,290 main INFO screen DeepSoma pass=0 dev=0.0 ins=20.51 pro=4 1a=False 1b=False 2=False (73.3s)
Sep 14 18:07:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:07:51,440 main INFO screen icecube pass=0 dev=0.0 ins=79.24 pro=0 1a=False 1b=True 2=True (58.8s)
Sep 14 18:08:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:08:24,749 main INFO screen OnlyFlies pass=0 dev=0.0 ins=11.38 pro=51 1a=False 1b=False 2=False (68.0s)
Sep 14 18:08:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:08:40,785 main INFO screen Muck pass=0 dev=0.0 ins=5.08 pro=46 1a=False 1b=False 2=False (57.5s)
Sep 14 18:08:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:08:56,949 main INFO screen SKELECAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 14 18:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:09:17,444 main INFO screen Solverse pass=0 dev=0.0 ins=19.14 pro=38 1a=False 1b=False 2=True (52.7s)
Sep 14 18:09:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:09:28,874 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:09:28 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:09:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:09:55,409 main INFO screen SLOTHSOL pass=0 dev=0.0 ins=0.81 pro=56 1a=False 1b=False 2=False (74.6s)
Sep 14 18:10:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:10:04,898 main INFO screen DOGGPT pass=0 dev=0.0 ins=31.83 pro=9 1a=False 1b=False 2=True (67.9s)
Sep 14 18:10:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:10:15,082 main INFO screen DCTT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.6s)
Sep 14 18:10:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:10:51,737 main INFO screen AETHERION pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.3s)
Sep 14 18:11:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:11:01,974 main INFO screen MCD pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (57.1s)
Sep 14 18:11:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:11:11,068 main INFO screen triketyson pass=0 dev=1.86 ins=78.31 pro=4 1a=False 1b=False 2=True (56.0s)
Sep 14 18:12:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:02,122 main INFO screen Stocklana pass=0 dev=0.0 ins=24.37 pro=73 1a=False 1b=False 2=True (70.4s)
Sep 14 18:12:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:12,061 main INFO screen AF1 pass=1 dev=0.0 ins=13.59 pro=30 1a=False 1b=False 2=False (70.1s)
Sep 14 18:12:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:14,002 main INFO screen FTFS pass=0 dev=0.0 ins=18.81 pro=1 1a=False 1b=False 2=True (62.9s)
Sep 14 18:12:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:38,005 aiohttp.access INFO 179.43.134.114 [14/Sep/2026:18:12:38 +0000] "UNKNOWN / HTTP/1.0" 400 235 "-" "-"
Sep 14 18:12:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:38,075 aiohttp.access INFO 179.43.134.114 [14/Sep/2026:18:12:38 +0000] "UNKNOWN / HTTP/1.0" 400 235 "-" "-"
Sep 14 18:12:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:12:48,930 aiohttp.access INFO 165.22.246.163 [14/Sep/2026:18:12:48 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 18:13:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:13:09,467 main INFO screen VANS pass=0 dev=0.0 ins=30.72 pro=55 1a=False 1b=False 2=True (67.3s)
Sep 14 18:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:13:11,926 main INFO screen AI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.9s)
Sep 14 18:13:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:13:16,989 main INFO screen CATE pass=0 dev=0.0 ins=110.84 pro=0 1a=False 1b=False 2=True (63.0s)
Sep 14 18:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:14:27,094 main INFO screen Barrack pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (75.2s)
Sep 14 18:14:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:14:29,560 main INFO screen ELON pass=0 dev=0.0 ins=19.77 pro=5 1a=False 1b=False 2=True (80.1s)
Sep 14 18:14:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:14:31,686 main INFO screen PP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (74.7s)
Sep 14 18:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:14:37,693 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:14:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T16:46:36Z
--- update 2026-09-14T16:52:04Z
--- update 2026-09-14T16:57:04Z
--- update 2026-09-14T17:02:05Z
--- update 2026-09-14T17:07:34Z
--- update 2026-09-14T17:12:36Z
--- update 2026-09-14T17:17:39Z
--- update 2026-09-14T17:22:47Z
--- update 2026-09-14T17:28:07Z
--- update 2026-09-14T17:33:20Z
--- update 2026-09-14T17:38:34Z
--- update 2026-09-14T17:43:36Z
--- update 2026-09-14T17:48:39Z
--- update 2026-09-14T17:53:42Z
--- update 2026-09-14T17:58:53Z
Running as unit: schaduwbot-wallets.service; invocation ID: 9f16fe299e444a8da42e4530eb930f0d
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T18:04:03Z
--- update 2026-09-14T18:09:27Z
--- update 2026-09-14T18:14:36Z
```

## Analyses (laatste 25 regels)
```
active
16:35:33   52000 tokens, 5213503 trades, 638616 posities (341s)
16:35:45   54000 tokens, 5392064 trades, 660041 posities (353s)
16:35:58   56000 tokens, 5596181 trades, 686230 posities (366s)
16:36:09   58000 tokens, 5774359 trades, 706776 posities (378s)
16:36:23   60000 tokens, 6000078 trades, 737951 posities (392s)
16:36:36   62000 tokens, 6182781 trades, 763126 posities (404s)
16:36:50   64000 tokens, 6399806 trades, 792698 posities (419s)
16:37:03   66000 tokens, 6596383 trades, 817546 posities (432s)
16:37:16   68000 tokens, 6798262 trades, 845064 posities (445s)
16:37:30   70000 tokens, 7001931 trades, 881382 posities (458s)
16:37:40 posities: 900358 uit 7154599 trades (470s)
16:37:52 200540 wallets gerekend
16:37:52 geluk-toets
16:38:27 persistentie
16:38:29 kopieer-simulatie
16:40:34 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
17:58:55 85764 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
17:59:20   ingelezen tot rowid 9035965 (200000 rijen, 200000 bruikbaar)
17:59:29   ingelezen tot rowid 9173289 (337324 rijen, 337324 bruikbaar)
17:59:31 ingelezen: 337324 nieuwe trades, 337324 bruikbaar (36s)
18:02:04 3000 aankopen van gevolgde wallets geëvalueerd
18:02:44 vroege kopers: 249 voldoen nu, register 436, 380 tokens beoordeeld
18:03:13 grote spelers: saldo van 386 wallets opgehaald
18:03:38 herkomst: 40 posities gekoppeld
18:03:48 klaar in 294s -> /opt/schaduwbot/reports/ledger.md
```

## IJking poolkoers (laatste 12 regels)
```
17:12:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:17:40 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:22:48 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:28:07 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:33:20 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:38:35 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:43:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:48:39 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:53:43 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:58:54 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
18:04:06 ijk: +1 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:09:31 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
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
