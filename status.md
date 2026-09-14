# Schaduwbot status

- tijd: 2026-09-14 22:11:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 8 hours, 24 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.4G/38G | geheugen: 2198/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 142649, "tokens_in_memory": 11338, "msgs": 20500594, "trades": 4252554, "creates": 45223, "decode_fail": 375873, "rpc_calls": 120930, "rpc_errors": 7, "sol_usd": 103.36299403848352, "open_positions": 67, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 21:45:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:45:35,323 main INFO screen CASHCATGPT pass=0 dev=0.0 ins=79.27 pro=2 1a=False 1b=False 2=True (77.7s)
Sep 14 21:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:45:45,777 main INFO screen RAVIOLI pass=0 dev=0.0 ins=32.33 pro=42 1a=False 1b=False 2=True (55.3s)
Sep 14 21:46:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:46:15,103 main INFO screen MOG pass=0 dev=0.0 ins=0.44 pro=14 1a=False 1b=True 2=False (52.0s)
Sep 14 21:46:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:46:33,364 main INFO screen DUDE pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (58.0s)
Sep 14 21:46:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:46:40,764 main INFO screen wombat pass=0 dev=0.0 ins=30.43 pro=63 1a=False 1b=False 2=True (55.0s)
Sep 14 21:47:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:47:09,906 main INFO screen PORTNOY pass=0 dev=0.0 ins=33.98 pro=73 1a=False 1b=False 2=True (54.8s)
Sep 14 21:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:47:27,939 main INFO screen updown  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.6s)
Sep 14 21:47:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:47:33,888 main INFO screen Shibabull pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.1s)
Sep 14 21:47:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:47:59,067 main INFO screen BINAFFLECK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.2s)
Sep 14 21:48:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:48:34,022 main INFO screen Nubzuki pass=0 dev=0.0 ins=18.23 pro=55 1a=False 1b=False 2=True (66.1s)
Sep 14 21:48:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:48:38,752 main INFO screen GhostSwap pass=0 dev=0.0 ins=25.28 pro=2 1a=False 1b=False 2=True (64.9s)
Sep 14 21:48:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:48:53,880 main INFO screen SPOOK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.8s)
Sep 14 21:49:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:49:25,173 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (51.1s)
Sep 14 21:49:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:49:38,674 main INFO screen ⁠$Cat pass=0 dev=1.15 ins=0.0 pro=2 1a=False 1b=False 2=False (59.9s)
Sep 14 21:49:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:49:55,961 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.1s)
Sep 14 21:50:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:50:20,005 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.8s)
Sep 14 21:50:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:50:37,554 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:50:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:50:48,331 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.7s)
Sep 14 21:50:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:50:50,270 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.3s)
Sep 14 21:51:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:51:11,425 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 14 21:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:51:54,168 main INFO screen JACO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.9s)
Sep 14 21:51:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:51:56,591 main INFO screen Skeleton pass=0 dev=0.0 ins=8.1 pro=65 1a=False 1b=False 2=False (68.3s)
Sep 14 21:52:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:52:17,287 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (65.9s)
Sep 14 21:53:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:00,550 main INFO screen 1000daddy pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (64.0s)
Sep 14 21:53:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:01,332 main INFO screen DJD pass=0 dev=0.0 ins=5.81 pro=43 1a=False 1b=False 2=False (67.2s)
Sep 14 21:53:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:09,025 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.7s)
Sep 14 21:53:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:49,093 main INFO screen Hope pass=0 dev=0.0 ins=22.84 pro=18 1a=False 1b=False 2=False (47.8s)
Sep 14 21:53:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:52,157 main INFO screen INJECTION pass=0 dev=0.0 ins=40.52 pro=3 1a=False 1b=False 2=True (51.6s)
Sep 14 21:53:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:53:58,957 main INFO screen DURVX pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.9s)
Sep 14 21:54:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:54:52,202 main INFO screen troll7 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.1s)
Sep 14 21:55:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:55:02,471 main INFO screen Hope pass=0 dev=0.0 ins=21.53 pro=71 1a=False 1b=False 2=True (70.3s)
Sep 14 21:55:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:55:05,429 main INFO screen Anthropic pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (66.5s)
Sep 14 21:55:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:55:45,803 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:21:55:45 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 21:55:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:55:48,820 main INFO screen $EGG pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (56.6s)
Sep 14 21:56:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:56:17,010 main INFO screen WASHED pass=0 dev=0.0 ins=0.0 pro=73 1a=False 1b=False 2=True (74.5s)
Sep 14 21:56:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:56:20,814 main INFO screen floker pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (75.4s)
Sep 14 21:57:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:57:06,898 main INFO screen Hope pass=0 dev=0.0 ins=13.59 pro=34 1a=False 1b=False 2=True (78.1s)
Sep 14 21:57:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:57:19,245 main INFO screen lmao pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (62.2s)
Sep 14 21:57:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:57:21,456 main INFO screen Hope pass=0 dev=0.0 ins=13.36 pro=37 1a=False 1b=False 2=False (60.6s)
Sep 14 21:57:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:57:35,723 aiohttp.access INFO 94.154.43.254 [14/Sep/2026:21:57:35 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 14 21:58:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:58:08,150 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 14 21:58:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:58:16,617 main INFO screen VINDIESEL pass=0 dev=0.0 ins=78.96 pro=2 1a=False 1b=True 2=True (57.4s)
Sep 14 21:58:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:58:17,878 main INFO screen WASHED pass=0 dev=0.0 ins=31.43 pro=18 1a=False 1b=False 2=True (56.4s)
Sep 14 21:59:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:59:05,595 main INFO screen SolLama pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.4s)
Sep 14 21:59:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:59:25,628 main INFO screen Charlie pass=0 dev=0.0 ins=11.38 pro=34 1a=False 1b=False 2=False (69.0s)
Sep 14 21:59:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 21:59:25,780 main INFO screen HIVE pass=0 dev=0.0 ins=10.16 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 14 22:00:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:00:18,938 main INFO screen GEORGEBUSH pass=0 dev=0.0 ins=3.39 pro=55 1a=False 1b=False 2=False (73.3s)
Sep 14 22:00:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:00:33,028 main INFO screen HYBRID pass=0 dev=0.0 ins=37.17 pro=46 1a=False 1b=False 2=True (67.2s)
Sep 14 22:00:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:00:38,837 main INFO screen ROO pass=0 dev=0.0 ins=26.23 pro=51 1a=False 1b=False 2=True (73.2s)
Sep 14 22:01:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:01:18,620 main INFO screen PYDHT2 pass=0 dev=0.04 ins=0.0 pro=57 1a=False 1b=False 2=True (59.7s)
Sep 14 22:01:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:01:32,012 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:22:01:32 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 14 22:01:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 22:01:33,122 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.1s)
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
```

## Update-log (laatste 20 regels)
```
analyses gestart (d1af81359b25)
--- update 2026-09-14T20:57:35Z
--- update 2026-09-14T21:02:36Z
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
```

## Analyses (laatste 25 regels)
```
active
21:35:52   70000 tokens, 6811620 trades, 838817 posities (499s)
21:36:08   72000 tokens, 7007378 trades, 867280 posities (515s)
21:36:24   74000 tokens, 7207555 trades, 898587 posities (531s)
21:36:28 posities: 902419 uit 7239579 trades (537s)
21:36:41 209406 wallets gerekend
21:36:41 geluk-toets
21:37:17 persistentie
21:37:20 kopieer-simulatie
21:39:47 klaar in 736s -> /opt/schaduwbot/reports/wallets.md
21:45:09 92805 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
21:45:30   ingelezen tot rowid 9766626 (136986 rijen, 136986 bruikbaar)
21:45:32 ingelezen: 136986 nieuwe trades, 136986 bruikbaar (26s)
21:48:14 3000 aankopen van gevolgde wallets geëvalueerd
21:49:05 vroege kopers: 258 voldoen nu, register 456, 184 tokens beoordeeld
21:49:33 grote spelers: saldo van 19 wallets opgehaald
21:50:01 herkomst: 40 posities gekoppeld
21:50:14 klaar in 308s -> /opt/schaduwbot/reports/ledger.md
22:02:54 S1: gezakt — toets n=25948, verkennend n=14656
22:02:54 klaar in 760s -> /opt/schaduwbot/reports/hypotheses.md
22:02:55 probe: 140 transacties ophalen
22:06:02 poolveld: 6 pools bekeken, 0 te gaan -> vastgesteld @43
22:07:15 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
22:07:15 prijsijk: n=7 -> nog 8 metingen binnen 5 minuten na de migratie te gaan
22:07:16 na-migratie: 100 paren te checken
22:08:58 na-migratie: 40 paren, 1 prijzen
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
