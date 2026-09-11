# Schaduwbot status

- tijd: 2026-09-11 19:40:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 5 hours, 53 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 2.8G/38G | geheugen: 552/3814 MB

## Health
```json
{"ok": false, "last_event_age_s": null, "uptime_s": 0}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 19:38 UTC

Gelogde schaduwtrades: **30725**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 22575 | 3402 | 37 | 3402 | 253 | 6227 | 18370 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 342 | 17% | 2.0% | +43.7% | -16.7% | -6.62% | 99% |
| dip35_V1_gescreend_fail | 3071 | 27% | 3.7% | +46.1% | -26.1% | -6.66% | 100% |
| dip35_V1_alle | 3558 | 26% | 3.7% | +45.3% | -25.5% | -6.84% | 100% |
| dip35_V2_gescreend_pass | 339 | 20% | 2.9% | +44.5% | -21.4% | -8.38% | 100% |
| dip35_V2_gescreend_fail | 3075 | 25% | 4.4% | +57.2% | -28.4% | -7.18% | 100% |
| dip35_V2_alle | 3527 | 24% | 4.4% | +55.4% | -28.0% | -7.68% | 100% |
| dip35_V3_gescreend_pass | 341 | 8% | 3.2% | +287.1% | -22.8% | +2.64% | 100% |
| dip35_V3_gescreend_fail | 3126 | 13% | 6.0% | +120.9% | -29.9% | -9.68% | 100% |
| dip35_V3_alle | 3570 | 13% | 5.9% | +126.5% | -29.4% | -8.95% | 100% |
| dip40_V1_gescreend_pass | 315 | 15% | 1.9% | +47.2% | -15.6% | -6.41% | 99% |
| dip40_V1_gescreend_fail | 2985 | 26% | 3.7% | +48.1% | -26.1% | -6.46% | 100% |
| dip40_V1_alle | 3416 | 26% | 3.7% | +48.0% | -25.3% | -6.49% | 100% |
| dip40_V2_gescreend_pass | 313 | 15% | 2.6% | +48.3% | -19.9% | -9.46% | 100% |
| dip40_V2_gescreend_fail | 2978 | 25% | 4.2% | +56.7% | -28.3% | -7.07% | 100% |
| dip40_V2_alle | 3380 | 24% | 4.2% | +55.8% | -27.7% | -7.69% | 100% |
| dip40_V3_gescreend_pass | 316 | 6% | 2.5% | +326.5% | -21.1% | +0.93% | 100% |
| dip40_V3_gescreend_fail | 3029 | 13% | 5.7% | +115.5% | -29.7% | -10.84% | 100% |
| dip40_V3_alle | 3425 | 12% | 5.6% | +122.9% | -29.1% | -10.22% | 100% |
| dip45_V1_gescreend_pass | 302 | 15% | 1.7% | +52.1% | -15.3% | -5.05% | 98% |
| dip45_V1_gescreend_fail | 2903 | 27% | 3.3% | +48.8% | -25.8% | -5.36% | 100% |
| dip45_V1_alle | 3294 | 26% | 3.2% | +49.1% | -25.0% | -5.43% | 100% |
| dip45_V2_gescreend_pass | 299 | 18% | 2.3% | +47.6% | -19.6% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 2886 | 25% | 3.8% | +59.7% | -27.9% | -5.95% | 100% |
| dip45_V2_alle | 3259 | 24% | 3.8% | +58.5% | -27.3% | -6.45% | 100% |
| dip45_V3_gescreend_pass | 302 | 7% | 2.3% | +379.4% | -20.3% | +6.15% | 100% |
| dip45_V3_gescreend_fail | 2929 | 14% | 5.5% | +123.6% | -29.3% | -8.04% | 100% |
| dip45_V3_alle | 3296 | 13% | 5.3% | +133.5% | -28.6% | -7.20% | 100% |

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
Sep 11 19:30:48 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:48,329 main INFO screen $CAJUN pass=0 dev=0.85 ins=0.0 pro=2 1a=False 1b=False 2=True (7.9s)
Sep 11 19:30:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:50,274 main INFO screen CCM pass=0 dev=3.0 ins=38.59 pro=64 1a=False 1b=False 2=True (24.4s)
Sep 11 19:31:05 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:05,921 main INFO screen 2x coin pass=0 dev=0.0 ins=21.11 pro=21 1a=False 1b=False 2=True (2.5s)
Sep 11 19:31:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:16,528 main INFO screen BIRDS pass=0 dev=0.0 ins=19.63 pro=37 1a=False 1b=False 2=True (3.8s)
Sep 11 19:31:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:23,493 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:31:25 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:25,937 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:31:28 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:28,564 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:31:30 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:30,967 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:31:39 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:39,882 main INFO screen $REGRET pass=0 dev=6.63 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 11 19:31:45 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:45,216 main INFO screen ZORIG pass=0 dev=0.0 ins=14.3 pro=57 1a=False 1b=False 2=True (21.8s)
Sep 11 19:31:46 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:46,815 main INFO screen ZORIG pass=0 dev=0.0 ins=15.18 pro=21 1a=False 1b=False 2=True (20.9s)
Sep 11 19:31:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:31:50,972 main INFO screen JIMAI pass=0 dev=33.96 ins=0.17 pro=15 1a=False 1b=False 2=True (3.3s)
Sep 11 19:32:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:17,196 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:32:25 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:25,085 main INFO screen Paz pass=0 dev=17.7 ins=7.86 pro=37 1a=False 1b=False 2=False (8.0s)
Sep 11 19:32:31 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:31,591 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:32:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:36,682 main INFO screen HOODI pass=1 dev=0.12 ins=0.0 pro=41 1a=False 1b=False 2=False (3.5s)
Sep 11 19:32:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:36,767 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:32:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:50,789 main INFO screen SHODL pass=0 dev=0.0 ins=43.65 pro=47 1a=False 1b=False 2=True (19.2s)
Sep 11 19:32:55 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:32:55,710 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:00 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:00,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:15,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:15,720 main INFO screen batonless pass=0 dev=0.0 ins=45.37 pro=30 1a=False 1b=False 2=True (20.1s)
Sep 11 19:33:19 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:19,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:20,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:27 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:27,618 main INFO screen $REGRET pass=0 dev=3.42 ins=0.0 pro=5 1a=False 1b=False 2=False (8.0s)
Sep 11 19:33:33 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:33,142 main INFO screen PHATLP pass=1 dev=0.0 ins=19.65 pro=11 1a=False 1b=False 2=False (1.8s)
Sep 11 19:33:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:34,170 main INFO screen FATMUSIC pass=0 dev=11.93 ins=7.22 pro=26 1a=False 1b=False 2=True (19.2s)
Sep 11 19:33:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:41,188 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:33:46 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:33:46,261 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:34:00 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:00,899 main INFO screen 9/11 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 11 19:34:10 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:10,500 main INFO screen $REGRET pass=0 dev=39.43 ins=0.0 pro=0 1a=False 1b=False 2=True (1.6s)
Sep 11 19:34:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:20,571 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:34:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:21,059 main INFO screen Paz pass=1 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (3.6s)
Sep 11 19:34:25 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:25,644 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:34:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:29,581 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:34:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:36,936 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 11 19:34:40 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:40,980 main INFO screen ZORIG pass=0 dev=0.0 ins=14.31 pro=20 1a=False 1b=False 2=True (20.6s)
Sep 11 19:34:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:47,680 main INFO screen KRACHI pass=0 dev=0.0 ins=35.8 pro=13 1a=False 1b=True 2=True (1.9s)
Sep 11 19:34:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:34:59,527 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:35:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:04,964 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:35:04 +0000] "GET /health HTTP/1.1" 200 447 "-" "Python-urllib/3.14"
Sep 11 19:35:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:06,697 main INFO screen Reptile pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 11 19:35:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:11,359 main INFO screen $GOAT pass=0 dev=0.64 ins=0.0 pro=4 1a=False 1b=False 2=False (2.0s)
Sep 11 19:35:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:16,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:35:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:21,505 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:35:35 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:35,632 main INFO screen Bee pass=0 dev=2.34 ins=20.85 pro=35 1a=False 1b=False 2=True (19.3s)
Sep 11 19:35:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:43,967 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:35:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:35:49,047 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:36:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:36:03,230 main INFO screen APEROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.0s)
Sep 11 19:36:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:36:04,484 main INFO screen GTA 6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.6s)
Sep 11 19:36:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:36:21,294 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:36:27 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:36:27,789 main INFO screen TINGLE pass=0 dev=0.0 ins=5.45 pro=37 1a=False 1b=False 2=True (6.6s)
Sep 11 19:37:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:11,470 main INFO screen FERSPE pass=0 dev=0.41 ins=0.0 pro=1 1a=False 1b=False 2=False (3.4s)
Sep 11 19:37:24 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:24,481 main INFO screen iMac pass=0 dev=0.0 ins=19.39 pro=22 1a=False 1b=False 2=True (3.7s)
Sep 11 19:37:33 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:33,088 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:37,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:37,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:38,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:43,071 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:44,586 main INFO screen SIXSEVEN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 19:37:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:44,646 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:49,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:52,646 main INFO screen PEEDY pass=0 dev=0.0 ins=45.94 pro=32 1a=False 1b=False 2=True (19.6s)
Sep 11 19:37:56 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:56,143 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:37:58 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:37:58,297 main INFO screen $REGRET pass=0 dev=6.63 ins=0.0 pro=1 1a=False 1b=False 2=False (20.4s)
Sep 11 19:38:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:38:01,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:38:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:38:04,458 main INFO screen ALL pass=0 dev=0.0 ins=55.6 pro=47 1a=False 1b=False 2=True (19.9s)
Sep 11 19:38:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:38:07,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:38:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:38:18,320 main INFO screen ROBOELON pass=0 dev=0.0 ins=20.36 pro=11 1a=False 1b=False 2=False (10.8s)
Sep 11 19:38:19 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:38:19,636 main INFO screen batonless pass=0 dev=0.0 ins=45.4 pro=29 1a=False 1b=False 2=True (23.6s)
Sep 11 19:39:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:39:12,477 main INFO screen SIXSEVEN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (4.3s)
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
```

