# Schaduwbot status

- tijd: 2026-09-15 08:04:23 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 18 hours, 17 minutes
- bot-service: active
- code-versie: a8d6b4f
- schijf: 6.9G/38G | geheugen: 2359/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 178216, "tokens_in_memory": 6381, "msgs": 26506641, "trades": 5374347, "creates": 57328, "decode_fail": 452765, "rpc_calls": 156373, "rpc_errors": 13, "sol_usd": 100.37111596461897, "open_positions": 60, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 07:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:00,861 main INFO screen biketrump pass=0 dev=0.0 ins=77.42 pro=3 1a=False 1b=True 2=True (57.9s)
Sep 15 07:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:02,859 main INFO screen $KOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 15 07:40:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:44,171 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.6s)
Sep 15 07:40:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:54,121 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.3s)
Sep 15 07:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:56,757 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.9s)
Sep 15 07:41:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:41:41,577 main INFO screen mentality pass=0 dev=0.0 ins=7.28 pro=32 1a=False 1b=False 2=False (57.4s)
Sep 15 07:42:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:04,108 main INFO screen Og pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (67.4s)
Sep 15 07:42:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:05,570 main INFO screen CharlieDurk pass=0 dev=0.0 ins=28.03 pro=61 1a=False 1b=False 2=True (71.4s)
Sep 15 07:42:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:39,645 main INFO screen BIKESHIBA pass=0 dev=0.0 ins=79.24 pro=8 1a=False 1b=True 2=True (58.1s)
Sep 15 07:43:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:08,783 main INFO screen sol pass=0 dev=0.0 ins=0.88 pro=2 1a=False 1b=False 2=True (64.7s)
Sep 15 07:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:11,698 main INFO screen MOSQUITO pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (66.1s)
Sep 15 07:43:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:30,930 main INFO screen UP COIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.3s)
Sep 15 07:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:53,475 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:43:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:43:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:57,614 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (48.8s)
Sep 15 07:44:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:44:13,139 main INFO screen PRIMETIME pass=0 dev=0.0 ins=45.35 pro=81 1a=False 1b=False 2=True (61.4s)
Sep 15 07:44:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:44:21,197 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (50.3s)
Sep 15 07:44:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:44:48,963 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.3s)
Sep 15 07:45:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:45:03,493 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (50.4s)
Sep 15 07:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:45:10,980 main INFO screen GS pass=0 dev=0.0 ins=18.84 pro=32 1a=False 1b=False 2=True (49.8s)
Sep 15 07:45:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:45:53,803 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (64.8s)
Sep 15 07:45:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:45:59,218 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (48.2s)
Sep 15 07:46:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:46:07,146 main INFO screen SIGMAN pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (63.6s)
Sep 15 07:46:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:46:50,402 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 15 07:46:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:46:59,363 main INFO screen CATBRAIN pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=False 2=True (60.1s)
Sep 15 07:47:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:47:03,500 main INFO screen ZERO6 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 15 07:47:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:47:44,873 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (54.5s)
Sep 15 07:48:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:48:02,749 main INFO screen fe pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (63.4s)
Sep 15 07:48:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:48:04,642 main INFO screen $SPEEDMIKE pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (61.1s)
Sep 15 07:48:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:48:34,539 main INFO screen TNT pass=0 dev=0.0 ins=33.47 pro=20 1a=False 1b=False 2=True (49.7s)
Sep 15 07:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:48:56,082 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.3s)
Sep 15 07:48:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:48:56,861 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:48:56 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:49:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:49:00,044 main INFO screen   pass=0 dev=0.0 ins=18.08 pro=63 1a=False 1b=False 2=True (55.4s)
Sep 15 07:49:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:49:40,272 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.7s)
Sep 15 07:49:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:49:58,297 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (62.2s)
Sep 15 07:50:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:50:05,383 main INFO screen XXXG-00W0 pass=0 dev=11.4 ins=0.0 pro=15 1a=False 1b=False 2=False (65.3s)
Sep 15 07:50:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:50:31,597 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (51.3s)
Sep 15 07:51:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:51:06,690 main INFO screen Profitable pass=0 dev=0.0 ins=18.47 pro=47 1a=False 1b=False 2=True (68.4s)
Sep 15 07:51:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:51:09,628 main INFO screen BG-5 pass=0 dev=0.0 ins=20.33 pro=69 1a=False 1b=False 2=True (64.2s)
Sep 15 07:51:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:51:28,757 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.2s)
Sep 15 07:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:51:54,936 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (48.2s)
Sep 15 07:51:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:51:58,219 main INFO screen biketyson pass=0 dev=0.0 ins=125.6 pro=0 1a=False 1b=False 2=True (48.6s)
Sep 15 07:52:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:52:32,535 main INFO screen BIKEMUSK pass=0 dev=0.0 ins=75.25 pro=28 1a=False 1b=False 2=True (63.8s)
Sep 15 07:52:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:52:46,542 main INFO screen ROLEX pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (51.6s)
Sep 15 07:52:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:52:53,021 main INFO screen DIG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.8s)
Sep 15 07:53:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:53:22,833 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 15 07:53:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:53:40,429 main INFO screen BULL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.9s)
Sep 15 07:53:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:53:45,846 main INFO screen SHIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.8s)
Sep 15 07:53:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:53:58,037 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:53:58 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:54:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:54:30,194 main INFO screen MOMO pass=0 dev=0.0 ins=0.0 pro=63 1a=False 1b=False 2=False (67.4s)
Sep 15 07:54:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:54:52,792 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.9s)
Sep 15 07:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:54:54,712 main INFO screen SSR pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (74.3s)
Sep 15 07:55:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:55:25,444 main INFO screen HOOD pass=0 dev=0.0 ins=158.62 pro=0 1a=False 1b=False 2=True (55.2s)
Sep 15 07:56:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:56:01,068 main INFO screen 333 pass=0 dev=0.29 ins=0.0 pro=13 1a=False 1b=False 2=False (66.4s)
Sep 15 07:56:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:56:02,536 main INFO screen MOONTOKEN pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (69.7s)
Sep 15 07:56:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:56:23,594 main INFO screen twinetard pass=0 dev=0.0 ins=77.66 pro=4 1a=False 1b=True 2=True (58.1s)
Sep 15 07:57:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:57:09,316 main INFO screen ROBINCAT pass=0 dev=0.0 ins=79.24 pro=3 1a=False 1b=False 2=True (66.8s)
Sep 15 07:57:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:57:12,239 main INFO screen BLAST pass=0 dev=0.0 ins=2.4 pro=58 1a=False 1b=False 2=False (71.2s)
Sep 15 07:57:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:57:17,683 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.1s)
Sep 15 07:58:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:58:14,538 main INFO screen $ROCKET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 15 07:58:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:58:14,954 main INFO screen CHILLCAPY pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (65.6s)
Sep 15 07:58:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:58:18,557 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (60.9s)
Sep 15 07:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:59:04,821 main INFO screen Chud pass=0 dev=0.0 ins=15.93 pro=9 1a=False 1b=False 2=False (49.9s)
Sep 15 07:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:59:06,477 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:59:06 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:59:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:59:24,901 main INFO screen MEOWERO pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (70.4s)
Sep 15 07:59:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:59:26,836 main INFO screen Motion pass=0 dev=0.0 ins=34.8 pro=70 1a=False 1b=False 2=True (68.3s)
Sep 15 07:59:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:59:58,619 main INFO screen ASH pass=0 dev=0.0 ins=0.24 pro=20 1a=False 1b=False 2=False (53.8s)
Sep 15 08:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:00:23,551 main INFO screen MOPH pass=0 dev=0.0 ins=79.27 pro=3 1a=False 1b=True 2=True (58.6s)
Sep 15 08:00:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:00:35,056 main INFO screen DONSTUMP pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (68.2s)
Sep 15 08:01:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:01:11,131 main INFO screen DCAPPY pass=0 dev=0.07 ins=0.0 pro=5 1a=False 1b=False 2=False (72.5s)
Sep 15 08:01:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:01:18,556 main INFO screen HOUSE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.0s)
Sep 15 08:01:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:01:44,024 main INFO screen SolFly pass=0 dev=0.0 ins=33.6 pro=56 1a=False 1b=False 2=True (69.0s)
Sep 15 08:01:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:01:45,398 aiohttp.access INFO 195.182.16.23 [15/Sep/2026:08:01:45 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 15 08:02:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:02:08,282 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (57.1s)
Sep 15 08:02:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:02:15,211 main INFO screen ASH pass=0 dev=0.0 ins=0.14 pro=24 1a=False 1b=False 2=False (56.7s)
Sep 15 08:02:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:02:37,281 main INFO screen PEPEBATON pass=0 dev=0.0 ins=78.94 pro=6 1a=False 1b=True 2=True (53.3s)
Sep 15 08:03:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:03:03,535 main INFO screen ASH pass=0 dev=0.0 ins=0.38 pro=20 1a=False 1b=False 2=False (55.3s)
Sep 15 08:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:03:26,607 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=True (71.4s)
Sep 15 08:03:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:03:27,615 main INFO screen 🌙 BUCK pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (50.3s)
Sep 15 08:04:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:04:20,817 main INFO screen CHILLGPT pass=0 dev=0.0 ins=75.32 pro=23 1a=False 1b=False 2=True (77.3s)
Sep 15 08:04:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:04:23,714 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:04:23 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T06:46:16Z
--- update 2026-09-15T06:51:34Z
--- update 2026-09-15T06:56:36Z
--- update 2026-09-15T07:01:46Z
--- update 2026-09-15T07:07:17Z
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
```

## Analyses (laatste 25 regels)
```
active
06:30:12   54000 tokens, 5196535 trades, 629071 posities (352s)
06:30:26   56000 tokens, 5386638 trades, 656411 posities (366s)
06:30:39   58000 tokens, 5556442 trades, 675632 posities (379s)
06:30:53   60000 tokens, 5747120 trades, 700684 posities (393s)
06:31:08   62000 tokens, 5938035 trades, 722696 posities (407s)
06:31:20   64000 tokens, 6133797 trades, 751257 posities (420s)
06:31:32   66000 tokens, 6333181 trades, 775959 posities (431s)
06:31:44   68000 tokens, 6522980 trades, 801090 posities (443s)
06:31:56   70000 tokens, 6699942 trades, 821373 posities (456s)
06:32:08   72000 tokens, 6901917 trades, 845358 posities (467s)
06:32:21   74000 tokens, 7110225 trades, 878785 posities (480s)
06:32:31 posities: 896682 uit 7257573 trades (496s)
06:32:47 209065 wallets gerekend
06:32:47 geluk-toets
06:33:30 persistentie
06:33:34 kopieer-simulatie
06:35:45 klaar in 690s -> /opt/schaduwbot/reports/wallets.md
07:43:53 105360 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
07:44:15   ingelezen tot rowid 10908607 (193314 rijen, 193314 bruikbaar)
07:44:18 ingelezen: 193314 nieuwe trades, 193314 bruikbaar (25s)
07:47:37 3000 aankopen van gevolgde wallets geëvalueerd
07:48:39 vroege kopers: 294 voldoen nu, register 517, 277 tokens beoordeeld
07:49:21 grote spelers: saldo van 1139 wallets opgehaald
07:49:55 herkomst: 40 posities gekoppeld
07:50:11 klaar in 378s -> /opt/schaduwbot/reports/ledger.md
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
