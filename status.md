# Schaduwbot status

- tijd: 2026-09-10 16:44:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 hours, 57 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 580/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 10561, "tokens_in_memory": 1486, "msgs": 1891522, "trades": 350256, "creates": 4215, "decode_fail": 35168, "rpc_calls": 5705, "rpc_errors": 678, "sol_usd": 99.21724628053286, "open_positions": 85}
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
Sep 10 16:35:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:23,118 main INFO screen CRATESOL pass=1 dev=3.42 ins=0.0 pro=35 1a=False 1b=False 2=False (3.3s)
Sep 10 16:35:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:29,919 main INFO screen RICK pass=0 dev=6.56 ins=0.0 pro=3 1a=False 1b=False 2=True (2.1s)
Sep 10 16:35:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:44,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:35:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:44,911 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:35:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:45,091 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 16:35:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:35:52,068 main INFO screen KOMODOE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 10 16:36:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:23,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:36:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:23,294 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:36:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:23,502 main INFO screen Kirkiversary pass=0 dev=0.0 ins=22.81 pro=29 1a=False 1b=False 2=True (0.4s)
Sep 10 16:36:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:36,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:36:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:37,100 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:36:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:37,380 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (1.1s)
Sep 10 16:36:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:41,851 main INFO screen AK pass=0 dev=0.0 ins=12.49 pro=37 1a=False 1b=False 2=True (8.4s)
Sep 10 16:36:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:58,446 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:36:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:58,544 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:36:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:36:58,722 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 10 16:37:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:21,712 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:37:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:21,812 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:37:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:22,017 main INFO screen NIKE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 16:37:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:32,515 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:37:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:32,643 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:37:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:37:33,003 main INFO screen PLTR pass=0 dev=0.0 ins=17.85 pro=20 1a=False 1b=False 2=True (0.6s)
Sep 10 16:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:04,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:38:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:04,895 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:38:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:05,802 main INFO screen PLTR pass=0 dev=0.0 ins=17.85 pro=8 1a=False 1b=False 2=True (1.1s)
Sep 10 16:38:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:16,458 main INFO screen Kirkaversery pass=1 dev=0.0 ins=9.22 pro=19 1a=False 1b=False 2=False (3.4s)
Sep 10 16:38:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:50,863 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:38:50 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 16:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:53,308 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:53,408 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:38:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:38:53,873 main INFO screen Kirkaversary pass=0 dev=0.0 ins=31.25 pro=10 1a=False 1b=False 2=True (0.7s)
Sep 10 16:39:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:30,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:31,069 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:39:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:31,262 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 16:39:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:45,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:39:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:45,281 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:39:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:45,602 main INFO screen PLTR pass=0 dev=0.0 ins=17.45 pro=20 1a=False 1b=False 2=True (0.5s)
Sep 10 16:39:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:46,685 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:39:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:46,811 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:39:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:39:46,953 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:17,017 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:17,120 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:40:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:17,308 main INFO screen MICHIBATON pass=0 dev=0.0 ins=77.54 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 16:40:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:31,547 main INFO screen FRANSEMTOP pass=0 dev=0.54 ins=0.0 pro=1 1a=False 1b=False 2=True (2.1s)
Sep 10 16:40:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:36,002 main INFO screen HIGHAI pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 10 16:40:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:40:52,436 main INFO screen SOLCITY pass=1 dev=0.0 ins=1.58 pro=55 1a=False 1b=False 2=False (3.5s)
Sep 10 16:41:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:06,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:41:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:06,718 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:41:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:06,856 main INFO screen POKEMON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 16:41:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:10,239 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:41:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:10,377 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:41:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:10,505 main INFO screen Come Back pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 16:41:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:12,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:41:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:12,205 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:41:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:12,422 main INFO screen HORO pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 10 16:41:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:18,562 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:41:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:18,761 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:41:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:18,867 main INFO screen HUTAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:41:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:41:40,088 main INFO screen magnet pass=0 dev=0.71 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 10 16:42:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:03,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:42:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:03,502 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:42:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:03,690 main INFO screen MIDAS pass=0 dev=0.0 ins=5.95 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 10 16:42:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:25,553 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:42:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:25,631 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:42:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:27,504 main INFO screen pup pass=0 dev=11.71 ins=0.13 pro=24 1a=False 1b=False 2=False (1.2s)
Sep 10 16:42:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:31,676 main INFO screen FREEDOM pass=0 dev=0.0 ins=9.88 pro=21 1a=False 1b=False 2=True (6.3s)
Sep 10 16:42:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:57,112 main INFO screen HOBO pass=0 dev=0.7 ins=0.0 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 10 16:42:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:58,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:42:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:58,119 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:42:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:42:58,280 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:43:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:06,694 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:43:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:06,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:43:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:06,961 main INFO screen Come Back pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 16:43:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:24,896 main INFO screen Kirkaversery pass=1 dev=0.0 ins=9.16 pro=39 1a=False 1b=False 2=False (3.3s)
Sep 10 16:43:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:34,234 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:43:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:34,307 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:43:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:34,522 main INFO screen PENPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 16:43:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:46,411 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:43:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:46,522 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:43:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:43:46,701 main INFO screen KURK pass=0 dev=0.0 ins=9.45 pro=14 1a=False 1b=False 2=True (0.4s)
Sep 10 16:44:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:44:17,884 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:44:17 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
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
