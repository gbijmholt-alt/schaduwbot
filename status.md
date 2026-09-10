# Schaduwbot status

- tijd: 2026-09-10 15:44:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 hour, 57 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 557/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 6980, "tokens_in_memory": 1475, "msgs": 1025726, "trades": 222068, "creates": 2737, "decode_fail": 23644, "rpc_calls": 3668, "rpc_errors": 459, "sol_usd": 99.65187895846593, "open_positions": 67}
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
Sep 10 15:35:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:30,569 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:15:35:30 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 15:35:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:37,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:35:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:37,882 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:35:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:38,500 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.0s)
Sep 10 15:35:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:41,064 main INFO screen cashback pass=1 dev=0.0 ins=1.36 pro=46 1a=False 1b=False 2=False (5.0s)
Sep 10 15:35:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:42,645 main INFO screen Stewie  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.4s)
Sep 10 15:35:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:51,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:35:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:51,871 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:35:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:35:52,316 main INFO screen blow pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 10 15:36:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:36:15,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:36:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:36:15,247 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:36:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:36:15,441 main INFO screen CT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:37:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:06,979 main INFO screen BUZZ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,010 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,123 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,251 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,637 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,805 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:37:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:08,936 main INFO screen Twerk pass=0 dev=0.0 ins=32.0 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 15:37:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:37:44,539 main INFO screen p pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.5s)
Sep 10 15:38:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:15,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:38:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:15,254 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:38:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:15,431 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 10 15:38:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:21,027 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:38:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:21,155 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:38:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:21,306 main INFO screen wifout pass=0 dev=0.0 ins=32.35 pro=21 1a=False 1b=False 2=True (0.3s)
Sep 10 15:38:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:30,768 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:38:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:30,896 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:38:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:31,387 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 10 15:38:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:51,975 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:38:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:52,106 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:38:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:52,435 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.5s)
Sep 10 15:38:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:38:52,482 main INFO screen att pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.2s)
Sep 10 15:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:03,642 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:03,783 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:39:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:03,944 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:39:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:06,085 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:39:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:06,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:39:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:06,331 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (0.3s)
Sep 10 15:39:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:11,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:39:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:12,227 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:39:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:12,729 main INFO screen TRUMPx pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.2s)
Sep 10 15:39:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:14,182 main INFO screen Chud pass=0 dev=0.42 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 10 15:39:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:30,464 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:39:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:30,552 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:39:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:30,751 main INFO screen 72x pass=0 dev=0.0 ins=79.24 pro=9 1a=False 1b=False 2=True (0.4s)
Sep 10 15:39:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:39:33,290 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:39:33 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
Sep 10 15:40:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:03,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:40:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:03,976 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:40:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:04,156 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 15:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:26,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:26,692 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:40:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:27,023 main INFO screen GRIMACE pass=0 dev=0.0 ins=15.22 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 10 15:40:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:48,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:40:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:48,622 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:40:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:48,874 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 15:40:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:40:53,305 main INFO screen ElonMusk pass=1 dev=0.0 ins=19.19 pro=22 1a=False 1b=False 2=False (1.8s)
Sep 10 15:41:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:26,102 main INFO screen cash pass=1 dev=0.0 ins=8.25 pro=44 1a=False 1b=False 2=False (3.9s)
Sep 10 15:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:37,647 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:37,738 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:41:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:37,915 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:41:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:57,564 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:41:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:57,666 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:41:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:41:58,003 main INFO screen CASHDOG pass=0 dev=0.0 ins=29.38 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 15:42:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:42:50,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:42:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:42:50,942 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:42:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:42:51,131 main INFO screen LONG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:43:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:10,980 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:43:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:11,076 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:43:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:11,284 main INFO screen Anal_Tony pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 15:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:12,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:12,572 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:12,707 main INFO screen XRPp pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:43:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:55,181 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:43:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:55,257 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:43:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:43:55,488 main INFO screen aids pass=0 dev=0.0 ins=11.7 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 15:44:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:03,440 main INFO screen SUI pass=0 dev=2.9 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 10 15:44:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:11,868 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 10 15:44:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:37,034 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:44:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:37,127 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:44:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
