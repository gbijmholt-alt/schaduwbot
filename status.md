# Schaduwbot status

- tijd: 2026-09-11 19:35:04 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 5 hours, 48 minutes
- bot-service: active
- code-versie: a16a395
- schijf: 2.8G/38G | geheugen: 610/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3407, "tokens_in_memory": 1377, "msgs": 578334, "trades": 132883, "creates": 1377, "decode_fail": 9625, "rpc_calls": 5436, "rpc_errors": 167, "sol_usd": 101.54189687962393, "open_positions": 71, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 18:38 UTC

Gelogde schaduwtrades: **29225**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 21102 | 3124 | 32 | 3124 | 226 | 5704 | 16870 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 323 | 17% | 1.9% | +42.4% | -16.4% | -6.56% | 99% |
| dip35_V1_gescreend_fail | 2946 | 27% | 3.6% | +46.3% | -25.9% | -6.28% | 100% |
| dip35_V1_alle | 3379 | 26% | 3.7% | +45.5% | -25.2% | -6.56% | 100% |
| dip35_V2_gescreend_pass | 320 | 19% | 2.5% | +45.7% | -21.3% | -8.32% | 100% |
| dip35_V2_gescreend_fail | 2955 | 25% | 4.3% | +57.5% | -28.1% | -6.80% | 100% |
| dip35_V2_alle | 3357 | 24% | 4.3% | +56.0% | -27.7% | -7.39% | 100% |
| dip35_V3_gescreend_pass | 323 | 8% | 2.8% | +283.6% | -22.7% | +2.94% | 100% |
| dip35_V3_gescreend_fail | 2993 | 13% | 5.9% | +119.2% | -29.7% | -9.72% | 100% |
| dip35_V3_alle | 3392 | 13% | 5.8% | +126.0% | -29.3% | -8.95% | 100% |
| dip40_V1_gescreend_pass | 299 | 15% | 1.7% | +46.4% | -15.4% | -6.30% | 99% |
| dip40_V1_gescreend_fail | 2861 | 27% | 3.6% | +48.3% | -25.9% | -6.20% | 100% |
| dip40_V1_alle | 3247 | 26% | 3.6% | +47.8% | -25.1% | -6.39% | 100% |
| dip40_V2_gescreend_pass | 297 | 15% | 2.4% | +50.5% | -19.9% | -9.45% | 100% |
| dip40_V2_gescreend_fail | 2858 | 25% | 4.1% | +56.7% | -28.1% | -7.00% | 100% |
| dip40_V2_alle | 3219 | 24% | 4.2% | +56.0% | -27.5% | -7.65% | 100% |
| dip40_V3_gescreend_pass | 301 | 7% | 2.3% | +326.5% | -20.9% | +2.16% | 100% |
| dip40_V3_gescreend_fail | 2898 | 13% | 5.8% | +108.5% | -29.6% | -11.72% | 100% |
| dip40_V3_alle | 3258 | 12% | 5.6% | +117.4% | -29.0% | -10.82% | 100% |
| dip45_V1_gescreend_pass | 286 | 15% | 1.4% | +51.5% | -15.1% | -4.86% | 98% |
| dip45_V1_gescreend_fail | 2781 | 27% | 3.2% | +49.0% | -25.6% | -5.11% | 100% |
| dip45_V1_alle | 3132 | 26% | 3.2% | +48.9% | -24.8% | -5.33% | 100% |
| dip45_V2_gescreend_pass | 283 | 18% | 2.1% | +49.4% | -19.3% | -7.15% | 99% |
| dip45_V2_gescreend_fail | 2769 | 25% | 3.8% | +59.9% | -27.6% | -5.73% | 100% |
| dip45_V2_alle | 3104 | 24% | 3.8% | +58.9% | -27.1% | -6.25% | 100% |
| dip45_V3_gescreend_pass | 287 | 7% | 2.1% | +379.4% | -20.1% | +7.75% | 100% |
| dip45_V3_gescreend_fail | 2803 | 14% | 5.5% | +117.3% | -29.1% | -8.87% | 100% |
| dip45_V3_alle | 3137 | 13% | 5.3% | +128.1% | -28.5% | -7.70% | 100% |

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
| met_xlink | 2161 | 12% | 2.7% | -9.76% | 100% |
| zonder_xlink | 558 | 18% | 0.0% | +21.55% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 19:25:48 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:25:48,638 main INFO screen CHIMPFONE pass=0 dev=0.37 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 19:25:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:25:50,638 main INFO screen wifwife pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 11 19:25:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:25:50,942 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:25:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:25:59,700 main INFO screen MEME pass=0 dev=0.0 ins=29.45 pro=61 1a=False 1b=False 2=True (8.8s)
Sep 11 19:26:05 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:05,125 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:06,151 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:10 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:10,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:11,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:17,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:23,281 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:32 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:32,526 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.5s)
Sep 11 19:26:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:34,468 main INFO screen $QAIS pass=0 dev=42.6 ins=0.0 pro=10 1a=False 1b=False 2=False (28.4s)
Sep 11 19:26:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:42,918 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:26:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:44,223 main INFO screen ROBIN pass=0 dev=98.58 ins=0.0 pro=1 1a=False 1b=False 2=True (26.5s)
Sep 11 19:26:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:26:47,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:27:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:04,503 main INFO screen hamster pass=0 dev=1.74 ins=0.0 pro=9 1a=False 1b=False 2=False (8.9s)
Sep 11 19:27:08 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:08,775 main INFO screen $QAIS pass=0 dev=58.93 ins=0.0 pro=7 1a=False 1b=False 2=False (25.9s)
Sep 11 19:27:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:12,822 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:27:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:17,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:27:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:17,906 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:27:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:22,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:27:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:36,712 main INFO screen BATONBRAIN pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=True 2=True (24.0s)
Sep 11 19:27:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:27:41,562 main INFO screen DOGGO pass=0 dev=0.0 ins=17.39 pro=53 1a=False 1b=False 2=True (24.4s)
Sep 11 19:28:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:28:11,557 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:28:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:28:16,641 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:28:35 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:28:35,959 main INFO screen Apollo pass=0 dev=12.42 ins=18.87 pro=57 1a=False 1b=False 2=True (24.5s)
Sep 11 19:28:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:28:38,531 main INFO screen Apollo pass=1 dev=0.0 ins=17.79 pro=50 1a=False 1b=False 2=False (3.9s)
Sep 11 19:28:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:28:52,576 main INFO screen BPCATE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.4s)
Sep 11 19:29:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:29:37,085 main INFO screen AILE pass=1 dev=0.03 ins=0.0 pro=37 1a=False 1b=False 2=False (6.8s)
Sep 11 19:29:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:29:51,492 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (8.0s)
Sep 11 19:29:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:29:59,071 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:30:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:03,414 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:30:03 +0000] "GET /health HTTP/1.1" 200 447 "-" "Python-urllib/3.14"
Sep 11 19:30:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:04,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:30:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:22,291 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:30:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:23,045 main INFO screen SOLFLY pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (24.1s)
Sep 11 19:30:25 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:25,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:30:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:29,681 main INFO screen Pay king  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 11 19:30:31 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:31,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:30:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:34,137 main INFO screen LMAO pass=0 dev=1.03 ins=0.0 pro=3 1a=False 1b=False 2=False (11.9s)
Sep 11 19:30:35 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:30:35,278 main INFO screen DOGGO pass=1 dev=0.0 ins=9.34 pro=28 1a=False 1b=False 2=False (5.6s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T18:17:20Z
--- update 2026-09-11T18:22:26Z
--- update 2026-09-11T18:27:35Z
--- update 2026-09-11T18:32:36Z
--- update 2026-09-11T18:38:13Z
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
```

## Analyses (laatste 25 regels)
```
inactive
18:07:51 persistentie
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
