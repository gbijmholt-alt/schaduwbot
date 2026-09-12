# Schaduwbot status

- tijd: 2026-09-12 09:47:05 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 20 hours, 0 minutes
- bot-service: active
- code-versie: 6d8fae6
- schijf: 3.5G/38G | geheugen: 621/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 6914, "tokens_in_memory": 1571, "msgs": 298049, "trades": 123541, "creates": 1572, "decode_fail": 4762, "rpc_calls": 3846, "rpc_errors": 195, "sol_usd": 101.9958815667303, "open_positions": 34, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 8436 | 1351 | 6 | 1351 | 93 | 2391 | 7209 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 503 | 16% | 2.0% | +44.1% | -16.6% | -6.93% | 100% |
| dip35_V1_gescreend_fail | 4124 | 27% | 3.8% | +45.5% | -25.8% | -6.62% | 100% |
| dip35_V1_alle | 5058 | 26% | 3.9% | +44.8% | -25.2% | -6.88% | 100% |
| dip35_V2_gescreend_pass | 500 | 21% | 2.8% | +43.1% | -20.9% | -7.42% | 100% |
| dip35_V2_gescreend_fail | 4159 | 25% | 4.3% | +56.0% | -27.9% | -6.92% | 100% |
| dip35_V2_alle | 5021 | 24% | 4.5% | +53.6% | -27.6% | -7.71% | 100% |
| dip35_V3_gescreend_pass | 502 | 8% | 3.2% | +297.3% | -22.3% | +4.45% | 100% |
| dip35_V3_gescreend_fail | 4247 | 13% | 5.8% | +114.4% | -29.5% | -10.28% | 100% |
| dip35_V3_alle | 5072 | 13% | 5.9% | +119.1% | -29.1% | -9.75% | 100% |
| dip40_V1_gescreend_pass | 473 | 14% | 2.1% | +46.7% | -15.9% | -7.07% | 100% |
| dip40_V1_gescreend_fail | 4051 | 26% | 3.7% | +47.1% | -25.6% | -6.54% | 100% |
| dip40_V1_alle | 4858 | 25% | 3.7% | +47.3% | -25.0% | -6.72% | 100% |
| dip40_V2_gescreend_pass | 471 | 17% | 2.5% | +46.2% | -19.8% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 4063 | 25% | 4.1% | +55.5% | -27.8% | -7.01% | 100% |
| dip40_V2_alle | 4815 | 24% | 4.3% | +54.0% | -27.4% | -7.85% | 100% |
| dip40_V3_gescreend_pass | 474 | 8% | 2.7% | +294.2% | -21.1% | +2.87% | 100% |
| dip40_V3_gescreend_fail | 4144 | 13% | 5.6% | +111.2% | -29.3% | -10.80% | 100% |
| dip40_V3_alle | 4868 | 13% | 5.6% | +116.8% | -28.8% | -10.28% | 100% |
| dip45_V1_gescreend_pass | 455 | 15% | 2.0% | +48.7% | -15.8% | -6.28% | 100% |
| dip45_V1_gescreend_fail | 3969 | 27% | 3.3% | +48.3% | -25.4% | -5.22% | 100% |
| dip45_V1_alle | 4704 | 26% | 3.3% | +48.7% | -24.7% | -5.55% | 100% |
| dip45_V2_gescreend_pass | 452 | 19% | 2.4% | +43.3% | -19.8% | -7.90% | 100% |
| dip45_V2_gescreend_fail | 3976 | 25% | 3.8% | +58.3% | -27.4% | -5.75% | 100% |
| dip45_V2_alle | 4663 | 24% | 3.9% | +57.1% | -27.0% | -6.50% | 100% |
| dip45_V3_gescreend_pass | 455 | 7% | 2.4% | +352.6% | -20.5% | +6.56% | 100% |
| dip45_V3_gescreend_fail | 4042 | 14% | 5.3% | +116.3% | -28.9% | -8.70% | 100% |
| dip45_V3_alle | 4706 | 13% | 5.3% | +124.9% | -28.3% | -8.05% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 394 | 15% | 5.6% | -9.69% | -12.8% tot -6.6% | -14.6% | – | 100% |
| per_token_zonder_xlink | 112 | 19% | 0.0% | +20.98% | -14.9% tot +56.8% | -13.3% | 131% | 54% |
| gepoold_met_xlink | 3307 | 13% | 3.2% | -10.31% | -11.7% tot -9.0% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 978 | 18% | 0.0% | +20.19% | +0.2% tot +40.1% | -14.6% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 09:21:38 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:21:38,312 main INFO screen MCX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.9s)
Sep 12 09:21:40 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:21:40,454 main INFO screen WALLY pass=0 dev=0.36 ins=47.11 pro=15 1a=True 1b=True 2=True (25.1s)
Sep 12 09:22:33 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:22:33,609 main INFO screen att pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 12 09:23:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:23:26,581 main INFO screen SHIA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 12 09:24:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:24:03,966 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:24:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:24:09,034 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:24:31 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:24:31,013 main INFO screen FTFS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.1s)
Sep 12 09:24:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:24:39,167 main INFO screen Athena pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 12 09:25:06 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:06,287 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:25:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:11,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:25:32 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:32,189 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 12 09:25:56 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:56,664 main INFO screen Usdtd pass=0 dev=0.63 ins=0.0 pro=1 1a=False 1b=False 2=False (8.4s)
Sep 12 09:25:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:58,012 main INFO screen BEARFROG pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (7.1s)
Sep 12 09:25:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:25:58,078 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:26:01 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:01,378 main INFO screen vrl pass=0 dev=0.23 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 12 09:26:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:02,646 main INFO screen LOKI pass=0 dev=0.0 ins=20.47 pro=47 1a=False 1b=False 2=True (6.0s)
Sep 12 09:26:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:03,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:26:17 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:17,121 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:26:17 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 09:26:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:22,036 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.0s)
Sep 12 09:26:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:29,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:26:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:34,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:26:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:51,826 main INFO screen FLYSTONKS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (22.4s)
Sep 12 09:26:56 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:26:56,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:27:01 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:27:01,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:27:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:27:20,270 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.6s)
Sep 12 09:27:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:27:48,575 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:27:53 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:27:53,651 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:28:16 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:28:16,689 main INFO screen DOGEIUS pass=0 dev=0.0 ins=18.12 pro=53 1a=False 1b=False 2=True (28.2s)
Sep 12 09:28:19 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:28:19,181 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:28:30 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:28:30,289 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.2s)
Sep 12 09:29:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:29:18,773 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.2s)
Sep 12 09:29:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:29:22,365 main INFO screen Cash dog pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.1s)
Sep 12 09:29:33 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:29:33,926 main INFO screen EVILGABEN pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 09:30:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:30:09,595 main INFO screen BetOnBlak pass=0 dev=0.69 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 12 09:30:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:30:20,648 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:30:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:30:34,172 main INFO screen FOFO pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (13.6s)
Sep 12 09:31:17 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:31:17,986 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:31:19 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:31:19,782 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:31:19 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 09:31:30 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:31:30,208 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.3s)
Sep 12 09:33:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:33:10,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:33:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:33:15,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:33:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:33:29,591 main INFO screen Grok pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=True 2=True (19.3s)
Sep 12 09:36:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:36:37,110 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:36:37 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 09:37:13 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:13,470 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:37:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:20,770 main INFO screen fuckumay pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 12 09:37:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:23,624 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:37:28 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:28,679 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:37:42 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:42,552 main INFO screen PepeCoin pass=0 dev=0.0 ins=15.45 pro=32 1a=False 1b=True 2=True (2.4s)
Sep 12 09:37:44 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:44,358 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:37:46 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:46,715 main INFO screen $MWM pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 12 09:37:47 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:47,037 main INFO screen USDF pass=0 dev=0.35 ins=38.59 pro=11 1a=False 1b=False 2=True (23.5s)
Sep 12 09:37:49 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:37:49,425 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:38:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:03,056 main INFO screen BLACKPEARL pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (19.3s)
Sep 12 09:38:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:18,821 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:38:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:23,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:38:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:37,151 main INFO screen flynsem pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=True 2=True (18.4s)
Sep 12 09:38:54 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:54,125 main INFO screen ANXIETYDOG pass=1 dev=0.0 ins=14.18 pro=10 1a=False 1b=False 2=False (1.6s)
Sep 12 09:38:59 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:38:59,367 main INFO screen BetOnBlak pass=0 dev=0.86 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 12 09:39:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:15,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:39:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:20,981 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:39:21 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:21,981 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:39:27 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:27,016 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:39:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:35,383 main INFO screen $MWM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.5s)
Sep 12 09:39:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:43,744 main INFO screen pif pass=0 dev=0.0 ins=49.44 pro=27 1a=True 1b=False 2=True (21.8s)
Sep 12 09:39:44 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:44,361 main INFO screen MOSQUITO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 12 09:39:55 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:39:55,264 main INFO screen HALH pass=0 dev=0.59 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 09:41:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:41:48,168 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:41:48 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 09:41:50 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:41:50,868 main INFO screen wind pass=0 dev=0.54 ins=0.0 pro=4 1a=False 1b=False 2=False (4.0s)
Sep 12 09:42:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:42:35,276 main INFO screen Maple pass=1 dev=0.0 ins=12.01 pro=41 1a=False 1b=False 2=False (3.4s)
Sep 12 09:42:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:42:35,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:42:40 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:42:40,697 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:42:42 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:42:42,498 main INFO screen EVILDOGE pass=0 dev=37.73 ins=0.15 pro=5 1a=False 1b=False 2=True (2.9s)
Sep 12 09:42:56 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:42:56,530 main INFO screen Maple pass=0 dev=0.0 ins=48.83 pro=55 1a=True 1b=True 2=True (21.1s)
Sep 12 09:44:46 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:44:46,009 main INFO screen PUDU DOG pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 12 09:45:04 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:45:04,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:45:08 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:45:08,290 main INFO screen Kikutaro pass=1 dev=0.0 ins=12.41 pro=31 1a=False 1b=False 2=False (3.7s)
Sep 12 09:45:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:45:11,829 main INFO screen LMAO pass=0 dev=0.85 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 09:45:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:45:22,653 main INFO screen Yarl pass=0 dev=0.0 ins=19.47 pro=39 1a=False 1b=False 2=True (1.2s)
Sep 12 09:46:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:46:48,439 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 12 09:47:05 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:47:05,277 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:47:05 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T08:18:16Z
--- update 2026-09-12T08:23:36Z
--- update 2026-09-12T08:29:17Z
--- update 2026-09-12T08:34:23Z
--- update 2026-09-12T08:39:30Z
--- update 2026-09-12T08:44:36Z
--- update 2026-09-12T08:49:42Z
--- update 2026-09-12T08:54:47Z
--- update 2026-09-12T08:59:47Z
--- update 2026-09-12T09:04:48Z
--- update 2026-09-12T09:10:27Z
--- update 2026-09-12T09:15:33Z
--- update 2026-09-12T09:20:36Z
--- update 2026-09-12T09:26:16Z
--- update 2026-09-12T09:31:18Z
--- update 2026-09-12T09:36:36Z
--- update 2026-09-12T09:41:47Z
--- update 2026-09-12T09:47:04Z
Running as unit: schaduwbot-wallets.service; invocation ID: 59ae4466605a4369ba7d98991ca62d2e
analyses gestart (571ea883d7b8)
```

## Analyses (laatste 25 regels)
```
active
07:53:00 klaar (551 rpc-calls, 0 fouten)
07:53:02 klaar in 2s: 16508 tokens, 34 nieuw -> /opt/schaduwbot/reports/video_replay.md
07:53:03 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 07:53 UTC
07:53:03 51130 tokens geladen
07:53:06   2000 tokens, 247228 trades, 51459 posities (3s)
07:53:08   4000 tokens, 500285 trades, 104134 posities (6s)
07:53:11   6000 tokens, 746680 trades, 151104 posities (8s)
07:53:13   8000 tokens, 997175 trades, 201671 posities (11s)
07:53:16   10000 tokens, 1260038 trades, 252158 posities (13s)
07:53:19   12000 tokens, 1529500 trades, 309045 posities (16s)
07:53:22   14000 tokens, 1773567 trades, 350771 posities (19s)
07:53:25   16000 tokens, 2034820 trades, 404904 posities (22s)
07:53:28   18000 tokens, 2304063 trades, 461465 posities (25s)
07:53:30   20000 tokens, 2547338 trades, 506874 posities (27s)
07:53:33   22000 tokens, 2801778 trades, 554566 posities (30s)
07:53:35   24000 tokens, 3028677 trades, 599750 posities (32s)
07:53:37   26000 tokens, 3291798 trades, 649697 posities (35s)
07:53:41   28000 tokens, 3560897 trades, 714082 posities (38s)
07:53:41 posities: 733209 uit 3641470 trades (39s)
07:53:52 159725 wallets gerekend
07:53:52 geluk-toets
07:54:30 persistentie
07:54:32 kopieer-simulatie
07:54:44 klaar in 102s -> /opt/schaduwbot/reports/wallets.md
09:47:05 27856 tokens sinds start volledige logging, waarvan 6835 met een gat door herstart
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
