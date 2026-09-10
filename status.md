# Schaduwbot status

- tijd: 2026-09-10 23:02:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 9 hours, 15 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 640/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 33250, "tokens_in_memory": 1543, "msgs": 6859533, "trades": 1261379, "creates": 13747, "decode_fail": 96979, "rpc_calls": 20618, "rpc_errors": 2053, "sol_usd": 99.26834253865668, "open_positions": 103}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 22:48 UTC

Gelogde schaduwtrades: **10555**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 13367 | 1895 | 28 | 1895 | 171 | 3561 | 10555 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 136 | 15% | 2.2% | +38.4% | -17.1% | -8.50% | 92% |
| dip35_V1_gescreend_fail | 1057 | 26% | 4.3% | +45.9% | -25.7% | -6.96% | 100% |
| dip35_V1_alle | 1231 | 25% | 4.3% | +44.7% | -25.1% | -7.57% | 100% |
| dip35_V2_gescreend_pass | 135 | 17% | 3.0% | +29.4% | -22.0% | -13.23% | 98% |
| dip35_V2_gescreend_fail | 1052 | 24% | 4.9% | +54.7% | -28.1% | -8.12% | 100% |
| dip35_V2_alle | 1216 | 23% | 5.0% | +52.0% | -27.8% | -9.27% | 100% |
| dip35_V3_gescreend_pass | 135 | 7% | 3.0% | +132.0% | -23.6% | -13.23% | 99% |
| dip35_V3_gescreend_fail | 1064 | 12% | 6.7% | +124.9% | -30.0% | -11.93% | 100% |
| dip35_V3_alle | 1226 | 11% | 6.5% | +122.0% | -29.5% | -12.61% | 100% |
| dip40_V1_gescreend_pass | 125 | 14% | 3.2% | +43.8% | -16.5% | -8.26% | 91% |
| dip40_V1_gescreend_fail | 1023 | 25% | 4.3% | +49.3% | -25.5% | -6.57% | 100% |
| dip40_V1_alle | 1179 | 24% | 4.3% | +48.3% | -24.7% | -7.03% | 100% |
| dip40_V2_gescreend_pass | 124 | 13% | 3.2% | +47.2% | -21.1% | -12.29% | 97% |
| dip40_V2_gescreend_fail | 1020 | 24% | 4.7% | +55.7% | -27.8% | -7.45% | 100% |
| dip40_V2_alle | 1165 | 23% | 4.7% | +54.6% | -27.3% | -8.39% | 100% |
| dip40_V3_gescreend_pass | 124 | 7% | 3.2% | +116.7% | -22.4% | -12.34% | 98% |
| dip40_V3_gescreend_fail | 1033 | 11% | 6.2% | +107.4% | -29.5% | -13.84% | 100% |
| dip40_V3_alle | 1176 | 11% | 6.0% | +105.8% | -28.9% | -14.04% | 100% |
| dip45_V1_gescreend_pass | 113 | 13% | 3.5% | +43.4% | -16.0% | -8.15% | 91% |
| dip45_V1_gescreend_fail | 990 | 26% | 3.7% | +51.1% | -24.9% | -4.96% | 100% |
| dip45_V1_alle | 1126 | 25% | 3.9% | +50.3% | -24.2% | -5.59% | 100% |
| dip45_V2_gescreend_pass | 112 | 16% | 4.5% | +40.3% | -20.6% | -10.83% | 94% |
| dip45_V2_gescreend_fail | 984 | 25% | 4.2% | +61.0% | -27.2% | -5.25% | 100% |
| dip45_V2_alle | 1112 | 24% | 4.4% | +59.2% | -26.8% | -6.21% | 100% |
| dip45_V3_gescreend_pass | 113 | 6% | 4.4% | +185.1% | -21.5% | -8.66% | 96% |
| dip45_V3_gescreend_fail | 997 | 12% | 5.8% | +128.5% | -28.9% | -9.47% | 100% |
| dip45_V3_alle | 1124 | 12% | 5.9% | +129.7% | -28.3% | -9.77% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 22:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:42,933 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:51:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:43,079 main INFO screen TNON pass=0 dev=0.0 ins=24.52 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 10 22:51:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:51:44,262 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:51:44 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 22:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:12,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:12,400 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:12,580 main INFO screen peesee pass=0 dev=0.0 ins=9.9 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 10 22:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:12,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:12,920 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:52:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:13,333 main INFO screen LBGJ pass=0 dev=0.0 ins=12.93 pro=16 1a=False 1b=False 2=True (0.6s)
Sep 10 22:52:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:44,977 main INFO screen PUMPFUN pass=0 dev=2.36 ins=19.77 pro=17 1a=False 1b=False 2=True (1.9s)
Sep 10 22:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:48,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:48,788 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:52:48,937 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 22:53:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:14,574 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:53:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:14,678 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:53:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:15,028 main INFO screen LBGJ pass=0 dev=0.0 ins=9.16 pro=20 1a=False 1b=False 2=True (0.5s)
Sep 10 22:53:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:16,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:53:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:16,347 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:53:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:16,900 main INFO screen OTC pass=0 dev=0.0 ins=11.78 pro=4 1a=False 1b=False 2=True (0.7s)
Sep 10 22:53:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:54,078 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:53:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:54,173 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:53:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:53:54,724 main INFO screen CURE pass=0 dev=0.0 ins=36.19 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 10 22:54:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:04,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:54:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:04,238 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:54:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:04,569 main INFO screen LBGJ pass=0 dev=0.0 ins=17.19 pro=19 1a=False 1b=False 2=True (0.5s)
Sep 10 22:54:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:09,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:54:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:09,228 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:54:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:54:09,350 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 22:55:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:08,865 main INFO screen Faceless pass=1 dev=0.03 ins=0.0 pro=42 1a=False 1b=False 2=False (3.6s)
Sep 10 22:55:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:30,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:55:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:30,610 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:55:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:30,815 main INFO screen TROLL pass=0 dev=0.0 ins=79.17 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 22:55:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:54,641 main INFO screen Puter pass=1 dev=0.0 ins=11.16 pro=35 1a=False 1b=False 2=False (3.9s)
Sep 10 22:55:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:55:55,033 main INFO screen CURE pass=0 dev=0.0 ins=19.03 pro=58 1a=False 1b=False 2=True (3.8s)
Sep 10 22:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:56:30,158 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:56:30,211 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:56:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:56:30,435 main INFO screen 10M pass=0 dev=0.0 ins=4.35 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 10 22:57:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:57:17,742 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:57:17 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 22:58:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:36,226 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:58:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:36,323 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:58:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:36,671 main INFO screen HOMO pass=0 dev=0.0 ins=20.17 pro=8 1a=False 1b=False 2=True (0.5s)
Sep 10 22:58:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:53,820 main INFO screen AICAT pass=0 dev=1.09 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 22:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:57,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:57,790 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:58:57,935 main INFO screen HOMO pass=0 dev=0.0 ins=24.15 pro=14 1a=False 1b=False 2=True (0.3s)
Sep 10 22:59:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:37,793 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:59:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:39,228 main INFO screen App pass=0 dev=5.37 ins=31.72 pro=40 1a=False 1b=False 2=True (2.1s)
Sep 10 22:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:40,484 main INFO screen Pumpban pass=1 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (4.1s)
Sep 10 22:59:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:49,393 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:59:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:49,466 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:59:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:49,630 main INFO screen App pass=0 dev=0.0 ins=36.2 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 10 22:59:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:49,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:59:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:49,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:59:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:50,031 main INFO screen App pass=0 dev=0.0 ins=23.52 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 22:59:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:54,557 main INFO screen Cure pass=0 dev=0.0 ins=22.56 pro=49 1a=False 1b=False 2=True (2.0s)
Sep 10 22:59:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:59:57,620 main INFO screen LCOST pass=0 dev=1.77 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 10 23:00:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:16,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:00:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:16,704 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:00:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:16,886 main INFO screen App pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=True (0.4s)
Sep 10 23:00:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:41,541 main INFO screen AICAT pass=0 dev=1.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 10 23:00:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:50,793 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:00:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:50,891 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:00:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:00:51,223 main INFO screen ape pass=0 dev=0.0 ins=17.32 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 10 23:01:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:13,597 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 10 23:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:14,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:14,367 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:14,717 main INFO screen ape pass=0 dev=0.0 ins=22.05 pro=10 1a=False 1b=False 2=True (0.5s)
Sep 10 23:01:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:31,846 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:01:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:31,971 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:01:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:36,152 main INFO screen nofun pass=0 dev=7.24 ins=0.0 pro=44 1a=False 1b=False 2=False (9.7s)
Sep 10 23:01:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:36,439 main INFO screen AICAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.7s)
Sep 10 23:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:49,593 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:49,721 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:01:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:50,036 main INFO screen FOMO pass=0 dev=0.0 ins=10.06 pro=29 1a=False 1b=False 2=True (0.5s)
Sep 10 23:01:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:01:53,805 main INFO screen BPCATE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 10 23:02:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:02:11,583 main INFO screen mmrich pass=0 dev=4.85 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 10 23:02:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:02:16,011 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 23:02:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:02:16,137 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 23:02:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:02:23,154 main INFO screen GIAB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.2s)
Sep 10 23:02:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 23:02:27,068 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:23:02:27 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
