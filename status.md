# Schaduwbot status

- tijd: 2026-09-12 00:45:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 10 hours, 58 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.2G/38G | geheugen: 992/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 18305, "tokens_in_memory": 6824, "msgs": 4215942, "trades": 753620, "creates": 6824, "decode_fail": 41061, "rpc_calls": 25248, "rpc_errors": 974, "sol_usd": 102.09786643881945, "open_positions": 65, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **37359**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 826 | 131 | 0 | 129 | 11 | 253 | 803 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 430 | 17% | 2.3% | +44.5% | -17.0% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 3585 | 27% | 3.6% | +45.6% | -25.9% | -6.81% | 100% |
| dip35_V1_alle | 4324 | 26% | 3.7% | +44.5% | -25.2% | -6.97% | 100% |
| dip35_V2_gescreend_pass | 427 | 22% | 3.3% | +45.3% | -21.5% | -7.10% | 100% |
| dip35_V2_gescreend_fail | 3606 | 25% | 4.2% | +56.4% | -28.1% | -7.23% | 100% |
| dip35_V2_alle | 4288 | 24% | 4.3% | +54.1% | -27.7% | -7.75% | 100% |
| dip35_V3_gescreend_pass | 428 | 9% | 3.7% | +331.7% | -22.9% | +7.80% | 100% |
| dip35_V3_gescreend_fail | 3682 | 13% | 5.9% | +119.1% | -29.6% | -9.76% | 100% |
| dip35_V3_alle | 4335 | 13% | 5.8% | +126.6% | -29.2% | -8.79% | 100% |
| dip40_V1_gescreend_pass | 400 | 15% | 2.5% | +47.3% | -16.3% | -6.96% | 100% |
| dip40_V1_gescreend_fail | 3515 | 26% | 3.7% | +47.4% | -25.9% | -6.70% | 100% |
| dip40_V1_alle | 4151 | 25% | 3.7% | +47.0% | -25.1% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 398 | 17% | 3.0% | +49.4% | -20.2% | -8.46% | 100% |
| dip40_V2_gescreend_fail | 3516 | 25% | 4.2% | +55.4% | -28.0% | -7.49% | 100% |
| dip40_V2_alle | 4108 | 24% | 4.3% | +54.0% | -27.5% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 401 | 8% | 3.2% | +343.8% | -21.4% | +5.91% | 100% |
| dip40_V3_gescreend_fail | 3591 | 13% | 5.8% | +116.6% | -29.5% | -10.50% | 100% |
| dip40_V3_alle | 4162 | 13% | 5.7% | +124.6% | -28.9% | -9.57% | 100% |
| dip45_V1_gescreend_pass | 385 | 16% | 2.3% | +48.8% | -16.2% | -5.91% | 100% |
| dip45_V1_gescreend_fail | 3431 | 27% | 3.2% | +47.9% | -25.6% | -5.51% | 100% |
| dip45_V1_alle | 4011 | 26% | 3.3% | +47.7% | -24.9% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 381 | 19% | 2.9% | +47.6% | -20.1% | -7.27% | 100% |
| dip45_V2_gescreend_fail | 3421 | 25% | 3.8% | +57.4% | -27.6% | -6.46% | 100% |
| dip45_V2_alle | 3965 | 24% | 3.9% | +55.8% | -27.1% | -7.07% | 100% |
| dip45_V3_gescreend_pass | 385 | 8% | 2.9% | +392.1% | -20.7% | +10.38% | 100% |
| dip45_V3_gescreend_fail | 3487 | 14% | 5.3% | +123.3% | -28.9% | -7.77% | 100% |
| dip45_V3_alle | 4015 | 13% | 5.3% | +134.0% | -28.4% | -6.74% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2772 | 13% | 3.8% | -10.06% | 100% |
| zonder_xlink | 863 | 18% | 0.0% | +23.78% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 00:29:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:29:14,849 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:29:14 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 00:29:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:29:33,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:29:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:29:39,019 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:30:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:30:00,205 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.3s)
Sep 12 00:30:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:30:33,678 main INFO screen SCREM pass=0 dev=1.88 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 12 00:31:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:31:05,034 main INFO screen pelmen pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (9.4s)
Sep 12 00:31:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:31:41,854 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:31:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:31:52,613 main INFO screen inprofit pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (10.9s)
Sep 12 00:32:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:16,046 main INFO screen $GOAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 12 00:32:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:38,085 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:32:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:39,911 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:32:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:45,366 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:32:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:46,934 main INFO screen B pass=1 dev=4.9 ins=11.81 pro=23 1a=False 1b=False 2=False (8.9s)
Sep 12 00:32:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:32:48,431 main INFO screen Snoopys pass=0 dev=1.24 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 12 00:33:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:33:04,282 main INFO screen ornot pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (24.5s)
Sep 12 00:33:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:33:13,335 main INFO screen STEEL pass=1 dev=3.08 ins=0.0 pro=39 1a=False 1b=False 2=False (3.2s)
Sep 12 00:33:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:33:48,382 main INFO screen STRANGE  pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 00:34:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:34:37,202 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:34:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 00:35:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:00,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:35:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:05,954 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:35:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:20,252 main INFO screen ROBUX pass=0 dev=0.0 ins=0.26 pro=24 1a=False 1b=False 2=True (19.5s)
Sep 12 00:35:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:39,027 main INFO screen $REGRET pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 12 00:35:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:45,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:35:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:35:50,069 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:03,477 main INFO screen Gurt pass=0 dev=0.0 ins=22.79 pro=34 1a=False 1b=False 2=True (18.5s)
Sep 12 00:36:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:07,276 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:12,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:27,123 main INFO screen     MIMI pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (19.9s)
Sep 12 00:36:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:47,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:52,121 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:53,692 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:36:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:36:58,759 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:37:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:07,351 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.4s)
Sep 12 00:37:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:08,819 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:37:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:12,816 main INFO screen Gurt pass=0 dev=6.63 ins=22.8 pro=40 1a=False 1b=False 2=True (19.2s)
Sep 12 00:37:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:16,089 main INFO screen TJR pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 12 00:37:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:28,872 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:37:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:37,236 main INFO screen DONKAI pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (8.4s)
Sep 12 00:37:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:51,292 main INFO screen ape  pass=1 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (3.3s)
Sep 12 00:37:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:37:55,956 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:01,027 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:15,860 main INFO screen HOOD pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 00:38:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:23,441 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:28,660 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:30,565 main INFO screen Canvas pass=1 dev=2.09 ins=8.39 pro=28 1a=False 1b=False 2=False (4.1s)
Sep 12 00:38:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:31,814 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:36,890 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:38:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:40,325 main INFO screen meme pass=0 dev=0.0 ins=18.27 pro=62 1a=False 1b=False 2=True (6.0s)
Sep 12 00:38:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:43,606 main INFO screen STEEL pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (20.2s)
Sep 12 00:38:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:48,480 main INFO screen blackswan pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.2s)
Sep 12 00:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:52,773 main INFO screen BEEP pass=0 dev=0.44 ins=47.66 pro=12 1a=False 1b=False 2=True (21.0s)
Sep 12 00:38:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:38:58,809 main INFO screen noob pass=0 dev=0.0 ins=17.73 pro=41 1a=False 1b=False 2=True (1.4s)
Sep 12 00:39:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:39:59,650 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:40:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:00,865 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:40:00 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 00:40:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:04,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:40:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:10,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:40:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:56,302 main INFO screen BIGO pass=0 dev=0.18 ins=79.13 pro=6 1a=False 1b=True 2=True (56.8s)
Sep 12 00:40:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:57,985 main INFO screen CTO pass=0 dev=0.0 ins=21.9 pro=15 1a=False 1b=False 2=True (47.1s)
Sep 12 00:40:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:40:59,935 main INFO screen DWAYNE pass=0 dev=1.97 ins=20.79 pro=62 1a=False 1b=False 2=True (5.6s)
Sep 12 00:41:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:41:35,512 main INFO screen coin pass=1 dev=0.0 ins=11.69 pro=22 1a=False 1b=False 2=False (1.4s)
Sep 12 00:41:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:41:55,487 main INFO screen retard pass=0 dev=0.0 ins=6.55 pro=47 1a=False 1b=False 2=True (2.5s)
Sep 12 00:42:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:42:19,282 main INFO screen fast pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (5.5s)
Sep 12 00:42:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:42:28,275 main INFO screen FREEDOM  pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 12 00:43:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:10,611 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:43:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:15,678 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:43:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:30,975 main INFO screen GAME pass=0 dev=0.0 ins=23.42 pro=21 1a=False 1b=False 2=True (20.5s)
Sep 12 00:43:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:35,342 main INFO screen RTD pass=1 dev=0.0 ins=5.53 pro=30 1a=False 1b=False 2=False (3.8s)
Sep 12 00:43:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:56,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:43:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:43:57,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:01,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:02,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:15,860 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:17,664 main INFO screen 777 pass=0 dev=0.0 ins=23.16 pro=11 1a=False 1b=False 2=True (21.7s)
Sep 12 00:44:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:18,881 main INFO screen Nasduck pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.6s)
Sep 12 00:44:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:20,951 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:35,514 main INFO screen FLYSTONKS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.1s)
Sep 12 00:44:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:46,864 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 00:44:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:44:53,361 main INFO screen 777 pass=0 dev=0.0 ins=22.93 pro=15 1a=False 1b=False 2=False (6.5s)
Sep 12 00:45:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:45:01,069 main INFO screen FLYSTONKS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 12 00:45:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 00:45:14,144 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:00:45:14 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T23:16:36Z
--- update 2026-09-11T23:22:10Z
--- update 2026-09-11T23:27:17Z
--- update 2026-09-11T23:32:26Z
--- update 2026-09-11T23:37:30Z
--- update 2026-09-11T23:42:35Z
--- update 2026-09-11T23:47:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: b162cdb09d844c599f2691bd2f42382f
analyses gestart (8746aefc73b4)
--- update 2026-09-11T23:52:35Z
--- update 2026-09-11T23:57:36Z
--- update 2026-09-12T00:02:54Z
--- update 2026-09-12T00:08:05Z
--- update 2026-09-12T00:13:36Z
--- update 2026-09-12T00:18:41Z
--- update 2026-09-12T00:24:13Z
--- update 2026-09-12T00:29:13Z
--- update 2026-09-12T00:34:36Z
--- update 2026-09-12T00:39:59Z
--- update 2026-09-12T00:45:13Z
```

## Analyses (laatste 25 regels)
```
inactive
23:47:43 ingelezen: 322040 nieuwe trades, 322040 bruikbaar (7s)
23:48:00 2429 aankopen van gevolgde wallets geëvalueerd
23:48:06 grote spelers: saldo van 404 wallets opgehaald
23:49:10 herkomst: 40 posities gekoppeld
23:49:11 klaar in 95s -> /opt/schaduwbot/reports/ledger.md
23:49:13   2000 nieuwe tokens doorgerekend
23:49:14 klaar in 4s: 8512 tokens, 2651 nieuw -> /opt/schaduwbot/reports/video_replay.md
23:49:15 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 23:49 UTC
23:49:15 43238 tokens geladen
23:49:17   2000 tokens, 267586 trades, 60734 posities (3s)
23:49:20   4000 tokens, 532423 trades, 117776 posities (5s)
23:49:22   6000 tokens, 799668 trades, 174921 posities (7s)
23:49:24   8000 tokens, 1110246 trades, 245252 posities (10s)
23:49:26   10000 tokens, 1366401 trades, 294918 posities (12s)
23:49:29   12000 tokens, 1641516 trades, 355008 posities (14s)
23:49:31   14000 tokens, 1922876 trades, 417966 posities (16s)
23:49:34   16000 tokens, 2201914 trades, 478052 posities (19s)
23:49:36   18000 tokens, 2446968 trades, 532110 posities (22s)
23:49:39   20000 tokens, 2731719 trades, 594313 posities (24s)
23:49:40 posities: 627709 uit 2860518 trades (26s)
23:49:48 141754 wallets gerekend
23:49:49 geluk-toets
23:50:14 persistentie
23:50:15 kopieer-simulatie
23:50:24 klaar in 70s -> /opt/schaduwbot/reports/wallets.md
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
