# Schaduwbot status

- tijd: 2026-09-11 18:48:57 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 5 hours, 2 minutes
- bot-service: active
- code-versie: a16a395
- schijf: 2.8G/38G | geheugen: 540/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 639, "tokens_in_memory": 251, "msgs": 76719, "trades": 20538, "creates": 251, "decode_fail": 1403, "rpc_calls": 1037, "rpc_errors": 21, "sol_usd": 101.22778366561309, "open_positions": 32, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 18:38 UTC

Gelogde schaduwtrades: **29225**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 21102 | 3124 | 32 | 3124 | 226 | 5704 | 16870 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 323 | 17% | 1.9% | +42.4% | -16.4% | -6.56% | 99% |
| dip35_V1_gescreend_fail | 2946 | 27% | 3.6% | +46.3% | -25.9% | -6.28% | 100% |
| dip35_V1_alle | 3379 | 26% | 3.7% | +45.5% | -25.2% | -6.56% | 100% |
| dip35_V2_gescreend_pass | 320 | 19% | 2.5% | +45.7% | -21.3% | -8.32% | 100% |
| dip35_V2_gescreend_fail | 2955 | 25% | 4.3% | +57.5% | -28.1% | -6.80% | 100% |
| dip35_V2_alle | 3357 | 24% | 4.3% | +56.0% | -27.7% | -7.39% | 100% |
| dip35_V3_gescreend_pass | 323 | 8% | 2.8% | +283.6% | -22.7% | +2.94% | 100% |
| dip35_V3_gescreend_fail | 2993 | 13% | 5.9% | +119.2% | -29.7% | -9.72% | 100% |
| dip35_V3_alle | 3392 | 13% | 5.8% | +126.0% | -29.3% | -8.95% | 100% |
| dip40_V1_gescreend_pass | 299 | 15% | 1.7% | +46.4% | -15.4% | -6.30% | 99% |
| dip40_V1_gescreend_fail | 2861 | 27% | 3.6% | +48.3% | -25.9% | -6.20% | 100% |
| dip40_V1_alle | 3247 | 26% | 3.6% | +47.8% | -25.1% | -6.39% | 100% |
| dip40_V2_gescreend_pass | 297 | 15% | 2.4% | +50.5% | -19.9% | -9.45% | 100% |
| dip40_V2_gescreend_fail | 2858 | 25% | 4.1% | +56.7% | -28.1% | -7.00% | 100% |
| dip40_V2_alle | 3219 | 24% | 4.2% | +56.0% | -27.5% | -7.65% | 100% |
| dip40_V3_gescreend_pass | 301 | 7% | 2.3% | +326.5% | -20.9% | +2.16% | 100% |
| dip40_V3_gescreend_fail | 2898 | 13% | 5.8% | +108.5% | -29.6% | -11.72% | 100% |
| dip40_V3_alle | 3258 | 12% | 5.6% | +117.4% | -29.0% | -10.82% | 100% |
| dip45_V1_gescreend_pass | 286 | 15% | 1.4% | +51.5% | -15.1% | -4.86% | 98% |
| dip45_V1_gescreend_fail | 2781 | 27% | 3.2% | +49.0% | -25.6% | -5.11% | 100% |
| dip45_V1_alle | 3132 | 26% | 3.2% | +48.9% | -24.8% | -5.33% | 100% |
| dip45_V2_gescreend_pass | 283 | 18% | 2.1% | +49.4% | -19.3% | -7.15% | 99% |
| dip45_V2_gescreend_fail | 2769 | 25% | 3.8% | +59.9% | -27.6% | -5.73% | 100% |
| dip45_V2_alle | 3104 | 24% | 3.8% | +58.9% | -27.1% | -6.25% | 100% |
| dip45_V3_gescreend_pass | 287 | 7% | 2.1% | +379.4% | -20.1% | +7.75% | 100% |
| dip45_V3_gescreend_fail | 2803 | 14% | 5.5% | +117.3% | -29.1% | -8.87% | 100% |
| dip45_V3_alle | 3137 | 13% | 5.3% | +128.1% | -28.5% | -7.70% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2161 | 12% | 2.7% | -9.76% | 100% |
| zonder_xlink | 558 | 18% | 0.0% | +21.55% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 48min 5.317s CPU time over 8h 48min 33.144s wall clock time, 732.6M memory peak.
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 18:38:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:38:18,233 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 18:38:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:38:18,343 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:38:18 +0000] "GET /health HTTP/1.1" 200 230 "-" "Python-urllib/3.14"
Sep 11 18:39:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:13,102 main INFO screen RAY6900 pass=0 dev=0.0 ins=15.36 pro=31 1a=False 1b=True 2=True (3.8s)
Sep 11 18:39:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:16,013 main INFO screen APPLECAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (6.6s)
Sep 11 18:39:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:16,852 main INFO screen DOGSOL pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 11 18:39:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:20,145 main INFO screen SIXSEVEN pass=0 dev=0.96 ins=0.0 pro=9 1a=False 1b=False 2=False (7.0s)
Sep 11 18:39:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:34,141 main INFO screen pic  pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.5s)
Sep 11 18:39:48 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:39:48,066 main INFO screen sol pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.5s)
Sep 11 18:40:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:40:15,079 main INFO screen sol pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (2.1s)
Sep 11 18:40:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:40:36,933 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (2.3s)
Sep 11 18:40:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:40:42,793 main INFO screen $REGRET pass=0 dev=2.79 ins=0.0 pro=6 1a=False 1b=False 2=False (2.5s)
Sep 11 18:40:53 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:40:53,831 main INFO screen KAROTEKIPU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 18:41:09 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:09,953 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:41:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:17,509 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 11 18:41:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:23,814 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (1.9s)
Sep 11 18:41:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:38,121 main INFO screen SOFT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 11 18:41:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:38,862 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:41:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:42,372 main INFO screen APPLECAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (5.4s)
Sep 11 18:41:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:42,615 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:41:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:42,999 main INFO screen $REGRET pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (4.0s)
Sep 11 18:41:45 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:45,190 main INFO screen CHOGE pass=1 dev=0.0 ins=19.13 pro=13 1a=False 1b=False 2=False (7.2s)
Sep 11 18:41:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:50,348 main INFO screen APPLECAT pass=0 dev=0.61 ins=0.0 pro=4 1a=False 1b=False 2=False (8.0s)
Sep 11 18:41:55 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:41:55,021 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:42:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:02,816 main INFO screen wind pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (7.8s)
Sep 11 18:42:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:11,773 main INFO screen Fukall pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 18:42:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:21,376 main INFO screen hamster pass=0 dev=7.97 ins=0.0 pro=6 1a=False 1b=False 2=False (3.7s)
Sep 11 18:42:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:44,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:42:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:49,365 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:42:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:51,365 main INFO screen CHOGE pass=0 dev=0.0 ins=20.52 pro=13 1a=False 1b=False 2=False (6.9s)
Sep 11 18:42:54 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:54,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:42:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:42:59,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:43:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:04,652 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:43:09 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:09,400 main INFO screen SOLAMA pass=0 dev=6.63 ins=72.68 pro=1 1a=False 1b=True 2=True (20.1s)
Sep 11 18:43:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:12,577 main INFO screen SIXSEVEN pass=0 dev=1.3 ins=0.0 pro=5 1a=False 1b=False 2=False (3.5s)
Sep 11 18:43:14 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:14,340 main INFO screen $REGRET pass=0 dev=3.42 ins=0.0 pro=1 1a=False 1b=False 2=True (1.8s)
Sep 11 18:43:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:22,311 main INFO screen ELON pass=1 dev=0.72 ins=0.0 pro=82 1a=False 1b=False 2=False (22.8s)
Sep 11 18:43:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:37,222 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:43:37 +0000] "GET /health HTTP/1.1" 200 437 "-" "Python-urllib/3.14"
Sep 11 18:43:48 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:43:48,873 main INFO screen $GOAT10 pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (3.1s)
Sep 11 18:44:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:44:22,986 main INFO screen winning pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.7s)
Sep 11 18:44:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:44:37,308 main INFO screen Unicorn pass=0 dev=0.17 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 18:44:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:44:50,259 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:44:55 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:44:55,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:44:58 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:44:58,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:45:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:07,357 main INFO screen $GOAT10 pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 11 18:45:10 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:10,606 main INFO screen CHARLIE pass=1 dev=1.83 ins=0.0 pro=76 1a=False 1b=False 2=False (20.4s)
Sep 11 18:45:24 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:24,935 main INFO screen SIXSEVEN pass=0 dev=0.1 ins=0.0 pro=7 1a=False 1b=False 2=False (4.1s)
Sep 11 18:45:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:26,224 main INFO screen bfwm pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (4.3s)
Sep 11 18:45:27 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:27,587 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:45:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:34,862 main INFO screen SMOKE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (7.3s)
Sep 11 18:45:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:41,213 main INFO screen DUDE pass=1 dev=0.5 ins=0.0 pro=52 1a=False 1b=False 2=False (4.1s)
Sep 11 18:45:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:41,825 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:45:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:43,282 main INFO screen spink pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 11 18:45:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:47,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:45:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:45:49,396 main INFO screen $QAIS pass=0 dev=2.08 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 11 18:46:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:01,093 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.0s)
Sep 11 18:46:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:03,943 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:46:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:11,597 main INFO screen SIXSEVEN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 11 18:46:24 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:24,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:46:31 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:31,804 main INFO screen SUITERDOG pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (7.2s)
Sep 11 18:46:48 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:48,315 main INFO screen crime pass=0 dev=0.2 ins=0.0 pro=1 1a=False 1b=False 2=True (1.8s)
Sep 11 18:46:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:50,333 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:46:55 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:46:55,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:47:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:02,616 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:47:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:06,165 main INFO screen $REGRET pass=0 dev=3.42 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 11 18:47:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:13,242 main INFO screen Tcat pass=0 dev=1.74 ins=0.0 pro=6 1a=False 1b=False 2=False (7.1s)
Sep 11 18:47:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:18,494 main INFO screen DUDE pass=1 dev=0.0 ins=1.25 pro=74 1a=False 1b=False 2=False (28.2s)
Sep 11 18:47:24 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:24,987 main INFO screen AI pass=0 dev=0.0 ins=15.1 pro=54 1a=False 1b=False 2=True (22.5s)
Sep 11 18:47:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:26,906 main INFO screen Vee pass=0 dev=0.0 ins=24.21 pro=55 1a=False 1b=False 2=True (8.4s)
Sep 11 18:47:27 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:27,839 main INFO screen USDTPrint pass=0 dev=0.25 ins=0.0 pro=9 1a=False 1b=False 2=False (14.6s)
Sep 11 18:47:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:47:37,154 main INFO screen SIXSEVEN pass=0 dev=1.51 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 18:48:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:48:02,118 main INFO screen CHAROC pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 18:48:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:48:07,138 main INFO screen rich pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 18:48:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:48:07,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:48:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:48:13,966 main INFO screen NOOB pass=0 dev=0.0 ins=14.18 pro=15 1a=False 1b=False 2=True (6.3s)
Sep 11 18:48:57 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:48:57,277 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:48:57 +0000] "GET /health HTTP/1.1" 200 441 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T17:41:37Z
--- update 2026-09-11T17:46:37Z
--- update 2026-09-11T17:51:39Z
--- update 2026-09-11T17:56:40Z
--- update 2026-09-11T18:01:40Z
--- update 2026-09-11T18:06:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: f4240d03c1404a3aa0fe2959269b0656
analyses gestart (8213ec5e675e)
--- update 2026-09-11T18:11:40Z
--- update 2026-09-11T18:17:20Z
--- update 2026-09-11T18:22:26Z
--- update 2026-09-11T18:27:35Z
--- update 2026-09-11T18:32:36Z
--- update 2026-09-11T18:38:13Z
nieuwe code: a16a395
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 1322d8308bda44ab89e4732e0436b52e
analyses gestart (ed3e144883fd)
--- update 2026-09-11T18:43:36Z
--- update 2026-09-11T18:48:56Z
```

## Analyses (laatste 25 regels)
```
inactive
18:07:51 persistentie
18:07:53 kopieer-simulatie
18:08:00 klaar in 58s -> /opt/schaduwbot/reports/wallets.md
18:38:17 11258 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
18:38:19   ingelezen tot rowid 2079733 (84068 rijen, 84068 bruikbaar)
18:38:19 ingelezen: 84068 nieuwe trades, 84068 bruikbaar (2s)
18:38:32 3000 aankopen van gevolgde wallets geëvalueerd
18:39:36 herkomst: 40 posities gekoppeld
18:39:37 klaar in 80s -> /opt/schaduwbot/reports/ledger.md
18:39:38 klaar in 0s: 2161 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
18:39:38 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 18:39 UTC
18:39:38 36134 tokens geladen
18:39:41   2000 tokens, 289638 trades, 71839 posities (3s)
18:39:43   4000 tokens, 572568 trades, 137840 posities (5s)
18:39:46   6000 tokens, 886184 trades, 210864 posities (9s)
18:39:49   8000 tokens, 1172465 trades, 278408 posities (11s)
18:39:52   10000 tokens, 1467251 trades, 349490 posities (14s)
18:39:55   12000 tokens, 1745027 trades, 416754 posities (17s)
18:39:57   14000 tokens, 2037014 trades, 487116 posities (19s)
18:39:58 posities: 500309 uit 2080675 trades (20s)
18:40:05 118282 wallets gerekend
18:40:06 geluk-toets
18:40:25 persistentie
18:40:27 kopieer-simulatie
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
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
