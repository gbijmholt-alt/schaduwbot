# Schaduwbot status

- tijd: 2026-09-15 15:37:42 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 1 hour, 50 minutes
- bot-service: active
- code-versie: caa47fa
- schijf: 7.3G/38G | geheugen: 3620/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 205414, "tokens_in_memory": 7714, "msgs": 29708777, "trades": 6253665, "creates": 66617, "decode_fail": 529139, "rpc_calls": 183625, "rpc_errors": 15, "sol_usd": 99.23582358218874, "open_positions": 69, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 15:14:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:14:46,384 main INFO screen Ainu pass=0 dev=0.0 ins=13.18 pro=59 1a=False 1b=False 2=False (66.5s)
Sep 15 15:15:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:15:08,155 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (78.3s)
Sep 15 15:15:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:15:36,530 main INFO screen TOTH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.1s)
Sep 15 15:15:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:15:38,512 main INFO screen WherWaldo pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (75.0s)
Sep 15 15:16:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:16:08,137 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (60.0s)
Sep 15 15:16:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:16:57,597 main INFO screen $PEPEGON pass=0 dev=0.29 ins=31.25 pro=62 1a=False 1b=False 2=True (79.1s)
Sep 15 15:16:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:16:58,104 main INFO screen MOONM pass=0 dev=0.53 ins=0.0 pro=23 1a=False 1b=False 2=False (81.6s)
Sep 15 15:17:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:17:10,341 main INFO screen TOTs pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.2s)
Sep 15 15:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:17:38,147 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:17:38 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:17:57,156 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (59.1s)
Sep 15 15:18:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:18:00,287 main INFO screen Clvicular pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.7s)
Sep 15 15:18:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:18:13,698 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.4s)
Sep 15 15:19:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:19:04,928 main INFO screen EFUEL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.8s)
Sep 15 15:19:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:19:14,379 main INFO screen Maybach pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (74.1s)
Sep 15 15:19:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:19:34,245 main INFO screen Plover pass=0 dev=0.0 ins=20.76 pro=43 1a=False 1b=False 2=True (80.5s)
Sep 15 15:20:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:20:14,229 main INFO screen Carrot pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (69.3s)
Sep 15 15:20:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:20:28,549 main INFO screen $TEME pass=0 dev=0.2 ins=0.0 pro=3 1a=False 1b=False 2=False (74.2s)
Sep 15 15:20:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:20:39,007 main INFO screen Samsung pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (64.8s)
Sep 15 15:21:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:21:28,145 main INFO screen NELLY pass=0 dev=0.0 ins=38.11 pro=58 1a=False 1b=False 2=True (73.9s)
Sep 15 15:21:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:21:30,342 main INFO screen WOFI pass=0 dev=0.79 ins=133.66 pro=1 1a=False 1b=False 2=True (61.8s)
Sep 15 15:21:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:21:42,547 main INFO screen $奶糖 pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (63.5s)
Sep 15 15:22:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:22:37,089 main INFO screen OCS pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=True (66.7s)
Sep 15 15:22:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:22:39,662 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:22:39 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 15 15:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:22:42,047 main INFO screen NORO pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (73.9s)
Sep 15 15:22:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:22:55,754 main INFO screen Bison pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (73.2s)
Sep 15 15:23:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:23:31,406 main INFO screen LOW pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.3s)
Sep 15 15:23:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:23:38,671 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.6s)
Sep 15 15:23:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:23:52,054 main INFO screen GOLDBULL pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (56.3s)
Sep 15 15:24:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:24:36,977 main INFO screen Tauros pass=0 dev=0.0 ins=7.93 pro=71 1a=False 1b=False 2=True (65.6s)
Sep 15 15:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:24:44,830 main INFO screen chump pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.2s)
Sep 15 15:25:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:25:03,328 main INFO screen BATMEDIAN pass=0 dev=0.0 ins=32.71 pro=58 1a=False 1b=False 2=True (71.3s)
Sep 15 15:25:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:25:30,441 aiohttp.access INFO 213.209.159.91 [15/Sep/2026:15:25:30 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 15 15:25:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:25:36,795 main INFO screen jakestall pass=0 dev=3.42 ins=35.08 pro=62 1a=False 1b=False 2=True (59.8s)
Sep 15 15:25:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:25:59,077 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.2s)
Sep 15 15:26:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:26:01,972 main INFO screen DOGISSI pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (58.6s)
Sep 15 15:26:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:26:33,755 main INFO screen Cucumber  pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.0s)
Sep 15 15:27:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:27:16,891 main INFO screen CYBER pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (74.9s)
Sep 15 15:27:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:27:18,143 main INFO screen DELWEIGH pass=0 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (79.1s)
Sep 15 15:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:27:41,209 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:27:41 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:27:41,356 main INFO screen Dodge pass=0 dev=0.0 ins=19.8 pro=49 1a=False 1b=False 2=False (67.6s)
Sep 15 15:28:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:28:14,999 main INFO screen OIL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (56.9s)
Sep 15 15:28:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:28:21,498 main INFO screen Kito pass=0 dev=0.0 ins=30.39 pro=58 1a=False 1b=False 2=True (64.6s)
Sep 15 15:28:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:28:31,766 main INFO screen Facebook pass=0 dev=0.0 ins=161.97 pro=0 1a=False 1b=False 2=True (50.4s)
Sep 15 15:29:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:29:10,956 main INFO screen KITO pass=0 dev=0.0 ins=20.2 pro=3 1a=False 1b=False 2=True (56.0s)
Sep 15 15:29:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:29:23,646 main INFO screen BullRun pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.1s)
Sep 15 15:29:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:29:39,478 main INFO screen ALI pass=0 dev=0.03 ins=0.0 pro=7 1a=False 1b=False 2=False (67.7s)
Sep 15 15:30:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:30:10,494 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.5s)
Sep 15 15:30:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:30:20,239 main INFO screen Liberty pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (56.6s)
Sep 15 15:30:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:30:39,400 main INFO screen MCoin pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (59.9s)
Sep 15 15:31:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:31:08,459 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 15 15:31:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:31:16,464 main INFO screen ALI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 15 15:31:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:31:45,900 main INFO screen TRUMPCALL pass=0 dev=0.0 ins=18.93 pro=3 1a=False 1b=False 2=True (66.5s)
Sep 15 15:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:32:05,307 main INFO screen DogeTrader pass=0 dev=0.0 ins=19.44 pro=0 1a=False 1b=False 2=False (56.8s)
Sep 15 15:32:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:32:23,469 main INFO screen pump pass=0 dev=0.36 ins=0.0 pro=3 1a=False 1b=False 2=False (67.0s)
Sep 15 15:32:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:32:39,283 main INFO screen     REAP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.4s)
Sep 15 15:32:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:32:42,095 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:32:42 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 15:33:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:33:09,739 main INFO screen Flycat pass=0 dev=0.0 ins=17.72 pro=47 1a=False 1b=False 2=False (64.4s)
Sep 15 15:33:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:33:20,607 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 15 15:33:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:33:35,348 main INFO screen $OMT pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (56.1s)
Sep 15 15:34:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:12,963 main INFO screen SPUDIQ pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (52.4s)
Sep 15 15:34:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:20,199 main INFO screen ETCH pass=0 dev=0.0 ins=0.0 pro=71 1a=False 1b=False 2=False (70.5s)
Sep 15 15:34:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:34:28,016 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (52.7s)
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:35:40,328 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 15:35:40 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 15:36:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:02,539 main INFO screen DOTKO pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (109.6s)
Sep 15 15:36:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:07,650 main INFO screen FINE pass=0 dev=0.0 ins=2.43 pro=45 1a=False 1b=False 2=False (107.4s)
Sep 15 15:36:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:30,753 main INFO screen GldOnion pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (122.7s)
Sep 15 15:36:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:36:59,256 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.7s)
Sep 15 15:37:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:02,396 main INFO screen USOR/SOL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.7s)
Sep 15 15:37:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:24,711 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.0s)
Sep 15 15:37:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 15:37:42,262 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:15:37:42 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T14:12:16Z
--- update 2026-09-15T14:17:16Z
--- update 2026-09-15T14:22:18Z
--- update 2026-09-15T14:27:19Z
--- update 2026-09-15T14:32:20Z
--- update 2026-09-15T14:37:22Z
--- update 2026-09-15T14:42:23Z
--- update 2026-09-15T14:47:24Z
--- update 2026-09-15T14:52:25Z
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
```

## Analyses (laatste 40 regels)
```
active
12:14:29   500/6807 lopers, 4334 koppelingen
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
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
10:01:00 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=230 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
10:01:04 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/154 | al gemeten: 616
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
