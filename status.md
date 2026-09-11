# Schaduwbot status

- tijd: 2026-09-11 05:49:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 16 hours, 2 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 644/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 57680, "tokens_in_memory": 870, "msgs": 10051494, "trades": 1933885, "creates": 21420, "decode_fail": 126962, "rpc_calls": 32565, "rpc_errors": 3075, "sol_usd": 99.77979383506549, "open_positions": 52}
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
Sep 11 05:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:34:39,724 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:34:39,814 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:34:40,001 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:34:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:34:52,479 main INFO screen beer pass=0 dev=3.65 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 05:35:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:14,540 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:05:35:14 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 05:35:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:18,704 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:35:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:18,959 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:35:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:19,142 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (0.8s)
Sep 11 05:35:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:19,331 main INFO screen $AURA pass=0 dev=4.99 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 05:35:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:35:50,615 main INFO screen VENOM pass=0 dev=0.86 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 05:36:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:36:07,948 main INFO screen Mar1o pass=0 dev=17.88 ins=0.0 pro=7 1a=False 1b=False 2=True (3.8s)
Sep 11 05:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:36:26,513 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:36:26,611 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:36:26,786 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 05:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:37:17,635 main INFO screen CHAROC pass=0 dev=5.04 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 05:37:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:37:57,292 main INFO screen KSHMIR pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 05:38:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:38:28,285 main INFO screen RICH pass=0 dev=0.0 ins=18.67 pro=68 1a=False 1b=False 2=True (3.2s)
Sep 11 05:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:02,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:02,522 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:02,716 main INFO screen FLYTRUMP pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 05:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:03,682 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:39:03 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:03,742 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:03,867 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:03,986 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 05:39:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:07,875 main INFO screen fds pass=0 dev=6.64 ins=0.0 pro=8 1a=False 1b=False 2=False (3.1s)
Sep 11 05:39:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:20,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:39:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:20,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:39:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:20,706 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 05:39:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:22,222 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:39:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:22,356 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:39:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:22,482 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 05:39:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:40,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:39:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:40,937 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:39:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:41,208 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:39:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:39:53,694 main INFO screen dfasd pass=0 dev=6.63 ins=0.0 pro=9 1a=False 1b=False 2=False (3.0s)
Sep 11 05:40:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:40:08,170 main INFO screen BUZZFLY pass=1 dev=0.0 ins=11.65 pro=16 1a=False 1b=False 2=False (3.8s)
Sep 11 05:42:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:05,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:42:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:05,359 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:42:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:05,585 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:42:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:18,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:42:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:18,893 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:42:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:19,015 main INFO screen NVIDOG pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 05:42:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:42:51,651 main INFO screen casino pass=0 dev=21.69 ins=1.38 pro=7 1a=False 1b=False 2=True (3.9s)
Sep 11 05:43:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:43:04,274 main INFO screen 100 pass=0 dev=3.43 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 05:43:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:43:45,501 main INFO screen CHAAGE pass=0 dev=1.73 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 05:44:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:44:12,245 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:44:12 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:44:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:44:35,534 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:44:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:44:35,631 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:44:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:44:36,004 main INFO screen FLYPAD pass=1 dev=0.0 ins=11.28 pro=17 1a=False 1b=False 2=False (0.6s)
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
