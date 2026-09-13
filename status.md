# Schaduwbot status

- tijd: 2026-09-13 11:28:30 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 21 hours, 41 minutes
- bot-service: active
- code-versie: 0a977ba
- schijf: 4.5G/38G | geheugen: 865/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 17663, "tokens_in_memory": 3350, "msgs": 853979, "trades": 289080, "creates": 3350, "decode_fail": 39435, "rpc_calls": 9391, "rpc_errors": 1, "sol_usd": 99.71112776297973, "open_positions": 25, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 10:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:19,050 aiohttp.access INFO 2.57.122.103 [13/Sep/2026:10:57:19 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 13 10:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:19,105 aiohttp.access INFO 2.57.122.103 [13/Sep/2026:10:57:19 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 13 10:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:19,159 aiohttp.access INFO 2.57.122.103 [13/Sep/2026:10:57:19 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 10:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:19,212 aiohttp.access INFO 2.57.122.103 [13/Sep/2026:10:57:19 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 10:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:19,264 aiohttp.access INFO 2.57.122.103 [13/Sep/2026:10:57:19 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 10:57:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:24,451 main INFO screen THB pass=0 dev=0.0 ins=25.87 pro=37 1a=False 1b=False 2=True (83.6s)
Sep 13 10:57:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:40,151 main INFO screen Fluffy pass=0 dev=0.0 ins=26.53 pro=60 1a=False 1b=False 2=True (80.8s)
Sep 13 10:57:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:57:45,684 main INFO screen HAMSTER  pass=0 dev=39.77 ins=0.02 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 13 10:59:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:59:12,596 main INFO screen Presidente pass=0 dev=0.0 ins=22.29 pro=52 1a=False 1b=False 2=True (60.6s)
Sep 13 10:59:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:59:58,069 main INFO screen SOLZ pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (49.9s)
Sep 13 11:01:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:01:05,871 main INFO screen RETARDIO pass=0 dev=0.0 ins=17.03 pro=46 1a=False 1b=False 2=True (66.6s)
Sep 13 11:01:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:01:45,173 main INFO screen $AURA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (54.9s)
Sep 13 11:01:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:01:52,460 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (49.3s)
Sep 13 11:02:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:02:17,422 main INFO screen batonhouse pass=0 dev=3.39 ins=75.89 pro=2 1a=True 1b=True 2=True (57.2s)
Sep 13 11:02:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:02:18,790 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:02:18 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 11:02:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:02:41,727 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 13 11:02:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:02:58,530 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.2s)
Sep 13 11:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:03:26,228 main INFO screen foff pass=0 dev=0.09 ins=0.0 pro=5 1a=False 1b=False 2=False (68.8s)
Sep 13 11:03:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:03:40,673 main INFO screen BATONSHIT pass=0 dev=0.14 ins=79.2 pro=8 1a=False 1b=True 2=True (58.9s)
Sep 13 11:04:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:04:00,000 main INFO screen baby pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 13 11:04:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:04:37,135 main INFO screen MIZOSOUP pass=1 dev=0.75 ins=0.0 pro=51 1a=False 1b=False 2=False (70.9s)
Sep 13 11:04:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:04:45,296 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.6s)
Sep 13 11:04:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:04:55,979 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 13 11:05:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:05:45,560 main INFO screen baby pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 13 11:05:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:05:51,172 main INFO screen SINGULARITY pass=0 dev=0.0 ins=24.97 pro=33 1a=False 1b=False 2=True (65.9s)
Sep 13 11:05:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:05:59,694 main INFO screen icat pass=1 dev=0.0 ins=15.88 pro=46 1a=False 1b=False 2=False (63.7s)
Sep 13 11:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:07:04,906 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.7s)
Sep 13 11:07:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:07:05,919 main INFO screen coin pass=0 dev=0.0 ins=18.24 pro=68 1a=False 1b=False 2=True (80.4s)
Sep 13 11:07:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:07:07,405 main INFO screen GPT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.7s)
Sep 13 11:07:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:07:20,439 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:07:20 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 11:07:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:07:56,496 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 13 11:08:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:08:08,976 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.6s)
Sep 13 11:08:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:08:10,670 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (64.7s)
Sep 13 11:09:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:09:01,408 main INFO screen Butthole pass=0 dev=0.0 ins=19.65 pro=49 1a=False 1b=False 2=True (64.9s)
Sep 13 11:09:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:09:22,390 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.4s)
Sep 13 11:09:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:09:26,682 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (76.0s)
Sep 13 11:10:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:10:15,345 main INFO screen GRL pass=0 dev=0.0 ins=18.62 pro=47 1a=False 1b=False 2=True (73.9s)
Sep 13 11:10:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:10:26,674 main INFO screen false  pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (64.3s)
Sep 13 11:10:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:10:30,151 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 13 11:11:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:11:27,714 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.4s)
Sep 13 11:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:11:37,307 main INFO screen POKEMON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (70.6s)
Sep 13 11:11:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:11:41,496 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.3s)
Sep 13 11:12:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:12:32,053 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 13 11:12:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:12:36,158 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:12:36 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 11:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:12:46,943 main INFO screen savemeeee pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 13 11:13:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:13:22,493 main INFO screen savemeeee pass=0 dev=0.0 ins=0.08 pro=7 1a=False 1b=False 2=False (52.1s)
Sep 13 11:13:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:13:53,235 main INFO screen savemeeee pass=0 dev=0.0 ins=0.11 pro=3 1a=False 1b=False 2=False (53.3s)
Sep 13 11:14:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:14:06,634 main INFO screen savemeeee pass=0 dev=0.03 ins=0.0 pro=2 1a=False 1b=False 2=False (52.1s)
Sep 13 11:14:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:14:56,465 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (65.2s)
Sep 13 11:15:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:15:27,575 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.3s)
Sep 13 11:16:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:16:52,009 main INFO screen kittylick pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (60.0s)
Sep 13 11:16:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:16:56,425 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.9s)
Sep 13 11:17:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:17:16,083 main INFO screen anki pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (59.4s)
Sep 13 11:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:17:37,113 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:17:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 11:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:17:57,851 main INFO screen RISE pass=0 dev=40.35 ins=0.0 pro=2 1a=False 1b=False 2=True (65.8s)
Sep 13 11:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:18:19,544 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.8s)
Sep 13 11:18:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:18:52,167 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 13 11:19:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:19:13,266 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (46.9s)
Sep 13 11:19:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:19:28,990 aiohttp.access INFO 45.63.4.69 [13/Sep/2026:11:19:28 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CyberConvoyScout/1.0; +https://scout.cyberconvoy.co)"
Sep 13 11:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:19:30,786 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.0s)
Sep 13 11:20:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:20:40,364 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 13 11:20:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:20:55,983 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.9s)
Sep 13 11:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:21:10,451 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.5s)
Sep 13 11:21:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:21:31,333 main INFO screen 666,666 pass=1 dev=0.0 ins=9.06 pro=51 1a=False 1b=False 2=False (51.0s)
Sep 13 11:21:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:21:59,769 main INFO screen 21e8 pass=0 dev=0.0 ins=19.13 pro=49 1a=False 1b=False 2=True (63.8s)
Sep 13 11:22:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:22:05,195 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.7s)
Sep 13 11:22:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:22:25,525 main INFO screen Tesla pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.2s)
Sep 13 11:22:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:22:52,309 main INFO screen savemeeee pass=0 dev=0.04 ins=0.0 pro=6 1a=False 1b=False 2=False (52.5s)
Sep 13 11:23:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:23:10,539 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:23:10 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 11:23:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:23:20,949 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (52.4s)
Sep 13 11:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:23:33,390 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.1s)
Sep 13 11:24:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:24:06,483 main INFO screen DOOB pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (67.6s)
Sep 13 11:24:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:24:45,994 main INFO screen $GRUDGY pass=0 dev=0.0 ins=3.43 pro=3 1a=False 1b=False 2=False (75.2s)
Sep 13 11:24:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:24:50,972 main INFO screen HOOD pass=0 dev=0.16 ins=79.2 pro=7 1a=False 1b=False 2=True (70.3s)
Sep 13 11:25:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:25:00,740 main INFO screen savemeeee pass=0 dev=0.03 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 13 11:25:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:25:39,988 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.0s)
Sep 13 11:25:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:25:51,465 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 13 11:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:25:52,469 main INFO screen savemeeee pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (51.7s)
Sep 13 11:26:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:26:33,447 main INFO screen moonshot  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.5s)
Sep 13 11:28:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:28:30,972 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:28:30 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T10:01:30Z
--- update 2026-09-13T10:06:34Z
--- update 2026-09-13T10:11:36Z
--- update 2026-09-13T10:16:43Z
--- update 2026-09-13T10:21:46Z
--- update 2026-09-13T10:26:47Z
--- update 2026-09-13T10:31:49Z
--- update 2026-09-13T10:36:49Z
--- update 2026-09-13T10:41:53Z
--- update 2026-09-13T10:47:00Z
--- update 2026-09-13T10:52:08Z
--- update 2026-09-13T10:57:08Z
--- update 2026-09-13T11:02:17Z
--- update 2026-09-13T11:07:19Z
--- update 2026-09-13T11:12:35Z
--- update 2026-09-13T11:17:36Z
--- update 2026-09-13T11:23:09Z
--- update 2026-09-13T11:28:29Z
Running as unit: schaduwbot-wallets.service; invocation ID: 8a3d763bc28340e1bd56e562391059f5
analyses gestart (2db583c97f2a)
```

## Analyses (laatste 25 regels)
```
active
09:42:07   14000 tokens, 1561073 trades, 248328 posities (19s)
09:42:09   16000 tokens, 1768685 trades, 279938 posities (21s)
09:42:12   18000 tokens, 2012157 trades, 322972 posities (24s)
09:42:15   20000 tokens, 2249230 trades, 366584 posities (27s)
09:42:18   22000 tokens, 2469849 trades, 399368 posities (30s)
09:42:21   24000 tokens, 2677236 trades, 431180 posities (33s)
09:42:24   26000 tokens, 2914563 trades, 471497 posities (36s)
09:42:27   28000 tokens, 3142623 trades, 507059 posities (39s)
09:42:29   30000 tokens, 3356830 trades, 540147 posities (42s)
09:42:32   32000 tokens, 3601467 trades, 583195 posities (45s)
09:42:35   34000 tokens, 3808823 trades, 614735 posities (47s)
09:42:37   36000 tokens, 4032618 trades, 650441 posities (50s)
09:42:40   38000 tokens, 4243396 trades, 682604 posities (52s)
09:42:43   40000 tokens, 4474588 trades, 721760 posities (55s)
09:42:45   42000 tokens, 4675975 trades, 754614 posities (57s)
09:42:48   44000 tokens, 4906666 trades, 795271 posities (60s)
09:42:51   46000 tokens, 5138255 trades, 832998 posities (63s)
09:42:53   48000 tokens, 5371937 trades, 872734 posities (66s)
09:42:57   50000 tokens, 5601720 trades, 921474 posities (69s)
09:42:58 posities: 948585 uit 5734887 trades (71s)
09:43:11 197038 wallets gerekend
09:43:12 geluk-toets
09:43:48 persistentie
09:43:51 kopieer-simulatie
09:44:15 klaar in 148s -> /opt/schaduwbot/reports/wallets.md
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
