# Schaduwbot status

- tijd: 2026-09-10 15:33:42 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 hour, 46 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 552/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 6325, "tokens_in_memory": 1509, "msgs": 941552, "trades": 200318, "creates": 2489, "decode_fail": 21226, "rpc_calls": 3405, "rpc_errors": 411, "sol_usd": 99.8346106758931, "open_positions": 81}
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
Sep 10 15:24:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:24:23,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:24:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:24:23,180 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:24:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:24:27,895 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 10 15:24:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:24:39,950 main INFO screen you6 pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 10 15:24:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:24:42,757 main INFO screen SMR pass=1 dev=0.0 ins=13.34 pro=22 1a=False 1b=False 2=False (3.9s)
Sep 10 15:25:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:09,712 main INFO screen p pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (9.4s)
Sep 10 15:25:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:43,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:25:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:43,756 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:25:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:48,407 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.9s)
Sep 10 15:25:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:57,272 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:25:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:25:57,394 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:26:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:00,632 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:26:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:00,797 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:26:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:03,329 main INFO screen Neil pass=0 dev=0.0 ins=27.21 pro=5 1a=False 1b=False 2=True (6.1s)
Sep 10 15:26:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:06,003 main INFO screen DOGERNAUT pass=0 dev=0.0 ins=78.71 pro=8 1a=False 1b=False 2=True (5.4s)
Sep 10 15:26:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:47,400 main INFO screen love pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 10 15:26:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:26:52,905 main INFO screen NEIL pass=1 dev=0.0 ins=19.04 pro=25 1a=False 1b=False 2=False (5.6s)
Sep 10 15:27:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:11,201 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:27:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:11,312 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:27:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:14,985 main INFO screen MIM pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 10 15:27:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:24,226 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (9.0s)
Sep 10 15:27:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:45,319 main INFO screen cash cat pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (6.4s)
Sep 10 15:27:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:46,109 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:27:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:46,261 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:27:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:27:51,136 main INFO screen BUZZ pass=0 dev=0.0 ins=52.0 pro=6 1a=False 1b=False 2=True (5.1s)
Sep 10 15:28:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:11,735 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:28:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:11,833 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:28:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:12,021 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:28:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:19,098 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:28:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:19,224 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:28:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:19,349 main INFO screen POOP pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.3s)
Sep 10 15:28:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:23,746 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:28:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:23,917 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:28:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:24,051 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 15:28:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:39,187 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:28:39 +0000] "GET /health HTTP/1.1" 200 423 "-" "Python-urllib/3.14"
Sep 10 15:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:46,635 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:46,735 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:28:46,920 main INFO screen MTF pass=0 dev=0.0 ins=19.51 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 10 15:29:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:11,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:29:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:11,250 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:29:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:11,439 main INFO screen MARIO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:19,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:19,282 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:19,455 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 15:29:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:23,748 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:29:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:23,877 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:29:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:24,009 main INFO screen MOON pass=1 dev=0.0 ins=1.17 pro=36 1a=False 1b=False 2=False (0.3s)
Sep 10 15:29:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:29:49,328 main INFO screen $AID TRr pass=0 dev=0.36 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 10 15:30:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:23,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:30:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:24,031 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:30:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:25,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:30:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:25,891 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:30:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:26,077 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 15:30:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:29,161 main INFO screen USELESS pass=1 dev=0.0 ins=9.84 pro=17 1a=False 1b=False 2=False (5.3s)
Sep 10 15:30:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:47,635 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:30:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:47,731 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:30:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:30:48,341 main INFO screen FATFILMS pass=0 dev=0.0 ins=24.44 pro=16 1a=False 1b=False 2=True (0.8s)
Sep 10 15:31:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:16,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:31:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:16,596 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:31:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:16,936 main INFO screen USEFUL pass=0 dev=0.0 ins=10.48 pro=24 1a=False 1b=False 2=True (0.5s)
Sep 10 15:31:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:37,732 main INFO screen SIKA pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 10 15:31:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:47,319 main INFO screen ROBOELON pass=1 dev=0.0 ins=18.62 pro=15 1a=False 1b=False 2=False (1.7s)
Sep 10 15:31:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:57,029 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:31:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:57,174 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:31:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:31:57,306 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 15:32:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:04,764 main INFO screen GB pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 10 15:32:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:11,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:32:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:11,446 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:32:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:11,637 main INFO screen cashback pass=0 dev=0.0 ins=3.92 pro=32 1a=False 1b=False 2=True (0.4s)
Sep 10 15:32:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:33,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:32:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:34,067 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:32:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:32:34,384 main INFO screen cash pass=0 dev=0.0 ins=16.5 pro=24 1a=False 1b=False 2=True (0.5s)
Sep 10 15:33:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:09,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:33:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:09,999 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:33:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:10,184 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:33:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:40,993 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 10 15:33:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:41,844 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 15:33:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:41,995 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 15:33:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:42,176 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 15:33:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 15:33:42,567 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:15:33:42 +0000] "GET /health HTTP/1.1" 200 422 "-" "Python-urllib/3.14"
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
