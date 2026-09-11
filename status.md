# Schaduwbot status

- tijd: 2026-09-11 22:30:36 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 8 hours, 43 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 791/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 10228, "tokens_in_memory": 3815, "msgs": 2565852, "trades": 450159, "creates": 3815, "decode_fail": 30100, "rpc_calls": 14114, "rpc_errors": 556, "sol_usd": 101.96633988104232, "open_positions": 109, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 21:40 UTC

Gelogde schaduwtrades: **33418**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 25144 | 3869 | 41 | 3866 | 323 | 7170 | 21063 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 392 | 17% | 2.0% | +43.1% | -17.1% | -6.97% | 100% |
| dip35_V1_gescreend_fail | 3269 | 27% | 3.7% | +46.2% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 3872 | 26% | 3.7% | +45.1% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 386 | 21% | 3.1% | +43.9% | -21.8% | -8.06% | 100% |
| dip35_V2_gescreend_fail | 3272 | 25% | 4.3% | +56.7% | -28.3% | -7.31% | 100% |
| dip35_V2_alle | 3828 | 24% | 4.3% | +54.6% | -27.9% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 388 | 8% | 3.6% | +374.3% | -23.1% | +8.68% | 100% |
| dip35_V3_gescreend_fail | 3339 | 13% | 5.9% | +119.3% | -29.8% | -9.88% | 100% |
| dip35_V3_alle | 3878 | 13% | 5.8% | +129.9% | -29.3% | -8.55% | 100% |
| dip40_V1_gescreend_pass | 362 | 15% | 1.9% | +46.6% | -16.2% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 3194 | 26% | 3.7% | +48.0% | -26.0% | -6.60% | 100% |
| dip40_V1_alle | 3721 | 25% | 3.6% | +47.7% | -25.2% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 356 | 16% | 2.5% | +48.9% | -20.4% | -9.09% | 100% |
| dip40_V2_gescreend_fail | 3185 | 25% | 4.2% | +56.0% | -28.2% | -7.32% | 100% |
| dip40_V2_alle | 3670 | 24% | 4.2% | +55.0% | -27.7% | -7.90% | 100% |
| dip40_V3_gescreend_pass | 361 | 7% | 2.8% | +423.8% | -21.4% | +8.19% | 100% |
| dip40_V3_gescreend_fail | 3251 | 13% | 5.7% | +113.9% | -29.6% | -11.00% | 100% |
| dip40_V3_alle | 3725 | 12% | 5.5% | +126.8% | -29.0% | -9.66% | 100% |
| dip45_V1_gescreend_pass | 348 | 16% | 1.7% | +50.0% | -16.0% | -5.37% | 99% |
| dip45_V1_gescreend_fail | 3112 | 27% | 3.2% | +48.6% | -25.7% | -5.39% | 100% |
| dip45_V1_alle | 3593 | 26% | 3.2% | +48.6% | -25.0% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 340 | 19% | 2.4% | +47.9% | -20.1% | -7.29% | 100% |
| dip45_V2_gescreend_fail | 3095 | 25% | 3.8% | +58.7% | -27.9% | -6.12% | 100% |
| dip45_V2_alle | 3543 | 24% | 3.8% | +57.4% | -27.3% | -6.72% | 100% |
| dip45_V3_gescreend_pass | 343 | 7% | 2.3% | +467.9% | -20.6% | +13.58% | 100% |
| dip45_V3_gescreend_fail | 3150 | 14% | 5.3% | +120.8% | -29.1% | -8.30% | 100% |
| dip45_V3_alle | 3588 | 13% | 5.2% | +136.3% | -28.5% | -6.77% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 1.1%, kans ruïne 98.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2548 | 13% | 3.2% | -10.54% | 100% |
| zonder_xlink | 728 | 19% | 0.0% | +30.12% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 22:19:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:19:47,777 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:19:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:19:52,846 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:20:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:11,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:20:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:14,520 main INFO screen MetaMask pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.8s)
Sep 11 22:20:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:19,679 main INFO screen Retail pass=0 dev=0.0 ins=11.89 pro=49 1a=False 1b=False 2=True (8.6s)
Sep 11 22:20:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:36,103 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:20:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:36,191 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:20:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:41,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:20:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:20:41,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:21:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:04,418 main INFO screen GitHub pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.4s)
Sep 11 22:21:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:04,722 main INFO screen QUBO pass=0 dev=0.0 ins=18.59 pro=71 1a=False 1b=False 2=True (28.6s)
Sep 11 22:21:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:06,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:21:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:11,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:21:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:34,250 main INFO screen RETARDFLY pass=0 dev=0.35 ins=41.04 pro=10 1a=False 1b=False 2=True (27.8s)
Sep 11 22:21:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:21:48,339 main INFO screen CRISPE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 11 22:22:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:39,020 main INFO screen Pipi pass=0 dev=0.0 ins=22.85 pro=72 1a=False 1b=False 2=True (12.4s)
Sep 11 22:22:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:42,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:22:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:46,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:22:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:47,292 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:22:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:51,060 main INFO screen Retail pass=1 dev=0.0 ins=10.69 pro=19 1a=False 1b=False 2=False (1.8s)
Sep 11 22:22:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:22:51,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:23:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:06,031 main INFO screen $Power pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (23.8s)
Sep 11 22:23:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:07,836 main INFO screen Retail pass=0 dev=0.0 ins=4.93 pro=25 1a=False 1b=False 2=True (21.7s)
Sep 11 22:23:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:14,664 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:23:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:19,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:23:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:37,932 main INFO screen pairs pass=0 dev=0.0 ins=29.56 pro=25 1a=False 1b=False 2=True (23.3s)
Sep 11 22:23:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:23:43,564 main INFO screen PHANTOM pass=0 dev=6.63 ins=17.01 pro=28 1a=False 1b=False 2=False (5.2s)
Sep 11 22:24:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:02,870 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:22:24:02 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 22:24:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:03,219 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:22:24:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 22:24:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:06,049 main INFO screen WCOI pass=0 dev=2.25 ins=0.0 pro=3 1a=False 1b=False 2=False (10.8s)
Sep 11 22:24:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:41,976 main INFO screen DICK pass=0 dev=0.0 ins=31.15 pro=21 1a=False 1b=False 2=False (10.9s)
Sep 11 22:24:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:46,051 main INFO screen Cantos pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 11 22:24:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:46,857 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:24:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:24:51,933 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:25:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:25:11,688 main INFO screen CHAROC pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=True (24.9s)
Sep 11 22:25:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:25:19,137 main INFO screen VENOM pass=0 dev=0.2 ins=0.0 pro=1 1a=False 1b=False 2=False (10.3s)
Sep 11 22:25:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:25:37,094 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:25:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 22:25:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:25:51,272 aiohttp.access INFO 89.42.231.200 [11/Sep/2026:22:25:51 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 11 22:25:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:25:58,653 main INFO screen TURTLE pass=0 dev=6.63 ins=19.0 pro=23 1a=False 1b=False 2=False (5.1s)
Sep 11 22:26:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:01,984 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:05,245 main INFO screen 9/9-9/10-9 pass=0 dev=0.53 ins=0.0 pro=45 1a=False 1b=True 2=False (9.8s)
Sep 11 22:26:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:07,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:14,252 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:19,454 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:22,143 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:27,203 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:26:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:27,929 main INFO screen FARTJAR pass=0 dev=0.0 ins=20.89 pro=28 1a=False 1b=False 2=True (26.0s)
Sep 11 22:26:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:37,625 main INFO screen OnlyDog pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (23.4s)
Sep 11 22:26:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:26:42,545 main INFO screen foid pass=0 dev=0.0 ins=21.35 pro=82 1a=False 1b=False 2=True (20.5s)
Sep 11 22:27:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:07,023 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:27:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:12,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:27:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:20,024 main INFO screen nasfly pass=0 dev=0.0 ins=27.57 pro=16 1a=False 1b=False 2=False (8.7s)
Sep 11 22:27:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:32,383 main INFO screen Batunk pass=0 dev=0.11 ins=79.2 pro=7 1a=False 1b=True 2=True (25.4s)
Sep 11 22:27:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:40,640 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:27:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:27:50,227 main INFO screen little pass=0 dev=0.0 ins=23.4 pro=47 1a=False 1b=False 2=True (9.6s)
Sep 11 22:28:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:02,662 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:28:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:08,059 main INFO screen BetOnBlak pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 11 22:28:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:14,894 main INFO screen Chungus pass=0 dev=6.63 ins=19.46 pro=34 1a=False 1b=False 2=True (12.8s)
Sep 11 22:28:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:16,631 main INFO screen mert pass=0 dev=2.06 ins=22.74 pro=26 1a=False 1b=False 2=True (8.5s)
Sep 11 22:28:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:16,751 main INFO screen WCOI pass=0 dev=2.08 ins=0.0 pro=4 1a=False 1b=False 2=False (9.9s)
Sep 11 22:28:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:42,189 main INFO screen mert pass=1 dev=0.0 ins=11.06 pro=25 1a=False 1b=False 2=False (7.7s)
Sep 11 22:28:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:46,729 main INFO screen FREEBOATS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 22:28:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:52,419 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:28:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:28:57,437 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:29:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:07,222 main INFO screen PAGER pass=0 dev=0.0 ins=20.1 pro=36 1a=False 1b=False 2=True (9.1s)
Sep 11 22:29:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:08,931 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:29:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:09,460 main INFO screen $CAJUN pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (9.9s)
Sep 11 22:29:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:14,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:29:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:16,735 main INFO screen Coca Cola pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.4s)
Sep 11 22:29:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:29,877 main INFO screen Beecat pass=0 dev=0.0 ins=15.11 pro=66 1a=False 1b=False 2=True (21.0s)
Sep 11 22:29:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:29:48,789 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:30:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:01,075 main INFO screen trell pass=0 dev=4.13 ins=22.98 pro=23 1a=False 1b=False 2=True (12.4s)
Sep 11 22:30:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:03,380 main INFO screen Jewneegy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (10.9s)
Sep 11 22:30:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:11,747 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:30:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:16,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:30:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:19,628 main INFO screen PI pass=0 dev=0.0 ins=18.25 pro=53 1a=False 1b=False 2=True (10.2s)
Sep 11 22:30:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:20,713 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:30:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:25,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:30:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:32,098 main INFO screen Swiftiephylus pass=0 dev=0.0 ins=17.8 pro=52 1a=False 1b=False 2=True (21.0s)
Sep 11 22:30:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:36,948 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:30:36 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T21:00:40Z
--- update 2026-09-11T21:05:43Z
--- update 2026-09-11T21:11:05Z
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
--- update 2026-09-11T21:42:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
--- update 2026-09-11T21:47:46Z
--- update 2026-09-11T21:53:06Z
--- update 2026-09-11T21:58:16Z
--- update 2026-09-11T22:03:36Z
--- update 2026-09-11T22:08:49Z
--- update 2026-09-11T22:14:14Z
--- update 2026-09-11T22:19:36Z
--- update 2026-09-11T22:25:36Z
--- update 2026-09-11T22:30:35Z
```

## Analyses (laatste 25 regels)
```
inactive
21:42:40   ingelezen tot rowid 2425120 (200000 rijen, 200000 bruikbaar)
21:42:43   ingelezen tot rowid 2533436 (308316 rijen, 308316 bruikbaar)
21:42:43 ingelezen: 308316 nieuwe trades, 308316 bruikbaar (6s)
21:42:56 777 aankopen van gevolgde wallets geëvalueerd
21:43:01 grote spelers: saldo van 425 wallets opgehaald
21:43:56 herkomst: 40 posities gekoppeld
21:43:58 klaar in 82s -> /opt/schaduwbot/reports/ledger.md
21:43:59 klaar in 1s: 6168 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
21:43:59 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 21:43 UTC
21:43:59 40246 tokens geladen
21:44:02   2000 tokens, 264665 trades, 62063 posities (3s)
21:44:04   4000 tokens, 539436 trades, 121662 posities (5s)
21:44:07   6000 tokens, 831867 trades, 188339 posities (8s)
21:44:10   8000 tokens, 1123316 trades, 253063 posities (10s)
21:44:12   10000 tokens, 1410949 trades, 318168 posities (13s)
21:44:15   12000 tokens, 1691732 trades, 380121 posities (16s)
21:44:18   14000 tokens, 1969718 trades, 443453 posities (19s)
21:44:20   16000 tokens, 2230065 trades, 499999 posities (21s)
21:44:23   18000 tokens, 2510034 trades, 567609 posities (24s)
21:44:23 posities: 576157 uit 2537772 trades (24s)
21:44:30 132608 wallets gerekend
21:44:31 geluk-toets
21:44:52 persistentie
21:44:53 kopieer-simulatie
21:45:01 klaar in 62s -> /opt/schaduwbot/reports/wallets.md
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
