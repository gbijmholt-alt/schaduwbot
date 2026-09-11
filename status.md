# Schaduwbot status

- tijd: 2026-09-11 01:08:28 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 11 hours, 21 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 649/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 40811, "tokens_in_memory": 1474, "msgs": 8051539, "trades": 1537831, "creates": 16622, "decode_fail": 109427, "rpc_calls": 25133, "rpc_errors": 2445, "sol_usd": 99.41650111815305, "open_positions": 64}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 00:48 UTC

Gelogde schaduwtrades: **13207**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 1153 | 134 | 0 | 135 | 13 | 286 | 852 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 162 | 15% | 1.9% | +37.5% | -17.3% | -8.81% | 96% |
| dip35_V1_gescreend_fail | 1320 | 25% | 4.2% | +44.8% | -25.8% | -7.86% | 100% |
| dip35_V1_alle | 1529 | 24% | 4.3% | +43.5% | -25.2% | -8.37% | 100% |
| dip35_V2_gescreend_pass | 161 | 16% | 2.5% | +31.2% | -21.8% | -13.23% | 99% |
| dip35_V2_gescreend_fail | 1328 | 23% | 4.9% | +52.0% | -28.2% | -9.54% | 100% |
| dip35_V2_alle | 1523 | 22% | 5.0% | +49.9% | -27.9% | -10.45% | 100% |
| dip35_V3_gescreend_pass | 163 | 6% | 2.5% | +143.0% | -23.3% | -13.07% | 99% |
| dip35_V3_gescreend_fail | 1337 | 12% | 6.5% | +125.8% | -30.0% | -11.93% | 100% |
| dip35_V3_alle | 1532 | 11% | 6.4% | +123.6% | -29.5% | -12.56% | 100% |
| dip40_V1_gescreend_pass | 151 | 12% | 2.6% | +43.2% | -16.7% | -9.56% | 96% |
| dip40_V1_gescreend_fail | 1282 | 25% | 4.4% | +48.1% | -25.9% | -7.72% | 100% |
| dip40_V1_alle | 1470 | 24% | 4.5% | +47.0% | -25.1% | -8.16% | 100% |
| dip40_V2_gescreend_pass | 150 | 12% | 2.7% | +43.6% | -21.0% | -13.26% | 99% |
| dip40_V2_gescreend_fail | 1291 | 24% | 4.8% | +53.8% | -28.1% | -8.78% | 100% |
| dip40_V2_alle | 1465 | 22% | 4.8% | +52.8% | -27.5% | -9.66% | 100% |
| dip40_V3_gescreend_pass | 152 | 6% | 2.6% | +116.7% | -22.0% | -13.78% | 99% |
| dip40_V3_gescreend_fail | 1302 | 11% | 6.3% | +112.0% | -29.7% | -13.49% | 100% |
| dip40_V3_alle | 1476 | 11% | 6.2% | +110.3% | -29.1% | -13.90% | 100% |
| dip45_V1_gescreend_pass | 140 | 14% | 2.9% | +49.0% | -16.0% | -7.17% | 93% |
| dip45_V1_gescreend_fail | 1239 | 27% | 3.7% | +49.9% | -25.3% | -5.12% | 100% |
| dip45_V1_alle | 1405 | 26% | 3.8% | +49.6% | -24.5% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 138 | 17% | 3.6% | +39.8% | -20.3% | -9.80% | 96% |
| dip45_V2_gescreend_fail | 1242 | 25% | 4.2% | +59.0% | -27.4% | -5.79% | 100% |
| dip45_V2_alle | 1398 | 24% | 4.4% | +57.3% | -26.9% | -6.57% | 100% |
| dip45_V3_gescreend_pass | 140 | 7% | 3.6% | +183.9% | -21.2% | -6.54% | 97% |
| dip45_V3_gescreend_fail | 1253 | 12% | 5.8% | +126.5% | -29.1% | -9.72% | 100% |
| dip45_V3_alle | 1409 | 12% | 5.8% | +128.5% | -28.5% | -9.77% | 100% |

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
Sep 11 00:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:14,251 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:14,605 main INFO screen 曙宝 pass=0 dev=0.0 ins=12.14 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 11 00:58:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:27,192 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:58:27 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 00:58:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:28,704 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:58:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:28,830 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:58:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:28,973 main INFO screen $GOOSE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 00:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:47,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:47,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:58:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:48,040 main INFO screen BULLCATE pass=0 dev=0.0 ins=32.03 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 00:59:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:06,884 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:59:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:06,981 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:59:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:07,171 main INFO screen 🇩🇪 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 00:59:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:07,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:59:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:07,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:59:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:07,987 main INFO screen BULL pass=0 dev=0.0 ins=42.99 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 11 00:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:26,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:26,182 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:26,358 main INFO screen corn pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 00:59:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:59:53,179 main INFO screen NEUS pass=1 dev=4.02 ins=0.8 pro=47 1a=False 1b=False 2=False (3.0s)
Sep 11 01:00:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:00:41,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:00:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:00:41,217 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:00:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:00:46,700 main INFO screen PUMPFROG pass=0 dev=0.0 ins=21.59 pro=12 1a=False 1b=False 2=True (5.7s)
Sep 11 01:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:14,686 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:14,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:01:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:21,621 main INFO screen Kirkaversa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.0s)
Sep 11 01:01:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:23,505 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:01:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:23,630 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:01:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:23,785 main INFO screen BROKE pass=0 dev=0.0 ins=26.38 pro=11 1a=False 1b=False 2=False (0.3s)
Sep 11 01:01:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:34,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:01:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:34,913 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:40,229 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.57 pro=4 1a=False 1b=False 2=True (5.5s)
Sep 11 01:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:40,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:40,605 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:01:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:01:46,655 main INFO screen PAIR pass=0 dev=0.0 ins=38.63 pro=8 1a=False 1b=False 2=True (6.2s)
Sep 11 01:02:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:02:24,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:02:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:02:24,619 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:02:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:02:25,043 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.6s)
Sep 11 01:02:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:02:43,946 main INFO screen KIRK pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 11 01:02:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:02:58,850 main INFO screen MISTAKE pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (7.3s)
Sep 11 01:03:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:03:28,424 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:03:28 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:03:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:03:52,987 main INFO screen SXSN pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=True (8.9s)
Sep 11 01:04:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:20,965 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:04:20 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 01:04:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:21,303 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:01:04:21 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 01:04:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:22,386 main INFO screen STOCKDOG pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 11 01:04:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:33,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:04:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:33,264 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:04:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:39,779 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.9 pro=3 1a=False 1b=False 2=True (6.7s)
Sep 11 01:04:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:44,785 main INFO screen Bliss pass=1 dev=0.0 ins=0.74 pro=24 1a=False 1b=False 2=False (9.5s)
Sep 11 01:04:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:04:58,420 main INFO screen cap pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 11 01:05:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:00,409 main INFO screen 曙宝 pass=1 dev=0.0 ins=11.04 pro=29 1a=False 1b=False 2=False (11.5s)
Sep 11 01:05:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:17,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:05:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:17,745 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:05:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:18,173 main INFO screen SCOOBY pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 11 01:05:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:24,704 main INFO screen CHILLFLY pass=0 dev=0.0 ins=42.3 pro=2 1a=False 1b=False 2=True (7.6s)
Sep 11 01:05:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:30,414 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:05:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:30,570 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:05:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:05:35,826 main INFO screen B pass=0 dev=0.0 ins=42.61 pro=14 1a=False 1b=False 2=True (5.4s)
Sep 11 01:06:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:05,034 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:06:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:05,170 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:06:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:05,774 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:06:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:05,903 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:06:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:06,273 main INFO screen B pass=0 dev=0.0 ins=19.28 pro=22 1a=False 1b=False 2=True (0.6s)
Sep 11 01:06:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:10,561 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.6s)
Sep 11 01:06:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:13,432 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:06:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:13,559 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:06:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:19,786 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=4 1a=False 1b=False 2=True (6.4s)
Sep 11 01:06:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:21,580 main INFO screen STOCKDOG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 11 01:06:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:23,305 main INFO screen B pass=1 dev=0.0 ins=8.37 pro=30 1a=False 1b=False 2=False (2.0s)
Sep 11 01:06:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:06:31,784 main INFO screen $OZZY pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (4.8s)
Sep 11 01:07:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:00,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:07:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:00,619 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:07:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:05,360 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=3 1a=False 1b=False 2=True (4.9s)
Sep 11 01:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:17,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:17,599 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:17,743 main INFO screen Luckyman pass=0 dev=0.0 ins=10.68 pro=19 1a=False 1b=False 2=True (0.3s)
Sep 11 01:07:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:35,291 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:07:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:35,429 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:07:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:07:39,556 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.3s)
Sep 11 01:08:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:08:01,215 main INFO screen VIPCAT pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 11 01:08:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:08:28,862 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:08:28 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
