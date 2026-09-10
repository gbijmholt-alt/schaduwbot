# Schaduwbot status

- tijd: 2026-09-10 18:08:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 hours, 21 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 580/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 15620, "tokens_in_memory": 1361, "msgs": 2895336, "trades": 519096, "creates": 6204, "decode_fail": 42575, "rpc_calls": 8761, "rpc_errors": 958, "sol_usd": 99.53263299791018, "open_positions": 74}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 17:48 UTC

Gelogde schaduwtrades: **4206**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 5678 | 778 | 16 | 778 | 98 | 1424 | 4206 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 77 | 12% | 1.3% | +32.1% | -15.5% | -9.92% | 81% |
| dip35_V1_gescreend_fail | 393 | 25% | 5.1% | +47.4% | -27.1% | -8.15% | 100% |
| dip35_V1_alle | 491 | 24% | 4.7% | +45.0% | -25.7% | -9.02% | 100% |
| dip35_V2_gescreend_pass | 76 | 16% | 1.3% | +22.9% | -19.8% | -13.04% | 88% |
| dip35_V2_gescreend_fail | 395 | 22% | 5.6% | +64.9% | -28.9% | -8.23% | 100% |
| dip35_V2_alle | 487 | 21% | 5.1% | +58.1% | -28.0% | -9.79% | 100% |
| dip35_V3_gescreend_pass | 76 | 7% | 1.3% | +75.2% | -22.2% | -15.78% | 92% |
| dip35_V3_gescreend_fail | 399 | 11% | 7.0% | +120.5% | -30.5% | -13.88% | 100% |
| dip35_V3_alle | 489 | 11% | 6.3% | +109.6% | -29.7% | -14.91% | 100% |
| dip40_V1_gescreend_pass | 73 | 16% | 1.4% | +43.7% | -14.9% | -5.30% | 67% |
| dip40_V1_gescreend_fail | 382 | 23% | 6.0% | +54.0% | -27.6% | -9.01% | 100% |
| dip40_V1_alle | 472 | 22% | 5.3% | +51.5% | -26.0% | -8.75% | 100% |
| dip40_V2_gescreend_pass | 72 | 17% | 1.4% | +54.4% | -19.3% | -7.03% | 73% |
| dip40_V2_gescreend_fail | 383 | 21% | 6.0% | +70.4% | -29.5% | -8.10% | 100% |
| dip40_V2_alle | 467 | 21% | 5.4% | +66.8% | -28.3% | -8.51% | 100% |
| dip40_V3_gescreend_pass | 72 | 10% | 1.4% | +57.1% | -21.0% | -13.37% | 88% |
| dip40_V3_gescreend_fail | 387 | 12% | 7.8% | +112.2% | -31.5% | -14.39% | 100% |
| dip40_V3_alle | 469 | 12% | 6.8% | +101.4% | -30.2% | -14.77% | 100% |
| dip45_V1_gescreend_pass | 65 | 18% | 1.5% | +44.4% | -14.4% | -3.53% | 63% |
| dip45_V1_gescreend_fail | 368 | 23% | 6.0% | +56.2% | -27.3% | -8.28% | 100% |
| dip45_V1_alle | 447 | 22% | 5.4% | +53.9% | -25.8% | -7.98% | 100% |
| dip45_V2_gescreend_pass | 63 | 24% | 1.6% | +42.8% | -17.6% | -3.21% | 60% |
| dip45_V2_gescreend_fail | 367 | 22% | 6.3% | +73.3% | -29.2% | -7.10% | 100% |
| dip45_V2_alle | 440 | 22% | 5.7% | +67.5% | -27.9% | -7.09% | 100% |
| dip45_V3_gescreend_pass | 64 | 9% | 1.6% | +108.1% | -19.2% | -7.29% | 80% |
| dip45_V3_gescreend_fail | 372 | 14% | 7.5% | +153.4% | -30.7% | -5.00% | 100% |
| dip45_V3_alle | 444 | 13% | 6.8% | +146.4% | -29.4% | -6.02% | 100% |

