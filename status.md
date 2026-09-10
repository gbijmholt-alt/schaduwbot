# Schaduwbot status

- tijd: 2026-09-10 18:55:04 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 hours, 8 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 642/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 18408, "tokens_in_memory": 1469, "msgs": 3407599, "trades": 623131, "creates": 7306, "decode_fail": 47097, "rpc_calls": 10606, "rpc_errors": 1091, "sol_usd": 99.84836449135885, "open_positions": 71}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 18:48 UTC

Gelogde schaduwtrades: **5438**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 7151 | 973 | 20 | 973 | 110 | 1831 | 5438 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 89 | 14% | 1.1% | +34.1% | -15.2% | -8.57% | 82% |
| dip35_V1_gescreend_fail | 521 | 26% | 4.8% | +45.4% | -26.2% | -7.26% | 100% |
| dip35_V1_alle | 633 | 25% | 4.4% | +43.8% | -25.1% | -8.02% | 100% |
| dip35_V2_gescreend_pass | 88 | 17% | 1.1% | +31.0% | -19.9% | -11.21% | 88% |
| dip35_V2_gescreend_fail | 520 | 24% | 5.2% | +55.6% | -28.0% | -8.37% | 100% |
| dip35_V2_alle | 626 | 22% | 4.8% | +51.8% | -27.3% | -9.47% | 100% |
| dip35_V3_gescreend_pass | 88 | 6% | 1.1% | +75.2% | -21.9% | -16.34% | 95% |
| dip35_V3_gescreend_fail | 530 | 12% | 6.4% | +100.3% | -29.6% | -13.67% | 100% |
| dip35_V3_alle | 634 | 12% | 5.8% | +94.8% | -28.9% | -14.67% | 100% |
| dip40_V1_gescreend_pass | 82 | 16% | 1.2% | +43.4% | -14.6% | -5.37% | 69% |
| dip40_V1_gescreend_fail | 507 | 24% | 5.5% | +50.2% | -26.7% | -8.02% | 100% |
| dip40_V1_alle | 608 | 23% | 4.9% | +48.8% | -25.3% | -8.02% | 100% |
| dip40_V2_gescreend_pass | 81 | 15% | 1.2% | +54.4% | -19.6% | -8.68% | 82% |
| dip40_V2_gescreend_fail | 508 | 23% | 5.5% | +59.2% | -28.5% | -8.13% | 100% |
| dip40_V2_alle | 603 | 22% | 5.0% | +57.9% | -27.6% | -8.73% | 100% |
| dip40_V3_gescreend_pass | 82 | 8% | 1.2% | +57.1% | -21.1% | -14.41% | 92% |
| dip40_V3_gescreend_fail | 514 | 12% | 7.0% | +97.4% | -30.4% | -14.49% | 100% |
| dip40_V3_alle | 608 | 12% | 6.2% | +91.1% | -29.4% | -14.95% | 100% |
| dip45_V1_gescreend_pass | 74 | 16% | 2.7% | +44.4% | -14.9% | -5.25% | 70% |
| dip45_V1_gescreend_fail | 488 | 25% | 4.9% | +52.2% | -26.1% | -6.22% | 100% |
| dip45_V1_alle | 578 | 24% | 4.7% | +51.1% | -25.0% | -6.54% | 100% |
| dip45_V2_gescreend_pass | 73 | 20% | 2.7% | +42.8% | -18.6% | -5.96% | 71% |
| dip45_V2_gescreend_fail | 486 | 24% | 5.1% | +64.3% | -28.1% | -5.89% | 100% |
| dip45_V2_alle | 571 | 24% | 4.9% | +61.3% | -27.2% | -6.44% | 100% |
| dip45_V3_gescreend_pass | 74 | 8% | 2.7% | +108.1% | -19.8% | -9.47% | 88% |
| dip45_V3_gescreend_fail | 493 | 14% | 6.5% | +127.9% | -29.7% | -7.32% | 100% |
| dip45_V3_alle | 577 | 13% | 6.1% | +124.9% | -28.7% | -8.18% | 100% |

