# Schaduwbot status

- tijd: 2026-09-14 14:10:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 23 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.8G/38G | geheugen: 1916/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 113789, "tokens_in_memory": 5444, "msgs": 13380006, "trades": 3052757, "creates": 31285, "decode_fail": 256690, "rpc_calls": 92261, "rpc_errors": 7, "sol_usd": 101.61875514310871, "open_positions": 56, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 13:45:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:16,636 main INFO screen HEISTNVIDI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 14 13:45:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:41,149 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.5s)
Sep 14 13:45:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:45:44,747 main INFO screen LEMEOW pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.4s)
Sep 14 13:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:12,692 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.1s)
Sep 14 13:46:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:38,272 main INFO screen SPIN pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 13:46:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:46:42,174 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 14 13:47:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:10,902 main INFO screen Charlie pass=0 dev=0.0 ins=20.44 pro=70 1a=False 1b=False 2=True (58.2s)
Sep 14 13:47:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:31,428 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 13:47:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:47:36,840 main INFO screen MESOL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.7s)
Sep 14 13:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:15,456 main INFO screen BBP pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (64.6s)
Sep 14 13:48:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:22,614 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.2s)
Sep 14 13:48:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:48:27,241 main INFO screen robinpepe pass=0 dev=0.14 ins=78.78 pro=9 1a=False 1b=True 2=True (50.4s)
Sep 14 13:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:13,605 main INFO screen SUNK pass=0 dev=0.0 ins=26.75 pro=10 1a=False 1b=False 2=True (51.0s)
Sep 14 13:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:20,576 main INFO screen PUMPFAST pass=0 dev=0.0 ins=16.17 pro=64 1a=False 1b=False 2=True (65.1s)
Sep 14 13:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:35,772 main INFO screen POLLY pass=0 dev=0.0 ins=30.99 pro=53 1a=False 1b=False 2=True (68.5s)
Sep 14 13:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:49:56,630 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:49:56 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:50:07,509 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 14 13:50:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:50:09,118 main INFO screen ApeOnFone pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (48.5s)
Sep 14 13:50:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:50:23,762 main INFO screen Marvel pass=0 dev=0.0 ins=64.84 pro=1 1a=False 1b=False 2=True (48.0s)
Sep 14 13:51:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:51:10,468 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 14 13:51:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:51:11,922 main INFO screen UAR pass=0 dev=1.91 ins=0.0 pro=3 1a=False 1b=False 2=False (62.8s)
Sep 14 13:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:51:13,942 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.2s)
Sep 14 13:52:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:52:13,418 main INFO screen Nole pass=1 dev=0.0 ins=17.92 pro=33 1a=False 1b=False 2=False (62.9s)
Sep 14 13:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:52:15,375 main INFO screen TREBH pass=1 dev=0.0 ins=13.55 pro=51 1a=False 1b=False 2=False (63.5s)
Sep 14 13:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:52:15,806 main INFO screen Duck pass=0 dev=0.0 ins=19.56 pro=51 1a=False 1b=False 2=True (61.9s)
Sep 14 13:53:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:53:05,733 main INFO screen solhouse pass=0 dev=0.0 ins=20.18 pro=22 1a=False 1b=False 2=False (52.3s)
Sep 14 13:53:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:53:18,113 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 14 13:53:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:53:19,617 main INFO screen Dr. E pass=1 dev=0.0 ins=19.44 pro=23 1a=False 1b=False 2=False (64.2s)
Sep 14 13:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:53:54,907 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (49.2s)
Sep 14 13:54:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:54:10,500 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 14 13:54:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:54:22,427 main INFO screen KFC pass=0 dev=0.0 ins=28.24 pro=72 1a=False 1b=False 2=True (64.3s)
Sep 14 13:54:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:54:49,838 main INFO screen KFC pass=1 dev=0.0 ins=8.28 pro=37 1a=False 1b=False 2=False (54.9s)
Sep 14 13:55:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:55:03,154 main INFO screen FUD pass=0 dev=0.0 ins=17.22 pro=37 1a=False 1b=False 2=True (52.7s)
Sep 14 13:55:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:55:08,142 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:13:55:08 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 13:55:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:55:13,935 main INFO screen STONKSON pass=0 dev=0.0 ins=36.87 pro=18 1a=False 1b=False 2=True (51.5s)
Sep 14 13:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:55:38,679 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.8s)
Sep 14 13:55:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:55:53,227 main INFO screen $JACK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.1s)
Sep 14 13:56:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:56:06,737 main INFO screen EMS pass=1 dev=0.0 ins=19.63 pro=25 1a=False 1b=False 2=False (52.8s)
Sep 14 13:56:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:56:37,789 main INFO screen STONKSON pass=0 dev=0.0 ins=36.03 pro=49 1a=False 1b=False 2=True (59.1s)
Sep 14 13:56:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:56:48,783 main INFO screen BABYLMAO! pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (55.6s)
Sep 14 13:57:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:57:01,081 main INFO screen STONKSON pass=0 dev=0.0 ins=36.13 pro=31 1a=False 1b=False 2=True (54.3s)
Sep 14 13:57:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:57:44,380 main INFO screen Spawn pass=0 dev=0.0 ins=9.32 pro=68 1a=False 1b=False 2=True (66.6s)
Sep 14 13:57:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:57:47,465 main INFO screen KIBA pass=0 dev=0.0 ins=132.24 pro=1 1a=False 1b=False 2=True (58.7s)
Sep 14 13:57:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:57:52,882 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.8s)
Sep 14 13:58:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:58:57,398 main INFO screen DogLMAO pass=0 dev=0.0 ins=0.21 pro=8 1a=False 1b=False 2=False (73.0s)
Sep 14 13:59:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:59:01,322 main INFO screen 胆子肥 pass=0 dev=0.0 ins=28.44 pro=9 1a=False 1b=False 2=False (73.9s)
Sep 14 13:59:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 13:59:02,692 main INFO screen STONKSON pass=0 dev=0.0 ins=36.63 pro=29 1a=False 1b=False 2=True (69.8s)
Sep 14 14:00:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:00:16,310 main INFO screen Pro-Human pass=0 dev=0.0 ins=32.19 pro=45 1a=False 1b=False 2=True (78.9s)
Sep 14 14:00:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:00:16,861 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:00:16 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:00:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:00:18,989 main INFO screen BIKINIHOUSE pass=1 dev=0.0 ins=19.42 pro=31 1a=False 1b=False 2=False (77.7s)
Sep 14 14:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:00:23,502 main INFO screen ZGUY pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=False 2=True (80.8s)
Sep 14 14:01:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:01:07,472 main INFO screen STONKSON pass=0 dev=0.0 ins=36.63 pro=13 1a=False 1b=False 2=True (51.2s)
Sep 14 14:01:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:01:29,646 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.7s)
Sep 14 14:01:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:01:33,425 main INFO screen LMAOOF pass=1 dev=4.74 ins=0.64 pro=59 1a=False 1b=False 2=False (69.9s)
Sep 14 14:02:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:02:06,463 main INFO screen STONKSON pass=0 dev=0.0 ins=36.63 pro=17 1a=False 1b=False 2=True (59.0s)
Sep 14 14:02:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:02:24,947 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.3s)
Sep 14 14:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:02:36,747 main INFO screen Eric  pass=0 dev=0.0 ins=34.75 pro=62 1a=False 1b=False 2=True (63.3s)
Sep 14 14:03:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:03:06,149 main INFO screen ELON pass=0 dev=0.0 ins=20.03 pro=30 1a=False 1b=False 2=False (59.7s)
Sep 14 14:03:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:03:20,994 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.0s)
Sep 14 14:03:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:03:45,390 main INFO screen GEEKBAR pass=0 dev=0.0 ins=37.49 pro=66 1a=False 1b=False 2=True (68.6s)
Sep 14 14:04:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:04:01,107 main INFO screen TSLAx pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (55.0s)
Sep 14 14:04:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:04:32,225 main INFO screen STONKSON pass=0 dev=0.0 ins=36.63 pro=31 1a=True 1b=False 2=True (71.2s)
Sep 14 14:04:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:04:35,850 main INFO screen 50DAYS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.5s)
Sep 14 14:05:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:05:02,911 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.8s)
Sep 14 14:05:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:05:30,953 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:05:30 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:05:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:05:38,057 main INFO screen Human pass=0 dev=0.0 ins=20.4 pro=26 1a=False 1b=False 2=False (62.2s)
Sep 14 14:05:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:05:48,863 main INFO screen HAI pass=1 dev=0.0 ins=8.51 pro=44 1a=False 1b=False 2=False (76.6s)
Sep 14 14:06:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:06:01,958 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.0s)
Sep 14 14:06:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:06:39,593 main INFO screen LMEOW pass=0 dev=0.0 ins=2.27 pro=4 1a=False 1b=False 2=False (61.5s)
Sep 14 14:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:06:56,983 main INFO screen BCATE pass=0 dev=3.15 ins=58.18 pro=28 1a=False 1b=False 2=True (68.1s)
Sep 14 14:07:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:07:04,401 main INFO screen NOTALIVE pass=0 dev=0.0 ins=17.57 pro=16 1a=False 1b=False 2=True (62.4s)
Sep 14 14:07:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:07:47,859 main INFO screen TRADY pass=1 dev=0.0 ins=0.21 pro=20 1a=False 1b=False 2=False (68.3s)
Sep 14 14:08:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:08:00,289 main INFO screen HashFly pass=1 dev=0.0 ins=0.14 pro=69 1a=False 1b=False 2=False (63.3s)
Sep 14 14:08:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:08:05,908 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.5s)
Sep 14 14:08:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:08:49,806 main INFO screen jeffed pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (61.9s)
Sep 14 14:09:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:09:29,332 main INFO screen Nubzuki pass=0 dev=0.0 ins=23.41 pro=61 1a=False 1b=False 2=True (83.4s)
Sep 14 14:09:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:09:32,237 main INFO screen Nubzuki pass=0 dev=0.0 ins=24.58 pro=75 1a=False 1b=False 2=True (91.9s)
Sep 14 14:10:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:10:14,492 main INFO screen $AIDOGE pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (84.7s)
Sep 14 14:10:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:10:36,872 main INFO screen SUPERHERO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (64.6s)
Sep 14 14:10:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:10:37,237 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:10:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T12:41:54Z
--- update 2026-09-14T12:47:08Z
--- update 2026-09-14T12:52:27Z
--- update 2026-09-14T12:57:36Z
--- update 2026-09-14T13:03:06Z
--- update 2026-09-14T13:08:21Z
--- update 2026-09-14T13:13:36Z
--- update 2026-09-14T13:18:54Z
--- update 2026-09-14T13:23:56Z
--- update 2026-09-14T13:29:19Z
--- update 2026-09-14T13:34:21Z
--- update 2026-09-14T13:39:33Z
--- update 2026-09-14T13:44:36Z
--- update 2026-09-14T13:49:55Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7b952af92e094c05ae1443fb1b8f089a
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T13:55:06Z
--- update 2026-09-14T14:00:15Z
--- update 2026-09-14T14:05:29Z
--- update 2026-09-14T14:10:36Z
```

## Analyses (laatste 25 regels)
```
active
12:27:50   68000 tokens, 6794379 trades, 846287 posities (429s)
12:28:02   70000 tokens, 6990170 trades, 880107 posities (441s)
12:28:09 posities: 896544 uit 7116580 trades (449s)
12:28:22 198620 wallets gerekend
12:28:23 geluk-toets
12:29:00 persistentie
12:29:03 kopieer-simulatie
12:31:05 klaar in 624s -> /opt/schaduwbot/reports/wallets.md
13:49:56 79238 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
13:50:18   ingelezen tot rowid 8556143 (200000 rijen, 200000 bruikbaar)
13:50:20   ingelezen tot rowid 8575292 (219149 rijen, 219149 bruikbaar)
13:50:21 ingelezen: 219149 nieuwe trades, 219149 bruikbaar (25s)
13:52:41 3000 aankopen van gevolgde wallets geëvalueerd
13:53:06 vroege kopers: 247 voldoen nu, register 420, 298 tokens beoordeeld
13:53:33 grote spelers: saldo van 461 wallets opgehaald
13:54:19 herkomst: 40 posities gekoppeld
13:54:28 klaar in 273s -> /opt/schaduwbot/reports/ledger.md
14:04:02 S1: gezakt — toets n=19541, verkennend n=14656
14:04:02 klaar in 573s -> /opt/schaduwbot/reports/hypotheses.md
14:04:03 probe: 150 transacties ophalen
14:07:29 poolveld: 16 pools bekeken, 0 te gaan -> vastgesteld @43
14:08:42 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
14:08:42 prijsijk: n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:08:43 na-migratie: 100 paren te checken
14:10:32 na-migratie: 49 paren, 8 prijzen
```

## IJking poolkoers (laatste 12 regels)
```
14:00:18 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
Traceback (most recent call last):
  File "/opt/schaduwbot/pumpswap.py", line 1183, in <module>
    main()
    ~~~~^^
  File "/opt/schaduwbot/pumpswap.py", line 1114, in main
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
14:10:36 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
