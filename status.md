# Schaduwbot status

- tijd: 2026-09-15 15:52:45 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 2 hours, 5 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.3G/38G | geheugen: 3642/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 206317, "tokens_in_memory": 7935, "msgs": 29991047, "trades": 6306158, "creates": 67160, "decode_fail": 533850, "rpc_calls": 184548, "rpc_errors": 15, "sol_usd": 99.3589264716272, "open_positions": 48, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 15:33:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:33:20,607 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 15 15:33:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:33:35,348 main INFO screen $OMT pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (56.1s)
Sep 15 15:34:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:12,963 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (52.4s)
Sep 15 15:34:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:20,199 main INFO screen ETCH pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (70.5s)
Sep 15 15:34:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:28,016 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (52.7s)
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:35:40,328 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 15:36:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:02,539 main INFO screen DOTKO pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (109.6s)
Sep 15 15:36:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:07,650 main INFO screen FINE pass=0 dev=0.0 ins=2.43 pro=45 1a=False 1b=False 2=False (107.4s)
Sep 15 15:36:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:30,753 main INFO screen GldOnion pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (122.7s)
Sep 15 15:36:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:59,256 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 15 15:37:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:02,396 main INFO screen USOR/SOL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.7s)
Sep 15 15:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:24,711 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.0s)
Sep 15 15:37:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:42,262 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:37:42 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:37:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:49,006 main INFO screen MM pass=0 dev=0.0 ins=19.07 pro=7 1a=False 1b=False 2=True (49.7s)
Sep 15 15:37:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:56,027 main INFO screen hoax pass=0 dev=0.0 ins=30.13 pro=14 1a=False 1b=False 2=True (53.6s)
Sep 15 15:38:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:38:29,974 main INFO screen MM pass=0 dev=0.0 ins=20.09 pro=7 1a=False 1b=False 2=True (65.3s)
Sep 15 15:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:38:46,440 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 15 15:38:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:38:52,294 aiohttp.access INFO 72.14.178.148 [15/Sep/2026:15:38:52 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 15 15:38:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:38:58,511 main INFO screen SDISCO pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (62.5s)
Sep 15 15:39:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:39:27,520 main INFO screen CATE pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (57.5s)
Sep 15 15:39:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:39:49,547 main INFO screen TOELY pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (63.1s)
Sep 15 15:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:40:02,990 main INFO screen Liberty pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (64.5s)
Sep 15 15:40:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:40:31,093 main INFO screen la peace  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 15 15:40:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:40:51,080 main INFO screen GCoin pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.5s)
Sep 15 15:41:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:41:03,918 main INFO screen BUMS pass=0 dev=0.0 ins=19.68 pro=5 1a=False 1b=False 2=False (60.9s)
Sep 15 15:41:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:41:49,576 main INFO screen APEPUMP pass=0 dev=0.0 ins=79.27 pro=5 1a=False 1b=False 2=True (78.5s)
Sep 15 15:42:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:42:03,746 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (72.7s)
Sep 15 15:42:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:42:14,274 main INFO screen BUMS pass=0 dev=0.0 ins=19.05 pro=4 1a=False 1b=False 2=True (70.4s)
Sep 15 15:42:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:42:44,184 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:42:44 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:42:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:42:47,627 main INFO screen /what_if pass=0 dev=0.0 ins=47.65 pro=19 1a=False 1b=False 2=True (58.0s)
Sep 15 15:43:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:43:03,836 main INFO screen chad pass=0 dev=0.0 ins=25.81 pro=76 1a=False 1b=False 2=True (60.1s)
Sep 15 15:43:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:43:14,746 main INFO screen puter pass=0 dev=0.0 ins=28.67 pro=52 1a=False 1b=False 2=True (60.5s)
Sep 15 15:43:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:43:43,256 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.6s)
Sep 15 15:43:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:43:46,177 aiohttp.access INFO 152.32.234.97 [15/Sep/2026:15:43:46 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 15:43:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:43:56,771 aiohttp.access INFO 152.32.234.97 [15/Sep/2026:15:43:56 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 15 15:44:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:03,075 main INFO screen duscord pass=0 dev=0.0 ins=20.64 pro=6 1a=False 1b=False 2=True (59.2s)
Sep 15 15:44:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:13,843 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (59.1s)
Sep 15 15:44:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:15,192 aiohttp.access INFO 152.32.234.97 [15/Sep/2026:15:44:15 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 15 15:44:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:15,584 aiohttp.access INFO 152.32.234.97 [15/Sep/2026:15:44:15 +0000] "GET /robots.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 15 15:44:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:16,097 aiohttp.access INFO 152.32.234.97 [15/Sep/2026:15:44:16 +0000] "GET /sitemap.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
Sep 15 15:44:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:34,345 main INFO screen BMW pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (51.1s)
Sep 15 15:44:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:44:58,448 main INFO screen CAPY pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (55.4s)
Sep 15 15:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:45:12,220 aiohttp.access INFO 172.236.228.208 [15/Sep/2026:15:45:12 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 15 15:45:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:45:12,222 main INFO screen PARK pass=0 dev=2.75 ins=5.74 pro=55 1a=False 1b=False 2=False (58.4s)
Sep 15 15:45:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:45:28,312 main INFO screen BATMAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.0s)
Sep 15 15:45:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:45:53,156 main INFO screen Kittens pass=0 dev=0.0 ins=19.98 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 15 15:46:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:46:01,809 main INFO screen LEGO pass=0 dev=0.0 ins=166.35 pro=1 1a=False 1b=False 2=True (49.6s)
Sep 15 15:46:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:46:20,780 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.5s)
Sep 15 15:46:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:46:47,979 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.8s)
Sep 15 15:46:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:46:59,225 main INFO screen ALI pass=0 dev=0.21 ins=0.07 pro=6 1a=False 1b=False 2=False (57.4s)
Sep 15 15:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:47:27,883 main INFO screen pumpoids pass=0 dev=0.0 ins=55.68 pro=22 1a=False 1b=False 2=True (67.1s)
Sep 15 15:47:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:47:39,624 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (51.6s)
Sep 15 15:47:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:47:44,315 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:47:44 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:47:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:47:51,138 main INFO screen fin pass=0 dev=0.0 ins=16.39 pro=10 1a=True 1b=True 2=True (51.9s)
Sep 15 15:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:48:18,374 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (50.5s)
Sep 15 15:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:48:47,483 main INFO screen V1 pass=0 dev=1.72 ins=0.0 pro=71 1a=False 1b=False 2=True (67.9s)
Sep 15 15:48:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:48:55,880 main INFO screen REDIRECT pass=0 dev=0.0 ins=19.01 pro=62 1a=False 1b=False 2=False (64.7s)
Sep 15 15:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:49:13,653 main INFO screen JERRY pass=0 dev=1.0 ins=49.51 pro=48 1a=False 1b=False 2=True (55.3s)
Sep 15 15:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:49:35,736 main INFO screen AIRFROG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (48.3s)
Sep 15 15:49:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:49:58,370 main INFO screen BOT pass=0 dev=0.0 ins=24.62 pro=0 1a=False 1b=False 2=False (62.5s)
Sep 15 15:50:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:50:01,726 main INFO screen AOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.1s)
Sep 15 15:50:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:50:21,982 main INFO screen flyfan pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (46.2s)
Sep 15 15:51:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:03,606 main INFO screen Etcamah pass=0 dev=0.0 ins=11.09 pro=44 1a=False 1b=False 2=False (61.9s)
Sep 15 15:51:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:05,606 main INFO screen BRRR pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (67.2s)
Sep 15 15:51:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:16,281 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.3s)
Sep 15 15:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:54,438 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.8s)
Sep 15 15:51:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:59,218 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.6s)
Sep 15 15:52:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:07,362 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (51.1s)
Sep 15 15:52:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:44,688 main INFO screen NTDA pass=0 dev=42.92 ins=0.0 pro=1 1a=False 1b=False 2=True (50.2s)
Sep 15 15:52:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:45,404 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:52:45 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T14:27:19Z
--- update 2026-09-15T14:32:20Z
--- update 2026-09-15T14:37:22Z
--- update 2026-09-15T14:42:23Z
--- update 2026-09-15T14:47:24Z
--- update 2026-09-15T14:52:25Z
--- update 2026-09-15T14:57:25Z
--- update 2026-09-15T15:02:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1214cbbf2de3446d84ae08388a8c7fa6
analyses gestart (0f687558a2d6)
--- update 2026-09-15T15:07:36Z
--- update 2026-09-15T15:12:37Z
--- update 2026-09-15T15:17:36Z
--- update 2026-09-15T15:22:38Z
--- update 2026-09-15T15:27:40Z
--- update 2026-09-15T15:32:40Z
--- update 2026-09-15T15:37:40Z
--- update 2026-09-15T15:42:42Z
--- update 2026-09-15T15:47:43Z
--- update 2026-09-15T15:52:44Z
```

## Analyses (laatste 40 regels)
```
active
12:14:29   500/6807 lopers, 4334 koppelingen
12:15:21   1000/6807 lopers, 7353 koppelingen
12:16:07   1500/6807 lopers, 11262 koppelingen
12:16:58   2000/6807 lopers, 15841 koppelingen
12:17:42   2500/6807 lopers, 18547 koppelingen
12:18:20   3000/6807 lopers, 21453 koppelingen
12:19:14   3500/6807 lopers, 25603 koppelingen
12:19:50   4000/6807 lopers, 28395 koppelingen
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
14:02:52 ijk: +6 van 14 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=238 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
14:02:53 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 14/45/160 | al gemeten: 637
15:03:01 ijk: +4 van 4 kandidaten (4 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=240 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
15:03:02 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 4/34/158 | al gemeten: 641
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
