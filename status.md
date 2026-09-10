# Schaduwbot status

- tijd: 2026-09-10 19:17:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 hours, 30 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 607/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 19741, "tokens_in_memory": 1445, "msgs": 3753371, "trades": 675828, "creates": 7867, "decode_fail": 50081, "rpc_calls": 11459, "rpc_errors": 1191, "sol_usd": 99.79733312901031, "open_positions": 55}
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
Sep 10 19:10:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:10:09,159 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:10:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:10:09,273 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:10:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:10:09,479 main INFO screen MEME pass=0 dev=0.0 ins=25.77 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 10 19:11:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:20,745 main INFO screen HOPPY pass=0 dev=0.0 ins=25.42 pro=19 1a=False 1b=False 2=False (1.8s)
Sep 10 19:11:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:23,713 main INFO screen $FROGGY pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=True (8.0s)
Sep 10 19:11:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:33,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:11:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:33,773 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:11:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:33,946 main INFO screen Lab pass=0 dev=0.0 ins=25.94 pro=20 1a=False 1b=False 2=True (0.4s)
Sep 10 19:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:37,154 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:11:37 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:11:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:58,588 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:11:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:11:58,713 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:12:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:03,740 main INFO screen 34% pass=0 dev=3.39 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 10 19:12:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:05,848 main INFO screen mind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.3s)
Sep 10 19:12:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:23,400 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:12:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:23,510 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:12:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:23,840 main INFO screen GOSTA pass=0 dev=0.0 ins=28.27 pro=18 1a=False 1b=False 2=True (0.5s)
Sep 10 19:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:34,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:34,729 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:12:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:34,882 main INFO screen FLYWARE pass=0 dev=0.0 ins=17.82 pro=16 1a=False 1b=False 2=True (0.3s)
Sep 10 19:12:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:35,683 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:12:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:35,818 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:12:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:12:42,659 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.0s)
Sep 10 19:13:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:11,464 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:13:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:11,525 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:13:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:13,193 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:13:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:13,266 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:13:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:16,686 main INFO screen CPU pass=0 dev=0.0 ins=44.38 pro=4 1a=False 1b=False 2=True (5.3s)
Sep 10 19:13:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:17,854 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (4.7s)
Sep 10 19:13:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:39,033 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:13:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:39,123 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:13:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:45,541 main INFO screen GrokAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 10 19:13:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:51,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:13:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:51,669 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:13:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:13:58,472 main INFO screen APEZCAT pass=1 dev=0.0 ins=1.76 pro=26 1a=False 1b=False 2=False (7.0s)
Sep 10 19:14:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:06,325 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:14:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:06,481 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:14:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:10,605 main INFO screen MetaMask pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 10 19:14:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:12,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:14:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:12,330 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:14:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:16,249 main INFO screen GIGAGAGA pass=0 dev=0.0 ins=37.84 pro=13 1a=False 1b=False 2=True (4.1s)
Sep 10 19:14:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:20,670 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:14:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:20,793 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:26,514 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.9s)
Sep 10 19:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:26,527 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:14:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:26,671 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:14:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:30,749 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 19:14:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:34,961 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:14:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:35,624 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:14:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:39,595 main INFO screen RCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 10 19:14:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:41,050 main INFO screen DRAGO pass=0 dev=0.18 ins=34.38 pro=43 1a=False 1b=False 2=True (8.6s)
Sep 10 19:14:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:14:47,514 main INFO screen GLDCAT pass=0 dev=0.73 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 10 19:15:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:08,484 main INFO screen CHAROC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.2s)
Sep 10 19:15:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:19,128 main INFO screen $NXT pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 10 19:15:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:25,697 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:15:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:25,817 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:15:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:32,804 main INFO screen PEPE pass=0 dev=0.0 ins=79.03 pro=6 1a=False 1b=False 2=True (7.2s)
Sep 10 19:15:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:34,768 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:15:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:34,821 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:15:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:36,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:15:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:36,798 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:15:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:40,969 main INFO screen ROBIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 10 19:15:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:41,707 main INFO screen stankmemes pass=0 dev=0.0 ins=37.66 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 10 19:15:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:58,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:15:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:15:58,831 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:16:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:05,004 main INFO screen ShoeCoin pass=0 dev=0.0 ins=38.16 pro=2 1a=False 1b=False 2=True (6.4s)
Sep 10 19:16:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:05,995 main INFO screen Anonymouse pass=0 dev=0.0 ins=25.32 pro=17 1a=False 1b=False 2=False (2.0s)
Sep 10 19:16:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:24,886 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:16:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:24,921 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:16:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:25,215 main INFO screen peen pass=0 dev=0.0 ins=26.25 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 10 19:16:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:25,769 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:16:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:25,905 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:16:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:26,632 main INFO screen GOYCAT pass=0 dev=0.36 ins=0.0 pro=3 1a=False 1b=False 2=False (7.1s)
Sep 10 19:16:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:29,360 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:16:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:29,526 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:16:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:31,099 main INFO screen MOOMOO pass=0 dev=0.0 ins=37.58 pro=13 1a=False 1b=False 2=True (5.4s)
Sep 10 19:16:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:33,092 main INFO screen $LesbCoin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 10 19:16:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:16:37,072 main INFO screen RocketFrog pass=0 dev=5.1 ins=5.87 pro=6 1a=False 1b=False 2=False (1.9s)
Sep 10 19:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:17,478 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:17:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:17,570 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:17:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:17:18,628 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:17:18 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
