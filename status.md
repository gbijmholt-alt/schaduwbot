# Schaduwbot status

- tijd: 2026-09-13 20:28:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 6 hours, 41 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.0G/38G | geheugen: 1851/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 50055, "tokens_in_memory": 7487, "msgs": 5750046, "trades": 1274652, "creates": 13704, "decode_fail": 123075, "rpc_calls": 37525, "rpc_errors": 2, "sol_usd": 101.31534981622141, "open_positions": 42, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 20:00:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:17,532 aiohttp.access INFO 204.76.203.11 [13/Sep/2026:20:00:17 +0000] "GET /api/json?tree=displayName HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 13 20:00:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:17,539 aiohttp.access INFO 204.76.203.11 [13/Sep/2026:20:00:17 +0000] "GET /cgi-bin/nas_sharing.cgi?user=messagebus&passwd=&cmd=15 HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 13 20:00:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:17,555 aiohttp.access INFO 204.76.203.11 [13/Sep/2026:20:00:17 +0000] "GET /api/json?tree=displayName HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
Sep 13 20:00:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:43,259 main INFO screen cummontitties pass=0 dev=0.0 ins=20.32 pro=65 1a=False 1b=False 2=True (75.9s)
Sep 13 20:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:50,166 main INFO screen SMACK pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (84.6s)
Sep 13 20:00:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:00:51,977 main INFO screen AGI pass=1 dev=1.64 ins=0.0 pro=10 1a=False 1b=False 2=False (81.7s)
Sep 13 20:01:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:01:32,916 aiohttp.access INFO 62.171.146.116 [13/Sep/2026:20:01:32 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 20:01:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:01:54,915 main INFO screen Taxless pass=0 dev=0.0 ins=20.29 pro=53 1a=False 1b=False 2=True (71.7s)
Sep 13 20:01:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:01:56,356 main INFO screen Taxless pass=0 dev=0.0 ins=24.6 pro=29 1a=False 1b=False 2=True (66.2s)
Sep 13 20:02:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:02:03,685 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.7s)
Sep 13 20:02:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:02:05,047 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:02:05 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:02:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:02:57,684 main INFO screen mikedyson pass=0 dev=0.0 ins=53.41 pro=42 1a=True 1b=True 2=True (62.8s)
Sep 13 20:03:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:03:07,557 main INFO screen INTELGOON pass=0 dev=35.53 ins=0.01 pro=5 1a=False 1b=False 2=True (71.2s)
Sep 13 20:03:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:03:12,158 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.5s)
Sep 13 20:03:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:03:48,097 main INFO screen COCK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.4s)
Sep 13 20:04:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:04:02,061 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.5s)
Sep 13 20:04:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:04:06,627 main INFO screen STK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.5s)
Sep 13 20:04:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:04:42,998 main INFO screen bikebull pass=0 dev=0.35 ins=78.96 pro=9 1a=False 1b=True 2=True (54.9s)
Sep 13 20:05:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:05:05,610 main INFO screen BARRON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.0s)
Sep 13 20:05:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:05:05,802 main INFO screen dedok pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.7s)
Sep 13 20:05:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:05:49,119 main INFO screen TCHAT pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (66.1s)
Sep 13 20:06:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:06:14,457 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (68.8s)
Sep 13 20:06:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:06:15,990 main INFO screen milk pass=0 dev=0.42 ins=0.0 pro=7 1a=False 1b=False 2=False (70.2s)
Sep 13 20:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:06:56,982 main INFO screen Heist pass=1 dev=0.0 ins=19.56 pro=63 1a=False 1b=False 2=False (67.9s)
Sep 13 20:07:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:07:11,644 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:07:11 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:07:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:07:12,788 main INFO screen NOCAP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.3s)
Sep 13 20:07:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:07:17,414 main INFO screen $BACK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.4s)
Sep 13 20:08:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:08:06,365 main INFO screen HIDE pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (69.4s)
Sep 13 20:08:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:08:26,189 main INFO screen CLAVICULUS pass=0 dev=0.0 ins=34.78 pro=64 1a=False 1b=False 2=True (68.8s)
Sep 13 20:08:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:08:33,642 main INFO screen SOL pass=1 dev=0.0 ins=7.08 pro=65 1a=False 1b=False 2=False (80.9s)
Sep 13 20:09:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:09:12,013 main INFO screen CEOP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 13 20:09:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:09:37,431 main INFO screen Btc pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.2s)
Sep 13 20:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:09:44,916 main INFO screen GALON pass=1 dev=2.76 ins=6.71 pro=56 1a=False 1b=False 2=False (71.3s)
Sep 13 20:10:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:10:12,234 main INFO screen NSKULL pass=0 dev=0.25 ins=0.0 pro=4 1a=False 1b=False 2=False (60.2s)
Sep 13 20:10:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:10:28,643 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.2s)
Sep 13 20:10:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:10:43,708 main INFO screen LCB pass=0 dev=1.74 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 13 20:11:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:11:16,400 main INFO screen vrl pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (64.2s)
Sep 13 20:11:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:11:58,026 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.7s)
Sep 13 20:11:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:11:59,002 main INFO screen $Flyhard pass=0 dev=0.88 ins=0.0 pro=58 1a=False 1b=False 2=True (72.1s)
Sep 13 20:12:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:12:27,355 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:12:27 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:12:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:12:27,408 main INFO screen Rabbit pass=0 dev=0.0 ins=36.29 pro=61 1a=False 1b=False 2=True (66.7s)
Sep 13 20:12:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:12:57,841 main INFO screen WEEN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.8s)
Sep 13 20:12:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:12:59,444 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.4s)
Sep 13 20:13:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:13:38,664 main INFO screen 100M pass=0 dev=0.0 ins=23.8 pro=32 1a=False 1b=False 2=True (71.3s)
Sep 13 20:14:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:14:08,109 main INFO screen Flybook pass=1 dev=0.18 ins=12.45 pro=55 1a=False 1b=False 2=False (70.3s)
Sep 13 20:14:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:14:23,355 main INFO screen ETH pass=0 dev=0.0 ins=17.62 pro=66 1a=False 1b=False 2=True (69.8s)
Sep 13 20:14:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:14:44,944 main INFO screen CHILLMAS pass=0 dev=0.0 ins=19.05 pro=51 1a=False 1b=False 2=True (66.3s)
Sep 13 20:15:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:15:20,567 main INFO screen Child pass=1 dev=0.39 ins=0.0 pro=16 1a=False 1b=False 2=False (72.5s)
Sep 13 20:15:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:15:33,612 main INFO screen BNB pass=0 dev=38.43 ins=0.0 pro=4 1a=False 1b=False 2=True (70.3s)
Sep 13 20:16:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:16:59,309 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.1s)
Sep 13 20:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:17:15,642 main INFO screen MAGACOIN pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 13 20:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:17:37,136 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:17:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:17:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:17:39,849 main INFO screen Maxq pass=0 dev=0.0 ins=48.98 pro=28 1a=False 1b=False 2=True (72.6s)
Sep 13 20:17:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:17:55,853 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 20:18:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:18:20,683 main INFO screen STACK pass=0 dev=0.0 ins=27.78 pro=79 1a=False 1b=True 2=True (65.0s)
Sep 13 20:19:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:19:01,807 main INFO screen HOODCAT pass=0 dev=0.0 ins=24.8 pro=12 1a=False 1b=False 2=False (73.1s)
Sep 13 20:19:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:19:02,569 main INFO screen MARVEL pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (65.1s)
Sep 13 20:19:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:19:35,866 main INFO screen BEETLE pass=0 dev=0.88 ins=0.0 pro=7 1a=False 1b=False 2=False (75.2s)
Sep 13 20:20:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:20:02,636 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.8s)
Sep 13 20:20:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:20:21,890 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.8s)
Sep 13 20:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:20:33,521 main INFO screen TRUBAT pass=0 dev=0.35 ins=78.96 pro=9 1a=False 1b=True 2=True (57.7s)
Sep 13 20:21:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:21:35,337 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.8s)
Sep 13 20:22:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:22:24,181 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.9s)
Sep 13 20:23:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:23:00,380 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:23:00 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 20:23:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:23:10,818 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.4s)
Sep 13 20:23:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:23:26,937 main INFO screen CHAROC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (64.8s)
Sep 13 20:23:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:23:40,438 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 13 20:24:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:24:12,308 main INFO screen DANGR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.5s)
Sep 13 20:24:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:24:20,011 main INFO screen mooncat pass=0 dev=0.17 ins=48.78 pro=26 1a=False 1b=False 2=True (53.1s)
Sep 13 20:24:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:24:50,966 main INFO screen COOKED pass=0 dev=0.45 ins=0.0 pro=5 1a=False 1b=False 2=False (70.5s)
Sep 13 20:25:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:25:27,080 main INFO screen PUMPNINA pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (74.8s)
Sep 13 20:25:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:25:36,851 main INFO screen BNB pass=1 dev=0.0 ins=0.0 pro=50 1a=False 1b=False 2=False (76.8s)
Sep 13 20:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:26:04,592 main INFO screen AIWHORE pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (73.6s)
Sep 13 20:26:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:26:41,344 main INFO screen LTC pass=0 dev=0.03 ins=8.46 pro=67 1a=False 1b=False 2=True (64.5s)
Sep 13 20:26:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:26:42,747 main INFO screen Chinese pass=1 dev=0.0 ins=9.55 pro=43 1a=False 1b=False 2=False (75.7s)
Sep 13 20:27:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:27:07,272 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.7s)
Sep 13 20:27:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:27:53,321 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.0s)
Sep 13 20:27:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:27:54,122 main INFO screen LMAO pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (71.4s)
Sep 13 20:28:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:28:06,677 main INFO screen LaMisery pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 13 20:28:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 20:28:23,373 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:20:28:23 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T19:09:35Z
--- update 2026-09-13T19:14:36Z
--- update 2026-09-13T19:19:37Z
--- update 2026-09-13T19:24:40Z
--- update 2026-09-13T19:30:00Z
--- update 2026-09-13T19:35:01Z
--- update 2026-09-13T19:40:13Z
--- update 2026-09-13T19:45:36Z
--- update 2026-09-13T19:51:12Z
--- update 2026-09-13T19:56:36Z
--- update 2026-09-13T20:02:04Z
Running as unit: schaduwbot-wallets.service; invocation ID: 2dbb790ea75240b38c7992bc29ec65e9
analyses gestart (87dd80a5c10e)
--- update 2026-09-13T20:07:10Z
nieuwe code: 69b3f7f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-13T20:12:26Z
--- update 2026-09-13T20:17:36Z
--- update 2026-09-13T20:22:59Z
--- update 2026-09-13T20:28:22Z
```

## Analyses (laatste 25 regels)
```
active
20:04:16 vroege kopers: 198 voldoen nu, register 333, 326 tokens beoordeeld
20:04:39 grote spelers: saldo van 1286 wallets opgehaald
20:05:01 herkomst: 40 posities gekoppeld
20:05:08 klaar in 184s -> /opt/schaduwbot/reports/ledger.md
20:09:54 S1: gezakt — toets n=10238, verkennend n=14656
20:09:54 klaar in 285s -> /opt/schaduwbot/reports/hypotheses.md
20:09:54 probe: 150 transacties ophalen
20:13:25 poolveld: 21 pools bekeken, 0 te gaan -> vastgesteld @43
20:14:36 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
20:14:36 prijsijk: n=30 -> mediane afwijking 100% boven 25%
20:14:37 na-migratie: 100 paren te checken
20:16:51 na-migratie: 89 paren, 20 prijzen
20:21:32 gemigreerde koersen: 96 gedaan, 1846 te gaan
20:21:32 klaar (697 rpc-calls, 50 fouten)
20:26:39 klaar in 306s -> /opt/schaduwbot/reports/lotgevallen.md
20:26:55   2000 nieuwe tokens doorgerekend
20:27:15 klaar in 37s: 35536 tokens, 2750 nieuw -> /opt/schaduwbot/reports/video_replay.md
20:27:16 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-10 20:27 UTC
20:27:18 86893 tokens geladen
20:27:31   2000 tokens, 201782 trades, 26495 posities (13s)
20:27:40   4000 tokens, 432303 trades, 63763 posities (22s)
20:27:48   6000 tokens, 639244 trades, 91060 posities (30s)
20:27:56   8000 tokens, 844227 trades, 120942 posities (38s)
20:28:04   10000 tokens, 1054093 trades, 151478 posities (46s)
20:28:14   12000 tokens, 1272977 trades, 180280 posities (56s)
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
