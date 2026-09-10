# Schaduwbot status

- tijd: 2026-09-10 21:17:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 7 hours, 30 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 633/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 26940, "tokens_in_memory": 1566, "msgs": 5494850, "trades": 990562, "creates": 10983, "decode_fail": 77236, "rpc_calls": 16404, "rpc_errors": 1677, "sol_usd": 100.03454068607513, "open_positions": 89}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 20:48 UTC

Gelogde schaduwtrades: **8017**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 10222 | 1462 | 27 | 1462 | 144 | 2707 | 8017 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 115 | 14% | 2.6% | +35.7% | -17.2% | -9.86% | 91% |
| dip35_V1_gescreend_fail | 790 | 26% | 4.4% | +46.2% | -26.1% | -6.97% | 100% |
| dip35_V1_alle | 936 | 25% | 4.4% | +44.5% | -25.3% | -7.78% | 100% |
| dip35_V2_gescreend_pass | 113 | 16% | 2.7% | +30.1% | -21.8% | -13.56% | 96% |
| dip35_V2_gescreend_fail | 789 | 24% | 5.2% | +53.7% | -28.3% | -8.52% | 100% |
| dip35_V2_alle | 925 | 23% | 5.1% | +50.8% | -27.8% | -9.69% | 100% |
| dip35_V3_gescreend_pass | 113 | 4% | 2.7% | +75.2% | -23.2% | -18.83% | 99% |
| dip35_V3_gescreend_fail | 803 | 12% | 6.2% | +112.2% | -29.8% | -12.66% | 100% |
| dip35_V3_alle | 937 | 11% | 6.0% | +106.5% | -29.3% | -13.91% | 100% |
| dip40_V1_gescreend_pass | 105 | 15% | 2.9% | +42.9% | -16.1% | -7.08% | 84% |
| dip40_V1_gescreend_fail | 767 | 26% | 4.8% | +50.5% | -26.3% | -6.59% | 100% |
| dip40_V1_alle | 896 | 25% | 4.6% | +48.9% | -25.2% | -6.87% | 100% |
| dip40_V2_gescreend_pass | 103 | 14% | 2.9% | +48.7% | -21.1% | -11.57% | 94% |
| dip40_V2_gescreend_fail | 768 | 25% | 5.3% | +55.6% | -28.6% | -7.91% | 100% |
| dip40_V2_alle | 886 | 23% | 5.1% | +54.4% | -27.9% | -8.67% | 100% |
| dip40_V3_gescreend_pass | 104 | 7% | 2.9% | +57.1% | -22.3% | -17.00% | 98% |
| dip40_V3_gescreend_fail | 783 | 12% | 6.5% | +94.2% | -30.0% | -15.28% | 100% |
| dip40_V3_alle | 900 | 11% | 6.1% | +89.2% | -29.3% | -15.76% | 100% |
| dip45_V1_gescreend_pass | 94 | 13% | 4.3% | +44.4% | -16.2% | -8.50% | 87% |
| dip45_V1_gescreend_fail | 735 | 27% | 4.2% | +52.6% | -25.7% | -4.52% | 100% |
| dip45_V1_alle | 848 | 26% | 4.2% | +51.7% | -24.8% | -5.29% | 100% |
| dip45_V2_gescreend_pass | 92 | 16% | 4.3% | +42.8% | -20.2% | -9.91% | 89% |
| dip45_V2_gescreend_fail | 732 | 25% | 4.8% | +65.2% | -27.9% | -4.63% | 100% |
| dip45_V2_alle | 837 | 24% | 4.8% | +62.9% | -27.2% | -5.58% | 100% |
| dip45_V3_gescreend_pass | 93 | 6% | 4.3% | +108.1% | -21.1% | -12.77% | 96% |
| dip45_V3_gescreend_fail | 748 | 13% | 6.1% | +120.1% | -29.4% | -10.17% | 100% |
| dip45_V3_alle | 852 | 12% | 6.0% | +117.3% | -28.6% | -10.80% | 100% |

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
Sep 10 21:04:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:04:48,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:04:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:04:48,684 main INFO screen DOG pass=0 dev=0.0 ins=12.98 pro=13 1a=False 1b=False 2=True (0.3s)
Sep 10 21:04:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:04:49,872 main INFO screen Solaners pass=0 dev=0.0 ins=21.2 pro=22 1a=False 1b=False 2=True (6.4s)
Sep 10 21:05:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:42,287 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (8.7s)
Sep 10 21:05:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:48,939 main INFO screen pump pass=1 dev=0.0 ins=0.0 pro=46 1a=False 1b=False 2=False (8.0s)
Sep 10 21:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:56,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:56,448 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:56,916 main INFO screen X pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 10 21:05:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:05:58,465 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 10 21:06:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:06:25,886 main INFO screen S&P500 pass=0 dev=0.88 ins=19.49 pro=11 1a=False 1b=False 2=True (8.6s)
Sep 10 21:07:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:07:12,283 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:07:12 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 21:07:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:07:33,586 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:07:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:07:33,681 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:07:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:07:40,220 main INFO screen bnbcat pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (6.7s)
Sep 10 21:08:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:08:12,362 aiohttp.access INFO 89.42.231.200 [10/Sep/2026:21:08:12 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 10 21:09:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:01,881 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:09:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:02,547 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:09:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:04,049 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:09:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:04,171 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:09:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:09,495 main INFO screen WENDY pass=0 dev=0.0 ins=9.44 pro=20 1a=False 1b=False 2=True (7.8s)
Sep 10 21:09:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:09,689 main INFO screen AIO pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 10 21:09:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:10,637 main INFO screen CASHCAT pass=0 dev=0.0 ins=79.17 pro=6 1a=False 1b=False 2=True (6.7s)
Sep 10 21:09:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:18,847 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:09:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:18,930 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:09:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:23,712 main INFO screen startpup pass=0 dev=0.0 ins=22.05 pro=14 1a=False 1b=False 2=True (4.9s)
Sep 10 21:09:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:35,652 main INFO screen $Burger pass=0 dev=1.68 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 10 21:09:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:37,851 main INFO screen SPCX pass=1 dev=0.0 ins=16.36 pro=14 1a=False 1b=False 2=False (5.0s)
Sep 10 21:09:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:44,037 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:09:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:44,129 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:09:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:48,959 main INFO screen JUGGBULL pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (5.0s)
Sep 10 21:09:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:59,011 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:09:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:09:59,147 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:10:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:02,617 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 10 21:10:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:15,608 main INFO screen BRR pass=0 dev=1.12 ins=0.0 pro=3 1a=False 1b=False 2=False (5.9s)
Sep 10 21:10:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:19,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:10:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:19,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:10:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:23,896 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 10 21:10:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:49,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:10:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:50,022 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:10:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:10:53,428 main INFO screen UNC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.6s)
Sep 10 21:12:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:12:12,656 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:12:12 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 21:12:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:12:54,801 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:12:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:12:54,904 main INFO screen 45 pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 10 21:12:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:12:54,920 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:12:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:12:58,800 main INFO screen sol pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=True (6.3s)
Sep 10 21:13:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:01,437 main INFO screen Nole pass=0 dev=0.0 ins=21.05 pro=6 1a=False 1b=False 2=True (6.7s)
Sep 10 21:13:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:15,013 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:13:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:15,112 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:13:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:20,389 main INFO screen Meowcraft pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 10 21:13:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:46,192 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:13:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:46,282 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:13:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:50,666 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 10 21:13:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:13:56,341 main INFO screen CHOKGLAZE pass=0 dev=34.09 ins=0.51 pro=2 1a=False 1b=False 2=True (7.0s)
Sep 10 21:14:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:14:24,965 main INFO screen BUBBLE pass=0 dev=0.25 ins=0.0 pro=4 1a=False 1b=False 2=False (7.1s)
Sep 10 21:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:14:26,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:14:26,495 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:14:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:14:31,288 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.0s)
Sep 10 21:14:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:14:56,628 main INFO screen DOOB pass=0 dev=6.56 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 10 21:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:08,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:08,596 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:15:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:12,377 main INFO screen Starbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 10 21:15:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:22,650 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:15:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:22,785 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:15:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:29,699 main INFO screen BOF pass=0 dev=0.0 ins=21.23 pro=11 1a=False 1b=False 2=True (7.1s)
Sep 10 21:15:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:15:52,641 main INFO screen lol pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 10 21:16:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:11,340 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:16:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:11,432 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:16:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:15,332 main INFO screen BTA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.1s)
Sep 10 21:16:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:21,956 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:16:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:22,124 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:16:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:28,332 main INFO screen gork pass=0 dev=0.0 ins=25.21 pro=8 1a=False 1b=False 2=True (6.4s)
Sep 10 21:16:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:33,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:16:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:33,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:16:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:37,977 main INFO screen gork pass=0 dev=0.0 ins=24.78 pro=9 1a=False 1b=False 2=True (4.8s)
Sep 10 21:16:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:59,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:16:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:16:59,764 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:17:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:17:03,720 main INFO screen Rocket pass=0 dev=0.0 ins=15.04 pro=3 1a=False 1b=False 2=True (4.5s)
Sep 10 21:17:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:17:04,139 main INFO screen hittit pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 10 21:17:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:17:16,134 main INFO screen DOOB pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 10 21:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:17:17,729 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:17:17 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
