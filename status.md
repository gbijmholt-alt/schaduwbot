# Schaduwbot status

- tijd: 2026-09-11 23:01:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 9 hours, 14 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 844/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 12075, "tokens_in_memory": 4582, "msgs": 3034150, "trades": 526292, "creates": 4582, "decode_fail": 33117, "rpc_calls": 16515, "rpc_errors": 643, "sol_usd": 101.78897488967203, "open_positions": 112, "log_all_trades": true}
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
Sep 11 22:52:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:02,966 main INFO screen MIRCO pass=0 dev=0.0 ins=26.49 pro=14 1a=False 1b=False 2=True (20.2s)
Sep 11 22:52:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:11,143 main INFO screen iPod pass=0 dev=0.0 ins=18.22 pro=60 1a=False 1b=False 2=True (4.1s)
Sep 11 22:52:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:13,095 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.9s)
Sep 11 22:52:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:13,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:52:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:21,168 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (8.0s)
Sep 11 22:52:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:52,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:52:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:52:57,395 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:53:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:00,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:53:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:05,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:53:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:11,978 main INFO screen Flyton pass=0 dev=0.0 ins=36.03 pro=20 1a=True 1b=False 2=True (19.8s)
Sep 11 22:53:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:18,765 main INFO screen BULLBRAIN pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 11 22:53:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:48,991 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:53:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:50,294 main INFO screen $CAJUN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (4.5s)
Sep 11 22:53:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:53:54,064 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:54:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:07,328 main INFO screen Alunk pass=0 dev=0.14 ins=79.17 pro=7 1a=False 1b=True 2=True (18.4s)
Sep 11 22:54:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:12,800 main INFO screen kittylick pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 11 22:54:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:34,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:54:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:39,165 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:54:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:46,324 main INFO screen FB pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=True (2.4s)
Sep 11 22:54:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:51,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:54:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:54,075 main INFO screen Flyton pass=0 dev=0.0 ins=36.18 pro=22 1a=False 1b=False 2=True (20.1s)
Sep 11 22:54:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:54:59,708 main INFO screen WTF pass=0 dev=0.0 ins=0.0 pro=65 1a=False 1b=False 2=True (8.6s)
Sep 11 22:55:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:55:12,690 main INFO screen WTF pass=0 dev=0.0 ins=23.13 pro=40 1a=False 1b=False 2=True (1.4s)
Sep 11 22:55:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:55:25,373 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:55:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:55:32,586 main INFO screen Druski pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 22:55:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:55:33,513 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:55:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:55:39,711 main INFO screen EMPLOYEE pass=0 dev=0.0 ins=15.09 pro=9 1a=False 1b=False 2=False (6.3s)
Sep 11 22:56:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:10,330 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:56:10 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 22:56:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:18,398 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:56:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:21,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:56:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:26,161 main INFO screen bam ban pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.9s)
Sep 11 22:56:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:29,714 main INFO screen FUD pass=0 dev=0.0 ins=21.12 pro=74 1a=False 1b=False 2=True (7.7s)
Sep 11 22:56:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:35,869 main INFO screen launchpad pass=1 dev=0.75 ins=0.0 pro=37 1a=False 1b=False 2=False (2.4s)
Sep 11 22:56:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:51,676 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:56:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:56,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:56:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:56:57,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:57:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:02,119 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:57:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:04,001 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:57:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:13,772 main INFO screen Flyton pass=0 dev=0.0 ins=36.52 pro=22 1a=True 1b=False 2=True (22.2s)
Sep 11 22:57:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:14,326 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:57:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:14,819 main INFO screen CAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (10.9s)
Sep 11 22:57:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:17,256 main INFO screen MEME pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 11 22:57:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:57:21,890 main INFO screen rinsed pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 22:58:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:08,428 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:58:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:13,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:58:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:31,880 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=2 1a=False 1b=False 2=True (23.6s)
Sep 11 22:58:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:32,287 main INFO screen WCOI pass=0 dev=1.57 ins=0.0 pro=3 1a=False 1b=False 2=True (6.0s)
Sep 11 22:58:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:32,803 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:58:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:37,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:58:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:58:53,921 main INFO screen T-FART pass=0 dev=0.0 ins=0.0 pro=45 1a=False 1b=False 2=True (21.2s)
Sep 11 22:59:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:05,429 main INFO screen $CAJUN pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 22:59:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:23,356 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:59:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:23,535 main INFO screen Bricko pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.1s)
Sep 11 22:59:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:31,133 main INFO screen sender pass=0 dev=0.61 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 22:59:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:41,399 main INFO screen bam ban pass=0 dev=1.96 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 22:59:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:45,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:59:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:52,189 main INFO screen WILLFLY pass=0 dev=0.0 ins=19.02 pro=35 1a=False 1b=False 2=True (6.3s)
Sep 11 22:59:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:59:59,249 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:03,850 main INFO screen HANGRY2 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 23:00:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:04,290 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:04,424 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:07,014 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (16.1s)
Sep 11 23:00:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:15,587 main INFO screen GLORY pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=True (8.0s)
Sep 11 23:00:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:15,773 main INFO screen TCKR pass=0 dev=24.53 ins=0.0 pro=2 1a=False 1b=False 2=False (11.5s)
Sep 11 23:00:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:23,329 main INFO screen BRAINROTFLY pass=0 dev=0.0 ins=17.9 pro=72 1a=False 1b=False 2=True (24.3s)
Sep 11 23:00:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:28,151 main INFO screen 1000X pass=0 dev=0.0 ins=17.32 pro=60 1a=False 1b=False 2=True (12.6s)
Sep 11 23:00:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:30,995 main INFO screen $$$ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.1s)
Sep 11 23:00:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:40,471 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:44,408 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:45,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:00:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:49,010 main INFO screen ALLFLY pass=1 dev=0.0 ins=19.95 pro=41 1a=False 1b=False 2=False (13.0s)
Sep 11 23:00:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:00:57,993 main INFO screen TCKR pass=0 dev=6.63 ins=0.0 pro=2 1a=False 1b=False 2=True (13.7s)
Sep 11 23:01:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:02,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:01:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:04,617 main INFO screen SM pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (24.2s)
Sep 11 23:01:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:07,492 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:01:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:13,906 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:01:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:17,671 main INFO screen rooster pass=0 dev=3.46 ins=15.84 pro=3 1a=False 1b=False 2=False (9.7s)
Sep 11 23:01:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:18,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:01:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:19,959 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 23:01:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 23:01:23,315 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:23:01:23 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
--- update 2026-09-11T21:42:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
--- update 2026-09-11T21:47:46Z
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
