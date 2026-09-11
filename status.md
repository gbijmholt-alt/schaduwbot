# Schaduwbot status

- tijd: 2026-09-11 20:55:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 7 hours, 8 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.9G/38G | geheugen: 637/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 4530, "tokens_in_memory": 1465, "msgs": 935159, "trades": 185682, "creates": 1465, "decode_fail": 13613, "rpc_calls": 5852, "rpc_errors": 259, "sol_usd": 102.15126201463454, "open_positions": 106, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 20:40 UTC

Gelogde schaduwtrades: **32081**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 23762 | 3627 | 39 | 3626 | 279 | 6708 | 19726 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 360 | 17% | 2.2% | +44.3% | -16.8% | -6.27% | 100% |
| dip35_V1_gescreend_fail | 3168 | 27% | 3.8% | +46.1% | -26.2% | -6.88% | 100% |
| dip35_V1_alle | 3714 | 26% | 3.8% | +45.2% | -25.5% | -7.01% | 100% |
| dip35_V2_gescreend_pass | 357 | 21% | 3.1% | +45.5% | -21.5% | -7.25% | 100% |
| dip35_V2_gescreend_fail | 3171 | 25% | 4.4% | +56.8% | -28.5% | -7.29% | 100% |
| dip35_V2_alle | 3677 | 24% | 4.4% | +55.1% | -28.0% | -7.72% | 100% |
| dip35_V3_gescreend_pass | 358 | 9% | 3.6% | +374.3% | -23.0% | +11.45% | 100% |
| dip35_V3_gescreend_fail | 3231 | 13% | 6.1% | +119.2% | -29.9% | -10.19% | 100% |
| dip35_V3_alle | 3725 | 13% | 6.0% | +130.9% | -29.4% | -8.63% | 100% |
| dip40_V1_gescreend_pass | 333 | 15% | 2.1% | +47.5% | -15.7% | -6.05% | 99% |
| dip40_V1_gescreend_fail | 3089 | 26% | 3.8% | +48.0% | -26.1% | -6.60% | 100% |
| dip40_V1_alle | 3570 | 26% | 3.7% | +47.9% | -25.3% | -6.57% | 100% |
| dip40_V2_gescreend_pass | 330 | 17% | 2.7% | +49.8% | -20.2% | -8.30% | 100% |
| dip40_V2_gescreend_fail | 3081 | 25% | 4.3% | +56.3% | -28.4% | -7.22% | 100% |
| dip40_V2_alle | 3527 | 24% | 4.3% | +55.5% | -27.8% | -7.72% | 100% |
| dip40_V3_gescreend_pass | 333 | 7% | 3.0% | +439.0% | -21.3% | +10.46% | 100% |
| dip40_V3_gescreend_fail | 3140 | 13% | 5.8% | +113.7% | -29.7% | -11.34% | 100% |
| dip40_V3_alle | 3578 | 12% | 5.7% | +127.8% | -29.1% | -9.81% | 100% |
| dip45_V1_gescreend_pass | 318 | 16% | 1.9% | +51.3% | -15.6% | -4.63% | 98% |
| dip45_V1_gescreend_fail | 3010 | 27% | 3.3% | +48.5% | -25.8% | -5.44% | 100% |
| dip45_V1_alle | 3446 | 26% | 3.3% | +48.6% | -25.1% | -5.57% | 100% |
| dip45_V2_gescreend_pass | 314 | 19% | 2.5% | +49.1% | -19.8% | -6.41% | 100% |
| dip45_V2_gescreend_fail | 2989 | 25% | 3.9% | +59.1% | -28.0% | -6.07% | 100% |
| dip45_V2_alle | 3400 | 24% | 3.9% | +58.0% | -27.5% | -6.58% | 100% |
| dip45_V3_gescreend_pass | 316 | 7% | 2.5% | +485.0% | -20.4% | +16.35% | 100% |
| dip45_V3_gescreend_fail | 3041 | 14% | 5.5% | +121.6% | -29.3% | -8.57% | 100% |
| dip45_V3_alle | 3444 | 13% | 5.3% | +138.2% | -28.6% | -6.84% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 2.0%, kans ruïne 97.5%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2374 | 13% | 3.4% | -9.88% | 100% |
| zonder_xlink | 645 | 21% | 0.0% | +35.85% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 20:45:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:22,321 main INFO screen air pass=0 dev=0.0 ins=17.67 pro=43 1a=False 1b=False 2=True (3.7s)
Sep 11 20:45:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:22,963 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:45:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:26,045 main INFO screen BPCATE pass=0 dev=0.7 ins=0.0 pro=4 1a=False 1b=False 2=False (2.5s)
Sep 11 20:45:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:34,457 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:45:34 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 20:45:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:37,417 main INFO screen $KRABS pass=0 dev=0.69 ins=0.0 pro=2 1a=False 1b=False 2=False (19.6s)
Sep 11 20:45:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:42,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:45:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:45,212 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:45:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:47,581 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:45:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:52,522 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:45:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:53,355 main INFO screen air pass=1 dev=0.0 ins=17.43 pro=23 1a=False 1b=False 2=False (8.2s)
Sep 11 20:45:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:45:57,594 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:46:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:03,265 main INFO screen BLKMAN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (4.5s)
Sep 11 20:46:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:05,243 main INFO screen POCKLY pass=0 dev=0.47 ins=49.6 pro=30 1a=False 1b=False 2=True (22.8s)
Sep 11 20:46:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:14,788 main INFO screen FLYTON pass=0 dev=0.0 ins=38.25 pro=9 1a=False 1b=False 2=True (22.6s)
Sep 11 20:46:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:15,520 main INFO screen flynu pass=0 dev=0.0 ins=27.64 pro=37 1a=False 1b=False 2=False (4.6s)
Sep 11 20:46:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:25,630 main INFO screen $GOAT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 20:46:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:31,355 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:46:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:36,425 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:46:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:50,956 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 11 20:46:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:52,484 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:46:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:46:57,565 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:12,443 main INFO screen b-all-in pass=0 dev=0.0 ins=5.32 pro=62 1a=False 1b=False 2=True (20.0s)
Sep 11 20:47:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:21,688 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:26,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:43,193 main INFO screen FLYTON pass=0 dev=0.0 ins=37.48 pro=17 1a=False 1b=False 2=True (21.6s)
Sep 11 20:47:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:48,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:53,122 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:53,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:47:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:47:58,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:48:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:07,913 main INFO screen GAMBLE pass=0 dev=0.0 ins=27.76 pro=72 1a=False 1b=False 2=True (19.9s)
Sep 11 20:48:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:14,261 main INFO screen BOY pass=0 dev=0.0 ins=16.71 pro=62 1a=False 1b=False 2=True (20.7s)
Sep 11 20:48:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:18,650 main INFO screen DOGELESS pass=0 dev=0.0 ins=16.89 pro=50 1a=False 1b=False 2=True (3.9s)
Sep 11 20:48:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:22,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:48:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:23,012 main INFO screen APPLECAT pass=0 dev=0.77 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 20:48:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:30,775 main INFO screen BOY pass=1 dev=0.0 ins=16.84 pro=37 1a=False 1b=False 2=False (9.2s)
Sep 11 20:48:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:42,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:48:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:50,221 main INFO screen DOOB pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 11 20:48:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:48:57,005 main INFO screen ALLINU pass=1 dev=0.0 ins=4.63 pro=51 1a=False 1b=False 2=False (5.0s)
Sep 11 20:49:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:49:11,794 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:49:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:49:15,811 main INFO screen GAMBLE pass=1 dev=0.0 ins=8.49 pro=20 1a=False 1b=False 2=False (1.8s)
Sep 11 20:49:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:49:16,873 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:49:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:49:31,676 main INFO screen NIKE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 11 20:49:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:49:37,698 main INFO screen NEEDOH pass=1 dev=0.0 ins=8.77 pro=20 1a=False 1b=False 2=False (1.5s)
Sep 11 20:50:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:21,232 main INFO screen Parker pass=1 dev=0.0 ins=16.61 pro=46 1a=False 1b=False 2=False (4.0s)
Sep 11 20:50:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:30,591 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:50:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:34,449 main INFO screen max pass=0 dev=0.0 ins=17.97 pro=31 1a=False 1b=False 2=True (2.2s)
Sep 11 20:50:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:37,149 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:50:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 20:50:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:37,873 main INFO screen ELONGUY pass=0 dev=0.0 ins=7.38 pro=13 1a=False 1b=False 2=True (7.4s)
Sep 11 20:50:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:47,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:50:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:53,309 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:50:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:50:54,272 main INFO screen Durkio pass=0 dev=0.24 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 11 20:51:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:09,445 main INFO screen PONS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (21.6s)
Sep 11 20:51:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:10,263 main INFO screen $Sponge pass=0 dev=0.69 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 11 20:51:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:14,698 main INFO screen AUtism pass=1 dev=0.0 ins=12.8 pro=14 1a=False 1b=False 2=False (1.2s)
Sep 11 20:51:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:18,960 main INFO screen DIOUF pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.4s)
Sep 11 20:51:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:19,508 main INFO screen air pass=1 dev=0.0 ins=8.95 pro=20 1a=False 1b=False 2=False (3.2s)
Sep 11 20:51:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:24,416 main INFO screen co1n9 pass=0 dev=0.0 ins=16.42 pro=31 1a=False 1b=False 2=True (6.0s)
Sep 11 20:51:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:28,768 main INFO screen ELONGUY pass=1 dev=0.0 ins=7.21 pro=18 1a=False 1b=False 2=False (1.3s)
Sep 11 20:51:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:35,955 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:51:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:41,026 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:51:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:45,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:51:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:54,293 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 11 20:51:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:51:55,814 main INFO screen BEAST pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 11 20:52:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:52:15,967 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 11 20:52:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:52:17,101 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 20:52:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:52:23,756 main INFO screen CAPY pass=0 dev=0.35 ins=36.76 pro=15 1a=False 1b=False 2=True (3.3s)
Sep 11 20:52:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:52:50,721 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:52:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:52:55,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:53:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:53:06,540 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 11 20:53:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:53:09,369 main INFO screen TOAD pass=0 dev=0.0 ins=0.04 pro=1 1a=False 1b=False 2=False (18.7s)
Sep 11 20:53:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:53:49,892 main INFO screen VENOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.6s)
Sep 11 20:54:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:54:52,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:54:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:54:55,823 main INFO screen $KAT pass=0 dev=0.29 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 20:55:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:00,278 main INFO screen Jarro pass=1 dev=5.0 ins=0.79 pro=37 1a=False 1b=False 2=False (8.0s)
Sep 11 20:55:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:08,914 main INFO screen CHAROC pass=0 dev=0.35 ins=0.0 pro=5 1a=False 1b=False 2=False (3.5s)
Sep 11 20:55:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:14,757 main INFO screen NEIL pass=1 dev=0.0 ins=7.79 pro=16 1a=False 1b=False 2=False (3.4s)
Sep 11 20:55:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:15,351 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:55:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:20,411 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 20:55:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:34,942 main INFO screen September  pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 11 20:55:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 20:55:38,870 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:20:55:38 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T19:40:04Z
nieuwe code: 1cefa36
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 670a5941fedf41389993862a94844cc9
analyses gestart (8746aefc73b4)
--- update 2026-09-11T19:45:08Z
--- update 2026-09-11T19:50:11Z
--- update 2026-09-11T19:55:12Z
--- update 2026-09-11T20:00:15Z
--- update 2026-09-11T20:05:16Z
--- update 2026-09-11T20:10:18Z
--- update 2026-09-11T20:15:22Z
--- update 2026-09-11T20:20:26Z
--- update 2026-09-11T20:25:28Z
--- update 2026-09-11T20:30:28Z
--- update 2026-09-11T20:35:28Z
--- update 2026-09-11T20:40:31Z
--- update 2026-09-11T20:45:33Z
--- update 2026-09-11T20:50:36Z
--- update 2026-09-11T20:55:37Z
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
