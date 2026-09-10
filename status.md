# Schaduwbot status

- tijd: 2026-09-10 19:06:28 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 hours, 19 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 606/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 19091, "tokens_in_memory": 1491, "msgs": 3568395, "trades": 647217, "creates": 7596, "decode_fail": 48204, "rpc_calls": 11080, "rpc_errors": 1137, "sol_usd": 99.75534556607393, "open_positions": 93}
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
Sep 10 18:56:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:23,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:56:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:23,666 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:56:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:23,806 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 18:56:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:42,246 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:56:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:42,380 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:56:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:42,612 main INFO screen manatee pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 10 18:56:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:56:56,555 main INFO screen hedgemonke pass=0 dev=24.53 ins=0.0 pro=20 1a=False 1b=False 2=False (2.3s)
Sep 10 18:57:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:18,733 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:57:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:18,823 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:57:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:19,036 main INFO screen MMM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 18:57:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:21,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:57:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:21,771 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:57:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:21,902 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:57:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:25,923 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:57:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:26,087 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:57:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:57:26,228 main INFO screen SYND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 18:58:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:58:42,618 main INFO screen lag pass=0 dev=0.52 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 10 18:58:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:58:42,967 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.6s)
Sep 10 18:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:02,185 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:02,269 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:59:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:02,706 main INFO screen MMM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.6s)
Sep 10 18:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:26,470 main INFO screen CATEUS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 10 18:59:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:29,399 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:59:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:29,582 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:59:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:29,706 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:59:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:45,803 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:59:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:45,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:59:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:46,091 main INFO screen Starbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 18:59:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:59:59,153 main INFO screen $WRLD pass=0 dev=0.32 ins=0.0 pro=6 1a=False 1b=False 2=False (3.0s)
Sep 10 19:00:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:00:37,143 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:00:37 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
Sep 10 19:00:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:00:52,253 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:00:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:00:52,372 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:00:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:00:53,223 main INFO screen ch pass=0 dev=4.24 ins=0.0 pro=4 1a=False 1b=False 2=False (9.1s)
Sep 10 19:00:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:00:58,144 main INFO screen corn pass=0 dev=0.0 ins=21.04 pro=13 1a=False 1b=False 2=True (6.0s)
Sep 10 19:01:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:30,092 main INFO screen up pass=0 dev=0.46 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 10 19:01:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:31,455 main INFO screen Maple pass=0 dev=0.0 ins=24.59 pro=67 1a=False 1b=False 2=True (4.1s)
Sep 10 19:01:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:35,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:01:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:35,705 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:01:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:42,271 main INFO screen Anonjak pass=0 dev=0.0 ins=78.49 pro=6 1a=False 1b=False 2=True (6.7s)
Sep 10 19:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:49,246 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:01:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:49,421 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:01:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:01:56,570 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 10 19:02:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:02:12,904 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:02:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:02:13,003 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:02:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:02:19,632 main INFO screen LC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 10 19:03:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:13,856 main INFO screen Hunter pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 10 19:03:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:28,874 main INFO screen PWOG pass=0 dev=0.18 ins=34.12 pro=15 1a=False 1b=False 2=True (9.3s)
Sep 10 19:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:49,679 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:03:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:49,802 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:03:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:52,851 main INFO screen DERP pass=0 dev=0.9 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 10 19:03:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:03:54,607 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (5.0s)
Sep 10 19:04:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:04:02,273 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:04:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:04:02,361 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:04:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:04:06,517 main INFO screen RUSH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 19:04:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:04:40,352 main INFO screen ZOL pass=1 dev=0.0 ins=16.5 pro=61 1a=False 1b=False 2=False (3.9s)
Sep 10 19:04:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:04:51,280 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.7s)
Sep 10 19:05:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:06,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:05:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:06,748 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:05:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:11,450 main INFO screen FAKER pass=0 dev=0.0 ins=46.11 pro=14 1a=False 1b=False 2=True (4.9s)
Sep 10 19:05:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:33,895 main INFO screen LOST pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 10 19:05:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:34,032 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:05:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:34,194 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:05:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:34,373 main INFO screen LEGACY pass=0 dev=0.0 ins=46.83 pro=10 1a=False 1b=False 2=True (0.4s)
Sep 10 19:05:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:44,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:05:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:44,630 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:05:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:44,948 main INFO screen MEME pass=0 dev=0.0 ins=28.67 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 19:05:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:56,833 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:05:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:57,028 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:05:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:05:57,284 main INFO screen MEME pass=0 dev=0.0 ins=20.87 pro=23 1a=False 1b=False 2=True (0.5s)
Sep 10 19:06:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:01,252 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:06:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:01,389 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:06:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:07,299 main INFO screen KIRK pass=0 dev=0.0 ins=16.13 pro=19 1a=False 1b=False 2=True (6.1s)
Sep 10 19:06:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:08,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:06:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:08,216 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:06:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:08,548 main INFO screen MEME pass=0 dev=0.0 ins=25.73 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 10 19:06:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:18,614 main INFO screen btcn pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 10 19:06:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:20,215 main INFO screen NPT pass=0 dev=2.49 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 10 19:06:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:26,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 19:06:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:26,681 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 19:06:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 19:06:28,148 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:19:06:28 +0000] "GET /health HTTP/1.1" 200 427 "-" "Python-urllib/3.14"
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
