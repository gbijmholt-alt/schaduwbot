# Schaduwbot status

- tijd: 2026-09-11 03:50:43 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 14 hours, 3 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 646/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 50546, "tokens_in_memory": 1021, "msgs": 9240441, "trades": 1773399, "creates": 19559, "decode_fail": 119980, "rpc_calls": 29494, "rpc_errors": 2813, "sol_usd": 99.26549282372895, "open_positions": 19}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 03:48 UTC

Gelogde schaduwtrades: **15837**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 4522 | 566 | 4 | 567 | 59 | 1152 | 3482 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 205 | 16% | 1.5% | +40.0% | -16.5% | -7.66% | 98% |
| dip35_V1_gescreend_fail | 1574 | 26% | 4.1% | +45.9% | -25.6% | -7.42% | 100% |
| dip35_V1_alle | 1836 | 25% | 4.1% | +44.6% | -25.0% | -7.85% | 100% |
| dip35_V2_gescreend_pass | 206 | 18% | 1.9% | +33.5% | -21.3% | -11.48% | 100% |
| dip35_V2_gescreend_fail | 1585 | 24% | 4.7% | +56.3% | -28.2% | -8.04% | 100% |
| dip35_V2_alle | 1832 | 23% | 4.7% | +53.6% | -27.7% | -8.95% | 100% |
| dip35_V3_gescreend_pass | 206 | 7% | 2.4% | +123.9% | -23.1% | -13.14% | 100% |
| dip35_V3_gescreend_fail | 1589 | 12% | 6.2% | +120.3% | -29.8% | -11.68% | 100% |
| dip35_V3_alle | 1834 | 12% | 6.0% | +117.1% | -29.3% | -12.32% | 100% |
| dip40_V1_gescreend_pass | 191 | 14% | 2.1% | +43.6% | -16.1% | -8.01% | 98% |
| dip40_V1_gescreend_fail | 1527 | 25% | 4.1% | +48.4% | -25.6% | -6.98% | 100% |
| dip40_V1_alle | 1761 | 24% | 4.1% | +47.3% | -24.8% | -7.36% | 100% |
| dip40_V2_gescreend_pass | 192 | 14% | 2.1% | +47.6% | -20.2% | -10.68% | 99% |
| dip40_V2_gescreend_fail | 1535 | 24% | 4.4% | +57.4% | -27.8% | -7.24% | 100% |
| dip40_V2_alle | 1756 | 23% | 4.4% | +56.2% | -27.2% | -8.07% | 100% |
| dip40_V3_gescreend_pass | 192 | 6% | 2.6% | +108.4% | -21.9% | -13.78% | 100% |
| dip40_V3_gescreend_fail | 1540 | 12% | 5.8% | +108.5% | -29.5% | -12.92% | 100% |
| dip40_V3_alle | 1759 | 11% | 5.7% | +106.5% | -28.9% | -13.41% | 100% |
| dip45_V1_gescreend_pass | 180 | 15% | 2.2% | +49.8% | -15.8% | -6.00% | 95% |
| dip45_V1_gescreend_fail | 1479 | 27% | 3.5% | +50.3% | -25.0% | -4.60% | 100% |
| dip45_V1_alle | 1689 | 26% | 3.6% | +50.0% | -24.2% | -5.01% | 100% |
| dip45_V2_gescreend_pass | 180 | 19% | 2.8% | +51.7% | -19.8% | -5.86% | 97% |
| dip45_V2_gescreend_fail | 1483 | 25% | 3.9% | +62.3% | -27.1% | -4.74% | 100% |
| dip45_V2_alle | 1684 | 24% | 4.0% | +60.9% | -26.5% | -5.24% | 100% |
| dip45_V3_gescreend_pass | 180 | 7% | 3.3% | +197.6% | -21.2% | -5.43% | 98% |
| dip45_V3_gescreend_fail | 1487 | 13% | 5.5% | +119.3% | -28.9% | -9.55% | 100% |
| dip45_V3_alle | 1686 | 12% | 5.5% | +122.5% | -28.2% | -9.45% | 100% |

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
Sep 11 03:39:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:38,568 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:03:39:38 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 03:39:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:38,929 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:03:39:38 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 03:39:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:56,910 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 03:39:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:39:59,457 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 11 03:40:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:09,286 main INFO screen PHAPIL pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 03:40:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:30,010 main INFO screen $MEOW pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 03:40:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:37,066 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:40:37 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
Sep 11 03:40:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:40:58,045 main INFO screen Cockroach pass=1 dev=2.99 ins=11.28 pro=56 1a=False 1b=False 2=False (3.3s)
Sep 11 03:41:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:15,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:41:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:15,736 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:41:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:16,603 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.1s)
Sep 11 03:41:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:22,653 main INFO screen help pass=0 dev=1.77 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 03:41:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:34,542 main INFO screen Rolex pass=0 dev=2.49 ins=0.0 pro=2 1a=False 1b=False 2=False (3.6s)
Sep 11 03:41:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:35,541 main INFO screen TRIGGER pass=0 dev=0.16 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 03:41:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:40,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:41:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:40,444 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:41:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:41:40,796 main INFO screen FLYGUY pass=0 dev=0.0 ins=15.94 pro=51 1a=False 1b=False 2=True (0.5s)
Sep 11 03:42:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:04,459 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:42:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:04,549 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:42:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:04,907 main INFO screen FLYGUY pass=0 dev=0.0 ins=12.46 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 11 03:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:41,473 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:41,566 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:42:41,766 main INFO screen pap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 03:43:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:18,354 main INFO screen LONG pass=0 dev=9.75 ins=0.0 pro=9 1a=False 1b=False 2=False (3.9s)
Sep 11 03:43:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:23,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:43:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:23,858 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:43:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:24,036 main INFO screen Sub5 pass=0 dev=0.0 ins=11.25 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 11 03:43:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:38,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:43:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:38,329 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:43:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:43:38,466 main INFO screen SOLIEN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 03:44:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:44:04,990 main INFO screen 🚀 pass=0 dev=0.44 ins=0.0 pro=7 1a=False 1b=False 2=False (3.2s)
Sep 11 03:44:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:44:21,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:44:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:44:21,291 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:44:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:44:21,589 main INFO screen TITS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 03:45:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:45:29,149 main INFO screen DIBS pass=0 dev=15.17 ins=0.0 pro=23 1a=False 1b=True 2=False (1.9s)
Sep 11 03:45:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:45:34,023 main INFO screen PHAPIL pass=0 dev=0.14 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 03:45:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:45:38,101 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:45:38 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 03:46:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:46:37,310 main INFO screen Sippp pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 03:46:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:46:38,560 main INFO screen Squad pass=0 dev=0.22 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 03:46:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:46:59,658 main INFO screen MAYHM pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (4.2s)
Sep 11 03:47:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:00,953 main INFO screen KIKE pass=0 dev=3.43 ins=25.13 pro=56 1a=False 1b=False 2=True (5.0s)
Sep 11 03:47:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:10,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:47:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:10,622 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:47:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:10,896 main INFO screen WALLETLESS pass=0 dev=0.0 ins=14.06 pro=14 1a=False 1b=False 2=True (0.5s)
Sep 11 03:47:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:15,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:47:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:15,769 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:47:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:15,904 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 03:47:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:36,313 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:47:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:36,412 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:47:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:36,595 main INFO screen Squad pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 03:47:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:47:40,476 main INFO screen WINSKI pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 03:48:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:00,039 main INFO screen FlyTrap pass=1 dev=2.93 ins=10.98 pro=51 1a=False 1b=False 2=False (3.6s)
Sep 11 03:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:05,101 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:05,215 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:05,354 main INFO screen Sorkin pass=0 dev=0.0 ins=12.72 pro=23 1a=False 1b=False 2=True (0.3s)
Sep 11 03:48:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:21,560 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:48:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:21,703 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:48:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:48:21,870 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 03:49:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:05,118 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:49:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:05,621 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:49:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:06,188 main INFO screen PEMP pass=0 dev=0.0 ins=11.95 pro=14 1a=False 1b=False 2=True (1.8s)
Sep 11 03:49:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:06,734 main INFO screen help pass=0 dev=0.48 ins=0.0 pro=3 1a=False 1b=False 2=False (4.9s)
Sep 11 03:49:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:06,859 main INFO screen BAO pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (4.6s)
Sep 11 03:49:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:06,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:49:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:07,121 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:49:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:07,236 main INFO screen BlackRock pass=0 dev=0.0 ins=12.72 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 03:49:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:32,852 main INFO screen rock pass=1 dev=0.0 ins=6.86 pro=29 1a=False 1b=False 2=False (4.0s)
Sep 11 03:49:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:35,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:49:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:36,013 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:49:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:36,170 main INFO screen PUKy pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 03:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:49,637 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:49,795 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:49:49,932 main INFO screen ZPONS pass=0 dev=0.0 ins=79.24 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 03:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:30,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:30,928 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:50:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:31,119 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 03:50:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:38,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 03:50:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:38,253 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 03:50:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:38,394 main INFO screen Midas pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 03:50:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 03:50:43,811 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:03:50:43 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
