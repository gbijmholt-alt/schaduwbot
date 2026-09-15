# Schaduwbot status

- tijd: 2026-09-15 20:18:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 6 hours, 31 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.6G/38G | geheugen: 2307/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.4, "uptime_s": 222246, "tokens_in_memory": 10604, "msgs": 35383000, "trades": 7074162, "creates": 74998, "decode_fail": 599277, "rpc_calls": 200701, "rpc_errors": 17, "sol_usd": 97.39746577251974, "open_positions": 66, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 19:52:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:52:39,241 main INFO screen $BEERDOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 15 19:53:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:17,993 main INFO screen CPT pass=0 dev=0.0 ins=32.44 pro=30 1a=False 1b=False 2=True (51.2s)
Sep 15 19:53:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:40,640 main INFO screen ZARXU pass=0 dev=0.0 ins=10.51 pro=45 1a=False 1b=False 2=True (66.4s)
Sep 15 19:53:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:53:43,824 main INFO screen SIGIL pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=True (64.6s)
Sep 15 19:54:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:11,828 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (53.8s)
Sep 15 19:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:28,890 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=32.44 pro=17 1a=False 1b=False 2=True (48.2s)
Sep 15 19:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:54:37,288 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.5s)
Sep 15 19:55:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:16,572 main INFO screen pinkfloyd pass=0 dev=0.0 ins=17.59 pro=56 1a=False 1b=False 2=False (64.7s)
Sep 15 19:55:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:34,788 main INFO screen ber pass=0 dev=0.0 ins=37.37 pro=64 1a=False 1b=False 2=True (65.9s)
Sep 15 19:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:55:37,747 main INFO screen YOUR pass=0 dev=0.0 ins=27.96 pro=56 1a=False 1b=False 2=True (60.5s)
Sep 15 19:56:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:10,326 main INFO screen YOUR pass=0 dev=0.0 ins=55.79 pro=37 1a=False 1b=False 2=True (53.8s)
Sep 15 19:56:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:20,883 main INFO screen $CLICK pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (46.1s)
Sep 15 19:56:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:56:24,418 main INFO screen 300008 pass=0 dev=0.0 ins=20.68 pro=0 1a=False 1b=False 2=False (46.7s)
Sep 15 19:57:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:03,246 main INFO screen Signor  pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (52.9s)
Sep 15 19:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:27,799 main INFO screen batcat pass=0 dev=0.0 ins=59.63 pro=60 1a=False 1b=False 2=True (66.9s)
Sep 15 19:57:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:30,653 main INFO screen Paid pass=0 dev=0.0 ins=33.13 pro=60 1a=False 1b=False 2=True (66.2s)
Sep 15 19:57:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:35,443 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:57:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 19:57:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:57:57,870 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.6s)
Sep 15 19:58:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:58:19,456 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (51.7s)
Sep 15 19:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:58:20,827 main INFO screen Microsoft pass=0 dev=0.0 ins=153.2 pro=0 1a=False 1b=False 2=True (50.2s)
Sep 15 19:58:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:58:47,695 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.8s)
Sep 15 19:59:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:59:22,406 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.6s)
Sep 15 19:59:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:59:23,854 main INFO screen DihFish pass=0 dev=0.89 ins=28.62 pro=55 1a=False 1b=False 2=False (64.4s)
Sep 15 19:59:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:59:54,953 main INFO screen CLARITITTY pass=0 dev=0.0 ins=36.24 pro=67 1a=False 1b=False 2=True (67.3s)
Sep 15 20:00:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:00:16,852 main INFO screen CHILL pass=0 dev=0.0 ins=19.37 pro=0 1a=False 1b=False 2=False (54.4s)
Sep 15 20:00:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:00:20,867 main INFO screen Morgano2.0 pass=0 dev=0.0 ins=16.93 pro=51 1a=False 1b=False 2=True (57.0s)
Sep 15 20:01:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:01:02,376 main INFO screen Burnerverse pass=0 dev=0.0 ins=35.59 pro=55 1a=False 1b=False 2=True (67.4s)
Sep 15 20:01:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:01:12,884 main INFO screen SU26 pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (56.0s)
Sep 15 20:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:01:30,442 main INFO screen FOMO pass=0 dev=0.0 ins=33.57 pro=9 1a=False 1b=False 2=True (69.6s)
Sep 15 20:02:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:02:01,552 main INFO screen Clarity pass=0 dev=0.0 ins=29.99 pro=65 1a=False 1b=False 2=True (59.2s)
Sep 15 20:02:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:02:26,308 main INFO screen hope pass=0 dev=0.0 ins=28.17 pro=65 1a=False 1b=False 2=True (73.4s)
Sep 15 20:02:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:02:26,435 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=9.75 pro=59 1a=False 1b=False 2=True (56.0s)
Sep 15 20:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:02:37,259 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:02:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:02:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:02:56,625 main INFO screen Anxiety  pass=0 dev=0.0 ins=39.34 pro=61 1a=False 1b=False 2=True (55.1s)
Sep 15 20:03:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:03:35,691 main INFO screen SOLFLY pass=0 dev=0.0 ins=0.0 pro=56 1a=False 1b=False 2=True (69.4s)
Sep 15 20:03:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:03:37,726 main INFO screen Animaniac pass=0 dev=0.35 ins=0.0 pro=7 1a=False 1b=False 2=False (71.3s)
Sep 15 20:03:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:03:59,824 main INFO screen ROCKET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.2s)
Sep 15 20:04:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:04:44,239 main INFO screen ELONHOUSE pass=0 dev=0.0 ins=19.22 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 15 20:04:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:04:48,759 main INFO screen pinkfloyd pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (73.1s)
Sep 15 20:04:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:04:56,836 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.0s)
Sep 15 20:05:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:05:45,507 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 15 20:05:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:05:56,531 main INFO screen BRUHCAT pass=0 dev=0.32 ins=0.0 pro=13 1a=False 1b=False 2=False (67.8s)
Sep 15 20:05:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:05:57,991 main INFO screen NTDA pass=0 dev=1.18 ins=127.59 pro=1 1a=False 1b=False 2=True (61.2s)
Sep 15 20:06:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:06:34,891 main INFO screen Instantly pass=0 dev=0.0 ins=24.06 pro=2 1a=False 1b=False 2=True (49.4s)
Sep 15 20:07:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:07:05,078 main INFO screen FINE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.1s)
Sep 15 20:07:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:07:06,021 main INFO screen JEET pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (69.5s)
Sep 15 20:07:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:07:45,096 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:07:45 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:07:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:07:45,376 main INFO screen PactAI pass=0 dev=0.0 ins=24.14 pro=3 1a=False 1b=False 2=True (70.5s)
Sep 15 20:08:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:08:13,361 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.3s)
Sep 15 20:08:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:08:15,290 main INFO screen Halphurt pass=0 dev=0.0 ins=0.69 pro=16 1a=False 1b=False 2=False (69.3s)
Sep 15 20:08:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:08:43,720 main INFO screen BUYBUYBUY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.3s)
Sep 15 20:09:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:09:07,808 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=33.87 pro=57 1a=False 1b=False 2=True (52.5s)
Sep 15 20:09:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:09:10,928 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 20:09:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:09:54,992 main INFO screen LEGAL pass=0 dev=0.0 ins=29.37 pro=34 1a=False 1b=False 2=True (71.3s)
Sep 15 20:10:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:10:11,146 main INFO screen DOGE2 pass=0 dev=0.39 ins=58.48 pro=50 1a=False 1b=False 2=True (63.3s)
Sep 15 20:10:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:10:14,452 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.5s)
Sep 15 20:11:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:11:05,571 main INFO screen Blaze pass=0 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (70.6s)
Sep 15 20:11:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:11:17,423 main INFO screen Sorky pass=0 dev=0.0 ins=0.0 pro=57 1a=False 1b=False 2=True (63.0s)
Sep 15 20:11:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:11:23,654 main INFO screen LOCKED pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 15 20:12:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:12:00,589 main INFO screen DIP pass=0 dev=0.0 ins=20.1 pro=54 1a=False 1b=False 2=True (55.0s)
Sep 15 20:12:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:12:13,082 main INFO screen FOX pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 20:12:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:12:27,044 main INFO screen richdog pass=0 dev=0.0 ins=41.55 pro=70 1a=False 1b=False 2=True (63.4s)
Sep 15 20:12:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:12:55,151 main INFO screen DIP pass=0 dev=0.0 ins=24.57 pro=3 1a=False 1b=False 2=False (54.6s)
Sep 15 20:13:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:13:10,136 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:13:10 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:13:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:13:13,335 main INFO screen oc pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (60.3s)
Sep 15 20:13:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:13:20,424 main INFO screen OpenAI pass=0 dev=0.0 ins=166.31 pro=0 1a=False 1b=False 2=True (53.4s)
Sep 15 20:13:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:13:49,742 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (54.6s)
Sep 15 20:14:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:14:23,261 main INFO screen RICHDOG pass=0 dev=0.0 ins=20.79 pro=3 1a=False 1b=False 2=False (69.9s)
Sep 15 20:14:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:14:24,680 main INFO screen SMILE pass=0 dev=0.0 ins=24.6 pro=0 1a=False 1b=False 2=True (64.3s)
Sep 15 20:14:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:14:54,310 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.6s)
Sep 15 20:15:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:15:30,000 main INFO screen chomik pass=0 dev=0.0 ins=17.15 pro=61 1a=False 1b=False 2=True (66.7s)
Sep 15 20:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:15:35,615 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (70.9s)
Sep 15 20:15:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:15:54,592 main INFO screen $TOGETHER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 15 20:16:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:24,206 main INFO screen TRAVIS pass=0 dev=0.0 ins=22.13 pro=63 1a=False 1b=False 2=True (54.2s)
Sep 15 20:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:37,767 main INFO screen Halphurt pass=0 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (62.2s)
Sep 15 20:16:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:48,832 main INFO screen HLDM pass=0 dev=0.0 ins=161.25 pro=0 1a=False 1b=False 2=True (54.2s)
Sep 15 20:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:28,499 main INFO screen BROS pass=0 dev=0.0 ins=24.53 pro=43 1a=False 1b=False 2=False (64.3s)
Sep 15 20:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:38,015 main INFO screen Him pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.2s)
Sep 15 20:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:52,230 main INFO screen Charzard  pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.4s)
Sep 15 20:18:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:18:14,384 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:18:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T19:00:36Z
--- update 2026-09-15T19:05:56Z
Running as unit: schaduwbot-wallets.service; invocation ID: d4e9a4210cb94fceb933a73dcc655635
analyses gestart (84579ff37485)
--- update 2026-09-15T19:10:57Z
--- update 2026-09-15T19:15:59Z
--- update 2026-09-15T19:21:24Z
--- update 2026-09-15T19:26:28Z
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
19:47:31 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=335 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:47:32 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 12/41/162 | al gemeten: 765
19:52:54 ijk: +5 van 5 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=339 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:52:54 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 14/41/163 | al gemeten: 770
19:58:04 ijk: +6 van 6 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=344 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:58:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 15/44/167 | al gemeten: 776
20:02:56 ijk: +4 van 4 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 10}) | verste bak n=348 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:02:56 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 14/47/164 | al gemeten: 780
20:07:53 ijk: +2 van 2 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 10}) | verste bak n=350 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:07:56 ijk-diagnose: nieuwste migratie 4.6 min oud | migraties 15/60/240 min: 12/45/165 | al gemeten: 782
20:13:16 ijk: +1 van 1 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=351 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:13:16 ijk-diagnose: nieuwste migratie 1.3 min oud | migraties 15/60/240 min: 7/46/162 | al gemeten: 783
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 4861 | 494 | 486 | 0 | 118 | 3.7 min |
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
| 09-15 18:00 | 3973 | 34 | 33 | 30 | 0 | 126.2 min |

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
