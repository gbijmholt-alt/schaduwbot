# Schaduwbot status

- tijd: 2026-09-14 14:31:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 44 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.8G/38G | geheugen: 2618/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 115049, "tokens_in_memory": 5659, "msgs": 13776946, "trades": 3099774, "creates": 31777, "decode_fail": 260941, "rpc_calls": 93482, "rpc_errors": 7, "sol_usd": 101.90669793299357, "open_positions": 56, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 14:26:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:26:22,127 main INFO screen CATWAY pass=0 dev=65.65 ins=0.0 pro=11 1a=False 1b=False 2=False (78.3s)
Sep 14 14:27:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:09,994 main INFO screen PUMPERS pass=0 dev=0.0 ins=29.56 pro=71 1a=False 1b=False 2=True (78.6s)
Sep 14 14:27:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:10,408 main INFO screen COLD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (77.6s)
Sep 14 14:27:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:27:15,947 main INFO screen PUMPERS pass=0 dev=0.0 ins=15.84 pro=15 1a=False 1b=False 2=True (53.8s)
Sep 14 14:28:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:03,556 main INFO screen PUMPERS pass=0 dev=0.0 ins=31.63 pro=45 1a=False 1b=False 2=True (53.1s)
Sep 14 14:28:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:05,306 main INFO screen ROBIN pass=0 dev=0.0 ins=162.79 pro=1 1a=False 1b=False 2=True (55.3s)
Sep 14 14:28:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:28:14,467 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.63 pro=25 1a=False 1b=False 2=True (58.5s)
Sep 14 14:29:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:16,318 main INFO screen X pass=1 dev=0.0 ins=4.98 pro=56 1a=False 1b=False 2=False (71.0s)
Sep 14 14:29:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:17,201 main INFO screen TIGR pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (73.6s)
Sep 14 14:29:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:29:28,455 main INFO screen dd pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.0s)
Sep 14 14:30:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:15,731 main INFO screen TRADY pass=0 dev=0.0 ins=55.52 pro=39 1a=True 1b=False 2=True (59.4s)
Sep 14 14:30:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:23,061 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 14 14:30:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:30:34,107 main INFO screen CHILLSON pass=0 dev=0.0 ins=36.28 pro=41 1a=True 1b=True 2=True (65.7s)
Sep 14 14:31:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:15,191 main INFO screen HIKKO pass=0 dev=0.0 ins=79.1 pro=6 1a=False 1b=True 2=True (59.5s)
Sep 14 14:31:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:32,600 main INFO screen Rack pass=0 dev=0.0 ins=3.4 pro=23 1a=False 1b=False 2=False (58.5s)
Sep 14 14:31:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 14:31:37,590 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:14:31:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T14:31:36Z
```

## Analyses (laatste 25 regels)
```
active
14:26:35   32000 tokens, 3238536 trades, 398558 posities (193s)
14:26:46   34000 tokens, 3433257 trades, 422988 posities (204s)
14:26:59   36000 tokens, 3651216 trades, 449494 posities (217s)
14:27:11   38000 tokens, 3855373 trades, 477025 posities (229s)
14:27:22   40000 tokens, 4058288 trades, 500003 posities (240s)
14:27:32   42000 tokens, 4231179 trades, 518624 posities (250s)
14:27:44   44000 tokens, 4431591 trades, 543117 posities (262s)
14:27:55   46000 tokens, 4628449 trades, 569121 posities (273s)
14:28:08   48000 tokens, 4835951 trades, 592426 posities (286s)
14:28:21   50000 tokens, 5042483 trades, 617257 posities (299s)
14:28:34   52000 tokens, 5232943 trades, 639976 posities (312s)
14:28:45   54000 tokens, 5400820 trades, 656278 posities (323s)
14:28:58   56000 tokens, 5607778 trades, 682670 posities (336s)
14:29:10   58000 tokens, 5779171 trades, 702483 posities (348s)
14:29:25   60000 tokens, 5995263 trades, 731299 posities (363s)
14:29:38   62000 tokens, 6195128 trades, 760023 posities (376s)
14:29:52   64000 tokens, 6409063 trades, 789743 posities (390s)
14:30:05   66000 tokens, 6613290 trades, 815749 posities (403s)
14:30:18   68000 tokens, 6815336 trades, 844682 posities (416s)
14:30:32   70000 tokens, 7014350 trades, 880257 posities (430s)
14:30:42 posities: 898781 uit 7156509 trades (444s)
14:30:55 201106 wallets gerekend
14:30:56 geluk-toets
14:31:33 persistentie
14:31:36 kopieer-simulatie
```

## IJking poolkoers (laatste 12 regels)
```
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
14:26:24 ijk: +0 | verste bak n=1 -> nog 14 metingen binnen 5 minuten na de migratie te gaan
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
