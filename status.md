# Schaduwbot status

- tijd: 2026-09-12 23:31:07 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 9 hours, 44 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.0G/38G | geheugen: 1013/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 10639, "tokens_in_memory": 4152, "msgs": 1173274, "trades": 376938, "creates": 4152, "decode_fail": 31819, "rpc_calls": 9303, "rpc_errors": 1, "sol_usd": 101.73936641708087, "open_positions": 81, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 21122 | 2763 | 15 | 2763 | 214 | 4904 | 14642 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 586 | 16% | 1.7% | +43.5% | -16.0% | -6.25% | 100% |
| dip35_V1_gescreend_fail | 4654 | 27% | 3.9% | +45.3% | -26.0% | -6.74% | 100% |
| dip35_V1_alle | 5918 | 26% | 4.0% | +44.4% | -25.5% | -7.03% | 100% |
| dip35_V2_gescreend_pass | 583 | 22% | 2.4% | +40.7% | -20.3% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 4710 | 25% | 4.4% | +54.8% | -28.1% | -7.08% | 100% |
| dip35_V2_alle | 5877 | 25% | 4.6% | +52.4% | -27.8% | -7.92% | 100% |
| dip35_V3_gescreend_pass | 586 | 9% | 2.9% | +263.0% | -22.1% | +4.16% | 100% |
| dip35_V3_gescreend_fail | 4820 | 14% | 6.1% | +114.4% | -29.8% | -10.14% | 100% |
| dip35_V3_alle | 5931 | 13% | 6.1% | +116.5% | -29.4% | -10.13% | 100% |
| dip40_V1_gescreend_pass | 555 | 14% | 1.8% | +44.7% | -15.5% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 4573 | 26% | 3.9% | +46.8% | -25.9% | -6.60% | 100% |
| dip40_V1_alle | 5688 | 26% | 3.9% | +46.4% | -25.3% | -6.95% | 100% |
| dip40_V2_gescreend_pass | 553 | 18% | 2.2% | +43.3% | -19.5% | -8.51% | 100% |
| dip40_V2_gescreend_fail | 4602 | 25% | 4.3% | +54.7% | -28.0% | -7.06% | 100% |
| dip40_V2_alle | 5641 | 24% | 4.5% | +52.9% | -27.7% | -8.07% | 100% |
| dip40_V3_gescreend_pass | 556 | 8% | 2.5% | +255.8% | -21.0% | +1.37% | 100% |
| dip40_V3_gescreend_fail | 4699 | 13% | 5.9% | +109.4% | -29.5% | -11.13% | 100% |
| dip40_V3_alle | 5695 | 13% | 5.9% | +111.5% | -29.2% | -11.15% | 100% |
| dip45_V1_gescreend_pass | 531 | 14% | 1.7% | +47.4% | -15.3% | -6.22% | 100% |
| dip45_V1_gescreend_fail | 4486 | 27% | 3.6% | +48.2% | -25.7% | -5.46% | 100% |
| dip45_V1_alle | 5498 | 26% | 3.6% | +48.2% | -25.1% | -5.96% | 100% |
| dip45_V2_gescreend_pass | 528 | 18% | 2.1% | +42.7% | -19.5% | -8.22% | 100% |
| dip45_V2_gescreend_fail | 4506 | 25% | 4.1% | +57.6% | -27.7% | -6.10% | 100% |
| dip45_V2_alle | 5452 | 24% | 4.2% | +56.3% | -27.4% | -7.01% | 100% |
| dip45_V3_gescreend_pass | 531 | 8% | 2.1% | +296.6% | -20.3% | +4.72% | 100% |
| dip45_V3_gescreend_fail | 4589 | 14% | 5.5% | +116.9% | -29.1% | -8.85% | 100% |
| dip45_V3_alle | 5498 | 13% | 5.5% | +121.4% | -28.7% | -8.89% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 459 | 15% | 5.0% | -9.15% | -11.9% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 133 | 21% | 0.0% | +17.74% | -12.5% tot +48.0% | -13.2% | 131% | 55% |
| gepoold_met_xlink | 3870 | 13% | 2.8% | -9.70% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1139 | 18% | 0.0% | +17.08% | -0.1% tot +34.2% | -14.6% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 23:03:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:03:12,222 main INFO screen sol pass=0 dev=0.69 ins=0.0 pro=5 1a=False 1b=False 2=False (78.8s)
Sep 12 23:03:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:03:38,342 main INFO screen McFly pass=0 dev=0.0 ins=36.03 pro=33 1a=False 1b=False 2=True (77.7s)
Sep 12 23:04:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:04:09,151 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.2s)
Sep 12 23:04:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:04:22,496 main INFO screen Okha pass=0 dev=0.0 ins=17.43 pro=66 1a=False 1b=False 2=True (70.3s)
Sep 12 23:04:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:04:34,664 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.3s)
Sep 12 23:05:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:05:17,199 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:05:17 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 23:05:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:05:22,436 main INFO screen Ghost pass=1 dev=1.07 ins=0.58 pro=55 1a=False 1b=False 2=False (73.3s)
Sep 12 23:05:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:05:38,521 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.0s)
Sep 12 23:05:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:05:42,295 main INFO screen batontrump pass=0 dev=0.14 ins=76.97 pro=7 1a=False 1b=False 2=True (67.6s)
Sep 12 23:06:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:06:30,662 main INFO screen AutiLap pass=0 dev=0.35 ins=59.37 pro=11 1a=False 1b=True 2=True (68.2s)
Sep 12 23:06:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:06:41,980 main INFO screen helpme pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.5s)
Sep 12 23:06:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:06:43,529 main INFO screen BELLA pass=0 dev=0.0 ins=21.91 pro=70 1a=False 1b=False 2=True (61.2s)
Sep 12 23:07:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:07:26,765 main INFO screen Launchpad pass=0 dev=0.0 ins=5.09 pro=28 1a=False 1b=False 2=False (56.1s)
Sep 12 23:07:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:07:58,652 main INFO screen Gobble pass=1 dev=2.59 ins=0.0 pro=69 1a=False 1b=False 2=False (75.1s)
Sep 12 23:07:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:07:59,548 main INFO screen OnlyUp pass=0 dev=0.0 ins=37.71 pro=56 1a=False 1b=False 2=False (77.6s)
Sep 12 23:08:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:08:44,809 main INFO screen CHILLHOUSE pass=1 dev=3.15 ins=0.0 pro=59 1a=False 1b=False 2=False (78.0s)
Sep 12 23:09:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:09:00,099 main INFO screen BAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.4s)
Sep 12 23:09:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:09:04,460 main INFO screen $PVE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (64.9s)
Sep 12 23:09:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:09:42,983 main INFO screen ME&MEMES pass=0 dev=0.31 ins=0.0 pro=3 1a=False 1b=False 2=False (58.2s)
Sep 12 23:10:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:10:05,690 main INFO screen kk pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (65.6s)
Sep 12 23:10:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:10:06,321 main INFO screen 0Bot pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.9s)
Sep 12 23:10:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:10:23,915 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:10:23 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 23:10:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:10:42,331 main INFO screen BOB pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.3s)
Sep 12 23:11:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:11:10,561 main INFO screen SPXW pass=0 dev=0.22 ins=0.0 pro=4 1a=False 1b=False 2=False (64.9s)
Sep 12 23:11:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:11:15,318 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 12 23:11:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:11:39,198 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.9s)
Sep 12 23:11:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:11:57,439 main INFO screen WENDYS pass=0 dev=0.0 ins=13.11 pro=7 1a=False 1b=False 2=False (46.9s)
Sep 12 23:12:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:12:27,957 main INFO screen cap pass=0 dev=0.03 ins=0.0 pro=9 1a=False 1b=False 2=False (72.6s)
Sep 12 23:12:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:12:44,381 main INFO screen Drone pass=0 dev=0.0 ins=45.08 pro=74 1a=False 1b=False 2=True (65.2s)
Sep 12 23:12:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:12:50,857 main INFO screen LIVEIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 12 23:13:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:13:28,489 main INFO screen alphabet pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.5s)
Sep 12 23:13:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:13:44,469 main INFO screen OpenAI pass=0 dev=0.39 ins=78.92 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 12 23:13:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:13:51,933 main INFO screen DUVE pass=1 dev=0.0 ins=1.92 pro=68 1a=False 1b=False 2=False (67.6s)
Sep 12 23:14:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:14:42,769 main INFO screen YO pass=0 dev=24.77 ins=0.0 pro=15 1a=False 1b=False 2=False (74.3s)
Sep 12 23:14:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:14:46,936 main INFO screen DEAD pass=1 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (62.5s)
Sep 12 23:14:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:14:55,375 main INFO screen HALH pass=0 dev=0.0 ins=0.04 pro=3 1a=False 1b=False 2=False (63.4s)
Sep 12 23:15:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:15:31,526 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:15:31 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 23:15:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:15:37,174 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (54.4s)
Sep 12 23:15:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:15:42,517 main INFO screen momo pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (55.6s)
Sep 12 23:15:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:15:55,193 main INFO screen BIRDS pass=0 dev=0.0 ins=17.94 pro=43 1a=False 1b=False 2=True (59.8s)
Sep 12 23:16:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:16:35,236 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (58.1s)
Sep 12 23:16:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:16:54,337 main INFO screen CAT pass=0 dev=0.9 ins=0.0 pro=3 1a=False 1b=False 2=False (71.8s)
Sep 12 23:17:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:17:02,013 main INFO screen CEO pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (66.8s)
Sep 12 23:17:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:17:43,895 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (68.7s)
Sep 12 23:17:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:17:51,923 main INFO screen STONKGPT pass=0 dev=0.35 ins=78.76 pro=6 1a=False 1b=True 2=True (57.6s)
Sep 12 23:18:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:18:12,656 main INFO screen DOOB pass=0 dev=7.5 ins=0.0 pro=8 1a=False 1b=False 2=False (70.6s)
Sep 12 23:18:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:18:55,077 main INFO screen fg pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (71.2s)
Sep 12 23:18:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:18:57,767 main INFO screen Anthropic pass=0 dev=0.0 ins=41.91 pro=1 1a=False 1b=False 2=True (65.8s)
Sep 12 23:19:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:19:12,029 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 12 23:20:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:02,003 main INFO screen SINGLE pass=0 dev=0.0 ins=21.8 pro=57 1a=False 1b=False 2=True (64.2s)
Sep 12 23:20:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:07,574 main INFO screen NOVA pass=0 dev=0.22 ins=0.0 pro=4 1a=False 1b=False 2=False (72.5s)
Sep 12 23:20:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:15,896 aiohttp.access INFO 89.42.231.200 [12/Sep/2026:23:20:15 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 23:20:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:28,879 main INFO screen vrl pass=0 dev=18.08 ins=0.0 pro=1 1a=False 1b=False 2=False (76.9s)
Sep 12 23:20:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:37,099 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:20:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:21:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:06,301 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 12 23:21:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:10,110 main INFO screen MIND pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.5s)
Sep 12 23:21:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:26,322 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.03 pro=23 1a=False 1b=False 2=True (57.4s)
Sep 12 23:22:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:10,948 main INFO screen 400 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 12 23:22:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:15,033 main INFO screen Cagefight pass=1 dev=3.76 ins=0.0 pro=65 1a=False 1b=False 2=False (68.7s)
Sep 12 23:22:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:32,534 main INFO screen DUVAL pass=0 dev=0.0 ins=21.49 pro=52 1a=False 1b=False 2=True (66.2s)
Sep 12 23:23:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:22,112 main INFO screen duluth pass=0 dev=0.0 ins=0.03 pro=3 1a=False 1b=False 2=False (67.1s)
Sep 12 23:23:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:23,462 main INFO screen $speed pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (72.5s)
Sep 12 23:23:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:28,620 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.03 pro=20 1a=False 1b=False 2=True (56.1s)
Sep 12 23:24:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:36,696 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (74.6s)
Sep 12 23:24:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:37,025 main INFO screen MEMPOOLS pass=0 dev=0.0 ins=48.5 pro=22 1a=False 1b=False 2=True (73.6s)
Sep 12 23:24:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:40,061 main INFO screen catsey pass=1 dev=1.25 ins=5.37 pro=45 1a=False 1b=False 2=False (71.4s)
Sep 12 23:25:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:41,205 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:25:41 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:25:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:54,645 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (77.9s)
Sep 12 23:25:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:55,827 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.8s)
Sep 12 23:25:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:56,565 main INFO screen LaMisery pass=0 dev=1.56 ins=0.0 pro=1 1a=False 1b=False 2=False (79.5s)
Sep 12 23:27:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:09,769 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.2s)
Sep 12 23:27:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:12,271 main INFO screen SOR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (76.4s)
Sep 12 23:27:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:12,906 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.62 pro=31 1a=False 1b=False 2=True (78.3s)
Sep 12 23:28:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:43,957 main INFO screen PRIMETIME pass=0 dev=0.0 ins=19.97 pro=36 1a=False 1b=False 2=True (91.1s)
Sep 12 23:28:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:46,013 main INFO screen pray pass=0 dev=8.79 ins=0.0 pro=52 1a=False 1b=False 2=False (93.7s)
Sep 12 23:28:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:48,533 main INFO screen SOLCHAN pass=0 dev=0.0 ins=9.55 pro=62 1a=False 1b=False 2=True (98.8s)
Sep 12 23:30:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:04,191 main INFO screen Desk pass=1 dev=0.0 ins=12.37 pro=21 1a=False 1b=False 2=False (78.2s)
Sep 12 23:30:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:09,197 main INFO screen $GOAT pass=1 dev=0.35 ins=0.0 pro=10 1a=False 1b=False 2=False (85.2s)
Sep 12 23:30:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:10,901 main INFO screen Duluth pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (82.4s)
Sep 12 23:31:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:31:07,702 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:31:07 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T22:02:18Z
--- update 2026-09-12T22:07:20Z
--- update 2026-09-12T22:12:36Z
--- update 2026-09-12T22:18:15Z
--- update 2026-09-12T22:23:36Z
--- update 2026-09-12T22:29:00Z
--- update 2026-09-12T22:34:03Z
--- update 2026-09-12T22:39:27Z
--- update 2026-09-12T22:44:28Z
--- update 2026-09-12T22:49:32Z
--- update 2026-09-12T22:54:36Z
--- update 2026-09-12T22:59:54Z
--- update 2026-09-12T23:05:16Z
--- update 2026-09-12T23:10:22Z
--- update 2026-09-12T23:15:30Z
--- update 2026-09-12T23:20:36Z
--- update 2026-09-12T23:25:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: 4b459aa2bd234295a955bfddf4ef5023
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T23:31:06Z
```

## Analyses (laatste 25 regels)
```
active
21:35:25   28000 tokens, 3243852 trades, 580513 posities (28s)
21:35:27   30000 tokens, 3459040 trades, 615508 posities (30s)
21:35:29   32000 tokens, 3690377 trades, 657198 posities (32s)
21:35:30   34000 tokens, 3910303 trades, 696922 posities (34s)
21:35:33   36000 tokens, 4150741 trades, 742994 posities (36s)
21:35:35   38000 tokens, 4391159 trades, 788453 posities (38s)
21:35:36   40000 tokens, 4609485 trades, 839321 posities (40s)
21:35:37 posities: 846701 uit 4636829 trades (40s)
21:35:48 177416 wallets gerekend
21:35:48 geluk-toets
21:36:20 persistentie
21:36:22 kopieer-simulatie
21:36:33 klaar in 96s -> /opt/schaduwbot/reports/wallets.md
23:25:41 40980 tokens sinds start volledige logging, waarvan 12041 met een gat door herstart
23:25:47   ingelezen tot rowid 4816991 (200000 rijen, 200000 bruikbaar)
23:25:49   ingelezen tot rowid 4885113 (268122 rijen, 268122 bruikbaar)
23:25:49 ingelezen: 268122 nieuwe trades, 268122 bruikbaar (9s)
23:26:28 2329 aankopen van gevolgde wallets geëvalueerd
23:26:39 vroege kopers: 146 voldoen nu, register 230, 233 tokens beoordeeld
23:26:59 grote spelers: saldo van 1464 wallets opgehaald
23:27:24 herkomst: 40 posities gekoppeld
23:27:27 klaar in 107s -> /opt/schaduwbot/reports/ledger.md
23:28:05 S1: gezakt — toets n=1753, verkennend n=14656
23:28:05 klaar in 37s -> /opt/schaduwbot/reports/hypotheses.md
23:28:06 na-migratie: 400 paren te checken
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
