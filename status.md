# Schaduwbot status

- tijd: 2026-09-10 22:46:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 8 hours, 59 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 634/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 32300, "tokens_in_memory": 1516, "msgs": 6514827, "trades": 1222597, "creates": 13313, "decode_fail": 93684, "rpc_calls": 19967, "rpc_errors": 1983, "sol_usd": 99.3684982307412, "open_positions": 118}
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
Sep 10 22:35:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:35:12,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:35:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:35:12,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:35:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:35:12,388 main INFO screen guys pass=0 dev=0.0 ins=22.91 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 10 22:35:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:35:48,007 main INFO screen TALIS!! pass=0 dev=0.58 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 22:36:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:16,792 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:36:16 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 22:36:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:30,112 main INFO screen 42 pass=0 dev=0.0 ins=15.95 pro=23 1a=False 1b=False 2=True (5.3s)
Sep 10 22:36:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:31,018 main INFO screen $CAJUN pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 10 22:36:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:32,221 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 10 22:36:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:36,742 main INFO screen BULL pass=0 dev=1.33 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 10 22:36:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:40,229 aiohttp.access INFO 123.56.6.232 [10/Sep/2026:22:36:40 +0000] "GET / HTTP/1.0" 404 174 "-" "-"
Sep 10 22:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:36:42,073 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 10 22:37:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:12,297 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:37:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:12,392 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:37:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:12,741 main INFO screen puter pass=0 dev=0.0 ins=12.94 pro=27 1a=False 1b=False 2=True (0.5s)
Sep 10 22:37:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:15,692 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:37:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:15,818 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:37:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:15,977 main INFO screen ape pass=0 dev=0.0 ins=36.03 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 22:37:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:39,876 main INFO screen OzemPIG pass=1 dev=0.0 ins=16.62 pro=37 1a=False 1b=False 2=False (1.2s)
Sep 10 22:37:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:55,278 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:37:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:55,375 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:37:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:37:55,572 main INFO screen puter pass=0 dev=0.0 ins=36.18 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 22:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:04,066 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:04,189 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:38:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:08,093 main INFO screen JPM pass=0 dev=0.0 ins=19.67 pro=11 1a=False 1b=False 2=True (4.1s)
Sep 10 22:38:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:18,133 aiohttp.access INFO 94.154.43.250 [10/Sep/2026:22:38:18 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 10 22:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:31,151 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:31,213 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:31,602 main INFO screen PUMPLESS pass=0 dev=0.0 ins=9.41 pro=53 1a=False 1b=False 2=True (0.5s)
Sep 10 22:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:59,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:59,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:38:59,286 main INFO screen APPLE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 22:39:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:01,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:39:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:01,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:39:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:02,022 main INFO screen JUGCHUA pass=0 dev=0.0 ins=79.17 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 10 22:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:13,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:13,260 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:39:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:13,399 main INFO screen LAPTOP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 22:39:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:39:50,444 main INFO screen hammy pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 10 22:40:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:06,536 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:40:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:06,597 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:40:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:06,820 main INFO screen FIX6900 pass=0 dev=0.0 ins=20.38 pro=23 1a=False 1b=False 2=True (0.4s)
Sep 10 22:40:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:28,136 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:40:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:28,234 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:40:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:30,879 main INFO screen fun pass=0 dev=0.0 ins=26.11 pro=10 1a=False 1b=False 2=True (2.8s)
Sep 10 22:40:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:40,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:40:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:41,103 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:40:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:41,229 main INFO screen APEON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 22:40:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:55,746 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:40:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:56,093 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:40:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:56,647 main INFO screen Kate pass=0 dev=0.0 ins=20.65 pro=11 1a=False 1b=False 2=True (1.3s)
Sep 10 22:40:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:40:57,050 main INFO screen HASH  pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 10 22:41:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:33,552 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:41:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:33,607 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:41:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:34,089 main INFO screen gob pass=0 dev=0.0 ins=10.68 pro=14 1a=False 1b=False 2=True (0.6s)
Sep 10 22:41:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:35,026 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:41:35 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 22:41:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:36,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:37,050 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:41:37,324 main INFO screen GOB pass=0 dev=0.0 ins=4.71 pro=36 1a=False 1b=False 2=True (0.5s)
Sep 10 22:42:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:42:32,307 main INFO screen APPLE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 10 22:43:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:14,448 main INFO screen Tcion pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 10 22:43:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:26,338 main INFO screen Dali pass=0 dev=6.71 ins=5.92 pro=20 1a=False 1b=False 2=False (3.4s)
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,272 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:43:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:35,714 main INFO screen AMD pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 22:43:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:56,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:57,345 main INFO screen PUMPLESS pass=0 dev=0.0 ins=15.61 pro=27 1a=False 1b=False 2=True (1.3s)
Sep 10 22:43:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:57,388 main INFO screen RAGE GURL pass=0 dev=0.73 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 10 22:43:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:43:59,988 main INFO screen $DRUSKI pass=0 dev=0.83 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 10 22:44:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:08,082 main INFO screen KATE pass=0 dev=1.16 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,090 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,349 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:44:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:10,461 main INFO screen Apu pass=0 dev=0.0 ins=16.96 pro=13 1a=False 1b=False 2=True (4.5s)
Sep 10 22:44:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:12,126 main INFO screen iPump pass=0 dev=0.0 ins=18.2 pro=10 1a=False 1b=False 2=True (2.2s)
Sep 10 22:44:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:39,352 main INFO screen Lingo pass=1 dev=0.0 ins=18.33 pro=12 1a=False 1b=False 2=False (1.6s)
Sep 10 22:44:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:44:55,986 main INFO screen AI pass=0 dev=0.0 ins=17.41 pro=16 1a=False 1b=False 2=True (3.8s)
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,360 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,451 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:45:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:45:54,642 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 22:46:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:46:12,749 main INFO screen solcat pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 10 22:46:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:46:37,148 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:46:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
