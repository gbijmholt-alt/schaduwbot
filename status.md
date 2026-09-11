# Schaduwbot status

- tijd: 2026-09-11 06:00:09 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 16 hours, 13 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 644/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 58312, "tokens_in_memory": 883, "msgs": 10089370, "trades": 1948350, "creates": 21612, "decode_fail": 127318, "rpc_calls": 32789, "rpc_errors": 3097, "sol_usd": 99.85914359759353, "open_positions": 35}
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
Sep 11 05:44:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:44:41,044 main INFO screen sdf pass=0 dev=12.49 ins=0.0 pro=7 1a=False 1b=True 2=False (2.9s)
Sep 11 05:45:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:01,778 main INFO screen VENOM pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 11 05:45:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:27,850 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:45:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:27,948 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:28,169 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:45:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:40,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:45:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:40,646 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:45:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:45:40,775 main INFO screen sdfsdfsdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 05:46:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:10,560 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:46:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:10,660 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:46:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:11,049 main INFO screen SYMBIENT pass=0 dev=0.0 ins=8.43 pro=5 1a=False 1b=False 2=True (0.6s)
Sep 11 05:46:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:29,535 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:46:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:29,631 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:46:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:29,822 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:46:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:46:40,784 main INFO screen GLP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.3s)
Sep 11 05:47:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:16,782 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:47:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:16,883 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:47:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:17,072 main INFO screen SIA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 05:47:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:28,570 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:47:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:28,698 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:47:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:28,818 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (0.3s)
Sep 11 05:47:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:32,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:47:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:32,347 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:47:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:32,481 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 05:47:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:47:56,938 main INFO screen USMS pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 05:49:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:03,020 rpc WARNING rpc getSignaturesForAddress exc
Sep 11 05:49:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:06,300 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (43.1s)
Sep 11 05:49:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:08,463 main INFO screen sdfsdf pass=0 dev=9.64 ins=0.0 pro=9 1a=False 1b=True 2=False (5.4s)
Sep 11 05:49:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:08,706 main INFO screen HONOR pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 11 05:49:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:25,459 main INFO screen ELLL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 11 05:49:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:37,070 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:49:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:49:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:45,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:49:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:45,978 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:49:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:48,768 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:49:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:48,895 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:49,071 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 05:49:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:49:52,490 main INFO screen Koinvase pass=0 dev=0.0 ins=9.26 pro=9 1a=False 1b=False 2=True (6.7s)
Sep 11 05:50:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:05,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:50:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:06,002 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:50:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:06,192 main INFO screen sdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (0.3s)
Sep 11 05:50:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:09,537 main INFO screen $AURA pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 05:50:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:24,161 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:50:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:24,323 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:50:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:50:25,532 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 11 05:51:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:51:12,334 main INFO screen PVE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 05:51:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:51:47,791 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:51:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:51:47,876 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:51:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:51:48,067 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (0.4s)
Sep 11 05:51:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:51:59,073 main INFO screen USMS pass=0 dev=1.25 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 05:52:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:52:12,201 main INFO screen BMOON pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.0s)
Sep 11 05:52:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:52:14,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:52:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:52:14,317 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:52:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:52:14,434 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 05:54:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:54:25,300 main INFO screen USMS pass=0 dev=23.34 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 05:54:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:54:28,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:54:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:54:28,358 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:54:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:54:28,466 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (0.3s)
Sep 11 05:55:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:55:08,103 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:55:08 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:55:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:55:50,822 main INFO screen FLYLON pass=0 dev=22.15 ins=9.6 pro=26 1a=False 1b=False 2=False (3.3s)
Sep 11 05:56:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:56:12,212 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:56:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:56:12,346 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:56:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:56:12,587 main INFO screen Nasbrain pass=0 dev=0.0 ins=78.99 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 05:56:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:56:40,430 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:56:40 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 05:56:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:56:40,795 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:56:40 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 05:57:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:57:03,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:57:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:57:03,571 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:57:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:57:03,753 main INFO screen COST pass=0 dev=0.0 ins=75.89 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 11 05:57:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:57:47,818 main INFO screen power pass=0 dev=0.31 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 05:58:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:58:09,040 main INFO screen THERA pass=0 dev=2.15 ins=0.0 pro=2 1a=False 1b=False 2=False (1.4s)
Sep 11 05:58:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:58:16,158 main INFO screen whale pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 05:58:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:58:55,593 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:58:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:58:55,687 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:58:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:58:55,879 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:59:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:28,574 aiohttp.access INFO 45.135.193.198 [11/Sep/2026:05:59:28 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 05:59:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:28,599 aiohttp.access INFO 45.135.193.198 [11/Sep/2026:05:59:28 +0000] "GET / HTTP/1.0" 404 174 "-" "0day"
Sep 11 05:59:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:39,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:40,119 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:40,275 main INFO screen NVIDOG pass=0 dev=0.0 ins=77.57 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 05:59:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:59:42,137 main INFO screen 100 pass=0 dev=14.39 ins=0.0 pro=2 1a=False 1b=False 2=True (1.7s)
Sep 11 06:00:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:00:09,350 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:00:09 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
