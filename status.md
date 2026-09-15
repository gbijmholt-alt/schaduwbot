# Schaduwbot status

- tijd: 2026-09-15 03:18:47 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 13 hours, 31 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.7G/38G | geheugen: 2240/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 161079, "tokens_in_memory": 8774, "msgs": 24630743, "trades": 4913162, "creates": 52496, "decode_fail": 421589, "rpc_calls": 139172, "rpc_errors": 13, "sol_usd": 101.29304113252404, "open_positions": 35, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 02:53:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:53:21,692 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:53:21 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:53:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:53:26,987 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.7s)
Sep 15 02:53:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:53:28,004 main INFO screen Optimus  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.1s)
Sep 15 02:54:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:54:27,950 main INFO screen Bulljak pass=0 dev=0.0 ins=57.48 pro=35 1a=False 1b=False 2=True (71.4s)
Sep 15 02:54:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:54:36,007 main INFO screen Deg pass=0 dev=0.0 ins=34.16 pro=64 1a=False 1b=False 2=True (69.0s)
Sep 15 02:54:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:54:39,940 main INFO screen ZSDC pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (71.9s)
Sep 15 02:55:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:55:27,735 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (51.7s)
Sep 15 02:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:55:38,349 main INFO screen sween pass=0 dev=3.25 ins=9.2 pro=52 1a=False 1b=False 2=False (70.4s)
Sep 15 02:55:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:55:42,354 main INFO screen &WASHED pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.4s)
Sep 15 02:56:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:56:41,224 main INFO screen Dam pass=0 dev=0.0 ins=3.63 pro=63 1a=False 1b=False 2=False (73.5s)
Sep 15 02:56:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:56:45,262 main INFO screen Poo pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.9s)
Sep 15 02:56:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:56:49,439 main INFO screen SWIENER pass=0 dev=0.0 ins=22.51 pro=47 1a=False 1b=False 2=True (67.1s)
Sep 15 02:57:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:57:40,164 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.9s)
Sep 15 02:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:57:41,085 main INFO screen MEME pass=0 dev=0.0 ins=80.28 pro=10 1a=True 1b=False 2=True (55.8s)
Sep 15 02:57:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:57:52,919 main INFO screen threedolla pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 15 02:58:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:58:22,233 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:02:58:22 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 02:58:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:58:26,588 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:02:58:26 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 02:58:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:58:42,364 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.2s)
Sep 15 02:58:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:58:43,211 main INFO screen Apple pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 15 02:58:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:58:53,176 main INFO screen BBYGANG$TR pass=0 dev=0.21 ins=0.0 pro=18 1a=False 1b=False 2=False (60.3s)
Sep 15 02:59:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:59:42,314 main INFO screen TRUMGPT pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (59.9s)
Sep 15 02:59:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 02:59:55,226 main INFO screen DD pass=0 dev=0.0 ins=24.97 pro=19 1a=False 1b=False 2=True (72.0s)
Sep 15 03:00:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:00:00,154 main INFO screen cappykidd pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.0s)
Sep 15 03:00:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:00:45,187 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.9s)
Sep 15 03:00:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:00:59,537 main INFO screen MEME pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (59.4s)
Sep 15 03:01:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:01:04,338 main INFO screen KANYEVEST pass=0 dev=0.0 ins=35.65 pro=56 1a=False 1b=False 2=True (69.1s)
Sep 15 03:01:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:01:59,932 main INFO screen MOCHI pass=0 dev=0.0 ins=45.92 pro=9 1a=False 1b=False 2=True (74.7s)
Sep 15 03:02:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:02:05,103 main INFO screen RIP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (65.6s)
Sep 15 03:02:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:02:09,654 main INFO screen SABLE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.3s)
Sep 15 03:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:02:51,924 main INFO screen ROI pass=0 dev=0.0 ins=21.47 pro=54 1a=False 1b=False 2=True (52.0s)
Sep 15 03:03:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:01,506 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (56.4s)
Sep 15 03:03:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:04,573 main INFO screen WOFI pass=0 dev=0.5 ins=270.56 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 15 03:03:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:24,583 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:03:24 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:03:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:48,888 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.0s)
Sep 15 03:03:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:58,279 main INFO screen Fluffy pass=0 dev=0.0 ins=8.62 pro=45 1a=False 1b=False 2=True (53.7s)
Sep 15 03:03:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:03:59,996 main INFO screen Moonsling pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 15 03:04:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:04:39,486 main INFO screen michi pass=0 dev=0.0 ins=18.37 pro=21 1a=False 1b=False 2=True (50.6s)
Sep 15 03:04:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:04:48,552 main INFO screen アルー pass=0 dev=0.0 ins=15.16 pro=55 1a=False 1b=False 2=True (48.6s)
Sep 15 03:04:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:04:57,741 main INFO screen STOC pass=0 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (59.5s)
Sep 15 03:05:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:05:44,974 main INFO screen PENNY pass=0 dev=0.0 ins=28.1 pro=57 1a=False 1b=False 2=True (65.5s)
Sep 15 03:05:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:05:58,932 main INFO screen $NPC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.4s)
Sep 15 03:06:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:06:04,663 main INFO screen Mia pass=0 dev=0.0 ins=1.18 pro=59 1a=False 1b=False 2=False (66.9s)
Sep 15 03:06:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:06:43,251 main INFO screen nshi pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 15 03:06:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:06:49,324 main INFO screen Voxa pass=0 dev=0.0 ins=21.55 pro=32 1a=False 1b=False 2=True (50.4s)
Sep 15 03:07:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:07:03,675 main INFO screen vodka pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (59.0s)
Sep 15 03:07:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:07:44,700 main INFO screen NOMONEY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.4s)
Sep 15 03:07:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:07:59,630 main INFO screen TRAVISSLOT pass=0 dev=0.0 ins=37.44 pro=32 1a=False 1b=False 2=False (70.3s)
Sep 15 03:08:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:08:10,911 main INFO screen SPOUT pass=0 dev=0.0 ins=5.36 pro=60 1a=False 1b=False 2=False (67.2s)
Sep 15 03:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:08:37,181 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:08:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 03:08:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:08:38,129 main INFO screen 404 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 15 03:08:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:08:56,665 main INFO screen EGENCY pass=0 dev=0.0 ins=33.08 pro=23 1a=True 1b=False 2=True (57.0s)
Sep 15 03:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:09:17,497 main INFO screen BRAIN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.6s)
Sep 15 03:09:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:09:31,093 main INFO screen MDOR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 15 03:10:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:10:05,164 main INFO screen 國語助理 pass=0 dev=0.0 ins=1.57 pro=71 1a=False 1b=False 2=False (68.5s)
Sep 15 03:10:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:10:12,285 main INFO screen pUSD pass=0 dev=0.0 ins=17.67 pro=48 1a=False 1b=False 2=True (54.8s)
Sep 15 03:10:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:10:31,511 main INFO screen hamilton pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.4s)
Sep 15 03:11:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:11:03,277 main INFO screen WIFGPT pass=0 dev=0.0 ins=78.77 pro=2 1a=False 1b=True 2=True (58.1s)
Sep 15 03:11:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:11:06,157 main INFO screen fomo pass=0 dev=0.0 ins=154.48 pro=0 1a=False 1b=False 2=True (53.9s)
Sep 15 03:11:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:11:39,837 main INFO screen HUHCAT pass=0 dev=0.0 ins=25.6 pro=69 1a=False 1b=False 2=True (68.3s)
Sep 15 03:12:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:12:19,554 main INFO screen DOOYET pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (76.3s)
Sep 15 03:12:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:12:21,187 main INFO screen DAH pass=0 dev=0.0 ins=18.32 pro=39 1a=False 1b=False 2=True (75.0s)
Sep 15 03:12:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:12:40,918 main INFO screen MSTR pass=0 dev=0.0 ins=50.42 pro=26 1a=True 1b=False 2=True (61.1s)
Sep 15 03:13:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:13:16,008 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.5s)
Sep 15 03:13:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:13:19,008 main INFO screen FucK YoU pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (57.8s)
Sep 15 03:13:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:13:44,585 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:13:44 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 03:13:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:13:51,349 main INFO screen bedsheeran pass=0 dev=0.53 ins=0.0 pro=54 1a=False 1b=False 2=False (70.4s)
Sep 15 03:14:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:14:08,600 aiohttp.access INFO 103.203.59.16 [15/Sep/2026:03:14:08 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 15 03:14:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:14:26,015 main INFO screen AssSlap pass=0 dev=0.0 ins=19.31 pro=56 1a=False 1b=True 2=True (70.0s)
Sep 15 03:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:14:27,064 main INFO screen $SIRUS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.1s)
Sep 15 03:15:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:15:01,197 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (69.8s)
Sep 15 03:15:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:15:40,499 main INFO screen Jimothée pass=0 dev=0.0 ins=4.71 pro=43 1a=False 1b=False 2=False (74.5s)
Sep 15 03:15:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:15:40,773 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (73.7s)
Sep 15 03:16:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:16:00,101 main INFO screen Bulljak pass=0 dev=0.0 ins=55.44 pro=15 1a=False 1b=False 2=True (58.9s)
Sep 15 03:16:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:16:46,837 main INFO screen DANGR pass=0 dev=56.09 ins=189.67 pro=1 1a=False 1b=False 2=True (66.3s)
Sep 15 03:16:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:16:58,315 main INFO screen TIMCURRY pass=0 dev=0.0 ins=0.35 pro=55 1a=False 1b=False 2=False (77.5s)
Sep 15 03:17:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:17:05,933 main INFO screen toely pass=0 dev=0.0 ins=33.97 pro=34 1a=False 1b=False 2=True (65.8s)
Sep 15 03:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:18:00,235 main INFO screen SINK pass=0 dev=0.0 ins=48.77 pro=74 1a=False 1b=False 2=True (73.4s)
Sep 15 03:18:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:18:17,911 main INFO screen GG pass=0 dev=0.0 ins=17.62 pro=25 1a=False 1b=False 2=True (72.0s)
Sep 15 03:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:18:19,353 main INFO screen BPCATE pass=0 dev=0.06 ins=0.0 pro=3 1a=False 1b=False 2=True (81.0s)
Sep 15 03:18:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 03:18:47,217 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:03:18:47 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T01:51:16Z
Running as unit: schaduwbot-wallets.service; invocation ID: 198697cd6df2473cb461b6a874faa3b9
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T01:56:31Z
--- update 2026-09-15T02:01:36Z
--- update 2026-09-15T02:06:42Z
--- update 2026-09-15T02:11:49Z
--- update 2026-09-15T02:17:06Z
--- update 2026-09-15T02:22:06Z
--- update 2026-09-15T02:27:10Z
--- update 2026-09-15T02:32:12Z
--- update 2026-09-15T02:37:36Z
--- update 2026-09-15T02:42:48Z
--- update 2026-09-15T02:48:18Z
--- update 2026-09-15T02:53:20Z
--- update 2026-09-15T02:58:21Z
--- update 2026-09-15T03:03:23Z
--- update 2026-09-15T03:08:36Z
--- update 2026-09-15T03:13:43Z
--- update 2026-09-15T03:18:46Z
```

## Analyses (laatste 25 regels)
```
inactive
02:35:45   38000 tokens, 3672841 trades, 438922 posities (261s)
02:35:59   40000 tokens, 3868151 trades, 465286 posities (275s)
02:36:13   42000 tokens, 4050923 trades, 484626 posities (289s)
02:36:26   44000 tokens, 4229969 trades, 507070 posities (302s)
02:36:40   46000 tokens, 4404490 trades, 527503 posities (316s)
02:36:54   48000 tokens, 4583089 trades, 547292 posities (330s)
02:37:09   50000 tokens, 4783817 trades, 571729 posities (345s)
02:37:24   52000 tokens, 4998695 trades, 600377 posities (361s)
02:37:39   54000 tokens, 5185471 trades, 621613 posities (375s)
02:37:55   56000 tokens, 5369938 trades, 647871 posities (391s)
02:38:09   58000 tokens, 5548035 trades, 669634 posities (406s)
02:38:24   60000 tokens, 5729093 trades, 691244 posities (420s)
02:38:39   62000 tokens, 5928987 trades, 715455 posities (436s)
02:38:55   64000 tokens, 6127099 trades, 744134 posities (451s)
02:39:11   66000 tokens, 6324136 trades, 768998 posities (467s)
02:39:27   68000 tokens, 6521044 trades, 794258 posities (483s)
02:39:43   70000 tokens, 6709770 trades, 817423 posities (499s)
02:39:58   72000 tokens, 6901181 trades, 840177 posities (514s)
02:40:16   74000 tokens, 7111581 trades, 876955 posities (532s)
02:40:26 posities: 888948 uit 7226958 trades (548s)
02:40:38 209899 wallets gerekend
02:40:39 geluk-toets
02:41:13 persistentie
02:41:16 kopieer-simulatie
02:43:47 klaar in 749s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
02:48:38 ijk: +6 van 10 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=95 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
02:48:39 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 10/38/154 | al gemeten: 410
02:53:27 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=96 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
02:53:27 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 9/36/154 | al gemeten: 413
02:58:21 ijk: +0 van 0 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=96 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
02:58:22 ijk-diagnose: nieuwste migratie 5.9 min oud | migraties 15/60/240 min: 6/32/149 | al gemeten: 413
03:03:38 ijk: +5 van 5 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 2}) | verste bak n=100 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:03:38 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 7/34/152 | al gemeten: 418
03:08:51 ijk: +5 van 5 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=105 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:08:51 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 10/34/154 | al gemeten: 423
03:13:56 ijk: +4 van 4 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=109 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
03:13:56 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 13/36/157 | al gemeten: 427
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
