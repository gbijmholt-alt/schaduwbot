# Schaduwbot status

- tijd: 2026-09-11 00:53:25 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 11 hours, 6 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 640/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 39909, "tokens_in_memory": 1384, "msgs": 7904253, "trades": 1508124, "creates": 16253, "decode_fail": 107914, "rpc_calls": 24748, "rpc_errors": 2379, "sol_usd": 98.8567518714715, "open_positions": 53}
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
Sep 11 00:39:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:39:53,804 main INFO screen DLS pass=0 dev=1.59 ins=0.0 pro=5 1a=False 1b=False 2=False (2.8s)
Sep 11 00:40:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:00,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:40:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:00,521 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:40:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:00,648 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 00:40:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:07,582 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:00:40:07 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 00:40:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:07,925 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:00:40:07 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 00:40:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:12,231 main INFO screen Bot pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 00:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:17,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:17,526 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:17,652 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 00:40:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:38,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:40:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:38,818 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:40:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:40:39,002 main INFO screen VISA pass=0 dev=0.0 ins=20.97 pro=27 1a=False 1b=False 2=True (0.4s)
Sep 11 00:41:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:19,742 main INFO screen VISA pass=0 dev=0.0 ins=22.39 pro=44 1a=False 1b=False 2=False (3.9s)
Sep 11 00:41:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:19,788 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.8s)
Sep 11 00:41:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:21,980 main INFO screen cat pass=0 dev=0.0 ins=20.57 pro=62 1a=False 1b=False 2=True (5.2s)
Sep 11 00:41:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:36,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:41:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:36,132 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:41:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:41:36,527 main INFO screen 10/14 pass=1 dev=0.0 ins=14.3 pro=20 1a=False 1b=False 2=False (0.5s)
Sep 11 00:42:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:19,293 main INFO screen tsunami pass=0 dev=0.16 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 00:42:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:37,068 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:42:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:42:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:39,369 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:42:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:39,507 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:42:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:39,804 main INFO screen 9/10 pass=0 dev=0.0 ins=0.77 pro=25 1a=False 1b=False 2=True (0.5s)
Sep 11 00:42:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:47,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:42:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:47,710 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:42:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:42:47,846 main INFO screen PENGU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 00:43:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:01,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:43:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:01,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:43:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:02,082 main INFO screen r3tards pass=0 dev=0.0 ins=26.54 pro=17 1a=False 1b=False 2=True (0.3s)
Sep 11 00:43:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:11,450 main INFO screen FROBERT pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 11 00:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:12,890 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:43:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:13,016 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:43:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:15,120 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.44 pro=2 1a=False 1b=False 2=True (2.3s)
Sep 11 00:43:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:33,056 main INFO screen $PTA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 00:43:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:43:45,274 main INFO screen FROST pass=0 dev=0.59 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 00:44:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:26,926 main INFO screen PMP pass=0 dev=1.19 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 00:44:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:29,187 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:44:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:29,306 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:44:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:29,484 main INFO screen GOTGATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 00:44:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:32,327 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:44:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:32,447 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:44:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:44:32,572 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 00:45:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:45:21,864 main INFO screen Investoor pass=1 dev=0.0 ins=12.35 pro=57 1a=False 1b=False 2=False (1.8s)
Sep 11 00:45:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:45:30,545 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:45:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:45:30,630 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:45:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:45:30,798 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 00:46:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:46:17,871 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:46:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:46:17,973 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:46:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:46:18,151 main INFO screen Investoor pass=0 dev=0.0 ins=20.54 pro=19 1a=False 1b=False 2=True (0.4s)
Sep 11 00:47:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:47:21,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:47:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:47:21,761 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:47:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:47:21,939 main INFO screen Investoor pass=0 dev=0.0 ins=22.13 pro=14 1a=False 1b=False 2=True (0.4s)
Sep 11 00:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:03,193 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:03,287 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:03,466 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.9 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 11 00:48:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:09,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:48:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:09,703 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:48:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:09,860 main INFO screen Investoor pass=0 dev=0.0 ins=21.14 pro=20 1a=False 1b=False 2=True (0.3s)
Sep 11 00:48:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:48:57,241 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:48:57 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 00:49:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:49:10,125 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:49:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:49:10,222 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:49:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:49:10,448 main INFO screen METH pass=0 dev=0.0 ins=18.74 pro=19 1a=False 1b=False 2=True (0.4s)
Sep 11 00:50:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:50:04,686 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:50:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:50:04,785 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:50:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:50:05,149 main INFO screen Save pass=0 dev=0.0 ins=13.46 pro=38 1a=False 1b=False 2=True (0.6s)
Sep 11 00:50:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:50:50,610 main INFO screen beer pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (1.5s)
Sep 11 00:51:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:23,315 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (4.0s)
Sep 11 00:51:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:38,576 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:51:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:38,672 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:51:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:39,152 main INFO screen TNT pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.7s)
Sep 11 00:51:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:55,719 main INFO screen BACKWARDS pass=0 dev=36.46 ins=0.04 pro=12 1a=False 1b=False 2=False (3.6s)
Sep 11 00:51:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:56,284 main INFO screen USELESS pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (4.2s)
Sep 11 00:51:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:56,416 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:51:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:56,793 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:51:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:57,159 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=4 1a=False 1b=False 2=True (1.1s)
Sep 11 00:51:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:51:59,426 main INFO screen $ONEMORE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 00:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:12,549 main INFO screen MONK pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 11 00:53:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:23,416 main INFO screen Insider pass=0 dev=0.0 ins=16.74 pro=50 1a=False 1b=False 2=True (3.2s)
Sep 11 00:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:26,044 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:53:26 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
