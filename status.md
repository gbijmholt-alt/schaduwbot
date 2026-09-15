# Schaduwbot status

- tijd: 2026-09-15 00:38:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 10 hours, 51 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.6G/38G | geheugen: 2232/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 151470, "tokens_in_memory": 10147, "msgs": 22632737, "trades": 4596597, "creates": 48763, "decode_fail": 401037, "rpc_calls": 129683, "rpc_errors": 13, "sol_usd": 102.63651799063476, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 00:15:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:03,089 main INFO screen Johy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.9s)
Sep 15 00:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:13,823 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.9s)
Sep 15 00:15:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:24,488 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (66.8s)
Sep 15 00:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:18,797 main INFO screen CATLLM pass=0 dev=0.0 ins=18.94 pro=3 1a=False 1b=False 2=False (75.7s)
Sep 15 00:16:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:25,766 main INFO screen MILKSWEENE pass=0 dev=7.44 ins=0.11 pro=21 1a=False 1b=False 2=False (71.9s)
Sep 15 00:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:31,068 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.6s)
Sep 15 00:17:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:13,737 main INFO screen memelord pass=0 dev=0.0 ins=20.54 pro=6 1a=False 1b=False 2=True (54.9s)
Sep 15 00:17:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:22,206 main INFO screen PADAI pass=0 dev=0.0 ins=68.18 pro=20 1a=True 1b=False 2=True (56.4s)
Sep 15 00:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:37,307 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:17:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 00:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:38,774 main INFO screen DRILLVAL pass=0 dev=0.0 ins=20.38 pro=64 1a=False 1b=False 2=True (67.7s)
Sep 15 00:18:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:18:13,273 main INFO screen USGR pass=0 dev=0.26 ins=130.99 pro=1 1a=False 1b=False 2=True (59.5s)
Sep 15 00:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:18:19,945 main INFO screen clarity pass=0 dev=0.0 ins=1.35 pro=67 1a=False 1b=False 2=True (57.7s)
Sep 15 00:18:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:18:37,139 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.4s)
Sep 15 00:19:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:19:33,141 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (79.9s)
Sep 15 00:19:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:19:36,568 main INFO screen nobrainer pass=0 dev=0.0 ins=41.1 pro=63 1a=False 1b=False 2=True (76.6s)
Sep 15 00:19:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:19:44,153 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (67.0s)
Sep 15 00:20:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:20:31,062 main INFO screen DAO pass=0 dev=0.0 ins=47.08 pro=44 1a=False 1b=False 2=True (57.9s)
Sep 15 00:20:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:20:50,264 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (73.7s)
Sep 15 00:20:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:20:58,908 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.8s)
Sep 15 00:21:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:21:48,593 main INFO screen $BABYCAT pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (77.5s)
Sep 15 00:21:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:21:56,501 main INFO screen Dog pass=0 dev=0.0 ins=20.43 pro=3 1a=False 1b=False 2=True (66.2s)
Sep 15 00:22:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:22:03,589 main INFO screen HEEHAW2.0 pass=0 dev=3.31 ins=23.74 pro=14 1a=True 1b=False 2=True (64.7s)
Sep 15 00:22:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:22:43,988 main INFO screen MeekMill pass=0 dev=0.0 ins=26.83 pro=19 1a=False 1b=False 2=True (55.4s)
Sep 15 00:22:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:22:47,741 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:22:47 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:23:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:23:08,070 main INFO screen nobrainer pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (71.6s)
Sep 15 00:23:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:23:13,874 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (70.3s)
Sep 15 00:23:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:23:43,372 main INFO screen SpaceX pass=0 dev=0.0 ins=175.46 pro=0 1a=False 1b=False 2=True (59.4s)
Sep 15 00:24:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:24:24,857 main INFO screen psyop pass=0 dev=0.0 ins=46.83 pro=78 1a=False 1b=False 2=True (76.8s)
Sep 15 00:24:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:24:31,890 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (78.0s)
Sep 15 00:24:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:24:40,828 main INFO screen BULLBIKE pass=0 dev=0.0 ins=78.96 pro=5 1a=False 1b=True 2=True (57.5s)
Sep 15 00:25:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:25:22,219 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 15 00:25:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:25:27,812 main INFO screen DRAIN pass=0 dev=0.0 ins=0.69 pro=14 1a=False 1b=False 2=False (55.9s)
Sep 15 00:25:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:25:55,263 main INFO screen EULER pass=0 dev=0.0 ins=9.32 pro=3 1a=False 1b=False 2=False (74.4s)
Sep 15 00:26:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:26:21,681 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (59.5s)
Sep 15 00:26:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:26:29,272 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 15 00:26:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:26:49,921 main INFO screen Dogcoin pass=0 dev=0.0 ins=23.58 pro=8 1a=False 1b=False 2=True (54.7s)
Sep 15 00:27:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:27:34,967 main INFO screen INTERN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.3s)
Sep 15 00:27:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:27:36,250 main INFO screen mike dyson pass=0 dev=0.0 ins=0.2 pro=63 1a=False 1b=False 2=True (67.0s)
Sep 15 00:27:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:27:47,786 main INFO screen TRASH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.9s)
Sep 15 00:28:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:28:03,779 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:28:03 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:28:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:28:45,012 main INFO screen Shibabull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.0s)
Sep 15 00:28:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:28:47,181 main INFO screen Dogcoin pass=0 dev=0.0 ins=64.46 pro=26 1a=True 1b=False 2=True (70.9s)
Sep 15 00:28:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:28:49,646 main INFO screen shitcoin pass=0 dev=0.0 ins=19.68 pro=5 1a=False 1b=False 2=True (61.9s)
Sep 15 00:29:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:29:46,085 main INFO screen Gcoin-1  pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (58.9s)
Sep 15 00:29:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:29:47,248 main INFO screen CATE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (57.6s)
Sep 15 00:29:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:29:47,593 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.6s)
Sep 15 00:29:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:29:49,992 aiohttp.access INFO 172.235.41.110 [15/Sep/2026:00:29:49 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 15 00:30:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:30:56,485 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.9s)
Sep 15 00:30:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:30:58,191 main INFO screen CAY pass=0 dev=0.0 ins=18.14 pro=5 1a=False 1b=False 2=False (70.9s)
Sep 15 00:30:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:30:59,137 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.0s)
Sep 15 00:32:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:32:01,726 main INFO screen TIRE pass=0 dev=0.0 ins=33.98 pro=65 1a=False 1b=False 2=True (65.2s)
Sep 15 00:32:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:32:09,386 main INFO screen RONALDOG pass=0 dev=0.0 ins=20.68 pro=4 1a=False 1b=False 2=False (71.2s)
Sep 15 00:32:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:32:10,483 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (71.3s)
Sep 15 00:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:13,591 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:33:13 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:13,810 main INFO screen NUT pass=0 dev=0.0 ins=36.89 pro=72 1a=False 1b=False 2=True (72.1s)
Sep 15 00:33:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:24,065 main INFO screen MALONE pass=0 dev=0.0 ins=0.06 pro=47 1a=False 1b=False 2=False (74.7s)
Sep 15 00:33:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:33:25,086 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.6s)
Sep 15 00:34:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:14,000 main INFO screen fropy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.2s)
Sep 15 00:34:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:18,691 main INFO screen INTIUITION pass=0 dev=0.0 ins=23.58 pro=8 1a=False 1b=False 2=True (53.6s)
Sep 15 00:34:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:34:27,981 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.9s)
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:35:23,679 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 00:35:23 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 00:36:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:04,064 main INFO screen Clam pass=0 dev=0.0 ins=54.57 pro=72 1a=False 1b=False 2=True (110.1s)
Sep 15 00:36:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:25,775 main INFO screen DFC pass=0 dev=0.0 ins=19.61 pro=1 1a=False 1b=False 2=False (117.8s)
Sep 15 00:36:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:36:30,500 main INFO screen nobrain pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (131.8s)
Sep 15 00:37:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:12,016 main INFO screen werld pass=0 dev=0.0 ins=20.89 pro=44 1a=False 1b=False 2=True (68.0s)
Sep 15 00:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:24,863 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.1s)
Sep 15 00:37:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:37:44,823 main INFO screen LSTP pass=0 dev=0.16 ins=0.0 pro=70 1a=False 1b=False 2=False (74.3s)
Sep 15 00:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:10,770 main INFO screen CHARGE pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (58.8s)
Sep 15 00:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:17,016 main INFO screen INTIUITION pass=0 dev=0.0 ins=19.47 pro=3 1a=False 1b=False 2=False (52.2s)
Sep 15 00:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:38:37,675 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:38:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T23:09:27Z
--- update 2026-09-14T23:14:36Z
--- update 2026-09-14T23:19:55Z
--- update 2026-09-14T23:24:58Z
--- update 2026-09-14T23:30:00Z
--- update 2026-09-14T23:35:20Z
--- update 2026-09-14T23:40:36Z
--- update 2026-09-14T23:46:20Z
Running as unit: schaduwbot-wallets.service; invocation ID: dc6a5a650126498b923bda7a46c6b0de
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T23:51:32Z
--- update 2026-09-14T23:56:36Z
--- update 2026-09-15T00:01:52Z
--- update 2026-09-15T00:07:23Z
--- update 2026-09-15T00:12:34Z
--- update 2026-09-15T00:17:36Z
--- update 2026-09-15T00:22:46Z
--- update 2026-09-15T00:28:02Z
--- update 2026-09-15T00:33:12Z
--- update 2026-09-15T00:38:36Z
```

## Analyses (laatste 25 regels)
```
inactive
00:29:52   38000 tokens, 3688000 trades, 442370 posities (248s)
00:30:05   40000 tokens, 3882064 trades, 469159 posities (261s)
00:30:19   42000 tokens, 4065709 trades, 486855 posities (274s)
00:30:33   44000 tokens, 4245991 trades, 510852 posities (289s)
00:30:47   46000 tokens, 4420440 trades, 531350 posities (303s)
00:31:02   48000 tokens, 4598102 trades, 550760 posities (318s)
00:31:19   50000 tokens, 4799757 trades, 574399 posities (335s)
00:31:36   52000 tokens, 5016691 trades, 603626 posities (352s)
00:31:52   54000 tokens, 5200426 trades, 625224 posities (367s)
00:32:06   56000 tokens, 5365533 trades, 644406 posities (382s)
00:32:23   58000 tokens, 5562944 trades, 669075 posities (399s)
00:32:39   60000 tokens, 5746516 trades, 689739 posities (415s)
00:32:57   62000 tokens, 5955952 trades, 716730 posities (433s)
00:33:13   64000 tokens, 6142789 trades, 744367 posities (449s)
00:33:30   66000 tokens, 6356758 trades, 771423 posities (466s)
00:33:43   68000 tokens, 6541957 trades, 795263 posities (479s)
00:33:56   70000 tokens, 6731219 trades, 818210 posities (492s)
00:34:10   72000 tokens, 6922572 trades, 843202 posities (506s)
00:34:25   74000 tokens, 7133262 trades, 878980 posities (521s)
00:34:30 posities: 885811 uit 7196469 trades (529s)
00:34:43 211069 wallets gerekend
00:34:43 geluk-toets
00:35:19 persistentie
00:35:22 kopieer-simulatie
00:37:42 klaar in 721s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
23:20:02 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=32 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:20:02 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 7/41/171 | al gemeten: 301
23:25:07 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=35 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:25:07 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/166 | al gemeten: 304
23:30:16 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=39 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:30:16 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/170 | al gemeten: 309
23:35:28 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=42 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:35:29 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 12/42/171 | al gemeten: 312
23:40:44 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=44 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:40:45 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/38/168 | al gemeten: 315
23:46:54 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=46 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:46:55 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 9/38/167 | al gemeten: 318
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
