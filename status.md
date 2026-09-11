# Schaduwbot status

- tijd: 2026-09-11 03:40:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 13 hours, 53 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 637/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 49940, "tokens_in_memory": 994, "msgs": 9154097, "trades": 1757657, "creates": 19365, "decode_fail": 119477, "rpc_calls": 29102, "rpc_errors": 2777, "sol_usd": 99.3757754791383, "open_positions": 18}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 02:48 UTC

Gelogde schaduwtrades: **14754**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 3510 | 408 | 0 | 409 | 43 | 792 | 2399 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 190 | 15% | 1.6% | +37.8% | -16.8% | -8.51% | 97% |
| dip35_V1_gescreend_fail | 1467 | 26% | 4.0% | +44.5% | -25.4% | -7.54% | 100% |
| dip35_V1_alle | 1710 | 25% | 4.1% | +43.2% | -24.8% | -7.98% | 100% |
| dip35_V2_gescreend_pass | 191 | 17% | 2.1% | +29.7% | -21.5% | -12.69% | 100% |
| dip35_V2_gescreend_fail | 1476 | 24% | 4.7% | +56.5% | -28.0% | -7.68% | 100% |
| dip35_V2_alle | 1704 | 23% | 4.8% | +53.5% | -27.6% | -8.73% | 100% |
| dip35_V3_gescreend_pass | 190 | 6% | 2.6% | +138.2% | -23.4% | -13.19% | 100% |
| dip35_V3_gescreend_fail | 1483 | 12% | 6.2% | +118.9% | -29.7% | -11.67% | 100% |
| dip35_V3_alle | 1708 | 12% | 6.1% | +116.4% | -29.2% | -12.27% | 100% |
| dip40_V1_gescreend_pass | 178 | 13% | 2.2% | +41.2% | -16.4% | -8.95% | 97% |
| dip40_V1_gescreend_fail | 1424 | 25% | 4.1% | +47.2% | -25.4% | -7.22% | 100% |
| dip40_V1_alle | 1641 | 24% | 4.1% | +46.0% | -24.6% | -7.60% | 100% |
| dip40_V2_gescreend_pass | 179 | 13% | 2.2% | +44.7% | -20.4% | -12.05% | 99% |
| dip40_V2_gescreend_fail | 1433 | 24% | 4.5% | +57.8% | -27.7% | -6.92% | 100% |
| dip40_V2_alle | 1637 | 23% | 4.5% | +56.5% | -27.1% | -7.88% | 100% |
| dip40_V3_gescreend_pass | 179 | 6% | 2.8% | +118.0% | -22.1% | -13.53% | 100% |
| dip40_V3_gescreend_fail | 1440 | 12% | 5.9% | +106.8% | -29.4% | -13.13% | 100% |
| dip40_V3_alle | 1642 | 11% | 5.8% | +105.3% | -28.8% | -13.51% | 100% |
| dip45_V1_gescreend_pass | 166 | 14% | 2.4% | +47.6% | -15.6% | -6.51% | 94% |
| dip45_V1_gescreend_fail | 1378 | 27% | 3.5% | +49.2% | -24.8% | -4.76% | 100% |
| dip45_V1_alle | 1572 | 26% | 3.6% | +48.7% | -24.0% | -5.17% | 100% |
| dip45_V2_gescreend_pass | 165 | 19% | 3.0% | +39.5% | -19.5% | -8.39% | 96% |
| dip45_V2_gescreend_fail | 1383 | 25% | 3.9% | +62.8% | -27.0% | -4.18% | 100% |
| dip45_V2_alle | 1567 | 25% | 4.0% | +60.4% | -26.4% | -4.99% | 100% |
| dip45_V3_gescreend_pass | 166 | 7% | 3.6% | +173.8% | -21.1% | -6.98% | 98% |
| dip45_V3_gescreend_fail | 1390 | 13% | 5.5% | +119.2% | -28.8% | -9.41% | 100% |
| dip45_V3_alle | 1573 | 12% | 5.5% | +120.8% | -28.1% | -9.48% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 11 03:26:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:13,809 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:26:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:20,012 main INFO screen SPX59X pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 11 03:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:47,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:47,723 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:26:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:26:51,950 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.4s)
Sep 11 03:27:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:37,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:27:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:37,931 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:41,599 main INFO screen JUGTROLL pass=0 dev=0.0 ins=79.24 pro=6 1a=False 1b=False 2=True (3.9s)
Sep 11 03:27:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:42,940 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:27:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:43,074 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:27:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:27:49,898 main INFO screen dollar pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=True (7.0s)
Sep 11 03:28:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:02,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:28:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:02,697 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:28:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:03,009 main INFO screen + pass=1 dev=0.0 ins=12.8 pro=12 1a=False 1b=False 2=False (0.5s)
Sep 11 03:28:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:37,281 main INFO screen Coinfly pass=0 dev=1.61 ins=0.0 pro=4 1a=False 1b=False 2=False (8.2s)
Sep 11 03:28:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:28:38,043 main INFO screen vrl pass=0 dev=1.28 ins=0.0 pro=2 1a=False 1b=False 2=False (6.4s)
Sep 11 03:29:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:01,425 main INFO screen MEMECOIN pass=0 dev=0.0 ins=9.51 pro=66 1a=False 1b=False 2=True (3.2s)
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,564 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:29:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:08,933 main INFO screen CREIOPCS pass=0 dev=0.0 ins=0.26 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 11 03:29:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:25,628 main INFO screen BROKE pass=0 dev=0.11 ins=0.0 pro=4 1a=False 1b=False 2=False (7.5s)
Sep 11 03:29:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:37,096 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:29:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 03:29:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:29:47,663 main INFO screen POP pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (9.3s)
Sep 11 03:31:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:31:27,891 main INFO screen TRIGGER pass=0 dev=0.2 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 03:31:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:31:52,275 main INFO screen lowkey pass=1 dev=3.43 ins=0.7 pro=50 1a=False 1b=False 2=False (3.8s)
Sep 11 03:31:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:31:56,114 main INFO screen STONK pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 03:32:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:04,232 main INFO screen PEPBoY pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 11 03:32:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:09,047 main INFO screen BROKE pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 03:32:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:23,695 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:32:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:23,811 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:32:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:23,958 main INFO screen PEG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 03:32:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:32:36,747 main INFO screen Squirt pass=1 dev=0.0 ins=9.35 pro=55 1a=False 1b=False 2=False (1.8s)
Sep 11 03:33:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:33:06,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:33:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:33:06,816 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:33:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:33:07,159 main INFO screen DESKFLY pass=1 dev=0.0 ins=15.6 pro=20 1a=False 1b=False 2=False (0.5s)
Sep 11 03:33:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:33:36,882 main INFO screen MakeHisD pass=0 dev=1.18 ins=0.0 pro=7 1a=False 1b=False 2=False (3.1s)
Sep 11 03:33:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:33:52,151 main INFO screen EIP-8288 pass=0 dev=9.75 ins=7.36 pro=56 1a=False 1b=False 2=True (3.4s)
Sep 11 03:34:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:34:33,898 main INFO screen Faucet pass=0 dev=0.0 ins=5.65 pro=76 1a=False 1b=False 2=True (3.5s)
Sep 11 03:35:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:35:05,727 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:35:05 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 03:35:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:35:24,130 main INFO screen LONGDONG pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 03:35:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:35:54,430 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 11 03:36:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:36:11,847 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:36:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:36:11,905 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:36:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:36:12,149 main INFO screen Bn pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 03:36:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:36:21,245 main INFO screen Kling pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 11 03:36:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:36:29,880 main INFO screen CATFISH pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 03:37:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:05,567 main INFO screen GOOD pass=0 dev=0.0 ins=0.0 pro=60 1a=False 1b=False 2=True (5.6s)
Sep 11 03:37:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:07,135 main INFO screen TITS pass=0 dev=0.56 ins=0.0 pro=4 1a=False 1b=False 2=False (6.2s)
Sep 11 03:37:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:07,404 main INFO screen BROKE pass=0 dev=0.07 ins=0.0 pro=4 1a=False 1b=False 2=False (5.7s)
Sep 11 03:37:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:28,381 main INFO screen $GOAT pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 11 03:37:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:41,918 main INFO screen flykiller pass=1 dev=1.74 ins=3.62 pro=45 1a=False 1b=False 2=False (3.7s)
Sep 11 03:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:45,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:45,997 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:37:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:46,115 main INFO screen TITS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 03:37:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:50,194 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:37:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:50,321 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:37:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:50,439 main INFO screen MEo pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (0.3s)
Sep 11 03:37:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:54,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:37:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:54,787 main INFO screen SOLS pass=0 dev=0.63 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 03:37:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:55,137 aiohttp.access INFO 147.185.132.94 [11/Sep/2026:03:37:55 +0000] "GET / HTTP/1.1" 404 174 "-" "Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity"
Sep 11 03:37:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:37:57,018 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:03:37:57 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 03:38:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:03,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:04,016 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:04,132 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 03:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:53,614 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:53,642 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:38:53,867 main INFO screen ~ʚ4° pass=0 dev=0.0 ins=22.35 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 03:39:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:21,031 main INFO screen PHAPIL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 03:39:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:27,706 aiohttp.access INFO 184.105.139.67 [11/Sep/2026:03:39:27 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 03:39:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:28,954 main INFO screen RUG pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 03:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:33,272 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:33,434 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:33,559 main INFO screen TITS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 03:39:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:38,568 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:03:39:38 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 03:39:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:38,929 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:03:39:38 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 03:39:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:56,910 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 03:39:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:59,457 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 11 03:40:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:09,286 main INFO screen PHAPIL pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 03:40:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:30,010 main INFO screen $MEOW pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 03:40:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:37,066 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:40:37 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
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
