# Schaduwbot status

- tijd: 2026-09-11 21:47:47 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 8 hours, 0 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.0G/38G | geheugen: 717/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 7659, "tokens_in_memory": 2746, "msgs": 1672197, "trades": 323815, "creates": 2746, "decode_fail": 23451, "rpc_calls": 10181, "rpc_errors": 427, "sol_usd": 102.58823412410312, "open_positions": 114, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 21:40 UTC

Gelogde schaduwtrades: **33418**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 25144 | 3869 | 41 | 3866 | 323 | 7170 | 21063 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 392 | 17% | 2.0% | +43.1% | -17.1% | -6.97% | 100% |
| dip35_V1_gescreend_fail | 3269 | 27% | 3.7% | +46.2% | -26.0% | -6.86% | 100% |
| dip35_V1_alle | 3872 | 26% | 3.7% | +45.1% | -25.3% | -7.07% | 100% |
| dip35_V2_gescreend_pass | 386 | 21% | 3.1% | +43.9% | -21.8% | -8.06% | 100% |
| dip35_V2_gescreend_fail | 3272 | 25% | 4.3% | +56.7% | -28.3% | -7.31% | 100% |
| dip35_V2_alle | 3828 | 24% | 4.3% | +54.6% | -27.9% | -7.82% | 100% |
| dip35_V3_gescreend_pass | 388 | 8% | 3.6% | +374.3% | -23.1% | +8.68% | 100% |
| dip35_V3_gescreend_fail | 3339 | 13% | 5.9% | +119.3% | -29.8% | -9.88% | 100% |
| dip35_V3_alle | 3878 | 13% | 5.8% | +129.9% | -29.3% | -8.55% | 100% |
| dip40_V1_gescreend_pass | 362 | 15% | 1.9% | +46.6% | -16.2% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 3194 | 26% | 3.7% | +48.0% | -26.0% | -6.60% | 100% |
| dip40_V1_alle | 3721 | 25% | 3.6% | +47.7% | -25.2% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 356 | 16% | 2.5% | +48.9% | -20.4% | -9.09% | 100% |
| dip40_V2_gescreend_fail | 3185 | 25% | 4.2% | +56.0% | -28.2% | -7.32% | 100% |
| dip40_V2_alle | 3670 | 24% | 4.2% | +55.0% | -27.7% | -7.90% | 100% |
| dip40_V3_gescreend_pass | 361 | 7% | 2.8% | +423.8% | -21.4% | +8.19% | 100% |
| dip40_V3_gescreend_fail | 3251 | 13% | 5.7% | +113.9% | -29.6% | -11.00% | 100% |
| dip40_V3_alle | 3725 | 12% | 5.5% | +126.8% | -29.0% | -9.66% | 100% |
| dip45_V1_gescreend_pass | 348 | 16% | 1.7% | +50.0% | -16.0% | -5.37% | 99% |
| dip45_V1_gescreend_fail | 3112 | 27% | 3.2% | +48.6% | -25.7% | -5.39% | 100% |
| dip45_V1_alle | 3593 | 26% | 3.2% | +48.6% | -25.0% | -5.63% | 100% |
| dip45_V2_gescreend_pass | 340 | 19% | 2.4% | +47.9% | -20.1% | -7.29% | 100% |
| dip45_V2_gescreend_fail | 3095 | 25% | 3.8% | +58.7% | -27.9% | -6.12% | 100% |
| dip45_V2_alle | 3543 | 24% | 3.8% | +57.4% | -27.3% | -6.72% | 100% |
| dip45_V3_gescreend_pass | 343 | 7% | 2.3% | +467.9% | -20.6% | +13.58% | 100% |
| dip45_V3_gescreend_fail | 3150 | 14% | 5.3% | +120.8% | -29.1% | -8.30% | 100% |
| dip45_V3_alle | 3588 | 13% | 5.2% | +136.3% | -28.5% | -6.77% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 1.1%, kans ruïne 98.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2548 | 13% | 3.2% | -10.54% | 100% |
| zonder_xlink | 728 | 19% | 0.0% | +30.12% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 21:38:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:16,032 main INFO screen RABFROG pass=0 dev=0.47 ins=53.04 pro=22 1a=False 1b=False 2=True (23.1s)
Sep 11 21:38:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:25,071 main INFO screen WCOI pass=0 dev=1.22 ins=0.0 pro=3 1a=False 1b=False 2=False (4.1s)
Sep 11 21:38:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:32,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,321 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,727 main INFO screen EMS pass=1 dev=0.0 ins=9.39 pro=14 1a=False 1b=False 2=False (1.5s)
Sep 11 21:38:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:38,769 aiohttp.access INFO 45.156.129.132 [11/Sep/2026:21:38:38 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 11 21:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:52,284 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:38:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:52,671 main INFO screen BUTTHOLE pass=0 dev=1.74 ins=19.05 pro=73 1a=False 1b=False 2=True (20.1s)
Sep 11 21:38:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:38:57,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,572 main INFO screen ELOGE pass=0 dev=0.0 ins=17.81 pro=39 1a=False 1b=False 2=True (5.9s)
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,796 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:00,888 main INFO screen Trump4Prez pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 11 21:39:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:03,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:05,868 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:08,286 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:39:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:13,645 main INFO screen Peg pass=0 dev=0.0 ins=20.94 pro=73 1a=False 1b=False 2=True (21.5s)
Sep 11 21:39:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:19,438 main INFO screen NOKY pass=0 dev=0.18 ins=79.13 pro=6 1a=False 1b=True 2=True (18.9s)
Sep 11 21:39:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:23,015 main INFO screen MEME pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 11 21:39:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:46,533 main INFO screen $CAT pass=0 dev=0.71 ins=0.0 pro=1 1a=False 1b=False 2=False (4.4s)
Sep 11 21:39:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:39:54,899 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:00,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:03,861 main INFO screen DOGA pass=0 dev=0.43 ins=0.0 pro=3 1a=False 1b=False 2=False (5.6s)
Sep 11 21:40:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:10,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:40:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:40:59,586 main INFO screen pill pass=0 dev=0.0 ins=24.51 pro=46 1a=False 1b=False 2=True (64.8s)
Sep 11 21:41:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:01,387 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 11 21:41:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:01,783 main INFO screen Inu pass=1 dev=0.0 ins=0.76 pro=53 1a=False 1b=False 2=False (6.6s)
Sep 11 21:41:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:02,918 main INFO screen CATBULL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.3s)
Sep 11 21:41:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:28,465 main INFO screen mmrich pass=0 dev=0.47 ins=0.0 pro=2 1a=False 1b=False 2=False (4.2s)
Sep 11 21:41:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:34,296 main INFO screen MOMO pass=1 dev=0.0 ins=11.3 pro=17 1a=False 1b=False 2=False (1.6s)
Sep 11 21:41:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:45,386 main INFO screen GOSI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 21:41:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:46,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:41:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:51,545 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:41:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:41:55,700 main INFO screen 911 pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 11 21:42:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:05,824 main INFO screen Meowcraft pass=0 dev=0.0 ins=22.31 pro=34 1a=False 1b=False 2=True (19.4s)
Sep 11 21:42:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:15,111 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:15,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:20,175 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:23,836 main INFO screen GOSI pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 21:42:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:27,418 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:32,615 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:42:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:35,834 main INFO screen FOMOLIFE pass=0 dev=0.0 ins=8.3 pro=46 1a=False 1b=False 2=True (20.8s)
Sep 11 21:42:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:37,270 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:42:37 +0000] "GET /health HTTP/1.1" 200 449 "-" "Python-urllib/3.14"
Sep 11 21:42:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:42:47,637 main INFO screen FOMOLIFE pass=0 dev=0.0 ins=25.97 pro=63 1a=False 1b=False 2=True (20.3s)
Sep 11 21:43:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:43:00,244 main INFO screen COCA-COLA pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 21:43:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:43:13,136 main INFO screen OPP pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 21:43:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:43:18,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:43:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:43:23,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:43:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:43:37,875 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 11 21:44:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:03,927 main INFO screen NUT pass=0 dev=0.0 ins=21.17 pro=72 1a=False 1b=False 2=True (3.8s)
Sep 11 21:44:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:08,958 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:44:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:09,466 main INFO screen cash cat pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=True (2.6s)
Sep 11 21:44:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:16,915 main INFO screen GOYSLOP pass=0 dev=1.39 ins=16.55 pro=66 1a=False 1b=False 2=True (8.4s)
Sep 11 21:44:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:42,915 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:44:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:47,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:44:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:50,446 main INFO screen SPOOKY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 11 21:44:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:50,557 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:44:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:52,615 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:44:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:44:58,782 main INFO screen 4neegy pass=0 dev=4.27 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 11 21:45:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:07,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:08,554 main INFO screen ktw pass=0 dev=9.66 ins=39.3 pro=77 1a=False 1b=False 2=True (21.1s)
Sep 11 21:45:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:12,153 main INFO screen CHONK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.9s)
Sep 11 21:45:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:12,661 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:14,018 main INFO screen mmrich pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 21:45:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:23,893 main INFO screen WCOI pass=0 dev=1.57 ins=0.0 pro=2 1a=False 1b=False 2=True (1.9s)
Sep 11 21:45:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:24,660 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:27,973 main INFO screen Clicking pass=0 dev=0.0 ins=20.18 pro=39 1a=False 1b=False 2=True (21.3s)
Sep 11 21:45:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:31,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:32,811 main INFO screen cap pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 11 21:45:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:36,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:43,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:49,016 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:45:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:45:52,681 main INFO screen MOCHI pass=0 dev=0.39 ins=44.3 pro=17 1a=False 1b=False 2=True (21.5s)
Sep 11 21:46:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:03,177 main INFO screen DFV pass=0 dev=0.0 ins=16.37 pro=30 1a=False 1b=False 2=True (19.5s)
Sep 11 21:46:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:29,184 main INFO screen brainsem pass=0 dev=0.0 ins=27.49 pro=20 1a=False 1b=False 2=False (3.0s)
Sep 11 21:46:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:30,789 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:46:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:32,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:46:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:38,103 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 21:46:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:39,441 main INFO screen AWAY pass=0 dev=1.08 ins=0.0 pro=2 1a=False 1b=False 2=False (8.7s)
Sep 11 21:46:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:46:52,414 main INFO screen ClaudeAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 11 21:47:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-11 21:47:47,765 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:21:47:47 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T20:20:26Z
--- update 2026-09-11T20:25:28Z
--- update 2026-09-11T20:30:28Z
--- update 2026-09-11T20:35:28Z
--- update 2026-09-11T20:40:31Z
--- update 2026-09-11T20:45:33Z
--- update 2026-09-11T20:50:36Z
--- update 2026-09-11T20:55:37Z
--- update 2026-09-11T21:00:40Z
--- update 2026-09-11T21:05:43Z
--- update 2026-09-11T21:11:05Z
--- update 2026-09-11T21:16:17Z
--- update 2026-09-11T21:21:36Z
--- update 2026-09-11T21:27:04Z
--- update 2026-09-11T21:32:13Z
--- update 2026-09-11T21:37:20Z
--- update 2026-09-11T21:42:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 849a8b3b0e3b4493a07ec162bd13876a
analyses gestart (8746aefc73b4)
--- update 2026-09-11T21:47:46Z
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
