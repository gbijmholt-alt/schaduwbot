# Schaduwbot status

- tijd: 2026-09-14 20:07:07 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 6 hours, 20 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.4G/38G | geheugen: 2147/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 135179, "tokens_in_memory": 10149, "msgs": 18843264, "trades": 3949041, "creates": 41355, "decode_fail": 345135, "rpc_calls": 113678, "rpc_errors": 7, "sol_usd": 103.37353542308496, "open_positions": 62, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 19:44:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:44:33,569 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.1s)
Sep 14 19:44:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:44:44,702 main INFO screen ☉ pass=0 dev=0.0 ins=48.18 pro=21 1a=False 1b=False 2=True (63.7s)
Sep 14 19:45:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:45:25,023 main INFO screen HODL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.5s)
Sep 14 19:45:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:45:34,899 main INFO screen HOLD pass=0 dev=0.0 ins=37.5 pro=22 1a=False 1b=False 2=True (50.2s)
Sep 14 19:45:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:45:36,263 main INFO screen LION pass=0 dev=0.0 ins=22.37 pro=45 1a=False 1b=False 2=True (69.0s)
Sep 14 19:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:46:17,470 main INFO screen TRICAT pass=0 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=False (52.4s)
Sep 14 19:46:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:46:38,426 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 14 19:46:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:46:41,987 main INFO screen LION pass=0 dev=0.0 ins=23.57 pro=24 1a=False 1b=False 2=False (67.1s)
Sep 14 19:46:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:46:53,653 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:46:53 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:47:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:47:04,118 main INFO screen TRIPLET pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (46.6s)
Sep 14 19:47:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:47:26,376 main INFO screen IRA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (47.9s)
Sep 14 19:47:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:47:44,959 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 14 19:47:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:47:49,683 main INFO screen HOLD pass=0 dev=0.0 ins=21.67 pro=21 1a=False 1b=False 2=True (45.6s)
Sep 14 19:48:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:48:18,167 main INFO screen USGR pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (51.8s)
Sep 14 19:48:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:48:52,544 main INFO screen STEPTOP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.9s)
Sep 14 19:48:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:48:54,800 main INFO screen 50 Scent pass=0 dev=0.0 ins=11.08 pro=41 1a=False 1b=False 2=False (69.8s)
Sep 14 19:49:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:49:19,134 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (61.0s)
Sep 14 19:49:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:49:48,258 main INFO screen ronny pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.7s)
Sep 14 19:49:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:49:49,180 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.4s)
Sep 14 19:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:50:07,257 main INFO screen bright pass=0 dev=0.0 ins=39.58 pro=18 1a=False 1b=False 2=True (48.1s)
Sep 14 19:50:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:50:50,817 main INFO screen BANANA67 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (62.6s)
Sep 14 19:50:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:50:52,581 main INFO screen GAKU pass=0 dev=0.0 ins=1.92 pro=50 1a=False 1b=False 2=False (63.4s)
Sep 14 19:51:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:51:12,758 main INFO screen biketom pass=0 dev=0.0 ins=49.55 pro=38 1a=False 1b=False 2=True (65.5s)
Sep 14 19:51:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:51:41,419 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.6s)
Sep 14 19:51:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:51:46,831 main INFO screen $NPC pass=0 dev=1.62 ins=0.0 pro=3 1a=False 1b=False 2=False (54.2s)
Sep 14 19:51:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:51:53,542 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:51:53 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:52:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:52:00,388 main INFO screen OpenAI pass=0 dev=0.0 ins=136.15 pro=1 1a=False 1b=False 2=True (47.6s)
Sep 14 19:52:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:52:25,728 aiohttp.access INFO 62.171.146.116 [14/Sep/2026:19:52:25 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 19:52:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:52:29,208 main INFO screen bill pass=0 dev=0.0 ins=40.0 pro=3 1a=False 1b=False 2=True (47.8s)
Sep 14 19:52:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:52:43,101 main INFO screen RISE pass=0 dev=0.0 ins=4.38 pro=3 1a=False 1b=False 2=True (56.3s)
Sep 14 19:52:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:52:53,135 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (52.7s)
Sep 14 19:53:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:53:18,516 main INFO screen Claude pass=0 dev=0.19 ins=123.57 pro=1 1a=False 1b=False 2=True (49.3s)
Sep 14 19:53:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:53:33,176 main INFO screen Mayor pass=0 dev=0.0 ins=40.28 pro=3 1a=False 1b=False 2=True (50.1s)
Sep 14 19:53:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:53:41,282 main INFO screen AMC pass=0 dev=0.01 ins=123.48 pro=1 1a=False 1b=False 2=True (48.1s)
Sep 14 19:54:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:54:06,146 main INFO screen FAIR pass=0 dev=0.01 ins=124.51 pro=1 1a=False 1b=False 2=True (47.6s)
Sep 14 19:54:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:54:24,348 main INFO screen WIFBIKE pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (51.2s)
Sep 14 19:54:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:54:44,665 main INFO screen FOUR pass=0 dev=0.0 ins=30.84 pro=56 1a=False 1b=False 2=True (63.4s)
Sep 14 19:54:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:54:58,135 main INFO screen NTDA pass=0 dev=0.0 ins=120.73 pro=1 1a=False 1b=False 2=True (52.0s)
Sep 14 19:55:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:55:14,944 main INFO screen TRIPAD pass=0 dev=0.0 ins=149.31 pro=0 1a=False 1b=False 2=True (50.6s)
Sep 14 19:55:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:55:31,059 main INFO screen Mayor pass=0 dev=0.0 ins=39.85 pro=2 1a=False 1b=False 2=True (46.4s)
Sep 14 19:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:55:48,338 main INFO screen clear.fun pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.2s)
Sep 14 19:56:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:56:02,121 main INFO screen SMOWL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (47.2s)
Sep 14 19:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:56:35,275 main INFO screen 4 pass=0 dev=0.0 ins=36.87 pro=56 1a=False 1b=False 2=True (64.2s)
Sep 14 19:56:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:56:42,217 main INFO screen TH3000 pass=0 dev=0.0 ins=40.66 pro=5 1a=False 1b=False 2=True (53.9s)
Sep 14 19:56:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:56:59,845 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:19:56:59 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 19:57:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:57:11,452 main INFO screen Challenge pass=0 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=False (69.3s)
Sep 14 19:57:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:57:31,183 main INFO screen MoMo pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.9s)
Sep 14 19:57:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:57:31,489 main INFO screen FAR pass=0 dev=0.0 ins=40.96 pro=1 1a=False 1b=False 2=True (49.3s)
Sep 14 19:58:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:58:04,314 main INFO screen Duvet pass=0 dev=0.0 ins=43.71 pro=23 1a=False 1b=False 2=True (52.9s)
Sep 14 19:58:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:58:16,962 main INFO screen AIRDROP pass=0 dev=0.0 ins=40.16 pro=1 1a=False 1b=False 2=True (45.8s)
Sep 14 19:58:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:58:24,437 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (52.9s)
Sep 14 19:58:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:58:51,416 main INFO screen AIRDROP pass=0 dev=0.0 ins=39.91 pro=0 1a=False 1b=False 2=True (47.1s)
Sep 14 19:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:59:04,057 main INFO screen ADOG pass=0 dev=0.0 ins=41.05 pro=0 1a=False 1b=False 2=True (47.1s)
Sep 14 19:59:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:59:09,837 main INFO screen ADOG pass=0 dev=0.0 ins=40.96 pro=0 1a=False 1b=False 2=True (45.4s)
Sep 14 19:59:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 19:59:40,525 main INFO screen AIRDROP pass=0 dev=0.0 ins=31.5 pro=5 1a=False 1b=False 2=True (49.1s)
Sep 14 20:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:00:15,183 main INFO screen BOOBS pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (71.1s)
Sep 14 20:00:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:00:18,008 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (68.2s)
Sep 14 20:00:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:00:39,925 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 14 20:01:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:01:05,504 main INFO screen HNMMMM pass=0 dev=0.0 ins=40.37 pro=1 1a=False 1b=False 2=True (47.5s)
Sep 14 20:01:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:01:11,659 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.5s)
Sep 14 20:01:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:01:36,468 main INFO screen PUMP10 pass=0 dev=0.0 ins=40.86 pro=5 1a=False 1b=False 2=True (56.5s)
Sep 14 20:01:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:01:59,942 main INFO screen fone pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 14 20:02:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:03,857 main INFO screen FUTUREIF pass=0 dev=0.0 ins=39.16 pro=2 1a=False 1b=False 2=True (52.2s)
Sep 14 20:02:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:04,684 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:02:04 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 20:02:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:22,971 main INFO screen Kirk pass=0 dev=0.0 ins=40.2 pro=2 1a=False 1b=False 2=True (46.5s)
Sep 14 20:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:50,989 main INFO screen cashcat pass=0 dev=0.0 ins=31.29 pro=33 1a=False 1b=False 2=True (47.1s)
Sep 14 20:02:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:02:54,313 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.4s)
Sep 14 20:03:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:03:15,761 main INFO screen cashcat pass=0 dev=0.0 ins=40.37 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 14 20:03:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:03:39,834 main INFO screen cashcat pass=0 dev=0.0 ins=40.31 pro=2 1a=False 1b=False 2=True (48.8s)
Sep 14 20:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:04,009 main INFO screen DOM pass=0 dev=0.0 ins=17.0 pro=73 1a=False 1b=False 2=True (69.7s)
Sep 14 20:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:04,684 main INFO screen FINE pass=0 dev=0.0 ins=40.56 pro=1 1a=False 1b=False 2=True (48.9s)
Sep 14 20:04:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:49,223 main INFO screen FINE pass=0 dev=0.0 ins=18.52 pro=56 1a=False 1b=False 2=False (45.2s)
Sep 14 20:04:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:49,288 main INFO screen glob pass=0 dev=0.0 ins=50.52 pro=21 1a=False 1b=False 2=True (69.5s)
Sep 14 20:04:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:04:55,059 main INFO screen FINE pass=0 dev=0.0 ins=40.28 pro=0 1a=False 1b=False 2=True (50.4s)
Sep 14 20:05:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:05:57,757 main INFO screen     NWN pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.5s)
Sep 14 20:05:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:05:59,699 main INFO screen WOFI pass=0 dev=0.78 ins=139.38 pro=1 1a=False 1b=False 2=True (64.6s)
Sep 14 20:06:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:06:00,588 main INFO screen pumpcat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.3s)
Sep 14 20:06:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:06:49,884 main INFO screen taxcat pass=0 dev=0.0 ins=39.98 pro=2 1a=False 1b=False 2=True (50.2s)
Sep 14 20:07:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:05,111 main INFO screen PVE pass=0 dev=0.0 ins=79.98 pro=67 1a=False 1b=False 2=False (67.4s)
Sep 14 20:07:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 20:07:07,606 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:20:07:07 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T18:40:39Z
--- update 2026-09-14T18:45:49Z
--- update 2026-09-14T18:50:57Z
--- update 2026-09-14T18:56:05Z
--- update 2026-09-14T19:01:07Z
--- update 2026-09-14T19:06:12Z
--- update 2026-09-14T19:11:15Z
--- update 2026-09-14T19:16:28Z
--- update 2026-09-14T19:21:34Z
--- update 2026-09-14T19:26:36Z
--- update 2026-09-14T19:31:43Z
--- update 2026-09-14T19:36:46Z
--- update 2026-09-14T19:41:50Z
--- update 2026-09-14T19:46:52Z
--- update 2026-09-14T19:51:52Z
--- update 2026-09-14T19:56:58Z
--- update 2026-09-14T20:02:03Z
Running as unit: schaduwbot-wallets.service; invocation ID: 14498679f71340f08b872ad37a3b0138
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T20:07:06Z
```

## Analyses (laatste 25 regels)
```
active
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
20:02:04 89494 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
20:02:30   ingelezen tot rowid 9373289 (200000 rijen, 200000 bruikbaar)
20:02:39   ingelezen tot rowid 9499553 (326264 rijen, 326264 bruikbaar)
20:02:40 ingelezen: 326264 nieuwe trades, 326264 bruikbaar (36s)
20:05:17 3000 aankopen van gevolgde wallets geëvalueerd
20:06:08 vroege kopers: 256 voldoen nu, register 449, 443 tokens beoordeeld
20:06:39 grote spelers: saldo van 479 wallets opgehaald
20:07:06 herkomst: 40 posities gekoppeld
```

## IJking poolkoers (laatste 12 regels)
```
19:06:13 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:11:16 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:16:29 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:21:34 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:26:36 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:31:44 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:36:47 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:41:51 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:46:53 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:51:53 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
19:56:59 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:02:04 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
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
