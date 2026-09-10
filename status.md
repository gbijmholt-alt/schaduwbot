# Schaduwbot status

- tijd: 2026-09-10 22:51:44 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 9 hours, 4 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 636/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 32607, "tokens_in_memory": 1543, "msgs": 6663127, "trades": 1236657, "creates": 13494, "decode_fail": 94340, "rpc_calls": 20287, "rpc_errors": 2012, "sol_usd": 99.53778856368744, "open_positions": 117}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 22:48 UTC

Gelogde schaduwtrades: **10555**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 13367 | 1895 | 28 | 1895 | 171 | 3561 | 10555 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 136 | 15% | 2.2% | +38.4% | -17.1% | -8.50% | 92% |
| dip35_V1_gescreend_fail | 1057 | 26% | 4.3% | +45.9% | -25.7% | -6.96% | 100% |
| dip35_V1_alle | 1231 | 25% | 4.3% | +44.7% | -25.1% | -7.57% | 100% |
| dip35_V2_gescreend_pass | 135 | 17% | 3.0% | +29.4% | -22.0% | -13.23% | 98% |
| dip35_V2_gescreend_fail | 1052 | 24% | 4.9% | +54.7% | -28.1% | -8.12% | 100% |
| dip35_V2_alle | 1216 | 23% | 5.0% | +52.0% | -27.8% | -9.27% | 100% |
| dip35_V3_gescreend_pass | 135 | 7% | 3.0% | +132.0% | -23.6% | -13.23% | 99% |
| dip35_V3_gescreend_fail | 1064 | 12% | 6.7% | +124.9% | -30.0% | -11.93% | 100% |
| dip35_V3_alle | 1226 | 11% | 6.5% | +122.0% | -29.5% | -12.61% | 100% |
| dip40_V1_gescreend_pass | 125 | 14% | 3.2% | +43.8% | -16.5% | -8.26% | 91% |
| dip40_V1_gescreend_fail | 1023 | 25% | 4.3% | +49.3% | -25.5% | -6.57% | 100% |
| dip40_V1_alle | 1179 | 24% | 4.3% | +48.3% | -24.7% | -7.03% | 100% |
| dip40_V2_gescreend_pass | 124 | 13% | 3.2% | +47.2% | -21.1% | -12.29% | 97% |
| dip40_V2_gescreend_fail | 1020 | 24% | 4.7% | +55.7% | -27.8% | -7.45% | 100% |
| dip40_V2_alle | 1165 | 23% | 4.7% | +54.6% | -27.3% | -8.39% | 100% |
| dip40_V3_gescreend_pass | 124 | 7% | 3.2% | +116.7% | -22.4% | -12.34% | 98% |
| dip40_V3_gescreend_fail | 1033 | 11% | 6.2% | +107.4% | -29.5% | -13.84% | 100% |
| dip40_V3_alle | 1176 | 11% | 6.0% | +105.8% | -28.9% | -14.04% | 100% |
| dip45_V1_gescreend_pass | 113 | 13% | 3.5% | +43.4% | -16.0% | -8.15% | 91% |
| dip45_V1_gescreend_fail | 990 | 26% | 3.7% | +51.1% | -24.9% | -4.96% | 100% |
| dip45_V1_alle | 1126 | 25% | 3.9% | +50.3% | -24.2% | -5.59% | 100% |
| dip45_V2_gescreend_pass | 112 | 16% | 4.5% | +40.3% | -20.6% | -10.83% | 94% |
| dip45_V2_gescreend_fail | 984 | 25% | 4.2% | +61.0% | -27.2% | -5.25% | 100% |
| dip45_V2_alle | 1112 | 24% | 4.4% | +59.2% | -26.8% | -6.21% | 100% |
| dip45_V3_gescreend_pass | 113 | 6% | 4.4% | +185.1% | -21.5% | -8.66% | 96% |
| dip45_V3_gescreend_fail | 997 | 12% | 5.8% | +128.5% | -28.9% | -9.47% | 100% |
| dip45_V3_alle | 1124 | 12% | 5.9% | +129.7% | -28.3% | -9.77% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 22:43:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:26,338 main INFO screen Dali pass=0 dev=6.71 ins=5.92 pro=20 1a=False 1b=False 2=False (3.4s)
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,272 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,714 main INFO screen AMD pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 22:43:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:56,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:57,345 main INFO screen PUMPLESS pass=0 dev=0.0 ins=15.61 pro=27 1a=False 1b=False 2=True (1.3s)
Sep 10 22:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:57,388 main INFO screen RAGE GURL pass=0 dev=0.73 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 10 22:43:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:59,988 main INFO screen $DRUSKI pass=0 dev=0.83 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 10 22:44:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:08,082 main INFO screen KATE pass=0 dev=1.16 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,090 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,349 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,461 main INFO screen Apu pass=0 dev=0.0 ins=16.96 pro=13 1a=False 1b=False 2=True (4.5s)
Sep 10 22:44:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:12,126 main INFO screen iPump pass=0 dev=0.0 ins=18.2 pro=10 1a=False 1b=False 2=True (2.2s)
Sep 10 22:44:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:39,352 main INFO screen Lingo pass=1 dev=0.0 ins=18.33 pro=12 1a=False 1b=False 2=False (1.6s)
Sep 10 22:44:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:55,986 main INFO screen AI pass=0 dev=0.0 ins=17.41 pro=16 1a=False 1b=False 2=True (3.8s)
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,360 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,451 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,642 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 22:46:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:46:12,749 main INFO screen solcat pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 10 22:46:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:46:37,148 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:46:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 22:47:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:11,837 main INFO screen Dali pass=0 dev=6.71 ins=5.92 pro=13 1a=False 1b=False 2=True (2.8s)
Sep 10 22:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:22,307 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:22,448 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:22,595 main INFO screen hippocampus pass=0 dev=0.0 ins=33.28 pro=31 1a=False 1b=False 2=True (0.3s)
Sep 10 22:47:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:27,243 main INFO screen Corf pass=0 dev=0.0 ins=0.92 pro=11 1a=False 1b=True 2=False (1.9s)
Sep 10 22:47:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:35,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:47:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:35,850 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:47:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:36,013 main INFO screen PUMP pass=0 dev=0.0 ins=18.01 pro=26 1a=False 1b=False 2=True (0.3s)
Sep 10 22:47:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:41,436 main INFO screen 1000X pass=0 dev=0.0 ins=18.55 pro=24 1a=False 1b=False 2=True (3.7s)
Sep 10 22:47:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:42,800 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:47:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:42,926 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:47:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:43,294 main INFO screen FOMO pass=0 dev=0.0 ins=18.48 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 22:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:51,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:47:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:51,384 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:47:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:52,154 main INFO screen CLICKING pass=0 dev=0.0 ins=19.16 pro=9 1a=False 1b=False 2=True (1.0s)
Sep 10 22:47:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:58,114 main INFO screen SOL CAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.4s)
Sep 10 22:47:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:58,673 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:47:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:58,792 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:47:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:47:58,965 main INFO screen RETARD pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 22:48:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:48:12,391 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:48:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:48:12,763 main INFO screen CATS pass=0 dev=2.08 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 22:48:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:48:14,846 main INFO screen BRAIN pass=0 dev=0.26 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 10 22:49:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:05,984 main INFO screen EARLY pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (8.9s)
Sep 10 22:49:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:07,132 main INFO screen CURE pass=0 dev=0.0 ins=15.3 pro=48 1a=False 1b=False 2=True (10.0s)
Sep 10 22:49:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:07,847 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:49:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:08,096 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:49:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:08,515 main INFO screen Puter pass=0 dev=0.0 ins=8.92 pro=12 1a=False 1b=False 2=True (0.8s)
Sep 10 22:49:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:09,180 main INFO screen CURE pass=0 dev=0.0 ins=24.24 pro=15 1a=False 1b=False 2=True (11.3s)
Sep 10 22:49:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:25,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:49:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:25,728 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:49:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:26,327 main INFO screen Puter pass=0 dev=0.0 ins=26.45 pro=7 1a=False 1b=False 2=True (0.8s)
Sep 10 22:49:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:41,108 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:49:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:41,319 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:49:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:41,885 main INFO screen OTC pass=0 dev=0.0 ins=12.57 pro=21 1a=False 1b=False 2=True (1.1s)
Sep 10 22:49:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:42,384 main INFO screen meme pass=0 dev=0.14 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 22:49:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:46,927 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:22:49:46 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 10 22:49:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:49:47,280 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:22:49:47 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 10 22:50:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:50:32,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:50:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:50:32,994 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:50:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:50:33,348 main INFO screen OTC pass=0 dev=0.0 ins=9.14 pro=26 1a=False 1b=False 2=True (0.6s)
Sep 10 22:51:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:00,259 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:51:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:00,374 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:00,740 main INFO screen puter pass=0 dev=0.0 ins=11.67 pro=41 1a=False 1b=False 2=True (0.6s)
Sep 10 22:51:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:06,473 main INFO screen LOST pass=0 dev=6.71 ins=5.92 pro=8 1a=False 1b=False 2=False (3.7s)
Sep 10 22:51:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:06,650 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:51:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:06,776 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:07,038 main INFO screen CURECОIN pass=0 dev=0.0 ins=6.66 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 22:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:14,167 main INFO screen ETHMINER pass=0 dev=0.03 ins=1.95 pro=60 1a=False 1b=True 2=False (2.0s)
Sep 10 22:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:14,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:14,980 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:15,380 main INFO screen 72X pass=0 dev=0.0 ins=17.93 pro=14 1a=False 1b=False 2=True (0.8s)
Sep 10 22:51:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:16,494 main INFO screen fancat pass=0 dev=0.0 ins=18.34 pro=7 1a=False 1b=False 2=False (2.0s)
Sep 10 22:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:22,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:22,803 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:22,930 main INFO screen CURECОIN pass=0 dev=0.0 ins=35.6 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 22:51:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:34,003 main INFO screen $CAJUN pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 10 22:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:42,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:42,933 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:43,079 main INFO screen TNON pass=0 dev=0.0 ins=24.52 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 10 22:51:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:44,262 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:51:44 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
