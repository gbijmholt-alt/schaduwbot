# Schaduwbot status

- tijd: 2026-09-15 01:25:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 11 hours, 38 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.6G/38G | geheugen: 2241/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 154289, "tokens_in_memory": 9987, "msgs": 23247503, "trades": 4695662, "creates": 50019, "decode_fail": 407208, "rpc_calls": 132382, "rpc_errors": 13, "sol_usd": 102.49879419018367, "open_positions": 64, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 01:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:00:45,733 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 15 01:01:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:01:15,779 main INFO screen HOODTARD pass=0 dev=0.0 ins=19.89 pro=11 1a=False 1b=False 2=True (56.9s)
Sep 15 01:01:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:01:24,891 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (54.3s)
Sep 15 01:01:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:01:57,029 main INFO screen fun pass=0 dev=0.0 ins=24.57 pro=54 1a=False 1b=False 2=True (71.3s)
Sep 15 01:02:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:02:15,096 main INFO screen kittylick pass=0 dev=0.0 ins=0.04 pro=2 1a=False 1b=False 2=True (59.3s)
Sep 15 01:02:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:02:34,979 main INFO screen BobCoin pass=0 dev=0.0 ins=48.48 pro=57 1a=False 1b=False 2=True (70.0s)
Sep 15 01:02:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:02:59,143 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.1s)
Sep 15 01:03:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:03:10,324 main INFO screen TOOMANY pass=0 dev=0.0 ins=12.74 pro=59 1a=False 1b=False 2=False (55.2s)
Sep 15 01:03:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:03:27,777 main INFO screen VIBREW pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (52.8s)
Sep 15 01:04:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:04:07,110 main INFO screen BC pass=0 dev=0.0 ins=16.34 pro=25 1a=False 1b=False 2=True (68.0s)
Sep 15 01:04:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:04:13,666 main INFO screen USFM pass=0 dev=0.0 ins=0.8 pro=15 1a=False 1b=False 2=False (63.3s)
Sep 15 01:04:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:04:24,776 main INFO screen BCEO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 15 01:04:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:04:37,119 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:04:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 01:05:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:05:02,016 main INFO screen Unlockable pass=0 dev=0.0 ins=44.08 pro=24 1a=False 1b=False 2=True (54.9s)
Sep 15 01:05:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:05:29,293 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.6s)
Sep 15 01:05:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:05:33,851 main INFO screen PEPTAMINE pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=False 2=True (69.1s)
Sep 15 01:06:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:06:02,689 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 15 01:06:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:06:31,318 main INFO screen trade pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.0s)
Sep 15 01:06:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:06:37,691 main INFO screen MUBARAK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.8s)
Sep 15 01:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:06:56,858 main INFO screen FOWLPLAY pass=0 dev=0.0 ins=13.0 pro=58 1a=False 1b=False 2=True (54.2s)
Sep 15 01:07:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:07:28,989 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.7s)
Sep 15 01:07:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:07:43,695 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (66.0s)
Sep 15 01:07:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:07:52,679 main INFO screen TORA pass=0 dev=0.0 ins=28.08 pro=17 1a=False 1b=False 2=True (55.8s)
Sep 15 01:08:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:08:28,024 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 15 01:08:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:08:38,875 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.2s)
Sep 15 01:08:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:08:50,797 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 15 01:09:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:09:25,627 main INFO screen RISE pass=0 dev=0.0 ins=4.32 pro=7 1a=False 1b=False 2=True (57.6s)
Sep 15 01:09:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:09:30,018 main INFO screen JUDE pass=0 dev=0.0 ins=17.37 pro=14 1a=False 1b=False 2=False (51.1s)
Sep 15 01:09:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:09:37,575 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:09:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:09:44,138 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (53.3s)
Sep 15 01:10:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:10:17,639 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.0s)
Sep 15 01:10:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:10:32,249 main INFO screen Shark pass=0 dev=0.0 ins=30.39 pro=62 1a=False 1b=False 2=True (62.2s)
Sep 15 01:10:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:10:45,612 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 15 01:11:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:11:17,175 main INFO screen RATRICH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.5s)
Sep 15 01:11:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:11:24,273 main INFO screen PMP7 pass=0 dev=0.0 ins=17.34 pro=40 1a=False 1b=False 2=False (52.0s)
Sep 15 01:11:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:11:41,436 main INFO screen RECREATED pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (55.8s)
Sep 15 01:12:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:12:11,869 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 15 01:12:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:12:23,304 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 15 01:12:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:12:31,221 main INFO screen SharkCAT pass=0 dev=0.0 ins=73.9 pro=24 1a=True 1b=False 2=False (49.8s)
Sep 15 01:13:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:13:17,038 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.2s)
Sep 15 01:13:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:13:23,564 main INFO screen niarbylf pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (60.3s)
Sep 15 01:13:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:13:32,456 main INFO screen STOKNBATON pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.2s)
Sep 15 01:14:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:14:17,398 main INFO screen boost pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (60.4s)
Sep 15 01:14:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:14:38,281 main INFO screen Retail pass=0 dev=0.0 ins=20.81 pro=56 1a=False 1b=False 2=True (74.7s)
Sep 15 01:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:14:48,774 main INFO screen Unyil pass=0 dev=0.0 ins=10.19 pro=79 1a=False 1b=False 2=False (76.3s)
Sep 15 01:15:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:15:14,129 main INFO screen chair pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 15 01:15:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:15:17,067 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:15:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:15:36,900 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.6s)
Sep 15 01:15:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:15:51,328 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.6s)
Sep 15 01:16:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:16:12,713 main INFO screen CRATER pass=0 dev=0.0 ins=23.52 pro=27 1a=False 1b=False 2=True (58.6s)
Sep 15 01:16:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:16:40,198 main INFO screen /what_if pass=0 dev=0.0 ins=26.55 pro=43 1a=False 1b=False 2=True (63.3s)
Sep 15 01:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:16:53,716 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.4s)
Sep 15 01:17:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:17:14,550 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.8s)
Sep 15 01:17:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:17:45,429 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.2s)
Sep 15 01:17:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:17:56,144 main INFO screen NEURON pass=0 dev=0.0 ins=45.45 pro=33 1a=False 1b=False 2=True (62.4s)
Sep 15 01:18:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:15,982 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.4s)
Sep 15 01:18:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:43,965 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 15 01:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:49,967 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 15 01:19:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:08,370 main INFO screen MCAT pass=0 dev=0.0 ins=29.6 pro=12 1a=False 1b=False 2=True (52.4s)
Sep 15 01:19:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:39,687 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.7s)
Sep 15 01:19:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:56,004 main INFO screen Supercycle pass=0 dev=0.0 ins=28.76 pro=73 1a=False 1b=False 2=True (66.0s)
Sep 15 01:20:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:06,040 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 01:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:33,927 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:20:33 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 01:20:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:38,111 main INFO screen GIGAFUND pass=0 dev=0.0 ins=20.69 pro=38 1a=False 1b=True 2=True (58.4s)
Sep 15 01:20:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:51,791 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.8s)
Sep 15 01:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:01,783 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 01:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:34,165 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.1s)
Sep 15 01:21:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:43,697 main INFO screen TRAVIS pass=0 dev=0.0 ins=18.25 pro=45 1a=False 1b=False 2=True (51.9s)
Sep 15 01:21:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:56,746 main INFO screen Obimach pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.0s)
Sep 15 01:22:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:26,568 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (52.4s)
Sep 15 01:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:42,476 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.8s)
Sep 15 01:22:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:52,107 main INFO screen Neocloud pass=0 dev=0.0 ins=17.57 pro=14 1a=False 1b=False 2=True (55.4s)
Sep 15 01:23:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:20,821 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 15 01:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:33,274 aiohttp.access INFO 170.130.204.50 [15/Sep/2026:01:23:33 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 15 01:23:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:34,838 main INFO screen SINGULARITY pass=0 dev=0.0 ins=26.37 pro=48 1a=False 1b=False 2=True (52.4s)
Sep 15 01:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:47,506 main INFO screen Rolex pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (55.4s)
Sep 15 01:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:35,738 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (74.9s)
Sep 15 01:24:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:43,291 main INFO screen TH3000 pass=0 dev=0.0 ins=28.21 pro=15 1a=False 1b=False 2=True (55.8s)
Sep 15 01:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:47,879 main INFO screen Gary pass=0 dev=0.0 ins=25.57 pro=69 1a=False 1b=False 2=True (73.0s)
Sep 15 01:25:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:25:37,195 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:25:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T23:51:32Z
--- update 2026-09-14T23:56:36Z
--- update 2026-09-15T00:01:52Z
--- update 2026-09-15T00:07:23Z
--- update 2026-09-15T00:12:34Z
--- update 2026-09-15T00:17:36Z
--- update 2026-09-15T00:22:46Z
--- update 2026-09-15T00:28:02Z
--- update 2026-09-15T00:33:12Z
--- update 2026-09-15T00:38:36Z
--- update 2026-09-15T00:43:36Z
--- update 2026-09-15T00:48:48Z
--- update 2026-09-15T00:54:19Z
--- update 2026-09-15T00:59:26Z
--- update 2026-09-15T01:04:36Z
--- update 2026-09-15T01:09:36Z
--- update 2026-09-15T01:15:15Z
--- update 2026-09-15T01:20:32Z
--- update 2026-09-15T01:25:36Z
```

## Analyses (laatste 25 regels)
```
inactive
00:29:52   38000 tokens, 3688000 trades, 442370 posities (248s)
00:30:05   40000 tokens, 3882064 trades, 469159 posities (261s)
00:30:19   42000 tokens, 4065709 trades, 486855 posities (274s)
00:30:33   44000 tokens, 4245991 trades, 510852 posities (289s)
00:30:47   46000 tokens, 4420440 trades, 531350 posities (303s)
00:31:02   48000 tokens, 4598102 trades, 550760 posities (318s)
00:31:19   50000 tokens, 4799757 trades, 574399 posities (335s)
00:31:36   52000 tokens, 5016691 trades, 603626 posities (352s)
00:31:52   54000 tokens, 5200426 trades, 625224 posities (367s)
00:32:06   56000 tokens, 5365533 trades, 644406 posities (382s)
00:32:23   58000 tokens, 5562944 trades, 669075 posities (399s)
00:32:39   60000 tokens, 5746516 trades, 689739 posities (415s)
00:32:57   62000 tokens, 5955952 trades, 716730 posities (433s)
00:33:13   64000 tokens, 6142789 trades, 744367 posities (449s)
00:33:30   66000 tokens, 6356758 trades, 771423 posities (466s)
00:33:43   68000 tokens, 6541957 trades, 795263 posities (479s)
00:33:56   70000 tokens, 6731219 trades, 818210 posities (492s)
00:34:10   72000 tokens, 6922572 trades, 843202 posities (506s)
00:34:25   74000 tokens, 7133262 trades, 878980 posities (521s)
00:34:30 posities: 885811 uit 7196469 trades (529s)
00:34:43 211069 wallets gerekend
00:34:43 geluk-toets
00:35:19 persistentie
00:35:22 kopieer-simulatie
00:37:42 klaar in 721s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
00:54:37 ijk: +6 van 6 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 2}) | verste bak n=59 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:54:37 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 8/38/160 | al gemeten: 347
00:59:43 ijk: +6 van 7 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=65 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:59:44 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 14/43/162 | al gemeten: 353
01:04:45 ijk: +3 van 3 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 12}) | verste bak n=66 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:04:45 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 15/41/161 | al gemeten: 356
01:09:54 ijk: +6 van 7 kandidaten (16 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=71 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:09:54 ijk-diagnose: nieuwste migratie 1.0 min oud | migraties 15/60/240 min: 16/42/166 | al gemeten: 362
01:15:28 ijk: +4 van 4 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=72 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:15:28 ijk-diagnose: nieuwste migratie 0.7 min oud | migraties 15/60/240 min: 12/41/164 | al gemeten: 366
01:20:44 ijk: +4 van 4 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=75 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:20:45 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 13/42/167 | al gemeten: 370
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
