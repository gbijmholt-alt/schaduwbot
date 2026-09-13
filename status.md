# Schaduwbot status

- tijd: 2026-09-13 15:19:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 1 hour, 32 minutes
- bot-service: active
- code-versie: 60bc96f
- schijf: 4.6G/38G | geheugen: 1182/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 31530, "tokens_in_memory": 5418, "msgs": 2330876, "trades": 621537, "creates": 7144, "decode_fail": 74321, "rpc_calls": 19266, "rpc_errors": 2, "sol_usd": 100.19188532779175, "open_positions": 21, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 14:36:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:36:26,821 main INFO screen SIKA pass=0 dev=0.0 ins=32.4 pro=18 1a=False 1b=False 2=True (64.4s)
Sep 13 14:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:06,612 main INFO screen cheese pass=0 dev=0.0 ins=33.53 pro=58 1a=False 1b=False 2=True (69.7s)
Sep 13 14:37:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:31,165 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:14:37:31 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 14:37:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:37:37,131 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:37:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:39:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:39:14,170 rpc WARNING rpc getTokenAccountsByOwner exc Server disconnected
Sep 13 14:39:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:39:17,501 main INFO screen MIMI pass=0 dev=0.0 ins=22.81 pro=63 1a=False 1b=False 2=True (77.2s)
Sep 13 14:40:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:40:57,367 main INFO screen RAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.9s)
Sep 13 14:41:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:11,919 main INFO screen RAWR pass=0 dev=0.0 ins=32.09 pro=38 1a=False 1b=True 2=True (66.1s)
Sep 13 14:41:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:23,452 main INFO screen $AURA pass=0 dev=0.19 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 13 14:41:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:41:46,132 main INFO screen KAWAIICAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.8s)
Sep 13 14:42:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:42:57,378 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:42:57 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:44:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:44:30,643 main INFO screen SSP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (48.0s)
Sep 13 14:44:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:44:53,679 main INFO screen RICK pass=0 dev=0.43 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 13 14:46:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:46:17,412 main INFO screen BotTrencher pass=1 dev=0.0 ins=11.38 pro=54 1a=False 1b=False 2=False (63.3s)
Sep 13 14:47:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:47:00,598 main INFO screen pleun pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 13 14:47:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:47:48,597 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.0s)
Sep 13 14:48:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:48:10,290 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:48:10 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:48:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:48:40,970 main INFO screen OpenAI pass=0 dev=99.3 ins=0.0 pro=1 1a=False 1b=False 2=True (46.2s)
Sep 13 14:49:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:49:08,256 main INFO screen $MIZO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (48.3s)
Sep 13 14:50:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:50:53,171 main INFO screen CROKAH pass=0 dev=0.0 ins=31.83 pro=30 1a=False 1b=True 2=True (49.9s)
Sep 13 14:52:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:01,898 main INFO screen Quack pass=1 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=False (67.5s)
Sep 13 14:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:04,837 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.3s)
Sep 13 14:52:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:29,001 main INFO screen HAND pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.7s)
Sep 13 14:52:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:52:47,735 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (45.8s)
Sep 13 14:53:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:53:20,419 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:53:20 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:53:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:53:57,725 main INFO screen PEPON pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (52.9s)
Sep 13 14:54:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:54:26,326 main INFO screen TSLA pass=1 dev=0.0 ins=0.0 pro=26 1a=False 1b=False 2=False (59.5s)
Sep 13 14:54:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:54:27,200 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.1s)
Sep 13 14:56:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:12,199 main INFO screen anonbikesn pass=0 dev=0.0 ins=36.19 pro=21 1a=False 1b=False 2=True (60.5s)
Sep 13 14:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:50,467 aiohttp.access INFO 150.107.36.82 [13/Sep/2026:14:56:50 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 13 14:56:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:56:50,814 aiohttp.access INFO 150.107.36.82 [13/Sep/2026:14:56:50 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 14:57:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:57:24,653 main INFO screen CANTY pass=0 dev=0.0 ins=31.82 pro=28 1a=False 1b=True 2=True (61.4s)
Sep 13 14:57:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:57:32,628 main INFO screen RAVEN pass=1 dev=0.0 ins=8.56 pro=19 1a=False 1b=False 2=False (49.3s)
Sep 13 14:58:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:00,464 main INFO screen CHEESE pass=1 dev=0.0 ins=15.33 pro=70 1a=False 1b=False 2=False (67.2s)
Sep 13 14:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:18,847 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 13 14:58:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:58:37,245 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:14:58:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 14:59:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 14:59:08,751 main INFO screen stocklana pass=0 dev=0.0 ins=25.12 pro=32 1a=False 1b=False 2=True (48.9s)
Sep 13 15:00:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:00:44,394 main INFO screen AAPLCAT pass=0 dev=5.78 ins=72.68 pro=0 1a=False 1b=False 2=True (52.0s)
Sep 13 15:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:30,087 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.7s)
Sep 13 15:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:30,366 main INFO screen RC pass=1 dev=0.01 ins=5.36 pro=40 1a=False 1b=False 2=False (71.4s)
Sep 13 15:01:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:01:37,911 main INFO screen SCM pass=0 dev=0.0 ins=32.33 pro=27 1a=False 1b=False 2=True (53.5s)
Sep 13 15:02:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:02:30,009 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.0s)
Sep 13 15:03:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:03:19,862 main INFO screen Stocklana pass=0 dev=0.0 ins=18.91 pro=59 1a=False 1b=False 2=True (61.6s)
Sep 13 15:03:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:03:32,321 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 13 15:04:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:04:08,669 main INFO screen batonguy pass=0 dev=0.0 ins=79.27 pro=0 1a=False 1b=True 2=True (52.0s)
Sep 13 15:04:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:04:11,823 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:04:11 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 15:05:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:05:14,033 main INFO screen PIKI pass=0 dev=0.0 ins=32.29 pro=33 1a=False 1b=True 2=True (63.0s)
Sep 13 15:06:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:06:33,345 main INFO screen CHONKS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.7s)
Sep 13 15:07:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:07:20,573 main INFO screen AMBR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.6s)
Sep 13 15:07:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:07:31,932 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.0s)
Sep 13 15:07:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:07:50,722 main INFO screen cheese  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 13 15:08:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:08:55,613 main INFO screen INU69 pass=0 dev=0.0 ins=32.48 pro=37 1a=False 1b=False 2=True (68.9s)
Sep 13 15:09:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:09:12,520 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:09:12 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 15:09:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:09:18,810 main INFO screen INU pass=1 dev=0.0 ins=0.74 pro=65 1a=False 1b=False 2=False (52.6s)
Sep 13 15:09:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:09:53,494 main INFO screen SLOWAI pass=0 dev=1.0 ins=0.0 pro=8 1a=False 1b=False 2=False (68.7s)
Sep 13 15:10:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:10:07,225 main INFO screen Swarm pass=0 dev=0.0 ins=25.68 pro=72 1a=False 1b=False 2=True (60.5s)
Sep 13 15:10:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:10:34,213 main INFO screen YOINK pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 13 15:10:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:10:47,244 main INFO screen BBC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 13 15:11:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:11:57,981 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 13 15:12:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:12:28,863 main INFO screen YONK pep pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (69.9s)
Sep 13 15:12:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:12:36,673 main INFO screen SOL人生  pass=0 dev=0.11 ins=0.0 pro=7 1a=False 1b=False 2=False (67.7s)
Sep 13 15:13:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:13:06,445 main INFO screen Google pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 13 15:13:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:13:59,064 main INFO screen Sloth pass=1 dev=0.35 ins=14.2 pro=54 1a=False 1b=False 2=False (66.3s)
Sep 13 15:14:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:14:15,212 main INFO screen Cat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.5s)
Sep 13 15:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:14:18,814 main INFO screen ‎  pass=0 dev=0.0 ins=21.82 pro=45 1a=False 1b=False 2=False (67.7s)
Sep 13 15:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:14:37,497 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:14:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 15:14:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:14:55,317 main INFO screen WRN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.3s)
Sep 13 15:15:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:15:10,573 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.4s)
Sep 13 15:15:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:15:11,133 main INFO screen Robinhood pass=0 dev=68.09 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 13 15:15:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:15:52,144 main INFO screen DoNgkyY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.8s)
Sep 13 15:16:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:16:20,848 main INFO screen DOOROC pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (69.7s)
Sep 13 15:16:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:16:22,384 main INFO screen Ernie pass=0 dev=0.0 ins=22.37 pro=70 1a=False 1b=False 2=True (71.8s)
Sep 13 15:16:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:16:55,689 main INFO screen PANIC pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 13 15:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:17:34,300 main INFO screen Daniel pass=0 dev=0.0 ins=35.28 pro=53 1a=False 1b=False 2=True (73.5s)
Sep 13 15:17:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:17:42,882 main INFO screen SHIT pass=1 dev=0.0 ins=5.36 pro=47 1a=False 1b=False 2=False (80.5s)
Sep 13 15:18:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:18:01,097 main INFO screen AAPLCAT pass=0 dev=3.14 ins=72.68 pro=2 1a=False 1b=True 2=True (65.4s)
Sep 13 15:18:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:18:55,198 main INFO screen BBP pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (80.9s)
Sep 13 15:18:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:18:56,738 main INFO screen STECHIO pass=0 dev=0.0 ins=32.1 pro=49 1a=False 1b=False 2=True (73.9s)
Sep 13 15:19:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:19:26,526 main INFO screen CHONKS pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (82.7s)
Sep 13 15:19:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:19:37,985 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:19:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T14:00:36Z
--- update 2026-09-13T14:05:53Z
--- update 2026-09-13T14:11:04Z
--- update 2026-09-13T14:16:36Z
--- update 2026-09-13T14:21:52Z
--- update 2026-09-13T14:27:12Z
--- update 2026-09-13T14:32:14Z
--- update 2026-09-13T14:37:36Z
--- update 2026-09-13T14:42:56Z
--- update 2026-09-13T14:48:09Z
--- update 2026-09-13T14:53:19Z
nieuwe code: 60bc96f
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 5753ff544a174b8f8dc6b2ae1512fa0d
analyses gestart (0d01412cf2b7)
--- update 2026-09-13T14:58:36Z
--- update 2026-09-13T15:04:10Z
--- update 2026-09-13T15:09:11Z
--- update 2026-09-13T15:14:36Z
--- update 2026-09-13T15:19:36Z
```

## Analyses (laatste 25 regels)
```
inactive
15:07:49   18000 tokens, 1957713 trades, 303012 posities (42s)
15:07:52   20000 tokens, 2205723 trades, 346819 posities (45s)
15:07:55   22000 tokens, 2415018 trades, 382348 posities (48s)
15:07:58   24000 tokens, 2637315 trades, 413206 posities (51s)
15:08:02   26000 tokens, 2842322 trades, 443504 posities (55s)
15:08:06   28000 tokens, 3079909 trades, 482361 posities (59s)
15:08:10   30000 tokens, 3309989 trades, 518436 posities (63s)
15:08:14   32000 tokens, 3521537 trades, 551003 posities (67s)
15:08:18   34000 tokens, 3746980 trades, 588738 posities (72s)
15:08:23   36000 tokens, 3970966 trades, 625445 posities (76s)
15:08:28   38000 tokens, 4180240 trades, 656597 posities (81s)
15:08:32   40000 tokens, 4388141 trades, 685749 posities (86s)
15:08:38   42000 tokens, 4602402 trades, 721807 posities (91s)
15:08:43   44000 tokens, 4819582 trades, 757957 posities (96s)
15:08:48   46000 tokens, 5038044 trades, 792211 posities (101s)
15:08:53   48000 tokens, 5250351 trades, 829492 posities (106s)
15:08:58   50000 tokens, 5474559 trades, 865169 posities (111s)
15:09:02   52000 tokens, 5706716 trades, 902907 posities (115s)
15:09:06   54000 tokens, 5939248 trades, 951801 posities (120s)
15:09:09 posities: 980409 uit 6088351 trades (123s)
15:09:22 200273 wallets gerekend
15:09:22 geluk-toets
15:09:55 persistentie
15:09:58 kopieer-simulatie
15:11:00 klaar in 234s -> /opt/schaduwbot/reports/wallets.md
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
