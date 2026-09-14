# Schaduwbot status

- tijd: 2026-09-14 00:10:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 10 hours, 23 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.2G/38G | geheugen: 1896/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 63376, "tokens_in_memory": 7988, "msgs": 8061570, "trades": 1739125, "creates": 18561, "decode_fail": 156971, "rpc_calls": 51036, "rpc_errors": 3, "sol_usd": 99.59030134152052, "open_positions": 61, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 23:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:40:56,898 main INFO screen Heal pass=0 dev=0.0 ins=6.39 pro=69 1a=False 1b=False 2=True (66.1s)
Sep 13 23:40:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:40:59,655 main INFO screen RAVNOIR pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 13 23:41:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:41:02,018 main INFO screen LMEOW pass=0 dev=0.0 ins=0.51 pro=2 1a=False 1b=False 2=True (71.7s)
Sep 13 23:42:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:42:02,979 main INFO screen DOGGO pass=0 dev=0.0 ins=59.26 pro=68 1a=False 1b=False 2=True (63.3s)
Sep 13 23:42:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:42:03,109 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.2s)
Sep 13 23:42:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:42:06,961 main INFO screen SexySol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.9s)
Sep 13 23:42:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:42:58,326 main INFO screen TH3000 pass=0 dev=0.0 ins=25.09 pro=76 1a=False 1b=False 2=True (55.3s)
Sep 13 23:43:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:43:07,307 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.3s)
Sep 13 23:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:43:11,908 main INFO screen LMEOW pass=0 dev=78.8 ins=0.51 pro=2 1a=False 1b=False 2=True (68.8s)
Sep 13 23:44:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:44:08,335 main INFO screen SPY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.0s)
Sep 13 23:44:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:44:15,793 main INFO screen SPYNA pass=0 dev=0.0 ins=27.74 pro=32 1a=False 1b=False 2=True (68.5s)
Sep 13 23:44:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:44:17,327 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (65.4s)
Sep 13 23:44:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:44:33,350 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:44:33 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:45:10,136 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.8s)
Sep 13 23:46:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:46:04,885 main INFO screen Girlfriend pass=0 dev=0.0 ins=6.67 pro=67 1a=False 1b=False 2=True (66.0s)
Sep 13 23:46:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:46:08,860 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.2s)
Sep 13 23:47:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:47:02,704 main INFO screen PIDGE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (62.5s)
Sep 13 23:47:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:47:04,119 main INFO screen NASA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.2s)
Sep 13 23:47:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:47:49,401 main INFO screen AI pass=0 dev=98.85 ins=0.0 pro=1 1a=False 1b=False 2=True (46.7s)
Sep 13 23:48:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:48:17,667 main INFO screen mEmE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.3s)
Sep 13 23:48:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:48:19,103 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 13 23:48:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:48:55,579 main INFO screen GAS pass=0 dev=0.0 ins=18.23 pro=46 1a=False 1b=False 2=True (66.2s)
Sep 13 23:49:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:49:22,948 main INFO screen FAGMAN pass=0 dev=0.0 ins=29.77 pro=76 1a=False 1b=False 2=True (65.3s)
Sep 13 23:49:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:49:24,425 main INFO screen Copytrador pass=0 dev=0.0 ins=25.66 pro=69 1a=False 1b=False 2=True (65.3s)
Sep 13 23:49:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:49:37,169 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:49:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:50:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:50:00,096 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=6 1a=False 1b=False 2=True (64.5s)
Sep 13 23:50:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:50:26,269 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 13 23:50:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:50:28,231 main INFO screen FAGMAN pass=1 dev=0.0 ins=11.39 pro=29 1a=False 1b=False 2=False (65.3s)
Sep 13 23:51:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:51:04,007 main INFO screen DOGESHITPO pass=1 dev=0.35 ins=0.0 pro=13 1a=False 1b=False 2=False (63.9s)
Sep 13 23:51:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:51:15,926 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.7s)
Sep 13 23:51:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:51:23,445 main INFO screen $CAT pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (55.2s)
Sep 13 23:52:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:52:13,792 main INFO screen maxi pass=1 dev=0.0 ins=14.75 pro=60 1a=False 1b=False 2=False (69.8s)
Sep 13 23:52:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:52:27,673 main INFO screen ELTON pass=1 dev=0.26 ins=0.0 pro=14 1a=False 1b=False 2=False (71.7s)
Sep 13 23:52:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:52:43,419 main INFO screen coin pass=0 dev=0.0 ins=18.22 pro=60 1a=False 1b=False 2=True (67.2s)
Sep 13 23:53:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:53:25,825 main INFO screen mmrich pass=1 dev=0.35 ins=0.0 pro=11 1a=False 1b=False 2=False (72.0s)
Sep 13 23:53:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:53:37,583 main INFO screen Meme pass=0 dev=0.0 ins=24.76 pro=48 1a=False 1b=False 2=True (69.9s)
Sep 13 23:53:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:53:48,916 main INFO screen tosho pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (64.5s)
Sep 13 23:54:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:54:32,663 main INFO screen MM pass=0 dev=0.0 ins=26.21 pro=75 1a=False 1b=False 2=True (66.8s)
Sep 13 23:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:54:37,639 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.1s)
Sep 13 23:54:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:54:40,154 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:54:40 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:55:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:55:12,925 main INFO screen WHTHS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.2s)
Sep 13 23:55:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:55:24,892 main INFO screen BALL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.2s)
Sep 13 23:56:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:56:05,189 main INFO screen FLY pass=0 dev=0.0 ins=29.01 pro=74 1a=False 1b=False 2=True (62.1s)
Sep 13 23:56:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:56:10,616 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (51.1s)
Sep 13 23:56:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:56:30,845 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.9s)
Sep 13 23:57:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:57:12,701 main INFO screen mmrich pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (67.5s)
Sep 13 23:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:57:27,503 main INFO screen Nvidia pass=0 dev=0.0 ins=17.41 pro=47 1a=False 1b=False 2=True (70.4s)
Sep 13 23:57:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:57:47,674 main INFO screen PUMP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (74.0s)
Sep 13 23:58:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:58:12,697 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 13 23:58:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:58:42,882 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (75.4s)
Sep 13 23:59:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:59:03,474 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (75.8s)
Sep 13 23:59:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:59:12,774 main INFO screen ZGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (60.1s)
Sep 13 23:59:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:59:41,870 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:23:59:41 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 13 23:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 23:59:59,851 main INFO screen FORTNITE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.0s)
Sep 14 00:00:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:00:11,183 main INFO screen doge pass=0 dev=0.0 ins=29.05 pro=66 1a=False 1b=False 2=True (67.7s)
Sep 14 00:00:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:00:12,492 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (59.7s)
Sep 14 00:00:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:00:59,613 main INFO screen CHEAP pass=1 dev=0.0 ins=8.58 pro=46 1a=False 1b=False 2=False (59.8s)
Sep 14 00:01:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:01:34,510 main INFO screen BLAST UP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 14 00:01:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:01:48,397 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.6s)
Sep 14 00:02:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:02:21,617 main INFO screen BNCSNS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 14 00:02:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:02:39,815 main INFO screen ROBLOX pass=0 dev=0.77 ins=0.0 pro=4 1a=False 1b=False 2=False (65.3s)
Sep 14 00:02:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:02:43,945 main INFO screen Catamount pass=0 dev=0.0 ins=28.18 pro=39 1a=False 1b=False 2=True (54.8s)
Sep 14 00:03:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:03:30,081 main INFO screen BULLISH pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (68.5s)
Sep 14 00:03:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:03:46,542 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 14 00:04:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:04:23,555 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.7s)
Sep 14 00:04:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:04:34,804 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (49.1s)
Sep 14 00:04:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:04:42,316 main INFO screen trade pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.6s)
Sep 14 00:04:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:04:46,338 aiohttp.access INFO 193.24.211.39 [14/Sep/2026:00:04:46 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 14 00:04:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:04:47,055 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:04:47 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:05:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:05:16,576 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (53.0s)
Sep 14 00:06:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:06:36,129 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.4s)
Sep 14 00:07:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:07:10,424 main INFO screen SOL pass=0 dev=0.18 ins=0.0 pro=76 1a=False 1b=False 2=True (80.3s)
Sep 14 00:07:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:07:15,324 main INFO screen TESTS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.6s)
Sep 14 00:08:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:08:44,839 main INFO screen Flybook pass=0 dev=0.0 ins=33.71 pro=20 1a=False 1b=False 2=True (67.1s)
Sep 14 00:09:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:09:00,570 main INFO screen UBC pass=0 dev=1.74 ins=55.52 pro=25 1a=False 1b=False 2=True (76.7s)
Sep 14 00:09:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:09:04,409 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 14 00:09:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:09:44,267 main INFO screen CUCK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 14 00:10:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:16,587 main INFO screen HvS pass=0 dev=0.0 ins=0.54 pro=1 1a=False 1b=False 2=False (76.0s)
Sep 14 00:10:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:20,970 main INFO screen PIG pass=0 dev=0.0 ins=43.21 pro=71 1a=False 1b=False 2=True (76.6s)
Sep 14 00:10:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:10:23,976 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:10:23 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T22:43:17Z
Running as unit: schaduwbot-wallets.service; invocation ID: bacba8bde01940a1872493ea161ca641
analyses gestart (e28253f0c5ee)
--- update 2026-09-13T22:48:19Z
--- update 2026-09-13T22:53:31Z
--- update 2026-09-13T22:58:32Z
--- update 2026-09-13T23:03:34Z
--- update 2026-09-13T23:08:36Z
--- update 2026-09-13T23:13:55Z
--- update 2026-09-13T23:19:11Z
--- update 2026-09-13T23:24:17Z
--- update 2026-09-13T23:29:20Z
--- update 2026-09-13T23:34:26Z
--- update 2026-09-13T23:39:29Z
--- update 2026-09-13T23:44:32Z
--- update 2026-09-13T23:49:36Z
--- update 2026-09-13T23:54:39Z
--- update 2026-09-13T23:59:40Z
--- update 2026-09-14T00:04:46Z
--- update 2026-09-14T00:10:22Z
```

## Analyses (laatste 25 regels)
```
inactive
23:13:05   26000 tokens, 2714180 trades, 375056 posities (140s)
23:13:17   28000 tokens, 2910347 trades, 398449 posities (152s)
23:13:28   30000 tokens, 3111752 trades, 425877 posities (163s)
23:13:41   32000 tokens, 3340745 trades, 458038 posities (176s)
23:13:53   34000 tokens, 3553363 trades, 489464 posities (188s)
23:14:05   36000 tokens, 3751673 trades, 513567 posities (200s)
23:14:16   38000 tokens, 3925965 trades, 534663 posities (212s)
23:14:30   40000 tokens, 4152994 trades, 570806 posities (226s)
23:14:42   42000 tokens, 4348336 trades, 595664 posities (237s)
23:14:53   44000 tokens, 4548599 trades, 621351 posities (248s)
23:15:05   46000 tokens, 4751977 trades, 646323 posities (260s)
23:15:17   48000 tokens, 4947857 trades, 676731 posities (273s)
23:15:30   50000 tokens, 5152223 trades, 704551 posities (286s)
23:15:42   52000 tokens, 5327073 trades, 727800 posities (297s)
23:15:53   54000 tokens, 5528435 trades, 756055 posities (309s)
23:16:05   56000 tokens, 5741491 trades, 787436 posities (320s)
23:16:15   58000 tokens, 5949257 trades, 815855 posities (330s)
23:16:24   60000 tokens, 6158655 trades, 848573 posities (339s)
23:16:34   62000 tokens, 6378507 trades, 891082 posities (349s)
23:16:43 posities: 913444 uit 6542295 trades (361s)
23:16:54 192830 wallets gerekend
23:16:54 geluk-toets
23:17:26 persistentie
23:17:28 kopieer-simulatie
23:19:10 klaar in 508s -> /opt/schaduwbot/reports/wallets.md
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
