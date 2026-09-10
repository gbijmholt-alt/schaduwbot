# Schaduwbot status

- tijd: 2026-09-10 23:44:07 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 9 hours, 57 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 641/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 35750, "tokens_in_memory": 1465, "msgs": 7360712, "trades": 1359623, "creates": 14703, "decode_fail": 101575, "rpc_calls": 22546, "rpc_errors": 2185, "sol_usd": 99.09162461060278, "open_positions": 76}
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
Sep 10 23:32:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:32:53,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:32:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:32:54,124 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:32:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:32:54,257 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 23:33:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:07,626 main INFO screen CANADA pass=0 dev=11.32 ins=2.32 pro=19 1a=False 1b=False 2=False (2.0s)
Sep 10 23:33:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:11,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:33:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:11,414 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:33:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:11,563 main INFO screen SLK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 23:33:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:49,071 main INFO screen Bruv pass=0 dev=0.0 ins=18.51 pro=44 1a=False 1b=False 2=True (2.8s)
Sep 10 23:33:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:33:50,540 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:33:50 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 23:34:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:14,326 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 23:34:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:30,601 main INFO screen BLFT pass=0 dev=0.63 ins=0.0 pro=7 1a=False 1b=False 2=False (3.7s)
Sep 10 23:34:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:37,574 main INFO screen KEEN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 10 23:34:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:41,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:34:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:41,827 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:34:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:42,160 main INFO screen foneless pass=0 dev=0.0 ins=23.68 pro=20 1a=False 1b=False 2=True (0.5s)
Sep 10 23:34:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:50,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:34:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:50,778 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:34:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:34:50,902 main INFO screen FLAPPY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 23:35:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:35:11,417 main INFO screen FINE pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 23:36:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:09,042 main INFO screen LCOST pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (2.8s)
Sep 10 23:36:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:47,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:36:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:47,375 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:36:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:47,566 main INFO screen SOL CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 23:36:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:48,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:36:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:48,168 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:36:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:48,287 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 23:36:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:49,600 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:36:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:49,722 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:36:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:49,864 main INFO screen DELULU pass=1 dev=0.0 ins=13.86 pro=11 1a=False 1b=False 2=False (0.3s)
Sep 10 23:36:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:36:55,852 main INFO screen DERP pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (3.6s)
Sep 10 23:37:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:02,514 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 10 23:37:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:10,123 main INFO screen BPCATE pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 23:37:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:26,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:37:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:26,561 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:37:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:27,518 main INFO screen DREGG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.2s)
Sep 10 23:37:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:29,498 main INFO screen DELULU pass=0 dev=0.0 ins=21.91 pro=43 1a=False 1b=False 2=True (1.2s)
Sep 10 23:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:45,118 main INFO screen PDFSURX pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 23:37:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:47,029 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:37:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:47,148 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:37:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:37:47,267 main INFO screen PMG pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 10 23:38:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:14,689 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 10 23:38:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:17,673 main INFO screen BIRDCAT pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (4.3s)
Sep 10 23:38:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:24,989 main INFO screen Cluck pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (3.2s)
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,368 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,424 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:38:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:38:41,653 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 23:39:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:00,425 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:39:00 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 23:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:02,302 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,127 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:13,239 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.0s)
Sep 10 23:39:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:15,897 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:39:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:16,031 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:39:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:16,151 main INFO screen Lulu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 23:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:39:33,443 main INFO screen dog pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (3.3s)
Sep 10 23:40:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:40:58,926 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 23:41:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:02,820 main INFO screen SLIPPAGE pass=0 dev=0.16 ins=0.0 pro=3 1a=False 1b=False 2=False (4.5s)
Sep 10 23:41:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:03,987 main INFO screen CHUMP pass=0 dev=1.65 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 23:41:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:10,672 main INFO screen TALIS!! pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,638 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:41:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:11,782 main INFO screen Kirkaversa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 23:41:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:19,308 main INFO screen PDFSURX pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 10 23:41:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:41,544 main INFO screen STONK pass=0 dev=10.22 ins=5.22 pro=46 1a=False 1b=False 2=False (3.3s)
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,445 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:41:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:53,567 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 10 23:41:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:41:57,528 main INFO screen Messi pass=0 dev=0.12 ins=0.0 pro=2 1a=False 1b=False 2=False (1.6s)
Sep 10 23:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:53,683 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:53,775 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:42:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:42:54,297 main INFO screen CRACKSKI pass=0 dev=0.0 ins=29.78 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 10 23:43:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:28,735 main INFO screen SOLCAT pass=0 dev=0.05 ins=16.55 pro=67 1a=False 1b=False 2=True (3.4s)
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:43:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:43:52,799 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 23:44:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:02,203 main INFO screen pumplive pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,488 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,605 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:44:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:06,864 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 23:44:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:44:07,781 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:44:07 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
