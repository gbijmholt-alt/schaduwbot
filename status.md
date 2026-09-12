# Schaduwbot status

- tijd: 2026-09-12 10:50:24 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 21 hours, 3 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.5G/38G | geheugen: 569/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 3484, "tokens_in_memory": 752, "msgs": 233298, "trades": 67851, "creates": 752, "decode_fail": 2611, "rpc_calls": 2071, "rpc_errors": 84, "sol_usd": 102.01351983121758, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 9229 | 1453 | 6 | 1453 | 96 | 2547 | 7662 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 505 | 16% | 2.0% | +44.2% | -16.6% | -6.84% | 100% |
| dip35_V1_gescreend_fail | 4166 | 27% | 3.8% | +45.6% | -25.8% | -6.59% | 100% |
| dip35_V1_alle | 5110 | 26% | 3.9% | +44.9% | -25.3% | -6.89% | 100% |
| dip35_V2_gescreend_pass | 502 | 21% | 2.8% | +42.9% | -20.9% | -7.40% | 100% |
| dip35_V2_gescreend_fail | 4201 | 25% | 4.3% | +55.9% | -27.9% | -6.94% | 100% |
| dip35_V2_alle | 5073 | 24% | 4.6% | +53.4% | -27.6% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 503 | 8% | 3.2% | +297.3% | -22.3% | +4.39% | 100% |
| dip35_V3_gescreend_fail | 4290 | 13% | 5.9% | +116.4% | -29.6% | -10.09% | 100% |
| dip35_V3_alle | 5123 | 13% | 6.0% | +120.7% | -29.2% | -9.65% | 100% |
| dip40_V1_gescreend_pass | 475 | 14% | 2.1% | +46.9% | -16.0% | -6.97% | 100% |
| dip40_V1_gescreend_fail | 4095 | 26% | 3.7% | +47.2% | -25.7% | -6.51% | 100% |
| dip40_V1_alle | 4910 | 25% | 3.8% | +47.3% | -25.1% | -6.75% | 100% |
| dip40_V2_gescreend_pass | 473 | 17% | 2.5% | +45.9% | -19.8% | -8.41% | 100% |
| dip40_V2_gescreend_fail | 4108 | 25% | 4.2% | +55.3% | -27.8% | -7.05% | 100% |
| dip40_V2_alle | 4868 | 24% | 4.4% | +53.8% | -27.4% | -7.93% | 100% |
| dip40_V3_gescreend_pass | 475 | 8% | 2.7% | +294.2% | -21.1% | +2.81% | 100% |
| dip40_V3_gescreend_fail | 4187 | 13% | 5.7% | +110.4% | -29.4% | -10.99% | 100% |
| dip40_V3_alle | 4918 | 13% | 5.8% | +116.1% | -28.9% | -10.51% | 100% |
| dip45_V1_gescreend_pass | 456 | 15% | 2.0% | +48.7% | -15.8% | -6.31% | 100% |
| dip45_V1_gescreend_fail | 4011 | 27% | 3.3% | +48.4% | -25.4% | -5.21% | 100% |
| dip45_V1_alle | 4752 | 26% | 3.4% | +48.8% | -24.7% | -5.60% | 100% |
| dip45_V2_gescreend_pass | 453 | 19% | 2.4% | +43.3% | -19.8% | -7.94% | 100% |
| dip45_V2_gescreend_fail | 4018 | 25% | 3.8% | +58.1% | -27.4% | -5.84% | 100% |
| dip45_V2_alle | 4711 | 24% | 4.0% | +56.9% | -27.0% | -6.62% | 100% |
| dip45_V3_gescreend_pass | 456 | 7% | 2.4% | +352.6% | -20.5% | +6.50% | 100% |
| dip45_V3_gescreend_fail | 4083 | 14% | 5.4% | +115.4% | -28.9% | -8.86% | 100% |
| dip45_V3_alle | 4753 | 13% | 5.4% | +124.1% | -28.4% | -8.25% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 396 | 15% | 5.6% | -9.61% | -12.7% tot -6.6% | -14.6% | – | 100% |
| per_token_zonder_xlink | 112 | 19% | 0.0% | +20.98% | -14.9% tot +56.8% | -13.3% | 131% | 54% |
| gepoold_met_xlink | 3320 | 13% | 3.2% | -10.29% | -11.6% tot -9.0% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 978 | 18% | 0.0% | +20.19% | +0.2% tot +40.1% | -14.6% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 10:28:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:28:34,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:28:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:28:48,300 main INFO screen fg pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (14.2s)
Sep 12 10:29:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:21,905 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:29:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:23,155 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:29:23 +0000] "GET /health HTTP/1.1" 200 496 "-" "Python-urllib/3.14"
Sep 12 10:29:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:27,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:29:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:28,152 main INFO screen launchpad pass=1 dev=0.0 ins=14.4 pro=31 1a=False 1b=False 2=False (4.2s)
Sep 12 10:29:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:47,793 main INFO screen CATE pass=0 dev=0.56 ins=0.0 pro=1 1a=False 1b=False 2=False (26.0s)
Sep 12 10:29:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:29:48,335 main INFO screen BUNDLEINU pass=0 dev=36.8 ins=0.0 pro=4 1a=False 1b=False 2=True (6.7s)
Sep 12 10:30:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:30:20,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:30:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:30:22,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:30:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:30:28,114 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:30:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:30:29,355 main INFO screen launchpad pass=0 dev=0.0 ins=23.5 pro=45 1a=False 1b=False 2=True (9.0s)
Sep 12 10:30:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:30:47,899 main INFO screen MercedesBe pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.5s)
Sep 12 10:32:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:32:28,458 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:32:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:32:33,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:32:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:32:36,360 main INFO screen PADDOG pass=1 dev=0.0 ins=0.0 pro=45 1a=False 1b=False 2=False (6.1s)
Sep 12 10:32:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:32:52,483 main INFO screen JESUSCASH pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (24.1s)
Sep 12 10:32:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:32:56,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:33:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:33:01,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:33:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:33:15,864 main INFO screen BREW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 10:33:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:33:34,157 main INFO screen . pass=0 dev=0.3 ins=0.0 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 12 10:33:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:33:40,280 main INFO screen POOL pass=1 dev=3.25 ins=3.17 pro=26 1a=False 1b=False 2=False (1.7s)
Sep 12 10:33:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:33:44,885 main INFO screen TAMPONS pass=1 dev=3.69 ins=0.0 pro=38 1a=False 1b=False 2=False (3.2s)
Sep 12 10:34:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:34:13,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:34:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:34:18,597 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:34:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:34:19,302 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 12 10:34:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:34:32,854 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.6s)
Sep 12 10:34:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:34:37,114 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:34:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 12 10:35:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:35:16,691 main INFO screen STMCN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 10:35:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:35:41,009 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:35:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:35:46,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:35:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:35:53,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:35:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:35:58,073 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:36:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:00,985 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 10:36:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:12,578 main INFO screen iPhone Duo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 10:36:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:19,688 main INFO screen Pepezzaro pass=0 dev=1.15 ins=0.0 pro=3 1a=False 1b=False 2=False (4.9s)
Sep 12 10:36:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:20,612 main INFO screen rob pass=1 dev=0.0 ins=15.08 pro=34 1a=False 1b=False 2=False (5.4s)
Sep 12 10:36:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:56,634 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.3s)
Sep 12 10:36:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:36:59,567 main INFO screen RBC pass=0 dev=0.13 ins=0.0 pro=4 1a=False 1b=False 2=False (6.5s)
Sep 12 10:37:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:00,132 main INFO screen STMCN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.7s)
Sep 12 10:37:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:15,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:37:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:20,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:37:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:33,748 main INFO screen WALLY pass=0 dev=0.36 ins=47.99 pro=13 1a=True 1b=True 2=True (18.4s)
Sep 12 10:37:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:36,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:37:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:43,866 main INFO screen launchpad pass=0 dev=1.06 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 12 10:37:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:37:55,550 main INFO screen S&P pass=0 dev=0.0 ins=12.94 pro=57 1a=False 1b=False 2=True (3.1s)
Sep 12 10:38:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:38:50,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:38:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:38:56,277 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:38:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:38:57,821 main INFO screen ANT-1 pass=1 dev=0.0 ins=13.24 pro=33 1a=False 1b=False 2=False (4.5s)
Sep 12 10:38:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:38:59,300 main INFO screen Pepusky pass=0 dev=0.3 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 12 10:39:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:39:09,471 main INFO screen ACAT pass=0 dev=0.21 ins=79.1 pro=8 1a=True 1b=True 2=True (18.9s)
Sep 12 10:39:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:39:56,505 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:39:56 +0000] "GET /health HTTP/1.1" 200 496 "-" "Python-urllib/3.14"
Sep 12 10:39:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:39:58,234 main INFO screen $CAT pass=0 dev=0.65 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 12 10:40:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:06,705 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:10:40:06 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 10:40:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:19,616 main INFO screen STMCN pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 10:40:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:19,767 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:40:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:24,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:40:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:39,367 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.7s)
Sep 12 10:40:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:41,247 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:40:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:40:46,307 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:41:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:41:00,686 main INFO screen SpicyPepe pass=0 dev=0.83 ins=0.0 pro=2 1a=False 1b=False 2=False (19.5s)
Sep 12 10:41:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:41:07,868 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 12 10:43:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:43:11,526 main INFO screen STMCNMTD pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.8s)
Sep 12 10:44:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:44:10,909 main INFO screen DOGES pass=1 dev=0.0 ins=7.83 pro=52 1a=False 1b=False 2=False (2.4s)
Sep 12 10:44:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:44:31,377 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:44:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:44:36,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:44:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:44:52,298 main INFO screen SlowRogan pass=0 dev=8.17 ins=31.44 pro=45 1a=False 1b=False 2=True (21.0s)
Sep 12 10:45:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:45:24,683 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:45:24 +0000] "GET /health HTTP/1.1" 200 496 "-" "Python-urllib/3.14"
Sep 12 10:45:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:45:38,334 main INFO screen . pass=0 dev=0.23 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 12 10:46:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:46:40,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:46:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:46:48,374 main INFO screen MGSTMCN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 12 10:47:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:47:44,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:47:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:47:49,799 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:48:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:48:03,636 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.0s)
Sep 12 10:49:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:49:28,904 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:49:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:49:34,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:49:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:49:35,217 main INFO screen RC pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 12 10:49:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:49:49,571 main INFO screen MCCAMEL pass=0 dev=0.07 ins=77.33 pro=9 1a=False 1b=True 2=True (20.8s)
Sep 12 10:50:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:50:00,846 main INFO screen GBNHVN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.4s)
Sep 12 10:50:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:50:24,981 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:50:24 +0000] "GET /health HTTP/1.1" 200 496 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T09:47:04Z
Running as unit: schaduwbot-wallets.service; invocation ID: 59ae4466605a4369ba7d98991ca62d2e
analyses gestart (571ea883d7b8)
--- update 2026-09-12T09:52:16Z
nieuwe code: 49e15c7
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T09:57:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 571283a9195f4501a57b6cd9bbbe5e84
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T10:02:36Z
--- update 2026-09-12T10:07:56Z
--- update 2026-09-12T10:13:22Z
--- update 2026-09-12T10:18:22Z
--- update 2026-09-12T10:23:36Z
--- update 2026-09-12T10:29:22Z
--- update 2026-09-12T10:34:36Z
--- update 2026-09-12T10:39:55Z
--- update 2026-09-12T10:45:23Z
--- update 2026-09-12T10:50:23Z
```

## Analyses (laatste 25 regels)
```
inactive
10:06:09 klaar (813 rpc-calls, 2 fouten)
10:06:12 klaar in 2s: 16508 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
10:06:12 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 10:06 UTC
10:06:12 52895 tokens geladen
10:06:15   2000 tokens, 247058 trades, 50537 posities (3s)
10:06:18   4000 tokens, 492472 trades, 99641 posities (6s)
10:06:21   6000 tokens, 735209 trades, 145534 posities (9s)
10:06:24   8000 tokens, 976677 trades, 193839 posities (12s)
10:06:26   10000 tokens, 1228727 trades, 240802 posities (15s)
10:06:29   12000 tokens, 1497671 trades, 298929 posities (17s)
10:06:32   14000 tokens, 1735520 trades, 339333 posities (20s)
10:06:35   16000 tokens, 1986175 trades, 387978 posities (23s)
10:06:37   18000 tokens, 2228897 trades, 433810 posities (25s)
10:06:40   20000 tokens, 2503151 trades, 490567 posities (28s)
10:06:43   22000 tokens, 2748558 trades, 535570 posities (31s)
10:06:46   24000 tokens, 2992686 trades, 583437 posities (34s)
10:06:48   26000 tokens, 3220982 trades, 627232 posities (36s)
10:06:51   28000 tokens, 3479029 trades, 676463 posities (39s)
10:06:54   30000 tokens, 3729766 trades, 734645 posities (42s)
10:06:55 posities: 748220 uit 3781782 trades (43s)
10:07:06 161757 wallets gerekend
10:07:06 geluk-toets
10:07:42 persistentie
10:07:44 kopieer-simulatie
10:07:56 klaar in 105s -> /opt/schaduwbot/reports/wallets.md
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
