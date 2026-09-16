# Schaduwbot status

- tijd: 2026-09-16 00:16:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 10 hours, 29 minutes
- bot-service: active
- code-versie: 85d446e
- schijf: 7.9G/38G | geheugen: 2493/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 236549, "tokens_in_memory": 11340, "msgs": 41755927, "trades": 7837686, "creates": 82796, "decode_fail": 646486, "rpc_calls": 215550, "rpc_errors": 19, "sol_usd": 96.85612593347433, "open_positions": 63, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 23:51:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:51:09,370 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 15 23:51:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:51:59,575 main INFO screen skipoo126 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (60.5s)
Sep 15 23:52:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:15,493 main INFO screen otis pass=0 dev=0.0 ins=30.65 pro=61 1a=False 1b=False 2=True (73.5s)
Sep 15 23:52:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:17,240 main INFO screen beer pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 15 23:52:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:52:59,017 main INFO screen cbBTC pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (59.4s)
Sep 15 23:53:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:25,042 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (69.5s)
Sep 15 23:53:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:30,833 main INFO screen Rich pass=0 dev=0.0 ins=19.31 pro=0 1a=False 1b=False 2=False (73.6s)
Sep 15 23:53:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:53:55,513 main INFO screen XPXGOLD pass=0 dev=0.0 ins=2.08 pro=0 1a=False 1b=False 2=True (56.5s)
Sep 15 23:54:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:22,319 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.3s)
Sep 15 23:54:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:28,053 main INFO screen DUBS pass=0 dev=0.0 ins=25.79 pro=1 1a=False 1b=False 2=False (57.2s)
Sep 15 23:54:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:54:54,144 main INFO screen YBR pass=0 dev=0.55 ins=0.0 pro=4 1a=False 1b=False 2=False (58.6s)
Sep 15 23:55:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:29,317 main INFO screen att pass=0 dev=0.21 ins=10.99 pro=9 1a=False 1b=False 2=False (67.0s)
Sep 15 23:55:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:30,755 main INFO screen parsa pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.7s)
Sep 15 23:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:38,100 aiohttp.access INFO 143.198.60.223 [15/Sep/2026:23:55:38 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
Sep 15 23:55:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:38,426 aiohttp.access INFO 143.198.60.223 [15/Sep/2026:23:55:38 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "http://167.233.49.49:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
Sep 15 23:55:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:43,275 main INFO screen NTDA pass=0 dev=0.0 ins=146.38 pro=1 1a=False 1b=False 2=True (49.1s)
Sep 15 23:55:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:55:49,741 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:23:55:49 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 23:56:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:56:32,802 main INFO screen ZCAT pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (62.0s)
Sep 15 23:56:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:56:33,516 main INFO screen HERO pass=0 dev=0.0 ins=26.42 pro=48 1a=False 1b=True 2=True (64.2s)
Sep 15 23:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:56:38,593 main INFO screen SolLama pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (55.3s)
Sep 15 23:57:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:57:23,352 main INFO screen ANIMALSG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.8s)
Sep 15 23:57:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:57:23,725 main INFO screen SPATI pass=0 dev=0.0 ins=79.13 pro=1 1a=False 1b=True 2=True (50.9s)
Sep 15 23:57:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:57:41,019 main INFO screen RobIncog pass=0 dev=0.0 ins=51.21 pro=9 1a=False 1b=False 2=True (62.4s)
Sep 15 23:58:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:58:31,257 main INFO screen SPED pass=0 dev=0.0 ins=13.62 pro=59 1a=False 1b=False 2=False (67.9s)
Sep 15 23:58:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:58:33,174 main INFO screen CMDT pass=0 dev=0.0 ins=0.0 pro=72 1a=False 1b=False 2=False (69.4s)
Sep 15 23:58:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:58:42,710 main INFO screen BC pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (61.7s)
Sep 15 23:59:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:59:37,026 main INFO screen Gcoin pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (65.8s)
Sep 15 23:59:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:59:39,967 main INFO screen arfo pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.8s)
Sep 15 23:59:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 23:59:43,554 main INFO screen steptop pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (60.8s)
Sep 16 00:00:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:00:32,746 main INFO screen SPEEDRUN pass=0 dev=0.0 ins=29.76 pro=35 1a=False 1b=False 2=True (55.7s)
Sep 16 00:00:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:00:46,248 main INFO screen MOONTICKET pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (66.3s)
Sep 16 00:00:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:00:46,273 main INFO screen LioraLLM pass=0 dev=0.0 ins=48.49 pro=13 1a=False 1b=False 2=True (62.7s)
Sep 16 00:01:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:01:00,339 aiohttp.access INFO 127.0.0.1 [16/Sep/2026:00:01:00 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 16 00:01:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:01:30,639 main INFO screen Iron Mike pass=0 dev=0.05 ins=0.0 pro=5 1a=False 1b=False 2=False (57.9s)
Sep 16 00:01:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:01:43,049 main INFO screen Rolex pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (56.8s)
Sep 16 00:01:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:01:49,230 main INFO screen WOTF pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (63.0s)
Sep 16 00:02:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:02:24,378 main INFO screen $COOK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.7s)
Sep 16 00:02:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:02:38,754 main INFO screen CPC01 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.7s)
Sep 16 00:02:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:02:52,092 main INFO screen H2O pass=0 dev=0.0 ins=2.54 pro=63 1a=False 1b=False 2=False (62.9s)
Sep 16 00:03:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:03:34,889 main INFO screen KC pass=0 dev=0.0 ins=14.81 pro=68 1a=False 1b=False 2=False (70.5s)
Sep 16 00:04:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:04:00,087 main INFO screen ZC pass=0 dev=0.0 ins=0.0 pro=55 1a=False 1b=False 2=False (68.0s)
Sep 16 00:04:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:04:01,518 main INFO screen DC pass=0 dev=0.0 ins=0.0 pro=65 1a=False 1b=False 2=False (82.8s)
Sep 16 00:04:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:04:38,686 main INFO screen aseven pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (63.8s)
Sep 16 00:05:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:05:13,168 main INFO screen Mitchelle pass=0 dev=0.0 ins=3.18 pro=58 1a=False 1b=False 2=False (73.1s)
Sep 16 00:05:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:05:13,487 main INFO screen gMS-α  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (72.0s)
Sep 16 00:05:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:05:49,426 main INFO screen PATRICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (70.7s)
Sep 16 00:06:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:06:13,004 aiohttp.access INFO 127.0.0.1 [16/Sep/2026:00:06:13 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 16 00:06:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:06:24,323 main INFO screen ELON pass=0 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=True (70.8s)
Sep 16 00:06:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:06:25,281 main INFO screen elizabETH pass=0 dev=0.0 ins=21.23 pro=2 1a=False 1b=False 2=True (72.1s)
Sep 16 00:06:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:06:50,667 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.2s)
Sep 16 00:07:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:07:36,938 main INFO screen HINT pass=0 dev=0.0 ins=33.68 pro=63 1a=False 1b=False 2=True (72.6s)
Sep 16 00:07:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:07:40,263 main INFO screen TRUMPERINE pass=0 dev=0.0 ins=24.98 pro=2 1a=False 1b=False 2=True (75.0s)
Sep 16 00:08:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:08:06,256 main INFO screen ICECUBE pass=0 dev=0.0 ins=25.96 pro=42 1a=False 1b=False 2=True (75.6s)
Sep 16 00:08:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:08:48,107 main INFO screen ANONYCAT pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (71.2s)
Sep 16 00:08:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:08:50,344 main INFO screen Bvlgari pass=0 dev=0.0 ins=139.52 pro=0 1a=False 1b=False 2=True (70.1s)
Sep 16 00:09:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:09:03,100 main INFO screen dougcotler pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.8s)
Sep 16 00:09:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:09:41,392 main INFO screen PATRICK pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (51.0s)
Sep 16 00:09:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:09:43,665 main INFO screen BJ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.6s)
Sep 16 00:10:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:10:07,894 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=74 1a=False 1b=False 2=False (64.8s)
Sep 16 00:10:55 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:10:55,113 main INFO screen OSbroker pass=0 dev=0.0 ins=48.46 pro=17 1a=False 1b=False 2=True (71.4s)
Sep 16 00:10:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:10:57,204 main INFO screen SALLY pass=0 dev=0.0 ins=25.39 pro=4 1a=False 1b=False 2=True (75.8s)
Sep 16 00:11:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:11:05,003 main INFO screen CPI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 16 00:11:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:11:18,233 aiohttp.access INFO 127.0.0.1 [16/Sep/2026:00:11:18 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 16 00:12:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:12:00,321 main INFO screen URCOIN pass=0 dev=3.4 ins=0.0 pro=72 1a=False 1b=False 2=False (63.1s)
Sep 16 00:12:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:12:03,773 main INFO screen $WAGMI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 16 00:12:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:12:06,553 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (61.5s)
Sep 16 00:13:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:13:01,357 main INFO screen LEADER pass=0 dev=0.0 ins=19.26 pro=1 1a=False 1b=False 2=True (61.0s)
Sep 16 00:13:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:13:08,834 main INFO screen MEIRA pass=0 dev=0.0 ins=79.13 pro=2 1a=False 1b=True 2=True (62.3s)
Sep 16 00:13:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:13:10,128 main INFO screen FART pass=0 dev=0.0 ins=24.76 pro=2 1a=False 1b=False 2=True (66.4s)
Sep 16 00:14:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:14:15,742 main INFO screen MadMoney pass=0 dev=0.0 ins=19.98 pro=1 1a=False 1b=False 2=True (66.9s)
Sep 16 00:14:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:14:18,413 main INFO screen RX-78-2 pass=0 dev=0.07 ins=0.0 pro=8 1a=False 1b=False 2=False (77.1s)
Sep 16 00:14:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:14:24,750 main INFO screen GG pass=0 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=True (74.6s)
Sep 16 00:15:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:15:06,687 main INFO screen launchpad pass=0 dev=0.0 ins=34.41 pro=56 1a=False 1b=False 2=True (48.3s)
Sep 16 00:15:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:15:07,586 main INFO screen PATRICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.8s)
Sep 16 00:15:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:15:22,292 aiohttp.access INFO 204.76.203.7 [16/Sep/2026:00:15:22 +0000] "GET / HTTP/1.0" 404 174 "-" "Mozilla/5.0"
Sep 16 00:15:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:15:26,836 main INFO screen GROK pass=0 dev=0.0 ins=22.43 pro=71 1a=False 1b=False 2=True (62.1s)
Sep 16 00:16:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:16:15,957 main INFO screen Brez pass=0 dev=0.0 ins=5.03 pro=70 1a=False 1b=False 2=False (69.3s)
Sep 16 00:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:16:18,645 main INFO screen alekbbesag pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.1s)
Sep 16 00:16:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:16:33,194 main INFO screen KIMCHI pass=0 dev=0.0 ins=6.1 pro=71 1a=False 1b=False 2=True (66.4s)
Sep 16 00:16:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-16 00:16:37,259 aiohttp.access INFO 127.0.0.1 [16/Sep/2026:00:16:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-15T23:45:36Z
--- update 2026-09-15T23:50:40Z
--- update 2026-09-15T23:55:48Z
--- update 2026-09-16T00:00:59Z
--- update 2026-09-16T00:06:11Z
--- update 2026-09-16T00:11:17Z
--- update 2026-09-16T00:16:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: db451c7c987e4b8083248956369ecb2e
analyses gestart (84579ff37485)
```

## Analyses (laatste 40 regels)
```
active
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
--- /opt/schaduwbot/video_replay.py 00:16:36
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
23:46:02 ijk: +5 van 5 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=453 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:46:02 ijk-diagnose: nieuwste migratie -0.2 min oud | migraties 15/60/240 min: 13/46/195 | al gemeten: 917
23:50:45 ijk: +1 van 1 kandidaten (10 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=453 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:50:46 ijk-diagnose: nieuwste migratie 4.9 min oud | migraties 15/60/240 min: 10/42/192 | al gemeten: 918
23:56:18 ijk: +6 van 6 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=457 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:56:18 ijk-diagnose: nieuwste migratie 1.7 min oud | migraties 15/60/240 min: 11/42/194 | al gemeten: 924
00:01:30 ijk: +6 van 7 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=463 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:01:30 ijk-diagnose: nieuwste migratie 0.6 min oud | migraties 15/60/240 min: 13/47/194 | al gemeten: 930
00:06:27 ijk: +3 van 3 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 11}) | verste bak n=464 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:06:27 ijk-diagnose: nieuwste migratie 0.5 min oud | migraties 15/60/240 min: 14/46/192 | al gemeten: 933
00:11:37 ijk: +4 van 4 kandidaten (13 migraties in het venster, overgeslagen: {'al_gemeten': 9}) | verste bak n=468 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:11:37 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 14/46/197 | al gemeten: 937
```

## Screening en houderscheck (laatste 3 dagen, per 6 uur)

| venster (UTC) | aangemaakt | gescreend | top5 gevuld | pas na 2u05 | binnen 90s | gem. wachttijd |
|---|---|---|---|---|---|---|
| 09-13 00:00 | 5654 | 639 | 625 | 0 | 289 | 2.2 min |
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
| 09-15 18:00 | 11470 | 700 | 647 | 696 | 0 | 161.1 min |
| 09-16 00:00 | 301 | 0 | 0 | 0 | 0 | - |

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
