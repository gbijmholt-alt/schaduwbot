# Schaduwbot status

- tijd: 2026-09-15 05:19:58 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 15 hours, 33 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.8G/38G | geheugen: 2249/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 168350, "tokens_in_memory": 7655, "msgs": 25682084, "trades": 5122385, "creates": 54827, "decode_fail": 437128, "rpc_calls": 146329, "rpc_errors": 13, "sol_usd": 100.69300777782627, "open_positions": 39, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 04:53:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:53:57,120 main INFO screen Horse pass=0 dev=0.0 ins=29.83 pro=63 1a=False 1b=False 2=True (65.3s)
Sep 15 04:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:00,609 main INFO screen NTDA pass=0 dev=0.0 ins=19.93 pro=1 1a=False 1b=False 2=True (63.8s)
Sep 15 04:54:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:37,215 main INFO screen INSTAR pass=0 dev=0.0 ins=20.28 pro=64 1a=False 1b=False 2=True (57.1s)
Sep 15 04:54:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:46,494 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:54:46 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 04:54:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:53,730 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (56.6s)
Sep 15 04:54:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:54:55,718 main INFO screen OPTIONS pass=0 dev=0.0 ins=56.41 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 15 04:55:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:29,296 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.1s)
Sep 15 04:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:48,840 main INFO screen WHITETYSON pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (55.1s)
Sep 15 04:55:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:55:50,253 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.5s)
Sep 15 04:56:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:26,791 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 15 04:56:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:45,478 main INFO screen NVDA pass=0 dev=0.0 ins=135.65 pro=0 1a=False 1b=False 2=True (56.6s)
Sep 15 04:56:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:56:56,489 main INFO screen LELD pass=0 dev=0.41 ins=0.15 pro=70 1a=False 1b=False 2=False (66.2s)
Sep 15 04:57:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:32,200 main INFO screen Bean pass=0 dev=0.0 ins=8.15 pro=28 1a=False 1b=False 2=False (65.4s)
Sep 15 04:57:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:52,569 main INFO screen MOon pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.1s)
Sep 15 04:57:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:57:57,108 main INFO screen Cocacola pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.6s)
Sep 15 04:58:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:58:31,203 main INFO screen HOT pass=0 dev=0.0 ins=36.85 pro=68 1a=False 1b=False 2=True (59.0s)
Sep 15 04:59:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:09,635 main INFO screen BABYSLING pass=0 dev=0.01 ins=2.36 pro=48 1a=False 1b=False 2=False (72.5s)
Sep 15 04:59:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:10,966 main INFO screen INf pass=0 dev=135.96 ins=0.0 pro=15 1a=False 1b=False 2=False (78.4s)
Sep 15 04:59:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:32,756 main INFO screen CREW pass=0 dev=0.0 ins=8.55 pro=30 1a=False 1b=False 2=False (61.6s)
Sep 15 04:59:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 04:59:50,429 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:04:59:50 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:00:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:00:09,575 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.9s)
Sep 15 05:00:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:00:12,659 main INFO screen lastwine pass=0 dev=0.0 ins=77.42 pro=8 1a=False 1b=True 2=True (61.7s)
Sep 15 05:00:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:00:30,494 main INFO screen $SCREM pass=0 dev=1.2 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 05:01:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:01:13,585 aiohttp.access INFO 45.156.128.37 [15/Sep/2026:05:01:13 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 05:01:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:01:17,702 main INFO screen V1 pass=0 dev=0.0 ins=30.8 pro=60 1a=False 1b=False 2=True (68.1s)
Sep 15 05:01:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:01:21,233 main INFO screen PD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.6s)
Sep 15 05:01:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:01:26,893 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 15 05:02:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:02:33,402 main INFO screen V1 pass=0 dev=0.0 ins=24.58 pro=53 1a=False 1b=False 2=True (75.7s)
Sep 15 05:02:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:02:34,864 main INFO screen HOT pass=0 dev=0.0 ins=35.12 pro=70 1a=False 1b=False 2=True (73.6s)
Sep 15 05:02:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:02:44,821 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (77.9s)
Sep 15 05:03:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:03:35,864 main INFO screen $ANSEM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.5s)
Sep 15 05:03:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:03:36,975 main INFO screen Mission  pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 15 05:03:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:03:39,744 aiohttp.access INFO 94.154.43.254 [15/Sep/2026:05:03:39 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 05:03:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:03:51,529 main INFO screen bigcoin pass=0 dev=0.0 ins=42.5 pro=83 1a=False 1b=False 2=True (66.7s)
Sep 15 05:04:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:04:30,356 main INFO screen wok pass=0 dev=0.0 ins=33.28 pro=25 1a=False 1b=False 2=True (53.4s)
Sep 15 05:04:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:04:40,562 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.7s)
Sep 15 05:04:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:04:50,320 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:04:50 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:05:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:05:10,221 main INFO screen FRAUD pass=0 dev=0.0 ins=430.07 pro=10 1a=False 1b=False 2=False (78.7s)
Sep 15 05:05:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:05:34,209 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (63.9s)
Sep 15 05:05:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:05:43,766 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.2s)
Sep 15 05:06:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:06:12,289 aiohttp.access INFO 54.81.128.62 [15/Sep/2026:05:06:12 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
Sep 15 05:06:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:06:28,976 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=False (78.8s)
Sep 15 05:06:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:06:54,679 main INFO screen SPLASH pass=0 dev=0.0 ins=30.68 pro=39 1a=False 1b=False 2=True (80.5s)
Sep 15 05:06:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:06:57,734 main INFO screen Rolex pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (74.0s)
Sep 15 05:07:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:07:44,846 main INFO screen TCAT pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (75.9s)
Sep 15 05:08:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:08:07,673 main INFO screen fomo pass=0 dev=0.0 ins=153.06 pro=0 1a=False 1b=False 2=True (69.9s)
Sep 15 05:08:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:08:07,895 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.2s)
Sep 15 05:08:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:08:51,499 main INFO screen bSOL pass=0 dev=0.0 ins=33.85 pro=57 1a=False 1b=False 2=True (66.7s)
Sep 15 05:09:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:09:03,301 main INFO screen GS pass=0 dev=0.0 ins=24.13 pro=28 1a=False 1b=False 2=True (55.4s)
Sep 15 05:09:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:09:11,592 main INFO screen INSTAR pass=0 dev=0.0 ins=22.03 pro=74 1a=False 1b=False 2=True (63.9s)
Sep 15 05:09:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:09:52,113 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:09:52 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:10:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:10:05,798 main INFO screen GO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (74.3s)
Sep 15 05:10:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:10:08,995 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.7s)
Sep 15 05:10:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:10:10,781 main INFO screen DP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.2s)
Sep 15 05:10:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:10:58,534 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.7s)
Sep 15 05:11:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:11:00,177 main INFO screen USMS pass=0 dev=0.0 ins=142.16 pro=1 1a=False 1b=False 2=True (51.2s)
Sep 15 05:11:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:11:10,137 main INFO screen TDOG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.4s)
Sep 15 05:12:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:12:07,062 main INFO screen SDOG pass=0 dev=0.0 ins=50.72 pro=71 1a=False 1b=False 2=True (66.9s)
Sep 15 05:12:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:12:10,553 main INFO screen GO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (72.0s)
Sep 15 05:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:12:20,486 main INFO screen America250 pass=0 dev=0.04 ins=146.27 pro=1 1a=False 1b=False 2=True (70.3s)
Sep 15 05:13:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:13:20,179 main INFO screen ishowseed pass=0 dev=0.0 ins=9.74 pro=27 1a=False 1b=False 2=False (69.6s)
Sep 15 05:13:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:13:20,211 main INFO screen STALLION pass=0 dev=0.0 ins=5.86 pro=42 1a=False 1b=False 2=False (73.1s)
Sep 15 05:13:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:13:29,937 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (69.4s)
Sep 15 05:14:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:14:29,408 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.2s)
Sep 15 05:14:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:14:29,481 main INFO screen btcchan pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 15 05:14:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:14:38,972 main INFO screen EXP pass=0 dev=0.0 ins=79.12 pro=9 1a=False 1b=False 2=True (69.0s)
Sep 15 05:14:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:14:52,033 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:14:52 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 05:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:15:36,429 main INFO screen Cocacola pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.0s)
Sep 15 05:15:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:15:39,816 main INFO screen SOL pass=0 dev=0.0 ins=3.39 pro=45 1a=False 1b=False 2=False (70.3s)
Sep 15 05:15:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:15:49,507 main INFO screen ASH pass=0 dev=0.0 ins=0.39 pro=28 1a=False 1b=False 2=False (70.5s)
Sep 15 05:16:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:16:50,457 main INFO screen SDOG pass=0 dev=0.0 ins=19.82 pro=27 1a=False 1b=False 2=False (70.6s)
Sep 15 05:16:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:16:53,314 main INFO screen NICOLASCAGE pass=0 dev=0.0 ins=29.6 pro=49 1a=False 1b=False 2=True (76.9s)
Sep 15 05:16:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:16:58,459 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 15 05:18:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:18:03,721 main INFO screen Stallions pass=0 dev=0.0 ins=21.92 pro=60 1a=False 1b=False 2=True (73.3s)
Sep 15 05:18:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:18:09,982 main INFO screen up pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (76.7s)
Sep 15 05:18:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:18:12,119 main INFO screen CAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (73.7s)
Sep 15 05:19:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:19:03,799 main INFO screen HI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.1s)
Sep 15 05:19:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:19:21,471 main INFO screen Bender pass=0 dev=0.0 ins=28.14 pro=57 1a=False 1b=False 2=True (69.4s)
Sep 15 05:19:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:19:26,115 main INFO screen SINPLERTIEMS pass=0 dev=0.0 ins=34.28 pro=28 1a=False 1b=False 2=True (76.1s)
Sep 15 05:19:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 05:19:58,511 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:05:19:58 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T03:54:12Z
Running as unit: schaduwbot-wallets.service; invocation ID: c556852febb7497c926f7c233c44f1d1
analyses gestart (96a46d7e3c26)
--- update 2026-09-15T03:59:12Z
--- update 2026-09-15T04:04:15Z
--- update 2026-09-15T04:09:16Z
--- update 2026-09-15T04:14:19Z
--- update 2026-09-15T04:19:20Z
--- update 2026-09-15T04:24:32Z
--- update 2026-09-15T04:29:35Z
--- update 2026-09-15T04:34:36Z
--- update 2026-09-15T04:39:36Z
--- update 2026-09-15T04:44:37Z
--- update 2026-09-15T04:49:40Z
--- update 2026-09-15T04:54:45Z
--- update 2026-09-15T04:59:49Z
--- update 2026-09-15T05:04:49Z
--- update 2026-09-15T05:09:51Z
--- update 2026-09-15T05:14:50Z
--- update 2026-09-15T05:19:57Z
```

## Analyses (laatste 25 regels)
```
inactive
04:37:40   38000 tokens, 3669904 trades, 439287 posities (251s)
04:37:56   40000 tokens, 3869261 trades, 465053 posities (267s)
04:38:12   42000 tokens, 4053581 trades, 487112 posities (283s)
04:38:27   44000 tokens, 4238786 trades, 509220 posities (299s)
04:38:42   46000 tokens, 4415347 trades, 529333 posities (314s)
04:38:58   48000 tokens, 4589550 trades, 549788 posities (329s)
04:39:15   50000 tokens, 4787116 trades, 574764 posities (347s)
04:39:32   52000 tokens, 4994455 trades, 600510 posities (363s)
04:39:46   54000 tokens, 5189287 trades, 624841 posities (378s)
04:40:00   56000 tokens, 5378072 trades, 652073 posities (392s)
04:40:14   58000 tokens, 5550259 trades, 672012 posities (405s)
04:40:27   60000 tokens, 5738205 trades, 695471 posities (419s)
04:40:42   62000 tokens, 5931456 trades, 717016 posities (433s)
04:40:56   64000 tokens, 6129963 trades, 746298 posities (448s)
04:41:11   66000 tokens, 6326343 trades, 770851 posities (462s)
04:41:26   68000 tokens, 6514137 trades, 794918 posities (478s)
04:41:42   70000 tokens, 6698016 trades, 817607 posities (493s)
04:41:57   72000 tokens, 6907408 trades, 843122 posities (509s)
04:42:13   74000 tokens, 7115774 trades, 877324 posities (525s)
04:42:25 posities: 894047 uit 7257996 trades (542s)
04:42:37 208926 wallets gerekend
04:42:38 geluk-toets
04:43:12 persistentie
04:43:15 kopieer-simulatie
04:45:48 klaar in 745s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
04:50:02 ijk: +6 van 7 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=140 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
04:50:02 ijk-diagnose: nieuwste migratie 3.3 min oud | migraties 15/60/240 min: 7/42/162 | al gemeten: 474
04:54:54 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=143 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
04:54:54 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 477
04:59:58 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=146 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
04:59:58 ijk-diagnose: nieuwste migratie 1.2 min oud | migraties 15/60/240 min: 7/38/156 | al gemeten: 480
05:04:58 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=149 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:04:59 ijk-diagnose: nieuwste migratie 0.7 min oud | migraties 15/60/240 min: 9/37/157 | al gemeten: 483
05:09:53 ijk: +1 van 1 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=150 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:09:54 ijk-diagnose: nieuwste migratie 3.3 min oud | migraties 15/60/240 min: 7/33/151 | al gemeten: 484
05:15:05 ijk: +5 van 5 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=155 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
05:15:06 ijk-diagnose: nieuwste migratie 1.0 min oud | migraties 15/60/240 min: 9/32/153 | al gemeten: 489
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
