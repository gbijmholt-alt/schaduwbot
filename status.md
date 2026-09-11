# Schaduwbot status

- tijd: 2026-09-11 22:14:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 8 hours, 27 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 766/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 9247, "tokens_in_memory": 3469, "msgs": 2176123, "trades": 401032, "creates": 3469, "decode_fail": 27231, "rpc_calls": 12741, "rpc_errors": 502, "sol_usd": 102.13582398737432, "open_positions": 134, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 21:40 UTC

Gelogde schaduwtrades: **33418**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 25144 | 3869 | 41 | 3866 | 323 | 7170 | 21063 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 392 | 17% | 2.0% | +43.1% | -17.1% | -6.97% | 100% |
| dip35_V1_gescreend_fail | 3269 | 27% | 3.7% | +46.2% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 3872 | 26% | 3.7% | +45.1% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 386 | 21% | 3.1% | +43.9% | -21.8% | -8.06% | 100% |
| dip35_V2_gescreend_fail | 3272 | 25% | 4.3% | +56.7% | -28.3% | -7.31% | 100% |
| dip35_V2_alle | 3828 | 24% | 4.3% | +54.6% | -27.9% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 388 | 8% | 3.6% | +374.3% | -23.1% | +8.68% | 100% |
| dip35_V3_gescreend_fail | 3339 | 13% | 5.9% | +119.3% | -29.8% | -9.88% | 100% |
| dip35_V3_alle | 3878 | 13% | 5.8% | +129.9% | -29.3% | -8.55% | 100% |
| dip40_V1_gescreend_pass | 362 | 15% | 1.9% | +46.6% | -16.2% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 3194 | 26% | 3.7% | +48.0% | -26.0% | -6.60% | 100% |
| dip40_V1_alle | 3721 | 25% | 3.6% | +47.7% | -25.2% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 356 | 16% | 2.5% | +48.9% | -20.4% | -9.09% | 100% |
| dip40_V2_gescreend_fail | 3185 | 25% | 4.2% | +56.0% | -28.2% | -7.32% | 100% |
| dip40_V2_alle | 3670 | 24% | 4.2% | +55.0% | -27.7% | -7.90% | 100% |
| dip40_V3_gescreend_pass | 361 | 7% | 2.8% | +423.8% | -21.4% | +8.19% | 100% |
| dip40_V3_gescreend_fail | 3251 | 13% | 5.7% | +113.9% | -29.6% | -11.00% | 100% |
| dip40_V3_alle | 3725 | 12% | 5.5% | +126.8% | -29.0% | -9.66% | 100% |
| dip45_V1_gescreend_pass | 348 | 16% | 1.7% | +50.0% | -16.0% | -5.37% | 99% |
| dip45_V1_gescreend_fail | 3112 | 27% | 3.2% | +48.6% | -25.7% | -5.39% | 100% |
| dip45_V1_alle | 3593 | 26% | 3.2% | +48.6% | -25.0% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 340 | 19% | 2.4% | +47.9% | -20.1% | -7.29% | 100% |
| dip45_V2_gescreend_fail | 3095 | 25% | 3.8% | +58.7% | -27.9% | -6.12% | 100% |
| dip45_V2_alle | 3543 | 24% | 3.8% | +57.4% | -27.3% | -6.72% | 100% |
| dip45_V3_gescreend_pass | 343 | 7% | 2.3% | +467.9% | -20.6% | +13.58% | 100% |
| dip45_V3_gescreend_fail | 3150 | 14% | 5.3% | +120.8% | -29.1% | -8.30% | 100% |
| dip45_V3_alle | 3588 | 13% | 5.2% | +136.3% | -28.5% | -6.77% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 1.1%, kans ruïne 98.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2548 | 13% | 3.2% | -10.54% | 100% |
| zonder_xlink | 728 | 19% | 0.0% | +30.12% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 22:01:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:38,961 main INFO screen 67Stunk pass=0 dev=0.14 ins=79.17 pro=6 1a=False 1b=True 2=True (25.0s)
Sep 11 22:01:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:43,866 main INFO screen BLUECHIP pass=0 dev=0.0 ins=36.72 pro=13 1a=False 1b=False 2=True (13.9s)
Sep 11 22:01:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:44,445 main INFO screen GA pass=1 dev=0.0 ins=12.08 pro=22 1a=False 1b=False 2=False (5.9s)
Sep 11 22:01:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:44,790 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:22:01:44 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 22:01:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:48,599 main INFO screen KTW pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 11 22:01:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:01:56,719 main INFO screen IN pass=1 dev=1.05 ins=6.5 pro=38 1a=False 1b=False 2=False (9.4s)
Sep 11 22:02:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:02:01,127 main INFO screen Rich pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (13.2s)
Sep 11 22:02:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:02:03,421 main INFO screen ALLFLY pass=0 dev=3.42 ins=0.0 pro=36 1a=False 1b=False 2=True (11.5s)
Sep 11 22:02:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:02:14,703 main INFO screen att pass=0 dev=0.57 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 11 22:02:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:02:16,786 main INFO screen $CAJUN pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 22:02:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:02:23,543 main INFO screen PEARL pass=1 dev=0.0 ins=11.16 pro=19 1a=False 1b=False 2=False (6.1s)
Sep 11 22:03:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:37,134 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:03:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 22:03:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:41,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:03:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:46,118 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:03:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:46,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:03:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:48,829 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:03:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:58,834 main INFO screen BLUECHIP pass=0 dev=0.0 ins=36.66 pro=8 1a=False 1b=False 2=True (12.8s)
Sep 11 22:03:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:59,379 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:03:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:03:59,738 main INFO screen ACH pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (11.0s)
Sep 11 22:04:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:04:05,055 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.9s)
Sep 11 22:04:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:04:11,459 main INFO screen ECTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (12.6s)
Sep 11 22:04:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:04:38,540 main INFO screen BANANA67 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 22:04:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:04:42,828 main INFO screen flyonfone pass=0 dev=0.0 ins=27.49 pro=19 1a=False 1b=False 2=False (8.2s)
Sep 11 22:04:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:04:48,484 main INFO screen WCOI pass=0 dev=1.57 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 22:05:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:04,669 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:05:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:09,740 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:05:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:20,421 main INFO screen BALLIN pass=0 dev=0.88 ins=0.0 pro=58 1a=False 1b=False 2=False (8.0s)
Sep 11 22:05:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:26,426 main INFO screen RUPIO pass=0 dev=0.18 ins=79.13 pro=6 1a=False 1b=True 2=True (21.8s)
Sep 11 22:05:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:36,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:05:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:41,858 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:05:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:43,728 main INFO screen cash cat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 22:05:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:46,986 main INFO screen ANIMAL pass=1 dev=0.01 ins=0.0 pro=41 1a=False 1b=False 2=False (8.1s)
Sep 11 22:05:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:53,221 main INFO screen JEWBUZZ pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (9.5s)
Sep 11 22:05:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:53,292 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:05:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:05:56,456 main INFO screen Cybercab pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.5s)
Sep 11 22:06:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:01,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:06:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:03,093 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.6s)
Sep 11 22:06:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:07,317 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (14.1s)
Sep 11 22:06:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:11,914 main INFO screen SOLSHEEP pass=1 dev=0.0 ins=6.42 pro=16 1a=False 1b=False 2=False (8.5s)
Sep 11 22:06:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:15,693 main INFO screen DOOYET pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=True (14.3s)
Sep 11 22:06:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:25,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:06:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:40,370 main INFO screen PUMPDOG pass=0 dev=0.0 ins=22.4 pro=59 1a=False 1b=False 2=True (14.6s)
Sep 11 22:06:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:41,824 main INFO screen MILKY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (11.3s)
Sep 11 22:06:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:06:57,888 main INFO screen $CAJUN pass=0 dev=0.74 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 11 22:08:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:06,033 main INFO screen gambling  pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (5.9s)
Sep 11 22:08:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:35,775 main INFO screen Rich pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 11 22:08:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:36,355 main INFO screen DUVAL pass=0 dev=0.0 ins=18.92 pro=34 1a=False 1b=False 2=True (10.1s)
Sep 11 22:08:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:43,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:08:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:50,146 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:08:50 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 22:08:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:08:56,965 main INFO screen USWAY pass=0 dev=1.07 ins=0.0 pro=4 1a=False 1b=False 2=False (14.0s)
Sep 11 22:09:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:09:05,475 main INFO screen ACH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 11 22:09:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:09:06,006 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:09:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:09:11,080 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:09:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:09:29,999 main INFO screen FlyEleven pass=0 dev=0.0 ins=36.03 pro=23 1a=False 1b=False 2=True (24.1s)
Sep 11 22:09:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:09:52,773 main INFO screen Catfish pass=0 dev=5.05 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 22:10:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:10:17,557 main INFO screen DOGE pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=True (8.8s)
Sep 11 22:10:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:10:43,377 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:10:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:10:48,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:11:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:00,905 main INFO screen CHILLSTONK pass=1 dev=3.17 ins=0.0 pro=24 1a=False 1b=False 2=False (9.3s)
Sep 11 22:11:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:06,008 main INFO screen FlyEleven pass=0 dev=0.0 ins=36.03 pro=17 1a=True 1b=True 2=True (22.7s)
Sep 11 22:11:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:22,247 main INFO screen TripleD pass=1 dev=0.0 ins=10.32 pro=17 1a=False 1b=False 2=False (6.7s)
Sep 11 22:11:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:25,049 main INFO screen BIGSPIN pass=0 dev=2.14 ins=1.01 pro=32 1a=False 1b=False 2=True (7.7s)
Sep 11 22:11:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:36,817 main INFO screen HEAVYBALLS pass=1 dev=0.0 ins=0.72 pro=33 1a=False 1b=False 2=False (9.6s)
Sep 11 22:11:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:48,709 main INFO screen CRISPE pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 11 22:11:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:53,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:11:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:11:57,222 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 11 22:12:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:12:02,478 main INFO screen Gary pass=0 dev=0.0 ins=18.01 pro=44 1a=False 1b=False 2=True (9.0s)
Sep 11 22:12:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:12:44,942 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:12:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:12:46,745 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:12:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:12:50,009 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:12:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:12:51,814 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:13:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:04,336 main INFO screen STONK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.5s)
Sep 11 22:13:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:13,502 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.8s)
Sep 11 22:13:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:16,365 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:13:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:21,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:13:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:33,837 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:13:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:38,910 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:13:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:42,449 main INFO screen CFD pass=0 dev=0.0 ins=17.13 pro=30 1a=False 1b=False 2=True (26.2s)
Sep 11 22:13:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:13:58,628 main INFO screen OpenClaw pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (25.0s)
Sep 11 22:14:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:14:15,879 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:14:15 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T20:45:33Z
--- update 2026-09-11T20:50:36Z
--- update 2026-09-11T20:55:37Z
--- update 2026-09-11T21:00:40Z
--- update 2026-09-11T21:05:43Z
--- update 2026-09-11T21:11:05Z
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
--- update 2026-09-11T21:42:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
--- update 2026-09-11T21:47:46Z
--- update 2026-09-11T21:53:06Z
--- update 2026-09-11T21:58:16Z
--- update 2026-09-11T22:03:36Z
--- update 2026-09-11T22:08:49Z
--- update 2026-09-11T22:14:14Z
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
