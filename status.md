# Schaduwbot status

- tijd: 2026-09-11 00:58:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 11 hours, 11 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 648/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 40210, "tokens_in_memory": 1416, "msgs": 7956815, "trades": 1517944, "creates": 16372, "decode_fail": 108371, "rpc_calls": 24854, "rpc_errors": 2405, "sol_usd": 99.1497750365132, "open_positions": 73}
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
Sep 11 00:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:26,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:26,398 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:53:26,688 main INFO screen TWIZZ pass=0 dev=0.0 ins=31.58 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 00:54:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:13,262 main INFO screen vrl pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 00:54:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:13,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:54:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:13,450 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:54:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:13,564 main INFO screen BULLCATE pass=0 dev=0.0 ins=31.3 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 00:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:32,771 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:32,905 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:54:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:54:33,190 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 00:55:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:26,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:55:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:26,374 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:55:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:26,563 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 00:55:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:33,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:55:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:33,205 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:55:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:33,321 main INFO screen paperclip pass=0 dev=0.0 ins=43.94 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 11 00:55:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:51,020 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:55:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:51,074 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:55:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:51,292 main INFO screen TROLL pass=0 dev=0.0 ins=42.83 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 11 00:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:53,840 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:53,926 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:55:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:55:54,171 main INFO screen BULLCATE pass=0 dev=0.0 ins=32.01 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 00:56:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:20,807 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:56:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:20,910 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:56:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:21,094 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 00:56:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:36,713 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:56:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:37,462 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:56:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:38,019 main INFO screen 曙宝 pass=0 dev=0.0 ins=19.93 pro=36 1a=False 1b=False 2=True (1.9s)
Sep 11 00:56:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:38,951 main INFO screen WIF pass=0 dev=0.0 ins=13.71 pro=51 1a=False 1b=False 2=True (4.1s)
Sep 11 00:56:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:45,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:56:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:45,621 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:56:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:45,857 main INFO screen 슈바오 pass=0 dev=0.0 ins=8.27 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 00:56:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:56:59,921 main INFO screen ANSEM pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 11 00:57:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:57:28,461 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:57:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:57:28,555 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:57:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:57:28,833 main INFO screen 슈바오 pass=0 dev=0.0 ins=8.27 pro=9 1a=False 1b=False 2=False (0.5s)
Sep 11 00:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:12,602 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:12,687 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:12,869 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 00:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:14,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:14,251 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:14,605 main INFO screen 曙宝 pass=0 dev=0.0 ins=12.14 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 11 00:58:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:58:27,192 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:58:27 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
