# Schaduwbot status

- tijd: 2026-09-13 09:31:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 19 hours, 44 minutes
- bot-service: active
- code-versie: 0a977ba
- schijf: 4.4G/38G | geheugen: 779/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 10630, "tokens_in_memory": 1819, "msgs": 526343, "trades": 157347, "creates": 1819, "decode_fail": 22368, "rpc_calls": 5416, "rpc_errors": 1, "sol_usd": 99.71760004640893, "open_positions": 32, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 08:45:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:15,507 main INFO screen ROBINCAT pass=0 dev=0.16 ins=0.0 pro=4 1a=False 1b=False 2=False (66.0s)
Sep 13 08:45:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:47,868 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:45:47 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
Sep 13 08:45:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:45:48,208 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:45:48 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
Sep 13 08:46:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:46:20,370 main INFO screen ONLY CATS pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (62.4s)
Sep 13 08:46:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:46:41,073 main INFO screen stonk pass=1 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (59.5s)
Sep 13 08:47:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:47:03,224 aiohttp.access INFO 107.150.100.197 [13/Sep/2026:08:47:03 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
Sep 13 08:48:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:48:45,298 main INFO screen stonk pass=1 dev=0.0 ins=0.05 pro=23 1a=False 1b=False 2=False (56.8s)
Sep 13 08:49:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:11,443 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=77.83 pro=16 1a=False 1b=True 2=True (53.3s)
Sep 13 08:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:20,899 rpc WARNING rpc getTokenLargestAccounts exc Server disconnected
Sep 13 08:49:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:49:34,712 main INFO screen CATGPTCOIN pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (52.8s)
Sep 13 08:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:50:26,900 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:50:26 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 08:50:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:50:43,019 main INFO screen TRUMPGPT pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (57.0s)
Sep 13 08:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:50:48,930 main INFO screen stonk pass=0 dev=65.71 ins=0.05 pro=21 1a=False 1b=True 2=False (54.9s)
Sep 13 08:53:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:53:33,279 main INFO screen HBD pass=0 dev=0.47 ins=0.0 pro=3 1a=False 1b=False 2=False (53.7s)
Sep 13 08:53:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:53:47,216 main INFO screen zcashers pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.7s)
Sep 13 08:55:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:55:24,429 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.8s)
Sep 13 08:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:55:37,117 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:08:55:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 08:55:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:55:45,978 main INFO screen VPN pass=0 dev=0.0 ins=20.22 pro=55 1a=False 1b=False 2=True (67.3s)
Sep 13 08:56:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:56:19,085 main INFO screen ROKUPHONE pass=0 dev=42.49 ins=0.0 pro=2 1a=False 1b=False 2=True (70.0s)
Sep 13 08:56:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:56:36,168 main INFO screen DOOMERGPT pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=False 2=True (70.0s)
Sep 13 08:58:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:58:04,450 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:08:58:04 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 08:58:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:58:14,239 main INFO screen KEBAB pass=0 dev=0.14 ins=78.91 pro=9 1a=False 1b=True 2=True (48.0s)
Sep 13 08:59:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:59:38,316 main INFO screen LMAO pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (64.6s)
Sep 13 08:59:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 08:59:39,259 main INFO screen TWICE pass=0 dev=7.55 ins=0.01 pro=43 1a=False 1b=False 2=False (65.0s)
Sep 13 09:00:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:00:39,264 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=1 1a=False 1b=False 2=True (69.7s)
Sep 13 09:00:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:00:42,530 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:00:42 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 13 09:01:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:01:55,597 main INFO screen HUMAN pass=0 dev=0.0 ins=30.35 pro=51 1a=False 1b=False 2=True (67.9s)
Sep 13 09:02:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:02:31,015 main INFO screen $WINNER pass=0 dev=0.0 ins=0.53 pro=6 1a=False 1b=False 2=False (58.6s)
Sep 13 09:02:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:02:52,643 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.7s)
Sep 13 09:03:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:03:18,761 main INFO screen EMBER pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 13 09:03:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:03:47,171 main INFO screen CTM pass=0 dev=0.0 ins=77.86 pro=24 1a=False 1b=True 2=True (53.7s)
Sep 13 09:04:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:04:01,315 main INFO screen UDOG pass=0 dev=36.33 ins=0.0 pro=4 1a=False 1b=False 2=True (60.5s)
Sep 13 09:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:04:46,734 main INFO screen Peccy pass=0 dev=0.0 ins=15.92 pro=52 1a=False 1b=False 2=True (68.6s)
Sep 13 09:05:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:05:51,716 main INFO screen HUSHFROG pass=0 dev=0.0 ins=53.2 pro=4 1a=False 1b=True 2=True (66.0s)
Sep 13 09:05:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:05:56,611 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:05:56 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 09:06:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:06:23,639 main INFO screen $DRUGS pass=0 dev=0.04 ins=0.0 pro=5 1a=False 1b=False 2=False (69.0s)
Sep 13 09:06:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:06:28,454 main INFO screen LVL6 pass=0 dev=1.72 ins=0.0 pro=8 1a=False 1b=False 2=False (55.7s)
Sep 13 09:08:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:08:26,369 main INFO screen 8647 pass=0 dev=0.0 ins=22.14 pro=34 1a=False 1b=False 2=True (61.0s)
Sep 13 09:08:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:08:52,182 main INFO screen cap pass=1 dev=0.35 ins=0.0 pro=18 1a=False 1b=False 2=False (66.7s)
Sep 13 09:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:09:17,139 main INFO screen Norman pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (57.5s)
Sep 13 09:10:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:10:44,678 main INFO screen $DRUGS pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (84.5s)
Sep 13 09:10:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:10:57,407 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:10:57 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 09:10:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:10:59,745 main INFO screen MIZOCAT pass=1 dev=1.76 ins=0.63 pro=61 1a=False 1b=False 2=False (81.6s)
Sep 13 09:11:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:11:01,523 main INFO screen NBA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (65.1s)
Sep 13 09:11:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:11:40,651 main INFO screen TEST pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=True (56.0s)
Sep 13 09:12:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:12:17,758 main INFO screen ROBINWIF pass=0 dev=0.11 ins=79.2 pro=7 1a=False 1b=False 2=True (76.2s)
Sep 13 09:12:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:12:19,016 main INFO screen SOL pass=0 dev=0.09 ins=0.0 pro=7 1a=False 1b=False 2=False (79.3s)
Sep 13 09:12:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:12:45,816 main INFO screen CASHINU pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (65.2s)
Sep 13 09:14:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:14:05,229 main INFO screen WHITBATON pass=0 dev=0.04 ins=79.27 pro=8 1a=False 1b=True 2=True (54.8s)
Sep 13 09:14:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:14:31,429 main INFO screen Sp pass=0 dev=0.7 ins=0.0 pro=5 1a=False 1b=False 2=False (71.3s)
Sep 13 09:14:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:14:33,305 main INFO screen MASCOT pass=1 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=False (67.2s)
Sep 13 09:16:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:16:05,443 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:16:05 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
Sep 13 09:16:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:16:29,538 main INFO screen McDonalds pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.3s)
Sep 13 09:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:16:33,317 main INFO screen Astrachan pass=0 dev=0.0 ins=21.12 pro=42 1a=False 1b=False 2=True (61.0s)
Sep 13 09:17:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:17:16,257 main INFO screen SCOT pass=0 dev=0.35 ins=0.0 pro=7 1a=False 1b=False 2=False (69.9s)
Sep 13 09:20:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:20:42,453 main INFO screen Speed pass=0 dev=0.71 ins=0.0 pro=4 1a=False 1b=False 2=False (66.7s)
Sep 13 09:20:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:20:48,704 main INFO screen $DRUGS pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (62.2s)
Sep 13 09:20:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:20:55,923 aiohttp.access INFO 89.42.231.200 [13/Sep/2026:09:20:55 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 13 09:21:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:21:11,698 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:21:11 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 09:22:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:22:40,819 main INFO screen Copytrador pass=0 dev=0.0 ins=20.33 pro=55 1a=False 1b=False 2=True (64.5s)
Sep 13 09:22:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:22:48,245 main INFO screen $DRUGS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.7s)
Sep 13 09:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:23:17,882 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 09:24:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:24:28,128 main INFO screen $DRUGS pass=0 dev=0.44 ins=0.0 pro=6 1a=False 1b=False 2=False (67.2s)
Sep 13 09:25:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:25:03,226 main INFO screen CTO pass=0 dev=0.0 ins=11.47 pro=68 1a=False 1b=False 2=True (73.4s)
Sep 13 09:25:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:25:12,375 main INFO screen CTM pass=0 dev=0.0 ins=79.28 pro=6 1a=False 1b=False 2=True (76.1s)
Sep 13 09:25:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:25:44,529 main INFO screen DEA pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (74.2s)
Sep 13 09:25:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:25:57,140 aiohttp.access INFO 74.82.47.3 [13/Sep/2026:09:25:57 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
Sep 13 09:25:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:25:58,169 main INFO screen CHILLBATON pass=0 dev=0.19 ins=79.2 pro=8 1a=False 1b=True 2=True (54.9s)
Sep 13 09:26:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:26:15,948 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:26:15 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 09:26:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:26:24,263 main INFO screen Pipi pass=0 dev=0.0 ins=21.66 pro=60 1a=False 1b=False 2=True (71.9s)
Sep 13 09:26:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:26:56,644 main INFO screen TWICE pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (72.1s)
Sep 13 09:27:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:27:21,887 aiohttp.access INFO 74.82.47.27 [13/Sep/2026:09:27:21 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
Sep 13 09:27:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:27:30,915 main INFO screen Claude pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (57.9s)
Sep 13 09:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:28:23,102 main INFO screen MSFT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.5s)
Sep 13 09:28:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:28:55,512 aiohttp.access INFO 74.82.47.35 [13/Sep/2026:09:28:55 +0000] "GET /?format=json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
Sep 13 09:29:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:29:06,016 main INFO screen LONGGPTCAT pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=False 2=True (68.8s)
Sep 13 09:29:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:29:06,813 aiohttp.access INFO 74.82.47.43 [13/Sep/2026:09:29:06 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
Sep 13 09:29:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:29:26,484 aiohttp.access INFO 74.82.47.3 [13/Sep/2026:09:29:26 +0000] "GET /geoserver/web/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
Sep 13 09:29:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:29:52,529 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.5s)
Sep 13 09:31:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:31:18,270 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:31:18 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T08:34:36Z
--- update 2026-09-13T08:39:35Z
--- update 2026-09-13T08:44:36Z
--- update 2026-09-13T08:50:25Z
--- update 2026-09-13T08:55:36Z
--- update 2026-09-13T09:00:41Z
--- update 2026-09-13T09:05:55Z
nieuwe code: 0a0ebf1
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: a74ba9bcc201477e9492614361eb5259
analyses gestart (f9e8e081cddf)
--- update 2026-09-13T09:10:56Z
--- update 2026-09-13T09:16:04Z
--- update 2026-09-13T09:21:10Z
--- update 2026-09-13T09:26:14Z
nieuwe code: 0a977ba
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 914aee17cb46472a9cf0adbbc20f19a7
analyses gestart (2db583c97f2a)
--- update 2026-09-13T09:31:17Z
```

## Analyses (laatste 25 regels)
```
active
09:18:06   34000 tokens, 3804605 trades, 614617 posities (50s)
09:18:08   36000 tokens, 4031422 trades, 650811 posities (52s)
09:18:11   38000 tokens, 4236869 trades, 682835 posities (55s)
09:18:14   40000 tokens, 4473723 trades, 722933 posities (57s)
09:18:16   42000 tokens, 4674096 trades, 755412 posities (60s)
09:18:19   44000 tokens, 4894073 trades, 793618 posities (63s)
09:18:22   46000 tokens, 5129561 trades, 832989 posities (66s)
09:18:25   48000 tokens, 5368411 trades, 874059 posities (69s)
09:18:28   50000 tokens, 5593189 trades, 921990 posities (71s)
09:18:29 posities: 945340 uit 5709321 trades (73s)
09:18:41 196620 wallets gerekend
09:18:42 geluk-toets
09:19:18 persistentie
09:19:21 kopieer-simulatie
09:19:44 klaar in 148s -> /opt/schaduwbot/reports/wallets.md
09:26:16 50145 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
09:26:18   ingelezen tot rowid 5717352 (19170 rijen, 19170 bruikbaar)
09:26:19 ingelezen: 19170 nieuwe trades, 19170 bruikbaar (4s)
09:27:10 1139 aankopen van gevolgde wallets geëvalueerd
09:27:24 vroege kopers: 170 voldoen nu, register 267, 20 tokens beoordeeld
09:27:37 grote spelers: saldo van 7 wallets opgehaald
09:28:53 herkomst: 40 posities gekoppeld
09:28:59 klaar in 163s -> /opt/schaduwbot/reports/ledger.md
09:30:00 S1: gezakt — toets n=5192, verkennend n=14656
09:30:00 klaar in 61s -> /opt/schaduwbot/reports/hypotheses.md
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
