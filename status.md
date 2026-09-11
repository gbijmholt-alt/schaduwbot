# Schaduwbot status

- tijd: 2026-09-11 00:05:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 10 hours, 18 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 640/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 37024, "tokens_in_memory": 1292, "msgs": 7509221, "trades": 1404047, "creates": 15090, "decode_fail": 103356, "rpc_calls": 23297, "rpc_errors": 2245, "sol_usd": 98.92041699068534, "open_positions": 59}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 23:48 UTC

Gelogde schaduwtrades: **12127**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14776 | 2109 | 28 | 2109 | 185 | 4062 | 12127 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 149 | 15% | 2.0% | +38.6% | -17.3% | -8.68% | 94% |
| dip35_V1_gescreend_fail | 1215 | 25% | 3.9% | +45.6% | -25.6% | -7.50% | 100% |
| dip35_V1_alle | 1406 | 24% | 4.0% | +44.5% | -25.1% | -8.11% | 100% |
| dip35_V2_gescreend_pass | 148 | 16% | 2.7% | +29.8% | -21.8% | -13.46% | 99% |
| dip35_V2_gescreend_fail | 1222 | 24% | 4.6% | +53.2% | -28.1% | -8.97% | 100% |
| dip35_V2_alle | 1402 | 22% | 4.7% | +50.9% | -27.7% | -10.03% | 100% |
| dip35_V3_gescreend_pass | 149 | 6% | 2.7% | +132.0% | -23.5% | -14.10% | 99% |
| dip35_V3_gescreend_fail | 1226 | 11% | 6.3% | +117.8% | -29.8% | -13.23% | 100% |
| dip35_V3_alle | 1405 | 11% | 6.2% | +115.7% | -29.4% | -13.84% | 100% |
| dip40_V1_gescreend_pass | 137 | 12% | 2.9% | +43.8% | -16.8% | -9.30% | 95% |
| dip40_V1_gescreend_fail | 1181 | 25% | 4.1% | +48.5% | -25.7% | -7.38% | 100% |
| dip40_V1_alle | 1351 | 24% | 4.1% | +47.6% | -25.0% | -7.87% | 100% |
| dip40_V2_gescreend_pass | 136 | 12% | 2.9% | +47.2% | -21.3% | -13.20% | 98% |
| dip40_V2_gescreend_fail | 1187 | 24% | 4.5% | +55.0% | -27.9% | -8.39% | 100% |
| dip40_V2_alle | 1346 | 22% | 4.5% | +54.0% | -27.4% | -9.30% | 100% |
| dip40_V3_gescreend_pass | 138 | 6% | 2.9% | +116.7% | -22.3% | -13.26% | 99% |
| dip40_V3_gescreend_fail | 1193 | 11% | 6.0% | +102.7% | -29.5% | -15.29% | 100% |
| dip40_V3_alle | 1352 | 10% | 5.8% | +101.6% | -29.0% | -15.43% | 100% |
| dip45_V1_gescreend_pass | 126 | 14% | 3.2% | +50.0% | -16.2% | -6.78% | 92% |
| dip45_V1_gescreend_fail | 1139 | 26% | 3.5% | +50.4% | -25.1% | -5.32% | 100% |
| dip45_V1_alle | 1290 | 25% | 3.7% | +50.1% | -24.5% | -5.81% | 100% |
| dip45_V2_gescreend_pass | 125 | 17% | 4.0% | +39.9% | -20.6% | -10.46% | 95% |
| dip45_V2_gescreend_fail | 1142 | 24% | 4.0% | +59.7% | -27.3% | -5.99% | 100% |
| dip45_V2_alle | 1285 | 24% | 4.3% | +57.9% | -26.9% | -6.84% | 100% |
| dip45_V3_gescreend_pass | 126 | 6% | 4.0% | +179.2% | -21.5% | -8.80% | 97% |
| dip45_V3_gescreend_fail | 1148 | 12% | 5.6% | +120.3% | -29.0% | -11.14% | 100% |
| dip45_V3_alle | 1290 | 11% | 5.7% | +122.0% | -28.4% | -11.30% | 100% |

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
Sep 10 23:59:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:50,315 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:59:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:50,441 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:59:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:50,554 main INFO screen CHefQueef pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 23:59:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:57,205 aiohttp.access INFO 64.34.81.199 [10/Sep/2026:23:59:57 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 10 23:59:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:57,207 aiohttp.access INFO 64.34.81.199 [10/Sep/2026:23:59:57 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 10 23:59:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:59:59,761 main INFO screen $FOMOPEPE pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (5.1s)
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,660 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /@vite/env HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,760 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /@vite/client HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,761 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /@vite/client.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,763 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /@vite/client.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,764 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /bundledDevClient.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,863 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/client HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,868 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/client.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,920 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/client.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,966 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/hmr HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,971 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/hmr.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:01,973 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:01 +0000] "GET /vite/hmr.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,068 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /@hmr HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,073 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /@hmr.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,074 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /@hmr.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,076 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /__hmrClient HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,170 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /__hmrClient.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,225 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET /__hmrClient.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,434 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:02,638 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:00:02 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:00:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:07,724 main INFO screen FROBERT pass=0 dev=0.16 ins=0.0 pro=1 1a=False 1b=False 2=False (12.2s)
Sep 11 00:00:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:08,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:00:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:08,937 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:00:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:09,556 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.8s)
Sep 11 00:00:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:20,649 main INFO screen RISE pass=0 dev=42.43 ins=0.0 pro=9 1a=False 1b=False 2=True (8.4s)
Sep 11 00:00:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:29,359 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:00:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:29,485 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:00:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:35,142 main INFO screen HULAHOP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.8s)
Sep 11 00:00:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:38,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:00:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:38,415 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:00:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:00:44,572 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 00:01:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:01:02,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:01:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:01:02,270 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:01:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:01:02,455 main INFO screen SOLCAT pass=0 dev=0.0 ins=7.78 pro=29 1a=False 1b=False 2=True (0.4s)
Sep 11 00:02:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:02:07,911 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 11 00:02:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:02:54,658 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:00:02:54 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 00:02:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:02:56,129 main INFO screen STONK DOG pass=1 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (2.6s)
Sep 11 00:03:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:34,289 main INFO screen stocktard pass=1 dev=0.0 ins=11.39 pro=27 1a=False 1b=False 2=False (8.8s)
Sep 11 00:03:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:43,109 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 00:03:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:43,111 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:43 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:45,284 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:45 +0000] "GET /?__vitesweep=34399560908a8923 HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:45,384 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:45 +0000] "GET /?__vitesweep=34399560908a8923 HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,566 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@vite/env HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,568 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@vite/client HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,669 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@vite/client.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,670 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@vite/client.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,671 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/client HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,673 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /bundledDevClient.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,772 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/client.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,797 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/client.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,800 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/hmr HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,823 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/hmr.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,896 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /vite/hmr.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,919 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@hmr HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,922 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@hmr.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:49,975 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:49 +0000] "GET /@hmr.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:50,022 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:50 +0000] "GET /__hmrClient HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:50,041 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:50 +0000] "GET /__hmrClient.js HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:50,065 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:50 +0000] "GET /__hmrClient.mjs HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:50,313 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:50 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:50,533 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:03:50 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:03:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:03:55,283 main INFO screen $CAJUN pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 11 00:04:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:01,547 main INFO screen SOLCAT pass=0 dev=0.0 ins=17.66 pro=62 1a=False 1b=False 2=True (3.5s)
Sep 11 00:04:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:10,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:04:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:10,638 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:04:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:14,202 main INFO screen $BIDEN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 11 00:04:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:35,072 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:04:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:35,211 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:04:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:35,568 main INFO screen fihdih pass=0 dev=0.0 ins=15.59 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 11 00:04:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:39,093 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 00:04:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:39,176 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 00:04:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:04:45,522 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 11 00:05:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:05:19,903 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:05:19 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 00:05:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:05:19,905 aiohttp.access INFO 64.34.81.199 [11/Sep/2026:00:05:19 +0000] "GET / HTTP/1.1" 404 174 "-" "vitesweep/1"
Sep 11 00:05:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 00:05:21,220 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:00:05:21 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
