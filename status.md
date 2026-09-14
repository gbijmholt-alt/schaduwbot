# Schaduwbot status

- tijd: 2026-09-14 07:27:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 17 hours, 40 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.5G/38G | geheugen: 1910/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 89609, "tokens_in_memory": 5293, "msgs": 11473731, "trades": 2436656, "creates": 25365, "decode_fail": 208964, "rpc_calls": 72092, "rpc_errors": 6, "sol_usd": 101.53681693933981, "open_positions": 45, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 06:38:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:38:54,212 aiohttp.access INFO 65.49.1.160 [14/Sep/2026:06:38:54 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
Sep 14 06:39:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:39:13,797 aiohttp.access INFO 65.49.1.152 [14/Sep/2026:06:39:13 +0000] "GET /geoserver/web/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0"
Sep 14 06:39:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:39:36,073 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:06:39:36 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 06:40:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:40:54,907 main INFO screen BetOnBlak pass=0 dev=0.29 ins=0.0 pro=4 1a=False 1b=False 2=False (62.9s)
Sep 14 06:42:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:42:01,477 main INFO screen GS pass=1 dev=0.0 ins=6.87 pro=54 1a=False 1b=False 2=False (62.8s)
Sep 14 06:42:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:42:37,590 main INFO screen RISE pass=0 dev=39.14 ins=0.0 pro=10 1a=False 1b=False 2=False (65.0s)
Sep 14 06:43:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:43:31,392 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.4s)
Sep 14 06:44:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:44:04,664 main INFO screen Etcamah pass=0 dev=0.0 ins=0.23 pro=27 1a=False 1b=False 2=True (61.6s)
Sep 14 06:44:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:44:37,192 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:06:44:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 06:45:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:45:06,799 main INFO screen 🫏 pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (63.4s)
Sep 14 06:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:45:10,271 main INFO screen WouldBull pass=0 dev=0.0 ins=56.41 pro=14 1a=False 1b=False 2=True (59.7s)
Sep 14 06:45:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:45:34,932 main INFO screen sol pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (50.5s)
Sep 14 06:45:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:45:59,604 main INFO screen rushver pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (52.8s)
Sep 14 06:46:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:46:09,026 main INFO screen WouldBull pass=0 dev=0.0 ins=56.23 pro=10 1a=False 1b=False 2=True (48.4s)
Sep 14 06:46:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:46:41,265 main INFO screen Etcamah pass=1 dev=0.0 ins=8.89 pro=58 1a=False 1b=False 2=False (66.3s)
Sep 14 06:47:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:47:03,857 main INFO screen DOOROC pass=1 dev=0.05 ins=0.0 pro=11 1a=False 1b=False 2=False (64.3s)
Sep 14 06:47:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:47:20,942 main INFO screen coded pass=0 dev=0.0 ins=22.72 pro=20 1a=False 1b=False 2=True (71.9s)
Sep 14 06:47:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:47:47,110 main INFO screen CTO pass=0 dev=0.0 ins=20.83 pro=67 1a=False 1b=False 2=True (65.8s)
Sep 14 06:47:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:47:57,586 main INFO screen Solana pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.7s)
Sep 14 06:48:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:48:11,670 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.7s)
Sep 14 06:48:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:48:34,991 main INFO screen Anthropic pass=0 dev=99.21 ins=0.0 pro=1 1a=False 1b=False 2=True (47.9s)
Sep 14 06:48:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:48:47,858 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 14 06:50:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:50:14,058 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:06:50:14 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 06:50:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:50:20,786 main INFO screen wontv pass=0 dev=1.15 ins=0.0 pro=4 1a=False 1b=False 2=False (59.5s)
Sep 14 06:51:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:51:08,922 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.2s)
Sep 14 06:51:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:51:39,328 main INFO screen TOM pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (52.9s)
Sep 14 06:52:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:52:03,324 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 14 06:52:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:52:23,471 main INFO screen Pocchi pass=0 dev=0.0 ins=20.33 pro=62 1a=False 1b=False 2=True (64.8s)
Sep 14 06:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:52:34,348 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (55.0s)
Sep 14 06:53:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:53:29,873 main INFO screen eventin pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (68.3s)
Sep 14 06:53:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:53:32,408 main INFO screen RICH pass=0 dev=0.0 ins=34.24 pro=71 1a=False 1b=False 2=True (67.2s)
Sep 14 06:54:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:54:14,239 main INFO screen baton pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.4s)
Sep 14 06:54:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:54:41,462 main INFO screen NAKEDYAHU pass=0 dev=0.0 ins=30.5 pro=36 1a=True 1b=False 2=True (49.6s)
Sep 14 06:54:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:54:52,166 main INFO screen fomo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.9s)
Sep 14 06:55:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:55:04,240 main INFO screen GORPCAT pass=0 dev=0.04 ins=79.18 pro=10 1a=False 1b=True 2=True (50.0s)
Sep 14 06:55:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:55:30,903 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.4s)
Sep 14 06:55:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:55:37,185 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:06:55:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 06:55:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:55:40,442 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.0s)
Sep 14 06:56:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:56:06,937 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.2s)
Sep 14 06:56:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:56:39,237 main INFO screen gateny pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (51.7s)
Sep 14 06:57:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:57:15,931 main INFO screen Boogley pass=0 dev=0.0 ins=29.69 pro=58 1a=False 1b=False 2=True (62.7s)
Sep 14 06:58:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:58:13,500 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 14 06:58:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 06:58:47,111 main INFO screen tothemoon pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.8s)
Sep 14 07:00:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:00:04,826 main INFO screen chillbike pass=0 dev=0.17 ins=77.5 pro=9 1a=False 1b=True 2=True (53.5s)
Sep 14 07:01:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:01:09,712 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:01:09 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:01:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:01:27,775 main INFO screen MacCoin pass=0 dev=0.0 ins=20.77 pro=64 1a=False 1b=False 2=True (67.0s)
Sep 14 07:01:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:01:33,256 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.5s)
Sep 14 07:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:02:51,679 main INFO screen Bibendum pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 14 07:03:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:03:42,993 main INFO screen Bob pass=1 dev=0.0 ins=1.28 pro=71 1a=False 1b=False 2=False (71.6s)
Sep 14 07:04:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:04:25,908 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.8s)
Sep 14 07:06:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:06:24,702 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:06:24 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:08:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:08:40,405 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 14 07:09:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:09:54,684 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.1s)
Sep 14 07:09:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:09:59,716 aiohttp.access INFO 89.42.231.200 [14/Sep/2026:07:09:59 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 14 07:10:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:10:24,023 main INFO screen mak pass=0 dev=0.06 ins=0.0 pro=8 1a=False 1b=False 2=False (71.0s)
Sep 14 07:11:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:11:31,101 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:11:31 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 07:11:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:11:41,176 main INFO screen Blondboob pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.1s)
Sep 14 07:12:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:12:43,615 main INFO screen TD pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (67.1s)
Sep 14 07:14:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:14:00,809 main INFO screen mak pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 14 07:15:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:15:42,126 main INFO screen NOVO pass=0 dev=0.0 ins=9.74 pro=10 1a=False 1b=False 2=False (45.1s)
Sep 14 07:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:16:37,265 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:16:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 07:17:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:17:39,244 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.4s)
Sep 14 07:18:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:18:29,429 main INFO screen TRUCE pass=0 dev=0.0 ins=30.07 pro=59 1a=False 1b=False 2=True (74.8s)
Sep 14 07:18:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:18:31,093 main INFO screen IBM pass=1 dev=0.0 ins=9.98 pro=55 1a=False 1b=False 2=False (71.5s)
Sep 14 07:19:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:19:30,712 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (70.3s)
Sep 14 07:20:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:08,129 main INFO screen BRONTO pass=0 dev=0.11 ins=77.5 pro=9 1a=False 1b=True 2=True (63.2s)
Sep 14 07:20:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:12,405 main INFO screen GMGNGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.1s)
Sep 14 07:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:20:33,832 main INFO screen BC pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.1s)
Sep 14 07:21:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:13,780 main INFO screen Girls pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (60.6s)
Sep 14 07:21:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:22,943 main INFO screen Solana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.9s)
Sep 14 07:21:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:21:55,252 main INFO screen VISA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (61.3s)
Sep 14 07:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:22:17,221 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:22:17 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 14 07:22:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:22:20,144 main INFO screen ai pass=0 dev=0.0 ins=18.15 pro=61 1a=False 1b=False 2=True (61.6s)
Sep 14 07:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:17,309 main INFO screen mak pass=1 dev=0.47 ins=0.0 pro=14 1a=False 1b=False 2=False (85.1s)
Sep 14 07:23:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:23,057 main INFO screen Rabbit pass=1 dev=0.0 ins=0.0 pro=76 1a=False 1b=False 2=False (76.6s)
Sep 14 07:23:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:23:41,889 main INFO screen Solana pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.0s)
Sep 14 07:24:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:24:11,353 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.0s)
Sep 14 07:25:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:25:49,919 main INFO screen CATZ pass=0 dev=0.04 ins=77.78 pro=9 1a=False 1b=True 2=True (53.8s)
Sep 14 07:26:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:26:17,217 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.4s)
Sep 14 07:27:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 07:27:37,248 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:07:27:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T05:57:36Z
--- update 2026-09-14T06:02:54Z
nieuwe code: 7a1ec62
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T06:08:05Z
--- update 2026-09-14T06:13:09Z
--- update 2026-09-14T06:18:36Z
--- update 2026-09-14T06:24:02Z
--- update 2026-09-14T06:29:09Z
--- update 2026-09-14T06:34:12Z
--- update 2026-09-14T06:39:34Z
--- update 2026-09-14T06:44:36Z
--- update 2026-09-14T06:50:12Z
--- update 2026-09-14T06:55:36Z
--- update 2026-09-14T07:01:08Z
--- update 2026-09-14T07:06:23Z
--- update 2026-09-14T07:11:29Z
--- update 2026-09-14T07:16:36Z
--- update 2026-09-14T07:22:16Z
--- update 2026-09-14T07:27:36Z
```

## Analyses (laatste 25 regels)
```
inactive
06:09:53   32000 tokens, 3225406 trades, 410420 posities (215s)
06:10:08   34000 tokens, 3436286 trades, 439217 posities (230s)
06:10:22   36000 tokens, 3657699 trades, 467459 posities (244s)
06:10:36   38000 tokens, 3848415 trades, 492446 posities (258s)
06:10:50   40000 tokens, 4037066 trades, 511931 posities (272s)
06:11:04   42000 tokens, 4220009 trades, 533937 posities (286s)
06:11:20   44000 tokens, 4437887 trades, 566538 posities (302s)
06:11:35   46000 tokens, 4627969 trades, 588174 posities (317s)
06:11:49   48000 tokens, 4823921 trades, 611243 posities (331s)
06:12:04   50000 tokens, 5025358 trades, 633953 posities (346s)
06:12:19   52000 tokens, 5206708 trades, 656081 posities (361s)
06:12:33   54000 tokens, 5407559 trades, 682492 posities (375s)
06:12:46   56000 tokens, 5583807 trades, 703011 posities (388s)
06:13:00   58000 tokens, 5780148 trades, 728335 posities (402s)
06:13:13   60000 tokens, 5970450 trades, 755769 posities (415s)
06:13:27   62000 tokens, 6193165 trades, 786012 posities (429s)
06:13:40   64000 tokens, 6391675 trades, 811172 posities (442s)
06:13:53   66000 tokens, 6594000 trades, 838935 posities (455s)
06:14:07   68000 tokens, 6800066 trades, 877664 posities (469s)
06:14:17 posities: 897901 uit 6953211 trades (483s)
06:14:30 194532 wallets gerekend
06:14:30 geluk-toets
06:15:05 persistentie
06:15:08 kopieer-simulatie
06:17:04 klaar in 650s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
06:29:10 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:34:13 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:39:35 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:44:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:50:13 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
06:55:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:01:09 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:06:24 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:11:30 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:16:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:22:16 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
07:27:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
