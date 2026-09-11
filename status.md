# Schaduwbot status

- tijd: 2026-09-11 18:06:41 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 4 hours, 19 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.7G/38G | geheugen: 927/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 29817, "tokens_in_memory": 7553, "msgs": 3683573, "trades": 893187, "creates": 9596, "decode_fail": 66607, "rpc_calls": 16866, "rpc_errors": 1442, "sol_usd": 100.85733520167157, "open_positions": 114, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 17:49 UTC

Gelogde schaduwtrades: **28037**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 20025 | 2920 | 31 | 2920 | 211 | 5313 | 15682 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 309 | 16% | 1.9% | +42.2% | -16.3% | -6.68% | 99% |
| dip35_V1_gescreend_fail | 2833 | 27% | 3.7% | +46.2% | -25.9% | -6.51% | 100% |
| dip35_V1_alle | 3241 | 26% | 3.8% | +45.5% | -25.2% | -6.75% | 100% |
| dip35_V2_gescreend_pass | 308 | 19% | 2.6% | +45.8% | -21.3% | -8.47% | 100% |
| dip35_V2_gescreend_fail | 2837 | 25% | 4.4% | +56.3% | -28.2% | -7.39% | 100% |
| dip35_V2_alle | 3218 | 24% | 4.4% | +54.9% | -27.8% | -7.91% | 100% |
| dip35_V3_gescreend_pass | 309 | 8% | 2.9% | +121.7% | -22.8% | -11.55% | 100% |
| dip35_V3_gescreend_fail | 2876 | 13% | 6.1% | +104.3% | -29.8% | -11.99% | 100% |
| dip35_V3_alle | 3253 | 13% | 6.0% | +102.8% | -29.3% | -12.30% | 100% |
| dip40_V1_gescreend_pass | 285 | 15% | 1.8% | +47.6% | -15.5% | -6.19% | 99% |
| dip40_V1_gescreend_fail | 2752 | 26% | 3.7% | +48.0% | -25.9% | -6.42% | 100% |
| dip40_V1_alle | 3115 | 26% | 3.7% | +47.7% | -25.1% | -6.54% | 100% |
| dip40_V2_gescreend_pass | 284 | 14% | 2.5% | +52.7% | -19.9% | -9.45% | 100% |
| dip40_V2_gescreend_fail | 2749 | 25% | 4.1% | +55.2% | -28.1% | -7.53% | 100% |
| dip40_V2_alle | 3089 | 24% | 4.2% | +54.8% | -27.5% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 286 | 7% | 2.4% | +100.2% | -21.2% | -13.13% | 100% |
| dip40_V3_gescreend_fail | 2787 | 13% | 5.8% | +91.9% | -29.6% | -13.93% | 100% |
| dip40_V3_alle | 3125 | 12% | 5.7% | +90.9% | -29.0% | -14.17% | 100% |
| dip45_V1_gescreend_pass | 272 | 15% | 1.5% | +53.0% | -15.1% | -4.61% | 98% |
| dip45_V1_gescreend_fail | 2680 | 27% | 3.3% | +49.4% | -25.6% | -5.24% | 100% |
| dip45_V1_alle | 3009 | 26% | 3.3% | +49.4% | -24.8% | -5.40% | 100% |
| dip45_V2_gescreend_pass | 270 | 18% | 2.2% | +50.5% | -19.3% | -6.88% | 99% |
| dip45_V2_gescreend_fail | 2664 | 25% | 3.8% | +58.9% | -27.6% | -6.26% | 100% |
| dip45_V2_alle | 2979 | 24% | 3.8% | +58.1% | -27.0% | -6.68% | 100% |
| dip45_V3_gescreend_pass | 272 | 7% | 2.2% | +155.9% | -20.3% | -7.98% | 100% |
| dip45_V3_gescreend_fail | 2695 | 14% | 5.5% | +105.2% | -29.1% | -10.75% | 100% |
| dip45_V3_alle | 3008 | 13% | 5.4% | +106.2% | -28.5% | -10.79% | 100% |