## Update-log (laatste 20 regels)
```
nieuwe code: a16a395
install klaar
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
```

## Analyses (laatste 25 regels)
```
active
18:07:53 kopieer-simulatie
18:08:00 klaar in 58s -> /opt/schaduwbot/reports/wallets.md
18:38:17 11258 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
18:38:19   ingelezen tot rowid 2079733 (84068 rijen, 84068 bruikbaar)
18:38:19 ingelezen: 84068 nieuwe trades, 84068 bruikbaar (2s)
18:38:32 3000 aankopen van gevolgde wallets geëvalueerd
18:39:36 herkomst: 40 posities gekoppeld
18:39:37 klaar in 80s -> /opt/schaduwbot/reports/ledger.md
18:39:38 klaar in 0s: 2161 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
18:39:38 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 18:39 UTC
18:39:38 36134 tokens geladen
18:39:41   2000 tokens, 289638 trades, 71839 posities (3s)
18:39:43   4000 tokens, 572568 trades, 137840 posities (5s)
18:39:46   6000 tokens, 886184 trades, 210864 posities (9s)
18:39:49   8000 tokens, 1172465 trades, 278408 posities (11s)
18:39:52   10000 tokens, 1467251 trades, 349490 posities (14s)
18:39:55   12000 tokens, 1745027 trades, 416754 posities (17s)
18:39:57   14000 tokens, 2037014 trades, 487116 posities (19s)
18:39:58 posities: 500309 uit 2080675 trades (20s)
18:40:05 118282 wallets gerekend
18:40:06 geluk-toets
18:40:25 persistentie
18:40:27 kopieer-simulatie
18:40:34 klaar in 56s -> /opt/schaduwbot/reports/wallets.md
19:40:08 12765 tokens sinds start volledige logging, waarvan 3627 met een gat door herstart
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
