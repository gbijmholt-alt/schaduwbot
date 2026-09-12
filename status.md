# Schaduwbot status

- tijd: 2026-09-12 17:10:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 3 hours, 23 minutes
- bot-service: active
- code-versie: 8d4b88e
- schijf: 3.8G/38G | geheugen: 890/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 26298, "tokens_in_memory": 7238, "msgs": 2909787, "trades": 716578, "creates": 8328, "decode_fail": 33302, "rpc_calls": 20567, "rpc_errors": 864, "sol_usd": 102.10660189229067, "open_positions": 61, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 16945 | 2396 | 14 | 2395 | 178 | 4220 | 12642 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 574 | 17% | 1.7% | +43.6% | -16.1% | -6.22% | 100% |
| dip35_V1_gescreend_fail | 4584 | 27% | 3.9% | +45.4% | -26.1% | -6.60% | 100% |
| dip35_V1_alle | 5690 | 26% | 4.1% | +44.7% | -25.4% | -6.85% | 100% |
| dip35_V2_gescreend_pass | 570 | 22% | 2.5% | +40.8% | -20.4% | -6.62% | 100% |
| dip35_V2_gescreend_fail | 4633 | 25% | 4.4% | +55.0% | -28.1% | -6.97% | 100% |
| dip35_V2_alle | 5648 | 25% | 4.6% | +52.3% | -27.8% | -7.83% | 100% |
| dip35_V3_gescreend_pass | 571 | 9% | 2.8% | +266.5% | -22.0% | +4.28% | 100% |
| dip35_V3_gescreend_fail | 4734 | 14% | 6.1% | +110.9% | -29.8% | -10.71% | 100% |
| dip35_V3_alle | 5701 | 13% | 6.1% | +114.9% | -29.4% | -10.27% | 100% |
| dip40_V1_gescreend_pass | 542 | 14% | 1.8% | +46.0% | -15.6% | -6.93% | 100% |
| dip40_V1_gescreend_fail | 4504 | 27% | 3.9% | +46.9% | -25.9% | -6.55% | 100% |
| dip40_V1_alle | 5464 | 26% | 4.0% | +46.8% | -25.2% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 539 | 17% | 2.2% | +43.6% | -19.5% | -8.49% | 100% |
| dip40_V2_gescreend_fail | 4529 | 25% | 4.3% | +54.8% | -28.1% | -7.02% | 100% |
| dip40_V2_alle | 5419 | 24% | 4.5% | +52.8% | -27.6% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 541 | 8% | 2.4% | +265.1% | -20.9% | +1.84% | 100% |
| dip40_V3_gescreend_fail | 4614 | 13% | 5.9% | +105.9% | -29.6% | -11.74% | 100% |
| dip40_V3_alle | 5469 | 13% | 5.9% | +110.5% | -29.1% | -11.31% | 100% |
| dip45_V1_gescreend_pass | 520 | 15% | 1.7% | +47.5% | -15.4% | -6.19% | 100% |
| dip45_V1_gescreend_fail | 4415 | 28% | 3.6% | +48.3% | -25.7% | -5.37% | 100% |
| dip45_V1_alle | 5285 | 26% | 3.6% | +48.3% | -25.0% | -5.80% | 100% |
| dip45_V2_gescreend_pass | 516 | 18% | 2.1% | +42.7% | -19.5% | -8.04% | 100% |
| dip45_V2_gescreend_fail | 4428 | 25% | 4.1% | +57.5% | -27.7% | -6.11% | 100% |
| dip45_V2_alle | 5240 | 24% | 4.1% | +55.9% | -27.3% | -6.99% | 100% |
| dip45_V3_gescreend_pass | 519 | 8% | 2.1% | +303.1% | -20.3% | +5.22% | 100% |
| dip45_V3_gescreend_fail | 4498 | 14% | 5.5% | +111.2% | -29.2% | -9.84% | 100% |
| dip45_V3_alle | 5282 | 13% | 5.5% | +118.1% | -28.6% | -9.26% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 448 | 15% | 4.9% | -9.04% | -11.8% tot -6.2% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3773 | 13% | 2.8% | -9.69% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 16:59:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:59:53,348 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:59:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:59:53,694 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 16:59:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 16:59:58,478 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:04,421 main INFO screen CP pass=0 dev=0.0 ins=24.63 pro=8 1a=False 1b=False 2=True (21.0s)
Sep 12 17:00:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:09,878 main INFO screen Meowcraft pass=0 dev=0.0 ins=16.14 pro=40 1a=False 1b=False 2=True (5.5s)
Sep 12 17:00:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:09,945 main INFO screen cashback pass=0 dev=0.0 ins=35.61 pro=10 1a=False 1b=False 2=True (21.4s)
Sep 12 17:00:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:10,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:18,301 main INFO screen HODL pass=0 dev=0.0 ins=33.16 pro=23 1a=False 1b=False 2=True (8.4s)
Sep 12 17:00:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:20,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:22,358 main INFO screen HODL pass=0 dev=0.0 ins=30.47 pro=12 1a=False 1b=False 2=True (12.4s)
Sep 12 17:00:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:25,110 main INFO screen HODL pass=0 dev=0.0 ins=17.52 pro=55 1a=False 1b=False 2=True (31.8s)
Sep 12 17:00:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:28,660 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:29,378 main INFO screen PAIR pass=0 dev=0.0 ins=34.12 pro=20 1a=False 1b=False 2=True (11.1s)
Sep 12 17:00:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:33,733 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:35,003 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:00:35 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 17:00:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:49,366 main INFO screen AIRDROP pass=0 dev=0.0 ins=41.14 pro=19 1a=False 1b=False 2=True (21.3s)
Sep 12 17:00:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:50,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:00:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:00:55,712 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:01:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:01:12,335 main INFO screen BAH pass=0 dev=0.0 ins=18.18 pro=14 1a=False 1b=False 2=True (21.7s)
Sep 12 17:01:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:01:46,764 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:01:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:01:59,579 main INFO screen afeng  pass=0 dev=3.38 ins=0.0 pro=2 1a=False 1b=False 2=False (13.0s)
Sep 12 17:02:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:02:10,570 main INFO screen CAJUN pass=0 dev=0.63 ins=0.0 pro=4 1a=False 1b=False 2=False (10.1s)
Sep 12 17:02:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:02:21,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:02:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:02:24,093 main INFO screen PATRICK pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (10.3s)
Sep 12 17:02:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:02:31,023 main INFO screen cap pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 12 17:02:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:02:34,375 main INFO screen BTCP pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (12.7s)
Sep 12 17:03:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:03:15,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:03:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:03:20,229 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:03:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:03:33,025 main INFO screen AIDNX pass=0 dev=10.0 ins=23.1 pro=13 1a=False 1b=False 2=False (7.2s)
Sep 12 17:03:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:03:36,018 main INFO screen SPA pass=0 dev=0.0 ins=20.87 pro=64 1a=False 1b=False 2=True (21.0s)
Sep 12 17:03:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:03:59,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:04:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:12,887 main INFO screen DERP pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (13.9s)
Sep 12 17:04:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:24,347 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:04:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:29,481 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:04:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:35,316 main INFO screen TITS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 12 17:04:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:44,043 main INFO screen LMTW pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 12 17:04:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:04:44,478 main INFO screen Pumpwheel pass=0 dev=0.0 ins=15.6 pro=38 1a=False 1b=False 2=True (20.2s)
Sep 12 17:05:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:12,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:05:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:23,632 main INFO screen $RAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.5s)
Sep 12 17:05:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:26,156 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:05:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:31,244 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:05:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:35,755 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:05:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:37,372 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:05:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 17:05:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:40,825 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:05:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:45,480 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.4s)
Sep 12 17:05:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:05:58,191 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:06:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:06:00,174 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (24.5s)
Sep 12 17:06:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:06:09,064 main INFO screen DFS pass=1 dev=0.0 ins=15.33 pro=52 1a=False 1b=False 2=False (11.0s)
Sep 12 17:06:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:06:27,286 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:06:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:06:32,319 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:06:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:06:49,936 main INFO screen Stonks pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (22.8s)
Sep 12 17:07:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:33,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:07:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:44,169 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (10.9s)
Sep 12 17:07:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:45,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:07:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:48,741 main INFO screen DRCA pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (11.5s)
Sep 12 17:07:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:48,838 main INFO screen BALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (11.2s)
Sep 12 17:07:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:07:50,374 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:04,715 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.4s)
Sep 12 17:08:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:13,648 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:18,306 main INFO screen BALLOONS pass=1 dev=0.0 ins=12.9 pro=52 1a=False 1b=False 2=False (3.6s)
Sep 12 17:08:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:18,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:18,844 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:23,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:24,667 main INFO screen HODL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.5s)
Sep 12 17:08:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:29,387 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:34,492 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:37,644 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.9s)
Sep 12 17:08:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:39,893 main INFO screen rewardog pass=0 dev=0.0 ins=53.23 pro=45 1a=False 1b=False 2=True (26.3s)
Sep 12 17:08:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:50,545 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 12 17:08:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:52,103 main INFO screen GEMI pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (22.8s)
Sep 12 17:08:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:55,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:00,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:05,295 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:10,364 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:22,841 main INFO screen TOMB pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (9.4s)
Sep 12 17:09:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:23,125 main INFO screen RTW pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (27.6s)
Sep 12 17:09:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:23,992 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.8s)
Sep 12 17:10:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:06,412 main INFO screen OpenAI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 12 17:10:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:35,061 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:10:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:38,911 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:10:38 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T16:02:16Z
--- update 2026-09-12T16:07:36Z
--- update 2026-09-12T16:13:17Z
--- update 2026-09-12T16:18:17Z
--- update 2026-09-12T16:23:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 734fe7fd71e047c5827569b33cc14ab3
analyses gestart (02faa7a55c91)
--- update 2026-09-12T16:28:48Z
--- update 2026-09-12T16:34:00Z
--- update 2026-09-12T16:39:17Z
--- update 2026-09-12T16:44:36Z
--- update 2026-09-12T16:50:10Z
--- update 2026-09-12T16:55:17Z
--- update 2026-09-12T17:00:34Z
--- update 2026-09-12T17:05:36Z
nieuwe code: 8d4b88e
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 4382a0e1c14a4f7986ac753e7d367fa4
analyses gestart (4ee13da033ab)
--- update 2026-09-12T17:10:37Z
```

## Analyses (laatste 25 regels)
```
active
16:33:00   20000 tokens, 2363976 trades, 436311 posities (21s)
16:33:02   22000 tokens, 2582686 trades, 474654 posities (23s)
16:33:05   24000 tokens, 2844904 trades, 527964 posities (25s)
16:33:07   26000 tokens, 3086184 trades, 570567 posities (28s)
16:33:09   28000 tokens, 3312079 trades, 611146 posities (30s)
16:33:11   30000 tokens, 3535303 trades, 651231 posities (31s)
16:33:13   32000 tokens, 3763932 trades, 694079 posities (33s)
16:33:16   34000 tokens, 4017731 trades, 742207 posities (36s)
16:33:18   36000 tokens, 4259150 trades, 795214 posities (38s)
16:33:19 posities: 829213 uit 4407533 trades (40s)
16:33:29 172443 wallets gerekend
16:33:30 geluk-toets
16:34:03 persistentie
16:34:05 kopieer-simulatie
16:34:23 klaar in 103s -> /opt/schaduwbot/reports/wallets.md
17:05:37 36044 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
17:05:39   ingelezen tot rowid 4474167 (81641 rijen, 81641 bruikbaar)
17:05:40 ingelezen: 81641 nieuwe trades, 81641 bruikbaar (3s)
17:06:14 1129 aankopen van gevolgde wallets geëvalueerd
17:06:23 vroege kopers: 151 voldoen nu, register 219, 110 tokens beoordeeld
17:06:32 grote spelers: saldo van 29 wallets opgehaald
17:07:37 herkomst: 40 posities gekoppeld
17:07:40 klaar in 123s -> /opt/schaduwbot/reports/ledger.md
17:07:40 telwijze -> probe-v4-pool-navragen: tellers en layout gewist, opnieuw opbouwen
17:07:40 na-migratie: 400 paren te checken
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
