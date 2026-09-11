# Schaduwbot status

- tijd: 2026-09-11 15:10:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 1 hour, 23 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 738/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 19252, "tokens_in_memory": 5523, "msgs": 1963900, "trades": 471283, "creates": 5523, "decode_fail": 38468, "rpc_calls": 8358, "rpc_errors": 786, "sol_usd": 103.05855874194611, "open_positions": 65, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 14:49 UTC

Gelogde schaduwtrades: **24489**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 15864 | 2207 | 24 | 2207 | 145 | 4118 | 12134 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 273 | 15% | 1.5% | +41.0% | -15.9% | -7.53% | 99% |
| dip35_V1_gescreend_fail | 2474 | 26% | 3.8% | +45.6% | -26.0% | -7.17% | 100% |
| dip35_V1_alle | 2832 | 26% | 3.9% | +44.6% | -25.3% | -7.50% | 100% |
| dip35_V2_gescreend_pass | 272 | 18% | 2.2% | +39.7% | -21.0% | -10.30% | 100% |
| dip35_V2_gescreend_fail | 2476 | 25% | 4.5% | +56.2% | -28.4% | -7.66% | 100% |
| dip35_V2_alle | 2810 | 24% | 4.6% | +54.4% | -28.0% | -8.35% | 100% |
| dip35_V3_gescreend_pass | 274 | 7% | 2.2% | +133.5% | -22.4% | -11.58% | 100% |
| dip35_V3_gescreend_fail | 2512 | 13% | 6.2% | +110.4% | -30.0% | -11.43% | 100% |
| dip35_V3_alle | 2843 | 13% | 6.1% | +108.7% | -29.5% | -11.87% | 100% |
| dip40_V1_gescreend_pass | 253 | 13% | 1.6% | +42.9% | -15.3% | -7.52% | 99% |
| dip40_V1_gescreend_fail | 2406 | 26% | 3.8% | +47.8% | -25.9% | -6.67% | 100% |
| dip40_V1_alle | 2722 | 25% | 3.8% | +46.9% | -25.1% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 252 | 14% | 2.4% | +49.8% | -20.0% | -10.59% | 100% |
| dip40_V2_gescreend_fail | 2400 | 25% | 4.2% | +55.8% | -28.2% | -7.50% | 100% |
| dip40_V2_alle | 2697 | 24% | 4.3% | +55.1% | -27.6% | -8.20% | 100% |
| dip40_V3_gescreend_pass | 254 | 6% | 2.4% | +112.1% | -21.4% | -13.48% | 100% |
| dip40_V3_gescreend_fail | 2438 | 13% | 5.8% | +98.8% | -29.7% | -13.01% | 100% |
| dip40_V3_alle | 2733 | 12% | 5.7% | +97.8% | -29.1% | -13.44% | 100% |
| dip45_V1_gescreend_pass | 242 | 14% | 1.7% | +49.5% | -15.3% | -6.19% | 98% |
| dip45_V1_gescreend_fail | 2338 | 27% | 3.4% | +49.5% | -25.6% | -5.01% | 100% |
| dip45_V1_alle | 2626 | 26% | 3.4% | +49.2% | -24.8% | -5.38% | 100% |
| dip45_V2_gescreend_pass | 240 | 18% | 2.5% | +49.2% | -19.7% | -7.34% | 99% |
| dip45_V2_gescreend_fail | 2320 | 25% | 3.8% | +58.7% | -27.7% | -5.99% | 100% |
| dip45_V2_alle | 2596 | 24% | 3.9% | +57.7% | -27.1% | -6.49% | 100% |
| dip45_V3_gescreend_pass | 242 | 7% | 2.5% | +180.2% | -20.6% | -7.31% | 100% |
| dip45_V3_gescreend_fail | 2356 | 14% | 5.6% | +112.8% | -29.2% | -9.68% | 100% |
| dip45_V3_alle | 2630 | 13% | 5.5% | +114.4% | -28.6% | -9.82% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1861 | 12% | 2.6% | -10.03% | 100% |
| zonder_xlink | 441 | 13% | 0.0% | -5.41% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 14:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:27,885 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:27,992 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:59:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:28,235 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 14:59:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:32,958 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:59:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:33,083 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:59:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:33,202 main INFO screen Stick pass=0 dev=0.0 ins=22.01 pro=13 1a=False 1b=False 2=True (0.3s)
Sep 11 14:59:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:59:35,238 main INFO screen VENOM pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.9s)
Sep 11 15:00:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:22,349 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:00:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:22,437 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:00:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:22,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:00:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:22,964 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:00:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:23,685 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:00:23 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:00:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:26,796 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.6s)
Sep 11 15:00:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:28,242 main INFO screen SLOUVRE pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=True (5.5s)
Sep 11 15:00:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:50,873 main INFO screen VENOM pass=0 dev=0.13 ins=0.0 pro=4 1a=False 1b=False 2=False (8.9s)
Sep 11 15:00:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:58,514 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:00:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:00:58,657 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:01:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:02,526 main INFO screen LASTFLY pass=0 dev=0.0 ins=79.13 pro=7 1a=False 1b=False 2=True (4.1s)
Sep 11 15:01:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:29,966 main INFO screen SCRVAN pass=0 dev=0.77 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 15:01:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:37,771 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:01:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:38,261 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:01:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:38,872 main INFO screen POOP pass=1 dev=0.0 ins=14.96 pro=10 1a=False 1b=False 2=False (1.6s)
Sep 11 15:01:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:43,914 main INFO screen Iolani pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 15:01:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:46,448 main INFO screen WEN pass=0 dev=0.0 ins=6.16 pro=58 1a=False 1b=False 2=True (5.0s)
Sep 11 15:01:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:47,429 main INFO screen MPNUT pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 15:01:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:01:52,560 main INFO screen muuu pass=0 dev=0.12 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 11 15:02:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:02:48,079 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:02:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:02:48,210 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:02:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:02:52,091 main INFO screen Leafy pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 11 15:03:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:02,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:03:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:02,477 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:03:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:09,201 main INFO screen INT pass=0 dev=0.0 ins=27.9 pro=6 1a=False 1b=False 2=True (6.9s)
Sep 11 15:03:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:23,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:03:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:23,363 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:03:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:29,060 main INFO screen HEDG pass=0 dev=0.0 ins=49.73 pro=7 1a=False 1b=False 2=True (5.9s)
Sep 11 15:03:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:41,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:03:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:42,002 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:03:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:42,354 main INFO screen Morty pass=0 dev=0.0 ins=18.99 pro=12 1a=False 1b=False 2=True (0.5s)
Sep 11 15:03:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:03:46,541 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 15:04:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:04,186 aiohttp.access INFO 85.11.167.74 [11/Sep/2026:15:04:04 +0000] "GET /login HTTP/1.1" 404 174 "-" "Mozilla/5.0"
Sep 11 15:04:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:11,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:04:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:11,455 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:04:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:18,570 main INFO screen FRONG pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (7.3s)
Sep 11 15:04:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:18,592 main INFO screen REWARDS pass=0 dev=0.51 ins=24.17 pro=18 1a=False 1b=False 2=False (6.1s)
Sep 11 15:04:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:21,631 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:04:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:21,768 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:04:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:25,173 main INFO screen BEAR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.6s)
Sep 11 15:04:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:33,434 main INFO screen GRANDMA pass=0 dev=0.57 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 15:04:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:37,358 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:04:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:37,502 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:04:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:04:42,606 main INFO screen TWINTOWERS pass=1 dev=0.0 ins=0.28 pro=18 1a=False 1b=False 2=False (5.3s)
Sep 11 15:05:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:05:24,693 main INFO screen DERPER pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 11 15:05:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:05:26,092 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:05:26 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:06:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:06:28,623 main INFO screen NABU pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 15:06:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:06:28,695 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:06:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:06:28,825 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:06:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:06:35,858 main INFO screen TWINTOWERS pass=0 dev=0.0 ins=30.61 pro=7 1a=False 1b=False 2=True (7.2s)
Sep 11 15:07:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:32,680 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:07:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:32,770 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:07:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:36,985 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 11 15:07:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:47,155 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:15:07:47 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 15:07:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:58,735 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:07:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:07:58,830 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:08:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:08:03,981 main INFO screen TRUMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.3s)
Sep 11 15:08:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:08:39,176 main INFO screen AOCME pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.3s)
Sep 11 15:09:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:10,528 main INFO screen NABU pass=0 dev=0.09 ins=0.0 pro=4 1a=False 1b=False 2=False (9.0s)
Sep 11 15:09:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:37,407 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:09:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:37,501 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:09:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:37,680 main INFO screen Cimol pass=0 dev=0.0 ins=13.21 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 15:09:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:37,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:09:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:37,938 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:09:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:09:38,148 main INFO screen Cimol pass=0 dev=0.0 ins=38.87 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 15:10:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:08,814 main INFO screen POOP pass=1 dev=0.06 ins=3.21 pro=37 1a=False 1b=False 2=False (9.9s)
Sep 11 15:10:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:11,732 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 15:10:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:23,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:10:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:23,544 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:10:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:27,499 main INFO screen Joe pass=0 dev=0.0 ins=26.11 pro=5 1a=False 1b=False 2=True (4.2s)
Sep 11 15:10:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:29,761 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:15:10:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 15:10:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:30,119 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:15:10:30 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 15:10:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:10:37,105 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:10:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T13:42:29Z
--- update 2026-09-11T13:47:30Z
--- update 2026-09-11T13:52:36Z
--- update 2026-09-11T13:57:48Z
--- update 2026-09-11T14:02:52Z
Running as unit: schaduwbot-wallets.service; invocation ID: c147433096084aa9b38d9e2b7eb6bf75
analyses gestart (8213ec5e675e)
--- update 2026-09-11T14:08:04Z
--- update 2026-09-11T14:13:36Z
--- update 2026-09-11T14:18:46Z
--- update 2026-09-11T14:23:51Z
--- update 2026-09-11T14:29:07Z
--- update 2026-09-11T14:34:22Z
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
--- update 2026-09-11T14:49:38Z
--- update 2026-09-11T14:54:48Z
--- update 2026-09-11T15:00:22Z
--- update 2026-09-11T15:05:25Z
--- update 2026-09-11T15:10:36Z
```

## Analyses (laatste 25 regels)
```
inactive
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
14:02:53 5048 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
14:02:56   ingelezen tot rowid 1452718 (196794 rijen, 196794 bruikbaar)
14:02:56 ingelezen: 196794 nieuwe trades, 196794 bruikbaar (3s)
14:02:59 klaar in 6s -> /opt/schaduwbot/reports/ledger.md
14:03:01 klaar in 2s: 1642 tokens, 1877 nieuw -> /opt/schaduwbot/reports/video_replay.md
14:03:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 14:03 UTC
14:03:01 29885 tokens geladen
14:03:05   2000 tokens, 356777 trades, 100453 posities (4s)
14:03:09   4000 tokens, 700400 trades, 193583 posities (7s)
14:03:12   6000 tokens, 1047800 trades, 291369 posities (11s)
14:03:16   8000 tokens, 1402251 trades, 394081 posities (15s)
14:03:16 posities: 409300 uit 1453102 trades (15s)
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
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
