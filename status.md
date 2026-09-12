# Schaduwbot status

- tijd: 2026-09-12 11:32:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 21 hours, 45 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.5G/38G | geheugen: 595/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 6000, "tokens_in_memory": 1378, "msgs": 447526, "trades": 121978, "creates": 1378, "decode_fail": 4931, "rpc_calls": 3668, "rpc_errors": 157, "sol_usd": 101.99661912895947, "open_positions": 28, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 10009 | 1558 | 7 | 1557 | 104 | 2729 | 8190 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 511 | 16% | 2.0% | +43.7% | -16.5% | -6.64% | 100% |
| dip35_V1_gescreend_fail | 4209 | 27% | 3.8% | +45.8% | -25.8% | -6.52% | 100% |
| dip35_V1_alle | 5173 | 26% | 3.9% | +45.1% | -25.3% | -6.78% | 100% |
| dip35_V2_gescreend_pass | 507 | 22% | 2.8% | +43.5% | -20.9% | -6.93% | 100% |
| dip35_V2_gescreend_fail | 4245 | 25% | 4.3% | +56.3% | -27.9% | -6.80% | 100% |
| dip35_V2_alle | 5133 | 25% | 4.5% | +53.8% | -27.6% | -7.63% | 100% |
| dip35_V3_gescreend_pass | 506 | 9% | 3.2% | +288.8% | -22.3% | +4.74% | 100% |
| dip35_V3_gescreend_fail | 4335 | 13% | 6.0% | +116.0% | -29.6% | -10.04% | 100% |
| dip35_V3_alle | 5181 | 13% | 6.0% | +120.3% | -29.2% | -9.61% | 100% |
| dip40_V1_gescreend_pass | 480 | 15% | 2.1% | +45.8% | -15.9% | -6.90% | 100% |
| dip40_V1_gescreend_fail | 4141 | 26% | 3.7% | +47.4% | -25.7% | -6.42% | 100% |
| dip40_V1_alle | 4971 | 25% | 3.8% | +47.5% | -25.1% | -6.66% | 100% |
| dip40_V2_gescreend_pass | 477 | 18% | 2.5% | +45.4% | -19.8% | -8.19% | 100% |
| dip40_V2_gescreend_fail | 4155 | 25% | 4.2% | +55.8% | -27.9% | -6.88% | 100% |
| dip40_V2_alle | 4927 | 24% | 4.4% | +54.2% | -27.4% | -7.78% | 100% |
| dip40_V3_gescreend_pass | 478 | 8% | 2.7% | +288.0% | -21.1% | +2.85% | 100% |
| dip40_V3_gescreend_fail | 4234 | 13% | 5.8% | +110.2% | -29.4% | -11.01% | 100% |
| dip40_V3_alle | 4976 | 13% | 5.8% | +115.7% | -29.0% | -10.53% | 100% |
| dip45_V1_gescreend_pass | 460 | 15% | 2.0% | +47.6% | -15.7% | -6.25% | 100% |
| dip45_V1_gescreend_fail | 4054 | 27% | 3.3% | +48.6% | -25.4% | -5.16% | 100% |
| dip45_V1_alle | 4809 | 26% | 3.3% | +48.9% | -24.8% | -5.55% | 100% |
| dip45_V2_gescreend_pass | 457 | 19% | 2.4% | +43.0% | -19.8% | -7.72% | 100% |
| dip45_V2_gescreend_fail | 4061 | 25% | 3.8% | +58.5% | -27.5% | -5.71% | 100% |
| dip45_V2_alle | 4767 | 24% | 3.9% | +57.2% | -27.0% | -6.50% | 100% |
| dip45_V3_gescreend_pass | 459 | 7% | 2.4% | +344.1% | -20.5% | +6.52% | 100% |
| dip45_V3_gescreend_fail | 4127 | 14% | 5.3% | +115.1% | -28.9% | -8.85% | 100% |
| dip45_V3_alle | 4809 | 13% | 5.3% | +123.4% | -28.4% | -8.25% | 100% |

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
| per_token_met_xlink | 399 | 15% | 5.5% | -9.33% | -12.4% tot -6.3% | -14.5% | – | 100% |
| per_token_zonder_xlink | 115 | 20% | 0.0% | +20.70% | -14.2% tot +55.6% | -13.2% | 130% | 54% |
| gepoold_met_xlink | 3340 | 13% | 3.2% | -10.12% | -11.5% tot -8.8% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 995 | 18% | 0.0% | +20.14% | +0.5% tot +39.7% | -14.4% | 69% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 11:10:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:10:34,047 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:10:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:10:39,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:10:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:10:48,947 main INFO screen lickdoge pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (8.9s)
Sep 12 11:10:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:10:56,600 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (8.1s)
Sep 12 11:11:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:00,632 main INFO screen VOID pass=0 dev=39.08 ins=0.0 pro=2 1a=False 1b=False 2=True (26.7s)
Sep 12 11:11:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:19,658 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:11:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:19,729 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:11:19 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 11:11:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:24,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:11:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:36,370 main INFO screen PAIN pass=0 dev=3.43 ins=21.07 pro=51 1a=False 1b=False 2=True (8.3s)
Sep 12 11:11:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:11:43,312 main INFO screen dih pass=0 dev=0.0 ins=22.35 pro=42 1a=False 1b=False 2=True (23.7s)
Sep 12 11:12:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:12:00,227 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:12:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:12:05,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:12:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:12:22,617 main INFO screen CEO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (22.5s)
Sep 12 11:12:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:12:31,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:12:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:12:40,074 main INFO screen CATTISM pass=0 dev=0.2 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 12 11:13:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:13:02,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:13:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:13:07,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:13:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:13:24,522 main INFO screen BULLGPT pass=0 dev=0.16 ins=76.34 pro=9 1a=False 1b=True 2=True (21.9s)
Sep 12 11:14:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:14:04,477 main INFO screen M&M  pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 12 11:14:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:14:12,277 main INFO screen B4B pass=1 dev=3.46 ins=4.65 pro=33 1a=False 1b=False 2=False (8.4s)
Sep 12 11:14:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:14:58,024 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:15:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:15:03,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:15:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:15:20,740 main INFO screen KIMCHI pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (22.8s)
Sep 12 11:16:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:16:04,853 main INFO screen iPAD pass=0 dev=33.64 ins=0.17 pro=15 1a=False 1b=False 2=True (11.2s)
Sep 12 11:16:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:16:37,133 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:16:37 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:16:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:16:46,528 main INFO screen LPUD pass=1 dev=1.42 ins=4.35 pro=34 1a=False 1b=False 2=False (10.4s)
Sep 12 11:16:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:16:49,898 main INFO screen USMS pass=0 dev=1.27 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 11:18:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:18:21,912 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:18:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:18:33,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:18:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:18:33,965 main INFO screen PAPERBAG pass=0 dev=0.0 ins=19.98 pro=51 1a=False 1b=False 2=True (12.2s)
Sep 12 11:18:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:18:38,383 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:18:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:18:55,367 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (22.1s)
Sep 12 11:19:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:19:02,223 main INFO screen PUI pass=0 dev=6.64 ins=0.0 pro=3 1a=False 1b=False 2=True (6.1s)
Sep 12 11:20:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:20:29,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:20:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:20:34,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:20:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:20:54,411 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.6s)
Sep 12 11:21:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:01,653 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:06,724 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:23,662 main INFO screen PUMPBRAIN pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (22.1s)
Sep 12 11:21:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:36,696 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:39,988 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:41,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:51,162 main INFO screen NMFMK pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (11.3s)
Sep 12 11:21:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:55,274 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:21:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:21:58,444 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:21:58 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:22:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:22:00,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:22:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:22:00,680 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.1s)
Sep 12 11:22:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:22:17,829 main INFO screen VPN pass=0 dev=0.0 ins=22.26 pro=25 1a=False 1b=False 2=True (22.6s)
Sep 12 11:25:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:08,297 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:13,366 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:21,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:26,946 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:31,800 main INFO screen PADSOL pass=0 dev=0.07 ins=77.33 pro=10 1a=False 1b=True 2=True (23.6s)
Sep 12 11:25:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:35,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:40,825 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:25:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:45,088 main INFO screen RETAIL pass=0 dev=0.0 ins=10.19 pro=20 1a=False 1b=True 2=False (8.4s)
Sep 12 11:25:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:45,982 main INFO screen WALLY pass=0 dev=0.36 ins=47.97 pro=14 1a=True 1b=True 2=True (24.2s)
Sep 12 11:25:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:25:56,707 main INFO screen WWW pass=0 dev=0.11 ins=0.0 pro=4 1a=False 1b=False 2=False (6.8s)
Sep 12 11:26:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:26:02,294 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (26.6s)
Sep 12 11:27:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:27:20,540 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:27:20 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 11:27:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:27:20,853 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:27:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:27:25,881 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:27:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:27:44,492 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (23.7s)
Sep 12 11:28:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:28:08,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:28:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:28:19,021 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (10.4s)
Sep 12 11:28:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:28:26,715 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:28:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:28:31,812 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:28:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:28:47,806 main INFO screen Morty pass=0 dev=0.0 ins=21.35 pro=42 1a=False 1b=False 2=True (21.2s)
Sep 12 11:30:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:30:26,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:30:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:30:38,537 main INFO screen SXSN pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (12.6s)
Sep 12 11:31:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:01,435 main INFO screen kikmi pass=0 dev=0.12 ins=0.0 pro=1 1a=False 1b=False 2=False (5.4s)
Sep 12 11:31:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:08,745 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:13,820 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:32,816 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:32,993 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.3s)
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,892 aiohttp.access INFO 194.187.176.92 [12/Sep/2026:11:31:37 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 11:31:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:37,924 aiohttp.access INFO 194.187.176.67 [12/Sep/2026:11:31:37 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
Sep 12 11:31:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:31:57,646 main INFO screen BATONUSD pass=0 dev=0.19 ins=79.12 pro=9 1a=True 1b=True 2=True (24.9s)
Sep 12 11:32:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 11:32:20,807 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:11:32:20 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T10:55:36Z
--- update 2026-09-12T11:01:03Z
--- update 2026-09-12T11:06:18Z
--- update 2026-09-12T11:11:18Z
--- update 2026-09-12T11:16:36Z
--- update 2026-09-12T11:21:57Z
--- update 2026-09-12T11:27:19Z
--- update 2026-09-12T11:32:19Z
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
