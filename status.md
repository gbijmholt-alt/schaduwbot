# Schaduwbot status

- tijd: 2026-09-14 07:43:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 17 hours, 56 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.5G/38G | geheugen: 1935/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 90569, "tokens_in_memory": 5206, "msgs": 11517856, "trades": 2457064, "creates": 25566, "decode_fail": 210524, "rpc_calls": 72812, "rpc_errors": 6, "sol_usd": 101.65612079339652, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 07:11:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:11:41,176 main INFO screen Blondboob pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.1s)
Sep 14 07:12:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:12:43,615 main INFO screen TD pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (67.1s)
Sep 14 07:14:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:14:00,809 main INFO screen mak pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 07:15:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:15:42,126 main INFO screen NOVO pass=0 dev=0.0 ins=9.74 pro=10 1a=False 1b=False 2=False (45.1s)
Sep 14 07:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:16:37,265 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:16:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 07:17:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:17:39,244 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.4s)
Sep 14 07:18:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:18:29,429 main INFO screen TRUCE pass=0 dev=0.0 ins=30.07 pro=59 1a=False 1b=False 2=True (74.8s)
Sep 14 07:18:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:18:31,093 main INFO screen IBM pass=1 dev=0.0 ins=9.98 pro=55 1a=False 1b=False 2=False (71.5s)
Sep 14 07:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:19:30,712 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.3s)
Sep 14 07:20:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:08,129 main INFO screen BRONTO pass=0 dev=0.11 ins=77.5 pro=9 1a=False 1b=True 2=True (63.2s)
Sep 14 07:20:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:12,405 main INFO screen GMGNGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.1s)
Sep 14 07:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:33,832 main INFO screen BC pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.1s)
Sep 14 07:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:13,780 main INFO screen Girls pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (60.6s)
Sep 14 07:21:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:22,943 main INFO screen Solana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.9s)
Sep 14 07:21:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:55,252 main INFO screen VISA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 14 07:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:22:17,221 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:22:17 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 07:22:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:22:20,144 main INFO screen ai pass=0 dev=0.0 ins=18.15 pro=61 1a=False 1b=False 2=True (61.6s)
Sep 14 07:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:17,309 main INFO screen mak pass=1 dev=0.47 ins=0.0 pro=14 1a=False 1b=False 2=False (85.1s)
Sep 14 07:23:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:23,057 main INFO screen Rabbit pass=1 dev=0.0 ins=0.0 pro=76 1a=False 1b=False 2=False (76.6s)
Sep 14 07:23:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:41,889 main INFO screen Solana pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.0s)
Sep 14 07:24:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:24:11,353 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.0s)
Sep 14 07:25:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:25:49,919 main INFO screen CATZ pass=0 dev=0.04 ins=77.78 pro=9 1a=False 1b=True 2=True (53.8s)
Sep 14 07:26:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:26:17,217 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.4s)
Sep 14 07:27:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:27:37,248 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:27:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:27:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:27:52,077 main INFO screen . pass=0 dev=0.09 ins=0.0 pro=8 1a=False 1b=False 2=False (56.1s)
Sep 14 07:28:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:28:15,311 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.8s)
Sep 14 07:29:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:29:01,261 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (69.9s)
Sep 14 07:29:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:29:20,882 aiohttp.access INFO 193.8.186.31 [14/Sep/2026:07:29:20 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 07:29:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:29:20,929 aiohttp.access INFO 193.8.186.31 [14/Sep/2026:07:29:20 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
Sep 14 07:29:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:29:44,707 main INFO screen drawer pass=0 dev=0.0 ins=48.22 pro=67 1a=False 1b=False 2=True (66.2s)
Sep 14 07:29:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:29:58,519 main INFO screen willy pass=0 dev=22.8 ins=0.87 pro=67 1a=False 1b=False 2=False (59.1s)
Sep 14 07:31:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:45,539 aiohttp.access INFO 69.5.169.156 [14/Sep/2026:07:31:45 +0000] "GET /zc?action=getInfo HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,286 aiohttp.access INFO 81.19.219.216 [14/Sep/2026:07:31:48 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,322 aiohttp.access INFO 217.146.80.110 [14/Sep/2026:07:31:48 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,380 aiohttp.access INFO 89.37.172.142 [14/Sep/2026:07:31:48 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,380 aiohttp.access INFO 31.14.254.28 [14/Sep/2026:07:31:48 +0000] "GET /mcp/ HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,381 aiohttp.access INFO 81.19.219.210 [14/Sep/2026:07:31:48 +0000] "GET /mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,381 aiohttp.access INFO 213.166.84.47 [14/Sep/2026:07:31:48 +0000] "GET /api/mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:48,422 aiohttp.access INFO 31.14.254.24 [14/Sep/2026:07:31:48 +0000] "GET /sse HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 14 07:31:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:31:54,861 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.1s)
Sep 14 07:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:32:05,364 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.2s)
Sep 14 07:32:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:32:42,344 main INFO screen SHKRELI pass=0 dev=0.0 ins=32.87 pro=38 1a=False 1b=False 2=True (69.5s)
Sep 14 07:32:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:32:49,762 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.9s)
Sep 14 07:32:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:32:57,203 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:32:57 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:33:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:33:04,377 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 14 07:33:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:33:54,182 main INFO screen willy pass=0 dev=0.0 ins=22.72 pro=45 1a=False 1b=False 2=False (64.4s)
Sep 14 07:33:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:33:56,668 main INFO screen $AURA pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (73.2s)
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:35:10,940 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 07:35:10 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 07:36:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:36:23,654 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.4s)
Sep 14 07:36:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:36:24,143 main INFO screen DOOYET pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (73.1s)
Sep 14 07:36:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:36:54,139 main INFO screen KNOB pass=0 dev=1.22 ins=0.0 pro=1 1a=False 1b=False 2=False (59.2s)
Sep 14 07:37:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:37:21,198 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.1s)
Sep 14 07:37:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:37:35,265 main INFO screen DOOYET pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (71.6s)
Sep 14 07:37:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:37:48,470 main INFO screen fomo pass=0 dev=49.42 ins=0.0 pro=1 1a=False 1b=False 2=True (54.3s)
Sep 14 07:38:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:38:22,594 main INFO screen POKÉDOLLAR pass=0 dev=0.0 ins=17.64 pro=59 1a=False 1b=False 2=True (61.4s)
Sep 14 07:38:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:38:23,905 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:38:23 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:38:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:38:48,536 main INFO screen PANIC pass=0 dev=2.08 ins=0.0 pro=5 1a=False 1b=False 2=False (70.4s)
Sep 14 07:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:38:55,390 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 14 07:39:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:39:17,817 main INFO screen Taro pass=0 dev=0.0 ins=3.75 pro=21 1a=True 1b=False 2=False (55.2s)
Sep 14 07:39:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:39:53,971 main INFO screen Papoy pass=1 dev=0.0 ins=0.81 pro=19 1a=False 1b=False 2=False (65.4s)
Sep 14 07:40:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:40:01,931 main INFO screen USDUP pass=0 dev=0.06 ins=77.91 pro=8 1a=False 1b=False 2=True (66.5s)
Sep 14 07:40:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:40:29,424 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.8s)
Sep 14 07:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:40:59,271 main INFO screen npc pass=0 dev=0.0 ins=17.15 pro=70 1a=False 1b=False 2=True (62.3s)
Sep 14 07:41:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:41:28,702 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (59.2s)
Sep 14 07:41:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:41:54,188 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.9s)
Sep 14 07:42:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:42:11,575 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 14 07:43:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:43:22,931 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.3s)
Sep 14 07:43:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:43:23,188 aiohttp.access INFO 20.163.11.168 [14/Sep/2026:07:43:23 +0000] "GET /hudson HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 14 07:43:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:43:36,314 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 14 07:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:43:37,195 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:43:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T06:13:09Z
--- update 2026-09-14T06:18:36Z
--- update 2026-09-14T06:24:02Z
--- update 2026-09-14T06:29:09Z
--- update 2026-09-14T06:34:12Z
--- update 2026-09-14T06:39:34Z
--- update 2026-09-14T06:44:36Z
--- update 2026-09-14T06:50:12Z
--- update 2026-09-14T06:55:36Z
--- update 2026-09-14T07:01:08Z
--- update 2026-09-14T07:06:23Z
--- update 2026-09-14T07:11:29Z
--- update 2026-09-14T07:16:36Z
--- update 2026-09-14T07:22:16Z
--- update 2026-09-14T07:27:36Z
--- update 2026-09-14T07:32:56Z
--- update 2026-09-14T07:38:22Z
--- update 2026-09-14T07:43:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 70fffb71339a4c6280f71f7916117380
analyses gestart (61d1b06b5cec)
```

## Analyses (laatste 25 regels)
```
active
06:10:08   34000 tokens, 3436286 trades, 439217 posities (230s)
06:10:22   36000 tokens, 3657699 trades, 467459 posities (244s)
06:10:36   38000 tokens, 3848415 trades, 492446 posities (258s)
06:10:50   40000 tokens, 4037066 trades, 511931 posities (272s)
06:11:04   42000 tokens, 4220009 trades, 533937 posities (286s)
06:11:20   44000 tokens, 4437887 trades, 566538 posities (302s)
06:11:35   46000 tokens, 4627969 trades, 588174 posities (317s)
06:11:49   48000 tokens, 4823921 trades, 611243 posities (331s)
06:12:04   50000 tokens, 5025358 trades, 633953 posities (346s)
06:12:19   52000 tokens, 5206708 trades, 656081 posities (361s)
06:12:33   54000 tokens, 5407559 trades, 682492 posities (375s)
06:12:46   56000 tokens, 5583807 trades, 703011 posities (388s)
06:13:00   58000 tokens, 5780148 trades, 728335 posities (402s)
06:13:13   60000 tokens, 5970450 trades, 755769 posities (415s)
06:13:27   62000 tokens, 6193165 trades, 786012 posities (429s)
06:13:40   64000 tokens, 6391675 trades, 811172 posities (442s)
06:13:53   66000 tokens, 6594000 trades, 838935 posities (455s)
06:14:07   68000 tokens, 6800066 trades, 877664 posities (469s)
06:14:17 posities: 897901 uit 6953211 trades (483s)
06:14:30 194532 wallets gerekend
06:14:30 geluk-toets
06:15:05 persistentie
06:15:08 kopieer-simulatie
06:17:04 klaar in 650s -> /opt/schaduwbot/reports/wallets.md
07:43:37 73938 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
```

## IJking poolkoers (laatste 12 regels)
```
06:44:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:50:13 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:55:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:01:09 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:06:24 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:11:30 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:16:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:22:16 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:27:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:32:56 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:38:23 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:43:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
