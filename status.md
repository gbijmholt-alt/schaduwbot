# Schaduwbot status

- tijd: 2026-09-14 16:41:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 2 hours, 54 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.0G/38G | geheugen: 1914/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 122835, "tokens_in_memory": 6761, "msgs": 15510630, "trades": 3386459, "creates": 34716, "decode_fail": 288107, "rpc_calls": 101339, "rpc_errors": 7, "sol_usd": 102.40055043200941, "open_positions": 97, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 16:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:18:00,551 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 14 16:19:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:05,392 main INFO screen $GOLD pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (74.3s)
Sep 14 16:19:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:06,933 main INFO screen KERALAM pass=0 dev=0.0 ins=42.35 pro=38 1a=False 1b=False 2=True (66.8s)
Sep 14 16:19:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:14,763 main INFO screen /what_if pass=0 dev=0.0 ins=27.13 pro=64 1a=False 1b=False 2=True (74.2s)
Sep 14 16:19:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:51,183 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:19:51 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 16:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:19:55,304 main INFO screen /what_if pass=0 dev=0.0 ins=39.22 pro=18 1a=False 1b=False 2=True (48.4s)
Sep 14 16:20:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:04,441 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 14 16:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:16,069 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.3s)
Sep 14 16:20:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:46,584 main INFO screen BMW pass=0 dev=0.0 ins=138.39 pro=1 1a=False 1b=False 2=True (51.3s)
Sep 14 16:20:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:20:57,781 main INFO screen Cody pass=1 dev=0.0 ins=19.84 pro=21 1a=False 1b=False 2=False (53.3s)
Sep 14 16:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:21:20,777 main INFO screen Sage pass=0 dev=0.0 ins=8.13 pro=63 1a=False 1b=False 2=True (64.7s)
Sep 14 16:22:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:01,355 main INFO screen BIGTITYCO pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.8s)
Sep 14 16:22:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:14,127 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.3s)
Sep 14 16:22:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:22:25,156 main INFO screen chrisbrocc pass=0 dev=0.07 ins=79.2 pro=1 1a=False 1b=True 2=True (64.4s)
Sep 14 16:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:17,338 main INFO screen Cody pass=0 dev=0.0 ins=20.1 pro=28 1a=False 1b=False 2=True (76.0s)
Sep 14 16:23:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:21,228 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.1s)
Sep 14 16:23:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:23:24,170 main INFO screen Emil pass=0 dev=0.0 ins=18.32 pro=28 1a=False 1b=False 2=True (59.0s)
Sep 14 16:24:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:16,897 main INFO screen HOGEY pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (59.6s)
Sep 14 16:24:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:22,757 main INFO screen GOLDGOOSE pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (61.5s)
Sep 14 16:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:24:35,895 main INFO screen FOMO pass=0 dev=79.31 ins=79.31 pro=0 1a=False 1b=False 2=True (71.7s)
Sep 14 16:25:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:25:19,111 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:25:19 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 16:25:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:25:20,648 main INFO screen BIKETROLL pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (63.8s)
Sep 14 16:25:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:25:24,632 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.9s)
Sep 14 16:25:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:25:38,282 main INFO screen Dogecoin pass=0 dev=79.31 ins=158.5 pro=1 1a=False 1b=False 2=True (62.4s)
Sep 14 16:26:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:26:30,147 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.5s)
Sep 14 16:26:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:26:39,467 main INFO screen Quanthrop pass=1 dev=0.0 ins=4.95 pro=39 1a=False 1b=False 2=False (74.8s)
Sep 14 16:26:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:26:47,891 main INFO screen XRPp pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (69.6s)
Sep 14 16:27:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:27:36,205 main INFO screen Taxcoin pass=0 dev=0.0 ins=47.08 pro=38 1a=False 1b=False 2=True (66.1s)
Sep 14 16:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:27:41,136 main INFO screen AI pass=0 dev=0.0 ins=29.8 pro=66 1a=False 1b=False 2=True (61.7s)
Sep 14 16:28:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:28:02,219 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.3s)
Sep 14 16:28:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:28:45,463 main INFO screen GREMLIN pass=0 dev=0.01 ins=0.0 pro=5 1a=False 1b=False 2=False (64.3s)
Sep 14 16:28:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:28:51,286 main INFO screen AI pass=0 dev=0.0 ins=20.62 pro=3 1a=False 1b=False 2=False (75.1s)
Sep 14 16:29:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:29:05,224 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 14 16:29:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:29:46,360 main INFO screen FASTTTTTT pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (60.9s)
Sep 14 16:29:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:29:56,962 main INFO screen SOLANGELES pass=0 dev=0.0 ins=49.01 pro=29 1a=False 1b=False 2=True (65.7s)
Sep 14 16:30:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:30:14,790 main INFO screen gptstonks pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=False 2=True (69.6s)
Sep 14 16:30:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:30:37,701 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:30:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 16:30:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:30:44,001 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 14 16:30:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:30:54,395 main INFO screen WHEEL TYSON pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (57.4s)
Sep 14 16:31:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:31:11,932 main INFO screen FlyBrain pass=0 dev=0.0 ins=55.52 pro=53 1a=False 1b=False 2=True (57.1s)
Sep 14 16:31:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:31:42,493 main INFO screen fuelcoin pass=0 dev=0.0 ins=14.91 pro=42 1a=False 1b=False 2=True (58.5s)
Sep 14 16:31:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:31:55,440 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.0s)
Sep 14 16:32:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:32:07,372 main INFO screen bolsonaro pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.4s)
Sep 14 16:32:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:32:50,851 main INFO screen FlyBrain pass=1 dev=0.0 ins=11.38 pro=49 1a=False 1b=False 2=False (68.4s)
Sep 14 16:33:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:33:02,476 main INFO screen 穷狗 pass=0 dev=0.0 ins=26.82 pro=52 1a=False 1b=False 2=True (67.0s)
Sep 14 16:33:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:33:11,043 main INFO screen BIKESEM pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=True (63.7s)
Sep 14 16:33:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:33:46,152 main INFO screen 穷狗 pass=0 dev=0.0 ins=18.32 pro=3 1a=False 1b=False 2=True (55.3s)
Sep 14 16:33:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:33:59,906 main INFO screen spx4200 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 14 16:34:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:34:07,401 main INFO screen FUM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:35:21,498 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 16:35:21 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 16:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:35:40,102 main INFO screen CHOGE pass=0 dev=0.0 ins=20.36 pro=9 1a=False 1b=False 2=False (100.2s)
Sep 14 16:35:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:35:41,585 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (115.4s)
Sep 14 16:35:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:35:58,733 main INFO screen DONALD pass=1 dev=0.0 ins=0.65 pro=51 1a=False 1b=False 2=False (111.3s)
Sep 14 16:36:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:36:17,258 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:36:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 16:36:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:36:41,438 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 14 16:36:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:36:47,493 main INFO screen Eat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 14 16:37:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:37:03,957 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.2s)
Sep 14 16:37:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:37:47,831 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (66.4s)
Sep 14 16:37:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:37:56,358 main INFO screen Elon pass=0 dev=0.0 ins=28.87 pro=62 1a=False 1b=False 2=True (68.9s)
Sep 14 16:38:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:38:22,454 main INFO screen Puter pass=0 dev=0.0 ins=20.38 pro=30 1a=False 1b=False 2=False (78.5s)
Sep 14 16:38:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:38:50,989 main INFO screen Elon pass=0 dev=0.0 ins=21.49 pro=7 1a=False 1b=False 2=True (54.6s)
Sep 14 16:38:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:38:53,062 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.2s)
Sep 14 16:39:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:39:15,519 main INFO screen Dust pass=0 dev=0.0 ins=50.41 pro=16 1a=False 1b=False 2=True (53.1s)
Sep 14 16:39:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:39:42,189 main INFO screen gy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.2s)
Sep 14 16:39:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:39:43,184 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.1s)
Sep 14 16:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:40:06,883 main INFO screen Elon pass=0 dev=0.0 ins=21.65 pro=33 1a=False 1b=False 2=False (51.4s)
Sep 14 16:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:40:46,202 main INFO screen ALAWN pass=0 dev=0.0 ins=28.39 pro=32 1a=False 1b=False 2=True (64.0s)
Sep 14 16:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:40:46,891 main INFO screen DripCat pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.7s)
Sep 14 16:40:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:40:55,359 main INFO screen Bell pass=0 dev=6.95 ins=0.0 pro=47 1a=False 1b=True 2=False (48.5s)
Sep 14 16:41:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:41:23,203 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:16:41:23 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T15:12:26Z
--- update 2026-09-14T15:17:27Z
--- update 2026-09-14T15:22:36Z
--- update 2026-09-14T15:28:10Z
--- update 2026-09-14T15:33:36Z
--- update 2026-09-14T15:38:40Z
--- update 2026-09-14T15:43:41Z
--- update 2026-09-14T15:48:53Z
--- update 2026-09-14T15:54:27Z
Running as unit: schaduwbot-wallets.service; invocation ID: bb9b36ab53964518996f9300eff1d4cf
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T15:59:36Z
--- update 2026-09-14T16:04:41Z
--- update 2026-09-14T16:09:46Z
--- update 2026-09-14T16:14:46Z
--- update 2026-09-14T16:19:50Z
--- update 2026-09-14T16:25:17Z
--- update 2026-09-14T16:30:36Z
--- update 2026-09-14T16:36:15Z
--- update 2026-09-14T16:41:21Z
```

## Analyses (laatste 25 regels)
```
inactive
16:33:38   34000 tokens, 3432567 trades, 425634 posities (227s)
16:33:53   36000 tokens, 3644007 trades, 450026 posities (242s)
16:34:08   38000 tokens, 3848659 trades, 478377 posities (256s)
16:34:22   40000 tokens, 4046955 trades, 500997 posities (271s)
16:34:35   42000 tokens, 4222952 trades, 519780 posities (283s)
16:34:47   44000 tokens, 4418580 trades, 544143 posities (295s)
16:34:58   46000 tokens, 4610884 trades, 567679 posities (307s)
16:35:10   48000 tokens, 4822586 trades, 593054 posities (319s)
16:35:22   50000 tokens, 5034610 trades, 619442 posities (330s)
16:35:33   52000 tokens, 5213503 trades, 638616 posities (341s)
16:35:45   54000 tokens, 5392064 trades, 660041 posities (353s)
16:35:58   56000 tokens, 5596181 trades, 686230 posities (366s)
16:36:09   58000 tokens, 5774359 trades, 706776 posities (378s)
16:36:23   60000 tokens, 6000078 trades, 737951 posities (392s)
16:36:36   62000 tokens, 6182781 trades, 763126 posities (404s)
16:36:50   64000 tokens, 6399806 trades, 792698 posities (419s)
16:37:03   66000 tokens, 6596383 trades, 817546 posities (432s)
16:37:16   68000 tokens, 6798262 trades, 845064 posities (445s)
16:37:30   70000 tokens, 7001931 trades, 881382 posities (458s)
16:37:40 posities: 900358 uit 7154599 trades (470s)
16:37:52 200540 wallets gerekend
16:37:52 geluk-toets
16:38:27 persistentie
16:38:29 kopieer-simulatie
16:40:34 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
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
16:30:37 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:36:18 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
