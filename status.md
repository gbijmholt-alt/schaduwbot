# Schaduwbot status

- tijd: 2026-09-15 07:28:20 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 17 hours, 41 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2238/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 176052, "tokens_in_memory": 6650, "msgs": 26322555, "trades": 5319270, "creates": 56733, "decode_fail": 449683, "rpc_calls": 154131, "rpc_errors": 13, "sol_usd": 100.839282620244, "open_positions": 34, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 07:02:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:02:30,078 main INFO screen sql pass=0 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=True (63.6s)
Sep 15 07:02:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:02:50,427 main INFO screen PERC30 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.7s)
Sep 15 07:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:02:51,124 main INFO screen SOLROCKET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (75.8s)
Sep 15 07:03:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:03:26,287 main INFO screen robinbaton pass=0 dev=0.0 ins=79.13 pro=1 1a=False 1b=True 2=True (56.2s)
Sep 15 07:03:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:03:59,180 main INFO screen SHIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.1s)
Sep 15 07:03:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:03:59,383 main INFO screen FLYT pass=0 dev=0.0 ins=1.72 pro=58 1a=False 1b=False 2=False (69.0s)
Sep 15 07:04:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:04:27,829 main INFO screen Stewie pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.5s)
Sep 15 07:05:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:05:00,724 main INFO screen RIPTOP pass=0 dev=1.65 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 15 07:05:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:05:09,840 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (70.5s)
Sep 15 07:05:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:05:38,326 main INFO screen pep pass=0 dev=0.0 ins=4.2 pro=71 1a=False 1b=False 2=False (70.5s)
Sep 15 07:05:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:05:58,813 main INFO screen GOONER pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (58.1s)
Sep 15 07:06:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:06:06,271 main INFO screen BIKE MJ pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (56.4s)
Sep 15 07:06:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:06:42,466 main INFO screen fatcat pass=0 dev=0.0 ins=30.55 pro=49 1a=False 1b=False 2=True (64.1s)
Sep 15 07:07:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:07:08,452 main INFO screen DOUGH pass=0 dev=0.0 ins=31.99 pro=40 1a=False 1b=False 2=True (69.6s)
Sep 15 07:07:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:07:12,235 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (66.0s)
Sep 15 07:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:07:19,085 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:07:19 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:07:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:07:52,095 main INFO screen BIKE MJ pass=0 dev=0.0 ins=26.49 pro=35 1a=False 1b=False 2=False (69.6s)
Sep 15 07:08:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:08:05,027 main INFO screen Huhcat pass=0 dev=0.0 ins=24.84 pro=70 1a=False 1b=False 2=True (56.6s)
Sep 15 07:08:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:08:24,058 main INFO screen pipetyson pass=0 dev=0.37 ins=0.0 pro=18 1a=False 1b=False 2=False (71.8s)
Sep 15 07:08:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:08:53,625 main INFO screen krispy pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (61.5s)
Sep 15 07:09:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:09:13,582 main INFO screen Goblin pass=0 dev=0.0 ins=15.13 pro=73 1a=False 1b=False 2=True (68.6s)
Sep 15 07:09:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:09:41,576 main INFO screen Pussycoin pass=0 dev=0.0 ins=21.87 pro=66 1a=False 1b=False 2=True (77.5s)
Sep 15 07:10:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:10:10,628 main INFO screen mikeflyson pass=0 dev=0.0 ins=21.33 pro=73 1a=False 1b=False 2=True (77.0s)
Sep 15 07:10:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:10:17,897 main INFO screen trumptwine pass=0 dev=0.0 ins=77.42 pro=4 1a=False 1b=True 2=True (64.3s)
Sep 15 07:10:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:10:40,005 main INFO screen PINK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.4s)
Sep 15 07:11:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:11:14,604 main INFO screen LCK  pass=0 dev=0.25 ins=0.0 pro=9 1a=False 1b=False 2=False (64.0s)
Sep 15 07:11:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:11:33,023 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (75.1s)
Sep 15 07:11:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:11:53,677 main INFO screen SOL pass=0 dev=0.0 ins=14.0 pro=65 1a=False 1b=False 2=True (73.7s)
Sep 15 07:12:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:12:19,214 main INFO screen GTA IV pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (64.6s)
Sep 15 07:12:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:12:20,622 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:12:20 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:12:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:12:49,441 main INFO screen ACCELERATE pass=0 dev=0.0 ins=27.92 pro=52 1a=False 1b=False 2=True (76.4s)
Sep 15 07:12:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:12:58,055 main INFO screen ASH pass=0 dev=0.0 ins=0.14 pro=19 1a=False 1b=False 2=False (64.4s)
Sep 15 07:13:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:13:36,685 main INFO screen $MOONCOIN pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (77.5s)
Sep 15 07:13:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:13:51,121 main INFO screen USGR pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (61.7s)
Sep 15 07:14:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:14:03,117 main INFO screen WhiteBull pass=0 dev=0.0 ins=55.44 pro=35 1a=False 1b=False 2=True (65.1s)
Sep 15 07:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:14:51,644 main INFO screen WALRUS pass=0 dev=0.0 ins=5.64 pro=46 1a=False 1b=False 2=False (75.0s)
Sep 15 07:14:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:14:52,604 main INFO screen GME pass=0 dev=0.0 ins=75.22 pro=1 1a=False 1b=False 2=True (61.5s)
Sep 15 07:14:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:14:56,584 main INFO screen MOONCOIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.5s)
Sep 15 07:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:16:01,003 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.4s)
Sep 15 07:16:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:16:04,706 main INFO screen OCD pass=0 dev=0.0 ins=12.3 pro=39 1a=False 1b=False 2=True (68.1s)
Sep 15 07:16:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:16:07,062 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (75.4s)
Sep 15 07:16:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:16:56,238 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.2s)
Sep 15 07:17:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:17:00,646 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.9s)
Sep 15 07:17:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:17:04,678 main INFO screen Jav pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.6s)
Sep 15 07:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:17:37,193 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:17:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:17:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:17:50,604 main INFO screen TNT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 15 07:18:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:18:08,896 main INFO screen BLAST pass=0 dev=0.0 ins=0.0 pro=61 1a=False 1b=False 2=False (68.2s)
Sep 15 07:18:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:18:14,797 main INFO screen sCAT pass=0 dev=0.0 ins=14.25 pro=73 1a=False 1b=False 2=True (70.1s)
Sep 15 07:18:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:18:46,972 main INFO screen Lemon pass=0 dev=0.0 ins=16.45 pro=63 1a=False 1b=False 2=True (56.4s)
Sep 15 07:19:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:19:07,362 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.5s)
Sep 15 07:19:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:19:22,084 main INFO screen $MSTONKS pass=0 dev=0.0 ins=0.05 pro=16 1a=False 1b=False 2=True (67.3s)
Sep 15 07:19:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:19:49,371 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.4s)
Sep 15 07:20:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:20:16,698 main INFO screen qweqwrqwtq pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.3s)
Sep 15 07:20:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:20:21,774 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.7s)
Sep 15 07:20:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:20:44,090 main INFO screen nebt pass=0 dev=0.0 ins=56.17 pro=14 1a=False 1b=False 2=True (54.7s)
Sep 15 07:21:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:21:03,021 main INFO screen SPL-404 pass=0 dev=0.0 ins=38.66 pro=76 1a=False 1b=False 2=True (46.3s)
Sep 15 07:21:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:21:25,892 aiohttp.access INFO 94.154.43.223 [15/Sep/2026:07:21:25 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 07:21:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:21:31,336 main INFO screen SPL-404 pass=0 dev=0.0 ins=11.54 pro=78 1a=False 1b=False 2=False (69.6s)
Sep 15 07:21:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:21:42,500 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (58.4s)
Sep 15 07:21:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:21:59,037 main INFO screen $BULL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.0s)
Sep 15 07:22:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:22:30,419 main INFO screen MIKEAISON pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (59.1s)
Sep 15 07:22:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:22:44,979 main INFO screen all in pass=0 dev=0.0 ins=27.92 pro=12 1a=False 1b=False 2=True (45.9s)
Sep 15 07:22:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:22:47,520 main INFO screen HIGHER pass=0 dev=0.0 ins=3.56 pro=59 1a=False 1b=False 2=False (65.0s)
Sep 15 07:23:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:23:11,475 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:23:11 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:23:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:23:36,555 main INFO screen All-In pass=0 dev=0.0 ins=0.04 pro=73 1a=False 1b=False 2=True (66.1s)
Sep 15 07:23:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:23:50,352 main INFO screen All Inu pass=0 dev=0.0 ins=26.82 pro=15 1a=False 1b=False 2=True (65.4s)
Sep 15 07:23:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:23:56,267 main INFO screen joedirt pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 15 07:24:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:24:50,337 main INFO screen BFD pass=0 dev=0.0 ins=55.94 pro=29 1a=False 1b=False 2=True (73.8s)
Sep 15 07:25:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:25:00,678 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (70.3s)
Sep 15 07:25:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:25:00,736 main INFO screen DEOD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.5s)
Sep 15 07:25:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:25:57,792 main INFO screen SHAQ pass=0 dev=0.0 ins=0.0 pro=53 1a=False 1b=False 2=False (67.5s)
Sep 15 07:26:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:26:04,194 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.5s)
Sep 15 07:26:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:26:05,767 main INFO screen titcoin pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.0s)
Sep 15 07:27:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:27:09,955 main INFO screen BM pass=0 dev=0.0 ins=0.0 pro=40 1a=False 1b=False 2=False (65.8s)
Sep 15 07:27:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:27:12,838 main INFO screen Foneton pass=0 dev=0.0 ins=76.26 pro=22 1a=False 1b=False 2=True (75.0s)
Sep 15 07:27:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:27:17,971 main INFO screen Asscoin pass=0 dev=0.0 ins=14.53 pro=74 1a=False 1b=False 2=True (72.2s)
Sep 15 07:28:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:28:08,367 main INFO screen trumpbaton pass=0 dev=0.0 ins=79.13 pro=1 1a=False 1b=True 2=True (55.5s)
Sep 15 07:28:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:28:08,460 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.5s)
Sep 15 07:28:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:28:17,227 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.3s)
Sep 15 07:28:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:28:20,414 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:28:20 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T05:50:30Z
--- update 2026-09-15T05:55:30Z
--- update 2026-09-15T06:00:31Z
--- update 2026-09-15T06:05:31Z
--- update 2026-09-15T06:10:36Z
--- update 2026-09-15T06:15:38Z
--- update 2026-09-15T06:20:58Z
--- update 2026-09-15T06:26:02Z
--- update 2026-09-15T06:31:06Z
--- update 2026-09-15T06:36:14Z
--- update 2026-09-15T06:41:14Z
--- update 2026-09-15T06:46:16Z
--- update 2026-09-15T06:51:34Z
--- update 2026-09-15T06:56:36Z
--- update 2026-09-15T07:01:46Z
--- update 2026-09-15T07:07:17Z
--- update 2026-09-15T07:12:19Z
--- update 2026-09-15T07:17:36Z
--- update 2026-09-15T07:23:10Z
--- update 2026-09-15T07:28:19Z
```

## Analyses (laatste 25 regels)
```
inactive
06:28:28   38000 tokens, 3681003 trades, 443940 posities (248s)
06:28:42   40000 tokens, 3878402 trades, 468824 posities (262s)
06:28:55   42000 tokens, 4065280 trades, 492092 posities (275s)
06:29:07   44000 tokens, 4243961 trades, 512326 posities (287s)
06:29:19   46000 tokens, 4422263 trades, 532650 posities (299s)
06:29:33   48000 tokens, 4597419 trades, 553807 posities (312s)
06:29:46   50000 tokens, 4788806 trades, 577841 posities (326s)
06:30:00   52000 tokens, 4999896 trades, 603952 posities (339s)
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
```

## IJking poolkoers (laatste 12 regels)
```
06:56:42 ijk: +2 van 2 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=194 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
06:56:42 ijk-diagnose: nieuwste migratie 2.5 min oud | migraties 15/60/240 min: 9/43/165 | al gemeten: 545
07:01:49 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=195 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:01:49 ijk-diagnose: nieuwste migratie 1.7 min oud | migraties 15/60/240 min: 6/41/164 | al gemeten: 546
07:07:30 ijk: +4 van 4 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=198 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:07:30 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 7/41/161 | al gemeten: 550
07:12:32 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=202 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:12:33 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 10/42/163 | al gemeten: 554
07:17:48 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=205 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:17:48 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 11/42/161 | al gemeten: 558
07:23:19 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=208 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:23:19 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/40/161 | al gemeten: 561
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
