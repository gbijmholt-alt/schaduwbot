# Schaduwbot status

- tijd: 2026-09-11 23:16:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 9 hours, 29 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.1G/38G | geheugen: 859/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 12988, "tokens_in_memory": 4926, "msgs": 3234411, "trades": 560356, "creates": 4926, "decode_fail": 33862, "rpc_calls": 18305, "rpc_errors": 696, "sol_usd": 102.11070992476918, "open_positions": 97, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 22:40 UTC

Gelogde schaduwtrades: **34765**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 26692 | 4119 | 41 | 4118 | 356 | 7605 | 22410 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 412 | 17% | 2.4% | +43.0% | -17.3% | -7.21% | 100% |
| dip35_V1_gescreend_fail | 3367 | 27% | 3.7% | +46.0% | -26.0% | -6.88% | 100% |
| dip35_V1_alle | 4023 | 26% | 3.7% | +44.8% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 407 | 21% | 3.4% | +46.2% | -21.9% | -7.52% | 100% |
| dip35_V2_gescreend_fail | 3380 | 25% | 4.3% | +56.5% | -28.3% | -7.45% | 100% |
| dip35_V2_alle | 3986 | 24% | 4.3% | +54.5% | -27.8% | -7.90% | 100% |
| dip35_V3_gescreend_pass | 410 | 8% | 3.9% | +349.6% | -23.1% | +8.70% | 100% |
| dip35_V3_gescreend_fail | 3453 | 13% | 5.9% | +120.6% | -29.8% | -9.84% | 100% |
| dip35_V3_alle | 4037 | 13% | 5.9% | +130.6% | -29.3% | -8.58% | 100% |
| dip40_V1_gescreend_pass | 381 | 15% | 2.6% | +46.5% | -16.7% | -7.38% | 100% |
| dip40_V1_gescreend_fail | 3296 | 26% | 3.7% | +47.8% | -25.9% | -6.68% | 100% |
| dip40_V1_alle | 3865 | 25% | 3.8% | +47.4% | -25.2% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 376 | 16% | 3.2% | +50.9% | -20.7% | -8.87% | 100% |
| dip40_V2_gescreend_fail | 3293 | 25% | 4.2% | +55.9% | -28.2% | -7.46% | 100% |
| dip40_V2_alle | 3821 | 24% | 4.3% | +54.9% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 382 | 7% | 3.4% | +367.0% | -21.6% | +6.84% | 100% |
| dip40_V3_gescreend_fail | 3361 | 13% | 5.7% | +115.5% | -29.6% | -10.85% | 100% |
| dip40_V3_alle | 3876 | 12% | 5.7% | +126.6% | -29.1% | -9.70% | 100% |
| dip45_V1_gescreend_pass | 366 | 16% | 2.5% | +49.0% | -16.5% | -5.98% | 100% |
| dip45_V1_gescreend_fail | 3214 | 27% | 3.3% | +48.4% | -25.7% | -5.52% | 100% |
| dip45_V1_alle | 3732 | 26% | 3.3% | +48.2% | -25.0% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 360 | 19% | 3.1% | +49.7% | -20.5% | -7.21% | 100% |
| dip45_V2_gescreend_fail | 3201 | 25% | 3.8% | +58.4% | -27.9% | -6.27% | 100% |
| dip45_V2_alle | 3687 | 24% | 3.9% | +57.0% | -27.3% | -6.89% | 100% |
| dip45_V3_gescreend_pass | 366 | 7% | 3.0% | +419.8% | -20.9% | +11.59% | 100% |
| dip45_V3_gescreend_fail | 3261 | 14% | 5.4% | +122.4% | -29.1% | -7.95% | 100% |
| dip45_V3_alle | 3738 | 13% | 5.3% | +135.9% | -28.5% | -6.65% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.5%, kans ruïne 99.5%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2662 | 13% | 4.0% | -10.32% | 100% |
| zonder_xlink | 798 | 18% | 0.0% | +26.25% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 23:06:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:28,758 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:06:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:33,816 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:06:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:35,107 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:06:35 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 23:06:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:47,136 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:06:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:49,251 main INFO screen PUMP pass=0 dev=0.0 ins=31.78 pro=50 1a=False 1b=False 2=True (20.6s)
Sep 11 23:06:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:06:52,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:14,531 main INFO screen ANTH pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.0s)
Sep 11 23:07:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:17,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:24,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:29,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:29,741 main INFO screen CT pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (12.3s)
Sep 11 23:07:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:45,512 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:50,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:53,514 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (29.7s)
Sep 11 23:07:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:53,542 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:07:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:55,556 main INFO screen FROBERT pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (10.4s)
Sep 11 23:07:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:07:59,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:08:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:07,693 main INFO screen FLYJAK pass=0 dev=0.0 ins=27.83 pro=23 1a=False 1b=False 2=False (9.9s)
Sep 11 23:08:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:11,334 main INFO screen WTML pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (25.9s)
Sep 11 23:08:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:14,087 main INFO screen trenchenergy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.4s)
Sep 11 23:08:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:25,698 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:08:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:26,251 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (32.7s)
Sep 11 23:08:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:27,985 main INFO screen SPRITEBOY pass=0 dev=3.35 ins=16.74 pro=22 1a=False 1b=False 2=True (8.3s)
Sep 11 23:08:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:30,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:08:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:43,089 main INFO screen Meowsterchef pass=0 dev=1.0 ins=32.66 pro=32 1a=False 1b=False 2=True (9.0s)
Sep 11 23:08:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:08:49,872 main INFO screen PEP pass=0 dev=0.47 ins=52.3 pro=20 1a=False 1b=False 2=True (24.2s)
Sep 11 23:09:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:10,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:09:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:13,469 main INFO screen STONKFLY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 11 23:09:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:15,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:09:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:20,267 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:09:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:24,019 main INFO screen UFD pass=0 dev=0.0 ins=22.84 pro=48 1a=False 1b=False 2=True (2.7s)
Sep 11 23:09:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:28,534 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:09:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:35,157 main INFO screen Choco coin pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (14.9s)
Sep 11 23:09:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:35,326 main INFO screen SNAILCAT pass=0 dev=6.63 ins=20.96 pro=37 1a=False 1b=False 2=False (7.1s)
Sep 11 23:09:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:36,707 main INFO screen Anthropic pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.9s)
Sep 11 23:09:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:46,237 main INFO screen WCOI pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=True (9.3s)
Sep 11 23:09:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:09:49,605 main INFO screen FROBERT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 11 23:10:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:04,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:10:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:09,184 main INFO screen mm pass=0 dev=0.88 ins=0.0 pro=4 1a=False 1b=False 2=False (7.5s)
Sep 11 23:10:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:17,923 main INFO screen DUMB pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.9s)
Sep 11 23:10:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:20,690 main INFO screen M&M  pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (16.3s)
Sep 11 23:10:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:37,510 main INFO screen CAT pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (11.9s)
Sep 11 23:10:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:10:58,372 main INFO screen ice man pass=0 dev=0.23 ins=0.0 pro=4 1a=False 1b=False 2=False (8.0s)
Sep 11 23:11:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:18,094 main INFO screen NEEGY pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 11 23:11:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:24,843 main INFO screen Bricko pass=0 dev=0.37 ins=0.0 pro=3 1a=False 1b=False 2=False (6.9s)
Sep 11 23:11:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:36,764 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:11:36 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 23:11:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:38,961 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:11:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:44,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:11:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:46,542 main INFO screen $CAJUN pass=0 dev=0.63 ins=0.0 pro=3 1a=False 1b=False 2=False (11.1s)
Sep 11 23:11:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:50,578 main INFO screen ice man pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.0s)
Sep 11 23:11:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:50,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:11:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:53,906 main INFO screen BTC pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (9.7s)
Sep 11 23:11:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:11:59,644 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:12:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:00,869 main INFO screen PUMP pass=0 dev=1.66 ins=20.35 pro=31 1a=False 1b=False 2=False (10.3s)
Sep 11 23:12:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:03,928 main INFO screen WTML pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (25.0s)
Sep 11 23:12:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:04,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:12:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:15,787 main INFO screen cap pass=0 dev=0.44 ins=0.0 pro=3 1a=False 1b=False 2=False (11.1s)
Sep 11 23:12:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:25,969 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.5s)
Sep 11 23:12:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:12:52,297 main INFO screen bam ban pass=0 dev=0.48 ins=0.0 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 11 23:13:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:06,300 main INFO screen MONEY pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 11 23:13:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:06,420 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:11,490 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:27,271 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:29,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:29,678 main INFO screen CHILLBRAIN pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (23.3s)
Sep 11 23:13:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:32,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:34,409 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:13:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:55,972 main INFO screen Quant pass=0 dev=0.0 ins=19.86 pro=69 1a=False 1b=False 2=True (28.8s)
Sep 11 23:13:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:56,067 main INFO screen DancingFly pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (26.8s)
Sep 11 23:13:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:13:59,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:14:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:14:07,306 main INFO screen COPS pass=0 dev=0.0 ins=21.31 pro=36 1a=False 1b=False 2=True (7.6s)
Sep 11 23:14:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:14:08,984 main INFO screen WCOI pass=0 dev=2.25 ins=0.0 pro=4 1a=False 1b=False 2=True (6.3s)
Sep 11 23:14:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:14:33,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:14:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:14:33,806 main INFO screen WTML pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 23:14:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:14:45,317 main INFO screen mm pass=0 dev=1.09 ins=0.0 pro=1 1a=False 1b=False 2=False (11.6s)
Sep 11 23:15:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:15:17,880 main INFO screen bam ban pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 23:15:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:15:33,946 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:15:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:15:39,013 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:16:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:16:00,615 main INFO screen risk pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (26.8s)
Sep 11 23:16:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:16:37,107 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:16:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
--- update 2026-09-11T21:47:46Z
--- update 2026-09-11T21:53:06Z
--- update 2026-09-11T21:58:16Z
--- update 2026-09-11T22:03:36Z
--- update 2026-09-11T22:08:49Z
--- update 2026-09-11T22:14:14Z
--- update 2026-09-11T22:19:36Z
--- update 2026-09-11T22:25:36Z
--- update 2026-09-11T22:30:35Z
--- update 2026-09-11T22:35:46Z
--- update 2026-09-11T22:40:58Z
--- update 2026-09-11T22:45:58Z
--- update 2026-09-11T22:51:07Z
--- update 2026-09-11T22:56:09Z
--- update 2026-09-11T23:01:22Z
--- update 2026-09-11T23:06:34Z
--- update 2026-09-11T23:11:35Z
--- update 2026-09-11T23:16:36Z
```

## Analyses (laatste 25 regels)
```
inactive
21:42:40   ingelezen tot rowid 2425120 (200000 rijen, 200000 bruikbaar)
21:42:43   ingelezen tot rowid 2533436 (308316 rijen, 308316 bruikbaar)
21:42:43 ingelezen: 308316 nieuwe trades, 308316 bruikbaar (6s)
21:42:56 777 aankopen van gevolgde wallets geëvalueerd
21:43:01 grote spelers: saldo van 425 wallets opgehaald
21:43:56 herkomst: 40 posities gekoppeld
21:43:58 klaar in 82s -> /opt/schaduwbot/reports/ledger.md
21:43:59 klaar in 1s: 6168 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
21:43:59 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 21:43 UTC
21:43:59 40246 tokens geladen
21:44:02   2000 tokens, 264665 trades, 62063 posities (3s)
21:44:04   4000 tokens, 539436 trades, 121662 posities (5s)
21:44:07   6000 tokens, 831867 trades, 188339 posities (8s)
21:44:10   8000 tokens, 1123316 trades, 253063 posities (10s)
21:44:12   10000 tokens, 1410949 trades, 318168 posities (13s)
21:44:15   12000 tokens, 1691732 trades, 380121 posities (16s)
21:44:18   14000 tokens, 1969718 trades, 443453 posities (19s)
21:44:20   16000 tokens, 2230065 trades, 499999 posities (21s)
21:44:23   18000 tokens, 2510034 trades, 567609 posities (24s)
21:44:23 posities: 576157 uit 2537772 trades (24s)
21:44:30 132608 wallets gerekend
21:44:31 geluk-toets
21:44:52 persistentie
21:44:53 kopieer-simulatie
21:45:01 klaar in 62s -> /opt/schaduwbot/reports/wallets.md
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
