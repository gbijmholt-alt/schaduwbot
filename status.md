# Schaduwbot status

- tijd: 2026-09-11 23:47:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 10 hours, 0 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.1G/38G | geheugen: 957/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 14848, "tokens_in_memory": 5594, "msgs": 3562591, "trades": 630356, "creates": 5594, "decode_fail": 36010, "rpc_calls": 21194, "rpc_errors": 816, "sol_usd": 102.43218227408441, "open_positions": 108, "log_all_trades": true}
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
Sep 11 23:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:05,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:39:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:08,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:39:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:10,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:39:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:13,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:39:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:25,001 main INFO screen NASA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 11 23:39:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:27,233 main INFO screen MEMES pass=0 dev=0.0 ins=36.27 pro=10 1a=False 1b=False 2=True (18.4s)
Sep 11 23:39:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:44,063 main INFO screen B pass=0 dev=0.0 ins=33.3 pro=38 1a=False 1b=False 2=True (3.8s)
Sep 11 23:39:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:39:55,853 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:40:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:40:00,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:41:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:03,559 main INFO screen CAlien pass=0 dev=0.08 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 11 23:41:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:03,989 main INFO screen te pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.2s)
Sep 11 23:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:04,922 main INFO screen $CAJUN pass=0 dev=0.5 ins=0.0 pro=3 1a=False 1b=False 2=False (10.1s)
Sep 11 23:41:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:07,336 main INFO screen LEBRO pass=0 dev=0.0 ins=29.48 pro=20 1a=False 1b=True 2=True (2.1s)
Sep 11 23:41:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:17,004 main INFO screen catlon pass=0 dev=0.57 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 11 23:41:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:19,332 main INFO screen ETH pass=0 dev=0.63 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 23:41:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:25,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:41:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:26,132 main INFO screen $BOXCAT pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 11 23:41:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:26,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:41:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:29,152 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 23:41:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:30,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:41:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:33,720 main INFO screen not a farm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.0s)
Sep 11 23:41:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:43,891 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:41:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:47,763 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.88 pro=15 1a=False 1b=False 2=True (22.8s)
Sep 11 23:41:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:50,221 main INFO screen FLYWIF pass=0 dev=0.0 ins=24.1 pro=12 1a=False 1b=False 2=False (7.9s)
Sep 11 23:41:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:41:51,615 main INFO screen cattrump pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 11 23:42:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:02,504 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:07,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:21,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:24,956 main INFO screen TOAD pass=0 dev=1.46 ins=58.86 pro=21 1a=False 1b=False 2=True (22.5s)
Sep 11 23:42:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:26,114 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:26,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:29,982 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:31,182 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:35,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:36,263 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:42:36 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 23:42:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:39,518 main INFO screen Swatter pass=0 dev=0.0 ins=20.35 pro=41 1a=True 1b=False 2=True (18.7s)
Sep 11 23:42:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:39,614 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:42:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:47,550 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.44 pro=19 1a=False 1b=False 2=True (21.5s)
Sep 11 23:42:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:50,179 main INFO screen AI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (10.7s)
Sep 11 23:42:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:50,905 main INFO screen brokr pass=0 dev=0.0 ins=39.55 pro=37 1a=False 1b=False 2=True (21.0s)
Sep 11 23:42:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:42:53,249 main INFO screen RIOT pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (5.7s)
Sep 11 23:43:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:14,534 main INFO screen GTFLY pass=0 dev=1.27 ins=9.36 pro=51 1a=False 1b=False 2=True (6.4s)
Sep 11 23:43:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:15,195 main INFO screen Costcow pass=0 dev=0.0 ins=15.92 pro=68 1a=False 1b=False 2=True (7.3s)
Sep 11 23:43:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:39,517 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:41,751 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:43,441 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:44,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:50,690 main INFO screen XDOG pass=0 dev=0.0 ins=17.62 pro=66 1a=False 1b=False 2=True (9.0s)
Sep 11 23:43:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:50,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:51,595 main INFO screen RIOT pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 11 23:43:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:56,000 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:56,348 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (4.7s)
Sep 11 23:43:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:56,416 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:43:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:59,282 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 11 23:43:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:43:59,424 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:44:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:01,482 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:44:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:05,601 main INFO screen XDOG pass=0 dev=6.63 ins=20.35 pro=22 1a=False 1b=False 2=True (6.3s)
Sep 11 23:44:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:10,818 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.44 pro=20 1a=False 1b=False 2=True (20.1s)
Sep 11 23:44:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:11,684 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 23:44:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:14,672 main INFO screen dog pass=0 dev=0.0 ins=29.45 pro=7 1a=True 1b=False 2=True (18.3s)
Sep 11 23:44:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:38,258 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:44:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:43,327 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:44:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:44:58,242 main INFO screen 91011 pass=0 dev=0.0 ins=8.79 pro=41 1a=False 1b=False 2=True (20.1s)
Sep 11 23:45:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:45:16,902 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:45:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:45:21,929 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:45:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:45:36,348 main INFO screen POW pass=0 dev=0.0 ins=16.38 pro=59 1a=False 1b=False 2=True (19.5s)
Sep 11 23:45:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:45:36,512 main INFO screen Milestones pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 23:46:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:08,694 main INFO screen CRISPE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 23:46:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:20,439 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:21,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:23,124 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:25,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:27,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:28,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:46:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:43,226 main INFO screen CCM pass=0 dev=0.0 ins=43.05 pro=59 1a=False 1b=False 2=True (22.9s)
Sep 11 23:46:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:45,945 main INFO screen GAKU pass=0 dev=6.63 ins=22.65 pro=38 1a=False 1b=False 2=True (22.9s)
Sep 11 23:46:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:48,687 main INFO screen imposter pass=0 dev=0.0 ins=18.76 pro=30 1a=False 1b=False 2=True (26.8s)
Sep 11 23:46:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:46:49,570 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.87 pro=19 1a=False 1b=False 2=True (6.3s)
Sep 11 23:47:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:47:11,671 main INFO screen $QAIS pass=0 dev=9.64 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 23:47:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:47:37,069 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:47:37 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T23:22:10Z
--- update 2026-09-11T23:27:17Z
--- update 2026-09-11T23:32:26Z
--- update 2026-09-11T23:37:30Z
--- update 2026-09-11T23:42:35Z
--- update 2026-09-11T23:47:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: b162cdb09d844c599f2691bd2f42382f
analyses gestart (8746aefc73b4)
```

## Analyses (laatste 25 regels)
```
active
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
23:47:36 18359 tokens sinds start volledige logging, waarvan 5134 met een gat door herstart
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
