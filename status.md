# Schaduwbot status

- tijd: 2026-09-11 20:15:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 6 hours, 28 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 585/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2115, "tokens_in_memory": 706, "msgs": 438716, "trades": 82497, "creates": 706, "decode_fail": 6206, "rpc_calls": 2515, "rpc_errors": 123, "sol_usd": 102.81310927186595, "open_positions": 36, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 19:40 UTC

Gelogde schaduwtrades: **30770**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 22609 | 3407 | 37 | 3406 | 253 | 6238 | 18415 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 342 | 17% | 2.0% | +43.7% | -16.7% | -6.62% | 99% |
| dip35_V1_gescreend_fail | 3077 | 27% | 3.8% | +46.1% | -26.2% | -6.71% | 100% |
| dip35_V1_alle | 3564 | 26% | 3.8% | +45.2% | -25.5% | -6.88% | 100% |
| dip35_V2_gescreend_pass | 339 | 20% | 2.9% | +44.5% | -21.4% | -8.38% | 100% |
| dip35_V2_gescreend_fail | 3082 | 25% | 4.4% | +57.2% | -28.4% | -7.20% | 100% |
| dip35_V2_alle | 3534 | 24% | 4.4% | +55.3% | -28.0% | -7.70% | 100% |
| dip35_V3_gescreend_pass | 341 | 8% | 3.2% | +287.1% | -22.8% | +2.64% | 100% |
| dip35_V3_gescreend_fail | 3132 | 13% | 6.1% | +120.7% | -29.9% | -9.72% | 100% |
| dip35_V3_alle | 3576 | 13% | 6.0% | +126.3% | -29.5% | -8.99% | 100% |
| dip40_V1_gescreend_pass | 315 | 15% | 1.9% | +47.2% | -15.6% | -6.41% | 99% |
| dip40_V1_gescreend_fail | 2989 | 26% | 3.7% | +48.1% | -26.1% | -6.48% | 100% |
| dip40_V1_alle | 3420 | 26% | 3.7% | +48.0% | -25.3% | -6.50% | 100% |
| dip40_V2_gescreend_pass | 313 | 15% | 2.6% | +48.3% | -19.9% | -9.46% | 100% |
| dip40_V2_gescreend_fail | 2983 | 25% | 4.2% | +56.6% | -28.3% | -7.09% | 100% |
| dip40_V2_alle | 3385 | 24% | 4.2% | +55.7% | -27.7% | -7.70% | 100% |
| dip40_V3_gescreend_pass | 316 | 6% | 2.5% | +326.5% | -21.1% | +0.93% | 100% |
| dip40_V3_gescreend_fail | 3033 | 13% | 5.8% | +115.3% | -29.7% | -10.85% | 100% |
| dip40_V3_alle | 3429 | 12% | 5.6% | +122.7% | -29.1% | -10.23% | 100% |
| dip45_V1_gescreend_pass | 302 | 15% | 1.7% | +52.1% | -15.3% | -5.05% | 98% |
| dip45_V1_gescreend_fail | 2907 | 27% | 3.3% | +48.7% | -25.8% | -5.37% | 100% |
| dip45_V1_alle | 3298 | 26% | 3.3% | +49.1% | -25.0% | -5.44% | 100% |
| dip45_V2_gescreend_pass | 299 | 18% | 2.3% | +47.6% | -19.6% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 2891 | 25% | 3.9% | +59.6% | -27.9% | -5.97% | 100% |
| dip45_V2_alle | 3264 | 24% | 3.9% | +58.5% | -27.3% | -6.46% | 100% |
| dip45_V3_gescreend_pass | 302 | 7% | 2.3% | +379.4% | -20.3% | +6.15% | 100% |
| dip45_V3_gescreend_fail | 2933 | 14% | 5.5% | +123.3% | -29.3% | -8.06% | 100% |
| dip45_V3_alle | 3300 | 13% | 5.3% | +133.2% | -28.6% | -7.21% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2293 | 12% | 3.0% | -9.86% | 100% |
| zonder_xlink | 576 | 18% | 0.0% | +20.52% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 20:03:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:21,032 main INFO screen NOPLANES pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (14.2s)
Sep 11 20:03:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:25,040 main INFO screen TRILL pass=0 dev=0.0 ins=42.52 pro=45 1a=False 1b=False 2=True (24.7s)
Sep 11 20:04:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:02,321 main INFO screen ALLCAT pass=1 dev=0.0 ins=0.0 pro=57 1a=False 1b=False 2=False (8.4s)
Sep 11 20:04:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:22,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:04:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:30,556 main INFO screen Gambler pass=0 dev=0.0 ins=17.99 pro=74 1a=False 1b=False 2=True (8.6s)
Sep 11 20:04:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:35,196 main INFO screen Squad pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.4s)
Sep 11 20:05:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:14,306 main INFO screen $COORATE pass=0 dev=0.46 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 11 20:05:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:17,796 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:05:17 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
Sep 11 20:05:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:32,062 aiohttp.access INFO 94.154.43.223 [11/Sep/2026:20:05:32 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 20:05:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:33,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:05:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:45,106 main INFO screen up pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (11.7s)
Sep 11 20:05:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:49,561 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:05:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:54,624 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:05:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:56,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:02,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:09,658 main INFO screen DONKEY pass=0 dev=0.0 ins=0.8 pro=32 1a=False 1b=False 2=True (20.2s)
Sep 11 20:06:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:12,571 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:16,923 main INFO screen DONKEY pass=0 dev=0.0 ins=38.19 pro=18 1a=False 1b=False 2=True (20.0s)
Sep 11 20:06:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:17,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:20,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:25,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:06:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:33,257 main INFO screen KONG pass=0 dev=79.11 ins=0.0 pro=2 1a=False 1b=False 2=True (20.7s)
Sep 11 20:06:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:46,133 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.5s)
Sep 11 20:06:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:06:57,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:02,089 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:06,767 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:11,841 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:19,805 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:21,865 main INFO screen trenchcat pass=0 dev=0.0 ins=52.13 pro=48 1a=False 1b=False 2=True (25.0s)
Sep 11 20:07:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:24,950 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:25,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:07:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:29,855 main INFO screen GTA 6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.2s)
Sep 11 20:07:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:36,170 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (10.7s)
Sep 11 20:07:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:07:45,928 main INFO screen RKT pass=0 dev=0.0 ins=1.04 pro=25 1a=False 1b=False 2=True (26.2s)
Sep 11 20:08:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:08:11,662 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:20:08:11 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 20:09:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:12,885 main INFO screen SIMPSON pass=0 dev=0.35 ins=0.04 pro=2 1a=False 1b=False 2=False (6.0s)
Sep 11 20:09:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:16,943 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:09:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:22,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:09:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:41,251 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:09:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:41,375 main INFO screen Elunk pass=0 dev=0.14 ins=76.31 pro=9 1a=False 1b=True 2=True (24.5s)
Sep 11 20:09:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:46,360 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:09:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:49,634 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 20:09:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:54,677 main INFO screen ZFBRAIN pass=1 dev=0.35 ins=0.0 pro=33 1a=False 1b=False 2=False (10.7s)
Sep 11 20:09:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:09:57,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:10:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:01,800 main INFO screen DKNG pass=0 dev=0.0 ins=15.68 pro=70 1a=False 1b=False 2=True (20.6s)
Sep 11 20:10:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:02,988 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (8.2s)
Sep 11 20:10:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:03,044 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:10:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:12,212 main INFO screen TRUMPCOIN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 11 20:10:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:19,377 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:10:19 +0000] "GET /health HTTP/1.1" 200 444 "-" "Python-urllib/3.14"
Sep 11 20:10:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:22,466 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.6s)
Sep 11 20:10:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:38,512 main INFO screen DERP pass=0 dev=0.87 ins=0.0 pro=3 1a=False 1b=False 2=False (11.2s)
Sep 11 20:10:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:46,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:10:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:10:51,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:11:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:11:12,385 main INFO screen Duplicate pass=0 dev=2.0 ins=77.31 pro=3 1a=True 1b=True 2=True (26.2s)
Sep 11 20:11:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:11:13,062 main INFO screen Soltrink pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (10.5s)
Sep 11 20:12:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:00,543 main INFO screen QUIVER pass=1 dev=1.81 ins=0.72 pro=46 1a=False 1b=False 2=False (10.5s)
Sep 11 20:12:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:01,250 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (11.5s)
Sep 11 20:12:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:06,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:12:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:10,775 main INFO screen $REGRET pass=0 dev=0.61 ins=0.0 pro=3 1a=False 1b=False 2=False (8.2s)
Sep 11 20:12:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:18,047 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (11.4s)
Sep 11 20:12:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:20,626 main INFO screen djsksn pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.4s)
Sep 11 20:12:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:26,754 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:12:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:31,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:12:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:32,105 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:12:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:37,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:12:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:49,860 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (23.2s)
Sep 11 20:12:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:12:56,243 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.2s)
Sep 11 20:13:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:13:11,189 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 20:13:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:13:12,303 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 20:13:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:13:29,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:13:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:13:34,382 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:13:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:13:55,420 main INFO screen VOID pass=0 dev=40.61 ins=0.0 pro=7 1a=False 1b=False 2=True (26.2s)
Sep 11 20:14:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:20,428 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:14:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:23,703 main INFO screen flyon pass=0 dev=0.0 ins=27.64 pro=8 1a=False 1b=False 2=False (8.5s)
Sep 11 20:14:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:25,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:14:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:36,829 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:14:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:41,862 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:14:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:14:47,488 main INFO screen VIRGIN pass=0 dev=0.0 ins=48.4 pro=28 1a=False 1b=False 2=True (27.1s)
Sep 11 20:15:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:15:02,712 main INFO screen Squad pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (26.0s)
Sep 11 20:15:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:15:23,479 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:15:23 +0000] "GET /health HTTP/1.1" 200 444 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T18:59:19Z
--- update 2026-09-11T19:04:36Z
--- update 2026-09-11T19:09:39Z
--- update 2026-09-11T19:14:45Z
--- update 2026-09-11T19:19:51Z
--- update 2026-09-11T19:24:55Z
--- update 2026-09-11T19:30:02Z
--- update 2026-09-11T19:35:03Z
--- update 2026-09-11T19:40:04Z
nieuwe code: 1cefa36
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 670a5941fedf41389993862a94844cc9
analyses gestart (8746aefc73b4)
--- update 2026-09-11T19:45:08Z
--- update 2026-09-11T19:50:11Z
--- update 2026-09-11T19:55:12Z
--- update 2026-09-11T20:00:15Z
--- update 2026-09-11T20:05:16Z
--- update 2026-09-11T20:10:18Z
--- update 2026-09-11T20:15:22Z
```

## Analyses (laatste 25 regels)
```
inactive
18:40:27 kopieer-simulatie
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
19:40:08 12765 tokens sinds start volledige logging, waarvan 3627 met een gat door herstart
19:40:11   ingelezen tot rowid 2225120 (145387 rijen, 145387 bruikbaar)
19:40:11 ingelezen: 145387 nieuwe trades, 145387 bruikbaar (3s)
19:40:22 177 aankopen van gevolgde wallets geëvalueerd
19:40:34 grote spelers: saldo van 2000 wallets opgehaald
19:41:46 herkomst: 40 posities gekoppeld
19:41:47 klaar in 99s -> /opt/schaduwbot/reports/ledger.md
19:41:49 klaar in 1s: 6168 tokens, 1142 nieuw -> /opt/schaduwbot/reports/video_replay.md
19:41:49 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 19:41 UTC
19:41:49 37636 tokens geladen
19:41:51   2000 tokens, 281880 trades, 68228 posities (2s)
19:41:53   4000 tokens, 562091 trades, 134424 posities (4s)
19:41:56   6000 tokens, 870184 trades, 206311 posities (7s)
19:41:58   8000 tokens, 1149114 trades, 266897 posities (9s)
19:42:01   10000 tokens, 1443511 trades, 336633 posities (12s)
19:42:03   12000 tokens, 1716836 trades, 400450 posities (14s)
19:42:06   14000 tokens, 1988268 trades, 462617 posities (17s)
19:42:08 posities: 523618 uit 2226699 trades (19s)
19:42:14 123108 wallets gerekend
19:42:14 geluk-toets
19:42:33 persistentie
19:42:34 kopieer-simulatie
19:42:39 klaar in 51s -> /opt/schaduwbot/reports/wallets.md
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
