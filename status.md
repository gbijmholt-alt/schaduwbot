# Schaduwbot status

- tijd: 2026-09-11 11:43:39 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 21 hours, 56 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 593/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 6834, "tokens_in_memory": 1764, "msgs": 544022, "trades": 135968, "creates": 1764, "decode_fail": 6045, "rpc_calls": 2090, "rpc_errors": 253, "sol_usd": 99.24828656858952, "open_positions": 78, "log_all_trades": true}
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
Sep 11 11:27:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:27:51,547 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:27:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:27:55,795 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.4s)
Sep 11 11:28:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:28:15,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:28:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:28:15,461 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:28:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:28:15,840 main INFO screen Launchpad pass=0 dev=0.0 ins=7.25 pro=28 1a=False 1b=False 2=True (0.6s)
Sep 11 11:28:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:28:38,620 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:28:38 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:28:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:28:59,698 main INFO screen beer pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 11:29:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:29:03,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:29:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:29:03,582 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:29:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:29:09,427 main INFO screen AERXOL pass=0 dev=0.0 ins=49.59 pro=7 1a=False 1b=False 2=True (6.0s)
Sep 11 11:29:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:29:13,733 main INFO screen lemoncat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 11 11:29:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:29:26,675 main INFO screen ch pass=0 dev=1.43 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 11:30:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:30:03,426 main INFO screen APCATE pass=0 dev=4.3 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 11 11:30:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:30:13,410 main INFO screen CPZ pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (8.2s)
Sep 11 11:30:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:30:56,759 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 11 11:31:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:01,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:31:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:02,067 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:31:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:02,195 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 11:31:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:49,136 main INFO screen SXSN pass=0 dev=1.64 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 11 11:31:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:58,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:31:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:58,775 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:31:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:31:58,890 main INFO screen Manifesto pass=0 dev=0.0 ins=49.83 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 11 11:32:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:32:03,633 main INFO screen ZZZ pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.0s)
Sep 11 11:32:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:32:06,191 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:32:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:32:06,313 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:32:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:32:06,424 main INFO screen SAD DOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 11:32:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:32:42,756 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:11:32:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 11:33:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:33:17,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:33:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:33:17,740 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:33:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:33:17,948 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 11:33:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:33:38,901 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:33:38 +0000] "GET /health HTTP/1.1" 200 445 "-" "Python-urllib/3.14"
Sep 11 11:34:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:16,224 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:34:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:16,320 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:34:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:16,508 main INFO screen TEIEFCAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 11:34:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:45,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:34:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:45,590 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:34:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:45,808 main INFO screen PIPE pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 11:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:52,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:52,334 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:34:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:52,465 main INFO screen YELL pass=0 dev=0.0 ins=38.59 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 11 11:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:58,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:58,944 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:34:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:34:59,076 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 11:36:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:36:07,566 main INFO screen legend pass=0 dev=0.31 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 11:36:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:36:24,139 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:36:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:36:24,235 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:36:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:36:24,428 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:37:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:40,579 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 11:37:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:42,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:37:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:42,220 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:37:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:42,332 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 11:37:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:46,065 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:37:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:46,189 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:37:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:37:46,308 main INFO screen TNT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 11:38:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:39,098 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:38:39 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:38:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:41,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:38:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:41,984 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:38:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:42,216 main INFO screen PEPENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:39:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:46,867 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:39:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:47,009 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:39:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:47,208 main INFO screen Nikki pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,357 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,442 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,606 main INFO screen THUG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,710 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,835 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,960 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 11:40:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:31,017 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 11:40:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:45,144 main INFO screen Animalio pass=0 dev=0.07 ins=27.64 pro=12 1a=False 1b=False 2=False (3.8s)
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,494 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,669 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,908 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.5s)
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,659 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,849 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,345 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,469 main INFO screen BULLSTER pass=0 dev=0.0 ins=37.77 pro=15 1a=False 1b=False 2=True (0.3s)
Sep 11 11:42:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:59,027 main INFO screen BUFF pass=0 dev=1.23 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 11:43:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:43:39,363 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:43:39 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T11:08:05Z
--- update 2026-09-11T11:13:36Z
--- update 2026-09-11T11:18:37Z
--- update 2026-09-11T11:23:37Z
--- update 2026-09-11T11:28:37Z
--- update 2026-09-11T11:33:37Z
--- update 2026-09-11T11:38:38Z
--- update 2026-09-11T11:43:38Z
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
