# Schaduwbot status

- tijd: 2026-09-12 07:41:19 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 17 hours, 54 minutes
- bot-service: active
- code-versie: 5e1921e
- schijf: 3.4G/38G | geheugen: 562/3814 MB

## Health
```json
{"ok": false, "last_event_age_s": null, "uptime_s": 0}
```

## Laatste rapport
```

Gelogde schaduwtrades: **43218**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 7443 | 1221 | 6 | 1221 | 93 | 2195 | 6662 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 503 | 16% | 2.0% | +44.1% | -16.6% | -6.93% | 100% |
| dip35_V1_gescreend_fail | 4068 | 27% | 3.8% | +45.6% | -25.9% | -6.61% | 100% |
| dip35_V1_alle | 4992 | 26% | 3.9% | +44.8% | -25.2% | -6.85% | 100% |
| dip35_V2_gescreend_pass | 500 | 21% | 2.8% | +43.1% | -20.9% | -7.42% | 100% |
| dip35_V2_gescreend_fail | 4105 | 25% | 4.3% | +56.3% | -27.9% | -6.88% | 100% |
| dip35_V2_alle | 4959 | 24% | 4.5% | +53.8% | -27.6% | -7.63% | 100% |
| dip35_V3_gescreend_pass | 502 | 8% | 3.2% | +297.3% | -22.3% | +4.45% | 100% |
| dip35_V3_gescreend_fail | 4189 | 14% | 5.9% | +115.1% | -29.6% | -10.10% | 100% |
| dip35_V3_alle | 5006 | 13% | 5.9% | +119.7% | -29.2% | -9.54% | 100% |
| dip40_V1_gescreend_pass | 473 | 14% | 2.1% | +46.7% | -15.9% | -7.07% | 100% |
| dip40_V1_gescreend_fail | 3998 | 26% | 3.7% | +47.2% | -25.7% | -6.53% | 100% |
| dip40_V1_alle | 4797 | 25% | 3.8% | +47.3% | -25.0% | -6.71% | 100% |
| dip40_V2_gescreend_pass | 471 | 17% | 2.5% | +46.2% | -19.8% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 4014 | 25% | 4.2% | +55.9% | -27.9% | -6.96% | 100% |
| dip40_V2_alle | 4759 | 24% | 4.3% | +54.3% | -27.4% | -7.77% | 100% |
| dip40_V3_gescreend_pass | 474 | 8% | 2.7% | +294.2% | -21.1% | +2.87% | 100% |
| dip40_V3_gescreend_fail | 4091 | 13% | 5.6% | +112.2% | -29.4% | -10.69% | 100% |
| dip40_V3_alle | 4808 | 13% | 5.6% | +117.8% | -28.9% | -10.15% | 100% |
| dip45_V1_gescreend_pass | 455 | 15% | 2.0% | +48.7% | -15.8% | -6.28% | 100% |
| dip45_V1_gescreend_fail | 3917 | 27% | 3.3% | +48.4% | -25.4% | -5.19% | 100% |
| dip45_V1_alle | 4644 | 26% | 3.4% | +48.7% | -24.7% | -5.52% | 100% |
| dip45_V2_gescreend_pass | 452 | 19% | 2.4% | +43.3% | -19.8% | -7.90% | 100% |
| dip45_V2_gescreend_fail | 3926 | 25% | 3.8% | +58.6% | -27.4% | -5.71% | 100% |
| dip45_V2_alle | 4606 | 24% | 3.9% | +57.3% | -27.0% | -6.43% | 100% |
| dip45_V3_gescreend_pass | 455 | 7% | 2.4% | +352.6% | -20.5% | +6.56% | 100% |
| dip45_V3_gescreend_fail | 3990 | 14% | 5.4% | +117.2% | -28.9% | -8.58% | 100% |
| dip45_V3_alle | 4647 | 13% | 5.3% | +125.9% | -28.4% | -7.90% | 100% |

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
| met_xlink | 3307 | 13% | 3.2% | -10.31% | 100% |
| zonder_xlink | 978 | 18% | 0.0% | +20.19% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 07:21:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:21:42,389 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:07:21:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 07:22:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:22:27,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:22:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:22:39,700 main INFO screen Pepegger pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (12.8s)
Sep 12 07:23:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:46,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:23:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:52,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:23:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:56,660 main INFO screen TCAT pass=0 dev=1.0 ins=24.36 pro=63 1a=False 1b=False 2=True (3.8s)
Sep 12 07:24:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:09,548 main INFO screen TCAT pass=0 dev=0.0 ins=20.99 pro=25 1a=False 1b=False 2=False (22.7s)
Sep 12 07:24:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:27,519 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:32,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:43,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:52,146 main INFO screen GEMEOW pass=0 dev=0.18 ins=79.13 pro=7 1a=False 1b=True 2=True (24.7s)
Sep 12 07:24:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:57,413 main INFO screen PUMP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (13.7s)
Sep 12 07:25:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:25:37,153 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:25:37 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 07:26:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:08,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:26:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:16,323 main INFO screen TCAT pass=0 dev=1.0 ins=17.15 pro=46 1a=False 1b=False 2=True (8.0s)
Sep 12 07:26:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:31,736 main INFO screen GPU pass=0 dev=0.0 ins=13.71 pro=27 1a=False 1b=False 2=True (9.0s)
Sep 12 07:26:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:47,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:59,942 main INFO screen MBST pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (12.9s)
Sep 12 07:27:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:27:30,981 main INFO screen OXYGEN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 12 07:28:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:28:58,604 main INFO screen JeJe pass=0 dev=0.24 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 12 07:29:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:29:24,036 main INFO screen Graduate pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 07:30:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:01,971 main INFO screen INU pass=0 dev=0.0 ins=20.21 pro=59 1a=False 1b=False 2=True (3.2s)
Sep 12 07:30:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:33,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,750 main INFO screen PLINE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 12 07:30:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:43,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:48,490 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:52,531 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:30:52 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:30:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:57,348 main INFO screen ANONKNIGHT pass=0 dev=0.18 ins=79.13 pro=9 1a=True 1b=True 2=True (24.5s)
Sep 12 07:31:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:10,576 main INFO screen ANZATOK pass=0 dev=0.0 ins=3.2 pro=49 1a=False 1b=False 2=True (27.2s)
Sep 12 07:31:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:52,392 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 12 07:31:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:54,550 main INFO screen DeDe pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 12 07:31:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:31:58,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:00,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:04,040 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:32:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:07,257 main INFO screen Polarbear pass=0 dev=0.0 ins=18.31 pro=32 1a=False 1b=False 2=True (7.3s)
Sep 12 07:32:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:32:22,907 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (24.0s)
Sep 12 07:33:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:19,427 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:24,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:29,763 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:33,230 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:34,831 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:38,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:33:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:39,009 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.7s)
Sep 12 07:33:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:42,183 main INFO screen DeFi pass=0 dev=0.03 ins=25.33 pro=46 1a=False 1b=False 2=True (3.2s)
Sep 12 07:33:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:48,784 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.1s)
Sep 12 07:33:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:33:53,096 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 07:34:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:34:11,951 main INFO screen NOTBAD pass=0 dev=0.62 ins=0.0 pro=7 1a=False 1b=False 2=False (3.5s)
Sep 12 07:34:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:34:37,136 main INFO screen $speed pass=0 dev=0.25 ins=0.0 pro=5 1a=False 1b=False 2=False (2.8s)
Sep 12 07:35:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:02,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:08,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:09,993 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (3.7s)
Sep 12 07:35:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:22,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:22,806 main INFO screen Starbucks pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 12 07:35:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:27,619 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:35,614 main INFO screen . pass=0 dev=0.49 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 12 07:35:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:42,209 main INFO screen RUFUS pass=0 dev=0.0 ins=14.03 pro=31 1a=False 1b=False 2=True (19.7s)
Sep 12 07:35:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:54,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:35:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:59,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:05,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:10,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:13,717 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:36:13 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:36:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:14,421 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 07:36:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:23,677 main INFO screen FLYPAIN pass=0 dev=0.04 ins=79.27 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 12 07:36:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:49,194 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:54,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:37:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:07,826 main INFO screen RUFUS pass=0 dev=0.0 ins=21.88 pro=30 1a=False 1b=True 2=True (18.7s)
Sep 12 07:37:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:10,248 main INFO screen $speed pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 12 07:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:05,811 main INFO screen HORACE pass=0 dev=0.0 ins=18.12 pro=24 1a=False 1b=False 2=True (2.1s)
Sep 12 07:39:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:10,050 main INFO screen Fox pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 12 07:40:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:40:02,878 main INFO screen GYROS pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 12 07:41:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:14,093 main INFO screen WOTF pass=0 dev=98.49 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 12 07:41:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:15,023 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 1h 22min 30.038s CPU time over 12h 1min 10.049s wall clock time, 1.1G memory peak.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,143 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,167 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:41:19 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T06:29:29Z
--- update 2026-09-12T06:34:34Z
--- update 2026-09-12T06:39:34Z
--- update 2026-09-12T06:44:35Z
--- update 2026-09-12T06:49:36Z
--- update 2026-09-12T06:54:39Z
--- update 2026-09-12T06:59:44Z
--- update 2026-09-12T07:04:47Z
--- update 2026-09-12T07:09:50Z
--- update 2026-09-12T07:14:57Z
--- update 2026-09-12T07:20:13Z
--- update 2026-09-12T07:25:36Z
--- update 2026-09-12T07:30:51Z
--- update 2026-09-12T07:36:12Z
--- update 2026-09-12T07:41:14Z
nieuwe code: 5e1921e
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 4ef46f4f0356436685dca4ab3e2f1d40
analyses gestart (e6fa7044d08b)
```

## Analyses (laatste 25 regels)
```
active
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
07:41:18   signaalversie -> signaal-v2-uitstappen: 13161 signalen worden opnieuw berekend
07:41:19 26121 tokens sinds start volledige logging, waarvan 5134 met een gat door herstart
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
