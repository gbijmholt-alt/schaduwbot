# Schaduwbot status

- tijd: 2026-09-14 18:40:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 4 hours, 53 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.1G/38G | geheugen: 2154/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 129992, "tokens_in_memory": 9012, "msgs": 17536486, "trades": 3700650, "creates": 38671, "decode_fail": 319882, "rpc_calls": 108513, "rpc_errors": 7, "sol_usd": 103.41721022257694, "open_positions": 84, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 18:21:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:21:14,116 main INFO screen $BROKE pass=0 dev=0.0 ins=0.42 pro=1 1a=False 1b=False 2=False (66.4s)
Sep 14 18:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:21:34,930 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.0s)
Sep 14 18:21:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:21:52,546 main INFO screen DOOYET pass=0 dev=22.76 ins=0.0 pro=8 1a=False 1b=False 2=False (69.4s)
Sep 14 18:22:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:22:09,443 main INFO screen PROFITABLE pass=0 dev=0.0 ins=17.86 pro=38 1a=False 1b=False 2=True (55.3s)
Sep 14 18:22:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:22:32,076 main INFO screen CHONKS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 18:22:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:22:59,125 main INFO screen mattdiamond pass=0 dev=0.0 ins=38.12 pro=31 1a=False 1b=False 2=True (66.6s)
Sep 14 18:23:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:23:05,413 main INFO screen Mr.Huang pass=0 dev=0.0 ins=18.1 pro=3 1a=False 1b=False 2=True (56.0s)
Sep 14 18:23:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:23:26,732 main INFO screen DUDE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 14 18:24:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:24:06,064 main INFO screen Michael pass=0 dev=0.0 ins=10.42 pro=45 1a=False 1b=False 2=False (66.9s)
Sep 14 18:24:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:24:09,579 main INFO screen SpaceX pass=0 dev=0.0 ins=163.22 pro=1 1a=False 1b=False 2=True (64.2s)
Sep 14 18:24:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:24:21,579 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 14 18:24:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:24:58,443 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.4s)
Sep 14 18:25:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:25:10,215 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:25:10 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:25:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:25:12,892 main INFO screen P(GOON) pass=0 dev=0.0 ins=18.62 pro=77 1a=False 1b=False 2=True (63.3s)
Sep 14 18:25:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:25:21,384 main INFO screen P(GOON) pass=0 dev=0.0 ins=19.46 pro=49 1a=False 1b=False 2=True (59.8s)
Sep 14 18:25:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:25:59,155 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.7s)
Sep 14 18:26:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:26:09,115 main INFO screen DAH pass=0 dev=0.0 ins=17.65 pro=47 1a=False 1b=False 2=True (56.2s)
Sep 14 18:26:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:26:34,566 main INFO screen USDTWINE pass=0 dev=0.0 ins=77.93 pro=3 1a=False 1b=False 2=True (73.2s)
Sep 14 18:27:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:01,555 main INFO screen P(GOON) pass=0 dev=0.0 ins=18.53 pro=1 1a=False 1b=False 2=False (62.4s)
Sep 14 18:27:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:18,597 main INFO screen Whale pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.5s)
Sep 14 18:27:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:31,289 main INFO screen PTK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.7s)
Sep 14 18:27:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:43,059 aiohttp.access INFO 205.210.31.248 [14/Sep/2026:18:27:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 18:27:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:43,473 aiohttp.access INFO 205.210.31.248 [14/Sep/2026:18:27:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 18:27:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:27:56,393 main INFO screen BBC pass=0 dev=0.0 ins=174.11 pro=0 1a=False 1b=False 2=True (54.8s)
Sep 14 18:28:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:28:16,351 main INFO screen moncat pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.8s)
Sep 14 18:28:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:28:26,873 main INFO screen eelonmusk pass=0 dev=0.0 ins=18.69 pro=39 1a=False 1b=False 2=True (55.6s)
Sep 14 18:28:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:28:46,461 main INFO screen Flywheeel pass=0 dev=0.0 ins=15.6 pro=35 1a=False 1b=False 2=False (50.1s)
Sep 14 18:29:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:29:16,678 main INFO screen GRIFFITH pass=0 dev=0.0 ins=31.51 pro=10 1a=False 1b=False 2=True (60.3s)
Sep 14 18:29:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:29:32,366 main INFO screen SOLGOODMAN  pass=0 dev=0.0 ins=20.76 pro=73 1a=False 1b=False 2=True (65.5s)
Sep 14 18:29:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:29:53,346 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.9s)
Sep 14 18:30:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:30:10,486 main INFO screen GRIFFITH pass=0 dev=0.0 ins=20.02 pro=3 1a=False 1b=False 2=False (53.8s)
Sep 14 18:30:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:30:27,136 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:30:27 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:30:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:30:49,280 main INFO screen PSTR pass=0 dev=0.0 ins=52.04 pro=45 1a=False 1b=False 2=True (76.9s)
Sep 14 18:30:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:30:59,723 main INFO screen SEPE pass=0 dev=0.0 ins=19.88 pro=5 1a=False 1b=False 2=False (66.4s)
Sep 14 18:31:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:31:06,745 main INFO screen __e2e pass=0 dev=0.0 ins=30.39 pro=10 1a=False 1b=False 2=True (56.3s)
Sep 14 18:31:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:31:36,277 main INFO screen PROBE pass=0 dev=0.0 ins=31.86 pro=27 1a=False 1b=False 2=True (47.0s)
Sep 14 18:32:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:32:07,309 main INFO screen probe pass=0 dev=0.0 ins=30.66 pro=36 1a=False 1b=False 2=True (67.6s)
Sep 14 18:32:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:32:13,918 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.2s)
Sep 14 18:32:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:32:28,396 main INFO screen E2E pass=0 dev=0.0 ins=18.62 pro=21 1a=False 1b=False 2=True (52.1s)
Sep 14 18:33:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:33:03,371 main INFO screen PROBE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 14 18:33:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:33:12,093 main INFO screen BECKER pass=0 dev=0.0 ins=26.55 pro=23 1a=False 1b=False 2=True (58.2s)
Sep 14 18:33:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:33:26,686 main INFO screen NEVER pass=0 dev=0.0 ins=21.91 pro=63 1a=False 1b=False 2=True (58.3s)
Sep 14 18:33:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:33:45,422 aiohttp.access INFO 152.32.171.73 [14/Sep/2026:18:33:45 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 18:33:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:33:56,042 aiohttp.access INFO 152.32.171.73 [14/Sep/2026:18:33:56 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 14 18:34:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:34:13,626 main INFO screen COMPANY pass=0 dev=0.0 ins=37.01 pro=87 1a=False 1b=False 2=True (70.3s)
Sep 14 18:34:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:34:14,445 aiohttp.access INFO 152.32.171.73 [14/Sep/2026:18:34:14 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 14 18:34:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:34:14,878 aiohttp.access INFO 152.32.171.73 [14/Sep/2026:18:34:14 +0000] "GET /robots.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 14 18:34:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:34:15,324 aiohttp.access INFO 152.32.171.73 [14/Sep/2026:18:34:15 +0000] "GET /sitemap.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 14 18:34:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:34:18,414 main INFO screen USGR pass=0 dev=0.0 ins=140.58 pro=1 1a=False 1b=False 2=True (66.3s)
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:18,569 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:18,734 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:18:35:18 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 18:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:19,080 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (112.4s)
Sep 14 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:37,439 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:35:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:01,735 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (108.1s)
Sep 14 18:36:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:03,889 aiohttp.access INFO 94.154.43.250 [14/Sep/2026:18:36:03 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 18:36:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:16,805 main INFO screen LAPUSHA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (118.4s)
Sep 14 18:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:27,955 main INFO screen pEyes pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 14 18:37:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:05,424 main INFO screen COMPANY pass=0 dev=0.0 ins=20.59 pro=23 1a=False 1b=False 2=False (63.7s)
Sep 14 18:37:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:15,894 main INFO screen Journey pass=0 dev=0.0 ins=48.15 pro=38 1a=False 1b=False 2=True (59.1s)
Sep 14 18:37:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:30,394 main INFO screen GPH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 14 18:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:10,499 main INFO screen TRIPAD pass=0 dev=3.99 ins=34.16 pro=73 1a=False 1b=False 2=True (65.1s)
Sep 14 18:38:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:28,278 main INFO screen Solada pass=0 dev=0.0 ins=31.55 pro=37 1a=False 1b=False 2=True (57.9s)
Sep 14 18:38:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:34,829 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (78.9s)
Sep 14 18:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:05,794 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 14 18:39:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:18,873 main INFO screen 67% pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (50.6s)
Sep 14 18:39:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:26,111 main INFO screen One pass=0 dev=0.0 ins=9.06 pro=82 1a=False 1b=False 2=True (51.3s)
Sep 14 18:39:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:56,426 main INFO screen $630 pass=0 dev=0.0 ins=9.31 pro=8 1a=False 1b=False 2=False (50.6s)
Sep 14 18:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:06,400 main INFO screen EVERYTHING pass=0 dev=0.0 ins=33.93 pro=18 1a=False 1b=False 2=True (47.5s)
Sep 14 18:40:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:16,220 main INFO screen MEME pass=0 dev=0.0 ins=40.88 pro=54 1a=False 1b=False 2=True (50.1s)
Sep 14 18:40:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:40,510 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:40:40 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T17:12:36Z
--- update 2026-09-14T17:17:39Z
--- update 2026-09-14T17:22:47Z
--- update 2026-09-14T17:28:07Z
--- update 2026-09-14T17:33:20Z
--- update 2026-09-14T17:38:34Z
--- update 2026-09-14T17:43:36Z
--- update 2026-09-14T17:48:39Z
--- update 2026-09-14T17:53:42Z
--- update 2026-09-14T17:58:53Z
Running as unit: schaduwbot-wallets.service; invocation ID: 9f16fe299e444a8da42e4530eb930f0d
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T18:04:03Z
--- update 2026-09-14T18:09:27Z
--- update 2026-09-14T18:14:36Z
--- update 2026-09-14T18:19:53Z
--- update 2026-09-14T18:25:09Z
--- update 2026-09-14T18:30:25Z
--- update 2026-09-14T18:35:36Z
--- update 2026-09-14T18:40:39Z
```

## Analyses (laatste 25 regels)
```
active
18:19:17 prijsijk: n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:19:18 na-migratie: 100 paren te checken
18:21:19 na-migratie: 55 paren, 20 prijzen
18:26:27 gemigreerde koersen: 95 gedaan, 1388 te gaan
18:26:29 klaar (705 rpc-calls, 88 fouten)
18:36:22 klaar in 594s -> /opt/schaduwbot/reports/lotgevallen.md
18:36:45   2000 nieuwe tokens doorgerekend
18:37:17 klaar in 54s: 53795 tokens, 2842 nieuw -> /opt/schaduwbot/reports/video_replay.md
18:37:18 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-11 18:37 UTC
18:37:22 111794 tokens geladen
18:37:36   2000 tokens, 177921 trades, 17589 posities (14s)
18:37:50   4000 tokens, 409229 trades, 55283 posities (28s)
18:38:02   6000 tokens, 615222 trades, 79125 posities (40s)
18:38:14   8000 tokens, 800287 trades, 98512 posities (52s)
18:38:26   10000 tokens, 996833 trades, 124114 posities (64s)
18:38:38   12000 tokens, 1196764 trades, 152025 posities (76s)
18:38:51   14000 tokens, 1409721 trades, 177693 posities (89s)
18:39:04   16000 tokens, 1605490 trades, 200109 posities (102s)
18:39:17   18000 tokens, 1803591 trades, 223727 posities (115s)
18:39:28   20000 tokens, 1987405 trades, 241997 posities (126s)
18:39:42   22000 tokens, 2220427 trades, 270991 posities (140s)
18:39:55   24000 tokens, 2414702 trades, 297642 posities (153s)
18:40:10   26000 tokens, 2641234 trades, 330744 posities (168s)
18:40:23   28000 tokens, 2838754 trades, 354938 posities (181s)
18:40:37   30000 tokens, 3034230 trades, 378869 posities (195s)
```

## IJking poolkoers (laatste 12 regels)
```
18:25:09 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:30:31 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
Traceback (most recent call last):
  File "/opt/schaduwbot/pumpswap.py", line 1183, in <module>
    main()
    ~~~~^^
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
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
