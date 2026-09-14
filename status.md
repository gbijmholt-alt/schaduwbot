# Schaduwbot status

- tijd: 2026-09-14 18:56:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 5 hours, 9 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.1G/38G | geheugen: 1974/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 130919, "tokens_in_memory": 9291, "msgs": 17771845, "trades": 3740769, "creates": 39175, "decode_fail": 322027, "rpc_calls": 109404, "rpc_errors": 7, "sol_usd": 103.55993902713406, "open_positions": 72, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 14 18:35:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:18,734 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:18:35:18 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 18:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:19,080 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (112.4s)
Sep 14 18:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:35:37,439 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:35:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:01,735 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (108.1s)
Sep 14 18:36:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:03,889 aiohttp.access INFO 94.154.43.250 [14/Sep/2026:18:36:03 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 18:36:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:16,805 main INFO screen LAPUSHA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (118.4s)
Sep 14 18:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:36:27,955 main INFO screen pEyes pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 14 18:37:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:05,424 main INFO screen COMPANY pass=0 dev=0.0 ins=20.59 pro=23 1a=False 1b=False 2=False (63.7s)
Sep 14 18:37:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:15,894 main INFO screen Journey pass=0 dev=0.0 ins=48.15 pro=38 1a=False 1b=False 2=True (59.1s)
Sep 14 18:37:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:37:30,394 main INFO screen GPH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 14 18:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:10,499 main INFO screen TRIPAD pass=0 dev=3.99 ins=34.16 pro=73 1a=False 1b=False 2=True (65.1s)
Sep 14 18:38:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:28,278 main INFO screen Solada pass=0 dev=0.0 ins=31.55 pro=37 1a=False 1b=False 2=True (57.9s)
Sep 14 18:38:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:38:34,829 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (78.9s)
Sep 14 18:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:05,794 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 14 18:39:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:18,873 main INFO screen 67% pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (50.6s)
Sep 14 18:39:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:26,111 main INFO screen One pass=0 dev=0.0 ins=9.06 pro=82 1a=False 1b=False 2=True (51.3s)
Sep 14 18:39:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:39:56,426 main INFO screen $630 pass=0 dev=0.0 ins=9.31 pro=8 1a=False 1b=False 2=False (50.6s)
Sep 14 18:40:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:06,400 main INFO screen EVERYTHING pass=0 dev=0.0 ins=33.93 pro=18 1a=False 1b=False 2=True (47.5s)
Sep 14 18:40:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:16,220 main INFO screen MEME pass=0 dev=0.0 ins=40.88 pro=54 1a=False 1b=False 2=True (50.1s)
Sep 14 18:40:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:40:40,510 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:40:40 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:41:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:01,478 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.1s)
Sep 14 18:41:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:04,794 main INFO screen TOAD pass=0 dev=0.0 ins=20.17 pro=21 1a=False 1b=False 2=False (48.6s)
Sep 14 18:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:05,229 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.8s)
Sep 14 18:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:51,331 main INFO screen FUNNY pass=0 dev=0.0 ins=34.89 pro=7 1a=False 1b=False 2=True (46.5s)
Sep 14 18:41:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:53,887 main INFO screen PVE pass=0 dev=0.0 ins=36.25 pro=78 1a=False 1b=False 2=True (52.4s)
Sep 14 18:41:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:41:58,205 main INFO screen MARKET pass=0 dev=0.0 ins=36.82 pro=30 1a=False 1b=False 2=True (53.0s)
Sep 14 18:42:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:42:43,698 main INFO screen MARKET pass=0 dev=0.0 ins=32.33 pro=21 1a=False 1b=False 2=True (49.8s)
Sep 14 18:42:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:42:45,607 main INFO screen PVE pass=0 dev=0.0 ins=23.8 pro=33 1a=False 1b=False 2=True (54.3s)
Sep 14 18:42:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:42:45,827 main INFO screen MARKET pass=0 dev=0.0 ins=36.88 pro=47 1a=False 1b=False 2=True (47.6s)
Sep 14 18:43:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:43:51,332 aiohttp.access INFO 94.154.43.223 [14/Sep/2026:18:43:51 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 18:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:43:53,367 main INFO screen BELIEVE pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (67.5s)
Sep 14 18:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:43:55,138 main INFO screen $LCBN pass=0 dev=0.66 ins=0.0 pro=2 1a=False 1b=False 2=False (71.4s)
Sep 14 18:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:43:55,892 main INFO screen MEME pass=0 dev=0.0 ins=19.58 pro=23 1a=False 1b=False 2=False (70.3s)
Sep 14 18:44:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:44:39,981 main INFO screen MARKET pass=0 dev=0.0 ins=18.97 pro=11 1a=False 1b=False 2=True (46.6s)
Sep 14 18:44:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:44:45,994 main INFO screen postmelon pass=0 dev=0.0 ins=79.24 pro=1 1a=False 1b=True 2=True (50.9s)
Sep 14 18:44:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:44:50,365 main INFO screen DONKI BU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.5s)
Sep 14 18:45:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:45:36,594 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (56.6s)
Sep 14 18:45:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:45:47,103 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.1s)
Sep 14 18:45:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:45:50,116 main INFO screen MARKET pass=0 dev=0.0 ins=36.17 pro=65 1a=False 1b=False 2=True (59.7s)
Sep 14 18:45:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:45:51,379 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:45:51 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 18:46:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:46:28,802 main INFO screen PVE pass=0 dev=0.0 ins=14.91 pro=34 1a=False 1b=False 2=True (52.2s)
Sep 14 18:46:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:46:52,903 main INFO screen LINK pass=0 dev=0.0 ins=22.0 pro=66 1a=False 1b=False 2=True (65.8s)
Sep 14 18:46:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:46:55,404 main INFO screen 3X pass=0 dev=0.0 ins=0.0 pro=67 1a=False 1b=False 2=False (65.3s)
Sep 14 18:47:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:47:18,596 main INFO screen RISE pass=0 dev=0.0 ins=0.55 pro=3 1a=False 1b=False 2=True (49.8s)
Sep 14 18:47:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:47:43,480 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.6s)
Sep 14 18:47:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:47:48,720 main INFO screen 67% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.3s)
Sep 14 18:48:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:48:08,439 main INFO screen USGR pass=0 dev=0.0 ins=119.74 pro=1 1a=False 1b=False 2=True (49.8s)
Sep 14 18:48:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:48:48,413 main INFO screen hoid pass=0 dev=0.0 ins=50.25 pro=68 1a=False 1b=False 2=True (64.9s)
Sep 14 18:48:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:48:49,759 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.0s)
Sep 14 18:48:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:48:58,707 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.3s)
Sep 14 18:49:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:49:26,864 aiohttp.access INFO 189.18.97.61 [14/Sep/2026:18:49:26 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 14 18:49:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:49:57,635 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (67.9s)
Sep 14 18:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:49:59,767 main INFO screen KABO pass=0 dev=0.0 ins=43.53 pro=45 1a=False 1b=False 2=True (71.4s)
Sep 14 18:50:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:50:05,481 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 14 18:50:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:50:54,919 main INFO screen BIKELUGA pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (57.3s)
Sep 14 18:50:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:50:58,910 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:50:58 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 18:51:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:51:10,551 main INFO screen Pink Bull pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (70.8s)
Sep 14 18:51:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:51:12,213 main INFO screen CATE pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (66.7s)
Sep 14 18:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:51:54,331 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 14 18:52:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:52:10,189 main INFO screen BMW pass=0 dev=0.0 ins=96.4 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 14 18:52:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:52:10,566 main INFO screen TOM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 14 18:52:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:52:48,487 main INFO screen NTDA pass=0 dev=0.0 ins=86.45 pro=0 1a=False 1b=False 2=True (54.2s)
Sep 14 18:53:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:53:23,128 main INFO screen CARS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (72.6s)
Sep 14 18:53:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:53:25,219 main INFO screen civic pass=0 dev=0.0 ins=30.39 pro=68 1a=False 1b=False 2=True (75.0s)
Sep 14 18:53:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:53:48,970 main INFO screen CARS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.5s)
Sep 14 18:54:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:54:29,275 main INFO screen WOFI pass=0 dev=0.45 ins=0.0 pro=1 1a=False 1b=False 2=True (64.1s)
Sep 14 18:54:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:54:32,410 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (69.3s)
Sep 14 18:54:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:54:39,471 main INFO screen CARS pass=0 dev=0.0 ins=20.45 pro=31 1a=True 1b=False 2=False (50.5s)
Sep 14 18:55:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:55:29,146 main INFO screen MBAR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.7s)
Sep 14 18:55:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:55:34,678 main INFO screen Bdog pass=0 dev=0.0 ins=17.17 pro=27 1a=False 1b=False 2=False (65.4s)
Sep 14 18:55:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:55:36,283 main INFO screen Solada pass=0 dev=0.0 ins=31.75 pro=41 1a=False 1b=False 2=True (63.9s)
Sep 14 18:56:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 18:56:06,876 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:18:56:06 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T17:28:07Z
--- update 2026-09-14T17:33:20Z
--- update 2026-09-14T17:38:34Z
--- update 2026-09-14T17:43:36Z
--- update 2026-09-14T17:48:39Z
--- update 2026-09-14T17:53:42Z
--- update 2026-09-14T17:58:53Z
Running as unit: schaduwbot-wallets.service; invocation ID: 9f16fe299e444a8da42e4530eb930f0d
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T18:04:03Z
--- update 2026-09-14T18:09:27Z
--- update 2026-09-14T18:14:36Z
--- update 2026-09-14T18:19:53Z
--- update 2026-09-14T18:25:09Z
--- update 2026-09-14T18:30:25Z
--- update 2026-09-14T18:35:36Z
--- update 2026-09-14T18:40:39Z
--- update 2026-09-14T18:45:49Z
--- update 2026-09-14T18:50:57Z
--- update 2026-09-14T18:56:05Z
```

## Analyses (laatste 25 regels)
```
inactive
18:41:17   36000 tokens, 3638093 trades, 448810 posities (235s)
18:41:30   38000 tokens, 3833313 trades, 474800 posities (248s)
18:41:44   40000 tokens, 4028615 trades, 498777 posities (262s)
18:41:57   42000 tokens, 4216542 trades, 518531 posities (275s)
18:42:10   44000 tokens, 4401553 trades, 541372 posities (288s)
18:42:22   46000 tokens, 4584158 trades, 563643 posities (300s)
18:42:34   48000 tokens, 4783790 trades, 585472 posities (312s)
18:42:47   50000 tokens, 5003074 trades, 615099 posities (325s)
18:42:59   52000 tokens, 5192448 trades, 634508 posities (337s)
18:43:09   54000 tokens, 5369608 trades, 656921 posities (347s)
18:43:21   56000 tokens, 5562048 trades, 679857 posities (359s)
18:43:32   58000 tokens, 5748838 trades, 703454 posities (370s)
18:43:45   60000 tokens, 5965794 trades, 730891 posities (383s)
18:43:57   62000 tokens, 6163332 trades, 760633 posities (395s)
18:44:10   64000 tokens, 6381264 trades, 789533 posities (408s)
18:44:22   66000 tokens, 6567294 trades, 814088 posities (420s)
18:44:35   68000 tokens, 6764874 trades, 841267 posities (433s)
18:44:48   70000 tokens, 6958343 trades, 869440 posities (446s)
18:45:00   72000 tokens, 7152236 trades, 898391 posities (458s)
18:45:02 posities: 902239 uit 7182626 trades (464s)
18:45:16 202478 wallets gerekend
18:45:16 geluk-toets
18:45:52 persistentie
18:45:55 kopieer-simulatie
18:48:01 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
    main()
    ~~~~^^
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
18:40:42 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:45:54 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:51:01 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
18:56:06 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
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
