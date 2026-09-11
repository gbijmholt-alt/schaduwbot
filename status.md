# Schaduwbot status

- tijd: 2026-09-11 12:46:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 22 hours, 59 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 629/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 10612, "tokens_in_memory": 2670, "msgs": 908896, "trades": 218816, "creates": 2670, "decode_fail": 13706, "rpc_calls": 3667, "rpc_errors": 370, "sol_usd": 101.07008472367849, "open_positions": 54, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 11:49 UTC

Gelogde schaduwtrades: **22005**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 12621 | 1705 | 23 | 1705 | 109 | 3291 | 9650 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 250 | 15% | 1.6% | +41.0% | -16.2% | -7.54% | 98% |
| dip35_V1_gescreend_fail | 2212 | 26% | 3.8% | +46.2% | -26.0% | -6.99% | 100% |
| dip35_V1_alle | 2542 | 26% | 3.9% | +45.0% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 249 | 18% | 2.0% | +39.4% | -21.1% | -10.15% | 100% |
| dip35_V2_gescreend_fail | 2217 | 24% | 4.5% | +56.6% | -28.4% | -7.67% | 100% |
| dip35_V2_alle | 2524 | 24% | 4.6% | +54.6% | -28.0% | -8.37% | 100% |
| dip35_V3_gescreend_pass | 251 | 7% | 2.4% | +137.5% | -22.9% | -12.01% | 100% |
| dip35_V3_gescreend_fail | 2255 | 13% | 6.3% | +117.5% | -30.1% | -10.72% | 100% |
| dip35_V3_alle | 2559 | 13% | 6.2% | +115.1% | -29.6% | -11.31% | 100% |
| dip40_V1_gescreend_pass | 232 | 14% | 1.7% | +43.1% | -15.7% | -7.57% | 98% |
| dip40_V1_gescreend_fail | 2153 | 26% | 3.7% | +48.1% | -26.0% | -6.52% | 100% |
| dip40_V1_alle | 2445 | 25% | 3.8% | +47.1% | -25.2% | -6.91% | 100% |
| dip40_V2_gescreend_pass | 231 | 14% | 2.2% | +49.8% | -20.1% | -10.41% | 100% |
| dip40_V2_gescreend_fail | 2149 | 25% | 4.1% | +56.0% | -28.3% | -7.41% | 100% |
| dip40_V2_alle | 2423 | 24% | 4.3% | +55.2% | -27.7% | -8.14% | 100% |
| dip40_V3_gescreend_pass | 233 | 6% | 2.6% | +114.0% | -21.9% | -13.69% | 100% |
| dip40_V3_gescreend_fail | 2189 | 13% | 5.8% | +105.0% | -29.8% | -12.25% | 100% |
| dip40_V3_alle | 2461 | 12% | 5.8% | +103.6% | -29.3% | -12.82% | 100% |
| dip45_V1_gescreend_pass | 221 | 14% | 1.8% | +50.1% | -15.6% | -6.09% | 97% |
| dip45_V1_gescreend_fail | 2093 | 27% | 3.3% | +49.6% | -25.6% | -4.99% | 100% |
| dip45_V1_alle | 2358 | 26% | 3.4% | +49.3% | -24.8% | -5.37% | 100% |
| dip45_V2_gescreend_pass | 218 | 19% | 2.3% | +49.7% | -19.7% | -6.64% | 98% |
| dip45_V2_gescreend_fail | 2078 | 25% | 3.8% | +59.1% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2330 | 25% | 3.9% | +58.0% | -27.2% | -6.24% | 100% |
| dip45_V3_gescreend_pass | 221 | 7% | 2.7% | +186.5% | -21.0% | -6.88% | 99% |
| dip45_V3_gescreend_fail | 2112 | 14% | 5.6% | +111.6% | -29.3% | -9.73% | 100% |
| dip45_V3_alle | 2363 | 13% | 5.6% | +113.5% | -28.8% | -9.85% | 100% |

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
| met_xlink | 1710 | 12% | 2.6% | -9.94% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 12:32:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:32:39,830 main INFO screen RICK pass=0 dev=9.92 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 12:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:33:44,285 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:33:44,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:33:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:33:44,557 main INFO screen PONSFLY pass=0 dev=0.0 ins=79.22 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 12:33:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:33:49,127 main INFO screen Meow pass=1 dev=0.0 ins=17.96 pro=15 1a=False 1b=False 2=False (1.7s)
Sep 11 12:34:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:00,942 main INFO screen .sol pass=0 dev=0.0 ins=25.43 pro=44 1a=False 1b=False 2=False (2.1s)
Sep 11 12:34:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:04,427 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 12:34:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:05,587 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 12:34:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:20,523 main INFO screen Launchcat pass=0 dev=0.54 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 12:34:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:25,683 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:12:34:25 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 12:34:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:26,035 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:12:34:26 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 12:34:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:35,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:34:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:35,708 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:34:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:34:35,902 main INFO screen FATMUSIC pass=0 dev=0.0 ins=6.83 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 12:35:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:35:34,850 main INFO screen FLS pass=0 dev=0.08 ins=0.04 pro=1 1a=False 1b=False 2=False (3.5s)
Sep 11 12:35:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:35:37,813 main INFO screen TOBY pass=0 dev=0.35 ins=37.77 pro=18 1a=False 1b=False 2=True (4.6s)
Sep 11 12:36:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:14,895 main INFO screen MONNY pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 11 12:36:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:30,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:31,376 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:36:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:31,986 main INFO screen ZGIGA pass=0 dev=0.0 ins=38.48 pro=2 1a=False 1b=False 2=True (1.6s)
Sep 11 12:36:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:32,160 main INFO screen sol pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 12:36:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:36:33,371 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:36:33 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:38:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:03,578 main INFO screen FEPE pass=0 dev=0.07 ins=35.06 pro=12 1a=False 1b=False 2=True (6.1s)
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,187 main INFO screen b pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,389 main INFO screen LEPRECHAUN pass=0 dev=0.24 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,639 main INFO screen cap pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,765 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:38:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:29,871 main INFO screen $1 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,639 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:38:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:53,944 main INFO screen Google pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 12:38:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:38:54,008 main INFO screen 100 pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 12:39:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:39:40,566 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.0s)
Sep 11 12:40:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:40:17,716 main INFO screen $CAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 12:40:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:40:27,368 main INFO screen Rufus pass=0 dev=1.2 ins=17.43 pro=21 1a=False 1b=False 2=True (1.2s)
Sep 11 12:41:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:12,822 main INFO screen 34% pass=0 dev=12.57 ins=0.0 pro=2 1a=False 1b=False 2=True (2.3s)
Sep 11 12:41:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:12,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:41:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:13,208 main INFO screen Launchcat pass=0 dev=0.53 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 12:41:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:34,539 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:41:34 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 12:41:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:51,173 main INFO screen kitty pass=0 dev=1.92 ins=16.6 pro=15 1a=False 1b=False 2=True (1.9s)
Sep 11 12:41:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:41:52,690 main INFO screen LMAO pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 11 12:42:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:09,108 main INFO screen me pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 12:42:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:24,240 main INFO screen CHAROC pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 11 12:42:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:25,006 main INFO screen TRANS pass=0 dev=0.48 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 12:42:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:30,777 main INFO screen Mamiko pass=1 dev=0.0 ins=6.6 pro=46 1a=False 1b=False 2=False (3.4s)
Sep 11 12:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:33,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:33,592 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:42:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:34,013 main INFO screen MEME pass=0 dev=0.0 ins=36.47 pro=10 1a=False 1b=False 2=True (1.0s)
Sep 11 12:42:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:34,329 main INFO screen b pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,128 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,277 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:42:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:42:45,393 main INFO screen KALSHE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,620 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:00,818 main INFO screen SUN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,106 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:43:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:43:31,330 main INFO screen STONKY pass=0 dev=0.0 ins=47.36 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 12:44:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:15,075 main INFO screen TURAGE pass=0 dev=0.13 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 11 12:44:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:16,233 main INFO screen LEPRECHAUN pass=0 dev=0.47 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,563 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:44:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:33,748 main INFO screen FLY BRAIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 12:44:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:49,672 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:44:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:49,806 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:44:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:44:50,015 main INFO screen b pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 12:45:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:00,403 main INFO screen FLS pass=0 dev=0.07 ins=0.1 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 11 12:45:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:02,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:45:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:02,917 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:45:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:03,072 main INFO screen SAVAGE pass=0 dev=0.0 ins=37.77 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 11 12:45:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:08,962 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:45:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:09,122 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:45:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:09,263 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 12:45:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:45:17,151 main INFO screen SOAG pass=1 dev=0.0 ins=12.62 pro=10 1a=False 1b=False 2=False (1.3s)
Sep 11 12:46:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:04,633 main INFO screen job pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,206 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 12:46:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:18,372 main INFO screen chillbrain pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 11 12:46:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 12:46:37,158 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:12:46:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T11:18:37Z
--- update 2026-09-11T11:23:37Z
--- update 2026-09-11T11:28:37Z
--- update 2026-09-11T11:33:37Z
--- update 2026-09-11T11:38:38Z
--- update 2026-09-11T11:43:38Z
--- update 2026-09-11T11:49:07Z
--- update 2026-09-11T11:54:33Z
--- update 2026-09-11T11:59:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 91d89b5fe55047b9bdf833a434bfc1f0
analyses gestart (8213ec5e675e)
--- update 2026-09-11T12:05:15Z
--- update 2026-09-11T12:10:30Z
--- update 2026-09-11T12:15:36Z
--- update 2026-09-11T12:20:40Z
--- update 2026-09-11T12:26:02Z
--- update 2026-09-11T12:31:19Z
--- update 2026-09-11T12:36:32Z
--- update 2026-09-11T12:41:33Z
--- update 2026-09-11T12:46:36Z
```

## Analyses (laatste 25 regels)
```
inactive
09:54:59 25844 tokens geladen
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
