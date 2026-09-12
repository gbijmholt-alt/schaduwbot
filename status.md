# Schaduwbot status

- tijd: 2026-09-12 07:09:51 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 17 hours, 22 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1139/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 41382, "tokens_in_memory": 5738, "msgs": 7303972, "trades": 1364013, "creates": 12996, "decode_fail": 64806, "rpc_calls": 45685, "rpc_errors": 1830, "sol_usd": 101.77548224249998, "open_positions": 27, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **42500**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 6729 | 1110 | 6 | 1110 | 84 | 1962 | 5944 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 491 | 16% | 2.0% | +44.1% | -16.6% | -6.70% | 100% |
| dip35_V1_gescreend_fail | 4011 | 27% | 3.8% | +45.4% | -25.8% | -6.59% | 100% |
| dip35_V1_alle | 4911 | 26% | 3.9% | +44.6% | -25.2% | -6.80% | 100% |
| dip35_V2_gescreend_pass | 487 | 22% | 2.9% | +43.1% | -21.0% | -7.14% | 100% |
| dip35_V2_gescreend_fail | 4050 | 25% | 4.3% | +56.3% | -27.9% | -6.84% | 100% |
| dip35_V2_alle | 4880 | 25% | 4.5% | +53.8% | -27.5% | -7.53% | 100% |
| dip35_V3_gescreend_pass | 489 | 9% | 3.3% | +297.3% | -22.4% | +5.07% | 100% |
| dip35_V3_gescreend_fail | 4127 | 14% | 5.9% | +115.8% | -29.6% | -9.94% | 100% |
| dip35_V3_alle | 4921 | 13% | 5.9% | +120.6% | -29.1% | -9.34% | 100% |
| dip40_V1_gescreend_pass | 461 | 14% | 2.2% | +46.7% | -15.9% | -6.80% | 100% |
| dip40_V1_gescreend_fail | 3942 | 26% | 3.7% | +47.1% | -25.7% | -6.50% | 100% |
| dip40_V1_alle | 4720 | 25% | 3.8% | +47.2% | -25.0% | -6.64% | 100% |
| dip40_V2_gescreend_pass | 458 | 18% | 2.6% | +46.2% | -19.8% | -8.13% | 100% |
| dip40_V2_gescreend_fail | 3960 | 25% | 4.2% | +55.9% | -27.8% | -6.89% | 100% |
| dip40_V2_alle | 4684 | 24% | 4.3% | +54.3% | -27.3% | -7.65% | 100% |
| dip40_V3_gescreend_pass | 461 | 8% | 2.8% | +294.2% | -21.1% | +3.52% | 100% |
| dip40_V3_gescreend_fail | 4031 | 13% | 5.7% | +112.9% | -29.4% | -10.57% | 100% |
| dip40_V3_alle | 4727 | 13% | 5.7% | +118.5% | -28.9% | -9.97% | 100% |
| dip45_V1_gescreend_pass | 443 | 15% | 2.0% | +48.7% | -15.8% | -6.02% | 100% |
| dip45_V1_gescreend_fail | 3858 | 27% | 3.3% | +48.3% | -25.4% | -5.20% | 100% |
| dip45_V1_alle | 4565 | 26% | 3.4% | +48.6% | -24.7% | -5.48% | 100% |
| dip45_V2_gescreend_pass | 439 | 19% | 2.5% | +43.7% | -19.7% | -7.60% | 100% |
| dip45_V2_gescreend_fail | 3867 | 25% | 3.9% | +58.6% | -27.4% | -5.64% | 100% |
| dip45_V2_alle | 4528 | 24% | 4.0% | +57.4% | -27.0% | -6.30% | 100% |
| dip45_V3_gescreend_pass | 442 | 8% | 2.5% | +352.6% | -20.5% | +7.34% | 100% |
| dip45_V3_gescreend_fail | 3926 | 14% | 5.4% | +117.7% | -29.0% | -8.41% | 100% |
| dip45_V3_alle | 4564 | 13% | 5.3% | +126.4% | -28.4% | -7.67% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 3235 | 13% | 3.3% | -10.11% | 100% |
| zonder_xlink | 936 | 18% | 0.0% | +21.82% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 06:46:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:46:19,763 main INFO screen OUROBOROS pass=0 dev=0.0 ins=1.76 pro=66 1a=False 1b=False 2=True (21.4s)
Sep 12 06:47:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:47:29,106 main INFO screen GF pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 12 06:47:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:47:30,201 main INFO screen PepBack pass=0 dev=0.58 ins=0.0 pro=3 1a=False 1b=False 2=False (4.6s)
Sep 12 06:47:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:47:51,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:47:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:47:59,285 main INFO screen GASCAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 12 06:48:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:48:55,273 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:49:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:00,341 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:49:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:14,813 main INFO screen Mart pass=0 dev=6.18 ins=27.1 pro=26 1a=False 1b=False 2=True (19.7s)
Sep 12 06:49:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:23,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:49:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:28,397 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:49:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:37,148 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:49:37 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:49:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:43,257 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 06:49:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:54,201 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:49:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:49:59,275 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:50:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:50:13,780 main INFO screen Pepolepro pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.6s)
Sep 12 06:50:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:50:18,914 main INFO screen shizuku pass=1 dev=3.46 ins=0.0 pro=15 1a=False 1b=False 2=False (2.7s)
Sep 12 06:51:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:51:09,445 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:51:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:51:14,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:51:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:51:29,142 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 06:52:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:18,464 main INFO screen PepButt pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 12 06:52:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:26,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:52:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:31,875 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:52:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:34,724 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (3.7s)
Sep 12 06:52:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:37,594 main INFO screen stockmarket pass=0 dev=0.0 ins=16.36 pro=17 1a=False 1b=False 2=True (1.4s)
Sep 12 06:52:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:52:46,321 main INFO screen $speed pass=0 dev=0.24 ins=0.0 pro=2 1a=False 1b=False 2=False (19.9s)
Sep 12 06:53:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:53:19,926 main INFO screen RELOAD pass=1 dev=0.0 ins=6.07 pro=38 1a=False 1b=False 2=False (3.8s)
Sep 12 06:53:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:53:22,374 main INFO screen Flying Fly pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 12 06:53:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:53:39,770 main INFO screen coin pass=1 dev=0.0 ins=9.74 pro=38 1a=False 1b=False 2=False (1.7s)
Sep 12 06:54:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:54:40,277 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:54:40 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:54:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:54:46,593 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:54:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:54:51,620 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:54:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:54:53,723 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:54:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:54:58,793 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:55:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:06,678 main INFO screen SDC pass=0 dev=0.0 ins=15.93 pro=66 1a=False 1b=False 2=True (20.2s)
Sep 12 06:55:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:11,991 main INFO screen NASBATON pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (18.3s)
Sep 12 06:55:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:26,652 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:55:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:31,861 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:55:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:31,891 main INFO screen REVOLVE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 12 06:55:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:38,364 main INFO screen LOVER pass=0 dev=0.56 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 12 06:55:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:45,955 main INFO screen Bitcoin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.4s)
Sep 12 06:55:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:49,574 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:55:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:55:55,786 main INFO screen SDC pass=0 dev=3.94 ins=20.28 pro=14 1a=False 1b=False 2=False (6.3s)
Sep 12 06:57:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:57:07,528 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:57:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:57:15,175 main INFO screen $speed pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (7.7s)
Sep 12 06:57:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:57:37,880 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:57:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:57:42,950 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:57:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:57:56,216 main INFO screen crashcat pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (18.5s)
Sep 12 06:58:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:58:15,434 main INFO screen REVCAT pass=0 dev=0.65 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 12 06:58:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:58:43,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:58:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:58:48,346 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:58:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:58:59,743 main INFO screen PepATHlon pass=0 dev=2.18 ins=0.07 pro=4 1a=False 1b=False 2=False (3.2s)
Sep 12 06:59:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:59:03,362 main INFO screen TRAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 12 06:59:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:59:45,151 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:59:45 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:00:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:00:19,197 main INFO screen max pass=0 dev=8.75 ins=0.85 pro=52 1a=False 1b=False 2=False (8.0s)
Sep 12 07:00:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:00:42,669 main INFO screen PepATHlon pass=0 dev=0.48 ins=0.0 pro=3 1a=False 1b=False 2=False (7.0s)
Sep 12 07:00:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:00:56,712 main INFO screen HOODIEZEC pass=1 dev=0.0 ins=16.29 pro=22 1a=False 1b=False 2=False (9.1s)
Sep 12 07:02:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:02:05,309 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (5.9s)
Sep 12 07:02:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:02:05,826 main INFO screen RAPE pass=0 dev=0.0 ins=19.28 pro=51 1a=False 1b=False 2=True (3.6s)
Sep 12 07:02:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:02:47,173 main INFO screen PepASroni pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.5s)
Sep 12 07:04:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:04:48,704 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:04:48 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:05:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:05:11,745 main INFO screen Fries pass=0 dev=0.0 ins=26.26 pro=49 1a=False 1b=False 2=True (3.0s)
Sep 12 07:06:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:06:19,984 main INFO screen Pepsama pass=0 dev=2.57 ins=0.0 pro=4 1a=False 1b=False 2=False (6.8s)
Sep 12 07:07:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:07:04,750 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:07:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:07:09,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:07:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:07:13,034 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 12 07:07:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:07:26,781 main INFO screen BOIII pass=0 dev=0.17 ins=48.39 pro=12 1a=False 1b=False 2=True (22.1s)
Sep 12 07:07:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:07:44,485 main INFO screen ch pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=True (7.2s)
Sep 12 07:08:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:08:29,711 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (10.3s)
Sep 12 07:08:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:08:31,158 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:08:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:08:41,983 main INFO screen AnsemSS pass=0 dev=0.38 ins=0.0 pro=4 1a=False 1b=False 2=False (10.9s)
Sep 12 07:08:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:08:50,724 main INFO screen Revolver pass=0 dev=34.65 ins=0.0 pro=7 1a=False 1b=False 2=True (5.3s)
Sep 12 07:09:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:00,413 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:09:00 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:18,084 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:09:18 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:18,173 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:09:18 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:18,229 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:09:18 +0000] "GET /js/NewWindow_2_all.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:21,746 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:09:21 +0000] "GET /login HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:48,839 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:09:48 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:48,880 aiohttp.access INFO 185.226.197.64 [12/Sep/2026:07:09:48 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:48,914 aiohttp.access INFO 185.226.197.64 [12/Sep/2026:07:09:48 +0000] "GET /showLogin.cc HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:09:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:09:51,206 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:09:51 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T05:43:36Z
--- update 2026-09-12T05:48:37Z
--- update 2026-09-12T05:53:38Z
--- update 2026-09-12T05:58:38Z
Running as unit: schaduwbot-wallets.service; invocation ID: c28a94468726478892cb2c2291593995
analyses gestart (8746aefc73b4)
--- update 2026-09-12T06:03:40Z
--- update 2026-09-12T06:08:44Z
--- update 2026-09-12T06:13:49Z
--- update 2026-09-12T06:19:09Z
--- update 2026-09-12T06:24:26Z
--- update 2026-09-12T06:29:29Z
--- update 2026-09-12T06:34:34Z
--- update 2026-09-12T06:39:34Z
--- update 2026-09-12T06:44:35Z
--- update 2026-09-12T06:49:36Z
--- update 2026-09-12T06:54:39Z
--- update 2026-09-12T06:59:44Z
--- update 2026-09-12T07:04:47Z
--- update 2026-09-12T07:09:50Z
```

## Analyses (laatste 25 regels)
```
inactive
06:00:21 herkomst: 40 posities gekoppeld
06:00:24 klaar in 105s -> /opt/schaduwbot/reports/ledger.md
06:00:26   2000 nieuwe tokens doorgerekend
06:00:28 klaar in 4s: 15164 tokens, 2060 nieuw -> /opt/schaduwbot/reports/video_replay.md
06:00:28 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 06:00 UTC
06:00:28 49689 tokens geladen
06:00:31   2000 tokens, 246938 trades, 51841 posities (3s)
06:00:34   4000 tokens, 499800 trades, 105942 posities (5s)
06:00:36   6000 tokens, 751494 trades, 153475 posities (8s)
06:00:39   8000 tokens, 995808 trades, 202157 posities (11s)
06:00:42   10000 tokens, 1288195 trades, 264246 posities (14s)
06:00:44   12000 tokens, 1532978 trades, 311516 posities (16s)
06:00:47   14000 tokens, 1796554 trades, 361411 posities (19s)
06:00:49   16000 tokens, 2038896 trades, 410768 posities (21s)
06:00:53   18000 tokens, 2311003 trades, 467733 posities (25s)
06:00:56   20000 tokens, 2564416 trades, 517269 posities (27s)
06:00:59   22000 tokens, 2805731 trades, 565457 posities (30s)
06:01:01   24000 tokens, 3062477 trades, 617032 posities (33s)
06:01:04   26000 tokens, 3331606 trades, 674482 posities (36s)
06:01:06 posities: 714595 uit 3489207 trades (38s)
06:01:16 156866 wallets gerekend
06:01:17 geluk-toets
06:01:51 persistentie
06:01:53 kopieer-simulatie
06:02:09 klaar in 101s -> /opt/schaduwbot/reports/wallets.md
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
