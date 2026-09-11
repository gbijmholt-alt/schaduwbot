# Schaduwbot status

- tijd: 2026-09-11 14:02:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 15 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.5G/38G | geheugen: 721/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 15189, "tokens_in_memory": 4112, "msgs": 1285864, "trades": 350252, "creates": 4112, "decode_fail": 29172, "rpc_calls": 6301, "rpc_errors": 572, "sol_usd": 105.47391713559182, "open_positions": 90, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 13:49 UTC

Gelogde schaduwtrades: **23540**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 14630 | 2033 | 23 | 2033 | 139 | 3820 | 11185 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 265 | 15% | 1.5% | +41.0% | -16.1% | -7.69% | 99% |
| dip35_V1_gescreend_fail | 2373 | 26% | 3.8% | +45.7% | -26.0% | -6.98% | 100% |
| dip35_V1_alle | 2723 | 26% | 3.9% | +44.7% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 264 | 17% | 1.9% | +39.3% | -20.9% | -10.39% | 100% |
| dip35_V2_gescreend_fail | 2373 | 25% | 4.4% | +56.1% | -28.5% | -7.59% | 100% |
| dip35_V2_alle | 2699 | 24% | 4.5% | +54.3% | -28.0% | -8.32% | 100% |
| dip35_V3_gescreend_pass | 266 | 7% | 2.3% | +136.1% | -22.6% | -11.87% | 100% |
| dip35_V3_gescreend_fail | 2416 | 13% | 6.2% | +113.0% | -30.0% | -10.92% | 100% |
| dip35_V3_alle | 2739 | 13% | 6.1% | +111.2% | -29.6% | -11.47% | 100% |
| dip40_V1_gescreend_pass | 245 | 14% | 1.6% | +43.0% | -15.6% | -7.69% | 99% |
| dip40_V1_gescreend_fail | 2308 | 26% | 3.7% | +47.9% | -26.0% | -6.42% | 100% |
| dip40_V1_alle | 2616 | 26% | 3.8% | +47.0% | -25.2% | -6.79% | 100% |
| dip40_V2_gescreend_pass | 244 | 13% | 2.0% | +49.8% | -19.9% | -10.78% | 100% |
| dip40_V2_gescreend_fail | 2302 | 25% | 4.1% | +55.6% | -28.2% | -7.34% | 100% |
| dip40_V2_alle | 2591 | 24% | 4.2% | +54.9% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 246 | 6% | 2.4% | +114.0% | -21.6% | -13.86% | 100% |
| dip40_V3_gescreend_fail | 2344 | 13% | 5.8% | +100.3% | -29.7% | -12.63% | 100% |
| dip40_V3_alle | 2631 | 12% | 5.7% | +99.2% | -29.1% | -13.14% | 100% |
| dip45_V1_gescreend_pass | 234 | 14% | 1.7% | +49.5% | -15.5% | -6.09% | 98% |
| dip45_V1_gescreend_fail | 2242 | 28% | 3.3% | +49.2% | -25.6% | -4.83% | 100% |
| dip45_V1_alle | 2522 | 27% | 3.4% | +48.8% | -24.8% | -5.23% | 100% |
| dip45_V2_gescreend_pass | 232 | 18% | 2.2% | +49.0% | -19.6% | -7.18% | 99% |
| dip45_V2_gescreend_fail | 2225 | 26% | 3.7% | +58.4% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2493 | 25% | 3.8% | +57.4% | -27.2% | -6.27% | 100% |
| dip45_V3_gescreend_pass | 234 | 6% | 2.6% | +186.5% | -20.8% | -7.50% | 100% |
| dip45_V3_gescreend_fail | 2260 | 14% | 5.6% | +107.1% | -29.3% | -10.26% | 100% |
| dip45_V3_alle | 2526 | 13% | 5.5% | +109.2% | -28.7% | -10.37% | 100% |

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
| met_xlink | 1819 | 12% | 2.5% | -10.15% | 100% |
| zonder_xlink | 411 | 13% | 0.0% | -5.49% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 13:50:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:50:47,928 main INFO screen NOSE pass=0 dev=0.0 ins=9.0 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 11 13:50:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:50:53,482 main INFO screen SAVPIR pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (3.0s)
Sep 11 13:50:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:50:56,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:50:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:50:56,286 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:50:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:50:56,440 main INFO screen EMBERCHUMP pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 13:51:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:09,772 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:51:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:09,877 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:51:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:10,030 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 13:51:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:29,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:51:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:29,745 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:51:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:51:29,962 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 13:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:15,400 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:15,502 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:52:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:15,693 main INFO screen Faucet pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:52:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:21,918 main INFO screen GAYS pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 13:52:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:28,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:52:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:29,393 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:52:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:29,950 main INFO screen pipejak pass=0 dev=0.0 ins=79.13 pro=7 1a=False 1b=False 2=True (1.8s)
Sep 11 13:52:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:30,759 main INFO screen pill pass=0 dev=0.0 ins=20.14 pro=73 1a=False 1b=False 2=True (4.4s)
Sep 11 13:52:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:37,245 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:52:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 13:52:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:52:39,694 main INFO screen ACCUSE pass=0 dev=35.84 ins=0.0 pro=9 1a=False 1b=False 2=True (2.2s)
Sep 11 13:53:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:08,166 main INFO screen OOZARU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 13:53:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:12,955 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:53:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:13,596 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:53:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:14,141 main INFO screen CCS pass=0 dev=0.0 ins=20.17 pro=5 1a=False 1b=False 2=True (1.7s)
Sep 11 13:53:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:14,652 main INFO screen USMS pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.5s)
Sep 11 13:53:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:27,909 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:53:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:28,073 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:53:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:28,214 main INFO screen FPC pass=0 dev=0.0 ins=77.42 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 11 13:53:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:53:53,399 main INFO screen TRANSDAD pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 13:54:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:00,677 main INFO screen LPC pass=0 dev=2.53 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 13:54:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:10,657 main INFO screen CHADSTER pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 13:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:37,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:37,959 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:54:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:38,192 main INFO screen PIPEJAK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:54:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:48,662 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:54:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:48,789 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:54:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:49,176 main INFO screen believe pass=0 dev=0.0 ins=18.58 pro=18 1a=False 1b=False 2=True (0.6s)
Sep 11 13:54:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:52,142 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:54:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:52,268 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:54:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:52,418 main INFO screen NUTS pass=0 dev=0.0 ins=25.57 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 13:54:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:57,348 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:54:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:57,431 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:54:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:54:57,622 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 13:55:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:55:36,180 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:55:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:55:36,268 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:55:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:55:36,467 main INFO screen STOCAT pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:56:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:34,772 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:56:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:34,872 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:56:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:35,058 main INFO screen BI6900 pass=0 dev=0.0 ins=21.35 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 13:56:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:42,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:56:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:43,040 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:56:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:56:43,182 main INFO screen help pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 13:57:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:07,098 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:57:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:07,185 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:57:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:07,376 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 13:57:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:34,839 main INFO screen help pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 13:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:37,466 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:37,593 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:37,724 main INFO screen USESTONK pass=0 dev=0.0 ins=77.57 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 13:57:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:57:49,385 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:13:57:49 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 13:58:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:58:00,516 main INFO screen CHADSTER pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 13:58:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:58:13,499 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:58:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:58:13,590 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:58:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:58:13,934 main INFO screen Looksmaxxing pass=0 dev=0.0 ins=26.32 pro=8 1a=False 1b=False 2=True (0.5s)
Sep 11 13:59:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:59:33,861 main INFO screen sh pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 13:59:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:59:48,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 13:59:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:59:49,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 13:59:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 13:59:49,597 main INFO screen ZAN pass=0 dev=0.0 ins=0.01 pro=4 1a=False 1b=False 2=True (3.8s)
Sep 11 14:00:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:00:41,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:00:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:00:41,232 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:00:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:00:41,532 main INFO screen OPAI pass=0 dev=0.0 ins=9.61 pro=32 1a=False 1b=False 2=True (0.5s)
Sep 11 14:01:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:01:27,967 main INFO screen ShoeCoin pass=0 dev=0.09 ins=23.44 pro=18 1a=False 1b=False 2=True (8.9s)
Sep 11 14:01:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:01:32,780 main INFO screen DISPLAY pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.4s)
Sep 11 14:02:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:20,271 main INFO screen $SC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 14:02:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:38,182 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 11 14:02:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:46,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 14:02:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:46,748 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 14:02:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:51,919 main INFO screen TRUMPCAT pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (5.4s)
Sep 11 14:02:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 14:02:53,509 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:14:02:53 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T12:36:32Z
--- update 2026-09-11T12:41:33Z
--- update 2026-09-11T12:46:36Z
--- update 2026-09-11T12:51:41Z
--- update 2026-09-11T12:56:44Z
--- update 2026-09-11T13:01:44Z
--- update 2026-09-11T13:06:49Z
--- update 2026-09-11T13:11:58Z
--- update 2026-09-11T13:16:59Z
--- update 2026-09-11T13:22:01Z
--- update 2026-09-11T13:27:04Z
--- update 2026-09-11T13:32:04Z
--- update 2026-09-11T13:37:17Z
--- update 2026-09-11T13:42:29Z
--- update 2026-09-11T13:47:30Z
--- update 2026-09-11T13:52:36Z
--- update 2026-09-11T13:57:48Z
--- update 2026-09-11T14:02:52Z
Running as unit: schaduwbot-wallets.service; invocation ID: c147433096084aa9b38d9e2b7eb6bf75
analyses gestart (8213ec5e675e)
```

## Analyses (laatste 25 regels)
```
active
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
11:59:36 2892 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
11:59:39   ingelezen tot rowid 1255924 (151022 rijen, 151022 bruikbaar)
11:59:39 ingelezen: 151022 nieuwe trades, 151022 bruikbaar (2s)
11:59:40 klaar in 4s -> /opt/schaduwbot/reports/ledger.md
11:59:40 klaar in 0s: 59 tokens, 67 nieuw -> /opt/schaduwbot/reports/video_replay.md
11:59:40 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 11:59 UTC
11:59:40 27728 tokens geladen
11:59:44   2000 tokens, 398779 trades, 119472 posities (4s)
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
14:02:53 5048 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
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
