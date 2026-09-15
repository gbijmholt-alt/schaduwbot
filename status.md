# Schaduwbot status

- tijd: 2026-09-15 17:54:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 4 hours, 7 minutes
- bot-service: active
- code-versie: 3840d00
- schijf: 7.5G/38G | geheugen: 2245/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 213601, "tokens_in_memory": 9501, "msgs": 32137232, "trades": 6672502, "creates": 70874, "decode_fail": 566600, "rpc_calls": 191745, "rpc_errors": 16, "sol_usd": 100.4200564822609, "open_positions": 73, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 17:31:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:31:32,231 main INFO screen LV pass=0 dev=0.0 ins=155.12 pro=0 1a=False 1b=False 2=True (53.2s)
Sep 15 17:31:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:31:54,202 main INFO screen JOHN pass=0 dev=0.0 ins=0.0 pro=65 1a=False 1b=False 2=False (66.1s)
Sep 15 17:32:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:32:45,801 main INFO screen MESSI pass=0 dev=0.35 ins=0.0 pro=16 1a=False 1b=False 2=False (80.3s)
Sep 15 17:32:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:32:49,740 main INFO screen train pass=0 dev=0.0 ins=18.4 pro=3 1a=False 1b=False 2=False (77.5s)
Sep 15 17:32:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:32:54,916 main INFO screen Ballistics  pass=0 dev=0.0 ins=20.89 pro=74 1a=False 1b=False 2=True (60.7s)
Sep 15 17:33:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:33:46,143 main INFO screen VIRGIN pass=0 dev=0.0 ins=46.23 pro=31 1a=False 1b=False 2=True (60.3s)
Sep 15 17:33:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:33:51,452 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:33:51 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 17:34:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:34:06,483 main INFO screen GLASSBOX pass=0 dev=0.0 ins=48.15 pro=36 1a=False 1b=False 2=True (76.7s)
Sep 15 17:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:34:08,480 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (73.6s)
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:35:39,757 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 17:35:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:35:39,883 rpc WARNING rpc getSignaturesForAddress exc
Sep 15 17:35:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:35:52,144 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (126.0s)
Sep 15 17:36:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:36:14,019 main INFO screen Noni pass=0 dev=0.0 ins=20.74 pro=66 1a=False 1b=False 2=True (125.5s)
Sep 15 17:36:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:36:22,362 main INFO screen AI GAMER pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (135.9s)
Sep 15 17:37:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:37:13,732 main INFO screen XCashtag pass=0 dev=0.0 ins=19.44 pro=2 1a=False 1b=False 2=False (81.6s)
Sep 15 17:37:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:37:15,205 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 15 17:37:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:37:31,336 main INFO screen Pokémane pass=0 dev=0.0 ins=10.07 pro=34 1a=False 1b=False 2=False (69.0s)
Sep 15 17:38:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:38:09,294 main INFO screen PONYX pass=0 dev=0.0 ins=37.78 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 15 17:38:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:38:13,377 main INFO screen ACT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.6s)
Sep 15 17:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:38:46,178 main INFO screen MESSI pass=0 dev=0.43 ins=0.0 pro=20 1a=False 1b=False 2=False (74.8s)
Sep 15 17:38:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:38:51,519 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:38:51 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 17:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:39:08,197 main INFO screen MOONCOIN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.9s)
Sep 15 17:39:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:39:25,092 main INFO screen SLOPNET pass=0 dev=0.0 ins=58.46 pro=11 1a=False 1b=False 2=True (71.7s)
Sep 15 17:39:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:39:42,838 main INFO screen ROBIN pass=0 dev=0.06 ins=0.0 pro=5 1a=False 1b=False 2=False (56.7s)
Sep 15 17:40:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:40:05,388 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.2s)
Sep 15 17:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:40:35,763 main INFO screen warren pass=0 dev=0.86 ins=5.65 pro=40 1a=False 1b=False 2=False (70.7s)
Sep 15 17:40:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:40:36,681 main INFO screen GIGAFROG pass=0 dev=0.0 ins=30.33 pro=10 1a=False 1b=False 2=True (53.8s)
Sep 15 17:41:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:41:15,476 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (70.1s)
Sep 15 17:41:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:41:43,864 main INFO screen Colony pass=0 dev=0.0 ins=14.58 pro=56 1a=False 1b=False 2=False (68.1s)
Sep 15 17:41:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:41:49,759 main INFO screen taycruise pass=0 dev=0.0 ins=0.88 pro=22 1a=False 1b=False 2=False (73.1s)
Sep 15 17:42:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:42:22,723 main INFO screen INF pass=0 dev=0.0 ins=26.22 pro=22 1a=False 1b=False 2=False (67.2s)
Sep 15 17:42:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:42:49,213 main INFO screen FLY pass=0 dev=0.0 ins=16.04 pro=78 1a=False 1b=False 2=True (65.3s)
Sep 15 17:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:42:52,161 main INFO screen $BANANA pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (62.4s)
Sep 15 17:43:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:43:12,703 main INFO screen ElonBus pass=0 dev=0.0 ins=26.61 pro=13 1a=False 1b=False 2=False (50.0s)
Sep 15 17:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:43:53,360 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:43:53 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 17:43:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:43:57,003 main INFO screen ZBATON pass=0 dev=0.0 ins=77.15 pro=9 1a=False 1b=False 2=True (67.8s)
Sep 15 17:43:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:43:58,228 main INFO screen ElonBus pass=0 dev=0.0 ins=26.56 pro=48 1a=False 1b=False 2=True (66.1s)
Sep 15 17:43:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:43:59,294 main INFO screen BUST pass=0 dev=0.0 ins=20.22 pro=1 1a=False 1b=False 2=False (46.6s)
Sep 15 17:45:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:45:07,737 main INFO screen PIE pass=0 dev=0.0 ins=11.29 pro=67 1a=False 1b=False 2=True (70.7s)
Sep 15 17:45:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:45:08,254 main INFO screen Blue pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (69.0s)
Sep 15 17:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:45:10,079 main INFO screen IRIDO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (71.8s)
Sep 15 17:45:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:45:59,880 main INFO screen EXIT pass=0 dev=0.0 ins=48.14 pro=11 1a=False 1b=False 2=True (52.1s)
Sep 15 17:46:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:46:01,889 main INFO screen bikepepe pass=0 dev=0.0 ins=79.17 pro=3 1a=False 1b=True 2=True (51.8s)
Sep 15 17:46:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:46:09,021 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 15 17:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:47:07,905 main INFO screen BOOST pass=0 dev=0.0 ins=47.89 pro=34 1a=False 1b=False 2=True (68.0s)
Sep 15 17:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:47:10,804 main INFO screen booster pass=0 dev=0.0 ins=20.22 pro=8 1a=False 1b=False 2=True (68.9s)
Sep 15 17:47:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:47:17,206 main INFO screen CLEAR pass=0 dev=0.0 ins=45.05 pro=75 1a=False 1b=False 2=True (68.2s)
Sep 15 17:48:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:48:05,511 main INFO screen NTDA pass=0 dev=0.0 ins=133.3 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 15 17:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:48:15,975 main INFO screen cashdog pass=0 dev=0.0 ins=30.34 pro=59 1a=False 1b=False 2=True (65.2s)
Sep 15 17:48:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:48:19,823 main INFO screen Neurot pass=0 dev=0.0 ins=25.52 pro=44 1a=False 1b=False 2=True (62.6s)
Sep 15 17:48:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:48:55,467 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:48:55 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 17:48:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:48:57,836 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.3s)
Sep 15 17:49:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:49:09,719 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 15 17:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:49:19,799 main INFO screen VICKS pass=0 dev=1.74 ins=0.0 pro=58 1a=False 1b=False 2=False (60.0s)
Sep 15 17:49:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:49:47,966 main INFO screen Tap pass=0 dev=0.0 ins=29.55 pro=48 1a=False 1b=False 2=True (50.1s)
Sep 15 17:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:49:59,514 main INFO screen PokeFi pass=0 dev=0.0 ins=46.79 pro=17 1a=False 1b=False 2=True (49.8s)
Sep 15 17:50:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:50:09,043 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.2s)
Sep 15 17:50:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:50:40,260 main INFO screen DECIDER pass=0 dev=0.0 ins=29.46 pro=12 1a=False 1b=False 2=False (52.3s)
Sep 15 17:50:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:50:50,336 main INFO screen PIXI pass=0 dev=0.0 ins=30.31 pro=10 1a=False 1b=False 2=True (50.8s)
Sep 15 17:50:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:50:59,494 main INFO screen cashdog pass=0 dev=0.0 ins=17.72 pro=58 1a=False 1b=False 2=True (50.4s)
Sep 15 17:51:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:51:30,815 main INFO screen cashdog pass=0 dev=0.0 ins=56.62 pro=48 1a=False 1b=False 2=True (50.6s)
Sep 15 17:51:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:51:37,064 main INFO screen wattacoin pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (46.7s)
Sep 15 17:51:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:51:49,578 main INFO screen chump pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.1s)
Sep 15 17:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:52:34,940 main INFO screen REALSMITH pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (64.1s)
Sep 15 17:52:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:52:36,398 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.3s)
Sep 15 17:52:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:52:53,432 main INFO screen Tap pass=0 dev=0.0 ins=29.55 pro=65 1a=False 1b=False 2=True (63.9s)
Sep 15 17:53:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:53:28,652 main INFO screen CLC pass=0 dev=0.0 ins=25.51 pro=29 1a=False 1b=False 2=True (52.3s)
Sep 15 17:53:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:53:30,183 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 15 17:53:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:53:41,660 main INFO screen ELON pass=0 dev=0.0 ins=34.14 pro=59 1a=False 1b=False 2=True (48.2s)
Sep 15 17:54:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:54:09,044 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:54:09 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T16:38:26Z
--- update 2026-09-15T16:43:26Z
--- update 2026-09-15T16:48:28Z
--- update 2026-09-15T16:53:28Z
nieuwe code: 3840d00
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T16:58:30Z
--- update 2026-09-15T17:03:32Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7c9219c3aae94dd6b36411ad76eddaca
analyses gestart (84579ff37485)
--- update 2026-09-15T17:08:36Z
--- update 2026-09-15T17:13:36Z
--- update 2026-09-15T17:18:40Z
--- update 2026-09-15T17:23:42Z
--- update 2026-09-15T17:28:49Z
--- update 2026-09-15T17:33:50Z
--- update 2026-09-15T17:38:50Z
--- update 2026-09-15T17:43:52Z
--- update 2026-09-15T17:48:54Z
--- update 2026-09-15T17:54:07Z
```

## Analyses (laatste 40 regels)
```
inactive
12:20:45   4500/6807 lopers, 32066 koppelingen
12:21:33   5000/6807 lopers, 35311 koppelingen
12:22:13   5500/6807 lopers, 38244 koppelingen
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
--- /opt/schaduwbot/vamp.py 13:01:37
13:01:37 tokens lezen
13:01:41 135941 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
13:13:51 6879 lopers, 19 niet-onderscheidende woorden
13:14:53   500/6879 lopers, 4294 koppelingen
13:15:46   1000/6879 lopers, 7299 koppelingen
13:16:30   1500/6879 lopers, 11181 koppelingen
13:17:20   2000/6879 lopers, 15724 koppelingen
13:18:02   2500/6879 lopers, 18375 koppelingen
13:18:35   3000/6879 lopers, 21263 koppelingen
13:19:25   3500/6879 lopers, 25366 koppelingen
13:19:59   4000/6879 lopers, 28115 koppelingen
13:20:55   4500/6879 lopers, 31747 koppelingen
13:21:39   5000/6879 lopers, 34889 koppelingen
13:22:16   5500/6879 lopers, 37799 koppelingen
13:23:41   6000/6879 lopers, 44142 koppelingen
13:24:27   6500/6879 lopers, 47629 koppelingen
13:24:50 uitkomsten uit de trades halen
13:38:33 69698 tokens met een instapkoers
13:38:34 klaar in 2217s: 6879 lopers, 27676 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 13:38:34
--- /opt/schaduwbot/video_replay.py 14:02:16
--- /opt/schaduwbot/video_replay.py 15:02:36
--- /opt/schaduwbot/video_replay.py 16:03:19
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
17:28:59 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=261 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:28:59 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 9/39/150 | al gemeten: 669
17:34:21 ijk: +6 van 7 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=266 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:34:21 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 12/40/155 | al gemeten: 675
17:39:03 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=267 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:39:03 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 11/41/154 | al gemeten: 678
17:44:20 ijk: +6 van 6 kandidaten (15 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=271 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:44:20 ijk-diagnose: nieuwste migratie -0.4 min oud | migraties 15/60/240 min: 17/44/158 | al gemeten: 684
17:49:24 ijk: +6 van 6 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=275 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:49:24 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 14/45/156 | al gemeten: 690
17:54:08 ijk: +0 van 0 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 12}) | verste bak n=275 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:54:09 ijk-diagnose: nieuwste migratie 6.3 min oud | migraties 15/60/240 min: 12/42/151 | al gemeten: 690
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
