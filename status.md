# Schaduwbot status

- tijd: 2026-09-15 22:58:29 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 9 hours, 11 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.8G/38G | geheugen: 2430/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 231862, "tokens_in_memory": 11568, "msgs": 40614857, "trades": 7640201, "creates": 80771, "decode_fail": 632887, "rpc_calls": 210730, "rpc_errors": 18, "sol_usd": 97.16722692558878, "open_positions": 159, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 22:35:35 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 22:35:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:35:36,480 main INFO screen MUSMASK pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (121.2s)
Sep 15 22:35:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:35:55,866 main INFO screen PLING pass=0 dev=0.0 ins=0.17 pro=74 1a=False 1b=False 2=True (128.7s)
Sep 15 22:36:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:36:38,707 main INFO screen Nike pass=0 dev=0.0 ins=170.16 pro=0 1a=False 1b=False 2=True (114.6s)
Sep 15 22:36:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:36:48,799 main INFO screen PATCH pass=0 dev=46.42 ins=28.6 pro=11 1a=False 1b=False 2=False (72.3s)
Sep 15 22:36:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:36:51,523 main INFO screen T128 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.7s)
Sep 15 22:37:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:37:17,589 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:37:17 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 22:37:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:37:37,947 main INFO screen Floor pass=0 dev=0.0 ins=14.58 pro=64 1a=False 1b=False 2=True (49.1s)
Sep 15 22:37:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:37:38,093 main INFO screen TEST pass=0 dev=0.0 ins=13.01 pro=42 1a=False 1b=False 2=True (59.4s)
Sep 15 22:37:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:37:50,551 main INFO screen CLIMATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 15 22:38:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:38:32,369 main INFO screen delayed pass=0 dev=0.0 ins=24.38 pro=3 1a=False 1b=False 2=True (54.4s)
Sep 15 22:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:38:37,747 main INFO screen Bitly pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (59.7s)
Sep 15 22:39:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:39:00,208 main INFO screen Repuplican pass=0 dev=0.0 ins=0.18 pro=18 1a=False 1b=False 2=True (69.7s)
Sep 15 22:39:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:39:29,099 main INFO screen KIBA pass=0 dev=0.0 ins=134.12 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 15 22:39:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:39:36,984 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.2s)
Sep 15 22:39:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:39:56,828 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 15 22:40:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:40:36,372 main INFO screen misunderstood pass=0 dev=0.0 ins=38.01 pro=65 1a=False 1b=False 2=True (67.3s)
Sep 15 22:40:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:40:44,843 main INFO screen CHEEZER pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.9s)
Sep 15 22:40:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:40:51,098 main INFO screen Manifesto pass=0 dev=0.0 ins=34.35 pro=58 1a=False 1b=False 2=True (54.3s)
Sep 15 22:41:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:41:38,433 main INFO screen SOLSCOPE pass=0 dev=0.0 ins=11.41 pro=78 1a=False 1b=False 2=True (62.1s)
Sep 15 22:41:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:41:38,522 main INFO screen SOLSCOPE pass=0 dev=0.0 ins=30.39 pro=19 1a=False 1b=False 2=True (53.7s)
Sep 15 22:41:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:41:44,947 main INFO screen PUSS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 15 22:42:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:42:24,628 main INFO screen SOLSCOPE pass=0 dev=0.0 ins=25.55 pro=2 1a=False 1b=False 2=True (46.2s)
Sep 15 22:42:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:42:34,559 main INFO screen WRII pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (56.0s)
Sep 15 22:42:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:42:36,017 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:42:36 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 22:42:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:42:44,187 main INFO screen INM pass=0 dev=0.0 ins=24.8 pro=2 1a=False 1b=False 2=True (59.2s)
Sep 15 22:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:43:18,954 main INFO screen CATI pass=0 dev=0.0 ins=19.32 pro=1 1a=False 1b=False 2=False (54.3s)
Sep 15 22:43:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:43:37,915 main INFO screen CRUISE pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=False 2=True (63.4s)
Sep 15 22:43:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:43:47,934 main INFO screen Pollentician pass=0 dev=0.0 ins=15.78 pro=54 1a=False 1b=False 2=True (63.7s)
Sep 15 22:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:44:28,351 main INFO screen JamesTalarico pass=0 dev=0.0 ins=25.17 pro=0 1a=False 1b=False 2=True (69.4s)
Sep 15 22:44:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:44:32,335 main INFO screen sth pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.4s)
Sep 15 22:44:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:44:38,764 aiohttp.access INFO 94.154.43.203 [15/Sep/2026:22:44:38 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0"
Sep 15 22:44:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:44:39,192 main INFO screen CAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (51.3s)
Sep 15 22:45:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:45:25,092 main INFO screen democat pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (56.7s)
Sep 15 22:45:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:45:37,000 main INFO screen CHEESEBALL pass=0 dev=0.0 ins=0.8 pro=71 1a=False 1b=False 2=False (64.7s)
Sep 15 22:45:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:45:44,145 main INFO screen anon pass=0 dev=0.0 ins=11.87 pro=58 1a=False 1b=False 2=True (65.0s)
Sep 15 22:46:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:46:14,459 main INFO screen BOB pass=0 dev=0.0 ins=25.13 pro=2 1a=False 1b=False 2=True (49.4s)
Sep 15 22:46:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:46:23,937 main INFO screen AURASEA pass=0 dev=0.0 ins=0.0 pro=45 1a=False 1b=False 2=False (46.9s)
Sep 15 22:46:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:46:49,335 main INFO screen Hanging pass=0 dev=0.0 ins=33.82 pro=76 1a=False 1b=False 2=True (65.2s)
Sep 15 22:47:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:47:25,484 main INFO screen Democat pass=0 dev=0.0 ins=10.9 pro=32 1a=False 1b=False 2=False (71.0s)
Sep 15 22:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:47:27,384 main INFO screen Inupendent pass=0 dev=0.0 ins=22.92 pro=59 1a=False 1b=False 2=True (63.4s)
Sep 15 22:47:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:47:37,196 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:47:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 22:48:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:48:05,101 main INFO screen KOLBY pass=0 dev=0.0 ins=32.96 pro=56 1a=False 1b=False 2=True (75.8s)
Sep 15 22:48:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:48:24,354 main INFO screen WOTF pass=0 dev=0.79 ins=133.15 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 15 22:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:48:31,923 main INFO screen Floor pass=0 dev=0.0 ins=14.58 pro=44 1a=False 1b=False 2=False (66.4s)
Sep 15 22:49:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:49:14,446 main INFO screen BOB pass=0 dev=0.0 ins=20.39 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 15 22:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:49:19,831 main INFO screen pillgates pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (55.5s)
Sep 15 22:49:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:49:30,430 main INFO screen INM pass=0 dev=0.0 ins=35.89 pro=65 1a=False 1b=False 2=True (58.5s)
Sep 15 22:50:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:50:28,333 main INFO screen CHARZARD  pass=0 dev=0.29 ins=0.0 pro=7 1a=False 1b=False 2=False (68.5s)
Sep 15 22:50:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:50:28,761 main INFO screen ICET pass=0 dev=0.0 ins=8.63 pro=59 1a=False 1b=False 2=True (74.3s)
Sep 15 22:50:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:50:39,289 main INFO screen Lit pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (68.9s)
Sep 15 22:51:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:51:26,489 main INFO screen mictyson pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (58.2s)
Sep 15 22:51:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:51:27,981 main INFO screen OpenAI pass=0 dev=0.0 ins=78.92 pro=0 1a=False 1b=False 2=True (59.2s)
Sep 15 22:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:51:35,388 main INFO screen JENSEN pass=0 dev=0.0 ins=24.3 pro=1 1a=False 1b=False 2=True (56.1s)
Sep 15 22:52:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:52:32,178 main INFO screen CAT pass=0 dev=0.0 ins=0.0 pro=67 1a=False 1b=False 2=True (65.7s)
Sep 15 22:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:52:34,273 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (66.3s)
Sep 15 22:52:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:52:36,690 main INFO screen CATE pass=0 dev=0.0 ins=2.08 pro=0 1a=False 1b=False 2=True (61.3s)
Sep 15 22:52:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:52:49,584 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:52:49 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 22:53:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:53:45,084 main INFO screen ily pass=0 dev=0.0 ins=33.52 pro=80 1a=False 1b=False 2=True (70.8s)
Sep 15 22:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:53:47,044 main INFO screen PAC-MAN pass=0 dev=1.04 ins=5.77 pro=69 1a=False 1b=False 2=True (74.9s)
Sep 15 22:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:53:47,513 main INFO screen REPUPLICAT pass=0 dev=0.0 ins=38.58 pro=43 1a=False 1b=False 2=True (70.8s)
Sep 15 22:54:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:54:56,310 main INFO screen TWINE pass=0 dev=0.0 ins=16.18 pro=77 1a=False 1b=False 2=True (69.3s)
Sep 15 22:54:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:54:59,831 main INFO screen NewCoin pass=0 dev=0.0 ins=0.35 pro=13 1a=False 1b=False 2=False (72.3s)
Sep 15 22:55:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:55:01,531 main INFO screen PAC-MAN pass=0 dev=0.0 ins=20.85 pro=1 1a=False 1b=False 2=False (76.4s)
Sep 15 22:55:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:55:45,801 main INFO screen TWINSINU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.5s)
Sep 15 22:55:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:55:56,659 main INFO screen T pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.8s)
Sep 15 22:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:56:01,101 main INFO screen ALONe pass=0 dev=0.0 ins=15.84 pro=23 1a=False 1b=False 2=False (59.6s)
Sep 15 22:56:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:56:47,531 main INFO screen Rebulican pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (61.7s)
Sep 15 22:57:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:57:08,090 main INFO screen PvP pass=0 dev=0.0 ins=27.96 pro=66 1a=False 1b=False 2=True (71.4s)
Sep 15 22:57:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:57:10,909 main INFO screen huhbike pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=False 2=True (69.8s)
Sep 15 22:57:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:57:47,699 main INFO screen ETHAN pass=0 dev=0.0 ins=24.71 pro=1 1a=False 1b=False 2=True (60.2s)
Sep 15 22:58:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:58:28,665 main INFO screen Dumbocrat pass=0 dev=0.0 ins=13.71 pro=55 1a=False 1b=False 2=False (80.6s)
Sep 15 22:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:58:29,212 main INFO screen PRINTER pass=0 dev=0.0 ins=26.01 pro=57 1a=False 1b=False 2=True (78.3s)
Sep 15 22:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:58:29,959 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:58:29 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T21:30:04Z
--- update 2026-09-15T21:35:31Z
--- update 2026-09-15T21:40:36Z
--- update 2026-09-15T21:45:43Z
--- update 2026-09-15T21:50:43Z
--- update 2026-09-15T21:55:52Z
--- update 2026-09-15T22:00:57Z
--- update 2026-09-15T22:06:36Z
--- update 2026-09-15T22:11:39Z
Running as unit: schaduwbot-wallets.service; invocation ID: b46f5ed8f5f6459e97deaaa3c5d20a86
analyses gestart (84579ff37485)
--- update 2026-09-15T22:16:44Z
--- update 2026-09-15T22:21:44Z
--- update 2026-09-15T22:26:45Z
--- update 2026-09-15T22:31:47Z
--- update 2026-09-15T22:37:16Z
--- update 2026-09-15T22:42:34Z
--- update 2026-09-15T22:47:36Z
--- update 2026-09-15T22:52:48Z
--- update 2026-09-15T22:58:28Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 16:03:19
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 18:04:11
18:04:12 venster 2026-09-13 06:04 UTC .. nu, 67852 tokens
18:05:01 klaar in 50s: 51584 tokens, 1905 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 19:05:57
19:05:58 venster 2026-09-13 07:05 UTC .. nu, 68842 tokens
19:06:46 klaar in 49s: 52628 tokens, 1902 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 20:07:44
20:07:45 venster 2026-09-13 08:07 UTC .. nu, 70021 tokens
20:08:37 klaar in 53s: 53536 tokens, 1839 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 21:09:36
21:09:36 venster 2026-09-13 09:09 UTC .. nu, 71175 tokens
21:10:29 klaar in 53s: 54456 tokens, 1720 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 22:11:40
22:11:40 venster 2026-09-13 10:11 UTC .. nu, 72419 tokens
22:12:33 klaar in 54s: 55545 tokens, 1912 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
22:26:51 ijk: +0 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=408 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:26:51 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 13/57/187 | al gemeten: 856
22:31:53 ijk: +0 van 10 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=408 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:31:53 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 10/58/187 | al gemeten: 856
22:38:04 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=412 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:38:04 ijk-diagnose: nieuwste migratie -0.5 min oud | migraties 15/60/240 min: 13/60/191 | al gemeten: 862
22:42:59 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=413 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:43:00 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 11/53/186 | al gemeten: 867
22:48:08 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=418 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:48:08 ijk-diagnose: nieuwste migratie -0.5 min oud | migraties 15/60/240 min: 14/54/189 | al gemeten: 873
22:53:18 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=422 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
22:53:18 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 13/53/191 | al gemeten: 879
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 1353 | 178 | 174 | 0 | 5 | 5.5 min |
| 09-13 00:00 | 5995 | 675 | 658 | 0 | 295 | 2.3 min |
| 09-13 06:00 | 4301 | 538 | 534 | 0 | 282 | 2.4 min |
| 09-13 12:00 | 6600 | 754 | 741 | 0 | 286 | 2.6 min |
| 09-13 18:00 | 8021 | 920 | 889 | 0 | 118 | 4.0 min |
| 09-14 00:00 | 6068 | 752 | 743 | 0 | 275 | 2.6 min |
| 09-14 06:00 | 4709 | 692 | 683 | 0 | 323 | 2.3 min |
| 09-14 12:00 | 8320 | 1156 | 1091 | 0 | 36 | 16.9 min |
| 09-14 18:00 | 10622 | 1266 | 1153 | 266 | 0 | 94.8 min |
| 09-15 00:00 | 7337 | 881 | 827 | 81 | 0 | 112.5 min |
| 09-15 06:00 | 6072 | 909 | 853 | 1 | 0 | 73.3 min |
| 09-15 12:00 | 9559 | 1252 | 1159 | 12 | 0 | 76.9 min |
| 09-15 18:00 | 9746 | 480 | 444 | 476 | 0 | 150.4 min |

'pas na 2u05' = gescreend nadat de replay het token al had vastgelegd; die tellen nooit mee.


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
