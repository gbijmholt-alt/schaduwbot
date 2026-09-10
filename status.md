# Schaduwbot status

- tijd: 2026-09-10 15:50:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 hours, 3 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 561/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 7340, "tokens_in_memory": 1395, "msgs": 1067174, "trades": 234034, "creates": 2869, "decode_fail": 24500, "rpc_calls": 3833, "rpc_errors": 475, "sol_usd": 99.57384643493738, "open_positions": 78}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 15:48 UTC

Gelogde schaduwtrades: **1955**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 2829 | 392 | 9 | 392 | 51 | 673 | 1955 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 36 | 6% | 2.8% | +35.4% | -18.8% | -15.77% | 70% |
| dip35_V1_gescreend_fail | 185 | 28% | 5.9% | +47.5% | -29.0% | -7.87% | 99% |
| dip35_V1_alle | 232 | 25% | 5.6% | +46.4% | -27.6% | -9.45% | 100% |
| dip35_V2_gescreend_pass | 35 | 6% | 2.9% | +1.1% | -22.5% | -21.18% | 78% |
| dip35_V2_gescreend_fail | 176 | 25% | 6.2% | +42.0% | -31.3% | -12.96% | 100% |
| dip35_V2_alle | 221 | 22% | 5.9% | +39.0% | -30.2% | -14.83% | 100% |
| dip35_V3_gescreend_pass | 36 | 6% | 2.8% | +1.3% | -24.0% | -22.61% | 82% |
| dip35_V3_gescreend_fail | 188 | 14% | 8.0% | +110.5% | -31.5% | -11.15% | 100% |
| dip35_V3_alle | 232 | 13% | 7.3% | +96.9% | -30.9% | -13.78% | 100% |
| dip40_V1_gescreend_pass | 34 | 15% | 2.9% | +48.0% | -17.9% | -8.19% | 55% |
| dip40_V1_gescreend_fail | 181 | 25% | 6.6% | +55.8% | -28.2% | -6.86% | 98% |
| dip40_V1_alle | 224 | 24% | 6.2% | +54.6% | -27.0% | -7.31% | 99% |
| dip40_V2_gescreend_pass | 33 | 9% | 3.0% | +64.8% | -21.3% | -13.50% | 66% |
| dip40_V2_gescreend_fail | 172 | 24% | 7.0% | +46.4% | -30.9% | -12.45% | 99% |
| dip40_V2_alle | 213 | 22% | 6.6% | +46.7% | -29.6% | -13.10% | 100% |
| dip40_V3_gescreend_pass | 34 | 6% | 2.9% | +2.3% | -22.4% | -20.97% | 77% |
| dip40_V3_gescreend_fail | 184 | 16% | 8.7% | +103.7% | -31.7% | -10.39% | 100% |
| dip40_V3_alle | 224 | 14% | 8.0% | +94.5% | -30.6% | -12.77% | 100% |
| dip45_V1_gescreend_pass | 29 | 21% | 3.4% | +44.7% | -17.3% | -4.51% | 48% |
| dip45_V1_gescreend_fail | 170 | 26% | 5.9% | +55.2% | -28.5% | -6.32% | 98% |
| dip45_V1_alle | 208 | 26% | 5.8% | +53.6% | -27.4% | -6.36% | 98% |
| dip45_V2_gescreend_pass | 28 | 18% | 3.6% | +42.5% | -18.7% | -7.79% | 51% |
| dip45_V2_gescreend_fail | 160 | 26% | 6.9% | +47.9% | -30.4% | -10.35% | 99% |
| dip45_V2_alle | 196 | 24% | 6.6% | +46.4% | -29.1% | -10.60% | 99% |
| dip45_V3_gescreend_pass | 29 | 10% | 3.4% | +142.5% | -20.0% | -3.15% | 54% |
| dip45_V3_gescreend_fail | 170 | 17% | 8.2% | +115.4% | -31.2% | -6.21% | 100% |
| dip45_V3_alle | 205 | 16% | 7.8% | +114.7% | -30.0% | -6.74% | 100% |

## Beste variant: dip45_V3_gescreend_fail

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ❌
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
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
Sep 10 15:44:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:37,137 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:44:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:37,332 main INFO screen GOOG pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:44:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:44:40,835 main INFO screen FATTY pass=1 dev=3.79 ins=0.69 pro=57 1a=False 1b=False 2=False (2.1s)
Sep 10 15:45:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:45:37,385 main INFO screen nothing pass=0 dev=4.22 ins=9.44 pro=5 1a=False 1b=False 2=False (1.4s)
Sep 10 15:45:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:45:48,975 main INFO screen SEM pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 10 15:46:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:46:27,472 main INFO screen FERSPE pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 15:46:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:46:38,588 main INFO screen vrl pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (1.9s)
Sep 10 15:47:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:03,272 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:47:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:03,371 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:47:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:03,700 main INFO screen CASH pass=0 dev=0.0 ins=23.0 pro=15 1a=False 1b=False 2=True (0.5s)
Sep 10 15:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:14,080 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:14,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:47:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:14,400 main INFO screen CASH pass=0 dev=0.0 ins=78.85 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 15:47:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:25,629 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:47:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:25,733 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:47:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:25,861 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:47:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:31,171 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:47:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:31,292 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:47:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:31,692 main INFO screen KYS pass=0 dev=0.0 ins=25.65 pro=11 1a=False 1b=False 2=True (0.6s)
Sep 10 15:47:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:38,765 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:47:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:38,886 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:47:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:47:39,054 main INFO screen NEIL pass=0 dev=0.0 ins=22.68 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 15:48:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:48:09,920 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:48:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:48:10,025 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:48:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:48:10,212 main INFO screen NEMOTRON pass=1 dev=0.0 ins=18.79 pro=10 1a=False 1b=False 2=False (0.4s)
Sep 10 15:48:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:48:50,308 main INFO screen CRISPE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 10 15:49:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:49:23,575 main INFO screen Stimmy pass=0 dev=0.0 ins=17.26 pro=44 1a=False 1b=False 2=True (4.3s)
Sep 10 15:49:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:49:26,579 main INFO screen BPCATE pass=0 dev=2.34 ins=0.0 pro=1 1a=False 1b=False 2=False (1.7s)
Sep 10 15:49:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:49:33,900 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:49:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:49:34,016 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:49:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:49:34,155 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 15:50:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:50:37,123 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:50:37 +0000] "GET /health HTTP/1.1" 200 424 "-" "Python-urllib/3.14"
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
