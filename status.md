# Schaduwbot status

- tijd: 2026-09-11 22:45:59 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 8 hours, 59 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 828/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 11151, "tokens_in_memory": 4180, "msgs": 2795178, "trades": 487319, "creates": 4180, "decode_fail": 32233, "rpc_calls": 15161, "rpc_errors": 586, "sol_usd": 101.93009465598821, "open_positions": 99, "log_all_trades": true}
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
Sep 11 22:30:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:30:45,530 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.8s)
Sep 11 22:31:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:31:37,054 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:31:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:31:42,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:31:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:31:53,704 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:31:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:31:55,394 main INFO screen Bag pass=0 dev=6.63 ins=20.35 pro=42 1a=False 1b=False 2=True (18.4s)
Sep 11 22:31:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:31:58,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:32:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:05,339 main INFO screen ALPHA pass=0 dev=0.0 ins=11.78 pro=59 1a=False 1b=False 2=True (2.5s)
Sep 11 22:32:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:14,497 main INFO screen GOGLZ pass=0 dev=0.47 ins=52.94 pro=25 1a=False 1b=False 2=True (20.9s)
Sep 11 22:32:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:25,880 main INFO screen $CLOCK pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 22:32:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:27,822 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:32:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:32,892 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:32:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:46,721 main INFO screen GIGAFLY pass=0 dev=0.0 ins=32.34 pro=28 1a=False 1b=False 2=True (5.1s)
Sep 11 22:32:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:48,267 main INFO screen Rocketman pass=1 dev=0.0 ins=9.83 pro=21 1a=False 1b=False 2=False (4.2s)
Sep 11 22:32:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:32:49,215 main INFO screen Neegyahu pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (21.4s)
Sep 11 22:33:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:33:41,360 main INFO screen SHIBAINU pass=0 dev=0.0 ins=20.55 pro=38 1a=False 1b=False 2=False (4.1s)
Sep 11 22:33:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:33:45,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:33:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:33:50,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:33:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:33:51,899 main INFO screen Jupsy pass=1 dev=0.0 ins=14.06 pro=57 1a=False 1b=False 2=False (3.7s)
Sep 11 22:34:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:07,046 main INFO screen BRAINZ pass=0 dev=0.35 ins=41.17 pro=10 1a=False 1b=False 2=True (21.6s)
Sep 11 22:34:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:10,073 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:15,156 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:28,850 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:29,691 main INFO screen OTC pass=0 dev=0.0 ins=18.0 pro=30 1a=False 1b=False 2=True (19.7s)
Sep 11 22:34:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:33,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:34,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:36,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:39,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:41,384 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:48,002 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.5s)
Sep 11 22:34:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:48,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:34:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:34:54,689 main INFO screen KOJI pass=0 dev=0.0 ins=37.02 pro=25 1a=False 1b=True 2=True (20.4s)
Sep 11 22:35:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:00,821 main INFO screen VOID pass=0 dev=39.08 ins=0.0 pro=5 1a=False 1b=False 2=True (12.8s)
Sep 11 22:35:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:01,771 main INFO screen KOJI pass=0 dev=0.0 ins=7.36 pro=76 1a=False 1b=False 2=True (25.5s)
Sep 11 22:35:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:02,543 main INFO screen Y pass=0 dev=31.36 ins=1.02 pro=20 1a=False 1b=False 2=False (7.9s)
Sep 11 22:35:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:05,351 main INFO screen WCOI pass=0 dev=2.25 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 11 22:35:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:47,439 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:35:47 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 22:35:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:55,900 main INFO screen Karen pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.1s)
Sep 11 22:35:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:35:56,870 main INFO screen kittylick pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 11 22:36:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:02,688 main INFO screen ALLCOIN pass=0 dev=0.0 ins=11.48 pro=68 1a=False 1b=False 2=True (4.4s)
Sep 11 22:36:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:11,023 main INFO screen CRISPE pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (5.3s)
Sep 11 22:36:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:47,554 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 22:36:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:54,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:36:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:56,747 main INFO screen soddyCUNT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.7s)
Sep 11 22:36:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:36:59,571 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:37:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:14,220 main INFO screen ROBIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 11 22:37:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:17,761 main INFO screen 911 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 22:37:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:27,874 main INFO screen PINHEAD pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 22:37:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:38,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:37:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:43,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:37:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:37:59,511 main INFO screen POLYFLY pass=0 dev=0.0 ins=12.66 pro=62 1a=False 1b=False 2=True (21.1s)
Sep 11 22:38:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:38:25,563 main INFO screen Sparky pass=0 dev=0.0 ins=22.71 pro=28 1a=False 1b=True 2=True (1.6s)
Sep 11 22:39:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:39:06,694 main INFO screen $CAJUN pass=0 dev=0.63 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 22:40:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:40:59,514 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:40:59 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 22:41:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:06,735 main INFO screen NIВZ pass=0 dev=0.47 ins=53.18 pro=26 1a=False 1b=False 2=True (8.5s)
Sep 11 22:41:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:08,586 main INFO screen BEAST pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (10.0s)
Sep 11 22:41:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:09,022 main INFO screen ADAM pass=0 dev=1.74 ins=21.22 pro=64 1a=False 1b=False 2=True (10.2s)
Sep 11 22:41:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:25,842 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:41:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:30,911 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:41:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:32,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:41:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:39,759 main INFO screen $LOAF pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 11 22:41:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:45,856 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:41:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:46,786 main INFO screen POLYFLY pass=1 dev=0.0 ins=16.04 pro=24 1a=False 1b=False 2=False (21.0s)
Sep 11 22:41:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:41:50,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:42:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:42:06,833 main INFO screen Pump pass=1 dev=0.0 ins=13.52 pro=31 1a=False 1b=False 2=False (3.0s)
Sep 11 22:42:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:42:06,881 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.6s)
Sep 11 22:42:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:42:36,532 main INFO screen VENOM pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 22:42:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:42:46,430 main INFO screen ShortBuss pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 22:43:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:43:02,763 main INFO screen WONTSTOP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 22:43:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:43:47,824 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:43:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:43:52,894 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:44:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:07,480 main INFO screen STRATEGY pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 11 22:44:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:15,954 main INFO screen FORKEPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 22:44:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:33,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:44:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:38,923 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:44:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:39,247 main INFO screen THWAY pass=0 dev=0.0 ins=16.05 pro=20 1a=False 1b=False 2=True (1.4s)
Sep 11 22:44:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:54,740 main INFO screen Gram pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=True (21.0s)
Sep 11 22:44:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:44:59,359 main INFO screen GOSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 22:45:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:45:26,904 main INFO screen COMPANY pass=1 dev=0.0 ins=11.05 pro=56 1a=False 1b=False 2=False (3.0s)
Sep 11 22:45:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:45:46,738 main INFO screen WCOI pass=0 dev=1.57 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 22:45:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:45:59,546 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:45:59 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
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
