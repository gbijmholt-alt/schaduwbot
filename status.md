# Schaduwbot status

- tijd: 2026-09-11 10:52:19 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 21 hours, 5 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 573/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3754, "tokens_in_memory": 941, "msgs": 289817, "trades": 72407, "creates": 941, "decode_fail": 3566, "rpc_calls": 1351, "rpc_errors": 112, "sol_usd": 99.28222694209818, "open_positions": 49, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 10:49 UTC

Gelogde schaduwtrades: **21403**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 11683 | 1592 | 22 | 1592 | 106 | 3088 | 9048 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 247 | 15% | 1.6% | +41.0% | -16.3% | -7.52% | 98% |
| dip35_V1_gescreend_fail | 2149 | 26% | 3.9% | +46.4% | -26.2% | -6.94% | 100% |
| dip35_V1_alle | 2476 | 26% | 4.0% | +45.1% | -25.5% | -7.33% | 100% |
| dip35_V2_gescreend_pass | 245 | 18% | 2.0% | +40.2% | -21.1% | -10.06% | 100% |
| dip35_V2_gescreend_fail | 2149 | 24% | 4.5% | +57.2% | -28.6% | -7.65% | 100% |
| dip35_V2_alle | 2452 | 24% | 4.6% | +55.1% | -28.2% | -8.36% | 100% |
| dip35_V3_gescreend_pass | 247 | 7% | 2.4% | +137.5% | -22.9% | -11.89% | 100% |
| dip35_V3_gescreend_fail | 2187 | 13% | 6.3% | +115.8% | -30.2% | -11.29% | 100% |
| dip35_V3_alle | 2487 | 12% | 6.2% | +113.5% | -29.7% | -11.81% | 100% |
| dip40_V1_gescreend_pass | 229 | 14% | 1.7% | +43.2% | -15.8% | -7.79% | 98% |
| dip40_V1_gescreend_fail | 2092 | 26% | 3.8% | +48.3% | -26.1% | -6.46% | 100% |
| dip40_V1_alle | 2381 | 26% | 3.9% | +47.3% | -25.4% | -6.89% | 100% |
| dip40_V2_gescreend_pass | 227 | 14% | 1.8% | +49.8% | -19.8% | -9.99% | 100% |
| dip40_V2_gescreend_fail | 2085 | 25% | 4.2% | +56.4% | -28.4% | -7.39% | 100% |
| dip40_V2_alle | 2355 | 24% | 4.2% | +55.6% | -27.8% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 229 | 6% | 2.2% | +114.0% | -21.6% | -13.33% | 100% |
| dip40_V3_gescreend_fail | 2124 | 13% | 5.8% | +103.4% | -29.9% | -12.66% | 100% |
| dip40_V3_alle | 2392 | 12% | 5.8% | +102.0% | -29.4% | -13.16% | 100% |
| dip45_V1_gescreend_pass | 218 | 15% | 1.8% | +50.1% | -15.6% | -5.99% | 96% |
| dip45_V1_gescreend_fail | 2034 | 28% | 3.4% | +49.9% | -25.8% | -4.82% | 100% |
| dip45_V1_alle | 2296 | 26% | 3.5% | +49.5% | -25.0% | -5.23% | 100% |
| dip45_V2_gescreend_pass | 215 | 19% | 2.3% | +49.7% | -19.5% | -6.28% | 97% |
| dip45_V2_gescreend_fail | 2018 | 26% | 3.8% | +59.5% | -27.9% | -5.65% | 100% |
| dip45_V2_alle | 2267 | 25% | 3.9% | +58.4% | -27.4% | -6.14% | 100% |
| dip45_V3_gescreend_pass | 217 | 7% | 2.8% | +186.5% | -20.8% | -6.50% | 99% |
| dip45_V3_gescreend_fail | 2050 | 14% | 5.7% | +110.2% | -29.5% | -10.12% | 100% |
| dip45_V3_alle | 2297 | 13% | 5.7% | +112.3% | -28.9% | -10.17% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1678 | 12% | 2.6% | -9.74% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 10:36:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:36:48,629 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:36:48 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 10:37:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:00,525 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:37:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:00,667 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:37:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:00,848 main INFO screen RETBRAIN pass=0 dev=0.0 ins=79.26 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 10:37:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:02,066 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:37:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:02,193 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:37:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:37:02,318 main INFO screen BOOZY pass=0 dev=0.0 ins=39.08 pro=10 1a=False 1b=False 2=True (0.3s)
Sep 11 10:38:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:38:08,014 main INFO screen PawPal pass=0 dev=0.0 ins=17.22 pro=40 1a=False 1b=False 2=True (2.6s)
Sep 11 10:38:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:38:44,848 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 10:38:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:38:46,016 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 10:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:38:53,428 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:10:38:53 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 10:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:38:53,774 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:10:38:53 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 10:39:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:39:09,537 main INFO screen HALH pass=0 dev=2.8 ins=0.0 pro=6 1a=False 1b=False 2=False (3.0s)
Sep 11 10:39:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:39:48,582 main INFO screen GOGO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 11 10:40:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:40:38,267 main INFO screen baton pass=0 dev=0.0 ins=0.35 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 10:41:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:41:48,849 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:41:48 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 10:42:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:12,635 main INFO screen imposter pass=0 dev=0.0 ins=20.41 pro=70 1a=False 1b=False 2=True (3.4s)
Sep 11 10:42:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:17,121 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:42:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:17,236 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:42:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:19,592 main INFO screen DEGEN pass=0 dev=0.0 ins=24.99 pro=9 1a=False 1b=False 2=True (2.5s)
Sep 11 10:42:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:22,305 main INFO screen BLAZE pass=0 dev=0.35 ins=38.88 pro=20 1a=False 1b=False 2=True (3.4s)
Sep 11 10:42:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:32,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:33,041 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:42:33,145 main INFO screen TELEGRAM pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 10:43:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:17,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:43:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:17,670 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:43:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:19,941 main INFO screen Meme pass=0 dev=0.0 ins=16.85 pro=16 1a=False 1b=False 2=True (2.4s)
Sep 11 10:43:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:42,576 main INFO screen BiteCoin pass=0 dev=26.16 ins=0.0 pro=4 1a=False 1b=False 2=False (1.9s)
Sep 11 10:43:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:47,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:43:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:47,964 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:43:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:48,282 main INFO screen air pass=0 dev=0.0 ins=20.2 pro=22 1a=False 1b=False 2=False (0.5s)
Sep 11 10:43:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:57,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:43:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:57,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:43:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:43:57,939 main INFO screen Agbaibor pass=0 dev=0.0 ins=19.96 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 11 10:44:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:44:30,345 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:44:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:44:30,919 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:44:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:44:31,666 main INFO screen BERR pass=0 dev=0.0 ins=46.37 pro=3 1a=False 1b=False 2=True (1.9s)
Sep 11 10:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:44:33,433 main INFO screen DFV pass=0 dev=0.0 ins=17.36 pro=34 1a=False 1b=False 2=True (4.2s)
Sep 11 10:45:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:45:14,838 main INFO screen FLY pass=1 dev=0.0 ins=17.7 pro=23 1a=False 1b=False 2=False (2.5s)
Sep 11 10:45:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:45:53,973 main INFO screen LEMON pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 10:46:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:46:25,013 main INFO screen Stockfathers pass=0 dev=0.0 ins=20.23 pro=57 1a=False 1b=False 2=True (3.2s)
Sep 11 10:47:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:07,495 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:47:07 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 10:47:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:41,733 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:47:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:41,832 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:47:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:42,071 main INFO screen NASPONS pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 10:47:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:52,073 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:47:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:52,202 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:47:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:52,364 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 10:47:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:58,492 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:47:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:58,578 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:47:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:47:58,739 main INFO screen 1 pass=0 dev=0.0 ins=49.42 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 10:48:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:44,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:48:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:44,530 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:48:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:45,756 main INFO screen RUSTY pass=0 dev=0.0 ins=39.09 pro=11 1a=False 1b=False 2=True (1.4s)
Sep 11 10:48:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:49,735 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:48:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:49,858 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:48:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:48:49,983 main INFO screen lastcoin pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 10:50:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:39,101 main INFO screen 91011 pass=1 dev=0.0 ins=9.51 pro=72 1a=False 1b=False 2=False (3.9s)
Sep 11 10:50:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:42,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:50:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:42,199 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:50:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:46,111 main INFO screen Hoodtard pass=0 dev=0.0 ins=21.82 pro=14 1a=False 1b=False 2=True (4.1s)
Sep 11 10:50:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:55,248 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:50:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:55,391 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:50:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:55,526 main INFO screen MINE pass=0 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=True (0.3s)
Sep 11 10:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:57,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:57,670 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:50:57,802 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 10:51:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:06,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:51:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:06,960 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:51:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:07,255 main INFO screen BULLBRAIN pass=0 dev=0.0 ins=79.26 pro=8 1a=False 1b=False 2=True (0.5s)
Sep 11 10:51:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:21,748 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:51:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:21,885 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:51:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:22,051 main INFO screen STOCKSMINE pass=0 dev=0.0 ins=10.07 pro=18 1a=False 1b=False 2=True (0.4s)
Sep 11 10:51:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:50,116 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:51:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:50,215 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:51:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:51:50,394 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 10:52:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:52:17,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:52:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:52:18,060 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:52:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:52:18,250 main INFO screen fone pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 10:52:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:52:19,290 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:52:19 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T09:34:22Z
--- update 2026-09-11T09:39:34Z
--- update 2026-09-11T09:44:36Z
--- update 2026-09-11T09:49:40Z
nieuwe code: 84f1f27
install klaar
--- update 2026-09-11T09:54:51Z
Running as unit: schaduwbot-wallets.service; invocation ID: c6aa21aab9e6404dbc76593d23c99364
analyses gestart (8213ec5e675e)
--- update 2026-09-11T10:00:16Z
--- update 2026-09-11T10:05:31Z
--- update 2026-09-11T10:10:36Z
--- update 2026-09-11T10:16:21Z
--- update 2026-09-11T10:21:20Z
--- update 2026-09-11T10:26:31Z
--- update 2026-09-11T10:31:36Z
--- update 2026-09-11T10:36:47Z
--- update 2026-09-11T10:41:47Z
--- update 2026-09-11T10:47:06Z
--- update 2026-09-11T10:52:18Z
```

## Analyses (laatste 25 regels)
```
inactive
08:52:52 79415 wallets gerekend
08:52:53 geluk-toets
08:53:06 persistentie
08:53:07 kopieer-simulatie
08:53:11 klaar in 34s -> /opt/schaduwbot/reports/wallets.md
09:54:51 1006 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
09:54:53   ingelezen tot rowid 200000 (200000 rijen, 0 bruikbaar)
09:54:54   ingelezen tot rowid 400000 (400000 rijen, 0 bruikbaar)
09:54:55   ingelezen tot rowid 600000 (600000 rijen, 0 bruikbaar)
09:54:56   ingelezen tot rowid 800000 (800000 rijen, 0 bruikbaar)
09:54:57   ingelezen tot rowid 1000000 (1000000 rijen, 0 bruikbaar)
09:54:58   ingelezen tot rowid 1104902 (1104902 rijen, 62330 bruikbaar)
09:54:58 ingelezen: 1104902 nieuwe trades, 62330 bruikbaar (7s)
09:54:59 klaar in 7s -> /opt/schaduwbot/reports/ledger.md
09:54:59 klaar in 0s: 0 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
09:54:59 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 09:54 UTC
09:54:59 25844 tokens geladen
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
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
