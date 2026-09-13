# Schaduwbot status

- tijd: 2026-09-13 18:16:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 4 hours, 29 minutes
- bot-service: active
- code-versie: 3997123
- schijf: 4.8G/38G | geheugen: 1577/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 42149, "tokens_in_memory": 6787, "msgs": 4343726, "trades": 1001117, "creates": 10724, "decode_fail": 102824, "rpc_calls": 29868, "rpc_errors": 2, "sol_usd": 101.02584342896678, "open_positions": 42, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 17:50:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:50:40,022 main INFO screen LEDGER pass=1 dev=0.0 ins=11.86 pro=67 1a=False 1b=False 2=False (64.7s)
Sep 13 17:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:50:48,669 main INFO screen DiCabrio pass=0 dev=0.0 ins=39.81 pro=66 1a=False 1b=False 2=True (53.2s)
Sep 13 17:51:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:51:43,444 main INFO screen Beef pass=1 dev=0.0 ins=0.15 pro=16 1a=False 1b=False 2=False (63.4s)
Sep 13 17:51:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:51:44,956 main INFO screen XCOINS pass=0 dev=0.13 ins=5.16 pro=73 1a=False 1b=False 2=True (68.0s)
Sep 13 17:51:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:51:50,336 main INFO screen GPRO pass=0 dev=31.23 ins=0.0 pro=1 1a=False 1b=False 2=True (61.7s)
Sep 13 17:52:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:52:57,093 main INFO screen TONKY pass=1 dev=0.0 ins=0.0 pro=26 1a=False 1b=False 2=False (72.1s)
Sep 13 17:52:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:52:59,528 main INFO screen ELON pass=1 dev=0.0 ins=0.0 pro=85 1a=False 1b=False 2=False (76.1s)
Sep 13 17:53:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:53:04,003 main INFO screen TRUNK pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=False 2=True (73.7s)
Sep 13 17:54:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:54:09,930 main INFO screen Beef pass=1 dev=0.0 ins=0.65 pro=42 1a=False 1b=False 2=False (70.4s)
Sep 13 17:54:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:54:11,271 main INFO screen ANSEM pass=0 dev=0.0 ins=0.0 pro=83 1a=False 1b=False 2=True (74.2s)
Sep 13 17:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:54:14,283 main INFO screen AssTyson pass=1 dev=0.0 ins=9.51 pro=56 1a=False 1b=False 2=False (70.3s)
Sep 13 17:54:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:54:59,617 main INFO screen gfd pass=0 dev=0.0 ins=32.33 pro=17 1a=False 1b=False 2=True (49.7s)
Sep 13 17:55:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:55:24,160 main INFO screen DTOM pass=0 dev=0.0 ins=32.33 pro=68 1a=False 1b=False 2=True (69.9s)
Sep 13 17:55:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:55:26,828 main INFO screen cabbage pass=1 dev=2.24 ins=0.0 pro=56 1a=False 1b=False 2=False (75.6s)
Sep 13 17:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:55:37,486 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:17:55:37 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 13 17:56:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:56:04,654 main INFO screen NINAGPT pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (65.0s)
Sep 13 17:56:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:56:19,418 main INFO screen PETIX pass=0 dev=15.0 ins=43.46 pro=39 1a=False 1b=True 2=True (55.3s)
Sep 13 17:56:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:56:21,236 main INFO screen DTOM pass=0 dev=0.0 ins=20.04 pro=48 1a=False 1b=False 2=True (54.4s)
Sep 13 17:57:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:57:04,077 main INFO screen Silk pass=0 dev=0.0 ins=30.9 pro=82 1a=False 1b=False 2=True (59.4s)
Sep 13 17:57:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:57:16,280 main INFO screen DOGGO pass=0 dev=0.04 ins=48.84 pro=51 1a=False 1b=False 2=True (56.9s)
Sep 13 17:57:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:57:21,286 main INFO screen AUTISMFT pass=0 dev=0.0 ins=45.96 pro=43 1a=False 1b=False 2=True (60.0s)
Sep 13 17:58:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:58:21,016 main INFO screen GADSDEN pass=0 dev=0.0 ins=30.93 pro=27 1a=False 1b=False 2=True (76.9s)
Sep 13 17:58:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:58:25,973 main INFO screen Vivet pass=0 dev=13.1 ins=0.0 pro=9 1a=False 1b=False 2=False (69.7s)
Sep 13 17:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:58:29,101 main INFO screen GADSDEN pass=0 dev=0.0 ins=30.39 pro=26 1a=False 1b=False 2=True (67.8s)
Sep 13 17:59:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:59:39,725 main INFO screen LONG pass=1 dev=0.0 ins=1.62 pro=62 1a=False 1b=False 2=False (78.7s)
Sep 13 17:59:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:59:40,363 main INFO screen aicate pass=0 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=True (74.4s)
Sep 13 17:59:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 17:59:49,158 main INFO screen sol pass=1 dev=0.14 ins=0.0 pro=20 1a=False 1b=False 2=False (80.1s)
Sep 13 18:00:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:00:36,523 main INFO screen PONSAUTI pass=0 dev=0.0 ins=59.71 pro=19 1a=False 1b=False 2=True (56.8s)
Sep 13 18:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:00:37,349 main INFO screen TNT pass=0 dev=28.16 ins=0.0 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 13 18:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:00:50,518 main INFO screen ALLMART pass=0 dev=3.42 ins=22.24 pro=51 1a=False 1b=False 2=True (61.4s)
Sep 13 18:01:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:01:00,060 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:01:00 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 18:01:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:01:45,784 main INFO screen SWAMIS pass=0 dev=0.0 ins=32.28 pro=60 1a=False 1b=False 2=True (69.3s)
Sep 13 18:01:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:01:50,963 main INFO screen FLB pass=0 dev=0.88 ins=0.0 pro=4 1a=False 1b=False 2=False (73.6s)
Sep 13 18:01:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:01:54,449 main INFO screen Dwayne pass=0 dev=0.0 ins=25.6 pro=69 1a=False 1b=False 2=False (63.9s)
Sep 13 18:02:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:02:10,841 aiohttp.access INFO 20.65.219.49 [13/Sep/2026:18:02:10 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 13 18:02:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:02:11,117 aiohttp.access INFO 20.65.219.49 [13/Sep/2026:18:02:11 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 13 18:02:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:02:47,708 main INFO screen NiggaButt pass=0 dev=0.0 ins=22.2 pro=52 1a=False 1b=False 2=False (61.9s)
Sep 13 18:02:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:02:57,991 main INFO screen wen pass=1 dev=4.16 ins=0.0 pro=15 1a=False 1b=False 2=False (67.0s)
Sep 13 18:03:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:03:00,638 main INFO screen COCA COLA pass=0 dev=0.0 ins=170.01 pro=1 1a=False 1b=False 2=True (66.2s)
Sep 13 18:03:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:03:55,723 main INFO screen RISE pass=0 dev=48.55 ins=0.0 pro=7 1a=False 1b=False 2=False (68.0s)
Sep 13 18:04:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:04:06,167 main INFO screen Biglingor pass=1 dev=0.0 ins=0.0 pro=46 1a=False 1b=False 2=False (65.5s)
Sep 13 18:04:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:04:10,062 main INFO screen STAKE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.1s)
Sep 13 18:04:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:04:48,435 main INFO screen aicate pass=0 dev=0.0 ins=37.02 pro=37 1a=False 1b=False 2=True (52.7s)
Sep 13 18:05:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:05:18,209 main INFO screen toely pass=0 dev=0.0 ins=37.68 pro=53 1a=False 1b=False 2=True (68.1s)
Sep 13 18:05:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:05:21,343 main INFO screen MEME1921 pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (75.2s)
Sep 13 18:05:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:05:49,286 main INFO screen DUMPLIN pass=0 dev=13.79 ins=0.0 pro=2 1a=False 1b=False 2=False (60.9s)
Sep 13 18:06:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:06:07,898 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:06:07 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 18:06:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:06:27,779 main INFO screen toely pass=1 dev=0.0 ins=1.76 pro=46 1a=False 1b=False 2=False (69.6s)
Sep 13 18:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:06:29,208 main INFO screen Flybook pass=0 dev=0.0 ins=33.9 pro=46 1a=False 1b=False 2=True (67.9s)
Sep 13 18:07:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:07:02,157 main INFO screen DRILLPIG pass=1 dev=0.0 ins=1.88 pro=73 1a=False 1b=False 2=False (72.9s)
Sep 13 18:07:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:07:27,064 aiohttp.access INFO 189.18.97.61 [13/Sep/2026:18:07:27 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 13 18:07:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:07:42,265 main INFO screen FAGUMEN pass=1 dev=0.0 ins=3.46 pro=79 1a=False 1b=False 2=False (74.5s)
Sep 13 18:07:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:07:46,814 main INFO screen dug pass=0 dev=0.0 ins=43.65 pro=46 1a=False 1b=False 2=True (77.6s)
Sep 13 18:08:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:08:20,259 main INFO screen BATONFONE pass=0 dev=0.0 ins=61.92 pro=14 1a=False 1b=False 2=True (78.1s)
Sep 13 18:08:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:08:39,667 main INFO screen GPU2 pass=0 dev=0.0 ins=0.16 pro=6 1a=False 1b=False 2=True (57.4s)
Sep 13 18:08:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:08:53,646 main INFO screen dug pass=1 dev=0.0 ins=1.92 pro=85 1a=False 1b=False 2=False (66.8s)
Sep 13 18:09:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:09:16,051 main INFO screen MONSTER pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (55.8s)
Sep 13 18:09:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:09:33,362 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 13 18:09:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:09:57,084 main INFO screen dancingdog pass=0 dev=0.0 ins=28.84 pro=37 1a=False 1b=False 2=True (63.4s)
Sep 13 18:10:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:10:20,161 main INFO screen STICKMAN pass=0 dev=0.0 ins=19.4 pro=54 1a=False 1b=False 2=True (64.1s)
Sep 13 18:10:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:10:42,214 main INFO screen CHRIS pass=1 dev=0.0 ins=16.58 pro=77 1a=False 1b=False 2=False (68.8s)
Sep 13 18:10:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:10:54,429 main INFO screen MIGA pass=0 dev=0.0 ins=23.74 pro=49 1a=False 1b=False 2=True (57.3s)
Sep 13 18:11:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:11:20,273 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:11:20 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 18:11:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:11:20,490 main INFO screen WTyson pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (60.3s)
Sep 13 18:11:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:11:44,946 main INFO screen mus pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (62.7s)
Sep 13 18:11:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:11:56,686 main INFO screen jeet pass=0 dev=0.0 ins=50.5 pro=29 1a=False 1b=False 2=True (62.3s)
Sep 13 18:12:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:12:30,013 main INFO screen ACGPT pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=False 2=True (69.5s)
Sep 13 18:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:12:46,895 main INFO screen INV pass=0 dev=0.0 ins=28.12 pro=20 1a=False 1b=False 2=False (61.9s)
Sep 13 18:12:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:12:52,095 aiohttp.access INFO 201.6.143.110 [13/Sep/2026:18:12:52 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 18:13:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:13:09,439 main INFO screen HOLDOR pass=1 dev=0.0 ins=0.8 pro=12 1a=False 1b=False 2=False (72.8s)
Sep 13 18:13:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:13:33,421 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (63.4s)
Sep 13 18:13:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:13:42,393 main INFO screen BEAST pass=0 dev=0.08 ins=14.6 pro=1 1a=False 1b=False 2=True (55.5s)
Sep 13 18:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:14:18,849 main INFO screen HOM pass=1 dev=0.0 ins=15.78 pro=60 1a=False 1b=False 2=False (69.4s)
Sep 13 18:14:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:14:30,654 main INFO screen ch pass=0 dev=1.15 ins=0.0 pro=4 1a=False 1b=False 2=False (57.2s)
Sep 13 18:14:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:14:40,771 main INFO screen PvP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.4s)
Sep 13 18:15:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:15:14,621 main INFO screen ONE1 pass=0 dev=1.39 ins=0.0 pro=5 1a=False 1b=False 2=False (55.8s)
Sep 13 18:15:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:15:42,232 main INFO screen PIG pass=1 dev=0.0 ins=2.2 pro=60 1a=False 1b=False 2=False (71.6s)
Sep 13 18:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:15:47,577 main INFO screen XCOINS pass=1 dev=0.0 ins=0.49 pro=21 1a=False 1b=False 2=False (66.8s)
Sep 13 18:16:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:16:26,460 main INFO screen STUA pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (71.8s)
Sep 13 18:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 18:16:37,077 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:18:16:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T17:19:12Z
--- update 2026-09-13T17:24:22Z
--- update 2026-09-13T17:29:36Z
nieuwe code: 0179c15
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 533a93800d144e6793b5ef63991613a5
analyses gestart (039886ebfa0c)
--- update 2026-09-13T17:34:49Z
--- update 2026-09-13T17:40:05Z
--- update 2026-09-13T17:45:17Z
--- update 2026-09-13T17:50:26Z
--- update 2026-09-13T17:55:36Z
--- update 2026-09-13T18:00:58Z
nieuwe code: 3997123
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 277a60b2a54543f3adc6304d0d8680f0
analyses gestart (87dd80a5c10e)
--- update 2026-09-13T18:06:06Z
--- update 2026-09-13T18:11:19Z
--- update 2026-09-13T18:16:36Z
```

## Analyses (laatste 25 regels)
```
active
17:54:25   52000 tokens, 5601530 trades, 851300 posities (154s)
17:54:32   54000 tokens, 5829352 trades, 887180 posities (161s)
17:54:39   56000 tokens, 6050812 trades, 931622 posities (168s)
17:54:46   58000 tokens, 6245716 trades, 966863 posities (175s)
17:54:46 posities: 969836 uit 6254391 trades (175s)
17:54:58 201010 wallets gerekend
17:54:59 geluk-toets
17:55:35 persistentie
17:55:37 kopieer-simulatie
17:56:54 klaar in 303s -> /opt/schaduwbot/reports/wallets.md
18:01:01 58706 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
18:01:12   ingelezen tot rowid 6524604 (77815 rijen, 77815 bruikbaar)
18:01:13 ingelezen: 77815 nieuwe trades, 77815 bruikbaar (14s)
18:02:36 1755 aankopen van gevolgde wallets geëvalueerd
18:02:53 vroege kopers: 185 voldoen nu, register 315, 75 tokens beoordeeld
18:03:09 grote spelers: saldo van 49 wallets opgehaald
18:03:54 herkomst: 40 posities gekoppeld
18:04:00 klaar in 181s -> /opt/schaduwbot/reports/ledger.md
18:07:12 S1: gezakt — toets n=8991, verkennend n=14656
18:07:12 klaar in 191s -> /opt/schaduwbot/reports/hypotheses.md
18:07:12 probe: 150 transacties ophalen
18:10:36 poolveld: 14 pools bekeken, 0 te gaan -> vastgesteld @43
18:11:18 prijsijk: n=0 -> nog 20 migraties van minder dan 120 minuten oud te gaan
18:11:19 na-migratie: 100 paren te checken
18:12:58 na-migratie: 48 paren, 0 prijzen
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
