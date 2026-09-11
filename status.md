# Schaduwbot status

- tijd: 2026-09-11 15:42:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 1 hour, 55 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 759/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 21172, "tokens_in_memory": 6107, "msgs": 2319635, "trades": 541980, "creates": 6107, "decode_fail": 43373, "rpc_calls": 9225, "rpc_errors": 898, "sol_usd": 103.31389838744927, "open_positions": 76, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 14:49 UTC

Gelogde schaduwtrades: **24489**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 15864 | 2207 | 24 | 2207 | 145 | 4118 | 12134 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 273 | 15% | 1.5% | +41.0% | -15.9% | -7.53% | 99% |
| dip35_V1_gescreend_fail | 2474 | 26% | 3.8% | +45.6% | -26.0% | -7.17% | 100% |
| dip35_V1_alle | 2832 | 26% | 3.9% | +44.6% | -25.3% | -7.50% | 100% |
| dip35_V2_gescreend_pass | 272 | 18% | 2.2% | +39.7% | -21.0% | -10.30% | 100% |
| dip35_V2_gescreend_fail | 2476 | 25% | 4.5% | +56.2% | -28.4% | -7.66% | 100% |
| dip35_V2_alle | 2810 | 24% | 4.6% | +54.4% | -28.0% | -8.35% | 100% |
| dip35_V3_gescreend_pass | 274 | 7% | 2.2% | +133.5% | -22.4% | -11.58% | 100% |
| dip35_V3_gescreend_fail | 2512 | 13% | 6.2% | +110.4% | -30.0% | -11.43% | 100% |
| dip35_V3_alle | 2843 | 13% | 6.1% | +108.7% | -29.5% | -11.87% | 100% |
| dip40_V1_gescreend_pass | 253 | 13% | 1.6% | +42.9% | -15.3% | -7.52% | 99% |
| dip40_V1_gescreend_fail | 2406 | 26% | 3.8% | +47.8% | -25.9% | -6.67% | 100% |
| dip40_V1_alle | 2722 | 25% | 3.8% | +46.9% | -25.1% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 252 | 14% | 2.4% | +49.8% | -20.0% | -10.59% | 100% |
| dip40_V2_gescreend_fail | 2400 | 25% | 4.2% | +55.8% | -28.2% | -7.50% | 100% |
| dip40_V2_alle | 2697 | 24% | 4.3% | +55.1% | -27.6% | -8.20% | 100% |
| dip40_V3_gescreend_pass | 254 | 6% | 2.4% | +112.1% | -21.4% | -13.48% | 100% |
| dip40_V3_gescreend_fail | 2438 | 13% | 5.8% | +98.8% | -29.7% | -13.01% | 100% |
| dip40_V3_alle | 2733 | 12% | 5.7% | +97.8% | -29.1% | -13.44% | 100% |
| dip45_V1_gescreend_pass | 242 | 14% | 1.7% | +49.5% | -15.3% | -6.19% | 98% |
| dip45_V1_gescreend_fail | 2338 | 27% | 3.4% | +49.5% | -25.6% | -5.01% | 100% |
| dip45_V1_alle | 2626 | 26% | 3.4% | +49.2% | -24.8% | -5.38% | 100% |
| dip45_V2_gescreend_pass | 240 | 18% | 2.5% | +49.2% | -19.7% | -7.34% | 99% |
| dip45_V2_gescreend_fail | 2320 | 25% | 3.8% | +58.7% | -27.7% | -5.99% | 100% |
| dip45_V2_alle | 2596 | 24% | 3.9% | +57.7% | -27.1% | -6.49% | 100% |
| dip45_V3_gescreend_pass | 242 | 7% | 2.5% | +180.2% | -20.6% | -7.31% | 100% |
| dip45_V3_gescreend_fail | 2356 | 14% | 5.6% | +112.8% | -29.2% | -9.68% | 100% |
| dip45_V3_alle | 2630 | 13% | 5.5% | +114.4% | -28.6% | -9.82% | 100% |

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
| met_xlink | 1861 | 12% | 2.6% | -10.03% | 100% |
| zonder_xlink | 441 | 13% | 0.0% | -5.41% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 15:29:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:33,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:29:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:33,320 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:29:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:39,947 main INFO screen $DM2K pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 15:29:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:49,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:29:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:49,734 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:29:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:53,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:29:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:53,260 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:29:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:53,695 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.2s)
Sep 11 15:29:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:56,013 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 11 15:29:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:29:56,767 main INFO screen Puter pass=1 dev=0.0 ins=19.18 pro=10 1a=False 1b=False 2=False (3.7s)
Sep 11 15:31:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:36,990 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:31:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:37,088 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:31:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:37,147 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:31:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:31:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:37,277 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:31:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:42,179 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:31:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:42,242 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:31:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:31:42,425 main INFO screen FLYBRAIN pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 15:32:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:22,471 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:32:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:22,648 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:32:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:22,808 main INFO screen KEVIN pass=0 dev=0.0 ins=24.76 pro=20 1a=False 1b=False 2=True (0.4s)
Sep 11 15:32:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:31,794 main INFO screen SAVPIR pass=0 dev=0.07 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 11 15:32:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:50,033 main INFO screen SOLFATE pass=0 dev=0.0 ins=12.52 pro=19 1a=False 1b=False 2=True (1.5s)
Sep 11 15:32:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:32:51,725 main INFO screen kanaka pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 15:33:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:02,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:33:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:03,034 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:33:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:03,388 main INFO screen 9/11 pass=0 dev=0.0 ins=18.41 pro=20 1a=False 1b=False 2=True (0.6s)
Sep 11 15:33:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:19,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:33:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:19,811 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:33:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:20,377 main INFO screen 9/11 pass=0 dev=0.0 ins=14.2 pro=17 1a=False 1b=False 2=True (0.8s)
Sep 11 15:33:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:22,679 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:33:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:22,829 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:33:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:22,960 main INFO screen Leafy pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:33:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:48,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:33:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:48,548 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:33:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:33:48,739 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 15:34:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:07,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:34:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:07,842 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:34:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:08,096 main INFO screen HOMO pass=1 dev=0.0 ins=3.42 pro=28 1a=False 1b=False 2=False (0.5s)
Sep 11 15:34:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:23,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:34:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:23,539 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:34:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:23,767 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:34:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:51,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:34:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:51,902 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:52,145 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 15:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:52,431 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:52,553 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:58,340 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:58,510 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:58,661 main INFO screen FLYBRAIN pass=0 dev=0.0 ins=78.04 pro=5 1a=False 1b=False 2=True (0.3s)
Sep 11 15:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:34:58,819 main INFO screen 9/10/11 pass=0 dev=0.0 ins=9.84 pro=20 1a=False 1b=False 2=True (6.5s)
Sep 11 15:35:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:35:05,937 aiohttp.access INFO 144.202.92.17 [11/Sep/2026:15:35:05 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; CyberConvoyScout/1.0; +https://scout.cyberconvoy.co)"
Sep 11 15:35:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:35:35,542 main INFO screen SWIFTIEPHYLUS pass=0 dev=0.0 ins=20.14 pro=16 1a=False 1b=False 2=False (1.6s)
Sep 11 15:35:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:35:44,519 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:35:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:35:44,614 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:35:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:35:44,957 main INFO screen DOGEIUS pass=0 dev=0.0 ins=19.48 pro=25 1a=False 1b=False 2=True (0.5s)
Sep 11 15:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:36:31,028 main INFO screen dot pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 11 15:36:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:36:33,272 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:36:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:36:33,345 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:36:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:36:33,525 main INFO screen BRAINSAHUR pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 15:37:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:37:24,485 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:37:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:37:24,584 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:37:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:37:25,325 main INFO screen ZAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.9s)
Sep 11 15:37:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:37:25,794 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:37:25 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
Sep 11 15:39:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:39:07,056 main INFO screen witz  pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 11 15:40:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:40:06,559 main INFO screen $CAT pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 11 15:40:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:40:44,734 main INFO screen MOODENG pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 11 15:40:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:40:54,847 aiohttp.access INFO 20.106.19.228 [11/Sep/2026:15:40:54 +0000] "GET /hudson HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 11 15:41:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:13,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:41:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:14,059 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:41:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:14,245 main INFO screen USJC pass=0 dev=0.0 ins=79.13 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 15:41:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:24,156 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:41:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:24,324 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:41:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:24,449 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:41:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:41:56,128 main INFO screen RICK pass=0 dev=0.31 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 15:42:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:01,481 main INFO screen $CAJUN pass=0 dev=0.63 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 11 15:42:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:09,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 15:42:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:10,175 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 15:42:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:10,324 main INFO screen BOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 15:42:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:26,198 main INFO screen MICROFLY pass=0 dev=0.0 ins=6.06 pro=50 1a=False 1b=True 2=True (2.9s)
Sep 11 15:42:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 15:42:37,252 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:15:42:37 +0000] "GET /health HTTP/1.1" 200 450 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (8213ec5e675e)
--- update 2026-09-11T14:08:04Z
--- update 2026-09-11T14:13:36Z
--- update 2026-09-11T14:18:46Z
--- update 2026-09-11T14:23:51Z
--- update 2026-09-11T14:29:07Z
--- update 2026-09-11T14:34:22Z
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
--- update 2026-09-11T14:49:38Z
--- update 2026-09-11T14:54:48Z
--- update 2026-09-11T15:00:22Z
--- update 2026-09-11T15:05:25Z
--- update 2026-09-11T15:10:36Z
--- update 2026-09-11T15:15:48Z
--- update 2026-09-11T15:21:20Z
--- update 2026-09-11T15:26:33Z
--- update 2026-09-11T15:31:36Z
--- update 2026-09-11T15:37:24Z
--- update 2026-09-11T15:42:36Z
```

## Analyses (laatste 25 regels)
```
inactive
11:59:48   4000 tokens, 797956 trades, 237448 posities (8s)
11:59:53   6000 tokens, 1196480 trades, 358550 posities (13s)
11:59:53 posities: 377872 uit 1255975 trades (13s)
11:59:59 84645 wallets gerekend
11:59:59 geluk-toets
12:00:15 persistentie
12:00:16 kopieer-simulatie
12:00:21 klaar in 41s -> /opt/schaduwbot/reports/wallets.md
14:02:53 5048 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
14:02:56   ingelezen tot rowid 1452718 (196794 rijen, 196794 bruikbaar)
14:02:56 ingelezen: 196794 nieuwe trades, 196794 bruikbaar (3s)
14:02:59 klaar in 6s -> /opt/schaduwbot/reports/ledger.md
14:03:01 klaar in 2s: 1642 tokens, 1877 nieuw -> /opt/schaduwbot/reports/video_replay.md
14:03:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 14:03 UTC
14:03:01 29885 tokens geladen
14:03:05   2000 tokens, 356777 trades, 100453 posities (4s)
14:03:09   4000 tokens, 700400 trades, 193583 posities (7s)
14:03:12   6000 tokens, 1047800 trades, 291369 posities (11s)
14:03:16   8000 tokens, 1402251 trades, 394081 posities (15s)
14:03:16 posities: 409300 uit 1453102 trades (15s)
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
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
