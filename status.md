# Schaduwbot status

- tijd: 2026-09-11 14:18:47 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 31 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 696/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 16142, "tokens_in_memory": 4472, "msgs": 1466621, "trades": 379524, "creates": 4472, "decode_fail": 31114, "rpc_calls": 6738, "rpc_errors": 634, "sol_usd": 103.8546979924385, "open_positions": 92, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 13:49 UTC

Gelogde schaduwtrades: **23540**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 14630 | 2033 | 23 | 2033 | 139 | 3820 | 11185 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 265 | 15% | 1.5% | +41.0% | -16.1% | -7.69% | 99% |
| dip35_V1_gescreend_fail | 2373 | 26% | 3.8% | +45.7% | -26.0% | -6.98% | 100% |
| dip35_V1_alle | 2723 | 26% | 3.9% | +44.7% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 264 | 17% | 1.9% | +39.3% | -20.9% | -10.39% | 100% |
| dip35_V2_gescreend_fail | 2373 | 25% | 4.4% | +56.1% | -28.5% | -7.59% | 100% |
| dip35_V2_alle | 2699 | 24% | 4.5% | +54.3% | -28.0% | -8.32% | 100% |
| dip35_V3_gescreend_pass | 266 | 7% | 2.3% | +136.1% | -22.6% | -11.87% | 100% |
| dip35_V3_gescreend_fail | 2416 | 13% | 6.2% | +113.0% | -30.0% | -10.92% | 100% |
| dip35_V3_alle | 2739 | 13% | 6.1% | +111.2% | -29.6% | -11.47% | 100% |
| dip40_V1_gescreend_pass | 245 | 14% | 1.6% | +43.0% | -15.6% | -7.69% | 99% |
| dip40_V1_gescreend_fail | 2308 | 26% | 3.7% | +47.9% | -26.0% | -6.42% | 100% |
| dip40_V1_alle | 2616 | 26% | 3.8% | +47.0% | -25.2% | -6.79% | 100% |
| dip40_V2_gescreend_pass | 244 | 13% | 2.0% | +49.8% | -19.9% | -10.78% | 100% |
| dip40_V2_gescreend_fail | 2302 | 25% | 4.1% | +55.6% | -28.2% | -7.34% | 100% |
| dip40_V2_alle | 2591 | 24% | 4.2% | +54.9% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 246 | 6% | 2.4% | +114.0% | -21.6% | -13.86% | 100% |
| dip40_V3_gescreend_fail | 2344 | 13% | 5.8% | +100.3% | -29.7% | -12.63% | 100% |
| dip40_V3_alle | 2631 | 12% | 5.7% | +99.2% | -29.1% | -13.14% | 100% |
| dip45_V1_gescreend_pass | 234 | 14% | 1.7% | +49.5% | -15.5% | -6.09% | 98% |
| dip45_V1_gescreend_fail | 2242 | 28% | 3.3% | +49.2% | -25.6% | -4.83% | 100% |
| dip45_V1_alle | 2522 | 27% | 3.4% | +48.8% | -24.8% | -5.23% | 100% |
| dip45_V2_gescreend_pass | 232 | 18% | 2.2% | +49.0% | -19.6% | -7.18% | 99% |
| dip45_V2_gescreend_fail | 2225 | 26% | 3.7% | +58.4% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2493 | 25% | 3.8% | +57.4% | -27.2% | -6.27% | 100% |
| dip45_V3_gescreend_pass | 234 | 6% | 2.6% | +186.5% | -20.8% | -7.50% | 100% |
| dip45_V3_gescreend_fail | 2260 | 14% | 5.6% | +107.1% | -29.3% | -10.26% | 100% |
| dip45_V3_alle | 2526 | 13% | 5.5% | +109.2% | -28.7% | -10.37% | 100% |

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
| met_xlink | 1819 | 12% | 2.5% | -10.15% | 100% |
| zonder_xlink | 411 | 13% | 0.0% | -5.49% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 14:09:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:27,974 main INFO screen OPAI pass=1 dev=0.0 ins=12.11 pro=17 1a=False 1b=False 2=False (0.5s)
Sep 11 14:09:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:30,055 main INFO screen stocklana pass=0 dev=0.46 ins=0.0 pro=3 1a=False 1b=False 2=False (4.3s)
Sep 11 14:09:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:32,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:09:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:32,252 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:09:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:36,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:09:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:36,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:09:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:38,068 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.0s)
Sep 11 14:09:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:41,812 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:09:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:41,943 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:09:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:42,814 main INFO screen BUBBLE pass=0 dev=0.0 ins=42.73 pro=7 1a=False 1b=False 2=True (6.5s)
Sep 11 14:09:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:09:48,934 main INFO screen coin pass=0 dev=0.0 ins=18.37 pro=6 1a=False 1b=False 2=True (7.2s)
Sep 11 14:10:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:15,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:10:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:15,669 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:10:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:19,445 main INFO screen 911 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 14:10:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:32,184 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:10:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:32,317 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:10:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:34,564 main INFO screen TRANSDAD pass=0 dev=0.48 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 11 14:10:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:37,032 main INFO screen SPSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 11 14:10:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:37,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:10:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:37,922 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:10:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:41,628 main INFO screen FLYSEM pass=0 dev=0.0 ins=32.27 pro=5 1a=False 1b=False 2=True (3.9s)
Sep 11 14:10:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:49,027 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:10:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:49,158 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:10:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:51,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:10:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:51,133 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:10:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:51,282 main INFO screen Hedgie pass=0 dev=0.0 ins=30.74 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 14:10:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:10:55,545 main INFO screen bub pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 11 14:11:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:11:00,830 main INFO screen DERP pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 11 14:11:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:11:16,120 main INFO screen MELBEL pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 11 14:11:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:11:31,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:11:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:11:31,676 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:11:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:11:31,856 main INFO screen saveme pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:12:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:02,475 main INFO screen BHAI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 14:12:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:23,368 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:12:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:23,624 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:12:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:23,939 main INFO screen saveme pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (1.1s)
Sep 11 14:12:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:28,568 main INFO screen lam pass=0 dev=0.0 ins=20.16 pro=14 1a=False 1b=False 2=False (6.8s)
Sep 11 14:12:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:30,161 main INFO screen PUMPDOG pass=0 dev=0.0 ins=21.06 pro=16 1a=False 1b=False 2=False (4.9s)
Sep 11 14:12:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:56,204 main INFO screen DOOROC pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 14:12:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:12:57,275 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:12:57 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 14:13:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:03,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:13:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:07,427 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:13:07 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 11 14:13:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:10,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:13:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:10,322 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:13:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:10,555 main INFO screen fone pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 14:13:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:13,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:13:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:13,893 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:13:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:16,414 main INFO screen FLYSEM pass=0 dev=0.0 ins=32.04 pro=4 1a=False 1b=False 2=True (6.2s)
Sep 11 14:13:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:19,464 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 14:13:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:25,524 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:13:25 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 11 14:13:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:25,628 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:13:25 +0000] "GET /robots.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 11 14:13:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:25,737 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:13:25 +0000] "GET /sitemap.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 11 14:13:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:29,980 aiohttp.access INFO 156.229.16.142 [11/Sep/2026:14:13:29 +0000] "POST /update_weights_from_tensor HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
Sep 11 14:13:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:37,232 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:13:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 14:13:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:37,695 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:13:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:37,782 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:13:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:13:44,068 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 11 14:14:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:07,826 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:14:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:07,975 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:14:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:11,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:14:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:11,626 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:14:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:13,308 main INFO screen Iolani pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.6s)
Sep 11 14:14:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:17,628 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.2s)
Sep 11 14:14:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:23,075 main INFO screen mmrich pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 14:14:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:53,851 main INFO screen Bub pass=0 dev=0.0 ins=0.0 pro=39 1a=False 1b=True 2=False (8.8s)
Sep 11 14:14:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:14:55,995 main INFO screen stocklana pass=0 dev=0.79 ins=0.0 pro=1 1a=False 1b=False 2=False (10.1s)
Sep 11 14:15:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:30,125 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:15:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:30,259 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:15:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:34,222 main INFO screen Sob pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.2s)
Sep 11 14:15:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:35,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:15:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:35,426 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:15:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:15:40,205 main INFO screen POKEMON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.0s)
Sep 11 14:17:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:12,791 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:17:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:12,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:17:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:18,215 main INFO screen FLYSEM pass=0 dev=0.0 ins=32.02 pro=4 1a=False 1b=False 2=True (5.5s)
Sep 11 14:17:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:26,120 main INFO screen CASHCAT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 11 14:17:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:28,837 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 14:17:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:29,974 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 14:18:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:01,837 main INFO screen VAULT pass=0 dev=0.0 ins=24.87 pro=75 1a=False 1b=True 2=True (7.8s)
Sep 11 14:18:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:47,393 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:18:47 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T12:51:41Z
--- update 2026-09-11T12:56:44Z
--- update 2026-09-11T13:01:44Z
--- update 2026-09-11T13:06:49Z
--- update 2026-09-11T13:11:58Z
--- update 2026-09-11T13:16:59Z
--- update 2026-09-11T13:22:01Z
--- update 2026-09-11T13:27:04Z
--- update 2026-09-11T13:32:04Z
--- update 2026-09-11T13:37:17Z
--- update 2026-09-11T13:42:29Z
--- update 2026-09-11T13:47:30Z
--- update 2026-09-11T13:52:36Z
--- update 2026-09-11T13:57:48Z
--- update 2026-09-11T14:02:52Z
Running as unit: schaduwbot-wallets.service; invocation ID: c147433096084aa9b38d9e2b7eb6bf75
analyses gestart (8213ec5e675e)
--- update 2026-09-11T14:08:04Z
--- update 2026-09-11T14:13:36Z
--- update 2026-09-11T14:18:46Z
```

## Analyses (laatste 25 regels)
```
inactive
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
14:02:53 5048 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
14:02:56   ingelezen tot rowid 1452718 (196794 rijen, 196794 bruikbaar)
14:02:56 ingelezen: 196794 nieuwe trades, 196794 bruikbaar (3s)
14:02:59 klaar in 6s -> /opt/schaduwbot/reports/ledger.md
14:03:01 klaar in 2s: 1642 tokens, 1877 nieuw -> /opt/schaduwbot/reports/video_replay.md
14:03:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 14:03 UTC
14:03:01 29885 tokens geladen
14:03:05   2000 tokens, 356777 trades, 100453 posities (4s)
14:03:09   4000 tokens, 700400 trades, 193583 posities (7s)
14:03:12   6000 tokens, 1047800 trades, 291369 posities (11s)
14:03:16   8000 tokens, 1402251 trades, 394081 posities (15s)
14:03:16 posities: 409300 uit 1453102 trades (15s)
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
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
