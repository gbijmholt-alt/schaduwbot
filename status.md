# Schaduwbot status

- tijd: 2026-09-10 15:13:13 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 hour, 26 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 545/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 5096, "tokens_in_memory": 1488, "msgs": 794099, "trades": 158391, "creates": 2058, "decode_fail": 16198, "rpc_calls": 2668, "rpc_errors": 329, "sol_usd": 100.02672360389046, "open_positions": 76}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 14:48 UTC

Gelogde schaduwtrades: **891**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 1428 | 184 | 5 | 184 | 29 | 324 | 891 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 22 | 4% | 4.5% | +32.3% | -18.4% | -16.07% | 54% |
| dip35_V1_gescreend_fail | 82 | 24% | 7.3% | +41.1% | -32.9% | -14.85% | 95% |
| dip35_V1_alle | 106 | 22% | 6.6% | +39.9% | -29.2% | -14.22% | 97% |
| dip35_V2_gescreend_pass | 20 | 0% | 5.0% | +0.0% | -20.4% | -20.38% | 57% |
| dip35_V2_gescreend_fail | 75 | 24% | 8.0% | +49.9% | -37.1% | -16.25% | 95% |
| dip35_V2_alle | 97 | 20% | 7.2% | +47.8% | -32.5% | -16.75% | 98% |
| dip35_V3_gescreend_pass | 22 | 4% | 4.5% | +0.8% | -21.4% | -20.39% | 60% |
| dip35_V3_gescreend_fail | 85 | 13% | 10.6% | +18.2% | -36.5% | -29.42% | 100% |
| dip35_V3_alle | 108 | 12% | 9.3% | +16.3% | -33.2% | -27.21% | 100% |
| dip40_V1_gescreend_pass | 21 | 14% | 4.8% | +66.9% | -17.8% | -5.65% | 37% |
| dip40_V1_gescreend_fail | 80 | 22% | 8.7% | +43.5% | -31.5% | -14.66% | 93% |
| dip40_V1_alle | 103 | 22% | 7.8% | +45.5% | -28.4% | -11.92% | 94% |
| dip40_V2_gescreend_pass | 19 | 5% | 5.3% | +193.1% | -18.5% | -7.37% | 37% |
| dip40_V2_gescreend_fail | 72 | 21% | 9.7% | +48.3% | -36.3% | -18.69% | 96% |
| dip40_V2_alle | 93 | 18% | 8.6% | +54.6% | -31.7% | -15.96% | 97% |
| dip40_V3_gescreend_pass | 21 | 10% | 4.8% | +2.3% | -20.1% | -17.95% | 54% |
| dip40_V3_gescreend_fail | 84 | 16% | 10.7% | +17.3% | -36.1% | -27.82% | 99% |
| dip40_V3_alle | 106 | 15% | 9.4% | +15.0% | -32.7% | -25.50% | 100% |
| dip45_V1_gescreend_pass | 18 | 28% | 5.6% | +53.5% | -18.8% | +1.25% | 29% |
| dip45_V1_gescreend_fail | 75 | 23% | 6.7% | +39.1% | -31.0% | -15.11% | 93% |
| dip45_V1_alle | 95 | 25% | 6.3% | +41.5% | -28.8% | -11.01% | 92% |
| dip45_V2_gescreend_pass | 16 | 19% | 6.2% | +70.3% | -20.1% | -3.17% | 31% |
| dip45_V2_gescreend_fail | 68 | 24% | 8.8% | +46.8% | -34.4% | -15.29% | 92% |
| dip45_V2_alle | 86 | 23% | 8.1% | +48.5% | -31.2% | -12.67% | 93% |
| dip45_V3_gescreend_pass | 18 | 17% | 5.6% | +142.5% | -20.8% | +6.43% | 37% |
| dip45_V3_gescreend_fail | 78 | 19% | 9.0% | +42.3% | -34.3% | -19.60% | 97% |
| dip45_V3_alle | 97 | 20% | 8.2% | +56.4% | -31.7% | -14.46% | 97% |

