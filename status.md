# Schaduwbot status

- tijd: 2026-09-12 02:02:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 12 hours, 15 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.2G/38G | geheugen: 1053/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 22934, "tokens_in_memory": 7896, "msgs": 4805082, "trades": 898999, "creates": 8385, "decode_fail": 48928, "rpc_calls": 30385, "rpc_errors": 1201, "sol_usd": 102.03369718444894, "open_positions": 84, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **38446**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 2011 | 344 | 0 | 344 | 21 | 634 | 1890 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 438 | 17% | 2.3% | +44.5% | -17.0% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 3678 | 27% | 3.7% | +45.6% | -25.9% | -6.85% | 100% |
| dip35_V1_alle | 4446 | 26% | 3.8% | +44.8% | -25.3% | -6.90% | 100% |
| dip35_V2_gescreend_pass | 435 | 22% | 3.2% | +44.2% | -21.6% | -7.21% | 100% |
| dip35_V2_gescreend_fail | 3702 | 25% | 4.3% | +56.4% | -28.1% | -7.23% | 100% |
| dip35_V2_alle | 4408 | 24% | 4.4% | +54.1% | -27.7% | -7.78% | 100% |
| dip35_V3_gescreend_pass | 438 | 8% | 3.7% | +331.7% | -22.8% | +7.15% | 100% |
| dip35_V3_gescreend_fail | 3785 | 13% | 5.9% | +117.9% | -29.7% | -9.94% | 100% |
| dip35_V3_alle | 4464 | 13% | 5.9% | +124.9% | -29.2% | -9.01% | 100% |
| dip40_V1_gescreend_pass | 409 | 15% | 2.4% | +47.3% | -16.3% | -6.81% | 100% |
| dip40_V1_gescreend_fail | 3609 | 26% | 3.8% | +47.4% | -25.9% | -6.72% | 100% |
| dip40_V1_alle | 4271 | 25% | 3.8% | +47.4% | -25.1% | -6.74% | 100% |
| dip40_V2_gescreend_pass | 406 | 18% | 3.0% | +47.1% | -20.2% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 3612 | 25% | 4.3% | +55.5% | -28.1% | -7.39% | 100% |
| dip40_V2_alle | 4224 | 24% | 4.4% | +54.0% | -27.5% | -7.99% | 100% |
| dip40_V3_gescreend_pass | 410 | 7% | 3.2% | +343.8% | -21.4% | +5.30% | 100% |
| dip40_V3_gescreend_fail | 3693 | 13% | 5.9% | +114.9% | -29.5% | -10.70% | 100% |
| dip40_V3_alle | 4285 | 13% | 5.8% | +122.5% | -29.0% | -9.82% | 100% |
| dip45_V1_gescreend_pass | 393 | 16% | 2.3% | +48.8% | -16.2% | -5.79% | 100% |
| dip45_V1_gescreend_fail | 3526 | 27% | 3.3% | +47.9% | -25.6% | -5.54% | 100% |
| dip45_V1_alle | 4129 | 26% | 3.4% | +48.1% | -24.9% | -5.76% | 100% |
| dip45_V2_gescreend_pass | 389 | 19% | 2.8% | +46.0% | -20.1% | -7.37% | 100% |
| dip45_V2_gescreend_fail | 3520 | 25% | 3.9% | +58.0% | -27.6% | -6.24% | 100% |
| dip45_V2_alle | 4083 | 24% | 4.0% | +56.2% | -27.2% | -6.91% | 100% |
| dip45_V3_gescreend_pass | 393 | 7% | 2.8% | +392.1% | -20.8% | +9.71% | 100% |
| dip45_V3_gescreend_fail | 3589 | 14% | 5.5% | +121.6% | -29.0% | -8.11% | 100% |
| dip45_V3_alle | 4136 | 13% | 5.4% | +132.0% | -28.5% | -7.12% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2841 | 13% | 3.7% | -10.15% | 100% |
| zonder_xlink | 870 | 19% | 0.0% | +23.66% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 01:48:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:48:31,256 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:48:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:48:32,005 main INFO screen nomoremrniceg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 12 01:48:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:48:36,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:48:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:48:51,080 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.1s)
Sep 12 01:49:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:11,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:49:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:16,867 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:49:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:23,606 main INFO screen CRISPE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 12 01:49:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:31,652 main INFO screen SEC pass=0 dev=0.0 ins=21.86 pro=64 1a=False 1b=False 2=True (20.0s)
Sep 12 01:49:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:45,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:49:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:52,396 main INFO screen nomoremrniceg pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=True (7.0s)
Sep 12 01:49:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:49:58,325 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:50:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:50:03,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:50:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:50:17,897 main INFO screen JOHN pass=0 dev=67.25 ins=0.0 pro=9 1a=False 1b=False 2=False (19.6s)
Sep 12 01:50:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:50:47,315 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:50:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:50:47,626 main INFO screen nomoremrniceg pass=0 dev=1.02 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 12 01:50:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:50:53,939 main INFO screen $CAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 12 01:51:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:11,283 main INFO screen nomoremrniceg pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 12 01:51:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:29,013 main INFO screen skipoo pass=0 dev=1.95 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 01:51:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:30,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:51:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:35,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:51:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:40,114 main INFO screen comini pass=0 dev=5.05 ins=15.54 pro=36 1a=False 1b=False 2=True (1.7s)
Sep 12 01:51:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:51:48,737 main INFO screen STUNKBRAIN pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.4s)
Sep 12 01:52:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:20,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:52:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:22,177 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:52:22 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 01:52:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:22,681 aiohttp.access INFO 47.250.57.127 [12/Sep/2026:01:52:22 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 01:52:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:23,017 aiohttp.access INFO 47.250.57.127 [12/Sep/2026:01:52:23 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 12 01:52:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:25,178 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:52:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:52:39,063 main INFO screen kingtap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.1s)
Sep 12 01:53:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:53:02,915 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:53:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:53:07,989 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:53:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:53:22,012 main INFO screen WeWorm pass=0 dev=0.0 ins=15.72 pro=56 1a=False 1b=False 2=True (19.2s)
Sep 12 01:53:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:53:47,379 main INFO screen FB pass=0 dev=1.73 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 12 01:53:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:53:53,143 main INFO screen Fries pass=1 dev=1.74 ins=6.3 pro=33 1a=False 1b=False 2=False (2.8s)
Sep 12 01:54:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:54:11,932 main INFO screen SEC pass=1 dev=0.0 ins=0.0 pro=31 1a=False 1b=False 2=False (3.3s)
Sep 12 01:54:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:54:43,265 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 12 01:55:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:55:32,573 main INFO screen DOOROC pass=0 dev=3.78 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 01:55:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:55:54,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:55:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:55:59,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:56:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:56:14,700 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 01:56:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:56:20,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:56:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:56:23,033 main INFO screen Toecoin pass=1 dev=1.76 ins=9.45 pro=33 1a=False 1b=False 2=False (2.5s)
Sep 12 01:56:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:56:28,622 main INFO screen SilverSurfer pass=0 dev=0.0 ins=16.1 pro=57 1a=False 1b=False 2=True (8.0s)
Sep 12 01:57:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:22,817 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:57:22 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 01:57:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:51,400 main INFO screen sol pass=0 dev=1.1 ins=0.0 pro=4 1a=False 1b=False 2=False (2.7s)
Sep 12 01:57:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:54,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:57:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:54,370 main INFO screen skipoo pass=0 dev=1.99 ins=0.0 pro=2 1a=False 1b=False 2=True (2.0s)
Sep 12 01:57:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:57,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:57:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:57:59,178 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:58:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:58:02,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:58:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:58:14,066 main INFO screen ALON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.3s)
Sep 12 01:58:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:58:17,220 main INFO screen fomo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 01:58:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:58:48,507 main INFO screen TolyMole pass=0 dev=2.29 ins=0.0 pro=4 1a=False 1b=False 2=False (2.6s)
Sep 12 01:59:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:05,618 main INFO screen 5 pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 12 01:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:10,640 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:59:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:15,703 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:59:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:29,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:59:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:30,349 main INFO screen SilverSurfer pass=0 dev=0.0 ins=19.67 pro=8 1a=False 1b=False 2=True (19.8s)
Sep 12 01:59:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:36,791 main INFO screen roundtrip pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 12 01:59:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:59:58,037 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:03,064 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:05,751 main INFO screen skipoo pass=0 dev=2.01 ins=0.0 pro=3 1a=False 1b=False 2=True (7.9s)
Sep 12 02:00:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:10,963 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:16,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:17,856 main INFO screen roundtrip pass=0 dev=0.89 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 12 02:00:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:19,094 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:21,762 main INFO screen SILVER pass=0 dev=0.0 ins=20.13 pro=31 1a=False 1b=False 2=True (23.8s)
Sep 12 02:00:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:24,163 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:00:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:38,265 main INFO screen GitHub pass=0 dev=98.3 ins=0.0 pro=1 1a=False 1b=False 2=True (27.9s)
Sep 12 02:00:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:00:45,598 main INFO screen Rack pass=0 dev=0.0 ins=16.66 pro=36 1a=False 1b=False 2=True (26.6s)
Sep 12 02:01:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:00,985 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:01:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:06,013 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:01:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:09,538 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:01:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:17,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:01:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:25,696 main INFO screen ch pass=0 dev=0.0 ins=0.03 pro=4 1a=False 1b=False 2=False (16.2s)
Sep 12 02:01:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:26,071 main INFO screen CPE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (25.2s)
Sep 12 02:01:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:26,463 main INFO screen Rack pass=0 dev=0.0 ins=0.0 pro=49 1a=False 1b=False 2=True (9.3s)
Sep 12 02:01:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:41,618 main INFO screen Toecoin pass=1 dev=1.76 ins=7.02 pro=28 1a=False 1b=False 2=False (4.4s)
Sep 12 02:01:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:01:50,705 main INFO screen DOOGAN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (11.8s)
Sep 12 02:02:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:02:18,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:02:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:02:23,120 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:02:23 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T00:34:36Z
--- update 2026-09-12T00:39:59Z
--- update 2026-09-12T00:45:13Z
--- update 2026-09-12T00:50:17Z
--- update 2026-09-12T00:55:36Z
--- update 2026-09-12T01:00:52Z
--- update 2026-09-12T01:06:31Z
--- update 2026-09-12T01:11:36Z
--- update 2026-09-12T01:16:55Z
--- update 2026-09-12T01:22:03Z
--- update 2026-09-12T01:27:11Z
--- update 2026-09-12T01:32:13Z
--- update 2026-09-12T01:37:15Z
--- update 2026-09-12T01:42:15Z
--- update 2026-09-12T01:47:19Z
--- update 2026-09-12T01:52:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 39f959b4ea4249ad9802ce16bcd55516
analyses gestart (8746aefc73b4)
--- update 2026-09-12T01:57:21Z
--- update 2026-09-12T02:02:22Z
```

## Analyses (laatste 25 regels)
```
inactive
01:52:48 3000 aankopen van gevolgde wallets geëvalueerd
01:53:00 grote spelers: saldo van 1359 wallets opgehaald
01:53:57 herkomst: 40 posities gekoppeld
01:53:58 klaar in 97s -> /opt/schaduwbot/reports/ledger.md
01:54:00   2000 nieuwe tokens doorgerekend
01:54:02 klaar in 4s: 11080 tokens, 2981 nieuw -> /opt/schaduwbot/reports/video_replay.md
01:54:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 01:54 UTC
01:54:02 45856 tokens geladen
01:54:04   2000 tokens, 253102 trades, 54428 posities (2s)
01:54:07   4000 tokens, 520825 trades, 111725 posities (5s)
01:54:09   6000 tokens, 782379 trades, 167557 posities (7s)
01:54:11   8000 tokens, 1054119 trades, 222555 posities (9s)
01:54:13   10000 tokens, 1329211 trades, 281413 posities (11s)
01:54:16   12000 tokens, 1594580 trades, 333921 posities (13s)
01:54:18   14000 tokens, 1836819 trades, 382990 posities (15s)
01:54:20   16000 tokens, 2119459 trades, 446339 posities (18s)
01:54:22   18000 tokens, 2395048 trades, 502642 posities (20s)
01:54:24   20000 tokens, 2629029 trades, 552671 posities (22s)
01:54:27   22000 tokens, 2903307 trades, 608372 posities (24s)
01:54:29 posities: 660394 uit 3108846 trades (26s)
01:54:37 148332 wallets gerekend
01:54:38 geluk-toets
01:55:03 persistentie
01:55:05 kopieer-simulatie
01:55:14 klaar in 72s -> /opt/schaduwbot/reports/wallets.md
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
