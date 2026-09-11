# Schaduwbot status

- tijd: 2026-09-11 02:57:03 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 13 hours, 10 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 645/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 47326, "tokens_in_memory": 974, "msgs": 8805632, "trades": 1692975, "creates": 18641, "decode_fail": 117142, "rpc_calls": 27785, "rpc_errors": 2684, "sol_usd": 99.32026820581638, "open_positions": 34}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 02:48 UTC

Gelogde schaduwtrades: **14754**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 3510 | 408 | 0 | 409 | 43 | 792 | 2399 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 190 | 15% | 1.6% | +37.8% | -16.8% | -8.51% | 97% |
| dip35_V1_gescreend_fail | 1467 | 26% | 4.0% | +44.5% | -25.4% | -7.54% | 100% |
| dip35_V1_alle | 1710 | 25% | 4.1% | +43.2% | -24.8% | -7.98% | 100% |
| dip35_V2_gescreend_pass | 191 | 17% | 2.1% | +29.7% | -21.5% | -12.69% | 100% |
| dip35_V2_gescreend_fail | 1476 | 24% | 4.7% | +56.5% | -28.0% | -7.68% | 100% |
| dip35_V2_alle | 1704 | 23% | 4.8% | +53.5% | -27.6% | -8.73% | 100% |
| dip35_V3_gescreend_pass | 190 | 6% | 2.6% | +138.2% | -23.4% | -13.19% | 100% |
| dip35_V3_gescreend_fail | 1483 | 12% | 6.2% | +118.9% | -29.7% | -11.67% | 100% |
| dip35_V3_alle | 1708 | 12% | 6.1% | +116.4% | -29.2% | -12.27% | 100% |
| dip40_V1_gescreend_pass | 178 | 13% | 2.2% | +41.2% | -16.4% | -8.95% | 97% |
| dip40_V1_gescreend_fail | 1424 | 25% | 4.1% | +47.2% | -25.4% | -7.22% | 100% |
| dip40_V1_alle | 1641 | 24% | 4.1% | +46.0% | -24.6% | -7.60% | 100% |
| dip40_V2_gescreend_pass | 179 | 13% | 2.2% | +44.7% | -20.4% | -12.05% | 99% |
| dip40_V2_gescreend_fail | 1433 | 24% | 4.5% | +57.8% | -27.7% | -6.92% | 100% |
| dip40_V2_alle | 1637 | 23% | 4.5% | +56.5% | -27.1% | -7.88% | 100% |
| dip40_V3_gescreend_pass | 179 | 6% | 2.8% | +118.0% | -22.1% | -13.53% | 100% |
| dip40_V3_gescreend_fail | 1440 | 12% | 5.9% | +106.8% | -29.4% | -13.13% | 100% |
| dip40_V3_alle | 1642 | 11% | 5.8% | +105.3% | -28.8% | -13.51% | 100% |
| dip45_V1_gescreend_pass | 166 | 14% | 2.4% | +47.6% | -15.6% | -6.51% | 94% |
| dip45_V1_gescreend_fail | 1378 | 27% | 3.5% | +49.2% | -24.8% | -4.76% | 100% |
| dip45_V1_alle | 1572 | 26% | 3.6% | +48.7% | -24.0% | -5.17% | 100% |
| dip45_V2_gescreend_pass | 165 | 19% | 3.0% | +39.5% | -19.5% | -8.39% | 96% |
| dip45_V2_gescreend_fail | 1383 | 25% | 3.9% | +62.8% | -27.0% | -4.18% | 100% |
| dip45_V2_alle | 1567 | 25% | 4.0% | +60.4% | -26.4% | -4.99% | 100% |
| dip45_V3_gescreend_pass | 166 | 7% | 3.6% | +173.8% | -21.1% | -6.98% | 98% |
| dip45_V3_gescreend_fail | 1390 | 13% | 5.5% | +119.2% | -28.8% | -9.41% | 100% |
| dip45_V3_alle | 1573 | 12% | 5.5% | +120.8% | -28.1% | -9.48% | 100% |

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
Sep 11 02:39:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:39:43,638 main INFO screen Trum  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 02:40:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:22,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:40:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:22,311 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:40:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:22,516 main INFO screen FLYBRAIN pass=1 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (0.4s)
Sep 11 02:40:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:37,827 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:40:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:37,972 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:40:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:38,172 main INFO screen MetaMask pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 02:40:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:40:41,913 main INFO screen 💩~4° pass=1 dev=2.08 ins=9.55 pro=36 1a=False 1b=False 2=False (3.8s)
Sep 11 02:41:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:03,185 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:41:03 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 02:41:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:20,399 main INFO screen Waff pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 02:41:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:54,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:41:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:54,239 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:41:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:54,685 main INFO screen Solsisters pass=0 dev=0.0 ins=20.54 pro=16 1a=False 1b=False 2=True (0.6s)
Sep 11 02:41:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:41:59,011 main INFO screen DOOROC pass=0 dev=0.39 ins=0.0 pro=3 1a=False 1b=False 2=False (4.8s)
Sep 11 02:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:42:41,083 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:42:41,188 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:42:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:42:43,398 main INFO screen bum pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 02:44:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:44:54,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:44:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:44:55,077 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:44:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:44:55,279 main INFO screen TolyGuac pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 02:45:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:45:00,044 main INFO screen LONGDONG pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (1.9s)
Sep 11 02:45:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:45:20,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:45:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:45:20,168 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:45:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:45:20,367 main INFO screen WhiteWhale pass=0 dev=0.0 ins=56.16 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 02:45:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:45:42,741 main INFO screen SUPERCYCLE pass=1 dev=0.0 ins=9.25 pro=40 1a=False 1b=False 2=False (2.0s)
Sep 11 02:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:27,172 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:27,267 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:27,451 main INFO screen MARIO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 02:46:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:28,409 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:46:28 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 02:46:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:43,884 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:46:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:43,982 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:46:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:46:44,175 main INFO screen CME pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 02:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:47:05,569 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:47:05,672 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:47:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:47:05,870 main INFO screen IMD pass=0 dev=0.0 ins=23.02 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 02:47:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:47:11,835 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 02:48:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:48:54,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:48:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:48:55,493 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:48:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:48:56,100 main INFO screen TRUM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 11 02:48:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:48:58,137 main INFO screen NEKO pass=0 dev=0.0 ins=19.33 pro=76 1a=False 1b=False 2=True (4.3s)
Sep 11 02:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:48:59,566 main INFO screen LMAO pass=0 dev=0.67 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 11 02:49:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:27,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:49:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:27,563 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:49:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:27,897 main INFO screen DesktopFly pass=0 dev=0.0 ins=6.16 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 11 02:49:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:54,125 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:49:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:54,227 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:49:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:49:54,406 main INFO screen ChichNug pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 02:50:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:50:23,302 main INFO screen SCRVAN pass=0 dev=1.23 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 02:51:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:06,296 main INFO screen TM pass=0 dev=6.18 ins=0.0 pro=16 1a=False 1b=False 2=False (3.5s)
Sep 11 02:51:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:09,844 main INFO screen $IMANG pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 02:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:14,523 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:14,635 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:51:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:14,767 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 02:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:22,363 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.4s)
Sep 11 02:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:33,341 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:33,482 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:33,803 main INFO screen NEKO pass=0 dev=0.0 ins=13.27 pro=17 1a=False 1b=False 2=True (0.5s)
Sep 11 02:51:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:51:37,289 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:51:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 11 02:52:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:52:42,332 main INFO screen DINO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 11 02:52:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:52:47,699 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:52:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:52:47,819 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:52:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:52:48,365 main INFO screen VOICECHAT pass=0 dev=0.0 ins=27.15 pro=9 1a=False 1b=False 2=True (0.7s)
Sep 11 02:53:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:53:20,317 main INFO screen LMAO pass=0 dev=0.34 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 02:53:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:53:28,881 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:53:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:53:28,965 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:53:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:53:29,118 main INFO screen bullshit pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.3s)
Sep 11 02:54:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:54:22,638 main INFO screen Quan pass=0 dev=0.36 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 02:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:54:32,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:54:32,693 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:54:32,817 main INFO screen Catanyahu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 02:55:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:55:12,451 main INFO screen 👑👑👑 pass=0 dev=6.63 ins=20.54 pro=27 1a=False 1b=False 2=False (2.4s)
Sep 11 02:55:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:55:45,214 main INFO screen 👑 pass=0 dev=0.0 ins=12.08 pro=70 1a=False 1b=False 2=True (2.7s)
Sep 11 02:56:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:09,726 main INFO screen doughboi pass=0 dev=1.08 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 02:56:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:12,969 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:56:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:13,054 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:56:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:13,242 main INFO screen NFLX pass=1 dev=0.0 ins=11.6 pro=29 1a=False 1b=False 2=False (0.3s)
Sep 11 02:56:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:20,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:56:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:21,041 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:56:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:56:21,154 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 02:57:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:57:03,849 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:57:03 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
