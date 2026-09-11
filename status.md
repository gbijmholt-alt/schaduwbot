# Schaduwbot status

- tijd: 2026-09-11 22:56:10 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 9 hours, 9 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 823/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 11762, "tokens_in_memory": 4428, "msgs": 2938051, "trades": 511896, "creates": 4428, "decode_fail": 32789, "rpc_calls": 15892, "rpc_errors": 618, "sol_usd": 101.81639129365657, "open_positions": 107, "log_all_trades": true}
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
Sep 11 22:46:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:16,855 main INFO screen VENOM pass=0 dev=0.5 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 11 22:46:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:21,814 main INFO screen FLYWARS pass=0 dev=0.35 ins=0.0 pro=32 1a=False 1b=False 2=True (5.8s)
Sep 11 22:46:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:31,742 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:46:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:32,873 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:46:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:38,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:46:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:39,231 main INFO screen KIRK pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 11 22:46:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:44,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:46:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:49,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:46:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:46:53,312 main INFO screen wSTONK pass=0 dev=3.42 ins=12.92 pro=79 1a=False 1b=False 2=True (20.5s)
Sep 11 22:47:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:03,823 main INFO screen minecat pass=0 dev=6.63 ins=72.68 pro=1 1a=False 1b=True 2=True (19.0s)
Sep 11 22:47:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:05,071 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:47:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:08,546 main INFO screen MIRCO pass=0 dev=0.0 ins=21.26 pro=28 1a=False 1b=True 2=True (1.3s)
Sep 11 22:47:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:10,145 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:47:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:19,242 main INFO screen $CAJUN pass=0 dev=0.69 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 22:47:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:26,465 main INFO screen stonkfly pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=True (21.5s)
Sep 11 22:47:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:47:59,390 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:48:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:48:03,429 main INFO screen ABORTmeme pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (2.1s)
Sep 11 22:48:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:48:06,213 main INFO screen MIRCO pass=0 dev=6.63 ins=21.94 pro=28 1a=False 1b=False 2=False (6.9s)
Sep 11 22:49:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:49:30,835 main INFO screen $(TCKR) pass=0 dev=40.39 ins=0.0 pro=1 1a=False 1b=False 2=True (3.5s)
Sep 11 22:49:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:49:33,066 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:49:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:49:38,093 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:49:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:49:51,384 main INFO screen wind pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 11 22:49:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:49:52,188 main INFO screen PEKKO pass=0 dev=0.88 ins=45.85 pro=14 1a=False 1b=True 2=True (19.2s)
Sep 11 22:50:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:17,659 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:50:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:25,443 main INFO screen Flyton pass=0 dev=0.0 ins=36.18 pro=12 1a=False 1b=False 2=True (7.9s)
Sep 11 22:50:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:26,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:50:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:36,464 main INFO screen BUZZFLY pass=0 dev=0.0 ins=15.78 pro=22 1a=False 1b=False 2=True (6.0s)
Sep 11 22:50:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:38,122 main INFO screen PEKKO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.3s)
Sep 11 22:50:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:41,569 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:50:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:46,352 main INFO screen WCOI pass=0 dev=1.91 ins=0.0 pro=3 1a=False 1b=False 2=False (2.7s)
Sep 11 22:50:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:48,776 main INFO screen $CAT pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 22:50:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:49,924 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:50:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:50:54,957 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:51:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:08,774 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:22:51:08 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 11 22:51:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:10,253 main INFO screen $$$ pass=0 dev=1.1 ins=0.0 pro=3 1a=False 1b=False 2=False (20.4s)
Sep 11 22:51:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:39,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:51:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:42,829 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:51:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:47,866 main INFO screen Neegyahu pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 11 22:51:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:47,939 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:51:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:52,386 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 22:51:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:56,740 main INFO screen whitefly pass=0 dev=0.0 ins=27.9 pro=14 1a=False 1b=False 2=False (4.8s)
Sep 11 22:51:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 22:51:57,446 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
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
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T22:51:07Z
--- update 2026-09-11T22:56:09Z
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
