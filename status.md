# Schaduwbot status

- tijd: 2026-09-11 13:01:45 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 23 hours, 14 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 657/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 11521, "tokens_in_memory": 2954, "msgs": 959571, "trades": 246932, "creates": 2954, "decode_fail": 17876, "rpc_calls": 4199, "rpc_errors": 404, "sol_usd": 101.3254617931799, "open_positions": 89, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 12:49 UTC

Gelogde schaduwtrades: **22644**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 13510 | 1846 | 23 | 1846 | 119 | 3508 | 10289 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 255 | 15% | 1.6% | +41.0% | -16.1% | -7.57% | 99% |
| dip35_V1_gescreend_fail | 2281 | 26% | 3.8% | +46.1% | -26.0% | -6.93% | 100% |
| dip35_V1_alle | 2618 | 26% | 3.9% | +45.0% | -25.4% | -7.30% | 100% |
| dip35_V2_gescreend_pass | 253 | 18% | 2.0% | +39.4% | -21.0% | -10.24% | 100% |
| dip35_V2_gescreend_fail | 2285 | 24% | 4.4% | +56.4% | -28.4% | -7.63% | 100% |
| dip35_V2_alle | 2597 | 24% | 4.5% | +54.5% | -28.0% | -8.34% | 100% |
| dip35_V3_gescreend_pass | 256 | 7% | 2.3% | +137.5% | -22.7% | -12.07% | 100% |
| dip35_V3_gescreend_fail | 2324 | 13% | 6.2% | +114.1% | -30.1% | -10.97% | 100% |
| dip35_V3_alle | 2634 | 13% | 6.2% | +112.1% | -29.6% | -11.54% | 100% |
| dip40_V1_gescreend_pass | 235 | 14% | 1.7% | +43.1% | -15.6% | -7.58% | 98% |
| dip40_V1_gescreend_fail | 2221 | 26% | 3.7% | +47.9% | -26.0% | -6.51% | 100% |
| dip40_V1_alle | 2517 | 25% | 3.8% | +47.0% | -25.2% | -6.86% | 100% |
| dip40_V2_gescreend_pass | 233 | 14% | 2.1% | +49.8% | -20.1% | -10.46% | 100% |
| dip40_V2_gescreend_fail | 2217 | 25% | 4.1% | +56.2% | -28.2% | -7.25% | 100% |
| dip40_V2_alle | 2493 | 24% | 4.2% | +55.5% | -27.7% | -7.99% | 100% |
| dip40_V3_gescreend_pass | 236 | 6% | 2.5% | +114.0% | -21.7% | -13.69% | 100% |
| dip40_V3_gescreend_fail | 2257 | 13% | 5.8% | +102.3% | -29.8% | -12.45% | 100% |
| dip40_V3_alle | 2532 | 12% | 5.8% | +101.0% | -29.2% | -12.98% | 100% |
| dip45_V1_gescreend_pass | 224 | 14% | 1.8% | +50.1% | -15.5% | -6.14% | 97% |
| dip45_V1_gescreend_fail | 2158 | 28% | 3.3% | +49.4% | -25.6% | -4.84% | 100% |
| dip45_V1_alle | 2426 | 26% | 3.4% | +49.0% | -24.8% | -5.24% | 100% |
| dip45_V2_gescreend_pass | 221 | 19% | 2.3% | +49.7% | -19.7% | -6.80% | 98% |
| dip45_V2_gescreend_fail | 2143 | 26% | 3.7% | +59.1% | -27.7% | -5.52% | 100% |
| dip45_V2_alle | 2398 | 25% | 3.8% | +58.1% | -27.2% | -6.04% | 100% |
| dip45_V3_gescreend_pass | 224 | 7% | 2.7% | +186.5% | -20.9% | -7.01% | 99% |
| dip45_V3_gescreend_fail | 2175 | 14% | 5.7% | +109.0% | -29.3% | -10.01% | 100% |
| dip45_V3_alle | 2429 | 13% | 5.6% | +111.0% | -28.7% | -10.10% | 100% |

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
| met_xlink | 1732 | 12% | 2.6% | -9.97% | 100% |
| zonder_xlink | 405 | 14% | 0.0% | -5.52% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 12:47:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:27,784 main INFO screen help pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 12:47:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:31,937 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 11 12:47:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:57,849 main INFO screen help pass=0 dev=1.4 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 11 12:48:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:48:05,505 main INFO screen GOLDCAT pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (1.5s)
Sep 11 12:48:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:48:25,446 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 12:48:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:48:47,436 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:48:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:48:47,534 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:48:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:48:47,723 main INFO screen FOMCAT pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 12:49:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:15,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:49:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:15,442 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:49:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:15,681 main INFO screen NEEDOH pass=0 dev=0.0 ins=16.99 pro=10 1a=False 1b=False 2=True (0.4s)
Sep 11 12:49:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:22,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:49:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:22,861 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:49:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:49:22,980 main INFO screen PEARL pass=0 dev=0.0 ins=17.47 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 11 12:50:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:50:36,509 main INFO screen eeee pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 11 12:50:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:50:36,559 main INFO screen help pass=0 dev=0.91 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 11 12:50:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:50:53,264 main INFO screen RISE pass=0 dev=40.6 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 12:51:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:01,945 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:51:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:02,028 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:51:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:02,139 main INFO screen UGOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 12:51:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:05,123 main INFO screen MCCAT pass=0 dev=0.0 ins=20.17 pro=20 1a=False 1b=False 2=True (1.3s)
Sep 11 12:51:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:11,626 main INFO screen STONKY pass=0 dev=0.41 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 12:51:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:34,546 main INFO screen HALH pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 12:51:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:42,243 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:51:42 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:51:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:45,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:51:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:45,422 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:51:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:51:45,556 main INFO screen TripleD pass=0 dev=0.0 ins=16.61 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 12:52:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:12,494 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:52:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:12,591 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:52:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:12,800 main INFO screen TripleD pass=0 dev=0.0 ins=17.8 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 12:52:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:16,302 main INFO screen Treecoin pass=0 dev=0.0 ins=19.29 pro=25 1a=False 1b=False 2=True (1.4s)
Sep 11 12:52:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:38,484 main INFO screen SUN pass=0 dev=0.06 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 12:52:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:39,203 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:52:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:39,283 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:52:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:39,535 main INFO screen ELON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 12:52:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:43,302 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:52:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:43,450 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:52:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:52:43,596 main INFO screen STONKY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 12:53:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:53:25,929 main INFO screen Pipi pass=0 dev=0.13 ins=21.35 pro=21 1a=False 1b=False 2=True (1.7s)
Sep 11 12:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:53:44,602 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:53:44,767 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:53:44,932 main INFO screen STONKY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 12:54:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:54:01,419 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:54:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:54:01,516 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:54:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:54:01,720 main INFO screen Axel pass=0 dev=0.0 ins=20.25 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 12:55:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:25,183 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:55:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:25,411 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:55:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:25,742 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 12:55:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:26,956 main INFO screen PC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.9s)
Sep 11 12:55:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:30,578 main INFO screen mert pass=1 dev=0.0 ins=17.68 pro=21 1a=False 1b=False 2=False (1.8s)
Sep 11 12:55:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:55:35,988 main INFO screen G pass=0 dev=1.9 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 12:56:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:04,799 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:56:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:05,052 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:56:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:05,369 main INFO screen ZKITTY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 11 12:56:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:06,683 main INFO screen bob pass=0 dev=0.0 ins=21.39 pro=24 1a=False 1b=False 2=True (2.1s)
Sep 11 12:56:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:30,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:56:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:31,119 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:56:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:31,422 main INFO screen Laptop pass=0 dev=0.0 ins=11.61 pro=5 1a=False 1b=False 2=True (0.7s)
Sep 11 12:56:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:31,754 main INFO screen BetOnBlak pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 12:56:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:56:45,558 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:56:45 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:57:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:00,068 main INFO screen RIGBY pass=0 dev=0.0 ins=17.43 pro=20 1a=False 1b=False 2=True (1.6s)
Sep 11 12:57:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:02,852 main INFO screen dnoc pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 12:57:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:22,234 main INFO screen STONKY pass=0 dev=0.8 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 11 12:57:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:25,785 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:57:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:25,901 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:57:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:26,032 main INFO screen OnlyEmber pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 12:57:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:45,405 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 12:57:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:57:48,374 main INFO screen DOOROC pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (1.5s)
Sep 11 12:58:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:05,210 main INFO screen catjak pass=0 dev=0.0 ins=17.52 pro=26 1a=False 1b=False 2=True (1.7s)
Sep 11 12:58:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:29,351 main INFO screen ZORTOISE pass=0 dev=0.0 ins=20.65 pro=21 1a=False 1b=False 2=True (1.5s)
Sep 11 12:58:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:35,313 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:58:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:35,436 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:58:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:37,707 main INFO screen DUST pass=0 dev=0.0 ins=18.79 pro=5 1a=False 1b=False 2=True (2.5s)
Sep 11 12:58:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:58:49,657 main INFO screen help pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 12:59:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:59:05,506 main INFO screen dnoc pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 12:59:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:59:33,983 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:59:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:59:34,079 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:59:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:59:34,280 main INFO screen TheGiga pass=0 dev=0.0 ins=77.37 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 11 13:01:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:01:30,082 main INFO screen BPCATE pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (6.0s)
Sep 11 13:01:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:01:45,452 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:01:45 +0000] "GET /health HTTP/1.1" 200 448 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T11:33:37Z
--- update 2026-09-11T11:38:38Z
--- update 2026-09-11T11:43:38Z
--- update 2026-09-11T11:49:07Z
--- update 2026-09-11T11:54:33Z
--- update 2026-09-11T11:59:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 91d89b5fe55047b9bdf833a434bfc1f0
analyses gestart (8213ec5e675e)
--- update 2026-09-11T12:05:15Z
--- update 2026-09-11T12:10:30Z
--- update 2026-09-11T12:15:36Z
--- update 2026-09-11T12:20:40Z
--- update 2026-09-11T12:26:02Z
--- update 2026-09-11T12:31:19Z
--- update 2026-09-11T12:36:32Z
--- update 2026-09-11T12:41:33Z
--- update 2026-09-11T12:46:36Z
--- update 2026-09-11T12:51:41Z
--- update 2026-09-11T12:56:44Z
--- update 2026-09-11T13:01:44Z
```

## Analyses (laatste 25 regels)
```
inactive
09:54:59 25844 tokens geladen
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
11:59:36 2892 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
11:59:39   ingelezen tot rowid 1255924 (151022 rijen, 151022 bruikbaar)
11:59:39 ingelezen: 151022 nieuwe trades, 151022 bruikbaar (2s)
11:59:40 klaar in 4s -> /opt/schaduwbot/reports/ledger.md
11:59:40 klaar in 0s: 59 tokens, 67 nieuw -> /opt/schaduwbot/reports/video_replay.md
11:59:40 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 11:59 UTC
11:59:40 27728 tokens geladen
11:59:44   2000 tokens, 398779 trades, 119472 posities (4s)
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
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
