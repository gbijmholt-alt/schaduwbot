# Schaduwbot status

- tijd: 2026-09-11 07:17:52 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 17 hours, 30 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 532/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 902, "tokens_in_memory": 217, "msgs": 79521, "trades": 14648, "creates": 217, "decode_fail": 869, "rpc_calls": 365, "rpc_errors": 48, "sol_usd": 99.9059789518272, "open_positions": 31}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 07:02 UTC

Gelogde schaduwtrades: **18616**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 7750 | 1036 | 13 | 1036 | 88 | 2094 | 6261 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 232 | 15% | 1.7% | +41.5% | -16.4% | -7.63% | 98% |
| dip35_V1_gescreend_fail | 1851 | 27% | 3.8% | +45.9% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 2152 | 26% | 3.9% | +44.7% | -25.3% | -7.34% | 100% |
| dip35_V2_gescreend_pass | 233 | 17% | 2.1% | +41.5% | -21.0% | -10.30% | 100% |
| dip35_V2_gescreend_fail | 1864 | 24% | 4.5% | +54.8% | -28.4% | -7.98% | 100% |
| dip35_V2_alle | 2146 | 24% | 4.6% | +52.9% | -27.9% | -8.70% | 100% |
| dip35_V3_gescreend_pass | 233 | 7% | 2.6% | +141.2% | -23.1% | -11.83% | 100% |
| dip35_V3_gescreend_fail | 1877 | 13% | 6.3% | +113.7% | -30.2% | -11.73% | 100% |
| dip35_V3_alle | 2155 | 12% | 6.2% | +112.1% | -29.7% | -12.19% | 100% |
| dip40_V1_gescreend_pass | 216 | 12% | 1.9% | +43.7% | -15.9% | -8.42% | 98% |
| dip40_V1_gescreend_fail | 1804 | 26% | 3.7% | +47.9% | -25.9% | -6.37% | 100% |
| dip40_V1_alle | 2070 | 25% | 3.8% | +46.9% | -25.1% | -6.89% | 100% |
| dip40_V2_gescreend_pass | 217 | 13% | 1.8% | +48.9% | -19.8% | -10.95% | 100% |
| dip40_V2_gescreend_fail | 1813 | 25% | 4.1% | +55.4% | -28.1% | -7.26% | 100% |
| dip40_V2_alle | 2064 | 24% | 4.2% | +54.5% | -27.4% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 217 | 6% | 2.3% | +116.7% | -21.8% | -13.46% | 100% |
| dip40_V3_gescreend_fail | 1824 | 13% | 5.9% | +102.8% | -29.9% | -13.06% | 100% |
| dip40_V3_alle | 2072 | 12% | 5.7% | +102.0% | -29.2% | -13.52% | 100% |
| dip45_V1_gescreend_pass | 205 | 15% | 2.0% | +52.2% | -15.6% | -5.70% | 95% |
| dip45_V1_gescreend_fail | 1750 | 28% | 3.3% | +49.7% | -25.6% | -4.55% | 100% |
| dip45_V1_alle | 1989 | 27% | 3.3% | +49.5% | -24.7% | -4.96% | 100% |
| dip45_V2_gescreend_pass | 205 | 18% | 2.4% | +52.0% | -19.5% | -6.24% | 97% |
| dip45_V2_gescreend_fail | 1751 | 26% | 3.7% | +59.5% | -27.5% | -5.22% | 100% |
| dip45_V2_alle | 1981 | 25% | 3.8% | +58.6% | -26.9% | -5.69% | 100% |
| dip45_V3_gescreend_pass | 205 | 7% | 2.9% | +198.9% | -20.8% | -5.81% | 99% |
| dip45_V3_gescreend_fail | 1760 | 14% | 5.6% | +112.0% | -29.3% | -10.17% | 100% |
| dip45_V3_alle | 1987 | 13% | 5.5% | +115.5% | -28.6% | -10.08% | 100% |

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
Sep 11 07:04:29 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:04:29,468 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:04:33 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:04:33,075 main INFO screen krkvsry pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.8s)
Sep 11 07:04:36 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:04:36,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:04:37 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:04:37,057 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:04:37 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:04:37,396 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 07:05:09 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:09,712 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:05:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:10,215 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:05:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:10,856 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.7s)
Sep 11 07:05:18 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:18,140 main INFO screen CAT pass=0 dev=0.57 ins=0.0 pro=1 1a=False 1b=False 2=False (9.4s)
Sep 11 07:05:25 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:25,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:05:25 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:25,745 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:05:27 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:27,857 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.3s)
Sep 11 07:05:39 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:39,119 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:05:39 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:39,244 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:05:40 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:40,033 main INFO screen DOOYET pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 11 07:05:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:46,334 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 07:05:49 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:49,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:05:49 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:49,590 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:05:50 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:50,164 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 11 07:05:54 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:54,233 main INFO screen power pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (6.4s)
Sep 11 07:05:57 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:57,699 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:07:05:57 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 07:05:58 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:05:58,038 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:07:05:58 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 07:06:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:10,132 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:06:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:10,191 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:06:10 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:10,640 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.6s)
Sep 11 07:06:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:46,206 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:06:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:46,266 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:06:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:06:47,722 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 11 07:07:14 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:14,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:07:14 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:14,166 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:07:14 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:14,566 main INFO screen NasDeer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.6s)
Sep 11 07:07:26 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:26,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:07:27 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:27,020 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:07:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:28,715 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:07:28 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:28,842 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:07:32 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:32,617 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.8s)
Sep 11 07:07:33 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:33,890 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:07:33 +0000] "GET /health HTTP/1.1" 200 411 "-" "Python-urllib/3.14"
Sep 11 07:07:35 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:35,493 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 11 07:07:58 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:58,575 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:07:58 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:07:58,698 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:08:00 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:00,859 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:08:00 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:00,939 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:08:03 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:03,212 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 11 07:08:06 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:06,329 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 07:08:11 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:11,919 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:08:12 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:12,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:08:18 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:18,086 main INFO screen Axel pass=0 dev=0.0 ins=48.94 pro=15 1a=False 1b=False 2=True (6.2s)
Sep 11 07:08:41 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:41,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:08:42 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:42,093 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:08:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:46,399 main INFO screen polycat pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=True (4.5s)
Sep 11 07:08:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:47,122 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:08:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:47,246 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:08:51 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:08:51,006 main INFO screen SpaceX pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 07:09:03 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:09:03,157 main INFO screen VENOM pass=0 dev=0.48 ins=0.0 pro=1 1a=False 1b=False 2=False (6.5s)
Sep 11 07:09:58 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:09:58,911 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:09:59 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:09:59,012 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:10:05 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:10:05,401 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 11 07:10:56 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:10:56,715 main INFO screen gold pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 11 07:12:30 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:12:30,147 main INFO screen WORTHLESS pass=1 dev=0.0 ins=11.28 pro=41 1a=False 1b=False 2=False (3.9s)
Sep 11 07:12:37 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:12:37,130 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:12:37 +0000] "GET /health HTTP/1.1" 200 413 "-" "Python-urllib/3.14"
Sep 11 07:13:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:13:47,970 main INFO screen RIch DoG pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 11 07:14:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:14:45,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:14:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:14:45,382 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:14:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:14:45,584 main INFO screen Poly pass=0 dev=0.0 ins=12.99 pro=41 1a=False 1b=False 2=True (0.4s)
Sep 11 07:15:05 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:05,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:15:05 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:05,139 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:15:11 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:11,575 main INFO screen PEPERED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 11 07:15:38 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:38,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:15:38 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:38,682 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:15:42 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:42,661 main INFO screen SQUIRREL pass=0 dev=0.0 ins=10.42 pro=6 1a=False 1b=False 2=False (4.6s)
Sep 11 07:15:45 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:45,209 main INFO screen RICK pass=0 dev=10.29 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 11 07:15:57 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:15:57,727 main INFO screen fly pass=0 dev=0.09 ins=0.0 pro=4 1a=False 1b=False 2=False (5.1s)
Sep 11 07:16:02 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:02,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:16:02 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:02,613 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:16:06 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:06,451 main INFO screen UPP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.1s)
Sep 11 07:16:25 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:25,513 main INFO screen polymarcat pass=1 dev=0.0 ins=8.13 pro=48 1a=False 1b=False 2=False (3.5s)
Sep 11 07:16:46 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:46,463 main INFO screen $DENNIS pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 11 07:16:47 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:47,238 main INFO screen tree pass=0 dev=0.56 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 11 07:16:48 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:16:48,938 main INFO screen ZTONK pass=0 dev=7.0 ins=14.57 pro=15 1a=False 1b=False 2=False (4.8s)
Sep 11 07:17:52 ubuntu-4gb-fsn1-1 python[22849]: 2026-09-11 07:17:52,823 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:17:52 +0000] "GET /health HTTP/1.1" 200 413 "-" "Python-urllib/3.14"
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
