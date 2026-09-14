# Schaduwbot status

- tijd: 2026-09-14 13:39:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 23 hours, 52 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.7G/38G | geheugen: 1909/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 111927, "tokens_in_memory": 5118, "msgs": 13128729, "trades": 2989851, "creates": 30613, "decode_fail": 250785, "rpc_calls": 90327, "rpc_errors": 7, "sol_usd": 101.38976068898062, "open_positions": 84, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 13:18:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:18:17,117 main INFO screen ISV pass=0 dev=0.0 ins=28.21 pro=67 1a=False 1b=False 2=True (55.7s)
Sep 14 13:18:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:18:17,725 main INFO screen stankmemes pass=1 dev=0.0 ins=17.77 pro=32 1a=False 1b=False 2=False (57.1s)
Sep 14 13:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:18:23,126 main INFO screen OpenAI pass=0 dev=0.0 ins=73.6 pro=1 1a=False 1b=False 2=True (57.1s)
Sep 14 13:18:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:18:55,222 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:18:55 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:19:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:19:11,325 main INFO screen Etcamah pass=0 dev=0.0 ins=24.33 pro=35 1a=False 1b=False 2=True (53.6s)
Sep 14 13:19:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:19:12,786 main INFO screen JUSTICE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (55.7s)
Sep 14 13:19:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:19:20,608 main INFO screen FLORA pass=0 dev=0.0 ins=20.1 pro=69 1a=False 1b=False 2=True (57.5s)
Sep 14 13:20:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:20:19,367 main INFO screen MOONER pass=1 dev=0.0 ins=16.68 pro=40 1a=False 1b=False 2=False (58.8s)
Sep 14 13:20:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:20:19,420 main INFO screen DOOYET pass=0 dev=0.05 ins=0.0 pro=6 1a=False 1b=False 2=False (68.1s)
Sep 14 13:20:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:20:24,019 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (71.2s)
Sep 14 13:21:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:21:26,347 main INFO screen E91 pass=0 dev=0.0 ins=21.91 pro=46 1a=False 1b=False 2=True (67.0s)
Sep 14 13:21:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:21:26,646 main INFO screen MINIME pass=0 dev=2.0 ins=30.75 pro=39 1a=False 1b=False 2=True (67.2s)
Sep 14 13:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:21:29,201 main INFO screen ALL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (65.2s)
Sep 14 13:22:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:22:23,804 main INFO screen BBC pass=0 dev=0.0 ins=175.41 pro=1 1a=False 1b=False 2=True (57.5s)
Sep 14 13:22:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:22:37,900 main INFO screen PUMPDOG pass=0 dev=0.0 ins=20.35 pro=22 1a=False 1b=False 2=False (71.3s)
Sep 14 13:22:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:22:37,981 main INFO screen INF pass=0 dev=0.0 ins=25.62 pro=22 1a=False 1b=False 2=True (68.8s)
Sep 14 13:23:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:23:20,887 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.1s)
Sep 14 13:23:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:23:27,961 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.1s)
Sep 14 13:23:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:23:38,163 main INFO screen wind pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (60.2s)
Sep 14 13:23:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:23:57,513 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:23:57 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:24:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:24:28,622 main INFO screen DJT pass=0 dev=0.0 ins=17.32 pro=46 1a=False 1b=False 2=True (67.7s)
Sep 14 13:24:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:24:34,586 main INFO screen ソル pass=0 dev=0.0 ins=33.52 pro=30 1a=False 1b=False 2=True (66.6s)
Sep 14 13:24:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:24:41,313 main INFO screen PUMPTYSON pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (63.1s)
Sep 14 13:25:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:25:26,754 main INFO screen Cock pass=0 dev=0.0 ins=0.06 pro=2 1a=False 1b=False 2=True (58.1s)
Sep 14 13:25:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:25:43,883 main INFO screen ANITA pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (69.3s)
Sep 14 13:25:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:25:48,363 main INFO screen KSC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.0s)
Sep 14 13:26:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:26:36,637 main INFO screen SOLANA pass=0 dev=0.0 ins=30.71 pro=68 1a=False 1b=False 2=True (69.9s)
Sep 14 13:26:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:26:52,892 main INFO screen SOLANA pass=0 dev=0.0 ins=19.31 pro=27 1a=False 1b=False 2=True (64.5s)
Sep 14 13:26:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:26:55,202 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (71.3s)
Sep 14 13:27:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:27:49,405 main INFO screen SOLANA pass=0 dev=0.0 ins=20.65 pro=31 1a=False 1b=False 2=True (72.8s)
Sep 14 13:27:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:27:59,350 main INFO screen KIBA pass=0 dev=0.0 ins=124.89 pro=1 1a=False 1b=False 2=True (64.1s)
Sep 14 13:28:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:28:12,056 main INFO screen RUG pass=0 dev=0.21 ins=0.0 pro=7 1a=False 1b=False 2=False (79.2s)
Sep 14 13:28:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:28:51,837 main INFO screen SOLANA pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (62.4s)
Sep 14 13:29:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:00,093 main INFO screen OpenAI pass=0 dev=0.0 ins=143.1 pro=1 1a=False 1b=False 2=True (60.7s)
Sep 14 13:29:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:21,034 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:29:21 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:29:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:34,240 main INFO screen BlackCate pass=0 dev=67.56 ins=0.0 pro=6 1a=False 1b=False 2=True (82.2s)
Sep 14 13:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:36,256 aiohttp.access INFO 151.245.151.239 [14/Sep/2026:13:29:36 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; ForestEngine/1.0; +https://forestengine.net/)"
Sep 14 13:29:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:36,273 aiohttp.access INFO 151.245.151.239 [14/Sep/2026:13:29:36 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; ForestEngine/1.0; +https://forestengine.net/)"
Sep 14 13:29:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:55,440 aiohttp.access INFO 103.74.20.116 [14/Sep/2026:13:29:55 +0000] "GET /boaform/admin/formLogin?username=user&psd=user HTTP/1.0" 404 174 "-" "-"
Sep 14 13:29:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:29:57,003 main INFO screen Foreskin pass=1 dev=0.0 ins=11.09 pro=42 1a=False 1b=False 2=False (65.2s)
Sep 14 13:30:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:30:10,481 main INFO screen CHEESEBURGER pass=0 dev=0.0 ins=20.92 pro=29 1a=False 1b=False 2=False (70.4s)
Sep 14 13:30:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:30:39,912 main INFO screen SINGULARITY pass=0 dev=0.0 ins=27.39 pro=69 1a=False 1b=False 2=True (65.7s)
Sep 14 13:30:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:30:50,181 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 13:31:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:31:21,391 main INFO screen P&G pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (70.9s)
Sep 14 13:31:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:31:38,825 main INFO screen MCAT pass=0 dev=0.0 ins=28.95 pro=54 1a=False 1b=False 2=True (58.9s)
Sep 14 13:31:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:31:50,377 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.2s)
Sep 14 13:32:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:32:15,574 main INFO screen MCAT pass=0 dev=0.0 ins=32.49 pro=30 1a=False 1b=False 2=True (54.2s)
Sep 14 13:32:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:32:37,243 main INFO screen ALTO pass=1 dev=0.0 ins=19.36 pro=36 1a=False 1b=False 2=False (58.4s)
Sep 14 13:32:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:32:43,042 main INFO screen slowlana pass=0 dev=0.0 ins=19.85 pro=24 1a=False 1b=False 2=True (52.7s)
Sep 14 13:33:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:33:06,871 main INFO screen LOL pass=0 dev=0.0 ins=19.15 pro=2 1a=False 1b=False 2=False (51.3s)
Sep 14 13:33:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:33:38,539 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 14 13:33:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:33:39,165 main INFO screen dd pass=0 dev=1.85 ins=0.0 pro=2 1a=False 1b=False 2=False (56.1s)
Sep 14 13:33:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:33:55,981 main INFO screen NEST pass=0 dev=0.0 ins=31.1 pro=22 1a=False 1b=False 2=True (49.1s)
Sep 14 13:34:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:34:22,556 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:34:22 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:35:20,477 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 13:35:20 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 13:35:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:35:43,396 main INFO screen Phytos pass=1 dev=0.0 ins=11.38 pro=59 1a=False 1b=False 2=False (124.9s)
Sep 14 13:35:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:35:50,668 main INFO screen kirkified pass=1 dev=0.0 ins=17.88 pro=60 1a=False 1b=False 2=False (131.5s)
Sep 14 13:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:35:55,700 main INFO screen ElonCoin pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (119.7s)
Sep 14 13:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:36:36,528 main INFO screen WORKS
Sep 14 13:36:36 ubuntu-4gb-fsn1-1 python[86554]:  pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (53.1s)
Sep 14 13:36:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:36:44,488 main INFO screen SAILOR pass=0 dev=0.0 ins=79.24 pro=1 1a=False 1b=True 2=True (53.8s)
Sep 14 13:36:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:36:52,167 main INFO screen Redbull pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 14 13:37:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:37:13,506 aiohttp.access INFO 13.205.173.126 [14/Sep/2026:13:37:13 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0"
Sep 14 13:37:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:37:50,788 main INFO screen XD pass=0 dev=0.0 ins=16.11 pro=45 1a=False 1b=False 2=True (66.3s)
Sep 14 13:37:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:37:51,180 main INFO screen Meow pass=0 dev=0.0 ins=20.29 pro=34 1a=False 1b=False 2=True (74.7s)
Sep 14 13:37:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:37:59,533 main INFO screen Papoy pass=0 dev=0.0 ins=27.89 pro=53 1a=False 1b=False 2=True (67.4s)
Sep 14 13:38:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:38:45,125 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.3s)
Sep 14 13:38:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:38:47,200 main INFO screen solcat pass=0 dev=0.0 ins=79.17 pro=3 1a=False 1b=True 2=True (56.0s)
Sep 14 13:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:39:07,397 main INFO screen $PACJ pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (67.9s)
Sep 14 13:39:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:39:34,772 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:39:34 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T11:59:52Z
--- update 2026-09-14T12:04:53Z
--- update 2026-09-14T12:09:58Z
--- update 2026-09-14T12:15:25Z
--- update 2026-09-14T12:20:36Z
--- update 2026-09-14T12:26:18Z
--- update 2026-09-14T12:31:36Z
--- update 2026-09-14T12:36:40Z
--- update 2026-09-14T12:41:54Z
--- update 2026-09-14T12:47:08Z
--- update 2026-09-14T12:52:27Z
--- update 2026-09-14T12:57:36Z
--- update 2026-09-14T13:03:06Z
--- update 2026-09-14T13:08:21Z
--- update 2026-09-14T13:13:36Z
--- update 2026-09-14T13:18:54Z
--- update 2026-09-14T13:23:56Z
--- update 2026-09-14T13:29:19Z
--- update 2026-09-14T13:34:21Z
--- update 2026-09-14T13:39:33Z
```

## Analyses (laatste 25 regels)
```
inactive
12:24:10   34000 tokens, 3435601 trades, 426342 posities (209s)
12:24:25   36000 tokens, 3657840 trades, 454829 posities (224s)
12:24:39   38000 tokens, 3859925 trades, 481486 posities (238s)
12:24:53   40000 tokens, 4059765 trades, 504756 posities (252s)
12:25:05   42000 tokens, 4234354 trades, 524489 posities (264s)
12:25:18   44000 tokens, 4431985 trades, 548318 posities (277s)
12:25:32   46000 tokens, 4626357 trades, 574418 posities (291s)
12:25:46   48000 tokens, 4835116 trades, 597599 posities (305s)
12:25:59   50000 tokens, 5038874 trades, 622075 posities (318s)
12:26:12   52000 tokens, 5223412 trades, 643069 posities (331s)
12:26:25   54000 tokens, 5397845 trades, 660920 posities (344s)
12:26:38   56000 tokens, 5602394 trades, 687587 posities (357s)
12:26:49   58000 tokens, 5776662 trades, 706640 posities (368s)
12:27:01   60000 tokens, 5985201 trades, 736365 posities (380s)
12:27:13   62000 tokens, 6183196 trades, 764072 posities (392s)
12:27:25   64000 tokens, 6394266 trades, 791990 posities (404s)
12:27:37   66000 tokens, 6593931 trades, 817825 posities (416s)
12:27:50   68000 tokens, 6794379 trades, 846287 posities (429s)
12:28:02   70000 tokens, 6990170 trades, 880107 posities (441s)
12:28:09 posities: 896544 uit 7116580 trades (449s)
12:28:22 198620 wallets gerekend
12:28:23 geluk-toets
12:29:00 persistentie
12:29:03 kopieer-simulatie
12:31:05 klaar in 624s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
12:41:55 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:47:09 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:52:28 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
12:57:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:03:06 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:08:22 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:13:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:18:54 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:23:57 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:29:20 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:34:24 ijk: +1 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
13:39:34 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
