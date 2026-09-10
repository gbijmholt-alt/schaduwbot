# Schaduwbot status

- tijd: 2026-09-10 15:02:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 hour, 15 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 534/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 4460, "tokens_in_memory": 1454, "msgs": 682908, "trades": 138566, "creates": 1788, "decode_fail": 14591, "rpc_calls": 2282, "rpc_errors": 283, "sol_usd": 99.81173279994283, "open_positions": 65}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 14:48 UTC

Gelogde schaduwtrades: **891**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 1428 | 184 | 5 | 184 | 29 | 324 | 891 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 22 | 4% | 4.5% | +32.3% | -18.4% | -16.07% | 54% |
| dip35_V1_gescreend_fail | 82 | 24% | 7.3% | +41.1% | -32.9% | -14.85% | 95% |
| dip35_V1_alle | 106 | 22% | 6.6% | +39.9% | -29.2% | -14.22% | 97% |
| dip35_V2_gescreend_pass | 20 | 0% | 5.0% | +0.0% | -20.4% | -20.38% | 57% |
| dip35_V2_gescreend_fail | 75 | 24% | 8.0% | +49.9% | -37.1% | -16.25% | 95% |
| dip35_V2_alle | 97 | 20% | 7.2% | +47.8% | -32.5% | -16.75% | 98% |
| dip35_V3_gescreend_pass | 22 | 4% | 4.5% | +0.8% | -21.4% | -20.39% | 60% |
| dip35_V3_gescreend_fail | 85 | 13% | 10.6% | +18.2% | -36.5% | -29.42% | 100% |
| dip35_V3_alle | 108 | 12% | 9.3% | +16.3% | -33.2% | -27.21% | 100% |
| dip40_V1_gescreend_pass | 21 | 14% | 4.8% | +66.9% | -17.8% | -5.65% | 37% |
| dip40_V1_gescreend_fail | 80 | 22% | 8.7% | +43.5% | -31.5% | -14.66% | 93% |
| dip40_V1_alle | 103 | 22% | 7.8% | +45.5% | -28.4% | -11.92% | 94% |
| dip40_V2_gescreend_pass | 19 | 5% | 5.3% | +193.1% | -18.5% | -7.37% | 37% |
| dip40_V2_gescreend_fail | 72 | 21% | 9.7% | +48.3% | -36.3% | -18.69% | 96% |
| dip40_V2_alle | 93 | 18% | 8.6% | +54.6% | -31.7% | -15.96% | 97% |
| dip40_V3_gescreend_pass | 21 | 10% | 4.8% | +2.3% | -20.1% | -17.95% | 54% |
| dip40_V3_gescreend_fail | 84 | 16% | 10.7% | +17.3% | -36.1% | -27.82% | 99% |
| dip40_V3_alle | 106 | 15% | 9.4% | +15.0% | -32.7% | -25.50% | 100% |
| dip45_V1_gescreend_pass | 18 | 28% | 5.6% | +53.5% | -18.8% | +1.25% | 29% |
| dip45_V1_gescreend_fail | 75 | 23% | 6.7% | +39.1% | -31.0% | -15.11% | 93% |
| dip45_V1_alle | 95 | 25% | 6.3% | +41.5% | -28.8% | -11.01% | 92% |
| dip45_V2_gescreend_pass | 16 | 19% | 6.2% | +70.3% | -20.1% | -3.17% | 31% |
| dip45_V2_gescreend_fail | 68 | 24% | 8.8% | +46.8% | -34.4% | -15.29% | 92% |
| dip45_V2_alle | 86 | 23% | 8.1% | +48.5% | -31.2% | -12.67% | 93% |
| dip45_V3_gescreend_pass | 18 | 17% | 5.6% | +142.5% | -20.8% | +6.43% | 37% |
| dip45_V3_gescreend_fail | 78 | 19% | 9.0% | +42.3% | -34.3% | -19.60% | 97% |
| dip45_V3_alle | 97 | 20% | 8.2% | +56.4% | -31.7% | -14.46% | 97% |

