# Schaduwbot status

- tijd: 2026-09-10 16:06:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 hours, 19 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 564/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 8303, "tokens_in_memory": 1327, "msgs": 1247573, "trades": 267448, "creates": 3207, "decode_fail": 29045, "rpc_calls": 4478, "rpc_errors": 526, "sol_usd": 99.55371631825042, "open_positions": 65}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 15:48 UTC

Gelogde schaduwtrades: **1955**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 2829 | 392 | 9 | 392 | 51 | 673 | 1955 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 36 | 6% | 2.8% | +35.4% | -18.8% | -15.77% | 70% |
| dip35_V1_gescreend_fail | 185 | 28% | 5.9% | +47.5% | -29.0% | -7.87% | 99% |
| dip35_V1_alle | 232 | 25% | 5.6% | +46.4% | -27.6% | -9.45% | 100% |
| dip35_V2_gescreend_pass | 35 | 6% | 2.9% | +1.1% | -22.5% | -21.18% | 78% |
| dip35_V2_gescreend_fail | 176 | 25% | 6.2% | +42.0% | -31.3% | -12.96% | 100% |
| dip35_V2_alle | 221 | 22% | 5.9% | +39.0% | -30.2% | -14.83% | 100% |
| dip35_V3_gescreend_pass | 36 | 6% | 2.8% | +1.3% | -24.0% | -22.61% | 82% |
| dip35_V3_gescreend_fail | 188 | 14% | 8.0% | +110.5% | -31.5% | -11.15% | 100% |
| dip35_V3_alle | 232 | 13% | 7.3% | +96.9% | -30.9% | -13.78% | 100% |
| dip40_V1_gescreend_pass | 34 | 15% | 2.9% | +48.0% | -17.9% | -8.19% | 55% |
| dip40_V1_gescreend_fail | 181 | 25% | 6.6% | +55.8% | -28.2% | -6.86% | 98% |
| dip40_V1_alle | 224 | 24% | 6.2% | +54.6% | -27.0% | -7.31% | 99% |
| dip40_V2_gescreend_pass | 33 | 9% | 3.0% | +64.8% | -21.3% | -13.50% | 66% |
| dip40_V2_gescreend_fail | 172 | 24% | 7.0% | +46.4% | -30.9% | -12.45% | 99% |
| dip40_V2_alle | 213 | 22% | 6.6% | +46.7% | -29.6% | -13.10% | 100% |
| dip40_V3_gescreend_pass | 34 | 6% | 2.9% | +2.3% | -22.4% | -20.97% | 77% |
| dip40_V3_gescreend_fail | 184 | 16% | 8.7% | +103.7% | -31.7% | -10.39% | 100% |
| dip40_V3_alle | 224 | 14% | 8.0% | +94.5% | -30.6% | -12.77% | 100% |
| dip45_V1_gescreend_pass | 29 | 21% | 3.4% | +44.7% | -17.3% | -4.51% | 48% |
| dip45_V1_gescreend_fail | 170 | 26% | 5.9% | +55.2% | -28.5% | -6.32% | 98% |
| dip45_V1_alle | 208 | 26% | 5.8% | +53.6% | -27.4% | -6.36% | 98% |
| dip45_V2_gescreend_pass | 28 | 18% | 3.6% | +42.5% | -18.7% | -7.79% | 51% |
| dip45_V2_gescreend_fail | 160 | 26% | 6.9% | +47.9% | -30.4% | -10.35% | 99% |
| dip45_V2_alle | 196 | 24% | 6.6% | +46.4% | -29.1% | -10.60% | 99% |
| dip45_V3_gescreend_pass | 29 | 10% | 3.4% | +142.5% | -20.0% | -3.15% | 54% |
| dip45_V3_gescreend_fail | 170 | 17% | 8.2% | +115.4% | -31.2% | -6.21% | 100% |
| dip45_V3_alle | 205 | 16% | 7.8% | +114.7% | -30.0% | -6.74% | 100% |

