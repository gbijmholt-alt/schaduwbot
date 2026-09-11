# Schaduwbot status

- tijd: 2026-09-11 06:15:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 16 hours, 28 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 647/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 59240, "tokens_in_memory": 960, "msgs": 10156976, "trades": 1966610, "creates": 21869, "decode_fail": 128443, "rpc_calls": 33198, "rpc_errors": 3161, "sol_usd": 99.90490763787007, "open_positions": 52}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 05:48 UTC

Gelogde schaduwtrades: **17399**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 6416 | 838 | 7 | 838 | 85 | 1679 | 5044 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 230 | 15% | 1.7% | +41.5% | -16.4% | -7.62% | 98% |
| dip35_V1_gescreend_fail | 1725 | 27% | 3.9% | +45.5% | -25.8% | -6.70% | 100% |
| dip35_V1_alle | 2015 | 26% | 4.0% | +44.4% | -25.0% | -7.17% | 100% |
| dip35_V2_gescreend_pass | 231 | 17% | 2.2% | +41.5% | -21.2% | -10.31% | 100% |
| dip35_V2_gescreend_fail | 1738 | 25% | 4.7% | +55.3% | -28.1% | -7.45% | 100% |
| dip35_V2_alle | 2010 | 24% | 4.6% | +53.5% | -27.6% | -8.26% | 100% |
| dip35_V3_gescreend_pass | 231 | 7% | 2.6% | +141.2% | -23.2% | -11.79% | 100% |
| dip35_V3_gescreend_fail | 1743 | 13% | 6.2% | +112.8% | -30.0% | -11.71% | 100% |
| dip35_V3_alle | 2013 | 12% | 6.0% | +111.9% | -29.4% | -12.15% | 100% |
| dip40_V1_gescreend_pass | 214 | 13% | 1.9% | +43.7% | -15.9% | -8.36% | 98% |
| dip40_V1_gescreend_fail | 1676 | 26% | 3.9% | +48.1% | -25.7% | -6.40% | 100% |
| dip40_V1_alle | 1935 | 25% | 3.8% | +47.0% | -24.8% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 214 | 13% | 1.9% | +48.9% | -19.9% | -10.92% | 100% |
| dip40_V2_gescreend_fail | 1685 | 25% | 4.3% | +56.5% | -27.9% | -6.79% | 100% |
| dip40_V2_alle | 1928 | 24% | 4.2% | +55.5% | -27.1% | -7.67% | 100% |
| dip40_V3_gescreend_pass | 214 | 6% | 2.3% | +116.7% | -21.8% | -13.42% | 100% |
| dip40_V3_gescreend_fail | 1691 | 13% | 5.7% | +103.3% | -29.7% | -12.67% | 100% |
| dip40_V3_alle | 1932 | 12% | 5.5% | +102.4% | -29.0% | -13.11% | 100% |
| dip45_V1_gescreend_pass | 203 | 15% | 2.0% | +52.2% | -15.7% | -5.63% | 95% |
| dip45_V1_gescreend_fail | 1625 | 28% | 3.4% | +49.5% | -25.3% | -4.46% | 100% |
| dip45_V1_alle | 1858 | 26% | 3.4% | +49.4% | -24.3% | -4.83% | 100% |
| dip45_V2_gescreend_pass | 202 | 19% | 2.5% | +52.0% | -19.6% | -6.16% | 97% |
| dip45_V2_gescreend_fail | 1629 | 26% | 3.8% | +60.4% | -27.2% | -4.66% | 100% |
| dip45_V2_alle | 1852 | 25% | 3.8% | +59.4% | -26.5% | -5.16% | 100% |
| dip45_V3_gescreend_pass | 202 | 7% | 3.0% | +198.9% | -20.9% | -5.68% | 99% |
| dip45_V3_gescreend_fail | 1635 | 14% | 5.4% | +112.0% | -29.0% | -9.59% | 100% |
| dip45_V3_alle | 1856 | 13% | 5.3% | +115.7% | -28.3% | -9.48% | 100% |

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
Sep 11 06:04:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:04:40,154 main INFO screen THE pass=0 dev=1.27 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 11 06:05:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:00,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:05:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:00,347 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:05:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:06,377 main INFO screen sfdfds pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.2s)
Sep 11 06:05:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:11,954 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:05:11 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:05:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:39,406 main INFO screen ASSDAQ pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 11 06:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:56,201 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:05:56,290 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:06:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:06:02,854 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (6.8s)
Sep 11 06:06:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:06:39,097 main INFO screen HAM pass=0 dev=3.32 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 06:07:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:07:42,985 main INFO screen ape pass=1 dev=3.76 ins=0.0 pro=35 1a=False 1b=False 2=False (9.5s)
Sep 11 06:07:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:07:54,672 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:07:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:07:54,765 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:08:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:01,807 main INFO screen dfdsfds pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (7.2s)
Sep 11 06:08:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:26,661 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:08:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:26,723 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:08:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:32,616 main INFO screen EYE pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (5.3s)
Sep 11 06:08:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:33,770 main INFO screen USOH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 11 06:08:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:47,823 main INFO screen wind pass=0 dev=7.19 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 06:08:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:08:54,542 main INFO screen power pass=0 dev=0.29 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 06:09:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:09:48,823 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:09:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:09:48,915 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:09:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:09:52,737 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 06:10:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:17,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:10:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:17,468 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:10:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:17,510 main INFO screen NMS pass=0 dev=0.14 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 11 06:10:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:22,393 main INFO screen sfdfds pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 11 06:10:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:36,533 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:10:36 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:10:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:10:42,219 main INFO screen DERP pass=0 dev=1.71 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 11 06:11:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:01,779 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:11:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:01,948 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:11:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:02,150 main INFO screen Gold pass=0 dev=0.0 ins=16.27 pro=41 1a=False 1b=False 2=True (0.4s)
Sep 11 06:11:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:04,072 main INFO screen MOLT pass=0 dev=1.98 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 11 06:11:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:07,661 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:11:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:07,787 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:11:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:12,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:11:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:13,015 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:11:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:14,434 main INFO screen sfdfds pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 06:11:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:11:17,449 main INFO screen SKRYPTO pass=0 dev=0.0 ins=15.86 pro=7 1a=False 1b=False 2=True (4.6s)
Sep 11 06:12:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:00,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:12:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:00,245 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:12:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:06,839 main INFO screen sdf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 06:12:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:52,969 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:12:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:53,070 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:12:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:12:56,443 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.6s)
Sep 11 06:13:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:21,404 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:13:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:21,455 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:13:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:25,067 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:13:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:25,173 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:13:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:26,979 main INFO screen fsdfsd pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.7s)
Sep 11 06:13:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:31,093 main INFO screen MASK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.1s)
Sep 11 06:13:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:35,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:13:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:35,186 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:13:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:35,334 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 06:13:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:46,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:13:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:47,015 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:13:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:13:53,559 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 11 06:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:18,273 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:18,324 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:18,564 main INFO screen shitcoin pass=0 dev=0.0 ins=28.09 pro=47 1a=False 1b=False 2=True (0.4s)
Sep 11 06:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:18,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:18,744 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:14:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:20,949 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:14:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:21,078 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:14:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:22,915 main INFO screen dffsd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.5s)
Sep 11 06:14:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:25,132 main INFO screen EGEAR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.3s)
Sep 11 06:14:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:34,066 main INFO screen Penny pass=0 dev=0.0 ins=9.31 pro=73 1a=False 1b=False 2=True (4.2s)
Sep 11 06:14:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:44,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:14:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:44,454 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:14:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:14:49,483 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 11 06:15:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:02,377 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:15:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:02,480 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:15:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:07,075 main INFO screen sdffds pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.8s)
Sep 11 06:15:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:17,802 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:15:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:17,956 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:15:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:18,046 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 06:15:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:27,791 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:15:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:27,918 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:15:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:32,412 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 11 06:15:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:15:37,078 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:15:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
