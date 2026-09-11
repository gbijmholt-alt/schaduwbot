# Schaduwbot status

- tijd: 2026-09-11 19:04:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 5 hours, 17 minutes
- bot-service: active
- code-versie: a16a395
- schijf: 2.8G/38G | geheugen: 571/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 1579, "tokens_in_memory": 651, "msgs": 216035, "trades": 59561, "creates": 651, "decode_fail": 3703, "rpc_calls": 2537, "rpc_errors": 62, "sol_usd": 101.0974459220601, "open_positions": 44, "log_all_trades": true}
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
Sep 11 18:52:53 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:52:53,645 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:01,219 main INFO screen fg pass=0 dev=0.45 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 18:53:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:02,981 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:08 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:08,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:10 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:10,153 main INFO screen S&M500 pass=0 dev=0.0 ins=18.99 pro=65 1a=False 1b=False 2=True (21.6s)
Sep 11 18:53:10 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:10,927 main INFO screen WEB pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (8.0s)
Sep 11 18:53:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:13,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:15,413 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:20,478 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:53:28 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:28,564 main INFO screen S&M500 pass=0 dev=31.52 ins=0.0 pro=41 1a=False 1b=False 2=False (21.0s)
Sep 11 18:53:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:37,109 main INFO screen S&M500 pass=0 dev=0.0 ins=15.68 pro=37 1a=False 1b=False 2=True (21.8s)
Sep 11 18:53:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:37,305 main INFO screen pic  pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=True (4.5s)
Sep 11 18:53:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:50,958 main INFO screen gon pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 11 18:53:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:53:52,115 main INFO screen somecall pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (4.3s)
Sep 11 18:54:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:54:06,513 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:54:06 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 18:54:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:54:16,172 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:54:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:54:22,854 main INFO screen PepeCoin pass=0 dev=2.19 ins=17.8 pro=24 1a=False 1b=False 2=True (6.8s)
Sep 11 18:55:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:01,457 main INFO screen PepeCoin pass=0 dev=0.0 ins=19.89 pro=59 1a=False 1b=False 2=True (3.8s)
Sep 11 18:55:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:15,988 main INFO screen infin pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 11 18:55:33 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:33,991 main INFO screen CAliens pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.7s)
Sep 11 18:55:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:49,094 main INFO screen duck pass=0 dev=7.15 ins=0.66 pro=24 1a=False 1b=False 2=False (4.3s)
Sep 11 18:55:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:50,503 main INFO screen hamster pass=0 dev=1.01 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 11 18:55:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:55:51,333 main INFO screen XRPp pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 11 18:56:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:11,048 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 18:56:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:11,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:56:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:16,198 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:56:30 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:30,290 main INFO screen Investoors pass=0 dev=0.0 ins=37.74 pro=73 1a=False 1b=False 2=True (19.3s)
Sep 11 18:56:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:47,123 main INFO screen PvP pass=0 dev=5.95 ins=0.0 pro=46 1a=False 1b=False 2=False (6.2s)
Sep 11 18:56:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:52,712 main INFO screen NFT pass=1 dev=0.0 ins=11.92 pro=31 1a=False 1b=False 2=False (8.3s)
Sep 11 18:56:53 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:56:53,251 main INFO screen OTC pass=1 dev=0.0 ins=18.2 pro=33 1a=False 1b=False 2=False (10.0s)
Sep 11 18:57:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:29,640 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:57:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:34,709 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:57:39 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:39,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:57:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:42,633 main INFO screen kittylick pass=0 dev=0.45 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 11 18:57:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:44,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:57:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:49,143 main INFO screen STONK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.6s)
Sep 11 18:57:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:57:59,503 main INFO screen PENIS  pass=0 dev=0.0 ins=47.95 pro=58 1a=False 1b=False 2=True (20.5s)
Sep 11 18:58:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:06,827 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:58:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:11,901 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:58:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:26,711 main INFO screen hamster pass=0 dev=0.44 ins=0.0 pro=6 1a=False 1b=False 2=False (4.4s)
Sep 11 18:58:28 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:28,803 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=3 1a=False 1b=False 2=True (22.0s)
Sep 11 18:58:31 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:31,097 main INFO screen SIXSEVEN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 18:58:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:58:41,853 main INFO screen $CAJUN pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 11 18:59:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:59:20,500 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:59:20 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
Sep 11 18:59:24 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:59:24,596 main INFO screen PG3D pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 18:59:32 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:59:32,664 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:59:39 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:59:39,527 main INFO screen FLYBODY pass=1 dev=0.0 ins=19.49 pro=15 1a=False 1b=False 2=False (6.9s)
Sep 11 19:00:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:03,313 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:08 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:08,342 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:20 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:20,063 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:23,994 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:25 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:25,138 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:29,067 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:00:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:29,173 main INFO screen cock pass=0 dev=0.0 ins=47.95 pro=20 1a=False 1b=False 2=True (26.0s)
Sep 11 19:00:35 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:35,613 main INFO screen IX3 pass=0 dev=0.7 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 11 19:00:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:42,255 main INFO screen PUMPST pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 19:00:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:43,131 main INFO screen Emberpepe pass=0 dev=0.18 ins=79.13 pro=7 1a=False 1b=True 2=True (23.1s)
Sep 11 19:00:49 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:49,957 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.7s)
Sep 11 19:00:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:51,774 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 11 19:00:53 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:53,360 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (29.4s)
Sep 11 19:00:55 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:55,781 main INFO screen INU pass=1 dev=0.0 ins=19.34 pro=15 1a=False 1b=False 2=False (5.8s)
Sep 11 19:00:59 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:00:59,203 main INFO screen Bricko pass=0 dev=0.19 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 19:01:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:01:01,298 main INFO screen WELD pass=1 dev=1.74 ins=0.0 pro=41 1a=False 1b=False 2=False (5.8s)
Sep 11 19:01:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:01:21,569 main INFO screen €W4IT pass=0 dev=0.53 ins=0.0 pro=6 1a=False 1b=False 2=False (9.7s)
Sep 11 19:01:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:01:22,503 main INFO screen DOOROC pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=True (6.1s)
Sep 11 19:01:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:01:38,770 main INFO screen jumpncar pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 11 19:02:40 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:02:40,177 main INFO screen kittylick pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (7.3s)
Sep 11 19:02:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:02:42,661 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:02:54 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:02:54,067 main INFO screen SPLIT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (11.5s)
Sep 11 19:02:58 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:02:58,815 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:03:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:03:03,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:03:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:03:18,462 main INFO screen CATFONE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.1s)
Sep 11 19:03:22 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:03:22,030 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.3s)
Sep 11 19:03:57 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:03:57,198 main INFO screen ca pass=0 dev=0.04 ins=0.0 pro=3 1a=False 1b=False 2=False (8.1s)
Sep 11 19:04:08 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:08,483 main INFO screen $unity pass=0 dev=19.92 ins=0.0 pro=26 1a=False 1b=False 2=False (11.9s)
Sep 11 19:04:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:11,149 main INFO screen SPLIT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (12.5s)
Sep 11 19:04:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:12,674 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (11.3s)
Sep 11 19:04:14 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:14,724 main INFO screen ANDOGROID pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (6.2s)
Sep 11 19:04:32 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:32,958 main INFO screen $CAJUN pass=0 dev=0.86 ins=0.0 pro=4 1a=False 1b=False 2=False (5.6s)
Sep 11 19:04:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:04:37,135 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:04:37 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T17:56:40Z
--- update 2026-09-11T18:01:40Z
--- update 2026-09-11T18:06:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: f4240d03c1404a3aa0fe2959269b0656
analyses gestart (8213ec5e675e)
--- update 2026-09-11T18:11:40Z
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
