# Schaduwbot status

- tijd: 2026-09-11 13:22:02 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 23 hours, 35 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 663/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 12738, "tokens_in_memory": 3292, "msgs": 1101784, "trades": 286590, "creates": 3292, "decode_fail": 23906, "rpc_calls": 5024, "rpc_errors": 466, "sol_usd": 101.4256236689908, "open_positions": 78, "log_all_trades": true}
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
Sep 11 13:10:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:12,867 main INFO screen PROTOC pass=0 dev=0.0 ins=17.33 pro=5 1a=False 1b=False 2=True (6.6s)
Sep 11 13:10:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:16,091 main INFO screen Astrachan pass=1 dev=0.0 ins=8.35 pro=26 1a=False 1b=False 2=False (5.7s)
Sep 11 13:10:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:16,710 main INFO screen shrk pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 11 13:10:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:22,613 main INFO screen Osama pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.7s)
Sep 11 13:10:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:49,617 main INFO screen help pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (10.2s)
Sep 11 13:10:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:10:57,948 main INFO screen Astrachan pass=1 dev=0.0 ins=0.3 pro=44 1a=False 1b=False 2=False (2.4s)
Sep 11 13:11:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:03,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:11:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:03,418 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:11:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:07,117 main INFO screen GEO pass=0 dev=0.0 ins=21.44 pro=27 1a=False 1b=False 2=False (5.4s)
Sep 11 13:11:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:08,382 main INFO screen help pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.6s)
Sep 11 13:11:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:40,171 main INFO screen Fly pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (8.5s)
Sep 11 13:11:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:48,188 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:11:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:48,317 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:11:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:48,663 main INFO screen Sauron pass=0 dev=0.0 ins=16.72 pro=39 1a=False 1b=False 2=True (0.5s)
Sep 11 13:11:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:11:59,585 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:11:59 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 13:12:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:12:01,768 main INFO screen KumoAngel pass=0 dev=0.0 ins=21.24 pro=21 1a=False 1b=False 2=True (5.8s)
Sep 11 13:12:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:12:34,394 main INFO screen LaMisery pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.2s)
Sep 11 13:13:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:15,250 main INFO screen FERDA pass=0 dev=6.95 ins=0.65 pro=6 1a=False 1b=False 2=False (8.0s)
Sep 11 13:13:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:19,070 main INFO screen DOG pass=1 dev=0.0 ins=16.22 pro=69 1a=False 1b=False 2=False (2.5s)
Sep 11 13:13:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:42,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:13:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:42,496 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:13:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:46,143 main INFO screen twin911 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 11 13:13:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:59,058 main INFO screen FIRE pass=1 dev=2.41 ins=1.72 pro=30 1a=False 1b=False 2=False (9.0s)
Sep 11 13:13:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:13:59,680 main INFO screen USMS pass=0 dev=1.07 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 11 13:14:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:14:19,419 main INFO screen Hank pass=0 dev=0.0 ins=19.49 pro=28 1a=False 1b=False 2=True (5.6s)
Sep 11 13:14:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:14:59,258 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:14:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:14:59,395 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:15:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:15:02,864 main INFO screen S&P6900 pass=0 dev=0.0 ins=12.37 pro=15 1a=False 1b=False 2=True (3.7s)
Sep 11 13:15:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:15:48,407 main INFO screen fg pass=0 dev=10.45 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 13:16:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:12,807 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:16:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:12,909 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:16:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:14,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:16:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:14,271 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:16:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:19,394 main INFO screen Tesla pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 11 13:16:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:20,428 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:16:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:20,556 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:16:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:20,918 main INFO screen ORCAT pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 13:16:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:23,838 main INFO screen ELOGE pass=0 dev=0.0 ins=17.17 pro=8 1a=False 1b=False 2=True (3.5s)
Sep 11 13:16:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:29,133 main INFO screen ©at pass=1 dev=0.0 ins=18.4 pro=16 1a=False 1b=False 2=False (7.7s)
Sep 11 13:16:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:42,174 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:16:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:42,344 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:16:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:43,236 main INFO screen USMS pass=0 dev=1.05 ins=0.0 pro=3 1a=False 1b=False 2=False (9.8s)
Sep 11 13:16:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:44,258 main INFO screen help pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (10.7s)
Sep 11 13:16:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:46,943 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.8s)
Sep 11 13:16:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:47,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:16:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:47,648 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:16:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:49,297 main INFO screen Stella pass=0 dev=0.0 ins=0.07 pro=83 1a=False 1b=False 2=True (4.2s)
Sep 11 13:16:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:16:53,220 main INFO screen BRAINRTRD pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (6.3s)
Sep 11 13:17:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:01,095 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:17:01 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 13:17:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:12,034 main INFO screen COINWORK pass=1 dev=3.42 ins=14.82 pro=26 1a=False 1b=False 2=False (1.3s)
Sep 11 13:17:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:14,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:17:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:14,495 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:17:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:18,583 main INFO screen FOMOX pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=False 2=True (4.3s)
Sep 11 13:17:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:34,637 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:17:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:34,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:17:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:40,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:17:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:40,414 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:17:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:41,341 main INFO screen Holy Guac pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.9s)
Sep 11 13:17:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:43,460 main INFO screen eeee pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (9.1s)
Sep 11 13:17:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:44,423 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.2s)
Sep 11 13:17:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:17:49,612 main INFO screen G pass=0 dev=0.0 ins=19.66 pro=23 1a=False 1b=False 2=True (5.6s)
Sep 11 13:18:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:19,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:18:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:19,536 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:18:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:23,638 main INFO screen SNOOPY pass=0 dev=0.0 ins=62.94 pro=4 1a=False 1b=False 2=True (4.3s)
Sep 11 13:18:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:26,399 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:18:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:26,526 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:18:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:30,713 main INFO screen $FLYPO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 11 13:18:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:18:54,122 main INFO screen SPNE pass=1 dev=0.0 ins=17.65 pro=20 1a=False 1b=False 2=False (7.3s)
Sep 11 13:19:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:19:42,640 main INFO screen SAVPIR pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 11 13:19:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:19:44,741 main INFO screen EGO pass=0 dev=18.22 ins=1.06 pro=17 1a=False 1b=True 2=False (1.2s)
Sep 11 13:19:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:19:44,910 main INFO screen DAWG pass=1 dev=0.75 ins=19.91 pro=31 1a=False 1b=False 2=False (5.3s)
Sep 11 13:20:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:20:34,220 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:20:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:20:34,313 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:20:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:20:41,849 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.7s)
Sep 11 13:21:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:21:16,062 main INFO screen eeee pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 11 13:21:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:21:29,695 main INFO screen Gutjang pass=1 dev=0.56 ins=19.74 pro=18 1a=False 1b=False 2=False (7.0s)
Sep 11 13:21:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:21:35,986 main INFO screen help pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 11 13:21:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:21:59,378 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:21:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:21:59,414 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:22:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:22:02,500 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:22:02 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T13:06:49Z
--- update 2026-09-11T13:11:58Z
--- update 2026-09-11T13:16:59Z
--- update 2026-09-11T13:22:01Z
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
