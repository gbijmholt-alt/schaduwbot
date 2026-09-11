# Schaduwbot status

- tijd: 2026-09-11 19:19:52 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 5 hours, 32 minutes
- bot-service: active
- code-versie: a16a395
- schijf: 2.8G/38G | geheugen: 585/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 2494, "tokens_in_memory": 1037, "msgs": 366647, "trades": 96470, "creates": 1037, "decode_fail": 6486, "rpc_calls": 4021, "rpc_errors": 112, "sol_usd": 101.13009015961106, "open_positions": 61, "log_all_trades": true}
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
Sep 11 19:11:17 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:11:17,134 main INFO screen $METH pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (9.4s)
Sep 11 19:11:42 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:11:42,473 main INFO screen $REGRET pass=0 dev=0.34 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 19:11:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:11:47,153 main INFO screen $REGRET pass=0 dev=17.7 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 11 19:12:09 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:09,534 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:12:11 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:11,798 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:12:14 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:14,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:12:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:16,874 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:12:30 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:30,430 main INFO screen STONKER pass=0 dev=0.26 ins=0.03 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 19:12:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:34,531 main INFO screen ALL pass=0 dev=0.0 ins=42.2 pro=65 1a=False 1b=True 2=True (25.1s)
Sep 11 19:12:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:38,086 main INFO screen callout pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 11 19:12:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:38,347 main INFO screen HENTINU pass=0 dev=0.0 ins=43.42 pro=46 1a=False 1b=False 2=True (26.6s)
Sep 11 19:12:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:52,650 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:12:57 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:12:57,723 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:13:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:02,989 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:13:08 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:08,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:13:15 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:15,026 main INFO screen CHEDDAR pass=0 dev=0.07 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 11 19:13:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:16,813 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (24.3s)
Sep 11 19:13:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:23,088 main INFO screen Bananaut pass=0 dev=0.0 ins=20.28 pro=13 1a=False 1b=False 2=False (6.9s)
Sep 11 19:13:23 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:23,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:13:27 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:27,737 main INFO screen LLAMAFONE pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 19:13:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:29,997 main INFO screen JUGGCAT pass=0 dev=0.0 ins=77.39 pro=8 1a=False 1b=True 2=True (27.1s)
Sep 11 19:13:37 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:37,913 main INFO screen $REGRET pass=0 dev=26.58 ins=0.0 pro=5 1a=False 1b=False 2=False (14.8s)
Sep 11 19:13:39 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:39,686 main INFO screen APPLECAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (11.9s)
Sep 11 19:13:45 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:45,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:13:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:13:52,935 main INFO screen meme pass=0 dev=0.0 ins=7.15 pro=49 1a=False 1b=False 2=True (7.5s)
Sep 11 19:14:04 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:04,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:06,722 main INFO screen STONKER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 11 19:14:09 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:09,117 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:19 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:19,034 main INFO screen aicat pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=False (15.0s)
Sep 11 19:14:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:21,995 main INFO screen Bulls pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (13.0s)
Sep 11 19:14:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:26,827 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:31 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:31,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:43,641 main INFO screen whatif pass=0 dev=0.17 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 19:14:44 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:44,074 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:46 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:46,925 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:14:46 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
Sep 11 19:14:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:51,138 main INFO screen 911 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.4s)
Sep 11 19:14:51 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:51,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:53 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:53,106 main INFO screen $REGRET pass=0 dev=15.17 ins=0.0 pro=6 1a=False 1b=False 2=False (11.0s)
Sep 11 19:14:56 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:56,678 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:14:58 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:14:58,490 main INFO screen DFV pass=0 dev=0.0 ins=16.96 pro=46 1a=False 1b=False 2=True (14.8s)
Sep 11 19:15:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:03,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:06 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:06,271 main INFO screen SCRVAN pass=0 dev=0.44 ins=0.0 pro=3 1a=False 1b=False 2=False (9.2s)
Sep 11 19:15:14 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:14,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:16,207 main INFO screen SEPE pass=1 dev=0.0 ins=19.71 pro=16 1a=False 1b=False 2=False (12.4s)
Sep 11 19:15:16 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:16,671 main INFO screen PFA pass=0 dev=0.0 ins=42.92 pro=5 1a=False 1b=True 2=True (25.5s)
Sep 11 19:15:19 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:19,658 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:21,723 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:26,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:34 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:34,186 main INFO screen SSM pass=0 dev=0.0 ins=27.75 pro=66 1a=False 1b=False 2=True (19.7s)
Sep 11 19:15:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:38,164 main INFO screen CAINE pass=1 dev=0.0 ins=7.99 pro=50 1a=False 1b=False 2=False (3.4s)
Sep 11 19:15:45 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:45,250 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:15:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:47,034 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (25.3s)
Sep 11 19:15:50 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:15:50,310 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:16:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:02,578 main INFO screen BPCATE pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=False (10.4s)
Sep 11 19:16:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:07,034 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 19:16:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:12,635 main INFO screen PABLO pass=0 dev=9.75 ins=0.0 pro=28 1a=False 1b=False 2=False (5.6s)
Sep 11 19:16:12 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:12,715 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:16:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:13,659 main INFO screen WTML pass=0 dev=0.35 ins=0.0 pro=5 1a=False 1b=False 2=False (11.1s)
Sep 11 19:16:13 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:13,714 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.6s)
Sep 11 19:16:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:26,959 main INFO screen Pepusky pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (14.3s)
Sep 11 19:16:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:36,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:16:41 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:16:41,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:17:01 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:01,327 main INFO screen sFOMO pass=0 dev=0.0 ins=43.05 pro=43 1a=False 1b=False 2=True (24.8s)
Sep 11 19:17:02 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:02,508 main INFO screen $BWC pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (10.7s)
Sep 11 19:17:21 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:21,890 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:17:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:26,964 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:17:38 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:38,877 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:17:43 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:43,950 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:17:46 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:46,188 main INFO screen ANSEM pass=0 dev=0.0 ins=17.95 pro=27 1a=False 1b=False 2=True (24.4s)
Sep 11 19:17:47 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:17:47,131 main INFO screen PUMPY pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 11 19:18:03 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:18:03,084 main INFO screen $REGRET pass=0 dev=42.6 ins=0.0 pro=5 1a=False 1b=False 2=False (24.3s)
Sep 11 19:18:05 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:18:05,587 main INFO screen shizuku pass=0 dev=12.62 ins=0.0 pro=35 1a=False 1b=False 2=False (3.7s)
Sep 11 19:18:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:18:52,250 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:19:05 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:05,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:19:07 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:07,944 main INFO screen Pippo pass=0 dev=0.0 ins=16.39 pro=59 1a=False 1b=False 2=True (15.8s)
Sep 11 19:19:19 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:19,528 main INFO screen pixelP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (14.1s)
Sep 11 19:19:26 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:26,190 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 19:19:29 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:29,386 main INFO screen baton pass=0 dev=0.0 ins=0.35 pro=5 1a=False 1b=False 2=False (9.6s)
Sep 11 19:19:36 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:36,873 main INFO screen $CHUMP pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (10.8s)
Sep 11 19:19:52 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 19:19:52,216 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:19:19:52 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-11T19:09:39Z
--- update 2026-09-11T19:14:45Z
--- update 2026-09-11T19:19:51Z
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
