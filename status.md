# Schaduwbot status

- tijd: 2026-09-15 23:24:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 9 hours, 37 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.8G/38G | geheugen: 2441/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 233427, "tokens_in_memory": 11710, "msgs": 41213551, "trades": 7716762, "creates": 81600, "decode_fail": 638309, "rpc_calls": 212375, "rpc_errors": 18, "sol_usd": 97.51271834167369, "open_positions": 96, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 22:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:58:29,959 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:58:29 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 22:58:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:58:50,788 main INFO screen BROS pass=0 dev=0.0 ins=25.1 pro=3 1a=False 1b=False 2=True (63.1s)
Sep 15 22:59:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:59:28,197 main INFO screen Democrat pass=0 dev=0.0 ins=111.02 pro=0 1a=False 1b=False 2=True (59.5s)
Sep 15 22:59:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:59:43,150 main INFO screen VOICE pass=0 dev=0.58 ins=14.25 pro=72 1a=False 1b=False 2=True (73.9s)
Sep 15 22:59:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:59:48,388 main INFO screen RISEINU pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (57.6s)
Sep 15 23:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:00:45,785 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (77.6s)
Sep 15 23:00:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:00:59,249 main INFO screen 21SAUSAGE pass=0 dev=0.0 ins=31.4 pro=16 1a=False 1b=False 2=True (70.9s)
Sep 15 23:00:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:00:59,727 main INFO screen F pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.6s)
Sep 15 23:01:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:01:38,965 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.2s)
Sep 15 23:01:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:01:50,798 main INFO screen Evader pass=0 dev=0.0 ins=20.07 pro=36 1a=False 1b=False 2=False (51.5s)
Sep 15 23:01:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:01:57,328 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 23:02:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:02:32,841 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (53.9s)
Sep 15 23:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:02:36,782 main INFO screen Lobster pass=0 dev=0.0 ins=18.7 pro=41 1a=False 1b=False 2=True (46.0s)
Sep 15 23:02:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:02:49,268 main INFO screen bytecat pass=0 dev=0.0 ins=18.59 pro=75 1a=False 1b=False 2=True (51.9s)
Sep 15 23:03:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:03:37,228 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:03:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 23:03:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:03:45,956 main INFO screen OT pass=0 dev=0.0 ins=21.23 pro=76 1a=False 1b=False 2=True (73.1s)
Sep 15 23:03:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:03:50,812 main INFO screen Mass pass=0 dev=0.0 ins=11.24 pro=39 1a=False 1b=False 2=True (74.0s)
Sep 15 23:03:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:03:53,499 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (64.2s)
Sep 15 23:04:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:04:39,338 main INFO screen EN pass=0 dev=0.08 ins=0.0 pro=3 1a=False 1b=False 2=False (53.4s)
Sep 15 23:04:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:04:53,661 main INFO screen WAR pass=0 dev=0.35 ins=0.0 pro=13 1a=False 1b=False 2=False (62.8s)
Sep 15 23:04:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:04:54,132 main INFO screen SolLama pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (60.6s)
Sep 15 23:05:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:05:46,974 main INFO screen ALON pass=0 dev=0.0 ins=0.0 pro=76 1a=False 1b=False 2=True (67.6s)
Sep 15 23:06:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:06:00,035 main INFO screen Dumbocrat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.4s)
Sep 15 23:06:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:06:12,765 main INFO screen Pyramid pass=0 dev=0.0 ins=49.04 pro=17 1a=False 1b=False 2=True (78.6s)
Sep 15 23:06:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:06:42,431 main INFO screen DOOM pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.5s)
Sep 15 23:06:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:06:58,141 main INFO screen BESTFRIEND pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (58.1s)
Sep 15 23:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:07:19,456 main INFO screen JACK pass=0 dev=0.0 ins=17.7 pro=63 1a=False 1b=False 2=True (66.7s)
Sep 15 23:08:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:08:00,693 main INFO screen PANICAN pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=False (78.3s)
Sep 15 23:08:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:08:13,657 main INFO screen 1 pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (75.5s)
Sep 15 23:08:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:08:36,854 main INFO screen BINDIESEL pass=0 dev=0.69 ins=0.0 pro=58 1a=False 1b=False 2=False (77.4s)
Sep 15 23:09:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:09:04,179 main INFO screen Beef6900 pass=0 dev=0.0 ins=25.76 pro=0 1a=False 1b=False 2=True (63.5s)
Sep 15 23:09:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:09:16,648 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:09:16 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 23:09:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:09:22,886 main INFO screen EN pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (69.2s)
Sep 15 23:09:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:09:39,495 main INFO screen Paid pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (62.6s)
Sep 15 23:09:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:09:59,064 main INFO screen DOOM pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.9s)
Sep 15 23:10:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:10:34,218 main INFO screen FLEX pass=0 dev=0.07 ins=0.0 pro=43 1a=False 1b=False 2=False (71.3s)
Sep 15 23:10:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:10:45,965 main INFO screen Kiki pass=0 dev=0.0 ins=36.47 pro=63 1a=False 1b=False 2=True (66.5s)
Sep 15 23:10:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:10:57,238 main INFO screen troll9 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.2s)
Sep 15 23:11:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:11:31,506 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.3s)
Sep 15 23:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:11:43,929 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 15 23:11:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:11:51,783 main INFO screen TRUMPET pass=0 dev=2.16 ins=14.19 pro=21 1a=False 1b=False 2=False (54.5s)
Sep 15 23:12:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:12:36,626 main INFO screen Kiki pass=0 dev=0.0 ins=32.44 pro=52 1a=False 1b=False 2=True (65.1s)
Sep 15 23:12:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:12:53,890 main INFO screen MCTRUMP pass=0 dev=0.0 ins=24.13 pro=1 1a=False 1b=False 2=False (62.1s)
Sep 15 23:12:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:12:58,445 main INFO screen Dictator pass=0 dev=0.0 ins=21.86 pro=28 1a=False 1b=False 2=False (74.5s)
Sep 15 23:13:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:13:26,791 main INFO screen FOID pass=0 dev=0.0 ins=41.02 pro=25 1a=False 1b=False 2=True (50.2s)
Sep 15 23:13:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:13:50,004 main INFO screen MHOOD pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (56.1s)
Sep 15 23:14:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:14:00,570 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.1s)
Sep 15 23:14:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:14:25,889 main INFO screen XPXGOLD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.1s)
Sep 15 23:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:14:27,443 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:14:27 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:15:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:15:03,932 main INFO screen QCOW pass=0 dev=0.0 ins=20.67 pro=2 1a=False 1b=False 2=True (73.9s)
Sep 15 23:15:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:15:11,060 main INFO screen mcap pass=0 dev=0.0 ins=31.19 pro=66 1a=False 1b=False 2=True (70.5s)
Sep 15 23:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:15:35,863 main INFO screen LMEOW pass=0 dev=0.0 ins=9.78 pro=83 1a=False 1b=False 2=True (70.0s)
Sep 15 23:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:16:01,363 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (57.4s)
Sep 15 23:16:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:16:09,777 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.7s)
Sep 15 23:16:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:16:28,521 main INFO screen LMEOW pass=0 dev=0.0 ins=24.52 pro=2 1a=False 1b=False 2=True (52.7s)
Sep 15 23:17:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:17:11,675 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (61.9s)
Sep 15 23:17:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:17:13,740 main INFO screen scooter pass=0 dev=0.0 ins=29.22 pro=25 1a=False 1b=False 2=True (72.4s)
Sep 15 23:17:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:17:24,215 main INFO screen OFF pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (55.7s)
Sep 15 23:18:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:18,734 main INFO screen FLY pass=0 dev=0.0 ins=28.95 pro=60 1a=False 1b=False 2=True (67.1s)
Sep 15 23:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:19,126 main INFO screen BANKS pass=0 dev=0.04 ins=0.0 pro=74 1a=False 1b=False 2=False (65.4s)
Sep 15 23:18:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:31,530 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.3s)
Sep 15 23:19:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:24,316 main INFO screen Inuvation pass=0 dev=0.0 ins=15.33 pro=33 1a=False 1b=False 2=False (65.6s)
Sep 15 23:19:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:27,763 main INFO screen WWR pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (68.6s)
Sep 15 23:19:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:32,968 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:19:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:19:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:45,118 main INFO screen GAS pass=0 dev=0.0 ins=49.11 pro=16 1a=False 1b=False 2=True (73.6s)
Sep 15 23:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:18,319 main INFO screen leaf pass=0 dev=0.0 ins=36.38 pro=46 1a=False 1b=False 2=True (50.6s)
Sep 15 23:20:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:20,339 main INFO screen bangbus pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (56.0s)
Sep 15 23:20:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:42,146 main INFO screen hiyf  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.0s)
Sep 15 23:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:10,074 main INFO screen PUSSY pass=0 dev=0.0 ins=32.69 pro=13 1a=False 1b=False 2=True (49.7s)
Sep 15 23:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:29,891 main INFO screen Rich Pill pass=0 dev=0.0 ins=0.48 pro=12 1a=False 1b=False 2=False (71.6s)
Sep 15 23:21:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:35,179 main INFO screen Pussies pass=0 dev=0.0 ins=17.88 pro=42 1a=False 1b=False 2=True (53.0s)
Sep 15 23:22:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:04,023 main INFO screen Pussies pass=0 dev=0.0 ins=20.67 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 15 23:22:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:40,019 main INFO screen Paragon pass=0 dev=0.0 ins=25.29 pro=0 1a=False 1b=False 2=True (70.1s)
Sep 15 23:22:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:41,828 aiohttp.access INFO 204.76.203.7 [15/Sep/2026:23:22:41 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0"
Sep 15 23:22:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:46,210 main INFO screen 1 pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (71.0s)
Sep 15 23:23:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:18,574 main INFO screen fruk pass=0 dev=0.0 ins=0.0 pro=47 1a=False 1b=False 2=False (74.5s)
Sep 15 23:23:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:27,352 main INFO screen Yun pass=0 dev=0.0 ins=33.82 pro=42 1a=False 1b=False 2=True (47.3s)
Sep 15 23:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:47,785 main INFO screen Whore pass=0 dev=0.0 ins=0.75 pro=36 1a=False 1b=False 2=False (61.6s)
Sep 15 23:24:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:31,160 main INFO screen mike pass=0 dev=0.0 ins=14.86 pro=58 1a=False 1b=False 2=True (72.6s)
Sep 15 23:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:35,001 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:24:34 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T22:06:36Z
--- update 2026-09-15T22:11:39Z
Running as unit: schaduwbot-wallets.service; invocation ID: b46f5ed8f5f6459e97deaaa3c5d20a86
analyses gestart (84579ff37485)
--- update 2026-09-15T22:16:44Z
--- update 2026-09-15T22:21:44Z
--- update 2026-09-15T22:26:45Z
--- update 2026-09-15T22:31:47Z
--- update 2026-09-15T22:37:16Z
--- update 2026-09-15T22:42:34Z
--- update 2026-09-15T22:47:36Z
--- update 2026-09-15T22:52:48Z
--- update 2026-09-15T22:58:28Z
--- update 2026-09-15T23:03:36Z
--- update 2026-09-15T23:09:15Z
--- update 2026-09-15T23:14:26Z
Running as unit: schaduwbot-wallets.service; invocation ID: 28b70ef890d5475a9c6286045b142940
analyses gestart (84579ff37485)
--- update 2026-09-15T23:19:31Z
--- update 2026-09-15T23:24:33Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 22:11:40
22:11:40 venster 2026-09-13 10:11 UTC .. nu, 72419 tokens
22:12:33 klaar in 54s: 55545 tokens, 1912 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 23:14:26
23:14:27 venster 2026-09-13 11:14 UTC .. nu, 73409 tokens
23:15:28 klaar in 61s: 56398 tokens, 1848 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
22:53:18 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=422 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:53:18 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 13/53/191 | al gemeten: 879
22:58:44 ijk: +3 van 3 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=424 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:58:44 ijk-diagnose: nieuwste migratie 3.3 min oud | migraties 15/60/240 min: 14/48/191 | al gemeten: 882
23:03:56 ijk: +4 van 4 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=428 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:03:56 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 12/49/194 | al gemeten: 886
23:09:30 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=431 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:09:30 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 8/46/193 | al gemeten: 889
23:15:07 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=436 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:15:13 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 14/49/199 | al gemeten: 895
23:19:56 ijk: +5 van 5 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=440 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:19:57 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 14/50/197 | al gemeten: 900
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 827 | 98 | 95 | 0 | 0 | 7.0 min |
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
| 09-15 18:00 | 10575 | 553 | 510 | 549 | 0 | 153.9 min |

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
