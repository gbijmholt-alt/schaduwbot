# Schaduwbot status

- tijd: 2026-09-15 08:30:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 18 hours, 43 minutes
- bot-service: active
- code-versie: a8d6b4f
- schijf: 7.0G/38G | geheugen: 2439/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 179789, "tokens_in_memory": 6272, "msgs": 26644181, "trades": 5417678, "creates": 57802, "decode_fail": 455230, "rpc_calls": 157894, "rpc_errors": 13, "sol_usd": 100.24453245753786, "open_positions": 57, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 08:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:06:56,131 main INFO screen tySON pass=0 dev=0.0 ins=25.24 pro=69 1a=False 1b=False 2=True (74.4s)
Sep 15 08:07:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:07:10,881 main INFO screen Claude pass=0 dev=0.0 ins=20.31 pro=16 1a=False 1b=False 2=False (78.7s)
Sep 15 08:07:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:07:37,305 main INFO screen hi pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 15 08:08:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:08:09,112 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (73.0s)
Sep 15 08:08:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:08:15,876 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (65.0s)
Sep 15 08:08:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:08:49,091 main INFO screen AD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.8s)
Sep 15 08:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:09:13,128 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.0s)
Sep 15 08:09:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:09:21,316 main INFO screen JOIDS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.4s)
Sep 15 08:09:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:09:37,379 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:09:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:10:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:10:09,725 main INFO screen Validate pass=0 dev=1.87 ins=31.17 pro=77 1a=False 1b=False 2=True (80.6s)
Sep 15 08:10:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:10:15,444 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (62.3s)
Sep 15 08:10:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:10:15,498 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (54.2s)
Sep 15 08:10:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:10:32,956 aiohttp.access INFO 94.154.43.254 [15/Sep/2026:08:10:32 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:11:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:11:16,785 main INFO screen MEOWERO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.1s)
Sep 15 08:11:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:11:21,915 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.4s)
Sep 15 08:11:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:11:29,090 main INFO screen Apple pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.6s)
Sep 15 08:12:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:12:35,077 main INFO screen Validate pass=0 dev=0.0 ins=0.0 pro=31 1a=False 1b=False 2=False (78.3s)
Sep 15 08:12:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:12:37,149 main INFO screen HBC pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (75.2s)
Sep 15 08:12:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:12:45,611 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.5s)
Sep 15 08:13:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:13:43,038 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.9s)
Sep 15 08:13:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:13:44,129 main INFO screen POOPTYSON pass=0 dev=0.04 ins=79.27 pro=3 1a=False 1b=True 2=True (69.1s)
Sep 15 08:14:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:03,695 main INFO screen 6 pass=0 dev=0.23 ins=0.0 pro=13 1a=False 1b=False 2=False (78.1s)
Sep 15 08:14:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:40,837 main INFO screen WICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.8s)
Sep 15 08:14:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:47,541 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:47 +0000] "GET / HTTP/1.0" 404 174 "-" "-"
Sep 15 08:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:48,208 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:48 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
Sep 15 08:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:48,464 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:48 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
Sep 15 08:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:48,464 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:48 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:48,468 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:48 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
Sep 15 08:14:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:48,946 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:48 +0000] "GET /favicon.png HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:14:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:49,517 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:49 +0000] "GET /favicon.svg HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:14:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:50,608 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:50 +0000] "GET /apple-touch-icon.png HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:14:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:50,847 aiohttp.access INFO 159.200.240.18 [15/Sep/2026:08:14:50 +0000] "GET /apple-touch-icon-precomposed.png HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 08:14:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:50,895 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 15 08:14:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:57,614 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.9s)
Sep 15 08:14:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:14:59,595 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:14:59 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:15:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:15:41,848 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.0s)
Sep 15 08:16:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:16:04,709 main INFO screen POKEMON pass=0 dev=0.0 ins=93.84 pro=7 1a=False 1b=False 2=True (73.8s)
Sep 15 08:16:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:16:13,382 main INFO screen DERPCAT pass=0 dev=0.0 ins=33.29 pro=73 1a=False 1b=False 2=True (75.8s)
Sep 15 08:16:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:16:46,030 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.2s)
Sep 15 08:17:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:17:12,429 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.7s)
Sep 15 08:17:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:17:12,506 main INFO screen TraderFly pass=0 dev=0.0 ins=31.87 pro=60 1a=False 1b=False 2=True (59.1s)
Sep 15 08:17:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:17:54,113 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (68.1s)
Sep 15 08:18:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:18:27,489 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (75.1s)
Sep 15 08:18:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:18:29,892 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (77.4s)
Sep 15 08:19:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:19:03,214 main INFO screen flare pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.1s)
Sep 15 08:19:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:19:42,617 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (72.7s)
Sep 15 08:19:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:19:44,746 main INFO screen taC pass=0 dev=0.0 ins=16.51 pro=57 1a=False 1b=False 2=False (77.3s)
Sep 15 08:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:20:18,014 main INFO screen taC pass=0 dev=0.0 ins=13.68 pro=54 1a=False 1b=False 2=False (74.8s)
Sep 15 08:20:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:20:19,750 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:20:19 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:20:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:20:54,520 main INFO screen Bender pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (69.8s)
Sep 15 08:20:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:20:55,022 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.4s)
Sep 15 08:21:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:21:20,223 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 15 08:21:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:21:47,142 main INFO screen Pcash pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.6s)
Sep 15 08:21:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:21:50,650 main INFO screen ONLYUP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (55.6s)
Sep 15 08:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:22:17,845 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 08:22:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:22:48,842 main INFO screen CATEBATON pass=0 dev=0.0 ins=79.24 pro=3 1a=False 1b=True 2=True (61.7s)
Sep 15 08:22:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:22:54,189 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 15 08:23:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:23:30,584 main INFO screen keycat pass=0 dev=0.0 ins=28.26 pro=66 1a=False 1b=False 2=False (72.7s)
Sep 15 08:24:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:24:06,319 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.1s)
Sep 15 08:24:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:24:06,919 main INFO screen ANSIM pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (78.1s)
Sep 15 08:24:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:24:36,261 main INFO screen STANDARD pass=0 dev=0.0 ins=79.13 pro=5 1a=False 1b=True 2=True (65.7s)
Sep 15 08:25:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:25:11,786 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.5s)
Sep 15 08:25:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:25:12,294 main INFO screen BREAK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.4s)
Sep 15 08:25:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:25:29,513 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:25:29 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:25:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:25:44,748 main INFO screen にゃご pass=0 dev=0.0 ins=16.64 pro=30 1a=False 1b=False 2=False (68.5s)
Sep 15 08:26:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:26:17,999 main INFO screen Meta pass=0 dev=0.0 ins=164.43 pro=1 1a=False 1b=False 2=True (65.7s)
Sep 15 08:26:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:26:21,956 main INFO screen taC pass=0 dev=0.0 ins=31.66 pro=82 1a=False 1b=False 2=True (70.2s)
Sep 15 08:26:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:26:50,392 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (65.6s)
Sep 15 08:27:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:27:24,098 main INFO screen BKS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.1s)
Sep 15 08:27:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:27:31,204 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:27:31 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
Sep 15 08:27:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:27:31,490 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:27:31 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 15 08:27:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:27:39,288 main INFO screen PumpFly pass=0 dev=0.0 ins=33.6 pro=64 1a=False 1b=False 2=True (77.3s)
Sep 15 08:27:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:27:48,071 main INFO screen NEWXMR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 08:28:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:28:26,244 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.1s)
Sep 15 08:28:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:28:59,180 main INFO screen DOG pass=0 dev=0.0 ins=7.73 pro=74 1a=False 1b=False 2=False (79.9s)
Sep 15 08:29:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:29:00,719 main INFO screen PumP pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (72.6s)
Sep 15 08:29:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:29:31,333 main INFO screen 21312412eq pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.1s)
Sep 15 08:30:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:30:05,069 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 15 08:30:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:30:10,571 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.8s)
Sep 15 08:30:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:30:37,097 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:30:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T07:12:19Z
--- update 2026-09-15T07:17:36Z
--- update 2026-09-15T07:23:10Z
--- update 2026-09-15T07:28:19Z
--- update 2026-09-15T07:33:28Z
--- update 2026-09-15T07:38:36Z
--- update 2026-09-15T07:43:52Z
Running as unit: schaduwbot-wallets.service; invocation ID: 490b6a2e509d44eea38db760fa673dd3
analyses gestart (ef01904db983)
--- update 2026-09-15T07:48:55Z
nieuwe code: a8d6b4f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T07:53:56Z
--- update 2026-09-15T07:59:05Z
--- update 2026-09-15T08:04:22Z
--- update 2026-09-15T08:09:36Z
--- update 2026-09-15T08:14:58Z
--- update 2026-09-15T08:20:18Z
--- update 2026-09-15T08:25:27Z
--- update 2026-09-15T08:30:35Z
```

## Analyses (laatste 25 regels)
```
active
08:25:22   82000 nieuwe tokens doorgerekend
08:25:31   84000 nieuwe tokens doorgerekend
08:25:41   86000 nieuwe tokens doorgerekend
08:25:51   88000 nieuwe tokens doorgerekend
08:26:01   90000 nieuwe tokens doorgerekend
08:26:52 klaar in 466s: 69648 tokens, 90036 nieuw -> /opt/schaduwbot/reports/video_replay.md
08:26:53 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-12 08:26 UTC
08:26:59 130941 tokens geladen
08:27:15   2000 tokens, 176934 trades, 18025 posities (16s)
08:27:30   4000 tokens, 392319 trades, 50374 posities (31s)
08:27:41   6000 tokens, 588180 trades, 73333 posities (43s)
08:27:52   8000 tokens, 756796 trades, 88094 posities (53s)
08:28:03   10000 tokens, 946611 trades, 109894 posities (64s)
08:28:15   12000 tokens, 1151396 trades, 139740 posities (76s)
08:28:27   14000 tokens, 1354506 trades, 164430 posities (88s)
08:28:39   16000 tokens, 1546247 trades, 184917 posities (100s)
08:28:51   18000 tokens, 1742659 trades, 209167 posities (113s)
08:29:03   20000 tokens, 1927633 trades, 229108 posities (124s)
08:29:14   22000 tokens, 2118447 trades, 249689 posities (135s)
08:29:27   24000 tokens, 2339224 trades, 279203 posities (148s)
08:29:40   26000 tokens, 2552931 trades, 307090 posities (161s)
08:29:53   28000 tokens, 2737912 trades, 330683 posities (174s)
08:30:04   30000 tokens, 2918474 trades, 352610 posities (186s)
08:30:17   32000 tokens, 3117456 trades, 378048 posities (198s)
08:30:29   34000 tokens, 3300957 trades, 398500 posities (211s)
```

## IJking poolkoers (laatste 12 regels)
```
07:17:48 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=205 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:17:48 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 11/42/161 | al gemeten: 558
07:23:19 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=208 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:23:19 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/40/161 | al gemeten: 561
07:28:25 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=210 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:28:25 ijk-diagnose: nieuwste migratie 3.4 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 563
07:33:31 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=211 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:33:31 ijk-diagnose: nieuwste migratie 4.8 min oud | migraties 15/60/240 min: 6/37/159 | al gemeten: 564
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
07:44:15 ijk: +2 van 2 kandidaten (5 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=216 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:44:16 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 5/32/158 | al gemeten: 569
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
