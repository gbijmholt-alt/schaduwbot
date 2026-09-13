# Schaduwbot status

- tijd: 2026-09-13 02:43:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 12 hours, 56 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.1G/38G | geheugen: 1382/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 22189, "tokens_in_memory": 7509, "msgs": 2410870, "trades": 702846, "creates": 7770, "decode_fail": 66774, "rpc_calls": 18709, "rpc_errors": 3, "sol_usd": 101.87375649706125, "open_positions": 23, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 2753 | 316 | 0 | 326 | 50 | 591 | 1808 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 604 | 17% | 1.7% | +43.5% | -15.9% | -6.06% | 100% |
| dip35_V1_gescreend_fail | 4696 | 27% | 3.9% | +45.1% | -26.0% | -6.78% | 100% |
| dip35_V1_alle | 6278 | 26% | 3.9% | +44.4% | -25.4% | -7.06% | 100% |
| dip35_V2_gescreend_pass | 601 | 22% | 2.3% | +41.0% | -20.2% | -6.47% | 100% |
| dip35_V2_gescreend_fail | 4772 | 25% | 4.4% | +54.8% | -27.9% | -7.01% | 100% |
| dip35_V2_alle | 6236 | 25% | 4.5% | +52.2% | -27.7% | -8.02% | 100% |
| dip35_V3_gescreend_pass | 609 | 9% | 3.3% | +261.0% | -22.1% | +3.98% | 100% |
| dip35_V3_gescreend_fail | 4893 | 14% | 6.1% | +118.4% | -29.6% | -9.40% | 100% |
| dip35_V3_alle | 6290 | 13% | 6.1% | +116.9% | -29.4% | -10.18% | 100% |
| dip40_V1_gescreend_pass | 575 | 15% | 1.7% | +44.5% | -15.4% | -6.68% | 100% |
| dip40_V1_gescreend_fail | 4617 | 26% | 3.9% | +46.7% | -25.8% | -6.64% | 100% |
| dip40_V1_alle | 6035 | 26% | 3.9% | +46.5% | -25.3% | -6.92% | 100% |
| dip40_V2_gescreend_pass | 574 | 18% | 2.1% | +43.6% | -19.5% | -8.16% | 100% |
| dip40_V2_gescreend_fail | 4669 | 25% | 4.3% | +54.6% | -27.9% | -7.00% | 100% |
| dip40_V2_alle | 5986 | 24% | 4.4% | +53.0% | -27.6% | -8.08% | 100% |
| dip40_V3_gescreend_pass | 582 | 8% | 2.9% | +260.2% | -21.0% | +2.15% | 100% |
| dip40_V3_gescreend_fail | 4776 | 13% | 5.8% | +113.9% | -29.4% | -10.30% | 100% |
| dip40_V3_alle | 6042 | 13% | 5.9% | +113.3% | -29.1% | -10.98% | 100% |
| dip45_V1_gescreend_pass | 554 | 15% | 1.6% | +47.0% | -15.2% | -5.87% | 100% |
| dip45_V1_gescreend_fail | 4532 | 27% | 3.6% | +48.1% | -25.6% | -5.53% | 100% |
| dip45_V1_alle | 5832 | 26% | 3.6% | +48.2% | -25.1% | -5.98% | 100% |
| dip45_V2_gescreend_pass | 552 | 19% | 2.0% | +42.8% | -19.4% | -7.82% | 100% |
| dip45_V2_gescreend_fail | 4576 | 25% | 4.0% | +58.3% | -27.6% | -5.86% | 100% |
| dip45_V2_alle | 5785 | 24% | 4.1% | +56.7% | -27.3% | -6.93% | 100% |
| dip45_V3_gescreend_pass | 560 | 8% | 2.5% | +286.8% | -20.4% | +4.29% | 100% |
| dip45_V3_gescreend_fail | 4669 | 14% | 5.5% | +120.5% | -29.0% | -7.97% | 100% |
| dip45_V3_alle | 5833 | 13% | 5.5% | +121.8% | -28.6% | -8.85% | 100% |

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
| per_token_met_xlink | 476 | 16% | 5.5% | -8.18% | -11.3% tot -5.0% | -14.3% | – | 100% |
| per_token_zonder_xlink | 147 | 23% | 0.0% | +19.56% | -8.8% tot +47.9% | -13.1% | 118% | 58% |
| gepoold_met_xlink | 3986 | 13% | 2.9% | -9.35% | -10.6% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1225 | 18% | 0.0% | +16.07% | +0.1% tot +32.1% | -14.3% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 02:05:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:09,333 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (63.9s)
Sep 13 02:05:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:09,886 main INFO screen GAW pass=0 dev=0.43 ins=0.0 pro=6 1a=False 1b=False 2=False (75.0s)
Sep 13 02:05:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:05:56,808 main INFO screen kittylick pass=0 dev=68.34 ins=0.0 pro=19 1a=False 1b=False 2=False (76.6s)
Sep 13 02:06:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:11,210 main INFO screen USFR pass=0 dev=0.01 ins=125.68 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 13 02:06:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:22,291 main INFO screen FTF pass=0 dev=0.02 ins=19.02 pro=74 1a=False 1b=False 2=True (73.0s)
Sep 13 02:06:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:06:59,029 main INFO screen CS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 13 02:07:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:23,679 main INFO screen MOWMOW pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.5s)
Sep 13 02:07:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:30,148 main INFO screen stomp pass=0 dev=0.18 ins=77.58 pro=8 1a=False 1b=True 2=True (66.7s)
Sep 13 02:07:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:07:46,375 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:07:46 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:08:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:08,352 main INFO screen BetOnBlak pass=1 dev=4.36 ins=0.0 pro=10 1a=False 1b=False 2=False (69.3s)
Sep 13 02:08:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:23,742 main INFO screen MOWMOW pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.1s)
Sep 13 02:08:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:08:36,318 main INFO screen $GOAT pass=0 dev=79.87 ins=0.0 pro=14 1a=False 1b=False 2=False (66.2s)
Sep 13 02:10:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:10:10,879 main INFO screen Stacy pass=0 dev=0.0 ins=19.43 pro=61 1a=False 1b=False 2=True (62.4s)
Sep 13 02:11:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:11:03,875 main INFO screen $AURA pass=0 dev=3.03 ins=0.0 pro=7 1a=False 1b=False 2=False (74.7s)
Sep 13 02:11:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:11:50,044 main INFO screen BetOnBlak pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (59.6s)
Sep 13 02:12:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:07,706 main INFO screen Him pass=0 dev=0.0 ins=5.14 pro=42 1a=False 1b=False 2=True (69.4s)
Sep 13 02:12:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:11,193 main INFO screen ROSHI pass=0 dev=0.0 ins=0.21 pro=6 1a=False 1b=False 2=False (64.8s)
Sep 13 02:12:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:12:59,406 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:12:59 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:13:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:13:03,810 main INFO screen PP pass=1 dev=0.43 ins=0.0 pro=13 1a=False 1b=False 2=False (73.8s)
Sep 13 02:13:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:13:05,196 main INFO screen XIAOMI pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (57.5s)
Sep 13 02:13:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:13:07,828 main INFO screen ZChan pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 13 02:14:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:14:09,691 main INFO screen MOWMOW pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.5s)
Sep 13 02:14:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:14:11,828 main INFO screen Hypest pass=0 dev=0.0 ins=48.57 pro=19 1a=False 1b=False 2=True (68.0s)
Sep 13 02:14:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:14:34,819 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.8s)
Sep 13 02:15:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:15:05,153 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 13 02:15:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:15:32,970 main INFO screen $NNA pass=0 dev=0.0 ins=0.28 pro=4 1a=False 1b=False 2=False (68.2s)
Sep 13 02:16:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:16:20,320 main INFO screen SOL-CHAN pass=0 dev=0.0 ins=19.23 pro=55 1a=False 1b=False 2=True (66.0s)
Sep 13 02:16:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:16:21,075 main INFO screen fg pass=0 dev=1.6 ins=0.0 pro=2 1a=False 1b=False 2=False (74.2s)
Sep 13 02:16:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:16:47,911 main INFO screen $BSTC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.9s)
Sep 13 02:17:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:17:16,524 main INFO screen United Sta pass=0 dev=0.01 ins=106.63 pro=1 1a=False 1b=False 2=True (56.2s)
Sep 13 02:17:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:17:35,314 main INFO screen Stockwork pass=0 dev=0.0 ins=18.05 pro=77 1a=False 1b=False 2=True (74.2s)
Sep 13 02:17:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:17:44,733 main INFO screen PIPEJAK pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (56.8s)
Sep 13 02:18:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:18:02,434 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:18:02 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:18:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:18:15,695 main INFO screen Mario pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.2s)
Sep 13 02:18:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:18:46,678 main INFO screen UP pass=1 dev=0.0 ins=13.05 pro=25 1a=False 1b=False 2=False (51.7s)
Sep 13 02:19:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:19:28,511 main INFO screen SNAKE pass=0 dev=0.17 ins=48.71 pro=24 1a=False 1b=False 2=True (56.8s)
Sep 13 02:19:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:19:37,729 main INFO screen LaMisery pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (58.3s)
Sep 13 02:21:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:21:05,196 main INFO screen POWPEW pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 13 02:21:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:21:40,075 main INFO screen 富贵 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 13 02:21:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:21:49,019 main INFO screen TRUMPGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (60.9s)
Sep 13 02:22:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:22:20,808 main INFO screen pumponks pass=0 dev=0.18 ins=79.13 pro=10 1a=False 1b=True 2=True (66.2s)
Sep 13 02:22:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:22:36,568 main INFO screen WOFI pass=0 dev=79.31 ins=39.65 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 02:23:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:23:01,961 main INFO screen TA pass=1 dev=0.0 ins=14.63 pro=63 1a=False 1b=False 2=False (72.9s)
Sep 13 02:23:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:23:05,417 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:23:05 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:23:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:23:23,968 main INFO screen TSC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 13 02:23:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:23:50,565 main INFO screen Micron pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.7s)
Sep 13 02:24:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:24:37,197 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.4s)
Sep 13 02:24:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:24:48,446 main INFO screen TIMHO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.4s)
Sep 13 02:25:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:25:45,411 main INFO screen cmon pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.5s)
Sep 13 02:25:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:25:47,833 main INFO screen TIMHO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.6s)
Sep 13 02:25:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:25:53,414 main INFO screen kittylick pass=0 dev=0.89 ins=0.0 pro=1 1a=False 1b=False 2=False (65.0s)
Sep 13 02:26:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:26:41,021 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.6s)
Sep 13 02:27:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:27:50,655 main INFO screen STOCKTIMES pass=1 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (52.4s)
Sep 13 02:28:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:28:06,483 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:28:06 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:28:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:28:32,133 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 13 02:29:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:29:09,557 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.6s)
Sep 13 02:29:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:29:20,739 main INFO screen NIGGA pass=0 dev=0.0 ins=18.07 pro=53 1a=False 1b=False 2=True (53.2s)
Sep 13 02:29:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:29:52,459 main INFO screen $LAMBO pass=0 dev=3.09 ins=0.0 pro=4 1a=False 1b=False 2=False (70.3s)
Sep 13 02:31:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:31:22,345 main INFO screen mayhem  pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (79.2s)
Sep 13 02:32:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:32:17,608 main INFO screen BetOnBlak pass=0 dev=2.32 ins=0.0 pro=5 1a=False 1b=False 2=False (77.2s)
Sep 13 02:32:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:32:45,892 main INFO screen GAS pass=0 dev=0.17 ins=48.56 pro=19 1a=False 1b=False 2=True (62.4s)
Sep 13 02:33:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:33:13,491 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:33:13 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:33:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:33:17,180 main INFO screen GLDN pass=1 dev=0.21 ins=0.0 pro=11 1a=False 1b=False 2=False (78.0s)
Sep 13 02:33:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:33:47,353 main INFO screen Dmomo pass=0 dev=0.0 ins=1.74 pro=1 1a=False 1b=False 2=False (62.9s)
Sep 13 02:34:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:34:32,415 rpc WARNING rpc getTokenLargestAccounts exc
Sep 13 02:34:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:34:49,140 main INFO screen Rolex pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (97.9s)
Sep 13 02:35:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:35:09,263 main INFO screen CSTUNK pass=0 dev=0.04 ins=79.27 pro=4 1a=False 1b=True 2=True (104.2s)
Sep 13 02:35:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:35:36,147 main INFO screen DESERTED pass=0 dev=0.0 ins=14.73 pro=30 1a=False 1b=False 2=True (63.3s)
Sep 13 02:35:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:35:57,500 main INFO screen $speed pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (68.4s)
Sep 13 02:37:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:37:41,128 main INFO screen RETARD pass=0 dev=0.0 ins=18.08 pro=49 1a=False 1b=False 2=True (53.3s)
Sep 13 02:38:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:38:08,120 main INFO screen BITCORN pass=0 dev=0.0 ins=21.53 pro=25 1a=False 1b=False 2=True (55.5s)
Sep 13 02:38:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:38:15,303 main INFO screen 🏨 pass=0 dev=0.05 ins=0.0 pro=7 1a=False 1b=False 2=False (55.8s)
Sep 13 02:38:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:38:35,240 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:38:35 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:40:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:40:40,839 main INFO screen PIPPINGPT pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (51.9s)
Sep 13 02:41:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:41:02,870 main INFO screen RENTOPOLY pass=0 dev=0.0 ins=48.6 pro=25 1a=False 1b=False 2=True (62.7s)
Sep 13 02:41:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:41:28,966 main INFO screen DOGE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.6s)
Sep 13 02:42:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:42:53,361 main INFO screen HODL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 13 02:42:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:42:54,840 main INFO screen KEYCAT pass=0 dev=0.0 ins=8.62 pro=49 1a=False 1b=False 2=True (64.0s)
Sep 13 02:43:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:43:35,523 main INFO screen sol pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (70.7s)
Sep 13 02:43:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:43:37,064 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:43:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T01:14:49Z
--- update 2026-09-13T01:20:35Z
--- update 2026-09-13T01:25:36Z
--- update 2026-09-13T01:30:50Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1f41f3dc42b0489e96e2321b9527b30f
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T01:36:30Z
--- update 2026-09-13T01:41:36Z
--- update 2026-09-13T01:47:00Z
--- update 2026-09-13T01:52:03Z
--- update 2026-09-13T01:57:12Z
--- update 2026-09-13T02:02:36Z
--- update 2026-09-13T02:07:45Z
--- update 2026-09-13T02:12:58Z
--- update 2026-09-13T02:18:01Z
--- update 2026-09-13T02:23:04Z
--- update 2026-09-13T02:28:05Z
--- update 2026-09-13T02:33:12Z
--- update 2026-09-13T02:38:34Z
--- update 2026-09-13T02:43:36Z
```

## Analyses (laatste 25 regels)
```
inactive
01:38:38   8000 tokens, 896463 trades, 154963 posities (7s)
01:38:39   10000 tokens, 1118644 trades, 190444 posities (8s)
01:38:41   12000 tokens, 1338288 trades, 228593 posities (10s)
01:38:43   14000 tokens, 1559070 trades, 261143 posities (12s)
01:38:45   16000 tokens, 1815116 trades, 309221 posities (14s)
01:38:47   18000 tokens, 2054344 trades, 353904 posities (16s)
01:38:49   20000 tokens, 2273316 trades, 387540 posities (17s)
01:38:51   22000 tokens, 2497395 trades, 423098 posities (19s)
01:38:53   24000 tokens, 2734666 trades, 464849 posities (22s)
01:38:55   26000 tokens, 2948676 trades, 499259 posities (24s)
01:38:57   28000 tokens, 3193751 trades, 544763 posities (26s)
01:38:59   30000 tokens, 3417064 trades, 581170 posities (28s)
01:39:02   32000 tokens, 3645058 trades, 619865 posities (31s)
01:39:05   34000 tokens, 3861173 trades, 655601 posities (33s)
01:39:07   36000 tokens, 4091321 trades, 695494 posities (36s)
01:39:10   38000 tokens, 4311336 trades, 733577 posities (39s)
01:39:13   40000 tokens, 4549726 trades, 777004 posities (42s)
01:39:16   42000 tokens, 4787461 trades, 819867 posities (45s)
01:39:19   44000 tokens, 5019931 trades, 871749 posities (48s)
01:39:21 posities: 893712 uit 5124941 trades (50s)
01:39:30 187794 wallets gerekend
01:39:31 geluk-toets
01:40:02 persistentie
01:40:04 kopieer-simulatie
01:40:38 klaar in 127s -> /opt/schaduwbot/reports/wallets.md
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
