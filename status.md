# Schaduwbot status

- tijd: 2026-09-11 10:21:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 20 hours, 34 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 544/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 1897, "tokens_in_memory": 448, "msgs": 126961, "trades": 33070, "creates": 448, "decode_fail": 1608, "rpc_calls": 743, "rpc_errors": 58, "sol_usd": 99.53932647783006, "open_positions": 34, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 09:49 UTC

Gelogde schaduwtrades: **20815**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 10781 | 1489 | 21 | 1489 | 102 | 2875 | 8460 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 244 | 16% | 1.6% | +41.0% | -16.4% | -7.48% | 98% |
| dip35_V1_gescreend_fail | 2082 | 26% | 4.0% | +46.6% | -26.4% | -7.13% | 100% |
| dip35_V1_alle | 2406 | 26% | 4.1% | +45.2% | -25.7% | -7.51% | 100% |
| dip35_V2_gescreend_pass | 243 | 18% | 2.1% | +40.2% | -21.1% | -9.99% | 100% |
| dip35_V2_gescreend_fail | 2090 | 24% | 4.6% | +55.2% | -28.7% | -8.35% | 100% |
| dip35_V2_alle | 2391 | 24% | 4.7% | +53.3% | -28.2% | -8.98% | 100% |
| dip35_V3_gescreend_pass | 245 | 7% | 2.4% | +137.5% | -23.0% | -11.84% | 100% |
| dip35_V3_gescreend_fail | 2120 | 13% | 6.5% | +113.3% | -30.4% | -11.73% | 100% |
| dip35_V3_alle | 2418 | 12% | 6.4% | +111.2% | -29.9% | -12.21% | 100% |
| dip40_V1_gescreend_pass | 226 | 13% | 1.8% | +43.4% | -15.8% | -7.97% | 98% |
| dip40_V1_gescreend_fail | 2027 | 26% | 3.9% | +48.4% | -26.3% | -6.65% | 100% |
| dip40_V1_alle | 2313 | 25% | 4.0% | +47.4% | -25.6% | -7.07% | 100% |
| dip40_V2_gescreend_pass | 225 | 14% | 1.8% | +50.6% | -19.8% | -10.12% | 100% |
| dip40_V2_gescreend_fail | 2027 | 25% | 4.3% | +56.4% | -28.5% | -7.62% | 100% |
| dip40_V2_alle | 2295 | 23% | 4.4% | +55.6% | -27.9% | -8.34% | 100% |
| dip40_V3_gescreend_pass | 227 | 6% | 2.2% | +114.0% | -21.6% | -13.21% | 100% |
| dip40_V3_gescreend_fail | 2058 | 13% | 6.0% | +105.8% | -30.1% | -12.54% | 100% |
| dip40_V3_alle | 2324 | 12% | 5.9% | +104.1% | -29.5% | -13.06% | 100% |
| dip45_V1_gescreend_pass | 215 | 14% | 1.9% | +50.6% | -15.7% | -6.15% | 96% |
| dip45_V1_gescreend_fail | 1970 | 28% | 3.5% | +50.4% | -25.9% | -4.83% | 100% |
| dip45_V1_alle | 2229 | 26% | 3.5% | +50.0% | -25.1% | -5.26% | 100% |
| dip45_V2_gescreend_pass | 213 | 19% | 2.3% | +50.3% | -19.5% | -6.38% | 97% |
| dip45_V2_gescreend_fail | 1961 | 25% | 3.9% | +60.1% | -27.9% | -5.71% | 100% |
| dip45_V2_alle | 2208 | 24% | 4.0% | +58.9% | -27.3% | -6.21% | 100% |
| dip45_V3_gescreend_pass | 215 | 7% | 2.8% | +186.5% | -20.8% | -6.32% | 99% |
| dip45_V3_gescreend_fail | 1986 | 14% | 5.8% | +113.2% | -29.6% | -9.88% | 100% |
| dip45_V3_alle | 2231 | 13% | 5.8% | +115.2% | -28.9% | -9.94% | 100% |

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
| met_xlink | 1657 | 12% | 2.6% | -9.77% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 10:03:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:03:47,182 main INFO screen beer pass=0 dev=0.17 ins=0.0 pro=3 1a=False 1b=False 2=False (6.0s)
Sep 11 10:04:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:06,602 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:04:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:06,698 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:04:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:10,125 main INFO screen FlyDev pass=0 dev=0.0 ins=4.28 pro=11 1a=False 1b=False 2=True (3.6s)
Sep 11 10:04:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:41,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:04:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:41,849 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:04:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:04:42,278 main INFO screen Alon pass=1 dev=0.0 ins=16.29 pro=25 1a=False 1b=False 2=False (0.6s)
Sep 11 10:05:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:05:22,558 main INFO screen $CAT pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (8.8s)
Sep 11 10:05:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:05:32,153 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:05:32 +0000] "GET /health HTTP/1.1" 200 438 "-" "Python-urllib/3.14"
Sep 11 10:05:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:05:34,632 main INFO screen FERSPE pass=0 dev=1.83 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 11 10:06:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:06:06,240 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:06:06 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:06:06,336 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:06:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:06:10,388 main INFO screen DOTCAT pass=0 dev=0.0 ins=79.31 pro=8 1a=False 1b=False 2=True (4.2s)
Sep 11 10:06:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:06:14,146 main INFO screen Alon pass=0 dev=0.0 ins=14.2 pro=30 1a=False 1b=True 2=False (3.0s)
Sep 11 10:07:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:07:25,030 main INFO screen LTC pass=0 dev=0.0 ins=17.18 pro=35 1a=False 1b=False 2=True (9.9s)
Sep 11 10:07:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:07:48,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:07:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:07:48,462 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:07:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:07:48,690 main INFO screen DIVERGENT pass=0 dev=0.0 ins=23.91 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 11 10:08:32 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:08:32,209 main INFO screen 9/11 pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (8.4s)
Sep 11 10:08:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:08:48,715 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:08:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:08:48,815 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:08:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:08:52,591 main INFO screen 911CANDLE pass=0 dev=0.0 ins=79.26 pro=7 1a=False 1b=False 2=True (4.0s)
Sep 11 10:09:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:39,685 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:09:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:39,912 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:09:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:40,390 main INFO screen co1n9 pass=0 dev=0.0 ins=19.88 pro=25 1a=False 1b=False 2=True (0.8s)
Sep 11 10:09:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:48,572 main INFO screen STONKY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 11 10:09:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:57,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:09:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:57,257 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:09:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:59,226 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:09:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:09:59,357 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:10:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:01,234 main INFO screen Flynance pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.2s)
Sep 11 10:10:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:03,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:10:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:03,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:10:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:04,350 main INFO screen HORIZON pass=0 dev=0.0 ins=76.87 pro=9 1a=False 1b=False 2=True (5.2s)
Sep 11 10:10:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:09,245 main INFO screen Pippo pass=0 dev=0.0 ins=17.32 pro=20 1a=False 1b=False 2=True (5.5s)
Sep 11 10:10:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:37,174 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:10:37 +0000] "GET /health HTTP/1.1" 200 440 "-" "Python-urllib/3.14"
Sep 11 10:10:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:48,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:10:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:48,824 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:10:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:10:53,688 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 11 10:11:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:16,350 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:11:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:16,443 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:11:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:18,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:11:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:19,105 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:11:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:23,336 main INFO screen sob pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.4s)
Sep 11 10:11:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:23,743 main INFO screen ZKITTY pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (7.5s)
Sep 11 10:11:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:28,707 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:11:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:28,794 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:11:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:11:29,159 main INFO screen BRICS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 10:12:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:12:40,868 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.3s)
Sep 11 10:12:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:12:58,871 main INFO screen sob pass=0 dev=4.12 ins=0.0 pro=3 1a=False 1b=False 2=False (7.2s)
Sep 11 10:13:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:13:16,422 main INFO screen 9/11 pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 11 10:14:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:14:47,155 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:14:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:14:47,299 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:14:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:14:47,827 main INFO screen airdrop pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 10:15:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:31,732 main INFO screen WTF pass=0 dev=0.0 ins=24.59 pro=50 1a=False 1b=False 2=True (8.3s)
Sep 11 10:15:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:33,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:15:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:33,280 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:15:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:33,823 main INFO screen airdrop pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 10:15:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:55,049 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:15:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:55,148 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:15:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:15:55,669 main INFO screen airdrop pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.7s)
Sep 11 10:16:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:20,777 main INFO screen OhMyGOWD pass=0 dev=1.26 ins=0.0 pro=4 1a=False 1b=False 2=False (8.0s)
Sep 11 10:16:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:22,206 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:16:22 +0000] "GET /health HTTP/1.1" 200 441 "-" "Python-urllib/3.14"
Sep 11 10:16:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:30,071 main INFO screen MemeFi pass=0 dev=0.0 ins=9.75 pro=46 1a=False 1b=False 2=True (3.2s)
Sep 11 10:16:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:30,188 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:16:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:30,305 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:16:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:16:30,800 main INFO screen airdrop pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.8s)
Sep 11 10:17:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:17:04,202 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:17:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:17:04,282 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:17:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:17:04,649 main INFO screen airdrop pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (0.6s)
Sep 11 10:18:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:18:12,734 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:18:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:18:20,506 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:18:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:18:24,705 main INFO screen 67 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.1s)
Sep 11 10:19:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:19:03,156 main INFO screen 9/11 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.0s)
Sep 11 10:19:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:19:31,822 main INFO screen meme pass=0 dev=0.0 ins=18.67 pro=30 1a=False 1b=False 2=True (9.5s)
Sep 11 10:21:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:21:07,691 main INFO screen MAGA pass=0 dev=0.22 ins=0.04 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 11 10:21:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:21:11,705 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 10:21:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:21:11,830 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 10:21:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:21:18,938 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 10:21:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 10:21:21,973 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:10:21:21 +0000] "GET /health HTTP/1.1" 200 441 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T09:02:40Z
--- update 2026-09-11T09:07:58Z
--- update 2026-09-11T09:13:03Z
--- update 2026-09-11T09:18:36Z
--- update 2026-09-11T09:23:40Z
--- update 2026-09-11T09:29:10Z
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
