# Schaduwbot status

- tijd: 2026-09-10 17:00:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 hours, 13 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 580/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 11540, "tokens_in_memory": 1553, "msgs": 2094260, "trades": 383930, "creates": 4657, "decode_fail": 36549, "rpc_calls": 6400, "rpc_errors": 732, "sol_usd": 99.66405045396229, "open_positions": 56}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 16:48 UTC

Gelogde schaduwtrades: **3046**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 4315 | 586 | 12 | 586 | 77 | 1040 | 3046 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 57 | 10% | 1.8% | +36.3% | -17.2% | -11.56% | 79% |
| dip35_V1_gescreend_fail | 284 | 26% | 5.6% | +47.6% | -27.7% | -8.06% | 100% |
| dip35_V1_alle | 355 | 24% | 5.1% | +46.3% | -26.4% | -9.24% | 100% |
| dip35_V2_gescreend_pass | 54 | 11% | 1.9% | +22.9% | -21.0% | -16.12% | 85% |
| dip35_V2_gescreend_fail | 284 | 22% | 6.0% | +79.1% | -29.5% | -5.82% | 100% |
| dip35_V2_alle | 350 | 20% | 5.4% | +71.9% | -28.6% | -8.25% | 100% |
| dip35_V3_gescreend_pass | 57 | 5% | 1.8% | +32.4% | -22.7% | -19.77% | 90% |
| dip35_V3_gescreend_fail | 291 | 13% | 7.9% | +128.1% | -31.2% | -10.43% | 100% |
| dip35_V3_alle | 358 | 12% | 7.0% | +115.9% | -30.3% | -12.74% | 100% |
| dip40_V1_gescreend_pass | 54 | 17% | 1.9% | +42.6% | -16.2% | -6.41% | 67% |
| dip40_V1_gescreend_fail | 277 | 24% | 6.1% | +55.7% | -27.9% | -7.36% | 100% |
| dip40_V1_alle | 343 | 23% | 5.5% | +53.9% | -26.5% | -7.77% | 100% |
| dip40_V2_gescreend_pass | 51 | 14% | 2.0% | +61.0% | -20.1% | -8.95% | 72% |
| dip40_V2_gescreend_fail | 278 | 22% | 6.1% | +84.9% | -29.7% | -5.01% | 100% |
| dip40_V2_alle | 339 | 20% | 5.6% | +80.7% | -28.6% | -6.38% | 100% |
| dip40_V3_gescreend_pass | 54 | 7% | 1.9% | +25.0% | -21.3% | -17.86% | 87% |
| dip40_V3_gescreend_fail | 281 | 14% | 8.2% | +119.3% | -31.8% | -10.80% | 100% |
| dip40_V3_alle | 343 | 13% | 7.3% | +108.2% | -30.5% | -12.67% | 100% |
| dip45_V1_gescreend_pass | 47 | 19% | 2.1% | +45.4% | -16.2% | -4.39% | 63% |
| dip45_V1_gescreend_fail | 261 | 25% | 6.1% | +56.0% | -28.4% | -7.07% | 100% |
| dip45_V1_alle | 320 | 24% | 5.6% | +54.5% | -27.2% | -7.29% | 100% |
| dip45_V2_gescreend_pass | 45 | 20% | 2.2% | +45.1% | -18.4% | -5.72% | 60% |
| dip45_V2_gescreend_fail | 263 | 23% | 6.5% | +87.6% | -29.8% | -3.01% | 100% |
| dip45_V2_alle | 318 | 22% | 6.0% | +80.5% | -28.6% | -4.29% | 100% |
| dip45_V3_gescreend_pass | 47 | 8% | 2.1% | +107.5% | -20.0% | -9.20% | 77% |
| dip45_V3_gescreend_fail | 265 | 16% | 7.9% | +122.2% | -31.3% | -7.58% | 100% |
| dip45_V3_alle | 320 | 14% | 7.2% | +118.5% | -30.1% | -8.71% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 16:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:49:49,421 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:49:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:49:49,777 main INFO screen UNDERVALUED pass=0 dev=0.0 ins=12.77 pro=16 1a=False 1b=False 2=True (0.6s)
Sep 10 16:50:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:50:15,883 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 10 16:50:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:50:26,225 main INFO screen KERMIT pass=0 dev=5.69 ins=0.0 pro=46 1a=False 1b=False 2=False (2.0s)
Sep 10 16:51:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:18,368 main INFO screen Koopa pass=0 dev=0.16 ins=0.0 pro=3 1a=False 1b=False 2=False (3.4s)
Sep 10 16:51:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:29,507 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:51:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:29,627 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:51:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:29,783 main INFO screen nostalgia pass=0 dev=0.0 ins=12.5 pro=28 1a=False 1b=False 2=True (0.3s)
Sep 10 16:51:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:49,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:51:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:49,614 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:51:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:51:49,790 main INFO screen myct pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 16:52:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:04,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:52:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:04,650 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:52:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:04,783 main INFO screen LEVERDOG pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=True (0.3s)
Sep 10 16:52:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:07,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:52:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:07,458 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:52:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:07,606 main INFO screen suitdog pass=0 dev=0.0 ins=18.8 pro=34 1a=False 1b=False 2=True (0.4s)
Sep 10 16:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:23,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:23,378 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:23,681 main INFO screen Kirkaversa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 16:52:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:28,832 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:52:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:28,900 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:52:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:29,059 main INFO screen BlaccBaton pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:52:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:57,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:52:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:52:57,177 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:53:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:00,551 main INFO screen noob pass=0 dev=0.0 ins=46.06 pro=3 1a=False 1b=False 2=True (3.6s)
Sep 10 16:53:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:01,089 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:53:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:01,206 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:53:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:01,387 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 16:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:12,777 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:53:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:12,881 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:53:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:13,226 main INFO screen KYC pass=0 dev=0.0 ins=25.05 pro=4 1a=False 1b=False 2=True (0.6s)
Sep 10 16:53:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:29,317 main INFO screen MOO pass=1 dev=0.8 ins=8.77 pro=35 1a=False 1b=False 2=False (2.7s)
Sep 10 16:53:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:42,463 main INFO screen sol pass=0 dev=0.08 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 10 16:53:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:47,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:53:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:48,039 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:53:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:53:48,170 main INFO screen WWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:54:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:54:08,461 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (3.0s)
Sep 10 16:54:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:54:44,139 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:16:54:44 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
Sep 10 16:54:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:54:50,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:54:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:54:50,638 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:54:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:54:50,858 main INFO screen KIRKCOIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 16:55:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:05,762 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:16:55:05 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 16:55:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:10,069 main INFO screen Clanker pass=1 dev=0.0 ins=11.38 pro=26 1a=False 1b=False 2=False (3.8s)
Sep 10 16:55:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:18,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:55:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:19,129 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:55:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:19,298 main INFO screen SPSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 16:55:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:55:37,238 main INFO screen TURK pass=1 dev=0.0 ins=5.02 pro=35 1a=False 1b=False 2=False (4.0s)
Sep 10 16:56:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:56:19,959 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:56:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:56:20,052 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:56:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:56:20,251 main INFO screen pepenis pass=0 dev=0.0 ins=32.67 pro=10 1a=False 1b=False 2=True (0.4s)
Sep 10 16:56:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:56:53,497 main INFO screen PC pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 10 16:57:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:57:54,041 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:57:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:57:54,138 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:57:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:57:54,306 main INFO screen LAPEPE pass=0 dev=0.0 ins=79.24 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 16:58:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:14,905 main INFO screen RETARDO pass=0 dev=1.26 ins=0.0 pro=2 1a=False 1b=False 2=True (2.2s)
Sep 10 16:58:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:16,437 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:58:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:16,524 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:58:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:16,693 main INFO screen VSNTC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 16:58:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:31,988 main INFO screen RISE pass=0 dev=39.11 ins=0.05 pro=2 1a=False 1b=False 2=True (2.2s)
Sep 10 16:58:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:37,927 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:38,052 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:58:38,353 main INFO screen WORTHLESS pass=1 dev=0.0 ins=13.3 pro=31 1a=False 1b=False 2=False (0.5s)
Sep 10 16:59:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:00,000 main INFO screen TURK pass=0 dev=0.0 ins=30.7 pro=60 1a=False 1b=False 2=True (2.8s)
Sep 10 16:59:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:03,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:59:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:04,501 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:59:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:05,072 main INFO screen pepenis pass=0 dev=0.0 ins=31.13 pro=4 1a=False 1b=False 2=True (1.8s)
Sep 10 16:59:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:05,167 main INFO screen $PTA pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (4.0s)
Sep 10 16:59:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:21,106 main INFO screen Midas pass=0 dev=0.47 ins=0.0 pro=4 1a=False 1b=False 2=False (2.1s)
Sep 10 16:59:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:25,804 main INFO screen KENDAL pass=0 dev=6.64 ins=0.66 pro=39 1a=False 1b=False 2=False (3.2s)
Sep 10 16:59:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:44,972 main INFO screen MARIO pass=0 dev=0.16 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 10 16:59:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:56,769 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 16:59:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:56,857 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 16:59:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 16:59:57,022 main INFO screen MIST pass=0 dev=0.0 ins=30.13 pro=35 1a=False 1b=False 2=True (0.3s)
Sep 10 17:00:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:16,464 main INFO screen SNAFIOSO pass=0 dev=35.47 ins=0.0 pro=9 1a=False 1b=False 2=True (9.2s)
Sep 10 17:00:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:21,294 main INFO screen ElRetardo pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.2s)
Sep 10 17:00:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:24,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 17:00:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:24,661 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 17:00:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:25,000 main INFO screen Charlie pass=0 dev=0.0 ins=16.92 pro=10 1a=False 1b=False 2=True (0.5s)
Sep 10 17:00:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 17:00:37,180 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:17:00:37 +0000] "GET /health HTTP/1.1" 200 425 "-" "Python-urllib/3.14"
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
