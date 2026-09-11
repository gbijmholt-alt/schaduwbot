# Schaduwbot status

- tijd: 2026-09-11 14:29:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 42 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 705/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 16764, "tokens_in_memory": 4649, "msgs": 1561419, "trades": 400995, "creates": 4649, "decode_fail": 32355, "rpc_calls": 7048, "rpc_errors": 674, "sol_usd": 103.75955935438573, "open_positions": 75, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 13:49 UTC

Gelogde schaduwtrades: **23540**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 14630 | 2033 | 23 | 2033 | 139 | 3820 | 11185 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 265 | 15% | 1.5% | +41.0% | -16.1% | -7.69% | 99% |
| dip35_V1_gescreend_fail | 2373 | 26% | 3.8% | +45.7% | -26.0% | -6.98% | 100% |
| dip35_V1_alle | 2723 | 26% | 3.9% | +44.7% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 264 | 17% | 1.9% | +39.3% | -20.9% | -10.39% | 100% |
| dip35_V2_gescreend_fail | 2373 | 25% | 4.4% | +56.1% | -28.5% | -7.59% | 100% |
| dip35_V2_alle | 2699 | 24% | 4.5% | +54.3% | -28.0% | -8.32% | 100% |
| dip35_V3_gescreend_pass | 266 | 7% | 2.3% | +136.1% | -22.6% | -11.87% | 100% |
| dip35_V3_gescreend_fail | 2416 | 13% | 6.2% | +113.0% | -30.0% | -10.92% | 100% |
| dip35_V3_alle | 2739 | 13% | 6.1% | +111.2% | -29.6% | -11.47% | 100% |
| dip40_V1_gescreend_pass | 245 | 14% | 1.6% | +43.0% | -15.6% | -7.69% | 99% |
| dip40_V1_gescreend_fail | 2308 | 26% | 3.7% | +47.9% | -26.0% | -6.42% | 100% |
| dip40_V1_alle | 2616 | 26% | 3.8% | +47.0% | -25.2% | -6.79% | 100% |
| dip40_V2_gescreend_pass | 244 | 13% | 2.0% | +49.8% | -19.9% | -10.78% | 100% |
| dip40_V2_gescreend_fail | 2302 | 25% | 4.1% | +55.6% | -28.2% | -7.34% | 100% |
| dip40_V2_alle | 2591 | 24% | 4.2% | +54.9% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 246 | 6% | 2.4% | +114.0% | -21.6% | -13.86% | 100% |
| dip40_V3_gescreend_fail | 2344 | 13% | 5.8% | +100.3% | -29.7% | -12.63% | 100% |
| dip40_V3_alle | 2631 | 12% | 5.7% | +99.2% | -29.1% | -13.14% | 100% |
| dip45_V1_gescreend_pass | 234 | 14% | 1.7% | +49.5% | -15.5% | -6.09% | 98% |
| dip45_V1_gescreend_fail | 2242 | 28% | 3.3% | +49.2% | -25.6% | -4.83% | 100% |
| dip45_V1_alle | 2522 | 27% | 3.4% | +48.8% | -24.8% | -5.23% | 100% |
| dip45_V2_gescreend_pass | 232 | 18% | 2.2% | +49.0% | -19.6% | -7.18% | 99% |
| dip45_V2_gescreend_fail | 2225 | 26% | 3.7% | +58.4% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2493 | 25% | 3.8% | +57.4% | -27.2% | -6.27% | 100% |
| dip45_V3_gescreend_pass | 234 | 6% | 2.6% | +186.5% | -20.8% | -7.50% | 100% |
| dip45_V3_gescreend_fail | 2260 | 14% | 5.6% | +107.1% | -29.3% | -10.26% | 100% |
| dip45_V3_alle | 2526 | 13% | 5.5% | +109.2% | -28.7% | -10.37% | 100% |

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
| met_xlink | 1819 | 12% | 2.5% | -10.15% | 100% |
| zonder_xlink | 411 | 13% | 0.0% | -5.49% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 14:17:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:28,837 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 14:17:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:17:29,974 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 14:18:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:01,837 main INFO screen VAULT pass=0 dev=0.0 ins=24.87 pro=75 1a=False 1b=True 2=True (7.8s)
Sep 11 14:18:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:47,393 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:18:47 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 14:18:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:56,969 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:18:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:18:57,104 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:19:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:04,026 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.9 pro=3 1a=False 1b=False 2=True (7.1s)
Sep 11 14:19:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:39,308 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:19:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:39,397 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:19:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:43,980 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.8s)
Sep 11 14:19:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:53,287 main INFO screen Bub pass=0 dev=7.58 ins=0.0 pro=35 1a=False 1b=False 2=False (7.2s)
Sep 11 14:19:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:19:55,990 main INFO screen stocklana pass=0 dev=0.46 ins=0.0 pro=1 1a=False 1b=False 2=False (10.7s)
Sep 11 14:20:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:14,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:20:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:14,201 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:20:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:19,165 main INFO screen FLYSEM pass=0 dev=0.0 ins=32.03 pro=4 1a=False 1b=False 2=True (5.2s)
Sep 11 14:20:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:48,460 main INFO screen Bananaut pass=0 dev=0.0 ins=21.56 pro=18 1a=False 1b=False 2=False (7.6s)
Sep 11 14:20:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:57,840 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:20:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:20:57,939 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:21:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:04,658 main INFO screen CHefQueef pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 11 14:21:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:17,703 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:21:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:17,749 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:21:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:18,124 main INFO screen blue pass=0 dev=0.0 ins=27.46 pro=19 1a=False 1b=False 2=True (0.5s)
Sep 11 14:21:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:25,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:21:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:25,591 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:21:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:29,840 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.5s)
Sep 11 14:21:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:37,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:21:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:38,129 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:21:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:38,473 main INFO screen blue pass=0 dev=0.0 ins=11.69 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 11 14:21:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:40,643 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:21:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:41,255 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:21:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:42,025 main INFO screen bleu pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=True (2.0s)
Sep 11 14:21:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:48,835 main INFO screen PUMPDOG pass=1 dev=0.0 ins=0.0 pro=46 1a=False 1b=False 2=False (9.3s)
Sep 11 14:21:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:21:49,989 main INFO screen beer pass=0 dev=0.81 ins=0.0 pro=3 1a=False 1b=False 2=False (9.3s)
Sep 11 14:22:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:33,132 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:22:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:33,234 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:22:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:38,128 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.3 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 11 14:22:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:43,629 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:22:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:43,753 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:22:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:22:48,845 main INFO screen emberdog pass=0 dev=0.0 ins=79.13 pro=9 1a=False 1b=False 2=True (5.3s)
Sep 11 14:23:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:03,702 main INFO screen shark pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 11 14:23:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:20,491 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:23:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:20,594 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:23:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:25,497 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 11 14:23:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:32,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:23:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:33,032 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:23:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:38,864 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.9 pro=3 1a=False 1b=False 2=True (6.0s)
Sep 11 14:23:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:52,262 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:23:52 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 14:23:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:23:59,514 main INFO screen BAG pass=0 dev=0.0 ins=15.12 pro=73 1a=False 1b=False 2=True (1.3s)
Sep 11 14:24:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:24:33,057 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:24:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:24:33,197 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:24:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:24:38,976 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 14:25:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:05,192 main INFO screen ARIMA pass=0 dev=2.08 ins=0.0 pro=3 1a=False 1b=False 2=False (8.7s)
Sep 11 14:25:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:38,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:25:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:38,948 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:25:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:43,304 main INFO screen Stocklana pass=0 dev=0.0 ins=16.12 pro=12 1a=False 1b=False 2=True (4.5s)
Sep 11 14:25:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:51,804 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:25:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:51,924 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:25:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:25:58,425 main INFO screen $OPC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 11 14:26:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:09,444 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:26:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:09,582 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:26:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:15,001 main INFO screen GOAF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.6s)
Sep 11 14:26:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:22,205 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:26:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:22,330 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:26:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:22,694 main INFO screen PSOL pass=0 dev=6.63 ins=0.0 pro=48 1a=False 1b=False 2=False (9.0s)
Sep 11 14:26:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:27,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:26:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:27,974 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:26:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:29,352 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.2s)
Sep 11 14:26:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:32,040 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.7 pro=5 1a=False 1b=False 2=True (4.3s)
Sep 11 14:26:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:26:34,059 main INFO screen NEIL pass=0 dev=0.0 ins=22.52 pro=31 1a=False 1b=False 2=False (5.4s)
Sep 11 14:27:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:27:25,326 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:27:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:27:25,494 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:27:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:27:28,174 main INFO screen HZN pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 14:27:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:27:32,505 main INFO screen BRAIN pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (7.2s)
Sep 11 14:27:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:27:57,679 main INFO screen CHADSTER pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 11 14:28:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:28:04,150 main INFO screen DOOYET pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (8.9s)
Sep 11 14:28:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:28:59,817 main INFO screen TDOGE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 14:29:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:01,622 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:29:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:01,754 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:29:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:07,503 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 14:29:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:08,862 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:29:08 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T13:01:44Z
--- update 2026-09-11T13:06:49Z
--- update 2026-09-11T13:11:58Z
--- update 2026-09-11T13:16:59Z
--- update 2026-09-11T13:22:01Z
--- update 2026-09-11T13:27:04Z
--- update 2026-09-11T13:32:04Z
--- update 2026-09-11T13:37:17Z
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
