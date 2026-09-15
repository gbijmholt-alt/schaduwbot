# Schaduwbot status

- tijd: 2026-09-15 19:26:29 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 5 hours, 39 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.6G/38G | geheugen: 2254/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 219141, "tokens_in_memory": 10276, "msgs": 34380738, "trades": 6926161, "creates": 73546, "decode_fail": 589718, "rpc_calls": 197460, "rpc_errors": 17, "sol_usd": 98.05609649485324, "open_positions": 44, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 18:59:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:59:48,935 main INFO screen RISE pass=0 dev=0.0 ins=4.36 pro=10 1a=False 1b=False 2=False (53.2s)
Sep 15 18:59:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 18:59:59,880 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (60.7s)
Sep 15 19:00:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:00:37,231 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:00:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 15 19:00:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:00:50,746 main INFO screen OP-OP pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (72.9s)
Sep 15 19:01:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:01:01,616 main INFO screen DOG pass=0 dev=0.0 ins=3.46 pro=55 1a=False 1b=False 2=True (61.7s)
Sep 15 19:01:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:01:02,578 main INFO screen CASHCAT pass=0 dev=0.0 ins=78.96 pro=0 1a=True 1b=False 2=True (73.6s)
Sep 15 19:01:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:01:47,370 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (56.6s)
Sep 15 19:02:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:02:24,854 main INFO screen BANK pass=0 dev=0.0 ins=29.04 pro=76 1a=False 1b=False 2=True (82.3s)
Sep 15 19:02:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:02:28,013 main INFO screen 10M pass=0 dev=0.0 ins=48.75 pro=47 1a=False 1b=False 2=True (86.4s)
Sep 15 19:02:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:02:48,234 main INFO screen SCAT pass=0 dev=0.0 ins=34.8 pro=34 1a=False 1b=False 2=True (60.9s)
Sep 15 19:03:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:03:10,830 main INFO screen cooker pass=0 dev=0.0 ins=4.47 pro=12 1a=False 1b=False 2=False (46.0s)
Sep 15 19:03:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:03:25,430 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (57.4s)
Sep 15 19:03:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:03:43,268 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.0s)
Sep 15 19:04:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:04:11,190 main INFO screen GayCat pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.4s)
Sep 15 19:04:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:04:22,308 main INFO screen #1 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.9s)
Sep 15 19:04:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:04:56,262 main INFO screen Blaze pass=0 dev=0.0 ins=4.16 pro=55 1a=False 1b=False 2=True (73.0s)
Sep 15 19:05:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:05:23,097 main INFO screen goon pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (71.9s)
Sep 15 19:05:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:05:28,924 main INFO screen Stallions pass=0 dev=0.0 ins=17.77 pro=54 1a=False 1b=False 2=True (66.6s)
Sep 15 19:05:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:05:58,198 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:05:58 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:06:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:06:02,712 main INFO screen ANON pass=0 dev=0.0 ins=32.79 pro=64 1a=False 1b=False 2=True (66.4s)
Sep 15 19:06:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:06:34,022 main INFO screen MALAKAS pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (70.9s)
Sep 15 19:06:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:06:37,196 main INFO screen bikewif pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (68.3s)
Sep 15 19:07:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:07:12,805 main INFO screen cook pass=0 dev=0.0 ins=49.14 pro=70 1a=False 1b=False 2=True (70.1s)
Sep 15 19:07:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:07:31,105 main INFO screen HLDM pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (57.1s)
Sep 15 19:07:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:07:42,221 main INFO screen $JOBLESS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.0s)
Sep 15 19:08:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:08:23,688 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (70.9s)
Sep 15 19:08:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:08:44,238 main INFO screen LILPUMP pass=0 dev=0.0 ins=79.27 pro=2 1a=False 1b=False 2=True (73.1s)
Sep 15 19:08:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:08:48,045 main INFO screen Lummis pass=0 dev=0.0 ins=23.25 pro=42 1a=False 1b=False 2=True (65.8s)
Sep 15 19:09:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:09:22,005 main INFO screen squidtham pass=0 dev=0.0 ins=66.4 pro=23 1a=False 1b=True 2=True (58.3s)
Sep 15 19:09:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:09:42,994 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 15 19:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:09:58,300 main INFO screen KASHCAT pass=0 dev=0.0 ins=25.6 pro=71 1a=False 1b=False 2=False (70.3s)
Sep 15 19:10:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:10:19,033 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (57.0s)
Sep 15 19:10:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:10:38,630 main INFO screen COCO  pass=0 dev=108.55 ins=0.0 pro=15 1a=False 1b=False 2=False (55.6s)
Sep 15 19:10:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:10:58,581 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:10:58 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 19:11:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:11:01,943 main INFO screen Lummis pass=0 dev=0.0 ins=18.65 pro=43 1a=False 1b=False 2=False (63.6s)
Sep 15 19:11:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:11:15,832 main INFO screen TINY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.8s)
Sep 15 19:11:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:11:33,004 main INFO screen TROLLP pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (54.4s)
Sep 15 19:11:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:11:54,852 main INFO screen TINY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.9s)
Sep 15 19:12:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:12:16,404 main INFO screen HEAVES pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (60.6s)
Sep 15 19:12:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:12:30,931 main INFO screen TORTA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 15 19:13:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:13:04,276 main INFO screen MULATE pass=0 dev=0.0 ins=17.08 pro=68 1a=False 1b=False 2=True (69.4s)
Sep 15 19:13:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:13:12,937 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.5s)
Sep 15 19:13:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:13:42,015 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (71.1s)
Sep 15 19:14:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:14:04,200 main INFO screen tough  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.9s)
Sep 15 19:14:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:14:04,541 main INFO screen Gaejook pass=0 dev=0.0 ins=4.15 pro=23 1a=False 1b=False 2=True (51.6s)
Sep 15 19:14:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:14:35,583 main INFO screen LARP pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (53.6s)
Sep 15 19:15:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:15:14,341 main INFO screen mtDNA pass=0 dev=2.34 ins=0.0 pro=2 1a=False 1b=False 2=False (70.1s)
Sep 15 19:15:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:15:18,459 main INFO screen NOPOOL pass=0 dev=0.0 ins=0.02 pro=58 1a=False 1b=False 2=False (73.9s)
Sep 15 19:15:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:15:47,797 main INFO screen ANON pass=0 dev=0.0 ins=6.93 pro=39 1a=False 1b=False 2=False (72.2s)
Sep 15 19:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:16:01,076 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:16:01 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:16:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:16:10,893 main INFO screen $EXIT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.6s)
Sep 15 19:16:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:16:13,116 main INFO screen SOLENNE pass=0 dev=0.0 ins=47.11 pro=21 1a=False 1b=False 2=True (54.7s)
Sep 15 19:16:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:16:42,865 main INFO screen NVM pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (55.1s)
Sep 15 19:17:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:17:24,449 main INFO screen Phantom pass=0 dev=0.21 ins=6.11 pro=50 1a=False 1b=False 2=False (71.3s)
Sep 15 19:17:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:17:27,555 main INFO screen $HIGHER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (76.7s)
Sep 15 19:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:17:57,152 main INFO screen $PLORD pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (74.3s)
Sep 15 19:18:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:18:41,447 main INFO screen BSC pass=0 dev=0.0 ins=13.45 pro=57 1a=False 1b=False 2=True (77.0s)
Sep 15 19:18:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:18:41,460 main INFO screen BRIAN pass=0 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (73.9s)
Sep 15 19:19:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:19:02,241 main INFO screen Clarity pass=0 dev=0.0 ins=25.14 pro=62 1a=False 1b=False 2=True (65.1s)
Sep 15 19:19:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:19:13,415 aiohttp.access INFO 89.42.231.200 [15/Sep/2026:19:19:13 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 15 19:19:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:19:52,551 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=18.57 pro=63 1a=False 1b=False 2=True (71.1s)
Sep 15 19:19:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:19:55,827 main INFO screen PONSAI pass=0 dev=0.0 ins=114.78 pro=5 1a=False 1b=False 2=True (74.4s)
Sep 15 19:20:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:20:01,820 main INFO screen WWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (59.6s)
Sep 15 19:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:21:01,721 main INFO screen TwineGuy pass=0 dev=0.0 ins=79.17 pro=2 1a=False 1b=True 2=True (69.2s)
Sep 15 19:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:21:01,723 main INFO screen mikedyson pass=0 dev=0.0 ins=72.68 pro=0 1a=False 1b=True 2=True (65.9s)
Sep 15 19:21:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:21:07,380 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.6s)
Sep 15 19:21:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:21:25,842 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:21:25 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 19:22:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:22:13,548 main INFO screen WARREN pass=0 dev=0.0 ins=6.75 pro=58 1a=False 1b=False 2=True (71.8s)
Sep 15 19:22:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:22:17,238 main INFO screen WARREN pass=0 dev=0.0 ins=29.4 pro=55 1a=False 1b=False 2=True (69.9s)
Sep 15 19:22:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:22:21,205 main INFO screen Machi pass=0 dev=0.0 ins=57.08 pro=21 1a=False 1b=False 2=True (79.5s)
Sep 15 19:23:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:23:25,772 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (68.5s)
Sep 15 19:23:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:23:28,171 main INFO screen 🚂 pass=0 dev=0.0 ins=24.13 pro=2 1a=False 1b=False 2=True (74.6s)
Sep 15 19:23:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:23:28,594 main INFO screen COOL COIN pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (67.4s)
Sep 15 19:24:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:24:26,025 main INFO screen HOE pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (57.4s)
Sep 15 19:24:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:24:27,831 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.1s)
Sep 15 19:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:24:35,896 main INFO screen Anxiety  pass=0 dev=0.0 ins=6.64 pro=70 1a=False 1b=False 2=True (67.7s)
Sep 15 19:25:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:25:30,864 main INFO screen Cat pass=0 dev=0.0 ins=26.95 pro=51 1a=False 1b=False 2=True (64.8s)
Sep 15 19:25:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:25:36,745 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 15 19:25:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:25:40,265 main INFO screen Ape  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.4s)
Sep 15 19:26:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 19:26:29,320 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:19:26:29 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T18:19:17Z
nieuwe code: 03bcc03
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:24:20Z
--- update 2026-09-15T18:29:34Z
nieuwe code: 85d446e
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T18:34:36Z
--- update 2026-09-15T18:39:36Z
--- update 2026-09-15T18:44:43Z
--- update 2026-09-15T18:49:44Z
--- update 2026-09-15T18:55:20Z
--- update 2026-09-15T19:00:36Z
--- update 2026-09-15T19:05:56Z
Running as unit: schaduwbot-wallets.service; invocation ID: d4e9a4210cb94fceb933a73dcc655635
analyses gestart (84579ff37485)
--- update 2026-09-15T19:10:57Z
--- update 2026-09-15T19:15:59Z
--- update 2026-09-15T19:21:24Z
--- update 2026-09-15T19:26:28Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 18:04:11
18:04:12 venster 2026-09-13 06:04 UTC .. nu, 67852 tokens
18:05:01 klaar in 50s: 51584 tokens, 1905 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 19:05:57
19:05:58 venster 2026-09-13 07:05 UTC .. nu, 68842 tokens
19:06:46 klaar in 49s: 52628 tokens, 1902 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
18:55:40 ijk: +4 van 4 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=308 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
18:55:40 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 12/39/153 | al gemeten: 731
19:00:46 ijk: +2 van 2 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=310 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:00:46 ijk-diagnose: nieuwste migratie 1.3 min oud | migraties 15/60/240 min: 10/38/153 | al gemeten: 733
19:06:01 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=311 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:06:02 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 6/37/153 | al gemeten: 734
19:11:14 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=312 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:11:15 ijk-diagnose: nieuwste migratie 4.7 min oud | migraties 15/60/240 min: 6/35/151 | al gemeten: 737
19:16:15 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=315 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:16:15 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 8/36/153 | al gemeten: 740
19:21:54 ijk: +6 van 7 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=321 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
19:21:55 ijk-diagnose: nieuwste migratie -0.4 min oud | migraties 15/60/240 min: 11/41/160 | al gemeten: 746
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 4861 | 494 | 486 | 0 | 118 | 3.7 min |
| 09-13 00:00 | 5995 | 675 | 658 | 0 | 295 | 2.3 min |
| 09-13 06:00 | 4301 | 538 | 534 | 0 | 282 | 2.4 min |
| 09-13 12:00 | 6600 | 754 | 741 | 0 | 286 | 2.6 min |
| 09-13 18:00 | 8021 | 920 | 889 | 0 | 118 | 4.0 min |
| 09-14 00:00 | 6068 | 752 | 743 | 0 | 275 | 2.6 min |
| 09-14 06:00 | 4709 | 692 | 683 | 0 | 323 | 2.3 min |
| 09-14 12:00 | 8320 | 1156 | 1091 | 0 | 36 | 16.9 min |
| 09-14 18:00 | 10622 | 1266 | 1153 | 266 | 0 | 94.8 min |
| 09-15 00:00 | 7337 | 881 | 827 | 81 | 0 | 112.5 min |
| 09-15 06:00 | 6072 | 909 | 853 | 1 | 0 | 73.3 min |
| 09-15 12:00 | 9559 | 1137 | 1052 | 2 | 0 | 72.4 min |
| 09-15 18:00 | 2521 | 0 | 0 | 0 | 0 | - |

'pas na 2u05' = gescreend nadat de replay het token al had vastgelegd; die tellen nooit mee.


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
