# Schaduwbot status

- tijd: 2026-09-11 04:37:26 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 14 hours, 50 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 659/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 53350, "tokens_in_memory": 986, "msgs": 9692466, "trades": 1842537, "creates": 20295, "decode_fail": 122817, "rpc_calls": 30699, "rpc_errors": 2900, "sol_usd": 99.79271781908807, "open_positions": 19}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 03:48 UTC

Gelogde schaduwtrades: **15837**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 4522 | 566 | 4 | 567 | 59 | 1152 | 3482 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 205 | 16% | 1.5% | +40.0% | -16.5% | -7.66% | 98% |
| dip35_V1_gescreend_fail | 1574 | 26% | 4.1% | +45.9% | -25.6% | -7.42% | 100% |
| dip35_V1_alle | 1836 | 25% | 4.1% | +44.6% | -25.0% | -7.85% | 100% |
| dip35_V2_gescreend_pass | 206 | 18% | 1.9% | +33.5% | -21.3% | -11.48% | 100% |
| dip35_V2_gescreend_fail | 1585 | 24% | 4.7% | +56.3% | -28.2% | -8.04% | 100% |
| dip35_V2_alle | 1832 | 23% | 4.7% | +53.6% | -27.7% | -8.95% | 100% |
| dip35_V3_gescreend_pass | 206 | 7% | 2.4% | +123.9% | -23.1% | -13.14% | 100% |
| dip35_V3_gescreend_fail | 1589 | 12% | 6.2% | +120.3% | -29.8% | -11.68% | 100% |
| dip35_V3_alle | 1834 | 12% | 6.0% | +117.1% | -29.3% | -12.32% | 100% |
| dip40_V1_gescreend_pass | 191 | 14% | 2.1% | +43.6% | -16.1% | -8.01% | 98% |
| dip40_V1_gescreend_fail | 1527 | 25% | 4.1% | +48.4% | -25.6% | -6.98% | 100% |
| dip40_V1_alle | 1761 | 24% | 4.1% | +47.3% | -24.8% | -7.36% | 100% |
| dip40_V2_gescreend_pass | 192 | 14% | 2.1% | +47.6% | -20.2% | -10.68% | 99% |
| dip40_V2_gescreend_fail | 1535 | 24% | 4.4% | +57.4% | -27.8% | -7.24% | 100% |
| dip40_V2_alle | 1756 | 23% | 4.4% | +56.2% | -27.2% | -8.07% | 100% |
| dip40_V3_gescreend_pass | 192 | 6% | 2.6% | +108.4% | -21.9% | -13.78% | 100% |
| dip40_V3_gescreend_fail | 1540 | 12% | 5.8% | +108.5% | -29.5% | -12.92% | 100% |
| dip40_V3_alle | 1759 | 11% | 5.7% | +106.5% | -28.9% | -13.41% | 100% |
| dip45_V1_gescreend_pass | 180 | 15% | 2.2% | +49.8% | -15.8% | -6.00% | 95% |
| dip45_V1_gescreend_fail | 1479 | 27% | 3.5% | +50.3% | -25.0% | -4.60% | 100% |
| dip45_V1_alle | 1689 | 26% | 3.6% | +50.0% | -24.2% | -5.01% | 100% |
| dip45_V2_gescreend_pass | 180 | 19% | 2.8% | +51.7% | -19.8% | -5.86% | 97% |
| dip45_V2_gescreend_fail | 1483 | 25% | 3.9% | +62.3% | -27.1% | -4.74% | 100% |
| dip45_V2_alle | 1684 | 24% | 4.0% | +60.9% | -26.5% | -5.24% | 100% |
| dip45_V3_gescreend_pass | 180 | 7% | 3.3% | +197.6% | -21.2% | -5.43% | 98% |
| dip45_V3_gescreend_fail | 1487 | 13% | 5.5% | +119.3% | -28.9% | -9.55% | 100% |
| dip45_V3_alle | 1686 | 12% | 5.5% | +122.5% | -28.2% | -9.45% | 100% |

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
Sep 11 04:17:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:17:07,563 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:17:07 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 04:17:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:17:45,762 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:17:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:17:45,855 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:17:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:17:46,238 main INFO screen meemee pass=0 dev=0.0 ins=17.07 pro=17 1a=False 1b=False 2=True (0.5s)
Sep 11 04:17:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:17:49,567 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 11 04:18:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:18:49,923 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:18:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:18:50,060 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:18:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:18:55,772 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 04:19:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:03,207 main INFO screen OMW pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 11 04:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:06,540 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:06,666 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:06,986 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:19:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:07,156 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:19:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:10,632 main INFO screen Apple pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 11 04:19:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:13,655 main INFO screen USTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 11 04:19:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:45,781 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:19:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:45,895 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:19:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:48,345 main INFO screen BYD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.0s)
Sep 11 04:19:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:19:51,965 main INFO screen HIMS pass=0 dev=0.0 ins=13.0 pro=26 1a=False 1b=False 2=True (6.3s)
Sep 11 04:20:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:20:08,278 main INFO screen Faucet pass=1 dev=0.11 ins=1.33 pro=46 1a=False 1b=False 2=False (8.9s)
Sep 11 04:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:20:19,594 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:20:19,644 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:20:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:20:24,274 main INFO screen SMAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.8s)
Sep 11 04:20:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:20:49,796 main INFO screen FLYGUY pass=1 dev=3.24 ins=0.0 pro=38 1a=False 1b=False 2=False (8.3s)
Sep 11 04:21:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:21:08,839 aiohttp.access INFO 94.154.43.223 [11/Sep/2026:04:21:08 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 04:21:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:21:57,057 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:21:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:21:57,147 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:22:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:22:03,231 main INFO screen STRATEGY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 04:22:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:22:09,040 main INFO screen CryptoFaucet pass=0 dev=0.0 ins=22.07 pro=33 1a=False 1b=False 2=False (5.1s)
Sep 11 04:22:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:22:17,250 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:22:17 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 04:25:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:25:16,269 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:25:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:25:16,368 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:25:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:25:22,349 main INFO screen S😀😁 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.2s)
Sep 11 04:26:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:26:31,140 aiohttp.access INFO 47.84.108.199 [11/Sep/2026:04:26:31 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 04:26:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:26:31,490 aiohttp.access INFO 47.84.108.199 [11/Sep/2026:04:26:31 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 11 04:26:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:26:31,774 main INFO screen TripleTowers pass=0 dev=0.0 ins=27.92 pro=52 1a=False 1b=True 2=True (2.4s)
Sep 11 04:26:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:26:32,099 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:04:26:32 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 04:26:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:26:32,444 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:04:26:32 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 04:27:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:27:20,878 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:27:20 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 04:28:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:31,855 main INFO screen LMAO pass=0 dev=0.39 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 04:28:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:37,551 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:28:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:37,675 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:28:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:41,783 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 11 04:28:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:50,652 main INFO screen download pass=1 dev=3.76 ins=0.69 pro=39 1a=False 1b=False 2=False (9.8s)
Sep 11 04:28:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:28:51,233 main INFO screen att pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (10.3s)
Sep 11 04:29:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:29:01,029 main INFO screen power pass=0 dev=0.29 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 11 04:30:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:30:12,143 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:30:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:30:16,419 main INFO screen SOLdiers pass=0 dev=6.63 ins=21.92 pro=32 1a=False 1b=False 2=False (4.4s)
Sep 11 04:30:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:30:44,154 main INFO screen power pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 04:31:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:31:43,689 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:31:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:31:44,437 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:31:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:31:45,180 main INFO screen UNICORN pass=0 dev=0.0 ins=14.97 pro=5 1a=False 1b=False 2=True (1.8s)
Sep 11 04:31:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:31:47,045 main INFO screen fish pass=0 dev=0.0 ins=25.27 pro=21 1a=False 1b=False 2=True (3.8s)
Sep 11 04:32:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:32:24,520 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:32:24 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 04:32:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:32:37,064 main INFO screen DERP pass=0 dev=1.04 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 04:33:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:18,436 aiohttp.access INFO 172.105.199.92 [11/Sep/2026:04:33:18 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 11 04:33:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:18,947 aiohttp.access INFO 172.105.199.92 [11/Sep/2026:04:33:18 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 11 04:33:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:45,614 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:33:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:45,711 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:33:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:45,899 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 04:33:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:48,225 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:33:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:48,353 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:33:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:33:48,468 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 04:34:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:34:12,929 main INFO screen CUMFaucet pass=1 dev=0.03 ins=13.16 pro=47 1a=False 1b=False 2=False (2.8s)
Sep 11 04:34:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:34:16,138 main INFO screen MotionCat pass=0 dev=0.46 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 11 04:34:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:34:36,330 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 04:35:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:10,918 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:35:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:11,011 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:35:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:11,201 main INFO screen MotionCat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:17,808 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:17,938 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:35:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:35:18,053 main INFO screen ISRAEL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 04:36:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:36:25,258 main INFO screen att pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 04:36:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:36:45,642 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:36:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:36:45,744 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:36:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:36:45,945 main INFO screen ISRAEL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 04:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:17,698 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:17,794 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:17,987 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:37:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:26,967 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:37:26 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
