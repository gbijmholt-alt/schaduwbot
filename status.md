# Schaduwbot status

- tijd: 2026-09-13 15:56:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 2 hours, 9 minutes
- bot-service: active
- code-versie: 54e958b
- schijf: 4.7G/38G | geheugen: 1242/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 33746, "tokens_in_memory": 5598, "msgs": 2590922, "trades": 685558, "creates": 7746, "decode_fail": 79826, "rpc_calls": 21393, "rpc_errors": 2, "sol_usd": 100.2617160294999, "open_positions": 19, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 15:31:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:31:36,830 main INFO screen $GOAT pass=0 dev=0.24 ins=0.0 pro=2 1a=False 1b=False 2=False (58.6s)
Sep 13 15:32:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:32:06,959 main INFO screen $SASS pass=0 dev=1.85 ins=0.0 pro=7 1a=False 1b=False 2=False (64.6s)
Sep 13 15:32:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:32:38,863 main INFO screen Catamount pass=0 dev=0.0 ins=11.08 pro=73 1a=False 1b=False 2=True (70.7s)
Sep 13 15:32:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:32:54,159 main INFO screen BONE pass=1 dev=2.08 ins=13.81 pro=49 1a=False 1b=False 2=False (71.2s)
Sep 13 15:33:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:33:53,422 main INFO screen NABU pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (71.7s)
Sep 13 15:33:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:33:56,952 main INFO screen PAINTER pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (66.2s)
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:34:56,675 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 15:34:56 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 15:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:35:23,417 main INFO screen BATONIUS pass=0 dev=0.35 ins=78.96 pro=1 1a=True 1b=True 2=True (103.9s)
Sep 13 15:35:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:35:24,762 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:35:24 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 13 15:35:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:35:54,354 main INFO screen Moon pass=0 dev=0.07 ins=0.0 pro=3 1a=False 1b=False 2=False (107.3s)
Sep 13 15:35:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:35:57,669 main INFO screen SI pass=0 dev=0.0 ins=23.32 pro=59 1a=False 1b=False 2=True (109.3s)
Sep 13 15:36:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:36:31,395 main INFO screen sadfrog  pass=0 dev=0.92 ins=0.0 pro=6 1a=False 1b=False 2=False (68.0s)
Sep 13 15:37:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:37:05,631 main INFO screen vrl pass=0 dev=29.6 ins=0.0 pro=14 1a=False 1b=False 2=False (71.3s)
Sep 13 15:37:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:37:07,607 main INFO screen SI pass=0 dev=0.0 ins=27.21 pro=35 1a=False 1b=False 2=True (69.9s)
Sep 13 15:37:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:37:41,314 main INFO screen PAINTER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.9s)
Sep 13 15:38:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:38:01,362 main INFO screen CHUDGPT pass=0 dev=0.06 ins=79.26 pro=7 1a=False 1b=True 2=True (55.7s)
Sep 13 15:38:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:38:01,563 main INFO screen SLOPNET pass=0 dev=0.0 ins=48.89 pro=45 1a=False 1b=False 2=True (54.0s)
Sep 13 15:38:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:38:35,615 main INFO screen PBUNNY pass=1 dev=0.0 ins=0.0 pro=63 1a=False 1b=False 2=False (54.3s)
Sep 13 15:39:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:39:07,895 main INFO screen DOM pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (66.5s)
Sep 13 15:39:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:39:09,388 main INFO screen SOUP pass=0 dev=0.0 ins=20.31 pro=58 1a=False 1b=False 2=True (66.2s)
Sep 13 15:39:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:39:44,690 main INFO screen OOPS pass=0 dev=0.21 ins=0.0 pro=8 1a=False 1b=False 2=False (69.1s)
Sep 13 15:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:40:00,922 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.5s)
Sep 13 15:40:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:40:03,081 main INFO screen SOUP pass=0 dev=0.0 ins=24.33 pro=23 1a=False 1b=False 2=True (55.2s)
Sep 13 15:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:40:37,636 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:40:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 15:40:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:40:37,988 main INFO screen HOUSE pass=0 dev=0.4 ins=0.0 pro=4 1a=False 1b=False 2=False (53.3s)
Sep 13 15:41:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:41:24,308 main INFO screen Joe&Sam pass=1 dev=0.18 ins=0.0 pro=59 1a=False 1b=False 2=False (53.8s)
Sep 13 15:41:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:41:50,486 main INFO screen SOUP pass=1 dev=0.0 ins=18.62 pro=48 1a=False 1b=False 2=False (67.3s)
Sep 13 15:42:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:42:28,418 main INFO screen ANONSEM pass=0 dev=0.0 ins=36.28 pro=15 1a=False 1b=False 2=True (68.9s)
Sep 13 15:43:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:43:09,127 main INFO screen SOUP pass=0 dev=0.0 ins=20.79 pro=36 1a=False 1b=False 2=False (51.0s)
Sep 13 15:43:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:43:43,179 main INFO screen SOUP pass=0 dev=0.0 ins=12.62 pro=20 1a=False 1b=False 2=True (81.8s)
Sep 13 15:43:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:43:44,637 main INFO screen OMEG pass=0 dev=0.0 ins=16.59 pro=67 1a=False 1b=False 2=True (76.1s)
Sep 13 15:44:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:44:15,263 main INFO screen Trio pass=0 dev=0.0 ins=5.82 pro=70 1a=False 1b=False 2=True (66.1s)
Sep 13 15:44:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:44:56,538 main INFO screen ANONSEM pass=0 dev=0.0 ins=31.85 pro=17 1a=False 1b=False 2=True (73.4s)
Sep 13 15:44:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:44:59,242 main INFO screen $RAS pass=1 dev=0.0 ins=0.0 pro=33 1a=False 1b=False 2=False (72.8s)
Sep 13 15:45:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:45:10,020 main INFO screen JubJub pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 13 15:46:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:46:00,425 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:46:00 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 15:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:46:12,428 main INFO screen ANONSEM pass=0 dev=0.0 ins=31.3 pro=17 1a=False 1b=False 2=True (73.2s)
Sep 13 15:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:46:12,790 main INFO screen MIAUW pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (76.3s)
Sep 13 15:46:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:46:23,764 main INFO screen SNUZ pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (73.7s)
Sep 13 15:47:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:47:30,055 main INFO screen CHAROC pass=0 dev=0.02 ins=0.0 pro=7 1a=False 1b=False 2=False (77.6s)
Sep 13 15:47:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:47:38,866 main INFO screen FUET pass=0 dev=25.05 ins=0.31 pro=27 1a=False 1b=False 2=False (73.9s)
Sep 13 15:47:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:47:47,943 main INFO screen ANONSEM pass=0 dev=0.0 ins=31.83 pro=19 1a=False 1b=False 2=True (72.1s)
Sep 13 15:48:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:48:36,821 main INFO screen RTAIL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 13 15:48:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:48:44,288 main INFO screen BATUNK pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (65.4s)
Sep 13 15:49:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:49:16,249 main INFO screen LOBSTER pass=0 dev=0.0 ins=31.12 pro=57 1a=False 1b=False 2=True (71.5s)
Sep 13 15:49:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:49:50,171 main INFO screen SOUP pass=0 dev=0.0 ins=22.59 pro=65 1a=False 1b=False 2=True (73.3s)
Sep 13 15:49:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:49:55,390 main INFO screen ANONSEM pass=0 dev=0.0 ins=31.85 pro=43 1a=False 1b=False 2=True (71.1s)
Sep 13 15:50:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:50:14,026 main INFO screen Jeni Cat pass=0 dev=0.0 ins=0.7 pro=1 1a=False 1b=False 2=False (57.8s)
Sep 13 15:50:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:50:57,298 main INFO screen REVOLEAK pass=0 dev=0.7 ins=0.0 pro=3 1a=False 1b=False 2=False (67.1s)
Sep 13 15:50:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:50:59,145 main INFO screen cap pass=0 dev=0.99 ins=0.0 pro=2 1a=False 1b=False 2=False (63.8s)
Sep 13 15:51:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:51:05,166 main INFO screen 777 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.1s)
Sep 13 15:51:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:51:27,207 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:51:27 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 15:51:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:51:44,644 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.3s)
Sep 13 15:51:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:51:50,128 main INFO screen SNUZ pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.0s)
Sep 13 15:52:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:52:09,322 main INFO screen NEURO pass=0 dev=0.0 ins=30.55 pro=41 1a=False 1b=True 2=True (58.2s)
Sep 13 15:52:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:52:36,700 main INFO screen HYPXL pass=0 dev=0.0 ins=0.24 pro=4 1a=False 1b=False 2=False (52.1s)
Sep 13 15:52:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:52:52,842 main INFO screen ANONSEM pass=0 dev=0.0 ins=31.87 pro=29 1a=False 1b=False 2=True (62.7s)
Sep 13 15:53:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:53:02,298 main INFO screen ECC pass=0 dev=0.0 ins=21.82 pro=37 1a=False 1b=False 2=True (53.0s)
Sep 13 15:53:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:53:39,179 main INFO screen BBP pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (62.5s)
Sep 13 15:53:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:53:46,203 main INFO screen ANONSEM pass=0 dev=0.0 ins=32.51 pro=15 1a=False 1b=False 2=True (47.6s)
Sep 13 15:54:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:54:07,387 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (50.4s)
Sep 13 15:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:54:54,555 main INFO screen TAKEOVER pass=0 dev=0.0 ins=62.4 pro=74 1a=False 1b=False 2=True (64.3s)
Sep 13 15:55:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:55:01,513 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (46.5s)
Sep 13 15:55:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:55:26,201 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.8s)
Sep 13 15:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:55:44,296 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (49.6s)
Sep 13 15:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:55:44,477 aiohttp.access INFO 47.250.93.99 [13/Sep/2026:15:55:44 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 13 15:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:55:44,817 aiohttp.access INFO 47.250.93.99 [13/Sep/2026:15:55:44 +0000] "GET / HTTP/1.1" 404 193 "-" "curl/7.74.0"
Sep 13 15:56:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:56:07,895 main INFO screen PORTNOY pass=0 dev=0.0 ins=0.0 pro=85 1a=False 1b=False 2=True (64.7s)
Sep 13 15:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:56:33,938 main INFO screen Neocloud pass=1 dev=0.0 ins=12.86 pro=66 1a=False 1b=False 2=False (67.7s)
Sep 13 15:56:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 15:56:34,646 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:15:56:34 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
nieuwe code: 60bc96f
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 5753ff544a174b8f8dc6b2ae1512fa0d
analyses gestart (0d01412cf2b7)
--- update 2026-09-13T14:58:36Z
--- update 2026-09-13T15:04:10Z
--- update 2026-09-13T15:09:11Z
--- update 2026-09-13T15:14:36Z
--- update 2026-09-13T15:19:36Z
--- update 2026-09-13T15:25:09Z
nieuwe code: 54e958b
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 7948cd6f3a7b4dfeb4d4bd945d22b179
analyses gestart (e3190511b57b)
--- update 2026-09-13T15:30:21Z
--- update 2026-09-13T15:35:23Z
--- update 2026-09-13T15:40:36Z
--- update 2026-09-13T15:45:59Z
--- update 2026-09-13T15:51:26Z
--- update 2026-09-13T15:56:33Z
```

## Analyses (laatste 25 regels)
```
inactive
15:37:05   18000 tokens, 1944204 trades, 298142 posities (51s)
15:37:10   20000 tokens, 2187868 trades, 342250 posities (57s)
15:37:15   22000 tokens, 2406411 trades, 378792 posities (62s)
15:37:19   24000 tokens, 2626614 trades, 409516 posities (65s)
15:37:22   26000 tokens, 2840165 trades, 441465 posities (69s)
15:37:26   28000 tokens, 3073379 trades, 477166 posities (73s)
15:37:30   30000 tokens, 3304489 trades, 515001 posities (77s)
15:37:34   32000 tokens, 3516909 trades, 546487 posities (80s)
15:37:38   34000 tokens, 3731214 trades, 580535 posities (84s)
15:37:43   36000 tokens, 3958328 trades, 619055 posities (89s)
15:37:48   38000 tokens, 4172693 trades, 651310 posities (95s)
15:37:53   40000 tokens, 4383091 trades, 680638 posities (99s)
15:37:57   42000 tokens, 4594546 trades, 716760 posities (104s)
15:38:02   44000 tokens, 4815309 trades, 751831 posities (109s)
15:38:07   46000 tokens, 5015503 trades, 782629 posities (114s)
15:38:13   48000 tokens, 5236735 trades, 820680 posities (120s)
15:38:20   50000 tokens, 5466284 trades, 857419 posities (127s)
15:38:27   52000 tokens, 5695807 trades, 893439 posities (134s)
15:38:34   54000 tokens, 5919511 trades, 938690 posities (141s)
15:38:40 posities: 976402 uit 6110942 trades (148s)
15:38:54 199901 wallets gerekend
15:38:54 geluk-toets
15:39:30 persistentie
15:39:33 kopieer-simulatie
15:40:43 klaar in 271s -> /opt/schaduwbot/reports/wallets.md
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
