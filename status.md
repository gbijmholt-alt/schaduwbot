# Schaduwbot status

- tijd: 2026-09-10 14:51:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 hour, 4 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 533/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 3803, "tokens_in_memory": 1411, "msgs": 591765, "trades": 120028, "creates": 1507, "decode_fail": 12574, "rpc_calls": 1896, "rpc_errors": 224, "sol_usd": 99.96582546667042, "open_positions": 83}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 14:48 UTC

Gelogde schaduwtrades: **891**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 1428 | 184 | 5 | 184 | 29 | 324 | 891 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 22 | 4% | 4.5% | +32.3% | -18.4% | -16.07% | 54% |
| dip35_V1_gescreend_fail | 82 | 24% | 7.3% | +41.1% | -32.9% | -14.85% | 95% |
| dip35_V1_alle | 106 | 22% | 6.6% | +39.9% | -29.2% | -14.22% | 97% |
| dip35_V2_gescreend_pass | 20 | 0% | 5.0% | +0.0% | -20.4% | -20.38% | 57% |
| dip35_V2_gescreend_fail | 75 | 24% | 8.0% | +49.9% | -37.1% | -16.25% | 95% |
| dip35_V2_alle | 97 | 20% | 7.2% | +47.8% | -32.5% | -16.75% | 98% |
| dip35_V3_gescreend_pass | 22 | 4% | 4.5% | +0.8% | -21.4% | -20.39% | 60% |
| dip35_V3_gescreend_fail | 85 | 13% | 10.6% | +18.2% | -36.5% | -29.42% | 100% |
| dip35_V3_alle | 108 | 12% | 9.3% | +16.3% | -33.2% | -27.21% | 100% |
| dip40_V1_gescreend_pass | 21 | 14% | 4.8% | +66.9% | -17.8% | -5.65% | 37% |
| dip40_V1_gescreend_fail | 80 | 22% | 8.7% | +43.5% | -31.5% | -14.66% | 93% |
| dip40_V1_alle | 103 | 22% | 7.8% | +45.5% | -28.4% | -11.92% | 94% |
| dip40_V2_gescreend_pass | 19 | 5% | 5.3% | +193.1% | -18.5% | -7.37% | 37% |
| dip40_V2_gescreend_fail | 72 | 21% | 9.7% | +48.3% | -36.3% | -18.69% | 96% |
| dip40_V2_alle | 93 | 18% | 8.6% | +54.6% | -31.7% | -15.96% | 97% |
| dip40_V3_gescreend_pass | 21 | 10% | 4.8% | +2.3% | -20.1% | -17.95% | 54% |
| dip40_V3_gescreend_fail | 84 | 16% | 10.7% | +17.3% | -36.1% | -27.82% | 99% |
| dip40_V3_alle | 106 | 15% | 9.4% | +15.0% | -32.7% | -25.50% | 100% |
| dip45_V1_gescreend_pass | 18 | 28% | 5.6% | +53.5% | -18.8% | +1.25% | 29% |
| dip45_V1_gescreend_fail | 75 | 23% | 6.7% | +39.1% | -31.0% | -15.11% | 93% |
| dip45_V1_alle | 95 | 25% | 6.3% | +41.5% | -28.8% | -11.01% | 92% |
| dip45_V2_gescreend_pass | 16 | 19% | 6.2% | +70.3% | -20.1% | -3.17% | 31% |
| dip45_V2_gescreend_fail | 68 | 24% | 8.8% | +46.8% | -34.4% | -15.29% | 92% |
| dip45_V2_alle | 86 | 23% | 8.1% | +48.5% | -31.2% | -12.67% | 93% |
| dip45_V3_gescreend_pass | 18 | 17% | 5.6% | +142.5% | -20.8% | +6.43% | 37% |
| dip45_V3_gescreend_fail | 78 | 19% | 9.0% | +42.3% | -34.3% | -19.60% | 97% |
| dip45_V3_alle | 97 | 20% | 8.2% | +56.4% | -31.7% | -14.46% | 97% |

