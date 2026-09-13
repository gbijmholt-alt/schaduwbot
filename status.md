# Schaduwbot status

- tijd: 2026-09-13 13:07:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 23 hours, 20 minutes
- bot-service: active
- code-versie: 4a93173
- schijf: 4.6G/38G | geheugen: 1044/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.7, "uptime_s": 23609, "tokens_in_memory": 4237, "msgs": 1329777, "trades": 418278, "creates": 4672, "decode_fail": 54098, "rpc_calls": 13436, "rpc_errors": 1, "sol_usd": 99.59185738846878, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 12:31:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:31:35,094 main INFO screen WhiteBull pass=0 dev=1.74 ins=57.28 pro=19 1a=False 1b=False 2=True (87.4s)
Sep 13 12:31:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:31:38,938 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=6 1a=False 1b=False 2=False (85.5s)
Sep 13 12:31:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:31:58,560 main INFO screen SOLCAT pass=0 dev=0.0 ins=32.42 pro=43 1a=False 1b=False 2=True (78.9s)
Sep 13 12:32:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:32:27,037 main INFO screen SOLCOIN pass=0 dev=0.0 ins=28.79 pro=14 1a=False 1b=False 2=True (51.9s)
Sep 13 12:32:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:32:44,136 main INFO screen BATONUS pass=0 dev=0.32 ins=78.99 pro=7 1a=False 1b=True 2=True (65.2s)
Sep 13 12:33:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:33:10,546 main INFO screen BTC pass=0 dev=0.0 ins=22.05 pro=39 1a=False 1b=False 2=False (72.0s)
Sep 13 12:33:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:33:21,038 main INFO screen SOLCAT pass=0 dev=0.0 ins=27.45 pro=33 1a=False 1b=False 2=True (54.0s)
Sep 13 12:33:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:33:43,064 main INFO screen FOLPY pass=0 dev=0.0 ins=29.57 pro=28 1a=False 1b=False 2=True (58.9s)
Sep 13 12:34:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:34:03,757 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.2s)
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:34:54,020 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 12:34:54 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 12:35:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:35:13,338 main INFO screen FOMO pass=0 dev=2.51 ins=0.0 pro=1 1a=False 1b=False 2=True (91.0s)
Sep 13 12:35:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:35:17,149 main INFO screen TFSE pass=1 dev=0.35 ins=8.89 pro=52 1a=False 1b=False 2=False (93.3s)
Sep 13 12:35:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:35:39,562 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:35:39 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 12:35:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:35:52,566 main INFO screen GIGABRAIN pass=0 dev=0.18 ins=79.13 pro=10 1a=False 1b=True 2=True (102.8s)
Sep 13 12:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:36:01,496 main INFO screen BRIAN pass=0 dev=0.0 ins=31.73 pro=9 1a=False 1b=False 2=True (48.2s)
Sep 13 12:38:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:38:38,303 main INFO screen ASPIE pass=0 dev=0.0 ins=18.74 pro=78 1a=False 1b=False 2=True (65.3s)
Sep 13 12:38:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:38:40,791 main INFO screen ARTPEPE pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=False 2=True (61.8s)
Sep 13 12:40:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:40:14,142 main INFO screen useless pass=0 dev=0.0 ins=32.74 pro=35 1a=False 1b=False 2=True (60.7s)
Sep 13 12:40:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:40:49,995 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:40:49 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:43:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:43:05,937 main INFO screen FADD pass=0 dev=0.0 ins=19.7 pro=62 1a=False 1b=False 2=True (63.4s)
Sep 13 12:43:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:43:31,331 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:12:43:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 12:44:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:44:06,652 main INFO screen Bawu pass=0 dev=0.0 ins=30.17 pro=61 1a=False 1b=False 2=True (72.4s)
Sep 13 12:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:46:15,129 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:46:15 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:46:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:46:24,727 main INFO screen michi pass=1 dev=0.0 ins=4.55 pro=66 1a=False 1b=False 2=False (86.4s)
Sep 13 12:46:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:46:28,672 main INFO screen BUBU pass=0 dev=0.0 ins=30.63 pro=40 1a=False 1b=False 2=True (83.4s)
Sep 13 12:46:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:46:32,656 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.5s)
Sep 13 12:48:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:48:03,531 main INFO screen $CAT pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (59.6s)
Sep 13 12:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:49:13,671 main INFO screen Bawa pass=1 dev=0.0 ins=17.88 pro=54 1a=False 1b=False 2=False (62.1s)
Sep 13 12:49:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:49:40,354 main INFO screen BBC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.7s)
Sep 13 12:49:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:49:58,104 main INFO screen NASDAWG pass=0 dev=0.36 ins=56.21 pro=20 1a=False 1b=True 2=True (48.4s)
Sep 13 12:50:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:50:22,684 main INFO screen CAJUN pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (64.9s)
Sep 13 12:50:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:50:49,301 main INFO screen SORA-KUN pass=0 dev=0.0 ins=15.19 pro=62 1a=False 1b=False 2=True (65.8s)
Sep 13 12:50:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:50:53,489 main INFO screen brainpeppu pass=0 dev=0.0 ins=34.8 pro=14 1a=False 1b=False 2=True (55.4s)
Sep 13 12:51:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:51:28,021 main INFO screen DOGELESS pass=0 dev=0.0 ins=16.7 pro=43 1a=False 1b=False 2=True (65.3s)
Sep 13 12:51:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:51:37,125 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:51:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:52:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:52:19,088 main INFO screen DOOROC pass=0 dev=0.53 ins=0.0 pro=5 1a=False 1b=False 2=False (68.6s)
Sep 13 12:52:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:52:21,052 main INFO screen $GOAT pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (61.0s)
Sep 13 12:53:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:53:13,851 main INFO screen RizzEagle pass=0 dev=1.74 ins=55.73 pro=21 1a=False 1b=False 2=True (65.9s)
Sep 13 12:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:54:14,590 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (73.3s)
Sep 13 12:54:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:54:15,741 main INFO screen RAWR pass=1 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (74.3s)
Sep 13 12:54:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:54:23,092 main INFO screen SINS pass=0 dev=0.4 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 13 12:55:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:55:17,949 main INFO screen Bawa pass=0 dev=0.0 ins=28.91 pro=43 1a=False 1b=False 2=True (63.4s)
Sep 13 12:55:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:55:47,620 main INFO screen QML pass=1 dev=1.05 ins=0.0 pro=67 1a=False 1b=False 2=False (64.6s)
Sep 13 12:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:56:38,725 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.5s)
Sep 13 12:57:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:57:25,936 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:57:25 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:57:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:57:36,305 main INFO screen  $LINKS pass=0 dev=6.38 ins=0.0 pro=55 1a=False 1b=False 2=False (61.0s)
Sep 13 12:58:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:58:09,036 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 13 12:58:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:58:49,970 main INFO screen NYT Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.1s)
Sep 13 12:59:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:59:17,311 main INFO screen SOLAI pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (67.5s)
Sep 13 12:59:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:59:18,731 main INFO screen 1 pass=0 dev=0.49 ins=0.0 pro=1 1a=False 1b=False 2=False (67.5s)
Sep 13 12:59:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:59:45,191 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.2s)
Sep 13 13:00:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:00:22,039 main INFO screen panda pass=1 dev=0.0 ins=0.66 pro=74 1a=False 1b=False 2=False (64.7s)
Sep 13 13:00:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:00:59,001 main INFO screen MTDG pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (47.6s)
Sep 13 13:01:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:01:52,909 main INFO screen KUKIS pass=0 dev=0.0 ins=30.89 pro=36 1a=False 1b=True 2=True (61.6s)
Sep 13 13:02:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:11,599 main INFO screen CATacombs pass=1 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (72.6s)
Sep 13 13:02:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:12,812 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.3s)
Sep 13 13:02:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:29,287 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:02:29 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 13:02:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:02:55,137 main INFO screen PONS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 13 13:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:03:26,315 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (74.7s)
Sep 13 13:03:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:03:29,267 main INFO screen titties pass=0 dev=4.6 ins=0.0 pro=3 1a=False 1b=False 2=False (76.5s)
Sep 13 13:04:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:08,642 main INFO screen IF ONLY pass=1 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=False (73.5s)
Sep 13 13:04:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:35,153 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.8s)
Sep 13 13:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:04:46,767 main INFO screen CRIP pass=1 dev=0.0 ins=0.9 pro=51 1a=False 1b=False 2=False (77.5s)
Sep 13 13:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:22,391 main INFO screen MoonDoor pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (73.7s)
Sep 13 13:05:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:34,219 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.1s)
Sep 13 13:05:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:05:52,151 main INFO screen KAT pass=0 dev=0.0 ins=78.87 pro=6 1a=False 1b=False 2=True (65.4s)
Sep 13 13:06:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:06:40,604 main INFO screen ANAI pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (78.2s)
Sep 13 13:06:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:06:47,337 main INFO screen NASHOUSE pass=0 dev=0.32 ins=78.99 pro=5 1a=False 1b=False 2=True (73.1s)
Sep 13 13:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:04,012 main INFO screen BeachOrca pass=0 dev=0.0 ins=55.86 pro=44 1a=False 1b=False 2=True (71.9s)
Sep 13 13:07:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 13:07:37,372 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:13:07:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T12:09:55Z
--- update 2026-09-13T12:15:01Z
--- update 2026-09-13T12:20:10Z
nieuwe code: 673b038
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 09b0ba4bf99c4fb49d28845dfc7b0c51
analyses gestart (ac57af7920e5)
--- update 2026-09-13T12:25:26Z
--- update 2026-09-13T12:30:36Z
--- update 2026-09-13T12:35:38Z
--- update 2026-09-13T12:40:48Z
--- update 2026-09-13T12:46:14Z
--- update 2026-09-13T12:51:36Z
--- update 2026-09-13T12:57:24Z
--- update 2026-09-13T13:02:27Z
nieuwe code: 4a93173
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: be001e47867c4d53bf64f959d70cd386
analyses gestart (00feb5de9af9)
--- update 2026-09-13T13:07:36Z
```

## Analyses (laatste 25 regels)
```
active
12:37:32   38000 tokens, 4247996 trades, 676454 posities (64s)
12:37:35   40000 tokens, 4450017 trades, 707309 posities (66s)
12:37:38   42000 tokens, 4681863 trades, 746679 posities (69s)
12:37:40   44000 tokens, 4887510 trades, 779645 posities (72s)
12:37:44   46000 tokens, 5106832 trades, 817366 posities (75s)
12:37:47   48000 tokens, 5342369 trades, 855935 posities (78s)
12:37:50   50000 tokens, 5575125 trades, 894034 posities (82s)
12:37:54   52000 tokens, 5804738 trades, 942843 posities (86s)
12:37:57 posities: 971417 uit 5945197 trades (89s)
12:38:09 200885 wallets gerekend
12:38:10 geluk-toets
12:38:45 persistentie
12:38:48 kopieer-simulatie
12:39:37 klaar in 189s -> /opt/schaduwbot/reports/wallets.md
13:02:30 52961 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
13:02:37   ingelezen tot rowid 5978206 (53011 rijen, 53011 bruikbaar)
13:02:37 ingelezen: 53011 nieuwe trades, 53011 bruikbaar (9s)
13:03:38 1311 aankopen van gevolgde wallets geëvalueerd
13:03:51 vroege kopers: 166 voldoen nu, register 279, 71 tokens beoordeeld
13:04:07 grote spelers: saldo van 43 wallets opgehaald
13:04:59 herkomst: 40 posities gekoppeld
13:05:05 klaar in 156s -> /opt/schaduwbot/reports/ledger.md
13:06:10 S1: gezakt — toets n=6380, verkennend n=14656
13:06:10 klaar in 65s -> /opt/schaduwbot/reports/hypotheses.md
13:06:10 nieuwe versie lot-v2-foutonderscheid: 388 opgeslagen ketenantwoorden weggegooid
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
