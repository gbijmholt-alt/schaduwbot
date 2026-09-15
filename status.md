# Schaduwbot status

- tijd: 2026-09-15 04:39:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 14 hours, 52 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.8G/38G | geheugen: 2531/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 165930, "tokens_in_memory": 8049, "msgs": 25457577, "trades": 5060697, "creates": 54139, "decode_fail": 430921, "rpc_calls": 143902, "rpc_errors": 13, "sol_usd": 101.25914934115131, "open_positions": 76, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 04:14:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:14:41,240 main INFO screen PROFITABLE pass=0 dev=0.0 ins=18.06 pro=47 1a=False 1b=False 2=True (57.2s)
Sep 15 04:15:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:42,832 main INFO screen MIKEANSON pass=0 dev=0.0 ins=32.09 pro=48 1a=False 1b=False 2=True (65.9s)
Sep 15 04:15:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:44,900 main INFO screen QUANT pass=0 dev=0.0 ins=19.21 pro=17 1a=False 1b=False 2=True (66.9s)
Sep 15 04:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:15:47,248 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.0s)
Sep 15 04:16:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:47,225 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (62.3s)
Sep 15 04:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:53,767 main INFO screen KIMCHI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.5s)
Sep 15 04:16:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:16:54,630 main INFO screen HILL pass=0 dev=0.0 ins=4.38 pro=36 1a=False 1b=False 2=False (71.8s)
Sep 15 04:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:17:38,590 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.4s)
Sep 15 04:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:00,892 main INFO screen RAIN pass=0 dev=0.0 ins=19.31 pro=55 1a=False 1b=False 2=True (66.3s)
Sep 15 04:18:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:05,285 main INFO screen MIKEANSON pass=0 dev=0.0 ins=31.77 pro=43 1a=False 1b=False 2=True (71.5s)
Sep 15 04:18:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:38,831 main INFO screen JIGG pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.2s)
Sep 15 04:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:56,681 main INFO screen SOLANA pass=0 dev=0.0 ins=10.33 pro=31 1a=False 1b=False 2=True (51.4s)
Sep 15 04:18:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:18:57,379 main INFO screen battwine pass=0 dev=0.0 ins=78.05 pro=18 1a=False 1b=True 2=True (56.5s)
Sep 15 04:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:19:22,028 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:19:22 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:19:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:19:36,685 main INFO screen MCAT pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 15 04:19:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:19:57,718 main INFO screen PRINT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 15 04:19:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:19:59,957 main INFO screen GOAT pass=0 dev=0.0 ins=35.25 pro=65 1a=False 1b=False 2=True (63.3s)
Sep 15 04:20:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:20:40,148 main INFO screen fomo pass=0 dev=79.31 ins=155.27 pro=0 1a=False 1b=False 2=True (63.5s)
Sep 15 04:21:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:21:03,135 main INFO screen IMP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.4s)
Sep 15 04:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:21:10,074 main INFO screen HUHCAT pass=0 dev=0.0 ins=0.65 pro=59 1a=False 1b=False 2=True (70.1s)
Sep 15 04:22:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:22:00,916 main INFO screen HOLLAND pass=0 dev=0.0 ins=0.18 pro=67 1a=False 1b=False 2=False (80.8s)
Sep 15 04:22:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:22:12,772 main INFO screen SOLANA pass=0 dev=0.0 ins=31.05 pro=67 1a=False 1b=False 2=True (62.7s)
Sep 15 04:22:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:22:18,002 main INFO screen Bolt pass=0 dev=0.0 ins=10.12 pro=33 1a=False 1b=False 2=False (74.9s)
Sep 15 04:23:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:23:12,212 main INFO screen AAPL pass=0 dev=79.31 ins=117.58 pro=0 1a=False 1b=False 2=True (71.3s)
Sep 15 04:23:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:23:28,281 main INFO screen RIPMichael pass=0 dev=79.31 ins=79.31 pro=0 1a=False 1b=False 2=True (75.5s)
Sep 15 04:23:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:23:40,030 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (82.0s)
Sep 15 04:24:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:24:28,652 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (76.4s)
Sep 15 04:24:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:24:33,600 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:24:33 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:24:35,371 main INFO screen WOFI pass=0 dev=0.0 ins=101.84 pro=1 1a=False 1b=False 2=True (67.1s)
Sep 15 04:25:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:25:00,000 main INFO screen 50scent pass=0 dev=0.02 ins=0.0 pro=57 1a=False 1b=False 2=False (80.0s)
Sep 15 04:25:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:25:34,180 main INFO screen $TRUMPVOTE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 15 04:25:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:25:40,825 main INFO screen TOTC pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=True 2=True (65.5s)
Sep 15 04:26:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:26:05,897 main INFO screen LaPeace pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.9s)
Sep 15 04:26:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:26:42,041 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (67.9s)
Sep 15 04:26:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:26:48,244 main INFO screen WWR pass=0 dev=6.11 ins=32.87 pro=1 1a=False 1b=False 2=True (67.4s)
Sep 15 04:27:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:27:35,066 main INFO screen DiNero pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (89.2s)
Sep 15 04:27:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:27:48,537 main INFO screen $TRUMPVOTE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.5s)
Sep 15 04:27:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:27:55,802 main INFO screen teslon pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (67.6s)
Sep 15 04:29:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:29:04,511 main INFO screen cookedcat pass=0 dev=0.0 ins=15.16 pro=46 1a=False 1b=False 2=False (89.4s)
Sep 15 04:29:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:29:12,598 main INFO screen Bull-ish pass=0 dev=0.0 ins=24.68 pro=40 1a=False 1b=False 2=True (84.1s)
Sep 15 04:29:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:29:13,041 main INFO screen cooked pass=0 dev=0.0 ins=14.61 pro=55 1a=False 1b=False 2=True (77.2s)
Sep 15 04:29:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:29:37,134 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:29:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:30:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:30:13,954 main INFO screen EMOBOYZ pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (69.4s)
Sep 15 04:30:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:30:23,093 main INFO screen Crew pass=0 dev=0.0 ins=4.93 pro=30 1a=False 1b=False 2=False (70.5s)
Sep 15 04:30:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:30:36,002 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (83.0s)
Sep 15 04:31:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:31:25,791 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (71.8s)
Sep 15 04:31:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:31:33,251 main INFO screen sender pass=0 dev=0.0 ins=17.8 pro=43 1a=False 1b=False 2=True (70.2s)
Sep 15 04:31:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:31:39,331 main INFO screen McFries pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.3s)
Sep 15 04:32:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:32:45,746 main INFO screen STUMP pass=0 dev=0.0 ins=9.66 pro=11 1a=False 1b=False 2=False (80.0s)
Sep 15 04:32:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:32:46,939 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.7s)
Sep 15 04:32:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:32:51,205 main INFO screen SOL pass=0 dev=0.0 ins=39.03 pro=66 1a=False 1b=False 2=True (71.9s)
Sep 15 04:33:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:33:40,588 main INFO screen SHyrox pass=0 dev=3.92 ins=90.49 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 15 04:33:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:33:56,031 main INFO screen ASPIE pass=0 dev=0.0 ins=15.6 pro=13 1a=False 1b=False 2=True (64.8s)
Sep 15 04:33:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:33:59,953 main INFO screen PFG pass=0 dev=130.83 ins=0.0 pro=17 1a=False 1b=False 2=False (73.0s)
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:28,440 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:28,567 main INFO screen KET pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (108.0s)
Sep 15 04:35:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:28,658 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:35:28 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 04:35:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:44,717 main INFO screen MDOR pass=0 dev=0.0 ins=19.58 pro=1 1a=False 1b=False 2=True (104.8s)
Sep 15 04:35:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:35:46,373 main INFO screen CATE pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (110.3s)
Sep 15 04:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:27,985 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 15 04:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:37,001 main INFO screen DogC pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (52.3s)
Sep 15 04:36:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:36:45,918 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 15 04:37:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:17,754 main INFO screen SOLdiers pass=0 dev=0.0 ins=22.07 pro=36 1a=False 1b=False 2=True (49.8s)
Sep 15 04:37:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:34,019 main INFO screen WOFI pass=0 dev=1.81 ins=118.36 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 15 04:37:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:37:59,086 main INFO screen STUMP pass=0 dev=10.3 ins=0.0 pro=23 1a=False 1b=False 2=False (73.2s)
Sep 15 04:38:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:16,207 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (58.5s)
Sep 15 04:38:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:29,140 main INFO screen Toely pass=0 dev=0.0 ins=36.06 pro=43 1a=False 1b=False 2=True (55.1s)
Sep 15 04:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:38:55,963 main INFO screen HIPPLEX pass=0 dev=0.0 ins=78.91 pro=18 1a=False 1b=True 2=True (56.9s)
Sep 15 04:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:05,741 main INFO screen 4096 pass=0 dev=0.0 ins=36.55 pro=69 1a=False 1b=False 2=True (49.5s)
Sep 15 04:39:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:39:38,226 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:39:38 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T03:13:43Z
--- update 2026-09-15T03:18:46Z
--- update 2026-09-15T03:23:46Z
--- update 2026-09-15T03:29:04Z
--- update 2026-09-15T03:34:05Z
--- update 2026-09-15T03:39:07Z
--- update 2026-09-15T03:44:09Z
--- update 2026-09-15T03:49:12Z
--- update 2026-09-15T03:54:12Z
Running as unit: schaduwbot-wallets.service; invocation ID: c556852febb7497c926f7c233c44f1d1
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T03:59:12Z
--- update 2026-09-15T04:04:15Z
--- update 2026-09-15T04:09:16Z
--- update 2026-09-15T04:14:19Z
--- update 2026-09-15T04:19:20Z
--- update 2026-09-15T04:24:32Z
--- update 2026-09-15T04:29:35Z
--- update 2026-09-15T04:34:36Z
--- update 2026-09-15T04:39:36Z
```

## Analyses (laatste 25 regels)
```
active
04:33:58   4000 tokens, 393143 trades, 50164 posities (30s)
04:34:10   6000 tokens, 584657 trades, 71297 posities (42s)
04:34:21   8000 tokens, 750663 trades, 85877 posities (52s)
04:34:32   10000 tokens, 940393 trades, 107709 posities (64s)
04:34:45   12000 tokens, 1141661 trades, 136638 posities (77s)
04:34:59   14000 tokens, 1344760 trades, 161937 posities (91s)
04:35:11   16000 tokens, 1533521 trades, 182480 posities (103s)
04:35:24   18000 tokens, 1729181 trades, 206553 posities (116s)
04:35:36   20000 tokens, 1905565 trades, 223681 posities (127s)
04:35:49   22000 tokens, 2101825 trades, 245093 posities (140s)
04:36:03   24000 tokens, 2325404 trades, 275091 posities (154s)
04:36:18   26000 tokens, 2537504 trades, 303375 posities (170s)
04:36:31   28000 tokens, 2721868 trades, 326320 posities (183s)
04:36:43   30000 tokens, 2900892 trades, 347277 posities (194s)
04:36:56   32000 tokens, 3097764 trades, 371033 posities (207s)
04:37:08   34000 tokens, 3281934 trades, 391491 posities (220s)
04:37:23   36000 tokens, 3476755 trades, 416750 posities (234s)
04:37:40   38000 tokens, 3669904 trades, 439287 posities (251s)
04:37:56   40000 tokens, 3869261 trades, 465053 posities (267s)
04:38:12   42000 tokens, 4053581 trades, 487112 posities (283s)
04:38:27   44000 tokens, 4238786 trades, 509220 posities (299s)
04:38:42   46000 tokens, 4415347 trades, 529333 posities (314s)
04:38:58   48000 tokens, 4589550 trades, 549788 posities (329s)
04:39:15   50000 tokens, 4787116 trades, 574764 posities (347s)
04:39:32   52000 tokens, 4994455 trades, 600510 posities (363s)
```

## IJking poolkoers (laatste 12 regels)
```
03:29:10 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=118 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:29:10 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 9/38/154 | al gemeten: 436
03:34:11 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=120 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:34:11 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 7/37/155 | al gemeten: 438
03:39:20 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=124 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:39:20 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 8/37/155 | al gemeten: 442
03:44:15 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=126 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:44:15 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 8/36/155 | al gemeten: 444
03:49:22 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=129 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:49:22 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 10/37/155 | al gemeten: 447
03:54:48 ijk: +6 van 6 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=133 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:54:52 ijk-diagnose: nieuwste migratie -0.3 min oud | migraties 15/60/240 min: 13/42/159 | al gemeten: 453
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
