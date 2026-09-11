# Schaduwbot status

- tijd: 2026-09-11 06:52:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 17 hours, 5 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 647/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 61438, "tokens_in_memory": 1112, "msgs": 10348150, "trades": 2018333, "creates": 22572, "decode_fail": 130216, "rpc_calls": 34087, "rpc_errors": 3299, "sol_usd": 99.7629506404651, "open_positions": 73}
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
Sep 11 06:42:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:42:21,478 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:42:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:42:21,610 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:42:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:42:21,746 main INFO screen aas pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 06:43:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:11,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:43:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:11,863 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:12,051 main INFO screen computer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:43:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:13,359 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:43:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:13,444 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:43:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:13,606 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 06:43:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:33,265 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:43:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:33,325 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:43:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:43:33,712 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 06:44:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:40,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:44:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:41,023 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:44:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:41,204 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 06:44:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:47,567 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 11 06:44:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:57,156 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:44:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:57,247 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:44:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:44:57,397 main INFO screen trash pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 06:45:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:13,984 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:45:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:14,384 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:45:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:14,985 main INFO screen Couscous pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=True (1.2s)
Sep 11 06:45:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:15,943 main INFO screen DOOYET pass=0 dev=7.24 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 06:45:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:26,903 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:45:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:27,030 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:45:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:27,163 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.3s)
Sep 11 06:45:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:53,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:45:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:53,570 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:45:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:45:53,759 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:46:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:06,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:46:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:06,323 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:46:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:06,462 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 06:46:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:23,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:46:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:23,401 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:46:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:23,608 main INFO screen PSYCH0 pass=0 dev=0.0 ins=43.3 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 11 06:46:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:40,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:46:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:40,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:46:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:41,286 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (0.5s)
Sep 11 06:46:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:52,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:46:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:52,709 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:46:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:46:52,875 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:47:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:11,386 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:47:11 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:47:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:20,644 main INFO screen sasa pass=0 dev=32.07 ins=0.0 pro=5 1a=False 1b=False 2=False (3.7s)
Sep 11 06:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:22,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:22,128 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:47:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:22,260 main INFO screen computer pass=0 dev=0.0 ins=0.06 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 06:47:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:30,367 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:47:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:30,445 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:47:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:47:30,606 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 06:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:03,020 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:03,109 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:48:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:03,463 main INFO screen sasa pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.6s)
Sep 11 06:48:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:48:08,437 main INFO screen flaysol pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
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
