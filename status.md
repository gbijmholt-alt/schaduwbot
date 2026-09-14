# Schaduwbot status

- tijd: 2026-09-14 11:28:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 21 hours, 41 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.6G/38G | geheugen: 1917/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 104069, "tokens_in_memory": 4545, "msgs": 12408559, "trades": 2760079, "creates": 28638, "decode_fail": 229953, "rpc_calls": 82701, "rpc_errors": 7, "sol_usd": 101.7934466730203, "open_positions": 42, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 10:57:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:57:44,850 main INFO screen vrl pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=False (61.2s)
Sep 14 10:58:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:58:47,661 main INFO screen EPEP pass=1 dev=0.0 ins=7.48 pro=48 1a=False 1b=False 2=False (76.3s)
Sep 14 10:58:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:58:52,595 main INFO screen wester pass=1 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (69.2s)
Sep 14 10:58:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:58:54,010 main INFO screen blackbunny pass=0 dev=0.0 ins=36.2 pro=12 1a=False 1b=False 2=True (69.2s)
Sep 14 11:00:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:00:02,876 main INFO screen BotTrencher pass=1 dev=0.0 ins=7.38 pro=29 1a=False 1b=False 2=False (70.3s)
Sep 14 11:00:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:00:06,503 main INFO screen PHYTOS pass=0 dev=0.0 ins=16.02 pro=56 1a=False 1b=False 2=True (72.5s)
Sep 14 11:00:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:00:07,084 main INFO screen RISE pass=0 dev=40.34 ins=0.0 pro=6 1a=False 1b=False 2=False (79.4s)
Sep 14 11:01:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:01:06,385 main INFO screen FrogCat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.5s)
Sep 14 11:01:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:01:13,131 main INFO screen PHYTOS pass=1 dev=0.0 ins=1.67 pro=26 1a=False 1b=False 2=False (66.0s)
Sep 14 11:01:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:01:15,814 main INFO screen ElonCoin pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (69.3s)
Sep 14 11:02:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:02:05,382 main INFO screen Amana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 14 11:02:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:02:19,198 main INFO screen TUFF pass=1 dev=0.0 ins=16.45 pro=35 1a=False 1b=False 2=False (66.1s)
Sep 14 11:02:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:02:25,325 main INFO screen BIKEBAN pass=0 dev=0.05 ins=79.26 pro=8 1a=False 1b=False 2=True (69.5s)
Sep 14 11:02:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:02:27,268 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:02:27 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:03:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:03:22,365 main INFO screen Jabal pass=0 dev=0.0 ins=27.07 pro=32 1a=False 1b=False 2=False (77.0s)
Sep 14 11:03:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:03:25,771 main INFO screen Jabali pass=0 dev=0.0 ins=24.76 pro=56 1a=False 1b=False 2=False (66.6s)
Sep 14 11:03:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:03:36,481 main INFO screen Uranus420 pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (71.2s)
Sep 14 11:04:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:04:29,046 main INFO screen Jabal pass=0 dev=0.0 ins=24.76 pro=64 1a=False 1b=False 2=False (66.7s)
Sep 14 11:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:04:38,220 main INFO screen what pass=0 dev=0.0 ins=2.76 pro=3 1a=False 1b=False 2=False (72.4s)
Sep 14 11:04:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:04:41,070 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.6s)
Sep 14 11:05:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:05:29,598 main INFO screen chillbike pass=0 dev=0.0 ins=33.53 pro=5 1a=False 1b=False 2=True (60.6s)
Sep 14 11:05:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:05:47,080 main INFO screen Phytos pass=1 dev=0.0 ins=11.38 pro=36 1a=False 1b=False 2=False (66.0s)
Sep 14 11:05:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:05:48,146 main INFO screen Jabal pass=1 dev=0.0 ins=1.87 pro=79 1a=False 1b=False 2=False (69.9s)
Sep 14 11:06:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:06:29,099 main INFO screen SHITCOIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 14 11:06:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:06:58,535 main INFO screen . pass=0 dev=0.26 ins=0.0 pro=3 1a=False 1b=False 2=False (71.5s)
Sep 14 11:07:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:07:00,035 main INFO screen ricky pass=1 dev=0.18 ins=0.0 pro=11 1a=False 1b=False 2=False (71.9s)
Sep 14 11:07:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:07:37,385 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:07:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:07:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:07:40,850 main INFO screen meincat pass=1 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (71.7s)
Sep 14 11:08:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:10,844 main INFO screen جَبَل pass=1 dev=0.0 ins=1.3 pro=82 1a=False 1b=False 2=False (70.8s)
Sep 14 11:08:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:11,519 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.0s)
Sep 14 11:08:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:21,907 aiohttp.access INFO 165.227.158.49 [14/Sep/2026:11:08:21 +0000] "GET / HTTP/1.0" 404 174 "-" "-"
Sep 14 11:08:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:22,111 aiohttp.access INFO 161.35.199.243 [14/Sep/2026:11:08:22 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 11:08:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:22,111 aiohttp.access INFO 164.90.173.183 [14/Sep/2026:11:08:22 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Odin; https://docs.getodin.com/)"
Sep 14 11:08:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:22,122 aiohttp.access INFO 161.35.199.243 [14/Sep/2026:11:08:22 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 11:08:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:22,128 aiohttp.access INFO 167.172.99.144 [14/Sep/2026:11:08:22 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 14 11:08:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:08:51,982 main INFO screen lostB pass=0 dev=0.0 ins=0.21 pro=7 1a=False 1b=False 2=False (71.1s)
Sep 14 11:09:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:09:08,352 main INFO screen ElonMusket pass=0 dev=0.0 ins=77.57 pro=3 1a=False 1b=True 2=True (57.5s)
Sep 14 11:09:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:09:17,423 main INFO screen shznzh pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.9s)
Sep 14 11:09:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:09:55,969 main INFO screen VOID pass=0 dev=42.5 ins=0.14 pro=1 1a=False 1b=False 2=False (64.0s)
Sep 14 11:10:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:10:26,612 main INFO screen INU pass=0 dev=0.44 ins=53.17 pro=33 1a=False 1b=False 2=True (78.3s)
Sep 14 11:11:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:11:33,473 main INFO screen DARWIN pass=0 dev=0.67 ins=0.0 pro=4 1a=False 1b=False 2=False (63.1s)
Sep 14 11:12:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:12:51,113 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:12:51 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:12:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:12:56,968 main INFO screen fomo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.0s)
Sep 14 11:14:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:14:05,913 main INFO screen PEPEPONS pass=0 dev=0.19 ins=79.12 pro=7 1a=False 1b=True 2=True (58.7s)
Sep 14 11:14:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:14:19,724 main INFO screen SPOOK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (67.0s)
Sep 14 11:15:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:15:26,232 main INFO screen Tina pass=1 dev=0.0 ins=14.2 pro=50 1a=False 1b=False 2=False (65.6s)
Sep 14 11:15:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:15:29,971 main INFO screen NELO pass=0 dev=0.0 ins=31.14 pro=44 1a=False 1b=True 2=True (72.1s)
Sep 14 11:15:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:15:39,330 main INFO screen fg pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (68.4s)
Sep 14 11:16:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:16:19,543 main INFO screen ☠️ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.3s)
Sep 14 11:16:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:16:23,398 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.4s)
Sep 14 11:16:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:16:55,445 main INFO screen DOOROC pass=0 dev=0.14 ins=0.0 pro=6 1a=False 1b=False 2=False (66.8s)
Sep 14 11:17:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:17:33,049 main INFO screen SUPERINT pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (69.7s)
Sep 14 11:17:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:17:34,361 main INFO screen hbt pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (74.8s)
Sep 14 11:17:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:17:57,622 main INFO screen dishes pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (62.2s)
Sep 14 11:17:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:17:59,031 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:17:59 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
Sep 14 11:18:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:18:47,447 main INFO screen Tina pass=1 dev=0.0 ins=11.09 pro=69 1a=False 1b=False 2=False (73.1s)
Sep 14 11:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:18:49,262 main INFO screen EmberGPT pass=0 dev=0.0 ins=79.11 pro=14 1a=False 1b=False 2=True (76.2s)
Sep 14 11:19:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:19:14,280 main INFO screen MOJO pass=0 dev=0.44 ins=53.17 pro=22 1a=False 1b=False 2=True (76.7s)
Sep 14 11:19:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:19:58,183 main INFO screen AME pass=0 dev=0.0 ins=0.69 pro=2 1a=False 1b=False 2=False (68.9s)
Sep 14 11:20:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:20:02,154 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=5 1a=False 1b=False 2=True (74.7s)
Sep 14 11:20:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:20:24,310 main INFO screen beer pass=1 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (70.0s)
Sep 14 11:20:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:20:53,772 main INFO screen MAN pass=0 dev=0.0 ins=27.14 pro=37 1a=False 1b=False 2=True (55.6s)
Sep 14 11:21:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:21:16,918 main INFO screen SPOOK pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (74.8s)
Sep 14 11:21:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:21:17,744 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 14 11:21:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:21:52,628 main INFO screen TWINEGUY pass=0 dev=0.35 ins=78.96 pro=5 1a=False 1b=True 2=True (58.9s)
Sep 14 11:22:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:22:09,501 main INFO screen Doggo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.6s)
Sep 14 11:22:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:22:14,352 main INFO screen corny pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 14 11:22:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:22:59,330 main INFO screen W pass=1 dev=0.0 ins=0.01 pro=67 1a=False 1b=False 2=False (66.7s)
Sep 14 11:23:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:23:05,641 main INFO screen DANCINGCATE pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (56.1s)
Sep 14 11:23:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:23:07,139 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:23:07 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 11:23:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:23:51,936 main INFO screen MOON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.1s)
Sep 14 11:24:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:24:34,489 main INFO screen TOAD pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (67.7s)
Sep 14 11:24:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:24:52,661 main INFO screen ILANDS pass=0 dev=0.0 ins=22.54 pro=49 1a=False 1b=False 2=True (65.8s)
Sep 14 11:25:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:25:53,214 main INFO screen Gamer pass=1 dev=0.0 ins=15.99 pro=30 1a=False 1b=False 2=False (57.0s)
Sep 14 11:26:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:26:06,942 main INFO screen COON pass=0 dev=2.0 ins=32.24 pro=41 1a=True 1b=True 2=True (55.2s)
Sep 14 11:26:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:26:45,263 main INFO screen kittylick pass=0 dev=0.24 ins=0.0 pro=4 1a=False 1b=False 2=False (67.0s)
Sep 14 11:27:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:27:41,070 main INFO screen CHUDGPT pass=0 dev=0.19 ins=79.12 pro=7 1a=False 1b=True 2=True (55.5s)
Sep 14 11:28:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:28:09,404 main INFO screen TrueIQ pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (70.3s)
Sep 14 11:28:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:28:12,455 main INFO screen DPCA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.5s)
Sep 14 11:28:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 11:28:37,189 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:11:28:37 +0000] "GET /health HTTP/1.1" 200 506 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T09:49:36Z
--- update 2026-09-14T09:54:37Z
--- update 2026-09-14T09:59:41Z
--- update 2026-09-14T10:05:20Z
--- update 2026-09-14T10:10:36Z
--- update 2026-09-14T10:15:50Z
--- update 2026-09-14T10:20:56Z
--- update 2026-09-14T10:26:04Z
--- update 2026-09-14T10:31:04Z
--- update 2026-09-14T10:36:11Z
--- update 2026-09-14T10:41:17Z
--- update 2026-09-14T10:46:36Z
--- update 2026-09-14T10:52:03Z
--- update 2026-09-14T10:57:13Z
--- update 2026-09-14T11:02:26Z
--- update 2026-09-14T11:07:36Z
--- update 2026-09-14T11:12:50Z
--- update 2026-09-14T11:17:57Z
--- update 2026-09-14T11:23:05Z
--- update 2026-09-14T11:28:36Z
```

## Analyses (laatste 25 regels)
```
inactive
10:17:17   34000 tokens, 3445797 trades, 426946 posities (228s)
10:17:31   36000 tokens, 3663031 trades, 454723 posities (243s)
10:17:46   38000 tokens, 3863147 trades, 480598 posities (258s)
10:18:00   40000 tokens, 4059696 trades, 501889 posities (272s)
10:18:13   42000 tokens, 4235861 trades, 522161 posities (284s)
10:18:26   44000 tokens, 4436601 trades, 546540 posities (298s)
10:18:37   46000 tokens, 4625596 trades, 570049 posities (308s)
10:18:49   48000 tokens, 4836921 trades, 596160 posities (320s)
10:18:59   50000 tokens, 5034151 trades, 618091 posities (331s)
10:19:10   52000 tokens, 5217058 trades, 639850 posities (341s)
10:19:21   54000 tokens, 5400605 trades, 660082 posities (353s)
10:19:32   56000 tokens, 5595459 trades, 686652 posities (364s)
10:19:43   58000 tokens, 5779455 trades, 707835 posities (374s)
10:19:55   60000 tokens, 5978226 trades, 735178 posities (386s)
10:20:06   62000 tokens, 6177793 trades, 763023 posities (398s)
10:20:19   64000 tokens, 6387196 trades, 789703 posities (410s)
10:20:31   66000 tokens, 6583185 trades, 815152 posities (422s)
10:20:42   68000 tokens, 6781231 trades, 844581 posities (434s)
10:20:55   70000 tokens, 6994817 trades, 881795 posities (446s)
10:21:01 posities: 893845 uit 7089253 trades (456s)
10:21:15 197310 wallets gerekend
10:21:15 geluk-toets
10:21:55 persistentie
10:21:58 kopieer-simulatie
10:24:01 klaar in 636s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
10:31:05 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:36:12 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:41:18 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:46:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:52:03 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:57:13 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:02:26 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:07:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:12:50 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:17:58 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:23:06 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
11:28:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
