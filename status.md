# Schaduwbot status

- tijd: 2026-09-12 15:35:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 1 hour, 48 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 763/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 20596, "tokens_in_memory": 5381, "msgs": 1975644, "trades": 517498, "creates": 5381, "decode_fail": 22289, "rpc_calls": 16251, "rpc_errors": 693, "sol_usd": 101.96024982865984, "open_positions": 46, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 13772 | 2124 | 13 | 2122 | 154 | 3717 | 11131 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 554 | 17% | 1.8% | +43.7% | -16.3% | -6.30% | 100% |
| dip35_V1_gescreend_fail | 4444 | 27% | 3.9% | +45.3% | -26.0% | -6.57% | 100% |
| dip35_V1_alle | 5510 | 26% | 4.1% | +44.6% | -25.4% | -6.83% | 100% |
| dip35_V2_gescreend_pass | 551 | 23% | 2.5% | +41.4% | -20.6% | -6.51% | 100% |
| dip35_V2_gescreend_fail | 4489 | 25% | 4.4% | +55.0% | -28.0% | -6.96% | 100% |
| dip35_V2_alle | 5468 | 25% | 4.7% | +52.4% | -27.8% | -7.81% | 100% |
| dip35_V3_gescreend_pass | 551 | 9% | 2.9% | +273.8% | -22.1% | +4.74% | 100% |
| dip35_V3_gescreend_fail | 4591 | 14% | 6.2% | +111.5% | -29.7% | -10.68% | 100% |
| dip35_V3_alle | 5524 | 13% | 6.2% | +115.8% | -29.4% | -10.19% | 100% |
| dip40_V1_gescreend_pass | 522 | 14% | 1.9% | +45.9% | -15.7% | -6.93% | 100% |
| dip40_V1_gescreend_fail | 4374 | 26% | 3.8% | +47.0% | -25.8% | -6.53% | 100% |
| dip40_V1_alle | 5295 | 26% | 4.0% | +46.9% | -25.2% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 520 | 18% | 2.3% | +44.3% | -19.7% | -8.34% | 100% |
| dip40_V2_gescreend_fail | 4393 | 25% | 4.3% | +55.0% | -28.0% | -7.03% | 100% |
| dip40_V2_alle | 5248 | 24% | 4.5% | +53.1% | -27.6% | -8.03% | 100% |
| dip40_V3_gescreend_pass | 521 | 8% | 2.5% | +265.1% | -21.0% | +2.57% | 100% |
| dip40_V3_gescreend_fail | 4481 | 13% | 6.0% | +106.1% | -29.6% | -11.73% | 100% |
| dip40_V3_alle | 5303 | 13% | 6.0% | +110.9% | -29.1% | -11.22% | 100% |
| dip45_V1_gescreend_pass | 501 | 15% | 1.8% | +47.7% | -15.5% | -6.29% | 100% |
| dip45_V1_gescreend_fail | 4290 | 27% | 3.5% | +48.3% | -25.6% | -5.34% | 100% |
| dip45_V1_alle | 5127 | 26% | 3.5% | +48.5% | -24.9% | -5.77% | 100% |
| dip45_V2_gescreend_pass | 498 | 18% | 2.2% | +43.2% | -19.6% | -8.13% | 100% |
| dip45_V2_gescreend_fail | 4301 | 25% | 4.0% | +57.7% | -27.7% | -6.02% | 100% |
| dip45_V2_alle | 5083 | 24% | 4.1% | +56.2% | -27.2% | -6.92% | 100% |
| dip45_V3_gescreend_pass | 501 | 8% | 2.2% | +308.2% | -20.5% | +5.75% | 100% |
| dip45_V3_gescreend_fail | 4372 | 14% | 5.5% | +112.9% | -29.1% | -9.51% | 100% |
| dip45_V3_alle | 5129 | 13% | 5.5% | +120.0% | -28.6% | -8.93% | 100% |

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
| per_token_met_xlink | 431 | 15% | 5.1% | -9.12% | -12.0% tot -6.2% | -14.3% | – | 100% |
| per_token_zonder_xlink | 126 | 21% | 0.0% | +19.17% | -12.8% tot +51.1% | -13.2% | 128% | 54% |
| gepoold_met_xlink | 3624 | 13% | 2.9% | -9.71% | -11.0% tot -8.4% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1095 | 18% | 0.0% | +18.09% | +0.2% tot +35.9% | -14.4% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 15:20:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:20:42,408 main INFO screen AI pass=0 dev=0.0 ins=9.14 pro=69 1a=False 1b=False 2=True (20.8s)
Sep 12 15:20:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:20:59,678 main INFO screen DOOROC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.5s)
Sep 12 15:21:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:21:26,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:21:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:21:31,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:21:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:21:47,584 main INFO screen GS pass=0 dev=0.0 ins=12.11 pro=32 1a=False 1b=False 2=True (20.8s)
Sep 12 15:21:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:21:57,462 main INFO screen mmrich pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 12 15:21:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:21:59,275 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:22:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:04,305 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:22:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:08,307 main INFO screen LIFE pass=1 dev=0.0 ins=8.65 pro=23 1a=False 1b=False 2=False (2.9s)
Sep 12 15:22:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:24,943 main INFO screen AORP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (25.7s)
Sep 12 15:22:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:26,440 main INFO screen DOOB pass=0 dev=30.9 ins=0.0 pro=6 1a=False 1b=False 2=False (11.0s)
Sep 12 15:22:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:44,830 main INFO screen WXM pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (12.8s)
Sep 12 15:22:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:22:56,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:23:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:05,546 main INFO screen GS pass=1 dev=0.0 ins=16.58 pro=25 1a=False 1b=False 2=False (9.0s)
Sep 12 15:23:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:24,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:23:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:29,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:23:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:43,620 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 12 15:23:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:48,953 main INFO screen SHITGPT pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (24.4s)
Sep 12 15:23:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:23:50,184 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:24:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:24:01,287 main INFO screen WEB0 pass=0 dev=0.0 ins=8.62 pro=16 1a=False 1b=False 2=True (11.2s)
Sep 12 15:24:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:24:06,746 main INFO screen EGG pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (12.8s)
Sep 12 15:24:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:24:34,237 main INFO screen Jesus pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.1s)
Sep 12 15:25:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:04,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:25:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:09,374 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:25:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:14,454 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:25:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:18,044 main INFO screen SPANK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (13.4s)
Sep 12 15:25:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:29,959 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:25:29 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 12 15:25:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:33,983 main INFO screen Fo Mo pass=0 dev=0.0 ins=50.09 pro=53 1a=False 1b=False 2=True (24.7s)
Sep 12 15:25:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:25:46,795 main INFO screen WINA pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 15:26:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:26:25,626 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:26:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:26:30,662 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:26:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:26:41,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:26:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:26:51,241 main INFO screen KEYCAT pass=0 dev=0.0 ins=48.9 pro=29 1a=True 1b=True 2=True (25.7s)
Sep 12 15:26:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:26:52,146 main INFO screen PCI6900 pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (11.2s)
Sep 12 15:27:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:27:00,164 main INFO screen NOCAP pass=0 dev=9.66 ins=0.0 pro=3 1a=False 1b=False 2=False (13.8s)
Sep 12 15:28:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:14,491 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:28:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:19,561 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:28:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:27,625 main INFO screen KSARD pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.5s)
Sep 12 15:28:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:33,974 main INFO screen Flyops pass=1 dev=0.0 ins=13.34 pro=32 1a=False 1b=False 2=False (4.7s)
Sep 12 15:28:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:39,764 main INFO screen CAPTCHA pass=0 dev=0.0 ins=9.64 pro=44 1a=False 1b=False 2=True (2.6s)
Sep 12 15:28:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:28:41,665 main INFO screen GitHub pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (27.3s)
Sep 12 15:29:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:00,976 main INFO screen FUD pass=0 dev=0.0 ins=22.58 pro=58 1a=False 1b=False 2=True (8.3s)
Sep 12 15:29:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:23,070 main INFO screen DOGE  pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 12 15:29:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:35,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:29:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:38,691 main INFO screen THG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 15:29:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:40,770 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:29:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:41,141 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:29:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:46,159 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:29:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:47,211 main INFO screen dc pass=0 dev=0.45 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 12 15:29:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:47,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:29:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:29:56,749 main INFO screen VOID pass=0 dev=41.29 ins=0.0 pro=1 1a=False 1b=False 2=True (9.5s)
Sep 12 15:30:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:01,821 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.2s)
Sep 12 15:30:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:04,354 main INFO screen baton pass=0 dev=0.0 ins=35.28 pro=17 1a=False 1b=False 2=True (23.5s)
Sep 12 15:30:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:09,114 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:30:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:14,146 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:30:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:31,980 main INFO screen のび子 pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (22.9s)
Sep 12 15:30:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:30:36,262 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:30:36 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 15:31:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:31:14,118 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:31:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:31:19,150 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:31:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:31:38,914 main INFO screen PAPERHANDS pass=0 dev=74.64 ins=0.0 pro=14 1a=False 1b=False 2=True (24.9s)
Sep 12 15:32:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:15,076 main INFO screen dc pass=0 dev=0.61 ins=0.0 pro=3 1a=False 1b=False 2=False (5.7s)
Sep 12 15:32:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:31,324 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:32:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:36,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:32:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:50,398 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:32:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:53,443 main INFO screen CATAPPLE pass=0 dev=0.07 ins=79.24 pro=8 1a=False 1b=True 2=True (22.2s)
Sep 12 15:32:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:32:55,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:33:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:03,309 main INFO screen dinosquirl pass=1 dev=0.0 ins=0.03 pro=48 1a=False 1b=False 2=False (3.9s)
Sep 12 15:33:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:04,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:33:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:09,316 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.0s)
Sep 12 15:33:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:09,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:33:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:23,787 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.4s)
Sep 12 15:33:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:33:32,290 main INFO screen TLD pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 12 15:34:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:13,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:34:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:16,469 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:34:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:21,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 15:34:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:22,192 main INFO screen $YO pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 12 15:34:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:37,431 main INFO screen SOLFLY pass=0 dev=0.0 ins=11.94 pro=65 1a=False 1b=False 2=True (21.0s)
Sep 12 15:34:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:34:53,050 main INFO screen Coin pass=1 dev=3.43 ins=9.56 pro=37 1a=False 1b=False 2=False (3.9s)
Sep 12 15:35:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:10,684 main INFO screen FART pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 12 15:35:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 15:35:37,092 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:15:35:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: f76b0ba
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-12T14:15:36Z
--- update 2026-09-12T14:21:31Z
Running as unit: schaduwbot-wallets.service; invocation ID: 231ef89f1987467a9f6d8d397018c1e2
analyses gestart (02faa7a55c91)
--- update 2026-09-12T14:26:36Z
--- update 2026-09-12T14:31:58Z
--- update 2026-09-12T14:37:10Z
--- update 2026-09-12T14:42:26Z
--- update 2026-09-12T14:47:36Z
--- update 2026-09-12T14:53:12Z
--- update 2026-09-12T14:58:35Z
--- update 2026-09-12T15:03:36Z
--- update 2026-09-12T15:09:30Z
--- update 2026-09-12T15:14:35Z
--- update 2026-09-12T15:19:36Z
--- update 2026-09-12T15:25:28Z
--- update 2026-09-12T15:30:35Z
--- update 2026-09-12T15:35:36Z
```

## Analyses (laatste 25 regels)
```
inactive
14:30:30 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 14:30 UTC
14:30:31 56838 tokens geladen
14:30:33   2000 tokens, 252349 trades, 49514 posities (2s)
14:30:35   4000 tokens, 494608 trades, 94985 posities (5s)
14:30:37   6000 tokens, 722751 trades, 137824 posities (7s)
14:30:39   8000 tokens, 957929 trades, 180570 posities (9s)
14:30:41   10000 tokens, 1190181 trades, 224203 posities (11s)
14:30:44   12000 tokens, 1452487 trades, 275238 posities (13s)
14:30:46   14000 tokens, 1716989 trades, 330574 posities (15s)
14:30:48   16000 tokens, 1938904 trades, 366489 posities (17s)
14:30:50   18000 tokens, 2198218 trades, 418143 posities (20s)
14:30:52   20000 tokens, 2430685 trades, 460461 posities (22s)
14:30:55   22000 tokens, 2695330 trades, 514894 posities (24s)
14:30:57   24000 tokens, 2940087 trades, 559865 posities (26s)
14:30:59   26000 tokens, 3170067 trades, 601122 posities (28s)
14:31:01   28000 tokens, 3403030 trades, 644659 posities (30s)
14:31:03   30000 tokens, 3646890 trades, 692146 posities (33s)
14:31:05   32000 tokens, 3903989 trades, 741913 posities (35s)
14:31:07   34000 tokens, 4145830 trades, 798529 posities (37s)
14:31:08 posities: 805880 uit 4173971 trades (37s)
14:31:18 168398 wallets gerekend
14:31:18 geluk-toets
14:31:51 persistentie
14:31:54 kopieer-simulatie
14:32:06 klaar in 95s -> /opt/schaduwbot/reports/wallets.md
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
