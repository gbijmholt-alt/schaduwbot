# Schaduwbot status

- tijd: 2026-09-12 01:06:32 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 11 hours, 19 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.2G/38G | geheugen: 1002/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 19584, "tokens_in_memory": 7194, "msgs": 4364976, "trades": 788459, "creates": 7194, "decode_fail": 45479, "rpc_calls": 26459, "rpc_errors": 1023, "sol_usd": 102.04697067647088, "open_positions": 80, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **37359**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 826 | 131 | 0 | 129 | 11 | 253 | 803 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 430 | 17% | 2.3% | +44.5% | -17.0% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 3585 | 27% | 3.6% | +45.6% | -25.9% | -6.81% | 100% |
| dip35_V1_alle | 4324 | 26% | 3.7% | +44.5% | -25.2% | -6.97% | 100% |
| dip35_V2_gescreend_pass | 427 | 22% | 3.3% | +45.3% | -21.5% | -7.10% | 100% |
| dip35_V2_gescreend_fail | 3606 | 25% | 4.2% | +56.4% | -28.1% | -7.23% | 100% |
| dip35_V2_alle | 4288 | 24% | 4.3% | +54.1% | -27.7% | -7.75% | 100% |
| dip35_V3_gescreend_pass | 428 | 9% | 3.7% | +331.7% | -22.9% | +7.80% | 100% |
| dip35_V3_gescreend_fail | 3682 | 13% | 5.9% | +119.1% | -29.6% | -9.76% | 100% |
| dip35_V3_alle | 4335 | 13% | 5.8% | +126.6% | -29.2% | -8.79% | 100% |
| dip40_V1_gescreend_pass | 400 | 15% | 2.5% | +47.3% | -16.3% | -6.96% | 100% |
| dip40_V1_gescreend_fail | 3515 | 26% | 3.7% | +47.4% | -25.9% | -6.70% | 100% |
| dip40_V1_alle | 4151 | 25% | 3.7% | +47.0% | -25.1% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 398 | 17% | 3.0% | +49.4% | -20.2% | -8.46% | 100% |
| dip40_V2_gescreend_fail | 3516 | 25% | 4.2% | +55.4% | -28.0% | -7.49% | 100% |
| dip40_V2_alle | 4108 | 24% | 4.3% | +54.0% | -27.5% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 401 | 8% | 3.2% | +343.8% | -21.4% | +5.91% | 100% |
| dip40_V3_gescreend_fail | 3591 | 13% | 5.8% | +116.6% | -29.5% | -10.50% | 100% |
| dip40_V3_alle | 4162 | 13% | 5.7% | +124.6% | -28.9% | -9.57% | 100% |
| dip45_V1_gescreend_pass | 385 | 16% | 2.3% | +48.8% | -16.2% | -5.91% | 100% |
| dip45_V1_gescreend_fail | 3431 | 27% | 3.2% | +47.9% | -25.6% | -5.51% | 100% |
| dip45_V1_alle | 4011 | 26% | 3.3% | +47.7% | -24.9% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 381 | 19% | 2.9% | +47.6% | -20.1% | -7.27% | 100% |
| dip45_V2_gescreend_fail | 3421 | 25% | 3.8% | +57.4% | -27.6% | -6.46% | 100% |
| dip45_V2_alle | 3965 | 24% | 3.9% | +55.8% | -27.1% | -7.07% | 100% |
| dip45_V3_gescreend_pass | 385 | 8% | 2.9% | +392.1% | -20.7% | +10.38% | 100% |
| dip45_V3_gescreend_fail | 3487 | 14% | 5.3% | +123.3% | -28.9% | -7.77% | 100% |
| dip45_V3_alle | 4015 | 13% | 5.3% | +134.0% | -28.4% | -6.74% | 100% |

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
| met_xlink | 2772 | 13% | 3.8% | -10.06% | 100% |
| zonder_xlink | 863 | 18% | 0.0% | +23.78% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 00:50:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:50:59,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:51:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:15,875 main INFO screen HODL pass=0 dev=0.0 ins=23.44 pro=8 1a=False 1b=False 2=True (21.9s)
Sep 12 00:51:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:16,179 main INFO screen STRATEGY pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.8s)
Sep 12 00:51:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:35,523 main INFO screen fast pass=0 dev=0.25 ins=0.0 pro=4 1a=False 1b=False 2=False (4.5s)
Sep 12 00:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:36,037 main INFO screen GLEKI pass=0 dev=0.18 ins=28.68 pro=23 1a=False 1b=True 2=False (3.8s)
Sep 12 00:51:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:43,941 main INFO screen planos? pass=0 dev=0.22 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 00:51:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:48,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:51:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:51:53,468 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:52:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:52:07,593 main INFO screen HODL pass=0 dev=6.63 ins=21.9 pro=11 1a=False 1b=False 2=True (19.3s)
Sep 12 00:53:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:14,235 main INFO screen $DABO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 12 00:53:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:22,500 main INFO screen CPU pass=1 dev=0.0 ins=19.05 pro=49 1a=False 1b=False 2=False (2.5s)
Sep 12 00:53:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:28,924 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:53:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:33,993 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:53:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:48,036 main INFO screen HODL pass=0 dev=4.97 ins=30.1 pro=38 1a=False 1b=False 2=True (19.1s)
Sep 12 00:53:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:53:54,037 main INFO screen FUCK pass=0 dev=6.13 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 12 00:54:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:54:00,693 main INFO screen and again pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 12 00:54:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:54:55,003 main INFO screen GLIAGE pass=0 dev=3.33 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 12 00:55:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:14,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:55:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:19,458 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:55:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:33,760 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.4s)
Sep 12 00:55:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:37,067 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:55:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 00:55:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:40,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:55:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:45,207 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:55:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:55:58,516 main INFO screen FLYCAT pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (18.4s)
Sep 12 00:56:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:56:10,277 main INFO screen cartio pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 12 00:57:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:57:07,824 main INFO screen     DHi pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 00:57:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:57:22,053 main INFO screen BIRDKICKS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 12 00:57:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:57:56,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:58:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:01,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:58:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:07,945 main INFO screen deliverINU pass=0 dev=0.0 ins=11.25 pro=53 1a=False 1b=False 2=True (3.4s)
Sep 12 00:58:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:16,315 main INFO screen OPAI pass=0 dev=0.0 ins=20.48 pro=12 1a=False 1b=False 2=True (20.2s)
Sep 12 00:58:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:42,052 main INFO screen fone pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 12 00:58:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:42,531 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:58:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:47,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:58:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:50,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:58:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:58:56,608 main INFO screen OPAI pass=0 dev=0.0 ins=20.63 pro=26 1a=False 1b=False 2=True (6.3s)
Sep 12 00:59:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:59:02,320 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 00:59:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:59:10,155 main INFO screen WATER pass=1 dev=0.0 ins=12.38 pro=24 1a=False 1b=False 2=False (1.6s)
Sep 12 00:59:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:59:16,121 main INFO screen SKID pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 12 00:59:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:59:32,001 main INFO screen $GOAT pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 12 01:00:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:03,782 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:00:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:08,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:00:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:15,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:00:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:18,637 main INFO screen NEKO pass=0 dev=0.0 ins=18.48 pro=36 1a=False 1b=False 2=True (9.8s)
Sep 12 01:00:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:20,773 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:00:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:28,337 main INFO screen ROBIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.6s)
Sep 12 01:00:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:41,678 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 12 01:00:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:53,868 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:00:53 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 01:00:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:00:59,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:01:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:04,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:01:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:07,383 main INFO screen gasolinu pass=0 dev=0.0 ins=17.77 pro=62 1a=False 1b=False 2=True (9.1s)
Sep 12 01:01:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:16,860 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:01:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:21,933 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:01:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:24,398 main INFO screen NEKO pass=0 dev=0.0 ins=18.72 pro=23 1a=False 1b=False 2=True (25.5s)
Sep 12 01:01:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:36,502 main INFO screen JAX pass=0 dev=0.0 ins=10.68 pro=15 1a=False 1b=True 2=False (19.8s)
Sep 12 01:01:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:48,563 main INFO screen CHAROC pass=0 dev=0.57 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 01:01:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:01:54,617 main INFO screen bOOb pass=0 dev=0.83 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 12 01:02:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:02:28,026 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:02:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:02:40,253 main INFO screen Gram pass=0 dev=0.0 ins=18.45 pro=64 1a=False 1b=False 2=True (12.3s)
Sep 12 01:02:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:02:45,860 main INFO screen cap pass=0 dev=0.33 ins=0.0 pro=3 1a=False 1b=False 2=False (6.6s)
Sep 12 01:02:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:02:50,406 main INFO screen CATEk pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.8s)
Sep 12 01:03:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:03:02,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:03:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:03:15,865 main INFO screen cattail pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (13.9s)
Sep 12 01:03:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:03:29,922 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:03:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:03:41,606 main INFO screen gilbert pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.8s)
Sep 12 01:04:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:04:47,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:04:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:04:52,135 main INFO screen Hoodtard pass=0 dev=0.0 ins=17.96 pro=41 1a=False 1b=False 2=True (5.8s)
Sep 12 01:04:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:04:59,533 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:05:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:00,384 main INFO screen Hoodtard pass=0 dev=0.0 ins=18.32 pro=25 1a=False 1b=False 2=True (13.7s)
Sep 12 01:05:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:04,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:05:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:09,932 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:05:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:20,680 main INFO screen $ALLDOG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.8s)
Sep 12 01:05:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:23,166 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.7s)
Sep 12 01:05:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:40,577 main INFO screen imposter pass=0 dev=0.0 ins=17.14 pro=65 1a=False 1b=False 2=True (10.1s)
Sep 12 01:05:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:42,192 main INFO screen gotswanned pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (6.0s)
Sep 12 01:05:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:49,961 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:05:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:05:55,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:06:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:06:15,484 main INFO screen DELULU pass=0 dev=0.0 ins=16.17 pro=34 1a=False 1b=False 2=True (25.6s)
Sep 12 01:06:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:06:31,234 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:06:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:06:32,463 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:06:32 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T00:29:13Z
--- update 2026-09-12T00:34:36Z
--- update 2026-09-12T00:39:59Z
--- update 2026-09-12T00:45:13Z
--- update 2026-09-12T00:50:17Z
--- update 2026-09-12T00:55:36Z
--- update 2026-09-12T01:00:52Z
--- update 2026-09-12T01:06:31Z
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
