# Schaduwbot status

- tijd: 2026-09-15 18:34:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 4 hours, 47 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.5G/38G | geheugen: 2245/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 216029, "tokens_in_memory": 9850, "msgs": 33093726, "trades": 6786822, "creates": 71989, "decode_fail": 576979, "rpc_calls": 194162, "rpc_errors": 16, "sol_usd": 99.57850848141484, "open_positions": 61, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 18:09:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:21,994 main INFO screen Pokex pass=0 dev=0.0 ins=48.48 pro=25 1a=False 1b=False 2=True (59.0s)
Sep 15 18:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:44,016 aiohttp.access INFO 204.76.203.7 [15/Sep/2026:18:09:44 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 15 18:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:44,248 aiohttp.access INFO 204.76.203.7 [15/Sep/2026:18:09:44 +0000] "GET /jenkins/api/json?tree=displayName HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 15 18:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:44,315 aiohttp.access INFO 204.76.203.7 [15/Sep/2026:18:09:44 +0000] "GET /api/json?tree=displayName HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 15 18:09:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:50,785 main INFO screen werld pass=0 dev=0.0 ins=48.06 pro=20 1a=False 1b=False 2=True (57.9s)
Sep 15 18:09:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:09:57,432 main INFO screen 日本 pass=0 dev=0.0 ins=34.51 pro=72 1a=False 1b=False 2=True (64.8s)
Sep 15 18:10:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:10:19,768 main INFO screen UNISUPPLY pass=0 dev=0.0 ins=122.58 pro=4 1a=False 1b=False 2=False (57.8s)
Sep 15 18:11:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:11:03,884 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (73.1s)
Sep 15 18:11:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:11:05,328 main INFO screen vibedog pass=0 dev=0.0 ins=19.46 pro=61 1a=False 1b=False 2=True (67.9s)
Sep 15 18:11:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:11:19,054 main INFO screen FC pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.3s)
Sep 15 18:12:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:12:03,432 main INFO screen GIGA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.5s)
Sep 15 18:12:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:12:04,855 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (59.5s)
Sep 15 18:12:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:12:07,537 main INFO screen fatcat pass=0 dev=0.0 ins=42.64 pro=16 1a=False 1b=False 2=True (48.5s)
Sep 15 18:13:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:13:05,743 main INFO screen BIGMANINU pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.9s)
Sep 15 18:13:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:13:17,483 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (69.9s)
Sep 15 18:13:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:13:20,194 main INFO screen $REPTOP1 pass=0 dev=12.66 ins=0.0 pro=12 1a=False 1b=False 2=False (76.8s)
Sep 15 18:14:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:14:14,107 main INFO screen $ACT pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (68.4s)
Sep 15 18:14:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:14:14,371 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:14:14 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:14:18,479 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.3s)
Sep 15 18:14:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:14:33,895 main INFO screen MARKETS pass=0 dev=0.0 ins=25.15 pro=19 1a=False 1b=False 2=True (76.4s)
Sep 15 18:15:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:15:33,276 main INFO screen SWIFT pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (74.8s)
Sep 15 18:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:15:35,082 main INFO screen ELONCOIN pass=0 dev=0.0 ins=24.28 pro=1 1a=False 1b=False 2=False (81.0s)
Sep 15 18:15:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:15:41,417 main INFO screen Charli pass=0 dev=0.0 ins=2.92 pro=59 1a=False 1b=False 2=False (67.5s)
Sep 15 18:16:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:16:44,839 main INFO screen OTTER pass=0 dev=0.0 ins=24.5 pro=2 1a=False 1b=False 2=True (71.6s)
Sep 15 18:16:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:16:46,965 main INFO screen XC pass=0 dev=0.0 ins=19.86 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 15 18:16:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:16:50,247 main INFO screen Tradition pass=0 dev=0.0 ins=49.09 pro=23 1a=False 1b=False 2=True (75.2s)
Sep 15 18:18:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:18:01,297 main INFO screen Lily pass=0 dev=0.0 ins=14.22 pro=54 1a=False 1b=False 2=True (74.3s)
Sep 15 18:18:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:18:02,390 main INFO screen GIGA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.1s)
Sep 15 18:18:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:18:04,198 main INFO screen DH pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (79.4s)
Sep 15 18:18:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:18:51,985 main INFO screen Charli pass=0 dev=0.0 ins=19.31 pro=2 1a=False 1b=False 2=True (50.7s)
Sep 15 18:18:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:18:59,508 main INFO screen PADDOG pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (57.1s)
Sep 15 18:19:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:19:09,447 main INFO screen MINITRUMP pass=0 dev=0.0 ins=78.31 pro=2 1a=False 1b=True 2=True (65.2s)
Sep 15 18:19:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:19:19,250 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:19:19 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:19:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:19:46,311 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (54.3s)
Sep 15 18:20:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:20:02,410 main INFO screen FLUX pass=0 dev=0.0 ins=14.69 pro=55 1a=False 1b=False 2=False (62.9s)
Sep 15 18:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:20:18,571 main INFO screen STK pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (69.1s)
Sep 15 18:20:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:20:50,210 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (63.9s)
Sep 15 18:20:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:20:55,411 main INFO screen FOPPE pass=0 dev=0.0 ins=21.42 pro=3 1a=False 1b=False 2=False (53.0s)
Sep 15 18:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:21:13,099 main INFO screen Charli pass=0 dev=0.0 ins=18.41 pro=0 1a=False 1b=False 2=False (54.5s)
Sep 15 18:21:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:21:59,478 main INFO screen CBB pass=0 dev=0.0 ins=40.66 pro=47 1a=False 1b=False 2=True (69.3s)
Sep 15 18:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:22:06,937 main INFO screen drillsmith pass=0 dev=0.0 ins=59.17 pro=21 1a=False 1b=False 2=True (71.5s)
Sep 15 18:22:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:22:23,392 main INFO screen Stallions pass=0 dev=0.0 ins=14.44 pro=55 1a=False 1b=False 2=True (70.3s)
Sep 15 18:22:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:22:32,316 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:18:22:32 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 18:22:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:22:49,191 main INFO screen Milstein pass=0 dev=0.0 ins=15.23 pro=24 1a=False 1b=False 2=True (49.7s)
Sep 15 18:23:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:23:11,177 main INFO screen Ass pass=0 dev=0.0 ins=26.22 pro=64 1a=False 1b=False 2=True (64.2s)
Sep 15 18:23:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:23:24,278 main INFO screen XCLR pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (60.9s)
Sep 15 18:23:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:23:56,037 main INFO screen QCOW pass=0 dev=0.0 ins=47.27 pro=72 1a=False 1b=False 2=True (66.8s)
Sep 15 18:24:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:24:08,066 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.9s)
Sep 15 18:24:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:24:21,817 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:24:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:24:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:24:21,870 main INFO screen TCM pass=0 dev=0.0 ins=48.42 pro=7 1a=False 1b=False 2=True (57.6s)
Sep 15 18:24:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:24:39,867 aiohttp.access INFO 217.60.195.128 [15/Sep/2026:18:24:39 +0000] "POST /v1/messages HTTP/1.1" 404 193 "-" "claude-code/1.x"
Sep 15 18:24:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:24:54,283 main INFO screen QCOW pass=0 dev=0.0 ins=20.3 pro=1 1a=False 1b=False 2=False (58.2s)
Sep 15 18:25:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:25:20,755 main INFO screen JohnFoppe pass=0 dev=0.0 ins=10.69 pro=27 1a=False 1b=False 2=False (72.7s)
Sep 15 18:25:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:25:21,181 main INFO screen 67BATON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.3s)
Sep 15 18:25:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:25:58,638 main INFO screen CAT pass=0 dev=0.0 ins=5.21 pro=54 1a=False 1b=False 2=True (64.4s)
Sep 15 18:26:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:26:13,953 main INFO screen GLIAGE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.2s)
Sep 15 18:26:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:26:17,208 main INFO screen BG-5 pass=0 dev=0.0 ins=29.1 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 15 18:27:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:27:08,968 main INFO screen TIMIZE pass=0 dev=0.0 ins=3.59 pro=68 1a=False 1b=False 2=True (70.3s)
Sep 15 18:27:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:27:16,563 main INFO screen WOFI pass=0 dev=0.0 ins=134.94 pro=1 1a=False 1b=False 2=True (62.6s)
Sep 15 18:27:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:27:22,810 main INFO screen RETRY pass=0 dev=0.0 ins=3.59 pro=4 1a=False 1b=False 2=False (65.6s)
Sep 15 18:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:28:23,943 main INFO screen Ella  pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (75.0s)
Sep 15 18:28:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:28:25,570 main INFO screen STEALF pass=0 dev=0.0 ins=37.44 pro=1 1a=False 1b=False 2=True (69.0s)
Sep 15 18:28:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:28:31,136 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (68.3s)
Sep 15 18:29:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:29:22,649 main INFO screen CHICK pass=0 dev=0.0 ins=48.06 pro=31 1a=False 1b=False 2=True (58.7s)
Sep 15 18:29:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:29:33,336 main INFO screen MEMES2026 pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (67.8s)
Sep 15 18:29:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:29:35,541 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:29:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 18:29:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:29:35,911 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.8s)
Sep 15 18:30:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:30:32,439 main INFO screen twodolla pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.1s)
Sep 15 18:30:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:30:44,731 main INFO screen NON pass=0 dev=0.0 ins=17.7 pro=45 1a=False 1b=False 2=True (68.8s)
Sep 15 18:30:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:30:45,100 main INFO screen CAT pass=0 dev=0.0 ins=35.03 pro=69 1a=False 1b=False 2=True (82.4s)
Sep 15 18:32:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:32:00,404 main INFO screen Stallions pass=0 dev=0.0 ins=17.62 pro=55 1a=False 1b=False 2=False (88.0s)
Sep 15 18:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:32:05,807 main INFO screen CBO pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (81.1s)
Sep 15 18:32:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:32:07,436 main INFO screen Musk pass=0 dev=0.0 ins=0.03 pro=53 1a=False 1b=False 2=False (82.3s)
Sep 15 18:33:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:33:03,507 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.1s)
Sep 15 18:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:33:21,237 main INFO screen GTAVI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (73.8s)
Sep 15 18:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:33:21,588 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (75.8s)
Sep 15 18:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:08,587 main INFO screen TALON pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (65.1s)
Sep 15 18:34:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:24,394 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.8s)
Sep 15 18:34:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:24,986 main INFO screen $ROCKET pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (63.7s)
Sep 15 18:34:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:34:37,294 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:18:34:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T17:28:49Z
--- update 2026-09-15T17:33:50Z
--- update 2026-09-15T17:38:50Z
--- update 2026-09-15T17:43:52Z
--- update 2026-09-15T17:48:54Z
--- update 2026-09-15T17:54:07Z
--- update 2026-09-15T17:59:11Z
--- update 2026-09-15T18:04:11Z
Running as unit: schaduwbot-wallets.service; invocation ID: e462df6ecd2e4a138f160f044589f580
analyses gestart (84579ff37485)
--- update 2026-09-15T18:09:12Z
--- update 2026-09-15T18:14:13Z
--- update 2026-09-15T18:19:17Z
nieuwe code: 03bcc03
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:24:20Z
--- update 2026-09-15T18:29:34Z
nieuwe code: 85d446e
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:34:36Z
```

## Analyses (laatste 40 regels)
```
inactive
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
18:04:30 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=279 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:04:32 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 7/42/149 | al gemeten: 697
18:09:28 ijk: +3 van 3 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=281 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:09:29 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 11/42/151 | al gemeten: 700
18:14:36 ijk: +4 van 4 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=284 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:14:36 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 10/44/151 | al gemeten: 704
18:19:28 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=286 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:19:28 ijk-diagnose: nieuwste migratie 2.6 min oud | migraties 15/60/240 min: 9/42/151 | al gemeten: 706
18:24:38 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=289 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:24:39 ijk-diagnose: nieuwste migratie 1.9 min oud | migraties 15/60/240 min: 9/42/150 | al gemeten: 710
18:29:35 ijk: +0 van 0 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=289 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:29:35 ijk-diagnose: nieuwste migratie 7.1 min oud | migraties 15/60/240 min: 6/38/146 | al gemeten: 710
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
| 09-15 12:00 | 9559 | 993 | 918 | 2 | 0 | 67.0 min |
| 09-15 18:00 | 964 | 0 | 0 | 0 | 0 | - |

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
