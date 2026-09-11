# Schaduwbot status

- tijd: 2026-09-11 17:31:33 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 3 hours, 44 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.7G/38G | geheugen: 851/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 27708, "tokens_in_memory": 7201, "msgs": 3400543, "trades": 811634, "creates": 8802, "decode_fail": 63311, "rpc_calls": 14840, "rpc_errors": 1314, "sol_usd": 102.2844698281351, "open_positions": 89, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 16:49 UTC

Gelogde schaduwtrades: **26758**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 18692 | 2655 | 28 | 2655 | 187 | 4886 | 14403 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 297 | 16% | 2.0% | +41.4% | -16.3% | -7.13% | 99% |
| dip35_V1_gescreend_fail | 2703 | 26% | 3.8% | +46.1% | -25.9% | -6.85% | 100% |
| dip35_V1_alle | 3094 | 26% | 3.9% | +45.3% | -25.2% | -7.09% | 100% |
| dip35_V2_gescreend_pass | 293 | 18% | 2.7% | +44.3% | -21.3% | -9.23% | 100% |
| dip35_V2_gescreend_fail | 2706 | 25% | 4.5% | +56.3% | -28.3% | -7.48% | 100% |
| dip35_V2_alle | 3068 | 24% | 4.6% | +54.9% | -27.9% | -8.06% | 100% |
| dip35_V3_gescreend_pass | 298 | 7% | 2.7% | +128.8% | -22.5% | -11.36% | 100% |
| dip35_V3_gescreend_fail | 2742 | 13% | 6.1% | +107.7% | -29.8% | -11.73% | 100% |
| dip35_V3_alle | 3104 | 13% | 6.0% | +106.3% | -29.3% | -12.08% | 100% |
| dip40_V1_gescreend_pass | 275 | 14% | 1.5% | +42.3% | -15.2% | -7.24% | 99% |
| dip40_V1_gescreend_fail | 2628 | 26% | 3.8% | +48.1% | -25.8% | -6.58% | 100% |
| dip40_V1_alle | 2975 | 25% | 3.8% | +47.4% | -25.0% | -6.79% | 100% |
| dip40_V2_gescreend_pass | 271 | 14% | 2.2% | +51.1% | -19.8% | -9.82% | 100% |
| dip40_V2_gescreend_fail | 2621 | 25% | 4.2% | +55.3% | -28.1% | -7.52% | 100% |
| dip40_V2_alle | 2944 | 24% | 4.3% | +54.7% | -27.5% | -8.12% | 100% |
| dip40_V3_gescreend_pass | 276 | 6% | 2.2% | +108.3% | -21.0% | -13.02% | 100% |
| dip40_V3_gescreend_fail | 2659 | 13% | 5.9% | +95.0% | -29.6% | -13.73% | 100% |
| dip40_V3_alle | 2983 | 12% | 5.8% | +94.1% | -29.0% | -14.00% | 100% |
| dip45_V1_gescreend_pass | 263 | 14% | 1.5% | +48.6% | -15.1% | -6.13% | 98% |
| dip45_V1_gescreend_fail | 2558 | 27% | 3.4% | +49.4% | -25.5% | -5.33% | 100% |
| dip45_V1_alle | 2875 | 26% | 3.4% | +49.3% | -24.7% | -5.61% | 100% |
| dip45_V2_gescreend_pass | 258 | 17% | 2.3% | +49.1% | -19.4% | -7.46% | 99% |
| dip45_V2_gescreend_fail | 2540 | 25% | 3.8% | +59.2% | -27.6% | -6.16% | 100% |
| dip45_V2_alle | 2841 | 24% | 3.8% | +58.2% | -27.0% | -6.64% | 100% |
| dip45_V3_gescreend_pass | 263 | 6% | 2.3% | +170.5% | -20.3% | -7.93% | 100% |
| dip45_V3_gescreend_fail | 2572 | 14% | 5.6% | +108.1% | -29.1% | -10.63% | 100% |
| dip45_V3_alle | 2874 | 13% | 5.4% | +109.5% | -28.5% | -10.71% | 100% |

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
| met_xlink | 2017 | 12% | 2.7% | -9.45% | 100% |
| zonder_xlink | 477 | 13% | 0.0% | -6.31% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 17:20:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:20:26,785 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:20:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:20:26,948 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:20:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:20:27,031 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:20:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:20:32,501 main INFO screen STONKITTY pass=0 dev=0.0 ins=78.26 pro=0 1a=False 1b=False 2=True (5.9s)
Sep 11 17:20:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:20:32,894 main INFO screen ELON pass=0 dev=0.0 ins=79.14 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 17:21:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:11,232 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:21:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:11,335 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:21:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:16,660 main INFO screen Stocklana pass=0 dev=0.0 ins=4.45 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 17:21:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:30,186 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:21:30 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 17:21:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:39,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:21:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:39,300 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:21:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:41,381 main INFO screen stocklana pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 17:21:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:47,401 main INFO screen BEER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (8.3s)
Sep 11 17:21:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:21:48,546 main INFO screen KYC pass=0 dev=0.0 ins=24.88 pro=16 1a=False 1b=False 2=True (5.9s)
Sep 11 17:22:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:22:09,415 main INFO screen EMOTD pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=True (8.1s)
Sep 11 17:23:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:05,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:23:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:05,865 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:23:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:10,246 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.6s)
Sep 11 17:23:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:35,232 main INFO screen MEME pass=0 dev=0.0 ins=17.74 pro=35 1a=False 1b=False 2=True (1.4s)
Sep 11 17:23:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:36,996 main INFO screen stocklana pass=0 dev=0.47 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 11 17:23:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:39,260 main INFO screen Coss pass=0 dev=1.82 ins=0.0 pro=2 1a=False 1b=False 2=False (10.1s)
Sep 11 17:23:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:51,208 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:23:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:51,294 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:23:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:23:57,427 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 17:24:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:24:09,863 main INFO screen Bricko pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (7.2s)
Sep 11 17:25:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:11,091 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 11 17:25:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:11,547 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:25:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:11,663 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:25:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:17,026 main INFO screen noob pass=0 dev=0.0 ins=44.31 pro=2 1a=False 1b=False 2=True (5.5s)
Sep 11 17:25:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:33,673 main INFO screen sol pass=1 dev=2.75 ins=0.0 pro=14 1a=False 1b=False 2=False (9.5s)
Sep 11 17:25:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:38,197 main INFO screen stocklana pass=0 dev=0.46 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 17:25:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:39,329 main INFO screen BOING pass=0 dev=12.44 ins=2.73 pro=44 1a=False 1b=False 2=False (9.9s)
Sep 11 17:25:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:53,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:25:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:53,151 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:25:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:25:53,542 main INFO screen frens pass=0 dev=0.0 ins=16.64 pro=8 1a=False 1b=False 2=True (0.6s)
Sep 11 17:26:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:07,373 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:26:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:07,536 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:26:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:12,581 main INFO screen TAP pass=0 dev=0.0 ins=27.82 pro=19 1a=False 1b=False 2=True (5.2s)
Sep 11 17:26:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:24,803 main INFO screen PUMPFI pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (4.0s)
Sep 11 17:26:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:33,521 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:26:33 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 17:26:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:36,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:26:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:36,491 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:26:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:37,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:26:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:41,509 main INFO screen CALLCAT pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 11 17:26:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:43,088 main INFO screen IDF pass=0 dev=0.86 ins=0.0 pro=1 1a=False 1b=False 2=True (5.6s)
Sep 11 17:26:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:26:50,697 main INFO screen stocklana pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 11 17:27:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:10,057 main INFO screen MEOW pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (9.5s)
Sep 11 17:27:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:20,973 main INFO screen Bricko pass=0 dev=0.13 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 17:27:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:41,870 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:27:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:41,934 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:27:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:47,059 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.3s)
Sep 11 17:27:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:54,571 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 17:27:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:27:57,238 main INFO screen $DKIRK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.5s)
Sep 11 17:28:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:01,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:28:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:01,231 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:28:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:07,139 main INFO screen XRPCAT pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=False 2=True (6.1s)
Sep 11 17:28:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:35,180 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:28:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:35,234 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:28:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:38,927 main INFO screen Pleb pass=0 dev=0.0 ins=8.62 pro=9 1a=False 1b=False 2=False (3.9s)
Sep 11 17:28:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:54,168 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 17:28:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:28:55,302 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 17:29:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:29:26,536 main INFO screen TROLL pass=0 dev=17.07 ins=2.98 pro=41 1a=False 1b=False 2=False (7.8s)
Sep 11 17:29:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:29:49,456 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:29:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:29:49,537 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:29:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:29:56,678 main INFO screen minibaton pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (7.3s)
Sep 11 17:30:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:30:02,849 main INFO screen CHEDDAR pass=0 dev=1.39 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 11 17:30:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:30:41,023 main INFO screen SUICA pass=0 dev=18.73 ins=0.0 pro=50 1a=False 1b=False 2=False (9.6s)
Sep 11 17:30:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:30:49,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:30:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:30:49,151 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:30:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:30:55,243 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 17:31:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:10,598 main INFO screen RISE pass=0 dev=40.89 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 17:31:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:17,114 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:31:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:17,230 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:31:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:17,370 main INFO screen IC pass=1 dev=0.0 ins=2.98 pro=26 1a=False 1b=False 2=False (0.3s)
Sep 11 17:31:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:19,872 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 11 17:31:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:23,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:31:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:23,477 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:31:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:33,208 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:31:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:33,328 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:31:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:31:33,333 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:31:33 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T16:03:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: bf2f0fbff9834af3ad8812a9ec61480b
analyses gestart (8213ec5e675e)
--- update 2026-09-11T16:08:54Z
--- update 2026-09-11T16:14:06Z
--- update 2026-09-11T16:19:29Z
--- update 2026-09-11T16:24:36Z
--- update 2026-09-11T16:29:47Z
--- update 2026-09-11T16:34:50Z
--- update 2026-09-11T16:40:09Z
--- update 2026-09-11T16:45:19Z
--- update 2026-09-11T16:50:30Z
--- update 2026-09-11T16:55:36Z
--- update 2026-09-11T17:00:58Z
--- update 2026-09-11T17:06:10Z
--- update 2026-09-11T17:11:21Z
--- update 2026-09-11T17:16:23Z
--- update 2026-09-11T17:21:29Z
--- update 2026-09-11T17:26:32Z
--- update 2026-09-11T17:31:32Z
```

## Analyses (laatste 25 regels)
```
inactive
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
16:03:36 7475 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
16:03:40   ingelezen tot rowid 1652718 (200000 rijen, 200000 bruikbaar)
16:03:41   ingelezen tot rowid 1684078 (231360 rijen, 231360 bruikbaar)
16:03:41 ingelezen: 231360 nieuwe trades, 231360 bruikbaar (4s)
16:03:46 klaar in 10s -> /opt/schaduwbot/reports/ledger.md
16:03:48   2000 nieuwe tokens doorgerekend
16:03:48 klaar in 2s: 3448 tokens, 2089 nieuw -> /opt/schaduwbot/reports/video_replay.md
16:03:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 16:03 UTC
16:03:48 32317 tokens geladen
16:03:51   2000 tokens, 318886 trades, 83589 posities (3s)
16:03:54   4000 tokens, 653328 trades, 170937 posities (6s)
16:03:57   6000 tokens, 953319 trades, 248089 posities (9s)
16:04:01   8000 tokens, 1282543 trades, 335538 posities (13s)
16:04:05   10000 tokens, 1602875 trades, 422034 posities (16s)
16:04:06 posities: 447031 uit 1684507 trades (17s)
16:04:12 104760 wallets gerekend
16:04:12 geluk-toets
16:04:29 persistentie
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
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
