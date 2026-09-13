# Schaduwbot status

- tijd: 2026-09-13 12:30:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 22 hours, 43 minutes
- bot-service: active
- code-versie: 673b038
- schijf: 4.5G/38G | geheugen: 969/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 21389, "tokens_in_memory": 4152, "msgs": 1166588, "trades": 373670, "creates": 4152, "decode_fail": 48666, "rpc_calls": 11889, "rpc_errors": 1, "sol_usd": 99.69783730856372, "open_positions": 25, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 11:49:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:49:38,709 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:49:38 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 11:49:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:49:59,592 main INFO screen FLY-TRADER pass=0 dev=0.0 ins=20.82 pro=52 1a=False 1b=False 2=True (67.5s)
Sep 13 11:50:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:50:02,859 main INFO screen DECDN pass=0 dev=7.22 ins=27.16 pro=15 1a=False 1b=False 2=False (64.5s)
Sep 13 11:50:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:50:23,919 main INFO screen FLY-TRADER pass=0 dev=0.0 ins=0.43 pro=49 1a=False 1b=False 2=True (69.4s)
Sep 13 11:50:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:50:55,587 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.0s)
Sep 13 11:51:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:51:07,106 main INFO screen CAT pass=1 dev=0.0 ins=1.23 pro=49 1a=False 1b=False 2=False (64.2s)
Sep 13 11:51:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:51:35,764 main INFO screen ROBINMAN pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (64.6s)
Sep 13 11:52:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:52:48,989 main INFO screen last one pass=0 dev=1.95 ins=0.0 pro=2 1a=False 1b=False 2=False (61.3s)
Sep 13 11:53:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:53:29,802 main INFO screen OpenAI pass=0 dev=99.3 ins=0.0 pro=1 1a=False 1b=False 2=True (46.4s)
Sep 13 11:54:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:54:43,260 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:54:43 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 11:54:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:54:59,649 main INFO screen PETIX pass=0 dev=9.62 ins=23.51 pro=23 1a=False 1b=False 2=False (65.0s)
Sep 13 11:55:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:55:01,078 main INFO screen PETIX pass=1 dev=0.0 ins=1.66 pro=77 1a=False 1b=False 2=False (65.6s)
Sep 13 11:56:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:56:19,520 main INFO screen MoonDoor pass=1 dev=0.0 ins=2.1 pro=45 1a=False 1b=False 2=False (68.6s)
Sep 13 11:56:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:56:21,986 main INFO screen BITSQUIRRE pass=1 dev=0.0 ins=0.77 pro=78 1a=False 1b=False 2=False (64.8s)
Sep 13 11:57:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:57:17,662 main INFO screen BABYHOLD pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (51.8s)
Sep 13 11:57:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:57:48,603 main INFO screen 狗狗币 pass=1 dev=0.0 ins=0.0 pro=67 1a=False 1b=False 2=False (67.7s)
Sep 13 11:58:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:58:22,536 main INFO screen PMUP pass=1 dev=0.0 ins=0.2 pro=77 1a=False 1b=False 2=False (64.8s)
Sep 13 11:59:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:59:33,858 main INFO screen RISE pass=0 dev=40.31 ins=0.0 pro=4 1a=False 1b=False 2=True (82.6s)
Sep 13 11:59:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:59:35,070 main INFO screen 狗狗币 pass=1 dev=0.48 ins=12.73 pro=51 1a=False 1b=False 2=False (88.1s)
Sep 13 11:59:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:59:43,934 main INFO screen Nasbaton pass=0 dev=0.25 ins=79.06 pro=3 1a=False 1b=True 2=True (81.4s)
Sep 13 11:59:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 11:59:47,887 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:11:59:47 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 12:00:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:00:55,578 main INFO screen SOLBOT pass=1 dev=0.0 ins=2.83 pro=35 1a=False 1b=False 2=False (81.7s)
Sep 13 12:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:01:01,076 main INFO screen MAYHEM pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (86.0s)
Sep 13 12:01:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:01:05,534 main INFO screen SOLBOT pass=1 dev=0.0 ins=0.0 pro=78 1a=False 1b=False 2=False (81.6s)
Sep 13 12:01:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:01:59,539 main INFO screen PETIX pass=0 dev=10.0 ins=39.71 pro=24 1a=False 1b=True 2=True (64.0s)
Sep 13 12:02:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:02:20,543 main INFO screen SOLBOT pass=1 dev=0.0 ins=13.27 pro=68 1a=False 1b=False 2=False (79.5s)
Sep 13 12:02:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:02:29,774 main INFO screen PEPEGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=False 2=True (84.2s)
Sep 13 12:03:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:03:01,966 main INFO screen PINKMAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.4s)
Sep 13 12:03:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:03:42,241 main INFO screen TIKTOK pass=0 dev=0.0 ins=27.46 pro=64 1a=False 1b=False 2=True (81.7s)
Sep 13 12:03:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:03:47,704 main INFO screen TIKTOK pass=1 dev=0.0 ins=0.93 pro=85 1a=False 1b=False 2=False (75.1s)
Sep 13 12:04:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:04:20,438 main INFO screen FOLLOWME pass=1 dev=0.0 ins=6.64 pro=55 1a=False 1b=False 2=False (78.5s)
Sep 13 12:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:04:38,744 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.5s)
Sep 13 12:04:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:04:49,679 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:04:49 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:05:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:05:00,545 main INFO screen CKTBR pass=1 dev=0.6 ins=0.0 pro=10 1a=False 1b=False 2=False (69.5s)
Sep 13 12:06:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:06:12,838 main INFO screen $Almost pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (67.4s)
Sep 13 12:06:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:06:49,746 main INFO screen ALONGPT pass=0 dev=0.19 ins=79.12 pro=10 1a=False 1b=True 2=True (61.9s)
Sep 13 12:06:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:06:50,902 main INFO screen Apple pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.6s)
Sep 13 12:07:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:07:27,997 main INFO screen CAD pass=1 dev=0.0 ins=0.0 pro=41 1a=False 1b=False 2=False (63.4s)
Sep 13 12:08:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:08:05,173 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (75.4s)
Sep 13 12:08:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:08:30,021 main INFO screen DOGSHIT pass=1 dev=0.0 ins=0.0 pro=77 1a=False 1b=False 2=False (73.3s)
Sep 13 12:08:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:08:39,117 main INFO screen FOMO pass=0 dev=75.36 ins=0.0 pro=1 1a=False 1b=False 2=True (59.2s)
Sep 13 12:09:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:09:16,068 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 13 12:09:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:09:34,011 aiohttp.access INFO 195.182.16.23 [13/Sep/2026:12:09:34 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 13 12:09:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:09:46,122 main INFO screen McDonald's pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.8s)
Sep 13 12:09:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:09:56,571 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:09:56 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:10:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:10:38,437 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.9s)
Sep 13 12:10:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:10:56,774 main INFO screen MSSA pass=1 dev=0.0 ins=1.41 pro=75 1a=False 1b=False 2=False (69.8s)
Sep 13 12:12:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:12:37,833 main INFO screen NIVI pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (69.6s)
Sep 13 12:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:12:49,554 main INFO screen Diablo pass=1 dev=0.0 ins=1.08 pro=42 1a=False 1b=False 2=False (76.6s)
Sep 13 12:13:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:13:58,832 main INFO screen HOT pass=1 dev=0.0 ins=1.49 pro=23 1a=False 1b=False 2=False (79.4s)
Sep 13 12:14:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:14:30,608 main INFO screen HOT pass=0 dev=0.0 ins=28.81 pro=41 1a=False 1b=False 2=False (72.0s)
Sep 13 12:14:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:14:34,718 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (82.0s)
Sep 13 12:15:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:15:02,823 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:15:02 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:15:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:15:41,215 main INFO screen nrnf pass=0 dev=0.0 ins=38.03 pro=11 1a=False 1b=False 2=True (64.1s)
Sep 13 12:16:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:16:09,361 main INFO screen JOTCHUAGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (60.5s)
Sep 13 12:16:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:16:41,939 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 13 12:17:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:17:20,862 main INFO screen yee pass=1 dev=0.43 ins=9.06 pro=60 1a=False 1b=False 2=False (72.7s)
Sep 13 12:17:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:17:39,415 main INFO screen NIKOHO pass=0 dev=0.0 ins=30.18 pro=23 1a=False 1b=False 2=True (68.4s)
Sep 13 12:17:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:17:47,124 main INFO screen $FISH pass=0 dev=1.97 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 13 12:18:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:18:43,071 main INFO screen DRIPCAT pass=1 dev=0.0 ins=0.0 pro=53 1a=False 1b=False 2=False (67.1s)
Sep 13 12:19:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:19:25,869 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.0s)
Sep 13 12:19:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:19:37,098 main INFO screen HOTCOIN pass=1 dev=0.0 ins=14.45 pro=28 1a=False 1b=False 2=False (70.5s)
Sep 13 12:20:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:20:10,583 main INFO screen HOPE pass=1 dev=0.0 ins=1.46 pro=33 1a=False 1b=False 2=False (72.7s)
Sep 13 12:20:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:20:12,173 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:20:12 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:21:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:21:57,236 main INFO screen BBC pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.1s)
Sep 13 12:22:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:22:21,105 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=2 1a=False 1b=False 2=True (68.6s)
Sep 13 12:23:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:23:58,356 main INFO screen $Dude pass=0 dev=0.0 ins=0.21 pro=2 1a=False 1b=False 2=True (84.7s)
Sep 13 12:24:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:24:00,017 main INFO screen BF pass=1 dev=0.0 ins=1.82 pro=56 1a=False 1b=False 2=False (84.9s)
Sep 13 12:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:24:47,936 main INFO screen RST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (76.8s)
Sep 13 12:25:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:25:27,227 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:25:27 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 12:26:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:26:09,734 main INFO screen Almond pass=0 dev=0.0 ins=28.6 pro=73 1a=False 1b=False 2=True (76.7s)
Sep 13 12:26:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:26:11,442 main INFO screen Good pass=1 dev=0.0 ins=16.96 pro=50 1a=False 1b=False 2=False (80.2s)
Sep 13 12:26:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:26:13,433 main INFO screen musk bike pass=0 dev=0.0 ins=31.53 pro=11 1a=False 1b=False 2=True (86.4s)
Sep 13 12:27:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:27:30,337 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (80.6s)
Sep 13 12:27:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:27:32,069 main INFO screen Almond pass=0 dev=0.0 ins=23.47 pro=50 1a=False 1b=False 2=False (63.9s)
Sep 13 12:28:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:28:06,699 main INFO screen SPC pass=1 dev=0.0 ins=0.0 pro=76 1a=False 1b=False 2=False (81.9s)
Sep 13 12:28:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:28:59,180 main INFO screen werld pass=0 dev=0.0 ins=18.62 pro=64 1a=False 1b=False 2=True (83.1s)
Sep 13 12:29:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:29:37,995 main INFO screen TH3000 pass=1 dev=0.0 ins=12.06 pro=58 1a=False 1b=False 2=False (77.6s)
Sep 13 12:29:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:29:50,763 main INFO screen TripleB pass=0 dev=0.0 ins=79.27 pro=0 1a=False 1b=True 2=True (66.9s)
Sep 13 12:30:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 12:30:37,106 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:12:30:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T11:23:09Z
--- update 2026-09-13T11:28:29Z
Running as unit: schaduwbot-wallets.service; invocation ID: 8a3d763bc28340e1bd56e562391059f5
analyses gestart (2db583c97f2a)
--- update 2026-09-13T11:33:36Z
--- update 2026-09-13T11:39:14Z
--- update 2026-09-13T11:44:36Z
--- update 2026-09-13T11:49:37Z
--- update 2026-09-13T11:54:42Z
--- update 2026-09-13T11:59:46Z
--- update 2026-09-13T12:04:48Z
--- update 2026-09-13T12:09:55Z
--- update 2026-09-13T12:15:01Z
--- update 2026-09-13T12:20:10Z
nieuwe code: 673b038
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 09b0ba4bf99c4fb49d28845dfc7b0c51
analyses gestart (ac57af7920e5)
--- update 2026-09-13T12:25:26Z
--- update 2026-09-13T12:30:36Z
```

## Analyses (laatste 25 regels)
```
active
11:44:20   40000 tokens, 4454173 trades, 712125 posities (54s)
11:44:23   42000 tokens, 4675653 trades, 749350 posities (56s)
11:44:25   44000 tokens, 4894101 trades, 784035 posities (59s)
11:44:28   46000 tokens, 5115184 trades, 822333 posities (61s)
11:44:30   48000 tokens, 5346172 trades, 860100 posities (63s)
11:44:33   50000 tokens, 5586096 trades, 902004 posities (66s)
11:44:35   52000 tokens, 5788998 trades, 946100 posities (69s)
11:44:36 posities: 963682 uit 5870637 trades (71s)
11:44:49 199603 wallets gerekend
11:44:49 geluk-toets
11:45:25 persistentie
11:45:28 kopieer-simulatie
11:46:20 klaar in 175s -> /opt/schaduwbot/reports/wallets.md
12:20:12 52365 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
12:20:19   ingelezen tot rowid 5925195 (70262 rijen, 70262 bruikbaar)
12:20:20 ingelezen: 70262 nieuwe trades, 70262 bruikbaar (8s)
12:21:18 1415 aankopen van gevolgde wallets geëvalueerd
12:21:31 vroege kopers: 165 voldoen nu, register 275, 90 tokens beoordeeld
12:21:52 grote spelers: saldo van 1305 wallets opgehaald
12:22:22 herkomst: 40 posities gekoppeld
12:22:27 klaar in 136s -> /opt/schaduwbot/reports/ledger.md
12:23:29 S1: gezakt — toets n=6064, verkennend n=14656
12:23:29 klaar in 61s -> /opt/schaduwbot/reports/hypotheses.md
12:27:12 klaar in 223s -> /opt/schaduwbot/reports/lotgevallen.md
12:27:12 na-migratie: 400 paren te checken
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
