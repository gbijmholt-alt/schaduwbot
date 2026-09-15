# Schaduwbot status

- tijd: 2026-09-15 23:40:32 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 9 hours, 53 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.8G/38G | geheugen: 2451/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 234384, "tokens_in_memory": 11643, "msgs": 41447211, "trades": 7757469, "creates": 82065, "decode_fail": 641189, "rpc_calls": 213304, "rpc_errors": 19, "sol_usd": 96.8441767755806, "open_positions": 130, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 23:17:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:17:24,215 main INFO screen OFF pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (55.7s)
Sep 15 23:18:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:18,734 main INFO screen FLY pass=0 dev=0.0 ins=28.95 pro=60 1a=False 1b=False 2=True (67.1s)
Sep 15 23:18:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:19,126 main INFO screen BANKS pass=0 dev=0.04 ins=0.0 pro=74 1a=False 1b=False 2=False (65.4s)
Sep 15 23:18:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:18:31,530 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (67.3s)
Sep 15 23:19:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:24,316 main INFO screen Inuvation pass=0 dev=0.0 ins=15.33 pro=33 1a=False 1b=False 2=False (65.6s)
Sep 15 23:19:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:27,763 main INFO screen WWR pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (68.6s)
Sep 15 23:19:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:32,968 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:19:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:19:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:19:45,118 main INFO screen GAS pass=0 dev=0.0 ins=49.11 pro=16 1a=False 1b=False 2=True (73.6s)
Sep 15 23:20:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:18,319 main INFO screen leaf pass=0 dev=0.0 ins=36.38 pro=46 1a=False 1b=False 2=True (50.6s)
Sep 15 23:20:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:20,339 main INFO screen bangbus pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (56.0s)
Sep 15 23:20:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:20:42,146 main INFO screen hiyf  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (57.0s)
Sep 15 23:21:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:10,074 main INFO screen PUSSY pass=0 dev=0.0 ins=32.69 pro=13 1a=False 1b=False 2=True (49.7s)
Sep 15 23:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:29,891 main INFO screen Rich Pill pass=0 dev=0.0 ins=0.48 pro=12 1a=False 1b=False 2=False (71.6s)
Sep 15 23:21:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:21:35,179 main INFO screen Pussies pass=0 dev=0.0 ins=17.88 pro=42 1a=False 1b=False 2=True (53.0s)
Sep 15 23:22:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:04,023 main INFO screen Pussies pass=0 dev=0.0 ins=20.67 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 15 23:22:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:40,019 main INFO screen Paragon pass=0 dev=0.0 ins=25.29 pro=0 1a=False 1b=False 2=True (70.1s)
Sep 15 23:22:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:41,828 aiohttp.access INFO 204.76.203.7 [15/Sep/2026:23:22:41 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0"
Sep 15 23:22:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:22:46,210 main INFO screen 1 pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (71.0s)
Sep 15 23:23:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:18,574 main INFO screen fruk pass=0 dev=0.0 ins=0.0 pro=47 1a=False 1b=False 2=False (74.5s)
Sep 15 23:23:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:27,352 main INFO screen Yun pass=0 dev=0.0 ins=33.82 pro=42 1a=False 1b=False 2=True (47.3s)
Sep 15 23:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:23:47,785 main INFO screen Whore pass=0 dev=0.0 ins=0.75 pro=36 1a=False 1b=False 2=False (61.6s)
Sep 15 23:24:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:31,160 main INFO screen mike pass=0 dev=0.0 ins=14.86 pro=58 1a=False 1b=False 2=True (72.6s)
Sep 15 23:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:35,001 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:24:34 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:24:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:37,264 main INFO screen courage pass=0 dev=0.0 ins=23.63 pro=2 1a=False 1b=False 2=True (69.9s)
Sep 15 23:24:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:24:40,506 main INFO screen bey nick pass=0 dev=0.0 ins=0.73 pro=5 1a=False 1b=False 2=False (52.7s)
Sep 15 23:25:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:25:38,988 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.7s)
Sep 15 23:25:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:25:41,059 main INFO screen FLYHIGH pass=0 dev=0.0 ins=4.99 pro=68 1a=False 1b=False 2=False (69.9s)
Sep 15 23:25:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:25:44,583 main INFO screen NOIRA pass=0 dev=0.0 ins=32.53 pro=9 1a=False 1b=False 2=True (64.1s)
Sep 15 23:26:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:26:51,833 main INFO screen Pussy pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (70.8s)
Sep 15 23:26:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:26:52,251 main INFO screen hiyf  pass=0 dev=0.21 ins=0.0 pro=22 1a=False 1b=False 2=False (73.3s)
Sep 15 23:26:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:26:56,505 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (71.9s)
Sep 15 23:27:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:27:59,869 main INFO screen SOLE pass=0 dev=0.0 ins=34.16 pro=62 1a=False 1b=False 2=True (63.4s)
Sep 15 23:28:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:28:01,392 main INFO screen SP00KY pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (69.6s)
Sep 15 23:28:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:28:01,544 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.3s)
Sep 15 23:28:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:28:48,896 main INFO screen SURVIVOR pass=0 dev=0.0 ins=35.19 pro=30 1a=False 1b=False 2=True (47.5s)
Sep 15 23:29:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:29:07,398 main INFO screen LMEOW pass=0 dev=0.0 ins=6.6 pro=74 1a=False 1b=False 2=False (65.9s)
Sep 15 23:29:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:29:09,756 main INFO screen QRIS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.9s)
Sep 15 23:29:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:29:37,211 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:29:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:30:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:30:01,185 main INFO screen Jasoncoin pass=0 dev=0.0 ins=8.47 pro=76 1a=False 1b=False 2=True (72.3s)
Sep 15 23:30:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:30:11,862 main INFO screen florkina pass=0 dev=0.0 ins=30.39 pro=7 1a=False 1b=False 2=True (62.1s)
Sep 15 23:30:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:30:14,909 main INFO screen SNAKE pass=0 dev=0.0 ins=48.71 pro=10 1a=False 1b=False 2=True (67.5s)
Sep 15 23:30:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:30:53,372 main INFO screen TSELLY pass=0 dev=0.0 ins=25.33 pro=5 1a=False 1b=False 2=True (52.2s)
Sep 15 23:31:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:31:16,769 main INFO screen BCCGANG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.9s)
Sep 15 23:31:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:31:19,594 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.7s)
Sep 15 23:32:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:32:04,287 main INFO screen CALIBRATE pass=0 dev=0.0 ins=22.98 pro=73 1a=False 1b=False 2=True (70.9s)
Sep 15 23:32:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:32:08,324 main INFO screen BEPE pass=0 dev=0.0 ins=20.77 pro=1 1a=False 1b=False 2=False (51.6s)
Sep 15 23:32:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:32:22,642 main INFO screen LMEOW pass=0 dev=0.0 ins=28.46 pro=66 1a=False 1b=False 2=True (63.0s)
Sep 15 23:33:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:33:05,652 main INFO screen OnlyFlies pass=0 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=False (57.3s)
Sep 15 23:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:33:17,098 main INFO screen buzz pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.5s)
Sep 15 23:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:33:19,861 main INFO screen fruk pass=0 dev=0.0 ins=0.0 pro=45 1a=False 1b=False 2=False (75.6s)
Sep 15 23:34:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:34:02,996 main INFO screen BATON pass=0 dev=0.0 ins=77.57 pro=2 1a=False 1b=True 2=True (57.3s)
Sep 15 23:34:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:34:29,322 main INFO screen CAVEMAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (72.2s)
Sep 15 23:34:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:34:30,258 main INFO screen POST pass=0 dev=0.0 ins=9.02 pro=53 1a=False 1b=False 2=False (70.4s)
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:35:38,756 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:35:38,892 rpc WARNING rpc getTokenLargestAccounts exc
Sep 15 23:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:35:38,996 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:35:38 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:35:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:35:59,955 main INFO screen Owl fun pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (117.0s)
Sep 15 23:36:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:36:35,620 main INFO screen Hypest pass=0 dev=0.0 ins=49.04 pro=5 1a=False 1b=False 2=True (125.4s)
Sep 15 23:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:36:36,969 main INFO screen FLY HIGH pass=0 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (127.6s)
Sep 15 23:37:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:09,451 main INFO screen sol pass=0 dev=0.0 ins=24.3 pro=5 1a=False 1b=False 2=True (69.5s)
Sep 15 23:37:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:43,463 main INFO screen URMOM pass=0 dev=0.0 ins=8.47 pro=70 1a=False 1b=False 2=True (66.5s)
Sep 15 23:37:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:37:46,075 main INFO screen compute pass=0 dev=0.0 ins=18.79 pro=5 1a=False 1b=False 2=True (70.5s)
Sep 15 23:38:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:03,479 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (54.0s)
Sep 15 23:38:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:46,313 main INFO screen Mafia pass=0 dev=0.0 ins=4.85 pro=55 1a=False 1b=False 2=True (60.2s)
Sep 15 23:38:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:38:48,230 main INFO screen LMEOW pass=0 dev=0.0 ins=35.3 pro=25 1a=False 1b=False 2=True (64.8s)
Sep 15 23:39:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:06,841 main INFO screen OnlyFlies pass=0 dev=0.0 ins=14.58 pro=56 1a=False 1b=False 2=False (63.4s)
Sep 15 23:39:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:52,629 main INFO screen CATNIS  pass=0 dev=0.02 ins=0.0 pro=3 1a=False 1b=False 2=False (64.4s)
Sep 15 23:39:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:54,354 main INFO screen NVDA pass=0 dev=0.0 ins=25.1 pro=0 1a=False 1b=False 2=True (68.0s)
Sep 15 23:39:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:39:58,532 main INFO screen AUTONOMOUS pass=0 dev=0.0 ins=6.53 pro=48 1a=False 1b=False 2=False (51.7s)
Sep 15 23:40:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:40:32,073 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:40:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (84579ff37485)
--- update 2026-09-15T22:16:44Z
--- update 2026-09-15T22:21:44Z
--- update 2026-09-15T22:26:45Z
--- update 2026-09-15T22:31:47Z
--- update 2026-09-15T22:37:16Z
--- update 2026-09-15T22:42:34Z
--- update 2026-09-15T22:47:36Z
--- update 2026-09-15T22:52:48Z
--- update 2026-09-15T22:58:28Z
--- update 2026-09-15T23:03:36Z
--- update 2026-09-15T23:09:15Z
--- update 2026-09-15T23:14:26Z
Running as unit: schaduwbot-wallets.service; invocation ID: 28b70ef890d5475a9c6286045b142940
analyses gestart (84579ff37485)
--- update 2026-09-15T23:19:31Z
--- update 2026-09-15T23:24:33Z
--- update 2026-09-15T23:29:36Z
--- update 2026-09-15T23:35:22Z
--- update 2026-09-15T23:40:30Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 22:11:40
22:11:40 venster 2026-09-13 10:11 UTC .. nu, 72419 tokens
22:12:33 klaar in 54s: 55545 tokens, 1912 nieuw -> /opt/schaduwbot/reports/video_replay.md
--- /opt/schaduwbot/video_replay.py 23:14:26
23:14:27 venster 2026-09-13 11:14 UTC .. nu, 73409 tokens
23:15:28 klaar in 61s: 56398 tokens, 1848 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
23:09:30 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=431 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:09:30 ijk-diagnose: nieuwste migratie 0.2 min oud | migraties 15/60/240 min: 8/46/193 | al gemeten: 889
23:15:07 ijk: +6 van 6 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=436 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:15:13 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 14/49/199 | al gemeten: 895
23:19:56 ijk: +5 van 5 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=440 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:19:57 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 14/50/197 | al gemeten: 900
23:24:43 ijk: +2 van 2 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=442 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:24:44 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 13/48/192 | al gemeten: 902
23:29:49 ijk: +3 van 3 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=444 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:29:49 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 9/47/192 | al gemeten: 905
23:35:32 ijk: +2 van 2 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=446 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:35:32 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 7/45/194 | al gemeten: 907
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 500 | 51 | 51 | 0 | 0 | 6.5 min |
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
| 09-15 18:00 | 11040 | 595 | 548 | 591 | 0 | 155.9 min |

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
