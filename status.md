# Schaduwbot status

- tijd: 2026-09-12 13:13:30 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 23 hours, 26 minutes
- bot-service: active
- code-versie: 1f31a46
- schijf: 3.6G/38G | geheugen: 1191/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 12070, "tokens_in_memory": 2760, "msgs": 1004360, "trades": 275203, "creates": 2760, "decode_fail": 12831, "rpc_calls": 8209, "rpc_errors": 380, "sol_usd": 102.00384284659405, "open_positions": 56, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 12:58:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:07,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:58:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:12,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:58:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:15,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:58:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:21,810 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 12:58:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:23,414 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.73 pro=13 1a=True 1b=True 2=True (8.5s)
Sep 12 12:58:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:27,730 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=3 1a=False 1b=False 2=True (20.4s)
Sep 12 12:58:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:58:58,702 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:59:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:59:03,773 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:59:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:59:19,396 main INFO screen LaMisery pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (20.8s)
Sep 12 12:59:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:59:59,696 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:00:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:04,769 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:00:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:06,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:00:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:12,007 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:00:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:24,217 main INFO screen PUKA pass=0 dev=0.0 ins=18.37 pro=22 1a=False 1b=False 2=True (24.6s)
Sep 12 13:00:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:33,423 main INFO screen $MSN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (26.6s)
Sep 12 13:00:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:47,398 main INFO screen Zorig pass=1 dev=0.44 ins=4.26 pro=53 1a=False 1b=False 2=False (8.1s)
Sep 12 13:00:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:53,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:00:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:00:58,225 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:01:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:01:18,731 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=20 1a=False 1b=False 2=True (25.7s)
Sep 12 13:01:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:01:50,449 main INFO screen momoon pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (11.0s)
Sep 12 13:02:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:02:37,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:02:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:02:42,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:02:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:02:56,798 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:02:56 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 12 13:03:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:00,885 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=18 1a=False 1b=False 2=True (23.7s)
Sep 12 13:03:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:11,886 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:03:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:16,959 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:03:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:32,761 main INFO screen Neko pass=0 dev=0.0 ins=21.38 pro=71 1a=False 1b=False 2=True (21.0s)
Sep 12 13:03:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:44,425 main INFO screen $CAJUN pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (10.1s)
Sep 12 13:03:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:46,603 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:03:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:03:48,432 main INFO screen DIOUF pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (8.7s)
Sep 12 13:04:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:04:00,802 main INFO screen DIOUF pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (14.3s)
Sep 12 13:04:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:04:39,971 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 12 13:05:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:05:11,253 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:05:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:05:21,625 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.5s)
Sep 12 13:06:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:05,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:06:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:16,487 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.59 pro=12 1a=False 1b=False 2=True (11.5s)
Sep 12 13:06:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:26,301 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 12 13:06:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:31,876 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:06:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:36,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:06:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:53,832 aiohttp.access INFO 94.154.43.92 [12/Sep/2026:13:06:53 +0000] "GET / HTTP/1.1" 404 174 "http://167.233.49.49:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 12 13:06:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:06:58,557 main INFO screen POOL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (26.7s)
Sep 12 13:07:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:07:36,832 main INFO screen Usdtd pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 12 13:07:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:07:51,063 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:07:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:07:56,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:08:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:12,477 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:08:12 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 12 13:08:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:16,787 main INFO screen UNHROC pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (8.4s)
Sep 12 13:08:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:18,391 main INFO screen STEPSIS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (27.4s)
Sep 12 13:08:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:19,249 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=True (7.0s)
Sep 12 13:08:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:22,105 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:08:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:27,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:08:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:34,699 main INFO screen DIOUF pass=0 dev=0.38 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 12 13:08:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:46,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:08:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:49,111 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.2s)
Sep 12 13:08:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:49,929 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.7 pro=22 1a=False 1b=False 2=True (27.9s)
Sep 12 13:08:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:08:57,618 main INFO screen D4rkUch1ha pass=0 dev=0.0 ins=15.19 pro=32 1a=False 1b=True 2=True (11.4s)
Sep 12 13:09:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:09:13,509 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:09:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:09:26,444 main INFO screen ✈️ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (13.0s)
Sep 12 13:09:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:09:30,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:09:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:09:35,949 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:09:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:09:55,125 main INFO screen NASBAYC pass=0 dev=0.35 ins=78.96 pro=8 1a=False 1b=True 2=True (24.3s)
Sep 12 13:10:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:10:30,689 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:10:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:10:35,764 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:10:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:10:54,912 main INFO screen PokeFi pass=0 dev=0.17 ins=48.36 pro=16 1a=False 1b=False 2=True (24.3s)
Sep 12 13:12:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:12:00,340 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:12:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:12:15,104 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=13 1a=False 1b=False 2=True (14.9s)
Sep 12 13:12:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:12:15,150 main INFO screen AI pass=0 dev=0.0 ins=17.08 pro=31 1a=False 1b=False 2=True (4.0s)
Sep 12 13:12:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:12:50,103 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=30.43 pro=24 1a=False 1b=True 2=True (5.7s)
Sep 12 13:13:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:13:11,383 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:13:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:13:16,453 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 13:13:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 13:13:30,306 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:13:13:30 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T13:02:55Z
nieuwe code: 1f31a46
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 88310e2f16cc42c39aad06b1953b4bf1
analyses gestart (83a2a6960268)
--- update 2026-09-12T13:08:11Z
--- update 2026-09-12T13:13:29Z
```

## Analyses (laatste 25 regels)
```
active
13:05:06 klaar in 130s -> /opt/schaduwbot/reports/ledger.md
13:05:07 na-migratie: 400 paren te checken
13:09:25 na-migratie: 399 paren, 39 prijzen
13:09:26 probe: 400 transacties ophalen
13:12:45 klaar (918 rpc-calls, 1 fouten)
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
