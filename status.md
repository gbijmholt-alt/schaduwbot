# Schaduwbot status

- tijd: 2026-09-15 11:21:00 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 21 hours, 34 minutes
- bot-service: active
- code-versie: b2d6d06
- schijf: 7.1G/38G | geheugen: 2335/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 190012, "tokens_in_memory": 5998, "msgs": 27517567, "trades": 5670459, "creates": 60838, "decode_fail": 471341, "rpc_calls": 168043, "rpc_errors": 15, "sol_usd": 100.72074944863778, "open_positions": 66, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 10:55:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:22,405 main INFO screen ONLYUP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (63.0s)
Sep 15 10:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:48,481 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:10:55:48 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 10:55:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:53,232 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.8s)
Sep 15 10:56:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:13,758 main INFO screen STOCKPILLS pass=0 dev=0.0 ins=1.68 pro=69 1a=False 1b=False 2=False (61.6s)
Sep 15 10:56:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:27,366 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=78.69 pro=5 1a=False 1b=True 2=True (65.0s)
Sep 15 10:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:50,462 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.2s)
Sep 15 10:57:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:12,312 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (58.6s)
Sep 15 10:57:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:22,517 main INFO screen Blavicular pass=0 dev=0.0 ins=28.56 pro=68 1a=False 1b=False 2=True (55.1s)
Sep 15 10:57:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:49,307 main INFO screen ONLYUP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.8s)
Sep 15 10:58:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:08,689 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 15 10:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:20,336 main INFO screen ONLYUP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.8s)
Sep 15 10:58:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:44,367 main INFO screen POOLS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 15 10:59:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:03,312 main INFO screen solinscrip pass=0 dev=0.0 ins=33.6 pro=42 1a=False 1b=False 2=True (54.6s)
Sep 15 10:59:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:15,781 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.4s)
Sep 15 10:59:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:34,585 main INFO screen nigga pass=0 dev=0.0 ins=18.89 pro=49 1a=False 1b=False 2=False (50.2s)
Sep 15 10:59:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:57,091 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 15 11:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:15,117 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.3s)
Sep 15 11:00:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:47,224 main INFO screen LMAO pass=0 dev=0.0 ins=5.07 pro=53 1a=False 1b=False 2=False (72.6s)
Sep 15 11:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:50,999 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 15 11:00:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:51,068 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:00:51 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:01:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:12,496 main INFO screen snail pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 15 11:01:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:42,371 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.1s)
Sep 15 11:01:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:52,963 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.0s)
Sep 15 11:02:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:06,057 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 15 11:02:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:34,670 main INFO screen CATE pass=0 dev=0.0 ins=135.64 pro=0 1a=False 1b=False 2=True (52.3s)
Sep 15 11:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:50,658 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 11:03:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:03,960 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 15 11:03:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:30,742 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 15 11:03:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:50,346 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (59.7s)
Sep 15 11:03:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:58,070 main INFO screen USELESSER pass=0 dev=0.0 ins=0.21 pro=4 1a=False 1b=False 2=False (54.1s)
Sep 15 11:04:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:04:35,849 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (65.1s)
Sep 15 11:05:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:04,103 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (73.8s)
Sep 15 11:05:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:04,141 main INFO screen sol pass=0 dev=0.03 ins=0.0 pro=1 1a=False 1b=False 2=True (66.1s)
Sep 15 11:05:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:47,367 main INFO screen mruh pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (71.5s)
Sep 15 11:05:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:50,484 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:05:50 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 11:05:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:54,702 main INFO screen GOAF pass=0 dev=0.0 ins=132.4 pro=1 1a=False 1b=False 2=True (50.6s)
Sep 15 11:06:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:06:01,316 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.2s)
Sep 15 11:07:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:07:08,154 main INFO screen ccode pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (80.8s)
Sep 15 11:07:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:07:10,076 main INFO screen Deafcoin pass=0 dev=0.0 ins=11.09 pro=63 1a=False 1b=False 2=False (75.4s)
Sep 15 11:07:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:07:16,756 main INFO screen solsounds pass=0 dev=0.0 ins=5.96 pro=65 1a=False 1b=False 2=False (75.4s)
Sep 15 11:08:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:08:06,591 main INFO screen memecoin pass=0 dev=0.0 ins=32.42 pro=59 1a=False 1b=False 2=True (58.4s)
Sep 15 11:08:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:08:17,054 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (67.0s)
Sep 15 11:08:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:08:17,655 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.9s)
Sep 15 11:09:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:09:05,100 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=78.22 pro=5 1a=False 1b=True 2=True (58.5s)
Sep 15 11:09:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:09:26,009 main INFO screen RickRoll pass=0 dev=0.0 ins=16.45 pro=56 1a=False 1b=False 2=False (68.4s)
Sep 15 11:09:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:09:32,131 main INFO screen Deafcoin pass=0 dev=0.0 ins=6.83 pro=64 1a=False 1b=False 2=False (75.1s)
Sep 15 11:10:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:10:22,036 main INFO screen RISE pass=0 dev=0.0 ins=4.28 pro=10 1a=False 1b=False 2=False (76.9s)
Sep 15 11:10:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:10:35,310 main INFO screen MPG pass=0 dev=0.0 ins=27.76 pro=13 1a=False 1b=False 2=True (63.2s)
Sep 15 11:10:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:10:37,980 main INFO screen kittylick pass=0 dev=0.14 ins=0.0 pro=2 1a=False 1b=False 2=False (72.0s)
Sep 15 11:10:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:10:50,645 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:10:50 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:11:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:11:17,541 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.5s)
Sep 15 11:11:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:11:33,860 main INFO screen Deafcoin pass=0 dev=0.0 ins=24.53 pro=46 1a=False 1b=False 2=False (55.9s)
Sep 15 11:11:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:11:40,871 main INFO screen RICKROLL pass=0 dev=0.0 ins=32.09 pro=59 1a=False 1b=False 2=True (65.6s)
Sep 15 11:12:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:12:28,693 main INFO screen TUDUM pass=0 dev=0.0 ins=22.51 pro=35 1a=False 1b=False 2=False (71.2s)
Sep 15 11:12:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:12:32,631 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 15 11:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:12:49,035 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.2s)
Sep 15 11:13:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:13:20,791 rpc WARNING rpc getSignaturesForAddress error {'code': -32019, 'message': 'Failed to query long-term storage; please try again'}
Sep 15 11:13:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:13:27,027 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.3s)
Sep 15 11:13:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:13:37,999 main INFO screen 67 pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=False (65.4s)
Sep 15 11:13:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:13:42,877 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 15 11:14:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:14:20,845 main INFO screen SNOOP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 15 11:14:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:14:31,023 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.0s)
Sep 15 11:14:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:14:43,738 main INFO screen HEADSET pass=0 dev=0.0 ins=31.51 pro=58 1a=False 1b=False 2=True (60.9s)
Sep 15 11:15:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:15:15,944 main INFO screen META pass=0 dev=0.0 ins=29.04 pro=8 1a=False 1b=False 2=True (55.1s)
Sep 15 11:15:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:15:29,579 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.6s)
Sep 15 11:15:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:15:34,862 main INFO screen 𒐫𒐫𒐫 pass=0 dev=0.0 ins=26.62 pro=69 1a=False 1b=False 2=True (51.1s)
Sep 15 11:15:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:15:55,522 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:15:55 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:16:29,310 main INFO screen Siri pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (73.4s)
Sep 15 11:16:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:16:40,939 main INFO screen BATONTYSON pass=0 dev=0.0 ins=79.26 pro=1 1a=False 1b=False 2=True (71.4s)
Sep 15 11:16:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:16:41,381 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 15 11:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:17:40,142 main INFO screen Deafcoin pass=0 dev=0.0 ins=26.19 pro=73 1a=False 1b=False 2=True (70.8s)
Sep 15 11:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:17:57,075 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (75.7s)
Sep 15 11:17:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:17:58,541 main INFO screen fg pass=0 dev=0.02 ins=0.0 pro=3 1a=False 1b=False 2=False (77.6s)
Sep 15 11:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:18:56,782 main INFO screen Hypnotize pass=0 dev=0.0 ins=11.65 pro=62 1a=False 1b=False 2=False (76.6s)
Sep 15 11:19:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:19:01,318 main INFO screen crossr pass=0 dev=0.0 ins=25.47 pro=6 1a=False 1b=False 2=False (62.8s)
Sep 15 11:19:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:19:01,537 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (64.5s)
Sep 15 11:19:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:19:53,246 main INFO screen Gulp pass=0 dev=0.0 ins=29.66 pro=22 1a=False 1b=False 2=True (56.5s)
Sep 15 11:20:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:20:19,994 main INFO screen Meow pass=0 dev=0.0 ins=20.87 pro=37 1a=False 1b=False 2=False (78.7s)
Sep 15 11:20:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:20:20,864 main INFO screen Meow pass=0 dev=0.0 ins=16.78 pro=49 1a=False 1b=False 2=False (79.3s)
Sep 15 11:21:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:21:00,081 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:21:00 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: 1978398
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T10:15:36Z
--- update 2026-09-15T10:20:40Z
nieuwe code: b2d6d06
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T10:25:40Z
--- update 2026-09-15T10:30:40Z
--- update 2026-09-15T10:35:41Z
--- update 2026-09-15T10:40:43Z
--- update 2026-09-15T10:45:43Z
--- update 2026-09-15T10:50:45Z
--- update 2026-09-15T10:55:47Z
--- update 2026-09-15T11:00:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: eaf6b7b4df234ac0b42ef826db918f51
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T11:05:49Z
--- update 2026-09-15T11:10:49Z
--- update 2026-09-15T11:15:54Z
--- update 2026-09-15T11:20:58Z
```

## Analyses (laatste 40 regels)
```
active
09:47:29   66000 tokens, 6368136 trades, 786022 posities (447s)
09:47:44   68000 tokens, 6558130 trades, 811760 posities (463s)
09:47:59   70000 tokens, 6738863 trades, 833010 posities (477s)
09:48:14   72000 tokens, 6940230 trades, 857491 posities (492s)
09:48:30   74000 tokens, 7140514 trades, 889117 posities (508s)
09:48:44   76000 tokens, 7316833 trades, 913068 posities (522s)
09:48:45 posities: 913473 uit 7325165 trades (529s)
09:48:58 210371 wallets gerekend
09:48:58 geluk-toets
09:49:35 persistentie
09:49:38 kopieer-simulatie
09:52:03 klaar in 727s -> /opt/schaduwbot/reports/wallets.md
10:13:23   500/6700 lopers, 14233 koppelingen
10:14:09   1000/6700 lopers, 27609 koppelingen
10:14:46   1500/6700 lopers, 35674 koppelingen
10:15:33   2000/6700 lopers, 46613 koppelingen
10:16:11   2500/6700 lopers, 55002 koppelingen
10:16:39   3000/6700 lopers, 62231 koppelingen
10:17:23   3500/6700 lopers, 71433 koppelingen
10:17:51   4000/6700 lopers, 77748 koppelingen
10:18:35   4500/6700 lopers, 85514 koppelingen
10:19:12   5000/6700 lopers, 93093 koppelingen
10:19:43   5500/6700 lopers, 99227 koppelingen
10:20:56   6000/6700 lopers, 110982 koppelingen
10:21:42   6500/6700 lopers, 117630 koppelingen
10:21:52 klaar in 1276s: 6700 lopers, 40017 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/vamp.py 11:00:50
11:00:50 tokens lezen
11:00:55 133728 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
11:12:30 6749 lopers, 18 niet-onderscheidende woorden
11:13:34   500/6749 lopers, 4334 koppelingen
11:14:27   1000/6749 lopers, 7353 koppelingen
11:15:10   1500/6749 lopers, 11262 koppelingen
11:16:04   2000/6749 lopers, 15841 koppelingen
11:16:46   2500/6749 lopers, 18547 koppelingen
11:17:20   3000/6749 lopers, 21453 koppelingen
11:18:10   3500/6749 lopers, 25603 koppelingen
11:18:45   4000/6749 lopers, 28395 koppelingen
11:19:40   4500/6749 lopers, 32066 koppelingen
11:20:29   5000/6749 lopers, 35311 koppelingen
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
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
