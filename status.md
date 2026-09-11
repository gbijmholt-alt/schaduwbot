# Schaduwbot status

- tijd: 2026-09-11 08:42:30 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 55 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 572/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3813, "tokens_in_memory": 1252, "msgs": 343354, "trades": 89501, "creates": 1321, "decode_fail": 4212, "rpc_calls": 1815, "rpc_errors": 303, "sol_usd": 99.9940563648368, "open_positions": 82}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 08:38 UTC

Gelogde schaduwtrades: **20078**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 9704 | 1345 | 18 | 1345 | 98 | 2616 | 7723 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 240 | 15% | 1.7% | +40.4% | -16.4% | -7.68% | 98% |
| dip35_V1_gescreend_fail | 2008 | 26% | 4.0% | +45.9% | -26.4% | -7.43% | 100% |
| dip35_V1_alle | 2323 | 26% | 4.1% | +44.7% | -25.7% | -7.79% | 100% |
| dip35_V2_gescreend_pass | 240 | 18% | 2.1% | +39.8% | -21.1% | -10.43% | 100% |
| dip35_V2_gescreend_fail | 2015 | 24% | 4.7% | +54.4% | -28.7% | -8.80% | 100% |
| dip35_V2_alle | 2309 | 23% | 4.7% | +52.6% | -28.2% | -9.40% | 100% |
| dip35_V3_gescreend_pass | 240 | 7% | 2.5% | +141.2% | -23.1% | -12.14% | 100% |
| dip35_V3_gescreend_fail | 2046 | 13% | 6.5% | +112.3% | -30.4% | -12.22% | 100% |
| dip35_V3_alle | 2335 | 12% | 6.4% | +110.6% | -29.9% | -12.65% | 100% |
| dip40_V1_gescreend_pass | 222 | 13% | 1.8% | +42.7% | -15.8% | -8.19% | 98% |
| dip40_V1_gescreend_fail | 1954 | 26% | 3.9% | +47.9% | -26.3% | -6.83% | 100% |
| dip40_V1_alle | 2232 | 25% | 3.9% | +46.9% | -25.5% | -7.23% | 100% |
| dip40_V2_gescreend_pass | 222 | 13% | 1.8% | +50.8% | -19.8% | -10.59% | 100% |
| dip40_V2_gescreend_fail | 1955 | 24% | 4.3% | +55.3% | -28.5% | -7.97% | 100% |
| dip40_V2_alle | 2216 | 23% | 4.3% | +54.6% | -27.8% | -8.67% | 100% |
| dip40_V3_gescreend_pass | 222 | 6% | 2.3% | +116.7% | -21.7% | -13.57% | 100% |
| dip40_V3_gescreend_fail | 1982 | 13% | 6.1% | +102.4% | -30.2% | -13.32% | 100% |
| dip40_V3_alle | 2239 | 12% | 6.0% | +101.3% | -29.5% | -13.76% | 100% |
| dip45_V1_gescreend_pass | 210 | 15% | 1.9% | +50.6% | -15.6% | -5.84% | 96% |
| dip45_V1_gescreend_fail | 1896 | 28% | 3.4% | +49.8% | -25.9% | -4.99% | 100% |
| dip45_V1_alle | 2146 | 26% | 3.5% | +49.4% | -25.1% | -5.34% | 100% |
| dip45_V2_gescreend_pass | 210 | 19% | 2.4% | +50.3% | -19.5% | -6.19% | 97% |
| dip45_V2_gescreend_fail | 1889 | 25% | 3.9% | +59.3% | -27.9% | -6.02% | 100% |
| dip45_V2_alle | 2129 | 24% | 3.9% | +58.2% | -27.3% | -6.44% | 100% |
| dip45_V3_gescreend_pass | 210 | 7% | 2.9% | +186.5% | -20.8% | -6.02% | 99% |
| dip45_V3_gescreend_fail | 1913 | 14% | 5.9% | +110.6% | -29.6% | -10.46% | 100% |
| dip45_V3_alle | 2149 | 13% | 5.8% | +113.2% | -28.9% | -10.40% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1620 | 12% | 2.7% | -9.96% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 08:28:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:00,637 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:28:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:00,784 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,782 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,959 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:28:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:05,882 main INFO screen asdcdas pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 08:28:07 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:07,643 main INFO screen Fluf pass=0 dev=0.0 ins=5.35 pro=22 1a=False 1b=False 2=True (7.0s)
Sep 11 08:29:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:41,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:29:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:41,529 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:29:44 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:44,961 main INFO screen MIDAS pass=0 dev=0.0 ins=20.9 pro=28 1a=False 1b=False 2=True (3.6s)
Sep 11 08:30:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:10,211 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 11 08:30:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:36,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:36,743 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,254 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,380 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,559 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:30:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:43,853 main INFO screen WBC pass=0 dev=0.0 ins=79.26 pro=7 1a=False 1b=False 2=True (7.3s)
Sep 11 08:30:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:52,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:52,517 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:56,213 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 11 08:31:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:31:37,112 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:31:37 +0000] "GET /health HTTP/1.1" 200 421 "-" "Python-urllib/3.14"
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,625 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,695 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,891 main INFO screen LCOST pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,320 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,406 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,615 main INFO screen BARREL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,778 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,901 main INFO screen BBB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:32:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:42,943 main INFO screen Aphrodite pass=0 dev=0.26 ins=0.0 pro=6 1a=False 1b=False 2=False (3.1s)
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,210 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,314 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,518 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,035 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,146 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,324 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:34:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:37,327 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 08:35:16 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:16,166 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,097 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,191 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,392 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:36:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:05,962 main INFO screen INCOGCAT pass=1 dev=0.0 ins=11.36 pro=24 1a=False 1b=False 2=False (3.5s)
Sep 11 08:36:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:06,107 main INFO screen KYC pass=0 dev=0.0 ins=11.25 pro=55 1a=False 1b=False 2=True (4.9s)
Sep 11 08:36:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:37,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:36:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:38,033 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:36:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:38,257 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:36:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:39,268 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:36:39 +0000] "GET /health HTTP/1.1" 200 421 "-" "Python-urllib/3.14"
Sep 11 08:36:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:43,484 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.3s)
Sep 11 08:36:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:58,728 main INFO screen Cat pass=1 dev=0.0 ins=11.38 pro=31 1a=False 1b=False 2=False (4.0s)
Sep 11 08:37:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:04,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:37:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:04,931 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:37:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:05,227 main INFO screen Lucy pass=0 dev=0.0 ins=21.31 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 11 08:37:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:05,293 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:37:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:05,380 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:37:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:05,553 main INFO screen ASHIBATON pass=0 dev=0.0 ins=79.12 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 08:37:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:11,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:37:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:11,814 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:37:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:11,945 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:37:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:50,605 main INFO screen WINO pass=0 dev=0.0 ins=29.37 pro=57 1a=False 1b=False 2=False (1.3s)
Sep 11 08:37:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:54,863 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:37:54 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 08:37:57 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:37:57,253 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:37:57 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,355 main INFO screen $USD pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,803 main INFO screen wind pass=0 dev=1.44 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 11 08:39:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:54,911 main INFO screen FYC pass=0 dev=0.0 ins=16.28 pro=52 1a=False 1b=False 2=True (8.5s)
Sep 11 08:39:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:39:58,237 main INFO screen PC pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (3.9s)
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,305 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,398 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:41:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:09,599 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,298 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:41:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:21,440 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:41:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:41:39,691 main INFO screen Lucy pass=1 dev=0.0 ins=10.58 pro=48 1a=False 1b=False 2=False (3.3s)
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,241 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,335 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:42:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:10,526 main INFO screen happen pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,238 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,299 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:42:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:29,515 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 08:42:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:42:30,532 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:42:30 +0000] "GET /health HTTP/1.1" 200 420 "-" "Python-urllib/3.14"
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