## Beste variant: dip45_V1_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2058 | 13% | 2.8% | -9.55% | 100% |
| zonder_xlink | 537 | 16% | 0.0% | -3.85% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 17:56:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:07,465 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:56:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:07,571 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:56:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:07,746 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 17:56:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:16,943 main INFO screen Fortsol pass=0 dev=26.58 ins=0.0 pro=21 1a=False 1b=False 2=False (2.5s)
Sep 11 17:56:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:17,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:56:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:17,713 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:56:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:17,839 main INFO screen Puter pass=0 dev=0.0 ins=20.56 pro=8 1a=False 1b=False 2=False (0.3s)
Sep 11 17:56:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:41,137 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:56:41 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 17:56:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:56:57,953 main INFO screen TRUMP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 11 17:57:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:57:56,970 main INFO screen NeverKirk pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 11 17:57:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:57:57,181 main INFO screen cat pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 17:58:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:17,263 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:58:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:17,365 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:58:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:17,579 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (0.4s)
Sep 11 17:58:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:26,141 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:58:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:26,267 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:58:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:26,409 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 17:58:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:38,469 main INFO screen PUMPSTOCK pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 11 17:58:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:52,514 aiohttp.access INFO 122.42.210.59 [11/Sep/2026:17:58:52 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 17:58:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:58,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:58:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:58:59,078 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:59:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:01,161 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.3s)
Sep 11 17:59:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:21,679 main INFO screen JABIK pass=0 dev=0.12 ins=0.0 pro=3 1a=False 1b=False 2=False (4.0s)
Sep 11 17:59:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:45,057 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:59:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:45,154 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:59:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:45,351 main INFO screen CHAD pass=1 dev=0.0 ins=2.85 pro=21 1a=False 1b=False 2=False (0.4s)
Sep 11 17:59:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:59:58,770 main INFO screen stocklana pass=0 dev=0.71 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 18:00:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:06,298 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:00:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:06,473 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:00:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:13,387 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.1s)
Sep 11 18:00:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:13,580 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:00:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:13,868 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:00:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:15,602 main INFO screen FORTSOL pass=0 dev=0.0 ins=47.11 pro=7 1a=False 1b=False 2=True (2.2s)
Sep 11 18:00:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:18,074 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.8s)
Sep 11 18:00:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:18,116 main INFO screen Trumpthis2 pass=0 dev=0.97 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 11 18:00:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:35,115 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:00:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:35,240 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:00:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:40,569 main INFO screen HEROBRINE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.6s)
Sep 11 18:00:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:00:59,311 main INFO screen Bricko pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 11 18:01:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:03,452 main INFO screen Pump pass=0 dev=0.0 ins=11.58 pro=29 1a=False 1b=False 2=True (6.6s)
Sep 11 18:01:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:05,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:01:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:06,091 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:01:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:10,849 main INFO screen Pump pass=1 dev=0.0 ins=2.46 pro=27 1a=False 1b=False 2=False (5.0s)
Sep 11 18:01:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:12,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:01:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:13,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:01:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:13,150 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:01:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:18,350 main INFO screen SEASONED pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 11 18:01:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:19,091 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 11 18:01:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:41,501 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:01:41 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 18:01:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:01:51,857 main INFO screen PEPE pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=True (9.0s)
Sep 11 18:02:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:31,829 main INFO screen vrl pass=0 dev=4.57 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 11 18:02:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:33,956 main INFO screen PUMPSTOCK pass=0 dev=0.36 ins=0.0 pro=1 1a=False 1b=False 2=False (11.1s)
Sep 11 18:02:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:40,050 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:02:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:40,214 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:02:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:40,404 main INFO screen harold pass=0 dev=0.0 ins=28.29 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 18:02:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:02:55,063 main INFO screen $PISS pass=0 dev=1.04 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 11 18:03:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:03:04,928 main INFO screen DOOYET pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=True (9.0s)
Sep 11 18:03:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:03:05,463 main INFO screen Kakas pass=0 dev=0.52 ins=0.0 pro=2 1a=False 1b=False 2=False (10.6s)
Sep 11 18:03:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:03:14,472 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 18:03:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:03:24,373 main INFO screen TRUMP pass=1 dev=1.83 ins=2.81 pro=66 1a=False 1b=False 2=False (9.3s)
Sep 11 18:03:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:03:31,141 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:18:03:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 18:04:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:13,225 main INFO screen $TRUMPCASH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.9s)
Sep 11 18:04:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:15,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:04:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:15,504 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:04:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:21,739 main INFO screen CDOG pass=1 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (6.4s)
Sep 11 18:04:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:31,714 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:04:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:31,833 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:04:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:32,915 main INFO screen harold pass=0 dev=0.0 ins=14.85 pro=17 1a=False 1b=False 2=True (1.3s)
Sep 11 18:04:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:34,693 main INFO screen CLICKBAIT pass=1 dev=3.06 ins=9.55 pro=54 1a=False 1b=False 2=False (8.5s)
Sep 11 18:04:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:04:43,079 main INFO screen APPLECAT pass=0 dev=0.81 ins=0.0 pro=3 1a=False 1b=False 2=False (10.8s)
Sep 11 18:05:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:05:07,390 main INFO screen $GOAT pass=0 dev=4.56 ins=0.0 pro=6 1a=False 1b=False 2=False (7.8s)
Sep 11 18:05:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:05:16,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:05:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:05:16,777 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:05:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:05:21,207 main INFO screen JABIK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 11 18:05:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:05:51,981 main INFO screen ACI pass=1 dev=0.0 ins=13.53 pro=61 1a=False 1b=False 2=False (7.1s)
Sep 11 18:06:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:06:05,861 main INFO screen 1UP pass=1 dev=0.0 ins=0.77 pro=67 1a=False 1b=False 2=False (10.3s)
Sep 11 18:06:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:06:10,004 main INFO screen $CAJUN pass=0 dev=1.44 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 11 18:06:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:06:26,852 main INFO screen NeverKirk pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 11 18:06:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:06:28,718 main INFO screen MEBT pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (7.4s)
Sep 11 18:06:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:06:41,763 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:06:41 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T16:40:09Z
--- update 2026-09-11T16:45:19Z
--- update 2026-09-11T16:50:30Z
--- update 2026-09-11T16:55:36Z
--- update 2026-09-11T17:00:58Z
--- update 2026-09-11T17:06:10Z
--- update 2026-09-11T17:11:21Z
--- update 2026-09-11T17:16:23Z
--- update 2026-09-11T17:21:29Z
--- update 2026-09-11T17:26:32Z
--- update 2026-09-11T17:31:32Z
--- update 2026-09-11T17:36:36Z
--- update 2026-09-11T17:41:37Z
--- update 2026-09-11T17:46:37Z
--- update 2026-09-11T17:51:39Z
--- update 2026-09-11T17:56:40Z
--- update 2026-09-11T18:01:40Z
--- update 2026-09-11T18:06:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: f4240d03c1404a3aa0fe2959269b0656
analyses gestart (8213ec5e675e)
```

## Analyses (laatste 25 regels)
```
active
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
16:03:36 7475 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
16:03:40   ingelezen tot rowid 1652718 (200000 rijen, 200000 bruikbaar)
16:03:41   ingelezen tot rowid 1684078 (231360 rijen, 231360 bruikbaar)
16:03:41 ingelezen: 231360 nieuwe trades, 231360 bruikbaar (4s)
16:03:46 klaar in 10s -> /opt/schaduwbot/reports/ledger.md
16:03:48   2000 nieuwe tokens doorgerekend
16:03:48 klaar in 2s: 3448 tokens, 2089 nieuw -> /opt/schaduwbot/reports/video_replay.md
16:03:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 16:03 UTC
16:03:48 32317 tokens geladen
16:03:51   2000 tokens, 318886 trades, 83589 posities (3s)
16:03:54   4000 tokens, 653328 trades, 170937 posities (6s)
16:03:57   6000 tokens, 953319 trades, 248089 posities (9s)
16:04:01   8000 tokens, 1282543 trades, 335538 posities (13s)
16:04:05   10000 tokens, 1602875 trades, 422034 posities (16s)
16:04:06 posities: 447031 uit 1684507 trades (17s)
16:04:12 104760 wallets gerekend
16:04:12 geluk-toets
16:04:29 persistentie
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
18:06:41 10533 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
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
