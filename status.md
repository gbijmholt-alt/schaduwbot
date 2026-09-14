# Schaduwbot status

- tijd: 2026-09-14 13:49:56 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 2 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.7G/38G | geheugen: 1929/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 112548, "tokens_in_memory": 5212, "msgs": 13205988, "trades": 3009439, "creates": 30866, "decode_fail": 253284, "rpc_calls": 90958, "rpc_errors": 7, "sol_usd": 101.73982690619489, "open_positions": 65, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 13:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:39:35,699 main INFO screen TRYPSIN pass=0 dev=0.0 ins=17.75 pro=20 1a=False 1b=False 2=True (50.6s)
Sep 14 13:39:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:39:55,009 main INFO screen lam pass=0 dev=0.0 ins=18.75 pro=3 1a=False 1b=False 2=False (67.8s)
Sep 14 13:39:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:39:59,106 main INFO screen PLATYPUS pass=0 dev=0.0 ins=19.41 pro=22 1a=False 1b=False 2=True (51.7s)
Sep 14 13:40:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:40:32,549 main INFO screen leeves pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (56.8s)
Sep 14 13:40:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:40:47,167 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (52.2s)
Sep 14 13:40:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:40:53,555 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.4s)
Sep 14 13:41:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:41:24,323 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.8s)
Sep 14 13:41:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:41:45,701 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 14 13:42:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:42:00,220 main INFO screen delusional pass=1 dev=0.0 ins=19.4 pro=28 1a=False 1b=False 2=False (66.7s)
Sep 14 13:42:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:42:23,641 main INFO screen TASHI pass=0 dev=0.0 ins=1.4 pro=3 1a=False 1b=True 2=False (59.3s)
Sep 14 13:42:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:42:36,462 main INFO screen POTPAL pass=0 dev=42.8 ins=1.85 pro=5 1a=False 1b=False 2=False (50.8s)
Sep 14 13:42:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:42:59,609 main INFO screen Doge4Goat pass=0 dev=0.0 ins=19.43 pro=68 1a=False 1b=False 2=True (59.4s)
Sep 14 13:43:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:43:17,289 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.6s)
Sep 14 13:43:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:43:49,951 main INFO screen PEOPLE pass=0 dev=0.0 ins=21.64 pro=70 1a=False 1b=False 2=True (73.5s)
Sep 14 13:43:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:43:54,180 main INFO screen PEOPLE pass=0 dev=0.0 ins=17.37 pro=79 1a=False 1b=False 2=True (54.6s)
Sep 14 13:44:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:44:17,230 main INFO screen PEOPLE pass=0 dev=0.0 ins=20.46 pro=67 1a=False 1b=False 2=True (59.9s)
Sep 14 13:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:44:37,216 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:44:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:44:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:44:44,633 main INFO screen PEOPLE pass=0 dev=0.0 ins=0.26 pro=15 1a=False 1b=False 2=False (54.7s)
Sep 14 13:44:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:44:52,308 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (58.1s)
Sep 14 13:45:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:16,636 main INFO screen HEISTNVIDI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 14 13:45:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:41,149 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.5s)
Sep 14 13:45:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:44,747 main INFO screen LEMEOW pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.4s)
Sep 14 13:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:12,692 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.1s)
Sep 14 13:46:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:38,272 main INFO screen SPIN pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 13:46:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:42,174 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 14 13:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:10,902 main INFO screen Charlie pass=0 dev=0.0 ins=20.44 pro=70 1a=False 1b=False 2=True (58.2s)
Sep 14 13:47:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:31,428 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 13:47:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:36,840 main INFO screen MESOL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 14 13:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:15,456 main INFO screen BBP pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (64.6s)
Sep 14 13:48:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:22,614 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.2s)
Sep 14 13:48:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:27,241 main INFO screen robinpepe pass=0 dev=0.14 ins=78.78 pro=9 1a=False 1b=True 2=True (50.4s)
Sep 14 13:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:13,605 main INFO screen SUNK pass=0 dev=0.0 ins=26.75 pro=10 1a=False 1b=False 2=True (51.0s)
Sep 14 13:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:20,576 main INFO screen PUMPFAST pass=0 dev=0.0 ins=16.17 pro=64 1a=False 1b=False 2=True (65.1s)
Sep 14 13:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:35,772 main INFO screen POLLY pass=0 dev=0.0 ins=30.99 pro=53 1a=False 1b=False 2=True (68.5s)
Sep 14 13:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:56,630 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:49:56 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T13:44:36Z
--- update 2026-09-14T13:49:55Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7b952af92e094c05ae1443fb1b8f089a
analyses gestart (61d1b06b5cec)
```

## Analyses (laatste 25 regels)
```
active
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
13:44:39 ijk: +1 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
13:49:56 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
