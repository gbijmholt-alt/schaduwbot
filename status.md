# Schaduwbot status

- tijd: 2026-09-14 22:27:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 8 hours, 40 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.4G/38G | geheugen: 2902/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 143609, "tokens_in_memory": 11370, "msgs": 20678096, "trades": 4297251, "creates": 45712, "decode_fail": 380988, "rpc_calls": 121881, "rpc_errors": 12, "sol_usd": 103.18012472347411, "open_positions": 64, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 22:01:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:01:38,776 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 14 22:02:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:02:18,313 main INFO screen DOJACAT pass=0 dev=0.0 ins=26.51 pro=61 1a=False 1b=False 2=False (59.7s)
Sep 14 22:02:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:02:31,624 main INFO screen WOFI pass=0 dev=0.0 ins=144.86 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 14 22:02:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:02:35,199 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (56.4s)
Sep 14 22:03:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:03:15,233 main INFO screen MUSA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.9s)
Sep 14 22:03:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:03:42,293 main INFO screen Progress pass=0 dev=0.0 ins=8.76 pro=68 1a=False 1b=False 2=False (70.7s)
Sep 14 22:03:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:03:47,002 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (71.8s)
Sep 14 22:04:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:04:19,881 main INFO screen btc pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (64.6s)
Sep 14 22:04:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:04:41,839 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (59.5s)
Sep 14 22:04:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:04:58,661 main INFO screen ROBOELON pass=0 dev=0.0 ins=9.58 pro=3 1a=False 1b=False 2=False (71.7s)
Sep 14 22:05:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:05:32,194 main INFO screen ADWIOS pass=0 dev=0.0 ins=28.2 pro=66 1a=False 1b=False 2=True (72.3s)
Sep 14 22:06:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:06:02,541 main INFO screen Clarity pass=0 dev=0.0 ins=16.91 pro=67 1a=False 1b=False 2=True (80.7s)
Sep 14 22:06:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:06:07,615 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 14 22:06:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:06:31,520 main INFO screen BUSTER pass=0 dev=0.0 ins=21.29 pro=11 1a=False 1b=False 2=True (59.3s)
Sep 14 22:06:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:06:37,180 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:06:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 22:07:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:07:01,676 main INFO screen MUSA pass=0 dev=0.44 ins=0.0 pro=1 1a=False 1b=False 2=False (59.1s)
Sep 14 22:07:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:07:19,854 main INFO screen ADWIOS pass=0 dev=0.0 ins=11.84 pro=3 1a=False 1b=False 2=True (72.2s)
Sep 14 22:07:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:07:49,331 main INFO screen koby pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.8s)
Sep 14 22:08:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:08:27,475 main INFO screen Clarity pass=0 dev=0.0 ins=31.46 pro=11 1a=False 1b=False 2=True (85.8s)
Sep 14 22:08:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:08:32,494 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.6s)
Sep 14 22:08:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:08:56,914 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.6s)
Sep 14 22:09:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:09:27,532 main INFO screen FERALFOX pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=True (60.1s)
Sep 14 22:09:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:09:36,450 main INFO screen 1000men pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.0s)
Sep 14 22:09:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:09:48,247 main INFO screen Clarity pass=0 dev=0.0 ins=24.06 pro=39 1a=False 1b=False 2=True (51.3s)
Sep 14 22:10:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:10:34,538 main INFO screen SEMI pass=0 dev=3.42 ins=75.89 pro=0 1a=False 1b=True 2=True (67.0s)
Sep 14 22:10:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:10:57,385 main INFO screen BREAD pass=0 dev=0.04 ins=0.0 pro=47 1a=False 1b=False 2=True (80.9s)
Sep 14 22:11:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:11:04,007 main INFO screen LECORN pass=0 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (75.8s)
Sep 14 22:11:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:11:37,475 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:11:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 22:11:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:11:39,299 main INFO screen btc pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.8s)
Sep 14 22:11:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:11:59,592 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=0 1a=False 1b=False 2=True (62.2s)
Sep 14 22:12:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:12:05,119 main INFO screen Buster pass=0 dev=0.0 ins=29.03 pro=68 1a=False 1b=False 2=True (61.1s)
Sep 14 22:12:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:12:43,398 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.1s)
Sep 14 22:13:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:11,590 main INFO screen BLUEPILL pass=0 dev=0.0 ins=40.41 pro=35 1a=False 1b=False 2=True (72.0s)
Sep 14 22:13:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:23,813 main INFO screen LEOPARDO pass=0 dev=2.06 ins=32.54 pro=67 1a=False 1b=False 2=True (78.7s)
Sep 14 22:13:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:32,501 rpc WARNING rpc getTokenAccountsByOwner error {'code': 503, 'message': 'Service unavailable'}
Sep 14 22:13:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:39,015 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.6s)
Sep 14 22:13:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:57,531 rpc WARNING rpc getTokenAccountsByOwner error {'code': 503, 'message': 'Service unavailable'}
Sep 14 22:13:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:13:58,186 main INFO screen Lummis pass=0 dev=0.0 ins=25.67 pro=60 1a=False 1b=False 2=True (46.6s)
Sep 14 22:14:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:11,654 rpc WARNING rpc getTokenAccountsByOwner error {'code': 503, 'message': 'Service unavailable'}
Sep 14 22:14:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:16,499 main INFO screen BIKEWOJAK pass=0 dev=0.35 ins=78.96 pro=2 1a=False 1b=True 2=True (52.7s)
Sep 14 22:14:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:27,570 rpc WARNING rpc getTokenAccountsByOwner error {'code': 503, 'message': 'Service unavailable'}
Sep 14 22:14:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:33,418 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.4s)
Sep 14 22:14:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:46,528 rpc WARNING rpc getTokenAccountsByOwner error {'code': 503, 'message': 'Service unavailable'}
Sep 14 22:14:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:14:51,365 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 14 22:15:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:15:21,925 main INFO screen DRYRUN pass=0 dev=4.89 ins=14.88 pro=69 1a=False 1b=False 2=True (65.4s)
Sep 14 22:15:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:15:43,095 main INFO screen BassHunt pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.7s)
Sep 14 22:16:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:16:01,586 main INFO screen mojo pass=0 dev=0.0 ins=49.83 pro=22 1a=False 1b=False 2=True (70.2s)
Sep 14 22:16:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:16:35,126 main INFO screen Instantly pass=0 dev=0.0 ins=12.14 pro=2 1a=False 1b=False 2=False (73.2s)
Sep 14 22:16:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:16:40,016 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:16:40 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:16:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:16:46,137 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 14 22:17:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:17:10,615 main INFO screen Cody pass=0 dev=0.0 ins=10.7 pro=3 1a=False 1b=False 2=False (69.0s)
Sep 14 22:17:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:17:47,064 main INFO screen Feral pass=0 dev=0.0 ins=16.19 pro=72 1a=False 1b=False 2=True (71.9s)
Sep 14 22:17:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:17:59,487 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (73.3s)
Sep 14 22:18:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:18:17,180 main INFO screen OpenAI pass=0 dev=0.0 ins=35.67 pro=1 1a=False 1b=False 2=True (66.6s)
Sep 14 22:18:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:18:54,422 main INFO screen 1SOL pass=0 dev=0.22 ins=35.1 pro=67 1a=False 1b=False 2=True (67.4s)
Sep 14 22:18:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:18:58,646 main INFO screen BLUEPILL pass=0 dev=0.0 ins=41.58 pro=3 1a=False 1b=False 2=True (59.2s)
Sep 14 22:19:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:19:25,526 main INFO screen yahoo pass=0 dev=0.0 ins=10.46 pro=69 1a=False 1b=False 2=True (68.3s)
Sep 14 22:20:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:20:13,233 main INFO screen MOTO pass=0 dev=0.0 ins=11.2 pro=4 1a=False 1b=False 2=False (78.8s)
Sep 14 22:20:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:20:14,109 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (75.5s)
Sep 14 22:20:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:20:38,273 main INFO screen LASER pass=0 dev=0.0 ins=23.36 pro=72 1a=False 1b=False 2=True (72.7s)
Sep 14 22:21:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:27,735 main INFO screen ROGE pass=0 dev=0.0 ins=9.81 pro=1 1a=False 1b=False 2=False (74.5s)
Sep 14 22:21:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:28,942 main INFO screen Kongal pass=0 dev=0.0 ins=10.28 pro=5 1a=False 1b=False 2=False (74.8s)
Sep 14 22:21:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:21:49,882 main INFO screen LASER pass=0 dev=0.0 ins=29.94 pro=51 1a=False 1b=False 2=True (71.6s)
Sep 14 22:22:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:16,916 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:22:16 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:22:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:35,115 main INFO screen VIVET pass=0 dev=0.0 ins=0.0 pro=30 1a=False 1b=False 2=False (67.4s)
Sep 14 22:22:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:44,099 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.2s)
Sep 14 22:22:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:22:50,414 main INFO screen MOONTICKET pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (60.5s)
Sep 14 22:23:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:35,290 main INFO screen DOWN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 14 22:23:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:44,793 main INFO screen Raven pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 14 22:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:23:47,767 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (57.4s)
Sep 14 22:24:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:31,820 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 14 22:24:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:44,301 main INFO screen DOGE pass=0 dev=0.0 ins=44.01 pro=41 1a=False 1b=True 2=True (59.5s)
Sep 14 22:24:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:24:53,533 main INFO screen INU pass=0 dev=3.65 ins=0.0 pro=4 1a=False 1b=False 2=False (65.8s)
Sep 14 22:25:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:47,342 main INFO screen DTK pass=0 dev=0.18 ins=0.0 pro=7 1a=False 1b=False 2=False (75.5s)
Sep 14 22:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:52,554 main INFO screen PoCat pass=0 dev=0.0 ins=3.39 pro=3 1a=False 1b=False 2=False (68.3s)
Sep 14 22:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:25:52,981 main INFO screen BIKEWOJAK pass=0 dev=0.0 ins=0.25 pro=5 1a=False 1b=False 2=False (59.4s)
Sep 14 22:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:00,064 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.5s)
Sep 14 22:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:00,240 main INFO screen LION KING pass=0 dev=0.0 ins=2.51 pro=24 1a=False 1b=False 2=False (72.9s)
Sep 14 22:27:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:03,303 main INFO screen BJS pass=0 dev=0.0 ins=0.0 pro=34 1a=False 1b=False 2=True (70.3s)
Sep 14 22:27:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:27:37,633 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:27:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: 2a95007
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-14T21:07:54Z
--- update 2026-09-14T21:13:21Z
--- update 2026-09-14T21:18:29Z
--- update 2026-09-14T21:23:36Z
--- update 2026-09-14T21:28:54Z
--- update 2026-09-14T21:34:36Z
--- update 2026-09-14T21:39:39Z
--- update 2026-09-14T21:45:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5eee46075898481b8005cdd132a55989
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T21:50:36Z
--- update 2026-09-14T21:55:44Z
--- update 2026-09-14T22:01:30Z
--- update 2026-09-14T22:06:35Z
--- update 2026-09-14T22:11:36Z
--- update 2026-09-14T22:16:38Z
--- update 2026-09-14T22:22:15Z
--- update 2026-09-14T22:27:36Z
```

## Analyses (laatste 25 regels)
```
active
22:21:53   32000 tokens, 3125868 trades, 381464 posities (208s)
22:22:07   34000 tokens, 3314663 trades, 402947 posities (222s)
22:22:22   36000 tokens, 3516117 trades, 427948 posities (236s)
22:22:35   38000 tokens, 3709788 trades, 448598 posities (250s)
22:22:50   40000 tokens, 3900481 trades, 473390 posities (264s)
22:23:04   42000 tokens, 4086379 trades, 492462 posities (278s)
22:23:17   44000 tokens, 4260028 trades, 515191 posities (291s)
22:23:30   46000 tokens, 4445005 trades, 537426 posities (305s)
22:23:44   48000 tokens, 4620265 trades, 558280 posities (319s)
22:23:59   50000 tokens, 4822700 trades, 580896 posities (334s)
22:24:14   52000 tokens, 5032898 trades, 607308 posities (349s)
22:24:28   54000 tokens, 5221391 trades, 629728 posities (363s)
22:24:42   56000 tokens, 5390312 trades, 650213 posities (377s)
22:24:58   58000 tokens, 5581326 trades, 674058 posities (393s)
22:25:12   60000 tokens, 5766236 trades, 695878 posities (407s)
22:25:27   62000 tokens, 5971487 trades, 721683 posities (422s)
22:25:40   64000 tokens, 6162947 trades, 750238 posities (435s)
22:25:55   66000 tokens, 6381573 trades, 779020 posities (450s)
22:26:08   68000 tokens, 6564687 trades, 802231 posities (463s)
22:26:23   70000 tokens, 6758719 trades, 827352 posities (478s)
22:26:37   72000 tokens, 6950951 trades, 853949 posities (492s)
22:26:52   74000 tokens, 7146187 trades, 885103 posities (506s)
22:26:56 posities: 891065 uit 7198322 trades (512s)
22:27:09 209874 wallets gerekend
22:27:10 geluk-toets
```

## IJking poolkoers (laatste 12 regels)
```
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
20:37:27 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:37:27 ijk-diagnose: nieuwste migratie 3.1 min oud | migraties 15/60/240 min: 13/46/185 | al gemeten: 229
20:42:38 ijk: +0 | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:42:38 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 16/48/184 | al gemeten: 229
20:47:38 ijk: +0 van 0 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 11}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:47:39 ijk-diagnose: nieuwste migratie 3.5 min oud | migraties 15/60/240 min: 11/45/183 | al gemeten: 229
20:52:38 ijk: +0 van 0 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 0, 'geen_curveprijs': 9}) | verste bak n=3 -> nog 12 metingen binnen 5 minuten na de migratie te gaan
20:52:39 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 9/43/182 | al gemeten: 229
21:45:44 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=7 -> nog 8 metingen binnen 5 minuten na de migratie te gaan
21:45:46 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 12/43/183 | al gemeten: 250
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
