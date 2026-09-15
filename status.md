# Schaduwbot status

- tijd: 2026-09-15 14:17:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 30 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.2G/38G | geheugen: 3595/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 200590, "tokens_in_memory": 6811, "msgs": 28854485, "trades": 6050818, "creates": 64370, "decode_fail": 505725, "rpc_calls": 178750, "rpc_errors": 15, "sol_usd": 100.12052910291135, "open_positions": 31, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 13:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:51:56,202 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:51:56 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 13:52:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:52:05,680 main INFO screen FOMO pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (55.2s)
Sep 15 13:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:52:15,155 main INFO screen GROWUP pass=0 dev=3.53 ins=0.0 pro=6 1a=False 1b=False 2=False (63.5s)
Sep 15 13:52:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:52:45,012 main INFO screen Risu pass=0 dev=0.0 ins=23.71 pro=23 1a=False 1b=False 2=True (65.5s)
Sep 15 13:53:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:53:00,564 main INFO screen stickman pass=0 dev=0.0 ins=7.04 pro=58 1a=False 1b=False 2=False (54.9s)
Sep 15 13:53:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:53:10,758 main INFO screen SALO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 15 13:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:53:47,432 main INFO screen stickman pass=0 dev=0.0 ins=18.79 pro=73 1a=False 1b=False 2=True (62.4s)
Sep 15 13:53:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:53:55,876 main INFO screen vrl pass=0 dev=0.03 ins=0.0 pro=3 1a=False 1b=False 2=False (55.3s)
Sep 15 13:53:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:53:59,520 main INFO screen WOTF pass=0 dev=0.0 ins=137.58 pro=1 1a=False 1b=False 2=True (48.8s)
Sep 15 13:54:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:54:43,654 main INFO screen TRUTH pass=0 dev=0.0 ins=23.42 pro=25 1a=False 1b=False 2=True (56.2s)
Sep 15 13:54:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:54:57,127 main INFO screen lock  pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.2s)
Sep 15 13:55:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:55:02,672 main INFO screen Johnny  pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (63.2s)
Sep 15 13:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:55:38,371 main INFO screen Hope pass=0 dev=0.09 ins=0.0 pro=6 1a=False 1b=False 2=False (54.7s)
Sep 15 13:55:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:55:47,896 main INFO screen TREE pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (50.8s)
Sep 15 13:55:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:55:51,109 main INFO screen Ameer pass=0 dev=0.0 ins=14.2 pro=60 1a=False 1b=False 2=False (48.4s)
Sep 15 13:56:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:56:55,045 main INFO screen Ameer pass=0 dev=0.0 ins=14.53 pro=66 1a=False 1b=False 2=False (76.7s)
Sep 15 13:56:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:56:57,795 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:13:56:57 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 13:57:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:57:00,785 main INFO screen HAMMY pass=0 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (72.9s)
Sep 15 13:57:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:57:02,773 main INFO screen HUHBIKE pass=0 dev=0.0 ins=0.63 pro=16 1a=False 1b=False 2=False (71.7s)
Sep 15 13:57:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:57:54,326 main INFO screen tit pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.3s)
Sep 15 13:58:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:58:12,890 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.1s)
Sep 15 13:58:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:58:13,020 main INFO screen McNuggets pass=0 dev=0.0 ins=69.21 pro=18 1a=False 1b=False 2=True (70.2s)
Sep 15 13:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:59:06,187 main INFO screen .003 pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (71.9s)
Sep 15 13:59:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:59:25,983 main INFO screen METCH pass=0 dev=0.0 ins=28.53 pro=64 1a=False 1b=False 2=True (73.1s)
Sep 15 13:59:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 13:59:26,911 main INFO screen THECOCK pass=0 dev=0.0 ins=17.53 pro=53 1a=False 1b=False 2=True (73.9s)
Sep 15 14:00:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:00:13,532 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (67.3s)
Sep 15 14:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:00:37,232 main INFO screen HUGO pass=0 dev=0.0 ins=15.52 pro=55 1a=False 1b=False 2=True (70.3s)
Sep 15 14:00:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:00:43,953 main INFO screen BIPR pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (78.0s)
Sep 15 14:01:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:01:10,261 main INFO screen banger pass=0 dev=0.0 ins=23.95 pro=26 1a=False 1b=False 2=True (56.7s)
Sep 15 14:01:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:01:44,854 main INFO screen Floor pass=0 dev=0.0 ins=17.72 pro=52 1a=False 1b=False 2=False (60.9s)
Sep 15 14:01:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:01:48,100 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (70.9s)
Sep 15 14:02:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:02:17,277 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:02:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 14:02:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:02:18,377 main INFO screen TAYO pass=0 dev=0.0 ins=19.11 pro=66 1a=False 1b=False 2=True (68.1s)
Sep 15 14:02:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:02:55,636 main INFO screen TAYO pass=0 dev=0.0 ins=15.33 pro=70 1a=False 1b=False 2=True (70.8s)
Sep 15 14:02:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:02:55,898 main INFO screen FOMO pass=0 dev=0.0 ins=14.46 pro=72 1a=False 1b=False 2=True (67.8s)
Sep 15 14:03:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:03:23,409 main INFO screen Meow pass=0 dev=0.0 ins=19.77 pro=11 1a=False 1b=False 2=False (65.0s)
Sep 15 14:04:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:04:02,752 main INFO screen Tayo pass=0 dev=0.0 ins=30.2 pro=74 1a=False 1b=False 2=True (66.9s)
Sep 15 14:04:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:04:08,179 main INFO screen help pass=0 dev=0.0 ins=0.21 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 15 14:04:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:04:15,257 main INFO screen TORNADO pass=0 dev=0.0 ins=34.67 pro=67 1a=False 1b=False 2=True (51.8s)
Sep 15 14:05:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:05:08,862 main INFO screen feg pass=0 dev=0.0 ins=37.32 pro=46 1a=False 1b=False 2=True (66.1s)
Sep 15 14:05:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:05:17,794 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (69.6s)
Sep 15 14:05:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:05:23,371 main INFO screen sg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (68.1s)
Sep 15 14:06:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:06:03,574 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 15 14:06:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:06:11,249 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (53.5s)
Sep 15 14:06:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:06:20,172 main INFO screen RACCM pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (56.8s)
Sep 15 14:07:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:07:00,340 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.8s)
Sep 15 14:07:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:07:17,018 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:07:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 14:07:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:07:27,194 main INFO screen sg pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.9s)
Sep 15 14:07:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:07:29,038 main INFO screen biketoe pass=0 dev=0.0 ins=79.26 pro=2 1a=False 1b=False 2=True (68.9s)
Sep 15 14:08:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:08:01,024 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.7s)
Sep 15 14:08:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:08:34,985 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.9s)
Sep 15 14:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:08:37,137 main INFO screen FO pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (69.9s)
Sep 15 14:09:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:09:12,737 main INFO screen cm pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (71.7s)
Sep 15 14:09:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:09:42,289 main INFO screen 2099850748917 pass=0 dev=0.0 ins=29.98 pro=47 1a=False 1b=False 2=True (65.2s)
Sep 15 14:09:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:09:47,109 main INFO screen Tayo pass=0 dev=0.0 ins=27.42 pro=32 1a=False 1b=False 2=True (72.1s)
Sep 15 14:10:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:10:11,072 main INFO screen CARTIER pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.3s)
Sep 15 14:10:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:10:49,782 main INFO screen HUGO pass=0 dev=0.0 ins=40.87 pro=73 1a=False 1b=False 2=True (62.7s)
Sep 15 14:10:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:10:56,442 main INFO screen SHIRAYUKI pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (74.2s)
Sep 15 14:11:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:11:22,810 main INFO screen BIKECASH pass=0 dev=0.0 ins=78.21 pro=15 1a=False 1b=False 2=True (71.7s)
Sep 15 14:12:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:12:05,118 main INFO screen MESSI pass=0 dev=0.09 ins=0.0 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 15 14:12:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:12:05,255 main INFO screen cm pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (75.5s)
Sep 15 14:12:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:12:17,621 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:12:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 14:12:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:12:28,271 main INFO screen feg pass=0 dev=0.0 ins=0.35 pro=54 1a=False 1b=False 2=True (65.5s)
Sep 15 14:13:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:13:04,270 main INFO screen Chudfrog pass=0 dev=0.0 ins=20.09 pro=7 1a=False 1b=False 2=False (59.2s)
Sep 15 14:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:13:07,663 main INFO screen HUGO pass=0 dev=0.0 ins=35.77 pro=54 1a=False 1b=False 2=True (62.4s)
Sep 15 14:13:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:13:24,655 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (56.4s)
Sep 15 14:14:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:14:01,924 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.7s)
Sep 15 14:14:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:14:09,842 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (62.2s)
Sep 15 14:14:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:14:34,867 main INFO screen DIPZ pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (70.2s)
Sep 15 14:14:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:14:58,444 main INFO screen GDFSJ pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=True 2=True (56.5s)
Sep 15 14:14:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:14:59,839 aiohttp.access INFO 45.79.181.223 [15/Sep/2026:14:14:59 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 14:15:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:15:00,032 aiohttp.access INFO 45.79.181.223 [15/Sep/2026:14:15:00 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 14:15:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:15:18,214 main INFO screen McCannon pass=0 dev=0.0 ins=38.69 pro=58 1a=False 1b=False 2=True (68.4s)
Sep 15 14:15:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:15:28,808 main INFO screen SpongeBob pass=0 dev=0.0 ins=29.37 pro=54 1a=False 1b=False 2=True (53.9s)
Sep 15 14:15:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:15:58,551 main INFO screen stickman pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (60.1s)
Sep 15 14:16:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:16:15,008 main INFO screen PepeCap pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (56.8s)
Sep 15 14:16:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:16:30,390 main INFO screen show pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.6s)
Sep 15 14:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:16:53,063 main INFO screen PARTY pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (54.5s)
Sep 15 14:17:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:17:12,358 main INFO screen Capsule pass=0 dev=0.0 ins=19.47 pro=7 1a=False 1b=False 2=False (57.3s)
Sep 15 14:17:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:17:18,086 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:17:18 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T13:06:35Z
--- update 2026-09-15T13:11:36Z
--- update 2026-09-15T13:16:44Z
nieuwe code: caa47fa
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T13:21:52Z
--- update 2026-09-15T13:26:51Z
--- update 2026-09-15T13:31:52Z
--- update 2026-09-15T13:36:51Z
--- update 2026-09-15T13:41:52Z
--- update 2026-09-15T13:46:53Z
--- update 2026-09-15T13:51:54Z
--- update 2026-09-15T13:56:56Z
--- update 2026-09-15T14:02:15Z
Running as unit: schaduwbot-wallets.service; invocation ID: 39762daa96b14ed5a0e2954268444ef8
analyses gestart (0f687558a2d6)
--- update 2026-09-15T14:07:15Z
--- update 2026-09-15T14:12:16Z
--- update 2026-09-15T14:17:16Z
```

## Analyses (laatste 40 regels)
```
active
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
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
14:02:52 ijk: +6 van 14 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=238 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
14:02:53 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 14/45/160 | al gemeten: 637
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
