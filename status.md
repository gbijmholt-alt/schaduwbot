# Schaduwbot status

- tijd: 2026-09-13 13:34:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 23 hours, 47 minutes
- bot-service: active
- code-versie: 6977315
- schijf: 4.6G/38G | geheugen: 1148/3814 MB

## Health
```json
(niet bereikbaar: timed out)
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
Sep 13 13:02:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:11,599 main INFO screen CATacombs pass=1 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (72.6s)
Sep 13 13:02:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:12,812 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.3s)
Sep 13 13:02:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:29,287 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:02:29 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 13:02:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:55,137 main INFO screen PONS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 13 13:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:03:26,315 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (74.7s)
Sep 13 13:03:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:03:29,267 main INFO screen titties pass=0 dev=4.6 ins=0.0 pro=3 1a=False 1b=False 2=False (76.5s)
Sep 13 13:04:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:08,642 main INFO screen IF ONLY pass=1 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=False (73.5s)
Sep 13 13:04:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:35,153 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.8s)
Sep 13 13:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:46,767 main INFO screen CRIP pass=1 dev=0.0 ins=0.9 pro=51 1a=False 1b=False 2=False (77.5s)
Sep 13 13:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:22,391 main INFO screen MoonDoor pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (73.7s)
Sep 13 13:05:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:34,219 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.1s)
Sep 13 13:05:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:52,151 main INFO screen KAT pass=0 dev=0.0 ins=78.87 pro=6 1a=False 1b=False 2=True (65.4s)
Sep 13 13:06:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:06:40,604 main INFO screen ANAI pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (78.2s)
Sep 13 13:06:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:06:47,337 main INFO screen NASHOUSE pass=0 dev=0.32 ins=78.99 pro=5 1a=False 1b=False 2=True (73.1s)
Sep 13 13:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:04,012 main INFO screen BeachOrca pass=0 dev=0.0 ins=55.86 pro=44 1a=False 1b=False 2=True (71.9s)
Sep 13 13:07:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:37,372 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:07:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:07:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:47,046 main INFO screen P.I.P.O pass=0 dev=3.24 ins=0.0 pro=1 1a=False 1b=False 2=False (66.4s)
Sep 13 13:07:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:53,152 main INFO screen LYNK pass=1 dev=0.0 ins=0.66 pro=48 1a=False 1b=False 2=False (65.8s)
Sep 13 13:08:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:08:03,020 main INFO screen RST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.0s)
Sep 13 13:08:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:08:43,477 main INFO screen NSTT pass=1 dev=0.0 ins=0.16 pro=49 1a=False 1b=False 2=False (56.4s)
Sep 13 13:08:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:08:51,551 main INFO screen BIGPLANE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.4s)
Sep 13 13:09:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:09:11,019 main INFO screen $AURA pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (68.0s)
Sep 13 13:10:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:10:06,269 main INFO screen GCAT pass=1 dev=0.0 ins=1.16 pro=57 1a=False 1b=False 2=False (82.8s)
Sep 13 13:10:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:10:10,065 main INFO screen $GTA6 pass=0 dev=0.0 ins=1.21 pro=1 1a=False 1b=False 2=False (78.5s)
Sep 13 13:10:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:10:19,196 aiohttp.access INFO 154.219.127.248 [13/Sep/2026:13:10:19 +0000] "GET /api/getSetting HTTP/1.0" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
Sep 13 13:10:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:10:24,682 main INFO screen BAWU pass=0 dev=0.0 ins=28.54 pro=72 1a=False 1b=False 2=True (73.7s)
Sep 13 13:11:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:11:12,753 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.5s)
Sep 13 13:11:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:11:27,483 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (77.4s)
Sep 13 13:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:11:43,321 main INFO screen ANAI pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (78.6s)
Sep 13 13:12:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:12:23,849 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.1s)
Sep 13 13:12:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:12:37,326 main INFO screen MOKOA pass=0 dev=0.0 ins=31.18 pro=42 1a=False 1b=True 2=True (69.8s)
Sep 13 13:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:12:49,707 main INFO screen VOID pass=0 dev=43.8 ins=0.0 pro=3 1a=False 1b=False 2=True (66.4s)
Sep 13 13:13:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:13:14,363 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:13:14 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:13:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:13:33,521 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (60.3s)
Sep 13 13:14:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:14:15,997 main INFO screen AI MEME pass=0 dev=0.0 ins=61.89 pro=60 1a=False 1b=False 2=True (68.8s)
Sep 13 13:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:15:13,574 main INFO screen TRUMPGOLF pass=1 dev=0.69 ins=0.0 pro=16 1a=False 1b=False 2=False (78.8s)
Sep 13 13:15:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:15:16,814 main INFO screen BeachCroc pass=0 dev=1.74 ins=55.73 pro=34 1a=False 1b=False 2=True (88.8s)
Sep 13 13:15:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:15:43,321 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.0s)
Sep 13 13:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:16:31,730 main INFO screen $MSQTO pass=0 dev=0.02 ins=0.0 pro=5 1a=False 1b=False 2=False (78.2s)
Sep 13 13:16:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:16:47,904 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.4s)
Sep 13 13:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:17:28,316 main INFO screen taxless pass=0 dev=0.0 ins=7.81 pro=70 1a=False 1b=False 2=True (80.5s)
Sep 13 13:17:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:17:49,631 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.7s)
Sep 13 13:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:17:52,182 main INFO screen ORCL pass=0 dev=0.0 ins=62.52 pro=67 1a=False 1b=False 2=True (80.5s)
Sep 13 13:18:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:18:30,286 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:18:30 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 13:18:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:18:31,258 main INFO screen LOBSTER pass=0 dev=0.0 ins=26.56 pro=70 1a=False 1b=False 2=True (62.9s)
Sep 13 13:18:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:18:50,151 main INFO screen LOBSTER pass=0 dev=0.0 ins=28.84 pro=48 1a=False 1b=False 2=True (58.0s)
Sep 13 13:18:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:18:54,256 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (64.6s)
Sep 13 13:19:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:19:27,843 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 13 13:19:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:19:44,764 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.6s)
Sep 13 13:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:19:55,859 main INFO screen ZEBRAFISH pass=0 dev=0.0 ins=14.76 pro=64 1a=False 1b=False 2=True (61.6s)
Sep 13 13:20:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:20:38,596 main INFO screen CrackyCat pass=1 dev=0.11 ins=0.0 pro=20 1a=False 1b=False 2=False (70.8s)
Sep 13 13:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:21:01,544 main INFO screen CRASHOUT pass=0 dev=0.0 ins=37.33 pro=74 1a=False 1b=False 2=True (65.7s)
Sep 13 13:21:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:21:02,454 main INFO screen MEMEVERSE pass=0 dev=0.0 ins=62.58 pro=64 1a=False 1b=False 2=True (77.7s)
Sep 13 13:21:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:21:38,687 main INFO screen DOGE pass=0 dev=0.32 ins=0.0 pro=3 1a=False 1b=False 2=False (60.1s)
Sep 13 13:21:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:21:59,026 main INFO screen AI MEME pass=0 dev=5.0 ins=0.0 pro=48 1a=False 1b=True 2=False (56.6s)
Sep 13 13:22:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:22:01,483 main INFO screen $GTA6 pass=0 dev=0.0 ins=3.06 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 13 13:22:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:22:29,869 main INFO screen ソル pass=0 dev=0.0 ins=20.78 pro=67 1a=False 1b=False 2=False (51.2s)
Sep 13 13:23:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:23:11,467 main INFO screen HOMELESS pass=1 dev=0.0 ins=14.0 pro=60 1a=False 1b=False 2=False (72.4s)
Sep 13 13:23:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:23:11,734 main INFO screen Evader pass=0 dev=0.0 ins=16.42 pro=69 1a=False 1b=False 2=True (68.3s)
Sep 13 13:23:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:23:37,405 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:23:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:24:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:24:13,777 main INFO screen Shakeass pass=1 dev=0.0 ins=1.63 pro=18 1a=False 1b=False 2=False (56.2s)
Sep 13 13:24:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:24:29,222 main INFO screen $CD-R pass=0 dev=0.01 ins=0.0 pro=7 1a=False 1b=False 2=False (65.4s)
Sep 13 13:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:24:47,047 main INFO screen RICK pass=1 dev=0.21 ins=0.0 pro=10 1a=False 1b=False 2=False (71.0s)
Sep 13 13:25:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:25:29,102 main INFO screen DOJI pass=0 dev=0.0 ins=31.75 pro=33 1a=False 1b=True 2=True (61.2s)
Sep 13 13:26:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:26:00,831 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (69.0s)
Sep 13 13:26:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:26:47,505 main INFO screen STKBCAT pass=0 dev=1.05 ins=78.26 pro=3 1a=False 1b=True 2=True (54.2s)
Sep 13 13:27:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:27:12,239 main INFO screen OS pass=0 dev=0.0 ins=24.71 pro=64 1a=False 1b=False 2=True (65.5s)
Sep 13 13:27:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:27:55,611 main INFO screen PC pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (57.2s)
Sep 13 13:28:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:28:11,135 main INFO screen MIZO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 13 13:28:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:28:12,241 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.6s)
Sep 13 13:28:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:28:50,285 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:28:50 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 13:29:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:29:29,317 main INFO screen JUBJUBMASK pass=0 dev=0.25 ins=79.06 pro=7 1a=False 1b=True 2=True (54.1s)
Sep 13 13:29:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:29:39,967 main INFO screen TRUMPx pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 13 13:30:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:30:08,570 main INFO screen 34% pass=0 dev=0.62 ins=0.0 pro=4 1a=False 1b=False 2=False (70.2s)
Sep 13 13:30:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:30:38,603 main INFO screen TH3000 pass=0 dev=0.0 ins=28.98 pro=28 1a=False 1b=False 2=True (63.5s)
Sep 13 13:31:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:31:43,400 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=5 1a=False 1b=False 2=False (64.7s)
Sep 13 13:32:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:32:02,077 main INFO screen $DINGUS pass=0 dev=0.88 ins=0.0 pro=5 1a=False 1b=False 2=False (67.8s)
Sep 13 13:32:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:32:06,312 main INFO screen Runnooor pass=1 dev=0.29 ins=5.64 pro=52 1a=False 1b=False 2=False (71.6s)
Sep 13 13:33:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:33:25,430 main INFO screen Buddy pass=0 dev=0.0 ins=25.36 pro=43 1a=False 1b=False 2=True (62.1s)
Sep 13 13:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:34:08,532 main INFO screen hookahfly pass=0 dev=0.0 ins=16.3 pro=56 1a=False 1b=False 2=True (65.4s)
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T12:35:38Z
--- update 2026-09-13T12:40:48Z
--- update 2026-09-13T12:46:14Z
--- update 2026-09-13T12:51:36Z
--- update 2026-09-13T12:57:24Z
--- update 2026-09-13T13:02:27Z
nieuwe code: 4a93173
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: be001e47867c4d53bf64f959d70cd386
analyses gestart (00feb5de9af9)
--- update 2026-09-13T13:07:36Z
--- update 2026-09-13T13:13:13Z
--- update 2026-09-13T13:18:29Z
nieuwe code: 6977315
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T13:23:36Z
--- update 2026-09-13T13:28:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: 6b131609667c446db5ee762a2a7e18b8
analyses gestart (29fd1f8386bc)
--- update 2026-09-13T13:34:14Z
```

