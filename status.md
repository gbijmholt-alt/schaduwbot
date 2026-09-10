# Schaduwbot status

- tijd: 2026-09-10 22:04:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 8 hours, 17 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 634/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 29758, "tokens_in_memory": 1587, "msgs": 6024745, "trades": 1119042, "creates": 12244, "decode_fail": 87071, "rpc_calls": 18622, "rpc_errors": 1853, "sol_usd": 99.85285079007974, "open_positions": 78}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 21:48 UTC

Gelogde schaduwtrades: **9333**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 11848 | 1695 | 28 | 1695 | 157 | 3131 | 9333 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 124 | 16% | 2.4% | +37.8% | -17.5% | -8.56% | 92% |
| dip35_V1_gescreend_fail | 929 | 27% | 4.5% | +46.5% | -26.2% | -6.89% | 100% |
| dip35_V1_alle | 1088 | 26% | 4.5% | +45.0% | -25.5% | -7.57% | 100% |
| dip35_V2_gescreend_pass | 123 | 18% | 3.3% | +30.6% | -22.5% | -13.03% | 97% |
| dip35_V2_gescreend_fail | 930 | 24% | 5.2% | +55.3% | -28.2% | -8.04% | 100% |
| dip35_V2_alle | 1080 | 23% | 5.2% | +52.3% | -27.9% | -9.20% | 100% |
| dip35_V3_gescreend_pass | 123 | 6% | 3.3% | +155.3% | -23.6% | -13.44% | 99% |
| dip35_V3_gescreend_fail | 940 | 12% | 6.6% | +133.0% | -30.0% | -10.61% | 100% |
| dip35_V3_alle | 1088 | 11% | 6.4% | +130.2% | -29.6% | -11.50% | 100% |
| dip40_V1_gescreend_pass | 112 | 15% | 2.7% | +43.8% | -16.4% | -7.26% | 87% |
| dip40_V1_gescreend_fail | 898 | 26% | 4.6% | +50.4% | -26.1% | -6.55% | 100% |
| dip40_V1_alle | 1038 | 25% | 4.4% | +49.1% | -25.2% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 111 | 14% | 2.7% | +47.2% | -21.1% | -11.23% | 94% |
| dip40_V2_gescreend_fail | 902 | 24% | 5.0% | +57.2% | -28.2% | -7.29% | 100% |
| dip40_V2_alle | 1032 | 23% | 4.8% | +55.8% | -27.6% | -8.12% | 100% |
| dip40_V3_gescreend_pass | 112 | 7% | 2.7% | +130.9% | -22.2% | -11.30% | 98% |
| dip40_V3_gescreend_fail | 915 | 12% | 6.3% | +116.0% | -29.8% | -12.74% | 100% |
| dip40_V3_alle | 1044 | 11% | 6.0% | +114.3% | -29.2% | -12.95% | 100% |
| dip45_V1_gescreend_pass | 101 | 13% | 4.0% | +45.5% | -16.6% | -8.60% | 90% |
| dip45_V1_gescreend_fail | 867 | 27% | 3.9% | +52.9% | -25.4% | -4.20% | 100% |
| dip45_V1_alle | 989 | 26% | 4.0% | +52.0% | -24.6% | -5.02% | 100% |
| dip45_V2_gescreend_pass | 100 | 17% | 4.0% | +42.1% | -20.3% | -9.67% | 90% |
| dip45_V2_gescreend_fail | 866 | 25% | 4.4% | +65.1% | -27.5% | -4.05% | 100% |
| dip45_V2_alle | 981 | 24% | 4.5% | +62.9% | -26.9% | -5.03% | 100% |
| dip45_V3_gescreend_pass | 101 | 7% | 4.0% | +185.1% | -21.1% | -6.79% | 96% |
| dip45_V3_gescreend_fail | 879 | 12% | 6.0% | +139.9% | -29.2% | -8.07% | 100% |
| dip45_V3_alle | 993 | 12% | 5.9% | +140.4% | -28.6% | -8.33% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 21:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:33,243 main INFO screen GTA6Coin pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 21:51:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:59,783 main INFO screen MEMEFACTORY pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 21:52:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:05,972 main INFO screen CATE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 10 21:52:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:10,815 main INFO screen BULLISH pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (3.5s)
Sep 10 21:52:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:26,631 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:26,890 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:27,089 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 10 21:52:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:27,486 main INFO screen anorchia pass=0 dev=0.0 ins=19.99 pro=57 1a=False 1b=False 2=True (3.2s)
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,348 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,513 main INFO screen HAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,824 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,931 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:43,228 main INFO screen DERP pass=0 dev=9.55 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 21:52:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:52,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:53,088 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:53,215 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,830 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,943 main INFO screen ELON pass=0 dev=0.0 ins=20.69 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 21:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:11,602 main INFO screen BROKE pass=0 dev=0.3 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 10 21:53:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:28,262 main INFO screen DGCOIN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 10 21:53:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:29,586 main INFO screen Orlando pass=0 dev=0.0 ins=17.3 pro=13 1a=False 1b=False 2=True (2.1s)
Sep 10 21:53:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:39,162 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 21:54:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:01,098 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:54:01 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 10 21:54:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:01,939 main INFO screen $GCCH pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 10 21:54:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:07,927 main INFO screen WAFFLE pass=0 dev=0.0 ins=23.73 pro=22 1a=False 1b=False 2=False (1.6s)
Sep 10 21:54:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:14,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:54:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:14,315 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:54:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:14,466 main INFO screen DEGEN pass=0 dev=0.0 ins=22.28 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 10 21:55:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:02,724 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:55:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:02,868 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:55:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:03,049 main INFO screen monkdog pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 21:55:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:10,976 main INFO screen NUGGET pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 10 21:55:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:27,171 main INFO screen TONTIN pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=True (4.5s)
Sep 10 21:55:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:29,107 main INFO screen RAJPUTIN pass=0 dev=0.0 ins=16.83 pro=57 1a=False 1b=False 2=True (6.1s)
Sep 10 21:55:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:55:45,195 main INFO screen DEGEN pass=0 dev=6.63 ins=16.62 pro=30 1a=False 1b=False 2=False (1.3s)
Sep 10 21:56:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:56:05,104 main INFO screen swerv pass=0 dev=12.49 ins=3.47 pro=10 1a=False 1b=False 2=False (2.4s)
Sep 10 21:56:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:56:41,834 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:56:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:56:41,929 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:56:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:56:42,129 main INFO screen INVESTOOOR pass=0 dev=0.0 ins=19.94 pro=25 1a=False 1b=False 2=True (0.4s)
Sep 10 21:57:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:57:27,887 main INFO screen FERSPE pass=0 dev=0.16 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 10 21:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:58:14,394 main INFO screen niki pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.1s)
Sep 10 21:58:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:58:16,209 main INFO screen TIKTOK pass=1 dev=0.0 ins=0.84 pro=26 1a=False 1b=False 2=False (5.5s)
Sep 10 21:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:58:38,945 main INFO screen DOOM pass=0 dev=35.01 ins=0.0 pro=15 1a=False 1b=False 2=True (1.1s)
Sep 10 21:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:58:47,172 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.2s)
Sep 10 21:58:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:58:52,236 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 10 21:59:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:59:07,242 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:59:07 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 21:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:59:40,054 main INFO screen LCAICOIN pass=0 dev=0.94 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 10 21:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:59:40,205 main INFO screen DGS pass=0 dev=0.85 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 10 22:00:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:00:39,060 main INFO screen RISE pass=0 dev=39.8 ins=0.0 pro=6 1a=False 1b=False 2=True (9.1s)
Sep 10 22:01:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:01,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:01:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:01,412 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:01:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:02,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:01:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:02,594 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:01:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:07,730 main INFO screen Ahegao pass=0 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=True (6.5s)
Sep 10 22:01:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:09,798 main INFO screen ALL pass=0 dev=0.0 ins=30.46 pro=16 1a=False 1b=False 2=True (7.4s)
Sep 10 22:01:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:38,349 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:01:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:38,445 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:01:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:39,409 main INFO screen Freebots pass=0 dev=0.0 ins=23.6 pro=7 1a=False 1b=False 2=True (1.2s)
Sep 10 22:01:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:01:55,448 main INFO screen MOON pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 10 22:02:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:09,999 main INFO screen CHAROC pass=0 dev=0.83 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 10 22:02:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:40,340 main INFO screen goat milk pass=0 dev=6.12 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 10 22:02:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:40,897 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:02:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:41,022 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:02:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:45,488 main INFO screen PEPEX pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.7s)
Sep 10 22:02:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:47,750 main INFO screen PATRICK pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 10 22:02:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:53,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:02:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:53,262 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:02:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:02:53,405 main INFO screen DEVIN pass=0 dev=0.0 ins=10.82 pro=14 1a=False 1b=False 2=True (0.3s)
Sep 10 22:03:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:31,920 main INFO screen ANGELS pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 10 22:03:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:35,250 main INFO screen FRIES pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 10 22:03:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:56,608 main INFO screen PATRICK pass=0 dev=0.07 ins=0.0 pro=3 1a=False 1b=False 2=False (9.2s)
Sep 10 22:03:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:57,161 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:03:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:57,287 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:03:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:03:58,803 main INFO screen bison pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 10 22:04:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:04:02,407 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.3s)
Sep 10 22:04:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:04:06,490 main INFO screen NEIL pass=0 dev=0.0 ins=17.58 pro=7 1a=False 1b=False 2=False (5.7s)
Sep 10 22:04:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:04:15,140 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:04:15 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
