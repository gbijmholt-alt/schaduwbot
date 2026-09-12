# Schaduwbot status

- tijd: 2026-09-12 05:53:39 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 16 hours, 6 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1113/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 36811, "tokens_in_memory": 6258, "msgs": 6842634, "trades": 1252183, "creates": 11997, "decode_fail": 60781, "rpc_calls": 42317, "rpc_errors": 1713, "sol_usd": 101.62924634325006, "open_positions": 39, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **41671**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 5902 | 963 | 4 | 963 | 68 | 1678 | 5115 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 483 | 17% | 2.1% | +44.1% | -16.7% | -6.63% | 100% |
| dip35_V1_gescreend_fail | 3934 | 27% | 3.8% | +45.7% | -25.9% | -6.57% | 100% |
| dip35_V1_alle | 4815 | 26% | 3.9% | +44.9% | -25.2% | -6.73% | 100% |
| dip35_V2_gescreend_pass | 480 | 22% | 2.9% | +43.1% | -21.1% | -7.03% | 100% |
| dip35_V2_gescreend_fail | 3972 | 25% | 4.4% | +56.7% | -27.9% | -6.77% | 100% |
| dip35_V2_alle | 4785 | 25% | 4.5% | +54.2% | -27.6% | -7.44% | 100% |
| dip35_V3_gescreend_pass | 482 | 9% | 3.3% | +297.3% | -22.4% | +5.42% | 100% |
| dip35_V3_gescreend_fail | 4051 | 14% | 5.9% | +115.7% | -29.6% | -9.89% | 100% |
| dip35_V3_alle | 4829 | 13% | 6.0% | +120.8% | -29.2% | -9.23% | 100% |
| dip40_V1_gescreend_pass | 452 | 15% | 2.2% | +46.7% | -16.0% | -6.72% | 100% |
| dip40_V1_gescreend_fail | 3866 | 26% | 3.8% | +47.3% | -25.7% | -6.44% | 100% |
| dip40_V1_alle | 4627 | 26% | 3.8% | +47.4% | -25.0% | -6.53% | 100% |
| dip40_V2_gescreend_pass | 450 | 18% | 2.7% | +46.2% | -19.9% | -8.01% | 100% |
| dip40_V2_gescreend_fail | 3882 | 25% | 4.2% | +56.5% | -27.8% | -6.77% | 100% |
| dip40_V2_alle | 4591 | 24% | 4.4% | +54.8% | -27.3% | -7.50% | 100% |
| dip40_V3_gescreend_pass | 453 | 8% | 2.9% | +294.2% | -21.2% | +3.88% | 100% |
| dip40_V3_gescreend_fail | 3956 | 13% | 5.7% | +113.3% | -29.4% | -10.41% | 100% |
| dip40_V3_alle | 4637 | 13% | 5.7% | +119.2% | -28.9% | -9.77% | 100% |
| dip45_V1_gescreend_pass | 434 | 15% | 2.1% | +48.7% | -15.9% | -5.91% | 100% |
| dip45_V1_gescreend_fail | 3782 | 27% | 3.3% | +48.4% | -25.4% | -5.15% | 100% |
| dip45_V1_alle | 4473 | 26% | 3.4% | +48.6% | -24.7% | -5.46% | 100% |
| dip45_V2_gescreend_pass | 431 | 20% | 2.6% | +43.7% | -19.8% | -7.41% | 100% |
| dip45_V2_gescreend_fail | 3791 | 25% | 3.9% | +58.9% | -27.4% | -5.55% | 100% |
| dip45_V2_alle | 4438 | 24% | 4.0% | +56.9% | -27.0% | -6.40% | 100% |
| dip45_V3_gescreend_pass | 433 | 8% | 2.5% | +352.6% | -20.5% | +7.92% | 100% |
| dip45_V3_gescreend_fail | 3852 | 14% | 5.4% | +118.8% | -28.9% | -8.11% | 100% |
| dip45_V3_alle | 4476 | 14% | 5.4% | +127.6% | -28.4% | -7.35% | 100% |

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
| met_xlink | 3183 | 13% | 3.3% | -10.01% | 100% |
| zonder_xlink | 915 | 19% | 0.0% | +22.62% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 05:39:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:04,912 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:05:39:04 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 05:39:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:14,210 main INFO screen cap pass=0 dev=1.72 ins=0.0 pro=4 1a=False 1b=False 2=False (4.2s)
Sep 12 05:39:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:17,369 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:39:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:22,437 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:39:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:32,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:39:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:36,372 main INFO screen cc pass=0 dev=0.0 ins=14.85 pro=57 1a=False 1b=False 2=True (19.1s)
Sep 12 05:39:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:41,064 main INFO screen LIL C pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 12 05:39:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:39:53,322 main INFO screen SHIB pass=0 dev=0.47 ins=0.0 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 12 05:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:41:04,253 aiohttp.access INFO 3.130.168.2 [12/Sep/2026:05:41:04 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 05:41:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:41:07,852 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (3.5s)
Sep 12 05:41:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:41:21,239 aiohttp.access INFO 3.130.168.2 [12/Sep/2026:05:41:21 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 05:41:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:41:40,717 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 12 05:42:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:42:07,404 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.8s)
Sep 12 05:43:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:19,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:43:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:28,139 main INFO screen revolve pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 12 05:43:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:33,235 main INFO screen LOVER pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 12 05:43:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:37,148 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:43:37 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:43:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:44,652 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:43:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:43:49,712 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:44:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:04,240 main INFO screen NOTBAD pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (19.7s)
Sep 12 05:44:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:07,278 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:44:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:12,335 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:44:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:12,529 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:44:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:20,218 main INFO screen WAGARI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 12 05:44:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:26,293 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.1s)
Sep 12 05:44:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:44:35,597 main INFO screen FUD pass=0 dev=0.0 ins=17.61 pro=42 1a=False 1b=False 2=True (4.8s)
Sep 12 05:45:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:05,115 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 05:45:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:15,771 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:45:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:20,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:45:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:31,181 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:45:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:34,102 main INFO screen SNIPY pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (18.4s)
Sep 12 05:45:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:39,630 main INFO screen Bricko pass=0 dev=0.06 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 12 05:45:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:45:55,644 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:46:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:46:03,278 main INFO screen CC pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 12 05:46:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:46:59,616 main INFO screen BYTE pass=0 dev=0.0 ins=21.05 pro=72 1a=False 1b=False 2=False (2.2s)
Sep 12 05:47:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:02,770 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:47:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:08,329 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:47:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:09,043 main INFO screen REVCAT pass=0 dev=0.0 ins=6.0 pro=53 1a=False 1b=False 2=True (4.2s)
Sep 12 05:47:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:23,212 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 12 05:47:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:24,353 main INFO screen FOMOCEO pass=0 dev=0.18 ins=79.1 pro=19 1a=False 1b=True 2=True (21.6s)
Sep 12 05:47:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:38,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:47:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:43,420 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:47:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:57,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:47:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:47:58,395 main INFO screen ALL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.1s)
Sep 12 05:48:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:48:02,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:48:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:48:11,713 main INFO screen NOTBAD pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.7s)
Sep 12 05:48:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:48:17,201 main INFO screen SpaceX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 05:48:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:48:38,487 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:48:38 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:49:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:49:14,831 main INFO screen Googles pass=0 dev=0.0 ins=16.7 pro=62 1a=False 1b=False 2=True (3.3s)
Sep 12 05:49:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:49:21,959 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:49:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:49:31,022 main INFO screen GOAT pass=0 dev=0.0 ins=3.39 pro=58 1a=False 1b=False 2=True (9.1s)
Sep 12 05:50:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:03,052 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:08,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:23,370 main INFO screen stonk pass=0 dev=60.99 ins=0.0 pro=18 1a=False 1b=False 2=True (20.4s)
Sep 12 05:50:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:33,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:40,885 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:41,582 main INFO screen HALH pass=0 dev=0.44 ins=0.0 pro=4 1a=False 1b=False 2=False (7.9s)
Sep 12 05:50:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:45,957 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:51,420 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:50:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:50:56,488 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:00,416 main INFO screen DrPeper pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.6s)
Sep 12 05:51:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:11,006 main INFO screen revolve pass=0 dev=96.37 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 05:51:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:14,983 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:20,053 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:27,354 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:36,304 main INFO screen BEAST pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (21.4s)
Sep 12 05:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:36,999 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.7s)
Sep 12 05:51:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:43,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:47,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:48,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:52,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:52:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:03,413 main INFO screen USGR pass=0 dev=42.92 ins=0.0 pro=2 1a=False 1b=False 2=True (19.6s)
Sep 12 05:52:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:06,639 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.3s)
Sep 12 05:52:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:46,755 main INFO screen NOTBAD pass=0 dev=0.27 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 12 05:53:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:21,937 main INFO screen Cashback pass=1 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (6.0s)
Sep 12 05:53:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:23,497 main INFO screen REVDOG pass=1 dev=2.75 ins=4.71 pro=39 1a=False 1b=False 2=False (4.0s)
Sep 12 05:53:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:26,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:53:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:32,051 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:53:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:36,132 main INFO screen MSTRbate pass=0 dev=0.0 ins=18.77 pro=29 1a=False 1b=False 2=True (3.6s)
Sep 12 05:53:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:39,489 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:53:39 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T04:15:47Z
--- update 2026-09-12T04:20:53Z
--- update 2026-09-12T04:25:56Z
--- update 2026-09-12T04:31:17Z
--- update 2026-09-12T04:36:20Z
--- update 2026-09-12T04:41:36Z
--- update 2026-09-12T04:46:50Z
--- update 2026-09-12T04:52:05Z
--- update 2026-09-12T04:57:05Z
--- update 2026-09-12T05:02:29Z
--- update 2026-09-12T05:07:36Z
--- update 2026-09-12T05:12:53Z
--- update 2026-09-12T05:18:21Z
--- update 2026-09-12T05:23:25Z
--- update 2026-09-12T05:28:27Z
--- update 2026-09-12T05:33:29Z
--- update 2026-09-12T05:38:34Z
--- update 2026-09-12T05:43:36Z
--- update 2026-09-12T05:48:37Z
--- update 2026-09-12T05:53:38Z
```

## Analyses (laatste 25 regels)
```
inactive
03:55:46 grote spelers: saldo van 418 wallets opgehaald
03:56:54 herkomst: 40 posities gekoppeld
03:56:57 klaar in 108s -> /opt/schaduwbot/reports/ledger.md
03:56:59   2000 nieuwe tokens doorgerekend
03:57:01 klaar in 4s: 13363 tokens, 2580 nieuw -> /opt/schaduwbot/reports/video_replay.md
03:57:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 03:57 UTC
03:57:01 47900 tokens geladen
03:57:04   2000 tokens, 246053 trades, 52081 posities (3s)
03:57:07   4000 tokens, 503264 trades, 107812 posities (6s)
03:57:09   6000 tokens, 764215 trades, 157570 posities (8s)
03:57:12   8000 tokens, 1014522 trades, 208740 posities (11s)
03:57:15   10000 tokens, 1313518 trades, 277037 posities (14s)
03:57:17   12000 tokens, 1549954 trades, 317998 posities (16s)
03:57:20   14000 tokens, 1819922 trades, 373769 posities (19s)
03:57:23   16000 tokens, 2091269 trades, 432443 posities (22s)
03:57:25   18000 tokens, 2350661 trades, 485256 posities (24s)
03:57:28   20000 tokens, 2609433 trades, 537071 posities (27s)
03:57:30   22000 tokens, 2847285 trades, 586776 posities (29s)
03:57:32   24000 tokens, 3117299 trades, 640240 posities (31s)
03:57:34 posities: 689428 uit 3308619 trades (33s)
03:57:43 153508 wallets gerekend
03:57:44 geluk-toets
03:58:14 persistentie
03:58:16 kopieer-simulatie
03:58:26 klaar in 85s -> /opt/schaduwbot/reports/wallets.md
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
