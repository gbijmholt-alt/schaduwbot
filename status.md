# Schaduwbot status

- tijd: 2026-09-15 22:00:58 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 8 hours, 14 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.7G/38G | geheugen: 2425/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 228410, "tokens_in_memory": 11172, "msgs": 38191808, "trades": 7415877, "creates": 78590, "decode_fail": 619557, "rpc_calls": 207204, "rpc_errors": 18, "sol_usd": 96.62385424094663, "open_positions": 204, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 21:35:38 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 21:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:35:38,984 rpc WARNING rpc getSignaturesForAddress exc
Sep 15 21:35:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:35:39,052 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:35:39 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:35:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:35:45,902 main INFO screen CLAST pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (113.0s)
Sep 15 21:36:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:36:46,681 main INFO screen Hellmo pass=0 dev=0.0 ins=27.1 pro=64 1a=False 1b=False 2=True (124.4s)
Sep 15 21:36:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:36:47,626 main INFO screen ber pass=0 dev=0.0 ins=45.86 pro=67 1a=False 1b=False 2=True (123.9s)
Sep 15 21:36:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:36:57,971 main INFO screen EMNM pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=False 2=True (72.1s)
Sep 15 21:37:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:37:52,446 main INFO screen Recount pass=0 dev=0.0 ins=19.23 pro=52 1a=False 1b=False 2=True (65.8s)
Sep 15 21:37:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:37:53,008 main INFO screen THOM pass=0 dev=0.0 ins=30.76 pro=32 1a=False 1b=False 2=True (65.4s)
Sep 15 21:38:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:38:02,374 main INFO screen BOWLCUT pass=0 dev=0.73 ins=0.0 pro=2 1a=False 1b=False 2=False (64.4s)
Sep 15 21:38:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:38:55,441 main INFO screen Recount pass=0 dev=0.0 ins=20.3 pro=66 1a=False 1b=False 2=True (63.0s)
Sep 15 21:39:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:39:01,136 main INFO screen LEFT pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (68.1s)
Sep 15 21:39:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:39:03,791 main INFO screen THOM pass=0 dev=0.0 ins=35.74 pro=55 1a=False 1b=False 2=True (61.4s)
Sep 15 21:40:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:40:04,121 main INFO screen Thom pass=0 dev=0.0 ins=26.56 pro=62 1a=False 1b=False 2=True (68.7s)
Sep 15 21:40:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:40:07,842 main INFO screen THOM pass=0 dev=0.0 ins=23.91 pro=69 1a=False 1b=False 2=True (64.0s)
Sep 15 21:40:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:40:10,939 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.8s)
Sep 15 21:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:40:37,143 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:40:37 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:41:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:41:05,666 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.5s)
Sep 15 21:41:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:41:10,991 main INFO screen CAS pass=0 dev=0.04 ins=0.0 pro=40 1a=False 1b=False 2=False (63.1s)
Sep 15 21:41:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:41:18,781 main INFO screen BRIDGE pass=0 dev=0.0 ins=18.6 pro=72 1a=False 1b=False 2=False (67.8s)
Sep 15 21:42:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:42:02,618 main INFO screen LEFT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.9s)
Sep 15 21:42:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:42:23,773 main INFO screen CTC pass=0 dev=0.0 ins=25.43 pro=1 1a=False 1b=False 2=True (72.8s)
Sep 15 21:42:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:42:25,756 main INFO screen Wing pass=0 dev=0.0 ins=14.58 pro=36 1a=False 1b=False 2=False (67.0s)
Sep 15 21:43:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:43:00,953 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.3s)
Sep 15 21:43:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:43:17,045 main INFO screen SOLT pass=0 dev=0.0 ins=2.76 pro=48 1a=False 1b=False 2=False (53.3s)
Sep 15 21:43:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:43:20,182 main INFO screen CUB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.4s)
Sep 15 21:43:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:43:55,195 main INFO screen BmC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.2s)
Sep 15 21:44:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:44:19,126 main INFO screen Chud pass=0 dev=0.0 ins=26.3 pro=45 1a=False 1b=False 2=True (62.1s)
Sep 15 21:44:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:44:30,693 main INFO screen CTC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (70.5s)
Sep 15 21:45:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:45:02,937 main INFO screen Lucas pass=0 dev=0.0 ins=17.9 pro=64 1a=False 1b=False 2=True (67.7s)
Sep 15 21:45:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:45:09,479 main INFO screen VOID pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 15 21:45:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:45:19,423 main INFO screen BITBADGER pass=0 dev=0.0 ins=21.25 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 15 21:45:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:45:44,063 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:45:44 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:46:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:46:10,871 main INFO screen DOOMGUY pass=0 dev=0.0 ins=55.51 pro=70 1a=False 1b=False 2=True (67.9s)
Sep 15 21:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:46:12,252 main INFO screen blueballs pass=0 dev=0.0 ins=25.51 pro=1 1a=False 1b=False 2=False (52.8s)
Sep 15 21:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:46:15,248 main INFO screen RAKE pass=0 dev=0.0 ins=14.03 pro=42 1a=False 1b=False 2=False (65.8s)
Sep 15 21:47:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:47:17,032 main INFO screen REPLYGUY pass=0 dev=0.0 ins=13.19 pro=54 1a=False 1b=False 2=True (64.8s)
Sep 15 21:47:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:47:19,067 main INFO screen STOCK pass=0 dev=0.0 ins=20.54 pro=0 1a=False 1b=False 2=False (68.2s)
Sep 15 21:47:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:47:19,525 main INFO screen worries pass=0 dev=0.0 ins=3.56 pro=61 1a=False 1b=False 2=True (64.3s)
Sep 15 21:48:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:48:03,919 main INFO screen STOCK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (46.9s)
Sep 15 21:48:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:48:21,418 main INFO screen TRUMPLESS pass=0 dev=0.0 ins=25.53 pro=0 1a=False 1b=False 2=True (61.9s)
Sep 15 21:48:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:48:23,364 main INFO screen highcat pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (64.3s)
Sep 15 21:48:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:48:58,382 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (54.5s)
Sep 15 21:49:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:49:13,036 main WARNING stream verbroken: sent 1002 (protocol error) invalid status code; no close frame received — opnieuw over 1s
Sep 15 21:49:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:49:14,871 main INFO verbonden met wss://api.mainnet-beta.solana.com
Sep 15 21:49:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:49:33,180 main INFO screen birds pass=0 dev=0.0 ins=11.42 pro=57 1a=False 1b=False 2=True (69.8s)
Sep 15 21:49:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:49:34,971 main INFO screen CHAIN pass=0 dev=0.0 ins=0.0 pro=76 1a=False 1b=False 2=False (73.6s)
Sep 15 21:50:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:50:13,905 main INFO screen Donkeyy pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (75.5s)
Sep 15 21:50:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:50:27,156 main INFO screen DOUCHE pass=0 dev=0.0 ins=41.68 pro=7 1a=False 1b=False 2=True (52.2s)
Sep 15 21:50:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:50:28,097 main INFO screen worries pass=0 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (54.9s)
Sep 15 21:50:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:50:44,650 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:50:44 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:51:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:51:30,736 main INFO screen BARRON pass=0 dev=0.0 ins=24.99 pro=61 1a=False 1b=False 2=True (76.8s)
Sep 15 21:51:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:51:36,769 main INFO screen BARRON pass=0 dev=0.0 ins=23.58 pro=1 1a=False 1b=False 2=True (69.6s)
Sep 15 21:51:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:51:40,632 main INFO screen BIRDS pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (72.5s)
Sep 15 21:52:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:52:46,849 main INFO screen   pass=0 dev=0.0 ins=36.62 pro=58 1a=False 1b=False 2=True (76.1s)
Sep 15 21:52:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:52:47,324 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (70.6s)
Sep 15 21:52:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:52:50,453 main INFO screen CSS pass=0 dev=0.0 ins=0.0 pro=69 1a=False 1b=False 2=False (69.8s)
Sep 15 21:53:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:53:44,917 main INFO screen WOFI pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.1s)
Sep 15 21:53:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:53:45,372 main INFO screen PAID pass=0 dev=1.57 ins=10.45 pro=83 1a=False 1b=False 2=False (58.0s)
Sep 15 21:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:53:54,985 main INFO screen DIRPY pass=0 dev=0.0 ins=44.32 pro=3 1a=False 1b=False 2=True (64.5s)
Sep 15 21:54:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:54:48,430 main INFO screen biketyson pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (63.1s)
Sep 15 21:54:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:54:51,641 main INFO screen Maddie pass=0 dev=0.0 ins=50.85 pro=70 1a=False 1b=False 2=True (66.7s)
Sep 15 21:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:54:54,916 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.9s)
Sep 15 21:55:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:55:51,252 main INFO screen PEG pass=0 dev=0.0 ins=19.8 pro=0 1a=False 1b=False 2=False (62.8s)
Sep 15 21:55:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:55:52,710 main INFO screen DUMOCRATS pass=0 dev=0.0 ins=20.08 pro=1 1a=False 1b=False 2=True (61.1s)
Sep 15 21:55:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:55:54,020 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:21:55:54 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 21:55:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:55:54,342 main INFO screen XP pass=0 dev=0.0 ins=23.64 pro=0 1a=False 1b=False 2=False (59.4s)
Sep 15 21:56:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:56:44,480 main INFO screen Liquidog pass=0 dev=0.0 ins=34.17 pro=35 1a=False 1b=False 2=True (50.1s)
Sep 15 21:56:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:56:55,025 main INFO screen DOOM pass=0 dev=0.0 ins=0.32 pro=9 1a=False 1b=False 2=True (62.3s)
Sep 15 21:56:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:56:56,543 main INFO screen SCS pass=0 dev=0.0 ins=18.9 pro=64 1a=False 1b=False 2=True (65.3s)
Sep 15 21:57:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:57:55,992 main INFO screen HTML pass=0 dev=0.0 ins=7.59 pro=64 1a=False 1b=False 2=True (71.5s)
Sep 15 21:58:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:58:00,221 main INFO screen WOTF pass=0 dev=0.0 ins=125.6 pro=1 1a=False 1b=False 2=True (65.2s)
Sep 15 21:58:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:58:04,239 main INFO screen BARRON pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (67.7s)
Sep 15 21:59:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:59:09,254 main INFO screen Liquidog pass=0 dev=0.0 ins=24.97 pro=1 1a=False 1b=False 2=True (69.0s)
Sep 15 21:59:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:59:11,156 main INFO screen ELON pass=0 dev=0.0 ins=16.66 pro=75 1a=False 1b=False 2=True (75.2s)
Sep 15 21:59:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 21:59:14,727 main INFO screen HTML pass=0 dev=0.0 ins=61.03 pro=46 1a=False 1b=False 2=True (70.5s)
Sep 15 22:00:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:00:21,886 main INFO screen MooMoo pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (70.7s)
Sep 15 22:00:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:00:22,133 main INFO screen DOOM pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (72.9s)
Sep 15 22:00:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:00:23,498 main INFO screen DAVESPICK pass=0 dev=0.0 ins=28.36 pro=73 1a=False 1b=False 2=True (68.8s)
Sep 15 22:00:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 22:00:58,644 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:22:00:58 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T20:33:25Z
--- update 2026-09-15T20:38:25Z
--- update 2026-09-15T20:43:36Z
--- update 2026-09-15T20:48:53Z
--- update 2026-09-15T20:54:01Z
--- update 2026-09-15T20:59:05Z
--- update 2026-09-15T21:04:26Z
--- update 2026-09-15T21:09:35Z
Running as unit: schaduwbot-wallets.service; invocation ID: 816305a7ccbb460db17cb3d4a36ce786
analyses gestart (84579ff37485)
--- update 2026-09-15T21:14:36Z
--- update 2026-09-15T21:19:37Z
--- update 2026-09-15T21:25:02Z
--- update 2026-09-15T21:30:04Z
--- update 2026-09-15T21:35:31Z
--- update 2026-09-15T21:40:36Z
--- update 2026-09-15T21:45:43Z
--- update 2026-09-15T21:50:43Z
--- update 2026-09-15T21:55:52Z
--- update 2026-09-15T22:00:57Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 20:07:44
20:07:45 venster 2026-09-13 08:07 UTC .. nu, 70021 tokens
20:08:37 klaar in 53s: 53536 tokens, 1839 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 21:09:36
21:09:36 venster 2026-09-13 09:09 UTC .. nu, 71175 tokens
21:10:29 klaar in 53s: 54456 tokens, 1720 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
21:30:20 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=393 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:30:20 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 8/47/168 | al gemeten: 841
21:35:46 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=396 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:35:47 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 8/49/169 | al gemeten: 844
21:41:06 ijk: +6 van 8 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=402 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:41:06 ijk-diagnose: nieuwste migratie -0.3 min oud | migraties 15/60/240 min: 14/51/174 | al gemeten: 850
21:46:12 ijk: +6 van 10 kandidaten (19 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=408 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:46:13 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 19/55/174 | al gemeten: 856
21:50:51 ijk: +0 van 9 kandidaten (21 migraties in het venster, overgeslagen: {'al_gemeten': 12}) | verste bak n=408 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:50:52 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 21/56/176 | al gemeten: 856
21:55:58 ijk: +0 van 11 kandidaten (17 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=408 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
21:55:59 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 17/55/176 | al gemeten: 856
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 2771 | 297 | 293 | 0 | 56 | 4.4 min |
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
| 09-15 12:00 | 9559 | 1252 | 1159 | 12 | 0 | 76.9 min |
| 09-15 18:00 | 7565 | 322 | 301 | 318 | 0 | 141.7 min |

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