## Analyses (laatste 25 regels)
```
active
13:23:33   42000 tokens, 4674447 trades, 745068 posities (80s)
13:23:37   44000 tokens, 4880081 trades, 778597 posities (84s)
13:23:43   46000 tokens, 5099629 trades, 814529 posities (90s)
13:23:49   48000 tokens, 5336345 trades, 854455 posities (96s)
13:23:54   50000 tokens, 5558289 trades, 889528 posities (101s)
13:24:00   52000 tokens, 5788575 trades, 935768 posities (107s)
13:24:04   54000 tokens, 5988638 trades, 976141 posities (111s)
13:24:05 posities: 981921 uit 6008773 trades (112s)
13:24:18 201876 wallets gerekend
13:24:19 geluk-toets
13:24:53 persistentie
13:24:55 kopieer-simulatie
13:25:39 klaar in 206s -> /opt/schaduwbot/reports/wallets.md
13:28:50 53383 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
13:28:55   ingelezen tot rowid 6021052 (42846 rijen, 42846 bruikbaar)
13:28:56 ingelezen: 42846 nieuwe trades, 42846 bruikbaar (6s)
13:29:54 1328 aankopen van gevolgde wallets geëvalueerd
13:30:09 vroege kopers: 174 voldoen nu, register 286, 46 tokens beoordeeld
13:30:23 grote spelers: saldo van 50 wallets opgehaald
13:30:48 herkomst: 40 posities gekoppeld
13:30:53 klaar in 124s -> /opt/schaduwbot/reports/ledger.md
13:32:01 S1: gezakt — toets n=6596, verkennend n=14656
13:32:01 klaar in 67s -> /opt/schaduwbot/reports/hypotheses.md
13:34:16 klaar in 135s -> /opt/schaduwbot/reports/lotgevallen.md
13:34:16 probe: 150 transacties ophalen
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
