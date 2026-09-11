# Schaduwbot status

- tijd: 2026-09-11 21:58:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 8 hours, 11 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 735/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 8289, "tokens_in_memory": 3028, "msgs": 1888152, "trades": 356443, "creates": 3028, "decode_fail": 25530, "rpc_calls": 11265, "rpc_errors": 459, "sol_usd": 102.11765459718436, "open_positions": 129, "log_all_trades": true}
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
Sep 11 21:49:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:03,659 main INFO screen wind pass=0 dev=0.6 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 11 21:49:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:04,266 main INFO screen cash cat pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.2s)
Sep 11 21:49:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:06,778 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:49:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:18,507 main INFO screen STONKANSEM pass=1 dev=0.0 ins=12.46 pro=14 1a=False 1b=False 2=False (2.9s)
Sep 11 21:49:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:22,565 main INFO screen DOG pass=0 dev=0.0 ins=15.88 pro=72 1a=False 1b=False 2=True (21.0s)
Sep 11 21:49:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:25,650 aiohttp.access INFO 91.230.168.182 [11/Sep/2026:21:49:25 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 21:49:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:31,745 aiohttp.access INFO 91.230.168.180 [11/Sep/2026:21:49:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0"
Sep 11 21:49:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:36,651 main INFO screen download pass=1 dev=0.0 ins=2.07 pro=54 1a=False 1b=False 2=False (3.0s)
Sep 11 21:49:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:37,469 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:49:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:43,899 main INFO screen WCOI pass=0 dev=1.57 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 11 21:49:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:49:45,151 main INFO screen bruh pass=0 dev=0.6 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 11 21:50:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:16,513 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:19,487 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:21,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:27,772 main INFO screen Clanker pass=0 dev=0.0 ins=21.19 pro=65 1a=False 1b=False 2=True (8.4s)
Sep 11 21:50:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:31,840 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:34,545 main INFO screen want rich pass=0 dev=0.31 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 21:50:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:36,901 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:37,108 main INFO screen VOLBAN pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (20.7s)
Sep 11 21:50:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:43,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:43,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:48,790 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:48,943 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:50:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:51,925 main INFO screen CCM pass=0 dev=0.0 ins=17.0 pro=76 1a=False 1b=False 2=True (20.2s)
Sep 11 21:50:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:50:55,991 main INFO screen BABYALL pass=1 dev=0.04 ins=0.0 pro=36 1a=False 1b=False 2=False (2.7s)
Sep 11 21:51:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:05,855 main INFO screen Rainbow pass=0 dev=98.85 ins=0.0 pro=1 1a=False 1b=False 2=True (22.2s)
Sep 11 21:51:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:06,279 main INFO screen NVIDALL pass=0 dev=0.35 ins=0.0 pro=66 1a=False 1b=False 2=True (22.5s)
Sep 11 21:51:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:16,416 main INFO screen Milly pass=0 dev=0.0 ins=17.36 pro=21 1a=False 1b=True 2=True (1.2s)
Sep 11 21:51:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:39,801 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:51:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:41,549 main INFO screen ALLFLY pass=1 dev=0.88 ins=9.64 pro=31 1a=False 1b=False 2=False (3.3s)
Sep 11 21:51:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:44,871 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:51:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:57,614 main INFO screen NOTALL pass=0 dev=33.79 ins=0.0 pro=6 1a=False 1b=False 2=True (3.5s)
Sep 11 21:51:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:51:58,063 main INFO screen SLABY pass=0 dev=0.0 ins=79.31 pro=5 1a=False 1b=True 2=True (18.7s)
Sep 11 21:52:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:08,635 main INFO screen FLYBULL pass=0 dev=0.0 ins=35.27 pro=17 1a=False 1b=False 2=True (3.2s)
Sep 11 21:52:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:14,378 main INFO screen 1 pass=1 dev=0.0 ins=11.46 pro=48 1a=False 1b=False 2=False (1.3s)
Sep 11 21:52:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:19,406 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:52:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:24,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:52:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:28,943 main INFO screen cash cat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 21:52:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:30,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:52:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:40,468 main INFO screen att pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (10.0s)
Sep 11 21:52:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:43,459 main INFO screen Tokabu pass=0 dev=0.0 ins=19.16 pro=79 1a=False 1b=False 2=True (24.1s)
Sep 11 21:52:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:52:49,702 main INFO screen COCA-COLA pass=0 dev=0.02 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 11 21:53:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:07,076 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:53:07 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 21:53:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:17,508 main INFO screen cap pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (3.6s)
Sep 11 21:53:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:41,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:53:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:46,443 main INFO screen jew pass=1 dev=0.0 ins=10.55 pro=22 1a=False 1b=False 2=False (2.5s)
Sep 11 21:53:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:46,667 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:53:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:54,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:53:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:53:55,407 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:54:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:00,858 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:54:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:02,417 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.9s)
Sep 11 21:54:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:03,527 main INFO screen 5neegy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.8s)
Sep 11 21:54:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:06,049 main INFO screen SNOOPY pass=0 dev=0.23 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 21:54:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:07,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:54:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:15,145 main INFO screen cap pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (8.0s)
Sep 11 21:54:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:16,205 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (20.9s)
Sep 11 21:54:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:32,945 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:54:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:38,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:54:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:54:52,944 main INFO screen frens pass=0 dev=0.0 ins=22.44 pro=32 1a=False 1b=False 2=True (20.1s)
Sep 11 21:55:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:08,907 main INFO screen 9/11 pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 21:55:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:23,912 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:55:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:24,865 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:55:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:33,794 main INFO screen CRACKED pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (10.0s)
Sep 11 21:55:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:36,028 main INFO screen BEG pass=0 dev=0.18 ins=0.0 pro=55 1a=False 1b=False 2=True (11.2s)
Sep 11 21:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:55:37,000 main INFO screen $CAT pass=0 dev=0.19 ins=0.0 pro=1 1a=False 1b=False 2=False (3.9s)
Sep 11 21:56:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:00,832 main INFO screen $CAJUN pass=0 dev=0.4 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 21:56:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:17,982 main INFO screen ch pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 21:56:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:29,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:56:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:36,224 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 11 21:56:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:38,151 main INFO screen $GOAT pass=0 dev=0.56 ins=0.0 pro=2 1a=False 1b=False 2=True (5.0s)
Sep 11 21:56:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:44,152 main INFO screen Caviar pass=0 dev=0.0 ins=17.97 pro=63 1a=False 1b=False 2=True (14.5s)
Sep 11 21:56:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:45,795 main INFO screen Whatever pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (8.3s)
Sep 11 21:56:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:56:57,015 main INFO screen ORANG pass=0 dev=0.0 ins=19.39 pro=45 1a=False 1b=False 2=True (3.9s)
Sep 11 21:57:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:57:14,274 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:57:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:57:22,922 main INFO screen SILVERBACK pass=0 dev=0.0 ins=9.69 pro=60 1a=False 1b=False 2=True (8.7s)
Sep 11 21:57:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:57:27,634 main INFO screen BUSH pass=0 dev=1.31 ins=25.27 pro=65 1a=False 1b=False 2=True (5.4s)
Sep 11 21:57:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:57:30,781 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 11 21:58:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:58:01,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:58:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:58:06,963 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:58:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:58:17,598 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:58:17 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T20:30:28Z
--- update 2026-09-11T20:35:28Z
--- update 2026-09-11T20:40:31Z
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
