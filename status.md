# Schaduwbot status

- tijd: 2026-09-13 15:04:11 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 1 hour, 17 minutes
- bot-service: active
- code-versie: 60bc96f
- schijf: 4.6G/38G | geheugen: 1168/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 30604, "tokens_in_memory": 5292, "msgs": 2216365, "trades": 592297, "creates": 6898, "decode_fail": 71936, "rpc_calls": 18529, "rpc_errors": 2, "sol_usd": 100.4209556776236, "open_positions": 44, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 14:20:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:20:26,732 main INFO screen USWS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (67.5s)
Sep 13 14:21:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:21:53,798 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:21:53 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:22:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:22:01,674 main INFO screen Hive pass=1 dev=0.0 ins=11.38 pro=56 1a=False 1b=False 2=False (68.0s)
Sep 13 14:22:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:22:06,213 main INFO screen Eugene pass=0 dev=0.0 ins=32.3 pro=60 1a=False 1b=False 2=True (67.0s)
Sep 13 14:23:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:23:31,352 main INFO screen MALF pass=0 dev=49.86 ins=0.08 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 13 14:24:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:24:03,929 main INFO screen PATATA pass=0 dev=0.0 ins=32.03 pro=18 1a=False 1b=False 2=True (67.5s)
Sep 13 14:24:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:24:30,527 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=5 1a=False 1b=False 2=False (69.0s)
Sep 13 14:25:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:25:24,291 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.0s)
Sep 13 14:25:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:25:27,316 main INFO screen SNUZ pass=0 dev=0.25 ins=0.0 pro=8 1a=False 1b=False 2=False (55.7s)
Sep 13 14:27:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:27:13,583 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:27:13 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:27:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:27:43,562 main INFO screen .$NOID pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.5s)
Sep 13 14:29:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:29:50,457 main INFO screen BWEP pass=0 dev=0.0 ins=32.48 pro=23 1a=False 1b=False 2=True (66.7s)
Sep 13 14:30:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:30:12,756 main INFO screen DOGE pass=0 dev=0.44 ins=0.0 pro=1 1a=False 1b=False 2=False (56.9s)
Sep 13 14:30:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:30:51,743 main INFO screen BotTrencher pass=1 dev=0.0 ins=12.27 pro=24 1a=False 1b=False 2=False (63.0s)
Sep 13 14:31:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:31:32,131 main INFO screen 四小龙 pass=0 dev=0.0 ins=13.27 pro=64 1a=False 1b=False 2=True (52.7s)
Sep 13 14:32:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:32:15,800 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:32:15 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:32:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:32:46,739 main INFO screen rat pass=0 dev=0.0 ins=31.44 pro=50 1a=False 1b=False 2=True (62.5s)
Sep 13 14:33:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:33:42,956 main INFO screen BITQUEEN pass=0 dev=3.33 ins=0.0 pro=6 1a=False 1b=False 2=False (58.1s)
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:34:55,387 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 14:34:55 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 14:34:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:34:56,071 main INFO screen benny pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (99.0s)
Sep 13 14:35:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:35:22,408 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=6 1a=False 1b=False 2=False (114.6s)
Sep 13 14:35:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:35:24,311 main INFO screen HUMAN pass=1 dev=0.0 ins=4.11 pro=55 1a=False 1b=False 2=False (101.4s)
Sep 13 14:35:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:35:56,923 main INFO screen mmrich pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (60.8s)
Sep 13 14:36:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:36:22,171 main INFO screen Moon pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.9s)
Sep 13 14:36:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:36:26,821 main INFO screen SIKA pass=0 dev=0.0 ins=32.4 pro=18 1a=False 1b=False 2=True (64.4s)
Sep 13 14:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:06,612 main INFO screen cheese pass=0 dev=0.0 ins=33.53 pro=58 1a=False 1b=False 2=True (69.7s)
Sep 13 14:37:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:31,165 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:14:37:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 14:37:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:37,131 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:37:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:39:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:39:14,170 rpc WARNING rpc getTokenAccountsByOwner exc Server disconnected
Sep 13 14:39:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:39:17,501 main INFO screen MIMI pass=0 dev=0.0 ins=22.81 pro=63 1a=False 1b=False 2=True (77.2s)
Sep 13 14:40:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:40:57,367 main INFO screen RAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.9s)
Sep 13 14:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:11,919 main INFO screen RAWR pass=0 dev=0.0 ins=32.09 pro=38 1a=False 1b=True 2=True (66.1s)
Sep 13 14:41:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:23,452 main INFO screen $AURA pass=0 dev=0.19 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 13 14:41:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:46,132 main INFO screen KAWAIICAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.8s)
Sep 13 14:42:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:42:57,378 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:42:57 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:44:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:44:30,643 main INFO screen SSP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (48.0s)
Sep 13 14:44:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:44:53,679 main INFO screen RICK pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 13 14:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:46:17,412 main INFO screen BotTrencher pass=1 dev=0.0 ins=11.38 pro=54 1a=False 1b=False 2=False (63.3s)
Sep 13 14:47:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:47:00,598 main INFO screen pleun pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 13 14:47:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:47:48,597 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.0s)
Sep 13 14:48:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:48:10,290 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:48:10 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:48:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:48:40,970 main INFO screen OpenAI pass=0 dev=99.3 ins=0.0 pro=1 1a=False 1b=False 2=True (46.2s)
Sep 13 14:49:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:49:08,256 main INFO screen $MIZO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.3s)
Sep 13 14:50:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:50:53,171 main INFO screen CROKAH pass=0 dev=0.0 ins=31.83 pro=30 1a=False 1b=True 2=True (49.9s)
Sep 13 14:52:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:01,898 main INFO screen Quack pass=1 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (67.5s)
Sep 13 14:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:04,837 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 13 14:52:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:29,001 main INFO screen HAND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.7s)
Sep 13 14:52:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:47,735 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.8s)
Sep 13 14:53:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:53:20,419 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:53:20 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:53:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:53:57,725 main INFO screen PEPON pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (52.9s)
Sep 13 14:54:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:54:26,326 main INFO screen TSLA pass=1 dev=0.0 ins=0.0 pro=26 1a=False 1b=False 2=False (59.5s)
Sep 13 14:54:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:54:27,200 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.1s)
Sep 13 14:56:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:12,199 main INFO screen anonbikesn pass=0 dev=0.0 ins=36.19 pro=21 1a=False 1b=False 2=True (60.5s)
Sep 13 14:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:50,467 aiohttp.access INFO 150.107.36.82 [13/Sep/2026:14:56:50 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 13 14:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:50,814 aiohttp.access INFO 150.107.36.82 [13/Sep/2026:14:56:50 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 14:57:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:57:24,653 main INFO screen CANTY pass=0 dev=0.0 ins=31.82 pro=28 1a=False 1b=True 2=True (61.4s)
Sep 13 14:57:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:57:32,628 main INFO screen RAVEN pass=1 dev=0.0 ins=8.56 pro=19 1a=False 1b=False 2=False (49.3s)
Sep 13 14:58:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:00,464 main INFO screen CHEESE pass=1 dev=0.0 ins=15.33 pro=70 1a=False 1b=False 2=False (67.2s)
Sep 13 14:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:18,847 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 13 14:58:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:37,245 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:58:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:59:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:59:08,751 main INFO screen stocklana pass=0 dev=0.0 ins=25.12 pro=32 1a=False 1b=False 2=True (48.9s)
Sep 13 15:00:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:00:44,394 main INFO screen AAPLCAT pass=0 dev=5.78 ins=72.68 pro=0 1a=False 1b=False 2=True (52.0s)
Sep 13 15:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:30,087 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.7s)
Sep 13 15:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:30,366 main INFO screen RC pass=1 dev=0.01 ins=5.36 pro=40 1a=False 1b=False 2=False (71.4s)
Sep 13 15:01:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:37,911 main INFO screen SCM pass=0 dev=0.0 ins=32.33 pro=27 1a=False 1b=False 2=True (53.5s)
Sep 13 15:02:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:02:30,009 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.0s)
Sep 13 15:03:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:03:19,862 main INFO screen Stocklana pass=0 dev=0.0 ins=18.91 pro=59 1a=False 1b=False 2=True (61.6s)
Sep 13 15:03:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:03:32,321 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 13 15:04:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:04:08,669 main INFO screen batonguy pass=0 dev=0.0 ins=79.27 pro=0 1a=False 1b=True 2=True (52.0s)
Sep 13 15:04:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:04:11,823 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:04:11 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T13:44:36Z
--- update 2026-09-13T13:49:54Z
--- update 2026-09-13T13:55:16Z
--- update 2026-09-13T14:00:36Z
--- update 2026-09-13T14:05:53Z
--- update 2026-09-13T14:11:04Z
--- update 2026-09-13T14:16:36Z
--- update 2026-09-13T14:21:52Z
--- update 2026-09-13T14:27:12Z
--- update 2026-09-13T14:32:14Z
--- update 2026-09-13T14:37:36Z
--- update 2026-09-13T14:42:56Z
--- update 2026-09-13T14:48:09Z
--- update 2026-09-13T14:53:19Z
nieuwe code: 60bc96f
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 5753ff544a174b8f8dc6b2ae1512fa0d
analyses gestart (0d01412cf2b7)
--- update 2026-09-13T14:58:36Z
--- update 2026-09-13T15:04:10Z
```

## Analyses (laatste 25 regels)
```
active
13:42:30   48000 tokens, 5336125 trades, 853347 posities (94s)
13:42:34   50000 tokens, 5563743 trades, 890112 posities (99s)
13:42:38   52000 tokens, 5789931 trades, 932064 posities (102s)
13:42:41   54000 tokens, 5990533 trades, 973580 posities (105s)
13:42:41 posities: 986877 uit 6042752 trades (106s)
13:42:55 202358 wallets gerekend
13:42:55 geluk-toets
13:43:28 persistentie
13:43:31 kopieer-simulatie
13:44:11 klaar in 196s -> /opt/schaduwbot/reports/wallets.md
14:53:20 55067 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
14:53:30   ingelezen tot rowid 6142170 (121118 rijen, 121118 bruikbaar)
14:53:30 ingelezen: 121118 nieuwe trades, 121118 bruikbaar (11s)
14:54:34 2153 aankopen van gevolgde wallets geëvalueerd
14:54:47 vroege kopers: 175 voldoen nu, register 289, 166 tokens beoordeeld
14:55:03 grote spelers: saldo van 301 wallets opgehaald
14:56:07 herkomst: 40 posities gekoppeld
14:56:12 klaar in 173s -> /opt/schaduwbot/reports/ledger.md
14:57:30 S1: gezakt — toets n=7305, verkennend n=14656
14:57:30 klaar in 77s -> /opt/schaduwbot/reports/hypotheses.md
14:59:58 klaar in 148s -> /opt/schaduwbot/reports/lotgevallen.md
14:59:58 probe: 150 transacties ophalen
15:03:16 poolveld: 9 pools bekeken, 0 te gaan -> vastgesteld @43
15:04:01 prijsijk: n=0 -> nog 20 verse migraties te gaan
15:04:02 na-migratie: 100 paren te checken
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
