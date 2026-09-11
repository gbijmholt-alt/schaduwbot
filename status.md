# Schaduwbot status

- tijd: 2026-09-11 20:05:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 6 hours, 18 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 582/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 1509, "tokens_in_memory": 542, "msgs": 358171, "trades": 58575, "creates": 542, "decode_fail": 4277, "rpc_calls": 1886, "rpc_errors": 88, "sol_usd": 102.40527510144939, "open_positions": 53, "log_all_trades": true}
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
Sep 11 19:55:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:13,752 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:55:13 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 19:55:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:17,684 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:55:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:27,919 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:55:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:36,962 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.4s)
Sep 11 19:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:37,710 main INFO screen BlackBag pass=0 dev=0.0 ins=20.85 pro=49 1a=False 1b=False 2=False (13.6s)
Sep 11 19:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:37,855 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:55:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:39,557 main INFO screen CHEDDAR pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (11.7s)
Sep 11 19:55:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:42,801 main INFO screen CATDUREX pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 11 19:55:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:42,929 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:55:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:58,362 main INFO screen FLT pass=0 dev=0.0 ins=46.0 pro=53 1a=False 1b=False 2=True (20.7s)
Sep 11 19:55:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:55:58,548 main INFO screen sKILLfun pass=0 dev=5.09 ins=0.79 pro=24 1a=False 1b=False 2=False (3.2s)
Sep 11 19:56:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:10,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:56:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:18,246 main INFO screen ALLINU pass=1 dev=0.0 ins=0.0 pro=60 1a=False 1b=False 2=False (8.1s)
Sep 11 19:56:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:31,070 main INFO screen unifying pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 19:56:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:33,121 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:56:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:36,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:56:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:38,190 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:56:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:42,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:56:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:51,903 main INFO screen YILF pass=0 dev=0.0 ins=20.49 pro=17 1a=False 1b=False 2=True (18.8s)
Sep 11 19:56:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:57,353 main INFO screen rlw pass=0 dev=0.0 ins=38.02 pro=15 1a=False 1b=False 2=True (20.4s)
Sep 11 19:56:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:56:58,027 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:57:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:03,102 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:57:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:13,992 main INFO screen hamster pass=0 dev=0.45 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 11 19:57:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:18,899 main INFO screen CASINO pass=0 dev=0.0 ins=7.38 pro=8 1a=False 1b=False 2=False (20.9s)
Sep 11 19:57:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:31,664 main INFO screen CASINU pass=1 dev=0.0 ins=16.73 pro=25 1a=False 1b=False 2=False (2.7s)
Sep 11 19:57:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:44,439 main INFO screen coin pass=0 dev=0.0 ins=17.35 pro=49 1a=False 1b=False 2=True (3.9s)
Sep 11 19:57:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:49,726 main INFO screen CATEus pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 11 19:57:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:57:58,242 main INFO screen CHIMP pass=1 dev=0.35 ins=0.0 pro=15 1a=False 1b=False 2=False (3.7s)
Sep 11 19:58:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:03,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:08,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:15,978 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:21,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:27,558 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=1 1a=False 1b=False 2=True (24.5s)
Sep 11 19:58:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:34,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:36,040 main INFO screen blackrock pass=0 dev=0.0 ins=15.83 pro=28 1a=False 1b=False 2=True (20.1s)
Sep 11 19:58:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:39,354 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:58:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:43,084 main INFO screen $REGRET pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 19:58:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:58:53,067 main INFO screen CHOGE pass=0 dev=0.0 ins=20.2 pro=15 1a=False 1b=False 2=True (19.3s)
Sep 11 19:59:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:21,680 main INFO screen 1 pass=0 dev=8.25 ins=0.0 pro=43 1a=False 1b=False 2=False (2.5s)
Sep 11 19:59:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:32,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:59:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:37,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:59:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:49,464 main INFO screen HIM/HER? pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 11 19:59:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:52,395 main INFO screen DOJO pass=0 dev=0.0 ins=14.55 pro=61 1a=False 1b=False 2=True (19.8s)
Sep 11 19:59:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:59:57,187 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:00:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:02,220 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:00:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:16,668 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:00:16 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
Sep 11 20:00:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:21,227 main INFO screen CATWIF pass=0 dev=0.0 ins=79.31 pro=3 1a=True 1b=True 2=True (24.1s)
Sep 11 20:00:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:50,406 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:00:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:53,554 main INFO screen Doggo pass=0 dev=0.0 ins=21.17 pro=54 1a=False 1b=False 2=True (4.2s)
Sep 11 20:00:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:00:55,476 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:01:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:00,795 main INFO screen ALLINU pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 11 20:01:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:02,006 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:01:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:11,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:01:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:16,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:01:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:17,024 main INFO screen Solnano pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (15.1s)
Sep 11 20:01:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:18,495 main INFO screen MOON pass=0 dev=0.0 ins=18.44 pro=38 1a=False 1b=False 2=True (28.9s)
Sep 11 20:01:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:28,777 main INFO screen hamster pass=1 dev=0.08 ins=0.0 pro=10 1a=False 1b=False 2=False (6.9s)
Sep 11 20:01:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:37,149 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (26.6s)
Sep 11 20:01:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:46,519 aiohttp.access INFO 62.171.146.116 [11/Sep/2026:20:01:46 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 20:01:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:50,728 main INFO screen USMS pass=0 dev=0.28 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 11 20:01:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:53,537 main INFO screen CHEDDAR pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 20:01:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:01:58,861 main INFO screen DOGE pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 20:02:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:23,670 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:02:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:28,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:02:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:33,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:02:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:39,155 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:02:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:43,802 main INFO screen RISK pass=0 dev=0.0 ins=16.2 pro=82 1a=False 1b=False 2=True (20.2s)
Sep 11 20:02:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:45,278 main INFO screen $CAJUN pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (6.4s)
Sep 11 20:02:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:02:59,902 main INFO screen 4XTRA pass=0 dev=1.05 ins=0.0 pro=25 1a=False 1b=False 2=True (26.0s)
Sep 11 20:03:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:00,450 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:03:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:05,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:03:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:06,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:03:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:21,032 main INFO screen NOPLANES pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (14.2s)
Sep 11 20:03:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:03:25,040 main INFO screen TRILL pass=0 dev=0.0 ins=42.52 pro=45 1a=False 1b=False 2=True (24.7s)
Sep 11 20:04:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:02,321 main INFO screen ALLCAT pass=1 dev=0.0 ins=0.0 pro=57 1a=False 1b=False 2=False (8.4s)
Sep 11 20:04:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:22,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:04:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:30,556 main INFO screen Gambler pass=0 dev=0.0 ins=17.99 pro=74 1a=False 1b=False 2=True (8.6s)
Sep 11 20:04:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:04:35,196 main INFO screen Squad pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.4s)
Sep 11 20:05:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:14,306 main INFO screen $COORATE pass=0 dev=0.46 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 11 20:05:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:05:17,796 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:05:17 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T18:48:56Z
--- update 2026-09-11T18:54:05Z
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
