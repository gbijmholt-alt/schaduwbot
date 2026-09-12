# Schaduwbot status

- tijd: 2026-09-12 14:53:13 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 1 hour, 6 minutes
- bot-service: active
- code-versie: f76b0ba
- schijf: 3.7G/38G | geheugen: 745/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 18053, "tokens_in_memory": 4560, "msgs": 1584257, "trades": 440944, "creates": 4560, "decode_fail": 19193, "rpc_calls": 13708, "rpc_errors": 601, "sol_usd": 101.9938460161697, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 14:39:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:02,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:39:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:07,158 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.67 pro=12 1a=False 1b=False 2=True (8.5s)
Sep 12 14:39:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:19,773 main INFO screen STONKOOR pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=True (22.1s)
Sep 12 14:39:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:20,882 main INFO screen da pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (4.4s)
Sep 12 14:39:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:41,438 main INFO screen Stonkoor pass=1 dev=0.0 ins=16.26 pro=26 1a=False 1b=False 2=False (4.0s)
Sep 12 14:39:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:39:47,021 main INFO screen DOOB pass=0 dev=1.33 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 12 14:40:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:16,711 main INFO screen BINGO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 12 14:40:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:38,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:39,076 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:44,487 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:40:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:46,848 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=14 1a=False 1b=False 2=True (8.8s)
Sep 12 14:40:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:40:59,047 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.1s)
Sep 12 14:41:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:13,146 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 12 14:41:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:37,102 main INFO screen spida pass=0 dev=4.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:41:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:41:58,252 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:03,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:10,973 main INFO screen Doge pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 12 14:42:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:11,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:16,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:16,691 main INFO screen MEME50 pass=0 dev=0.17 ins=50.82 pro=21 1a=False 1b=False 2=True (18.6s)
Sep 12 14:42:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:26,381 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:27,148 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:42:27 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:42:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:31,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:42:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:31,825 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=16 1a=False 1b=False 2=True (20.8s)
Sep 12 14:42:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:42:45,911 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 14:43:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:08,251 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:16,095 main INFO screen Tradcat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 14:43:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:41,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:46,552 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:43:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:43:56,600 main INFO screen spida pass=0 dev=4.26 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:44:01,117 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (19.7s)
Sep 12 14:45:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:13,079 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:45:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:18,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:45:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:32,317 main INFO screen $AURA pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (19.3s)
Sep 12 14:45:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:45:54,104 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,238 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /@vite/client HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,468 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /nonexistent-lane-control-cf9x2 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,652 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /__nextjs_source-map?filename=file:///nonexistent-lane-cf9x2 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:44,949 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:44 +0000] "GET /vite.svg HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,232 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.tsx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,487 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.ts HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,699 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.jsx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:45,887 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:45 +0000] "GET /src/main.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,171 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.mts HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,390 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.vue HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:46:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:46:46,594 aiohttp.access INFO 67.213.122.19 [12/Sep/2026:14:46:46 +0000] "GET /src/main.svelte HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
Sep 12 14:47:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:15,718 main INFO screen FAG pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 12 14:47:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:37,126 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:47:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 14:47:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:37,382 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:47:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:42,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:47:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:47:58,038 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.03 pro=17 1a=False 1b=False 2=True (20.7s)
Sep 12 14:48:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:48:31,970 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:48:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:48:39,155 main INFO screen MONEY pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.3s)
Sep 12 14:48:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:48:54,675 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:48:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:48:59,748 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:49:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:49:05,207 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 12 14:49:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:49:12,959 main INFO screen stooooonks pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (18.4s)
Sep 12 14:49:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:49:37,618 main INFO screen OINK pass=0 dev=4.42 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 12 14:50:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:31,834 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:50:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:32,232 main INFO screen Coin pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 12 14:50:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:36,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:50:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:46,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:50:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:51,034 main INFO screen WOTF pass=0 dev=97.21 ins=0.0 pro=1 1a=False 1b=True 2=True (19.6s)
Sep 12 14:50:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:54,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:50:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:55,325 main INFO screen Peptidog pass=0 dev=0.51 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 12 14:50:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:50:55,536 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:51:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:00,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:51:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:02,761 main INFO screen ANONBATON pass=0 dev=0.0 ins=36.67 pro=7 1a=False 1b=False 2=True (9.0s)
Sep 12 14:51:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:14,952 main INFO screen Rexler pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.5s)
Sep 12 14:51:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:19,207 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:51:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:26,297 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 12 14:51:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:27,177 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:51:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:32,250 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:51:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:32,508 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (2.3s)
Sep 12 14:51:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:51:45,431 main INFO screen STUNKINU pass=0 dev=0.46 ins=70.19 pro=2 1a=True 1b=True 2=True (18.3s)
Sep 12 14:52:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:52:06,046 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:52:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:52:11,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:52:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:52:13,437 main INFO screen Pepe pass=0 dev=0.45 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 12 14:52:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:52:21,232 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 14:53:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 14:53:13,608 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:14:53:13 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T13:54:38Z
--- update 2026-09-12T13:59:47Z
--- update 2026-09-12T14:04:59Z
nieuwe code: 9a7e741
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 367f286af9504770be86685502142335
analyses gestart (6b9b2315b322)
--- update 2026-09-12T14:10:11Z
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
