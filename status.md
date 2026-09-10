# Schaduwbot status

- tijd: 2026-09-10 17:42:11 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 hours, 55 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 582/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 14035, "tokens_in_memory": 1417, "msgs": 2500869, "trades": 464344, "creates": 5560, "decode_fail": 40084, "rpc_calls": 7797, "rpc_errors": 884, "sol_usd": 100.07359316422244, "open_positions": 61}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 16:48 UTC

Gelogde schaduwtrades: **3046**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 4315 | 586 | 12 | 586 | 77 | 1040 | 3046 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 57 | 10% | 1.8% | +36.3% | -17.2% | -11.56% | 79% |
| dip35_V1_gescreend_fail | 284 | 26% | 5.6% | +47.6% | -27.7% | -8.06% | 100% |
| dip35_V1_alle | 355 | 24% | 5.1% | +46.3% | -26.4% | -9.24% | 100% |
| dip35_V2_gescreend_pass | 54 | 11% | 1.9% | +22.9% | -21.0% | -16.12% | 85% |
| dip35_V2_gescreend_fail | 284 | 22% | 6.0% | +79.1% | -29.5% | -5.82% | 100% |
| dip35_V2_alle | 350 | 20% | 5.4% | +71.9% | -28.6% | -8.25% | 100% |
| dip35_V3_gescreend_pass | 57 | 5% | 1.8% | +32.4% | -22.7% | -19.77% | 90% |
| dip35_V3_gescreend_fail | 291 | 13% | 7.9% | +128.1% | -31.2% | -10.43% | 100% |
| dip35_V3_alle | 358 | 12% | 7.0% | +115.9% | -30.3% | -12.74% | 100% |
| dip40_V1_gescreend_pass | 54 | 17% | 1.9% | +42.6% | -16.2% | -6.41% | 67% |
| dip40_V1_gescreend_fail | 277 | 24% | 6.1% | +55.7% | -27.9% | -7.36% | 100% |
| dip40_V1_alle | 343 | 23% | 5.5% | +53.9% | -26.5% | -7.77% | 100% |
| dip40_V2_gescreend_pass | 51 | 14% | 2.0% | +61.0% | -20.1% | -8.95% | 72% |
| dip40_V2_gescreend_fail | 278 | 22% | 6.1% | +84.9% | -29.7% | -5.01% | 100% |
| dip40_V2_alle | 339 | 20% | 5.6% | +80.7% | -28.6% | -6.38% | 100% |
| dip40_V3_gescreend_pass | 54 | 7% | 1.9% | +25.0% | -21.3% | -17.86% | 87% |
| dip40_V3_gescreend_fail | 281 | 14% | 8.2% | +119.3% | -31.8% | -10.80% | 100% |
| dip40_V3_alle | 343 | 13% | 7.3% | +108.2% | -30.5% | -12.67% | 100% |
| dip45_V1_gescreend_pass | 47 | 19% | 2.1% | +45.4% | -16.2% | -4.39% | 63% |
| dip45_V1_gescreend_fail | 261 | 25% | 6.1% | +56.0% | -28.4% | -7.07% | 100% |
| dip45_V1_alle | 320 | 24% | 5.6% | +54.5% | -27.2% | -7.29% | 100% |
| dip45_V2_gescreend_pass | 45 | 20% | 2.2% | +45.1% | -18.4% | -5.72% | 60% |
| dip45_V2_gescreend_fail | 263 | 23% | 6.5% | +87.6% | -29.8% | -3.01% | 100% |
| dip45_V2_alle | 318 | 22% | 6.0% | +80.5% | -28.6% | -4.29% | 100% |
| dip45_V3_gescreend_pass | 47 | 8% | 2.1% | +107.5% | -20.0% | -9.20% | 77% |
| dip45_V3_gescreend_fail | 265 | 16% | 7.9% | +122.2% | -31.3% | -7.58% | 100% |
| dip45_V3_alle | 320 | 14% | 7.2% | +118.5% | -30.1% | -8.71% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 17:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:39,400 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:39,529 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:39,744 main INFO screen TEMPLE pass=0 dev=0.0 ins=18.37 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 10 17:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:40,428 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:40,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:34:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:40,708 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (0.3s)
Sep 10 17:34:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:56,301 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:34:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:56,393 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:34:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:34:56,582 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 17:35:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:00,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:35:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:00,953 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:35:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:01,221 main INFO screen Rishabh pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 17:35:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:16,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,042 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,571 main INFO screen 5 pass=0 dev=0.0 ins=8.13 pro=40 1a=False 1b=False 2=True (1.7s)
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,680 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,936 main INFO screen jobdq pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.8s)
Sep 10 17:35:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:17,985 main INFO screen 5 pass=1 dev=0.0 ins=14.61 pro=25 1a=False 1b=False 2=False (4.5s)
Sep 10 17:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:23,930 main INFO screen SNOP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 10 17:35:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:30,189 main INFO screen HALH pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 10 17:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:38,058 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:38,186 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:38,341 main INFO screen 5 pass=0 dev=0.0 ins=18.59 pro=28 1a=False 1b=False 2=True (0.4s)
Sep 10 17:35:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:54,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:35:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:54,673 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:35:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:55,366 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (1.7s)
Sep 10 17:35:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:35:55,983 main INFO screen $LAPTOP pass=1 dev=1.8 ins=0.35 pro=27 1a=False 1b=False 2=False (3.9s)
Sep 10 17:36:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:36:03,104 main INFO screen PONDSCOIN pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 10 17:36:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:36:34,709 main INFO screen gnome pass=0 dev=6.63 ins=0.0 pro=43 1a=False 1b=False 2=False (2.7s)
Sep 10 17:36:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:36:59,623 main INFO screen Kirky pass=1 dev=0.03 ins=0.0 pro=38 1a=False 1b=False 2=False (5.0s)
Sep 10 17:37:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:01,653 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:37:01 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
Sep 10 17:37:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:07,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:37:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:07,576 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:37:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:07,709 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 17:37:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:43,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:37:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:43,595 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:37:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:37:44,172 main INFO screen KEKIUSBOT pass=0 dev=0.0 ins=7.37 pro=7 1a=False 1b=False 2=True (0.8s)
Sep 10 17:38:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:05,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:38:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:06,684 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:38:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:07,539 main INFO screen KEKIUS pass=0 dev=0.0 ins=13.37 pro=23 1a=False 1b=False 2=True (2.1s)
Sep 10 17:38:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:08,738 main INFO screen CEO pass=0 dev=3.43 ins=0.0 pro=61 1a=False 1b=False 2=True (4.3s)
Sep 10 17:38:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:19,760 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:38:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:19,890 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:38:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:20,029 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 17:38:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:22,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:38:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:22,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:38:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:22,524 main INFO screen CRYPT-1 pass=0 dev=0.0 ins=15.14 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 10 17:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:31,640 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:31,762 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:38:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:32,017 main INFO screen KEKIUS pass=1 dev=0.0 ins=13.0 pro=13 1a=False 1b=False 2=False (0.5s)
Sep 10 17:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:59,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:59,625 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:38:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:38:59,818 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 17:39:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:39:24,885 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:39:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:39:25,018 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:39:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:39:25,223 main INFO screen Groyper pass=0 dev=0.0 ins=26.02 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 17:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:26,394 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 10 17:40:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:27,100 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:40:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:27,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:40:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:27,347 main INFO screen juggerjak pass=0 dev=0.0 ins=79.13 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 10 17:40:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:28,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:40:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:28,290 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:40:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:28,470 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 17:40:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:51,210 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:40:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:51,259 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:40:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:51,485 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 17:40:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:40:54,703 main INFO screen KEKIUS pass=1 dev=0.0 ins=3.24 pro=22 1a=False 1b=False 2=False (2.1s)
Sep 10 17:41:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:01,760 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:41:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:01,884 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:41:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:02,212 main INFO screen KEKIUS pass=0 dev=0.0 ins=7.93 pro=30 1a=False 1b=False 2=True (0.5s)
Sep 10 17:41:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:16,021 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:41:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:16,146 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:41:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:16,313 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 17:41:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:26,984 main INFO screen wavy pass=0 dev=0.48 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 10 17:41:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:27,985 main INFO screen KekiusBot pass=0 dev=0.0 ins=0.27 pro=59 1a=False 1b=False 2=True (5.9s)
Sep 10 17:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:37,504 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:37,638 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:41:37,797 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 17:42:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:42:11,964 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:42:11 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
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
