# Schaduwbot status

- tijd: 2026-09-11 11:02:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 21 hours, 15 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 577/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 4372, "tokens_in_memory": 1138, "msgs": 358650, "trades": 88519, "creates": 1138, "decode_fail": 4147, "rpc_calls": 1566, "rpc_errors": 140, "sol_usd": 98.98599161703449, "open_positions": 56, "log_all_trades": true}
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
Sep 11 10:52:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:52:29,064 main INFO screen zokkun pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (2.7s)
Sep 11 10:53:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:05,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:53:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:05,524 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:53:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:05,716 main INFO screen BLUEY pass=0 dev=0.0 ins=38.88 pro=16 1a=False 1b=False 2=True (0.4s)
Sep 11 10:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:44,358 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:44,456 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:53:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:44,642 main INFO screen DELULU pass=0 dev=0.0 ins=17.09 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 10:53:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:50,711 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:53:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:50,800 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:53:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:53:50,964 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 10:54:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:54:17,471 main INFO screen SVGCAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 10:54:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:54:37,572 main INFO screen MEME pass=0 dev=0.0 ins=12.45 pro=31 1a=False 1b=False 2=True (2.9s)
Sep 11 10:54:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:54:59,485 main INFO screen BPCATE pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 10:55:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:55:19,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:55:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:55:19,763 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:55:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:55:19,988 main INFO screen ROPE pass=0 dev=0.0 ins=22.02 pro=22 1a=False 1b=False 2=True (0.4s)
Sep 11 10:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:55:29,420 main INFO screen iPod pass=0 dev=0.0 ins=16.39 pro=12 1a=False 1b=False 2=True (3.7s)
Sep 11 10:56:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:56:31,578 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:56:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:56:31,682 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:56:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:56:32,027 main INFO screen IRA pass=0 dev=0.0 ins=14.62 pro=25 1a=False 1b=False 2=True (0.5s)
Sep 11 10:56:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:56:53,710 main INFO screen SempakCoi pass=0 dev=1.84 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 10:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:57:37,039 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:57:37 +0000] "GET /health HTTP/1.1" 200 445 "-" "Python-urllib/3.14"
Sep 11 10:57:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:57:43,799 main INFO screen GrokInu pass=0 dev=0.41 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 10:57:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:57:49,489 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:57:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:57:49,630 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:57:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:57:49,753 main INFO screen MEME pass=0 dev=0.0 ins=49.5 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 11 10:58:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:05,945 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:58:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:06,035 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:58:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:06,227 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 10:58:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:53,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:58:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:53,520 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:58:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:58:57,310 main INFO screen fish pass=0 dev=0.0 ins=20.34 pro=14 1a=False 1b=False 2=True (3.9s)
Sep 11 10:59:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:06,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:59:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:06,759 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:59:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:06,882 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 10:59:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:50,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:59:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:50,350 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:59:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:59:50,544 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:00:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:00:16,897 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:00:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:00:16,997 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:00:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:00:23,114 main INFO screen JUGGCAT pass=0 dev=0.0 ins=79.13 pro=9 1a=False 1b=False 2=True (6.3s)
Sep 11 11:01:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:01:02,341 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:01:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:01:02,403 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:01:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:01:07,097 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 11 11:01:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:01:47,765 main INFO screen Ballish pass=1 dev=0.0 ins=12.5 pro=31 1a=False 1b=False 2=False (5.6s)
Sep 11 11:02:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:04,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:02:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:04,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:02:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:08,294 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 11 11:02:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:15,303 aiohttp.access INFO 185.226.92.153 [11/Sep/2026:11:02:15 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 11:02:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:17,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:02:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:17,929 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:02:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:24,326 main INFO screen TIT pass=0 dev=0.0 ins=36.04 pro=19 1a=False 1b=False 2=True (6.5s)
Sep 11 11:02:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:29,679 main INFO screen WORKMONK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.0s)
Sep 11 11:02:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:36,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:02:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:36,808 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:02:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:02:36,930 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:02:36 +0000] "GET /health HTTP/1.1" 200 445 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T10:57:35Z
--- update 2026-09-11T11:02:35Z
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
