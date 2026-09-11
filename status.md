# Schaduwbot status

- tijd: 2026-09-11 02:09:16 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 12 hours, 22 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.2G/38G | geheugen: 637/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 44459, "tokens_in_memory": 1244, "msgs": 8482697, "trades": 1630482, "creates": 17877, "decode_fail": 114111, "rpc_calls": 26566, "rpc_errors": 2559, "sol_usd": 99.37516341543237, "open_positions": 10}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 01:48 UTC

Gelogde schaduwtrades: **14017**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 2526 | 270 | 0 | 271 | 26 | 546 | 1662 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 174 | 16% | 1.7% | +37.6% | -16.8% | -8.38% | 96% |
| dip35_V1_gescreend_fail | 1400 | 25% | 4.0% | +44.7% | -25.6% | -7.71% | 100% |
| dip35_V1_alle | 1624 | 25% | 4.1% | +43.3% | -25.0% | -8.15% | 100% |
| dip35_V2_gescreend_pass | 175 | 17% | 2.3% | +30.3% | -21.4% | -12.54% | 99% |
| dip35_V2_gescreend_fail | 1407 | 24% | 4.7% | +53.7% | -28.1% | -8.73% | 100% |
| dip35_V2_alle | 1619 | 23% | 4.8% | +51.0% | -27.6% | -9.63% | 100% |
| dip35_V3_gescreend_pass | 175 | 7% | 2.9% | +138.2% | -23.3% | -12.26% | 100% |
| dip35_V3_gescreend_fail | 1415 | 12% | 6.2% | +121.6% | -29.7% | -11.87% | 100% |
| dip35_V3_alle | 1625 | 11% | 6.2% | +118.7% | -29.3% | -12.36% | 100% |
| dip40_V1_gescreend_pass | 162 | 13% | 2.5% | +43.2% | -16.3% | -8.61% | 96% |
| dip40_V1_gescreend_fail | 1361 | 25% | 4.3% | +47.3% | -25.6% | -7.53% | 100% |
| dip40_V1_alle | 1561 | 24% | 4.3% | +46.1% | -24.8% | -7.88% | 100% |
| dip40_V2_gescreend_pass | 163 | 14% | 2.5% | +46.7% | -20.6% | -11.52% | 99% |
| dip40_V2_gescreend_fail | 1365 | 24% | 4.6% | +55.4% | -27.9% | -7.92% | 100% |
| dip40_V2_alle | 1553 | 23% | 4.6% | +54.2% | -27.3% | -8.70% | 100% |
| dip40_V3_gescreend_pass | 163 | 7% | 3.1% | +118.0% | -22.1% | -12.68% | 99% |
| dip40_V3_gescreend_fail | 1373 | 12% | 6.1% | +109.7% | -29.5% | -13.49% | 100% |
| dip40_V3_alle | 1559 | 11% | 6.0% | +107.8% | -28.9% | -13.76% | 100% |
| dip45_V1_gescreend_pass | 151 | 15% | 2.6% | +47.9% | -15.7% | -6.02% | 93% |
| dip45_V1_gescreend_fail | 1317 | 27% | 3.6% | +49.4% | -25.0% | -5.04% | 100% |
| dip45_V1_alle | 1495 | 26% | 3.7% | +48.9% | -24.2% | -5.42% | 100% |
| dip45_V2_gescreend_pass | 151 | 19% | 3.3% | +41.8% | -19.8% | -7.92% | 96% |
| dip45_V2_gescreend_fail | 1318 | 25% | 4.0% | +60.6% | -27.1% | -5.10% | 100% |
| dip45_V2_alle | 1488 | 24% | 4.2% | +58.6% | -26.6% | -5.75% | 100% |
| dip45_V3_gescreend_pass | 151 | 8% | 4.0% | +173.8% | -21.2% | -5.68% | 97% |
| dip45_V3_gescreend_fail | 1325 | 12% | 5.7% | +125.0% | -28.8% | -9.66% | 100% |
| dip45_V3_alle | 1493 | 12% | 5.7% | +126.3% | -28.2% | -9.60% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 11 01:55:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:00,766 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:55:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:06,821 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:55:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:06,948 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:55:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:07,066 main INFO screen GIAB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 01:55:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:09,736 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:55:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:09,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:55:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:55:10,065 main INFO screen SPSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:56:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:56:11,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:56:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:56:11,785 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:56:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:56:15,879 main INFO screen MEMEMAN pass=0 dev=0.0 ins=36.62 pro=11 1a=False 1b=False 2=True (4.2s)
Sep 11 01:56:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:56:47,565 main INFO screen GIAB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 01:57:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:57:55,750 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:57:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:57:55,849 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:57:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:57:56,026 main INFO screen Gamestonk pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:58:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:03,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:58:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:03,925 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:58:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:04,074 main INFO screen Horse  pass=0 dev=0.0 ins=21.58 pro=32 1a=False 1b=False 2=True (0.3s)
Sep 11 01:58:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:24,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:58:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:24,997 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:58:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:25,190 main INFO screen Horse  pass=0 dev=0.0 ins=20.54 pro=15 1a=False 1b=False 2=True (0.4s)
Sep 11 01:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:38,324 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:38,490 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:58:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:38,646 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 01:58:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:58:54,517 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:01:58:54 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 01:59:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:11,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:59:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:11,546 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:59:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:11,735 main INFO screen MISTAKE pass=0 dev=0.0 ins=60.02 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 11 01:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:40,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 01:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:40,337 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 01:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:40,538 main INFO screen CLANK pass=0 dev=0.0 ins=36.88 pro=15 1a=False 1b=False 2=True (0.4s)
Sep 11 01:59:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 01:59:55,161 main INFO screen ELEFEPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 02:00:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:00:10,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:00:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:00:10,344 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:00:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:00:10,704 main INFO screen cokecat pass=0 dev=0.0 ins=19.84 pro=14 1a=False 1b=False 2=True (0.6s)
Sep 11 02:01:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:01:17,918 main INFO screen help pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 11 02:01:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:01:56,734 main INFO screen BITTY pass=0 dev=6.63 ins=21.67 pro=31 1a=False 1b=False 2=False (2.4s)
Sep 11 02:02:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:02:41,294 aiohttp.access INFO 94.154.43.223 [11/Sep/2026:02:02:41 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 02:03:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:03:04,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:03:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:03:04,303 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:03:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:03:09,243 main INFO screen ALON pass=0 dev=0.0 ins=79.24 pro=7 1a=False 1b=False 2=True (5.1s)
Sep 11 02:03:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:03:52,408 main INFO screen Kirk pass=0 dev=6.72 ins=0.0 pro=31 1a=False 1b=False 2=False (10.2s)
Sep 11 02:04:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:02,465 main INFO screen ᶜᵉᵗ pass=1 dev=0.0 ins=7.86 pro=37 1a=False 1b=False 2=False (2.6s)
Sep 11 02:04:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:06,147 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:04:06 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 02:04:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:09,981 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:04:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:10,105 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:04:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:15,444 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.5s)
Sep 11 02:04:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:04:27,307 main INFO screen mmrich pass=0 dev=2.56 ins=0.0 pro=2 1a=False 1b=False 2=False (7.2s)
Sep 11 02:06:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:06:33,305 main INFO screen sal pass=0 dev=0.11 ins=0.0 pro=9 1a=False 1b=False 2=False (9.4s)
Sep 11 02:06:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:06:35,263 main INFO screen PePenis pass=1 dev=0.06 ins=1.23 pro=41 1a=False 1b=False 2=False (10.5s)
Sep 11 02:06:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:06:59,364 main INFO screen TBC pass=1 dev=0.0 ins=11.69 pro=27 1a=False 1b=False 2=False (2.2s)
Sep 11 02:07:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:14,472 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:07:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:14,549 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:17,624 main INFO screen kittylick pass=0 dev=1.07 ins=0.0 pro=3 1a=False 1b=False 2=False (8.0s)
Sep 11 02:07:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:20,353 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:07:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:20,470 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:07:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:20,590 main INFO screen tss pass=0 dev=0.0 ins=36.29 pro=11 1a=False 1b=False 2=True (6.2s)
Sep 11 02:07:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:24,956 main INFO screen Giovanni pass=0 dev=0.0 ins=21.43 pro=20 1a=False 1b=False 2=True (4.7s)
Sep 11 02:07:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:42,993 main INFO screen CHAYET pass=0 dev=2.63 ins=0.0 pro=4 1a=False 1b=False 2=False (8.2s)
Sep 11 02:07:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:43,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:07:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:43,857 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:07:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:44,339 main INFO screen NFLX pass=0 dev=0.0 ins=14.94 pro=59 1a=False 1b=False 2=True (6.6s)
Sep 11 02:07:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:07:49,977 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 02:08:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:33,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:08:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:33,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:08:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:34,494 main INFO screen ~4° pass=1 dev=3.09 ins=3.04 pro=39 1a=False 1b=False 2=False (9.1s)
Sep 11 02:08:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:37,890 main INFO screen BUY pass=0 dev=0.0 ins=46.16 pro=12 1a=False 1b=False 2=True (4.9s)
Sep 11 02:08:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:47,205 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:02:08:47 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 02:08:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:47,545 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:02:08:47 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 02:08:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:52,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:08:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:52,823 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:08:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:08:59,734 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.1s)
Sep 11 02:09:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:06,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:09:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:06,239 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:09:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:10,297 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:09:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:10,384 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:09:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:10,763 main INFO screen ~4° pass=0 dev=0.0 ins=9.64 pro=31 1a=False 1b=False 2=True (0.5s)
Sep 11 02:09:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:13,132 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.0s)
Sep 11 02:09:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:15,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 02:09:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:15,897 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 02:09:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 02:09:16,341 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:02:09:16 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
