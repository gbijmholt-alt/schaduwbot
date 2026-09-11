# Schaduwbot status

- tijd: 2026-09-11 14:44:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 57 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 719/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 17692, "tokens_in_memory": 4978, "msgs": 1696491, "trades": 425091, "creates": 4978, "decode_fail": 34606, "rpc_calls": 7469, "rpc_errors": 712, "sol_usd": 103.09209477038829, "open_positions": 52, "log_all_trades": true}
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
Sep 11 14:29:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:50,307 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:29:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:29:56,195 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.1s)
Sep 11 14:30:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:00,712 main INFO screen NIGGA pass=0 dev=0.04 ins=0.0 pro=5 1a=False 1b=False 2=False (10.5s)
Sep 11 14:30:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:04,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:30:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:04,969 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:30:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:05,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:30:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:05,562 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:30:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:09,172 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 11 14:30:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:10,296 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 14:30:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:11,055 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:30:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:11,173 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:30:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:15,480 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.5s)
Sep 11 14:30:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:34,455 main INFO screen Twins pass=1 dev=0.01 ins=0.14 pro=30 1a=False 1b=False 2=False (9.5s)
Sep 11 14:30:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:30:49,653 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 11 14:31:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:31:13,529 main INFO screen cashback pass=0 dev=7.22 ins=10.85 pro=29 1a=False 1b=False 2=False (1.8s)
Sep 11 14:31:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:31:23,631 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:31:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:31:23,765 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:31:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:31:23,890 main INFO screen $BBCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 14:32:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:32:27,139 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:32:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:32:27,182 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:32:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:32:27,544 main INFO screen SOL pass=0 dev=0.0 ins=0.43 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 11 14:32:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:32:56,318 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 14:33:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:33:16,440 aiohttp.access INFO 165.22.47.52 [11/Sep/2026:14:33:16 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 11 14:33:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:33:33,861 main INFO screen $CAT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (1.7s)
Sep 11 14:33:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:33:38,467 main INFO screen VAULT pass=0 dev=0.0 ins=26.36 pro=47 1a=False 1b=True 2=False (1.9s)
Sep 11 14:33:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:33:59,532 main INFO screen RISE pass=0 dev=37.85 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 14:34:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:07,841 main INFO screen CHAROC pass=0 dev=2.32 ins=0.0 pro=2 1a=False 1b=False 2=True (1.5s)
Sep 11 14:34:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:17,528 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 11 14:34:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:21,707 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:34:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:21,837 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:34:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:22,071 main INFO screen SOL pass=1 dev=0.0 ins=1.06 pro=12 1a=False 1b=False 2=False (0.4s)
Sep 11 14:34:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:23,318 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:34:23 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 14:34:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:34:38,724 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 14:35:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:35:43,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:35:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:35:43,692 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:35:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:35:43,878 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:36:31,393 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:36:31,487 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:36:31,696 main INFO screen OpenClaw pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 14:37:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:37:23,035 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:37:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:37:23,164 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:37:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:37:23,342 main INFO screen HELIUSCAT pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 14:38:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:38:27,918 main INFO screen stocklana pass=0 dev=0.39 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 14:39:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:05,002 main INFO screen STOCKDOGE pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 11 14:39:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:10,980 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:39:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:11,111 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:39:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:11,249 main INFO screen PONCAT pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 14:39:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:19,793 main INFO screen fg pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 11 14:39:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:35,257 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:39:35 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 14:39:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:45,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:39:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:45,491 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:39:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:39:45,675 main INFO screen mergemind pass=0 dev=0.0 ins=36.52 pro=20 1a=False 1b=False 2=True (0.4s)
Sep 11 14:40:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:19,800 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:40:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:19,893 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:40:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:20,086 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:40:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:32,046 main INFO screen DERP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.6s)
Sep 11 14:40:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:46,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:40:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:46,924 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:40:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:40:47,053 main INFO screen $PTA  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:41:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:41:15,093 main INFO screen J777CRYPTO pass=0 dev=0.0 ins=24.6 pro=13 1a=False 1b=False 2=True (2.0s)
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:16,784 main INFO screen s pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 14:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:27,895 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:28,062 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:28,193 main INFO screen HZN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 14:42:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:29,858 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:42:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:29,983 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:42:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:42:30,142 main INFO screen BULL pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 14:43:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:24,615 main INFO screen NASDARQ pass=0 dev=3.46 ins=33.08 pro=12 1a=False 1b=False 2=True (1.3s)
Sep 11 14:43:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:32,342 main INFO screen kittylick pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 14:43:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:41,161 main INFO screen USMS pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,550 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,810 main INFO screen brainpeppe pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=False 2=True (0.7s)
Sep 11 14:43:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:43:49,934 main INFO screen nudey pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,544 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:44:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:07,747 main INFO screen Flybook pass=0 dev=0.0 ins=36.52 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 14:44:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:44:37,319 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:44:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T14:34:22Z
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
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