## Beste variant: dip45_V1_alle

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 14:54:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:54:21,754 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:54:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:54:23,608 main INFO screen Upward pass=0 dev=0.0 ins=41.24 pro=4 1a=False 1b=False 2=True (2.1s)
Sep 10 14:54:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:54:38,867 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:54:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:54:39,010 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:54:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:54:39,386 main INFO screen Upward pass=0 dev=0.0 ins=39.3 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 10 14:55:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:27,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:55:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:27,237 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:55:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:27,659 main INFO screen Dihvidends pass=0 dev=0.0 ins=27.09 pro=35 1a=False 1b=False 2=True (0.6s)
Sep 10 14:55:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:36,541 main INFO screen SXhSN pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 10 14:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:52,635 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:52,780 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:55:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:55:52,959 main INFO screen SOL GRND pass=0 dev=0.0 ins=0.13 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:56:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:23,950 main INFO screen GRINDER pass=0 dev=0.0 ins=20.3 pro=54 1a=False 1b=False 2=True (3.1s)
Sep 10 14:56:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:28,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:56:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:28,197 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:56:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:28,351 main INFO screen CATESEM pass=0 dev=0.0 ins=31.95 pro=3 1a=False 1b=False 2=True (0.4s)
Sep 10 14:56:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:47,556 main INFO screen SXhSN pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (2.0s)
Sep 10 14:56:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:56:57,247 main INFO screen p pass=0 dev=0.18 ins=0.0 pro=5 1a=False 1b=False 2=False (2.5s)
Sep 10 14:57:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:23,158 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:57:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:23,230 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:57:23 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 14:57:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:23,618 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:57:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:24,500 main INFO screen SON🙏 pass=1 dev=0.0 ins=1.53 pro=29 1a=False 1b=False 2=False (1.7s)
Sep 10 14:57:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:24,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:57:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:25,024 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:57:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:25,312 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.8s)
Sep 10 14:57:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:25,607 main INFO screen SON pass=1 dev=0.0 ins=0.31 pro=36 1a=False 1b=False 2=False (3.8s)
Sep 10 14:57:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:39,975 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:57:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:40,095 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:57:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:40,228 main INFO screen SON🙏 pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=True (0.3s)
Sep 10 14:57:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:43,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:57:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:43,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:57:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:43,356 main INFO screen free pass=0 dev=0.0 ins=39.75 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 14:57:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:51,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:57:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:51,171 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:57:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:57:51,293 main INFO screen The CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 14:58:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:03,980 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:58:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:04,100 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:58:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:04,227 main INFO screen LONG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:58:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:11,837 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:58:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:11,914 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:58:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:12,080 main INFO screen RUDY pass=0 dev=0.0 ins=17.65 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 10 14:58:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:15,080 aiohttp.access INFO 94.154.43.223 [10/Sep/2026:14:58:15 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 10 14:58:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:23,232 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:58:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:23,363 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:58:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:23,483 main INFO screen Cat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:58:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:39,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:58:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:39,967 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:58:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:40,195 main INFO screen CIND pass=0 dev=0.0 ins=78.99 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 10 14:58:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:46,349 main INFO screen SXhSk pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (3.4s)
Sep 10 14:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:47,441 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:47,602 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:47,749 main INFO screen CATESEM pass=0 dev=0.0 ins=32.03 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 10 14:58:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:58:59,854 main INFO screen fancat pass=1 dev=0.0 ins=17.52 pro=24 1a=False 1b=False 2=False (1.6s)
Sep 10 14:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:59:26,549 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:59:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:59:26,640 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:59:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:59:30,267 main INFO screen MILKIS pass=0 dev=0.0 ins=66.24 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 10 15:00:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:00,760 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:00:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:06,353 main INFO screen Stonkfly pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 10 15:00:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:17,851 main INFO screen Analtoly pass=0 dev=2.45 ins=0.0 pro=3 1a=False 1b=False 2=False (6.9s)
Sep 10 15:00:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:38,741 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:00:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:38,836 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:00:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:39,186 main INFO screen Kirk pass=0 dev=0.0 ins=39.65 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 15:00:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:47,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:00:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:47,138 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:00:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:47,446 main INFO screen STONKFLY pass=0 dev=0.0 ins=34.01 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 15:00:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:52,598 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:00:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:52,727 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:00:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:00:56,647 main INFO screen GROKCAT pass=0 dev=0.0 ins=1.54 pro=2 1a=False 1b=False 2=True (4.1s)
Sep 10 15:01:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:11,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:01:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:11,198 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:01:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:14,737 main INFO screen CATESEM pass=0 dev=0.0 ins=32.02 pro=3 1a=False 1b=False 2=True (3.9s)
Sep 10 15:01:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:22,103 main INFO screen FRONG pass=0 dev=36.63 ins=0.0 pro=16 1a=False 1b=False 2=True (7.3s)
Sep 10 15:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:40,516 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:40,619 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:01:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:01:40,978 main INFO screen ENTEI pass=0 dev=0.0 ins=15.56 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 15:02:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:02:06,715 main INFO screen JAS pass=1 dev=1.23 ins=0.69 pro=50 1a=False 1b=False 2=False (9.5s)
Sep 10 15:02:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:02:27,954 main INFO screen Analtoly pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (8.6s)
Sep 10 15:02:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:02:35,846 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:02:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:02:35,954 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:02:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:02:37,292 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:02:37 +0000] "GET /health HTTP/1.1" 200 423 "-" "Python-urllib/3.14"
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
