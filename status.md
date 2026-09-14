# Schaduwbot status

- tijd: 2026-09-14 12:26:19 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 22 hours, 39 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.7G/38G | geheugen: 2222/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 107531, "tokens_in_memory": 4757, "msgs": 12691361, "trades": 2844794, "creates": 29468, "decode_fail": 235224, "rpc_calls": 85868, "rpc_errors": 7, "sol_usd": 101.68189020140828, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 12:05:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:05:24,800 main INFO screen USMS pass=0 dev=0.26 ins=0.0 pro=5 1a=False 1b=False 2=False (73.0s)
Sep 14 12:05:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:05:37,989 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 14 12:05:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:05:47,656 main INFO screen Wholesome pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.6s)
Sep 14 12:06:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:06:22,593 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.8s)
Sep 14 12:06:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:06:34,355 main INFO screen kk pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 14 12:06:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:06:54,837 main INFO screen $RZILLA pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (67.2s)
Sep 14 12:08:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:08:09,884 main INFO screen LMAO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (66.7s)
Sep 14 12:08:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:08:18,633 main INFO screen BBC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 14 12:08:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:08:45,480 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 14 12:09:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:09:46,276 main INFO screen DRUG pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.3s)
Sep 14 12:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:09:58,568 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.8s)
Sep 14 12:09:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:09:59,601 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:09:59 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 12:10:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:10:20,085 main INFO screen Pumpers pass=1 dev=0.0 ins=13.5 pro=48 1a=False 1b=False 2=False (75.0s)
Sep 14 12:10:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:10:41,709 main INFO screen Google pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.4s)
Sep 14 12:11:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:11:13,522 main INFO screen ZEC pass=1 dev=0.0 ins=0.76 pro=55 1a=False 1b=False 2=False (75.0s)
Sep 14 12:11:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:11:36,560 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=4 1a=False 1b=False 2=False (76.5s)
Sep 14 12:11:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:11:47,529 main INFO screen WHS pass=0 dev=0.19 ins=79.12 pro=11 1a=False 1b=True 2=True (65.8s)
Sep 14 12:12:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:12:17,970 main INFO screen Cappy pass=0 dev=0.0 ins=24.11 pro=48 1a=False 1b=False 2=True (64.4s)
Sep 14 12:12:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:12:51,200 main INFO screen Koshimizu pass=1 dev=0.1 ins=12.76 pro=46 1a=False 1b=False 2=False (74.6s)
Sep 14 12:13:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:13:02,475 main INFO screen TRNCHR pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (74.9s)
Sep 14 12:13:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:13:19,160 main INFO screen Evader pass=0 dev=0.0 ins=25.91 pro=44 1a=False 1b=False 2=True (61.2s)
Sep 14 12:14:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:14:02,273 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.8s)
Sep 14 12:14:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:14:03,404 main INFO screen 🤝 pass=0 dev=0.34 ins=0.0 pro=6 1a=False 1b=False 2=False (72.2s)
Sep 14 12:14:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:14:19,063 main INFO screen Moonhouse pass=0 dev=0.0 ins=23.31 pro=27 1a=False 1b=False 2=True (59.9s)
Sep 14 12:15:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:15:18,652 main INFO screen mm pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (65.7s)
Sep 14 12:15:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:15:26,395 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:15:26 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 12:15:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:15:30,439 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.5s)
Sep 14 12:16:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:16:10,702 main INFO screen I he’ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 12:16:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:16:27,916 aiohttp.access INFO 195.182.16.23 [14/Sep/2026:12:16:27 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 14 12:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:16:33,719 main INFO screen grug pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (66.6s)
Sep 14 12:16:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:16:52,262 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (57.5s)
Sep 14 12:17:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:17:30,212 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.8s)
Sep 14 12:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:17:52,823 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.4s)
Sep 14 12:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:18:19,525 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (63.0s)
Sep 14 12:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:18:49,892 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (79.2s)
Sep 14 12:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:18:56,499 main INFO screen PUMPCATE pass=0 dev=1.05 ins=78.26 pro=2 1a=False 1b=True 2=True (63.7s)
Sep 14 12:19:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:19:17,722 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.2s)
Sep 14 12:19:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:19:41,241 main INFO screen BBP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.3s)
Sep 14 12:19:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:19:45,821 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.3s)
Sep 14 12:20:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:20:07,846 main INFO screen Pumpers pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.1s)
Sep 14 12:20:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:20:36,520 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.3s)
Sep 14 12:20:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:20:37,736 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:20:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 12:20:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:20:50,613 main INFO screen BBP pass=0 dev=1.46 ins=0.0 pro=3 1a=False 1b=False 2=False (64.8s)
Sep 14 12:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:21:13,662 main INFO screen Tardie pass=0 dev=0.0 ins=21.4 pro=59 1a=False 1b=False 2=True (65.8s)
Sep 14 12:21:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:21:35,909 main INFO screen IBM pass=0 dev=0.0 ins=15.63 pro=44 1a=False 1b=False 2=True (59.4s)
Sep 14 12:21:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:21:56,629 main INFO screen POLARBEAR pass=0 dev=0.0 ins=22.37 pro=57 1a=False 1b=False 2=True (66.0s)
Sep 14 12:22:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:22:08,985 main INFO screen TARDIE pass=1 dev=0.0 ins=18.14 pro=61 1a=False 1b=False 2=False (55.3s)
Sep 14 12:22:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:22:20,283 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:12:22:20 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 12:22:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:22:32,561 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 14 12:23:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:23:08,718 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (72.1s)
Sep 14 12:23:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:23:11,094 main INFO screen Gemini AI pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (62.1s)
Sep 14 12:23:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:23:36,050 main INFO screen MFT pass=0 dev=0.0 ins=0.21 pro=4 1a=False 1b=False 2=False (63.5s)
Sep 14 12:24:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:24:00,884 main INFO screen niketyson pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (52.2s)
Sep 14 12:24:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:24:04,755 main INFO screen TRADY pass=0 dev=0.0 ins=1.31 pro=24 1a=False 1b=True 2=False (53.7s)
Sep 14 12:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:24:44,649 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (68.6s)
Sep 14 12:24:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:24:54,539 main INFO screen 100X pass=0 dev=0.0 ins=38.96 pro=15 1a=False 1b=False 2=True (53.7s)
Sep 14 12:25:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:25:16,264 main INFO screen MIKEICEON pass=0 dev=0.0 ins=37.54 pro=26 1a=True 1b=False 2=True (71.5s)
Sep 14 12:25:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:25:39,865 main INFO screen CATE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
Sep 14 12:26:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:26:01,016 main INFO screen 100X pass=1 dev=0.0 ins=19.59 pro=28 1a=False 1b=False 2=False (66.5s)
Sep 14 12:26:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 12:26:19,529 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:12:26:19 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T12:09:58Z
--- update 2026-09-14T12:15:25Z
--- update 2026-09-14T12:20:36Z
--- update 2026-09-14T12:26:18Z
```

## Analyses (laatste 25 regels)
```
active
12:21:07   4000 tokens, 399598 trades, 53361 posities (26s)
12:21:18   6000 tokens, 607348 trades, 77710 posities (37s)
12:21:28   8000 tokens, 790506 trades, 97115 posities (47s)
12:21:39   10000 tokens, 989412 trades, 123122 posities (58s)
12:21:50   12000 tokens, 1192174 trades, 149190 posities (69s)
12:22:02   14000 tokens, 1402996 trades, 173202 posities (81s)
12:22:14   16000 tokens, 1602703 trades, 196834 posities (93s)
12:22:26   18000 tokens, 1800739 trades, 218299 posities (105s)
12:22:37   20000 tokens, 1981409 trades, 239299 posities (116s)
12:22:50   22000 tokens, 2207020 trades, 266778 posities (129s)
12:23:03   24000 tokens, 2417622 trades, 296742 posities (143s)
12:23:18   26000 tokens, 2643798 trades, 328573 posities (157s)
12:23:30   28000 tokens, 2834712 trades, 352949 posities (169s)
12:23:43   30000 tokens, 3038314 trades, 378594 posities (182s)
12:23:56   32000 tokens, 3240129 trades, 401239 posities (195s)
12:24:10   34000 tokens, 3435601 trades, 426342 posities (209s)
12:24:25   36000 tokens, 3657840 trades, 454829 posities (224s)
12:24:39   38000 tokens, 3859925 trades, 481486 posities (238s)
12:24:53   40000 tokens, 4059765 trades, 504756 posities (252s)
12:25:05   42000 tokens, 4234354 trades, 524489 posities (264s)
12:25:18   44000 tokens, 4431985 trades, 548318 posities (277s)
12:25:32   46000 tokens, 4626357 trades, 574418 posities (291s)
12:25:46   48000 tokens, 4835116 trades, 597599 posities (305s)
12:25:59   50000 tokens, 5038874 trades, 622075 posities (318s)
12:26:12   52000 tokens, 5223412 trades, 643069 posities (331s)
```

## IJking poolkoers (laatste 12 regels)
```
12:09:59 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
12:20:38 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
