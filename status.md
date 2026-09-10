# Schaduwbot status

- tijd: 2026-09-10 18:45:04 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 hours, 58 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 599/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 17807, "tokens_in_memory": 1457, "msgs": 3314403, "trades": 601433, "creates": 7068, "decode_fail": 46282, "rpc_calls": 10194, "rpc_errors": 1061, "sol_usd": 99.49007374413043, "open_positions": 56}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 17:48 UTC

Gelogde schaduwtrades: **4206**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 5678 | 778 | 16 | 778 | 98 | 1424 | 4206 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 77 | 12% | 1.3% | +32.1% | -15.5% | -9.92% | 81% |
| dip35_V1_gescreend_fail | 393 | 25% | 5.1% | +47.4% | -27.1% | -8.15% | 100% |
| dip35_V1_alle | 491 | 24% | 4.7% | +45.0% | -25.7% | -9.02% | 100% |
| dip35_V2_gescreend_pass | 76 | 16% | 1.3% | +22.9% | -19.8% | -13.04% | 88% |
| dip35_V2_gescreend_fail | 395 | 22% | 5.6% | +64.9% | -28.9% | -8.23% | 100% |
| dip35_V2_alle | 487 | 21% | 5.1% | +58.1% | -28.0% | -9.79% | 100% |
| dip35_V3_gescreend_pass | 76 | 7% | 1.3% | +75.2% | -22.2% | -15.78% | 92% |
| dip35_V3_gescreend_fail | 399 | 11% | 7.0% | +120.5% | -30.5% | -13.88% | 100% |
| dip35_V3_alle | 489 | 11% | 6.3% | +109.6% | -29.7% | -14.91% | 100% |
| dip40_V1_gescreend_pass | 73 | 16% | 1.4% | +43.7% | -14.9% | -5.30% | 67% |
| dip40_V1_gescreend_fail | 382 | 23% | 6.0% | +54.0% | -27.6% | -9.01% | 100% |
| dip40_V1_alle | 472 | 22% | 5.3% | +51.5% | -26.0% | -8.75% | 100% |
| dip40_V2_gescreend_pass | 72 | 17% | 1.4% | +54.4% | -19.3% | -7.03% | 73% |
| dip40_V2_gescreend_fail | 383 | 21% | 6.0% | +70.4% | -29.5% | -8.10% | 100% |
| dip40_V2_alle | 467 | 21% | 5.4% | +66.8% | -28.3% | -8.51% | 100% |
| dip40_V3_gescreend_pass | 72 | 10% | 1.4% | +57.1% | -21.0% | -13.37% | 88% |
| dip40_V3_gescreend_fail | 387 | 12% | 7.8% | +112.2% | -31.5% | -14.39% | 100% |
| dip40_V3_alle | 469 | 12% | 6.8% | +101.4% | -30.2% | -14.77% | 100% |
| dip45_V1_gescreend_pass | 65 | 18% | 1.5% | +44.4% | -14.4% | -3.53% | 63% |
| dip45_V1_gescreend_fail | 368 | 23% | 6.0% | +56.2% | -27.3% | -8.28% | 100% |
| dip45_V1_alle | 447 | 22% | 5.4% | +53.9% | -25.8% | -7.98% | 100% |
| dip45_V2_gescreend_pass | 63 | 24% | 1.6% | +42.8% | -17.6% | -3.21% | 60% |
| dip45_V2_gescreend_fail | 367 | 22% | 6.3% | +73.3% | -29.2% | -7.10% | 100% |
| dip45_V2_alle | 440 | 22% | 5.7% | +67.5% | -27.9% | -7.09% | 100% |
| dip45_V3_gescreend_pass | 64 | 9% | 1.6% | +108.1% | -19.2% | -7.29% | 80% |
| dip45_V3_gescreend_fail | 372 | 14% | 7.5% | +153.4% | -30.7% | -5.00% | 100% |
| dip45_V3_alle | 444 | 13% | 6.8% | +146.4% | -29.4% | -6.02% | 100% |

