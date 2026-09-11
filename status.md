# Schaduwbot status

- tijd: 2026-09-11 05:18:10 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 15 hours, 31 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 642/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 55793, "tokens_in_memory": 958, "msgs": 9912369, "trades": 1892360, "creates": 20943, "decode_fail": 124917, "rpc_calls": 31555, "rpc_errors": 2996, "sol_usd": 99.71090615974475, "open_positions": 17}
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
Sep 11 05:00:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:00:57,699 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:01:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:01,418 main INFO screen ClaudeAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 11 05:01:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:03,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:01:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:03,466 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:01:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:03,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:01:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:03,840 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:01:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:04,197 main INFO screen BEAN pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=True (0.7s)
Sep 11 05:01:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:06,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:01:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:06,134 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:01:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:07,716 main INFO screen ANONINU pass=0 dev=0.0 ins=79.24 pro=6 1a=False 1b=False 2=True (4.4s)
Sep 11 05:01:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:10,378 main INFO screen discat pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 11 05:01:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:42,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:01:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:43,030 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:01:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:01:47,119 main INFO screen $GWALLEY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.3s)
Sep 11 05:02:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:14,178 main INFO screen TIKTOK pass=0 dev=0.0 ins=25.55 pro=38 1a=True 1b=False 2=True (8.2s)
Sep 11 05:02:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:19,657 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:02:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:19,829 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:02:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:25,926 main INFO screen TROLL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 05:02:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:33,528 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:02:33 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:02:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:02:54,283 main INFO screen power pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 11 05:04:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:04:17,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:04:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:04:18,015 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:04:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:04:24,630 main INFO screen Starbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 05:05:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:05:12,384 main INFO screen TrumpWif pass=0 dev=46.91 ins=0.0 pro=3 1a=False 1b=False 2=False (9.5s)
Sep 11 05:06:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:06:21,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:06:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:06:22,038 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:06:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:06:28,231 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.4s)
Sep 11 05:07:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:07:08,219 main INFO screen fat pig pass=1 dev=3.46 ins=0.0 pro=20 1a=False 1b=False 2=False (3.1s)
Sep 11 05:07:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:07:32,105 main INFO screen death pass=0 dev=0.14 ins=0.0 pro=2 1a=False 1b=False 2=True (6.1s)
Sep 11 05:07:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:07:35,329 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:07:35 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 05:07:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:07:52,207 main INFO screen Fly pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 11 05:08:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:08:33,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:08:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:08:33,156 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:08:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:08:36,567 main INFO screen PBATON pass=0 dev=0.0 ins=78.87 pro=7 1a=False 1b=False 2=True (3.6s)
Sep 11 05:09:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:09:08,258 main INFO screen $FREEMAN pass=0 dev=2.08 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 11 05:09:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:09:51,961 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:09:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:09:52,120 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:09:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:09:55,972 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.1s)
Sep 11 05:10:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:10:00,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:10:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:10:00,721 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:10:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:10:06,242 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 05:10:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:10:12,285 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:10:12 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 05:10:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:10:12,622 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:05:10:12 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 05:11:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:11:12,823 main INFO screen HorseFly pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 05:12:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:12:32,388 aiohttp.access INFO 18.234.77.126 [11/Sep/2026:05:12:32 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
Sep 11 05:12:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:12:37,129 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:12:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 05:12:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:12:40,739 main INFO screen WEINERS pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 11 05:12:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:12:57,479 main INFO screen 🌟  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 05:13:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:13:44,957 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:13:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:13:45,053 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:13:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:13:48,906 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 05:13:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:13:54,416 main INFO screen LaMisery pass=0 dev=3.64 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 11 05:14:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:15,198 main INFO screen KHAIN pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.1s)
Sep 11 05:14:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:20,720 main INFO screen FLYSCAPE pass=0 dev=0.0 ins=8.05 pro=64 1a=False 1b=False 2=True (2.4s)
Sep 11 05:14:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:34,583 main INFO screen DERP pass=0 dev=3.48 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 11 05:14:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:47,644 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:14:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:47,740 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:14:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:48,020 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:14:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:48,150 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:14:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:52,024 main INFO screen meow pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.1s)
Sep 11 05:14:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:14:52,381 main INFO screen WEINERS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.8s)
Sep 11 05:15:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:09,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:15:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:09,845 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:15:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:14,595 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 11 05:15:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:25,656 main INFO screen VENOM pass=0 dev=2.2 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 11 05:15:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:26,971 main INFO screen Manifesto pass=1 dev=0.0 ins=1.94 pro=53 1a=False 1b=False 2=False (3.2s)
Sep 11 05:15:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:36,384 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:15:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:36,468 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:15:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:36,794 main INFO screen PUMPER pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 11 05:15:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:15:44,825 main INFO screen SAVPIR pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 11 05:16:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:16:01,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:16:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:16:01,353 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:16:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:16:06,695 main INFO screen FTFS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 05:17:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:01,973 main INFO screen crossing  pass=0 dev=0.14 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 11 05:17:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:08,969 main INFO screen VENOM pass=0 dev=1.55 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 05:17:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:11,951 main INFO screen $GOAT pass=0 dev=3.22 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 11 05:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:17,606 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 05:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:17,723 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 05:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:17:17,894 main INFO screen FLY pass=0 dev=0.0 ins=11.31 pro=26 1a=False 1b=False 2=True (0.4s)
Sep 11 05:18:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 05:18:10,481 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:05:18:10 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
