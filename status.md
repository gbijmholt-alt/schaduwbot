# Schaduwbot status

- tijd: 2026-09-13 10:36:50 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 20 hours, 49 minutes
- bot-service: active
- code-versie: 0a977ba
- schijf: 4.5G/38G | geheugen: 788/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 14563, "tokens_in_memory": 2615, "msgs": 669252, "trades": 225915, "creates": 2615, "decode_fail": 31876, "rpc_calls": 7257, "rpc_errors": 1, "sol_usd": 99.77489874974178, "open_positions": 30, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 09:47:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:47:12,785 main INFO screen HORACE pass=0 dev=0.0 ins=21.26 pro=54 1a=False 1b=False 2=True (62.6s)
Sep 13 09:47:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:47:29,848 main INFO screen PERPSPAD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.4s)
Sep 13 09:51:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:51:11,979 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 13 09:51:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:51:27,866 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:51:27 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 09:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:54:37,864 main INFO screen GIGACAT pass=1 dev=0.0 ins=14.65 pro=67 1a=False 1b=False 2=False (62.5s)
Sep 13 09:56:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:56:06,282 main INFO screen Flybook pass=0 dev=0.0 ins=31.37 pro=47 1a=False 1b=False 2=True (61.5s)
Sep 13 09:56:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:56:12,571 main INFO screen Cupsey pass=1 dev=0.0 ins=0.04 pro=25 1a=False 1b=False 2=False (50.1s)
Sep 13 09:56:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:56:29,005 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:09:56:29 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 09:56:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:56:51,057 aiohttp.access INFO 65.49.1.212 [13/Sep/2026:09:56:51 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 09:57:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:57:29,232 main INFO screen RACCOON pass=1 dev=1.76 ins=0.0 pro=57 1a=False 1b=False 2=False (61.7s)
Sep 13 09:57:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:57:54,896 main INFO screen Bulljak pass=0 dev=1.74 ins=55.73 pro=22 1a=False 1b=False 2=True (62.5s)
Sep 13 09:59:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 09:59:27,772 main INFO screen RISE pass=0 dev=40.33 ins=0.0 pro=3 1a=False 1b=False 2=False (60.7s)
Sep 13 10:01:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:01:00,890 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 13 10:01:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:01:14,049 main INFO screen e/dcc pass=0 dev=0.0 ins=27.57 pro=60 1a=False 1b=False 2=True (60.5s)
Sep 13 10:01:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:01:31,145 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:01:31 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:02:51,630 main INFO screen MIZODOG pass=1 dev=0.36 ins=0.0 pro=49 1a=False 1b=False 2=False (67.9s)
Sep 13 10:05:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:05:01,269 main INFO screen Nut pass=1 dev=0.0 ins=15.37 pro=61 1a=False 1b=False 2=False (72.2s)
Sep 13 10:05:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:05:02,733 main INFO screen BATONGPT pass=0 dev=0.04 ins=78.26 pro=7 1a=False 1b=False 2=True (72.4s)
Sep 13 10:06:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:06:23,429 main INFO screen NICESO pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (66.4s)
Sep 13 10:06:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:06:28,496 main INFO screen $BNOVA pass=0 dev=0.35 ins=0.0 pro=5 1a=False 1b=False 2=False (55.3s)
Sep 13 10:06:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:06:35,234 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:06:35 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 13 10:07:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:07:50,412 main INFO screen OFFBATON pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (54.3s)
Sep 13 10:07:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:07:58,057 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 13 10:08:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:08:56,176 main INFO screen batonpepe pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (55.3s)
Sep 13 10:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:09:13,897 main INFO screen ROBINMICHI pass=0 dev=0.11 ins=77.36 pro=31 1a=False 1b=True 2=True (58.9s)
Sep 13 10:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:11:37,155 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:11:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:13:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:13:21,784 main INFO screen STONKX pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (68.0s)
Sep 13 10:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:14:27,907 aiohttp.access INFO 204.76.203.11 [13/Sep/2026:10:14:27 +0000] "GET /api/json?tree=displayName HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 13 10:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:14:37,832 aiohttp.access INFO 204.76.203.11 [13/Sep/2026:10:14:37 +0000] "GET /cgi-bin/nas_sharing.cgi?user=messagebus&passwd=&cmd=15 HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 13 10:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:15:36,326 main INFO screen Rack pass=0 dev=0.0 ins=17.07 pro=55 1a=False 1b=False 2=True (73.4s)
Sep 13 10:16:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:16:44,961 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:16:44 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:17:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:17:09,287 main INFO screen ZDUCK pass=0 dev=0.0 ins=27.56 pro=30 1a=False 1b=False 2=True (60.9s)
Sep 13 10:17:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:17:33,451 main INFO screen 空气币 pass=0 dev=0.11 ins=0.0 pro=62 1a=False 1b=False 2=True (75.4s)
Sep 13 10:17:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:17:51,794 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.7s)
Sep 13 10:18:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:18:53,872 main INFO screen FHALES pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.0s)
Sep 13 10:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:19:35,893 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.1s)
Sep 13 10:20:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:20:30,113 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.2s)
Sep 13 10:20:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:20:45,492 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (52.6s)
Sep 13 10:21:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:21:40,405 main INFO screen CURVE pass=1 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (68.8s)
Sep 13 10:21:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:21:47,666 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:21:47 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:22:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:22:10,667 main INFO screen WOLFY pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (56.0s)
Sep 13 10:22:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:22:15,215 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.3s)
Sep 13 10:22:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:22:31,045 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.6s)
Sep 13 10:23:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:23:07,207 main INFO screen SCRVAN pass=0 dev=11.54 ins=0.0 pro=2 1a=False 1b=False 2=False (56.5s)
Sep 13 10:23:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:23:23,860 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.0s)
Sep 13 10:23:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:23:51,015 main INFO screen Ryoshi pass=1 dev=0.0 ins=1.53 pro=45 1a=False 1b=False 2=False (69.2s)
Sep 13 10:24:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:24:46,047 main INFO screen MIC pass=0 dev=0.42 ins=20.95 pro=60 1a=False 1b=False 2=True (66.6s)
Sep 13 10:25:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:25:58,596 main INFO screen JOSEPH pass=1 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=False (73.9s)
Sep 13 10:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:26:04,563 main INFO screen RICK pass=0 dev=6.1 ins=0.0 pro=6 1a=False 1b=False 2=False (72.2s)
Sep 13 10:26:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:26:48,967 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:26:48 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:27:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:27:01,893 main INFO screen RETARDGEKO pass=1 dev=0.0 ins=1.28 pro=72 1a=False 1b=False 2=False (67.4s)
Sep 13 10:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:27:41,081 main INFO screen Bulljak pass=0 dev=0.0 ins=50.44 pro=16 1a=False 1b=False 2=True (62.2s)
Sep 13 10:28:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:28:00,778 main INFO screen JuBaton pass=0 dev=0.31 ins=0.0 pro=2 1a=False 1b=False 2=False (62.4s)
Sep 13 10:28:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:28:29,404 main INFO screen EMBER pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.0s)
Sep 13 10:29:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:29:58,051 main INFO screen utility pass=0 dev=0.0 ins=18.29 pro=68 1a=False 1b=False 2=True (76.3s)
Sep 13 10:30:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:30:02,625 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (76.5s)
Sep 13 10:30:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:30:36,345 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (66.8s)
Sep 13 10:30:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:30:54,739 main INFO screen batonhouse pass=0 dev=3.18 ins=75.89 pro=1 1a=True 1b=True 2=True (56.7s)
Sep 13 10:31:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:31:21,186 main INFO screen FHALES pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.4s)
Sep 13 10:31:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:31:50,923 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:31:50 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 13 10:32:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:32:13,030 main INFO screen MIZO pass=0 dev=0.0 ins=1.72 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 13 10:32:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:32:59,912 main INFO screen CATHOOD pass=0 dev=0.11 ins=79.2 pro=8 1a=False 1b=True 2=True (58.9s)
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:34:57,067 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 10:34:57 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 10:35:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:35:03,750 main INFO screen PUSD pass=1 dev=0.0 ins=12.02 pro=58 1a=False 1b=False 2=False (111.7s)
Sep 13 10:35:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:35:19,532 main INFO screen e/dec pass=0 dev=0.0 ins=30.49 pro=84 1a=False 1b=False 2=True (126.9s)
Sep 13 10:35:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:35:32,063 main INFO screen holder  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (117.9s)
Sep 13 10:36:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:36:18,064 main INFO screen FRED pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (58.5s)
Sep 13 10:36:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:36:21,957 main INFO screen foff pass=0 dev=0.11 ins=0.0 pro=2 1a=False 1b=False 2=False (78.2s)
Sep 13 10:36:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:36:37,411 main INFO screen NinjaCat pass=0 dev=0.0 ins=18.3 pro=65 1a=False 1b=False 2=True (65.3s)
Sep 13 10:36:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 10:36:50,876 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:10:36:50 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T09:21:10Z
--- update 2026-09-13T09:26:14Z
nieuwe code: 0a977ba
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 914aee17cb46472a9cf0adbbc20f19a7
analyses gestart (2db583c97f2a)
--- update 2026-09-13T09:31:17Z
--- update 2026-09-13T09:36:23Z
--- update 2026-09-13T09:41:24Z
--- update 2026-09-13T09:46:26Z
--- update 2026-09-13T09:51:26Z
--- update 2026-09-13T09:56:27Z
--- update 2026-09-13T10:01:30Z
--- update 2026-09-13T10:06:34Z
--- update 2026-09-13T10:11:36Z
--- update 2026-09-13T10:16:43Z
--- update 2026-09-13T10:21:46Z
--- update 2026-09-13T10:26:47Z
--- update 2026-09-13T10:31:49Z
--- update 2026-09-13T10:36:49Z
```

## Analyses (laatste 25 regels)
```
inactive
09:42:07   14000 tokens, 1561073 trades, 248328 posities (19s)
09:42:09   16000 tokens, 1768685 trades, 279938 posities (21s)
09:42:12   18000 tokens, 2012157 trades, 322972 posities (24s)
09:42:15   20000 tokens, 2249230 trades, 366584 posities (27s)
09:42:18   22000 tokens, 2469849 trades, 399368 posities (30s)
09:42:21   24000 tokens, 2677236 trades, 431180 posities (33s)
09:42:24   26000 tokens, 2914563 trades, 471497 posities (36s)
09:42:27   28000 tokens, 3142623 trades, 507059 posities (39s)
09:42:29   30000 tokens, 3356830 trades, 540147 posities (42s)
09:42:32   32000 tokens, 3601467 trades, 583195 posities (45s)
09:42:35   34000 tokens, 3808823 trades, 614735 posities (47s)
09:42:37   36000 tokens, 4032618 trades, 650441 posities (50s)
09:42:40   38000 tokens, 4243396 trades, 682604 posities (52s)
09:42:43   40000 tokens, 4474588 trades, 721760 posities (55s)
09:42:45   42000 tokens, 4675975 trades, 754614 posities (57s)
09:42:48   44000 tokens, 4906666 trades, 795271 posities (60s)
09:42:51   46000 tokens, 5138255 trades, 832998 posities (63s)
09:42:53   48000 tokens, 5371937 trades, 872734 posities (66s)
09:42:57   50000 tokens, 5601720 trades, 921474 posities (69s)
09:42:58 posities: 948585 uit 5734887 trades (71s)
09:43:11 197038 wallets gerekend
09:43:12 geluk-toets
09:43:48 persistentie
09:43:51 kopieer-simulatie
09:44:15 klaar in 148s -> /opt/schaduwbot/reports/wallets.md
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
