# Schaduwbot status

- tijd: 2026-09-11 17:00:59 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 3 hours, 14 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.7G/38G | geheugen: 834/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 25875, "tokens_in_memory": 7077, "msgs": 3192347, "trades": 743802, "creates": 8176, "decode_fail": 58975, "rpc_calls": 13490, "rpc_errors": 1205, "sol_usd": 102.40916348601267, "open_positions": 76, "log_all_trades": true}
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
Sep 11 16:53:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:53:39,533 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 16:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:53:44,376 main INFO screen BetOnBlak pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 16:53:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:53:54,416 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 11 16:53:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:53:59,429 main INFO screen shrk pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 16:54:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:18,058 main INFO screen stocklana pass=0 dev=0.36 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 11 16:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:37,557 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:37,653 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:37,842 main INFO screen CHEDDAR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 16:54:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:42,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:54:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:42,805 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:54:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:43,122 main INFO screen ily pass=0 dev=0.0 ins=25.33 pro=46 1a=False 1b=False 2=True (0.5s)
Sep 11 16:54:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:54:50,067 main INFO screen USMS pass=0 dev=0.77 ins=0.0 pro=5 1a=False 1b=False 2=False (2.6s)
Sep 11 16:55:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:16,202 main INFO screen lm pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=True (2.1s)
Sep 11 16:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:29,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:29,368 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:29,493 main INFO screen NEIL pass=0 dev=0.0 ins=18.89 pro=7 1a=False 1b=False 2=False (0.3s)
Sep 11 16:55:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:37,154 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:55:37 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 16:55:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:39,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:55:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:39,979 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:55:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:43,570 main INFO screen Ottos pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.8s)
Sep 11 16:55:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:46,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:55:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:46,232 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:55:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:46,370 main INFO screen NEIL pass=1 dev=0.0 ins=2.71 pro=37 1a=False 1b=False 2=False (0.3s)
Sep 11 16:55:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:55,837 main INFO screen NEIL pass=0 dev=2.56 ins=20.3 pro=8 1a=False 1b=False 2=False (1.2s)
Sep 11 16:55:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:58,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:55:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:58,490 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:55:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:55:58,601 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 16:56:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:17,954 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:56:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:18,311 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:56:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:18,509 main INFO screen Barley pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (1.0s)
Sep 11 16:56:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:18,703 main INFO screen Athena pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 16:56:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:23,677 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:56:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:23,804 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:56:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:23,944 main INFO screen Suica pass=0 dev=0.0 ins=17.87 pro=10 1a=False 1b=False 2=True (0.3s)
Sep 11 16:56:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:52,596 main INFO screen kittylick pass=0 dev=1.21 ins=0.0 pro=3 1a=False 1b=False 2=False (5.3s)
Sep 11 16:56:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:56:53,138 main INFO screen COINS BUY pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.3s)
Sep 11 16:57:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:30,748 main INFO screen CHEDDAR pass=0 dev=0.26 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 16:57:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:36,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:37,096 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:37,251 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 16:57:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:53,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:57:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:53,257 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:57:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:53,440 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 16:57:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:54,210 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:57:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:54,337 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:57:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:57:54,519 main INFO screen STONKCAT pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 16:58:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:01,484 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:58:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:01,612 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:58:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:01,765 main INFO screen PONSIBLE pass=0 dev=0.48 ins=0.0 pro=5 1a=False 1b=False 2=False (4.9s)
Sep 11 16:58:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:03,684 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:58:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:03,807 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:58:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:03,826 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 16:58:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:03,930 main INFO screen HEDGE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.3s)
Sep 11 16:58:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:34,143 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:58:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:34,242 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:58:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:58:36,208 main INFO screen HENTCLIPPY pass=0 dev=0.0 ins=43.83 pro=8 1a=False 1b=False 2=True (2.2s)
Sep 11 16:59:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:04,340 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 16:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:27,425 main INFO screen $CAJUN pass=0 dev=0.49 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 16:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:27,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:27,704 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:59:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:27,869 main INFO screen VSNTC pass=0 dev=0.0 ins=0.05 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 16:59:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:32,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:59:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:32,341 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:59:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:34,474 main INFO screen CATPITALIST pass=0 dev=0.0 ins=71.91 pro=5 1a=False 1b=False 2=True (2.3s)
Sep 11 16:59:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:46,797 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:59:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:46,877 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:59:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:47,519 main INFO screen RICH pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.8s)
Sep 11 16:59:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:57,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:59:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:59:58,065 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:00:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:00,092 main INFO screen frens pass=0 dev=0.0 ins=18.17 pro=10 1a=False 1b=False 2=True (2.2s)
Sep 11 17:00:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:10,339 main INFO screen stocklana pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 17:00:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:12,124 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:00:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:12,219 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:00:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:19,143 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.1s)
Sep 11 17:00:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:20,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:00:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:20,365 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:00:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:24,547 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 11 17:00:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:33,252 main INFO screen PONSIBLE pass=0 dev=0.72 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 17:00:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:39,558 main INFO screen JENNIFER pass=0 dev=0.0 ins=20.23 pro=21 1a=False 1b=False 2=True (1.7s)
Sep 11 17:00:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:00:59,881 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:00:59 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T15:31:36Z
--- update 2026-09-11T15:37:24Z
--- update 2026-09-11T15:42:36Z
--- update 2026-09-11T15:48:24Z
--- update 2026-09-11T15:53:29Z
--- update 2026-09-11T15:58:34Z
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
