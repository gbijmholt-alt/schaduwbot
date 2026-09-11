# Schaduwbot status

- tijd: 2026-09-11 04:52:29 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 15 hours, 5 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 645/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 54252, "tokens_in_memory": 1028, "msgs": 9764471, "trades": 1862842, "creates": 20605, "decode_fail": 123529, "rpc_calls": 31019, "rpc_errors": 2942, "sol_usd": 99.71392561825849, "open_positions": 24}
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
Sep 11 04:37:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:26,967 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:37:26 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 04:37:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:52,016 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:37:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:52,099 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:37:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:37:52,360 main INFO screen Noah pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.5s)
Sep 11 04:38:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:38:11,436 main INFO screen MotionCat pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 11 04:39:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:11,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:39:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:11,308 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:39:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:11,497 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:39:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:34,811 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:39:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:34,933 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:39:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:35,115 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 04:39:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:54,603 main INFO screen MotionCat pass=0 dev=0.13 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 11 04:39:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:39:59,007 main INFO screen XENT pass=0 dev=0.39 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 04:40:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:02,080 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:40:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:02,197 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:40:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:02,361 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 04:40:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:25,134 main INFO screen RETAIL pass=1 dev=0.0 ins=1.45 pro=35 1a=False 1b=False 2=False (3.4s)
Sep 11 04:40:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:39,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:40:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:40,069 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:40:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:40:40,256 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,102 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,199 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,387 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,722 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,858 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:41:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:45,974 main INFO screen BDSM pass=0 dev=0.0 ins=20.54 pro=17 1a=False 1b=False 2=True (0.3s)
Sep 11 04:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:59,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:59,870 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:41:59,991 main INFO screen $GEYE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 04:42:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:42:26,288 main INFO screen power pass=0 dev=0.51 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 11 04:42:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:42:27,347 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:42:27 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 11 04:42:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:42:45,642 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:42:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:42:45,779 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:42:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:42:45,965 main INFO screen $SHEKEL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 04:44:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:07,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:44:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:07,242 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:44:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:07,412 main INFO screen LOOP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:15,213 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:15,301 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:15,455 main INFO screen WWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 04:44:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:44:25,889 main INFO screen Jose pass=1 dev=0.0 ins=6.01 pro=60 1a=False 1b=False 2=False (2.7s)
Sep 11 04:45:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:45:00,493 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:45:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:45:00,588 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:45:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:45:00,770 main INFO screen Faucet pass=0 dev=0.0 ins=20.54 pro=23 1a=False 1b=False 2=True (0.4s)
Sep 11 04:45:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:45:24,997 main INFO screen FISH pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 11 04:46:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:01,971 main INFO screen Fruitless pass=1 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=False (4.1s)
Sep 11 04:46:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:18,873 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:46:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:18,968 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:46:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:19,211 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:46:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:41,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:46:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:41,742 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:46:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:46:41,921 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 04:47:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:47:27,182 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:47:27 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 11 04:47:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:47:47,949 main INFO screen $GEYE pass=0 dev=0.7 ins=0.0 pro=4 1a=False 1b=False 2=False (4.5s)
Sep 11 04:48:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:48:11,933 main INFO screen power pass=0 dev=0.4 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 04:48:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:48:20,624 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:48:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:48:20,751 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:48:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:48:20,872 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 04:49:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:01,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:49:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:01,842 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:49:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:02,025 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 04:49:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:12,848 main INFO screen PigMaxx pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 04:49:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:20,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:49:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:20,567 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:49:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:49:20,689 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 04:50:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:50:02,925 main INFO screen att pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 04:50:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:50:20,863 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:50:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:50:20,964 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:50:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:50:21,157 main INFO screen Flycraft pass=0 dev=0.0 ins=46.56 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 04:51:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:10,875 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:51:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:10,969 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:51:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:11,200 main INFO screen FLYBRAINL pass=0 dev=0.0 ins=79.27 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 04:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:22,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:22,482 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:22,621 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 04:51:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:35,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 04:51:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:35,854 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 04:51:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:51:35,981 main INFO screen ZeroCool pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 04:52:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:52:07,444 main INFO screen power pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 04:52:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 04:52:29,082 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:04:52:29 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
