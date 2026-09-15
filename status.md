# Schaduwbot status

- tijd: 2026-09-15 16:13:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 2 hours, 26 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.3G/38G | geheugen: 3582/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 207554, "tokens_in_memory": 8212, "msgs": 30319967, "trades": 6374775, "creates": 67833, "decode_fail": 540258, "rpc_calls": 185765, "rpc_errors": 15, "sol_usd": 98.86607075552196, "open_positions": 74, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 15:49:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:49:35,736 main INFO screen AIRFROG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (48.3s)
Sep 15 15:49:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:49:58,370 main INFO screen BOT pass=0 dev=0.0 ins=24.62 pro=0 1a=False 1b=False 2=False (62.5s)
Sep 15 15:50:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:50:01,726 main INFO screen AOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (48.1s)
Sep 15 15:50:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:50:21,982 main INFO screen flyfan pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (46.2s)
Sep 15 15:51:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:03,606 main INFO screen Etcamah pass=0 dev=0.0 ins=11.09 pro=44 1a=False 1b=False 2=False (61.9s)
Sep 15 15:51:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:05,606 main INFO screen BRRR pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (67.2s)
Sep 15 15:51:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:16,281 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (54.3s)
Sep 15 15:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:54,438 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.8s)
Sep 15 15:51:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:51:59,218 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.6s)
Sep 15 15:52:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:07,362 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (51.1s)
Sep 15 15:52:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:44,688 main INFO screen NTDA pass=0 dev=42.92 ins=0.0 pro=1 1a=False 1b=False 2=True (50.2s)
Sep 15 15:52:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:52:45,404 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:52:45 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 15 15:53:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:53:07,716 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (68.5s)
Sep 15 15:53:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:53:09,117 main INFO screen HOAX pass=0 dev=0.0 ins=29.65 pro=40 1a=False 1b=False 2=False (61.8s)
Sep 15 15:53:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:53:37,921 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.2s)
Sep 15 15:54:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:54:10,017 main INFO screen Cp. pass=0 dev=0.0 ins=47.54 pro=46 1a=False 1b=False 2=True (62.3s)
Sep 15 15:54:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:54:11,963 main INFO screen SOLDOG pass=0 dev=0.0 ins=19.22 pro=76 1a=False 1b=False 2=True (62.8s)
Sep 15 15:54:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:54:30,631 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.7s)
Sep 15 15:54:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:54:57,191 main INFO screen SOLDOG pass=0 dev=0.0 ins=17.07 pro=21 1a=False 1b=False 2=True (47.2s)
Sep 15 15:55:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:55:01,144 main INFO screen RMB pass=0 dev=0.0 ins=33.26 pro=44 1a=False 1b=False 2=True (49.2s)
Sep 15 15:55:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:55:21,305 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (50.7s)
Sep 15 15:55:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:55:46,019 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:15:55:46 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 15:55:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:55:47,157 main INFO screen PPLC pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (50.0s)
Sep 15 15:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:56:01,970 main INFO screen CLIT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.8s)
Sep 15 15:56:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:56:11,459 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.2s)
Sep 15 15:56:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:56:51,659 main INFO screen STAMPY pass=0 dev=0.41 ins=6.64 pro=83 1a=False 1b=False 2=True (64.5s)
Sep 15 15:56:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:56:56,157 main INFO screen SOLDOG pass=0 dev=0.0 ins=23.57 pro=0 1a=False 1b=False 2=False (54.2s)
Sep 15 15:56:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:56:57,760 main INFO screen Lewis pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (46.3s)
Sep 15 15:57:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:57:46,533 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:57:46 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:57:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:57:48,504 main INFO screen stinkyair pass=0 dev=0.0 ins=31.68 pro=12 1a=True 1b=False 2=True (56.8s)
Sep 15 15:57:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:57:59,876 main INFO screen RICH pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=False (63.7s)
Sep 15 15:58:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:58:01,660 main INFO screen ncoin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.9s)
Sep 15 15:58:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:58:42,145 main INFO screen GoldenDome pass=0 dev=0.0 ins=45.56 pro=23 1a=True 1b=False 2=True (53.6s)
Sep 15 15:59:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:59:03,115 main INFO screen Lewis pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (63.2s)
Sep 15 15:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:59:04,271 main INFO screen la peace pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (62.6s)
Sep 15 15:59:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:59:32,910 main INFO screen COSM pass=0 dev=11.11 ins=0.0 pro=14 1a=False 1b=False 2=False (50.8s)
Sep 15 16:00:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:00:06,657 main INFO screen puter pass=0 dev=0.0 ins=9.86 pro=59 1a=False 1b=False 2=False (63.5s)
Sep 15 16:00:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:00:11,202 main INFO screen CHANEL pass=0 dev=0.0 ins=144.34 pro=0 1a=False 1b=False 2=True (66.9s)
Sep 15 16:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:00:37,923 main INFO screen elizabuth pass=0 dev=0.0 ins=27.55 pro=66 1a=False 1b=False 2=True (65.0s)
Sep 15 16:01:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:01:19,779 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (68.6s)
Sep 15 16:01:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:01:20,203 main INFO screen MIRA pass=0 dev=0.0 ins=18.1 pro=54 1a=False 1b=False 2=True (73.5s)
Sep 15 16:01:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:01:35,183 main INFO screen Buddy pass=0 dev=0.0 ins=29.32 pro=33 1a=True 1b=False 2=True (57.3s)
Sep 15 16:02:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:02:22,810 main INFO screen WARRANT pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (63.0s)
Sep 15 16:02:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:02:31,396 main INFO screen Plover pass=0 dev=0.0 ins=24.8 pro=1 1a=False 1b=False 2=False (71.2s)
Sep 15 16:02:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:02:44,271 main INFO screen Stallions pass=0 dev=0.0 ins=20.75 pro=12 1a=False 1b=False 2=True (69.1s)
Sep 15 16:03:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:03:18,571 main INFO screen BLUEPILL pass=0 dev=0.0 ins=25.3 pro=69 1a=False 1b=False 2=True (55.8s)
Sep 15 16:03:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:03:20,434 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:03:20 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:03:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:03:40,787 main INFO screen STAMPYCAT pass=0 dev=0.0 ins=6.74 pro=62 1a=False 1b=False 2=True (69.4s)
Sep 15 16:03:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:03:48,935 main INFO screen JERRY pass=0 dev=1.0 ins=31.68 pro=43 1a=False 1b=False 2=True (64.7s)
Sep 15 16:04:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:04:15,274 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (56.7s)
Sep 15 16:04:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:04:36,955 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (56.2s)
Sep 15 16:04:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:04:44,235 main INFO screen RBX pass=0 dev=0.0 ins=0.28 pro=6 1a=False 1b=False 2=False (55.3s)
Sep 15 16:05:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:05:08,836 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.6s)
Sep 15 16:05:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:05:34,053 main INFO screen TWF pass=0 dev=0.0 ins=20.23 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 15 16:05:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:05:40,791 main INFO screen FLYCOIN pass=0 dev=0.22 ins=0.0 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 15 16:06:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:06:03,733 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.9s)
Sep 15 16:06:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:06:25,712 main INFO screen thiswill pass=0 dev=0.0 ins=53.88 pro=24 1a=False 1b=False 2=True (51.7s)
Sep 15 16:06:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:06:35,933 main INFO screen thiswill pass=0 dev=0.0 ins=41.78 pro=15 1a=True 1b=False 2=True (55.1s)
Sep 15 16:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:06:56,612 main INFO screen Flywheel pass=0 dev=0.0 ins=37.23 pro=28 1a=False 1b=False 2=True (52.9s)
Sep 15 16:07:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:07:21,700 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.0s)
Sep 15 16:07:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:07:28,561 main INFO screen LEGO pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (52.6s)
Sep 15 16:07:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:07:53,491 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 15 16:08:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:08:07,127 main INFO screen ROSE pass=0 dev=0.0 ins=31.3 pro=25 1a=False 1b=False 2=True (45.4s)
Sep 15 16:08:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:08:20,577 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:08:20 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:08:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:08:38,527 main INFO screen BBC pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (70.0s)
Sep 15 16:08:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:08:49,429 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.9s)
Sep 15 16:09:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:04,053 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (56.9s)
Sep 15 16:09:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:32,773 main INFO screen MIGHTFLY pass=0 dev=0.0 ins=52.29 pro=16 1a=True 1b=False 2=True (54.2s)
Sep 15 16:09:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:47,124 main INFO screen PONK pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (57.7s)
Sep 15 16:09:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:09:51,261 main INFO screen MIGHTFLY pass=0 dev=0.0 ins=24.16 pro=1 1a=False 1b=False 2=False (47.2s)
Sep 15 16:10:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:28,510 main INFO screen PONS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 16:10:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:41,182 main INFO screen BTC pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (54.1s)
Sep 15 16:10:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:10:44,083 main INFO screen DIP pass=0 dev=0.0 ins=34.81 pro=13 1a=False 1b=False 2=True (52.8s)
Sep 15 16:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:37,774 main INFO screen Neuro pass=0 dev=0.0 ins=10.26 pro=64 1a=False 1b=False 2=False (69.3s)
Sep 15 16:11:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:43,679 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (59.6s)
Sep 15 16:11:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:11:46,758 main INFO screen Neuro pass=0 dev=0.0 ins=17.72 pro=49 1a=False 1b=False 2=False (65.6s)
Sep 15 16:12:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:33,291 main INFO screen ORCA pass=0 dev=0.0 ins=48.56 pro=6 1a=False 1b=False 2=True (55.5s)
Sep 15 16:12:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:46,147 main INFO screen PricedIn pass=0 dev=0.0 ins=18.74 pro=4 1a=False 1b=False 2=False (59.4s)
Sep 15 16:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:12:49,271 main INFO screen taxless pass=0 dev=0.0 ins=45.07 pro=24 1a=False 1b=False 2=True (65.6s)
Sep 15 16:13:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:13:21,795 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:13:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T14:57:25Z
--- update 2026-09-15T15:02:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1214cbbf2de3446d84ae08388a8c7fa6
analyses gestart (0f687558a2d6)
--- update 2026-09-15T15:07:36Z
--- update 2026-09-15T15:12:37Z
--- update 2026-09-15T15:17:36Z
--- update 2026-09-15T15:22:38Z
--- update 2026-09-15T15:27:40Z
--- update 2026-09-15T15:32:40Z
--- update 2026-09-15T15:37:40Z
--- update 2026-09-15T15:42:42Z
--- update 2026-09-15T15:47:43Z
--- update 2026-09-15T15:52:44Z
--- update 2026-09-15T15:57:45Z
--- update 2026-09-15T16:03:18Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1702f0d8babc48c590b11e6b42957c29
analyses gestart (0f687558a2d6)
--- update 2026-09-15T16:08:19Z
--- update 2026-09-15T16:13:20Z
```

## Analyses (laatste 40 regels)
```
active
12:15:21   1000/6807 lopers, 7353 koppelingen
12:16:07   1500/6807 lopers, 11262 koppelingen
12:16:58   2000/6807 lopers, 15841 koppelingen
12:17:42   2500/6807 lopers, 18547 koppelingen
12:18:20   3000/6807 lopers, 21453 koppelingen
12:19:14   3500/6807 lopers, 25603 koppelingen
12:19:50   4000/6807 lopers, 28395 koppelingen
12:20:45   4500/6807 lopers, 32066 koppelingen
12:21:33   5000/6807 lopers, 35311 koppelingen
12:22:13   5500/6807 lopers, 38244 koppelingen
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
--- /opt/schaduwbot/vamp.py 13:01:37
13:01:37 tokens lezen
13:01:41 135941 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
13:13:51 6879 lopers, 19 niet-onderscheidende woorden
13:14:53   500/6879 lopers, 4294 koppelingen
13:15:46   1000/6879 lopers, 7299 koppelingen
13:16:30   1500/6879 lopers, 11181 koppelingen
13:17:20   2000/6879 lopers, 15724 koppelingen
13:18:02   2500/6879 lopers, 18375 koppelingen
13:18:35   3000/6879 lopers, 21263 koppelingen
13:19:25   3500/6879 lopers, 25366 koppelingen
13:19:59   4000/6879 lopers, 28115 koppelingen
13:20:55   4500/6879 lopers, 31747 koppelingen
13:21:39   5000/6879 lopers, 34889 koppelingen
13:22:16   5500/6879 lopers, 37799 koppelingen
13:23:41   6000/6879 lopers, 44142 koppelingen
13:24:27   6500/6879 lopers, 47629 koppelingen
13:24:50 uitkomsten uit de trades halen
13:38:33 69698 tokens met een instapkoers
13:38:34 klaar in 2217s: 6879 lopers, 27676 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 13:38:34
--- /opt/schaduwbot/video_replay.py 14:02:16
--- /opt/schaduwbot/video_replay.py 15:02:36
--- /opt/schaduwbot/video_replay.py 16:03:19
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
11:01:24 ijk: +6 van 9 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=232 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
11:01:25 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 9/35/148 | al gemeten: 622
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
14:02:52 ijk: +6 van 14 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=238 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
14:02:53 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 14/45/160 | al gemeten: 637
15:03:01 ijk: +4 van 4 kandidaten (4 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=240 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
15:03:02 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 4/34/158 | al gemeten: 641
16:03:54 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=246 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
16:03:55 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 12/35/164 | al gemeten: 647
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
