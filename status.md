# Schaduwbot status

- tijd: 2026-09-11 12:51:42 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 23 hours, 4 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 650/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 10917, "tokens_in_memory": 2766, "msgs": 924680, "trades": 228010, "creates": 2766, "decode_fail": 15084, "rpc_calls": 3895, "rpc_errors": 380, "sol_usd": 101.34718687269735, "open_positions": 70, "log_all_trades": true}
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
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,639 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,944 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 12:38:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:54,008 main INFO screen 100 pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 12:39:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:39:40,566 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.0s)
Sep 11 12:40:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:40:17,716 main INFO screen $CAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 12:40:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:40:27,368 main INFO screen Rufus pass=0 dev=1.2 ins=17.43 pro=21 1a=False 1b=False 2=True (1.2s)
Sep 11 12:41:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:12,822 main INFO screen 34% pass=0 dev=12.57 ins=0.0 pro=2 1a=False 1b=False 2=True (2.3s)
Sep 11 12:41:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:12,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:41:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:13,208 main INFO screen Launchcat pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 12:41:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:34,539 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:41:34 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:41:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:51,173 main INFO screen kitty pass=0 dev=1.92 ins=16.6 pro=15 1a=False 1b=False 2=True (1.9s)
Sep 11 12:41:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:52,690 main INFO screen LMAO pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 12:42:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:09,108 main INFO screen me pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 12:42:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:24,240 main INFO screen CHAROC pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 12:42:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:25,006 main INFO screen TRANS pass=0 dev=0.48 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 12:42:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:30,777 main INFO screen Mamiko pass=1 dev=0.0 ins=6.6 pro=46 1a=False 1b=False 2=False (3.4s)
Sep 11 12:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:33,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:33,592 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:42:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:34,013 main INFO screen MEME pass=0 dev=0.0 ins=36.47 pro=10 1a=False 1b=False 2=True (1.0s)
Sep 11 12:42:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:34,329 main INFO screen b pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,128 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,277 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,393 main INFO screen KALSHE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,620 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,818 main INFO screen SUN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,106 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,330 main INFO screen STONKY pass=0 dev=0.0 ins=47.36 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 12:44:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:15,075 main INFO screen TURAGE pass=0 dev=0.13 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 11 12:44:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:16,233 main INFO screen LEPRECHAUN pass=0 dev=0.47 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,563 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,748 main INFO screen FLY BRAIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 12:44:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:49,672 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:44:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:49,806 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:44:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:50,015 main INFO screen b pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 12:45:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:00,403 main INFO screen FLS pass=0 dev=0.07 ins=0.1 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 12:45:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:02,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:45:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:02,917 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:45:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:03,072 main INFO screen SAVAGE pass=0 dev=0.0 ins=37.77 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 11 12:45:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:08,962 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:45:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:09,122 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:45:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:09,263 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 12:45:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:17,151 main INFO screen SOAG pass=1 dev=0.0 ins=12.62 pro=10 1a=False 1b=False 2=False (1.3s)
Sep 11 12:46:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:04,633 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,206 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,372 main INFO screen chillbrain pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 12:46:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:37,158 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:46:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:47:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:03,475 main INFO screen TRANS pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 11 12:47:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:20,109 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:47:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:20,356 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:47:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:20,668 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.8s)
Sep 11 12:47:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:47:22,043 main INFO screen 100 pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=True (2.1s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T11:23:37Z
--- update 2026-09-11T11:28:37Z
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
