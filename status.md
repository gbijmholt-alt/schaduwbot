# Schaduwbot status

- tijd: 2026-09-15 20:38:26 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 6 hours, 51 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.6G/38G | geheugen: 2333/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 223459, "tokens_in_memory": 10666, "msgs": 35834786, "trades": 7138144, "creates": 75608, "decode_fail": 603877, "rpc_calls": 201981, "rpc_errors": 17, "sol_usd": 96.99521821770405, "open_positions": 83, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 20:15:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:15:54,592 main INFO screen $TOGETHER pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.3s)
Sep 15 20:16:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:24,206 main INFO screen TRAVIS pass=0 dev=0.0 ins=22.13 pro=63 1a=False 1b=False 2=True (54.2s)
Sep 15 20:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:37,767 main INFO screen Halphurt pass=0 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (62.2s)
Sep 15 20:16:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:16:48,832 main INFO screen HLDM pass=0 dev=0.0 ins=161.25 pro=0 1a=False 1b=False 2=True (54.2s)
Sep 15 20:17:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:28,499 main INFO screen BROS pass=0 dev=0.0 ins=24.53 pro=43 1a=False 1b=False 2=False (64.3s)
Sep 15 20:17:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:38,015 main INFO screen Him pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.2s)
Sep 15 20:17:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:17:52,230 main INFO screen Charzard  pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (63.4s)
Sep 15 20:18:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:18:14,384 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:18:14 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:18:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:18:21,466 main INFO screen ELIZABUTT pass=0 dev=0.0 ins=19.12 pro=2 1a=False 1b=False 2=False (53.0s)
Sep 15 20:18:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:18:33,301 main INFO screen ONEDOLLAR pass=0 dev=0.0 ins=78.13 pro=8 1a=False 1b=True 2=True (55.3s)
Sep 15 20:18:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:18:49,169 main INFO screen LUMMIS pass=0 dev=0.0 ins=31.06 pro=46 1a=False 1b=False 2=True (56.9s)
Sep 15 20:19:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:19:33,005 main INFO screen CLARITITTY pass=0 dev=0.0 ins=20.1 pro=49 1a=False 1b=False 2=True (71.5s)
Sep 15 20:19:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:19:37,349 main INFO screen COCK pass=0 dev=0.0 ins=25.44 pro=3 1a=False 1b=False 2=True (64.0s)
Sep 15 20:19:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:19:59,360 main INFO screen OPAQUE pass=0 dev=0.0 ins=38.6 pro=71 1a=False 1b=False 2=True (70.2s)
Sep 15 20:20:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:20:43,516 main INFO screen COCK pass=0 dev=0.0 ins=13.4 pro=57 1a=False 1b=False 2=False (70.5s)
Sep 15 20:20:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:20:45,041 main INFO screen blackfloyd pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (67.7s)
Sep 15 20:21:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:21:01,827 main INFO screen Floor pass=0 dev=0.0 ins=14.58 pro=42 1a=False 1b=False 2=False (62.5s)
Sep 15 20:21:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:21:44,199 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 15 20:21:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:21:45,971 main INFO screen Lummis pass=0 dev=0.0 ins=28.27 pro=52 1a=False 1b=False 2=True (60.9s)
Sep 15 20:21:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:21:53,271 main INFO screen TOELY pass=0 dev=0.0 ins=78.92 pro=0 1a=True 1b=True 2=True (51.4s)
Sep 15 20:22:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:22:59,302 main INFO screen Mike pass=0 dev=0.0 ins=21.1 pro=74 1a=False 1b=False 2=True (75.1s)
Sep 15 20:23:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:23:00,886 main INFO screen KOID pass=0 dev=0.0 ins=24.43 pro=1 1a=False 1b=False 2=True (74.9s)
Sep 15 20:23:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:23:02,305 main INFO screen Juan pass=0 dev=0.0 ins=30.89 pro=49 1a=False 1b=False 2=True (69.0s)
Sep 15 20:23:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:23:17,620 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:23:17 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 20:23:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:23:47,556 main INFO screen LASEREYES pass=0 dev=0.0 ins=29.9 pro=27 1a=False 1b=False 2=True (48.3s)
Sep 15 20:24:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:24:04,748 main INFO screen FTHR pass=0 dev=0.0 ins=4.01 pro=22 1a=False 1b=False 2=False (62.4s)
Sep 15 20:24:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:24:06,678 main INFO screen SALO pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (65.8s)
Sep 15 20:24:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:24:57,004 main INFO screen OPAQUE pass=0 dev=0.0 ins=20.06 pro=2 1a=False 1b=False 2=False (69.4s)
Sep 15 20:25:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:25:13,653 main INFO screen THEGLOCK pass=0 dev=0.0 ins=26.31 pro=58 1a=False 1b=False 2=False (68.9s)
Sep 15 20:25:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:25:15,206 main INFO screen PIVO pass=0 dev=9.78 ins=0.0 pro=50 1a=False 1b=False 2=False (68.5s)
Sep 15 20:25:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:25:52,683 main INFO screen EMBER pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (55.7s)
Sep 15 20:26:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:26:22,200 main INFO screen ELONMASK pass=0 dev=0.0 ins=53.55 pro=57 1a=False 1b=False 2=True (67.0s)
Sep 15 20:26:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:26:23,667 main INFO screen COCK pass=0 dev=0.0 ins=9.75 pro=63 1a=False 1b=False 2=False (70.0s)
Sep 15 20:26:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:26:37,925 aiohttp.access INFO 14.5.162.54 [15/Sep/2026:20:26:37 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 20:27:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:27:00,990 main INFO screen CLARITITTY pass=0 dev=0.0 ins=4.45 pro=69 1a=False 1b=False 2=False (68.3s)
Sep 15 20:27:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:27:15,392 main INFO screen CLARITITTY pass=0 dev=0.0 ins=25.49 pro=0 1a=False 1b=False 2=False (53.2s)
Sep 15 20:27:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:27:24,047 main INFO screen METACOIN pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.4s)
Sep 15 20:27:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:27:51,782 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (50.8s)
Sep 15 20:28:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:28:20,458 main INFO screen LEXAPOOP pass=0 dev=0.0 ins=30.98 pro=55 1a=False 1b=False 2=True (65.1s)
Sep 15 20:28:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:28:21,110 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:28:21 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 20:28:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:28:24,417 main INFO screen 1EDGE pass=0 dev=0.0 ins=11.07 pro=21 1a=False 1b=False 2=False (60.4s)
Sep 15 20:28:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:28:46,750 main INFO screen LEXAPOOP pass=0 dev=0.0 ins=2.4 pro=29 1a=False 1b=False 2=True (55.0s)
Sep 15 20:29:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:29:08,791 main INFO screen Win pass=0 dev=0.0 ins=33.21 pro=15 1a=False 1b=False 2=True (48.3s)
Sep 15 20:29:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:29:15,349 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.9s)
Sep 15 20:29:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:29:48,175 main INFO screen SHIELD pass=0 dev=0.0 ins=23.66 pro=71 1a=False 1b=False 2=True (61.4s)
Sep 15 20:29:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:29:58,458 main INFO screen MUTE pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (49.7s)
Sep 15 20:30:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:30:25,033 main INFO screen SHIELD pass=0 dev=0.0 ins=0.85 pro=26 1a=False 1b=False 2=False (69.7s)
Sep 15 20:30:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:30:48,520 main INFO screen Pussycat pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.3s)
Sep 15 20:30:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:30:52,065 main INFO screen CRYPTO pass=0 dev=0.0 ins=20.3 pro=33 1a=False 1b=False 2=True (53.6s)
Sep 15 20:31:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:31:27,056 main INFO screen OPAQUE pass=0 dev=0.0 ins=9.64 pro=61 1a=False 1b=False 2=True (62.0s)
Sep 15 20:31:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:31:38,001 main INFO screen CUTEDOGE pass=0 dev=0.0 ins=24.86 pro=1 1a=False 1b=False 2=True (49.5s)
Sep 15 20:32:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:32:05,073 main INFO screen SLIPPO pass=0 dev=0.0 ins=31.29 pro=66 1a=False 1b=False 2=True (73.0s)
Sep 15 20:32:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:32:35,049 main INFO screen SHIELD pass=0 dev=0.0 ins=19.72 pro=0 1a=False 1b=False 2=False (68.0s)
Sep 15 20:32:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:32:50,104 main INFO screen votecat pass=0 dev=0.0 ins=33.13 pro=62 1a=False 1b=False 2=True (72.1s)
Sep 15 20:33:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:33:06,014 main INFO screen MUTE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.9s)
Sep 15 20:33:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:33:26,630 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:33:26 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 20:33:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:33:48,029 main INFO screen HCAT pass=0 dev=2.64 ins=1.32 pro=81 1a=False 1b=False 2=True (73.0s)
Sep 15 20:33:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:33:52,883 main INFO screen Mike pass=0 dev=0.0 ins=6.7 pro=79 1a=False 1b=False 2=True (62.8s)
Sep 15 20:34:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:34:15,541 main INFO screen Mike pass=0 dev=0.0 ins=4.81 pro=35 1a=False 1b=False 2=False (69.5s)
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:35:38,406 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 20:35:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:35:38,501 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (110.5s)
Sep 15 20:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:01,860 main INFO screen BC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (106.3s)
Sep 15 20:36:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:01,871 main INFO screen Lokas pass=0 dev=0.0 ins=9.81 pro=52 1a=False 1b=False 2=False (129.0s)
Sep 15 20:36:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:36,656 main INFO screen motion pass=0 dev=0.0 ins=25.01 pro=34 1a=False 1b=False 2=True (58.1s)
Sep 15 20:36:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:53,904 main INFO screen ALLCAT pass=0 dev=0.0 ins=75.89 pro=0 1a=True 1b=True 2=True (52.0s)
Sep 15 20:36:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:36:54,006 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (52.1s)
Sep 15 20:37:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:26,767 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.1s)
Sep 15 20:37:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:44,508 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (50.6s)
Sep 15 20:37:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:37:49,163 main INFO screen Clarity pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (55.2s)
Sep 15 20:38:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 20:38:26,776 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:20:38:26 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T19:10:57Z
--- update 2026-09-15T19:15:59Z
--- update 2026-09-15T19:21:24Z
--- update 2026-09-15T19:26:28Z
--- update 2026-09-15T19:31:32Z
--- update 2026-09-15T19:36:36Z
--- update 2026-09-15T19:42:03Z
--- update 2026-09-15T19:47:11Z
--- update 2026-09-15T19:52:29Z
--- update 2026-09-15T19:57:34Z
--- update 2026-09-15T20:02:36Z
--- update 2026-09-15T20:07:43Z
Running as unit: schaduwbot-wallets.service; invocation ID: 5a26243331f64387869dcc88488d69a0
analyses gestart (84579ff37485)
--- update 2026-09-15T20:13:08Z
--- update 2026-09-15T20:18:13Z
--- update 2026-09-15T20:23:16Z
--- update 2026-09-15T20:28:20Z
--- update 2026-09-15T20:33:25Z
--- update 2026-09-15T20:38:25Z
```

## Analyses (laatste 40 regels)
```
inactive
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
--- /opt/schaduwbot/video_replay.py 20:07:44
20:07:45 venster 2026-09-13 08:07 UTC .. nu, 70021 tokens
20:08:37 klaar in 53s: 53536 tokens, 1839 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
20:07:53 ijk: +2 van 2 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 10}) | verste bak n=350 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:07:56 ijk-diagnose: nieuwste migratie 4.6 min oud | migraties 15/60/240 min: 12/45/165 | al gemeten: 782
20:13:16 ijk: +1 van 1 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=351 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:13:16 ijk-diagnose: nieuwste migratie 1.3 min oud | migraties 15/60/240 min: 7/46/162 | al gemeten: 783
20:18:18 ijk: +1 van 1 kandidaten (2 migraties in het venster, overgeslagen: {'al_gemeten': 1}) | verste bak n=352 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:18:18 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 3/43/160 | al gemeten: 784
20:23:46 ijk: +6 van 8 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 2}) | verste bak n=358 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:23:46 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 11/44/165 | al gemeten: 790
20:28:39 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=359 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:28:40 ijk-diagnose: nieuwste migratie 0.0 min oud | migraties 15/60/240 min: 11/40/164 | al gemeten: 794
20:33:35 ijk: +2 van 2 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=361 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
20:33:35 ijk-diagnose: nieuwste migratie 0.9 min oud | migraties 15/60/240 min: 11/42/160 | al gemeten: 796
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-12 18:00 | 4725 | 483 | 475 | 0 | 109 | 3.8 min |
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
| 09-15 18:00 | 4583 | 90 | 88 | 86 | 0 | 129.8 min |

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