## Beste variant: dip45_V3_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 15:55:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:42,812 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:55:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:42,997 main INFO screen SOL GRND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:55:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:46,171 main INFO screen PWP pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 15:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:52,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:52,521 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:55:52,658 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:56:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:00,582 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:56:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:00,674 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:56:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:00,831 main INFO screen RANDOM pass=1 dev=0.0 ins=12.55 pro=23 1a=False 1b=False 2=False (0.4s)
Sep 10 15:56:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:15,572 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:56:15 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 15:56:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:17,570 main INFO screen CIA pass=1 dev=0.0 ins=18.82 pro=23 1a=False 1b=False 2=False (4.0s)
Sep 10 15:56:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:56:35,326 main INFO screen LMAO pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 15:57:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:11,073 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:57:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:11,171 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:57:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:11,365 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:57:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:12,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:57:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:12,334 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:57:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:57:12,444 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:58:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:10,817 main INFO screen max pass=0 dev=0.0 ins=11.09 pro=37 1a=False 1b=False 2=True (4.1s)
Sep 10 15:58:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:13,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:14,272 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:14,506 main INFO screen AirTag pass=0 dev=0.0 ins=46.35 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 10 15:58:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:19,502 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 10 15:58:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:19,761 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.0s)
Sep 10 15:58:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:51,890 main INFO screen Democratism pass=1 dev=0.0 ins=5.99 pro=42 1a=False 1b=False 2=False (3.8s)
Sep 10 15:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:57,221 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:57,378 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:58:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:57,681 main INFO screen stocktard pass=0 dev=0.0 ins=20.3 pro=17 1a=False 1b=False 2=True (0.5s)
Sep 10 15:58:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:58,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:58:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:58,244 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:58:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:58:58,402 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:59:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:05,300 main INFO screen GAYMAN pass=1 dev=0.0 ins=9.88 pro=54 1a=False 1b=False 2=False (2.7s)
Sep 10 15:59:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:10,310 main INFO screen AirTag pass=0 dev=0.0 ins=24.34 pro=21 1a=False 1b=False 2=False (1.7s)
Sep 10 15:59:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:19,724 main INFO screen Vortex pass=1 dev=0.0 ins=11.88 pro=40 1a=False 1b=False 2=False (3.2s)
Sep 10 15:59:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:56,927 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:59:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:57,554 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:59:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:58,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:59:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:58,371 main INFO screen MOON pass=0 dev=0.0 ins=16.93 pro=9 1a=False 1b=False 2=True (2.2s)
Sep 10 15:59:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:58,933 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:59:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:59:59,679 main INFO screen stocktard pass=0 dev=0.0 ins=31.04 pro=6 1a=False 1b=False 2=True (2.1s)
Sep 10 16:00:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:00,549 main INFO screen wifmotion pass=1 dev=0.0 ins=11.38 pro=19 1a=False 1b=False 2=False (4.7s)
Sep 10 16:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:01,731 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:00:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:01,952 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:00:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:09,086 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.4s)
Sep 10 16:00:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:22,556 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:00:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:22,640 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:00:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:23,092 main INFO screen BOG pass=0 dev=0.0 ins=24.18 pro=18 1a=False 1b=False 2=True (0.6s)
Sep 10 16:00:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:25,235 main INFO screen $PCAT pass=0 dev=0.55 ins=0.0 pro=6 1a=False 1b=False 2=False (7.1s)
Sep 10 16:00:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:30,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:00:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:30,938 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:00:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:35,895 main INFO screen Rising pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.1s)
Sep 10 16:00:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:36,476 main INFO screen cap pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (12.0s)
Sep 10 16:00:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:00:37,485 main INFO screen Athena pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (12.7s)
Sep 10 16:01:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:01:08,788 main INFO screen fukkksc pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 10 16:01:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:01:28,435 main INFO screen stocktard pass=1 dev=0.0 ins=0.73 pro=62 1a=False 1b=False 2=False (8.6s)
Sep 10 16:01:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:01:37,202 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:01:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 16:02:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:02:45,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:02:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:02:45,251 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:02:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:02:50,197 main INFO screen CT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 10 16:02:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:02:59,377 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.3s)
Sep 10 16:03:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:03:07,275 main INFO screen Meow pass=1 dev=0.0 ins=18.59 pro=26 1a=False 1b=False 2=False (6.7s)
Sep 10 16:03:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:03:41,050 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:03:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:03:41,138 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:03:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:03:46,614 main INFO screen JUGGERNAUT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 10 16:03:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:03:51,200 main INFO screen LaMisery pass=0 dev=1.92 ins=0.0 pro=7 1a=False 1b=False 2=False (10.0s)
Sep 10 16:04:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:00,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:04:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:00,344 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:04:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:05,454 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.3s)
Sep 10 16:04:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:25,856 main INFO screen DEX pass=0 dev=0.16 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 10 16:04:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:53,648 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:04:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:53,687 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:04:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:04:59,436 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 10 16:05:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:05:15,837 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:05:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:05:15,928 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:05:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:05:20,272 main INFO screen DT pass=0 dev=0.0 ins=77.54 pro=9 1a=False 1b=False 2=True (4.5s)
Sep 10 16:05:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:05:26,876 main INFO screen GPTBOT pass=0 dev=0.0 ins=25.13 pro=22 1a=False 1b=False 2=True (8.0s)
Sep 10 16:06:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:06:01,506 main INFO screen DERP pass=0 dev=0.8 ins=0.0 pro=1 1a=False 1b=False 2=False (6.1s)
Sep 10 16:06:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:06:33,860 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:06:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:06:39,277 main INFO screen $AURA pass=0 dev=3.51 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 10 16:06:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:06:40,687 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:06:40 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
