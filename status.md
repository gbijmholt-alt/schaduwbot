# Schaduwbot status

- tijd: 2026-09-11 07:02:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 17 hours, 15 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.4G/38G | geheugen: 602/3814 MB

## Health
```json
(niet bereikbaar: timed out)
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 06:48 UTC

Gelogde schaduwtrades: **18405**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 7514 | 1002 | 13 | 1003 | 86 | 2018 | 6050 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 231 | 15% | 1.7% | +41.5% | -16.4% | -7.63% | 98% |
| dip35_V1_gescreend_fail | 1832 | 27% | 3.7% | +46.0% | -25.9% | -6.73% | 100% |
| dip35_V1_alle | 2130 | 26% | 3.8% | +44.8% | -25.2% | -7.21% | 100% |
| dip35_V2_gescreend_pass | 232 | 17% | 2.2% | +41.5% | -21.1% | -10.32% | 100% |
| dip35_V2_gescreend_fail | 1846 | 25% | 4.4% | +54.8% | -28.3% | -7.80% | 100% |
| dip35_V2_alle | 2125 | 24% | 4.5% | +53.0% | -27.8% | -8.54% | 100% |
| dip35_V3_gescreend_pass | 232 | 7% | 2.6% | +141.2% | -23.1% | -11.81% | 100% |
| dip35_V3_gescreend_fail | 1853 | 13% | 6.2% | +114.5% | -30.2% | -11.59% | 100% |
| dip35_V3_alle | 2129 | 12% | 6.1% | +112.8% | -29.6% | -12.05% | 100% |
| dip40_V1_gescreend_pass | 215 | 13% | 1.9% | +43.7% | -15.9% | -8.41% | 98% |
| dip40_V1_gescreend_fail | 1785 | 26% | 3.6% | +48.1% | -25.9% | -6.29% | 100% |
| dip40_V1_alle | 2048 | 25% | 3.7% | +47.2% | -25.0% | -6.81% | 100% |
| dip40_V2_gescreend_pass | 216 | 13% | 1.9% | +48.9% | -19.9% | -10.97% | 100% |
| dip40_V2_gescreend_fail | 1794 | 25% | 4.1% | +55.6% | -28.0% | -7.10% | 100% |
| dip40_V2_alle | 2042 | 24% | 4.1% | +54.8% | -27.4% | -7.97% | 100% |
| dip40_V3_gescreend_pass | 216 | 6% | 2.3% | +116.7% | -21.8% | -13.44% | 100% |
| dip40_V3_gescreend_fail | 1799 | 13% | 5.7% | +103.1% | -29.9% | -12.93% | 100% |
| dip40_V3_alle | 2045 | 12% | 5.6% | +102.3% | -29.2% | -13.38% | 100% |
| dip45_V1_gescreend_pass | 204 | 15% | 2.0% | +52.2% | -15.7% | -5.68% | 95% |
| dip45_V1_gescreend_fail | 1730 | 28% | 3.2% | +49.9% | -25.6% | -4.46% | 100% |
| dip45_V1_alle | 1966 | 27% | 3.3% | +49.7% | -24.6% | -4.86% | 100% |
| dip45_V2_gescreend_pass | 204 | 19% | 2.5% | +52.0% | -19.6% | -6.23% | 97% |
| dip45_V2_gescreend_fail | 1732 | 26% | 3.7% | +59.7% | -27.6% | -5.08% | 100% |
| dip45_V2_alle | 1959 | 25% | 3.8% | +58.8% | -26.9% | -5.57% | 100% |
| dip45_V3_gescreend_pass | 204 | 7% | 2.9% | +198.9% | -20.8% | -5.75% | 99% |
| dip45_V3_gescreend_fail | 1736 | 14% | 5.6% | +112.4% | -29.3% | -10.08% | 100% |
| dip45_V3_alle | 1961 | 13% | 5.5% | +115.9% | -28.6% | -9.96% | 100% |

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
Sep 11 06:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:17,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:17,681 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:17,802 main INFO screen Whale pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 06:48:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:22,657 main INFO screen asas pass=0 dev=10.26 ins=0.0 pro=5 1a=False 1b=False 2=False (3.3s)
Sep 11 06:49:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:13,370 main INFO screen 911 pass=0 dev=1.3 ins=0.0 pro=6 1a=False 1b=False 2=False (8.9s)
Sep 11 06:49:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:13,414 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (8.9s)
Sep 11 06:49:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:15,033 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:49:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:15,177 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=True (10.6s)
Sep 11 06:49:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:15,216 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:49:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:15,463 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 06:49:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:52,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:49:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:52,927 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:49:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:53,336 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.6s)
Sep 11 06:49:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:49:59,763 main INFO screen KHYX pass=0 dev=1.85 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 06:50:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:08,358 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:50:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:08,493 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:50:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:08,601 main INFO screen BUFO pass=0 dev=0.0 ins=49.58 pro=19 1a=False 1b=False 2=True (0.3s)
Sep 11 06:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:26,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:26,474 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:50:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:50:27,096 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.8s)
Sep 11 06:51:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:25,652 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:51:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:25,744 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:51:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:26,104 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.6s)
Sep 11 06:51:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:48,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:51:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:48,618 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:51:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:51:49,287 main INFO screen RSGN pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.9s)
Sep 11 06:52:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:52:14,894 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:52:14 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:52:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:52:51,338 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:52:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:52:51,433 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:52:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:52:51,624 main INFO screen GigaCoon pass=0 dev=0.0 ins=55.42 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 11 06:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:53:26,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:53:26,200 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:53:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:53:26,379 main INFO screen Doodlecat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:53:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:53:58,690 main INFO screen Whale pass=0 dev=1.26 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 11 06:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:54:23,496 main INFO screen kirkelevn pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (3.0s)
Sep 11 06:54:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:54:52,679 main INFO screen Claude  pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 06:54:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:54:57,202 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:54:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:54:57,265 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:54:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:54:57,760 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 06:55:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:55:19,649 main INFO screen vomitcoin pass=0 dev=0.0 ins=17.43 pro=53 1a=False 1b=False 2=True (3.4s)
Sep 11 06:55:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:55:45,415 main INFO screen KEYCAT pass=1 dev=0.0 ins=14.56 pro=38 1a=False 1b=False 2=False (3.0s)
Sep 11 06:55:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:55:54,567 main INFO screen jihcl pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 06:56:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:56:04,558 main INFO screen flayher pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (3.1s)
Sep 11 06:56:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:56:15,282 main INFO screen korea.fun pass=1 dev=0.0 ins=13.58 pro=49 1a=False 1b=False 2=False (2.9s)
Sep 11 06:57:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:57:15,272 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:57:15 +0000] "GET /health HTTP/1.1" 200 431 "-" "Python-urllib/3.14"
Sep 11 06:57:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:57:46,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:57:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:57:46,413 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:57:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:57:46,621 main INFO screen BFLYBRAIN pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 06:57:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:57:48,847 main INFO screen VENOM pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 06:58:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:06,141 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:58:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:06,836 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:58:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:07,625 main INFO screen jihcl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.9s)
Sep 11 06:58:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:09,038 main INFO screen excrementcoin pass=0 dev=0.0 ins=29.79 pro=63 1a=False 1b=False 2=True (3.9s)
Sep 11 06:58:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:24,553 main INFO screen XAT pass=0 dev=1.16 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 11 06:58:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:56,535 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:58:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:56,616 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:58:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:58:56,793 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:00:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:06,571 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:00:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:06,673 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:00:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:10,904 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 11 07:00:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:32,470 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:00:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:32,728 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:00:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:36,656 main INFO screen COST pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 11 07:00:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 07:00:36,840 main INFO screen DOOM pass=0 dev=0.0 ins=10.55 pro=41 1a=False 1b=False 2=True (4.4s)
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 1h 27min 25.296s CPU time over 17h 12min 29.302s wall clock time, 537.6M memory peak.
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 07:00:46 ubuntu-4gb-fsn1-1 python[18520]: 2026-09-11 07:00:46,951 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 07:01:04 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 07:01:05 ubuntu-4gb-fsn1-1 python[19120]: 2026-09-11 07:01:05,439 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 07:01:35 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 07:01:35 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 07:01:35 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 07:01:35 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 29.524s CPU time over 30.858s wall clock time, 56.6M memory peak.
Sep 11 07:01:35 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 07:01:36 ubuntu-4gb-fsn1-1 python[19926]: 2026-09-11 07:01:36,528 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 07:02:03 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 07:02:04 ubuntu-4gb-fsn1-1 python[21519]: 2026-09-11 07:02:04,453 main INFO verbonden met wss://mainnet.helius-rpc.com/
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
