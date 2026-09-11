# Schaduwbot status

- tijd: 2026-09-11 09:23:41 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 19 hours, 36 minutes
- bot-service: active
- code-versie: 3e65967
- schijf: 2.4G/38G | geheugen: 545/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2162, "tokens_in_memory": 503, "msgs": 106128, "trades": 31376, "creates": 504, "decode_fail": 3451, "rpc_calls": 826, "rpc_errors": 62, "sol_usd": 99.61706248066764, "open_positions": 27, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 08:47 UTC

Gelogde schaduwtrades: **20217**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 9843 | 1366 | 18 | 1366 | 99 | 2655 | 7862 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 241 | 15% | 1.7% | +40.4% | -16.5% | -7.74% | 98% |
| dip35_V1_gescreend_fail | 2021 | 26% | 4.0% | +46.0% | -26.4% | -7.46% | 100% |
| dip35_V1_alle | 2338 | 25% | 4.1% | +44.7% | -25.7% | -7.82% | 100% |
| dip35_V2_gescreend_pass | 242 | 18% | 2.1% | +39.3% | -21.1% | -10.35% | 100% |
| dip35_V2_gescreend_fail | 2029 | 24% | 4.6% | +55.0% | -28.7% | -8.72% | 100% |
| dip35_V2_alle | 2326 | 23% | 4.7% | +53.1% | -28.2% | -9.33% | 100% |
| dip35_V3_gescreend_pass | 242 | 7% | 2.5% | +141.2% | -23.1% | -12.22% | 100% |
| dip35_V3_gescreend_fail | 2057 | 13% | 6.5% | +111.6% | -30.4% | -12.26% | 100% |
| dip35_V3_alle | 2349 | 12% | 6.3% | +110.0% | -29.9% | -12.70% | 100% |
| dip40_V1_gescreend_pass | 223 | 13% | 1.8% | +42.7% | -15.9% | -8.26% | 98% |
| dip40_V1_gescreend_fail | 1966 | 26% | 3.9% | +47.9% | -26.3% | -6.87% | 100% |
| dip40_V1_alle | 2246 | 25% | 3.9% | +46.9% | -25.5% | -7.27% | 100% |
| dip40_V2_gescreend_pass | 224 | 13% | 1.8% | +49.8% | -19.8% | -10.50% | 100% |
| dip40_V2_gescreend_fail | 1967 | 24% | 4.3% | +55.9% | -28.5% | -7.90% | 100% |
| dip40_V2_alle | 2231 | 23% | 4.3% | +55.1% | -27.8% | -8.60% | 100% |
| dip40_V3_gescreend_pass | 224 | 6% | 2.2% | +116.7% | -21.7% | -13.64% | 100% |
| dip40_V3_gescreend_fail | 1995 | 13% | 6.1% | +103.3% | -30.2% | -13.11% | 100% |
| dip40_V3_alle | 2255 | 12% | 5.9% | +102.1% | -29.5% | -13.59% | 100% |
| dip45_V1_gescreend_pass | 212 | 15% | 1.9% | +50.6% | -15.7% | -6.02% | 96% |
| dip45_V1_gescreend_fail | 1909 | 28% | 3.4% | +49.9% | -25.9% | -5.06% | 100% |
| dip45_V1_alle | 2162 | 26% | 3.5% | +49.5% | -25.0% | -5.42% | 100% |
| dip45_V2_gescreend_pass | 212 | 19% | 2.4% | +50.3% | -19.5% | -6.37% | 97% |
| dip45_V2_gescreend_fail | 1902 | 25% | 3.8% | +59.8% | -27.9% | -5.97% | 100% |
| dip45_V2_alle | 2145 | 24% | 3.9% | +58.7% | -27.3% | -6.42% | 100% |
| dip45_V3_gescreend_pass | 212 | 7% | 2.8% | +186.5% | -20.9% | -6.20% | 99% |
| dip45_V3_gescreend_fail | 1926 | 14% | 5.9% | +111.7% | -29.6% | -10.29% | 100% |
| dip45_V3_alle | 2165 | 13% | 5.8% | +114.2% | -28.9% | -10.27% | 100% |

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
| met_xlink | 1636 | 12% | 2.6% | -10.04% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 09:03:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:03:48,244 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:03:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:03:48,563 main INFO screen Jeetless pass=0 dev=0.0 ins=20.43 pro=22 1a=False 1b=False 2=True (0.5s)
Sep 11 09:04:16 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:16,454 main INFO screen SHOAL pass=0 dev=3.09 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 11 09:04:21 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:21,972 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:04:22 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:22,099 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:04:24 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:24,982 main INFO screen Trum pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (10.0s)
Sep 11 09:04:27 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:27,084 main INFO screen GCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.2s)
Sep 11 09:04:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:39,361 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:04:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:39,496 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:04:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:04:43,021 main INFO screen AMD pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (3.7s)
Sep 11 09:06:07 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:06:07,939 main INFO screen GOSI pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (8.7s)
Sep 11 09:06:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:06:12,410 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:09:06:12 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 09:06:30 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:06:30,962 main INFO screen Horse pass=0 dev=0.0 ins=10.67 pro=59 1a=False 1b=False 2=True (2.3s)
Sep 11 09:07:36 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:07:36,802 main INFO screen REM pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (7.0s)
Sep 11 09:07:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:07:46,441 main INFO screen GOT pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.0s)
Sep 11 09:07:59 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:07:59,579 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:07:59 +0000] "GET /health HTTP/1.1" 200 440 "-" "Python-urllib/3.14"
Sep 11 09:08:02 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:08:02,025 main INFO screen HATSUNE01 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.2s)
Sep 11 09:08:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:08:47,917 main INFO screen Clanker pass=1 dev=0.0 ins=12.14 pro=36 1a=False 1b=False 2=False (4.0s)
Sep 11 09:09:10 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:10,665 main INFO screen Wolf pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (5.6s)
Sep 11 09:09:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:12,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:09:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:12,174 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:09:18 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:18,383 main INFO screen BCAT pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=True (6.4s)
Sep 11 09:09:33 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:33,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:09:33 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:33,894 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:09:38 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:09:38,331 main INFO screen APES pass=0 dev=0.0 ins=19.43 pro=11 1a=False 1b=False 2=True (4.6s)
Sep 11 09:10:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:10:12,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:10:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:10:12,471 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:10:16 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:10:16,243 main INFO screen AG pass=0 dev=0.0 ins=77.97 pro=6 1a=False 1b=False 2=True (4.0s)
Sep 11 09:11:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:09,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:11:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:09,628 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:11:11 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:11,413 main INFO screen sweet pass=0 dev=4.58 ins=0.0 pro=3 1a=False 1b=False 2=False (6.6s)
Sep 11 09:11:14 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:14,338 main INFO screen FLYSTONKS pass=0 dev=0.0 ins=77.91 pro=8 1a=False 1b=False 2=True (4.9s)
Sep 11 09:11:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:41,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:11:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:41,276 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:11:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:11:48,466 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.4s)
Sep 11 09:12:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:12:39,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:12:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:12:39,309 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:12:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:12:46,388 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 09:12:58 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:12:58,189 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:12:58 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:12:58,314 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:13:00 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:00,659 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:13:00 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:00,792 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:13:02 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:02,995 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:13:03 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:03,162 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:13:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:04,498 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:13:04 +0000] "GET /health HTTP/1.1" 200 440 "-" "Python-urllib/3.14"
Sep 11 09:13:04 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:04,974 main INFO screen STONKPUMP pass=0 dev=0.0 ins=79.13 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 11 09:13:05 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:05,234 main INFO screen bunny pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.6s)
Sep 11 09:13:10 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:10,151 main INFO screen TWINGANG pass=0 dev=0.0 ins=77.91 pro=7 1a=False 1b=False 2=True (7.2s)
Sep 11 09:13:40 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:13:40,355 main INFO screen Bull pass=0 dev=24.5 ins=0.0 pro=16 1a=False 1b=False 2=False (6.4s)
Sep 11 09:14:07 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:14:07,525 main INFO screen HEDGIE pass=0 dev=0.0 ins=18.15 pro=44 1a=False 1b=False 2=True (6.2s)
Sep 11 09:14:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:14:46,906 main INFO screen SLOP pass=0 dev=7.58 ins=20.43 pro=6 1a=False 1b=False 2=False (7.8s)
Sep 11 09:15:17 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:15:17,850 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:15:17 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:15:17,909 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:15:24 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:15:24,164 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 11 09:16:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:16:41,519 main INFO screen maxi pass=0 dev=0.0 ins=16.11 pro=26 1a=False 1b=False 2=True (10.0s)
Sep 11 09:18:37 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:18:37,099 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:18:37 +0000] "GET /health HTTP/1.1" 200 439 "-" "Python-urllib/3.14"
Sep 11 09:19:20 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:19:20,606 main INFO screen $CR7MOON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.6s)
Sep 11 09:19:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:19:48,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:19:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:19:48,892 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:19:54 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:19:54,125 main INFO screen TRENCHFLY pass=0 dev=0.0 ins=14.04 pro=10 1a=False 1b=False 2=True (5.4s)
Sep 11 09:20:56 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:20:56,373 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:20:56 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:20:56,477 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:21:02 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:02,330 main INFO screen $SC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 11 09:21:19 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:19,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:21:19 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:19,809 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:21:20 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:20,275 main INFO screen SUPERSTONK pass=0 dev=0.0 ins=8.95 pro=43 1a=False 1b=False 2=True (1.4s)
Sep 11 09:21:28 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:28,113 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 11 09:21:51 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:51,438 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:21:51 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:51,531 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:21:59 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:21:59,032 main INFO screen WHITEFLY pass=0 dev=0.0 ins=79.27 pro=8 1a=False 1b=False 2=True (7.7s)
Sep 11 09:22:08 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:08,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:22:08 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:08,216 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:22:14 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:14,408 main INFO screen PUMPCAT pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 11 09:22:44 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:44,563 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:22:44 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:44,666 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:22:48 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:22:48,406 main INFO screen AMD pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 11 09:23:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:23:23,744 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:23:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:23:23,840 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:23:27 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:23:27,523 main INFO screen ! pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 11 09:23:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:23:41,608 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:23:41 +0000] "GET /health HTTP/1.1" 200 441 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T08:04:36Z
--- update 2026-09-11T08:09:59Z
--- update 2026-09-11T08:15:36Z
--- update 2026-09-11T08:20:55Z
--- update 2026-09-11T08:26:04Z
--- update 2026-09-11T08:31:36Z
--- update 2026-09-11T08:36:38Z
--- update 2026-09-11T08:42:29Z
--- update 2026-09-11T08:47:35Z
nieuwe code: 3e65967
install klaar
--- update 2026-09-11T08:52:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 277361cb46e7428ca1de36d4214ea43b
wallet-analyse gestart (e04fe8bd5728)
--- update 2026-09-11T08:57:39Z
--- update 2026-09-11T09:02:40Z
--- update 2026-09-11T09:07:58Z
--- update 2026-09-11T09:13:03Z
--- update 2026-09-11T09:18:36Z
--- update 2026-09-11T09:23:40Z
```

## Wallet-analyse (laatste 15 regels)
```
inactive
08:52:36 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 08:52 UTC
08:52:36 24905 tokens geladen
08:52:43   2000 tokens, 587636 trades, 196383 posities (6s)
08:52:47 posities: 352960 uit 1045578 trades (11s)
08:52:52 79415 wallets gerekend
08:52:53 geluk-toets
08:53:06 persistentie
08:53:07 kopieer-simulatie
08:53:11 klaar in 34s -> /opt/schaduwbot/reports/wallets.md
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
