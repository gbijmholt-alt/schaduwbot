# Schaduwbot status

- tijd: 2026-09-10 22:19:58 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 8 hours, 33 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 636/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 30701, "tokens_in_memory": 1539, "msgs": 6182178, "trades": 1158636, "creates": 12599, "decode_fail": 89669, "rpc_calls": 19071, "rpc_errors": 1902, "sol_usd": 99.99837870762667, "open_positions": 91}
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
Sep 10 22:06:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:06:01,269 main INFO screen MEMEFACTORY pass=0 dev=0.41 ins=0.0 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 10 22:06:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:06:03,005 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 10 22:06:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:06:05,358 main INFO screen PATRICK pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 10 22:06:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:06:14,697 main INFO screen CYBERBULL pass=0 dev=0.0 ins=17.61 pro=7 1a=False 1b=False 2=False (7.8s)
Sep 10 22:06:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:06:25,020 main INFO screen MEMESTR pass=1 dev=0.13 ins=0.0 pro=26 1a=False 1b=False 2=False (7.5s)
Sep 10 22:07:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:02,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:07:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:02,586 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:07:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:07,673 main INFO screen Batman pass=0 dev=0.0 ins=79.17 pro=7 1a=False 1b=False 2=True (5.3s)
Sep 10 22:07:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:28,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:07:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:28,514 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:07:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:31,783 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.5s)
Sep 10 22:07:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:50,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:07:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:50,961 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:07:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:07:55,060 main INFO screen BULLIEVE pass=0 dev=0.0 ins=69.42 pro=8 1a=False 1b=False 2=True (4.3s)
Sep 10 22:08:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:05,533 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:08:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:05,579 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:08:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:09,572 main INFO screen SEPE pass=0 dev=0.0 ins=17.28 pro=9 1a=False 1b=False 2=False (4.1s)
Sep 10 22:08:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:12,563 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:08:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:12,690 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:08:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:17,639 main INFO screen PATRICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 10 22:08:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:24,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:08:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:25,096 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:08:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:30,226 main INFO screen Hoodtard pass=0 dev=0.0 ins=23.79 pro=9 1a=False 1b=False 2=True (5.3s)
Sep 10 22:08:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:31,608 main INFO screen CHARLIE  pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 10 22:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:37,537 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:22:08:37 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 10 22:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:08:37,883 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:22:08:37 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 10 22:09:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:12,898 main INFO screen $TTLONG pass=0 dev=0.0 ins=0.82 pro=12 1a=True 1b=False 2=False (8.2s)
Sep 10 22:09:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:33,836 main INFO screen STONK pass=0 dev=8.16 ins=0.0 pro=39 1a=False 1b=False 2=False (8.5s)
Sep 10 22:09:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:37,020 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:09:37 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 10 22:09:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:37,094 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:09:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:37,254 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:09:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:37,583 main INFO screen S&P6900 pass=0 dev=0.0 ins=13.64 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 10 22:09:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:42,959 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:09:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:43,075 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:09:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:09:48,509 main INFO screen GIGAORC pass=0 dev=0.0 ins=20.92 pro=8 1a=False 1b=False 2=True (5.6s)
Sep 10 22:10:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:00,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:10:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:00,968 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:10:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:07,557 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.8s)
Sep 10 22:10:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:30,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:10:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:30,319 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:10:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:10:36,020 main INFO screen COMEBACK pass=0 dev=0.0 ins=46.0 pro=5 1a=False 1b=False 2=True (5.9s)
Sep 10 22:11:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:07,880 main INFO screen 34% pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 10 22:11:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:16,707 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:11:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:16,808 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:11:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:21,241 main INFO screen Sprocket pass=0 dev=0.0 ins=16.91 pro=15 1a=False 1b=False 2=True (4.6s)
Sep 10 22:11:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:51,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:11:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:51,957 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:11:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:11:52,147 main INFO screen NUTS pass=0 dev=0.0 ins=20.09 pro=27 1a=False 1b=False 2=True (0.4s)
Sep 10 22:12:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:01,179 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:12:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:01,315 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:12:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:02,474 main INFO screen $Cat pass=0 dev=0.53 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 10 22:12:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:05,528 main INFO screen PUMPDOG pass=0 dev=0.0 ins=17.92 pro=9 1a=False 1b=False 2=False (4.6s)
Sep 10 22:12:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:07,949 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 10 22:12:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:32,125 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (10.6s)
Sep 10 22:12:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:12:55,400 main INFO screen BAGCOON pass=0 dev=0.65 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 10 22:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:14:18,235 main INFO screen SPRITEBOY pass=0 dev=0.0 ins=17.52 pro=48 1a=False 1b=False 2=True (3.0s)
Sep 10 22:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:14:18,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:14:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:14:18,803 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:14:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:14:23,593 main INFO screen bridgoor pass=0 dev=0.0 ins=15.59 pro=27 1a=False 1b=False 2=True (5.0s)
Sep 10 22:14:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:14:40,643 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:14:40 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 22:15:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:15:00,191 main INFO screen WiggaCock pass=1 dev=0.0 ins=13.21 pro=29 1a=False 1b=False 2=False (3.0s)
Sep 10 22:15:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:15:43,044 main INFO screen NPC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.4s)
Sep 10 22:16:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:16:09,575 main INFO screen pepsurge pass=0 dev=1.41 ins=0.0 pro=9 1a=False 1b=False 2=False (10.7s)
Sep 10 22:17:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:24,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:17:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:24,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:17:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:31,378 main INFO screen chip pass=0 dev=0.0 ins=21.31 pro=23 1a=False 1b=False 2=True (6.7s)
Sep 10 22:17:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:51,487 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:17:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:51,614 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:17:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:54,372 main INFO screen ʞnoɿӘ pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=True (8.4s)
Sep 10 22:17:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:17:58,128 main INFO screen fihdih pass=0 dev=0.0 ins=23.12 pro=14 1a=False 1b=False 2=True (6.7s)
Sep 10 22:18:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:18:48,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:18:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:18:48,504 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:18:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:18:53,758 main INFO screen Spindle pass=0 dev=0.0 ins=16.91 pro=14 1a=False 1b=False 2=True (5.4s)
Sep 10 22:19:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:15,299 main INFO screen catdog pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (10.6s)
Sep 10 22:19:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:33,842 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 22:19:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:33,941 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 22:19:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:37,732 aiohttp.access INFO 185.226.92.131 [10/Sep/2026:22:19:37 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 10 22:19:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:37,967 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.2s)
Sep 10 22:19:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:47,652 main INFO screen SILYAN pass=0 dev=0.0 ins=14.47 pro=36 1a=False 1b=False 2=True (7.5s)
Sep 10 22:19:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 22:19:58,227 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:22:19:58 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