## Beste variant: dip45_V2_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 18:33:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:33:21,773 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:33:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:33:21,833 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:33:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:33:22,004 main INFO screen NICHE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:33:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:33:58,910 main INFO screen 34% pass=0 dev=9.55 ins=0.0 pro=2 1a=False 1b=False 2=True (2.6s)
Sep 10 18:34:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:00,916 main INFO screen PFE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 10 18:34:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:04,454 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.3s)
Sep 10 18:34:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:05,230 main INFO screen gambler pass=0 dev=0.0 ins=23.04 pro=62 1a=False 1b=False 2=True (5.2s)
Sep 10 18:34:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:14,212 main INFO screen SHLAPA pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 18:34:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:18,765 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 18:34:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:22,031 main INFO screen LOX pass=0 dev=21.57 ins=1.65 pro=9 1a=False 1b=True 2=False (2.2s)
Sep 10 18:34:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:36,096 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:18:34:36 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 18:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:39,602 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:39,697 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:34:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:39,899 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 18:34:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:46,548 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:34:46 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
Sep 10 18:34:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:34:58,811 main INFO screen $CAT pass=0 dev=0.77 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 18:35:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:35:29,415 main INFO screen ANBU pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 10 18:35:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:35:44,537 main INFO screen Pump cat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 10 18:35:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:35:57,414 main INFO screen SKD pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (14.0s)
Sep 10 18:36:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:05,691 main INFO screen SAVPIR pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 10 18:36:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:08,847 main INFO screen REALPEPE pass=1 dev=0.38 ins=0.0 pro=33 1a=False 1b=False 2=False (3.2s)
Sep 10 18:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:42,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:42,454 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:36:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:42,706 main INFO screen PUDGYSOCK pass=0 dev=35.26 ins=0.17 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 10 18:36:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:43,445 main INFO screen Slopper pass=0 dev=0.0 ins=19.76 pro=41 1a=False 1b=False 2=True (1.2s)
Sep 10 18:36:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:36:56,351 main INFO screen att pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 18:37:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:37:30,407 main INFO screen JAILTOP pass=0 dev=9.66 ins=0.0 pro=25 1a=False 1b=True 2=False (1.9s)
Sep 10 18:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:37:45,094 main INFO screen $SEX pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 10 18:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:37:45,791 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:37:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:37:45,919 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:37:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:37:46,205 main INFO screen KEYCAT pass=0 dev=0.0 ins=22.34 pro=9 1a=False 1b=False 2=True (0.5s)
Sep 10 18:38:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:38:27,434 main INFO screen HEDGE pass=0 dev=1.57 ins=9.24 pro=59 1a=False 1b=False 2=True (2.8s)
Sep 10 18:39:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:06,980 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:39:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:07,079 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:39:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:07,713 main INFO screen ZENCAT pass=0 dev=0.0 ins=22.51 pro=19 1a=False 1b=False 2=True (0.8s)
Sep 10 18:39:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:10,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:39:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:10,199 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:39:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:11,153 main INFO screen Ballhallah pass=0 dev=0.0 ins=40.87 pro=5 1a=False 1b=False 2=True (1.1s)
Sep 10 18:39:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:39:15,293 main INFO screen femlet pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 18:40:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:40:04,411 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:18:40:04 +0000] "GET /health HTTP/1.1" 200 426 "-" "Python-urllib/3.14"
Sep 10 18:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:40:17,579 main INFO screen femlet pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.9s)
Sep 10 18:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:40:26,459 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:40:26,728 main INFO screen MAMA pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 18:40:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:40:43,098 main INFO screen wind pass=0 dev=3.18 ins=0.0 pro=4 1a=False 1b=False 2=False (2.5s)
Sep 10 18:41:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:41:12,491 main INFO screen Gamblur pass=0 dev=0.0 ins=19.72 pro=62 1a=False 1b=False 2=True (2.7s)
Sep 10 18:41:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:41:54,653 main INFO screen vrl pass=0 dev=7.82 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 10 18:42:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:00,352 main INFO screen TWIST pass=1 dev=3.42 ins=0.0 pro=30 1a=False 1b=False 2=False (3.5s)
Sep 10 18:42:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:05,004 main INFO screen HIM pass=0 dev=3.43 ins=31.02 pro=62 1a=False 1b=False 2=True (2.7s)
Sep 10 18:42:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:07,778 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:42:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:07,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:08,312 main INFO screen BATON pass=0 dev=0.0 ins=6.72 pro=18 1a=False 1b=False 2=True (0.6s)
Sep 10 18:42:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:11,860 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:42:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:12,030 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:12,311 main INFO screen BATON pass=0 dev=0.0 ins=13.53 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 18:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:16,645 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 18:42:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:25,273 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:42:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:25,392 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:25,535 main INFO screen gaywif pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 18:42:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:27,865 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:42:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:27,966 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:28,232 main INFO screen ZENCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 18:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:41,731 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 18:42:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:42,147 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 18:42:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:43,245 main INFO screen Stonkfly pass=0 dev=0.0 ins=14.98 pro=9 1a=False 1b=False 2=True (1.9s)
Sep 10 18:42:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:43,372 main INFO screen $BREAD pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 10 18:42:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:50,476 main INFO screen sol pass=0 dev=3.39 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 10 18:42:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:52,464 main INFO screen DERP pass=0 dev=9.55 ins=0.0 pro=3 1a=False 1b=False 2=True (2.4s)
Sep 10 18:42:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 18:42:52,942 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
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