## Beste variant: dip45_V1_alle

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 14:41:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:26,354 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:41:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:26,759 main INFO screen HOMO pass=0 dev=0.0 ins=18.21 pro=17 1a=False 1b=False 2=True (0.6s)
Sep 10 14:41:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:43,906 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:41:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:43,998 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:41:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:44,185 main INFO screen Bob pass=0 dev=0.0 ins=12.39 pro=24 1a=False 1b=False 2=True (0.4s)
Sep 10 14:42:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:05,963 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:42:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:06,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:42:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:06,292 main INFO screen BATON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:42:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:10,471 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:42:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:10,589 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:42:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:10,719 main INFO screen TCAT pass=0 dev=0.0 ins=79.24 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 14:42:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:15,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:16,113 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:16,510 main INFO screen Nasduck pass=0 dev=0.0 ins=18.4 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 10 14:42:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:24,343 main INFO screen Nasduck pass=1 dev=0.0 ins=4.97 pro=14 1a=False 1b=False 2=False (3.2s)
Sep 10 14:42:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:33,337 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:42:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:33,464 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:42:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:33,687 main INFO screen GROKCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:42:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:49,240 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:42:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:49,331 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:42:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:42:49,682 main INFO screen KYA pass=0 dev=0.0 ins=14.34 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 14:43:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:21,471 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:43:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:21,561 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:43:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:21,744 main INFO screen KYA pass=0 dev=0.0 ins=39.77 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 14:43:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:22,074 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:43:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:22,371 main INFO screen scar pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 14:43:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:37,910 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:43:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:38,024 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:43:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:38,208 main INFO screen IPHONEPDM pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 10 14:43:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:43,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:43:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:43,521 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:43:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:49,627 main INFO screen FIX6900 pass=1 dev=0.0 ins=13.98 pro=14 1a=False 1b=False 2=False (6.3s)
Sep 10 14:43:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:58,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:43:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:58,522 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:43:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:43:58,650 main INFO screen PENPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:44:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:25,357 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:44:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:25,418 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:44:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:25,648 main INFO screen UPS pass=0 dev=0.0 ins=12.5 pro=39 1a=False 1b=False 2=True (0.4s)
Sep 10 14:44:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:52,712 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:44:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:52,806 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:44:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:44:53,005 main INFO screen cash cat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 14:45:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:45:19,133 main INFO screen TRADE pass=0 dev=0.0 ins=25.57 pro=21 1a=False 1b=False 2=False (1.8s)
Sep 10 14:45:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:45:41,050 main INFO screen cash cat pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 10 14:46:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:06,761 main INFO screen CHAROC pass=0 dev=4.44 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 10 14:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:27,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:27,415 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:27,790 main INFO screen Simple pass=0 dev=0.0 ins=7.75 pro=11 1a=False 1b=False 2=True (0.6s)
Sep 10 14:46:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:37,393 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:46:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 14:46:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:46:58,823 main INFO screen WC pass=0 dev=0.5 ins=0.0 pro=7 1a=False 1b=False 2=False (3.8s)
Sep 10 14:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:05,353 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:05,423 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:47:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:11,212 main INFO screen Shrek pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 14:47:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:11,393 main INFO screen CATESEM pass=0 dev=0.0 ins=32.33 pro=8 1a=False 1b=False 2=True (6.1s)
Sep 10 14:47:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:17,868 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:47:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:17,957 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:47:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:18,097 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:47:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:19,391 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:47:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:19,519 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:47:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:47:23,412 main INFO screen FDA pass=0 dev=0.0 ins=17.13 pro=25 1a=False 1b=False 2=True (4.1s)
Sep 10 14:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:17,473 main INFO screen Faggor pass=1 dev=0.0 ins=0.51 pro=30 1a=False 1b=False 2=False (3.9s)
Sep 10 14:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:17,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:48:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:18,093 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:48:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:18,552 main INFO screen FIX6900 pass=0 dev=0.0 ins=8.62 pro=10 1a=False 1b=False 2=True (0.7s)
Sep 10 14:48:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:37,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:48:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:37,692 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:48:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:38,258 main INFO screen solly pass=0 dev=0.0 ins=22.66 pro=12 1a=False 1b=False 2=True (1.8s)
Sep 10 14:48:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:48:39,657 main INFO screen WC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 10 14:50:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:18,895 main INFO screen BUCKAZOID pass=1 dev=0.0 ins=19.58 pro=25 1a=False 1b=False 2=False (2.4s)
Sep 10 14:50:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:36,414 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:50:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:36,506 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:50:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:36,699 main INFO screen CATESEM pass=0 dev=0.0 ins=32.01 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 10 14:50:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:44,630 aiohttp.access INFO 189.18.97.61 [10/Sep/2026:14:50:44 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 10 14:50:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:50:51,759 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 10 14:51:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:32,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:51:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:32,960 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:33,160 main INFO screen The CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:51:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:38,905 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:51:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:39,036 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:51:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:39,155 main INFO screen 1 A.K. pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 14:51:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:51:40,283 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:51:40 +0000] "GET /health HTTP/1.1" 200 423 "-" "Python-urllib/3.14"
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
