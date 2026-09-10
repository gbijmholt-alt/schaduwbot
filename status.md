# Schaduwbot status

- tijd: 2026-09-10 18:24:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 hours, 37 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 600/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 16580, "tokens_in_memory": 1388, "msgs": 3126514, "trades": 555307, "creates": 6594, "decode_fail": 44323, "rpc_calls": 9373, "rpc_errors": 1020, "sol_usd": 99.35533835506581, "open_positions": 77}
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
Sep 10 18:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:37,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:37,981 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:11:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:38,536 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:11:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:38,678 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:11:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:38,931 main INFO screen STACKED pass=0 dev=0.0 ins=9.26 pro=9 1a=False 1b=False 2=True (0.5s)
Sep 10 18:11:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:11:43,636 main INFO screen chillcate pass=1 dev=0.0 ins=15.66 pro=14 1a=False 1b=False 2=False (5.8s)
Sep 10 18:13:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:13:22,337 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:13:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:13:22,428 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:13:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:13:27,246 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.0s)
Sep 10 18:13:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:13:33,819 main INFO screen Gfly pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (5.0s)
Sep 10 18:13:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:13:48,812 main INFO screen $AURA pass=0 dev=2.06 ins=0.0 pro=2 1a=False 1b=False 2=False (9.3s)
Sep 10 18:14:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:03,014 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:14:03 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 18:14:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:04,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:14:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:04,687 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:14:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:05,492 main INFO screen ZENCAT pass=0 dev=0.0 ins=16.39 pro=18 1a=False 1b=False 2=True (1.8s)
Sep 10 18:14:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:12,209 main INFO screen ! pass=0 dev=0.44 ins=0.0 pro=7 1a=False 1b=False 2=False (10.2s)
Sep 10 18:14:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:12,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:14:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:12,869 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:14:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:13,080 main INFO screen WTG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 10 18:14:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:13,230 main INFO screen ZENCAT pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=True (0.5s)
Sep 10 18:14:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:30,090 main INFO screen meh pass=0 dev=6.33 ins=3.09 pro=37 1a=False 1b=False 2=False (10.0s)
Sep 10 18:14:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:41,442 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:14:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:41,540 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:14:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:14:41,858 main INFO screen Zcat pass=0 dev=0.0 ins=12.32 pro=10 1a=False 1b=False 2=True (0.5s)
Sep 10 18:15:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:07,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:15:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:07,876 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:08,368 main INFO screen zencate pass=0 dev=0.0 ins=3.64 pro=35 1a=False 1b=False 2=True (0.7s)
Sep 10 18:15:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:16,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:15:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:16,296 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:15:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:15:21,504 main INFO screen S&P6900 pass=0 dev=0.0 ins=27.83 pro=5 1a=False 1b=False 2=True (5.4s)
Sep 10 18:16:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:16:37,965 main INFO screen Based pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 10 18:16:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:16:59,383 main INFO screen STACO pass=0 dev=0.36 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 10 18:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:17:17,531 main INFO screen DERP pass=0 dev=2.57 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 10 18:17:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:17:45,381 main INFO screen YCAT pass=0 dev=0.04 ins=0.0 pro=7 1a=False 1b=False 2=True (7.6s)
Sep 10 18:17:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:17:48,630 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:17:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:17:48,753 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:17:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:17:55,734 main INFO screen S&P6900 pass=0 dev=0.0 ins=30.4 pro=6 1a=False 1b=False 2=True (7.2s)
Sep 10 18:18:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:18:22,243 main INFO screen Zencat pass=0 dev=1.74 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 10 18:18:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:18:35,103 main INFO screen HONOR⁠ pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (8.3s)
Sep 10 18:19:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:19:16,336 main INFO screen Zencat pass=0 dev=1.67 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 10 18:19:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:19:17,643 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:19:17 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
Sep 10 18:19:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:19:46,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:19:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:19:46,620 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:19:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:19:46,962 main INFO screen PAD pass=0 dev=0.0 ins=12.54 pro=18 1a=False 1b=False 2=True (0.6s)
Sep 10 18:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:19,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:19,136 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:20:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:25,707 main INFO screen NIKE pass=0 dev=0.0 ins=18.43 pro=3 1a=False 1b=False 2=True (6.8s)
Sep 10 18:20:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:51,458 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:20:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:52,081 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:20:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:57,966 main INFO screen $PANIC pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 10 18:20:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:20:59,342 main INFO screen ASS pass=0 dev=0.0 ins=44.96 pro=23 1a=False 1b=False 2=True (8.4s)
Sep 10 18:21:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:00,512 main INFO screen bliss pass=0 dev=3.43 ins=25.83 pro=64 1a=False 1b=False 2=True (11.1s)
Sep 10 18:21:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:04,096 main INFO screen GTAVICHICK pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 10 18:21:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:15,000 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:21:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:15,103 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:21:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:19,410 main INFO screen VIRGIN pass=0 dev=0.0 ins=42.25 pro=6 1a=False 1b=False 2=True (4.5s)
Sep 10 18:21:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:25,058 main INFO screen DOOYET pass=0 dev=1.79 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 10 18:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:38,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:38,702 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:21:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:21:38,891 main INFO screen AGI pass=0 dev=0.0 ins=21.2 pro=26 1a=False 1b=False 2=True (0.4s)
Sep 10 18:22:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:13,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:22:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:13,805 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:22:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:19,463 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (5.9s)
Sep 10 18:22:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:31,595 main INFO screen TDF pass=0 dev=5.06 ins=1.32 pro=26 1a=False 1b=True 2=False (8.3s)
Sep 10 18:22:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:39,230 main INFO screen LEGEND pass=0 dev=2.45 ins=0.0 pro=1 1a=False 1b=False 2=False (9.4s)
Sep 10 18:22:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:22:55,887 main INFO screen FERSPE pass=0 dev=3.45 ins=0.0 pro=1 1a=False 1b=False 2=False (6.1s)
Sep 10 18:23:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:09,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:23:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:09,343 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:23:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:13,190 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 18:23:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:15,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:23:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:15,883 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:23:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:21,785 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.3s)
Sep 10 18:23:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:23:55,660 main INFO screen RELAX pass=1 dev=2.72 ins=8.77 pro=64 1a=False 1b=False 2=False (9.1s)
Sep 10 18:24:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:03,361 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:24:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:03,492 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:24:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:08,078 main INFO screen TRENCHFLY pass=0 dev=0.0 ins=9.0 pro=14 1a=False 1b=False 2=True (4.8s)
Sep 10 18:24:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:14,132 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:24:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:14,261 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:24:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:19,322 main INFO screen GROKCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.3s)
Sep 10 18:24:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:24:37,104 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:24:37 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
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
