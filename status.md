# Schaduwbot status

- tijd: 2026-09-13 07:16:11 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 17 hours, 29 minutes
- bot-service: active
- code-versie: e5a2860
- schijf: 4.3G/38G | geheugen: 606/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2523, "tokens_in_memory": 518, "msgs": 200280, "trades": 39550, "creates": 518, "decode_fail": 5714, "rpc_calls": 1541, "rpc_errors": 0, "sol_usd": 101.30380371155245, "open_positions": 18, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 06:36:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:08,028 main INFO screen cco pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (61.0s)
Sep 13 06:36:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:09,430 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 13 06:36:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:29,831 main INFO screen batonwif pass=0 dev=3.11 ins=75.89 pro=1 1a=True 1b=True 2=True (57.3s)
Sep 13 06:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:37:06,478 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.4s)
Sep 13 06:37:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:37:30,597 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.7s)
Sep 13 06:38:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:38:26,924 main INFO screen PNUT pass=0 dev=0.0 ins=25.45 pro=46 1a=False 1b=False 2=True (70.2s)
Sep 13 06:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:39:08,069 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:39:08 +0000] "GET /health HTTP/1.1" 200 486 "-" "Python-urllib/3.14"
Sep 13 06:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:40:02,085 main INFO screen Rabbit pass=0 dev=0.0 ins=36.24 pro=72 1a=False 1b=False 2=True (74.7s)
Sep 13 06:40:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:40:22,289 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.7s)
Sep 13 06:40:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:40:33,356 main INFO screen PSYCHO pass=0 dev=15.18 ins=0.0 pro=3 1a=False 1b=False 2=False (73.5s)
Sep 13 06:40:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:40:52,503 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (50.4s)
Sep 13 06:41:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:41:12,211 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.9s)
Sep 13 06:41:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:41:36,218 main INFO screen BaldEagle pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.9s)
Sep 13 06:41:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:41:41,176 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 13 06:42:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:42:04,959 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.7s)
Sep 13 06:42:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:42:27,054 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (50.8s)
Sep 13 06:42:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:42:47,543 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (66.4s)
Sep 13 06:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:42:52,925 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.0s)
Sep 13 06:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:43:18,244 main INFO screen Benz pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.2s)
Sep 13 06:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:43:55,536 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (62.6s)
Sep 13 06:43:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:43:57,165 main INFO screen NUT pass=0 dev=0.0 ins=10.34 pro=72 1a=False 1b=False 2=True (69.6s)
Sep 13 06:44:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:44:10,922 main INFO screen 10x pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (52.7s)
Sep 13 06:44:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:44:12,122 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:44:12 +0000] "GET /health HTTP/1.1" 200 491 "-" "Python-urllib/3.14"
Sep 13 06:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:44:59,375 main INFO screen Verity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (63.8s)
Sep 13 06:45:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:45:05,777 main INFO screen Verity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.6s)
Sep 13 06:45:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:45:08,795 main INFO screen 3 sol pass=0 dev=0.29 ins=0.0 pro=3 1a=False 1b=False 2=False (57.3s)
Sep 13 06:45:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:45:49,977 main INFO screen NUT pass=0 dev=0.0 ins=20.34 pro=38 1a=False 1b=False 2=True (50.6s)
Sep 13 06:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:46:35,958 main INFO screen TP pass=0 dev=0.0 ins=18.21 pro=58 1a=False 1b=False 2=True (59.0s)
Sep 13 06:47:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:47:04,982 main INFO screen Optimist pass=1 dev=0.0 ins=7.72 pro=46 1a=False 1b=False 2=False (71.5s)
Sep 13 06:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:47:07,983 main INFO screen ponks pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=False 2=True (67.1s)
Sep 13 06:47:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:47:55,754 main INFO screen HIMA pass=0 dev=0.0 ins=25.77 pro=53 1a=False 1b=False 2=True (72.7s)
Sep 13 06:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:18,562 main INFO screen $MOMO pass=1 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (73.6s)
Sep 13 06:48:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:27,427 main INFO screen Nuts pass=0 dev=0.0 ins=10.34 pro=63 1a=False 1b=False 2=True (67.3s)
Sep 13 06:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:48:56,445 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.5s)
Sep 13 06:49:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:26,413 main INFO screen NUT pass=1 dev=0.0 ins=3.22 pro=77 1a=False 1b=False 2=False (63.9s)
Sep 13 06:49:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:30,009 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (48.4s)
Sep 13 06:49:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:49:37,266 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:49:37 +0000] "GET /health HTTP/1.1" 200 492 "-" "Python-urllib/3.14"
Sep 13 06:50:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:50:56,426 main INFO screen PBJT pass=1 dev=0.0 ins=6.67 pro=57 1a=False 1b=False 2=False (68.3s)
Sep 13 06:50:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:50:58,916 main INFO screen EMPIPE pass=0 dev=0.14 ins=79.2 pro=8 1a=False 1b=False 2=True (65.5s)
Sep 13 06:53:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:53:46,365 main INFO screen ponks pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (60.7s)
Sep 13 06:54:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:54:04,297 main INFO screen Nutsack pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=True (61.1s)
Sep 13 06:54:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:54:53,289 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:54:53 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 13 06:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:56:01,147 main INFO screen PUMP pass=0 dev=0.0 ins=35.85 pro=73 1a=False 1b=False 2=True (67.0s)
Sep 13 06:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:56:39,482 main INFO screen Heist pass=0 dev=0.0 ins=18.19 pro=44 1a=False 1b=False 2=True (69.4s)
Sep 13 06:57:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:57:25,324 main INFO screen dddd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.0s)
Sep 13 06:58:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:58:21,469 main INFO screen HOLDINGS pass=1 dev=0.0 ins=1.74 pro=22 1a=False 1b=False 2=False (70.4s)
Sep 13 07:00:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:06,596 main INFO screen PEPEHOUSE pass=0 dev=0.07 ins=79.24 pro=6 1a=False 1b=False 2=True (78.2s)
Sep 13 07:00:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:10,045 main INFO screen agent pass=1 dev=0.0 ins=1.61 pro=66 1a=False 1b=False 2=False (86.4s)
Sep 13 07:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:23,101 main INFO screen BALI pass=1 dev=0.21 ins=0.0 pro=10 1a=False 1b=False 2=False (74.0s)
Sep 13 07:00:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:00:36,118 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:00:36 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 13 07:01:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:01:04,225 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 13 07:01:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:01:26,002 main INFO screen 男人 pass=0 dev=0.0 ins=27.12 pro=58 1a=False 1b=False 2=True (65.4s)
Sep 13 07:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:04,382 main INFO screen LILI pass=0 dev=0.0 ins=12.88 pro=52 1a=False 1b=False 2=True (72.4s)
Sep 13 07:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:21,225 main INFO screen mmrich pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (58.3s)
Sep 13 07:02:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:02:53,073 main INFO screen PRINCESSV pass=0 dev=0.06 ins=0.0 pro=6 1a=False 1b=False 2=False (70.4s)
Sep 13 07:05:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:01,206 main INFO screen ANONPUMP pass=0 dev=0.04 ins=77.96 pro=8 1a=False 1b=True 2=True (55.2s)
Sep 13 07:05:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:16,695 main INFO screen NIGER pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (48.2s)
Sep 13 07:05:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:05:37,160 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:05:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:06:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:06:05,253 main INFO screen SS pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=True (48.8s)
Sep 13 07:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:08:37,203 main INFO screen sirpump pass=0 dev=0.11 ins=79.2 pro=9 1a=False 1b=True 2=True (54.3s)
Sep 13 07:09:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:07,392 main INFO screen SAVPIR pass=0 dev=7.97 ins=0.0 pro=6 1a=False 1b=False 2=False (79.9s)
Sep 13 07:09:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:30,524 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (61.7s)
Sep 13 07:09:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:09:49,335 main INFO screen PSYCHO pass=0 dev=1.57 ins=0.0 pro=1 1a=False 1b=False 2=False (72.1s)
Sep 13 07:10:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:10:40,021 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:10:40 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 13 07:11:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:11:55,820 main INFO screen GROK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (63.0s)
Sep 13 07:12:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:12:01,057 main INFO screen ASI pass=0 dev=0.0 ins=30.95 pro=41 1a=False 1b=False 2=True (60.3s)
Sep 13 07:12:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:12:32,588 main INFO screen PFS pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (69.5s)
Sep 13 07:13:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:03,094 main INFO screen GHOSTDOG pass=0 dev=35.46 ins=0.0 pro=2 1a=False 1b=False 2=True (67.3s)
Sep 13 07:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:11,067 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.0s)
Sep 13 07:13:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:13:52,391 main INFO screen ASI pass=1 dev=0.0 ins=1.35 pro=73 1a=False 1b=False 2=False (79.8s)
Sep 13 07:14:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:14:56,002 main INFO screen Pepex pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.6s)
Sep 13 07:16:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 07:16:11,466 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:07:16:11 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T06:03:08Z
--- update 2026-09-13T06:08:19Z
--- update 2026-09-13T06:13:23Z
--- update 2026-09-13T06:18:36Z
--- update 2026-09-13T06:23:39Z
--- update 2026-09-13T06:28:57Z
--- update 2026-09-13T06:34:02Z
nieuwe code: e5a2860
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: a7e508db89c149a5bfe6a64d43f3bf81
analyses gestart (53ca44e52d90)
--- update 2026-09-13T06:39:07Z
--- update 2026-09-13T06:44:11Z
--- update 2026-09-13T06:49:36Z
--- update 2026-09-13T06:54:52Z
--- update 2026-09-13T07:00:35Z
--- update 2026-09-13T07:05:36Z
--- update 2026-09-13T07:10:38Z
--- update 2026-09-13T07:16:10Z
```

## Analyses (laatste 25 regels)
```
inactive
06:46:08   12000 tokens, 1331240 trades, 213061 posities (13s)
06:46:10   14000 tokens, 1550375 trades, 248713 posities (15s)
06:46:12   16000 tokens, 1770321 trades, 284135 posities (17s)
06:46:14   18000 tokens, 2028443 trades, 332786 posities (19s)
06:46:16   20000 tokens, 2261098 trades, 373667 posities (21s)
06:46:18   22000 tokens, 2469423 trades, 403595 posities (23s)
06:46:20   24000 tokens, 2690715 trades, 437685 posities (25s)
06:46:22   26000 tokens, 2927736 trades, 478556 posities (26s)
06:46:23   28000 tokens, 3147534 trades, 510862 posities (28s)
06:46:25   30000 tokens, 3360931 trades, 544389 posities (30s)
06:46:27   32000 tokens, 3602222 trades, 587266 posities (32s)
06:46:29   34000 tokens, 3828453 trades, 623402 posities (34s)
06:46:31   36000 tokens, 4041222 trades, 655838 posities (36s)
06:46:33   38000 tokens, 4264353 trades, 692910 posities (37s)
06:46:35   40000 tokens, 4481113 trades, 729064 posities (39s)
06:46:36   42000 tokens, 4702532 trades, 765628 posities (41s)
06:46:39   44000 tokens, 4944450 trades, 808280 posities (43s)
06:46:41   46000 tokens, 5177530 trades, 847648 posities (46s)
06:46:43   48000 tokens, 5408790 trades, 895593 posities (48s)
06:46:45 posities: 930082 uit 5575165 trades (50s)
06:46:56 194340 wallets gerekend
06:46:57 geluk-toets
06:47:32 persistentie
06:47:34 kopieer-simulatie
06:47:56 klaar in 121s -> /opt/schaduwbot/reports/wallets.md
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
