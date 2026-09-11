# Schaduwbot status

- tijd: 2026-09-11 23:32:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 9 hours, 45 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.1G/38G | geheugen: 888/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 13938, "tokens_in_memory": 5231, "msgs": 3376161, "trades": 593578, "creates": 5231, "decode_fail": 35073, "rpc_calls": 19797, "rpc_errors": 751, "sol_usd": 102.2523615422199, "open_positions": 120, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 22:40 UTC

Gelogde schaduwtrades: **34765**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 26692 | 4119 | 41 | 4118 | 356 | 7605 | 22410 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 412 | 17% | 2.4% | +43.0% | -17.3% | -7.21% | 100% |
| dip35_V1_gescreend_fail | 3367 | 27% | 3.7% | +46.0% | -26.0% | -6.88% | 100% |
| dip35_V1_alle | 4023 | 26% | 3.7% | +44.8% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 407 | 21% | 3.4% | +46.2% | -21.9% | -7.52% | 100% |
| dip35_V2_gescreend_fail | 3380 | 25% | 4.3% | +56.5% | -28.3% | -7.45% | 100% |
| dip35_V2_alle | 3986 | 24% | 4.3% | +54.5% | -27.8% | -7.90% | 100% |
| dip35_V3_gescreend_pass | 410 | 8% | 3.9% | +349.6% | -23.1% | +8.70% | 100% |
| dip35_V3_gescreend_fail | 3453 | 13% | 5.9% | +120.6% | -29.8% | -9.84% | 100% |
| dip35_V3_alle | 4037 | 13% | 5.9% | +130.6% | -29.3% | -8.58% | 100% |
| dip40_V1_gescreend_pass | 381 | 15% | 2.6% | +46.5% | -16.7% | -7.38% | 100% |
| dip40_V1_gescreend_fail | 3296 | 26% | 3.7% | +47.8% | -25.9% | -6.68% | 100% |
| dip40_V1_alle | 3865 | 25% | 3.8% | +47.4% | -25.2% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 376 | 16% | 3.2% | +50.9% | -20.7% | -8.87% | 100% |
| dip40_V2_gescreend_fail | 3293 | 25% | 4.2% | +55.9% | -28.2% | -7.46% | 100% |
| dip40_V2_alle | 3821 | 24% | 4.3% | +54.9% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 382 | 7% | 3.4% | +367.0% | -21.6% | +6.84% | 100% |
| dip40_V3_gescreend_fail | 3361 | 13% | 5.7% | +115.5% | -29.6% | -10.85% | 100% |
| dip40_V3_alle | 3876 | 12% | 5.7% | +126.6% | -29.1% | -9.70% | 100% |
| dip45_V1_gescreend_pass | 366 | 16% | 2.5% | +49.0% | -16.5% | -5.98% | 100% |
| dip45_V1_gescreend_fail | 3214 | 27% | 3.3% | +48.4% | -25.7% | -5.52% | 100% |
| dip45_V1_alle | 3732 | 26% | 3.3% | +48.2% | -25.0% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 360 | 19% | 3.1% | +49.7% | -20.5% | -7.21% | 100% |
| dip45_V2_gescreend_fail | 3201 | 25% | 3.8% | +58.4% | -27.9% | -6.27% | 100% |
| dip45_V2_alle | 3687 | 24% | 3.9% | +57.0% | -27.3% | -6.89% | 100% |
| dip45_V3_gescreend_pass | 366 | 7% | 3.0% | +419.8% | -20.9% | +11.59% | 100% |
| dip45_V3_gescreend_fail | 3261 | 14% | 5.4% | +122.4% | -29.1% | -7.95% | 100% |
| dip45_V3_alle | 3738 | 13% | 5.3% | +135.9% | -28.5% | -6.65% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.5%, kans ruïne 99.5%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2662 | 13% | 4.0% | -10.32% | 100% |
| zonder_xlink | 798 | 18% | 0.0% | +26.25% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 23:23:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:10,901 main INFO screen CHILLBRAIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 11 23:23:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:20,454 main INFO screen flyson pass=1 dev=3.61 ins=0.0 pro=37 1a=False 1b=False 2=False (11.2s)
Sep 11 23:23:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:41,291 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:23:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:46,736 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:23:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:51,806 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:23:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:23:53,523 main INFO screen offgrannys pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.3s)
Sep 11 23:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:01,343 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:24:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:06,421 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:24:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:09,813 main INFO screen FLYWHEEL pass=0 dev=0.0 ins=60.0 pro=66 1a=False 1b=False 2=True (23.3s)
Sep 11 23:24:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:24,756 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.9 pro=20 1a=False 1b=False 2=True (23.5s)
Sep 11 23:24:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:25,614 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (9.6s)
Sep 11 23:24:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:27,900 main INFO screen WTF pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 23:24:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:32,117 main INFO screen BTC pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=False (7.4s)
Sep 11 23:24:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:49,020 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:24:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:54,090 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:24:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:54,653 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:24:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:24:59,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:25:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:25:14,275 main INFO screen Redbull pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.4s)
Sep 11 23:25:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:25:19,400 main INFO screen $POLAR pass=0 dev=6.63 ins=20.35 pro=35 1a=False 1b=False 2=True (24.8s)
Sep 11 23:25:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:25:45,804 main INFO screen lino pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 23:25:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:25:55,330 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:00,399 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:14,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:18,401 main INFO screen FLYTROLL pass=0 dev=0.0 ins=29.29 pro=32 1a=False 1b=False 2=True (9.2s)
Sep 11 23:26:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:19,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:20,020 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.78 pro=22 1a=False 1b=False 2=True (24.8s)
Sep 11 23:26:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:25,208 main INFO screen WC pass=0 dev=0.44 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 11 23:26:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:25,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:30,705 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:26:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:36,416 main INFO screen runnn pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 11 23:26:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:37,465 main INFO screen Neegyahu pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (23.4s)
Sep 11 23:26:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:53,303 main INFO screen Neegyahu pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 23:26:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:55,520 main INFO screen BROCCOLI pass=0 dev=0.4 ins=56.49 pro=23 1a=False 1b=False 2=True (29.9s)
Sep 11 23:26:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:26:57,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:27:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:02,361 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:27:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:07,734 main INFO screen $CAJUN pass=0 dev=0.78 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 23:27:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:14,484 main INFO screen WCOI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 11 23:27:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:16,946 main INFO screen GOONER pass=0 dev=1.05 ins=27.04 pro=45 1a=False 1b=False 2=True (20.0s)
Sep 11 23:27:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:18,236 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:27:18 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 23:27:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:27,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:27:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:32,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:27:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:51,913 main INFO screen FLYSEM pass=0 dev=0.0 ins=31.78 pro=25 1a=False 1b=False 2=True (24.4s)
Sep 11 23:27:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:27:55,902 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:28:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:00,972 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:28:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:09,219 main INFO screen WCOI pass=0 dev=2.42 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 11 23:28:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:20,599 main INFO screen homo pass=0 dev=0.0 ins=30.93 pro=17 1a=False 1b=False 2=True (24.8s)
Sep 11 23:28:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:22,812 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:28:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:27,840 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:28:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:48,581 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.9 pro=22 1a=False 1b=False 2=True (25.8s)
Sep 11 23:28:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:50,076 main INFO screen Bricko pass=0 dev=0.23 ins=0.0 pro=2 1a=False 1b=False 2=False (5.5s)
Sep 11 23:28:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:28:53,780 main INFO screen 911NYC pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 11 23:29:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:21,375 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (9.3s)
Sep 11 23:29:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:26,915 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:29:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:31,985 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:29:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:48,363 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (21.5s)
Sep 11 23:29:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:54,019 main INFO screen megaaaa pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 11 23:29:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:29:56,086 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:30:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:01,158 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:30:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:15,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:30:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:17,371 main INFO screen 1kcook pass=0 dev=0.89 ins=0.0 pro=4 1a=False 1b=False 2=False (7.7s)
Sep 11 23:30:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:20,616 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:30:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:21,462 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.44 pro=15 1a=False 1b=False 2=True (25.4s)
Sep 11 23:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:38,269 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:30:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:39,161 main INFO screen CAlien pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (23.7s)
Sep 11 23:30:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:30:43,298 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:01,530 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:02,505 main INFO screen GitHub pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.3s)
Sep 11 23:31:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:05,355 main INFO screen IssaBirb pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 23:31:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:06,578 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:19,769 main INFO screen PONSBRAIN pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 11 23:31:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:32,513 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:37,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:39,033 main INFO screen KYC pass=1 dev=0.0 ins=11.14 pro=55 1a=False 1b=False 2=False (2.9s)
Sep 11 23:31:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:52,408 main INFO screen FLYSEM pass=0 dev=10.23 ins=31.92 pro=18 1a=False 1b=False 2=True (19.9s)
Sep 11 23:31:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:54,271 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:31:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:31:59,338 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:32:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:32:12,600 main INFO screen CORF pass=0 dev=2.96 ins=39.88 pro=30 1a=False 1b=False 2=True (18.4s)
Sep 11 23:32:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:32:16,492 main INFO screen BTC pass=0 dev=0.8 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 23:32:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:32:20,804 main INFO screen DOGE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 11 23:32:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:32:27,188 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:32:27 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T21:53:06Z
--- update 2026-09-11T21:58:16Z
--- update 2026-09-11T22:03:36Z
--- update 2026-09-11T22:08:49Z
--- update 2026-09-11T22:14:14Z
--- update 2026-09-11T22:19:36Z
--- update 2026-09-11T22:25:36Z
--- update 2026-09-11T22:30:35Z
--- update 2026-09-11T22:35:46Z
--- update 2026-09-11T22:40:58Z
--- update 2026-09-11T22:45:58Z
--- update 2026-09-11T22:51:07Z
--- update 2026-09-11T22:56:09Z
--- update 2026-09-11T23:01:22Z
--- update 2026-09-11T23:06:34Z
--- update 2026-09-11T23:11:35Z
--- update 2026-09-11T23:16:36Z
--- update 2026-09-11T23:22:10Z
--- update 2026-09-11T23:27:17Z
--- update 2026-09-11T23:32:26Z
```

## Analyses (laatste 25 regels)
```
inactive
21:42:40   ingelezen tot rowid 2425120 (200000 rijen, 200000 bruikbaar)
21:42:43   ingelezen tot rowid 2533436 (308316 rijen, 308316 bruikbaar)
21:42:43 ingelezen: 308316 nieuwe trades, 308316 bruikbaar (6s)
21:42:56 777 aankopen van gevolgde wallets geëvalueerd
21:43:01 grote spelers: saldo van 425 wallets opgehaald
21:43:56 herkomst: 40 posities gekoppeld
21:43:58 klaar in 82s -> /opt/schaduwbot/reports/ledger.md
21:43:59 klaar in 1s: 6168 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
21:43:59 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 21:43 UTC
21:43:59 40246 tokens geladen
21:44:02   2000 tokens, 264665 trades, 62063 posities (3s)
21:44:04   4000 tokens, 539436 trades, 121662 posities (5s)
21:44:07   6000 tokens, 831867 trades, 188339 posities (8s)
21:44:10   8000 tokens, 1123316 trades, 253063 posities (10s)
21:44:12   10000 tokens, 1410949 trades, 318168 posities (13s)
21:44:15   12000 tokens, 1691732 trades, 380121 posities (16s)
21:44:18   14000 tokens, 1969718 trades, 443453 posities (19s)
21:44:20   16000 tokens, 2230065 trades, 499999 posities (21s)
21:44:23   18000 tokens, 2510034 trades, 567609 posities (24s)
21:44:23 posities: 576157 uit 2537772 trades (24s)
21:44:30 132608 wallets gerekend
21:44:31 geluk-toets
21:44:52 persistentie
21:44:53 kopieer-simulatie
21:45:01 klaar in 62s -> /opt/schaduwbot/reports/wallets.md
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
