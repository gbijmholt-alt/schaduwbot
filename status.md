# Schaduwbot status

- tijd: 2026-09-15 14:32:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 45 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.2G/38G | geheugen: 3598/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 201493, "tokens_in_memory": 6922, "msgs": 29026008, "trades": 6090899, "creates": 64766, "decode_fail": 509828, "rpc_calls": 179690, "rpc_errors": 15, "sol_usd": 99.89715521324891, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 14:17:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:17:27,416 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.0s)
Sep 15 14:17:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:17:49,554 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 15 14:18:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:18:11,626 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.3s)
Sep 15 14:18:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:18:26,393 main INFO screen PAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.0s)
Sep 15 14:18:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:18:43,961 main INFO screen CLARITYBIK pass=0 dev=0.0 ins=0.0 pro=29 1a=False 1b=False 2=False (54.4s)
Sep 15 14:19:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:19:18,423 main INFO screen SPACE pass=0 dev=0.0 ins=0.0 pro=47 1a=False 1b=False 2=False (66.8s)
Sep 15 14:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:19:30,789 main INFO screen KatyCherry pass=0 dev=0.0 ins=67.21 pro=30 1a=False 1b=True 2=True (64.4s)
Sep 15 14:19:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:19:45,542 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (61.6s)
Sep 15 14:20:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:20:12,930 main INFO screen Gondola pass=0 dev=0.0 ins=18.76 pro=7 1a=False 1b=False 2=False (54.5s)
Sep 15 14:20:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:20:46,725 main INFO screen DART pass=0 dev=0.0 ins=3.36 pro=57 1a=False 1b=False 2=False (75.9s)
Sep 15 14:20:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:20:49,670 main INFO screen feg pass=0 dev=0.0 ins=28.98 pro=55 1a=False 1b=False 2=False (64.1s)
Sep 15 14:21:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:21:22,472 main INFO screen Gondola pass=0 dev=0.0 ins=18.71 pro=3 1a=False 1b=False 2=False (69.5s)
Sep 15 14:21:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:21:51,596 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (64.9s)
Sep 15 14:22:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:22:00,610 main INFO screen $$$$ pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (70.9s)
Sep 15 14:22:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:22:19,687 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:22:19 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 14:22:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:22:22,156 main INFO screen VANDIESEL pass=0 dev=0.0 ins=23.29 pro=8 1a=False 1b=False 2=False (59.7s)
Sep 15 14:23:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:23:01,006 main INFO screen AC pass=0 dev=0.0 ins=5.67 pro=37 1a=False 1b=False 2=True (69.4s)
Sep 15 14:23:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:23:05,121 main INFO screen VANDIESEL pass=0 dev=0.0 ins=28.38 pro=28 1a=False 1b=False 2=False (64.5s)
Sep 15 14:23:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:23:21,031 main INFO screen IVCN pass=0 dev=0.0 ins=0.88 pro=12 1a=False 1b=False 2=False (58.9s)
Sep 15 14:23:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:23:54,386 main INFO screen WOTF pass=0 dev=0.79 ins=0.0 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 15 14:24:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:24:04,428 main INFO screen BNPL pass=0 dev=0.0 ins=16.97 pro=25 1a=False 1b=False 2=False (59.3s)
Sep 15 14:24:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:24:32,348 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (71.3s)
Sep 15 14:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:24:49,636 main INFO screen Mitch pass=0 dev=0.0 ins=27.76 pro=65 1a=False 1b=False 2=True (55.2s)
Sep 15 14:25:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:25:11,363 main INFO screen GRHINU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 15 14:25:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:25:28,018 main INFO screen rug pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 14:25:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:25:42,195 main INFO screen VANDIESEL pass=0 dev=0.0 ins=27.38 pro=12 1a=False 1b=False 2=False (52.6s)
Sep 15 14:26:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:26:13,963 main INFO screen One pass=0 dev=0.0 ins=9.45 pro=54 1a=False 1b=False 2=False (62.6s)
Sep 15 14:26:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:26:25,902 main INFO screen VANDIESEL pass=0 dev=0.0 ins=29.1 pro=28 1a=False 1b=False 2=True (57.9s)
Sep 15 14:26:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:26:37,945 main INFO screen Pepebike pass=0 dev=0.0 ins=79.04 pro=2 1a=False 1b=True 2=True (55.7s)
Sep 15 14:27:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:27:13,142 main INFO screen VANDIESEL pass=0 dev=0.0 ins=27.98 pro=39 1a=True 1b=False 2=True (59.2s)
Sep 15 14:27:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:27:21,314 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:27:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 14:27:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:27:27,578 main INFO screen Mission pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.7s)
Sep 15 14:27:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:27:42,459 main INFO screen One pass=0 dev=0.0 ins=17.72 pro=44 1a=False 1b=False 2=False (64.5s)
Sep 15 14:28:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:28:12,824 main INFO screen WOTF pass=0 dev=0.04 ins=20.27 pro=1 1a=False 1b=False 2=True (59.7s)
Sep 15 14:28:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:28:42,691 main INFO screen PEPEBIKE pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=True (75.1s)
Sep 15 14:28:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:28:47,976 main INFO screen TrumpC47 pass=0 dev=0.0 ins=0.21 pro=3 1a=False 1b=False 2=False (65.5s)
Sep 15 14:29:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:29:20,826 main INFO screen WESTF pass=0 dev=0.0 ins=3.18 pro=68 1a=False 1b=False 2=False (68.0s)
Sep 15 14:29:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:29:42,191 main INFO screen CASPER pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (59.5s)
Sep 15 14:29:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:29:53,304 main INFO screen Cash Cat pass=0 dev=0.0 ins=0.18 pro=20 1a=False 1b=False 2=False (65.3s)
Sep 15 14:30:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:30:38,100 main INFO screen SWC pass=0 dev=0.0 ins=17.47 pro=58 1a=False 1b=False 2=False (77.3s)
Sep 15 14:30:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:30:47,819 main INFO screen 镜隙 pass=0 dev=0.0 ins=19.73 pro=67 1a=False 1b=False 2=True (65.6s)
Sep 15 14:31:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:31:14,417 main INFO screen TolyWater pass=0 dev=0.0 ins=7.82 pro=64 1a=False 1b=False 2=False (81.1s)
Sep 15 14:31:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:31:40,597 main INFO screen Mission pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (62.5s)
Sep 15 14:32:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:32:02,183 main INFO screen BALE pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=True (74.4s)
Sep 15 14:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:32:14,915 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (60.5s)
Sep 15 14:32:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:32:21,506 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:32:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-15T14:22:18Z
--- update 2026-09-15T14:27:19Z
--- update 2026-09-15T14:32:20Z
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
