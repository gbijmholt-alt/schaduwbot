# Schaduwbot status

- tijd: 2026-09-15 11:51:01 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 22 hours, 4 minutes
- bot-service: active
- code-versie: b2d6d06
- schijf: 7.1G/38G | geheugen: 3615/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 191813, "tokens_in_memory": 6071, "msgs": 27627642, "trades": 5716615, "creates": 61311, "decode_fail": 473698, "rpc_calls": 169745, "rpc_errors": 15, "sol_usd": 100.60780034792994, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 11:30:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:30:02,110 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.6s)
Sep 15 11:30:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:30:02,194 main INFO screen BRR pass=0 dev=0.0 ins=15.87 pro=71 1a=False 1b=False 2=True (77.6s)
Sep 15 11:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:30:48,514 main INFO screen PEPE pass=0 dev=0.0 ins=21.86 pro=56 1a=False 1b=False 2=False (66.8s)
Sep 15 11:31:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:31:00,147 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:31:00 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:31:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:31:01,799 main INFO screen RIZZ pass=0 dev=0.0 ins=46.57 pro=33 1a=False 1b=True 2=True (59.7s)
Sep 15 11:31:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:31:05,528 main INFO screen Habibi pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.3s)
Sep 15 11:31:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:31:43,895 main INFO screen STRATEGY pass=0 dev=0.0 ins=132.83 pro=1 1a=False 1b=False 2=True (55.4s)
Sep 15 11:32:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:32:11,002 main INFO screen fart pass=0 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=True (69.2s)
Sep 15 11:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:32:14,401 main INFO screen CATE pass=0 dev=0.0 ins=0.0 pro=50 1a=False 1b=False 2=False (68.9s)
Sep 15 11:32:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:32:56,125 main INFO screen $MUMPH pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (72.2s)
Sep 15 11:33:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:33:07,069 main INFO screen Silence pass=0 dev=0.0 ins=38.11 pro=64 1a=False 1b=False 2=True (56.1s)
Sep 15 11:33:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:33:13,812 main INFO screen MPG pass=0 dev=0.0 ins=32.14 pro=47 1a=False 1b=False 2=True (59.4s)
Sep 15 11:33:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:33:52,545 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 15 11:34:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:34:10,179 main INFO screen METAL PIPE pass=0 dev=0.0 ins=5.56 pro=9 1a=False 1b=False 2=False (56.4s)
Sep 15 11:34:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:34:18,238 main INFO screen fart pass=0 dev=0.0 ins=9.64 pro=62 1a=False 1b=False 2=True (71.2s)
Sep 15 11:34:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:34:24,953 aiohttp.access INFO 209.38.208.214 [15/Sep/2026:11:34:24 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:35:35,861 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 11:35:35 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 11:35:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:35:59,973 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:35:59 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 11:36:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:36:07,426 main INFO screen つむぎ pass=0 dev=0.0 ins=27.55 pro=75 1a=False 1b=False 2=True (134.9s)
Sep 15 11:36:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:36:16,748 main INFO screen HOM pass=0 dev=3.76 ins=0.0 pro=22 1a=False 1b=False 2=False (126.6s)
Sep 15 11:36:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:36:22,989 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (124.7s)
Sep 15 11:37:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:37:08,670 main INFO screen DOGE pass=0 dev=0.67 ins=0.0 pro=6 1a=False 1b=False 2=False (61.2s)
Sep 15 11:37:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:37:23,994 main INFO screen DrFill pass=0 dev=0.0 ins=53.35 pro=24 1a=False 1b=False 2=True (67.2s)
Sep 15 11:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:37:24,425 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.4s)
Sep 15 11:38:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:38:04,229 main INFO screen DrFill pass=0 dev=0.0 ins=53.87 pro=29 1a=False 1b=False 2=True (55.6s)
Sep 15 11:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:38:37,059 main INFO screen Alon  pass=0 dev=0.0 ins=0.0 pro=47 1a=False 1b=False 2=False (73.1s)
Sep 15 11:38:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:38:38,431 main INFO screen Nora pass=0 dev=0.0 ins=16.07 pro=31 1a=False 1b=False 2=True (74.0s)
Sep 15 11:39:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:39:09,655 main INFO screen onepage pass=0 dev=2.82 ins=7.9 pro=60 1a=False 1b=False 2=False (65.4s)
Sep 15 11:39:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:39:35,936 main INFO screen Fusor pass=0 dev=0.0 ins=37.94 pro=15 1a=False 1b=False 2=True (57.5s)
Sep 15 11:39:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:39:39,955 main INFO screen golf  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (62.9s)
Sep 15 11:40:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:40:16,544 main INFO screen SOUND pass=0 dev=0.0 ins=4.79 pro=37 1a=False 1b=False 2=False (66.9s)
Sep 15 11:40:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:40:35,022 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (59.1s)
Sep 15 11:40:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:40:36,974 main INFO screen DrFill pass=0 dev=0.0 ins=53.05 pro=36 1a=False 1b=False 2=True (57.0s)
Sep 15 11:41:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:41:00,959 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:41:00 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:41:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:41:12,574 main INFO screen truth pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.0s)
Sep 15 11:41:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:41:27,831 main INFO screen DrFill pass=0 dev=0.0 ins=53.68 pro=32 1a=False 1b=False 2=True (52.8s)
Sep 15 11:41:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:41:34,169 main INFO screen EMBERTON pass=0 dev=0.0 ins=79.31 pro=2 1a=False 1b=True 2=True (57.2s)
Sep 15 11:42:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:42:13,686 main INFO screen Sepe pass=0 dev=0.0 ins=14.17 pro=42 1a=False 1b=False 2=False (61.1s)
Sep 15 11:42:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:42:19,092 main INFO screen NIGGER pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (51.3s)
Sep 15 11:42:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:42:26,583 main INFO screen UFO pass=0 dev=0.34 ins=0.0 pro=3 1a=False 1b=False 2=False (52.4s)
Sep 15 11:42:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:42:30,453 aiohttp.access INFO 15.235.146.43 [15/Sep/2026:11:42:30 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 masscan-recon"
Sep 15 11:43:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:43:08,927 main INFO screen Orphic pass=0 dev=0.0 ins=37.87 pro=13 1a=False 1b=False 2=True (49.8s)
Sep 15 11:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:43:18,361 main INFO screen FALLBACK pass=0 dev=0.0 ins=20.18 pro=44 1a=False 1b=False 2=False (64.7s)
Sep 15 11:43:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:43:20,375 main INFO screen DrFill pass=0 dev=0.0 ins=53.3 pro=59 1a=False 1b=False 2=True (53.8s)
Sep 15 11:44:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:44:00,152 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.2s)
Sep 15 11:44:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:44:21,747 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.4s)
Sep 15 11:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:44:28,552 main INFO screen CEEPEE pass=0 dev=0.0 ins=23.68 pro=50 1a=False 1b=False 2=True (70.2s)
Sep 15 11:44:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:44:51,385 main INFO screen PUMP pass=0 dev=0.0 ins=25.1 pro=47 1a=False 1b=False 2=True (51.2s)
Sep 15 11:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:45:12,005 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.3s)
Sep 15 11:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:45:30,628 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.1s)
Sep 15 11:45:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:45:42,040 main INFO screen $JOKER pass=0 dev=0.24 ins=0.0 pro=2 1a=False 1b=False 2=False (50.7s)
Sep 15 11:46:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:46:01,225 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:46:01 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 11:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:46:15,316 main INFO screen LILY pass=0 dev=0.0 ins=11.81 pro=61 1a=False 1b=False 2=False (63.3s)
Sep 15 11:46:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:46:20,276 main INFO screen DrFill pass=0 dev=0.0 ins=53.49 pro=60 1a=False 1b=False 2=True (49.6s)
Sep 15 11:46:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:46:38,940 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (56.9s)
Sep 15 11:47:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:47:11,962 main INFO screen METAWIN pass=0 dev=0.0 ins=28.6 pro=42 1a=False 1b=False 2=False (56.6s)
Sep 15 11:47:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:47:13,920 main INFO screen GayCat pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (53.6s)
Sep 15 11:47:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:47:42,156 main INFO screen $UNEMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 15 11:47:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:47:54,789 aiohttp.access INFO 51.57.80.177 [15/Sep/2026:11:47:54 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 15 11:47:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:47:55,132 aiohttp.access INFO 51.57.80.177 [15/Sep/2026:11:47:55 +0000] "UNKNOWN / HTTP/1.0" 400 230 "-" "-"
Sep 15 11:48:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:48:07,205 main INFO screen YESSIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 15 11:48:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:48:09,142 main INFO screen Muskmoth pass=0 dev=0.0 ins=0.69 pro=3 1a=False 1b=False 2=False (55.2s)
Sep 15 11:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:48:31,835 main INFO screen Ex.End pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.7s)
Sep 15 11:49:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:49:10,786 main INFO screen scribe pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.6s)
Sep 15 11:49:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:49:11,655 main INFO screen Farley pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (64.4s)
Sep 15 11:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:49:21,687 main INFO screen KIBA pass=0 dev=0.0 ins=142.99 pro=0 1a=False 1b=False 2=True (49.9s)
Sep 15 11:50:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:50:24,034 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (72.4s)
Sep 15 11:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:50:26,938 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (76.2s)
Sep 15 11:50:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:50:31,516 main INFO screen MEOW pass=0 dev=0.0 ins=30.95 pro=62 1a=False 1b=False 2=True (69.8s)
Sep 15 11:51:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:51:01,430 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:51:01 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T10:25:40Z
--- update 2026-09-15T10:30:40Z
--- update 2026-09-15T10:35:41Z
--- update 2026-09-15T10:40:43Z
--- update 2026-09-15T10:45:43Z
--- update 2026-09-15T10:50:45Z
--- update 2026-09-15T10:55:47Z
--- update 2026-09-15T11:00:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: eaf6b7b4df234ac0b42ef826db918f51
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T11:05:49Z
--- update 2026-09-15T11:10:49Z
--- update 2026-09-15T11:15:54Z
--- update 2026-09-15T11:20:58Z
--- update 2026-09-15T11:25:58Z
--- update 2026-09-15T11:30:58Z
--- update 2026-09-15T11:35:58Z
--- update 2026-09-15T11:40:59Z
--- update 2026-09-15T11:45:59Z
--- update 2026-09-15T11:51:00Z
```

## Analyses (laatste 40 regels)
```
active
09:48:58 210371 wallets gerekend
09:48:58 geluk-toets
09:49:35 persistentie
09:49:38 kopieer-simulatie
09:52:03 klaar in 727s -> /opt/schaduwbot/reports/wallets.md
10:13:23   500/6700 lopers, 14233 koppelingen
10:14:09   1000/6700 lopers, 27609 koppelingen
10:14:46   1500/6700 lopers, 35674 koppelingen
10:15:33   2000/6700 lopers, 46613 koppelingen
10:16:11   2500/6700 lopers, 55002 koppelingen
10:16:39   3000/6700 lopers, 62231 koppelingen
10:17:23   3500/6700 lopers, 71433 koppelingen
10:17:51   4000/6700 lopers, 77748 koppelingen
10:18:35   4500/6700 lopers, 85514 koppelingen
10:19:12   5000/6700 lopers, 93093 koppelingen
10:19:43   5500/6700 lopers, 99227 koppelingen
10:20:56   6000/6700 lopers, 110982 koppelingen
10:21:42   6500/6700 lopers, 117630 koppelingen
10:21:52 klaar in 1276s: 6700 lopers, 40017 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/vamp.py 11:00:50
11:00:50 tokens lezen
11:00:55 133728 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
11:12:30 6749 lopers, 18 niet-onderscheidende woorden
11:13:34   500/6749 lopers, 4334 koppelingen
11:14:27   1000/6749 lopers, 7353 koppelingen
11:15:10   1500/6749 lopers, 11262 koppelingen
11:16:04   2000/6749 lopers, 15841 koppelingen
11:16:46   2500/6749 lopers, 18547 koppelingen
11:17:20   3000/6749 lopers, 21453 koppelingen
11:18:10   3500/6749 lopers, 25603 koppelingen
11:18:45   4000/6749 lopers, 28395 koppelingen
11:19:40   4500/6749 lopers, 32066 koppelingen
11:20:29   5000/6749 lopers, 35311 koppelingen
11:21:10   5500/6749 lopers, 38244 koppelingen
11:22:29   6000/6749 lopers, 44729 koppelingen
11:23:19   6500/6749 lopers, 48371 koppelingen
11:23:34 uitkomsten uit de trades halen
11:37:02 68207 tokens met een instapkoers
11:37:02 klaar in 2172s: 6749 lopers, 27371 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 11:37:02
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
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