## Beste variant: dip45_V1_alle

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 15:03:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:03:59,766 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:04:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:03,456 main INFO screen POLITICO pass=0 dev=0.0 ins=39.09 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 10 15:04:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:03,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:04:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:03,752 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:04:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:10,330 main INFO screen CATESEM pass=0 dev=0.0 ins=31.55 pro=5 1a=False 1b=False 2=True (6.8s)
Sep 10 15:04:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:17,630 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 10 15:04:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:18,768 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 10 15:04:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:41,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:04:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:41,784 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:04:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:04:42,001 main INFO screen Hoodtard pass=0 dev=0.0 ins=1.65 pro=21 1a=False 1b=False 2=True (0.4s)
Sep 10 15:05:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:02,406 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:05:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:02,460 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:05:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:07,411 main INFO screen CATESEM pass=0 dev=0.0 ins=32.02 pro=4 1a=False 1b=False 2=True (5.1s)
Sep 10 15:05:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:15,739 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.6s)
Sep 10 15:05:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:32,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:05:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:32,866 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:05:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:37,785 main INFO screen STENKS pass=0 dev=2.1 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 10 15:05:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:05:37,962 main INFO screen POLITICO pass=0 dev=0.0 ins=39.4 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 10 15:06:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:03,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:06:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:04,009 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:06:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:10,268 main INFO screen BATONGUY pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (6.5s)
Sep 10 15:06:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:25,538 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (7.1s)
Sep 10 15:06:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:31,196 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:06:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:31,452 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:06:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:35,927 main INFO screen lnw pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.0s)
Sep 10 15:06:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:36,785 main INFO screen YEET pass=1 dev=0.0 ins=19.58 pro=25 1a=False 1b=False 2=False (6.9s)
Sep 10 15:06:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:39,638 main INFO screen carwoode pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (5.4s)
Sep 10 15:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:53,587 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:06:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:06:53,692 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:07:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:00,883 main INFO screen GAY pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (7.4s)
Sep 10 15:07:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:21,948 main INFO screen Chud pass=0 dev=0.67 ins=0.0 pro=1 1a=False 1b=False 2=False (8.4s)
Sep 10 15:07:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:25,073 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:07:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:25,947 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:27,004 main INFO screen BFF pass=0 dev=0.0 ins=8.29 pro=19 1a=False 1b=False 2=True (2.8s)
Sep 10 15:07:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:32,775 main INFO screen STENKS pass=0 dev=1.31 ins=0.0 pro=1 1a=False 1b=False 2=False (10.7s)
Sep 10 15:07:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:07:33,818 main INFO screen MARIO pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (11.9s)
Sep 10 15:08:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:00,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:08:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:00,658 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:08:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:02,096 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:08:02 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 15:08:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:05,711 main INFO screen GROKCAT pass=0 dev=0.0 ins=1.54 pro=2 1a=False 1b=False 2=True (5.3s)
Sep 10 15:08:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:18,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:08:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:18,334 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:08:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:18,746 main INFO screen Josh pass=0 dev=0.0 ins=8.67 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 10 15:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:37,425 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:37,531 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:08:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:41,764 main INFO screen WC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 10 15:08:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:57,627 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:08:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:08:57,716 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:09:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:09:01,141 main INFO screen CATESEM pass=0 dev=0.0 ins=31.98 pro=3 1a=False 1b=False 2=True (3.6s)
Sep 10 15:09:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:09:49,915 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 10 15:11:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:10,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:11:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:10,882 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:11:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:16,618 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 10 15:11:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:17,437 main INFO screen PIMP pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 10 15:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:37,353 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:11:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:37,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:11:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:40,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:11:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:40,558 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:11:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:41,790 main INFO screen $MM pass=0 dev=0.0 ins=3.19 pro=7 1a=False 1b=False 2=False (8.2s)
Sep 10 15:11:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:42,475 main INFO screen LONG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 10 15:11:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:43,419 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:11:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:43,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:11:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:44,332 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:11:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:44,467 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:11:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:44,498 main INFO screen Mar1o pass=0 dev=0.0 ins=15.68 pro=9 1a=False 1b=False 2=False (4.1s)
Sep 10 15:11:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:49,241 main INFO screen MAGACOIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 10 15:11:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:11:49,738 main INFO screen TESTICLE pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 10 15:12:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:15,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:12:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:15,609 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:12:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:16,124 main INFO screen nirvana pass=0 dev=0.0 ins=17.9 pro=4 1a=False 1b=False 2=True (0.7s)
Sep 10 15:12:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:18,985 main INFO screen suckh pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 10 15:12:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:32,219 main INFO screen Chud pass=0 dev=0.45 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 10 15:12:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:35,313 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:12:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:35,428 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:12:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:37,106 main INFO screen carwoode pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 10 15:12:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:12:40,784 main INFO screen CATESEM pass=0 dev=0.0 ins=31.98 pro=4 1a=False 1b=False 2=True (5.5s)
Sep 10 15:13:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:13:08,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:13:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:13:08,741 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:13:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:13:12,252 main INFO screen CRISPE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 10 15:13:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:13:13,578 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:13:13 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
