# Schaduwbot status

- tijd: 2026-09-12 06:24:27 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 16 hours, 37 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1121/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 38658, "tokens_in_memory": 6021, "msgs": 7021852, "trades": 1297835, "creates": 12404, "decode_fail": 62116, "rpc_calls": 43870, "rpc_errors": 1766, "sol_usd": 101.70449277779848, "open_positions": 17, "log_all_trades": true}
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
Sep 12 06:03:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:15,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:03:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:20,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:03:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:40,215 main INFO screen Gatto pass=0 dev=15.17 ins=0.0 pro=22 1a=False 1b=True 2=False (5.5s)
Sep 12 06:03:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:41,135 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:03:41 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:03:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:41,388 main INFO screen stonk pass=0 dev=64.06 ins=0.06 pro=17 1a=False 1b=False 2=False (26.0s)
Sep 12 06:04:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:04:06,310 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:04:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:04:11,384 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:04:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:04:32,420 main INFO screen dihcoin pass=0 dev=0.0 ins=16.64 pro=48 1a=False 1b=False 2=True (26.2s)
Sep 12 06:06:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:08,496 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:06:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:13,565 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:06:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:14,806 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:06:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:19,873 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:06:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:33,138 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (24.7s)
Sep 12 06:06:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:35,899 main INFO screen stuART pass=0 dev=2.53 ins=0.0 pro=4 1a=False 1b=False 2=False (7.1s)
Sep 12 06:06:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:06:39,621 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.9s)
Sep 12 06:07:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:05,181 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:07:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:10,251 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:07:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:30,267 main INFO screen bagtone pass=0 dev=6.32 ins=27.29 pro=18 1a=False 1b=True 2=True (25.2s)
Sep 12 06:07:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:51,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:07:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:57,057 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (6.9s)
Sep 12 06:07:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:07:57,059 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:08:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:12,039 main INFO screen Dihcoin pass=0 dev=0.0 ins=23.91 pro=51 1a=False 1b=False 2=True (20.6s)
Sep 12 06:08:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:29,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:08:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:34,452 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:08:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:35,146 main INFO screen SASS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.7s)
Sep 12 06:08:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:45,038 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:08:45 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:08:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:08:56,675 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.7s)
Sep 12 06:09:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:09:18,426 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:09:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:09:23,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:09:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:09:42,226 main INFO screen Bricko pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (23.9s)
Sep 12 06:10:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:10:45,068 main INFO screen IT pass=0 dev=0.0 ins=11.28 pro=47 1a=False 1b=False 2=True (2.3s)
Sep 12 06:10:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:10:59,684 main INFO screen Pepizza pass=0 dev=1.84 ins=0.0 pro=2 1a=False 1b=False 2=False (9.4s)
Sep 12 06:11:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:11:10,201 main INFO screen oilcoin pass=1 dev=3.5 ins=1.63 pro=28 1a=False 1b=False 2=False (9.2s)
Sep 12 06:11:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:11:58,851 main INFO screen REVOLVER pass=1 dev=0.18 ins=0.0 pro=50 1a=False 1b=False 2=False (8.6s)
Sep 12 06:12:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:12:03,954 main INFO screen REVOLVER pass=1 dev=0.0 ins=9.64 pro=36 1a=False 1b=False 2=False (3.9s)
Sep 12 06:12:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:12:21,589 main INFO screen fuelcoin pass=0 dev=0.0 ins=11.48 pro=49 1a=False 1b=False 2=True (7.2s)
Sep 12 06:12:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:12:28,346 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (8.4s)
Sep 12 06:12:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:12:44,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:12:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:12:49,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:13:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:04,845 main INFO screen WENDEEZ pass=0 dev=0.0 ins=20.05 pro=57 1a=False 1b=False 2=True (20.8s)
Sep 12 06:13:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:25,806 main INFO screen DDKONG pass=0 dev=33.74 ins=0.17 pro=7 1a=False 1b=False 2=True (6.2s)
Sep 12 06:13:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:40,208 aiohttp.access INFO 89.42.231.200 [12/Sep/2026:06:13:40 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 06:13:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:40,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:13:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:45,905 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:13:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:13:50,592 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:13:50 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:14:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:14:04,728 main INFO screen LBT pass=0 dev=10.0 ins=25.15 pro=14 1a=False 1b=True 2=True (24.0s)
Sep 12 06:15:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:10,810 main INFO screen GLDFISH pass=0 dev=1.05 ins=10.18 pro=35 1a=False 1b=False 2=True (3.3s)
Sep 12 06:15:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:17,517 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:15:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:21,399 main INFO screen DEVOLVE pass=0 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=True (7.1s)
Sep 12 06:15:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:22,589 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:15:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:26,641 main INFO screen MEOWL pass=0 dev=1.05 ins=0.0 pro=5 1a=False 1b=False 2=False (10.3s)
Sep 12 06:15:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:33,967 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 06:15:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:40,330 main INFO screen Peppapig pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (23.2s)
Sep 12 06:15:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:50,790 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:15:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:54,082 main INFO screen Costcow pass=0 dev=0.0 ins=10.38 pro=37 1a=False 1b=False 2=True (8.0s)
Sep 12 06:15:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:15:55,859 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:16:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:16:13,015 main INFO screen Innitpep? pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (22.3s)
Sep 12 06:17:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:17:34,354 main INFO screen Gubby pass=0 dev=0.0 ins=11.78 pro=30 1a=False 1b=False 2=True (8.4s)
Sep 12 06:17:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:17:59,832 main INFO screen GOOSE pass=0 dev=1.05 ins=0.0 pro=4 1a=False 1b=False 2=False (7.2s)
Sep 12 06:18:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:18:10,202 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:18:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:18:22,994 main INFO screen $speed pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (12.9s)
Sep 12 06:19:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:19:10,359 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:19:10 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 06:19:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:19:59,566 main INFO screen LOOM pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 12 06:20:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:20:12,551 main INFO screen GRC pass=1 dev=0.0 ins=12.6 pro=70 1a=False 1b=False 2=False (7.3s)
Sep 12 06:20:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:20:39,329 main INFO screen Pepecake pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 12 06:22:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:22:10,066 main INFO screen Peputitin pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 12 06:22:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:22:43,669 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:22:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:22:45,122 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:22:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:22:48,773 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:22:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:22:50,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:23:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:10,757 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.2s)
Sep 12 06:23:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:11,003 main INFO screen FROK pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (26.0s)
Sep 12 06:23:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:11,715 main INFO screen DOOB pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 12 06:23:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:17,266 main INFO screen DIP pass=0 dev=0.0 ins=0.0 pro=29 1a=False 1b=False 2=True (3.8s)
Sep 12 06:23:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:25,755 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:23:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:26,738 main INFO screen meme pass=0 dev=0.0 ins=12.63 pro=31 1a=False 1b=False 2=True (6.5s)
Sep 12 06:23:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:30,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:23:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:23:49,493 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (23.8s)
Sep 12 06:24:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:24:09,998 main INFO screen imposter pass=0 dev=0.0 ins=16.41 pro=31 1a=False 1b=False 2=True (7.5s)
Sep 12 06:24:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:24:27,082 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:24:27 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T05:58:38Z
Running as unit: schaduwbot-wallets.service; invocation ID: c28a94468726478892cb2c2291593995
analyses gestart (8746aefc73b4)
--- update 2026-09-12T06:03:40Z
--- update 2026-09-12T06:08:44Z
--- update 2026-09-12T06:13:49Z
--- update 2026-09-12T06:19:09Z
--- update 2026-09-12T06:24:26Z
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
