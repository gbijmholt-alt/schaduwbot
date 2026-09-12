# Schaduwbot status

- tijd: 2026-09-12 10:02:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 20 hours, 15 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.5G/38G | geheugen: 582/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 616, "tokens_in_memory": 123, "msgs": 56241, "trades": 9336, "creates": 123, "decode_fail": 388, "rpc_calls": 336, "rpc_errors": 17, "sol_usd": 102.09891565251435, "open_positions": 8, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 09:47:13 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:47:13,853 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:47:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:47:18,892 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:47:33 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:47:33,165 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (19.4s)
Sep 12 09:48:40 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:48:40,992 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 12 09:49:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:49:20,565 main INFO screen Snailcat pass=0 dev=0.0 ins=16.32 pro=46 1a=False 1b=True 2=True (1.3s)
Sep 12 09:49:31 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:49:31,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:49:36 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:49:36,180 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:49:50 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:49:50,954 main INFO screen FTFS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 09:50:07 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:50:07,407 main INFO screen popcat pass=0 dev=0.0 ins=5.99 pro=44 1a=False 1b=True 2=False (1.6s)
Sep 12 09:50:08 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:50:08,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:50:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:50:15,531 main INFO screen MALLORCA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 12 09:50:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:50:29,132 aiohttp.access INFO 216.218.206.66 [12/Sep/2026:09:50:29 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 09:51:14 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:51:14,537 main INFO screen $AURA pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 6min 52.188s CPU time over 2h 28.836s wall clock time, 200.1M memory peak.
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:52:20,727 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:52:20 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 12 09:52:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:52:20,811 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 09:53:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:53:20,871 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:09:53:20 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 09:53:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:53:20,871 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:09:53:20 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 09:53:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:53:21,432 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:53:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:53:23,708 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (2.5s)
Sep 12 09:53:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:53:27,763 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (6.5s)
Sep 12 09:54:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:54:10,556 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:54:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:54:15,594 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:54:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:54:31,138 main INFO screen Flork pass=0 dev=0.0 ins=36.55 pro=68 1a=False 1b=False 2=True (20.7s)
Sep 12 09:55:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:55:41,461 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:55:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:55:48,074 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 12 09:56:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:56:39,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:56:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:56:40,110 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=6 1a=False 1b=False 2=False (3.3s)
Sep 12 09:56:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:56:44,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:57:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:02,130 main INFO screen WOWCOIN pass=0 dev=0.0 ins=48.89 pro=61 1a=True 1b=True 2=True (22.4s)
Sep 12 09:57:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:22,510 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:57:22 +0000] "GET /health HTTP/1.1" 200 487 "-" "Python-urllib/3.14"
Sep 12 09:57:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:26,020 main INFO screen wind pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (1.6s)
Sep 12 09:57:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:48,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:57:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:53,984 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:57:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:57:56,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:01,924 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:02,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:07,677 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:08,674 main INFO screen MSTRx pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=True 2=True (19.9s)
Sep 12 09:58:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:10,263 main INFO screen $peanie pass=0 dev=0.4 ins=0.0 pro=2 1a=False 1b=False 2=False (1.6s)
Sep 12 09:58:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:15,132 main INFO screen WALLY pass=0 dev=0.36 ins=47.99 pro=17 1a=True 1b=True 2=True (18.3s)
Sep 12 09:58:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:22,651 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=3 1a=False 1b=False 2=False (20.4s)
Sep 12 09:58:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:24,856 main INFO screen eyecoin pass=0 dev=0.0 ins=20.02 pro=42 1a=False 1b=False 2=True (1.4s)
Sep 12 09:58:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:26,216 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:31,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:58:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:58:46,708 main INFO screen RST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.6s)
Sep 12 09:59:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:21,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:59:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:26,533 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:59:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 09:59:42,338 main INFO screen primed pass=0 dev=0.0 ins=8.53 pro=62 1a=False 1b=False 2=True (20.9s)
Sep 12 10:00:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:31,620 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 10:00:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:41,147 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (7.4s)
Sep 12 10:00:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:00:41,810 main INFO screen Pochita  pass=0 dev=0.0 ins=21.9 pro=53 1a=False 1b=False 2=True (10.3s)
Sep 12 10:02:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 10:02:37,095 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:10:02:37 +0000] "GET /health HTTP/1.1" 200 490 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T09:52:16Z
nieuwe code: 49e15c7
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T09:57:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 571283a9195f4501a57b6cd9bbbe5e84
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T10:02:36Z
```

## Analyses (laatste 25 regels)
```
active
09:54:10   12000 tokens, 1502758 trades, 299428 posities (17s)
09:54:13   14000 tokens, 1734578 trades, 338972 posities (20s)
09:54:16   16000 tokens, 1991344 trades, 388468 posities (22s)
09:54:18   18000 tokens, 2229001 trades, 432491 posities (25s)
09:54:21   20000 tokens, 2500830 trades, 489338 posities (28s)
09:54:24   22000 tokens, 2747143 trades, 535081 posities (31s)
09:54:26   24000 tokens, 2990334 trades, 582631 posities (33s)
09:54:29   26000 tokens, 3225355 trades, 629150 posities (36s)
09:54:32   28000 tokens, 3491754 trades, 679900 posities (39s)
09:54:34   30000 tokens, 3730066 trades, 734857 posities (41s)
09:54:35 posities: 745944 uit 3769235 trades (42s)
09:54:47 161540 wallets gerekend
09:54:47 geluk-toets
09:55:27 persistentie
09:55:29 kopieer-simulatie
09:55:42 klaar in 109s -> /opt/schaduwbot/reports/wallets.md
09:57:22 27948 tokens sinds start volledige logging, waarvan 8445 met een gat door herstart
09:57:22   ingelezen tot rowid 3771495 (6848 rijen, 6848 bruikbaar)
09:57:22 ingelezen: 6848 nieuwe trades, 6848 bruikbaar (1s)
09:57:57 3000 aankopen van gevolgde wallets geëvalueerd
09:58:05 vroege kopers: 142 voldoen nu, register 177, 0 tokens beoordeeld
09:58:15 grote spelers: saldo van 436 wallets opgehaald
09:59:20 herkomst: 40 posities gekoppeld
09:59:22 klaar in 121s -> /opt/schaduwbot/reports/ledger.md
09:59:23 na-migratie: 400 paren te checken
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
