# Schaduwbot status

- tijd: 2026-09-12 22:02:19 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 8 hours, 15 minutes
- bot-service: active
- code-versie: b458321
- schijf: 3.9G/38G | geheugen: 781/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 5312, "tokens_in_memory": 2125, "msgs": 610056, "trades": 178411, "creates": 2125, "decode_fail": 15117, "rpc_calls": 4451, "rpc_errors": 1, "sol_usd": 101.39904081524541, "open_positions": 55, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 19803 | 2651 | 15 | 2649 | 202 | 4672 | 13887 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 583 | 16% | 1.7% | +43.6% | -16.0% | -6.28% | 100% |
| dip35_V1_gescreend_fail | 4638 | 27% | 3.9% | +45.3% | -26.1% | -6.73% | 100% |
| dip35_V1_alle | 5837 | 26% | 4.1% | +44.5% | -25.5% | -6.99% | 100% |
| dip35_V2_gescreend_pass | 580 | 22% | 2.4% | +40.8% | -20.4% | -6.85% | 100% |
| dip35_V2_gescreend_fail | 4689 | 25% | 4.4% | +54.8% | -28.1% | -7.10% | 100% |
| dip35_V2_alle | 5791 | 25% | 4.7% | +52.3% | -27.9% | -7.93% | 100% |
| dip35_V3_gescreend_pass | 581 | 9% | 2.9% | +266.5% | -22.1% | +3.72% | 100% |
| dip35_V3_gescreend_fail | 4797 | 14% | 6.1% | +110.8% | -29.8% | -10.78% | 100% |
| dip35_V3_alle | 5847 | 13% | 6.2% | +113.7% | -29.5% | -10.53% | 100% |
| dip40_V1_gescreend_pass | 551 | 14% | 1.8% | +44.9% | -15.5% | -6.95% | 100% |
| dip40_V1_gescreend_fail | 4556 | 27% | 3.9% | +46.8% | -25.9% | -6.61% | 100% |
| dip40_V1_alle | 5605 | 26% | 4.0% | +46.6% | -25.3% | -6.95% | 100% |
| dip40_V2_gescreend_pass | 549 | 17% | 2.2% | +43.5% | -19.5% | -8.62% | 100% |
| dip40_V2_gescreend_fail | 4580 | 25% | 4.3% | +54.6% | -28.1% | -7.10% | 100% |
| dip40_V2_alle | 5553 | 24% | 4.5% | +53.0% | -27.7% | -8.11% | 100% |
| dip40_V3_gescreend_pass | 551 | 8% | 2.5% | +261.0% | -21.0% | +1.48% | 100% |
| dip40_V3_gescreend_fail | 4676 | 13% | 5.9% | +105.5% | -29.6% | -11.78% | 100% |
| dip40_V3_alle | 5610 | 13% | 5.9% | +108.9% | -29.2% | -11.52% | 100% |
| dip45_V1_gescreend_pass | 526 | 14% | 1.7% | +47.5% | -15.3% | -6.25% | 100% |
| dip45_V1_gescreend_fail | 4468 | 28% | 3.6% | +48.2% | -25.8% | -5.45% | 100% |
| dip45_V1_alle | 5419 | 26% | 3.6% | +48.2% | -25.1% | -5.94% | 100% |
| dip45_V2_gescreend_pass | 523 | 18% | 2.1% | +42.7% | -19.5% | -8.21% | 100% |
| dip45_V2_gescreend_fail | 4480 | 25% | 4.1% | +57.4% | -27.8% | -6.19% | 100% |
| dip45_V2_alle | 5367 | 24% | 4.2% | +56.1% | -27.4% | -7.05% | 100% |
| dip45_V3_gescreend_pass | 526 | 8% | 2.1% | +303.1% | -20.3% | +4.88% | 100% |
| dip45_V3_gescreend_fail | 4562 | 14% | 5.6% | +111.4% | -29.2% | -9.84% | 100% |
| dip45_V3_alle | 5414 | 13% | 5.5% | +117.2% | -28.7% | -9.53% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 456 | 15% | 5.0% | -9.28% | -12.0% tot -6.5% | -14.4% | – | 100% |
| per_token_zonder_xlink | 131 | 21% | 0.0% | +18.07% | -12.7% tot +48.8% | -13.2% | 130% | 54% |
| gepoold_met_xlink | 3845 | 13% | 2.8% | -9.84% | -11.1% tot -8.6% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1125 | 18% | 0.0% | +17.41% | +0.0% tot +34.8% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 21:25:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:45,653 main INFO screen Holder pass=0 dev=0.0 ins=50.54 pro=76 1a=False 1b=False 2=True (75.9s)
Sep 12 21:25:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:46,545 main INFO screen Bot pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (76.1s)
Sep 12 21:25:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:47,196 main INFO screen BURP pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.6s)
Sep 12 21:26:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:50,105 main INFO screen $CHILL pass=0 dev=0.06 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 12 21:26:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:50,384 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.2s)
Sep 12 21:26:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:53,575 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 12 21:28:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:09,599 main INFO screen USMS pass=0 dev=0.01 ins=0.0 pro=8 1a=False 1b=False 2=False (79.2s)
Sep 12 21:28:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:10,926 main INFO screen ZEC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (77.3s)
Sep 12 21:28:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:11,543 main INFO screen HOODLANA pass=0 dev=0.0 ins=39.65 pro=61 1a=False 1b=False 2=True (81.4s)
Sep 12 21:29:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:18,182 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.6s)
Sep 12 21:29:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:28,642 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.7s)
Sep 12 21:29:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:30,776 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (79.2s)
Sep 12 21:30:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:30,924 main INFO screen BS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (72.7s)
Sep 12 21:30:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:41,461 main INFO screen REVOLUT pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (72.8s)
Sep 12 21:30:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:49,313 main INFO screen PUPPY pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (78.5s)
Sep 12 21:31:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:31:21,348 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:31:21 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 12 21:31:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:31:26,970 main INFO screen OpenAI pass=0 dev=99.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.0s)
Sep 12 21:31:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:31:37,196 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 12 21:31:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:31:46,688 main INFO screen KaiCenat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 12 21:32:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:32:38,102 main INFO screen OCC pass=0 dev=0.7 ins=0.0 pro=71 1a=False 1b=False 2=True (71.1s)
Sep 12 21:32:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:32:45,509 main INFO screen ZTR pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.3s)
Sep 12 21:32:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:32:49,109 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 12 21:33:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:33:46,323 main INFO screen TCAT pass=0 dev=0.0 ins=73.09 pro=10 1a=False 1b=False 2=True (68.2s)
Sep 12 21:33:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:33:48,907 main INFO screen BOBCAT pass=0 dev=52.41 ins=0.0 pro=6 1a=False 1b=False 2=False (63.4s)
Sep 12 21:34:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:34:36,144 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (107.0s)
Sep 12 21:35:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:35:18,931 main INFO screen GLONK pass=0 dev=0.0 ins=50.17 pro=50 1a=False 1b=False 2=True (92.6s)
Sep 12 21:35:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:35:24,369 main INFO screen $SONY pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.9s)
Sep 12 21:35:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:35:26,400 main INFO screen PUMP pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (50.3s)
Sep 12 21:36:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:36:25,665 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:36:25 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 21:36:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:36:26,385 main INFO screen USMS pass=0 dev=7.61 ins=0.0 pro=12 1a=False 1b=False 2=False (67.5s)
Sep 12 21:36:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:36:26,575 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 12 21:36:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:36:28,613 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.2s)
Sep 12 21:37:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:37:33,930 main INFO screen CURWIZ pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (67.5s)
Sep 12 21:37:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:37:35,851 main INFO screen Familia  pass=1 dev=0.42 ins=0.0 pro=15 1a=False 1b=False 2=False (69.3s)
Sep 12 21:38:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:38:11,593 main INFO screen HOODCAT pass=0 dev=0.0 ins=32.99 pro=17 1a=False 1b=False 2=True (69.8s)
Sep 12 21:39:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:39:04,828 main INFO screen elontrump pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (65.7s)
Sep 12 21:39:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:39:06,260 main INFO screen watch pass=0 dev=6.64 ins=0.0 pro=3 1a=False 1b=False 2=False (65.5s)
Sep 12 21:39:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:39:17,804 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.0s)
Sep 12 21:39:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:39:51,064 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.2s)
Sep 12 21:41:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:41:21,091 main INFO screen sigma pass=1 dev=0.0 ins=0.0 pro=62 1a=False 1b=False 2=False (64.4s)
Sep 12 21:41:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:41:27,818 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:41:27 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 21:41:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:41:49,217 main INFO screen monkdog pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (56.9s)
Sep 12 21:42:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:42:08,738 main INFO screen SCAT pass=0 dev=0.0 ins=42.98 pro=80 1a=False 1b=False 2=True (63.5s)
Sep 12 21:42:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:42:15,652 main INFO screen FLUFFY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.6s)
Sep 12 21:42:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:42:58,893 main INFO screen Therry pass=1 dev=0.0 ins=0.03 pro=59 1a=False 1b=False 2=False (65.9s)
Sep 12 21:43:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:43:33,532 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 12 21:44:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:44:10,232 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.0s)
Sep 12 21:45:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:45:21,912 main INFO screen TWINECAT pass=0 dev=0.0 ins=55.51 pro=59 1a=False 1b=False 2=True (52.9s)
Sep 12 21:46:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:46:36,633 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:46:36 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 21:49:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:49:19,334 main INFO screen PAPERBAG pass=0 dev=0.0 ins=18.99 pro=54 1a=False 1b=False 2=True (50.2s)
Sep 12 21:50:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:50:21,780 main INFO screen DOOB pass=0 dev=5.2 ins=0.0 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 12 21:51:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:51:28,383 main INFO screen Holdoor pass=0 dev=0.0 ins=37.5 pro=61 1a=False 1b=False 2=True (62.4s)
Sep 12 21:51:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:51:37,123 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:51:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 21:52:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:52:06,557 main INFO screen CPCR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.5s)
Sep 12 21:53:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:53:20,134 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.9s)
Sep 12 21:54:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:54:09,879 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 12 21:54:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:54:21,493 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (66.8s)
Sep 12 21:54:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:54:23,330 main INFO screen aw pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (60.4s)
Sep 12 21:55:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:55:04,628 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.7s)
Sep 12 21:55:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:55:34,151 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (70.8s)
Sep 12 21:55:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:55:36,124 main INFO screen SCAT pass=0 dev=0.0 ins=24.27 pro=59 1a=False 1b=False 2=True (74.6s)
Sep 12 21:56:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:56:05,007 main INFO screen UNDERDOG pass=0 dev=0.0 ins=32.79 pro=17 1a=False 1b=False 2=True (60.4s)
Sep 12 21:56:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:56:42,422 main INFO screen SCAT pass=0 dev=0.0 ins=12.62 pro=23 1a=False 1b=False 2=True (68.3s)
Sep 12 21:56:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:56:42,467 main INFO screen Underdog pass=1 dev=0.0 ins=19.41 pro=76 1a=False 1b=False 2=False (66.3s)
Sep 12 21:57:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:57:02,952 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:57:02 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 21:57:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:57:16,021 main INFO screen UNDERDOG pass=0 dev=0.0 ins=9.16 pro=77 1a=False 1b=False 2=True (71.0s)
Sep 12 21:57:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:57:51,251 main INFO screen Pretend pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (68.8s)
Sep 12 21:57:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:57:52,702 main INFO screen BUMP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (70.3s)
Sep 12 21:58:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:58:05,805 main INFO screen $REGRET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (49.8s)
Sep 12 21:58:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:58:57,147 main INFO screen PP pass=1 dev=2.59 ins=1.8 pro=53 1a=False 1b=False 2=False (65.9s)
Sep 12 21:59:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:59:03,324 main INFO screen $ARTDOG pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (70.6s)
Sep 12 21:59:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:59:14,144 main INFO screen MONTY pass=0 dev=0.0 ins=15.69 pro=58 1a=False 1b=False 2=True (68.3s)
Sep 12 21:59:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:59:52,010 main INFO screen TOLY pass=0 dev=0.0 ins=32.68 pro=37 1a=False 1b=False 2=True (54.9s)
Sep 12 22:00:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:00:12,412 main INFO screen DOOYET pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (69.1s)
Sep 12 22:00:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:00:18,368 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.2s)
Sep 12 22:01:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:01:05,361 main INFO screen RISE pass=0 dev=41.51 ins=0.0 pro=7 1a=False 1b=False 2=False (73.4s)
Sep 12 22:01:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:01:13,729 main INFO screen $Probe pass=0 dev=0.29 ins=0.0 pro=9 1a=False 1b=False 2=False (61.3s)
Sep 12 22:01:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:01:17,947 main INFO screen SolChan pass=0 dev=0.0 ins=23.24 pro=61 1a=False 1b=False 2=True (59.6s)
Sep 12 22:02:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:02:18,566 main INFO screen VSNTC pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (64.8s)
Sep 12 22:02:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:02:19,858 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:02:19 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
install klaar
--- update 2026-09-12T20:38:58Z
--- update 2026-09-12T20:44:07Z
--- update 2026-09-12T20:49:15Z
--- update 2026-09-12T20:54:28Z
--- update 2026-09-12T20:59:33Z
--- update 2026-09-12T21:04:36Z
--- update 2026-09-12T21:10:10Z
--- update 2026-09-12T21:15:15Z
--- update 2026-09-12T21:20:14Z
--- update 2026-09-12T21:25:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: ad453f090a6d431a85bbf496eb255234
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T21:31:20Z
--- update 2026-09-12T21:36:24Z
--- update 2026-09-12T21:41:26Z
--- update 2026-09-12T21:46:35Z
--- update 2026-09-12T21:51:36Z
--- update 2026-09-12T21:57:01Z
--- update 2026-09-12T22:02:18Z
```

## Analyses (laatste 25 regels)
```
inactive
21:35:00   4000 tokens, 469629 trades, 83678 posities (4s)
21:35:03   6000 tokens, 686889 trades, 124260 posities (6s)
21:35:05   8000 tokens, 915934 trades, 161908 posities (8s)
21:35:07   10000 tokens, 1134225 trades, 200519 posities (10s)
21:35:09   12000 tokens, 1348165 trades, 236816 posities (12s)
21:35:11   14000 tokens, 1606497 trades, 285128 posities (14s)
21:35:13   16000 tokens, 1845445 trades, 332302 posities (16s)
21:35:15   18000 tokens, 2069349 trades, 368627 posities (18s)
21:35:17   20000 tokens, 2302073 trades, 408799 posities (20s)
21:35:19   22000 tokens, 2532730 trades, 450683 posities (22s)
21:35:20   24000 tokens, 2749646 trades, 487179 posities (24s)
21:35:23   26000 tokens, 3007294 trades, 538811 posities (26s)
21:35:25   28000 tokens, 3243852 trades, 580513 posities (28s)
21:35:27   30000 tokens, 3459040 trades, 615508 posities (30s)
21:35:29   32000 tokens, 3690377 trades, 657198 posities (32s)
21:35:30   34000 tokens, 3910303 trades, 696922 posities (34s)
21:35:33   36000 tokens, 4150741 trades, 742994 posities (36s)
21:35:35   38000 tokens, 4391159 trades, 788453 posities (38s)
21:35:36   40000 tokens, 4609485 trades, 839321 posities (40s)
21:35:37 posities: 846701 uit 4636829 trades (40s)
21:35:48 177416 wallets gerekend
21:35:48 geluk-toets
21:36:20 persistentie
21:36:22 kopieer-simulatie
21:36:33 klaar in 96s -> /opt/schaduwbot/reports/wallets.md
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
