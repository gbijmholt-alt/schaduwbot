# Schaduwbot status

- tijd: 2026-09-11 20:30:29 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 6 hours, 43 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 608/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3021, "tokens_in_memory": 991, "msgs": 634586, "trades": 119408, "creates": 991, "decode_fail": 8711, "rpc_calls": 3656, "rpc_errors": 180, "sol_usd": 102.4495329490737, "open_positions": 94, "log_all_trades": true}
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
Sep 11 20:21:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:07,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:08,108 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:12,219 main INFO screen GS pass=0 dev=0.0 ins=18.37 pro=34 1a=False 1b=True 2=True (6.2s)
Sep 11 20:21:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:12,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:14,098 main INFO screen GRUMPPYDOG pass=1 dev=0.0 ins=15.6 pro=16 1a=False 1b=False 2=False (1.9s)
Sep 11 20:21:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:18,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:24,092 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:26,770 main INFO screen kitty pass=0 dev=0.0 ins=12.69 pro=25 1a=False 1b=False 2=True (23.8s)
Sep 11 20:21:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:27,683 main INFO screen MM pass=0 dev=0.0 ins=0.9 pro=6 1a=False 1b=False 2=False (20.4s)
Sep 11 20:21:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:40,605 main INFO screen arc pass=0 dev=0.0 ins=14.66 pro=31 1a=False 1b=False 2=True (21.7s)
Sep 11 20:21:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:47,194 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:21:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:21:52,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:22:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:01,449 main INFO screen ALLIN pass=1 dev=0.0 ins=0.0 pro=46 1a=False 1b=False 2=False (9.9s)
Sep 11 20:22:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:02,542 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:22:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:10,063 main INFO screen ARC pass=0 dev=0.89 ins=14.48 pro=38 1a=False 1b=True 2=True (7.6s)
Sep 11 20:22:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:11,686 main INFO screen Architects pass=1 dev=0.46 ins=17.45 pro=17 1a=False 1b=False 2=False (2.2s)
Sep 11 20:22:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:12,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:22:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:13,483 main INFO screen JPM pass=0 dev=0.0 ins=21.19 pro=27 1a=False 1b=False 2=True (26.4s)
Sep 11 20:22:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:17,626 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:22:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:32,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:22:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:33,291 main INFO screen ARC pass=0 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=True (20.8s)
Sep 11 20:22:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:22:44,663 main INFO screen Moosk pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (12.4s)
Sep 11 20:23:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:03,910 main INFO screen CALLDOG pass=1 dev=0.0 ins=14.61 pro=20 1a=False 1b=False 2=False (7.9s)
Sep 11 20:23:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:27,293 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (8.8s)
Sep 11 20:23:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:48,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:23:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:48,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:23:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:53,397 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:23:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:53,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:23:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:23:53,703 main INFO screen Bricko pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (6.9s)
Sep 11 20:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:01,678 main INFO screen NUT pass=1 dev=0.0 ins=19.56 pro=47 1a=False 1b=False 2=False (8.0s)
Sep 11 20:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:01,760 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:24:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:07,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:24:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:15,947 main INFO screen TRADCAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (27.5s)
Sep 11 20:24:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:15,974 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.9s)
Sep 11 20:24:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:22,299 main INFO screen Allinu pass=0 dev=0.0 ins=8.78 pro=74 1a=False 1b=False 2=True (20.6s)
Sep 11 20:24:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:43,307 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 20:24:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:44,456 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 20:24:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:44,905 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:24:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:24:59,734 main INFO screen TRADCAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (14.9s)
Sep 11 20:25:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:17,259 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:22,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:29,164 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:25:29 +0000] "GET /health HTTP/1.1" 200 445 "-" "Python-urllib/3.14"
Sep 11 20:25:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:30,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:35,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:37,826 main INFO screen Rambo pass=0 dev=0.0 ins=20.12 pro=68 1a=False 1b=False 2=True (20.7s)
Sep 11 20:25:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:38,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:43,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:25:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:25:55,868 main INFO screen YEAST pass=0 dev=0.0 ins=21.53 pro=41 1a=False 1b=False 2=True (25.8s)
Sep 11 20:26:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:26:05,014 main INFO screen GTA 6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.7s)
Sep 11 20:26:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:26:17,578 main INFO screen LOTTO pass=0 dev=0.41 ins=0.0 pro=3 1a=False 1b=False 2=False (8.3s)
Sep 11 20:26:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:26:27,968 main INFO screen RIPANSEM pass=1 dev=2.71 ins=0.0 pro=50 1a=False 1b=False 2=False (9.1s)
Sep 11 20:26:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:26:54,482 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:26:59,551 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:14,379 main INFO screen BOY pass=0 dev=0.0 ins=16.45 pro=50 1a=False 1b=False 2=True (20.0s)
Sep 11 20:27:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:36,740 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:41,840 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:46,225 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:47,635 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:52,808 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:27:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:27:56,458 main INFO screen DONKAI pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (10.3s)
Sep 11 20:28:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:03,602 main INFO screen TRUMPTACO pass=0 dev=0.14 ins=0.0 pro=4 1a=False 1b=False 2=False (26.9s)
Sep 11 20:28:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:09,541 main INFO screen Degen pass=0 dev=1.0 ins=17.52 pro=78 1a=False 1b=False 2=True (22.0s)
Sep 11 20:28:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:13,860 main INFO screen Moon Cat pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 20:28:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:16,335 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:28:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:21,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:28:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:39,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:28:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:43,194 main INFO screen SOLAMA pass=0 dev=63.74 ins=0.0 pro=12 1a=False 1b=False 2=False (26.9s)
Sep 11 20:28:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:47,254 main INFO screen $GOAT pass=0 dev=0.66 ins=0.0 pro=2 1a=False 1b=False 2=True (10.7s)
Sep 11 20:28:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:52,760 main INFO screen Pumpabu pass=0 dev=0.0 ins=21.9 pro=29 1a=False 1b=False 2=True (13.7s)
Sep 11 20:28:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:53,114 main INFO screen WCCF pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 11 20:28:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:28:53,330 main INFO screen Catsnif pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (10.1s)
Sep 11 20:29:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:02,225 main INFO screen BOY pass=1 dev=0.04 ins=0.0 pro=44 1a=False 1b=False 2=False (3.1s)
Sep 11 20:29:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:19,609 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:29:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:24,689 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:29:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:44,776 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.3s)
Sep 11 20:29:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:47,801 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:29:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:29:52,875 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:30:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:30:10,581 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.9s)
Sep 11 20:30:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:30:23,964 main INFO screen FILES pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 20:30:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:30:29,488 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:30:29 +0000] "GET /health HTTP/1.1" 200 444 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T20:20:26Z
--- update 2026-09-11T20:25:28Z
--- update 2026-09-11T20:30:28Z
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
