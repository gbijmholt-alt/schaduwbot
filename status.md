# Schaduwbot status

- tijd: 2026-09-14 01:59:33 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 12 hours, 12 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.3G/38G | geheugen: 1900/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 69925, "tokens_in_memory": 7632, "msgs": 9096271, "trades": 1955366, "creates": 20755, "decode_fail": 171890, "rpc_calls": 57037, "rpc_errors": 3, "sol_usd": 100.0219679798519, "open_positions": 35, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 01:35:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:35:00,956 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (101.7s)
Sep 14 01:35:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:35:16,489 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (100.1s)
Sep 14 01:36:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:36:13,276 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (72.4s)
Sep 14 01:36:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:36:16,355 main INFO screen eelonmusk pass=0 dev=0.0 ins=16.28 pro=68 1a=False 1b=False 2=True (69.9s)
Sep 14 01:36:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:36:24,502 main INFO screen real pepe pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.7s)
Sep 14 01:37:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:37:20,538 main INFO screen Peg pass=0 dev=0.0 ins=46.44 pro=79 1a=False 1b=False 2=True (64.2s)
Sep 14 01:37:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:37:26,961 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.7s)
Sep 14 01:37:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:37:29,842 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.3s)
Sep 14 01:38:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:38:41,560 main INFO screen JohnWick pass=0 dev=0.0 ins=21.7 pro=81 1a=False 1b=False 2=True (67.7s)
Sep 14 01:38:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:38:47,175 main INFO screen UP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.8s)
Sep 14 01:38:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:38:48,190 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:38:48 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:39:02,628 main INFO screen SOL pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (71.9s)
Sep 14 01:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:39:35,328 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 14 01:40:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:40:07,576 main INFO screen SexBoy pass=0 dev=0.14 ins=0.0 pro=1 1a=False 1b=False 2=False (53.0s)
Sep 14 01:40:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:40:31,722 main INFO screen Whalbird pass=1 dev=3.43 ins=0.0 pro=72 1a=False 1b=False 2=False (64.3s)
Sep 14 01:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:40:35,882 main INFO screen SOL pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 14 01:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:40:56,655 main INFO screen BEAST pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (49.1s)
Sep 14 01:41:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:41:36,994 main INFO screen eelon pass=1 dev=0.0 ins=17.88 pro=58 1a=False 1b=False 2=False (65.3s)
Sep 14 01:42:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:42:02,374 main INFO screen billion pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (55.7s)
Sep 14 01:43:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:43:12,758 main INFO screen UP pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (66.0s)
Sep 14 01:43:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:43:14,360 main INFO screen PLASMA pass=0 dev=15.17 ins=1.96 pro=68 1a=False 1b=False 2=False (71.7s)
Sep 14 01:43:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:43:41,714 main INFO screen clearfun pass=1 dev=0.0 ins=0.74 pro=75 1a=False 1b=False 2=False (67.9s)
Sep 14 01:44:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:44:09,851 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.1s)
Sep 14 01:44:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:44:11,166 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:44:11 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:44:19,610 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.1s)
Sep 14 01:44:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:44:35,447 main INFO screen FRINK pass=0 dev=0.0 ins=19.23 pro=70 1a=False 1b=False 2=True (53.7s)
Sep 14 01:45:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:45:15,299 main INFO screen DOGE pass=0 dev=0.48 ins=0.0 pro=6 1a=False 1b=False 2=False (65.4s)
Sep 14 01:45:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:45:21,774 main INFO screen wind pass=0 dev=8.94 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 14 01:45:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:45:25,792 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 14 01:46:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:46:33,952 main INFO screen m&m pass=1 dev=3.82 ins=3.43 pro=62 1a=False 1b=False 2=False (63.2s)
Sep 14 01:47:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:47:01,582 main INFO screen cryptocats pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=True 2=True (51.4s)
Sep 14 01:47:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:47:48,859 main INFO screen MAYHEM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 14 01:47:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:47:50,502 main INFO screen tySON pass=1 dev=0.0 ins=19.11 pro=46 1a=False 1b=False 2=False (62.9s)
Sep 14 01:48:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:48:32,072 main INFO screen SWAMIS pass=0 dev=0.0 ins=21.92 pro=71 1a=False 1b=False 2=True (71.8s)
Sep 14 01:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:48:47,122 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 14 01:48:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:48:53,651 main INFO screen MANGRE pass=0 dev=1.72 ins=0.0 pro=8 1a=False 1b=False 2=False (64.8s)
Sep 14 01:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:49:20,375 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.3s)
Sep 14 01:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:49:21,710 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:49:21 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:49:33,408 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.3s)
Sep 14 01:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:49:56,094 main INFO screen UP pass=0 dev=0.14 ins=0.0 pro=6 1a=False 1b=False 2=False (62.4s)
Sep 14 01:50:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:50:30,426 main INFO screen Nom pass=0 dev=0.0 ins=15.89 pro=73 1a=False 1b=False 2=True (70.0s)
Sep 14 01:50:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:50:38,699 main INFO screen STONKFLY pass=0 dev=0.0 ins=34.4 pro=53 1a=False 1b=False 2=True (65.3s)
Sep 14 01:50:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:50:51,249 main INFO screen fap fap pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.2s)
Sep 14 01:51:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:51:37,602 main INFO screen m&m pass=0 dev=0.0 ins=20.94 pro=70 1a=False 1b=False 2=True (67.2s)
Sep 14 01:51:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:51:39,104 main INFO screen M&M pass=0 dev=0.0 ins=34.07 pro=47 1a=False 1b=False 2=True (60.4s)
Sep 14 01:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:51:58,140 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 14 01:52:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:52:32,870 main INFO screen FROBERT pass=0 dev=0.36 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 14 01:52:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:52:43,092 main INFO screen TOELY pass=0 dev=0.0 ins=38.42 pro=71 1a=False 1b=False 2=True (64.0s)
Sep 14 01:52:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:52:50,385 main INFO screen PEMPFUN pass=0 dev=0.0 ins=29.59 pro=36 1a=True 1b=False 2=True (52.2s)
Sep 14 01:53:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:53:24,062 main INFO screen ICECUBE pass=0 dev=0.0 ins=12.8 pro=64 1a=False 1b=False 2=True (51.2s)
Sep 14 01:53:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:53:41,160 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 14 01:53:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:53:51,322 main INFO screen TOELY pass=1 dev=0.0 ins=19.46 pro=64 1a=False 1b=False 2=False (60.9s)
Sep 14 01:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:54:13,252 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.2s)
Sep 14 01:54:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:54:27,292 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:54:27 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:54:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:54:33,865 main INFO screen BOOBS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.7s)
Sep 14 01:54:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:54:52,903 main INFO screen Chiwiwi pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (61.6s)
Sep 14 01:54:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:54:59,663 aiohttp.access INFO 130.61.131.237 [14/Sep/2026:01:54:59 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0"
Sep 14 01:55:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:55:15,499 main INFO screen ILANDS pass=0 dev=0.0 ins=24.49 pro=78 1a=False 1b=False 2=True (62.2s)
Sep 14 01:55:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:55:26,985 main INFO screen fap fap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.1s)
Sep 14 01:55:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:55:56,766 main INFO screen $baldburg pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (63.9s)
Sep 14 01:56:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:56:11,307 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.8s)
Sep 14 01:56:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:56:21,810 main INFO screen PippinBull pass=0 dev=0.0 ins=55.29 pro=18 1a=False 1b=False 2=True (54.8s)
Sep 14 01:57:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:57:07,821 main INFO screen jaSON pass=1 dev=0.0 ins=12.62 pro=70 1a=False 1b=False 2=False (71.1s)
Sep 14 01:57:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:57:17,626 main INFO screen GlitchBull pass=0 dev=1.74 ins=55.29 pro=44 1a=False 1b=False 2=True (66.3s)
Sep 14 01:57:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:57:21,190 main INFO screen cant hear pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 14 01:58:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:58:01,509 main INFO screen fap fap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.7s)
Sep 14 01:58:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:58:06,308 main INFO screen PVE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 14 01:58:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:58:09,308 main INFO screen GPT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.1s)
Sep 14 01:59:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:59:16,226 main INFO screen billion pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.7s)
Sep 14 01:59:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:59:18,099 main INFO screen dog pass=0 dev=0.0 ins=37.89 pro=18 1a=True 1b=False 2=True (71.8s)
Sep 14 01:59:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:59:21,094 main INFO screen fomotwine pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=False 2=True (71.8s)
Sep 14 01:59:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:59:33,416 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:59:33 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T00:31:06Z
--- update 2026-09-14T00:36:11Z
--- update 2026-09-14T00:41:30Z
--- update 2026-09-14T00:46:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7e8a0dc2ace745d49c06fa77ab8fe773
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T00:51:59Z
--- update 2026-09-14T00:57:07Z
--- update 2026-09-14T01:02:13Z
--- update 2026-09-14T01:07:28Z
--- update 2026-09-14T01:12:34Z
--- update 2026-09-14T01:17:36Z
--- update 2026-09-14T01:22:41Z
--- update 2026-09-14T01:28:17Z
--- update 2026-09-14T01:33:36Z
--- update 2026-09-14T01:38:47Z
--- update 2026-09-14T01:44:10Z
--- update 2026-09-14T01:49:20Z
--- update 2026-09-14T01:54:26Z
--- update 2026-09-14T01:59:32Z
```

## Analyses (laatste 25 regels)
```
inactive
01:18:52   28000 tokens, 2875090 trades, 384850 posities (157s)
01:19:03   30000 tokens, 3070813 trades, 408250 posities (168s)
01:19:16   32000 tokens, 3286227 trades, 438353 posities (181s)
01:19:30   34000 tokens, 3508623 trades, 467675 posities (195s)
01:19:43   36000 tokens, 3711001 trades, 496997 posities (207s)
01:19:55   38000 tokens, 3899681 trades, 517816 posities (220s)
01:20:07   40000 tokens, 4093171 trades, 544267 posities (231s)
01:20:20   42000 tokens, 4301788 trades, 575006 posities (245s)
01:20:32   44000 tokens, 4496449 trades, 598746 posities (256s)
01:20:45   46000 tokens, 4702106 trades, 624669 posities (270s)
01:20:58   48000 tokens, 4900381 trades, 650745 posities (283s)
01:21:11   50000 tokens, 5090194 trades, 674603 posities (296s)
01:21:23   52000 tokens, 5279569 trades, 701217 posities (308s)
01:21:36   54000 tokens, 5472054 trades, 724710 posities (320s)
01:21:48   56000 tokens, 5666068 trades, 752606 posities (333s)
01:22:02   58000 tokens, 5879279 trades, 782376 posities (346s)
01:22:13   60000 tokens, 6079352 trades, 809473 posities (357s)
01:22:23   62000 tokens, 6287006 trades, 840673 posities (368s)
01:22:34   64000 tokens, 6500356 trades, 880050 posities (379s)
01:22:42 posities: 902414 uit 6662391 trades (391s)
01:22:55 192331 wallets gerekend
01:22:55 geluk-toets
01:23:30 persistentie
01:23:33 kopieer-simulatie
01:25:22 klaar in 551s -> /opt/schaduwbot/reports/wallets.md
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
