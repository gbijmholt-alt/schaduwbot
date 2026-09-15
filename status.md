# Schaduwbot status

- tijd: 2026-09-15 08:52:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 19 hours, 5 minutes
- bot-service: active
- code-versie: 6952951
- schijf: 7.0G/38G | geheugen: 2289/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 181087, "tokens_in_memory": 6227, "msgs": 26771813, "trades": 5449035, "creates": 58226, "decode_fail": 457232, "rpc_calls": 159237, "rpc_errors": 14, "sol_usd": 100.41684482599963, "open_positions": 51, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 08:32:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:32:42,393 main INFO screen JOJO pass=0 dev=0.0 ins=16.5 pro=64 1a=False 1b=False 2=True (65.3s)
Sep 15 08:32:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:32:54,824 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:32:54 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
Sep 15 08:32:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:32:55,111 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:32:55 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 15 08:33:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:33:12,702 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (57.2s)
Sep 15 08:33:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:33:39,173 main INFO screen ASH pass=0 dev=0.0 ins=0.24 pro=26 1a=False 1b=False 2=False (69.6s)
Sep 15 08:33:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:33:41,838 main INFO screen JOJO pass=0 dev=0.0 ins=1.31 pro=30 1a=False 1b=False 2=False (59.4s)
Sep 15 08:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:34:08,974 main INFO screen FLOPPA pass=0 dev=0.0 ins=77.42 pro=4 1a=False 1b=True 2=True (56.3s)
Sep 15 08:34:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:34:30,767 main INFO screen Pactra pass=0 dev=0.0 ins=0.94 pro=24 1a=False 1b=False 2=False (51.6s)
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:35:27,816 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 08:35:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:35:27,910 rpc WARNING rpc getSignaturesForAddress exc
Sep 15 08:35:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:35:37,918 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:35:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:35:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:35:49,564 main INFO screen Stingoor pass=0 dev=1.9 ins=0.0 pro=62 1a=False 1b=False 2=False (127.7s)
Sep 15 08:35:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:35:58,331 main INFO screen ASH pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (109.4s)
Sep 15 08:36:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:36:16,837 main INFO screen KYC pass=0 dev=0.0 ins=30.69 pro=59 1a=False 1b=False 2=True (106.1s)
Sep 15 08:36:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:36:39,631 main INFO screen MEOWERO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.1s)
Sep 15 08:36:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:36:55,845 aiohttp.access INFO 45.156.128.131 [15/Sep/2026:08:36:55 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 15 08:37:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:04,896 main INFO screen APEFACE pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (66.6s)
Sep 15 08:37:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:10,314 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (53.5s)
Sep 15 08:37:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:12,458 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:37:12 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
Sep 15 08:37:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:12,745 aiohttp.access INFO 209.141.56.109 [15/Sep/2026:08:37:12 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 15 08:37:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:34,924 main INFO screen KVW pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (55.3s)
Sep 15 08:37:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:37:55,868 main INFO screen broke pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.0s)
Sep 15 08:38:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:38:02,647 main INFO screen OTC pass=0 dev=0.03 ins=97.3 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 15 08:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:38:37,569 main INFO screen にゃご pass=0 dev=0.0 ins=27.35 pro=53 1a=False 1b=False 2=True (62.6s)
Sep 15 08:39:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:39:03,692 main INFO screen BITCAT pass=0 dev=0.0 ins=12.05 pro=70 1a=False 1b=False 2=True (67.8s)
Sep 15 08:39:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:39:06,449 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.1 pro=9 1a=False 1b=False 2=True (63.8s)
Sep 15 08:39:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:39:36,362 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.8s)
Sep 15 08:40:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:40:07,746 main INFO screen SOLdiers pass=0 dev=0.0 ins=13.43 pro=53 1a=False 1b=False 2=True (64.1s)
Sep 15 08:40:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:40:14,534 main INFO screen SQUID pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (68.1s)
Sep 15 08:40:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:40:33,308 main INFO screen SpaceX pass=0 dev=0.0 ins=136.12 pro=0 1a=False 1b=False 2=True (56.9s)
Sep 15 08:41:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:41:06,647 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.1s)
Sep 15 08:41:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:41:08,533 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:41:08 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:41:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:41:16,765 main INFO screen PokeMonero pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (69.0s)
Sep 15 08:41:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:41:25,653 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.1 pro=12 1a=False 1b=False 2=False (52.3s)
Sep 15 08:42:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:42:04,867 main INFO screen BONZO pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=True 2=True (58.2s)
Sep 15 08:42:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:42:23,451 main INFO screen pork pass=0 dev=0.0 ins=18.1 pro=64 1a=False 1b=False 2=True (66.7s)
Sep 15 08:42:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:42:26,434 main INFO screen QUMIS pass=0 dev=0.0 ins=12.3 pro=50 1a=False 1b=False 2=True (60.8s)
Sep 15 08:42:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:42:56,308 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.1 pro=11 1a=False 1b=False 2=False (51.4s)
Sep 15 08:43:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:43:10,681 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (47.2s)
Sep 15 08:43:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:43:18,691 main INFO screen NJN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.3s)
Sep 15 08:43:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:43:52,373 main INFO screen BanJin pass=0 dev=0.0 ins=31.4 pro=67 1a=False 1b=False 2=True (56.1s)
Sep 15 08:44:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:44:15,618 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (64.9s)
Sep 15 08:44:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:44:17,120 main INFO screen DANGR pass=0 dev=0.0 ins=152.8 pro=1 1a=False 1b=False 2=True (58.4s)
Sep 15 08:44:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:44:43,579 main INFO screen money pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.2s)
Sep 15 08:45:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:45:18,386 main INFO screen NJN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.8s)
Sep 15 08:45:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:45:20,773 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (63.7s)
Sep 15 08:45:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:45:36,130 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.5s)
Sep 15 08:46:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:46:11,215 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.8s)
Sep 15 08:46:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:46:24,104 main INFO screen Mayhem pass=0 dev=0.01 ins=0.0 pro=10 1a=False 1b=False 2=False (63.3s)
Sep 15 08:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:46:37,693 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:46:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 08:46:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:46:40,783 main INFO screen chomik pass=0 dev=0.0 ins=20.66 pro=64 1a=False 1b=False 2=True (64.7s)
Sep 15 08:47:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:47:24,672 main INFO screen SOLANA pass=0 dev=0.0 ins=25.07 pro=69 1a=False 1b=False 2=True (73.5s)
Sep 15 08:47:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:47:34,636 main INFO screen FORK pass=0 dev=0.96 ins=0.0 pro=4 1a=False 1b=False 2=False (70.5s)
Sep 15 08:47:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:47:41,743 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.0s)
Sep 15 08:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:48:15,473 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.8s)
Sep 15 08:48:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:48:24,894 main INFO screen JOYKO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.3s)
Sep 15 08:48:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:48:44,571 main INFO screen BTTI pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (62.8s)
Sep 15 08:49:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:49:03,548 aiohttp.access INFO 16.5.0.236 [15/Sep/2026:08:49:03 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 15 08:49:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:49:05,134 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.05 pro=16 1a=False 1b=False 2=True (49.7s)
Sep 15 08:49:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:49:18,626 main INFO screen dinu pass=0 dev=0.0 ins=23.77 pro=58 1a=False 1b=False 2=False (53.7s)
Sep 15 08:49:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:49:38,342 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (53.8s)
Sep 15 08:49:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:49:56,524 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.4s)
Sep 15 08:50:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:50:07,037 main INFO screen PokeMONero pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (48.4s)
Sep 15 08:50:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:50:42,571 main INFO screen dudeova pass=0 dev=0.0 ins=14.36 pro=63 1a=False 1b=False 2=True (64.2s)
Sep 15 08:50:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:50:51,882 main INFO screen RDX pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (55.4s)
Sep 15 08:51:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:51:13,430 main INFO screen BTCAT pass=0 dev=0.0 ins=0.0 pro=66 1a=False 1b=False 2=True (66.4s)
Sep 15 08:51:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:51:36,082 main INFO screen OLTSEASON pass=0 dev=0.0 ins=0.05 pro=27 1a=False 1b=False 2=False (53.5s)
Sep 15 08:51:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:51:42,438 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.6s)
Sep 15 08:52:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:52:14,723 main INFO screen BG-5 pass=0 dev=0.0 ins=27.7 pro=61 1a=False 1b=False 2=True (61.3s)
Sep 15 08:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 08:52:15,595 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:08:52:15 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: a8d6b4f
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T07:53:56Z
--- update 2026-09-15T07:59:05Z
--- update 2026-09-15T08:04:22Z
--- update 2026-09-15T08:09:36Z
--- update 2026-09-15T08:14:58Z
--- update 2026-09-15T08:20:18Z
--- update 2026-09-15T08:25:27Z
--- update 2026-09-15T08:30:35Z
--- update 2026-09-15T08:35:36Z
nieuwe code: 03656c3
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T08:41:07Z
Running as unit: schaduwbot-wallets.service; invocation ID: fbbefad4940a4854a92f58face2550ce
analyses gestart (f5eb6a3d8915)
--- update 2026-09-15T08:46:36Z
--- update 2026-09-15T08:52:13Z
nieuwe code: 6952951
alleen analyses/documentatie gewijzigd: geen herstart
```

## Analyses (laatste 40 regels)
```
active
08:29:27   24000 tokens, 2339224 trades, 279203 posities (148s)
08:29:40   26000 tokens, 2552931 trades, 307090 posities (161s)
08:29:53   28000 tokens, 2737912 trades, 330683 posities (174s)
08:30:04   30000 tokens, 2918474 trades, 352610 posities (186s)
08:30:17   32000 tokens, 3117456 trades, 378048 posities (198s)
08:30:29   34000 tokens, 3300957 trades, 398500 posities (211s)
08:30:43   36000 tokens, 3490232 trades, 421763 posities (224s)
08:30:56   38000 tokens, 3693325 trades, 447213 posities (237s)
08:31:10   40000 tokens, 3892921 trades, 471436 posities (251s)
08:31:23   42000 tokens, 4084616 trades, 495436 posities (264s)
08:31:35   44000 tokens, 4263963 trades, 515730 posities (277s)
08:31:48   46000 tokens, 4443964 trades, 536909 posities (289s)
08:32:00   48000 tokens, 4617845 trades, 557858 posities (301s)
08:32:14   50000 tokens, 4813243 trades, 582988 posities (315s)
08:32:28   52000 tokens, 5028428 trades, 610553 posities (329s)
08:32:41   54000 tokens, 5224072 trades, 634982 posities (343s)
08:32:56   56000 tokens, 5417955 trades, 662700 posities (357s)
08:33:11   58000 tokens, 5592527 trades, 681801 posities (372s)
08:33:27   60000 tokens, 5777115 trades, 706345 posities (388s)
08:33:42   62000 tokens, 5977379 trades, 730548 posities (403s)
08:33:57   64000 tokens, 6167932 trades, 757805 posities (419s)
08:34:14   66000 tokens, 6366714 trades, 782198 posities (435s)
08:34:30   68000 tokens, 6555872 trades, 807992 posities (451s)
08:34:45   70000 tokens, 6727019 trades, 826700 posities (466s)
08:35:00   72000 tokens, 6928802 trades, 850428 posities (481s)
08:35:16   74000 tokens, 7132074 trades, 882785 posities (497s)
08:35:30 posities: 905040 uit 7299848 trades (516s)
08:35:43 209933 wallets gerekend
08:35:43 geluk-toets
08:36:18 persistentie
08:36:22 kopieer-simulatie
08:38:47 klaar in 714s -> /opt/schaduwbot/reports/wallets.md
08:41:12 106376 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
08:41:25   ingelezen tot rowid 10998740 (90133 rijen, 90133 bruikbaar)
08:41:27 ingelezen: 90133 nieuwe trades, 90133 bruikbaar (20s)
08:44:45 3000 aankopen van gevolgde wallets geëvalueerd
08:45:33 vroege kopers: 297 voldoen nu, register 522, 150 tokens beoordeeld
08:46:20 grote spelers: saldo van 380 wallets opgehaald
08:46:51 herkomst: 40 posities gekoppeld
08:47:06 klaar in 359s -> /opt/schaduwbot/reports/ledger.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
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
08:41:49 ijk: +6 van 8 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=220 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
08:41:50 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/154 | al gemeten: 590
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
