# Schaduwbot status

- tijd: 2026-09-14 21:23:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 7 hours, 36 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.4G/38G | geheugen: 2276/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 139769, "tokens_in_memory": 11045, "msgs": 20013525, "trades": 4151310, "creates": 43868, "decode_fail": 365675, "rpc_calls": 118151, "rpc_errors": 7, "sol_usd": 103.8474103551774, "open_positions": 61, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 20:58:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:58:19,085 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (47.9s)
Sep 14 20:58:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:58:27,526 main INFO screen meta pass=0 dev=0.0 ins=30.95 pro=2 1a=False 1b=False 2=True (55.7s)
Sep 14 20:58:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:58:36,069 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 14 20:59:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:59:12,326 main INFO screen MMM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 20:59:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:59:20,442 main INFO screen PROPHET pass=0 dev=0.0 ins=79.12 pro=1 1a=False 1b=False 2=True (52.9s)
Sep 14 20:59:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:59:27,146 main INFO screen PACKLY pass=0 dev=0.0 ins=39.75 pro=2 1a=False 1b=False 2=True (51.1s)
Sep 14 21:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:00:15,699 main INFO screen SOLBROKER pass=0 dev=0.0 ins=4.92 pro=17 1a=False 1b=False 2=False (48.6s)
Sep 14 21:00:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:00:19,889 main INFO screen TESLAMASK pass=0 dev=0.0 ins=15.33 pro=15 1a=False 1b=False 2=True (59.4s)
Sep 14 21:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:00:23,272 main INFO screen Pretend pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (70.9s)
Sep 14 21:01:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:01:32,491 main INFO screen 7H pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.6s)
Sep 14 21:01:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:01:33,796 main INFO screen CHAD pass=0 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (70.5s)
Sep 14 21:01:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:01:36,531 main INFO screen Ray pass=0 dev=0.0 ins=40.33 pro=63 1a=False 1b=False 2=True (80.8s)
Sep 14 21:02:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:02:32,621 main INFO screen ERON pass=0 dev=0.0 ins=39.38 pro=1 1a=False 1b=False 2=True (60.1s)
Sep 14 21:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:02:37,933 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:02:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:02:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:02:42,683 main INFO screen PUMPATHON pass=0 dev=0.17 ins=23.27 pro=83 1a=False 1b=False 2=True (66.2s)
Sep 14 21:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:02:51,389 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.6s)
Sep 14 21:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:03:26,609 main INFO screen TESLAMUSK pass=0 dev=0.0 ins=20.46 pro=4 1a=False 1b=False 2=True (54.0s)
Sep 14 21:03:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:03:51,797 main INFO screen MUSKSAN pass=0 dev=0.0 ins=20.95 pro=3 1a=False 1b=False 2=False (69.1s)
Sep 14 21:04:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:04:03,190 main INFO screen BenDrillr pass=0 dev=0.0 ins=31.0 pro=60 1a=False 1b=False 2=True (71.8s)
Sep 14 21:04:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:04:29,227 main INFO screen MUSK-SAN pass=0 dev=0.0 ins=40.9 pro=1 1a=False 1b=False 2=True (62.6s)
Sep 14 21:04:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:04:50,315 main INFO screen MCTEST pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (58.5s)
Sep 14 21:04:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:04:58,538 main INFO screen MUSKSAN pass=0 dev=0.0 ins=29.71 pro=1 1a=False 1b=False 2=True (55.3s)
Sep 14 21:05:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:05:29,016 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.8s)
Sep 14 21:05:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:05:53,768 main INFO screen Black Pearl pass=0 dev=0.0 ins=16.52 pro=32 1a=False 1b=False 2=True (63.5s)
Sep 14 21:06:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:06:01,993 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.5s)
Sep 14 21:06:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:06:34,304 main INFO screen buy pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.3s)
Sep 14 21:07:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:07:03,191 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.2s)
Sep 14 21:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:07:04,445 main INFO screen FOUR pass=0 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (70.7s)
Sep 14 21:07:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:07:40,506 main INFO screen Sol  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.2s)
Sep 14 21:07:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:07:56,094 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:07:56 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:08:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:08:16,473 main INFO screen HAPI pass=0 dev=0.0 ins=26.68 pro=73 1a=False 1b=False 2=True (73.3s)
Sep 14 21:08:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:08:18,482 main INFO screen HAPI-ness pass=0 dev=0.0 ins=36.16 pro=59 1a=False 1b=False 2=True (74.0s)
Sep 14 21:08:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:08:31,583 aiohttp.access INFO 45.58.168.180 [14/Sep/2026:21:08:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Synthient-Research-Scanner/1.0"
Sep 14 21:08:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:08:50,622 main INFO screen HAPI pass=0 dev=0.0 ins=27.17 pro=30 1a=False 1b=False 2=True (70.1s)
Sep 14 21:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:09:13,168 main INFO screen pockly pass=0 dev=0.0 ins=52.26 pro=51 1a=False 1b=False 2=True (54.7s)
Sep 14 21:09:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:09:14,657 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.2s)
Sep 14 21:09:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:09:43,328 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.7s)
Sep 14 21:10:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:10:18,446 main INFO screen HAPI-ness pass=0 dev=0.0 ins=19.92 pro=1 1a=False 1b=False 2=True (65.3s)
Sep 14 21:10:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:10:22,297 main INFO screen Stuart pass=0 dev=0.0 ins=25.68 pro=81 1a=False 1b=False 2=True (67.6s)
Sep 14 21:10:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:10:44,305 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (61.0s)
Sep 14 21:11:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:11:11,371 main INFO screen Vibrew pass=0 dev=0.0 ins=35.79 pro=70 1a=False 1b=False 2=True (52.9s)
Sep 14 21:11:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:11:27,713 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.4s)
Sep 14 21:11:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:11:40,253 main INFO screen Pretend pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.9s)
Sep 14 21:12:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:12:01,332 main INFO screen NORBY pass=0 dev=0.0 ins=0.0 pro=39 1a=False 1b=False 2=False (50.0s)
Sep 14 21:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:12:20,543 main INFO screen NORBY pass=0 dev=0.0 ins=13.51 pro=20 1a=False 1b=False 2=True (52.8s)
Sep 14 21:12:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:12:41,311 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.1s)
Sep 14 21:13:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:13:02,411 main INFO screen VIBREW pass=0 dev=0.0 ins=5.16 pro=82 1a=False 1b=False 2=True (61.1s)
Sep 14 21:13:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:13:14,294 main INFO screen Pearl pass=0 dev=0.0 ins=13.83 pro=55 1a=False 1b=False 2=False (53.7s)
Sep 14 21:13:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:13:22,604 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:13:22 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:13:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:13:45,874 main INFO screen 中村 pass=0 dev=0.0 ins=23.65 pro=2 1a=False 1b=False 2=True (64.6s)
Sep 14 21:13:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:13:53,645 main INFO screen HAPI pass=0 dev=0.0 ins=25.43 pro=46 1a=False 1b=False 2=True (51.2s)
Sep 14 21:14:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:14:06,677 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (52.4s)
Sep 14 21:14:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:14:38,119 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (52.2s)
Sep 14 21:14:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:14:50,561 main INFO screen DRT pass=0 dev=0.0 ins=0.7 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 14 21:15:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:15:10,689 main INFO screen HAPI pass=0 dev=0.0 ins=20.59 pro=5 1a=False 1b=False 2=True (64.0s)
Sep 14 21:15:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:15:44,343 main INFO screen MUSKRAT pass=0 dev=0.0 ins=23.12 pro=26 1a=False 1b=False 2=True (66.2s)
Sep 14 21:15:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:15:54,870 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (64.3s)
Sep 14 21:16:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:16:28,033 main INFO screen KOLO pass=0 dev=11.4 ins=0.0 pro=14 1a=False 1b=False 2=False (77.3s)
Sep 14 21:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:16:54,531 main INFO screen Avengers pass=0 dev=0.0 ins=26.61 pro=40 1a=False 1b=False 2=True (70.2s)
Sep 14 21:17:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:17:00,555 main INFO screen  Lil Wig pass=0 dev=0.0 ins=8.87 pro=60 1a=False 1b=False 2=True (65.7s)
Sep 14 21:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:17:34,500 main INFO screen American pass=0 dev=0.0 ins=29.55 pro=5 1a=False 1b=False 2=True (66.5s)
Sep 14 21:17:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:17:43,362 main INFO screen TOE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.8s)
Sep 14 21:17:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:17:53,440 main INFO screen COOK pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (52.9s)
Sep 14 21:18:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:18:26,281 main INFO screen Buttcoin pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.8s)
Sep 14 21:18:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:18:30,685 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:18:30 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:18:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:18:47,757 main INFO screen HEMEP pass=0 dev=0.0 ins=20.62 pro=28 1a=False 1b=False 2=True (64.4s)
Sep 14 21:19:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:19:07,709 main INFO screen MECHAZILLA pass=0 dev=0.0 ins=19.98 pro=9 1a=False 1b=False 2=False (74.3s)
Sep 14 21:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:19:30,623 main INFO screen pomp pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.3s)
Sep 14 21:19:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:19:45,450 main INFO screen TRADER pass=0 dev=0.0 ins=23.69 pro=5 1a=False 1b=False 2=False (57.7s)
Sep 14 21:19:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:19:58,605 main INFO screen TICK pass=0 dev=0.0 ins=35.6 pro=18 1a=False 1b=False 2=True (50.9s)
Sep 14 21:20:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:20:29,405 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 14 21:20:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:20:55,241 main INFO screen SIMULATION pass=0 dev=0.0 ins=11.3 pro=36 1a=False 1b=False 2=True (69.8s)
Sep 14 21:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:21:10,989 main INFO screen Hedge pass=0 dev=0.0 ins=24.98 pro=60 1a=False 1b=False 2=True (72.4s)
Sep 14 21:21:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:21:37,768 main INFO screen HYBRID pass=0 dev=0.0 ins=26.82 pro=71 1a=False 1b=False 2=True (68.4s)
Sep 14 21:21:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:21:58,329 aiohttp.access INFO 195.182.16.23 [14/Sep/2026:21:21:58 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 14 21:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:22:17,213 main INFO screen how pass=0 dev=0.05 ins=0.0 pro=7 1a=False 1b=False 2=False (82.0s)
Sep 14 21:22:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:22:18,296 main INFO screen RISE pass=0 dev=0.0 ins=4.28 pro=7 1a=False 1b=False 2=True (67.3s)
Sep 14 21:22:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:22:33,848 main INFO screen PUMP10 pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=True (56.1s)
Sep 14 21:23:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:37,284 main INFO screen SAKE pass=0 dev=0.0 ins=1.1 pro=18 1a=False 1b=False 2=False (80.1s)
Sep 14 21:23:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:23:37,471 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:23:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T20:27:19Z
--- update 2026-09-14T20:32:22Z
--- update 2026-09-14T20:37:22Z
nieuwe code: a8c6844
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T20:42:34Z
--- update 2026-09-14T20:47:34Z
nieuwe code: a1e210f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T20:52:35Z
Running as unit: schaduwbot-wallets.service; invocation ID: 69a69562f5464aaa85ae3e414157ea6c
analyses gestart (d1af81359b25)
--- update 2026-09-14T20:57:35Z
--- update 2026-09-14T21:02:36Z
nieuwe code: 2a95007
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T21:07:54Z
--- update 2026-09-14T21:13:21Z
--- update 2026-09-14T21:18:29Z
--- update 2026-09-14T21:23:36Z
```

## Analyses (laatste 25 regels)
```
active
20:49:04   72000 tokens, 7083937 trades, 885573 posities (481s)
20:49:16 posities: 901948 uit 7229176 trades (497s)
20:49:29 206737 wallets gerekend
20:49:29 geluk-toets
20:50:05 persistentie
20:50:09 kopieer-simulatie
20:52:32 klaar in 693s -> /opt/schaduwbot/reports/wallets.md
20:52:39 91239 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
20:53:00   ingelezen tot rowid 9629640 (130087 rijen, 130087 bruikbaar)
20:53:01 ingelezen: 130087 nieuwe trades, 130087 bruikbaar (25s)
20:55:52 3000 aankopen van gevolgde wallets geëvalueerd
20:56:33 vroege kopers: 259 voldoen nu, register 452, 224 tokens beoordeeld
20:57:03 grote spelers: saldo van 21 wallets opgehaald
20:57:29 herkomst: 40 posities gekoppeld
20:57:41 klaar in 305s -> /opt/schaduwbot/reports/ledger.md
21:10:35 S1: gezakt — toets n=25133, verkennend n=14656
21:10:35 klaar in 774s -> /opt/schaduwbot/reports/hypotheses.md
21:10:36 probe: 150 transacties ophalen
21:13:53 poolveld: 9 pools bekeken, 0 te gaan -> vastgesteld @43
21:15:05 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
21:15:05 prijsijk: n=4 -> nog 11 metingen binnen 5 minuten na de migratie te gaan
21:15:06 na-migratie: 100 paren te checken
21:16:45 na-migratie: 38 paren, 0 prijzen
21:19:49 gemigreerde koersen: 39 gedaan, 1498 te gaan
21:19:50 klaar (551 rpc-calls, 146 fouten)
```

## IJking poolkoers (laatste 12 regels)
```
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
20:37:27 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:37:27 ijk-diagnose: nieuwste migratie 3.1 min oud | migraties 15/60/240 min: 13/46/185 | al gemeten: 229
20:42:38 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:42:38 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 16/48/184 | al gemeten: 229
20:47:38 ijk: +0 van 0 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 11}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:47:39 ijk-diagnose: nieuwste migratie 3.5 min oud | migraties 15/60/240 min: 11/45/183 | al gemeten: 229
20:52:38 ijk: +0 van 0 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 9}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:52:39 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 9/43/182 | al gemeten: 229
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
