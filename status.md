# Schaduwbot status

- tijd: 2026-09-11 16:34:51 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 2 hours, 47 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 813/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 24307, "tokens_in_memory": 6886, "msgs": 3006194, "trades": 677173, "creates": 7558, "decode_fail": 53920, "rpc_calls": 11741, "rpc_errors": 1102, "sol_usd": 101.93010353466752, "open_positions": 74, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 15:49 UTC

Gelogde schaduwtrades: **25464**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 17033 | 2392 | 26 | 2392 | 164 | 4446 | 13109 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 286 | 16% | 1.7% | +41.5% | -16.2% | -7.10% | 99% |
| dip35_V1_gescreend_fail | 2573 | 26% | 3.8% | +45.5% | -25.9% | -7.06% | 100% |
| dip35_V1_alle | 2946 | 26% | 3.9% | +44.5% | -25.2% | -7.35% | 100% |
| dip35_V2_gescreend_pass | 283 | 18% | 2.5% | +41.9% | -21.2% | -9.84% | 100% |
| dip35_V2_gescreend_fail | 2575 | 24% | 4.5% | +55.4% | -28.3% | -7.79% | 100% |
| dip35_V2_alle | 2922 | 24% | 4.6% | +53.8% | -27.9% | -8.42% | 100% |
| dip35_V3_gescreend_pass | 286 | 7% | 2.4% | +133.4% | -22.6% | -11.70% | 100% |
| dip35_V3_gescreend_fail | 2612 | 13% | 6.2% | +107.3% | -29.9% | -11.70% | 100% |
| dip35_V3_alle | 2957 | 13% | 6.1% | +106.0% | -29.4% | -12.12% | 100% |
| dip40_V1_gescreend_pass | 262 | 14% | 1.5% | +42.7% | -15.4% | -7.46% | 99% |
| dip40_V1_gescreend_fail | 2502 | 26% | 3.8% | +47.9% | -25.9% | -6.60% | 100% |
| dip40_V1_alle | 2829 | 25% | 3.8% | +47.1% | -25.1% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 260 | 14% | 2.3% | +50.8% | -20.0% | -10.47% | 100% |
| dip40_V2_gescreend_fail | 2497 | 25% | 4.2% | +55.0% | -28.1% | -7.64% | 100% |
| dip40_V2_alle | 2804 | 24% | 4.3% | +54.4% | -27.6% | -8.31% | 100% |
| dip40_V3_gescreend_pass | 263 | 6% | 2.3% | +112.1% | -21.4% | -13.74% | 100% |
| dip40_V3_gescreend_fail | 2534 | 13% | 5.8% | +96.5% | -29.6% | -13.33% | 100% |
| dip40_V3_alle | 2840 | 12% | 5.7% | +95.7% | -29.0% | -13.74% | 100% |
| dip45_V1_gescreend_pass | 251 | 14% | 1.6% | +48.9% | -15.4% | -6.18% | 98% |
| dip45_V1_gescreend_fail | 2431 | 27% | 3.3% | +49.6% | -25.5% | -5.06% | 100% |
| dip45_V1_alle | 2730 | 26% | 3.4% | +49.2% | -24.7% | -5.44% | 100% |
| dip45_V2_gescreend_pass | 248 | 18% | 2.4% | +50.0% | -19.7% | -7.32% | 99% |
| dip45_V2_gescreend_fail | 2416 | 25% | 3.7% | +58.7% | -27.6% | -6.05% | 100% |
| dip45_V2_alle | 2702 | 24% | 3.8% | +57.8% | -27.1% | -6.54% | 100% |
| dip45_V3_gescreend_pass | 251 | 6% | 2.4% | +180.2% | -20.6% | -7.80% | 100% |
| dip45_V3_gescreend_fail | 2449 | 14% | 5.5% | +109.6% | -29.2% | -10.05% | 100% |
| dip45_V3_alle | 2734 | 13% | 5.4% | +111.4% | -28.5% | -10.19% | 100% |

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
| met_xlink | 1931 | 12% | 2.6% | -9.83% | 100% |
| zonder_xlink | 459 | 13% | 0.0% | -6.08% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 16:23:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:32,336 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:23:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:32,491 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:23:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:37,133 main INFO screen JIMMER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 11 16:23:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:37,767 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:23:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:38,384 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:23:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:42,471 main INFO screen JUGGHOUSE pass=0 dev=0.0 ins=78.96 pro=8 1a=False 1b=False 2=True (5.4s)
Sep 11 16:23:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:45,541 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 11 16:23:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:53,897 main INFO screen NEVERFORGET pass=1 dev=0.0 ins=18.74 pro=14 1a=False 1b=False 2=False (7.3s)
Sep 11 16:23:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:23:56,891 main INFO screen MPUP pass=0 dev=0.0 ins=20.17 pro=19 1a=False 1b=False 2=True (1.4s)
Sep 11 16:24:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:23,480 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.3s)
Sep 11 16:24:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:30,648 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:24:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:30,773 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:24:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:36,089 main INFO screen pepember pass=0 dev=0.0 ins=34.92 pro=5 1a=False 1b=False 2=True (5.5s)
Sep 11 16:24:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:37,215 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:24:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 16:24:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:59,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:24:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:24:59,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:25:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:05,566 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:25:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:05,690 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:25:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:06,664 main INFO screen BARRON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.4s)
Sep 11 16:25:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:09,390 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 11 16:25:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:28,861 main INFO screen Peter pass=1 dev=0.03 ins=0.0 pro=30 1a=False 1b=False 2=False (8.4s)
Sep 11 16:25:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:31,568 main INFO screen Home pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (9.7s)
Sep 11 16:25:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:33,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:25:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:33,953 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:25:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:38,779 main INFO screen FAUCAT pass=1 dev=0.0 ins=2.74 pro=69 1a=False 1b=False 2=False (10.7s)
Sep 11 16:25:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:39,793 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 11 16:25:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:48,915 main INFO screen AVO pass=0 dev=0.0 ins=20.21 pro=21 1a=False 1b=False 2=False (7.3s)
Sep 11 16:25:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:54,008 main INFO screen cpuai pass=0 dev=2.06 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 16:25:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:54,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:25:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:54,553 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:25:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:58,889 main INFO screen CARTELCAT pass=0 dev=6.71 ins=0.62 pro=29 1a=False 1b=False 2=False (7.8s)
Sep 11 16:25:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:25:59,112 main INFO screen FLYCHUD pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (4.9s)
Sep 11 16:26:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:26:06,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:26:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:26:07,198 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:26:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:26:11,033 main INFO screen Long pass=0 dev=0.0 ins=2.38 pro=15 1a=False 1b=False 2=True (4.3s)
Sep 11 16:26:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:26:13,467 main INFO screen MOONPAW pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 11 16:27:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:27:25,938 main INFO screen LMAO pass=0 dev=0.29 ins=0.0 pro=6 1a=False 1b=False 2=False (6.5s)
Sep 11 16:27:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:27:47,426 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.0s)
Sep 11 16:27:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:27:58,019 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:27:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:27:58,116 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:28:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:02,631 main INFO screen KONYANI pass=0 dev=0.0 ins=33.93 pro=14 1a=False 1b=False 2=True (4.7s)
Sep 11 16:28:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:03,903 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:28:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:04,078 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:28:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:08,149 main INFO screen AI pass=0 dev=0.0 ins=48.0 pro=4 1a=False 1b=False 2=True (4.3s)
Sep 11 16:28:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:30,132 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 16:28:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:28:48,025 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 11 16:29:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:04,007 main INFO screen OPOL  pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.8s)
Sep 11 16:29:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:04,017 main INFO screen FatDog pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.4s)
Sep 11 16:29:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:12,360 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 16:29:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:21,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:29:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:21,333 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:29:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:23,813 main INFO screen EULER pass=0 dev=0.0 ins=8.62 pro=11 1a=False 1b=False 2=True (2.7s)
Sep 11 16:29:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:37,546 main INFO screen $AURA pass=0 dev=0.5 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 16:29:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:48,163 main INFO screen EULER pass=1 dev=0.0 ins=19.03 pro=18 1a=False 1b=False 2=False (1.4s)
Sep 11 16:29:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:48,447 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:29:48 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 16:29:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:29:58,923 main INFO screen EULER pass=0 dev=0.88 ins=32.14 pro=28 1a=False 1b=False 2=True (5.4s)
Sep 11 16:30:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:00,052 main INFO screen btc pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.1s)
Sep 11 16:30:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:01,938 aiohttp.access INFO 94.154.43.70 [11/Sep/2026:16:30:01 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 16:30:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:02,899 main INFO screen Google pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 11 16:30:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:32,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:30:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:32,538 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:30:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:30:36,060 main INFO screen $VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 11 16:31:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:31:05,345 main INFO screen CHAROC pass=0 dev=0.28 ins=0.0 pro=3 1a=False 1b=False 2=False (1.9s)
Sep 11 16:31:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:31:11,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:31:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:31:11,169 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:31:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:31:13,307 main INFO screen FomoApp pass=0 dev=0.0 ins=0.01 pro=2 1a=False 1b=False 2=True (2.4s)
Sep 11 16:31:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:31:57,355 main INFO screen $GATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 11 16:32:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:16,834 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:32:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:16,922 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:32:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:17,103 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 16:32:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:33,953 main INFO screen stocklana pass=0 dev=0.48 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 11 16:32:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:39,299 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:32:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:39,425 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:32:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:32:39,594 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 16:33:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:33:01,642 main INFO screen stocklana pass=0 dev=0.36 ins=0.07 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 16:33:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:33:12,299 main INFO screen go pass=0 dev=0.23 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 16:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:33:44,651 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:33:44,790 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:33:44,945 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 16:34:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:34:51,412 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:34:51 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T15:05:25Z
--- update 2026-09-11T15:10:36Z
--- update 2026-09-11T15:15:48Z
--- update 2026-09-11T15:21:20Z
--- update 2026-09-11T15:26:33Z
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
