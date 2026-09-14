# Schaduwbot status

- tijd: 2026-09-14 23:46:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 9 hours, 59 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.5G/38G | geheugen: 2280/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 148333, "tokens_in_memory": 11034, "msgs": 21960234, "trades": 4494185, "creates": 47798, "decode_fail": 395042, "rpc_calls": 126675, "rpc_errors": 12, "sol_usd": 102.59909909760566, "open_positions": 87, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 23:24:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:24:13,081 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.8s)
Sep 14 23:24:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:24:30,511 main INFO screen gambler pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.2s)
Sep 14 23:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:24:44,521 main INFO screen ​Market pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.5s)
Sep 14 23:24:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:24:59,484 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:24:59 +0000] "GET /health HTTP/1.1" 200 511 "-" "Python-urllib/3.14"
Sep 14 23:25:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:25:05,910 main INFO screen MOLECULAS pass=0 dev=1.22 ins=0.0 pro=11 1a=False 1b=False 2=False (52.8s)
Sep 14 23:25:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:25:46,369 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (75.9s)
Sep 14 23:25:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:25:54,357 main INFO screen SENDOOR pass=0 dev=0.0 ins=23.47 pro=42 1a=False 1b=False 2=False (69.8s)
Sep 14 23:26:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:26:08,451 main INFO screen MadisonBeer pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (62.5s)
Sep 14 23:26:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:26:41,040 main INFO screen BUTTERIN pass=0 dev=0.0 ins=9.65 pro=5 1a=False 1b=False 2=False (54.7s)
Sep 14 23:26:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:26:57,533 main INFO screen Freeman pass=0 dev=0.0 ins=3.43 pro=8 1a=False 1b=False 2=False (63.2s)
Sep 14 23:27:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:27:07,101 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (58.6s)
Sep 14 23:27:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:27:35,924 main INFO screen CocaCola pass=0 dev=0.0 ins=161.44 pro=0 1a=False 1b=False 2=True (54.9s)
Sep 14 23:27:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:27:58,037 main INFO screen $BUFFET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.5s)
Sep 14 23:28:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:28:18,775 main INFO screen KINU pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (71.7s)
Sep 14 23:28:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:28:35,990 main INFO screen JAILPANDA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.1s)
Sep 14 23:28:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:28:54,953 main INFO screen $PROCK pass=0 dev=14.12 ins=0.0 pro=8 1a=False 1b=False 2=False (56.9s)
Sep 14 23:29:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:29:19,563 main INFO screen JAILPANDA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.8s)
Sep 14 23:29:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:29:34,500 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (58.5s)
Sep 14 23:29:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:29:51,755 main INFO screen DERP pass=0 dev=0.76 ins=0.0 pro=1 1a=False 1b=False 2=False (56.8s)
Sep 14 23:30:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:30:02,340 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:30:02 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 23:30:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:30:15,650 main INFO screen BUBBLE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.1s)
Sep 14 23:30:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:30:26,620 main INFO screen AMERICOIN pass=0 dev=0.0 ins=34.89 pro=58 1a=False 1b=False 2=True (52.1s)
Sep 14 23:31:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:31:00,458 main INFO screen leaves pass=0 dev=0.0 ins=25.64 pro=25 1a=False 1b=False 2=True (68.7s)
Sep 14 23:31:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:31:11,064 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (55.4s)
Sep 14 23:31:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:31:39,595 main INFO screen TOM pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (73.0s)
Sep 14 23:31:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:31:58,749 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.3s)
Sep 14 23:32:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:32:21,418 main INFO screen snoopdog pass=0 dev=0.0 ins=5.75 pro=47 1a=False 1b=False 2=False (70.4s)
Sep 14 23:32:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:32:36,590 main INFO screen TOEKNEE pass=0 dev=0.0 ins=35.46 pro=39 1a=False 1b=False 2=True (57.0s)
Sep 14 23:32:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:32:54,153 main INFO screen BMW pass=0 dev=0.0 ins=140.6 pro=0 1a=False 1b=False 2=True (55.4s)
Sep 14 23:33:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:33:29,490 main INFO screen アルー pass=0 dev=0.0 ins=15.62 pro=37 1a=False 1b=False 2=True (68.1s)
Sep 14 23:33:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:33:35,934 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.3s)
Sep 14 23:33:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:33:58,324 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (64.2s)
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:35:19,687 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 23:35:19 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 23:35:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:35:21,214 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:35:21 +0000] "GET /health HTTP/1.1" 200 511 "-" "Python-urllib/3.14"
Sep 14 23:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:35:28,067 main INFO screen GOOD pass=0 dev=0.0 ins=10.36 pro=45 1a=False 1b=False 2=False (118.6s)
Sep 14 23:35:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:35:32,485 main INFO screen Kohaku pass=0 dev=0.0 ins=31.68 pro=45 1a=False 1b=False 2=True (116.6s)
Sep 14 23:35:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:35:32,564 main INFO screen Kohaku pass=0 dev=0.0 ins=29.95 pro=12 1a=False 1b=False 2=True (94.2s)
Sep 14 23:36:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:36:22,882 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.8s)
Sep 14 23:36:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:36:31,673 main INFO screen STEAK pass=0 dev=0.0 ins=3.46 pro=36 1a=False 1b=False 2=False (59.1s)
Sep 14 23:36:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:36:39,108 main INFO screen buy pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.6s)
Sep 14 23:37:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:37:25,684 main INFO screen TIRE pass=0 dev=0.0 ins=25.87 pro=56 1a=False 1b=False 2=True (62.8s)
Sep 14 23:37:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:37:47,365 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.7s)
Sep 14 23:37:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:37:50,130 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.0s)
Sep 14 23:38:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:38:34,813 main INFO screen BRAIN pass=0 dev=0.18 ins=0.0 pro=64 1a=False 1b=False 2=False (69.1s)
Sep 14 23:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:38:46,304 main INFO screen MOLECULAS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 14 23:38:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:38:57,475 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (67.3s)
Sep 14 23:39:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:39:27,878 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.1s)
Sep 14 23:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:39:35,590 main INFO screen TIRE pass=0 dev=0.0 ins=31.62 pro=29 1a=False 1b=False 2=True (49.3s)
Sep 14 23:39:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:39:45,920 main INFO screen SpaceX pass=0 dev=0.0 ins=166.5 pro=0 1a=False 1b=False 2=True (48.4s)
Sep 14 23:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:40:35,687 main INFO screen lana pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (67.8s)
Sep 14 23:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:40:37,162 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:40:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 23:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:40:39,648 main INFO screen DECELS pass=0 dev=0.0 ins=28.42 pro=55 1a=False 1b=False 2=True (64.1s)
Sep 14 23:40:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:40:45,175 main INFO screen Sidequest pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.3s)
Sep 14 23:41:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:41:32,063 main INFO screen TIRE pass=0 dev=0.0 ins=39.55 pro=42 1a=False 1b=False 2=True (56.4s)
Sep 14 23:41:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:41:42,966 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (63.3s)
Sep 14 23:41:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:41:47,433 main INFO screen DEEPSEEKCH pass=0 dev=0.0 ins=0.0 pro=49 1a=False 1b=False 2=False (62.3s)
Sep 14 23:42:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:42:27,602 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.5s)
Sep 14 23:42:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:42:43,735 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.8s)
Sep 14 23:42:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:42:45,654 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.2s)
Sep 14 23:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:43:18,965 main INFO screen DOOMRPG pass=0 dev=0.0 ins=47.27 pro=62 1a=False 1b=False 2=True (51.4s)
Sep 14 23:43:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:43:33,512 main INFO screen KFC pass=0 dev=0.0 ins=26.13 pro=15 1a=False 1b=False 2=True (47.9s)
Sep 14 23:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:43:37,562 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (53.8s)
Sep 14 23:44:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:44:23,862 main INFO screen CATBRAIN pass=0 dev=0.0 ins=13.55 pro=64 1a=False 1b=False 2=True (64.9s)
Sep 14 23:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:44:28,333 main INFO screen Gooner pass=0 dev=0.0 ins=18.16 pro=30 1a=False 1b=False 2=False (50.8s)
Sep 14 23:44:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:44:32,290 main INFO screen CATBRAIN pass=0 dev=0.0 ins=18.19 pro=52 1a=False 1b=False 2=False (58.8s)
Sep 14 23:45:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:45:15,118 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (51.3s)
Sep 14 23:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:45:32,235 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 14 23:45:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:45:34,107 main INFO screen Sidequest pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.8s)
Sep 14 23:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:46:12,017 aiohttp.access INFO 45.33.109.8 [14/Sep/2026:23:46:12 +0000] "UNKNOWN / HTTP/1.0" 400 379 "-" "-"
Sep 14 23:46:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:46:21,156 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:46:21 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T22:16:38Z
--- update 2026-09-14T22:22:15Z
--- update 2026-09-14T22:27:36Z
--- update 2026-09-14T22:32:54Z
--- update 2026-09-14T22:37:58Z
--- update 2026-09-14T22:43:01Z
--- update 2026-09-14T22:48:36Z
--- update 2026-09-14T22:53:43Z
--- update 2026-09-14T22:59:05Z
--- update 2026-09-14T23:04:17Z
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
```

## Analyses (laatste 25 regels)
```
active
22:22:35   38000 tokens, 3709788 trades, 448598 posities (250s)
22:22:50   40000 tokens, 3900481 trades, 473390 posities (264s)
22:23:04   42000 tokens, 4086379 trades, 492462 posities (278s)
22:23:17   44000 tokens, 4260028 trades, 515191 posities (291s)
22:23:30   46000 tokens, 4445005 trades, 537426 posities (305s)
22:23:44   48000 tokens, 4620265 trades, 558280 posities (319s)
22:23:59   50000 tokens, 4822700 trades, 580896 posities (334s)
22:24:14   52000 tokens, 5032898 trades, 607308 posities (349s)
22:24:28   54000 tokens, 5221391 trades, 629728 posities (363s)
22:24:42   56000 tokens, 5390312 trades, 650213 posities (377s)
22:24:58   58000 tokens, 5581326 trades, 674058 posities (393s)
22:25:12   60000 tokens, 5766236 trades, 695878 posities (407s)
22:25:27   62000 tokens, 5971487 trades, 721683 posities (422s)
22:25:40   64000 tokens, 6162947 trades, 750238 posities (435s)
22:25:55   66000 tokens, 6381573 trades, 779020 posities (450s)
22:26:08   68000 tokens, 6564687 trades, 802231 posities (463s)
22:26:23   70000 tokens, 6758719 trades, 827352 posities (478s)
22:26:37   72000 tokens, 6950951 trades, 853949 posities (492s)
22:26:52   74000 tokens, 7146187 trades, 885103 posities (506s)
22:26:56 posities: 891065 uit 7198322 trades (512s)
22:27:09 209874 wallets gerekend
22:27:10 geluk-toets
22:27:44 persistentie
22:27:47 kopieer-simulatie
22:30:19 klaar in 715s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
23:14:42 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=30 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:14:42 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 7/41/173 | al gemeten: 298
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
