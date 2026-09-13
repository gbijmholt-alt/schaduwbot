# Schaduwbot status

- tijd: 2026-09-13 03:41:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 13 hours, 54 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.1G/38G | geheugen: 1389/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 25669, "tokens_in_memory": 6869, "msgs": 2677199, "trades": 785174, "creates": 8561, "decode_fail": 79343, "rpc_calls": 21134, "rpc_errors": 5, "sol_usd": 101.84368902117846, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 3593 | 424 | 7 | 432 | 70 | 773 | 2341 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 606 | 17% | 1.7% | +43.3% | -15.9% | -5.93% | 100% |
| dip35_V1_gescreend_fail | 4706 | 27% | 3.9% | +45.1% | -25.9% | -6.78% | 100% |
| dip35_V1_alle | 6338 | 26% | 3.9% | +44.4% | -25.4% | -7.01% | 100% |
| dip35_V2_gescreend_pass | 604 | 23% | 2.3% | +40.7% | -20.2% | -6.40% | 100% |
| dip35_V2_gescreend_fail | 4783 | 25% | 4.4% | +54.7% | -27.9% | -7.03% | 100% |
| dip35_V2_alle | 6295 | 25% | 4.5% | +52.2% | -27.7% | -7.99% | 100% |
| dip35_V3_gescreend_pass | 611 | 9% | 3.3% | +261.0% | -22.0% | +3.91% | 100% |
| dip35_V3_gescreend_fail | 4910 | 14% | 6.1% | +118.2% | -29.6% | -9.43% | 100% |
| dip35_V3_alle | 6349 | 13% | 6.1% | +116.6% | -29.4% | -10.31% | 100% |
| dip40_V1_gescreend_pass | 577 | 15% | 1.7% | +43.7% | -15.4% | -6.62% | 100% |
| dip40_V1_gescreend_fail | 4631 | 26% | 3.9% | +46.7% | -25.8% | -6.66% | 100% |
| dip40_V1_alle | 6094 | 26% | 3.9% | +46.5% | -25.3% | -6.97% | 100% |
| dip40_V2_gescreend_pass | 577 | 18% | 2.1% | +43.2% | -19.5% | -8.07% | 100% |
| dip40_V2_gescreend_fail | 4684 | 25% | 4.3% | +54.7% | -27.8% | -6.99% | 100% |
| dip40_V2_alle | 6045 | 24% | 4.4% | +53.1% | -27.6% | -8.05% | 100% |
| dip40_V3_gescreend_pass | 584 | 8% | 2.9% | +260.2% | -21.0% | +2.07% | 100% |
| dip40_V3_gescreend_fail | 4795 | 13% | 5.8% | +113.9% | -29.4% | -10.29% | 100% |
| dip40_V3_alle | 6101 | 13% | 5.9% | +113.1% | -29.1% | -11.09% | 100% |
| dip45_V1_gescreend_pass | 556 | 15% | 1.6% | +46.7% | -15.2% | -5.82% | 100% |
| dip45_V1_gescreend_fail | 4549 | 27% | 3.6% | +48.1% | -25.6% | -5.54% | 100% |
| dip45_V1_alle | 5892 | 26% | 3.6% | +48.2% | -25.1% | -6.02% | 100% |
| dip45_V2_gescreend_pass | 555 | 19% | 2.0% | +42.5% | -19.5% | -7.87% | 100% |
| dip45_V2_gescreend_fail | 4594 | 25% | 4.0% | +58.4% | -27.5% | -5.82% | 100% |
| dip45_V2_alle | 5845 | 24% | 4.1% | +56.7% | -27.3% | -6.90% | 100% |
| dip45_V3_gescreend_pass | 562 | 8% | 2.5% | +286.8% | -20.4% | +4.16% | 100% |
| dip45_V3_gescreend_fail | 4689 | 14% | 5.5% | +120.6% | -28.9% | -7.99% | 100% |
| dip45_V3_alle | 5891 | 13% | 5.5% | +121.7% | -28.7% | -9.00% | 100% |

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
| per_token_met_xlink | 478 | 16% | 5.4% | -8.14% | -11.3% tot -5.0% | -14.3% | – | 100% |
| per_token_zonder_xlink | 147 | 23% | 0.0% | +19.56% | -8.8% tot +47.9% | -13.1% | 118% | 58% |
| gepoold_met_xlink | 4007 | 14% | 2.9% | -9.30% | -10.5% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1225 | 18% | 0.0% | +16.07% | +0.1% tot +32.1% | -14.3% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
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
Sep 13 03:31:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:31:10,865 main INFO screen LAMBO pass=0 dev=9.64 ins=0.0 pro=45 1a=False 1b=False 2=False (55.8s)
Sep 13 03:31:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:31:58,919 main INFO screen ASTRAL pass=0 dev=13.0 ins=24.94 pro=12 1a=False 1b=False 2=False (60.0s)
Sep 13 03:32:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:32:55,967 main INFO screen BENZ pass=0 dev=7.96 ins=0.0 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 13 03:33:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:33:10,854 main INFO screen DINGLE pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (72.5s)
Sep 13 03:33:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:33:42,995 main INFO screen INU pass=1 dev=0.0 ins=4.51 pro=63 1a=False 1b=False 2=False (72.1s)
Sep 13 03:34:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:34:33,411 rpc WARNING rpc getSignaturesForAddress exc
Sep 13 03:34:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:34:33,421 rpc WARNING rpc getSignaturesForAddress exc
Sep 13 03:34:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:34:42,356 main INFO screen FLYINU pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (106.4s)
Sep 13 03:34:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:34:59,419 main INFO screen LUIGI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (102.1s)
Sep 13 03:35:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:35:35,889 main INFO screen Mclowny11 pass=0 dev=0.0 ins=8.14 pro=79 1a=False 1b=False 2=True (112.9s)
Sep 13 03:35:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:35:40,078 main INFO screen Mclowny11 pass=0 dev=0.0 ins=15.14 pro=28 1a=False 1b=False 2=True (57.7s)
Sep 13 03:35:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:35:54,433 main INFO screen Mclowny11 pass=0 dev=0.0 ins=24.7 pro=11 1a=False 1b=False 2=False (55.0s)
Sep 13 03:36:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:36:12,258 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:36:12 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 03:36:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:36:28,936 main INFO screen Mclowny11 pass=0 dev=0.0 ins=25.78 pro=10 1a=False 1b=False 2=True (53.0s)
Sep 13 03:36:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:36:39,430 main INFO screen PNUTGPT pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (59.4s)
Sep 13 03:37:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:37:02,004 main INFO screen Mclowny11 pass=0 dev=0.0 ins=25.03 pro=43 1a=False 1b=False 2=True (67.6s)
Sep 13 03:37:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:37:34,883 main INFO screen IRIS pass=0 dev=10.0 ins=39.12 pro=16 1a=False 1b=True 2=True (54.1s)
Sep 13 03:37:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:37:55,183 main INFO screen Smiski pass=0 dev=0.0 ins=21.07 pro=63 1a=False 1b=False 2=True (63.3s)
Sep 13 03:40:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:40:06,441 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.4s)
Sep 13 03:40:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:40:06,511 main INFO screen LMAO pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (78.1s)
Sep 13 03:40:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:40:29,288 main INFO screen FR! pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.5s)
Sep 13 03:41:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 03:41:37,225 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:03:41:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-13T03:36:11Z
Running as unit: schaduwbot-wallets.service; invocation ID: 19b30d28839c4560ad0bcf4c5e040823
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T03:41:36Z
```

## Analyses (laatste 25 regels)
```
active
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
03:36:12 45414 tokens sinds start volledige logging, waarvan 12041 met een gat door herstart
03:36:23   ingelezen tot rowid 5297733 (187788 rijen, 187788 bruikbaar)
03:36:24 ingelezen: 187788 nieuwe trades, 187788 bruikbaar (12s)
03:37:13 2342 aankopen van gevolgde wallets geëvalueerd
03:37:24 vroege kopers: 162 voldoen nu, register 249, 253 tokens beoordeeld
03:37:37 grote spelers: saldo van 367 wallets opgehaald
03:38:01 herkomst: 40 posities gekoppeld
03:38:06 klaar in 115s -> /opt/schaduwbot/reports/ledger.md
03:38:56 S1: gezakt — toets n=3844, verkennend n=14656
03:38:56 klaar in 50s -> /opt/schaduwbot/reports/hypotheses.md
03:38:57 na-migratie: 400 paren te checken
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
