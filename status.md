# Schaduwbot status

- tijd: 2026-09-12 07:46:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 17 hours, 59 minutes
- bot-service: active
- code-versie: 5e1921e
- schijf: 3.5G/38G | geheugen: 560/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 318, "tokens_in_memory": 82, "msgs": 15960, "trades": 4975, "creates": 82, "decode_fail": 229, "rpc_calls": 164, "rpc_errors": 8, "sol_usd": 101.63629893206887, "open_positions": 4, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

Gelogde schaduwtrades: **43222**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 7455 | 1223 | 6 | 1223 | 93 | 2198 | 6666 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 503 | 16% | 2.0% | +44.1% | -16.6% | -6.93% | 100% |
| dip35_V1_gescreend_fail | 4069 | 27% | 3.8% | +45.6% | -25.9% | -6.59% | 100% |
| dip35_V1_alle | 4993 | 26% | 3.9% | +44.8% | -25.2% | -6.84% | 100% |
| dip35_V2_gescreend_pass | 500 | 21% | 2.8% | +43.1% | -20.9% | -7.42% | 100% |
| dip35_V2_gescreend_fail | 4105 | 25% | 4.3% | +56.3% | -27.9% | -6.88% | 100% |
| dip35_V2_alle | 4959 | 24% | 4.5% | +53.8% | -27.6% | -7.63% | 100% |
| dip35_V3_gescreend_pass | 502 | 8% | 3.2% | +297.3% | -22.3% | +4.45% | 100% |
| dip35_V3_gescreend_fail | 4189 | 14% | 5.9% | +115.1% | -29.6% | -10.10% | 100% |
| dip35_V3_alle | 5006 | 13% | 5.9% | +119.7% | -29.2% | -9.54% | 100% |
| dip40_V1_gescreend_pass | 473 | 14% | 2.1% | +46.7% | -15.9% | -7.07% | 100% |
| dip40_V1_gescreend_fail | 3999 | 26% | 3.7% | +47.2% | -25.7% | -6.52% | 100% |
| dip40_V1_alle | 4798 | 25% | 3.8% | +47.3% | -25.0% | -6.69% | 100% |
| dip40_V2_gescreend_pass | 471 | 17% | 2.5% | +46.2% | -19.8% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 4014 | 25% | 4.2% | +55.9% | -27.9% | -6.96% | 100% |
| dip40_V2_alle | 4759 | 24% | 4.3% | +54.3% | -27.4% | -7.77% | 100% |
| dip40_V3_gescreend_pass | 474 | 8% | 2.7% | +294.2% | -21.1% | +2.87% | 100% |
| dip40_V3_gescreend_fail | 4091 | 13% | 5.6% | +112.2% | -29.4% | -10.69% | 100% |
| dip40_V3_alle | 4808 | 13% | 5.6% | +117.8% | -28.9% | -10.15% | 100% |
| dip45_V1_gescreend_pass | 455 | 15% | 2.0% | +48.7% | -15.8% | -6.28% | 100% |
| dip45_V1_gescreend_fail | 3918 | 28% | 3.3% | +48.4% | -25.4% | -5.17% | 100% |
| dip45_V1_alle | 4645 | 26% | 3.4% | +48.7% | -24.7% | -5.50% | 100% |
| dip45_V2_gescreend_pass | 452 | 19% | 2.4% | +43.3% | -19.8% | -7.90% | 100% |
| dip45_V2_gescreend_fail | 3927 | 25% | 3.8% | +58.6% | -27.4% | -5.69% | 100% |
| dip45_V2_alle | 4607 | 24% | 3.9% | +57.4% | -27.0% | -6.41% | 100% |
| dip45_V3_gescreend_pass | 455 | 7% | 2.4% | +352.6% | -20.5% | +6.56% | 100% |
| dip45_V3_gescreend_fail | 3990 | 14% | 5.4% | +117.2% | -28.9% | -8.58% | 100% |
| dip45_V3_alle | 4647 | 13% | 5.3% | +125.9% | -28.4% | -7.90% | 100% |

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
| met_xlink | 3307 | 13% | 3.2% | -10.31% | 100% |
| zonder_xlink | 978 | 18% | 0.0% | +20.19% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 07:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:59,942 main INFO screen MBST pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (12.9s)
Sep 12 07:27:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:27:30,981 main INFO screen OXYGEN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 12 07:28:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:28:58,604 main INFO screen JeJe pass=0 dev=0.24 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 12 07:29:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:29:24,036 main INFO screen Graduate pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 07:30:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:01,971 main INFO screen INU pass=0 dev=0.0 ins=20.21 pro=59 1a=False 1b=False 2=True (3.2s)
Sep 12 07:30:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:33,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,750 main INFO screen PLINE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 12 07:30:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:43,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:48,490 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:52,531 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:30:52 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:30:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:57,348 main INFO screen ANONKNIGHT pass=0 dev=0.18 ins=79.13 pro=9 1a=True 1b=True 2=True (24.5s)
Sep 12 07:31:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:10,576 main INFO screen ANZATOK pass=0 dev=0.0 ins=3.2 pro=49 1a=False 1b=False 2=True (27.2s)
Sep 12 07:31:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:52,392 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 12 07:31:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:54,550 main INFO screen DeDe pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 12 07:31:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:58,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:00,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:04,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:07,257 main INFO screen Polarbear pass=0 dev=0.0 ins=18.31 pro=32 1a=False 1b=False 2=True (7.3s)
Sep 12 07:32:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:22,907 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (24.0s)
Sep 12 07:33:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:19,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:24,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:29,763 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:33,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:34,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:38,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:39,009 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.7s)
Sep 12 07:33:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:42,183 main INFO screen DeFi pass=0 dev=0.03 ins=25.33 pro=46 1a=False 1b=False 2=True (3.2s)
Sep 12 07:33:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:48,784 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.1s)
Sep 12 07:33:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:53,096 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 07:34:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:34:11,951 main INFO screen NOTBAD pass=0 dev=0.62 ins=0.0 pro=7 1a=False 1b=False 2=False (3.5s)
Sep 12 07:34:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:34:37,136 main INFO screen $speed pass=0 dev=0.25 ins=0.0 pro=5 1a=False 1b=False 2=False (2.8s)
Sep 12 07:35:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:02,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:08,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:09,993 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (3.7s)
Sep 12 07:35:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:22,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:22,806 main INFO screen Starbucks pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 12 07:35:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:27,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:35,614 main INFO screen . pass=0 dev=0.49 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 12 07:35:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:42,209 main INFO screen RUFUS pass=0 dev=0.0 ins=14.03 pro=31 1a=False 1b=False 2=True (19.7s)
Sep 12 07:35:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:54,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:59,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:05,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:10,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:13,717 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:36:13 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:36:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:14,421 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 07:36:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:23,677 main INFO screen FLYPAIN pass=0 dev=0.04 ins=79.27 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 12 07:36:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:49,194 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:54,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:37:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:07,826 main INFO screen RUFUS pass=0 dev=0.0 ins=21.88 pro=30 1a=False 1b=True 2=True (18.7s)
Sep 12 07:37:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:10,248 main INFO screen $speed pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 12 07:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:05,811 main INFO screen HORACE pass=0 dev=0.0 ins=18.12 pro=24 1a=False 1b=False 2=True (2.1s)
Sep 12 07:39:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:10,050 main INFO screen Fox pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 12 07:40:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:40:02,878 main INFO screen GYROS pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 12 07:41:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:14,093 main INFO screen WOTF pass=0 dev=98.49 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 12 07:41:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:15,023 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 1h 22min 30.038s CPU time over 12h 1min 10.049s wall clock time, 1.1G memory peak.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,143 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,167 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:41:19 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 12 07:42:54 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:42:54,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:42:59 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:42:59,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:43:14 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:43:14,171 main INFO screen UP pass=0 dev=0.0 ins=35.87 pro=40 1a=True 1b=False 2=True (20.1s)
Sep 12 07:44:23 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:44:23,814 main INFO screen DOOYET pass=0 dev=1.72 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 12 07:44:51 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:44:51,213 main INFO screen moneyCAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.8s)
Sep 12 07:45:15 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:15,182 main INFO screen XeXe pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (5.4s)
Sep 12 07:45:15 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:15,379 main INFO screen chickjock pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.6s)
Sep 12 07:45:56 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:56,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:00 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:00,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:01 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:01,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:05 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:05,472 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:06 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:06,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:11 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:11,827 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:16 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:16,687 main INFO screen MEGACAT pass=0 dev=0.0 ins=15.14 pro=65 1a=False 1b=False 2=True (20.2s)
Sep 12 07:46:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:19,941 main INFO screen HolyGuac pass=0 dev=0.89 ins=0.0 pro=5 1a=False 1b=False 2=False (19.6s)
Sep 12 07:46:25 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:25,973 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.3s)
Sep 12 07:46:37 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:37,155 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:46:37 +0000] "GET /health HTTP/1.1" 200 487 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T06:44:35Z
--- update 2026-09-12T06:49:36Z
--- update 2026-09-12T06:54:39Z
--- update 2026-09-12T06:59:44Z
--- update 2026-09-12T07:04:47Z
--- update 2026-09-12T07:09:50Z
--- update 2026-09-12T07:14:57Z
--- update 2026-09-12T07:20:13Z
--- update 2026-09-12T07:25:36Z
--- update 2026-09-12T07:30:51Z
--- update 2026-09-12T07:36:12Z
--- update 2026-09-12T07:41:14Z
nieuwe code: 5e1921e
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 4ef46f4f0356436685dca4ab3e2f1d40
analyses gestart (e6fa7044d08b)
--- update 2026-09-12T07:46:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 2a89401955f64382a4bf605244d564d2
analyses gestart (571ea883d7b8)
```

## Analyses (laatste 25 regels)
```
active
07:43:36 klaar in 4s: 16478 tokens, 1513 nieuw -> /opt/schaduwbot/reports/video_replay.md
07:43:36 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 07:43 UTC
07:43:36 50998 tokens geladen
07:43:39   2000 tokens, 246714 trades, 51459 posities (3s)
07:43:42   4000 tokens, 499956 trades, 104136 posities (6s)
07:43:44   6000 tokens, 749227 trades, 152151 posities (8s)
07:43:47   8000 tokens, 999139 trades, 202085 posities (11s)
07:43:50   10000 tokens, 1271068 trades, 256059 posities (14s)
07:43:53   12000 tokens, 1533406 trades, 310311 posities (17s)
07:43:55   14000 tokens, 1781576 trades, 353376 posities (19s)
07:43:58   16000 tokens, 2036937 trades, 405460 posities (22s)
07:44:01   18000 tokens, 2309820 trades, 463215 posities (25s)
07:44:04   20000 tokens, 2552066 trades, 508909 posities (28s)
07:44:07   22000 tokens, 2809574 trades, 558007 posities (31s)
07:44:09   24000 tokens, 3039168 trades, 603658 posities (33s)
07:44:12   26000 tokens, 3303104 trades, 653816 posities (36s)
07:44:14   28000 tokens, 3567162 trades, 716938 posities (38s)
07:44:15 posities: 732216 uit 3631910 trades (39s)
07:44:26 159638 wallets gerekend
07:44:26 geluk-toets
07:45:01 persistentie
07:45:04 kopieer-simulatie
07:45:16 klaar in 101s -> /opt/schaduwbot/reports/wallets.md
07:46:36 26203 tokens sinds start volledige logging, waarvan 6671 met een gat door herstart
07:46:37   ingelezen tot rowid 3635359 (4975 rijen, 4975 bruikbaar)
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
