# Schaduwbot status

- tijd: 2026-09-14 12:04:54 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 22 hours, 17 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.7G/38G | geheugen: 1916/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 106246, "tokens_in_memory": 4711, "msgs": 12599680, "trades": 2814182, "creates": 29174, "decode_fail": 232563, "rpc_calls": 84627, "rpc_errors": 7, "sol_usd": 101.34825522795029, "open_positions": 57, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 11:36:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:36:20,138 main INFO screen Truninu pass=0 dev=0.0 ins=0.01 pro=10 1a=False 1b=False 2=True (64.9s)
Sep 14 11:36:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:36:27,298 main INFO screen HALH pass=0 dev=0.04 ins=0.0 pro=7 1a=False 1b=False 2=False (72.6s)
Sep 14 11:37:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:37:04,977 main INFO screen lucky pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 14 11:37:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:37:10,901 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 14 11:37:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:37:36,418 main INFO screen MILIA pass=0 dev=0.0 ins=31.49 pro=40 1a=False 1b=False 2=True (69.1s)
Sep 14 11:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:38:17,141 main INFO screen POF pass=0 dev=9.75 ins=0.01 pro=64 1a=False 1b=False 2=True (66.2s)
Sep 14 11:38:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:38:17,536 main INFO screen UHI pass=0 dev=0.0 ins=22.51 pro=57 1a=False 1b=False 2=False (72.6s)
Sep 14 11:38:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:38:30,535 main INFO screen Amazon pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 14 11:39:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:39:16,616 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:39:16 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:39:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:39:30,612 main INFO screen öbhfy pass=1 dev=0.0 ins=0.88 pro=10 1a=False 1b=False 2=False (73.5s)
Sep 14 11:39:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:39:32,828 main INFO screen NUT pass=0 dev=0.0 ins=25.72 pro=47 1a=False 1b=False 2=True (75.3s)
Sep 14 11:39:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:39:41,804 main INFO screen SCROOGE pass=0 dev=35.83 ins=0.81 pro=4 1a=False 1b=False 2=True (71.3s)
Sep 14 11:40:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:40:28,280 main INFO screen cartyson pass=0 dev=0.06 ins=79.26 pro=8 1a=False 1b=True 2=True (57.7s)
Sep 14 11:40:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:40:42,664 main INFO screen coded pass=1 dev=0.0 ins=1.39 pro=68 1a=False 1b=False 2=False (69.8s)
Sep 14 11:40:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:40:45,436 main INFO screen vodka pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 14 11:41:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:41:16,148 aiohttp.access INFO 35.240.97.242 [14/Sep/2026:11:41:16 +0000] "GET / HTTP/1.1" 404 174 "-" "python-requests/2.32.5"
Sep 14 11:41:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:41:47,507 main INFO screen UHI pass=1 dev=0.11 ins=9.95 pro=28 1a=False 1b=False 2=False (79.2s)
Sep 14 11:41:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:41:54,086 main INFO screen SIRI AI pass=0 dev=0.0 ins=23.37 pro=65 1a=False 1b=False 2=True (71.4s)
Sep 14 11:41:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:41:57,448 main INFO screen tolyet pass=0 dev=0.0 ins=28.76 pro=56 1a=False 1b=False 2=False (72.0s)
Sep 14 11:42:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:42:43,713 main INFO screen transfer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.2s)
Sep 14 11:43:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:43:02,574 main INFO screen grow pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.5s)
Sep 14 11:43:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:43:04,073 main INFO screen NUT pass=1 dev=0.0 ins=0.88 pro=82 1a=False 1b=False 2=False (66.6s)
Sep 14 11:43:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:43:40,569 main INFO screen Errol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 14 11:44:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:44:16,114 main INFO screen アルー pass=0 dev=0.0 ins=36.4 pro=65 1a=False 1b=False 2=True (72.0s)
Sep 14 11:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:44:19,389 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:44:19 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:44:19,953 main INFO screen falcon pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (77.4s)
Sep 14 11:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:44:37,064 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 14 11:45:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:45:21,725 main INFO screen TRADY pass=0 dev=0.0 ins=0.41 pro=40 1a=False 1b=True 2=False (61.8s)
Sep 14 11:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:45:32,945 main INFO screen hycate pass=1 dev=0.21 ins=0.0 pro=13 1a=False 1b=False 2=False (76.8s)
Sep 14 11:45:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:45:50,379 main INFO screen water pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 14 11:46:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:46:29,780 main INFO screen HOBL pass=0 dev=0.0 ins=24.26 pro=45 1a=False 1b=False 2=True (68.1s)
Sep 14 11:47:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:47:49,967 main INFO screen pvpdog pass=0 dev=0.0 ins=26.98 pro=59 1a=False 1b=False 2=True (72.8s)
Sep 14 11:47:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:47:58,871 main INFO screen yugllihC pass=0 dev=0.19 ins=79.12 pro=10 1a=False 1b=True 2=True (56.4s)
Sep 14 11:48:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:48:29,314 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=7 1a=False 1b=False 2=False (70.7s)
Sep 14 11:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:48:47,434 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 14 11:49:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:49:06,667 main INFO screen DIPPO pass=0 dev=0.0 ins=31.62 pro=38 1a=False 1b=False 2=True (67.8s)
Sep 14 11:49:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:49:26,356 main INFO screen pvedog pass=0 dev=0.0 ins=29.8 pro=75 1a=False 1b=False 2=True (57.0s)
Sep 14 11:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:49:35,768 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:49:35 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:49:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:49:42,884 main INFO screen s pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.4s)
Sep 14 11:50:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:50:03,580 main INFO screen fg pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 14 11:50:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:50:20,667 main INFO screen molly pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (54.3s)
Sep 14 11:50:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:50:47,848 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.9s)
Sep 14 11:51:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:51:11,494 main INFO screen GRIPTO pass=1 dev=0.0 ins=16.54 pro=50 1a=False 1b=False 2=False (51.3s)
Sep 14 11:52:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:52:03,661 main INFO screen PANIC pass=1 dev=0.0 ins=0.0 pro=39 1a=False 1b=False 2=False (63.4s)
Sep 14 11:52:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:52:12,703 main INFO screen TH3000 pass=0 dev=0.0 ins=25.48 pro=21 1a=False 1b=False 2=True (47.6s)
Sep 14 11:52:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:52:19,799 main INFO screen BUNNY pass=0 dev=0.0 ins=26.77 pro=61 1a=False 1b=False 2=True (63.3s)
Sep 14 11:53:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:53:03,673 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.8s)
Sep 14 11:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:54:37,467 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:54:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:54:54,077 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.1s)
Sep 14 11:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:54:55,654 main INFO screen UNITY pass=0 dev=0.0 ins=19.0 pro=72 1a=False 1b=False 2=True (81.7s)
Sep 14 11:54:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:54:57,649 main INFO screen NICHOLAS pass=0 dev=0.0 ins=21.67 pro=45 1a=False 1b=False 2=True (72.4s)
Sep 14 11:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:55:44,752 main INFO screen INU pass=0 dev=0.0 ins=27.08 pro=39 1a=False 1b=False 2=True (50.7s)
Sep 14 11:55:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:55:59,266 main INFO screen TWINEBRAIN pass=0 dev=0.35 ins=78.96 pro=5 1a=False 1b=False 2=True (61.6s)
Sep 14 11:56:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:56:00,775 main INFO screen cap pass=0 dev=0.62 ins=0.0 pro=2 1a=False 1b=False 2=False (65.1s)
Sep 14 11:56:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:56:34,741 main INFO screen UNITY pass=0 dev=0.0 ins=14.3 pro=30 1a=False 1b=False 2=True (50.0s)
Sep 14 11:56:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:56:49,493 main INFO screen fomo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 14 11:56:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:56:53,976 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 14 11:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:57:27,254 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.5s)
Sep 14 11:57:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:57:46,896 main INFO screen WWR pass=0 dev=0.01 ins=105.47 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 14 11:57:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:57:56,787 main INFO screen LMAO pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (67.3s)
Sep 14 11:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:58:20,087 main INFO screen ACW pass=0 dev=0.19 ins=79.12 pro=6 1a=False 1b=True 2=True (52.8s)
Sep 14 11:58:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:58:56,555 main INFO screen TRENCHER pass=1 dev=3.24 ins=3.75 pro=53 1a=False 1b=False 2=False (69.7s)
Sep 14 11:59:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:59:01,457 main INFO screen $HYPOO pass=1 dev=0.21 ins=0.0 pro=13 1a=False 1b=False 2=False (64.7s)
Sep 14 11:59:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:59:15,270 main INFO screen CHILLNINA pass=0 dev=0.06 ins=77.91 pro=8 1a=False 1b=True 2=True (55.2s)
Sep 14 11:59:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:59:53,438 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:59:53 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 12:00:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:00:14,989 main INFO screen RISE pass=0 dev=0.0 ins=0.01 pro=13 1a=False 1b=False 2=True (73.5s)
Sep 14 12:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:00:15,214 main INFO screen SAVPIR pass=0 dev=0.02 ins=0.0 pro=8 1a=False 1b=False 2=False (78.7s)
Sep 14 12:00:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:00:18,970 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.7s)
Sep 14 12:01:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:01:18,209 main INFO screen 双休 pass=0 dev=0.0 ins=6.56 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 14 12:01:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:01:20,145 main INFO screen Liberland pass=0 dev=0.0 ins=23.66 pro=77 1a=False 1b=False 2=True (61.2s)
Sep 14 12:01:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:01:29,873 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (74.7s)
Sep 14 12:02:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:02:16,498 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.4s)
Sep 14 12:02:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:02:16,573 main INFO screen LIKE pass=0 dev=36.97 ins=0.01 pro=5 1a=False 1b=False 2=True (58.4s)
Sep 14 12:02:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:02:43,941 main INFO screen whale pass=1 dev=4.46 ins=0.0 pro=38 1a=False 1b=False 2=False (74.1s)
Sep 14 12:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:03:26,590 main INFO screen VAR pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (70.1s)
Sep 14 12:03:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:03:29,012 main INFO screen BABLLES pass=0 dev=0.0 ins=60.37 pro=42 1a=False 1b=True 2=True (72.4s)
Sep 14 12:03:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:03:38,839 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.9s)
Sep 14 12:04:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:04:28,980 main INFO screen USBDC pass=1 dev=0.0 ins=17.55 pro=49 1a=False 1b=False 2=False (62.4s)
Sep 14 12:04:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:04:39,416 main INFO screen mm pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (70.4s)
Sep 14 12:04:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:04:54,656 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:04:54 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T10:36:11Z
--- update 2026-09-14T10:41:17Z
--- update 2026-09-14T10:46:36Z
--- update 2026-09-14T10:52:03Z
--- update 2026-09-14T10:57:13Z
--- update 2026-09-14T11:02:26Z
--- update 2026-09-14T11:07:36Z
--- update 2026-09-14T11:12:50Z
--- update 2026-09-14T11:17:57Z
--- update 2026-09-14T11:23:05Z
--- update 2026-09-14T11:28:36Z
--- update 2026-09-14T11:33:42Z
--- update 2026-09-14T11:39:15Z
--- update 2026-09-14T11:44:18Z
--- update 2026-09-14T11:49:34Z
Running as unit: schaduwbot-wallets.service; invocation ID: 26c0b13a204d4f3ea8d30078009f924a
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T11:54:36Z
--- update 2026-09-14T11:59:52Z
--- update 2026-09-14T12:04:53Z
```

## Analyses (laatste 25 regels)
```
active
10:19:32   56000 tokens, 5595459 trades, 686652 posities (364s)
10:19:43   58000 tokens, 5779455 trades, 707835 posities (374s)
10:19:55   60000 tokens, 5978226 trades, 735178 posities (386s)
10:20:06   62000 tokens, 6177793 trades, 763023 posities (398s)
10:20:19   64000 tokens, 6387196 trades, 789703 posities (410s)
10:20:31   66000 tokens, 6583185 trades, 815152 posities (422s)
10:20:42   68000 tokens, 6781231 trades, 844581 posities (434s)
10:20:55   70000 tokens, 6994817 trades, 881795 posities (446s)
10:21:01 posities: 893845 uit 7089253 trades (456s)
10:21:15 197310 wallets gerekend
10:21:15 geluk-toets
10:21:55 persistentie
10:21:58 kopieer-simulatie
10:24:01 klaar in 636s -> /opt/schaduwbot/reports/wallets.md
11:49:35 77318 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
11:49:55   ingelezen tot rowid 8356143 (180317 rijen, 180317 bruikbaar)
11:49:56 ingelezen: 180317 nieuwe trades, 180317 bruikbaar (21s)
11:52:15 3000 aankopen van gevolgde wallets geëvalueerd
11:52:38 vroege kopers: 227 voldoen nu, register 398, 243 tokens beoordeeld
11:53:03 grote spelers: saldo van 368 wallets opgehaald
11:53:28 herkomst: 40 posities gekoppeld
11:53:39 klaar in 244s -> /opt/schaduwbot/reports/ledger.md
12:02:40 S1: gezakt — toets n=18454, verkennend n=14656
12:02:40 klaar in 541s -> /opt/schaduwbot/reports/hypotheses.md
12:02:41 probe: 150 transacties ophalen
```

## IJking poolkoers (laatste 12 regels)
```
11:02:26 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:07:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:12:50 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:17:58 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:23:06 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:28:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:33:43 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:39:16 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:44:18 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:49:35 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:54:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:59:55 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