## Beste variant: dip45_V1_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 18:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:53,059 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:53,192 main INFO screen Nasduck pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 18:43:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:43:17,381 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (3.0s)
Sep 10 18:43:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:43:58,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:43:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:43:58,980 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:43:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:43:59,171 main INFO screen BEPE pass=0 dev=0.0 ins=31.74 pro=21 1a=False 1b=False 2=True (0.4s)
Sep 10 18:44:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:44:38,313 main INFO screen 34% pass=0 dev=9.55 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 18:44:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:44:47,337 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:44:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:44:47,427 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:44:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:44:47,580 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 18:44:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:44:52,297 aiohttp.access INFO 185.226.92.131 [10/Sep/2026:18:44:52 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 10 18:45:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:04,780 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:45:04 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 18:45:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:09,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:45:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:11,304 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:45:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:15,375 main INFO screen PRIVACY pass=0 dev=0.0 ins=19.88 pro=51 1a=False 1b=False 2=True (9.2s)
Sep 10 18:45:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:32,246 main INFO screen CITY CAT pass=0 dev=15.17 ins=7.06 pro=34 1a=False 1b=False 2=False (2.1s)
Sep 10 18:45:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:45:41,057 main INFO screen LMAO pass=0 dev=1.08 ins=0.0 pro=5 1a=False 1b=False 2=False (2.6s)
Sep 10 18:46:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:46:31,224 aiohttp.access INFO 204.76.203.49 [10/Sep/2026:18:46:31 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 10 18:46:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:46:31,249 aiohttp.access INFO 204.76.203.49 [10/Sep/2026:18:46:31 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 10 18:46:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:46:37,987 main INFO screen RICK pass=0 dev=4.69 ins=0.0 pro=4 1a=False 1b=False 2=False (3.7s)
Sep 10 18:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:14,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:14,413 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:14,618 main INFO screen BILLY pass=0 dev=0.0 ins=25.84 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 18:47:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:40,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:47:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:40,836 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:47:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:47:41,032 main INFO screen Cat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 18:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:05,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:05,768 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:48:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:05,977 main INFO screen Lapauti pass=0 dev=0.0 ins=77.44 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 18:48:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:13,776 main INFO screen APK pass=0 dev=0.41 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 10 18:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:59,378 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:59,507 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:59,753 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:48:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:48:59,890 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:49:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:00,622 main INFO screen etse pass=0 dev=0.0 ins=30.6 pro=19 1a=False 1b=False 2=True (1.4s)
Sep 10 18:49:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:00,809 main INFO screen Bazaar pass=0 dev=0.0 ins=43.42 pro=40 1a=False 1b=False 2=True (1.5s)
Sep 10 18:49:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:02,021 main INFO screen RETARDO pass=0 dev=2.08 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 10 18:49:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:03,925 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:04,045 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:49:04,169 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:50:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:04,950 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:50:04 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 18:50:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:09,499 main INFO screen $AURA pass=0 dev=4.48 ins=0.0 pro=4 1a=False 1b=False 2=False (3.6s)
Sep 10 18:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:30,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:30,351 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:30,581 main INFO screen NOMU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 18:50:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:47,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:50:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:47,571 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:50:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:47,785 main INFO screen $FROGGY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 18:50:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:50:53,440 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.5s)
Sep 10 18:51:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:17,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:51:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:17,504 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:51:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:17,822 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.6s)
Sep 10 18:51:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:17,994 main INFO screen rug pass=0 dev=0.81 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 18:51:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:18,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:51:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:18,493 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:51:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:18,619 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 18:51:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:38,964 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:51:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:39,058 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:51:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:51:39,246 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 18:52:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:52:01,449 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.4s)
Sep 10 18:52:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:52:18,220 main INFO screen MEOW pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 18:52:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:52:30,528 main INFO screen Geee pass=0 dev=0.19 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 10 18:52:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:52:32,374 main INFO screen RICK pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=True (1.9s)
Sep 10 18:53:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:07,624 main INFO screen CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 18:53:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:27,098 main INFO screen Butterfly pass=0 dev=14.39 ins=0.0 pro=20 1a=False 1b=False 2=False (3.0s)
Sep 10 18:53:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:36,563 main INFO screen beer pass=0 dev=4.81 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 10 18:53:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:48,826 main INFO screen SXSN pass=0 dev=9.55 ins=0.0 pro=3 1a=False 1b=False 2=True (2.1s)
Sep 10 18:53:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:52,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:53:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:52,943 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:53:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:53:53,291 main INFO screen OINKINGTON pass=0 dev=0.0 ins=19.82 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 18:54:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:21,521 main INFO screen $FROGGY pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=True (2.3s)
Sep 10 18:54:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:22,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:23,043 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:23,170 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:54:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:27,505 main INFO screen CONVICTION pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (3.5s)
Sep 10 18:54:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:28,383 main INFO screen BRAIN pass=0 dev=6.63 ins=0.76 pro=20 1a=False 1b=True 2=False (1.7s)
Sep 10 18:54:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:42,494 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:54:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:42,621 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:54:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:54:42,749 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:55:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:55:04,942 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:55:04 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
