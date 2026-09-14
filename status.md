# Schaduwbot status

- tijd: 2026-09-14 03:20:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 13 hours, 33 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 2035/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 74789, "tokens_in_memory": 7517, "msgs": 10120774, "trades": 2118142, "creates": 22418, "decode_fail": 184311, "rpc_calls": 61922, "rpc_errors": 3, "sol_usd": 101.05363831709506, "open_positions": 49, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 02:48:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:48:01,084 main INFO screen Toely pass=0 dev=0.0 ins=28.54 pro=33 1a=False 1b=False 2=True (66.0s)
Sep 14 02:48:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:48:40,103 main INFO screen GrokSolver pass=0 dev=0.0 ins=35.88 pro=13 1a=True 1b=False 2=True (55.5s)
Sep 14 02:49:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:46,832 main INFO screen KYC pass=0 dev=0.0 ins=29.85 pro=27 1a=False 1b=False 2=True (83.2s)
Sep 14 02:49:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:51,370 main INFO screen DOOB pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (77.1s)
Sep 14 02:49:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:49:55,899 main INFO screen orangie pass=0 dev=0.0 ins=15.01 pro=56 1a=False 1b=False 2=True (75.8s)
Sep 14 02:50:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:50:19,131 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:50:19 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:50:46,198 main INFO screen seed pass=0 dev=0.0 ins=27.85 pro=16 1a=True 1b=False 2=True (59.4s)
Sep 14 02:51:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:51:03,941 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 14 02:51:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:51:42,440 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 14 02:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:14,906 main INFO screen PSYOPZ pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=False 2=True (71.0s)
Sep 14 02:52:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:16,858 main INFO screen ShibaShil pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (89.9s)
Sep 14 02:52:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:52:58,494 main INFO screen Saturween pass=0 dev=6.3 ins=0.0 pro=34 1a=False 1b=False 2=False (76.1s)
Sep 14 02:53:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:53:11,976 main INFO screen STAQ pass=0 dev=0.0 ins=38.92 pro=16 1a=True 1b=False 2=False (57.1s)
Sep 14 02:53:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:53:12,496 main INFO screen 奶龙 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.6s)
Sep 14 02:54:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:54:20,868 main INFO screen $AO pass=0 dev=40.13 ins=11.57 pro=10 1a=False 1b=False 2=False (58.3s)
Sep 14 02:55:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:06,845 main INFO screen EPIKGPT pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (60.3s)
Sep 14 02:55:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:20,640 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:02:55:20 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 02:55:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:25,359 main INFO screen USMS pass=0 dev=19.77 ins=0.0 pro=11 1a=False 1b=False 2=False (72.8s)
Sep 14 02:55:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:55:31,257 main INFO screen pubic pass=0 dev=0.0 ins=30.66 pro=37 1a=False 1b=False 2=True (70.4s)
Sep 14 02:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:26,219 main INFO screen TYTHON pass=1 dev=1.92 ins=6.32 pro=59 1a=False 1b=False 2=False (79.4s)
Sep 14 02:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:35,742 main INFO screen TWINEAURA pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=False 2=True (70.4s)
Sep 14 02:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:56:38,678 main INFO screen FROBERT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.4s)
Sep 14 02:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:57:41,409 main INFO screen USMS pass=0 dev=6.06 ins=0.0 pro=2 1a=False 1b=False 2=False (53.7s)
Sep 14 02:57:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:57:53,371 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.7s)
Sep 14 02:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:58:29,520 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (51.8s)
Sep 14 02:58:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:58:58,786 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.5s)
Sep 14 02:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:59:16,692 main INFO screen MONTY pass=0 dev=0.0 ins=18.92 pro=50 1a=False 1b=False 2=True (52.8s)
Sep 14 02:59:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 02:59:36,779 main INFO screen Banks pass=0 dev=0.0 ins=21.47 pro=60 1a=False 1b=False 2=True (63.4s)
Sep 14 03:00:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:00:20,516 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:00:20 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 03:00:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:00:32,182 main INFO screen SOLGOODMAN  pass=0 dev=0.0 ins=27.87 pro=66 1a=False 1b=False 2=True (53.8s)
Sep 14 03:00:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:00:47,035 main INFO screen biketyson pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.8s)
Sep 14 03:01:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:01:08,802 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (53.0s)
Sep 14 03:01:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:01:47,702 main INFO screen JohnWick pass=1 dev=0.0 ins=8.13 pro=75 1a=False 1b=False 2=False (66.9s)
Sep 14 03:02:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:02:27,696 main INFO screen biketyson pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (67.7s)
Sep 14 03:02:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:02:42,040 main INFO screen rasmr pass=0 dev=0.0 ins=23.47 pro=65 1a=False 1b=False 2=True (60.8s)
Sep 14 03:02:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:02:58,733 main INFO screen Banks pass=0 dev=0.0 ins=17.35 pro=91 1a=False 1b=False 2=True (64.9s)
Sep 14 03:03:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:03:42,211 main INFO screen BIKE67 pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (55.8s)
Sep 14 03:04:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:04:01,927 main INFO screen ETAC pass=0 dev=0.31 ins=0.0 pro=2 1a=False 1b=False 2=False (67.3s)
Sep 14 03:04:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:04:05,263 main INFO screen biketyson pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 14 03:05:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:05:02,655 main INFO screen IIM pass=1 dev=0.0 ins=8.18 pro=64 1a=False 1b=False 2=False (80.4s)
Sep 14 03:05:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:05:16,722 main INFO screen moin pass=0 dev=0.0 ins=34.25 pro=74 1a=False 1b=False 2=True (74.8s)
Sep 14 03:05:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:05:18,449 main INFO screen DUVET pass=1 dev=0.0 ins=5.11 pro=46 1a=False 1b=False 2=False (73.2s)
Sep 14 03:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:05:22,899 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:05:22 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 03:05:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:05:56,958 main INFO screen LNTRNS pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (54.3s)
Sep 14 03:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:06:29,379 main INFO screen FIGHT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.8s)
Sep 14 03:07:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:07:28,504 main INFO screen Coach pass=0 dev=0.0 ins=22.97 pro=62 1a=False 1b=False 2=True (63.6s)
Sep 14 03:08:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:08:00,516 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.5s)
Sep 14 03:08:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:08:02,771 main INFO screen DV pass=0 dev=0.0 ins=27.18 pro=50 1a=False 1b=False 2=True (72.2s)
Sep 14 03:08:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:08:24,602 main INFO screen Gemini AI pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (56.1s)
Sep 14 03:09:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:09:20,814 main INFO screen ECTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 14 03:09:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:09:46,468 main INFO screen $GOAT pass=0 dev=0.99 ins=0.0 pro=1 1a=False 1b=False 2=False (66.9s)
Sep 14 03:10:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:10:12,252 main INFO screen SEYONG pass=0 dev=0.0 ins=18.82 pro=74 1a=False 1b=False 2=True (66.6s)
Sep 14 03:10:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:10:25,738 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:10:25 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:10:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:10:38,041 main INFO screen WIFCHART pass=0 dev=0.18 ins=77.98 pro=9 1a=False 1b=True 2=True (77.2s)
Sep 14 03:11:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:11:04,775 main INFO screen cap pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (78.3s)
Sep 14 03:11:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:11:22,271 main INFO screen Gatto pass=0 dev=3.79 ins=0.99 pro=71 1a=False 1b=True 2=False (70.0s)
Sep 14 03:11:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:11:40,153 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.1s)
Sep 14 03:12:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:12:28,920 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.16 pro=44 1a=False 1b=False 2=True (84.1s)
Sep 14 03:12:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:12:37,204 main INFO screen sling pass=0 dev=0.0 ins=33.44 pro=65 1a=False 1b=False 2=True (74.9s)
Sep 14 03:13:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:02,070 main INFO screen TESSERACT pass=1 dev=0.0 ins=3.01 pro=16 1a=False 1b=False 2=False (81.9s)
Sep 14 03:13:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:33,539 main INFO screen BRAINMUSK pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (64.6s)
Sep 14 03:13:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:13:53,425 main INFO screen STRAWDOG pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (76.2s)
Sep 14 03:14:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:14:12,494 main INFO screen Bank pass=0 dev=0.0 ins=27.83 pro=50 1a=False 1b=False 2=True (70.4s)
Sep 14 03:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:14:51,356 main INFO screen MWG pass=1 dev=0.0 ins=7.58 pro=62 1a=False 1b=False 2=False (77.8s)
Sep 14 03:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:13,932 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (80.5s)
Sep 14 03:15:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:17,414 main INFO screen $tOp pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.9s)
Sep 14 03:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:15:36,351 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:15:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:01,315 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (70.0s)
Sep 14 03:16:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:11,879 main INFO screen SOLLADY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 14 03:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:16:18,908 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.5s)
Sep 14 03:17:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:14,081 main INFO screen vrl pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (72.8s)
Sep 14 03:17:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:26,544 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (74.7s)
Sep 14 03:17:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:17:33,007 main INFO screen BOB pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (74.1s)
Sep 14 03:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:23,353 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (69.3s)
Sep 14 03:18:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:26,734 main INFO screen Trump pass=0 dev=50.78 ins=0.0 pro=1 1a=False 1b=False 2=True (60.2s)
Sep 14 03:18:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:18:29,081 main INFO screen ECTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.1s)
Sep 14 03:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:35,927 main INFO screen TESSERACT pass=1 dev=0.0 ins=0.0 pro=33 1a=False 1b=False 2=False (72.6s)
Sep 14 03:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:35,933 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.2s)
Sep 14 03:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:19:38,709 main INFO screen FASTER. PU pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (69.6s)
Sep 14 03:20:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:20:37,572 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:20:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T01:54:26Z
--- update 2026-09-14T01:59:32Z
--- update 2026-09-14T02:04:36Z
--- update 2026-09-14T02:09:37Z
--- update 2026-09-14T02:14:44Z
--- update 2026-09-14T02:19:48Z
--- update 2026-09-14T02:24:49Z
--- update 2026-09-14T02:29:58Z
--- update 2026-09-14T02:34:59Z
--- update 2026-09-14T02:40:05Z
--- update 2026-09-14T02:45:08Z
--- update 2026-09-14T02:50:18Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5c723321a25a43918dd7f5917cca7869
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T02:55:19Z
--- update 2026-09-14T03:00:19Z
--- update 2026-09-14T03:05:21Z
--- update 2026-09-14T03:10:24Z
--- update 2026-09-14T03:15:35Z
--- update 2026-09-14T03:20:36Z
```

## Analyses (laatste 25 regels)
```
active
02:55:31 klaar in 312s -> /opt/schaduwbot/reports/ledger.md
03:02:20 S1: gezakt — toets n=14608, verkennend n=14656
03:02:20 klaar in 409s -> /opt/schaduwbot/reports/hypotheses.md
03:02:20 probe: 0 transacties ophalen
03:03:01 poolveld: 0 pools bekeken, 0 te gaan -> vastgesteld @43
03:04:14 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
03:04:14 prijsijk: n=89 -> mediane afwijking 100% boven 25%
03:04:15 na-migratie: 100 paren te checken
03:06:20 na-migratie: 75 paren, 20 prijzen
03:10:38 gemigreerde koersen: 96 gedaan, 1690 te gaan
03:10:39 klaar (494 rpc-calls, 65 fouten)
03:18:07 klaar in 448s -> /opt/schaduwbot/reports/lotgevallen.md
03:18:25   2000 nieuwe tokens doorgerekend
03:18:49 klaar in 42s: 42358 tokens, 2417 nieuw -> /opt/schaduwbot/reports/video_replay.md
03:18:50 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-11 03:18 UTC
03:18:53 95589 tokens geladen
03:19:04   2000 tokens, 180680 trades, 19747 posities (10s)
03:19:16   4000 tokens, 415943 trades, 60641 posities (23s)
03:19:25   6000 tokens, 620818 trades, 84053 posities (32s)
03:19:34   8000 tokens, 811652 trades, 107073 posities (41s)
03:19:45   10000 tokens, 1008956 trades, 134687 posities (51s)
03:19:55   12000 tokens, 1214468 trades, 161700 posities (62s)
03:20:06   14000 tokens, 1418576 trades, 183676 posities (73s)
03:20:17   16000 tokens, 1615270 trades, 205493 posities (84s)
03:20:27   18000 tokens, 1796146 trades, 228523 posities (94s)
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
