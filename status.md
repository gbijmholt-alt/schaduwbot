# Schaduwbot status

- tijd: 2026-09-15 02:32:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 12 hours, 45 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.7G/38G | geheugen: 2284/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 158286, "tokens_in_memory": 9446, "msgs": 24272039, "trades": 4835754, "creates": 51567, "decode_fail": 415921, "rpc_calls": 136384, "rpc_errors": 13, "sol_usd": 102.28634844340515, "open_positions": 22, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 5572 | 625 | 10 | 635 | 107 | 1125 | 3395 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 617 | 17% | 1.6% | +43.2% | -15.9% | -5.99% | 100% |
| dip35_V1_gescreend_fail | 4728 | 27% | 4.0% | +45.1% | -25.9% | -6.78% | 100% |
| dip35_V1_alle | 6456 | 26% | 4.0% | +44.4% | -25.5% | -7.05% | 100% |
| dip35_V2_gescreend_pass | 616 | 23% | 2.3% | +40.7% | -20.1% | -6.31% | 100% |
| dip35_V2_gescreend_fail | 4810 | 25% | 4.4% | +54.6% | -27.9% | -7.05% | 100% |
| dip35_V2_alle | 6416 | 25% | 4.5% | +52.3% | -27.8% | -7.95% | 100% |
| dip35_V3_gescreend_pass | 625 | 9% | 3.2% | +253.7% | -21.9% | +3.65% | 100% |
| dip35_V3_gescreend_fail | 4943 | 14% | 6.1% | +119.4% | -29.6% | -9.19% | 100% |
| dip35_V3_alle | 6472 | 13% | 6.1% | +116.5% | -29.4% | -10.33% | 100% |
| dip40_V1_gescreend_pass | 588 | 15% | 1.7% | +43.7% | -15.4% | -6.70% | 100% |
| dip40_V1_gescreend_fail | 4653 | 26% | 3.9% | +46.6% | -25.7% | -6.64% | 100% |
| dip40_V1_alle | 6210 | 26% | 3.9% | +46.4% | -25.3% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 589 | 18% | 2.0% | +43.0% | -19.4% | -7.95% | 100% |
| dip40_V2_gescreend_fail | 4712 | 25% | 4.3% | +54.6% | -27.8% | -6.97% | 100% |
| dip40_V2_alle | 6164 | 24% | 4.4% | +53.3% | -27.6% | -7.94% | 100% |
| dip40_V3_gescreend_pass | 598 | 8% | 2.8% | +251.7% | -21.0% | +1.83% | 100% |
| dip40_V3_gescreend_fail | 4828 | 13% | 5.8% | +115.5% | -29.3% | -9.97% | 100% |
| dip40_V3_alle | 6220 | 13% | 5.9% | +113.2% | -29.1% | -11.05% | 100% |
| dip45_V1_gescreend_pass | 568 | 15% | 1.6% | +46.7% | -15.1% | -5.90% | 100% |
| dip45_V1_gescreend_fail | 4570 | 27% | 3.6% | +48.0% | -25.5% | -5.53% | 100% |
| dip45_V1_alle | 6003 | 26% | 3.6% | +48.1% | -25.1% | -6.06% | 100% |
| dip45_V2_gescreend_pass | 567 | 19% | 1.9% | +42.4% | -19.4% | -7.86% | 100% |
| dip45_V2_gescreend_fail | 4621 | 25% | 4.0% | +58.3% | -27.5% | -5.83% | 100% |
| dip45_V2_alle | 5957 | 24% | 4.1% | +56.9% | -27.3% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 578 | 8% | 2.4% | +276.6% | -20.3% | +3.82% | 100% |
| dip45_V3_gescreend_fail | 4723 | 14% | 5.4% | +121.9% | -28.9% | -7.66% | 100% |
| dip45_V3_alle | 6006 | 13% | 5.5% | +121.6% | -28.7% | -8.97% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 488 | 16% | 5.3% | -8.21% | -11.3% tot -5.1% | -14.3% | – | 100% |
| per_token_zonder_xlink | 154 | 23% | 0.0% | +18.49% | -8.6% tot +45.6% | -13.1% | 119% | 58% |
| gepoold_met_xlink | 4066 | 14% | 2.9% | -9.32% | -10.5% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1280 | 18% | 0.0% | +15.22% | -0.1% tot +30.5% | -14.3% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 15 02:04:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:04:45,747 main INFO screen Carbonoid pass=0 dev=0.0 ins=25.32 pro=78 1a=False 1b=False 2=True (73.3s)
Sep 15 02:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:22,147 main INFO screen Ferrari pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (75.4s)
Sep 15 02:05:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:26,562 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.6s)
Sep 15 02:05:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:41,105 aiohttp.access INFO 172.235.40.131 [15/Sep/2026:02:05:41 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 15 02:05:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:05:43,175 main INFO screen DRILLNYE pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (57.4s)
Sep 15 02:06:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:35,194 main INFO screen FAR pass=0 dev=0.0 ins=18.88 pro=30 1a=False 1b=False 2=False (68.6s)
Sep 15 02:06:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:36,919 main INFO screen TWIN pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=False (74.8s)
Sep 15 02:06:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:44,162 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:06:44 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:06:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:06:48,032 main INFO screen ⬆️ pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.9s)
Sep 15 02:07:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:07:55,746 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (78.8s)
Sep 15 02:07:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:07:55,905 main INFO screen GOTHDOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (80.7s)
Sep 15 02:07:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:07:56,946 main INFO screen FOBE pass=0 dev=0.0 ins=26.77 pro=64 1a=False 1b=False 2=True (68.9s)
Sep 15 02:09:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:09:01,855 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (65.9s)
Sep 15 02:09:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:09:06,466 main INFO screen open pass=0 dev=0.0 ins=25.09 pro=67 1a=False 1b=False 2=True (69.5s)
Sep 15 02:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:09:13,359 main INFO screen Samsung pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (77.6s)
Sep 15 02:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:09:58,607 main INFO screen OTF pass=0 dev=0.0 ins=34.05 pro=10 1a=False 1b=False 2=True (56.8s)
Sep 15 02:09:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:09:59,027 main INFO screen FRONTIER pass=0 dev=0.0 ins=34.02 pro=8 1a=False 1b=False 2=True (52.6s)
Sep 15 02:10:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:10:06,727 main INFO screen POOHOUSE pass=0 dev=0.0 ins=34.02 pro=6 1a=False 1b=False 2=True (53.4s)
Sep 15 02:10:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:10:54,632 main INFO screen open pass=0 dev=0.0 ins=28.67 pro=16 1a=False 1b=False 2=True (55.6s)
Sep 15 02:11:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:11:13,672 main INFO screen MACHINE pass=0 dev=0.0 ins=14.22 pro=59 1a=False 1b=False 2=True (66.9s)
Sep 15 02:11:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:11:18,292 main INFO screen MCAT pass=0 dev=0.0 ins=24.66 pro=75 1a=False 1b=False 2=True (79.7s)
Sep 15 02:11:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:11:50,704 main INFO screen HYBRID pass=0 dev=0.0 ins=26.83 pro=70 1a=False 1b=False 2=True (56.1s)
Sep 15 02:11:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:11:50,991 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:11:50 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:12:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:12:16,367 main INFO screen BIKE PEPE pass=0 dev=0.0 ins=78.66 pro=12 1a=False 1b=True 2=True (62.7s)
Sep 15 02:12:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:12:21,215 main INFO screen faucat pass=0 dev=0.0 ins=36.37 pro=69 1a=False 1b=False 2=True (62.9s)
Sep 15 02:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:12:49,941 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.2s)
Sep 15 02:13:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:13:09,489 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (53.1s)
Sep 15 02:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:13:11,219 main INFO screen LOS pass=0 dev=0.0 ins=30.23 pro=48 1a=False 1b=False 2=True (50.0s)
Sep 15 02:13:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:13:57,686 main INFO screen $WAGE pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (67.7s)
Sep 15 02:14:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:14:17,169 main INFO screen RA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.9s)
Sep 15 02:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:14:18,481 main INFO screen JUDE pass=0 dev=0.0 ins=11.01 pro=71 1a=False 1b=False 2=True (69.0s)
Sep 15 02:15:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:01,651 main INFO screen Clasiclux pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.0s)
Sep 15 02:15:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:31,075 main INFO screen FART pass=0 dev=1.05 ins=0.0 pro=4 1a=False 1b=False 2=False (72.6s)
Sep 15 02:15:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:15:35,557 main INFO screen SPAMCAT pass=0 dev=0.0 ins=28.42 pro=60 1a=False 1b=False 2=True (78.4s)
Sep 15 02:16:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:03,749 main INFO screen MEEK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.1s)
Sep 15 02:16:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:45,583 main INFO screen ISHOWSPEED pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.0s)
Sep 15 02:16:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:16:52,540 main INFO screen Bob pass=0 dev=0.0 ins=24.04 pro=68 1a=False 1b=False 2=True (81.5s)
Sep 15 02:17:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:17:07,563 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:17:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:17:15,191 main INFO screen WOJAKTYSON pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (71.4s)
Sep 15 02:18:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:10,801 main INFO screen BUFF pass=0 dev=0.0 ins=9.29 pro=60 1a=False 1b=False 2=False (85.2s)
Sep 15 02:18:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:16,116 main INFO screen NETO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (83.6s)
Sep 15 02:18:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:18:24,672 main INFO screen bundloor pass=0 dev=0.0 ins=21.1 pro=49 1a=False 1b=False 2=True (69.5s)
Sep 15 02:19:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:34,522 main INFO screen Jizz pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (78.4s)
Sep 15 02:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:38,806 main INFO screen BEARISH pass=0 dev=0.21 ins=0.0 pro=15 1a=False 1b=False 2=False (88.0s)
Sep 15 02:19:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:19:40,510 main INFO screen Bridge402 pass=0 dev=39.93 ins=0.0 pro=60 1a=False 1b=False 2=True (75.8s)
Sep 15 02:20:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:32,480 main INFO screen Rolex pass=0 dev=0.0 ins=175.36 pro=0 1a=False 1b=False 2=True (58.0s)
Sep 15 02:20:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:43,516 main INFO screen Museum pass=0 dev=0.0 ins=33.47 pro=27 1a=False 1b=False 2=True (63.0s)
Sep 15 02:20:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:20:49,004 main INFO screen SAN pass=0 dev=0.0 ins=11.61 pro=27 1a=False 1b=False 2=True (70.2s)
Sep 15 02:21:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:21:39,124 main INFO screen pumpoids pass=0 dev=0.0 ins=17.11 pro=27 1a=False 1b=False 2=True (55.6s)
Sep 15 02:21:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:21:50,849 main INFO screen JUDE pass=0 dev=0.0 ins=19.49 pro=57 1a=False 1b=False 2=False (78.4s)
Sep 15 02:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:06,930 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (77.9s)
Sep 15 02:22:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:08,135 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:22:08 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 02:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:31,222 main INFO screen Bridge402 pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (52.1s)
Sep 15 02:22:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:22:58,255 main INFO screen AI pass=0 dev=0.0 ins=26.01 pro=60 1a=False 1b=False 2=True (67.4s)
Sep 15 02:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:23:17,469 main INFO screen INSTAR pass=0 dev=5.0 ins=4.24 pro=51 1a=False 1b=False 2=True (70.5s)
Sep 15 02:23:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:23:45,678 main INFO screen DERP pass=0 dev=0.0 ins=46.02 pro=9 1a=False 1b=False 2=True (74.5s)
Sep 15 02:24:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:12,981 main INFO screen GS pass=0 dev=0.0 ins=23.99 pro=39 1a=False 1b=False 2=True (74.7s)
Sep 15 02:24:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:30,972 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (73.5s)
Sep 15 02:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:24:49,091 main INFO screen DUO pass=0 dev=0.0 ins=31.63 pro=54 1a=False 1b=True 2=True (63.4s)
Sep 15 02:25:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:25:08,435 main INFO screen tiger pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.5s)
Sep 15 02:25:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:25:29,433 main INFO screen cappykidd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 15 02:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:04,549 main INFO screen 天議論 pass=0 dev=0.0 ins=28.96 pro=64 1a=False 1b=False 2=True (75.5s)
Sep 15 02:26:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:19,351 main INFO screen Hedge pass=0 dev=0.0 ins=16.35 pro=30 1a=False 1b=False 2=True (70.9s)
Sep 15 02:26:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:26:34,037 main INFO screen GS pass=0 dev=0.0 ins=40.9 pro=36 1a=False 1b=False 2=True (64.6s)
Sep 15 02:27:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:11,034 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:27:11 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:27:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:20,412 main INFO screen Papoy pass=0 dev=0.0 ins=16.9 pro=44 1a=False 1b=False 2=False (75.9s)
Sep 15 02:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:41,737 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (67.7s)
Sep 15 02:27:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:27:44,243 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (84.9s)
Sep 15 02:28:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:17,051 main INFO screen Lanaroads pass=0 dev=0.0 ins=4.96 pro=45 1a=False 1b=False 2=False (56.6s)
Sep 15 02:28:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:41,991 main INFO screen JUDE pass=0 dev=0.0 ins=12.61 pro=56 1a=False 1b=False 2=True (60.3s)
Sep 15 02:28:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:28:59,378 main INFO screen QUVO pass=0 dev=0.0 ins=18.42 pro=19 1a=False 1b=False 2=True (75.1s)
Sep 15 02:29:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:29:23,595 main INFO screen Q50 coin pass=0 dev=0.04 ins=0.0 pro=4 1a=False 1b=False 2=False (66.5s)
Sep 15 02:29:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:29:45,291 main INFO screen Nbaton pass=0 dev=0.0 ins=21.51 pro=3 1a=False 1b=False 2=False (63.3s)
Sep 15 02:30:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:05,991 main INFO screen WhiteBull pass=0 dev=0.0 ins=56.74 pro=26 1a=False 1b=False 2=True (66.6s)
Sep 15 02:30:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:18,955 main INFO screen PENIS pass=0 dev=0.0 ins=32.69 pro=25 1a=False 1b=False 2=True (55.4s)
Sep 15 02:30:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:30:45,624 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (60.3s)
Sep 15 02:31:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:01,293 main INFO screen JUDE pass=0 dev=0.0 ins=78.96 pro=0 1a=True 1b=True 2=True (55.3s)
Sep 15 02:31:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:10,364 main INFO screen USGR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 15 02:31:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:31:46,799 main INFO screen MEME pass=0 dev=0.0 ins=37.3 pro=67 1a=False 1b=False 2=True (61.2s)
Sep 15 02:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:32:14,146 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:32:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T01:04:36Z
--- update 2026-09-15T01:09:36Z
--- update 2026-09-15T01:15:15Z
--- update 2026-09-15T01:20:32Z
--- update 2026-09-15T01:25:36Z
--- update 2026-09-15T01:30:37Z
--- update 2026-09-15T01:35:39Z
--- update 2026-09-15T01:40:45Z
--- update 2026-09-15T01:46:14Z
--- update 2026-09-15T01:51:16Z
Running as unit: schaduwbot-wallets.service; invocation ID: 198697cd6df2473cb461b6a874faa3b9
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T01:56:31Z
--- update 2026-09-15T02:01:36Z
--- update 2026-09-15T02:06:42Z
--- update 2026-09-15T02:11:49Z
--- update 2026-09-15T02:17:06Z
--- update 2026-09-15T02:22:06Z
--- update 2026-09-15T02:27:10Z
--- update 2026-09-15T02:32:12Z
```

## Analyses (laatste 25 regels)
```
active
01:51:45   ingelezen tot rowid 10315765 (255758 rijen, 255758 bruikbaar)
01:51:47 ingelezen: 255758 nieuwe trades, 255758 bruikbaar (30s)
01:54:40 3000 aankopen van gevolgde wallets geëvalueerd
01:55:31 vroege kopers: 270 voldoen nu, register 480, 346 tokens beoordeeld
01:56:05 grote spelers: saldo van 396 wallets opgehaald
01:56:37 herkomst: 40 posities gekoppeld
01:56:49 klaar in 333s -> /opt/schaduwbot/reports/ledger.md
02:11:15 S1: gezakt — toets n=29059, verkennend n=14656
02:11:15 klaar in 866s -> /opt/schaduwbot/reports/hypotheses.md
02:11:16 probe: 150 transacties ophalen
02:14:34 poolveld: 10 pools bekeken, 0 te gaan -> vastgesteld @43
02:15:46 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
02:15:46 prijsijk: n=91 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
02:15:48 na-migratie: 100 paren te checken
02:17:59 na-migratie: 49 paren, 20 prijzen
02:21:15 gemigreerde koersen: 65 gedaan, 1676 te gaan
02:21:16 klaar (596 rpc-calls, 126 fouten)
02:30:19 klaar in 543s -> /opt/schaduwbot/reports/lotgevallen.md
02:30:40   2000 nieuwe tokens doorgerekend
02:31:17 klaar in 58s: 63926 tokens, 3027 nieuw -> /opt/schaduwbot/reports/video_replay.md
02:31:18 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-12 02:31 UTC
02:31:24 124758 tokens geladen
02:31:38   2000 tokens, 174569 trades, 17216 posities (15s)
02:31:54   4000 tokens, 397218 trades, 51398 posities (30s)
02:32:07   6000 tokens, 588812 trades, 71889 posities (43s)
```

## IJking poolkoers (laatste 12 regels)
```
01:25:42 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=77 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:25:42 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 8/40/164 | al gemeten: 372
01:30:43 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=79 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:30:43 ijk-diagnose: nieuwste migratie 1.8 min oud | migraties 15/60/240 min: 8/39/158 | al gemeten: 374
01:35:51 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=83 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:35:52 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 8/41/158 | al gemeten: 378
01:40:57 ijk: +4 van 4 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=85 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:40:57 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 10/43/158 | al gemeten: 382
01:46:21 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=86 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:46:21 ijk-diagnose: nieuwste migratie 1.5 min oud | migraties 15/60/240 min: 11/45/157 | al gemeten: 385
01:51:50 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=90 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:51:54 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 11/46/159 | al gemeten: 389
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
