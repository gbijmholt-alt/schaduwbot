# Schaduwbot status

- tijd: 2026-09-14 04:22:45 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 14 hours, 35 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.4G/38G | geheugen: 1907/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 78517, "tokens_in_memory": 7014, "msgs": 10591581, "trades": 2217264, "creates": 23362, "decode_fail": 193263, "rpc_calls": 64467, "rpc_errors": 3, "sol_usd": 101.04170631170469, "open_positions": 15, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 03:39:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:39:50,208 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (50.2s)
Sep 14 03:40:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:29,249 main INFO screen SCRVAN pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (71.0s)
Sep 14 03:40:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:39,696 main INFO screen . pass=1 dev=0.42 ins=0.0 pro=12 1a=False 1b=False 2=False (64.3s)
Sep 14 03:40:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:45,699 main INFO screen OOmarley pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.5s)
Sep 14 03:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:40:59,139 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:40:59 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:41:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:41:19,392 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 14 03:41:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:41:38,213 main INFO screen POON pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (58.5s)
Sep 14 03:41:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:41:42,758 aiohttp.access INFO 195.182.16.23 [14/Sep/2026:03:41:42 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 14 03:41:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:41:51,502 main INFO screen TOON pass=1 dev=1.89 ins=0.0 pro=13 1a=False 1b=False 2=False (65.8s)
Sep 14 03:42:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:42:27,530 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (68.1s)
Sep 14 03:42:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:42:47,385 main INFO screen LOS pass=0 dev=0.0 ins=26.16 pro=76 1a=False 1b=False 2=True (69.2s)
Sep 14 03:42:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:42:56,166 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.7s)
Sep 14 03:43:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:43:34,623 main INFO screen C80S pass=0 dev=11.13 ins=0.0 pro=11 1a=False 1b=False 2=False (67.1s)
Sep 14 03:43:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:43:43,014 main INFO screen BABYCATE pass=0 dev=2.9 ins=75.89 pro=1 1a=True 1b=True 2=True (48.0s)
Sep 14 03:44:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:44:50,529 main INFO screen NOLA pass=0 dev=0.0 ins=27.16 pro=46 1a=False 1b=False 2=True (66.1s)
Sep 14 03:44:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:44:56,969 main INFO screen G2OZRD1KAU pass=0 dev=0.01 ins=0.0 pro=8 1a=False 1b=False 2=False (66.5s)
Sep 14 03:45:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:45:05,991 main INFO screen SUNK pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=False 2=True (65.1s)
Sep 14 03:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:45:45,773 main INFO screen SNOX pass=0 dev=0.04 ins=79.27 pro=6 1a=False 1b=True 2=True (55.2s)
Sep 14 03:46:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:46:14,007 main INFO screen soltwine pass=0 dev=0.18 ins=79.13 pro=9 1a=False 1b=False 2=True (62.7s)
Sep 14 03:46:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:46:14,996 main INFO screen DOG pass=0 dev=0.0 ins=34.02 pro=61 1a=False 1b=False 2=True (69.0s)
Sep 14 03:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:46:37,012 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:46:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:48:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:48:17,717 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (60.4s)
Sep 14 03:48:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:48:19,646 main INFO screen OB pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (66.8s)
Sep 14 03:48:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:48:22,150 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.2s)
Sep 14 03:49:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:49:24,588 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (66.9s)
Sep 14 03:49:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:49:34,687 main INFO screen POON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 14 03:49:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:49:50,278 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.7s)
Sep 14 03:50:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:50:20,009 main INFO screen Zaiken pass=0 dev=0.0 ins=14.64 pro=6 1a=False 1b=False 2=False (55.4s)
Sep 14 03:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:51:35,243 main INFO screen RADR pass=0 dev=36.36 ins=0.0 pro=2 1a=False 1b=False 2=True (53.8s)
Sep 14 03:51:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:51:36,959 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:51:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 03:51:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:51:43,911 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.9s)
Sep 14 03:52:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:52:16,523 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.4s)
Sep 14 03:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:53:54,695 main INFO screen BILL pass=0 dev=0.0 ins=25.15 pro=63 1a=False 1b=True 2=True (54.3s)
Sep 14 03:54:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:54:19,351 main INFO screen kittylick pass=1 dev=1.15 ins=0.0 pro=12 1a=False 1b=False 2=False (66.2s)
Sep 14 03:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:55:43,477 main INFO screen COMCAT pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (50.7s)
Sep 14 03:56:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:56:37,681 main INFO screen LUMEN pass=1 dev=3.92 ins=0.0 pro=39 1a=False 1b=False 2=False (51.7s)
Sep 14 03:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:56:39,162 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:03:56:39 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 03:56:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:56:58,313 main INFO screen TAC pass=0 dev=0.6 ins=3.2 pro=64 1a=False 1b=False 2=True (63.0s)
Sep 14 03:57:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:57:23,680 main INFO screen CATWIF pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (55.1s)
Sep 14 03:57:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:57:47,222 main INFO screen TUNASUB pass=0 dev=0.0 ins=25.39 pro=39 1a=False 1b=False 2=True (52.8s)
Sep 14 03:58:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:58:27,943 main INFO screen HORIZON pass=0 dev=38.09 ins=0.0 pro=3 1a=False 1b=False 2=True (49.4s)
Sep 14 03:59:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 03:59:24,125 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.9s)
Sep 14 04:00:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:00:12,160 main INFO screen Racecar pass=0 dev=0.0 ins=23.31 pro=62 1a=False 1b=False 2=True (63.3s)
Sep 14 04:00:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:00:31,397 main INFO screen BOOB pass=0 dev=0.0 ins=22.59 pro=74 1a=False 1b=False 2=True (62.1s)
Sep 14 04:00:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:00:52,908 aiohttp.access INFO 176.65.148.93 [14/Sep/2026:04:00:52 +0000] "CONNECT  HTTP/1.1" 404 193 "-" "-"
Sep 14 04:00:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:00:53,269 aiohttp.access INFO 176.65.148.93 [14/Sep/2026:04:00:53 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 14 04:00:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:00:53,741 aiohttp.access INFO 176.65.148.93 [14/Sep/2026:04:00:53 +0000] "GET / HTTP/1.1" 404 193 "-" "ifhttp"
Sep 14 04:01:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:01:38,372 main INFO screen $AURA pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (77.1s)
Sep 14 04:01:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:01:46,052 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (73.7s)
Sep 14 04:01:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:01:46,134 main INFO screen nttl pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (74.7s)
Sep 14 04:02:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:02:08,671 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:02:08 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 04:02:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:02:38,228 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.7s)
Sep 14 04:04:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:04:26,810 main INFO screen 34% pass=0 dev=0.09 ins=0.0 pro=5 1a=False 1b=False 2=False (67.9s)
Sep 14 04:04:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:04:39,042 main INFO screen GPEPET pass=0 dev=0.37 ins=78.96 pro=7 1a=False 1b=True 2=True (60.0s)
Sep 14 04:05:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:06,919 main INFO screen BMW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.3s)
Sep 14 04:05:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:17,708 main INFO screen TIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 14 04:05:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:05:44,222 main INFO screen poop pass=0 dev=0.0 ins=26.54 pro=51 1a=False 1b=False 2=True (50.2s)
Sep 14 04:06:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:06:27,279 main INFO screen Gen pass=1 dev=0.42 ins=0.0 pro=17 1a=False 1b=False 2=False (67.5s)
Sep 14 04:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:07:30,961 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:07:30 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 04:07:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:07:39,247 main INFO screen RETARD pass=0 dev=0.0 ins=25.34 pro=69 1a=False 1b=False 2=True (60.0s)
Sep 14 04:11:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:15,642 main INFO screen CTO pass=0 dev=0.0 ins=16.75 pro=71 1a=False 1b=False 2=True (63.5s)
Sep 14 04:11:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:21,878 main INFO screen TRUMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 14 04:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:11:43,260 main INFO screen SHATGPT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 14 04:12:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:24,934 main INFO screen EMEM pass=0 dev=0.0 ins=25.29 pro=66 1a=False 1b=False 2=True (69.3s)
Sep 14 04:12:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:34,218 main INFO screen twineACT pass=0 dev=0.18 ins=77.58 pro=17 1a=False 1b=False 2=True (72.3s)
Sep 14 04:12:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:12:35,583 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:12:35 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 04:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:13:07,106 main INFO screen ShanaTova pass=0 dev=0.0 ins=17.41 pro=40 1a=False 1b=False 2=True (72.5s)
Sep 14 04:14:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:06,262 main INFO screen Nike pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.0s)
Sep 14 04:14:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:22,861 main INFO screen POP pass=0 dev=0.0 ins=14.23 pro=55 1a=False 1b=False 2=True (58.7s)
Sep 14 04:14:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:14:32,946 main INFO screen MEMEBACK pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (59.0s)
Sep 14 04:15:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:15:56,598 main INFO screen Rotator pass=0 dev=0.0 ins=33.81 pro=80 1a=False 1b=False 2=True (62.5s)
Sep 14 04:16:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:16:34,665 main INFO screen poop pass=0 dev=0.0 ins=21.86 pro=65 1a=False 1b=False 2=True (61.0s)
Sep 14 04:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:17:37,132 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:17:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 04:18:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:18:23,112 main INFO screen Rotator pass=1 dev=0.0 ins=8.76 pro=49 1a=False 1b=False 2=False (60.3s)
Sep 14 04:18:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:18:40,445 main INFO screen MIKESEM pass=0 dev=34.74 ins=0.0 pro=5 1a=False 1b=False 2=True (62.3s)
Sep 14 04:19:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:19:39,878 main INFO screen Humanity pass=0 dev=0.0 ins=33.57 pro=71 1a=False 1b=False 2=True (64.4s)
Sep 14 04:20:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:20:15,653 main INFO screen $RENT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.8s)
Sep 14 04:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:20:18,240 main INFO screen GUMP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.5s)
Sep 14 04:21:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:21:25,613 main INFO screen . pass=0 dev=0.26 ins=0.0 pro=4 1a=False 1b=False 2=False (65.7s)
Sep 14 04:22:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 04:22:45,479 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:04:22:45 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 5c723321a25a43918dd7f5917cca7869
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T02:55:19Z
--- update 2026-09-14T03:00:19Z
--- update 2026-09-14T03:05:21Z
--- update 2026-09-14T03:10:24Z
--- update 2026-09-14T03:15:35Z
--- update 2026-09-14T03:20:36Z
--- update 2026-09-14T03:25:45Z
--- update 2026-09-14T03:30:49Z
--- update 2026-09-14T03:35:52Z
--- update 2026-09-14T03:40:58Z
--- update 2026-09-14T03:46:36Z
--- update 2026-09-14T03:51:35Z
--- update 2026-09-14T03:56:38Z
--- update 2026-09-14T04:02:07Z
--- update 2026-09-14T04:07:29Z
--- update 2026-09-14T04:12:34Z
--- update 2026-09-14T04:17:36Z
--- update 2026-09-14T04:22:44Z
```

## Analyses (laatste 25 regels)
```
inactive
03:21:51   32000 tokens, 3238043 trades, 422854 posities (177s)
03:22:04   34000 tokens, 3461147 trades, 451926 posities (191s)
03:22:17   36000 tokens, 3662732 trades, 479673 posities (204s)
03:22:31   38000 tokens, 3865753 trades, 505063 posities (218s)
03:22:43   40000 tokens, 4045000 trades, 525732 posities (230s)
03:22:57   42000 tokens, 4249962 trades, 552995 posities (244s)
03:23:10   44000 tokens, 4446595 trades, 578153 posities (257s)
03:23:24   46000 tokens, 4659194 trades, 606292 posities (270s)
03:23:36   48000 tokens, 4854158 trades, 628527 posities (283s)
03:23:48   50000 tokens, 5042947 trades, 653903 posities (295s)
03:24:00   52000 tokens, 5230122 trades, 676078 posities (307s)
03:24:11   54000 tokens, 5422843 trades, 703819 posities (318s)
03:24:23   56000 tokens, 5615846 trades, 727463 posities (330s)
03:24:35   58000 tokens, 5810050 trades, 754947 posities (341s)
03:24:47   60000 tokens, 6031857 trades, 786254 posities (354s)
03:24:57   62000 tokens, 6234325 trades, 813935 posities (364s)
03:25:07   64000 tokens, 6430429 trades, 840854 posities (374s)
03:25:18   66000 tokens, 6647572 trades, 880931 posities (385s)
03:25:28   68000 tokens, 6828531 trades, 905157 posities (394s)
03:25:28 posities: 907715 uit 6836758 trades (398s)
03:25:40 194054 wallets gerekend
03:25:40 geluk-toets
03:26:14 persistentie
03:26:17 kopieer-simulatie
03:28:13 klaar in 563s -> /opt/schaduwbot/reports/wallets.md
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
