# Schaduwbot status

- tijd: 2026-09-12 00:24:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 10 hours, 37 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.1G/38G | geheugen: 965/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 17046, "tokens_in_memory": 6379, "msgs": 4028190, "trades": 713109, "creates": 6379, "decode_fail": 38584, "rpc_calls": 24036, "rpc_errors": 926, "sol_usd": 102.30215299647564, "open_positions": 85, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 23:40 UTC

Gelogde schaduwtrades: **36036**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28017 | 4378 | 41 | 4376 | 367 | 8031 | 23681 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 420 | 17% | 2.4% | +44.7% | -17.2% | -6.61% | 100% |
| dip35_V1_gescreend_fail | 3472 | 27% | 3.7% | +45.7% | -26.0% | -6.87% | 100% |
| dip35_V1_alle | 4172 | 26% | 3.7% | +44.6% | -25.3% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 417 | 22% | 3.4% | +46.2% | -21.8% | -7.08% | 100% |
| dip35_V2_gescreend_fail | 3481 | 25% | 4.3% | +56.5% | -28.2% | -7.34% | 100% |
| dip35_V2_alle | 4130 | 24% | 4.4% | +54.3% | -27.8% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 417 | 9% | 3.8% | +331.7% | -23.0% | +8.45% | 100% |
| dip35_V3_gescreend_fail | 3561 | 13% | 5.9% | +118.6% | -29.7% | -9.86% | 100% |
| dip35_V3_alle | 4180 | 13% | 5.8% | +127.1% | -29.3% | -8.73% | 100% |
| dip40_V1_gescreend_pass | 390 | 15% | 2.6% | +47.3% | -16.5% | -6.86% | 100% |
| dip40_V1_gescreend_fail | 3401 | 26% | 3.7% | +47.4% | -25.9% | -6.72% | 100% |
| dip40_V1_alle | 4007 | 25% | 3.7% | +47.1% | -25.2% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 388 | 17% | 3.1% | +50.1% | -20.4% | -8.40% | 100% |
| dip40_V2_gescreend_fail | 3392 | 25% | 4.2% | +55.5% | -28.1% | -7.55% | 100% |
| dip40_V2_alle | 3959 | 24% | 4.2% | +54.2% | -27.6% | -8.11% | 100% |
| dip40_V3_gescreend_pass | 391 | 8% | 3.3% | +343.8% | -21.5% | +6.53% | 100% |
| dip40_V3_gescreend_fail | 3469 | 13% | 5.6% | +113.5% | -29.5% | -10.94% | 100% |
| dip40_V3_alle | 4015 | 13% | 5.6% | +122.7% | -29.0% | -9.85% | 100% |
| dip45_V1_gescreend_pass | 374 | 16% | 2.4% | +48.8% | -16.4% | -5.75% | 100% |
| dip45_V1_gescreend_fail | 3322 | 27% | 3.2% | +47.8% | -25.6% | -5.55% | 100% |
| dip45_V1_alle | 3873 | 26% | 3.3% | +47.7% | -25.0% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 371 | 19% | 3.0% | +48.3% | -20.2% | -7.12% | 100% |
| dip45_V2_gescreend_fail | 3305 | 25% | 3.8% | +57.6% | -27.7% | -6.37% | 100% |
| dip45_V2_alle | 3826 | 24% | 3.9% | +56.0% | -27.2% | -6.97% | 100% |
| dip45_V3_gescreend_pass | 375 | 8% | 2.9% | +392.1% | -20.8% | +11.14% | 100% |
| dip45_V3_gescreend_fail | 3369 | 14% | 5.3% | +120.2% | -29.0% | -8.15% | 100% |
| dip45_V3_alle | 3874 | 13% | 5.2% | +132.0% | -28.4% | -6.94% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.6%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2718 | 13% | 3.9% | -9.99% | 100% |
| zonder_xlink | 825 | 19% | 0.0% | +25.41% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 00:09:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:09:46,093 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.1s)
Sep 12 00:10:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:12,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:17,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:30,244 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:34,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:35,313 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:36,911 main INFO screen PINO pass=0 dev=1.46 ins=59.01 pro=9 1a=False 1b=False 2=True (24.1s)
Sep 12 00:10:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:38,266 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:39,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:43,335 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:10:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:50,726 main INFO screen HUC pass=0 dev=0.0 ins=17.44 pro=58 1a=False 1b=False 2=True (20.6s)
Sep 12 00:10:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:10:53,387 main INFO screen Bary pass=0 dev=6.63 ins=23.33 pro=25 1a=False 1b=False 2=True (19.3s)
Sep 12 00:11:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:11:01,182 main INFO screen SUITDOG pass=0 dev=0.0 ins=25.45 pro=77 1a=False 1b=False 2=True (23.0s)
Sep 12 00:11:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:11:11,377 main INFO screen PepeCoin pass=0 dev=0.0 ins=20.88 pro=80 1a=False 1b=False 2=True (8.2s)
Sep 12 00:11:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:11:16,069 main INFO screen 0 pass=1 dev=0.0 ins=16.31 pro=15 1a=False 1b=False 2=False (7.2s)
Sep 12 00:11:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:11:36,017 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:11:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:11:41,087 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:12:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:05,505 main INFO screen 0 pass=0 dev=0.0 ins=22.56 pro=15 1a=False 1b=False 2=True (29.6s)
Sep 12 00:12:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:19,820 main INFO screen Anything pass=0 dev=0.0 ins=21.0 pro=31 1a=False 1b=False 2=True (5.1s)
Sep 12 00:12:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:26,888 main INFO screen mygranny pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.3s)
Sep 12 00:12:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:27,208 main INFO screen Dih pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (8.2s)
Sep 12 00:12:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:34,563 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:12:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:46,660 main INFO screen ASS pass=0 dev=0.35 ins=0.0 pro=6 1a=False 1b=False 2=False (12.2s)
Sep 12 00:12:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:12:57,197 main INFO screen FlyEleven pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 12 00:13:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:01,239 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:00:13:01 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 00:13:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:10,376 main INFO screen PALESTINE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.4s)
Sep 12 00:13:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:23,398 main INFO screen $CAJUN pass=0 dev=1.08 ins=0.0 pro=4 1a=False 1b=False 2=False (9.4s)
Sep 12 00:13:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:37,101 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:13:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 00:13:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:41,240 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:13:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:13:50,033 main INFO screen ㅤ pass=0 dev=0.0 ins=26.69 pro=71 1a=False 1b=False 2=True (8.9s)
Sep 12 00:14:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:14:03,551 main INFO screen FLY pass=0 dev=0.0 ins=29.14 pro=17 1a=False 1b=False 2=False (9.1s)
Sep 12 00:14:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:14:47,159 main INFO screen howaboutmy? pass=0 dev=0.89 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 12 00:14:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:14:52,561 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:14:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:14:57,632 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:15:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:15:07,268 main INFO screen ㅤ pass=0 dev=0.0 ins=11.25 pro=33 1a=False 1b=False 2=True (2.9s)
Sep 12 00:15:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:15:16,498 main INFO screen ZBCN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.0s)
Sep 12 00:15:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:15:27,885 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:15:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:15:41,190 main INFO screen notmybag :( pass=0 dev=0.0 ins=0.03 pro=2 1a=False 1b=False 2=False (13.4s)
Sep 12 00:16:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:16:53,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:17:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:17:01,054 main INFO screen Gubby pass=0 dev=7.98 ins=0.06 pro=19 1a=False 1b=False 2=False (8.0s)
Sep 12 00:17:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:17:33,794 main INFO screen PALESTINE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 12 00:17:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:17:39,367 main INFO screen notmybag :( pass=0 dev=0.89 ins=0.03 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 12 00:17:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:17:54,839 main INFO screen WoDs pass=0 dev=0.62 ins=0.04 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 12 00:18:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:21,584 main INFO screen BLCKFROGE pass=0 dev=34.26 ins=0.0 pro=4 1a=False 1b=False 2=True (6.4s)
Sep 12 00:18:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:42,939 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:18:42 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 12 00:18:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:48,843 main INFO screen BetOnBlak pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 12 00:18:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:51,063 main INFO screen ARNO pass=0 dev=0.0 ins=0.04 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 00:18:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:52,074 main INFO screen ㅤ  pass=0 dev=0.0 ins=22.28 pro=62 1a=False 1b=False 2=True (3.2s)
Sep 12 00:18:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:55,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:18:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:18:56,190 main INFO screen $LION pass=0 dev=0.35 ins=0.04 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 00:19:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:00,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:19:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:19,339 main INFO screen ZBULL pass=0 dev=0.35 ins=60.59 pro=14 1a=False 1b=True 2=True (23.6s)
Sep 12 00:19:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:21,101 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.3s)
Sep 12 00:19:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:42,476 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:19:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:45,039 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:19:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:47,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:19:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:50,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:19:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:50,200 main INFO screen BEBEH pass=1 dev=1.22 ins=0.03 pro=13 1a=False 1b=False 2=False (8.8s)
Sep 12 00:19:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:19:59,529 main INFO screen ㅤ pass=1 dev=0.0 ins=0.46 pro=36 1a=False 1b=False 2=False (7.5s)
Sep 12 00:20:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:03,586 main INFO screen PIT pass=0 dev=0.0 ins=33.24 pro=52 1a=False 1b=False 2=True (21.4s)
Sep 12 00:20:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:09,344 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.4s)
Sep 12 00:20:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:12,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:20:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:22,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:20:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:27,106 main INFO screen WIFBATON pass=0 dev=0.72 ins=35.44 pro=4 1a=False 1b=False 2=True (9.9s)
Sep 12 00:20:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:27,202 main INFO screen $SCREM pass=0 dev=0.0 ins=0.04 pro=4 1a=False 1b=False 2=False (15.0s)
Sep 12 00:20:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:27,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:20:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:38,156 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.5s)
Sep 12 00:20:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:20:49,982 main INFO screen ROBIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.4s)
Sep 12 00:21:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:21:02,543 main INFO screen Zebra pass=0 dev=0.0 ins=15.12 pro=54 1a=False 1b=False 2=True (10.2s)
Sep 12 00:21:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:21:17,868 main INFO screen fast pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (9.7s)
Sep 12 00:21:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:21:34,561 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:21:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:21:49,800 main INFO screen ROMAN pass=0 dev=0.0 ins=17.56 pro=24 1a=False 1b=True 2=True (15.3s)
Sep 12 00:22:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:22:21,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:22:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:22:26,582 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:22:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:22:47,177 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.8s)
Sep 12 00:23:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:23:02,613 main INFO screen $WICK pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (6.7s)
Sep 12 00:23:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:23:10,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:23:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:23:15,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:23:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:23:34,844 main INFO screen suitdog pass=0 dev=0.0 ins=40.93 pro=21 1a=False 1b=False 2=True (24.6s)
Sep 12 00:24:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:24:14,578 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:24:14 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T22:56:09Z
--- update 2026-09-11T23:01:22Z
--- update 2026-09-11T23:06:34Z
--- update 2026-09-11T23:11:35Z
--- update 2026-09-11T23:16:36Z
--- update 2026-09-11T23:22:10Z
--- update 2026-09-11T23:27:17Z
--- update 2026-09-11T23:32:26Z
--- update 2026-09-11T23:37:30Z
--- update 2026-09-11T23:42:35Z
--- update 2026-09-11T23:47:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: b162cdb09d844c599f2691bd2f42382f
analyses gestart (8746aefc73b4)
--- update 2026-09-11T23:52:35Z
--- update 2026-09-11T23:57:36Z
--- update 2026-09-12T00:02:54Z
--- update 2026-09-12T00:08:05Z
--- update 2026-09-12T00:13:36Z
--- update 2026-09-12T00:18:41Z
--- update 2026-09-12T00:24:13Z
```

## Analyses (laatste 25 regels)
```
inactive
23:47:43 ingelezen: 322040 nieuwe trades, 322040 bruikbaar (7s)
23:48:00 2429 aankopen van gevolgde wallets geëvalueerd
23:48:06 grote spelers: saldo van 404 wallets opgehaald
23:49:10 herkomst: 40 posities gekoppeld
23:49:11 klaar in 95s -> /opt/schaduwbot/reports/ledger.md
23:49:13   2000 nieuwe tokens doorgerekend
23:49:14 klaar in 4s: 8512 tokens, 2651 nieuw -> /opt/schaduwbot/reports/video_replay.md
23:49:15 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 23:49 UTC
23:49:15 43238 tokens geladen
23:49:17   2000 tokens, 267586 trades, 60734 posities (3s)
23:49:20   4000 tokens, 532423 trades, 117776 posities (5s)
23:49:22   6000 tokens, 799668 trades, 174921 posities (7s)
23:49:24   8000 tokens, 1110246 trades, 245252 posities (10s)
23:49:26   10000 tokens, 1366401 trades, 294918 posities (12s)
23:49:29   12000 tokens, 1641516 trades, 355008 posities (14s)
23:49:31   14000 tokens, 1922876 trades, 417966 posities (16s)
23:49:34   16000 tokens, 2201914 trades, 478052 posities (19s)
23:49:36   18000 tokens, 2446968 trades, 532110 posities (22s)
23:49:39   20000 tokens, 2731719 trades, 594313 posities (24s)
23:49:40 posities: 627709 uit 2860518 trades (26s)
23:49:48 141754 wallets gerekend
23:49:49 geluk-toets
23:50:14 persistentie
23:50:15 kopieer-simulatie
23:50:24 klaar in 70s -> /opt/schaduwbot/reports/wallets.md
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
