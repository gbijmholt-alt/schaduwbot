# Schaduwbot status

- tijd: 2026-09-15 11:05:50 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 21 hours, 18 minutes
- bot-service: active
- code-versie: b2d6d06
- schijf: 7.1G/38G | geheugen: 2298/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 189102, "tokens_in_memory": 6015, "msgs": 27436362, "trades": 5647085, "creates": 60600, "decode_fail": 469740, "rpc_calls": 167121, "rpc_errors": 14, "sol_usd": 100.8238934473602, "open_positions": 51, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 10:40:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:40:51,704 main INFO screen bruh pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.4s)
Sep 15 10:41:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:41:30,890 main INFO screen NEEGY pass=0 dev=0.0 ins=9.33 pro=66 1a=False 1b=False 2=True (72.0s)
Sep 15 10:41:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:41:35,172 main INFO screen STOCKPILLS pass=0 dev=0.0 ins=0.0 pro=45 1a=False 1b=False 2=False (68.6s)
Sep 15 10:41:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:41:56,413 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.7s)
Sep 15 10:42:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:42:22,002 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.1s)
Sep 15 10:42:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:42:37,274 main INFO screen bruh pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (62.1s)
Sep 15 10:42:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:42:52,312 main INFO screen OIIAOIIA pass=0 dev=0.0 ins=0.0 pro=52 1a=False 1b=False 2=True (55.9s)
Sep 15 10:43:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:43:16,633 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (54.6s)
Sep 15 10:43:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:43:36,338 main INFO screen MESSI pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (59.1s)
Sep 15 10:43:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:43:44,140 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.8s)
Sep 15 10:44:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:44:08,288 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.7s)
Sep 15 10:44:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:44:28,443 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (52.1s)
Sep 15 10:44:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:44:33,093 main INFO screen deeznuts pass=0 dev=0.0 ins=31.51 pro=61 1a=False 1b=False 2=True (49.0s)
Sep 15 10:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:44:59,499 main INFO screen Batonbrain pass=0 dev=0.0 ins=78.55 pro=4 1a=False 1b=True 2=True (51.2s)
Sep 15 10:45:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:45:40,527 main INFO screen NIGGER pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (72.1s)
Sep 15 10:45:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:45:43,597 main INFO screen KACHING pass=0 dev=0.0 ins=24.76 pro=69 1a=False 1b=False 2=False (70.5s)
Sep 15 10:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:45:45,099 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:10:45:45 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 10:45:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:45:55,329 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.8s)
Sep 15 10:46:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:46:34,492 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.0s)
Sep 15 10:46:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:46:35,911 main INFO screen STONK10 pass=0 dev=0.0 ins=136.5 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 15 10:46:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:46:49,568 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=77.99 pro=3 1a=False 1b=True 2=True (54.2s)
Sep 15 10:47:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:47:39,610 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.7s)
Sep 15 10:47:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:47:43,076 main INFO screen NTFS pass=0 dev=0.0 ins=114.63 pro=1 1a=False 1b=False 2=True (53.5s)
Sep 15 10:47:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:47:46,651 main INFO screen UPTOOMUCH pass=0 dev=0.0 ins=26.13 pro=76 1a=False 1b=False 2=True (72.2s)
Sep 15 10:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:48:47,149 main INFO screen BRRRRRR pass=0 dev=0.0 ins=26.42 pro=31 1a=False 1b=False 2=False (67.5s)
Sep 15 10:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:48:47,416 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 15 10:48:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:48:52,414 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (65.8s)
Sep 15 10:49:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:49:58,100 main INFO screen Dudeass pass=0 dev=0.0 ins=72.21 pro=77 1a=False 1b=False 2=True (70.7s)
Sep 15 10:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:49:59,153 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.0s)
Sep 15 10:50:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:50:02,462 main INFO screen TOMTANKS pass=0 dev=0.0 ins=46.11 pro=44 1a=False 1b=False 2=True (70.0s)
Sep 15 10:50:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:50:46,428 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:10:50:46 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 10:50:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:50:54,068 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.0s)
Sep 15 10:51:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:51:03,524 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.1s)
Sep 15 10:51:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:51:04,574 main INFO screen fart pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.4s)
Sep 15 10:52:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:52:02,947 main INFO screen Hypnotize pass=0 dev=0.0 ins=1.1 pro=70 1a=False 1b=False 2=False (68.9s)
Sep 15 10:52:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:52:09,418 main INFO screen WWR pass=0 dev=0.0 ins=76.04 pro=1 1a=False 1b=False 2=True (65.9s)
Sep 15 10:52:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:52:11,566 main INFO screen BUY pass=0 dev=0.0 ins=25.39 pro=76 1a=False 1b=False 2=True (67.0s)
Sep 15 10:52:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:52:56,484 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (53.5s)
Sep 15 10:53:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:53:13,338 main INFO screen OOF pass=0 dev=0.0 ins=24.53 pro=71 1a=False 1b=False 2=True (63.9s)
Sep 15 10:53:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:53:14,567 main INFO screen soundcoin pass=0 dev=0.0 ins=26.56 pro=44 1a=False 1b=False 2=True (63.0s)
Sep 15 10:53:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:53:48,712 main INFO screen MEMEMESSI pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (52.2s)
Sep 15 10:54:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:54:18,364 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.0s)
Sep 15 10:54:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:54:19,358 main INFO screen SHIT pass=0 dev=0.0 ins=30.95 pro=59 1a=False 1b=False 2=True (64.8s)
Sep 15 10:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:54:55,399 main INFO screen RICKROLL pass=0 dev=0.0 ins=25.11 pro=70 1a=False 1b=False 2=True (66.7s)
Sep 15 10:55:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:12,203 main INFO screen STONK pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (53.8s)
Sep 15 10:55:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:22,405 main INFO screen ONLYUP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (63.0s)
Sep 15 10:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:48,481 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:10:55:48 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 10:55:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:55:53,232 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.8s)
Sep 15 10:56:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:13,758 main INFO screen STOCKPILLS pass=0 dev=0.0 ins=1.68 pro=69 1a=False 1b=False 2=False (61.6s)
Sep 15 10:56:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:27,366 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=78.69 pro=5 1a=False 1b=True 2=True (65.0s)
Sep 15 10:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:56:50,462 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (57.2s)
Sep 15 10:57:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:12,312 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (58.6s)
Sep 15 10:57:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:22,517 main INFO screen Blavicular pass=0 dev=0.0 ins=28.56 pro=68 1a=False 1b=False 2=True (55.1s)
Sep 15 10:57:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:57:49,307 main INFO screen ONLYUP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.8s)
Sep 15 10:58:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:08,689 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 15 10:58:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:20,336 main INFO screen ONLYUP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.8s)
Sep 15 10:58:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:58:44,367 main INFO screen POOLS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 15 10:59:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:03,312 main INFO screen solinscrip pass=0 dev=0.0 ins=33.6 pro=42 1a=False 1b=False 2=True (54.6s)
Sep 15 10:59:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:15,781 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.4s)
Sep 15 10:59:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:34,585 main INFO screen nigga pass=0 dev=0.0 ins=18.89 pro=49 1a=False 1b=False 2=False (50.2s)
Sep 15 10:59:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 10:59:57,091 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 15 11:00:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:15,117 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.3s)
Sep 15 11:00:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:47,224 main INFO screen LMAO pass=0 dev=0.0 ins=5.07 pro=53 1a=False 1b=False 2=False (72.6s)
Sep 15 11:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:50,999 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.9s)
Sep 15 11:00:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:00:51,068 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:00:51 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 11:01:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:12,496 main INFO screen snail pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 15 11:01:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:42,371 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.1s)
Sep 15 11:01:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:01:52,963 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.0s)
Sep 15 11:02:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:06,057 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 15 11:02:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:34,670 main INFO screen CATE pass=0 dev=0.0 ins=135.64 pro=0 1a=False 1b=False 2=True (52.3s)
Sep 15 11:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:02:50,658 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 11:03:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:03,960 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 15 11:03:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:30,742 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 15 11:03:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:50,346 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (59.7s)
Sep 15 11:03:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:03:58,070 main INFO screen USELESSER pass=0 dev=0.0 ins=0.21 pro=4 1a=False 1b=False 2=False (54.1s)
Sep 15 11:04:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:04:35,849 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (65.1s)
Sep 15 11:05:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:04,103 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (73.8s)
Sep 15 11:05:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:04,141 main INFO screen sol pass=0 dev=0.03 ins=0.0 pro=1 1a=False 1b=False 2=True (66.1s)
Sep 15 11:05:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:47,367 main INFO screen mruh pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (71.5s)
Sep 15 11:05:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 11:05:50,484 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:11:05:50 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (ea3860901364)
--- update 2026-09-15T10:05:35Z
--- update 2026-09-15T10:10:35Z
nieuwe code: 1978398
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T10:15:36Z
--- update 2026-09-15T10:20:40Z
nieuwe code: b2d6d06
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T10:25:40Z
--- update 2026-09-15T10:30:40Z
--- update 2026-09-15T10:35:41Z
--- update 2026-09-15T10:40:43Z
--- update 2026-09-15T10:45:43Z
--- update 2026-09-15T10:50:45Z
--- update 2026-09-15T10:55:47Z
--- update 2026-09-15T11:00:49Z
Running as unit: schaduwbot-wallets.service; invocation ID: eaf6b7b4df234ac0b42ef826db918f51
analyses gestart (5b8847ad3b6d)
--- update 2026-09-15T11:05:49Z
```

## Analyses (laatste 40 regels)
```
active
09:44:55   44000 tokens, 4267583 trades, 519384 posities (293s)
09:45:07   46000 tokens, 4445286 trades, 541079 posities (306s)
09:45:20   48000 tokens, 4625749 trades, 562677 posities (318s)
09:45:34   50000 tokens, 4813554 trades, 585505 posities (332s)
09:45:49   52000 tokens, 5034036 trades, 615083 posities (347s)
09:46:03   54000 tokens, 5222179 trades, 638754 posities (361s)
09:46:18   56000 tokens, 5420893 trades, 666757 posities (377s)
09:46:31   58000 tokens, 5587511 trades, 684159 posities (390s)
09:46:47   60000 tokens, 5783930 trades, 710882 posities (405s)
09:47:01   62000 tokens, 5973435 trades, 733938 posities (420s)
09:47:15   64000 tokens, 6172546 trades, 762658 posities (433s)
09:47:29   66000 tokens, 6368136 trades, 786022 posities (447s)
09:47:44   68000 tokens, 6558130 trades, 811760 posities (463s)
09:47:59   70000 tokens, 6738863 trades, 833010 posities (477s)
09:48:14   72000 tokens, 6940230 trades, 857491 posities (492s)
09:48:30   74000 tokens, 7140514 trades, 889117 posities (508s)
09:48:44   76000 tokens, 7316833 trades, 913068 posities (522s)
09:48:45 posities: 913473 uit 7325165 trades (529s)
09:48:58 210371 wallets gerekend
09:48:58 geluk-toets
09:49:35 persistentie
09:49:38 kopieer-simulatie
09:52:03 klaar in 727s -> /opt/schaduwbot/reports/wallets.md
10:13:23   500/6700 lopers, 14233 koppelingen
10:14:09   1000/6700 lopers, 27609 koppelingen
10:14:46   1500/6700 lopers, 35674 koppelingen
10:15:33   2000/6700 lopers, 46613 koppelingen
10:16:11   2500/6700 lopers, 55002 koppelingen
10:16:39   3000/6700 lopers, 62231 koppelingen
10:17:23   3500/6700 lopers, 71433 koppelingen
10:17:51   4000/6700 lopers, 77748 koppelingen
10:18:35   4500/6700 lopers, 85514 koppelingen
10:19:12   5000/6700 lopers, 93093 koppelingen
10:19:43   5500/6700 lopers, 99227 koppelingen
10:20:56   6000/6700 lopers, 110982 koppelingen
10:21:42   6500/6700 lopers, 117630 koppelingen
10:21:52 klaar in 1276s: 6700 lopers, 40017 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/vamp.py 11:00:50
11:00:50 tokens lezen
11:00:55 133728 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
09:56:04 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=226 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
09:56:04 ijk-diagnose: nieuwste migratie 0.4 min oud | migraties 15/60/240 min: 11/39/155 | al gemeten: 611
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
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
