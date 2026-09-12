# Schaduwbot status

- tijd: 2026-09-12 04:57:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 15 hours, 10 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1107/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 33418, "tokens_in_memory": 6696, "msgs": 6476173, "trades": 1167042, "creates": 11150, "decode_fail": 58498, "rpc_calls": 39536, "rpc_errors": 1599, "sol_usd": 101.61296260050959, "open_positions": 46, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **40946**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 5003 | 828 | 3 | 826 | 53 | 1440 | 4390 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 470 | 17% | 2.1% | +44.4% | -16.7% | -6.46% | 100% |
| dip35_V1_gescreend_fail | 3879 | 27% | 3.8% | +45.7% | -25.9% | -6.65% | 100% |
| dip35_V1_alle | 4734 | 26% | 3.9% | +45.0% | -25.2% | -6.77% | 100% |
| dip35_V2_gescreend_pass | 467 | 22% | 3.0% | +43.5% | -21.2% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 3916 | 25% | 4.3% | +56.0% | -27.9% | -7.07% | 100% |
| dip35_V2_alle | 4703 | 24% | 4.5% | +53.6% | -27.6% | -7.67% | 100% |
| dip35_V3_gescreend_pass | 468 | 9% | 3.4% | +304.4% | -22.6% | +6.08% | 100% |
| dip35_V3_gescreend_fail | 3993 | 14% | 5.9% | +116.4% | -29.6% | -9.90% | 100% |
| dip35_V3_alle | 4746 | 13% | 5.9% | +122.0% | -29.2% | -9.15% | 100% |
| dip40_V1_gescreend_pass | 438 | 15% | 2.3% | +47.2% | -16.0% | -6.52% | 100% |
| dip40_V1_gescreend_fail | 3808 | 26% | 3.8% | +47.5% | -25.7% | -6.52% | 100% |
| dip40_V1_alle | 4545 | 25% | 3.8% | +47.6% | -25.0% | -6.54% | 100% |
| dip40_V2_gescreend_pass | 435 | 18% | 2.8% | +45.9% | -20.0% | -8.04% | 100% |
| dip40_V2_gescreend_fail | 3825 | 25% | 4.2% | +55.7% | -27.8% | -7.09% | 100% |
| dip40_V2_alle | 4508 | 24% | 4.4% | +54.1% | -27.3% | -7.74% | 100% |
| dip40_V3_gescreend_pass | 438 | 8% | 3.0% | +309.4% | -21.3% | +4.39% | 100% |
| dip40_V3_gescreend_fail | 3898 | 13% | 5.7% | +114.3% | -29.4% | -10.46% | 100% |
| dip40_V3_alle | 4555 | 13% | 5.7% | +120.5% | -28.9% | -9.74% | 100% |
| dip45_V1_gescreend_pass | 421 | 16% | 2.1% | +48.6% | -16.0% | -5.86% | 100% |
| dip45_V1_gescreend_fail | 3726 | 27% | 3.3% | +48.5% | -25.4% | -5.22% | 100% |
| dip45_V1_alle | 4396 | 26% | 3.4% | +48.7% | -24.8% | -5.51% | 100% |
| dip45_V2_gescreend_pass | 417 | 19% | 2.6% | +44.2% | -19.9% | -7.60% | 100% |
| dip45_V2_gescreend_fail | 3736 | 25% | 3.9% | +58.0% | -27.4% | -5.90% | 100% |
| dip45_V2_alle | 4360 | 24% | 4.0% | +56.2% | -27.0% | -6.73% | 100% |
| dip45_V3_gescreend_pass | 420 | 7% | 2.6% | +373.1% | -20.6% | +8.45% | 100% |
| dip45_V3_gescreend_fail | 3795 | 14% | 5.4% | +119.5% | -28.9% | -8.11% | 100% |
| dip45_V3_alle | 4399 | 13% | 5.4% | +129.0% | -28.4% | -7.32% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 3059 | 13% | 3.5% | -10.00% | 100% |
| zonder_xlink | 915 | 19% | 0.0% | +22.62% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 04:36:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:21,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:36:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:21,973 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:36:21 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:36:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:26,375 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:36:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:31,916 main INFO screen USGC pass=0 dev=0.18 ins=79.1 pro=17 1a=False 1b=True 2=True (18.4s)
Sep 12 04:36:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:36,250 main INFO screen mortus pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 04:36:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:41,538 main INFO screen PeHomie pass=0 dev=1.33 ins=0.0 pro=2 1a=False 1b=False 2=False (20.3s)
Sep 12 04:37:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:37:42,282 main INFO screen BUTTHOLE pass=1 dev=0.0 ins=12.19 pro=50 1a=False 1b=False 2=False (4.0s)
Sep 12 04:37:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:37:55,791 main INFO screen CHONKY pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.7s)
Sep 12 04:38:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:38:05,535 aiohttp.access INFO 195.182.16.23 [12/Sep/2026:04:38:05 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 04:38:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:38:20,601 main INFO screen vrl pass=0 dev=1.72 ins=0.01 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 12 04:38:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:38:39,797 main INFO screen skipoo pass=0 dev=2.04 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 12 04:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:38:52,402 main INFO screen Gatto pass=0 dev=15.17 ins=1.3 pro=22 1a=False 1b=True 2=False (2.5s)
Sep 12 04:39:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:39:35,232 main INFO screen $AURA pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 12 04:39:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:39:52,998 main INFO screen . pass=0 dev=0.24 ins=0.0 pro=1 1a=False 1b=False 2=False (4.4s)
Sep 12 04:40:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:40:02,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:40:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:40:07,467 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:40:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:40:11,205 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:41:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:03,745 main INFO screen Starbucks pass=0 dev=79.3 ins=0.0 pro=1 1a=False 1b=False 2=True (52.6s)
Sep 12 04:41:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:03,935 main INFO screen NTDA pass=0 dev=98.49 ins=0.0 pro=1 1a=False 1b=False 2=True (61.6s)
Sep 12 04:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:04,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:41:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:04,227 main INFO screen NOOT pass=0 dev=0.0 ins=15.89 pro=22 1a=False 1b=False 2=True (6.7s)
Sep 12 04:41:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:09,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:41:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:24,151 main INFO screen RWA BABIES pass=0 dev=2.43 ins=48.48 pro=17 1a=False 1b=False 2=True (20.4s)
Sep 12 04:41:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:26,062 main INFO screen mortus pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (2.1s)
Sep 12 04:41:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:41:37,112 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:41:37 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:42:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:23,627 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:42:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:26,597 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:42:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:28,723 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:42:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:31,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:42:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:43,284 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 04:42:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:42:46,304 main INFO screen LONG pass=0 dev=98.29 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 04:43:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:43:01,264 main INFO screen skipoo pass=0 dev=2.1 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 04:43:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:43:25,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:43:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:43:32,581 main INFO screen bam ban pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 04:44:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:44:16,115 main INFO screen skipoo pass=0 dev=2.28 ins=0.0 pro=2 1a=False 1b=False 2=True (2.0s)
Sep 12 04:44:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:44:52,985 main INFO screen RDIH pass=0 dev=4.41 ins=16.0 pro=34 1a=False 1b=False 2=True (3.3s)
Sep 12 04:45:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:45:32,619 main INFO screen USGC pass=0 dev=0.57 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 12 04:46:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:46:15,815 main INFO screen skipoo pass=0 dev=2.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 12 04:46:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:46:43,861 main INFO screen RESELLOR pass=1 dev=0.0 ins=16.39 pro=42 1a=False 1b=False 2=False (3.9s)
Sep 12 04:46:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:46:51,405 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:46:51 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:47:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:47:33,625 main INFO screen Buttcoin pass=0 dev=0.0 ins=9.06 pro=46 1a=False 1b=False 2=True (2.7s)
Sep 12 04:48:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:48:20,750 main INFO screen DUOLINGO pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 12 04:48:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:48:39,193 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:48:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:48:44,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:48:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:48:58,658 main INFO screen SpaceX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 04:49:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:49:07,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:49:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:49:12,493 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:49:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:49:27,016 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.7s)
Sep 12 04:50:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:50:03,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:50:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:50:08,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:50:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:50:22,353 main INFO screen EYES pass=0 dev=3.46 ins=46.56 pro=13 1a=False 1b=False 2=True (19.2s)
Sep 12 04:50:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:50:25,718 main INFO screen banana pass=0 dev=0.0 ins=9.86 pro=65 1a=False 1b=False 2=True (3.2s)
Sep 12 04:51:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:51:26,952 main INFO screen skipoo pass=0 dev=2.67 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 12 04:51:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:51:42,518 main INFO screen BUTTCOIN pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 04:51:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:51:56,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:52:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:52:01,964 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:52:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:52:06,030 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:52:06 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:52:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:52:17,888 main INFO screen Archie pass=0 dev=42.49 ins=6.34 pro=13 1a=False 1b=False 2=False (21.1s)
Sep 12 04:53:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:53:22,407 main INFO screen BUTTCOIN pass=0 dev=0.56 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 12 04:53:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:53:43,443 main INFO screen . pass=0 dev=0.49 ins=0.0 pro=1 1a=False 1b=False 2=True (2.1s)
Sep 12 04:53:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:53:59,931 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:54:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:54:05,000 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:54:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:54:20,264 main INFO screen BUTTCOIN pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (20.5s)
Sep 12 04:54:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:54:22,819 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:54:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:54:27,887 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:54:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:54:43,789 main INFO screen chud pass=0 dev=0.0 ins=19.42 pro=60 1a=False 1b=False 2=True (21.0s)
Sep 12 04:55:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:55:22,666 main INFO screen Gropper pass=0 dev=0.0 ins=12.63 pro=67 1a=False 1b=False 2=True (3.8s)
Sep 12 04:55:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:55:42,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:55:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:55:47,489 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:56:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:00,747 main INFO screen GROAK pass=0 dev=0.18 ins=77.54 pro=17 1a=False 1b=True 2=True (18.4s)
Sep 12 04:56:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:28,979 main INFO screen $CAT pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 12 04:56:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:35,722 main INFO screen BUTTCOIN pass=0 dev=0.73 ins=0.0 pro=2 1a=False 1b=False 2=False (1.8s)
Sep 12 04:56:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:42,091 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:56:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:47,160 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:56:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:50,597 main INFO screen Ass pass=0 dev=0.34 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 12 04:56:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:57,051 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 12 04:56:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:56:57,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:57:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:57:01,608 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 12 04:57:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:57:02,749 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:57:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:57:06,386 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:57:06 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T03:28:37Z
--- update 2026-09-12T03:33:53Z
--- update 2026-09-12T03:39:36Z
--- update 2026-09-12T03:44:43Z
--- update 2026-09-12T03:49:57Z
--- update 2026-09-12T03:55:08Z
Running as unit: schaduwbot-wallets.service; invocation ID: 65c97d0888f44ae1a8047aba8afd8a37
analyses gestart (8746aefc73b4)
--- update 2026-09-12T04:00:11Z
--- update 2026-09-12T04:05:13Z
--- update 2026-09-12T04:10:36Z
--- update 2026-09-12T04:15:47Z
--- update 2026-09-12T04:20:53Z
--- update 2026-09-12T04:25:56Z
--- update 2026-09-12T04:31:17Z
--- update 2026-09-12T04:36:20Z
--- update 2026-09-12T04:41:36Z
--- update 2026-09-12T04:46:50Z
--- update 2026-09-12T04:52:05Z
--- update 2026-09-12T04:57:05Z
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
