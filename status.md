# Schaduwbot status

- tijd: 2026-09-12 12:57:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 23 hours, 10 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.6G/38G | geheugen: 633/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 11116, "tokens_in_memory": 2482, "msgs": 910148, "trades": 247636, "creates": 2482, "decode_fail": 10797, "rpc_calls": 7491, "rpc_errors": 347, "sol_usd": 101.94022714307955, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 11622 | 1804 | 10 | 1804 | 132 | 3143 | 9403 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 534 | 16% | 1.9% | +43.9% | -16.4% | -6.44% | 100% |
| dip35_V1_gescreend_fail | 4299 | 27% | 3.8% | +45.5% | -25.9% | -6.59% | 100% |
| dip35_V1_alle | 5312 | 26% | 4.0% | +44.8% | -25.3% | -6.81% | 100% |
| dip35_V2_gescreend_pass | 530 | 23% | 2.6% | +41.9% | -20.9% | -6.65% | 100% |
| dip35_V2_gescreend_fail | 4340 | 25% | 4.3% | +55.7% | -27.9% | -6.87% | 100% |
| dip35_V2_alle | 5269 | 25% | 4.6% | +53.0% | -27.7% | -7.68% | 100% |
| dip35_V3_gescreend_pass | 532 | 9% | 3.0% | +274.0% | -22.2% | +5.04% | 100% |
| dip35_V3_gescreend_fail | 4436 | 14% | 6.0% | +114.3% | -29.6% | -10.15% | 100% |
| dip35_V3_alle | 5324 | 13% | 6.0% | +118.4% | -29.2% | -9.66% | 100% |
| dip40_V1_gescreend_pass | 502 | 14% | 2.0% | +46.0% | -15.7% | -6.87% | 100% |
| dip40_V1_gescreend_fail | 4230 | 26% | 3.8% | +47.1% | -25.7% | -6.53% | 100% |
| dip40_V1_alle | 5105 | 25% | 3.9% | +47.1% | -25.1% | -6.74% | 100% |
| dip40_V2_gescreend_pass | 499 | 18% | 2.4% | +45.1% | -19.8% | -8.26% | 100% |
| dip40_V2_gescreend_fail | 4247 | 25% | 4.2% | +55.3% | -27.9% | -7.01% | 100% |
| dip40_V2_alle | 5058 | 24% | 4.4% | +53.5% | -27.5% | -7.92% | 100% |
| dip40_V3_gescreend_pass | 502 | 8% | 2.6% | +271.2% | -21.1% | +2.73% | 100% |
| dip40_V3_gescreend_fail | 4331 | 13% | 5.8% | +108.3% | -29.4% | -11.22% | 100% |
| dip40_V3_alle | 5112 | 13% | 5.8% | +113.2% | -29.0% | -10.71% | 100% |
| dip45_V1_gescreend_pass | 482 | 15% | 1.9% | +47.7% | -15.6% | -6.30% | 100% |
| dip45_V1_gescreend_fail | 4146 | 27% | 3.4% | +48.4% | -25.5% | -5.22% | 100% |
| dip45_V1_alle | 4942 | 26% | 3.4% | +48.6% | -24.8% | -5.59% | 100% |
| dip45_V2_gescreend_pass | 478 | 19% | 2.3% | +43.1% | -19.8% | -7.94% | 100% |
| dip45_V2_gescreend_fail | 4153 | 25% | 3.9% | +57.9% | -27.5% | -5.80% | 100% |
| dip45_V2_alle | 4896 | 24% | 4.0% | +56.5% | -27.1% | -6.63% | 100% |
| dip45_V3_gescreend_pass | 482 | 8% | 2.3% | +317.5% | -20.6% | +6.07% | 100% |
| dip45_V3_gescreend_fail | 4222 | 14% | 5.4% | +113.4% | -28.9% | -9.07% | 100% |
| dip45_V3_alle | 4941 | 13% | 5.4% | +120.8% | -28.4% | -8.46% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 417 | 15% | 5.3% | -9.36% | -12.3% tot -6.4% | -14.6% | – | 100% |
| per_token_zonder_xlink | 120 | 22% | 0.0% | +20.87% | -12.6% tot +54.4% | -13.2% | 123% | 54% |
| gepoold_met_xlink | 3500 | 13% | 3.0% | -10.00% | -11.3% tot -8.7% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1041 | 19% | 0.0% | +19.81% | +1.0% tot +38.6% | -14.0% | 67% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 12:41:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:17,308 main INFO screen CBRAIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.8s)
Sep 12 12:41:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:37,103 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:41:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 12:41:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:49,483 main INFO screen SOL pass=0 dev=0.14 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 12 12:42:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:46,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:42:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:49,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:42:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:52,995 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.5s)
Sep 12 12:42:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:54,348 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:07,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:07,674 main INFO screen SHIBAGO pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.4s)
Sep 12 12:43:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:12,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:25,795 main INFO screen bulesh pass=0 dev=0.07 ins=79.24 pro=8 1a=False 1b=True 2=True (19.1s)
Sep 12 12:43:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:29,585 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 12:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:01,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:01,334 main INFO screen MONOPOLY pass=0 dev=0.0 ins=10.94 pro=34 1a=False 1b=False 2=True (3.7s)
Sep 12 12:44:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:06,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:19,775 main INFO screen FERSPE pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (18.6s)
Sep 12 12:44:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:40,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:45,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:45:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:45:13,148 main INFO screen LARPTOP pass=0 dev=0.0 ins=71.67 pro=67 1a=False 1b=False 2=True (32.7s)
Sep 12 12:45:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:45:19,431 aiohttp.access INFO 94.154.43.223 [12/Sep/2026:12:45:19 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 12 12:46:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:30,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:46:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:39,115 main INFO screen DEGENFLY pass=1 dev=0.0 ins=7.86 pro=57 1a=False 1b=False 2=False (9.2s)
Sep 12 12:46:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:56,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:47:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:01,182 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:47:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:05,154 main INFO screen TAL pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (3.8s)
Sep 12 12:47:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:06,661 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:47:06 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 12:47:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:18,483 main INFO screen BetOnBlak pass=0 dev=0.91 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 12:47:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:18,663 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.23 pro=11 1a=False 1b=False 2=True (22.7s)
Sep 12 12:47:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:29,125 main INFO screen duckdegen pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 12 12:48:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:48:06,463 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:12:48:06 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 12:48:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:48:06,487 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:12:48:06 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 12 12:48:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:48:23,349 main INFO screen INSANE pass=1 dev=2.09 ins=12.87 pro=56 1a=False 1b=False 2=False (3.8s)
Sep 12 12:49:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:49:38,371 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:49:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:49:46,745 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.71 pro=10 1a=False 1b=False 2=True (8.4s)
Sep 12 12:51:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:27,658 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (2.2s)
Sep 12 12:51:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:28,464 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:51:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:32,794 main INFO screen RICK pass=0 dev=1.66 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 12 12:51:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:36,233 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=14 1a=False 1b=False 2=True (7.8s)
Sep 12 12:51:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:51,248 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:51:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:51:56,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:52:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:52:10,764 main INFO screen $2CB pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (4.0s)
Sep 12 12:52:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:52:11,913 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (20.7s)
Sep 12 12:52:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:52:11,981 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:52:11 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 12 12:53:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:07,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:53:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:12,388 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:53:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:25,677 main INFO screen LAPTOP pass=0 dev=0.0 ins=79.27 pro=6 1a=False 1b=True 2=True (18.5s)
Sep 12 12:53:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:42,822 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:53:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:45,041 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 12 12:53:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:53:50,577 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=13 1a=True 1b=True 2=True (8.3s)
Sep 12 12:54:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:22,859 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:54:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:26,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:54:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:27,933 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:54:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:31,089 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:54:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:43,967 main INFO screen $CAJUN pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 12 12:54:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:46,152 main INFO screen fapfap pass=0 dev=0.49 ins=0.0 pro=6 1a=False 1b=False 2=False (23.4s)
Sep 12 12:54:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:54:48,045 main INFO screen DCN pass=0 dev=0.0 ins=10.16 pro=73 1a=False 1b=False 2=True (22.1s)
Sep 12 12:55:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:27,844 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:27,953 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:29,811 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:32,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:33,046 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:34,883 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:55:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:51,539 main INFO screen DCN pass=1 dev=0.0 ins=13.46 pro=18 1a=False 1b=False 2=False (23.8s)
Sep 12 12:55:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:51,874 main INFO screen DCN pass=0 dev=0.0 ins=15.33 pro=24 1a=False 1b=True 2=True (24.0s)
Sep 12 12:55:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:55:52,165 main INFO screen WALLY pass=0 dev=0.36 ins=47.45 pro=21 1a=False 1b=False 2=True (22.4s)
Sep 12 12:56:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:00,184 main INFO screen Mormonism pass=0 dev=0.0 ins=27.5 pro=12 1a=False 1b=False 2=False (8.6s)
Sep 12 12:56:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:00,455 main INFO screen DCN pass=0 dev=11.77 ins=18.85 pro=33 1a=False 1b=False 2=False (8.6s)
Sep 12 12:56:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:08,549 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:56:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:10,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:56:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:13,620 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:56:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:19,211 main INFO screen GOLD pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (9.2s)
Sep 12 12:56:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:20,908 main INFO screen Rufus pass=1 dev=0.44 ins=0.02 pro=33 1a=False 1b=False 2=False (4.1s)
Sep 12 12:56:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:30,980 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.67 pro=28 1a=False 1b=False 2=True (22.5s)
Sep 12 12:56:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:31,822 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:56:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:32,259 main INFO screen Silversem pass=1 dev=3.43 ins=3.57 pro=30 1a=False 1b=False 2=False (6.0s)
Sep 12 12:56:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:36,891 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:56:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:56:50,815 main INFO screen EMBER pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=True 2=True (19.4s)
Sep 12 12:57:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:57:16,742 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:57:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:57:25,551 main INFO screen dedu pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=True (9.0s)
Sep 12 12:57:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:57:37,133 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:57:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T11:27:19Z
--- update 2026-09-12T11:32:19Z
--- update 2026-09-12T11:37:36Z
--- update 2026-09-12T11:43:20Z
--- update 2026-09-12T11:48:20Z
--- update 2026-09-12T11:53:36Z
--- update 2026-09-12T11:59:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 67d32d30228c414781697fb76280fa59
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T12:04:33Z
--- update 2026-09-12T12:09:34Z
--- update 2026-09-12T12:14:36Z
--- update 2026-09-12T12:20:11Z
--- update 2026-09-12T12:25:36Z
--- update 2026-09-12T12:31:17Z
--- update 2026-09-12T12:36:23Z
--- update 2026-09-12T12:41:36Z
--- update 2026-09-12T12:47:05Z
--- update 2026-09-12T12:52:10Z
--- update 2026-09-12T12:57:36Z
```

## Analyses (laatste 25 regels)
```
inactive
12:08:37 klaar (851 rpc-calls, 13 fouten)
12:08:39 klaar in 2s: 16626 tokens, 144 nieuw -> /opt/schaduwbot/reports/video_replay.md
12:08:39 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 12:08 UTC
12:08:40 54535 tokens geladen
12:08:42   2000 tokens, 250045 trades, 51008 posities (2s)
12:08:44   4000 tokens, 496319 trades, 99458 posities (5s)
12:08:47   6000 tokens, 732039 trades, 144482 posities (7s)
12:08:49   8000 tokens, 966346 trades, 188464 posities (9s)
12:08:51   10000 tokens, 1209956 trades, 232898 posities (12s)
12:08:54   12000 tokens, 1492659 trades, 295155 posities (14s)
12:08:56   14000 tokens, 1728094 trades, 337299 posities (17s)
12:08:59   16000 tokens, 1980589 trades, 384171 posities (19s)
12:09:02   18000 tokens, 2223133 trades, 430721 posities (22s)
12:09:04   20000 tokens, 2484878 trades, 484120 posities (25s)
12:09:07   22000 tokens, 2725661 trades, 529712 posities (27s)
12:09:09   24000 tokens, 2971988 trades, 575609 posities (29s)
12:09:11   26000 tokens, 3193304 trades, 615760 posities (31s)
12:09:13   28000 tokens, 3442466 trades, 664641 posities (33s)
12:09:16   30000 tokens, 3709953 trades, 717663 posities (36s)
12:09:18 posities: 773628 uit 3942433 trades (39s)
12:09:29 164863 wallets gerekend
12:09:29 geluk-toets
12:10:06 persistentie
12:10:08 kopieer-simulatie
12:10:21 klaar in 102s -> /opt/schaduwbot/reports/wallets.md
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
