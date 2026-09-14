# Schaduwbot status

- tijd: 2026-09-14 05:25:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 15 hours, 38 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 2110/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 82268, "tokens_in_memory": 6391, "msgs": 11087445, "trades": 2295630, "creates": 24061, "decode_fail": 199822, "rpc_calls": 67168, "rpc_errors": 3, "sol_usd": 100.99640969752846, "open_positions": 24, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 04:43:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:39,488 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:43:39 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:43:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:43:48,340 main INFO screen JAKE pass=1 dev=0.04 ins=0.0 pro=13 1a=False 1b=False 2=False (66.6s)
Sep 14 04:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:44:19,145 main INFO screen Is pass=0 dev=0.0 ins=27.32 pro=59 1a=False 1b=False 2=True (67.5s)
Sep 14 04:45:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:45:38,040 main INFO screen TEIZA pass=0 dev=10.0 ins=28.42 pro=18 1a=False 1b=True 2=False (53.2s)
Sep 14 04:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:15,353 main INFO screen Humanity pass=1 dev=0.0 ins=4.23 pro=59 1a=False 1b=False 2=False (79.4s)
Sep 14 04:46:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:16,445 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=5 1a=False 1b=False 2=False (77.4s)
Sep 14 04:46:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:46:58,743 main INFO screen Humanity pass=0 dev=0.0 ins=11.81 pro=50 1a=False 1b=False 2=True (80.7s)
Sep 14 04:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:47:10,416 main INFO screen BikeTyson pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.1s)
Sep 14 04:47:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:47:35,230 main INFO screen Sloth pass=1 dev=0.0 ins=9.26 pro=56 1a=False 1b=False 2=False (72.4s)
Sep 14 04:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:48:31,018 main INFO screen SpaceX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 14 04:48:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:48:50,515 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:48:50 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:49:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:49:01,443 main INFO screen ZAP pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 14 04:49:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:49:45,876 main INFO screen ocs pass=0 dev=9.38 ins=24.34 pro=21 1a=False 1b=False 2=False (48.4s)
Sep 14 04:50:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:50:45,394 main INFO screen Jerry pass=1 dev=0.0 ins=19.41 pro=44 1a=False 1b=False 2=False (53.0s)
Sep 14 04:51:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:33,396 main INFO screen mictyson pass=0 dev=1.74 ins=77.57 pro=2 1a=False 1b=False 2=True (68.4s)
Sep 14 04:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:35,283 main INFO screen USDF pass=0 dev=71.24 ins=0.0 pro=10 1a=False 1b=False 2=True (70.9s)
Sep 14 04:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:51:56,440 main INFO screen FOMO pass=0 dev=0.0 ins=15.35 pro=62 1a=False 1b=False 2=True (71.0s)
Sep 14 04:52:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:52:42,389 main INFO screen Rotator pass=0 dev=0.0 ins=38.08 pro=76 1a=False 1b=False 2=True (69.0s)
Sep 14 04:52:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:52:43,681 main INFO screen INBRED pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (68.4s)
Sep 14 04:53:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:01,339 main INFO screen FakeTaxi pass=1 dev=0.0 ins=0.24 pro=32 1a=False 1b=False 2=False (64.9s)
Sep 14 04:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:54,808 main INFO screen Fork pass=0 dev=0.0 ins=42.27 pro=67 1a=False 1b=False 2=True (71.1s)
Sep 14 04:53:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:53:56,137 main INFO screen HI pass=0 dev=0.0 ins=34.37 pro=70 1a=False 1b=False 2=True (73.7s)
Sep 14 04:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:54:00,493 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:54:00 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:54:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:54:05,584 main INFO screen FakeTaxi pass=0 dev=55.95 ins=0.0 pro=59 1a=False 1b=True 2=False (64.2s)
Sep 14 04:55:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:55:33,651 main INFO screen SHELL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.9s)
Sep 14 04:57:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:57:48,001 main INFO screen Human pass=0 dev=0.0 ins=25.9 pro=68 1a=False 1b=False 2=True (61.7s)
Sep 14 04:58:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:05,146 main INFO screen Basilisk pass=0 dev=0.0 ins=29.82 pro=74 1a=False 1b=False 2=True (59.5s)
Sep 14 04:58:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:22,753 main INFO screen SubSneak pass=0 dev=0.01 ins=0.0 pro=2 1a=False 1b=False 2=False (67.7s)
Sep 14 04:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:54,230 main INFO screen Luddites pass=1 dev=0.0 ins=4.79 pro=38 1a=False 1b=False 2=False (66.2s)
Sep 14 04:58:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:58:57,215 main INFO screen NINA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.1s)
Sep 14 04:59:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:59:10,783 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:59:10 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:59:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:59:56,967 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 14 05:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:00:45,636 main INFO screen SHROOMS pass=0 dev=0.7 ins=55.34 pro=11 1a=False 1b=True 2=True (55.6s)
Sep 14 05:00:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:00:57,091 main INFO screen trumpndmp pass=0 dev=8.06 ins=0.0 pro=11 1a=False 1b=False 2=False (64.7s)
Sep 14 05:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:01:01,724 main INFO screen LMAO pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (64.3s)
Sep 14 05:01:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:01:58,562 main INFO screen BPCATE pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (72.9s)
Sep 14 05:02:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:02:03,352 main INFO screen PONSLv pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=False 2=True (66.3s)
Sep 14 05:02:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:02:32,689 main INFO screen REVPEPE pass=0 dev=0.07 ins=0.0 pro=4 1a=False 1b=False 2=False (68.9s)
Sep 14 05:03:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:03:17,470 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.1s)
Sep 14 05:03:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:03:38,352 main INFO screen HYPILL pass=0 dev=0.0 ins=21.35 pro=65 1a=False 1b=False 2=True (61.1s)
Sep 14 05:04:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:04:32,553 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:04:32 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:04:38,913 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=5 1a=False 1b=False 2=False (68.3s)
Sep 14 05:05:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:05:22,443 main INFO screen TWICE pass=0 dev=5.01 ins=0.0 pro=54 1a=False 1b=False 2=False (66.8s)
Sep 14 05:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:07:04,675 main INFO screen Sloth pass=0 dev=0.0 ins=14.64 pro=64 1a=False 1b=False 2=True (63.3s)
Sep 14 05:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:07:19,910 main INFO screen AI pass=0 dev=0.0 ins=9.55 pro=34 1a=False 1b=False 2=True (67.8s)
Sep 14 05:08:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:08:25,848 main INFO screen PETIX pass=0 dev=10.0 ins=23.63 pro=18 1a=False 1b=False 2=False (73.7s)
Sep 14 05:09:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:24,134 main INFO screen NFA pass=0 dev=0.0 ins=36.86 pro=65 1a=False 1b=False 2=True (76.1s)
Sep 14 05:09:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:26,959 main INFO screen $AURA pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (79.0s)
Sep 14 05:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:36,564 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:09:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:09:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:09:37,411 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (70.9s)
Sep 14 05:10:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:24,183 main INFO screen BLAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (60.0s)
Sep 14 05:10:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:51,316 main INFO screen MTC pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (84.4s)
Sep 14 05:10:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:10:59,854 main INFO screen GS pass=0 dev=0.0 ins=27.71 pro=73 1a=False 1b=False 2=True (82.4s)
Sep 14 05:11:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:11:29,673 main INFO screen FYPM pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (65.5s)
Sep 14 05:12:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:12:39,634 main INFO screen ANTIAI pass=0 dev=0.0 ins=28.72 pro=29 1a=False 1b=False 2=False (75.3s)
Sep 14 05:13:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:13:51,175 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (56.5s)
Sep 14 05:14:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:01,197 main INFO screen Rabbitson pass=0 dev=0.7 ins=55.23 pro=14 1a=False 1b=True 2=True (55.6s)
Sep 14 05:14:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:11,041 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 14 05:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:37,044 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:14:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 05:14:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:46,631 main INFO screen BEAST pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (55.5s)
Sep 14 05:14:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:14:54,324 main INFO screen CIT pass=0 dev=7.67 ins=27.19 pro=18 1a=False 1b=False 2=False (53.1s)
Sep 14 05:15:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:15:09,144 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 14 05:15:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:15:38,902 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 14 05:15:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:15:54,355 aiohttp.access INFO 32.193.241.45 [14/Sep/2026:05:15:54 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
Sep 14 05:16:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:16:15,106 main INFO screen SolSlugs pass=0 dev=0.0 ins=24.62 pro=56 1a=False 1b=False 2=True (80.8s)
Sep 14 05:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:16:33,094 main INFO screen PXL pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=True (83.9s)
Sep 14 05:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:16:53,920 main INFO screen EAGLEF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.0s)
Sep 14 05:17:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:17:09,967 main INFO screen KIBA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 14 05:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:17:52,861 main INFO screen BAAN-KUN pass=0 dev=0.0 ins=19.99 pro=66 1a=False 1b=False 2=True (79.8s)
Sep 14 05:19:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:21,414 main INFO screen dog pass=0 dev=0.0 ins=9.26 pro=57 1a=False 1b=False 2=True (69.8s)
Sep 14 05:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:22,969 main INFO screen LaMisery pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (71.8s)
Sep 14 05:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:35,614 main INFO screen FYPM pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.1s)
Sep 14 05:19:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:19:59,619 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:19:59 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 05:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:20:16,668 main INFO screen SCT pass=0 dev=8.16 ins=28.4 pro=17 1a=False 1b=False 2=False (55.3s)
Sep 14 05:22:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:22:49,152 main INFO screen BEER pass=0 dev=0.0 ins=37.17 pro=76 1a=False 1b=False 2=True (67.7s)
Sep 14 05:22:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:22:51,466 main INFO screen MadisonBeer pass=0 dev=0.0 ins=39.93 pro=76 1a=False 1b=False 2=True (64.2s)
Sep 14 05:23:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:23:54,668 main INFO screen flyhouse pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (57.3s)
Sep 14 05:24:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:24:48,334 main INFO screen AI pass=0 dev=0.0 ins=23.04 pro=61 1a=False 1b=False 2=True (66.8s)
Sep 14 05:24:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:24:52,350 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 14 05:25:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 05:25:15,762 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:05:25:15 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T03:56:38Z
--- update 2026-09-14T04:02:07Z
--- update 2026-09-14T04:07:29Z
--- update 2026-09-14T04:12:34Z
--- update 2026-09-14T04:17:36Z
--- update 2026-09-14T04:22:44Z
--- update 2026-09-14T04:28:04Z
--- update 2026-09-14T04:33:32Z
--- update 2026-09-14T04:38:36Z
--- update 2026-09-14T04:43:38Z
--- update 2026-09-14T04:48:49Z
--- update 2026-09-14T04:53:59Z
Running as unit: schaduwbot-wallets.service; invocation ID: f736891630a542c892110e5793ff0a8a
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T04:59:09Z
--- update 2026-09-14T05:04:31Z
--- update 2026-09-14T05:09:35Z
--- update 2026-09-14T05:14:36Z
--- update 2026-09-14T05:19:58Z
--- update 2026-09-14T05:25:14Z
```

## Analyses (laatste 25 regels)
```
active
05:10:14 na-migratie: 100 paren te checken
05:12:33 na-migratie: 78 paren, 20 prijzen
05:16:48 gemigreerde koersen: 79 gedaan, 1681 te gaan
05:16:49 klaar (674 rpc-calls, 67 fouten)
05:20:56 klaar in 248s -> /opt/schaduwbot/reports/lotgevallen.md
05:21:16   2000 nieuwe tokens doorgerekend
05:21:39 klaar in 42s: 44305 tokens, 2530 nieuw -> /opt/schaduwbot/reports/video_replay.md
05:21:40 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-11 05:21 UTC
05:21:43 97229 tokens geladen
05:21:57   2000 tokens, 180860 trades, 20149 posities (14s)
05:22:12   4000 tokens, 412432 trades, 59147 posities (28s)
05:22:24   6000 tokens, 618135 trades, 82516 posities (40s)
05:22:35   8000 tokens, 802848 trades, 102813 posities (51s)
05:22:46   10000 tokens, 991221 trades, 126829 posities (62s)
05:22:58   12000 tokens, 1204024 trades, 156160 posities (74s)
05:23:09   14000 tokens, 1402743 trades, 177890 posities (86s)
05:23:21   16000 tokens, 1598653 trades, 199438 posities (98s)
05:23:33   18000 tokens, 1792659 trades, 223255 posities (109s)
05:23:44   20000 tokens, 1985457 trades, 244562 posities (121s)
05:23:57   22000 tokens, 2189103 trades, 274150 posities (133s)
05:24:10   24000 tokens, 2417264 trades, 307380 posities (147s)
05:24:24   26000 tokens, 2629575 trades, 338454 posities (161s)
05:24:38   28000 tokens, 2846331 trades, 368905 posities (174s)
05:24:50   30000 tokens, 3033145 trades, 389746 posities (187s)
05:25:04   32000 tokens, 3240617 trades, 415355 posities (200s)
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
