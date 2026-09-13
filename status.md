# Schaduwbot status

- tijd: 2026-09-13 16:53:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 3 hours, 6 minutes
- bot-service: active
- code-versie: 54e958b
- schijf: 4.7G/38G | geheugen: 1377/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 37170, "tokens_in_memory": 5904, "msgs": 3174389, "trades": 797400, "creates": 8752, "decode_fail": 88872, "rpc_calls": 24718, "rpc_errors": 2, "sol_usd": 100.74056963224156, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 16:26:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:26:43,924 main INFO screen BROKE pass=0 dev=0.05 ins=0.0 pro=4 1a=False 1b=False 2=False (58.8s)
Sep 13 16:27:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:27:07,725 main INFO screen FLYWHEEL pass=0 dev=0.0 ins=14.26 pro=31 1a=False 1b=False 2=True (50.8s)
Sep 13 16:27:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:27:20,088 main INFO screen FLYWHEEL pass=0 dev=0.0 ins=16.62 pro=30 1a=False 1b=False 2=True (50.4s)
Sep 13 16:27:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:27:42,686 main INFO screen baton pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (58.8s)
Sep 13 16:28:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:28:00,188 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:28:00 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 16:28:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:28:03,570 main INFO screen NJN pass=0 dev=0.12 ins=0.0 pro=1 1a=False 1b=False 2=False (55.8s)
Sep 13 16:28:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:28:29,761 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.7s)
Sep 13 16:28:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:28:44,454 main INFO screen HEALCAT pass=0 dev=1.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.8s)
Sep 13 16:29:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:29:03,087 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 13 16:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:29:36,693 main INFO screen $REGRET pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (66.9s)
Sep 13 16:30:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:30:33,025 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (66.7s)
Sep 13 16:30:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:30:58,694 main INFO screen DUST pass=0 dev=0.21 ins=0.0 pro=8 1a=False 1b=False 2=False (69.0s)
Sep 13 16:31:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:31:26,155 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.6s)
Sep 13 16:31:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:31:34,172 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.1s)
Sep 13 16:32:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:32:08,557 main INFO screen MUNCH pass=1 dev=0.0 ins=1.99 pro=58 1a=False 1b=False 2=False (66.8s)
Sep 13 16:32:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:32:19,297 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.1s)
Sep 13 16:32:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:32:27,888 main INFO screen USA pass=0 dev=0.0 ins=14.72 pro=38 1a=False 1b=False 2=True (49.3s)
Sep 13 16:33:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:33:06,333 main INFO screen FUMU pass=1 dev=0.0 ins=13.99 pro=44 1a=False 1b=False 2=False (57.8s)
Sep 13 16:33:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:33:16,412 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:33:16 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 16:33:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:33:35,004 main INFO screen MUNCH pass=1 dev=0.0 ins=0.0 pro=64 1a=False 1b=False 2=False (75.7s)
Sep 13 16:33:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:33:39,767 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.9s)
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:34:58,369 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 16:34:58 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 16:34:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:34:59,012 main INFO screen BlueCreep pass=1 dev=0.56 ins=0.0 pro=51 1a=False 1b=False 2=False (112.7s)
Sep 13 16:35:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:35:25,468 main INFO screen $AURA pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (110.5s)
Sep 13 16:35:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:35:29,423 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (109.7s)
Sep 13 16:36:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:36:04,109 main INFO screen 슈바오 pass=0 dev=0.0 ins=30.6 pro=64 1a=False 1b=False 2=True (65.1s)
Sep 13 16:36:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:36:17,848 main INFO screen BIKERCOIN pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (52.4s)
Sep 13 16:36:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:36:32,970 main INFO screen MINT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.5s)
Sep 13 16:37:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:37:01,125 main INFO screen revovle pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.0s)
Sep 13 16:37:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:37:09,803 main INFO screen SOLAVA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (52.0s)
Sep 13 16:37:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:37:23,285 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.3s)
Sep 13 16:37:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:37:55,051 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.9s)
Sep 13 16:38:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:38:00,950 main INFO screen 牛来SOL pass=0 dev=24.45 ins=0.0 pro=1 1a=False 1b=False 2=True (51.1s)
Sep 13 16:38:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:38:25,018 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:38:25 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 16:38:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:38:28,201 main INFO screen CHAOS pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (64.9s)
Sep 13 16:38:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:38:52,761 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 13 16:39:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:39:01,246 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 13 16:39:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:39:16,852 main INFO screen 牛来 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 13 16:40:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:40:24,088 main INFO screen Steak pass=0 dev=5.11 ins=42.44 pro=77 1a=False 1b=False 2=True (66.1s)
Sep 13 16:40:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:40:45,785 main INFO screen WSBC pass=1 dev=0.0 ins=19.71 pro=30 1a=False 1b=False 2=False (65.8s)
Sep 13 16:40:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:40:47,752 main INFO screen salary pass=0 dev=0.07 ins=0.0 pro=6 1a=False 1b=False 2=False (73.4s)
Sep 13 16:41:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:41:20,200 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 13 16:41:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:41:40,644 main INFO screen  1 pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.9s)
Sep 13 16:42:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:42:17,247 main INFO screen NAKEDNYAHU pass=0 dev=0.0 ins=30.54 pro=65 1a=False 1b=False 2=True (54.4s)
Sep 13 16:42:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:42:46,396 main INFO screen salary pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (70.8s)
Sep 13 16:42:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:42:54,321 main INFO screen IWORM pass=0 dev=0.05 ins=79.26 pro=9 1a=False 1b=False 2=True (64.0s)
Sep 13 16:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:43:37,108 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:43:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 16:43:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:43:42,553 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 13 16:43:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:43:51,554 main INFO screen Rui pass=0 dev=0.11 ins=18.44 pro=76 1a=False 1b=False 2=True (63.3s)
Sep 13 16:44:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:44:06,682 main INFO screen SUPPER pass=0 dev=35.3 ins=0.0 pro=5 1a=False 1b=False 2=True (51.1s)
Sep 13 16:45:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:45:09,627 main INFO screen PAPER pass=0 dev=0.02 ins=11.76 pro=64 1a=False 1b=False 2=True (60.1s)
Sep 13 16:46:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:46:08,270 main INFO screen ksubi  pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (62.5s)
Sep 13 16:46:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:46:10,268 main INFO screen Hamster pass=0 dev=0.0 ins=38.16 pro=65 1a=False 1b=False 2=True (65.0s)
Sep 13 16:46:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:46:28,595 main INFO screen Hamster pass=0 dev=0.0 ins=34.31 pro=44 1a=False 1b=False 2=True (65.4s)
Sep 13 16:47:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:47:14,108 main INFO screen EVO pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (65.8s)
Sep 13 16:47:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:47:16,705 main INFO screen $AURA pass=0 dev=0.3 ins=0.0 pro=3 1a=False 1b=False 2=False (66.4s)
Sep 13 16:48:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:48:13,553 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (48.9s)
Sep 13 16:48:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:48:37,603 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:48:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 16:48:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:48:44,663 main INFO screen V1EVE pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (65.6s)
Sep 13 16:48:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:48:52,601 main INFO screen $AURA pass=0 dev=0.3 ins=0.0 pro=2 1a=False 1b=False 2=False (56.5s)
Sep 13 16:49:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:49:42,584 main INFO screen Pearl pass=0 dev=0.0 ins=23.97 pro=81 1a=False 1b=False 2=True (72.9s)
Sep 13 16:49:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:49:51,387 main INFO screen BSTR pass=1 dev=0.0 ins=15.98 pro=53 1a=False 1b=False 2=False (64.5s)
Sep 13 16:50:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:50:52,314 main INFO screen LOAN pass=1 dev=0.0 ins=1.04 pro=14 1a=False 1b=False 2=False (61.0s)
Sep 13 16:51:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:51:57,653 main INFO screen PURPS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (60.0s)
Sep 13 16:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:51:58,065 main INFO screen nothing pass=0 dev=20.1 ins=19.63 pro=67 1a=False 1b=False 2=True (69.0s)
Sep 13 16:52:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:52:06,615 main INFO screen nothing pass=0 dev=0.0 ins=43.65 pro=52 1a=False 1b=False 2=True (65.5s)
Sep 13 16:52:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:52:53,180 main INFO screen nothing pass=0 dev=0.0 ins=21.23 pro=32 1a=False 1b=False 2=True (55.5s)
Sep 13 16:53:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:53:06,523 main INFO screen TTC pass=1 dev=0.88 ins=0.0 pro=63 1a=False 1b=False 2=False (68.5s)
Sep 13 16:53:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:53:11,900 main INFO screen nothing pass=0 dev=0.0 ins=37.97 pro=59 1a=False 1b=False 2=True (65.3s)
Sep 13 16:53:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 16:53:38,484 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:16:53:38 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 7948cd6f3a7b4dfeb4d4bd945d22b179
analyses gestart (e3190511b57b)
--- update 2026-09-13T15:30:21Z
--- update 2026-09-13T15:35:23Z
--- update 2026-09-13T15:40:36Z
--- update 2026-09-13T15:45:59Z
--- update 2026-09-13T15:51:26Z
--- update 2026-09-13T15:56:33Z
--- update 2026-09-13T16:01:34Z
--- update 2026-09-13T16:06:36Z
--- update 2026-09-13T16:12:13Z
--- update 2026-09-13T16:17:33Z
--- update 2026-09-13T16:22:36Z
--- update 2026-09-13T16:27:59Z
--- update 2026-09-13T16:33:15Z
--- update 2026-09-13T16:38:24Z
--- update 2026-09-13T16:43:36Z
--- update 2026-09-13T16:48:36Z
--- update 2026-09-13T16:53:37Z
```

## Analyses (laatste 25 regels)
```
inactive
15:37:05   18000 tokens, 1944204 trades, 298142 posities (51s)
15:37:10   20000 tokens, 2187868 trades, 342250 posities (57s)
15:37:15   22000 tokens, 2406411 trades, 378792 posities (62s)
15:37:19   24000 tokens, 2626614 trades, 409516 posities (65s)
15:37:22   26000 tokens, 2840165 trades, 441465 posities (69s)
15:37:26   28000 tokens, 3073379 trades, 477166 posities (73s)
15:37:30   30000 tokens, 3304489 trades, 515001 posities (77s)
15:37:34   32000 tokens, 3516909 trades, 546487 posities (80s)
15:37:38   34000 tokens, 3731214 trades, 580535 posities (84s)
15:37:43   36000 tokens, 3958328 trades, 619055 posities (89s)
15:37:48   38000 tokens, 4172693 trades, 651310 posities (95s)
15:37:53   40000 tokens, 4383091 trades, 680638 posities (99s)
15:37:57   42000 tokens, 4594546 trades, 716760 posities (104s)
15:38:02   44000 tokens, 4815309 trades, 751831 posities (109s)
15:38:07   46000 tokens, 5015503 trades, 782629 posities (114s)
15:38:13   48000 tokens, 5236735 trades, 820680 posities (120s)
15:38:20   50000 tokens, 5466284 trades, 857419 posities (127s)
15:38:27   52000 tokens, 5695807 trades, 893439 posities (134s)
15:38:34   54000 tokens, 5919511 trades, 938690 posities (141s)
15:38:40 posities: 976402 uit 6110942 trades (148s)
15:38:54 199901 wallets gerekend
15:38:54 geluk-toets
15:39:30 persistentie
15:39:33 kopieer-simulatie
15:40:43 klaar in 271s -> /opt/schaduwbot/reports/wallets.md
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
