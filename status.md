# Schaduwbot status

- tijd: 2026-09-14 01:22:42 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 11 hours, 35 minutes
- bot-service: active
- code-versie: 69b3f7f
- schijf: 5.2G/38G | geheugen: 2304/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 67715, "tokens_in_memory": 7819, "msgs": 8612826, "trades": 1873827, "creates": 19958, "decode_fail": 166233, "rpc_calls": 54807, "rpc_errors": 3, "sol_usd": 99.33633082490753, "open_positions": 18, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 00:48:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:48:09,885 main INFO screen JANE pass=0 dev=0.28 ins=0.0 pro=5 1a=False 1b=False 2=False (64.4s)
Sep 14 00:48:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:48:58,659 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.1s)
Sep 14 00:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:49:21,173 main INFO screen SOLBOT pass=0 dev=0.0 ins=23.42 pro=66 1a=False 1b=False 2=True (50.6s)
Sep 14 00:49:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:49:49,777 main INFO screen LetsRide pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (51.4s)
Sep 14 00:50:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:50:55,276 main INFO screen PANIC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.9s)
Sep 14 00:51:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:51:38,634 main INFO screen Nintendo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.4s)
Sep 14 00:52:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:00,785 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:52:00 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:04,822 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.5s)
Sep 14 00:52:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:06,761 main INFO screen TWINBER pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=False 2=True (68.2s)
Sep 14 00:52:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:40,147 main INFO screen Shane pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 14 00:52:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:52:55,733 main INFO screen NJAR pass=0 dev=0.0 ins=51.54 pro=13 1a=False 1b=True 2=False (50.9s)
Sep 14 00:53:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:53:07,309 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.5s)
Sep 14 00:53:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:53:32,978 main INFO screen SANDER pass=1 dev=0.0 ins=10.79 pro=59 1a=False 1b=False 2=False (52.8s)
Sep 14 00:53:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:53:45,949 main INFO screen bundloor pass=0 dev=0.0 ins=19.64 pro=60 1a=False 1b=False 2=True (50.2s)
Sep 14 00:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:54:00,213 aiohttp.access INFO 204.76.203.49 [14/Sep/2026:00:54:00 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 14 00:54:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:54:00,236 aiohttp.access INFO 204.76.203.49 [14/Sep/2026:00:54:00 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 14 00:54:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:54:10,254 main INFO screen MWJ pass=1 dev=0.0 ins=0.0 pro=60 1a=False 1b=False 2=False (62.9s)
Sep 14 00:54:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:54:23,722 main INFO screen TBG pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (50.7s)
Sep 14 00:54:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:54:33,778 main INFO screen SpaceX pass=0 dev=78.44 ins=0.0 pro=1 1a=False 1b=False 2=True (47.8s)
Sep 14 00:55:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:55:20,175 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=8 1a=False 1b=False 2=True (62.7s)
Sep 14 00:55:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:55:34,645 main INFO screen VIRTUES pass=0 dev=0.0 ins=24.01 pro=26 1a=False 1b=False 2=False (49.5s)
Sep 14 00:56:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:56:07,762 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.5s)
Sep 14 00:57:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:57:04,147 main INFO screen JANE pass=0 dev=0.01 ins=0.0 pro=4 1a=False 1b=False 2=False (66.2s)
Sep 14 00:57:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:57:08,324 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:00:57:08 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 00:57:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:57:10,102 main INFO screen BORGOBOT pass=1 dev=0.53 ins=0.0 pro=15 1a=False 1b=False 2=False (62.6s)
Sep 14 00:58:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:58:25,913 main INFO screen CREAM pass=0 dev=1.02 ins=0.0 pro=9 1a=False 1b=False 2=False (67.5s)
Sep 14 00:58:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:58:29,130 main INFO screen Is pass=0 dev=0.0 ins=33.39 pro=36 1a=False 1b=False 2=True (66.8s)
Sep 14 00:59:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:59:02,531 main INFO screen Bullabu pass=0 dev=1.74 ins=55.56 pro=35 1a=False 1b=False 2=True (70.9s)
Sep 14 00:59:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:59:40,616 main INFO screen mictyson pass=0 dev=0.04 ins=8.49 pro=75 1a=False 1b=False 2=True (74.7s)
Sep 14 00:59:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 00:59:43,057 main INFO screen THE CHEAT pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (73.9s)
Sep 14 01:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:00:23,844 main INFO screen F9 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.5s)
Sep 14 01:01:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:01:58,537 main INFO screen BORGOBOT pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (65.2s)
Sep 14 01:02:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:02:05,550 main INFO screen NVIDIA pass=0 dev=0.0 ins=17.61 pro=32 1a=False 1b=False 2=True (55.9s)
Sep 14 01:02:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:02:14,337 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:02:14 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:02:50,008 main INFO screen STARMAN pass=0 dev=0.0 ins=21.63 pro=32 1a=False 1b=False 2=False (64.6s)
Sep 14 01:03:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:03:29,228 main INFO screen $UMB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.3s)
Sep 14 01:04:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:04:27,356 main INFO screen ntkr  pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (77.2s)
Sep 14 01:05:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:05:21,365 main INFO screen DOGE pass=1 dev=0.52 ins=0.0 pro=15 1a=False 1b=False 2=False (73.3s)
Sep 14 01:06:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:06:10,517 main INFO screen Kit Kat  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.6s)
Sep 14 01:06:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:06:47,634 main INFO screen SOL pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (75.8s)
Sep 14 01:07:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:07:29,804 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:07:29 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 14 01:07:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:07:30,618 main INFO screen HALH pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (89.9s)
Sep 14 01:07:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:07:32,254 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 14 01:08:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:08:13,113 main INFO screen mictyson pass=0 dev=0.0 ins=20.68 pro=47 1a=False 1b=False 2=False (85.5s)
Sep 14 01:08:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:08:57,570 main INFO screen CHILLCAT pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (87.0s)
Sep 14 01:09:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:09:15,922 main INFO screen DNS pass=1 dev=1.05 ins=2.35 pro=36 1a=False 1b=False 2=False (81.4s)
Sep 14 01:09:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:09:27,354 main INFO screen Stack pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.2s)
Sep 14 01:10:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:10:15,984 main INFO screen CHILLCAT pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (78.4s)
Sep 14 01:11:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:11:28,804 main INFO screen ECTF pass=0 dev=97.19 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 14 01:12:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:12:34,236 main INFO screen DONGDQ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 14 01:12:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:12:35,836 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:12:35 +0000] "GET /health HTTP/1.1" 200 503 "-" "Python-urllib/3.14"
Sep 14 01:12:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:12:45,122 main INFO screen BetOnBlak pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (75.0s)
Sep 14 01:12:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:12:52,343 main INFO screen Tim pass=1 dev=0.0 ins=0.0 pro=47 1a=False 1b=False 2=False (75.2s)
Sep 14 01:13:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:13:30,732 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.5s)
Sep 14 01:13:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:13:54,570 main INFO screen JSHIB pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (69.4s)
Sep 14 01:14:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:14:03,520 main INFO screen IRONMIKE pass=0 dev=0.0 ins=51.18 pro=75 1a=False 1b=False 2=True (71.2s)
Sep 14 01:14:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:14:32,762 main INFO screen TYSON pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (62.0s)
Sep 14 01:14:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:14:58,694 main INFO screen NUT pass=1 dev=0.02 ins=3.92 pro=62 1a=False 1b=False 2=False (64.1s)
Sep 14 01:15:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:15:09,584 main INFO screen PERKS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (66.1s)
Sep 14 01:15:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:15:31,701 main INFO screen SpaceX pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.9s)
Sep 14 01:16:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:16:10,774 main INFO screen SOL pass=0 dev=12.08 ins=0.0 pro=10 1a=False 1b=False 2=False (72.1s)
Sep 14 01:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:16:18,466 main INFO screen 100 pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (68.9s)
Sep 14 01:16:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:16:41,890 main INFO screen IRONMIKE pass=0 dev=0.0 ins=14.94 pro=77 1a=False 1b=False 2=True (70.2s)
Sep 14 01:17:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:17:23,761 main INFO screen FERSPE pass=0 dev=25.44 ins=0.0 pro=6 1a=False 1b=False 2=False (73.0s)
Sep 14 01:17:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:17:26,749 main INFO screen maxi pass=1 dev=0.0 ins=13.59 pro=63 1a=False 1b=False 2=False (68.3s)
Sep 14 01:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:17:37,517 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:17:37 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 14 01:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:17:52,743 main INFO screen IRONMIKE pass=1 dev=0.07 ins=0.0 pro=11 1a=False 1b=False 2=False (70.8s)
Sep 14 01:18:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:18:16,630 main INFO screen WOTF pass=0 dev=97.17 ins=0.0 pro=1 1a=False 1b=False 2=True (52.9s)
Sep 14 01:18:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:18:37,332 main INFO screen Kanye  pass=1 dev=0.0 ins=5.35 pro=44 1a=False 1b=False 2=False (70.6s)
Sep 14 01:19:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:19:05,462 main INFO screen ACTB pass=0 dev=1.74 ins=56.05 pro=41 1a=False 1b=False 2=True (72.7s)
Sep 14 01:19:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:19:19,187 main INFO screen $MIC pass=0 dev=49.91 ins=0.0 pro=2 1a=False 1b=False 2=False (62.6s)
Sep 14 01:19:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:19:38,579 main INFO screen kite ty pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.2s)
Sep 14 01:20:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:20:14,271 main INFO screen RANK pass=1 dev=0.07 ins=0.0 pro=61 1a=False 1b=False 2=False (68.8s)
Sep 14 01:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:20:18,985 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.8s)
Sep 14 01:20:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:20:32,553 main WARNING stream verbroken: sent 1011 (internal error) keepalive ping timeout; no close frame received — opnieuw over 1s
Sep 14 01:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:20:33,632 main INFO verbonden met wss://api.mainnet-beta.solana.com
Sep 14 01:20:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:20:38,906 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.3s)
Sep 14 01:22:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:22:07,475 main INFO screen GOHOS pass=0 dev=6.89 ins=1.87 pro=20 1a=False 1b=False 2=False (66.6s)
Sep 14 01:22:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:22:33,982 main INFO screen BLAST pass=0 dev=6.08 ins=0.0 pro=7 1a=False 1b=False 2=False (72.4s)
Sep 14 01:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 01:22:42,859 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:01:22:42 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T23:54:39Z
--- update 2026-09-13T23:59:40Z
--- update 2026-09-14T00:04:46Z
--- update 2026-09-14T00:10:22Z
--- update 2026-09-14T00:15:23Z
--- update 2026-09-14T00:20:34Z
--- update 2026-09-14T00:25:36Z
--- update 2026-09-14T00:31:06Z
--- update 2026-09-14T00:36:11Z
--- update 2026-09-14T00:41:30Z
--- update 2026-09-14T00:46:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7e8a0dc2ace745d49c06fa77ab8fe773
analyses gestart (e28253f0c5ee)
--- update 2026-09-14T00:51:59Z
--- update 2026-09-14T00:57:07Z
--- update 2026-09-14T01:02:13Z
--- update 2026-09-14T01:07:28Z
--- update 2026-09-14T01:12:34Z
--- update 2026-09-14T01:17:36Z
--- update 2026-09-14T01:22:41Z
```

## Analyses (laatste 25 regels)
```
active
01:17:42   16000 tokens, 1624546 trades, 210401 posities (87s)
01:17:53   18000 tokens, 1819605 trades, 234242 posities (98s)
01:18:03   20000 tokens, 2018541 trades, 261264 posities (108s)
01:18:15   22000 tokens, 2237060 trades, 295130 posities (120s)
01:18:29   24000 tokens, 2473330 trades, 330944 posities (134s)
01:18:40   26000 tokens, 2665380 trades, 358242 posities (145s)
01:18:52   28000 tokens, 2875090 trades, 384850 posities (157s)
01:19:03   30000 tokens, 3070813 trades, 408250 posities (168s)
01:19:16   32000 tokens, 3286227 trades, 438353 posities (181s)
01:19:30   34000 tokens, 3508623 trades, 467675 posities (195s)
01:19:43   36000 tokens, 3711001 trades, 496997 posities (207s)
01:19:55   38000 tokens, 3899681 trades, 517816 posities (220s)
01:20:07   40000 tokens, 4093171 trades, 544267 posities (231s)
01:20:20   42000 tokens, 4301788 trades, 575006 posities (245s)
01:20:32   44000 tokens, 4496449 trades, 598746 posities (256s)
01:20:45   46000 tokens, 4702106 trades, 624669 posities (270s)
01:20:58   48000 tokens, 4900381 trades, 650745 posities (283s)
01:21:11   50000 tokens, 5090194 trades, 674603 posities (296s)
01:21:23   52000 tokens, 5279569 trades, 701217 posities (308s)
01:21:36   54000 tokens, 5472054 trades, 724710 posities (320s)
01:21:48   56000 tokens, 5666068 trades, 752606 posities (333s)
01:22:02   58000 tokens, 5879279 trades, 782376 posities (346s)
01:22:13   60000 tokens, 6079352 trades, 809473 posities (357s)
01:22:23   62000 tokens, 6287006 trades, 840673 posities (368s)
01:22:34   64000 tokens, 6500356 trades, 880050 posities (379s)
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
