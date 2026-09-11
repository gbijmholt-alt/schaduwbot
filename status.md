# Schaduwbot status

- tijd: 2026-09-11 14:54:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 1 hour, 7 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 718/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 18304, "tokens_in_memory": 5189, "msgs": 1759069, "trades": 439440, "creates": 5189, "decode_fail": 36051, "rpc_calls": 7775, "rpc_errors": 736, "sol_usd": 103.3701293313587, "open_positions": 53, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 14:49 UTC

Gelogde schaduwtrades: **24489**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 15864 | 2207 | 24 | 2207 | 145 | 4118 | 12134 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 273 | 15% | 1.5% | +41.0% | -15.9% | -7.53% | 99% |
| dip35_V1_gescreend_fail | 2474 | 26% | 3.8% | +45.6% | -26.0% | -7.17% | 100% |
| dip35_V1_alle | 2832 | 26% | 3.9% | +44.6% | -25.3% | -7.50% | 100% |
| dip35_V2_gescreend_pass | 272 | 18% | 2.2% | +39.7% | -21.0% | -10.30% | 100% |
| dip35_V2_gescreend_fail | 2476 | 25% | 4.5% | +56.2% | -28.4% | -7.66% | 100% |
| dip35_V2_alle | 2810 | 24% | 4.6% | +54.4% | -28.0% | -8.35% | 100% |
| dip35_V3_gescreend_pass | 274 | 7% | 2.2% | +133.5% | -22.4% | -11.58% | 100% |
| dip35_V3_gescreend_fail | 2512 | 13% | 6.2% | +110.4% | -30.0% | -11.43% | 100% |
| dip35_V3_alle | 2843 | 13% | 6.1% | +108.7% | -29.5% | -11.87% | 100% |
| dip40_V1_gescreend_pass | 253 | 13% | 1.6% | +42.9% | -15.3% | -7.52% | 99% |
| dip40_V1_gescreend_fail | 2406 | 26% | 3.8% | +47.8% | -25.9% | -6.67% | 100% |
| dip40_V1_alle | 2722 | 25% | 3.8% | +46.9% | -25.1% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 252 | 14% | 2.4% | +49.8% | -20.0% | -10.59% | 100% |
| dip40_V2_gescreend_fail | 2400 | 25% | 4.2% | +55.8% | -28.2% | -7.50% | 100% |
| dip40_V2_alle | 2697 | 24% | 4.3% | +55.1% | -27.6% | -8.20% | 100% |
| dip40_V3_gescreend_pass | 254 | 6% | 2.4% | +112.1% | -21.4% | -13.48% | 100% |
| dip40_V3_gescreend_fail | 2438 | 13% | 5.8% | +98.8% | -29.7% | -13.01% | 100% |
| dip40_V3_alle | 2733 | 12% | 5.7% | +97.8% | -29.1% | -13.44% | 100% |
| dip45_V1_gescreend_pass | 242 | 14% | 1.7% | +49.5% | -15.3% | -6.19% | 98% |
| dip45_V1_gescreend_fail | 2338 | 27% | 3.4% | +49.5% | -25.6% | -5.01% | 100% |
| dip45_V1_alle | 2626 | 26% | 3.4% | +49.2% | -24.8% | -5.38% | 100% |
| dip45_V2_gescreend_pass | 240 | 18% | 2.5% | +49.2% | -19.7% | -7.34% | 99% |
| dip45_V2_gescreend_fail | 2320 | 25% | 3.8% | +58.7% | -27.7% | -5.99% | 100% |
| dip45_V2_alle | 2596 | 24% | 3.9% | +57.7% | -27.1% | -6.49% | 100% |
| dip45_V3_gescreend_pass | 242 | 7% | 2.5% | +180.2% | -20.6% | -7.31% | 100% |
| dip45_V3_gescreend_fail | 2356 | 14% | 5.6% | +112.8% | -29.2% | -9.68% | 100% |
| dip45_V3_alle | 2630 | 13% | 5.5% | +114.4% | -28.6% | -9.82% | 100% |

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
| met_xlink | 1861 | 12% | 2.6% | -10.03% | 100% |
| zonder_xlink | 441 | 13% | 0.0% | -5.41% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 14:40:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:32,046 main INFO screen DERP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 11 14:40:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:46,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:40:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:46,924 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:40:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:47,053 main INFO screen $PTA  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:41:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:41:15,093 main INFO screen J777CRYPTO pass=0 dev=0.0 ins=24.6 pro=13 1a=False 1b=False 2=True (2.0s)
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,784 main INFO screen s pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:27,895 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:28,062 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:28,193 main INFO screen HZN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:42:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:29,858 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:29,983 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:30,142 main INFO screen BULL pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 14:43:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:24,615 main INFO screen NASDARQ pass=0 dev=3.46 ins=33.08 pro=12 1a=False 1b=False 2=True (1.3s)
Sep 11 14:43:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:32,342 main INFO screen kittylick pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 14:43:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:41,161 main INFO screen USMS pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,550 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,810 main INFO screen brainpeppe pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,934 main INFO screen nudey pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,544 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,747 main INFO screen Flybook pass=0 dev=0.0 ins=36.52 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 14:44:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:37,319 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:44:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 14:45:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:00,035 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:45:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:00,130 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:45:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:00,345 main INFO screen s pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:45:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:19,621 main INFO screen stockpump pass=1 dev=0.03 ins=1.82 pro=22 1a=False 1b=False 2=False (3.2s)
Sep 11 14:45:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:57,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:45:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:57,970 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:45:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:45:58,174 main INFO screen TRUTH pass=0 dev=0.0 ins=20.84 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 11 14:46:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:46:22,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:46:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:46:22,293 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:46:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:46:22,707 main INFO screen WEN pass=0 dev=0.0 ins=8.42 pro=5 1a=False 1b=False 2=True (0.6s)
Sep 11 14:46:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:46:56,819 main INFO screen BurndSend pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 11 14:47:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:09,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:47:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:09,860 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:47:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:10,004 main INFO screen USWS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:47:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:22,105 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:47:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:22,232 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:47:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:22,393 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 14:47:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:35,305 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:47:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:35,429 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:47:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:35,574 main INFO screen HIMOTHY pass=0 dev=0.0 ins=15.14 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 11 14:47:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:59,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:47:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:47:59,841 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:48:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:48:00,025 main INFO screen Camel Toe pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 14:48:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:48:31,692 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:48:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:48:32,844 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:48:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:48:35,216 main INFO screen BULLFLY pass=0 dev=0.0 ins=32.08 pro=6 1a=False 1b=False 2=True (3.6s)
Sep 11 14:48:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:48:46,710 aiohttp.access INFO 89.42.231.200 [11/Sep/2026:14:48:46 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 11 14:49:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:49:41,144 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:49:41 +0000] "GET /health HTTP/1.1" 200 447 "-" "Python-urllib/3.14"
Sep 11 14:49:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:49:42,533 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 11 14:50:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:50:40,803 main INFO screen TRANSDAD pass=0 dev=0.02 ins=0.0 pro=7 1a=False 1b=False 2=False (6.7s)
Sep 11 14:50:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:50:41,127 main INFO screen SXSN pass=0 dev=9.67 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 14:50:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:50:42,394 main INFO screen carols pass=0 dev=0.93 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 11 14:51:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:51:15,105 aiohttp.access INFO 204.76.203.49 [11/Sep/2026:14:51:15 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 11 14:51:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:51:15,128 aiohttp.access INFO 204.76.203.49 [11/Sep/2026:14:51:15 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 11 14:51:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:51:24,071 main INFO screen Iolani pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 14:52:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:09,717 main INFO screen UPS pass=0 dev=8.1 ins=17.78 pro=19 1a=False 1b=False 2=True (1.3s)
Sep 11 14:52:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:32,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:52:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:32,177 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:52:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:32,379 main INFO screen SheHere pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 14:52:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:32,482 main INFO screen MoonPepe pass=0 dev=0.0 ins=25.31 pro=18 1a=False 1b=False 2=True (2.8s)
Sep 11 14:52:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:34,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:52:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:35,061 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:52:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:35,191 main INFO screen BULLFLY pass=0 dev=0.0 ins=31.92 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 11 14:52:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:48,493 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:52:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:48,606 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:52:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:52:48,758 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:53:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:03,720 main INFO screen $GOAT pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 14:53:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:09,023 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:53:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:09,143 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:53:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:09,375 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 14:53:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:25,341 main INFO screen SEPE pass=0 dev=0.0 ins=20.36 pro=17 1a=False 1b=False 2=False (1.8s)
Sep 11 14:53:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:52,350 main INFO screen scae pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (13.8s)
Sep 11 14:53:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:53:57,705 main INFO screen CHADSTER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 14:54:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:54:07,644 main INFO screen quant pass=1 dev=3.47 ins=2.05 pro=40 1a=False 1b=False 2=False (3.5s)
Sep 11 14:54:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:54:49,238 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:54:49 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T14:23:51Z
--- update 2026-09-11T14:29:07Z
--- update 2026-09-11T14:34:22Z
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
--- update 2026-09-11T14:49:38Z
--- update 2026-09-11T14:54:48Z
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
