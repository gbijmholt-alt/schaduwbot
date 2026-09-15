# Schaduwbot status

- tijd: 2026-09-15 15:02:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 1 hour, 15 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.3G/38G | geheugen: 2241/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 203309, "tokens_in_memory": 7179, "msgs": 29315081, "trades": 6168984, "creates": 65565, "decode_fail": 518477, "rpc_calls": 181497, "rpc_errors": 15, "sol_usd": 98.5712780057152, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 14:37:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:37:09,517 main INFO screen NOOB pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (78.5s)
Sep 15 14:37:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:37:23,570 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:37:23 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 15 14:37:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:37:38,135 main INFO screen FGTV pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.3s)
Sep 15 14:37:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:37:43,952 main INFO screen Catcash pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.0s)
Sep 15 14:38:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:38:18,178 main INFO screen rug pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.7s)
Sep 15 14:38:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:38:59,265 main INFO screen maneki pass=0 dev=0.0 ins=51.47 pro=11 1a=False 1b=False 2=True (81.1s)
Sep 15 14:39:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:39:00,823 main INFO screen Jackcat pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (76.9s)
Sep 15 14:39:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:39:25,193 main INFO screen Milo pass=0 dev=0.0 ins=24.74 pro=8 1a=False 1b=False 2=True (67.0s)
Sep 15 14:40:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:40:13,358 main INFO screen pork pass=0 dev=0.07 ins=0.0 pro=58 1a=False 1b=False 2=True (74.1s)
Sep 15 14:40:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:40:18,967 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (78.1s)
Sep 15 14:40:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:40:31,090 main INFO screen Puglas pass=0 dev=0.0 ins=18.05 pro=33 1a=False 1b=False 2=True (65.9s)
Sep 15 14:41:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:41:06,768 main INFO screen TOTH pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (53.4s)
Sep 15 14:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:41:30,593 main INFO screen FROG pass=0 dev=0.0 ins=29.37 pro=63 1a=False 1b=False 2=True (71.6s)
Sep 15 14:41:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:41:33,994 main INFO screen CHAROC pass=0 dev=4.97 ins=0.0 pro=8 1a=False 1b=False 2=False (62.9s)
Sep 15 14:42:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:42:14,098 main INFO screen LIDL pass=0 dev=0.0 ins=8.37 pro=56 1a=False 1b=False 2=False (67.3s)
Sep 15 14:42:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:42:20,467 main INFO screen OpenAI pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (49.9s)
Sep 15 14:42:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:42:24,583 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:42:24 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 14:42:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:42:37,147 main INFO screen KIMCHI pass=0 dev=0.0 ins=0.29 pro=29 1a=False 1b=False 2=False (63.2s)
Sep 15 14:43:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:43:07,239 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.1s)
Sep 15 14:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:43:11,159 main INFO screen BALD pass=0 dev=0.0 ins=53.95 pro=9 1a=False 1b=False 2=True (50.7s)
Sep 15 14:43:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:43:40,850 main INFO screen fomofamily pass=0 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=True (63.7s)
Sep 15 14:44:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:44:16,807 main INFO screen JackCat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.6s)
Sep 15 14:44:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:44:17,781 main INFO screen BLANK pass=0 dev=0.0 ins=78.55 pro=2 1a=False 1b=True 2=True (66.6s)
Sep 15 14:44:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:44:38,605 main INFO screen Wheelis pass=0 dev=0.0 ins=7.44 pro=43 1a=False 1b=False 2=False (57.8s)
Sep 15 14:45:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:45:20,731 main INFO screen QUOK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.9s)
Sep 15 14:45:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:45:21,129 main INFO screen MIKE pass=0 dev=0.0 ins=17.98 pro=60 1a=False 1b=False 2=False (63.3s)
Sep 15 14:45:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:45:42,571 main INFO screen WhiteBull pass=0 dev=0.0 ins=53.95 pro=24 1a=True 1b=False 2=True (64.0s)
Sep 15 14:46:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:46:26,125 main INFO screen HLDM pass=0 dev=0.0 ins=96.41 pro=0 1a=False 1b=False 2=True (65.0s)
Sep 15 14:46:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:46:27,675 main INFO screen Millie pass=0 dev=0.0 ins=17.4 pro=26 1a=False 1b=False 2=False (66.9s)
Sep 15 14:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:46:35,141 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (52.6s)
Sep 15 14:47:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:47:16,016 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.9s)
Sep 15 14:47:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:47:17,902 main INFO screen CARTIER pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (50.2s)
Sep 15 14:47:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:47:25,755 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:47:25 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 14:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:47:27,426 main INFO screen JACKET pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (52.3s)
Sep 15 14:48:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:48:21,905 main INFO screen MCCONNELL pass=0 dev=0.0 ins=47.99 pro=63 1a=False 1b=False 2=True (65.9s)
Sep 15 14:48:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:48:25,219 main INFO screen /QQQ pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.3s)
Sep 15 14:48:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:48:29,686 main INFO screen DonTrunk pass=0 dev=0.0 ins=74.7 pro=28 1a=False 1b=False 2=True (62.3s)
Sep 15 14:49:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:49:12,416 aiohttp.access INFO 172.235.40.131 [15/Sep/2026:14:49:12 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 15 14:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:49:33,572 main INFO screen lab pass=0 dev=0.0 ins=16.0 pro=66 1a=False 1b=False 2=True (68.4s)
Sep 15 14:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:49:33,624 main INFO screen BUFFER pass=0 dev=32.23 ins=3.81 pro=50 1a=False 1b=False 2=False (71.7s)
Sep 15 14:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:49:35,811 main INFO screen stickman pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.1s)
Sep 15 14:50:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:50:42,579 main INFO screen BOT pass=0 dev=0.0 ins=25.49 pro=2 1a=False 1b=False 2=True (69.0s)
Sep 15 14:50:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:50:47,284 main INFO screen Lingo pass=0 dev=0.0 ins=19.51 pro=3 1a=False 1b=False 2=True (71.5s)
Sep 15 14:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:50:48,326 main INFO screen Mower pass=0 dev=0.31 ins=0.0 pro=65 1a=False 1b=False 2=False (74.8s)
Sep 15 14:51:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:51:33,540 main INFO screen $FIVE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.0s)
Sep 15 14:51:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:51:50,085 main INFO screen WOFI pass=0 dev=1.18 ins=125.28 pro=1 1a=False 1b=False 2=True (61.8s)
Sep 15 14:51:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:51:51,157 main INFO screen Cruelty pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (63.9s)
Sep 15 14:52:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:52:26,848 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:52:26 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 14:52:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:52:46,415 main INFO screen Aphrodite pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (72.9s)
Sep 15 14:53:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:53:03,054 main INFO screen Dangalabba pass=0 dev=0.0 ins=28.33 pro=66 1a=False 1b=False 2=True (73.0s)
Sep 15 14:53:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:53:04,520 main INFO screen Crashcat pass=0 dev=0.0 ins=43.73 pro=71 1a=False 1b=False 2=True (73.4s)
Sep 15 14:53:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:53:46,182 main INFO screen /QQQ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.8s)
Sep 15 14:53:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:53:57,186 main INFO screen birk pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (52.7s)
Sep 15 14:53:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:53:58,362 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.3s)
Sep 15 14:54:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:54:39,896 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (53.7s)
Sep 15 14:55:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:55:08,954 main INFO screen Foreskin pass=0 dev=0.0 ins=11.2 pro=45 1a=False 1b=False 2=False (71.8s)
Sep 15 14:55:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:55:09,151 main INFO screen SpaceX pass=0 dev=0.0 ins=142.52 pro=0 1a=False 1b=False 2=True (70.8s)
Sep 15 14:55:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:55:53,338 main INFO screen Gosling pass=0 dev=0.0 ins=7.42 pro=63 1a=False 1b=False 2=False (73.4s)
Sep 15 14:56:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:56:08,609 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.7s)
Sep 15 14:56:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:56:10,120 main INFO screen MNGY pass=0 dev=0.0 ins=27.53 pro=37 1a=False 1b=False 2=True (61.0s)
Sep 15 14:56:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:56:51,665 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 15 14:57:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:57:20,627 main INFO screen MNGY pass=0 dev=0.0 ins=21.73 pro=3 1a=False 1b=False 2=False (72.0s)
Sep 15 14:57:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:57:21,076 main INFO screen MNGY pass=0 dev=0.0 ins=13.71 pro=70 1a=False 1b=False 2=True (71.0s)
Sep 15 14:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:57:27,127 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:14:57:27 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 14:57:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:57:53,647 main INFO screen IVCN pass=0 dev=0.0 ins=0.88 pro=14 1a=False 1b=False 2=False (62.0s)
Sep 15 14:58:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:58:17,800 main INFO screen XPXGOLD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 15 14:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:58:18,214 main INFO screen HLDM pass=0 dev=0.79 ins=0.0 pro=1 1a=False 1b=False 2=True (57.6s)
Sep 15 14:58:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:58:35,437 aiohttp.access INFO 2.27.248.13 [15/Sep/2026:14:58:35 +0000] "GET /login HTTP/1.1" 404 193 "-" "Go-http-client/1.1"
Sep 15 14:58:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:58:59,460 main INFO screen $LARDO pass=0 dev=1.69 ins=0.0 pro=4 1a=False 1b=False 2=False (65.8s)
Sep 15 14:59:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:59:21,597 main INFO screen MNGY pass=0 dev=0.0 ins=21.55 pro=3 1a=False 1b=False 2=True (63.8s)
Sep 15 14:59:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:59:22,090 main INFO screen SALOLO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.9s)
Sep 15 14:59:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 14:59:52,781 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.3s)
Sep 15 15:00:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:00:17,148 main INFO screen TikTok pass=0 dev=0.0 ins=159.21 pro=0 1a=False 1b=False 2=True (55.5s)
Sep 15 15:00:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:00:33,308 main INFO screen QUMIS pass=0 dev=0.0 ins=12.37 pro=71 1a=False 1b=False 2=False (71.2s)
Sep 15 15:00:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:00:51,609 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.8s)
Sep 15 15:01:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:01:25,128 main INFO screen BTRC pass=0 dev=0.0 ins=0.0 pro=77 1a=False 1b=False 2=False (51.8s)
Sep 15 15:01:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:01:27,340 main INFO screen Quack pass=0 dev=0.0 ins=0.0 pro=52 1a=False 1b=False 2=False (70.2s)
Sep 15 15:02:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:02:06,626 main INFO screen BFC pass=0 dev=0.0 ins=20.34 pro=6 1a=False 1b=False 2=False (75.0s)
Sep 15 15:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:02:36,106 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (68.8s)
Sep 15 15:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:02:37,313 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:02:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T13:46:53Z
--- update 2026-09-15T13:51:54Z
--- update 2026-09-15T13:56:56Z
--- update 2026-09-15T14:02:15Z
Running as unit: schaduwbot-wallets.service; invocation ID: 39762daa96b14ed5a0e2954268444ef8
analyses gestart (0f687558a2d6)
--- update 2026-09-15T14:07:15Z
--- update 2026-09-15T14:12:16Z
--- update 2026-09-15T14:17:16Z
--- update 2026-09-15T14:22:18Z
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
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
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
