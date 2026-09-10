# Schaduwbot status

- tijd: 2026-09-10 21:02:04 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 7 hours, 15 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 634/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 26027, "tokens_in_memory": 1516, "msgs": 5360566, "trades": 953242, "creates": 10572, "decode_fail": 73199, "rpc_calls": 16001, "rpc_errors": 1619, "sol_usd": 100.09622983573115, "open_positions": 67}
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
Sep 10 20:50:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:29,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:50:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:29,856 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:30,184 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=13.27 pro=19 1a=False 1b=False 2=True (0.5s)
Sep 10 20:50:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:34,651 main INFO screen XRPp pass=0 dev=0.03 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 20:50:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:38,809 main INFO screen OIL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 10 20:50:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:50,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:50:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:51,057 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:50:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:50:51,186 main INFO screen DIAMOND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 20:51:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:51:11,593 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:51:11 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 10 20:52:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:08,765 main INFO screen ANBU pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 10 20:52:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:13,130 main INFO screen XRPp pass=0 dev=0.01 ins=0.0 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 10 20:52:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:21,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:52:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:22,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:52:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:22,210 main INFO screen BTC pass=0 dev=0.0 ins=6.92 pro=29 1a=False 1b=False 2=True (0.3s)
Sep 10 20:52:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:25,774 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:52:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:25,843 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:52:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:26,010 main INFO screen DOG pass=0 dev=0.0 ins=30.41 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 10 20:52:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:30,662 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:52:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:30,772 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:52:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:30,933 main INFO screen JPM pass=0 dev=0.0 ins=23.5 pro=11 1a=False 1b=False 2=True (0.3s)
Sep 10 20:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:39,340 main INFO screen PSYCHO pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 10 20:52:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:40,306 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:52:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:40,413 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:52:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:40,557 main INFO screen HONOR pass=0 dev=0.0 ins=17.66 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 10 20:52:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:42,060 main INFO screen DWBI pass=1 dev=0.0 ins=17.84 pro=21 1a=False 1b=False 2=False (1.5s)
Sep 10 20:52:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:44,843 main INFO screen PC pass=0 dev=15.17 ins=0.01 pro=5 1a=False 1b=False 2=False (2.2s)
Sep 10 20:52:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:47,923 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:48,030 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:52:48,352 main INFO screen LIZARD pass=1 dev=0.0 ins=17.59 pro=28 1a=False 1b=False 2=False (0.5s)
Sep 10 20:53:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:32,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:53:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:33,091 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:53:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:33,265 main INFO screen ICAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 20:53:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:37,026 main INFO screen $CAJUN pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=True (1.8s)
Sep 10 20:53:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:44,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:53:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:44,651 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:53:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:44,767 main INFO screen GAS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 20:53:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:55,837 main INFO screen DOOB pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (4.4s)
Sep 10 20:53:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:53:57,085 main INFO screen Factory pass=0 dev=0.0 ins=10.8 pro=73 1a=False 1b=False 2=True (4.1s)
Sep 10 20:54:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:04,859 main INFO screen DIAMOND pass=0 dev=2.4 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 20:54:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:10,864 main INFO screen MELON pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 10 20:54:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:12,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:54:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:12,229 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:54:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:12,373 main INFO screen BTC pass=0 dev=0.0 ins=9.46 pro=31 1a=False 1b=False 2=True (0.3s)
Sep 10 20:54:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:22,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:23,012 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:23,506 main INFO screen JUGWHALE pass=0 dev=0.0 ins=79.13 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 10 20:54:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:27,539 main INFO screen BABYCATE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 10 20:54:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:54:59,265 main INFO screen 🇩🇪 pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.3s)
Sep 10 20:55:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:04,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:55:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:04,447 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:55:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:04,559 main INFO screen ZCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 20:55:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:40,194 main INFO screen FROG pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 20:55:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:42,832 main INFO screen BTC pass=0 dev=0.0 ins=20.27 pro=62 1a=False 1b=False 2=True (3.0s)
Sep 10 20:55:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:51,488 main INFO screen FACTORY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.6s)
Sep 10 20:55:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:55:53,124 main INFO screen Caton pass=0 dev=0.0 ins=15.67 pro=65 1a=False 1b=False 2=True (4.5s)
Sep 10 20:56:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:56:37,138 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:56:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 20:57:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:57:26,987 main INFO screen FATCAAT pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 10 20:57:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:57:36,168 main INFO screen $CAJUN pass=0 dev=0.33 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 10 20:58:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:09,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:58:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:09,965 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:58:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:10,188 main INFO screen KITSY pass=0 dev=0.0 ins=41.39 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 20:58:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:11,925 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:12,734 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:12,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:58:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:13,298 main INFO screen CopyCat pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=True (1.6s)
Sep 10 20:58:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:13,562 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:58:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:13,809 main INFO screen TSLA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.5s)
Sep 10 20:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:58:14,720 main INFO screen 100K pass=0 dev=4.04 ins=0.0 pro=6 1a=False 1b=False 2=False (3.2s)
Sep 10 20:59:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:01,136 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:59:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:01,189 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:59:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:01,409 main INFO screen Claude pass=0 dev=0.0 ins=21.72 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 10 20:59:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:12,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:59:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:12,277 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:59:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:12,445 main INFO screen DOG pass=1 dev=0.0 ins=17.59 pro=26 1a=False 1b=False 2=False (0.4s)
Sep 10 20:59:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:51,143 main INFO screen RISE pass=0 dev=38.34 ins=0.0 pro=7 1a=False 1b=False 2=True (3.0s)
Sep 10 20:59:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:59:51,609 main INFO screen LICK pass=0 dev=2.37 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 10 21:00:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:00:22,880 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:00:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:00:22,960 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:00:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:00:29,345 main INFO screen stankmemes pass=0 dev=0.0 ins=20.55 pro=10 1a=False 1b=False 2=True (6.6s)
Sep 10 21:02:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:02:04,454 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:02:04 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
