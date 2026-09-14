# Schaduwbot status

- tijd: 2026-09-14 14:26:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 39 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.8G/38G | geheugen: 2105/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 114734, "tokens_in_memory": 5595, "msgs": 13665916, "trades": 3087744, "creates": 31648, "decode_fail": 259705, "rpc_calls": 93210, "rpc_errors": 7, "sol_usd": 101.40746952105366, "open_positions": 58, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 14:10:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:10:42,668 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.3s)
Sep 14 14:11:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:11:11,833 main INFO screen $HAIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.3s)
Sep 14 14:11:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:11:31,309 main INFO screen conviction pass=0 dev=3.97 ins=75.34 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 14 14:11:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:11:47,940 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.3s)
Sep 14 14:12:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:12:07,196 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.4s)
Sep 14 14:12:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:12:41,020 main INFO screen RICK pass=0 dev=0.32 ins=0.0 pro=5 1a=False 1b=False 2=False (69.7s)
Sep 14 14:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:12:46,071 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 14 14:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:13:07,800 main INFO screen MIKESTONK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.6s)
Sep 14 14:13:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:13:39,050 main INFO screen ponspepe pass=0 dev=0.0 ins=79.13 pro=7 1a=False 1b=True 2=True (58.0s)
Sep 14 14:13:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:13:50,619 main INFO screen mm pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (64.5s)
Sep 14 14:14:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:14:00,716 main INFO screen GERO pass=0 dev=0.0 ins=79.13 pro=6 1a=False 1b=True 2=True (52.9s)
Sep 14 14:14:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:14:36,292 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.2s)
Sep 14 14:14:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:14:49,388 main INFO screen ELON pass=1 dev=0.0 ins=18.93 pro=25 1a=False 1b=False 2=False (58.8s)
Sep 14 14:14:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:14:54,544 main INFO screen $HOME pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.8s)
Sep 14 14:15:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:15:31,646 main INFO screen cro pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.4s)
Sep 14 14:15:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:15:45,878 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:15:45 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:15:47,011 main INFO screen RAT pass=0 dev=0.0 ins=29.37 pro=48 1a=False 1b=False 2=True (57.6s)
Sep 14 14:15:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:15:51,615 main INFO screen cro pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.1s)
Sep 14 14:16:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:16:28,201 main INFO screen bikenina pass=0 dev=0.0 ins=78.96 pro=1 1a=False 1b=True 2=True (56.6s)
Sep 14 14:16:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:16:40,862 main INFO screen CHUD pass=0 dev=0.0 ins=50.35 pro=59 1a=False 1b=False 2=True (53.8s)
Sep 14 14:17:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:17:01,736 main INFO screen $OBER pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (70.1s)
Sep 14 14:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:17:37,236 main INFO screen Duo pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 14 14:17:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:17:41,742 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.9s)
Sep 14 14:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:17:57,859 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.1s)
Sep 14 14:18:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:18:54,863 main INFO screen AWARDS150M pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (73.1s)
Sep 14 14:19:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:19:07,808 main INFO screen Bolt pass=1 dev=0.0 ins=3.19 pro=48 1a=False 1b=False 2=False (90.6s)
Sep 14 14:19:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:19:21,073 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.8 pro=20 1a=False 1b=False 2=True (83.2s)
Sep 14 14:20:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:20:01,586 main INFO screen ADFREE pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (66.7s)
Sep 14 14:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:20:16,450 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.6s)
Sep 14 14:20:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:20:23,406 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 14 14:20:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:20:59,409 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:20:59 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 14:21:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:21:18,451 main INFO screen HumanCoin pass=0 dev=0.0 ins=27.41 pro=60 1a=False 1b=False 2=True (76.9s)
Sep 14 14:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:21:34,492 main INFO screen CARD pass=0 dev=0.0 ins=20.06 pro=31 1a=False 1b=False 2=False (71.1s)
Sep 14 14:21:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:21:36,381 main INFO screen EXIT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (79.9s)
Sep 14 14:22:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:22:24,040 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.6s)
Sep 14 14:22:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:22:45,957 main INFO screen Human pass=1 dev=0.0 ins=17.3 pro=60 1a=False 1b=False 2=False (69.6s)
Sep 14 14:22:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:22:48,727 main INFO screen HumanCoin pass=1 dev=0.0 ins=17.59 pro=60 1a=False 1b=False 2=False (74.2s)
Sep 14 14:23:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:23:39,220 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.65 pro=17 1a=False 1b=False 2=True (75.2s)
Sep 14 14:23:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:23:51,292 main INFO screen NVDA pass=0 dev=0.0 ins=79.36 pro=1 1a=False 1b=False 2=True (65.3s)
Sep 14 14:23:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:23:52,950 main INFO screen DAVID pass=0 dev=0.0 ins=19.92 pro=78 1a=False 1b=False 2=True (64.2s)
Sep 14 14:24:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:24:46,881 main INFO screen GUMBALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.7s)
Sep 14 14:24:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:24:49,288 main INFO screen KIBA pass=0 dev=0.0 ins=126.1 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 14 14:25:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:03,862 main INFO screen human pass=0 dev=0.0 ins=20.71 pro=64 1a=False 1b=False 2=True (70.9s)
Sep 14 14:25:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:51,400 main INFO screen WTF pass=0 dev=0.0 ins=75.89 pro=0 1a=True 1b=True 2=True (64.5s)
Sep 14 14:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:25:52,784 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.64 pro=6 1a=False 1b=False 2=True (63.5s)
Sep 14 14:26:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:26:21,858 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:26:21 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T14:15:44Z
--- update 2026-09-14T14:20:58Z
--- update 2026-09-14T14:26:20Z
```

## Analyses (laatste 25 regels)
```
active
14:07:29 poolveld: 16 pools bekeken, 0 te gaan -> vastgesteld @43
14:08:42 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
14:08:42 prijsijk: n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
14:08:43 na-migratie: 100 paren te checken
14:10:32 na-migratie: 49 paren, 8 prijzen
14:15:29 gemigreerde koersen: 103 gedaan, 1453 te gaan
14:15:30 klaar (680 rpc-calls, 76 fouten)
14:22:32 klaar in 422s -> /opt/schaduwbot/reports/lotgevallen.md
14:23:17 klaar in 44s: 49915 tokens, 1763 nieuw -> /opt/schaduwbot/reports/video_replay.md
14:23:18 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-11 14:23 UTC
14:23:22 104803 tokens geladen
14:23:34   2000 tokens, 169899 trades, 16257 posities (12s)
14:23:49   4000 tokens, 392338 trades, 51363 posities (27s)
14:23:59   6000 tokens, 596778 trades, 74469 posities (37s)
14:24:10   8000 tokens, 784842 trades, 94322 posities (48s)
14:24:21   10000 tokens, 983833 trades, 120214 posities (59s)
14:24:33   12000 tokens, 1181915 trades, 146463 posities (71s)
14:24:44   14000 tokens, 1396043 trades, 171672 posities (82s)
14:24:56   16000 tokens, 1593244 trades, 194924 posities (94s)
14:25:08   18000 tokens, 1793582 trades, 216990 posities (106s)
14:25:19   20000 tokens, 1978318 trades, 238351 posities (117s)
14:25:31   22000 tokens, 2206858 trades, 266427 posities (129s)
14:25:44   24000 tokens, 2413621 trades, 294447 posities (142s)
14:25:57   26000 tokens, 2642132 trades, 326400 posities (155s)
14:26:09   28000 tokens, 2833960 trades, 350487 posities (167s)
```

## IJking poolkoers (laatste 12 regels)
```
14:10:36 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
14:21:03 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
