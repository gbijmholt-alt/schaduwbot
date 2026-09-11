# Schaduwbot status

- tijd: 2026-09-11 12:10:31 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 22 hours, 23 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 620/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 8447, "tokens_in_memory": 2082, "msgs": 644575, "trades": 167319, "creates": 2082, "decode_fail": 7596, "rpc_calls": 2594, "rpc_errors": 301, "sol_usd": 99.23262458816714, "open_positions": 72, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 11:49 UTC

Gelogde schaduwtrades: **22005**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 12621 | 1705 | 23 | 1705 | 109 | 3291 | 9650 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 250 | 15% | 1.6% | +41.0% | -16.2% | -7.54% | 98% |
| dip35_V1_gescreend_fail | 2212 | 26% | 3.8% | +46.2% | -26.0% | -6.99% | 100% |
| dip35_V1_alle | 2542 | 26% | 3.9% | +45.0% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 249 | 18% | 2.0% | +39.4% | -21.1% | -10.15% | 100% |
| dip35_V2_gescreend_fail | 2217 | 24% | 4.5% | +56.6% | -28.4% | -7.67% | 100% |
| dip35_V2_alle | 2524 | 24% | 4.6% | +54.6% | -28.0% | -8.37% | 100% |
| dip35_V3_gescreend_pass | 251 | 7% | 2.4% | +137.5% | -22.9% | -12.01% | 100% |
| dip35_V3_gescreend_fail | 2255 | 13% | 6.3% | +117.5% | -30.1% | -10.72% | 100% |
| dip35_V3_alle | 2559 | 13% | 6.2% | +115.1% | -29.6% | -11.31% | 100% |
| dip40_V1_gescreend_pass | 232 | 14% | 1.7% | +43.1% | -15.7% | -7.57% | 98% |
| dip40_V1_gescreend_fail | 2153 | 26% | 3.7% | +48.1% | -26.0% | -6.52% | 100% |
| dip40_V1_alle | 2445 | 25% | 3.8% | +47.1% | -25.2% | -6.91% | 100% |
| dip40_V2_gescreend_pass | 231 | 14% | 2.2% | +49.8% | -20.1% | -10.41% | 100% |
| dip40_V2_gescreend_fail | 2149 | 25% | 4.1% | +56.0% | -28.3% | -7.41% | 100% |
| dip40_V2_alle | 2423 | 24% | 4.3% | +55.2% | -27.7% | -8.14% | 100% |
| dip40_V3_gescreend_pass | 233 | 6% | 2.6% | +114.0% | -21.9% | -13.69% | 100% |
| dip40_V3_gescreend_fail | 2189 | 13% | 5.8% | +105.0% | -29.8% | -12.25% | 100% |
| dip40_V3_alle | 2461 | 12% | 5.8% | +103.6% | -29.3% | -12.82% | 100% |
| dip45_V1_gescreend_pass | 221 | 14% | 1.8% | +50.1% | -15.6% | -6.09% | 97% |
| dip45_V1_gescreend_fail | 2093 | 27% | 3.3% | +49.6% | -25.6% | -4.99% | 100% |
| dip45_V1_alle | 2358 | 26% | 3.4% | +49.3% | -24.8% | -5.37% | 100% |
| dip45_V2_gescreend_pass | 218 | 19% | 2.3% | +49.7% | -19.7% | -6.64% | 98% |
| dip45_V2_gescreend_fail | 2078 | 25% | 3.8% | +59.1% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2330 | 25% | 3.9% | +58.0% | -27.2% | -6.24% | 100% |
| dip45_V3_gescreend_pass | 221 | 7% | 2.7% | +186.5% | -21.0% | -6.88% | 99% |
| dip45_V3_gescreend_fail | 2112 | 14% | 5.6% | +111.6% | -29.3% | -9.73% | 100% |
| dip45_V3_alle | 2363 | 13% | 5.6% | +113.5% | -28.8% | -9.85% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1710 | 12% | 2.6% | -9.94% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,333 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,460 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,602 main INFO screen WATER pass=0 dev=0.0 ins=25.62 pro=21 1a=False 1b=False 2=True (0.3s)
Sep 11 11:54:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:34,133 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:54:34 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:54:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:35,800 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:35,926 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:54:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:36,144 main INFO screen Launchcat pass=0 dev=0.0 ins=30.95 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 11:54:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:59,136 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:59,241 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:55:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:01,475 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 11:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:29,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:55:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:30,013 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:55:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:30,234 main INFO screen JPPEPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:56:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:44,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:56:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:44,875 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:56:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:45,082 main INFO screen PRAWN pass=0 dev=0.0 ins=51.51 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 11:57:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:36,807 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:57:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:36,904 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:37,094 main INFO screen TRANS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 11:58:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:07,411 main INFO screen BUSTER pass=0 dev=0.35 ins=37.77 pro=16 1a=False 1b=False 2=True (3.9s)
Sep 11 11:58:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:31,367 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 11:58:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:35,054 main INFO screen RISE pass=0 dev=42.48 ins=0.0 pro=6 1a=False 1b=False 2=True (3.5s)
Sep 11 11:58:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:50,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:58:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:50,991 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:58:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:51,189 main INFO screen PHAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,079 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,176 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,360 main INFO screen Wolf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:59:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:37,161 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:59:37 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:59:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:46,959 aiohttp.access INFO 64.62.156.202 [11/Sep/2026:11:59:46 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.48 Safari/537.36"
Sep 11 12:00:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:00:51,600 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:00:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:00:51,705 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:00:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:00:57,970 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 12:01:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:12,746 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:01:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:12,844 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:01:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:13,245 main INFO screen pempfun pass=0 dev=0.0 ins=18.9 pro=14 1a=False 1b=False 2=True (0.6s)
Sep 11 12:01:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:18,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:01:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:18,601 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:01:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:23,459 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 11 12:01:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:26,994 aiohttp.access INFO 64.62.156.211 [11/Sep/2026:12:01:26 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0"
Sep 11 12:01:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:01:52,208 main INFO screen Investoor pass=0 dev=0.0 ins=18.95 pro=22 1a=False 1b=False 2=True (7.7s)
Sep 11 12:02:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:03,056 main INFO screen MIZO pass=0 dev=26.58 ins=0.0 pro=19 1a=False 1b=False 2=True (6.7s)
Sep 11 12:02:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:07,478 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 12:02:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:08,597 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 12:02:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:31,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:02:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:31,321 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:02:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:35,202 main INFO screen ROBINJAK pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (4.1s)
Sep 11 12:02:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:44,360 main INFO screen TEST pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 12:02:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:02:55,652 aiohttp.access INFO 64.62.156.205 [11/Sep/2026:12:02:55 +0000] "GET /?format=json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
Sep 11 12:03:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:17,210 aiohttp.access INFO 64.62.156.211 [11/Sep/2026:12:03:17 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
Sep 11 12:03:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:29,904 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:03:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:30,038 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:03:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:36,590 main INFO screen CPZ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 11 12:03:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:45,571 aiohttp.access INFO 64.62.156.202 [11/Sep/2026:12:03:45 +0000] "GET /geoserver/web/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
Sep 11 12:03:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:03:46,548 main INFO screen up pass=0 dev=0.4 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 11 12:04:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:01,070 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 12:04:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:06,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:04:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:06,289 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:04:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:10,867 main INFO screen HOMO pass=0 dev=0.0 ins=49.44 pro=6 1a=False 1b=False 2=True (4.8s)
Sep 11 12:04:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:19,570 main INFO screen WORKYMONK pass=1 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (7.4s)
Sep 11 12:04:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:26,417 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:04:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:26,545 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:04:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:04:31,006 main INFO screen MCX pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 11 12:05:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:05:16,613 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:05:16 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 12:06:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:06:04,745 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:06:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:06:04,846 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:06:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:06:11,984 main INFO screen Jotchua pass=0 dev=0.0 ins=49.13 pro=6 1a=False 1b=False 2=True (7.3s)
Sep 11 12:06:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:06:41,872 main INFO screen SCRVAN pass=0 dev=0.6 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 11 12:07:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:07:03,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:07:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:07:03,983 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:07:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:07:10,276 main INFO screen GETSTONKED pass=0 dev=0.0 ins=35.32 pro=22 1a=False 1b=False 2=True (6.5s)
Sep 11 12:07:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:07:23,526 main INFO screen IPO pass=1 dev=0.0 ins=10.07 pro=56 1a=False 1b=False 2=False (9.8s)
Sep 11 12:07:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:07:59,227 main INFO screen HALH pass=0 dev=3.94 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 12:09:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:04,632 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:09:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:04,719 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:09:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:10,505 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 12:09:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:30,567 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (10.1s)
Sep 11 12:09:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:43,566 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:12:09:43 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 12:09:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:09:43,915 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:12:09:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 12:10:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:10:31,540 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:10:31 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T10:41:47Z
--- update 2026-09-11T10:47:06Z
--- update 2026-09-11T10:52:18Z
--- update 2026-09-11T10:57:35Z
--- update 2026-09-11T11:02:35Z
--- update 2026-09-11T11:08:05Z
--- update 2026-09-11T11:13:36Z
--- update 2026-09-11T11:18:37Z
--- update 2026-09-11T11:23:37Z
--- update 2026-09-11T11:28:37Z
--- update 2026-09-11T11:33:37Z
--- update 2026-09-11T11:38:38Z
--- update 2026-09-11T11:43:38Z
--- update 2026-09-11T11:49:07Z
--- update 2026-09-11T11:54:33Z
--- update 2026-09-11T11:59:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 91d89b5fe55047b9bdf833a434bfc1f0
analyses gestart (8213ec5e675e)
--- update 2026-09-11T12:05:15Z
--- update 2026-09-11T12:10:30Z
```

## Analyses (laatste 25 regels)
```
inactive
09:54:59 25844 tokens geladen
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
11:59:36 2892 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
11:59:39   ingelezen tot rowid 1255924 (151022 rijen, 151022 bruikbaar)
11:59:39 ingelezen: 151022 nieuwe trades, 151022 bruikbaar (2s)
11:59:40 klaar in 4s -> /opt/schaduwbot/reports/ledger.md
11:59:40 klaar in 0s: 59 tokens, 67 nieuw -> /opt/schaduwbot/reports/video_replay.md
11:59:40 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 11:59 UTC
11:59:40 27728 tokens geladen
11:59:44   2000 tokens, 398779 trades, 119472 posities (4s)
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
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
