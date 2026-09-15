# Schaduwbot status

- tijd: 2026-09-15 01:40:46 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 11 hours, 53 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.6G/38G | geheugen: 2246/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 155199, "tokens_in_memory": 9912, "msgs": 23427856, "trades": 4725312, "creates": 50379, "decode_fail": 409172, "rpc_calls": 133149, "rpc_errors": 13, "sol_usd": 102.41564563180124, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 01:18:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:15,982 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.4s)
Sep 15 01:18:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:43,965 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.5s)
Sep 15 01:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:18:49,967 main INFO screen POM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 15 01:19:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:08,370 main INFO screen MCAT pass=0 dev=0.0 ins=29.6 pro=12 1a=False 1b=False 2=True (52.4s)
Sep 15 01:19:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:39,687 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (55.7s)
Sep 15 01:19:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:19:56,004 main INFO screen Supercycle pass=0 dev=0.0 ins=28.76 pro=73 1a=False 1b=False 2=True (66.0s)
Sep 15 01:20:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:06,040 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.7s)
Sep 15 01:20:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:33,927 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:20:33 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 01:20:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:38,111 main INFO screen GIGAFUND pass=0 dev=0.0 ins=20.69 pro=38 1a=False 1b=True 2=True (58.4s)
Sep 15 01:20:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:20:51,791 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.8s)
Sep 15 01:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:01,783 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.7s)
Sep 15 01:21:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:34,165 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.1s)
Sep 15 01:21:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:43,697 main INFO screen TRAVIS pass=0 dev=0.0 ins=18.25 pro=45 1a=False 1b=False 2=True (51.9s)
Sep 15 01:21:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:21:56,746 main INFO screen Obimach pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.0s)
Sep 15 01:22:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:26,568 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=False (52.4s)
Sep 15 01:22:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:42,476 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.8s)
Sep 15 01:22:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:22:52,107 main INFO screen Neocloud pass=0 dev=0.0 ins=17.57 pro=14 1a=False 1b=False 2=True (55.4s)
Sep 15 01:23:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:20,821 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 15 01:23:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:33,274 aiohttp.access INFO 170.130.204.50 [15/Sep/2026:01:23:33 +0000] "UNKNOWN / HTTP/1.0" 400 267 "-" "-"
Sep 15 01:23:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:34,838 main INFO screen SINGULARITY pass=0 dev=0.0 ins=26.37 pro=48 1a=False 1b=False 2=True (52.4s)
Sep 15 01:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:23:47,506 main INFO screen Rolex pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (55.4s)
Sep 15 01:24:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:35,738 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (74.9s)
Sep 15 01:24:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:43,291 main INFO screen TH3000 pass=0 dev=0.0 ins=28.21 pro=15 1a=False 1b=False 2=True (55.8s)
Sep 15 01:24:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:24:47,879 main INFO screen Gary pass=0 dev=0.0 ins=25.57 pro=69 1a=False 1b=False 2=True (73.0s)
Sep 15 01:25:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:25:37,195 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:25:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:25:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:25:38,919 main INFO screen UKAUKA pass=0 dev=0.0 ins=36.56 pro=61 1a=False 1b=False 2=True (63.2s)
Sep 15 01:25:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:25:45,516 main INFO screen Hope pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.2s)
Sep 15 01:25:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:25:58,253 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (70.4s)
Sep 15 01:26:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:26:50,646 main INFO screen SCCKFFF pass=0 dev=0.0 ins=26.31 pro=56 1a=False 1b=False 2=True (71.7s)
Sep 15 01:26:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:26:59,014 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.8s)
Sep 15 01:26:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:26:59,600 main INFO screen WHITEBULL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (74.1s)
Sep 15 01:27:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:27:53,288 main INFO screen OpenAI pass=0 dev=0.0 ins=143.7 pro=0 1a=False 1b=False 2=True (62.6s)
Sep 15 01:27:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:27:57,522 main INFO screen WOTF pass=0 dev=0.0 ins=136.58 pro=1 1a=False 1b=False 2=True (58.5s)
Sep 15 01:27:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:27:58,381 main INFO screen Callout pass=0 dev=0.0 ins=25.83 pro=75 1a=False 1b=False 2=True (58.8s)
Sep 15 01:28:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:28:52,526 main INFO screen SCCKFFF pass=0 dev=0.0 ins=26.64 pro=8 1a=True 1b=False 2=True (59.2s)
Sep 15 01:28:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:28:55,666 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 15 01:29:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:29:08,959 main INFO screen WHITEBULL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.6s)
Sep 15 01:29:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:29:49,362 main INFO screen UKAUKA pass=0 dev=0.0 ins=25.17 pro=53 1a=False 1b=False 2=True (56.8s)
Sep 15 01:30:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:30:04,086 main INFO screen jewcycle pass=0 dev=0.0 ins=15.16 pro=57 1a=False 1b=False 2=False (68.4s)
Sep 15 01:30:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:30:11,248 main INFO screen WEENIE pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 15 01:30:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:30:38,267 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:30:38 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:30:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:30:46,752 main INFO screen WHITEBULL pass=0 dev=0.0 ins=0.18 pro=1 1a=False 1b=False 2=False (57.4s)
Sep 15 01:31:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:31:03,502 main INFO screen NYT Coin pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (59.4s)
Sep 15 01:31:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:31:12,865 main INFO screen GATE pass=0 dev=0.0 ins=43.76 pro=21 1a=True 1b=False 2=False (61.6s)
Sep 15 01:31:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:31:36,881 main INFO screen Gary pass=0 dev=0.0 ins=40.5 pro=67 1a=False 1b=False 2=True (50.1s)
Sep 15 01:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:32:05,568 main INFO screen GATE pass=0 dev=0.0 ins=17.22 pro=21 1a=False 1b=False 2=True (62.1s)
Sep 15 01:32:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:32:14,559 main INFO screen SAME pass=0 dev=0.0 ins=23.34 pro=36 1a=False 1b=False 2=True (61.7s)
Sep 15 01:32:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:32:49,420 main INFO screen Entropy pass=0 dev=0.0 ins=19.09 pro=39 1a=False 1b=False 2=True (72.5s)
Sep 15 01:33:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:33:10,176 main INFO screen ch pass=0 dev=0.0 ins=0.21 pro=1 1a=False 1b=False 2=False (64.6s)
Sep 15 01:33:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:33:10,844 main INFO screen wifbike pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (56.3s)
Sep 15 01:33:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:33:58,156 main INFO screen JUDE pass=0 dev=0.0 ins=20.59 pro=74 1a=False 1b=False 2=True (68.7s)
Sep 15 01:34:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:34:09,220 main INFO screen GIRL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.0s)
Sep 15 01:34:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:34:27,471 main INFO screen MM pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (76.6s)
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:35:23,165 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 01:35:23 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 01:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:35:40,281 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:35:40 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 01:35:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:35:46,304 main INFO screen Launchpad pass=0 dev=0.0 ins=16.35 pro=71 1a=False 1b=False 2=True (108.1s)
Sep 15 01:36:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:36:02,898 main INFO screen GARY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (113.7s)
Sep 15 01:36:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:36:23,488 main INFO screen Shitcoin pass=0 dev=0.0 ins=22.94 pro=35 1a=False 1b=False 2=True (116.0s)
Sep 15 01:36:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:36:46,762 main INFO screen Roads pass=0 dev=0.0 ins=15.1 pro=65 1a=False 1b=False 2=True (60.5s)
Sep 15 01:37:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:37:02,498 main INFO screen Parmesan pass=0 dev=0.0 ins=55.55 pro=26 1a=True 1b=False 2=True (59.6s)
Sep 15 01:37:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:37:33,853 main INFO screen FARMM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.4s)
Sep 15 01:37:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:37:52,172 main INFO screen SUZI pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (65.4s)
Sep 15 01:38:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:38:10,023 main INFO screen VANS pass=0 dev=0.0 ins=78.96 pro=0 1a=False 1b=True 2=True (67.5s)
Sep 15 01:38:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:38:43,777 main INFO screen ALFAFA pass=0 dev=4.79 ins=0.0 pro=13 1a=False 1b=False 2=False (69.9s)
Sep 15 01:39:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:39:01,428 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (69.3s)
Sep 15 01:39:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:39:17,411 main INFO screen Plover pass=0 dev=0.0 ins=34.37 pro=69 1a=False 1b=False 2=True (67.4s)
Sep 15 01:39:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:39:50,997 main INFO screen punchhall5 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.2s)
Sep 15 01:40:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:40:03,111 main INFO screen JUDE pass=0 dev=0.0 ins=13.53 pro=63 1a=False 1b=False 2=False (61.7s)
Sep 15 01:40:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:40:19,185 main INFO screen 💵 pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (61.8s)
Sep 15 01:40:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 01:40:46,702 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:01:40:46 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T00:01:52Z
--- update 2026-09-15T00:07:23Z
--- update 2026-09-15T00:12:34Z
--- update 2026-09-15T00:17:36Z
--- update 2026-09-15T00:22:46Z
--- update 2026-09-15T00:28:02Z
--- update 2026-09-15T00:33:12Z
--- update 2026-09-15T00:38:36Z
--- update 2026-09-15T00:43:36Z
--- update 2026-09-15T00:48:48Z
--- update 2026-09-15T00:54:19Z
--- update 2026-09-15T00:59:26Z
--- update 2026-09-15T01:04:36Z
--- update 2026-09-15T01:09:36Z
--- update 2026-09-15T01:15:15Z
--- update 2026-09-15T01:20:32Z
--- update 2026-09-15T01:25:36Z
--- update 2026-09-15T01:30:37Z
--- update 2026-09-15T01:35:39Z
--- update 2026-09-15T01:40:45Z
```

## Analyses (laatste 25 regels)
```
inactive
00:29:52   38000 tokens, 3688000 trades, 442370 posities (248s)
00:30:05   40000 tokens, 3882064 trades, 469159 posities (261s)
00:30:19   42000 tokens, 4065709 trades, 486855 posities (274s)
00:30:33   44000 tokens, 4245991 trades, 510852 posities (289s)
00:30:47   46000 tokens, 4420440 trades, 531350 posities (303s)
00:31:02   48000 tokens, 4598102 trades, 550760 posities (318s)
00:31:19   50000 tokens, 4799757 trades, 574399 posities (335s)
00:31:36   52000 tokens, 5016691 trades, 603626 posities (352s)
00:31:52   54000 tokens, 5200426 trades, 625224 posities (367s)
00:32:06   56000 tokens, 5365533 trades, 644406 posities (382s)
00:32:23   58000 tokens, 5562944 trades, 669075 posities (399s)
00:32:39   60000 tokens, 5746516 trades, 689739 posities (415s)
00:32:57   62000 tokens, 5955952 trades, 716730 posities (433s)
00:33:13   64000 tokens, 6142789 trades, 744367 posities (449s)
00:33:30   66000 tokens, 6356758 trades, 771423 posities (466s)
00:33:43   68000 tokens, 6541957 trades, 795263 posities (479s)
00:33:56   70000 tokens, 6731219 trades, 818210 posities (492s)
00:34:10   72000 tokens, 6922572 trades, 843202 posities (506s)
00:34:25   74000 tokens, 7133262 trades, 878980 posities (521s)
00:34:30 posities: 885811 uit 7196469 trades (529s)
00:34:43 211069 wallets gerekend
00:34:43 geluk-toets
00:35:19 persistentie
00:35:22 kopieer-simulatie
00:37:42 klaar in 721s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
01:09:54 ijk: +6 van 7 kandidaten (16 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=71 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:09:54 ijk-diagnose: nieuwste migratie 1.0 min oud | migraties 15/60/240 min: 16/42/166 | al gemeten: 362
01:15:28 ijk: +4 van 4 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=72 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:15:28 ijk-diagnose: nieuwste migratie 0.7 min oud | migraties 15/60/240 min: 12/41/164 | al gemeten: 366
01:20:44 ijk: +4 van 4 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=75 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:20:45 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 13/42/167 | al gemeten: 370
01:25:42 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=77 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:25:42 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 8/40/164 | al gemeten: 372
01:30:43 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=79 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:30:43 ijk-diagnose: nieuwste migratie 1.8 min oud | migraties 15/60/240 min: 8/39/158 | al gemeten: 374
01:35:51 ijk: +4 van 4 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=83 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
01:35:52 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 8/41/158 | al gemeten: 378
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
