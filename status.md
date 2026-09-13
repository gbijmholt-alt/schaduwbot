# Schaduwbot status

- tijd: 2026-09-13 03:30:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 13 hours, 43 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.1G/38G | geheugen: 1396/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 25009, "tokens_in_memory": 6957, "msgs": 2614294, "trades": 771070, "creates": 8420, "decode_fail": 77223, "rpc_calls": 20734, "rpc_errors": 3, "sol_usd": 101.89005198599742, "open_positions": 23, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 02:53:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:53:51,490 main INFO screen McDonald's pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.7s)
Sep 13 02:54:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:54:34,362 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:54:34 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 02:54:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:54:42,349 main INFO screen Pump pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.5s)
Sep 13 02:55:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:55:18,807 main INFO screen DOOROC pass=0 dev=14.46 ins=0.0 pro=4 1a=False 1b=False 2=False (72.3s)
Sep 13 02:55:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:55:21,455 main INFO screen SEVEN pass=1 dev=0.87 ins=0.0 pro=18 1a=False 1b=False 2=False (67.5s)
Sep 13 02:56:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:56:05,046 main INFO screen FLYTOWN pass=0 dev=0.0 ins=29.8 pro=67 1a=False 1b=False 2=True (71.5s)
Sep 13 02:56:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:56:10,452 main INFO screen DAWS pass=0 dev=42.6 ins=0.0 pro=0 1a=False 1b=False 2=True (50.2s)
Sep 13 02:56:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:56:32,118 main INFO screen CATPUMP pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (61.4s)
Sep 13 02:56:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:56:56,760 main INFO screen AnsemGirls pass=0 dev=3.18 ins=72.68 pro=1 1a=False 1b=False 2=True (51.7s)
Sep 13 02:57:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:57:10,832 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.0s)
Sep 13 02:57:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:57:25,955 main INFO screen Pump pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.8s)
Sep 13 02:58:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:58:00,184 main INFO screen JAR pass=0 dev=0.0 ins=22.94 pro=51 1a=False 1b=False 2=True (63.4s)
Sep 13 02:59:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:59:29,289 main INFO screen FTF pass=0 dev=0.7 ins=26.87 pro=56 1a=False 1b=False 2=True (63.1s)
Sep 13 02:59:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 02:59:37,129 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:02:59:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:01:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:01:03,545 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.3s)
Sep 13 03:02:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:02:36,050 main INFO screen Cuck pass=1 dev=0.0 ins=14.83 pro=63 1a=False 1b=False 2=False (65.1s)
Sep 13 03:03:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:03:03,648 main INFO screen FWHALES pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.6s)
Sep 13 03:03:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:03:17,952 main INFO screen DURKIO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.2s)
Sep 13 03:03:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:03:52,782 main INFO screen Amazon pass=0 dev=96.33 ins=0.0 pro=1 1a=False 1b=False 2=True (61.0s)
Sep 13 03:04:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:04:26,070 main INFO screen fg pass=0 dev=1.7 ins=0.0 pro=5 1a=False 1b=False 2=False (80.4s)
Sep 13 03:04:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:04:34,246 main INFO screen OPONSAI pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (66.5s)
Sep 13 03:04:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:04:48,112 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:04:48 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:04:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:04:55,194 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.4s)
Sep 13 03:05:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:05:36,619 main INFO screen Dogcoin pass=1 dev=0.0 ins=13.14 pro=35 1a=False 1b=False 2=False (62.4s)
Sep 13 03:05:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:05:37,274 main INFO screen GOSEND pass=1 dev=4.27 ins=0.0 pro=71 1a=False 1b=False 2=False (71.2s)
Sep 13 03:05:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:05:53,199 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 13 03:06:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:06:38,295 main INFO screen FONE pass=0 dev=0.0 ins=24.76 pro=8 1a=False 1b=False 2=True (61.0s)
Sep 13 03:06:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:06:40,224 main INFO screen DOGE pass=0 dev=0.84 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 13 03:07:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:07:02,952 main INFO screen Medusa pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (69.8s)
Sep 13 03:07:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:07:27,429 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:03:07:27 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 03:07:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:07:49,502 main INFO screen Medusa pass=0 dev=65.07 ins=0.0 pro=44 1a=False 1b=False 2=False (71.2s)
Sep 13 03:08:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:08:11,459 main INFO screen mog pass=1 dev=0.0 ins=13.5 pro=30 1a=False 1b=False 2=False (55.1s)
Sep 13 03:09:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:09:17,311 main INFO screen 15 pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (74.4s)
Sep 13 03:09:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:09:23,446 main INFO screen UP pass=0 dev=0.17 ins=48.6 pro=20 1a=False 1b=False 2=True (71.4s)
Sep 13 03:09:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:09:29,994 main INFO screen USMS pass=0 dev=93.46 ins=0.0 pro=16 1a=False 1b=False 2=False (67.1s)
Sep 13 03:09:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:09:51,509 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:09:51 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 03:10:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:10:14,616 main INFO screen PEPEGO pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (57.3s)
Sep 13 03:10:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:10:19,333 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.9s)
Sep 13 03:10:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:10:54,365 main INFO screen One pass=0 dev=0.0 ins=47.24 pro=82 1a=False 1b=False 2=True (62.6s)
Sep 13 03:11:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:11:18,563 main INFO screen One pass=0 dev=0.0 ins=37.54 pro=16 1a=False 1b=False 2=True (50.5s)
Sep 13 03:12:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:12:10,010 main INFO screen MERD pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (67.4s)
Sep 13 03:12:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:12:48,024 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.4s)
Sep 13 03:13:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:13:09,366 main INFO screen GORJUS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.4s)
Sep 13 03:13:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:13:47,517 main INFO screen CANADA pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (66.0s)
Sep 13 03:14:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:14:58,947 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:14:58 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:15:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:15:03,253 main INFO screen BOLD pass=0 dev=0.0 ins=21.86 pro=71 1a=False 1b=False 2=True (66.6s)
Sep 13 03:15:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:15:20,564 main INFO screen BOLD pass=0 dev=0.0 ins=24.81 pro=18 1a=False 1b=False 2=True (70.3s)
Sep 13 03:15:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:15:26,122 main INFO screen Medusa pass=0 dev=67.25 ins=0.17 pro=43 1a=False 1b=False 2=False (63.9s)
Sep 13 03:15:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:15:57,420 main INFO screen SEAOPEN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.2s)
Sep 13 03:16:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:16:27,409 main INFO screen BOLDCOIN pass=0 dev=0.0 ins=28.68 pro=24 1a=False 1b=False 2=True (61.3s)
Sep 13 03:16:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:16:31,452 main INFO screen TRENDS pass=0 dev=0.0 ins=26.35 pro=19 1a=False 1b=False 2=False (70.9s)
Sep 13 03:17:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:17:04,435 main INFO screen BuildIP pass=1 dev=0.0 ins=14.73 pro=43 1a=False 1b=False 2=False (67.0s)
Sep 13 03:17:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:17:40,074 main INFO screen Dmomo pass=1 dev=0.0 ins=0.21 pro=18 1a=False 1b=False 2=False (72.7s)
Sep 13 03:17:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:17:41,372 main INFO screen Addidas pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (69.9s)
Sep 13 03:18:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:18:02,417 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 13 03:18:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:18:36,796 main INFO screen $LAMBO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.7s)
Sep 13 03:18:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:18:49,441 main INFO screen toof pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (62.4s)
Sep 13 03:19:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:19:33,005 main INFO screen BROKER pass=0 dev=1.24 ins=21.2 pro=64 1a=False 1b=False 2=True (72.2s)
Sep 13 03:19:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:19:48,780 main INFO screen BPCATE pass=0 dev=4.47 ins=0.0 pro=9 1a=False 1b=False 2=False (72.0s)
Sep 13 03:20:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:20:32,254 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:20:32 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:20:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:20:47,251 main INFO screen 40U pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.9s)
Sep 13 03:21:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:21:05,142 main INFO screen Boldcoin pass=1 dev=0.0 ins=2.42 pro=64 1a=False 1b=False 2=False (67.7s)
Sep 13 03:21:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:21:18,435 main INFO screen Dmomo pass=0 dev=0.0 ins=0.21 pro=6 1a=False 1b=False 2=False (73.9s)
Sep 13 03:22:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:22:13,484 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.1s)
Sep 13 03:22:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:22:30,518 aiohttp.access INFO 195.182.16.23 [13/Sep/2026:03:22:30 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 13 03:23:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:23:40,969 main INFO screen NVIDIA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 13 03:24:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:24:17,472 main INFO screen GS pass=0 dev=0.0 ins=15.89 pro=48 1a=False 1b=False 2=True (64.2s)
Sep 13 03:25:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:25:11,863 main INFO screen ZOOAI pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (56.2s)
Sep 13 03:25:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:25:27,165 main INFO screen NOVISCIA pass=0 dev=6.25 ins=29.76 pro=15 1a=False 1b=False 2=True (59.2s)
Sep 13 03:25:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:25:37,135 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:25:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:25:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:25:40,396 main INFO screen Medusa pass=0 dev=67.25 ins=0.0 pro=40 1a=False 1b=False 2=False (71.1s)
Sep 13 03:26:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:26:26,558 main INFO screen NEKO pass=0 dev=71.24 ins=0.0 pro=3 1a=False 1b=False 2=True (74.7s)
Sep 13 03:26:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:26:27,614 main INFO screen OOmarley pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (60.4s)
Sep 13 03:26:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:26:39,172 main INFO screen BMW pass=0 dev=0.03 ins=0.0 pro=8 1a=False 1b=False 2=False (58.8s)
Sep 13 03:27:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:27:33,163 main INFO screen BMSPLZ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 13 03:27:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:27:39,116 main INFO screen mmrich pass=0 dev=33.1 ins=0.0 pro=16 1a=False 1b=False 2=False (72.6s)
Sep 13 03:28:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:28:08,210 main INFO screen WHALEZ pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (63.9s)
Sep 13 03:28:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:28:35,848 main INFO screen VPN pass=0 dev=0.0 ins=20.58 pro=39 1a=False 1b=False 2=True (54.4s)
Sep 13 03:28:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:28:47,333 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (52.0s)
Sep 13 03:30:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:30:36,925 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:30:36 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-13T02:49:09Z
--- update 2026-09-13T02:54:33Z
--- update 2026-09-13T02:59:36Z
--- update 2026-09-13T03:04:47Z
--- update 2026-09-13T03:09:50Z
--- update 2026-09-13T03:14:57Z
--- update 2026-09-13T03:20:31Z
--- update 2026-09-13T03:25:36Z
--- update 2026-09-13T03:30:35Z
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
