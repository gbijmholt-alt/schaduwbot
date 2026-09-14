# Schaduwbot status

- tijd: 2026-09-14 14:46:59 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 1 hour, 0 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.8G/38G | geheugen: 1938/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 115971, "tokens_in_memory": 5799, "msgs": 14069522, "trades": 3137549, "creates": 32122, "decode_fail": 263367, "rpc_calls": 94382, "rpc_errors": 7, "sol_usd": 101.68322304374259, "open_positions": 56, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 14:24:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:24:46,881 main INFO screen GUMBALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.7s)
Sep 14 14:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:24:49,288 main INFO screen KIBA pass=0 dev=0.0 ins=126.1 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 14 14:25:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:03,862 main INFO screen human pass=0 dev=0.0 ins=20.71 pro=64 1a=False 1b=False 2=True (70.9s)
Sep 14 14:25:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:51,400 main INFO screen WTF pass=0 dev=0.0 ins=75.89 pro=0 1a=True 1b=True 2=True (64.5s)
Sep 14 14:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:52,784 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.64 pro=6 1a=False 1b=False 2=True (63.5s)
Sep 14 14:26:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:26:21,858 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:26:21 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:26:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:26:22,127 main INFO screen CATWAY pass=0 dev=65.65 ins=0.0 pro=11 1a=False 1b=False 2=False (78.3s)
Sep 14 14:27:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:09,994 main INFO screen PUMPERS pass=0 dev=0.0 ins=29.56 pro=71 1a=False 1b=False 2=True (78.6s)
Sep 14 14:27:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:10,408 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (77.6s)
Sep 14 14:27:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:15,947 main INFO screen PUMPERS pass=0 dev=0.0 ins=15.84 pro=15 1a=False 1b=False 2=True (53.8s)
Sep 14 14:28:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:03,556 main INFO screen PUMPERS pass=0 dev=0.0 ins=31.63 pro=45 1a=False 1b=False 2=True (53.1s)
Sep 14 14:28:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:05,306 main INFO screen ROBIN pass=0 dev=0.0 ins=162.79 pro=1 1a=False 1b=False 2=True (55.3s)
Sep 14 14:28:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:14,467 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.63 pro=25 1a=False 1b=False 2=True (58.5s)
Sep 14 14:29:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:16,318 main INFO screen X pass=1 dev=0.0 ins=4.98 pro=56 1a=False 1b=False 2=False (71.0s)
Sep 14 14:29:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:17,201 main INFO screen TIGR pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (73.6s)
Sep 14 14:29:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:28,455 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.0s)
Sep 14 14:30:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:15,731 main INFO screen TRADY pass=0 dev=0.0 ins=55.52 pro=39 1a=True 1b=False 2=True (59.4s)
Sep 14 14:30:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:23,061 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 14 14:30:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:34,107 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.28 pro=41 1a=True 1b=True 2=True (65.7s)
Sep 14 14:31:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:15,191 main INFO screen HIKKO pass=0 dev=0.0 ins=79.1 pro=6 1a=False 1b=True 2=True (59.5s)
Sep 14 14:31:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:32,600 main INFO screen Rack pass=0 dev=0.0 ins=3.4 pro=23 1a=False 1b=False 2=False (58.5s)
Sep 14 14:31:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:37,590 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:31:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:31:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:40,186 main INFO screen DTCNTR pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.1s)
Sep 14 14:32:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:32:26,408 main INFO screen HumanCoin pass=1 dev=0.0 ins=6.49 pro=25 1a=False 1b=False 2=False (71.2s)
Sep 14 14:32:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:32:33,268 aiohttp.access INFO 89.42.231.200 [14/Sep/2026:14:32:33 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 14 14:32:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:32:45,696 main INFO screen LIFE pass=0 dev=0.0 ins=32.55 pro=68 1a=False 1b=False 2=True (73.1s)
Sep 14 14:32:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:32:48,795 main INFO screen LVL pass=0 dev=39.22 ins=0.0 pro=6 1a=False 1b=False 2=False (68.6s)
Sep 14 14:33:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:33:30,396 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.0s)
Sep 14 14:33:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:33:43,225 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 14 14:33:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:33:45,045 main INFO screen headleaf pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:35:21,411 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 14:35:21 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 14:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:35:38,196 main INFO screen FOBE pass=0 dev=0.0 ins=49.99 pro=66 1a=False 1b=False 2=True (127.8s)
Sep 14 14:35:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:35:41,346 main INFO screen FOBE pass=0 dev=0.0 ins=19.55 pro=31 1a=False 1b=False 2=True (116.3s)
Sep 14 14:35:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:35:45,977 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (122.8s)
Sep 14 14:36:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:36:48,911 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:36:48 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 14:36:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:36:50,862 main INFO screen Blind pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (72.7s)
Sep 14 14:36:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:36:51,788 main INFO screen GOAT pass=0 dev=0.0 ins=55.89 pro=60 1a=False 1b=False 2=True (70.4s)
Sep 14 14:36:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:36:55,559 main INFO screen PARODY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.6s)
Sep 14 14:37:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:37:46,220 main INFO screen cro pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.4s)
Sep 14 14:38:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:38:00,820 main INFO screen Carbonoid pass=0 dev=0.0 ins=32.68 pro=60 1a=False 1b=False 2=True (65.3s)
Sep 14 14:38:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:38:05,290 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (73.5s)
Sep 14 14:38:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:38:52,510 main INFO screen Ponsjak pass=0 dev=0.0 ins=79.13 pro=3 1a=False 1b=True 2=True (66.3s)
Sep 14 14:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:39:05,367 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.5s)
Sep 14 14:39:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:39:06,536 main INFO screen SOVDOGE pass=0 dev=0.0 ins=29.28 pro=8 1a=True 1b=True 2=False (61.2s)
Sep 14 14:39:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:39:44,884 aiohttp.access INFO 153.75.81.83 [14/Sep/2026:14:39:44 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0 (compatible; probe/1.0)"
Sep 14 14:40:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:40:01,713 main INFO screen SOLANA pass=0 dev=0.0 ins=30.93 pro=8 1a=False 1b=False 2=True (55.2s)
Sep 14 14:40:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:40:05,729 main INFO screen Orange pass=0 dev=0.0 ins=23.82 pro=40 1a=False 1b=False 2=False (73.2s)
Sep 14 14:40:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:40:11,614 main INFO screen Humans pass=0 dev=0.0 ins=32.05 pro=49 1a=False 1b=False 2=True (66.2s)
Sep 14 14:40:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:40:57,738 main INFO screen LaMisery pass=0 dev=0.02 ins=0.0 pro=7 1a=False 1b=False 2=False (56.0s)
Sep 14 14:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:41:11,088 main INFO screen ADFREE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.4s)
Sep 14 14:41:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:41:16,008 main INFO screen cat pass=0 dev=0.0 ins=27.93 pro=65 1a=False 1b=False 2=True (64.4s)
Sep 14 14:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:41:51,877 main INFO screen GRR pass=0 dev=0.0 ins=28.68 pro=6 1a=True 1b=True 2=False (54.1s)
Sep 14 14:41:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:41:58,205 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:41:58 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:41:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:41:59,289 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (48.2s)
Sep 14 14:42:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:42:07,893 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.9s)
Sep 14 14:42:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:42:43,860 main INFO screen Niall  pass=0 dev=0.0 ins=19.21 pro=66 1a=False 1b=False 2=True (52.0s)
Sep 14 14:42:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:42:51,210 main INFO screen BEAST pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (51.9s)
Sep 14 14:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:43:11,381 main INFO screen NABU pass=0 dev=0.06 ins=0.0 pro=3 1a=False 1b=False 2=False (63.5s)
Sep 14 14:43:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:43:48,575 main INFO screen GORT pass=0 dev=0.0 ins=29.47 pro=37 1a=False 1b=False 2=True (64.7s)
Sep 14 14:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:43:53,208 main INFO screen WOFI pass=0 dev=3.97 ins=93.57 pro=1 1a=False 1b=False 2=True (62.0s)
Sep 14 14:44:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:44:04,340 main INFO screen MEWLIP pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (53.0s)
Sep 14 14:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:44:37,750 main INFO screen FERSPE pass=0 dev=1.18 ins=0.0 pro=1 1a=False 1b=False 2=False (49.2s)
Sep 14 14:44:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:44:41,553 main INFO screen Robinhood pass=0 dev=0.0 ins=146.8 pro=1 1a=False 1b=False 2=True (48.3s)
Sep 14 14:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:45:12,049 main INFO screen DOOROC pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (67.7s)
Sep 14 14:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:45:45,163 main INFO screen StopAI pass=0 dev=0.0 ins=23.71 pro=65 1a=False 1b=False 2=True (67.4s)
Sep 14 14:45:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:45:48,654 main INFO screen SAVPIR pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (67.1s)
Sep 14 14:46:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:46:05,377 main INFO screen AGI pass=0 dev=0.0 ins=22.74 pro=28 1a=False 1b=False 2=False (53.3s)
Sep 14 14:46:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:46:36,741 main INFO screen ROBIN pass=0 dev=0.0 ins=116.82 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 14 14:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:46:37,360 main INFO screen fruitfly pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (48.7s)
Sep 14 14:46:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:46:59,190 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:46:59 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T13:18:54Z
--- update 2026-09-14T13:23:56Z
--- update 2026-09-14T13:29:19Z
--- update 2026-09-14T13:34:21Z
--- update 2026-09-14T13:39:33Z
--- update 2026-09-14T13:44:36Z
--- update 2026-09-14T13:49:55Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7b952af92e094c05ae1443fb1b8f089a
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T13:55:06Z
--- update 2026-09-14T14:00:15Z
--- update 2026-09-14T14:05:29Z
--- update 2026-09-14T14:10:36Z
--- update 2026-09-14T14:15:44Z
--- update 2026-09-14T14:20:58Z
--- update 2026-09-14T14:26:20Z
--- update 2026-09-14T14:31:36Z
--- update 2026-09-14T14:36:47Z
--- update 2026-09-14T14:41:57Z
--- update 2026-09-14T14:46:58Z
```

## Analyses (laatste 25 regels)
```
inactive
14:26:46   34000 tokens, 3433257 trades, 422988 posities (204s)
14:26:59   36000 tokens, 3651216 trades, 449494 posities (217s)
14:27:11   38000 tokens, 3855373 trades, 477025 posities (229s)
14:27:22   40000 tokens, 4058288 trades, 500003 posities (240s)
14:27:32   42000 tokens, 4231179 trades, 518624 posities (250s)
14:27:44   44000 tokens, 4431591 trades, 543117 posities (262s)
14:27:55   46000 tokens, 4628449 trades, 569121 posities (273s)
14:28:08   48000 tokens, 4835951 trades, 592426 posities (286s)
14:28:21   50000 tokens, 5042483 trades, 617257 posities (299s)
14:28:34   52000 tokens, 5232943 trades, 639976 posities (312s)
14:28:45   54000 tokens, 5400820 trades, 656278 posities (323s)
14:28:58   56000 tokens, 5607778 trades, 682670 posities (336s)
14:29:10   58000 tokens, 5779171 trades, 702483 posities (348s)
14:29:25   60000 tokens, 5995263 trades, 731299 posities (363s)
14:29:38   62000 tokens, 6195128 trades, 760023 posities (376s)
14:29:52   64000 tokens, 6409063 trades, 789743 posities (390s)
14:30:05   66000 tokens, 6613290 trades, 815749 posities (403s)
14:30:18   68000 tokens, 6815336 trades, 844682 posities (416s)
14:30:32   70000 tokens, 7014350 trades, 880257 posities (430s)
14:30:42 posities: 898781 uit 7156509 trades (444s)
14:30:55 201106 wallets gerekend
14:30:56 geluk-toets
14:31:33 persistentie
14:31:36 kopieer-simulatie
14:33:43 klaar in 625s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
14:21:03 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:26:24 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:31:40 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:36:51 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:41:57 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:46:58 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
