# Schaduwbot status

- tijd: 2026-09-15 17:38:51 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 3 hours, 51 minutes
- bot-service: active
- code-versie: 3840d00
- schijf: 7.4G/38G | geheugen: 2258/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 212683, "tokens_in_memory": 9255, "msgs": 31814309, "trades": 6618267, "creates": 70366, "decode_fail": 562394, "rpc_calls": 190788, "rpc_errors": 16, "sol_usd": 100.02855631333728, "open_positions": 46, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 17:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:16:37,243 main INFO screen CABAL pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=True (65.7s)
Sep 15 17:17:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:17:11,284 main INFO screen POST pass=0 dev=0.0 ins=19.2 pro=3 1a=False 1b=False 2=False (62.5s)
Sep 15 17:17:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:17:25,969 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (56.7s)
Sep 15 17:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:17:34,693 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.4s)
Sep 15 17:18:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:18:06,795 main INFO screen CR7 pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (55.5s)
Sep 15 17:18:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:18:35,009 main INFO screen Foreskin pass=0 dev=0.0 ins=11.09 pro=50 1a=False 1b=False 2=False (69.0s)
Sep 15 17:18:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:18:37,255 main INFO screen RWA pass=0 dev=0.0 ins=45.07 pro=20 1a=False 1b=False 2=True (62.6s)
Sep 15 17:18:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:18:41,783 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:18:41 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 17:19:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:19:16,670 main INFO screen HERO pass=0 dev=0.0 ins=20.31 pro=62 1a=False 1b=False 2=False (69.9s)
Sep 15 17:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:19:35,104 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.8s)
Sep 15 17:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:19:35,254 main INFO screen $GTA6 pass=0 dev=0.0 ins=1.04 pro=7 1a=False 1b=False 2=False (60.2s)
Sep 15 17:20:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:20:04,881 aiohttp.access INFO 217.60.195.128 [15/Sep/2026:17:20:04 +0000] "POST /v1/messages HTTP/1.1" 404 193 "-" "claude-code/1.x"
Sep 15 17:20:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:20:13,322 main INFO screen sol pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (56.7s)
Sep 15 17:20:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:20:27,496 main INFO screen HEY pass=0 dev=0.0 ins=31.18 pro=17 1a=False 1b=False 2=True (52.2s)
Sep 15 17:20:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:20:32,730 main INFO screen TRUMP pass=0 dev=0.0 ins=25.3 pro=3 1a=False 1b=False 2=True (57.6s)
Sep 15 17:21:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:21:21,998 main INFO screen SIMPLE pass=0 dev=0.0 ins=32.86 pro=58 1a=False 1b=False 2=True (68.7s)
Sep 15 17:21:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:21:27,145 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.6s)
Sep 15 17:21:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:21:38,390 main INFO screen $DURACELL pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (65.7s)
Sep 15 17:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:22:17,884 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.9s)
Sep 15 17:22:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:22:22,312 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (55.2s)
Sep 15 17:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:22:31,506 main INFO screen NDX pass=0 dev=0.0 ins=28.81 pro=7 1a=False 1b=False 2=False (53.1s)
Sep 15 17:23:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:23:12,335 main INFO screen BIGWEEK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.4s)
Sep 15 17:23:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:23:23,026 main INFO screen 69 pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (60.7s)
Sep 15 17:23:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:23:29,318 main INFO screen 🟢 pass=0 dev=0.0 ins=54.15 pro=26 1a=False 1b=False 2=True (57.8s)
Sep 15 17:23:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:23:43,148 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:23:43 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 15 17:24:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:24:07,441 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.1s)
Sep 15 17:24:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:24:19,470 main INFO screen CLIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 15 17:24:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:24:25,768 main INFO screen PEPE pass=0 dev=0.0 ins=0.24 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 15 17:25:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:25:01,735 main INFO screen Starbucks pass=0 dev=0.0 ins=173.25 pro=0 1a=False 1b=False 2=True (54.3s)
Sep 15 17:25:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:25:35,664 main INFO screen TechCat pass=0 dev=0.0 ins=0.34 pro=58 1a=False 1b=False 2=False (76.2s)
Sep 15 17:25:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:25:39,246 main INFO screen icecube pass=0 dev=0.0 ins=78.96 pro=4 1a=False 1b=False 2=True (73.5s)
Sep 15 17:26:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:26:06,209 main INFO screen TechCat pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (64.5s)
Sep 15 17:26:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:26:28,339 main INFO screen SATOSHI pass=0 dev=0.0 ins=20.25 pro=5 1a=False 1b=False 2=True (52.7s)
Sep 15 17:26:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:26:36,575 main INFO screen SATOSHI pass=0 dev=0.0 ins=49.87 pro=3 1a=False 1b=False 2=True (57.3s)
Sep 15 17:27:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:27:04,015 main INFO screen MB pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.8s)
Sep 15 17:27:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:27:27,181 main INFO screen wifGPT pass=0 dev=0.0 ins=79.13 pro=7 1a=False 1b=True 2=True (58.8s)
Sep 15 17:27:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:27:44,712 main INFO screen SHARK pass=0 dev=0.62 ins=0.0 pro=14 1a=False 1b=False 2=False (68.1s)
Sep 15 17:28:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:28:02,293 main INFO screen MEMES pass=0 dev=0.0 ins=28.43 pro=13 1a=False 1b=False 2=False (58.3s)
Sep 15 17:28:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:28:28,566 main INFO screen COAT pass=0 dev=0.0 ins=32.44 pro=52 1a=False 1b=False 2=True (61.4s)
Sep 15 17:28:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:28:37,158 main INFO screen SOLSHAPES pass=0 dev=0.0 ins=48.72 pro=23 1a=False 1b=False 2=True (52.4s)
Sep 15 17:28:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:28:50,652 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:28:50 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 17:28:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:28:56,637 main INFO screen SOLROCKET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.3s)
Sep 15 17:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:29:36,703 main INFO screen SATOSHI pass=0 dev=0.0 ins=31.63 pro=86 1a=False 1b=False 2=True (68.1s)
Sep 15 17:29:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:29:43,026 main INFO screen CATA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 15 17:29:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:29:51,327 main INFO screen KENDUCK pass=0 dev=0.0 ins=6.26 pro=7 1a=False 1b=False 2=False (54.7s)
Sep 15 17:30:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:30:31,330 main INFO screen O’SEAL pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (54.6s)
Sep 15 17:30:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:30:39,070 main INFO screen DONGDING pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.0s)
Sep 15 17:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:30:48,093 main INFO screen IRIDO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.8s)
Sep 15 17:31:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:31:25,479 main INFO screen ftgg pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (54.1s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T16:23:21Z
--- update 2026-09-15T16:28:23Z
--- update 2026-09-15T16:33:24Z
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
17:09:01 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=253 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:09:01 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 11/40/153 | al gemeten: 658
17:13:46 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=255 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:13:46 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 9/39/153 | al gemeten: 660
17:19:00 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=259 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:19:00 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 9/39/151 | al gemeten: 664
17:23:55 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=260 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:23:55 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 10/40/153 | al gemeten: 667
17:28:59 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=261 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:28:59 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 9/39/150 | al gemeten: 669
17:34:21 ijk: +6 van 7 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=266 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:34:21 ijk-diagnose: nieuwste migratie 1.6 min oud | migraties 15/60/240 min: 12/40/155 | al gemeten: 675
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
