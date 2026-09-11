# Schaduwbot status

- tijd: 2026-09-11 21:42:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 7 hours, 55 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 748/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 7348, "tokens_in_memory": 2598, "msgs": 1556927, "trades": 308316, "creates": 2598, "decode_fail": 22575, "rpc_calls": 9736, "rpc_errors": 410, "sol_usd": 102.5885159877797, "open_positions": 128, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 21:40 UTC

Gelogde schaduwtrades: **33418**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 25144 | 3869 | 41 | 3866 | 323 | 7170 | 21063 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 392 | 17% | 2.0% | +43.1% | -17.1% | -6.97% | 100% |
| dip35_V1_gescreend_fail | 3269 | 27% | 3.7% | +46.2% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 3872 | 26% | 3.7% | +45.1% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 386 | 21% | 3.1% | +43.9% | -21.8% | -8.06% | 100% |
| dip35_V2_gescreend_fail | 3272 | 25% | 4.3% | +56.7% | -28.3% | -7.31% | 100% |
| dip35_V2_alle | 3828 | 24% | 4.3% | +54.6% | -27.9% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 388 | 8% | 3.6% | +374.3% | -23.1% | +8.68% | 100% |
| dip35_V3_gescreend_fail | 3339 | 13% | 5.9% | +119.3% | -29.8% | -9.88% | 100% |
| dip35_V3_alle | 3878 | 13% | 5.8% | +129.9% | -29.3% | -8.55% | 100% |
| dip40_V1_gescreend_pass | 362 | 15% | 1.9% | +46.6% | -16.2% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 3194 | 26% | 3.7% | +48.0% | -26.0% | -6.60% | 100% |
| dip40_V1_alle | 3721 | 25% | 3.6% | +47.7% | -25.2% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 356 | 16% | 2.5% | +48.9% | -20.4% | -9.09% | 100% |
| dip40_V2_gescreend_fail | 3185 | 25% | 4.2% | +56.0% | -28.2% | -7.32% | 100% |
| dip40_V2_alle | 3670 | 24% | 4.2% | +55.0% | -27.7% | -7.90% | 100% |
| dip40_V3_gescreend_pass | 361 | 7% | 2.8% | +423.8% | -21.4% | +8.19% | 100% |
| dip40_V3_gescreend_fail | 3251 | 13% | 5.7% | +113.9% | -29.6% | -11.00% | 100% |
| dip40_V3_alle | 3725 | 12% | 5.5% | +126.8% | -29.0% | -9.66% | 100% |
| dip45_V1_gescreend_pass | 348 | 16% | 1.7% | +50.0% | -16.0% | -5.37% | 99% |
| dip45_V1_gescreend_fail | 3112 | 27% | 3.2% | +48.6% | -25.7% | -5.39% | 100% |
| dip45_V1_alle | 3593 | 26% | 3.2% | +48.6% | -25.0% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 340 | 19% | 2.4% | +47.9% | -20.1% | -7.29% | 100% |
| dip45_V2_gescreend_fail | 3095 | 25% | 3.8% | +58.7% | -27.9% | -6.12% | 100% |
| dip45_V2_alle | 3543 | 24% | 3.8% | +57.4% | -27.3% | -6.72% | 100% |
| dip45_V3_gescreend_pass | 343 | 7% | 2.3% | +467.9% | -20.6% | +13.58% | 100% |
| dip45_V3_gescreend_fail | 3150 | 14% | 5.3% | +120.8% | -29.1% | -8.30% | 100% |
| dip45_V3_alle | 3588 | 13% | 5.2% | +136.3% | -28.5% | -6.77% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 1.1%, kans ruïne 98.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2548 | 13% | 3.2% | -10.54% | 100% |
| zonder_xlink | 728 | 19% | 0.0% | +30.12% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 21:33:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:20,919 main INFO screen JASON pass=1 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (3.5s)
Sep 11 21:33:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:49,575 main INFO screen Bank pass=0 dev=0.0 ins=14.56 pro=78 1a=False 1b=False 2=True (3.1s)
Sep 11 21:33:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:55,267 main INFO screen Matrix pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 21:33:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:33:56,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:01,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:02,199 main INFO screen Greed pass=1 dev=0.0 ins=7.51 pro=19 1a=False 1b=False 2=False (2.3s)
Sep 11 21:34:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:05,312 main INFO screen Stick pass=0 dev=0.0 ins=19.53 pro=67 1a=False 1b=False 2=True (9.3s)
Sep 11 21:34:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:06,879 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:12,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:17,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:21,533 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 11 21:34:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:31,856 main INFO screen POSES pass=1 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (4.5s)
Sep 11 21:34:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:32,954 main INFO screen ElonWifHat pass=0 dev=78.8 ins=0.0 pro=4 1a=False 1b=False 2=True (20.5s)
Sep 11 21:34:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:45,024 main INFO screen 100 pass=0 dev=4.41 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 21:34:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:53,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:57,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:34:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:34:58,416 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:02,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:09,868 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.1s)
Sep 11 21:35:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:12,905 main INFO screen TOKABU pass=0 dev=0.0 ins=15.68 pro=57 1a=False 1b=False 2=True (19.6s)
Sep 11 21:35:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:16,506 main INFO screen LMC pass=0 dev=0.0 ins=18.34 pro=37 1a=False 1b=False 2=True (19.0s)
Sep 11 21:35:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:36,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:35:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:43,225 main INFO screen KIRK pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 21:35:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:43,795 main INFO screen YOTSUBA pass=0 dev=0.18 ins=0.0 pro=36 1a=False 1b=True 2=False (7.6s)
Sep 11 21:35:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:51,256 main INFO screen HALH pass=0 dev=0.94 ins=0.0 pro=4 1a=False 1b=False 2=False (2.7s)
Sep 11 21:35:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:35:55,124 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:36:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:03,645 main INFO screen BRAINS pass=0 dev=13.58 ins=0.0 pro=30 1a=False 1b=False 2=False (4.4s)
Sep 11 21:36:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:04,284 main INFO screen ice man pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 21:36:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:24,470 main INFO screen ATH pass=1 dev=1.74 ins=12.96 pro=53 1a=False 1b=False 2=False (6.0s)
Sep 11 21:36:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:36:38,815 main INFO screen SUPERSTONK pass=0 dev=0.0 ins=18.48 pro=68 1a=False 1b=False 2=True (3.8s)
Sep 11 21:37:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:21,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:37:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:21,292 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:37:21 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 21:37:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:23,203 main INFO screen EARTHVALLEY pass=1 dev=0.0 ins=5.21 pro=47 1a=False 1b=False 2=False (3.2s)
Sep 11 21:37:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:29,390 main INFO screen DOGELESS pass=0 dev=0.0 ins=0.0 pro=68 1a=False 1b=False 2=True (8.8s)
Sep 11 21:37:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:43,789 main INFO screen Bricko pass=0 dev=0.3 ins=0.0 pro=5 1a=False 1b=False 2=False (2.2s)
Sep 11 21:37:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:52,653 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 21:37:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:52,969 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:37:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:37:58,070 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:16,032 main INFO screen RABFROG pass=0 dev=0.47 ins=53.04 pro=22 1a=False 1b=False 2=True (23.1s)
Sep 11 21:38:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:25,071 main INFO screen WCOI pass=0 dev=1.22 ins=0.0 pro=3 1a=False 1b=False 2=False (4.1s)
Sep 11 21:38:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:32,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,727 main INFO screen EMS pass=1 dev=0.0 ins=9.39 pro=14 1a=False 1b=False 2=False (1.5s)
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,769 aiohttp.access INFO 45.156.129.132 [11/Sep/2026:21:38:38 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 11 21:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:52,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:52,671 main INFO screen BUTTHOLE pass=0 dev=1.74 ins=19.05 pro=73 1a=False 1b=False 2=True (20.1s)
Sep 11 21:38:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:57,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,572 main INFO screen ELOGE pass=0 dev=0.0 ins=17.81 pro=39 1a=False 1b=False 2=True (5.9s)
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,796 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,888 main INFO screen Trump4Prez pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 11 21:39:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:03,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:05,868 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:08,286 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:13,645 main INFO screen Peg pass=0 dev=0.0 ins=20.94 pro=73 1a=False 1b=False 2=True (21.5s)
Sep 11 21:39:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:19,438 main INFO screen NOKY pass=0 dev=0.18 ins=79.13 pro=6 1a=False 1b=True 2=True (18.9s)
Sep 11 21:39:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:23,015 main INFO screen MEME pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 11 21:39:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:46,533 main INFO screen $CAT pass=0 dev=0.71 ins=0.0 pro=1 1a=False 1b=False 2=False (4.4s)
Sep 11 21:39:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:54,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:00,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:03,861 main INFO screen DOGA pass=0 dev=0.43 ins=0.0 pro=3 1a=False 1b=False 2=False (5.6s)
Sep 11 21:40:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:10,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:59,586 main INFO screen pill pass=0 dev=0.0 ins=24.51 pro=46 1a=False 1b=False 2=True (64.8s)
Sep 11 21:41:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:01,387 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 11 21:41:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:01,783 main INFO screen Inu pass=1 dev=0.0 ins=0.76 pro=53 1a=False 1b=False 2=False (6.6s)
Sep 11 21:41:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:02,918 main INFO screen CATBULL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 11 21:41:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:28,465 main INFO screen mmrich pass=0 dev=0.47 ins=0.0 pro=2 1a=False 1b=False 2=False (4.2s)
Sep 11 21:41:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:34,296 main INFO screen MOMO pass=1 dev=0.0 ins=11.3 pro=17 1a=False 1b=False 2=False (1.6s)
Sep 11 21:41:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:45,386 main INFO screen GOSI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 21:41:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:46,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:41:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:51,545 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:41:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:55,700 main INFO screen 911 pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 11 21:42:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:05,824 main INFO screen Meowcraft pass=0 dev=0.0 ins=22.31 pro=34 1a=False 1b=False 2=True (19.4s)
Sep 11 21:42:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:15,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:15,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:20,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:23,836 main INFO screen GOSI pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 21:42:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:27,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:32,615 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:35,834 main INFO screen FOMOLIFE pass=0 dev=0.0 ins=8.3 pro=46 1a=False 1b=False 2=True (20.8s)
Sep 11 21:42:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:37,270 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:42:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T20:15:22Z
--- update 2026-09-11T20:20:26Z
--- update 2026-09-11T20:25:28Z
--- update 2026-09-11T20:30:28Z
--- update 2026-09-11T20:35:28Z
--- update 2026-09-11T20:40:31Z
--- update 2026-09-11T20:45:33Z
--- update 2026-09-11T20:50:36Z
--- update 2026-09-11T20:55:37Z
--- update 2026-09-11T21:00:40Z
--- update 2026-09-11T21:05:43Z
--- update 2026-09-11T21:11:05Z
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
--- update 2026-09-11T21:42:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
```

## Analyses (laatste 25 regels)
```
active
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
19:40:08 12765 tokens sinds start volledige logging, waarvan 3627 met een gat door herstart
19:40:11   ingelezen tot rowid 2225120 (145387 rijen, 145387 bruikbaar)
19:40:11 ingelezen: 145387 nieuwe trades, 145387 bruikbaar (3s)
19:40:22 177 aankopen van gevolgde wallets geëvalueerd
19:40:34 grote spelers: saldo van 2000 wallets opgehaald
19:41:46 herkomst: 40 posities gekoppeld
19:41:47 klaar in 99s -> /opt/schaduwbot/reports/ledger.md
19:41:49 klaar in 1s: 6168 tokens, 1142 nieuw -> /opt/schaduwbot/reports/video_replay.md
19:41:49 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 19:41 UTC
19:41:49 37636 tokens geladen
19:41:51   2000 tokens, 281880 trades, 68228 posities (2s)
19:41:53   4000 tokens, 562091 trades, 134424 posities (4s)
19:41:56   6000 tokens, 870184 trades, 206311 posities (7s)
19:41:58   8000 tokens, 1149114 trades, 266897 posities (9s)
19:42:01   10000 tokens, 1443511 trades, 336633 posities (12s)
19:42:03   12000 tokens, 1716836 trades, 400450 posities (14s)
19:42:06   14000 tokens, 1988268 trades, 462617 posities (17s)
19:42:08 posities: 523618 uit 2226699 trades (19s)
19:42:14 123108 wallets gerekend
19:42:14 geluk-toets
19:42:33 persistentie
19:42:34 kopieer-simulatie
19:42:39 klaar in 51s -> /opt/schaduwbot/reports/wallets.md
21:42:36 15363 tokens sinds start volledige logging, waarvan 5134 met een gat door herstart
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
