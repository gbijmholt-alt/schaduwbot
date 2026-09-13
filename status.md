# Schaduwbot status

- tijd: 2026-09-13 22:18:03 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 8 hours, 31 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.1G/38G | geheugen: 1865/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 56636, "tokens_in_memory": 8095, "msgs": 6761004, "trades": 1511232, "creates": 16217, "decode_fail": 140010, "rpc_calls": 44440, "rpc_errors": 2, "sol_usd": 99.80405473256624, "open_positions": 81, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 21:50:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:50:08,403 main INFO screen DOGE pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (66.5s)
Sep 13 21:50:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:50:11,352 main INFO screen WWR pass=0 dev=0.0 ins=132.24 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 13 21:50:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:50:37,024 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 13 21:51:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:51:16,791 main INFO screen GM pass=0 dev=0.0 ins=26.52 pro=53 1a=False 1b=False 2=True (68.4s)
Sep 13 21:51:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:51:18,852 main INFO screen $AFTER pass=1 dev=0.0 ins=1.94 pro=60 1a=False 1b=False 2=False (67.5s)
Sep 13 21:51:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:51:42,996 main INFO screen TERMINAL pass=0 dev=0.01 ins=0.0 pro=6 1a=False 1b=False 2=False (66.0s)
Sep 13 21:52:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:52:09,454 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.6s)
Sep 13 21:52:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:52:17,599 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:52:17 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:52:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:52:22,668 main INFO screen babybike pass=0 dev=0.0 ins=53.12 pro=47 1a=False 1b=False 2=True (65.9s)
Sep 13 21:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:52:34,418 main INFO screen BetOnBlak pass=0 dev=0.05 ins=0.0 pro=5 1a=False 1b=False 2=False (51.4s)
Sep 13 21:53:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:53:02,136 main INFO screen Gronk pass=0 dev=0.0 ins=26.45 pro=22 1a=True 1b=False 2=True (52.7s)
Sep 13 21:53:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:53:18,835 main INFO screen EGO pass=1 dev=0.0 ins=2.21 pro=22 1a=False 1b=False 2=False (56.2s)
Sep 13 21:53:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:53:28,490 main INFO screen brokr pass=0 dev=0.0 ins=47.77 pro=13 1a=True 1b=False 2=True (54.1s)
Sep 13 21:54:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:54:08,332 main INFO screen HONEY pass=0 dev=7.23 ins=0.0 pro=15 1a=False 1b=False 2=False (66.2s)
Sep 13 21:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:54:28,911 main INFO screen titless pass=1 dev=0.1 ins=2.67 pro=58 1a=False 1b=False 2=False (70.1s)
Sep 13 21:54:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:54:32,399 main INFO screen AKIRO pass=1 dev=0.0 ins=9.23 pro=23 1a=False 1b=False 2=False (63.9s)
Sep 13 21:55:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:55:18,600 main INFO screen Timothy pass=1 dev=0.0 ins=0.0 pro=57 1a=False 1b=False 2=False (70.3s)
Sep 13 21:55:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:55:41,203 main INFO screen Moon pass=0 dev=1.06 ins=0.0 pro=4 1a=False 1b=False 2=False (72.3s)
Sep 13 21:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:55:44,762 main INFO screen babybike pass=0 dev=0.0 ins=53.05 pro=48 1a=True 1b=False 2=True (72.4s)
Sep 13 21:56:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:56:22,667 main INFO screen SXSN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (64.1s)
Sep 13 21:56:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:56:40,446 main INFO screen CL pass=0 dev=0.0 ins=22.0 pro=35 1a=False 1b=False 2=True (59.2s)
Sep 13 21:56:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:56:46,357 main INFO screen NLV72 pass=0 dev=0.0 ins=38.98 pro=14 1a=False 1b=False 2=True (61.6s)
Sep 13 21:57:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:57:16,428 main INFO screen MCAT pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 13 21:57:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:57:32,847 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:21:57:32 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 21:57:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:57:52,913 main INFO screen POEM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.6s)
Sep 13 21:57:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:57:55,128 main INFO screen E/ACC pass=1 dev=0.0 ins=0.36 pro=70 1a=False 1b=False 2=False (74.7s)
Sep 13 21:58:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:58:16,215 main INFO screen Fap pass=0 dev=0.0 ins=13.92 pro=68 1a=False 1b=True 2=False (59.8s)
Sep 13 21:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:59:04,122 main INFO screen DATACENTER pass=1 dev=0.0 ins=9.43 pro=59 1a=False 1b=False 2=False (71.2s)
Sep 13 21:59:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:59:13,908 main INFO screen GVP pass=0 dev=0.0 ins=12.26 pro=71 1a=False 1b=False 2=True (78.8s)
Sep 13 21:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 21:59:16,383 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.2s)
Sep 13 22:00:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:00:17,115 main INFO screen Chill pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (73.0s)
Sep 13 22:00:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:00:24,882 main INFO screen RISE pass=0 dev=0.0 ins=0.3 pro=9 1a=False 1b=False 2=False (71.0s)
Sep 13 22:00:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:00:27,220 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.8s)
Sep 13 22:01:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:01:10,721 main INFO screen NVDA pass=0 dev=40.46 ins=0.0 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 13 22:01:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:01:40,450 main INFO screen BIKE TRUMP pass=0 dev=0.14 ins=79.17 pro=7 1a=False 1b=False 2=True (73.2s)
Sep 13 22:01:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:01:41,532 main INFO screen Kimothy pass=1 dev=3.76 ins=7.07 pro=52 1a=False 1b=False 2=False (76.6s)
Sep 13 22:02:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:02:20,686 main INFO screen DDOS pass=0 dev=0.0 ins=21.4 pro=70 1a=False 1b=False 2=True (70.0s)
Sep 13 22:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:02:37,111 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:02:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 22:02:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:02:45,305 main INFO screen EDGE pass=1 dev=0.0 ins=5.65 pro=35 1a=False 1b=False 2=False (63.8s)
Sep 13 22:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:02:50,660 main INFO screen $NINTOK pass=0 dev=2.12 ins=0.0 pro=5 1a=False 1b=False 2=False (70.2s)
Sep 13 22:03:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:03:28,880 main INFO screen $AFRO pass=1 dev=0.21 ins=0.0 pro=12 1a=False 1b=False 2=False (68.2s)
Sep 13 22:03:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:03:43,660 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (58.4s)
Sep 13 22:03:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:03:55,006 main INFO screen nugget pass=0 dev=0.0 ins=18.55 pro=66 1a=False 1b=False 2=True (64.3s)
Sep 13 22:04:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:04:29,630 main INFO screen INU pass=1 dev=0.0 ins=11.2 pro=44 1a=False 1b=False 2=False (60.7s)
Sep 13 22:04:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:04:42,349 main INFO screen LMAO pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=False (58.7s)
Sep 13 22:05:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:05:03,092 main INFO screen ily pass=0 dev=0.0 ins=13.36 pro=69 1a=False 1b=False 2=True (68.1s)
Sep 13 22:05:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:05:20,981 main INFO screen DDOS pass=0 dev=0.0 ins=21.47 pro=23 1a=False 1b=False 2=True (51.4s)
Sep 13 22:05:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:05:41,731 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.4s)
Sep 13 22:05:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:05:56,914 main INFO screen TOLY pass=0 dev=0.0 ins=31.79 pro=56 1a=False 1b=False 2=True (53.8s)
Sep 13 22:06:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:06:31,939 main INFO screen CLUSTER pass=1 dev=0.0 ins=18.09 pro=75 1a=False 1b=False 2=False (71.0s)
Sep 13 22:06:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:06:38,746 main INFO screen OpenAI pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 13 22:06:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:06:54,548 main INFO screen STONK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 13 22:07:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:07:39,461 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:07:39 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 22:07:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:07:45,532 main INFO screen FERCAN pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (73.6s)
Sep 13 22:07:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:07:51,016 main INFO screen COPY pass=1 dev=0.0 ins=12.23 pro=59 1a=False 1b=False 2=False (72.3s)
Sep 13 22:08:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:08:10,245 main INFO screen FEED pass=0 dev=0.0 ins=32.44 pro=61 1a=False 1b=False 2=True (75.7s)
Sep 13 22:08:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:08:55,786 main INFO screen YEWIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.8s)
Sep 13 22:08:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:08:58,089 main INFO screen SOLANA pass=0 dev=0.0 ins=24.94 pro=63 1a=False 1b=False 2=True (72.6s)
Sep 13 22:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:09:13,993 main INFO screen FEED pass=0 dev=0.0 ins=35.2 pro=41 1a=False 1b=False 2=True (63.7s)
Sep 13 22:10:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:10:06,909 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.8s)
Sep 13 22:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:10:16,183 main INFO screen Wsg pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (80.4s)
Sep 13 22:10:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:10:18,858 main INFO screen STONKS pass=0 dev=0.0 ins=8.04 pro=69 1a=False 1b=False 2=True (64.9s)
Sep 13 22:11:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:11:16,680 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.8s)
Sep 13 22:11:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:11:52,802 main INFO screen NOCOIN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.4s)
Sep 13 22:11:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:11:53,783 main INFO screen SAVPIR pass=0 dev=1.09 ins=0.0 pro=2 1a=False 1b=False 2=True (70.6s)
Sep 13 22:12:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:12:50,709 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:12:50 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 22:12:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:12:56,565 main INFO screen BBL pass=1 dev=0.0 ins=9.16 pro=29 1a=False 1b=False 2=False (61.3s)
Sep 13 22:13:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:13:05,465 main INFO screen SCAN pass=0 dev=1.27 ins=15.75 pro=76 1a=False 1b=False 2=True (55.4s)
Sep 13 22:13:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:13:57,875 main INFO screen HAMSTER pass=0 dev=0.95 ins=0.0 pro=1 1a=False 1b=False 2=False (68.1s)
Sep 13 22:14:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:14:05,915 main INFO screen 20CM pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (66.8s)
Sep 13 22:15:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:15:14,340 main INFO screen BetOnBlak pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (63.9s)
Sep 13 22:15:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:15:38,984 main INFO screen Real pass=1 dev=0.0 ins=4.54 pro=64 1a=False 1b=False 2=False (71.1s)
Sep 13 22:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:15:47,689 main INFO screen MYERS pass=0 dev=30.51 ins=13.64 pro=9 1a=False 1b=False 2=False (69.3s)
Sep 13 22:16:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:16:27,158 main INFO screen tob pass=0 dev=0.0 ins=16.72 pro=61 1a=False 1b=False 2=True (64.7s)
Sep 13 22:16:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:16:47,848 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (60.2s)
Sep 13 22:16:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:16:52,398 main INFO screen HAMSTER pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (73.4s)
Sep 13 22:17:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:17:23,650 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 22:17:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:17:41,989 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.1s)
Sep 13 22:17:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:17:56,192 main INFO screen OW pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.8s)
Sep 13 22:18:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 22:18:04,039 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:22:18:04 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T20:44:08Z
--- update 2026-09-13T20:49:14Z
--- update 2026-09-13T20:54:15Z
--- update 2026-09-13T20:59:36Z
--- update 2026-09-13T21:04:58Z
--- update 2026-09-13T21:10:36Z
--- update 2026-09-13T21:15:38Z
--- update 2026-09-13T21:21:09Z
--- update 2026-09-13T21:26:22Z
--- update 2026-09-13T21:31:24Z
--- update 2026-09-13T21:36:35Z
--- update 2026-09-13T21:41:36Z
--- update 2026-09-13T21:47:07Z
--- update 2026-09-13T21:52:16Z
--- update 2026-09-13T21:57:31Z
--- update 2026-09-13T22:02:36Z
--- update 2026-09-13T22:07:38Z
--- update 2026-09-13T22:12:49Z
--- update 2026-09-13T22:18:02Z
```

## Analyses (laatste 25 regels)
```
inactive
20:58:24   24000 tokens, 2539115 trades, 362670 posities (122s)
20:58:34   26000 tokens, 2749363 trades, 392838 posities (132s)
20:58:44   28000 tokens, 2951661 trades, 418764 posities (143s)
20:58:55   30000 tokens, 3167138 trades, 449939 posities (153s)
20:59:06   32000 tokens, 3395846 trades, 485427 posities (164s)
20:59:16   34000 tokens, 3598592 trades, 514118 posities (174s)
20:59:27   36000 tokens, 3791936 trades, 538973 posities (185s)
20:59:38   38000 tokens, 4009130 trades, 571221 posities (196s)
20:59:50   40000 tokens, 4217529 trades, 602889 posities (208s)
21:00:01   42000 tokens, 4419767 trades, 629224 posities (219s)
21:00:11   44000 tokens, 4617797 trades, 654225 posities (229s)
21:00:22   46000 tokens, 4814574 trades, 683467 posities (240s)
21:00:34   48000 tokens, 5035877 trades, 716964 posities (253s)
21:00:45   50000 tokens, 5214248 trades, 742397 posities (263s)
21:00:57   52000 tokens, 5426165 trades, 774722 posities (275s)
21:01:10   54000 tokens, 5649674 trades, 809593 posities (289s)
21:01:23   56000 tokens, 5861579 trades, 840319 posities (301s)
21:01:36   58000 tokens, 6086009 trades, 875935 posities (315s)
21:01:48   60000 tokens, 6302939 trades, 921314 posities (327s)
21:01:55 posities: 941185 uit 6436124 trades (336s)
21:02:09 199194 wallets gerekend
21:02:10 geluk-toets
21:02:45 persistentie
21:02:48 kopieer-simulatie
21:04:24 klaar in 485s -> /opt/schaduwbot/reports/wallets.md
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
