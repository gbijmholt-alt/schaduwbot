# Schaduwbot status

- tijd: 2026-09-11 15:53:30 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 2 hours, 6 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 771/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 21826, "tokens_in_memory": 6281, "msgs": 2426650, "trades": 563582, "creates": 6329, "decode_fail": 45148, "rpc_calls": 9694, "rpc_errors": 932, "sol_usd": 102.04494687269836, "open_positions": 70, "log_all_trades": true}
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
Sep 11 15:42:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:01,481 main INFO screen $CAJUN pass=0 dev=0.63 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 11 15:42:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:09,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:42:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:10,175 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:42:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:10,324 main INFO screen BOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:42:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:26,198 main INFO screen MICROFLY pass=0 dev=0.0 ins=6.06 pro=50 1a=False 1b=True 2=True (2.9s)
Sep 11 15:42:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:37,252 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:42:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:42:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:52,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:42:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:52,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:42:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:52,436 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:42:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:56,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:42:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:56,477 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:42:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:56,613 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 15:43:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:43:40,937 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:43:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:43:41,034 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:43:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:43:41,235 main INFO screen HailMary  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 15:43:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:43:59,886 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:43:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:43:59,982 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:44:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:00,265 main INFO screen Sirius pass=0 dev=0.0 ins=19.03 pro=40 1a=False 1b=False 2=True (0.5s)
Sep 11 15:44:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:28,745 main INFO screen NABU pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 11 15:44:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:35,566 main INFO screen DOOROC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 11 15:44:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:35,847 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:44:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:35,961 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:44:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:36,125 main INFO screen Sirius pass=0 dev=0.0 ins=24.12 pro=11 1a=False 1b=False 2=True (0.3s)
Sep 11 15:44:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:44:49,098 main INFO screen hailmary pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 15:45:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:07,950 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:45:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:08,049 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:45:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:08,330 main INFO screen Swen pass=0 dev=0.0 ins=22.69 pro=12 1a=False 1b=False 2=False (0.5s)
Sep 11 15:45:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:14,370 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:45:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:14,468 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:45:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:14,588 main INFO screen $1 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:45:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:29,743 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 15:45:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:35,760 main INFO screen HolyGuaca pass=0 dev=0.64 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 11 15:45:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:45:37,645 main INFO screen $Pto pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 15:46:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:46:23,347 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:46:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:46:23,444 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:46:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:46:23,678 main INFO screen BULLISHCAT pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:47:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:00,299 main INFO screen Rick pass=1 dev=0.0 ins=14.24 pro=41 1a=False 1b=False 2=False (4.0s)
Sep 11 15:47:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:12,169 main INFO screen HedgeHog pass=1 dev=0.0 ins=19.17 pro=46 1a=False 1b=False 2=False (2.9s)
Sep 11 15:47:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:33,007 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:47:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:33,099 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:47:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:33,301 main INFO screen Ben pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:47:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:47:50,124 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.1s)
Sep 11 15:48:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:03,441 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:48:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:03,560 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:48:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:03,695 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 15:48:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:23,781 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:48:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:23,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:48:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:24,104 main INFO screen BLY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:48:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:25,182 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:48:25 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 15:48:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:35,856 main INFO screen Pep/11 pass=0 dev=1.97 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 15:48:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:48:37,511 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 15:49:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:23,731 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:49:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:23,814 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:49:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:24,173 main INFO screen CYBERZ pass=0 dev=0.0 ins=78.04 pro=8 1a=False 1b=False 2=True (0.6s)
Sep 11 15:49:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:38,185 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:49:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:38,309 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:49:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:49:38,492 main INFO screen MONEYCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:50:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:40,049 main INFO screen Cocaine pass=0 dev=0.0 ins=38.54 pro=72 1a=False 1b=False 2=True (9.0s)
Sep 11 15:50:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:40,117 main INFO screen LaMisery pass=0 dev=1.96 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 11 15:50:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:40,214 main INFO screen stocklana pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 11 15:50:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:46,681 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 15:50:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:47,993 main INFO screen DogAss pass=0 dev=6.63 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 11 15:50:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:49,313 main INFO screen HOMO pass=1 dev=0.0 ins=18.6 pro=24 1a=False 1b=False 2=False (9.2s)
Sep 11 15:50:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:50:50,335 main INFO screen humabird pass=0 dev=1.37 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 15:51:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:18,778 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:51:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:18,878 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:51:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:19,085 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:51:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:49,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:51:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:49,586 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:51:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:51:49,806 main INFO screen FlyTable pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 15:52:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:02,503 main INFO screen Pep100kRC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 15:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:15,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:15,845 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:15,977 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:52:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:27,524 main INFO screen hailmary pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 15:52:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:52:42,469 main INFO screen $CAJUN pass=0 dev=1.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 15:53:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:02,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:53:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:03,048 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:53:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:03,223 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 15:53:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:53:30,924 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:53:30 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T15:15:48Z
--- update 2026-09-11T15:21:20Z
--- update 2026-09-11T15:26:33Z
--- update 2026-09-11T15:31:36Z
--- update 2026-09-11T15:37:24Z
--- update 2026-09-11T15:42:36Z
--- update 2026-09-11T15:48:24Z
--- update 2026-09-11T15:53:29Z
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
