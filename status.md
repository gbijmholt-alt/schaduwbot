# Schaduwbot status

- tijd: 2026-09-12 17:52:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 4 hours, 5 minutes
- bot-service: active
- code-versie: e364fd9
- schijf: 3.8G/38G | geheugen: 561/3814 MB

## Health
```json
{"ok": false, "last_event_age_s": 1326.7, "uptime_s": 2187, "tokens_in_memory": 434, "msgs": 160742, "trades": 24230, "creates": 434, "decode_fail": 3289, "rpc_calls": 470, "rpc_errors": 15, "sol_usd": 102.04092456366078, "open_positions": 0, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 17832 | 2481 | 14 | 2481 | 180 | 4374 | 13076 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 576 | 16% | 1.7% | +43.6% | -16.0% | -6.21% | 100% |
| dip35_V1_gescreend_fail | 4617 | 27% | 3.9% | +45.4% | -26.1% | -6.71% | 100% |
| dip35_V1_alle | 5739 | 26% | 4.1% | +44.6% | -25.5% | -6.96% | 100% |
| dip35_V2_gescreend_pass | 573 | 22% | 2.4% | +40.8% | -20.3% | -6.66% | 100% |
| dip35_V2_gescreend_fail | 4670 | 25% | 4.4% | +54.9% | -28.1% | -7.03% | 100% |
| dip35_V2_alle | 5699 | 25% | 4.6% | +52.2% | -27.8% | -7.92% | 100% |
| dip35_V3_gescreend_pass | 574 | 9% | 3.0% | +266.5% | -22.1% | +4.05% | 100% |
| dip35_V3_gescreend_fail | 4770 | 14% | 6.1% | +111.1% | -29.8% | -10.74% | 100% |
| dip35_V3_alle | 5751 | 13% | 6.2% | +115.0% | -29.4% | -10.35% | 100% |
| dip40_V1_gescreend_pass | 544 | 14% | 1.8% | +45.4% | -15.5% | -6.92% | 100% |
| dip40_V1_gescreend_fail | 4536 | 26% | 3.9% | +46.8% | -26.0% | -6.63% | 100% |
| dip40_V1_alle | 5512 | 26% | 4.0% | +46.7% | -25.3% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 542 | 17% | 2.2% | +43.6% | -19.5% | -8.51% | 100% |
| dip40_V2_gescreend_fail | 4562 | 25% | 4.3% | +54.7% | -28.1% | -7.08% | 100% |
| dip40_V2_alle | 5466 | 24% | 4.5% | +52.7% | -27.6% | -8.15% | 100% |
| dip40_V3_gescreend_pass | 544 | 8% | 2.6% | +265.1% | -21.0% | +1.62% | 100% |
| dip40_V3_gescreend_fail | 4650 | 13% | 5.9% | +106.0% | -29.6% | -11.78% | 100% |
| dip40_V3_alle | 5519 | 13% | 5.9% | +110.4% | -29.1% | -11.40% | 100% |
| dip45_V1_gescreend_pass | 521 | 15% | 1.7% | +47.5% | -15.4% | -6.20% | 100% |
| dip45_V1_gescreend_fail | 4447 | 28% | 3.6% | +48.2% | -25.8% | -5.46% | 100% |
| dip45_V1_alle | 5330 | 26% | 3.6% | +48.2% | -25.0% | -5.89% | 100% |
| dip45_V2_gescreend_pass | 518 | 18% | 2.1% | +42.7% | -19.5% | -8.08% | 100% |
| dip45_V2_gescreend_fail | 4462 | 25% | 4.1% | +57.4% | -27.8% | -6.15% | 100% |
| dip45_V2_alle | 5286 | 24% | 4.1% | +55.9% | -27.3% | -7.07% | 100% |
| dip45_V3_gescreend_pass | 521 | 8% | 2.1% | +303.1% | -20.3% | +5.13% | 100% |
| dip45_V3_gescreend_fail | 4534 | 14% | 5.6% | +111.2% | -29.2% | -9.90% | 100% |
| dip45_V3_alle | 5330 | 13% | 5.5% | +118.0% | -28.6% | -9.35% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 450 | 15% | 5.1% | -9.18% | -12.0% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3794 | 13% | 2.8% | -9.75% | -11.0% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 17:16:48 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:16:48,382 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.5s)
Sep 12 17:17:22 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:17:22,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:17:30 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:17:30,642 main INFO screen MIM pass=1 dev=0.0 ins=6.63 pro=37 1a=False 1b=False 2=False (8.3s)
Sep 12 17:17:48 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:17:48,588 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:17:17:48 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 17:17:48 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:17:48,613 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:17:17:48 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 12 17:18:08 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:08,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:18:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:13,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:18:26 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:26,226 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:18:29 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:29,421 main INFO screen LMAO pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 12 17:18:29 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:29,858 main INFO screen neet pass=0 dev=0.0 ins=29.47 pro=59 1a=False 1b=False 2=True (21.3s)
Sep 12 17:18:31 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:31,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:18:50 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:18:50,928 main INFO screen faudoge pass=0 dev=0.53 ins=52.08 pro=7 1a=False 1b=True 2=True (24.9s)
Sep 12 17:19:26 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:19:26,111 main INFO screen DOOB pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (9.4s)
Sep 12 17:19:26 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:19:26,325 main INFO screen SHODL pass=0 dev=0.0 ins=18.13 pro=41 1a=False 1b=False 2=True (7.8s)
Sep 12 17:19:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:19:42,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:19:54 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:19:54,359 main INFO screen AIGOLD pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (11.5s)
Sep 12 17:20:50 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:20:50,619 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:20:50 +0000] "GET /health HTTP/1.1" 200 490 "-" "Python-urllib/3.14"
Sep 12 17:21:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:21:43,461 main INFO screen USEFUL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 12 17:22:05 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:05,640 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:22:09 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:09,143 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:22:10 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:10,714 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:22:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:14,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:22:24 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:24,959 main INFO screen RTW pass=0 dev=3.43 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 12 17:22:27 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:27,975 main INFO screen MSQTBRN  pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (22.4s)
Sep 12 17:22:35 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:35,279 main INFO screen COCA COLA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.2s)
Sep 12 17:22:48 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:22:48,711 main INFO screen godcha pass=0 dev=8.95 ins=29.15 pro=8 1a=False 1b=False 2=False (6.6s)
Sep 12 17:23:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:23:13,655 main INFO screen x pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (1.6s)
Sep 12 17:23:57 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:23:57,629 main INFO screen BALL pass=0 dev=0.45 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 12 17:24:20 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:24:20,411 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:24:25 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:24:25,441 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:24:47 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:24:47,220 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.9s)
Sep 12 17:25:02 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:25:02,957 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 12 17:25:31 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:25:31,280 main INFO screen SMACK pass=0 dev=6.64 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 12 17:26:01 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:26:01,929 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:26:01 +0000] "GET /health HTTP/1.1" 200 493 "-" "Python-urllib/3.14"
Sep 12 17:27:15 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:27:15,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:27:25 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:27:25,604 main INFO screen BALLOON pass=0 dev=0.0 ins=6.63 pro=42 1a=False 1b=False 2=True (4.7s)
Sep 12 17:27:28 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:27:28,637 main INFO screen DOOROC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (13.7s)
Sep 12 17:28:46 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:28:46,078 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:28:51 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:28:51,184 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:28:55 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:28:55,501 main INFO screen morro pass=0 dev=7.0 ins=26.95 pro=11 1a=False 1b=False 2=False (6.6s)
Sep 12 17:29:08 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:29:08,991 main INFO screen faufone pass=0 dev=0.36 ins=50.34 pro=10 1a=False 1b=False 2=True (23.0s)
Sep 12 17:30:03 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:03,265 main INFO screen DURKCAT pass=0 dev=6.63 ins=0.0 pro=1 1a=False 1b=False 2=False (10.8s)
Sep 12 17:30:03 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:03,703 main INFO screen Pumployed pass=1 dev=0.0 ins=0.35 pro=45 1a=False 1b=False 2=False (9.4s)
Sep 12 17:30:09 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:09,232 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 1s
Sep 12 17:30:10 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:10,309 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 2s
Sep 12 17:30:12 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:12,382 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 4s
Sep 12 17:30:16 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:16,461 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 8s
Sep 12 17:30:24 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:24,549 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 16s
Sep 12 17:30:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:30:40,633 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 32s
Sep 12 17:31:12 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:31:12,716 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:31:20 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:31:20,803 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:31:20 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 12 17:32:12 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:32:12,804 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:33:12 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:33:12,892 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:34:12 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:34:12,992 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:35:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:35:13,066 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:36:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:36:13,172 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:36:37 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:36:37,204 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:36:37 +0000] "GET /health HTTP/1.1" 503 514 "-" "Python-urllib/3.14"
Sep 12 17:37:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:37:13,280 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:38:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:38:13,399 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:39:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:39:13,468 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:40:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:40:13,541 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:41:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:41:13,622 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:41:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:41:39,625 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:41:39 +0000] "GET /health HTTP/1.1" 503 514 "-" "Python-urllib/3.14"
Sep 12 17:42:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:42:13,710 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:43:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:43:13,794 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:44:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:44:13,882 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:45:13 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:45:13,970 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:46:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:46:14,051 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:47:07 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:47:07,221 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:47:07 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 17:47:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:47:14,138 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:48:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:48:14,225 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:49:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:49:14,316 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:50:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:50:14,401 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:51:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:51:14,520 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:51:37 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:51:37,158 aiohttp.access INFO 77.239.124.104 [12/Sep/2026:17:51:37 +0000] "GET /login HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Edg/132.0.0.0"
Sep 12 17:51:37 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:51:37,301 aiohttp.access INFO 77.239.124.104 [12/Sep/2026:17:51:37 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
Sep 12 17:51:37 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:51:37,635 aiohttp.access INFO 77.239.124.104 [12/Sep/2026:17:51:37 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 17:51:37 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:51:37,791 aiohttp.access INFO 77.239.124.104 [12/Sep/2026:17:51:37 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 17:52:14 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:52:14,600 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 17:52:15 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 17:52:15,841 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:52:15 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T17:00:34Z
--- update 2026-09-12T17:05:36Z
nieuwe code: 8d4b88e
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 4382a0e1c14a4f7986ac753e7d367fa4
analyses gestart (4ee13da033ab)
--- update 2026-09-12T17:10:37Z
--- update 2026-09-12T17:15:43Z
nieuwe code: e364fd9
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T17:20:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: 0c873533369e446096672962d9fecab8
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T17:26:00Z
--- update 2026-09-12T17:31:19Z
--- update 2026-09-12T17:36:36Z
--- update 2026-09-12T17:41:38Z
--- update 2026-09-12T17:47:06Z
--- update 2026-09-12T17:52:14Z
```