## Beste variant: dip45_V2_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 17:58:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:04,221 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:58:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:04,372 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 17:58:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:09,429 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:58:09 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
Sep 10 17:58:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:26,863 main INFO screen gato pass=1 dev=0.0 ins=10.75 pro=60 1a=False 1b=False 2=False (3.4s)
Sep 10 17:58:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:31,374 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 10 17:58:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:35,918 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:58:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:36,050 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:58:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:36,183 main INFO screen AD pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 17:58:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:58:48,358 main INFO screen RISE pass=0 dev=39.04 ins=0.0 pro=8 1a=False 1b=False 2=True (2.4s)
Sep 10 17:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:02,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:02,591 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:02,864 main INFO screen SMART pass=0 dev=0.0 ins=36.1 pro=8 1a=False 1b=False 2=True (0.5s)
Sep 10 17:59:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:11,844 main INFO screen fuk pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 10 17:59:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:27,848 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.4s)
Sep 10 17:59:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:29,509 main INFO screen Gösta  pass=1 dev=1.22 ins=0.0 pro=27 1a=False 1b=False 2=False (3.8s)
Sep 10 17:59:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:54,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:59:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:54,744 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:59:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:59:55,375 main INFO screen FETTERFLY pass=0 dev=0.0 ins=21.87 pro=11 1a=False 1b=False 2=True (0.8s)
Sep 10 18:00:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:10,955 main INFO screen Midas pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 10 18:00:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:15,032 main INFO screen JOKOWI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 10 18:00:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:23,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:00:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:23,740 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:00:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:30,711 main INFO screen GATO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 10 18:00:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:00:59,718 main INFO screen Robinhood pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.8s)
Sep 10 18:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:01:49,194 main INFO screen ! pass=0 dev=0.32 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 10 18:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:01:49,979 main INFO screen help pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.7s)
Sep 10 18:02:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:02,973 main INFO screen KDAY pass=0 dev=6.78 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 10 18:02:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:21,292 main INFO screen BTCNC pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=True (5.8s)
Sep 10 18:02:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:21,378 main INFO screen BOOBS pass=0 dev=2.61 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 10 18:02:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:40,114 main INFO screen lena pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 10 18:02:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:52,785 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:02:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:52,883 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:02:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:02:53,186 main INFO screen Stonkfly pass=0 dev=0.0 ins=18.4 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 18:03:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:03:36,392 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:03:36 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 18:03:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:03:48,157 main INFO screen CHAROC pass=0 dev=15.01 ins=0.0 pro=2 1a=False 1b=False 2=False (13.0s)
Sep 10 18:04:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:04:02,471 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 10 18:05:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:04,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:05:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:04,704 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:05:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:05,319 main INFO screen RICK pass=0 dev=1.92 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 10 18:05:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:11,841 main INFO screen PIPECAT pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (7.3s)
Sep 10 18:05:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:27,945 main INFO screen 988 pass=0 dev=0.0 ins=15.7 pro=47 1a=False 1b=False 2=True (3.8s)
Sep 10 18:05:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:50,693 main INFO screen Minik pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 10 18:05:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:05:59,600 main INFO screen 988 pass=1 dev=0.0 ins=15.83 pro=22 1a=False 1b=False 2=False (3.6s)
Sep 10 18:06:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:01,256 main INFO screen ! pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 10 18:06:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:51,770 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:06:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:51,903 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:06:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:52,249 main INFO screen SUPERCYCLE pass=0 dev=0.0 ins=14.05 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 10 18:06:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:52,580 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:06:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:52,742 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:53,017 main INFO screen MSC pass=0 dev=0.0 ins=25.8 pro=3 1a=False 1b=False 2=True (0.5s)
Sep 10 18:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:53,119 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:53,249 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:53,541 main INFO screen OIL pass=0 dev=0.0 ins=16.1 pro=10 1a=False 1b=False 2=True (0.5s)
Sep 10 18:06:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:54,547 main INFO screen BUNJIM pass=0 dev=36.91 ins=0.0 pro=8 1a=False 1b=False 2=True (6.4s)
Sep 10 18:06:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:57,536 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:06:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:57,656 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:06:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:06:57,836 main INFO screen DTM pass=0 dev=0.0 ins=16.81 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 10 18:07:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:07,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:07,864 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:08,282 main INFO screen PUMPLIFE pass=0 dev=0.0 ins=5.67 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 10 18:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:17,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:18,059 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:18,492 main INFO screen PUMPLIFE pass=0 dev=0.0 ins=11.56 pro=10 1a=False 1b=False 2=True (0.6s)
Sep 10 18:07:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:19,405 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:19,531 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:19,853 main INFO screen PUMPLIFE pass=0 dev=0.0 ins=23.61 pro=26 1a=False 1b=False 2=True (0.5s)
Sep 10 18:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:27,357 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:27,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:27,767 main INFO screen DTM pass=1 dev=0.0 ins=12.37 pro=14 1a=False 1b=False 2=False (0.5s)
Sep 10 18:07:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:31,244 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 10 18:07:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:32,551 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:32,633 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:35,769 main INFO screen PUMPLIFE pass=0 dev=0.0 ins=19.15 pro=9 1a=False 1b=False 2=True (3.3s)
Sep 10 18:07:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:42,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:07:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:42,922 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:07:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:07:44,359 main INFO screen STACKED pass=0 dev=0.0 ins=38.91 pro=7 1a=False 1b=False 2=True (1.6s)
Sep 10 18:08:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:08:03,442 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:08:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:08:03,538 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:08:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:08:10,864 main INFO screen Veronica pass=0 dev=0.0 ins=5.01 pro=27 1a=False 1b=False 2=True (7.5s)
Sep 10 18:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:08:37,069 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:08:37 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
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
