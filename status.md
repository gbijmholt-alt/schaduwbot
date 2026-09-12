# Schaduwbot status

- tijd: 2026-09-12 03:28:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 13 hours, 41 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1095/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 28109, "tokens_in_memory": 7635, "msgs": 5637734, "trades": 1037435, "creates": 9822, "decode_fail": 54909, "rpc_calls": 35114, "rpc_errors": 1430, "sol_usd": 101.66671197179325, "open_positions": 36, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **39337**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 3089 | 511 | 3 | 510 | 29 | 905 | 2781 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 448 | 17% | 2.2% | +44.4% | -16.9% | -6.46% | 100% |
| dip35_V1_gescreend_fail | 3748 | 27% | 3.7% | +45.6% | -25.9% | -6.79% | 100% |
| dip35_V1_alle | 4548 | 26% | 3.8% | +44.7% | -25.2% | -6.89% | 100% |
| dip35_V2_gescreend_pass | 445 | 22% | 3.1% | +43.5% | -21.4% | -7.14% | 100% |
| dip35_V2_gescreend_fail | 3781 | 25% | 4.3% | +56.5% | -27.9% | -7.17% | 100% |
| dip35_V2_alle | 4516 | 24% | 4.4% | +54.0% | -27.6% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 447 | 8% | 3.6% | +323.1% | -22.7% | +6.69% | 100% |
| dip35_V3_gescreend_fail | 3854 | 13% | 5.9% | +117.5% | -29.6% | -9.99% | 100% |
| dip35_V3_alle | 4560 | 13% | 5.9% | +124.0% | -29.2% | -9.14% | 100% |
| dip40_V1_gescreend_pass | 418 | 15% | 2.4% | +47.1% | -16.2% | -6.64% | 100% |
| dip40_V1_gescreend_fail | 3681 | 26% | 3.8% | +47.5% | -25.8% | -6.60% | 100% |
| dip40_V1_alle | 4370 | 25% | 3.8% | +47.4% | -25.1% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 416 | 18% | 2.9% | +46.1% | -20.1% | -8.33% | 100% |
| dip40_V2_gescreend_fail | 3693 | 25% | 4.3% | +55.5% | -27.9% | -7.24% | 100% |
| dip40_V2_alle | 4332 | 24% | 4.4% | +53.8% | -27.4% | -7.91% | 100% |
| dip40_V3_gescreend_pass | 419 | 7% | 3.1% | +332.9% | -21.3% | +4.87% | 100% |
| dip40_V3_gescreend_fail | 3761 | 13% | 5.8% | +115.7% | -29.4% | -10.49% | 100% |
| dip40_V3_alle | 4378 | 13% | 5.8% | +122.6% | -28.9% | -9.72% | 100% |
| dip45_V1_gescreend_pass | 402 | 16% | 2.2% | +48.7% | -16.1% | -5.78% | 100% |
| dip45_V1_gescreend_fail | 3596 | 27% | 3.3% | +48.4% | -25.5% | -5.29% | 100% |
| dip45_V1_alle | 4223 | 26% | 3.4% | +48.4% | -24.8% | -5.60% | 100% |
| dip45_V2_gescreend_pass | 399 | 19% | 2.8% | +45.1% | -20.0% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 3598 | 25% | 3.9% | +58.0% | -27.5% | -6.06% | 100% |
| dip45_V2_alle | 4185 | 24% | 4.0% | +56.1% | -27.1% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 402 | 7% | 2.7% | +392.1% | -20.7% | +9.12% | 100% |
| dip45_V3_gescreend_fail | 3656 | 14% | 5.5% | +121.3% | -29.0% | -7.99% | 100% |
| dip45_V3_alle | 4225 | 13% | 5.5% | +131.2% | -28.5% | -7.14% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2926 | 13% | 3.6% | -10.08% | 100% |
| zonder_xlink | 870 | 19% | 0.0% | +23.66% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 03:13:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:23,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:13:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:28,267 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:13:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:47,959 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.9s)
Sep 12 03:13:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:50,708 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:13:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:53,259 main INFO screen Googles pass=1 dev=0.0 ins=13.16 pro=20 1a=False 1b=False 2=False (9.9s)
Sep 12 03:13:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:55,774 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:13:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:13:59,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:14:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:14:04,575 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:14:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:14:13,688 main INFO screen Googles pass=0 dev=0.0 ins=22.05 pro=35 1a=True 1b=False 2=True (23.1s)
Sep 12 03:14:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:14:19,076 main INFO screen X pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 03:14:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:14:47,848 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:15:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:15:00,436 main INFO screen Token pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (12.7s)
Sep 12 03:15:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:15:15,560 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:15:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:15:20,629 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:15:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:15:40,448 main INFO screen CHILLBRAIN pass=0 dev=2.42 ins=40.61 pro=17 1a=False 1b=False 2=True (25.0s)
Sep 12 03:16:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:02,333 main INFO screen CGL pass=0 dev=3.43 ins=0.0 pro=7 1a=False 1b=False 2=False (8.0s)
Sep 12 03:16:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:05,664 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:16:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:08,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:16:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:10,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:16:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:18,781 main INFO screen NETFLIIX pass=0 dev=6.63 ins=21.72 pro=27 1a=False 1b=False 2=False (10.8s)
Sep 12 03:16:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:20,133 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:16:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:26,374 main INFO screen OLIVE pass=0 dev=0.0 ins=22.6 pro=62 1a=False 1b=False 2=True (20.8s)
Sep 12 03:16:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:34,107 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (14.0s)
Sep 12 03:16:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:36,728 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:16:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:16:41,803 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:17:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:17:03,938 main INFO screen Watching pass=0 dev=0.0 ins=14.79 pro=67 1a=False 1b=False 2=True (27.3s)
Sep 12 03:17:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:17:04,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:17:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:17:09,792 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:17:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:17:29,345 main INFO screen Benz pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.7s)
Sep 12 03:17:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:17:55,322 main INFO screen skipoo pass=0 dev=1.42 ins=0.0 pro=3 1a=False 1b=False 2=False (8.4s)
Sep 12 03:18:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:08,587 main INFO screen GPU pass=1 dev=0.0 ins=0.62 pro=34 1a=False 1b=False 2=False (9.4s)
Sep 12 03:18:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:11,731 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:18:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:16,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:18:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:30,704 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:18:30 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 03:18:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:34,847 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (23.2s)
Sep 12 03:18:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:39,526 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:18:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:43,337 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:18:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:43,583 main INFO screen CAT pass=0 dev=0.0 ins=30.74 pro=20 1a=False 1b=True 2=True (6.2s)
Sep 12 03:18:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:53,125 main INFO screen V2Tooth pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (13.8s)
Sep 12 03:18:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:18:57,035 main INFO screen DCVU pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (13.7s)
Sep 12 03:19:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:05,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:19:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:10,747 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:19:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:21,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:19:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:26,614 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:19:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:32,988 main INFO screen Bulljak pass=0 dev=1.39 ins=41.08 pro=9 1a=False 1b=False 2=True (27.4s)
Sep 12 03:19:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:19:42,163 main INFO screen NIGGA pass=0 dev=0.0 ins=20.93 pro=69 1a=False 1b=False 2=True (20.7s)
Sep 12 03:21:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:21:17,750 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:21:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:21:30,146 main INFO screen wind pass=0 dev=2.92 ins=0.0 pro=3 1a=False 1b=False 2=False (12.5s)
Sep 12 03:21:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:21:46,860 main INFO screen WENIS pass=0 dev=3.76 ins=10.84 pro=42 1a=False 1b=False 2=True (7.3s)
Sep 12 03:22:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:04,842 main INFO screen crabcat pass=1 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (9.0s)
Sep 12 03:22:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:08,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:22:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:13,901 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:22:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:23,909 main INFO screen FlyingMan pass=0 dev=2.22 ins=0.0 pro=4 1a=False 1b=False 2=False (6.9s)
Sep 12 03:22:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:27,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:22:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:28,576 main INFO screen KURONEKO pass=0 dev=0.0 ins=13.27 pro=16 1a=False 1b=False 2=True (19.8s)
Sep 12 03:22:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:40,185 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.7s)
Sep 12 03:22:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:46,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:22:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:22:59,993 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (14.1s)
Sep 12 03:23:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:28,198 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:23:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:33,266 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:23:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:37,138 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:23:37 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 03:23:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:49,589 main INFO screen ICDA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 12 03:23:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:52,196 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.1s)
Sep 12 03:23:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:23:55,666 main INFO screen CRASHGPT pass=0 dev=35.28 ins=0.0 pro=4 1a=False 1b=False 2=True (10.0s)
Sep 12 03:24:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:24:16,993 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:24:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:24:29,456 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (12.6s)
Sep 12 03:24:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:24:49,843 main INFO screen HUSDC pass=0 dev=1.27 ins=18.95 pro=9 1a=False 1b=True 2=False (5.0s)
Sep 12 03:25:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:25:47,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:25:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:25:52,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:26:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:10,864 main INFO screen V3Tooth pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (23.3s)
Sep 12 03:26:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:14,674 main INFO screen wiftism pass=0 dev=0.0 ins=22.33 pro=61 1a=False 1b=False 2=True (2.5s)
Sep 12 03:26:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:16,421 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:26:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:21,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:26:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:41,536 main INFO screen $HUG pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.1s)
Sep 12 03:26:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:26:48,694 main INFO screen skipoo pass=0 dev=1.81 ins=0.0 pro=4 1a=False 1b=False 2=False (10.0s)
Sep 12 03:27:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:27:38,706 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:27:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:27:47,205 main INFO screen stockmarket pass=0 dev=0.0 ins=11.96 pro=61 1a=False 1b=False 2=True (8.6s)
Sep 12 03:28:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:28:16,778 main INFO screen . pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 12 03:28:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:28:36,933 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 03:28:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 03:28:38,203 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:03:28:38 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (8746aefc73b4)
--- update 2026-09-12T01:57:21Z
--- update 2026-09-12T02:02:22Z
--- update 2026-09-12T02:07:22Z
--- update 2026-09-12T02:12:26Z
--- update 2026-09-12T02:17:29Z
--- update 2026-09-12T02:22:33Z
--- update 2026-09-12T02:27:33Z
--- update 2026-09-12T02:32:33Z
--- update 2026-09-12T02:37:36Z
--- update 2026-09-12T02:42:48Z
--- update 2026-09-12T02:47:52Z
--- update 2026-09-12T02:52:55Z
--- update 2026-09-12T02:58:01Z
--- update 2026-09-12T03:03:02Z
--- update 2026-09-12T03:08:04Z
--- update 2026-09-12T03:13:08Z
--- update 2026-09-12T03:18:29Z
--- update 2026-09-12T03:23:36Z
--- update 2026-09-12T03:28:37Z
```

## Analyses (laatste 25 regels)
```
inactive
01:52:48 3000 aankopen van gevolgde wallets geëvalueerd
01:53:00 grote spelers: saldo van 1359 wallets opgehaald
01:53:57 herkomst: 40 posities gekoppeld
01:53:58 klaar in 97s -> /opt/schaduwbot/reports/ledger.md
01:54:00   2000 nieuwe tokens doorgerekend
01:54:02 klaar in 4s: 11080 tokens, 2981 nieuw -> /opt/schaduwbot/reports/video_replay.md
01:54:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 01:54 UTC
01:54:02 45856 tokens geladen
01:54:04   2000 tokens, 253102 trades, 54428 posities (2s)
01:54:07   4000 tokens, 520825 trades, 111725 posities (5s)
01:54:09   6000 tokens, 782379 trades, 167557 posities (7s)
01:54:11   8000 tokens, 1054119 trades, 222555 posities (9s)
01:54:13   10000 tokens, 1329211 trades, 281413 posities (11s)
01:54:16   12000 tokens, 1594580 trades, 333921 posities (13s)
01:54:18   14000 tokens, 1836819 trades, 382990 posities (15s)
01:54:20   16000 tokens, 2119459 trades, 446339 posities (18s)
01:54:22   18000 tokens, 2395048 trades, 502642 posities (20s)
01:54:24   20000 tokens, 2629029 trades, 552671 posities (22s)
01:54:27   22000 tokens, 2903307 trades, 608372 posities (24s)
01:54:29 posities: 660394 uit 3108846 trades (26s)
01:54:37 148332 wallets gerekend
01:54:38 geluk-toets
01:55:03 persistentie
01:55:05 kopieer-simulatie
01:55:14 klaar in 72s -> /opt/schaduwbot/reports/wallets.md
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
