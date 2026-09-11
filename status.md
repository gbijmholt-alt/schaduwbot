# Schaduwbot status

- tijd: 2026-09-11 06:47:11 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 17 hours, 0 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 644/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 61134, "tokens_in_memory": 1082, "msgs": 10337366, "trades": 2011597, "creates": 22477, "decode_fail": 130023, "rpc_calls": 33887, "rpc_errors": 3279, "sol_usd": 99.6905854297352, "open_positions": 66}
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
Sep 11 06:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:34:40,574 main INFO screen ANDREW pass=0 dev=0.0 ins=16.21 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 06:35:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:00,356 main INFO screen MCLJ pass=0 dev=1.57 ins=0.0 pro=2 1a=False 1b=False 2=True (1.9s)
Sep 11 06:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:23,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:23,464 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:23,636 main INFO screen STRAPON pass=0 dev=0.0 ins=49.35 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 06:35:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:32,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:35:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:32,610 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:35:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:32,963 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.5s)
Sep 11 06:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:38,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:38,458 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:35:38,620 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 06:36:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:36:04,243 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:36:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:36:04,339 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:36:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:36:04,518 main INFO screen asdfasdf pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 06:36:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:36:37,126 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:36:37 +0000] "GET /health HTTP/1.1" 200 431 "-" "Python-urllib/3.14"
Sep 11 06:37:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:37:41,156 main INFO screen GoldenPump pass=0 dev=0.0 ins=19.04 pro=71 1a=False 1b=False 2=True (4.1s)
Sep 11 06:38:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:38:11,564 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:38:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:38:11,622 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:38:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:38:11,836 main INFO screen EGG pass=0 dev=0.0 ins=48.76 pro=20 1a=False 1b=False 2=True (0.4s)
Sep 11 06:39:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:01,762 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:39:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:01,853 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:02,205 main INFO screen Plum pass=0 dev=0.0 ins=11.21 pro=26 1a=False 1b=False 2=True (0.5s)
Sep 11 06:39:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:10,724 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 06:39:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:12,346 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:39:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:12,484 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:39:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:12,628 main INFO screen TOWNIE pass=0 dev=0.0 ins=17.55 pro=23 1a=False 1b=False 2=True (0.3s)
Sep 11 06:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:31,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:31,675 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:39:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:39:32,052 main INFO screen GG pass=0 dev=0.0 ins=11.96 pro=8 1a=False 1b=False 2=True (0.6s)
Sep 11 06:40:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:40:32,251 main INFO screen period  pass=0 dev=0.66 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 06:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:37,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:37,913 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:41:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:38,101 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:41:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:58,961 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:59,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:41:59,294 main INFO screen NVIDOG pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 06:42:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:42:00,172 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:42:00 +0000] "GET /health HTTP/1.1" 200 431 "-" "Python-urllib/3.14"
Sep 11 06:42:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:42:19,701 main INFO screen GoldenShower pass=0 dev=0.0 ins=15.4 pro=60 1a=False 1b=False 2=True (3.4s)
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
