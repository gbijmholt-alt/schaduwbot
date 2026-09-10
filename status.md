# Schaduwbot status

- tijd: 2026-09-10 23:23:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 9 hours, 36 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 632/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 34498, "tokens_in_memory": 1521, "msgs": 7109148, "trades": 1311417, "creates": 14206, "decode_fail": 99170, "rpc_calls": 21521, "rpc_errors": 2115, "sol_usd": 99.09590372419443, "open_positions": 87}
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
Sep 10 23:10:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:12,271 main INFO screen Democratism pass=1 dev=0.0 ins=11.97 pro=20 1a=False 1b=False 2=False (0.6s)
Sep 10 23:10:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:15,029 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:10:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:15,158 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:10:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:20,408 main INFO screen JarSol pass=0 dev=0.0 ins=12.34 pro=17 1a=False 1b=False 2=True (5.4s)
Sep 10 23:10:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:44,693 main INFO screen KTM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 10 23:10:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:10:52,757 main INFO screen ASSmeat pass=0 dev=0.15 ins=0.0 pro=5 1a=False 1b=False 2=False (3.7s)
Sep 10 23:11:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:15,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:11:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:15,125 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:11:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:17,519 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:23:11:17 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 10 23:11:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:17,875 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:23:11:17 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 10 23:11:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:19,181 main INFO screen moon pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 10 23:11:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:22,154 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 10 23:11:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:31,007 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:11:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:31,104 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:11:37,293 main INFO screen GRIMBUS pass=0 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=True (6.4s)
Sep 10 23:12:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:12:21,948 main INFO screen BOMB pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 10 23:13:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:13:05,916 main INFO screen HALH pass=0 dev=3.94 ins=0.0 pro=3 1a=False 1b=False 2=False (8.7s)
Sep 10 23:13:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:13:07,126 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:13:07 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 23:14:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:14:27,360 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:14:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:14:27,488 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:14:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:14:27,851 main INFO screen DUST pass=0 dev=0.0 ins=20.64 pro=34 1a=False 1b=False 2=True (0.6s)
Sep 10 23:15:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:18,550 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:15:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:18,686 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:15:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:18,729 main INFO screen Ordihood pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 10 23:15:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:24,932 main INFO screen PUMPBALL pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=True (6.4s)
Sep 10 23:15:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:41,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:15:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:41,731 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:15:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:15:47,765 main INFO screen FINE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (6.2s)
Sep 10 23:16:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:12,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:16:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:13,126 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:16:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:17,380 main INFO screen FLS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 10 23:16:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:51,868 main INFO screen pegged pass=0 dev=0.0 ins=22.41 pro=60 1a=False 1b=False 2=True (6.7s)
Sep 10 23:16:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:51,964 main INFO screen 10M pass=0 dev=19.67 ins=3.66 pro=18 1a=False 1b=True 2=False (9.7s)
Sep 10 23:16:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:53,531 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:16:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:53,697 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:16:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:16:59,790 main INFO screen pegged pass=0 dev=0.0 ins=22.62 pro=15 1a=False 1b=False 2=True (6.3s)
Sep 10 23:17:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:17:16,928 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:17:17,019 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:17:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:17:21,296 main INFO screen SK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.5s)
Sep 10 23:17:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:17:42,378 main INFO screen $CAJUN pass=0 dev=0.57 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 10 23:17:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:17:46,031 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (10.8s)
Sep 10 23:18:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:06,151 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:18:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:06,242 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:18:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:06,581 main INFO screen TOGE pass=0 dev=0.0 ins=0.0 pro=31 1a=False 1b=False 2=True (0.5s)
Sep 10 23:18:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:07,331 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:18:07 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 23:18:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:24,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:18:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:24,133 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:18:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:18:30,662 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 10 23:19:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:07,273 main INFO screen FİRST  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 10 23:19:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:09,404 main INFO screen Solaween pass=0 dev=0.0 ins=16.31 pro=24 1a=False 1b=False 2=True (3.8s)
Sep 10 23:19:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:14,830 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:19:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:14,987 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:19:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:18,979 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.2s)
Sep 10 23:19:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:19:54,231 main INFO screen pumponfone pass=0 dev=6.63 ins=23.09 pro=38 1a=False 1b=False 2=False (6.8s)
Sep 10 23:21:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:03,958 main INFO screen $GOAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 10 23:21:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:17,277 main INFO screen sol pass=0 dev=0.07 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 10 23:21:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:18,759 main INFO screen muu pass=1 dev=3.42 ins=11.75 pro=46 1a=False 1b=False 2=False (2.5s)
Sep 10 23:21:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:26,653 main INFO screen last coin pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 10 23:21:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:30,406 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:21:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:30,575 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:21:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:37,504 main INFO screen TikTok pass=0 dev=0.0 ins=44.09 pro=8 1a=False 1b=False 2=True (7.1s)
Sep 10 23:21:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:39,156 main INFO screen $WTC pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 10 23:21:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:53,511 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:21:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:53,565 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:21:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:21:59,274 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 10 23:22:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:27,350 main INFO screen NFT pass=0 dev=0.0 ins=16.15 pro=65 1a=False 1b=False 2=True (5.5s)
Sep 10 23:22:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:31,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:22:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:31,852 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:22:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:35,951 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 10 23:22:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:36,523 main INFO screen TOTH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 10 23:22:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:37,470 main INFO screen GAT pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 10 23:22:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:45,021 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:22:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:45,147 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:22:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:22:49,038 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 23:23:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:14,463 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:23:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:14,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:23:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:14,693 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:23:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:14,814 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:23:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:15,144 main INFO screen JEET pass=0 dev=0.0 ins=15.44 pro=10 1a=False 1b=False 2=True (0.8s)
Sep 10 23:23:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:23:15,781 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:23:15 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
