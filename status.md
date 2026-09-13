# Schaduwbot status

- tijd: 2026-09-13 23:34:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 9 hours, 47 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.1G/38G | geheugen: 1994/3814 MB

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
Sep 13 23:03:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:03:45,756 main INFO screen DICKOWEEN pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (79.1s)
Sep 13 23:03:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:03:46,315 main INFO screen MILLI pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (79.1s)
Sep 13 23:04:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:04:14,065 main INFO screen BUTTHOLE pass=0 dev=0.0 ins=22.91 pro=47 1a=False 1b=False 2=True (66.7s)
Sep 13 23:04:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:04:57,730 main INFO screen TCAT pass=0 dev=0.0 ins=23.59 pro=48 1a=False 1b=False 2=False (71.4s)
Sep 13 23:04:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:04:58,432 main INFO screen bonke pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (72.7s)
Sep 13 23:05:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:05:20,471 main INFO screen SOL pass=0 dev=0.0 ins=26.82 pro=51 1a=False 1b=False 2=True (66.4s)
Sep 13 23:06:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:06:02,198 main INFO screen TCAT pass=0 dev=0.0 ins=9.75 pro=59 1a=False 1b=False 2=True (64.5s)
Sep 13 23:06:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:06:21,244 main INFO screen SOL pass=0 dev=15.18 ins=3.75 pro=25 1a=False 1b=False 2=False (60.8s)
Sep 13 23:06:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:06:22,799 main INFO screen $TOGO pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (84.4s)
Sep 13 23:07:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:07:21,028 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (78.8s)
Sep 13 23:07:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:07:28,219 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (65.4s)
Sep 13 23:07:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:07:41,428 main INFO screen popdog pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (80.2s)
Sep 13 23:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:08:37,317 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:08:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:08:37,458 main INFO screen Peccy pass=0 dev=0.0 ins=16.62 pro=62 1a=False 1b=False 2=True (76.4s)
Sep 13 23:08:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:08:41,621 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (73.4s)
Sep 13 23:08:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:08:53,103 main INFO screen TITTIES pass=0 dev=0.0 ins=44.18 pro=85 1a=False 1b=False 2=True (71.7s)
Sep 13 23:09:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:09:46,817 main INFO screen mmrich pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (65.2s)
Sep 13 23:09:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:09:56,205 main INFO screen     YMON pass=0 dev=6.49 ins=0.0 pro=13 1a=False 1b=False 2=False (78.7s)
Sep 13 23:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:09:58,441 main INFO screen BTC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (65.3s)
Sep 13 23:10:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:10:41,842 main INFO screen DIH pass=0 dev=0.0 ins=63.96 pro=16 1a=False 1b=False 2=True (55.0s)
Sep 13 23:11:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:11:06,841 main INFO screen anorchia pass=0 dev=0.0 ins=14.53 pro=45 1a=False 1b=False 2=True (68.4s)
Sep 13 23:11:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:11:10,465 main INFO screen MOREGAIN pass=1 dev=0.0 ins=16.6 pro=41 1a=False 1b=False 2=False (74.3s)
Sep 13 23:11:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:11:48,409 main INFO screen NINTOK pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (66.6s)
Sep 13 23:12:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:12:24,773 main INFO screen UNIDROP pass=0 dev=63.89 ins=0.0 pro=4 1a=False 1b=False 2=True (74.3s)
Sep 13 23:12:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:12:26,304 main INFO screen GRILL pass=1 dev=0.0 ins=0.02 pro=47 1a=False 1b=False 2=False (79.5s)
Sep 13 23:13:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:13:06,837 main INFO screen FAZO pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (78.4s)
Sep 13 23:13:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:13:41,812 main INFO screen TITTIES pass=0 dev=0.0 ins=45.35 pro=73 1a=False 1b=False 2=True (75.5s)
Sep 13 23:13:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:13:45,147 main INFO screen bruh pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (80.4s)
Sep 13 23:13:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:13:56,894 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:13:56 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:14:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:14:09,448 main INFO screen fries pass=0 dev=0.0 ins=15.8 pro=13 1a=False 1b=False 2=True (62.6s)
Sep 13 23:15:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:15:06,195 main INFO screen ROMAN pass=0 dev=0.0 ins=15.92 pro=44 1a=False 1b=False 2=True (81.0s)
Sep 13 23:15:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:15:07,067 main INFO screen ZITTIES pass=0 dev=41.04 ins=0.0 pro=12 1a=False 1b=False 2=False (85.3s)
Sep 13 23:15:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:15:24,017 main INFO screen ASTRO pass=0 dev=0.0 ins=16.43 pro=41 1a=False 1b=False 2=True (74.6s)
Sep 13 23:16:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:16:03,919 main INFO screen testicles pass=0 dev=0.0 ins=1.09 pro=3 1a=False 1b=False 2=True (56.9s)
Sep 13 23:16:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:16:25,603 main INFO screen MCDS pass=1 dev=0.0 ins=3.71 pro=68 1a=False 1b=False 2=False (79.4s)
Sep 13 23:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:16:29,433 main INFO screen WORLD pass=0 dev=0.0 ins=58.55 pro=67 1a=False 1b=False 2=True (65.4s)
Sep 13 23:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:16:53,707 main INFO screen copycat pass=0 dev=0.0 ins=5.91 pro=23 1a=False 1b=False 2=True (49.8s)
Sep 13 23:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:17:15,187 main INFO screen MCLRN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.6s)
Sep 13 23:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:17:38,690 main INFO screen GPT pass=1 dev=0.0 ins=1.88 pro=60 1a=False 1b=False 2=False (69.3s)
Sep 13 23:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:17:40,102 main INFO screen copycat pass=0 dev=0.0 ins=5.51 pro=38 1a=False 1b=False 2=True (46.4s)
Sep 13 23:18:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:18:10,128 main INFO screen DIH pass=0 dev=0.0 ins=65.07 pro=18 1a=False 1b=False 2=True (54.9s)
Sep 13 23:18:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:18:50,940 main INFO screen MCDOG pass=1 dev=0.0 ins=0.21 pro=11 1a=False 1b=False 2=False (70.8s)
Sep 13 23:18:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:18:51,810 main INFO screen VOID pass=0 dev=43.8 ins=0.0 pro=4 1a=False 1b=False 2=True (73.1s)
Sep 13 23:19:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:19:13,312 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:19:13 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:19:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:19:18,374 main INFO screen BOOBS pass=1 dev=0.0 ins=5.92 pro=51 1a=False 1b=False 2=False (68.2s)
Sep 13 23:19:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:19:44,211 main INFO screen TWINE pass=0 dev=0.0 ins=14.86 pro=34 1a=False 1b=False 2=True (53.3s)
Sep 13 23:20:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:20:05,136 main INFO screen 100 pass=0 dev=0.94 ins=0.0 pro=4 1a=False 1b=False 2=False (73.3s)
Sep 13 23:20:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:20:24,367 main INFO screen TITTIES pass=0 dev=0.0 ins=52.75 pro=34 1a=False 1b=False 2=True (66.0s)
Sep 13 23:20:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:20:42,289 main INFO screen ANWH pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (58.1s)
Sep 13 23:20:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:20:53,440 main INFO screen copycat pass=0 dev=0.0 ins=5.51 pro=22 1a=False 1b=False 2=True (48.3s)
Sep 13 23:21:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:21:32,353 main INFO screen MCLRN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.0s)
Sep 13 23:21:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:21:52,879 main INFO screen Yuki pass=1 dev=0.0 ins=13.34 pro=55 1a=False 1b=False 2=False (70.6s)
Sep 13 23:21:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:21:57,897 main INFO screen mimi pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.5s)
Sep 13 23:22:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:22:36,444 aiohttp.access INFO 138.68.153.47 [13/Sep/2026:23:22:36 +0000] "GET /aaa9 HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 13 23:22:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:22:39,375 aiohttp.access INFO 138.68.153.47 [13/Sep/2026:23:22:39 +0000] "GET /aab8 HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 13 23:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:22:42,524 main INFO screen BTC pass=1 dev=2.18 ins=4.95 pro=56 1a=False 1b=False 2=False (65.6s)
Sep 13 23:22:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:22:50,625 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.2s)
Sep 13 23:22:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:22:53,102 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
Sep 13 23:23:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:23:32,567 main INFO screen UPOWEEN pass=1 dev=0.0 ins=9.89 pro=30 1a=False 1b=False 2=False (50.0s)
Sep 13 23:24:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:24:18,526 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:24:18 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:24:35,849 main INFO screen Chud pass=0 dev=0.0 ins=28.53 pro=66 1a=False 1b=False 2=True (70.2s)
Sep 13 23:25:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:25:06,154 main INFO screen SEND pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (74.0s)
Sep 13 23:25:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:25:45,940 main INFO screen INU pass=0 dev=0.0 ins=16.38 pro=56 1a=False 1b=False 2=True (79.2s)
Sep 13 23:25:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:25:47,642 main INFO screen AI pass=0 dev=99.29 ins=0.0 pro=1 1a=False 1b=False 2=True (71.8s)
Sep 13 23:26:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:26:24,288 main INFO screen CABAL pass=1 dev=0.0 ins=1.79 pro=31 1a=False 1b=False 2=False (77.0s)
Sep 13 23:28:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:28:16,310 aiohttp.access INFO 205.210.31.95 [13/Sep/2026:23:28:16 +0000] "GET / HTTP/1.1" 404 174 "-" "Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity"
Sep 13 23:29:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:29:10,015 main INFO screen MSGA pass=0 dev=0.0 ins=36.4 pro=58 1a=False 1b=False 2=True (68.1s)
Sep 13 23:29:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:29:21,266 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:29:21 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:29:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:29:58,663 main INFO screen Pair pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (69.9s)
Sep 13 23:30:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:30:12,028 main INFO screen Fred pass=1 dev=3.76 ins=4.67 pro=61 1a=False 1b=False 2=False (71.7s)
Sep 13 23:30:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:30:16,785 main INFO screen peccy pass=0 dev=0.2 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 13 23:30:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:30:55,864 main INFO screen Flybook pass=0 dev=0.0 ins=22.37 pro=44 1a=False 1b=False 2=True (57.2s)
Sep 13 23:31:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:31:08,635 main INFO screen $FLYHIGH pass=0 dev=0.13 ins=0.0 pro=3 1a=False 1b=False 2=False (56.6s)
Sep 13 23:31:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:31:21,444 main INFO screen DONGINOS pass=0 dev=0.29 ins=0.0 pro=5 1a=False 1b=False 2=False (64.7s)
Sep 13 23:31:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:31:50,638 main INFO screen DIAMOND pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 13 23:32:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:32:21,076 main INFO screen npc pass=0 dev=0.0 ins=1.46 pro=66 1a=False 1b=False 2=True (72.4s)
Sep 13 23:32:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:32:29,866 main INFO screen HACHIMI pass=0 dev=0.0 ins=28.44 pro=21 1a=False 1b=False 2=False (68.4s)
Sep 13 23:33:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:33:02,612 main INFO screen MONKEY pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (72.0s)
Sep 13 23:33:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:33:29,723 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:23:33:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 23:33:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:33:31,404 main INFO screen TRIN pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (70.3s)
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T22:07:38Z
--- update 2026-09-13T22:12:49Z
--- update 2026-09-13T22:18:02Z
--- update 2026-09-13T22:23:04Z
--- update 2026-09-13T22:28:11Z
--- update 2026-09-13T22:33:12Z
--- update 2026-09-13T22:38:16Z
--- update 2026-09-13T22:43:17Z
Running as unit: schaduwbot-wallets.service; invocation ID: bacba8bde01940a1872493ea161ca641
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T22:48:19Z
--- update 2026-09-13T22:53:31Z
--- update 2026-09-13T22:58:32Z
--- update 2026-09-13T23:03:34Z
--- update 2026-09-13T23:08:36Z
--- update 2026-09-13T23:13:55Z
--- update 2026-09-13T23:19:11Z
--- update 2026-09-13T23:24:17Z
--- update 2026-09-13T23:29:20Z
--- update 2026-09-13T23:34:26Z
```

## Analyses (laatste 25 regels)
```
inactive
23:13:05   26000 tokens, 2714180 trades, 375056 posities (140s)
23:13:17   28000 tokens, 2910347 trades, 398449 posities (152s)
23:13:28   30000 tokens, 3111752 trades, 425877 posities (163s)
23:13:41   32000 tokens, 3340745 trades, 458038 posities (176s)
23:13:53   34000 tokens, 3553363 trades, 489464 posities (188s)
23:14:05   36000 tokens, 3751673 trades, 513567 posities (200s)
23:14:16   38000 tokens, 3925965 trades, 534663 posities (212s)
23:14:30   40000 tokens, 4152994 trades, 570806 posities (226s)
23:14:42   42000 tokens, 4348336 trades, 595664 posities (237s)
23:14:53   44000 tokens, 4548599 trades, 621351 posities (248s)
23:15:05   46000 tokens, 4751977 trades, 646323 posities (260s)
23:15:17   48000 tokens, 4947857 trades, 676731 posities (273s)
23:15:30   50000 tokens, 5152223 trades, 704551 posities (286s)
23:15:42   52000 tokens, 5327073 trades, 727800 posities (297s)
23:15:53   54000 tokens, 5528435 trades, 756055 posities (309s)
23:16:05   56000 tokens, 5741491 trades, 787436 posities (320s)
23:16:15   58000 tokens, 5949257 trades, 815855 posities (330s)
23:16:24   60000 tokens, 6158655 trades, 848573 posities (339s)
23:16:34   62000 tokens, 6378507 trades, 891082 posities (349s)
23:16:43 posities: 913444 uit 6542295 trades (361s)
23:16:54 192830 wallets gerekend
23:16:54 geluk-toets
23:17:26 persistentie
23:17:28 kopieer-simulatie
23:19:10 klaar in 508s -> /opt/schaduwbot/reports/wallets.md
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