## Analyses (laatste 25 regels)
```
inactive
17:31:02   2000 tokens, 234531 trades, 43728 posities (2s)
17:31:05   4000 tokens, 469930 trades, 86030 posities (5s)
17:31:06   6000 tokens, 686745 trades, 126162 posities (6s)
17:31:09   8000 tokens, 912039 trades, 165110 posities (9s)
17:31:10   10000 tokens, 1134949 trades, 207013 posities (11s)
17:31:12   12000 tokens, 1363173 trades, 244092 posities (13s)
17:31:15   14000 tokens, 1629244 trades, 297867 posities (15s)
17:31:17   16000 tokens, 1861152 trades, 340904 posities (17s)
17:31:19   18000 tokens, 2080015 trades, 376103 posities (19s)
17:31:21   20000 tokens, 2329827 trades, 420414 posities (21s)
17:31:23   22000 tokens, 2553211 trades, 460401 posities (23s)
17:31:25   24000 tokens, 2796749 trades, 506835 posities (25s)
17:31:27   26000 tokens, 3030508 trades, 549163 posities (27s)
17:31:29   28000 tokens, 3260600 trades, 588722 posities (29s)
17:31:31   30000 tokens, 3497390 trades, 631312 posities (31s)
17:31:33   32000 tokens, 3708145 trades, 669692 posities (33s)
17:31:35   34000 tokens, 3939276 trades, 712847 posities (35s)
17:31:37   36000 tokens, 4195644 trades, 763072 posities (37s)
17:31:39   38000 tokens, 4428707 trades, 815767 posities (39s)
17:31:40 posities: 836053 uit 4520254 trades (40s)
17:31:50 174384 wallets gerekend
17:31:51 geluk-toets
17:32:23 persistentie
17:32:25 kopieer-simulatie
17:32:37 klaar in 97s -> /opt/schaduwbot/reports/wallets.md
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
