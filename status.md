# Schaduwbot status

- tijd: 2026-09-11 19:50:12 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 6 hours, 3 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.8G/38G | geheugen: 556/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 604, "tokens_in_memory": 200, "msgs": 150571, "trades": 18094, "creates": 200, "decode_fail": 1604, "rpc_calls": 691, "rpc_errors": 36, "sol_usd": 101.69797579687446, "open_positions": 7, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 19:40 UTC

Gelogde schaduwtrades: **30770**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 22609 | 3407 | 37 | 3406 | 253 | 6238 | 18415 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 342 | 17% | 2.0% | +43.7% | -16.7% | -6.62% | 99% |
| dip35_V1_gescreend_fail | 3077 | 27% | 3.8% | +46.1% | -26.2% | -6.71% | 100% |
| dip35_V1_alle | 3564 | 26% | 3.8% | +45.2% | -25.5% | -6.88% | 100% |
| dip35_V2_gescreend_pass | 339 | 20% | 2.9% | +44.5% | -21.4% | -8.38% | 100% |
| dip35_V2_gescreend_fail | 3082 | 25% | 4.4% | +57.2% | -28.4% | -7.20% | 100% |
| dip35_V2_alle | 3534 | 24% | 4.4% | +55.3% | -28.0% | -7.70% | 100% |
| dip35_V3_gescreend_pass | 341 | 8% | 3.2% | +287.1% | -22.8% | +2.64% | 100% |
| dip35_V3_gescreend_fail | 3132 | 13% | 6.1% | +120.7% | -29.9% | -9.72% | 100% |
| dip35_V3_alle | 3576 | 13% | 6.0% | +126.3% | -29.5% | -8.99% | 100% |
| dip40_V1_gescreend_pass | 315 | 15% | 1.9% | +47.2% | -15.6% | -6.41% | 99% |
| dip40_V1_gescreend_fail | 2989 | 26% | 3.7% | +48.1% | -26.1% | -6.48% | 100% |
| dip40_V1_alle | 3420 | 26% | 3.7% | +48.0% | -25.3% | -6.50% | 100% |
| dip40_V2_gescreend_pass | 313 | 15% | 2.6% | +48.3% | -19.9% | -9.46% | 100% |
| dip40_V2_gescreend_fail | 2983 | 25% | 4.2% | +56.6% | -28.3% | -7.09% | 100% |
| dip40_V2_alle | 3385 | 24% | 4.2% | +55.7% | -27.7% | -7.70% | 100% |
| dip40_V3_gescreend_pass | 316 | 6% | 2.5% | +326.5% | -21.1% | +0.93% | 100% |
| dip40_V3_gescreend_fail | 3033 | 13% | 5.8% | +115.3% | -29.7% | -10.85% | 100% |
| dip40_V3_alle | 3429 | 12% | 5.6% | +122.7% | -29.1% | -10.23% | 100% |
| dip45_V1_gescreend_pass | 302 | 15% | 1.7% | +52.1% | -15.3% | -5.05% | 98% |
| dip45_V1_gescreend_fail | 2907 | 27% | 3.3% | +48.7% | -25.8% | -5.37% | 100% |
| dip45_V1_alle | 3298 | 26% | 3.3% | +49.1% | -25.0% | -5.44% | 100% |
| dip45_V2_gescreend_pass | 299 | 18% | 2.3% | +47.6% | -19.6% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 2891 | 25% | 3.9% | +59.6% | -27.9% | -5.97% | 100% |
| dip45_V2_alle | 3264 | 24% | 3.9% | +58.5% | -27.3% | -6.46% | 100% |
| dip45_V3_gescreend_pass | 302 | 7% | 2.3% | +379.4% | -20.3% | +6.15% | 100% |
| dip45_V3_gescreend_fail | 2933 | 14% | 5.5% | +123.3% | -29.3% | -8.06% | 100% |
| dip45_V3_alle | 3300 | 13% | 5.3% | +133.2% | -28.6% | -7.21% | 100% |

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
| met_xlink | 2293 | 12% | 3.0% | -9.86% | 100% |
| zonder_xlink | 576 | 18% | 0.0% | +20.52% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 19:39:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:39:12,698 main INFO screen ROBOELON pass=0 dev=0.0 ins=20.09 pro=24 1a=False 1b=False 2=True (4.6s)
Sep 11 19:39:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:39:49,835 main INFO screen $REGRET pass=0 dev=5.8 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 19:40:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:40:07,507 main INFO screen Divergent pass=0 dev=1.0 ins=17.96 pro=51 1a=False 1b=False 2=True (6.2s)
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 7min 1.812s CPU time over 1h 1min 50.785s wall clock time, 225.4M memory peak.
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 19:40:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:40:08,959 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 19:40:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:40:09,005 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:40:09 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 11 19:41:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:01,480 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:04,851 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:06,557 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:07,407 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:11,788 main INFO screen fancat pass=0 dev=0.0 ins=20.47 pro=15 1a=False 1b=False 2=True (7.0s)
Sep 11 19:41:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:12,442 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:17,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:20,504 main INFO screen Insider pass=0 dev=0.0 ins=48.15 pro=50 1a=False 1b=False 2=True (19.1s)
Sep 11 19:41:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:20,563 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:25,850 main INFO screen beer pass=0 dev=0.31 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 11 19:41:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:33,008 main INFO screen batonless pass=0 dev=5.18 ins=45.4 pro=28 1a=False 1b=False 2=True (25.7s)
Sep 11 19:41:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:36,216 main INFO screen SNOOT pass=0 dev=0.0 ins=16.63 pro=45 1a=False 1b=False 2=True (15.7s)
Sep 11 19:41:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:55,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:41:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:41:56,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:00,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:01,444 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:03,065 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 11 19:42:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:05,392 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:18,529 main INFO screen AEROTY pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (5.1s)
Sep 11 19:42:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:18,585 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (22.6s)
Sep 11 19:42:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:20,965 main INFO screen Koinvase pass=0 dev=0.0 ins=14.34 pro=77 1a=False 1b=False 2=True (20.7s)
Sep 11 19:42:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:24,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:24,201 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:29,036 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:29,271 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:31,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:36,922 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:45,680 main INFO screen NOIZ pass=0 dev=0.0 ins=25.9 pro=23 1a=False 1b=False 2=True (21.7s)
Sep 11 19:42:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:45,856 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (21.8s)
Sep 11 19:42:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:53,027 main INFO screen ZION pass=0 dev=11.31 ins=0.0 pro=23 1a=False 1b=False 2=False (3.3s)
Sep 11 19:42:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:53,134 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.4s)
Sep 11 19:42:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:54,882 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:42:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:42:59,912 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:43:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:43:14,785 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 11 19:43:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:43:22,132 main INFO screen sol pass=0 dev=0.14 ins=0.07 pro=5 1a=False 1b=False 2=False (3.6s)
Sep 11 19:43:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:43:40,447 main INFO screen CHEDDAR pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 19:44:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:44:16,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:44:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:44:21,304 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:44:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:44:35,225 main INFO screen batonless pass=0 dev=0.0 ins=53.56 pro=30 1a=True 1b=False 2=True (19.1s)
Sep 11 19:44:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:44:47,307 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:44:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:44:55,151 main INFO screen ZenoCoin pass=0 dev=0.0 ins=20.82 pro=70 1a=False 1b=False 2=True (7.9s)
Sep 11 19:45:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:09,473 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:45:09 +0000] "GET /health HTTP/1.1" 200 438 "-" "Python-urllib/3.14"
Sep 11 19:45:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:18,158 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:45:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:23,757 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:45:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:24,459 main INFO screen BROWNCEY pass=0 dev=0.0 ins=8.84 pro=35 1a=False 1b=True 2=False (3.9s)
Sep 11 19:45:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:38,429 main INFO screen BEAST pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (20.3s)
Sep 11 19:45:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:42,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:45:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:45:47,671 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:46:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:46:04,919 main INFO screen PUPPER pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (5.8s)
Sep 11 19:46:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:46:05,584 main INFO screen Squad pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (23.0s)
Sep 11 19:46:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:46:09,441 main INFO screen Coma Tozze pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (4.6s)
Sep 11 19:46:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:46:57,655 main INFO screen tgreen pass=0 dev=5.9 ins=0.0 pro=53 1a=False 1b=False 2=False (5.0s)
Sep 11 19:46:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:46:58,106 main INFO screen SAVPIR pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (4.9s)
Sep 11 19:47:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:47:17,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:47:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:47:24,824 main INFO screen 100k/Rug pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 11 19:48:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:48:42,657 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:48:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:48:47,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:01,742 main INFO screen CHEDDAR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (19.2s)
Sep 11 19:49:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:04,867 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:09,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:12,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:13,458 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:17,688 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:18,527 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:49:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:24,164 main INFO screen Paz pass=0 dev=0.0 ins=21.04 pro=67 1a=False 1b=False 2=True (19.4s)
Sep 11 19:49:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:33,685 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.3s)
Sep 11 19:49:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:49:35,369 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.8s)
Sep 11 19:50:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:50:02,347 main INFO screen $CAJUN pass=0 dev=0.32 ins=0.0 pro=3 1a=False 1b=False 2=False (5.9s)
Sep 11 19:50:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:50:02,949 main INFO screen TRUMPCOIN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 19:50:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 19:50:12,623 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:50:12 +0000] "GET /health HTTP/1.1" 200 440 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 1322d8308bda44ab89e4732e0436b52e
analyses gestart (ed3e144883fd)
--- update 2026-09-11T18:43:36Z
--- update 2026-09-11T18:48:56Z
--- update 2026-09-11T18:54:05Z
--- update 2026-09-11T18:59:19Z
--- update 2026-09-11T19:04:36Z
--- update 2026-09-11T19:09:39Z
--- update 2026-09-11T19:14:45Z
--- update 2026-09-11T19:19:51Z
--- update 2026-09-11T19:24:55Z
--- update 2026-09-11T19:30:02Z
--- update 2026-09-11T19:35:03Z
--- update 2026-09-11T19:40:04Z
nieuwe code: 1cefa36
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 670a5941fedf41389993862a94844cc9
analyses gestart (8746aefc73b4)
--- update 2026-09-11T19:45:08Z
--- update 2026-09-11T19:50:11Z
```

## Analyses (laatste 25 regels)
```
inactive
18:40:27 kopieer-simulatie
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
19:40:08 12765 tokens sinds start volledige logging, waarvan 3627 met een gat door herstart
19:40:11   ingelezen tot rowid 2225120 (145387 rijen, 145387 bruikbaar)
19:40:11 ingelezen: 145387 nieuwe trades, 145387 bruikbaar (3s)
19:40:22 177 aankopen van gevolgde wallets geëvalueerd
19:40:34 grote spelers: saldo van 2000 wallets opgehaald
19:41:46 herkomst: 40 posities gekoppeld
19:41:47 klaar in 99s -> /opt/schaduwbot/reports/ledger.md
19:41:49 klaar in 1s: 6168 tokens, 1142 nieuw -> /opt/schaduwbot/reports/video_replay.md
19:41:49 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 19:41 UTC
19:41:49 37636 tokens geladen
19:41:51   2000 tokens, 281880 trades, 68228 posities (2s)
19:41:53   4000 tokens, 562091 trades, 134424 posities (4s)
19:41:56   6000 tokens, 870184 trades, 206311 posities (7s)
19:41:58   8000 tokens, 1149114 trades, 266897 posities (9s)
19:42:01   10000 tokens, 1443511 trades, 336633 posities (12s)
19:42:03   12000 tokens, 1716836 trades, 400450 posities (14s)
19:42:06   14000 tokens, 1988268 trades, 462617 posities (17s)
19:42:08 posities: 523618 uit 2226699 trades (19s)
19:42:14 123108 wallets gerekend
19:42:14 geluk-toets
19:42:33 persistentie
19:42:34 kopieer-simulatie
19:42:39 klaar in 51s -> /opt/schaduwbot/reports/wallets.md
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
