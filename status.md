# Schaduwbot status

- tijd: 2026-09-13 00:53:45 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 11 hours, 6 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.0G/38G | geheugen: 1175/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 15597, "tokens_in_memory": 5873, "msgs": 1777260, "trades": 520225, "creates": 5873, "decode_fail": 47741, "rpc_calls": 13477, "rpc_errors": 1, "sol_usd": 101.71904677495611, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 629 | 67 | 0 | 78 | 13 | 119 | 375 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 597 | 16% | 1.7% | +43.5% | -15.9% | -6.17% | 100% |
| dip35_V1_gescreend_fail | 4670 | 27% | 3.9% | +45.2% | -26.0% | -6.75% | 100% |
| dip35_V1_alle | 6112 | 26% | 4.0% | +44.5% | -25.4% | -6.98% | 100% |
| dip35_V2_gescreend_pass | 593 | 22% | 2.4% | +40.2% | -20.3% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 4738 | 25% | 4.4% | +54.9% | -28.0% | -7.02% | 100% |
| dip35_V2_alle | 6068 | 25% | 4.6% | +52.2% | -27.7% | -7.98% | 100% |
| dip35_V3_gescreend_pass | 600 | 9% | 2.8% | +261.0% | -22.0% | +4.43% | 100% |
| dip35_V3_gescreend_fail | 4855 | 14% | 6.1% | +118.5% | -29.7% | -9.42% | 100% |
| dip35_V3_alle | 6125 | 13% | 6.1% | +117.9% | -29.3% | -9.82% | 100% |
| dip40_V1_gescreend_pass | 567 | 14% | 1.8% | +44.5% | -15.5% | -6.79% | 100% |
| dip40_V1_gescreend_fail | 4592 | 26% | 3.9% | +46.8% | -25.8% | -6.62% | 100% |
| dip40_V1_alle | 5877 | 26% | 3.9% | +46.5% | -25.2% | -6.84% | 100% |
| dip40_V2_gescreend_pass | 565 | 18% | 2.1% | +42.5% | -19.5% | -8.51% | 100% |
| dip40_V2_gescreend_fail | 4635 | 25% | 4.3% | +54.7% | -27.9% | -7.02% | 100% |
| dip40_V2_alle | 5827 | 24% | 4.4% | +52.7% | -27.6% | -8.05% | 100% |
| dip40_V3_gescreend_pass | 571 | 8% | 2.5% | +253.8% | -20.9% | +1.70% | 100% |
| dip40_V3_gescreend_fail | 4739 | 13% | 5.8% | +114.0% | -29.4% | -10.35% | 100% |
| dip40_V3_alle | 5884 | 13% | 5.8% | +113.3% | -29.1% | -10.74% | 100% |
| dip45_V1_gescreend_pass | 545 | 15% | 1.7% | +47.2% | -15.2% | -6.07% | 100% |
| dip45_V1_gescreend_fail | 4507 | 27% | 3.6% | +48.2% | -25.6% | -5.49% | 100% |
| dip45_V1_alle | 5680 | 26% | 3.6% | +48.4% | -25.0% | -5.91% | 100% |
| dip45_V2_gescreend_pass | 542 | 18% | 2.0% | +41.5% | -19.5% | -8.20% | 100% |
| dip45_V2_gescreend_fail | 4542 | 25% | 4.0% | +58.3% | -27.6% | -5.86% | 100% |
| dip45_V2_alle | 5631 | 24% | 4.1% | +56.6% | -27.3% | -6.90% | 100% |
| dip45_V3_gescreend_pass | 549 | 8% | 2.0% | +286.8% | -20.2% | +4.92% | 100% |
| dip45_V3_gescreend_fail | 4631 | 14% | 5.5% | +121.0% | -29.0% | -8.03% | 100% |
| dip45_V3_alle | 5680 | 13% | 5.4% | +123.3% | -28.6% | -8.52% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 470 | 16% | 4.9% | -8.29% | -11.5% tot -5.1% | -14.3% | – | 100% |
| per_token_zonder_xlink | 143 | 22% | 0.0% | +16.44% | -11.7% tot +44.6% | -13.2% | 131% | 58% |
| gepoold_met_xlink | 3941 | 13% | 2.7% | -9.45% | -10.7% tot -8.2% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1188 | 19% | 0.0% | +16.34% | -0.1% tot +32.8% | -14.4% | 72% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 13 00:13:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:13:44,384 main INFO screen Solana pass=0 dev=0.52 ins=0.0 pro=2 1a=False 1b=False 2=False (67.5s)
Sep 13 00:14:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:14:02,449 main INFO screen GME pass=0 dev=0.0 ins=16.7 pro=26 1a=False 1b=False 2=True (55.2s)
Sep 13 00:14:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:14:29,795 main INFO screen $AGENT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.2s)
Sep 13 00:14:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:14:50,989 main INFO screen DOOB pass=0 dev=8.72 ins=0.0 pro=17 1a=False 1b=False 2=False (66.6s)
Sep 13 00:15:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:15:05,101 main INFO screen MIST pass=0 dev=0.0 ins=20.11 pro=54 1a=False 1b=False 2=True (62.7s)
Sep 13 00:15:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:15:16,512 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:00:15:16 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 00:15:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:15:37,332 main INFO screen Hedgehog pass=0 dev=0.0 ins=12.9 pro=67 1a=False 1b=False 2=True (67.5s)
Sep 13 00:15:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:15:54,392 main INFO screen Memestonk pass=0 dev=0.0 ins=12.17 pro=67 1a=False 1b=False 2=True (63.4s)
Sep 13 00:16:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:16:35,554 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (53.2s)
Sep 13 00:16:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:16:56,775 main INFO screen Toyota pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.4s)
Sep 13 00:17:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:17:16,589 main INFO screen Pipi pass=0 dev=0.0 ins=15.78 pro=35 1a=False 1b=False 2=True (51.5s)
Sep 13 00:17:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:17:33,366 main INFO screen AXIOM pass=0 dev=0.0 ins=27.68 pro=33 1a=False 1b=False 2=True (48.4s)
Sep 13 00:17:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:17:37,086 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:17:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:18:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:18:09,336 main INFO screen WOFI pass=0 dev=0.0 ins=79.31 pro=4 1a=False 1b=False 2=True (65.2s)
Sep 13 00:18:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:18:15,678 main INFO screen AXIOM pass=0 dev=0.0 ins=24.24 pro=15 1a=False 1b=False 2=True (59.1s)
Sep 13 00:18:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:18:24,213 main INFO screen AXIOM pass=0 dev=0.0 ins=9.94 pro=36 1a=False 1b=False 2=False (50.8s)
Sep 13 00:19:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:19:01,071 main INFO screen MIST pass=1 dev=0.0 ins=19.34 pro=23 1a=False 1b=False 2=False (51.7s)
Sep 13 00:19:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:19:29,582 main INFO screen AXIOM pass=0 dev=0.0 ins=24.78 pro=39 1a=False 1b=False 2=True (73.9s)
Sep 13 00:19:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:19:38,787 main INFO screen PMARCA pass=0 dev=38.19 ins=2.94 pro=1 1a=False 1b=False 2=True (74.6s)
Sep 13 00:20:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:20:04,973 main INFO screen AXIOM pass=0 dev=0.0 ins=21.42 pro=68 1a=False 1b=False 2=True (63.9s)
Sep 13 00:20:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:20:52,828 main INFO screen VOID pass=0 dev=40.67 ins=0.0 pro=3 1a=False 1b=False 2=False (83.2s)
Sep 13 00:20:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:20:56,915 main INFO screen TOAD pass=1 dev=0.21 ins=0.0 pro=17 1a=False 1b=False 2=False (78.1s)
Sep 13 00:21:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:21:20,530 main INFO screen JUSTICEHOUSE pass=0 dev=0.0 ins=26.79 pro=66 1a=False 1b=False 2=True (75.6s)
Sep 13 00:21:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:21:59,020 main INFO screen Popups pass=0 dev=0.0 ins=48.54 pro=20 1a=False 1b=False 2=True (66.2s)
Sep 13 00:22:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:22:10,903 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (74.0s)
Sep 13 00:22:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:22:27,276 main INFO screen CHADSTER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.7s)
Sep 13 00:22:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:22:48,124 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:22:48 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:23:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:23:05,368 main INFO screen Axiom pass=0 dev=0.0 ins=27.28 pro=69 1a=False 1b=False 2=True (66.3s)
Sep 13 00:23:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:23:16,524 main INFO screen Hasan  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.6s)
Sep 13 00:23:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:23:25,351 main INFO screen WIFS pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (58.1s)
Sep 13 00:23:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:23:28,277 aiohttp.access INFO 149.232.209.58 [13/Sep/2026:00:23:28 +0000] "GET / HTTP/1.0" 404 174 "-" "-"
Sep 13 00:23:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:23:56,974 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 13 00:24:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:24:07,647 main INFO screen Axiom pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (51.1s)
Sep 13 00:24:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:24:19,609 main INFO screen $TWINE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.3s)
Sep 13 00:24:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:24:50,612 main INFO screen ALONBER pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (53.6s)
Sep 13 00:26:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:26:41,579 main INFO screen Stable pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=True 2=True (63.8s)
Sep 13 00:27:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:27:49,265 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:27:49 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:28:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:28:19,836 main INFO screen SHADYPEPE pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (69.1s)
Sep 13 00:28:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:28:43,191 main INFO screen batonpepe pass=0 dev=0.14 ins=79.17 pro=6 1a=False 1b=True 2=True (57.7s)
Sep 13 00:29:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:29:30,556 main INFO screen GAYCOIN pass=1 dev=3.47 ins=10.24 pro=49 1a=False 1b=False 2=False (68.6s)
Sep 13 00:31:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:31:40,189 main INFO screen OpenAI pass=0 dev=99.32 ins=0.0 pro=1 1a=False 1b=False 2=True (50.1s)
Sep 13 00:31:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:31:54,126 main INFO screen COOK pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=False (51.3s)
Sep 13 00:32:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:32:00,042 main INFO screen LEGO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.1s)
Sep 13 00:32:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:32:52,679 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:32:52 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 13 00:33:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:33:07,204 main INFO screen LAST pass=0 dev=0.17 ins=47.65 pro=23 1a=False 1b=False 2=True (55.0s)
Sep 13 00:33:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:33:29,360 main INFO screen TPD pass=0 dev=0.0 ins=1.72 pro=2 1a=False 1b=False 2=False (53.8s)
Sep 13 00:34:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:34:55,743 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (99.5s)
Sep 13 00:35:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:35:48,066 main INFO screen Rugxiom pass=1 dev=0.49 ins=5.95 pro=38 1a=False 1b=False 2=False (70.5s)
Sep 13 00:37:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:37:46,168 main INFO screen Stable pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=True 2=True (59.9s)
Sep 13 00:38:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:38:17,645 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:38:17 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:38:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:38:31,386 main INFO screen LINK pass=0 dev=0.0 ins=25.43 pro=70 1a=False 1b=False 2=True (67.2s)
Sep 13 00:38:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:38:39,520 main INFO screen ☉ pass=0 dev=0.0 ins=16.54 pro=44 1a=False 1b=False 2=True (62.0s)
Sep 13 00:38:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:38:56,976 main INFO screen VOLVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.1s)
Sep 13 00:40:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:40:28,208 main INFO screen BOHM pass=0 dev=3.42 ins=10.21 pro=75 1a=False 1b=False 2=True (61.5s)
Sep 13 00:42:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:42:06,268 main INFO screen BetOnBlak pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (59.5s)
Sep 13 00:42:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:42:30,107 main INFO screen HOBBES pass=0 dev=0.0 ins=22.96 pro=47 1a=False 1b=False 2=False (61.8s)
Sep 13 00:43:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:43:32,550 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:43:32 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:43:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:43:58,152 main INFO screen Outsider pass=0 dev=0.0 ins=17.88 pro=63 1a=False 1b=False 2=True (62.1s)
Sep 13 00:44:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:44:22,514 main INFO screen fuh ai pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.0s)
Sep 13 00:45:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:45:10,591 main INFO screen LaMisery pass=0 dev=0.03 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 13 00:45:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:45:17,016 main INFO screen batonbull pass=0 dev=0.11 ins=79.2 pro=8 1a=False 1b=True 2=True (51.1s)
Sep 13 00:46:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:46:06,309 main INFO screen Z&Z pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (56.8s)
Sep 13 00:47:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:47:06,737 main INFO screen WOJAKGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (54.0s)
Sep 13 00:48:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:48:02,756 main INFO screen Claude pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (50.3s)
Sep 13 00:48:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:48:37,336 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:48:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:48:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:48:40,298 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.7s)
Sep 13 00:48:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:48:49,637 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.6s)
Sep 13 00:50:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:50:14,060 main INFO screen MIRAGE pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (57.2s)
Sep 13 00:50:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:50:42,847 main INFO screen MIRAGE pass=0 dev=0.0 ins=15.62 pro=67 1a=False 1b=False 2=True (75.7s)
Sep 13 00:50:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:50:44,419 main INFO screen DAD pass=0 dev=0.0 ins=0.45 pro=72 1a=False 1b=False 2=True (76.5s)
Sep 13 00:51:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:51:24,173 main INFO screen MIRAGE pass=0 dev=0.0 ins=8.49 pro=69 1a=False 1b=False 2=True (70.1s)
Sep 13 00:51:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:51:33,282 main INFO screen MIRAGE pass=0 dev=0.0 ins=5.67 pro=29 1a=False 1b=False 2=True (48.9s)
Sep 13 00:51:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:51:35,926 main INFO screen mirage pass=0 dev=0.0 ins=7.81 pro=6 1a=False 1b=False 2=True (53.1s)
Sep 13 00:52:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:52:16,886 main INFO screen MIRAGE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.7s)
Sep 13 00:52:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:52:25,582 main INFO screen Samsung pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.3s)
Sep 13 00:52:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:52:29,555 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.6s)
Sep 13 00:53:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:53:10,188 main INFO screen MIRAGE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.3s)
Sep 13 00:53:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:53:35,072 main INFO screen MIRAGE pass=1 dev=0.0 ins=7.14 pro=49 1a=False 1b=False 2=False (69.5s)
Sep 13 00:53:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:53:38,692 main INFO screen Wood pass=0 dev=0.39 ins=0.0 pro=4 1a=False 1b=False 2=False (69.1s)
Sep 13 00:53:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:53:45,255 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:53:45 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T23:25:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: 4b459aa2bd234295a955bfddf4ef5023
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T23:31:06Z
--- update 2026-09-12T23:36:09Z
--- update 2026-09-12T23:41:31Z
--- update 2026-09-12T23:46:36Z
--- update 2026-09-12T23:51:35Z
--- update 2026-09-12T23:56:36Z
--- update 2026-09-13T00:01:41Z
--- update 2026-09-13T00:07:34Z
--- update 2026-09-13T00:12:34Z
--- update 2026-09-13T00:17:36Z
--- update 2026-09-13T00:22:47Z
--- update 2026-09-13T00:27:48Z
--- update 2026-09-13T00:32:51Z
--- update 2026-09-13T00:38:16Z
--- update 2026-09-13T00:43:31Z
--- update 2026-09-13T00:48:36Z
--- update 2026-09-13T00:53:44Z
```

## Analyses (laatste 25 regels)
```
inactive
23:35:46   6000 tokens, 688210 trades, 122374 posities (6s)
23:35:48   8000 tokens, 921686 trades, 162734 posities (8s)
23:35:50   10000 tokens, 1135604 trades, 196113 posities (10s)
23:35:51   12000 tokens, 1349153 trades, 233527 posities (12s)
23:35:53   14000 tokens, 1588659 trades, 274748 posities (14s)
23:35:55   16000 tokens, 1834927 trades, 321633 posities (16s)
23:35:57   18000 tokens, 2068652 trades, 363238 posities (18s)
23:35:59   20000 tokens, 2279221 trades, 395972 posities (19s)
23:36:01   22000 tokens, 2522883 trades, 438063 posities (22s)
23:36:03   24000 tokens, 2754441 trades, 480456 posities (24s)
23:36:05   26000 tokens, 2971188 trades, 518109 posities (26s)
23:36:08   28000 tokens, 3219985 trades, 563915 posities (28s)
23:36:10   30000 tokens, 3442161 trades, 600680 posities (31s)
23:36:12   32000 tokens, 3661378 trades, 636345 posities (32s)
23:36:14   34000 tokens, 3894647 trades, 678808 posities (34s)
23:36:16   36000 tokens, 4117009 trades, 718803 posities (36s)
23:36:18   38000 tokens, 4355204 trades, 762415 posities (38s)
23:36:20   40000 tokens, 4596413 trades, 807401 posities (40s)
23:36:22   42000 tokens, 4826483 trades, 859888 posities (42s)
23:36:23 posities: 876726 uit 4907398 trades (43s)
23:36:34 183439 wallets gerekend
23:36:34 geluk-toets
23:37:07 persistentie
23:37:10 kopieer-simulatie
23:37:33 klaar in 113s -> /opt/schaduwbot/reports/wallets.md
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
