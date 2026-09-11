# Schaduwbot status

- tijd: 2026-09-11 05:44:12 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 15 hours, 57 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 647/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 57355, "tokens_in_memory": 951, "msgs": 10038635, "trades": 1926028, "creates": 21348, "decode_fail": 126265, "rpc_calls": 32395, "rpc_errors": 3058, "sol_usd": 99.82808632685746, "open_positions": 42}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 04:48 UTC

Gelogde schaduwtrades: **16659**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 5534 | 699 | 5 | 700 | 79 | 1422 | 4304 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 223 | 15% | 1.3% | +42.7% | -16.0% | -7.06% | 98% |
| dip35_V1_gescreend_fail | 1650 | 26% | 4.1% | +45.2% | -25.7% | -7.22% | 100% |
| dip35_V1_alle | 1930 | 25% | 4.0% | +44.2% | -24.9% | -7.58% | 100% |
| dip35_V2_gescreend_pass | 222 | 17% | 1.8% | +40.7% | -20.9% | -10.36% | 100% |
| dip35_V2_gescreend_fail | 1663 | 24% | 4.8% | +56.0% | -28.2% | -7.68% | 100% |
| dip35_V2_alle | 1926 | 23% | 4.7% | +54.1% | -27.6% | -8.49% | 100% |
| dip35_V3_gescreend_pass | 223 | 7% | 2.2% | +136.2% | -22.9% | -12.19% | 100% |
| dip35_V3_gescreend_fail | 1665 | 12% | 6.3% | +115.6% | -30.0% | -12.06% | 100% |
| dip35_V3_alle | 1927 | 12% | 6.1% | +113.8% | -29.4% | -12.52% | 100% |
| dip40_V1_gescreend_pass | 208 | 13% | 1.9% | +43.7% | -15.7% | -8.00% | 98% |
| dip40_V1_gescreend_fail | 1600 | 26% | 4.0% | +47.6% | -25.6% | -6.86% | 100% |
| dip40_V1_alle | 1851 | 24% | 3.9% | +46.7% | -24.7% | -7.25% | 100% |
| dip40_V2_gescreend_pass | 207 | 13% | 1.9% | +47.6% | -19.9% | -11.07% | 99% |
| dip40_V2_gescreend_fail | 1611 | 25% | 4.3% | +57.1% | -27.9% | -6.92% | 100% |
| dip40_V2_alle | 1847 | 23% | 4.3% | +56.0% | -27.1% | -7.82% | 100% |
| dip40_V3_gescreend_pass | 208 | 6% | 2.4% | +108.4% | -21.7% | -14.23% | 100% |
| dip40_V3_gescreend_fail | 1613 | 12% | 5.8% | +104.5% | -29.6% | -13.18% | 100% |
| dip40_V3_alle | 1848 | 12% | 5.6% | +102.9% | -28.9% | -13.67% | 100% |
| dip45_V1_gescreend_pass | 197 | 15% | 2.0% | +52.2% | -15.4% | -5.11% | 95% |
| dip45_V1_gescreend_fail | 1552 | 28% | 3.5% | +49.8% | -25.1% | -4.41% | 100% |
| dip45_V1_alle | 1779 | 26% | 3.5% | +49.6% | -24.2% | -4.74% | 100% |
| dip45_V2_gescreend_pass | 194 | 19% | 2.6% | +51.2% | -19.5% | -6.04% | 97% |
| dip45_V2_gescreend_fail | 1559 | 26% | 3.8% | +61.5% | -27.1% | -4.42% | 100% |
| dip45_V2_alle | 1774 | 25% | 3.9% | +60.2% | -26.5% | -4.96% | 100% |
| dip45_V3_gescreend_pass | 196 | 7% | 3.1% | +197.6% | -20.8% | -6.28% | 99% |
| dip45_V3_gescreend_fail | 1562 | 13% | 5.5% | +114.2% | -29.0% | -9.80% | 100% |
| dip45_V3_alle | 1777 | 13% | 5.4% | +117.6% | -28.2% | -9.74% | 100% |

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
Sep 11 05:29:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:29:41,228 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.2s)
Sep 11 05:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:29:44,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:29:44,416 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:29:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:29:48,871 main INFO screen UKFLMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 11 05:30:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:30:57,229 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:30:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:30:57,452 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:31:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:02,974 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 05:31:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:03,540 main INFO screen cap pass=0 dev=2.1 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 05:31:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:13,829 main INFO screen FLYWHEEL pass=0 dev=0.0 ins=21.5 pro=64 1a=False 1b=False 2=True (3.4s)
Sep 11 05:31:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:34,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:31:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:34,616 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:31:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:35,013 main INFO screen Koi In Vase pass=0 dev=0.0 ins=15.75 pro=10 1a=False 1b=False 2=True (0.6s)
Sep 11 05:31:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:31:51,521 main INFO screen NEKO pass=0 dev=19.41 ins=0.0 pro=16 1a=False 1b=False 2=False (4.5s)
Sep 11 05:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:06,551 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:06,628 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:32:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:06,836 main INFO screen COOKED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:32:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:16,045 aiohttp.access INFO 178.128.101.234 [11/Sep/2026:05:32:16 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 05:32:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:19,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:32:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:19,176 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:32:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:32:19,295 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 05:33:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:10,251 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:33:10 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 05:33:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:10,593 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:33:10 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 05:33:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:26,918 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:33:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:27,021 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:33:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:27,200 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 05:33:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:37,033 main INFO screen dsfwfsdsfd pass=0 dev=6.65 ins=0.0 pro=8 1a=False 1b=True 2=False (8.2s)
Sep 11 05:33:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:37,722 main INFO screen RICK pass=0 dev=0.4 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 05:33:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:37,827 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:33:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:33:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:56,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:33:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:56,753 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:33:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:56,939 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 05:33:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:58,819 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:33:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:58,901 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:33:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:33:59,066 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
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
