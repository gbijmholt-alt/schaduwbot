# Schaduwbot status

- tijd: 2026-09-12 22:59:54 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 9 hours, 12 minutes
- bot-service: active
- code-versie: b458321
- schijf: 3.9G/38G | geheugen: 914/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 8767, "tokens_in_memory": 3533, "msgs": 954973, "trades": 299362, "creates": 3533, "decode_fail": 26017, "rpc_calls": 7369, "rpc_errors": 1, "sol_usd": 101.66328394887428, "open_positions": 41, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 21122 | 2763 | 15 | 2763 | 214 | 4904 | 14642 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 586 | 16% | 1.7% | +43.5% | -16.0% | -6.25% | 100% |
| dip35_V1_gescreend_fail | 4654 | 27% | 3.9% | +45.3% | -26.0% | -6.74% | 100% |
| dip35_V1_alle | 5918 | 26% | 4.0% | +44.4% | -25.5% | -7.03% | 100% |
| dip35_V2_gescreend_pass | 583 | 22% | 2.4% | +40.7% | -20.3% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 4710 | 25% | 4.4% | +54.8% | -28.1% | -7.08% | 100% |
| dip35_V2_alle | 5877 | 25% | 4.6% | +52.4% | -27.8% | -7.92% | 100% |
| dip35_V3_gescreend_pass | 586 | 9% | 2.9% | +263.0% | -22.1% | +4.16% | 100% |
| dip35_V3_gescreend_fail | 4820 | 14% | 6.1% | +114.4% | -29.8% | -10.14% | 100% |
| dip35_V3_alle | 5931 | 13% | 6.1% | +116.5% | -29.4% | -10.13% | 100% |
| dip40_V1_gescreend_pass | 555 | 14% | 1.8% | +44.7% | -15.5% | -6.84% | 100% |
| dip40_V1_gescreend_fail | 4573 | 26% | 3.9% | +46.8% | -25.9% | -6.60% | 100% |
| dip40_V1_alle | 5688 | 26% | 3.9% | +46.4% | -25.3% | -6.95% | 100% |
| dip40_V2_gescreend_pass | 553 | 18% | 2.2% | +43.3% | -19.5% | -8.51% | 100% |
| dip40_V2_gescreend_fail | 4602 | 25% | 4.3% | +54.7% | -28.0% | -7.06% | 100% |
| dip40_V2_alle | 5641 | 24% | 4.5% | +52.9% | -27.7% | -8.07% | 100% |
| dip40_V3_gescreend_pass | 556 | 8% | 2.5% | +255.8% | -21.0% | +1.37% | 100% |
| dip40_V3_gescreend_fail | 4699 | 13% | 5.9% | +109.4% | -29.5% | -11.13% | 100% |
| dip40_V3_alle | 5695 | 13% | 5.9% | +111.5% | -29.2% | -11.15% | 100% |
| dip45_V1_gescreend_pass | 531 | 14% | 1.7% | +47.4% | -15.3% | -6.22% | 100% |
| dip45_V1_gescreend_fail | 4486 | 27% | 3.6% | +48.2% | -25.7% | -5.46% | 100% |
| dip45_V1_alle | 5498 | 26% | 3.6% | +48.2% | -25.1% | -5.96% | 100% |
| dip45_V2_gescreend_pass | 528 | 18% | 2.1% | +42.7% | -19.5% | -8.22% | 100% |
| dip45_V2_gescreend_fail | 4506 | 25% | 4.1% | +57.6% | -27.7% | -6.10% | 100% |
| dip45_V2_alle | 5452 | 24% | 4.2% | +56.3% | -27.4% | -7.01% | 100% |
| dip45_V3_gescreend_pass | 531 | 8% | 2.1% | +296.6% | -20.3% | +4.72% | 100% |
| dip45_V3_gescreend_fail | 4589 | 14% | 5.5% | +116.9% | -29.1% | -8.85% | 100% |
| dip45_V3_alle | 5498 | 13% | 5.5% | +121.4% | -28.7% | -8.89% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 459 | 15% | 5.0% | -9.15% | -11.9% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 133 | 21% | 0.0% | +17.74% | -12.5% tot +48.0% | -13.2% | 131% | 55% |
| gepoold_met_xlink | 3870 | 13% | 2.8% | -9.70% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1139 | 18% | 0.0% | +17.08% | -0.1% tot +34.2% | -14.6% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 22:29:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:29:04,901 main INFO screen CHILLGPT pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (53.8s)
Sep 12 22:29:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:29:07,316 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.3s)
Sep 12 22:29:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:29:48,973 main INFO screen Sherwood pass=0 dev=0.0 ins=11.95 pro=58 1a=False 1b=False 2=True (60.1s)
Sep 12 22:30:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:30:02,816 main INFO screen APEBAIT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.9s)
Sep 12 22:30:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:30:04,422 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (57.1s)
Sep 12 22:30:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:30:54,628 main INFO screen XMRCAT pass=0 dev=0.0 ins=15.93 pro=50 1a=False 1b=False 2=True (65.7s)
Sep 12 22:32:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:32:51,015 main INFO screen CZECHEDGE pass=1 dev=0.0 ins=4.73 pro=64 1a=False 1b=False 2=False (68.5s)
Sep 12 22:33:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:33:04,127 main INFO screen ZSTOCK pass=0 dev=0.0 ins=0.87 pro=4 1a=False 1b=False 2=False (55.1s)
Sep 12 22:33:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:33:15,581 main INFO screen SOLCHAN pass=0 dev=0.0 ins=20.79 pro=36 1a=False 1b=False 2=True (64.1s)
Sep 12 22:33:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:33:41,465 main INFO screen wifhat pass=0 dev=0.35 ins=61.39 pro=23 1a=False 1b=True 2=True (50.4s)
Sep 12 22:34:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:34:34,134 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:34:34 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 22:35:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:35:28,572 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.2s)
Sep 12 22:35:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:35:43,860 main INFO screen ANONFLY pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (69.5s)
Sep 12 22:36:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:36:29,959 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (74.1s)
Sep 12 22:36:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:36:41,503 main INFO screen Breadcoin pass=0 dev=0.0 ins=44.42 pro=73 1a=False 1b=False 2=True (72.9s)
Sep 12 22:36:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:36:51,131 main INFO screen Loop pass=1 dev=0.0 ins=11.38 pro=23 1a=False 1b=False 2=False (67.3s)
Sep 12 22:37:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:37:01,929 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:22:37:01 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 22:37:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:37:29,081 main INFO screen PNUT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (59.1s)
Sep 12 22:37:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:37:49,823 main INFO screen DogeI2P pass=1 dev=0.0 ins=0.31 pro=25 1a=False 1b=False 2=False (68.3s)
Sep 12 22:37:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:37:58,452 main INFO screen CHBU pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (67.3s)
Sep 12 22:38:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:38:01,433 aiohttp.access INFO 213.209.159.16 [12/Sep/2026:22:38:01 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 12 22:38:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:38:01,434 aiohttp.access INFO 213.209.159.19 [12/Sep/2026:22:38:01 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 22:38:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:38:01,460 aiohttp.access INFO 213.209.159.21 [12/Sep/2026:22:38:01 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 22:38:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:38:01,484 aiohttp.access INFO 213.209.159.16 [12/Sep/2026:22:38:01 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 22:38:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:38:37,769 main INFO screen OFFAI pass=1 dev=0.0 ins=0.21 pro=11 1a=False 1b=False 2=False (68.7s)
Sep 12 22:39:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:39:03,581 main INFO screen $Mask pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.8s)
Sep 12 22:39:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:39:04,745 main INFO screen Humanscan pass=0 dev=6.63 ins=8.54 pro=32 1a=False 1b=False 2=False (66.3s)
Sep 12 22:39:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:39:28,247 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:39:28 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 22:39:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:39:45,583 main INFO screen Breadcoin pass=0 dev=0.0 ins=11.83 pro=68 1a=False 1b=False 2=True (67.8s)
Sep 12 22:40:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:40:08,732 main INFO screen Zebrigrade pass=0 dev=0.0 ins=16.5 pro=40 1a=False 1b=False 2=True (65.2s)
Sep 12 22:40:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:40:28,013 main INFO screen $cr7 pass=0 dev=0.02 ins=0.0 pro=4 1a=False 1b=False 2=False (70.3s)
Sep 12 22:40:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:40:41,085 main INFO screen zrobincat pass=0 dev=0.35 ins=61.81 pro=18 1a=False 1b=True 2=True (55.5s)
Sep 12 22:41:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:41:04,757 main INFO screen 404 pass=0 dev=0.11 ins=0.0 pro=3 1a=False 1b=False 2=False (56.0s)
Sep 12 22:41:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:41:23,360 main INFO screen Breadcoin pass=0 dev=0.0 ins=4.31 pro=56 1a=False 1b=False 2=True (55.3s)
Sep 12 22:42:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:42:30,219 main INFO screen ANONFLY pass=0 dev=0.0 ins=36.58 pro=25 1a=True 1b=False 2=True (68.6s)
Sep 12 22:42:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:42:51,492 main INFO screen Breadcoin pass=1 dev=0.0 ins=13.59 pro=50 1a=False 1b=False 2=False (68.9s)
Sep 12 22:42:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:42:54,265 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (65.9s)
Sep 12 22:43:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:43:42,154 main INFO screen ANDRÉ pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (71.9s)
Sep 12 22:43:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:43:56,934 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (65.4s)
Sep 12 22:44:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:44:00,886 main INFO screen VPN pass=0 dev=0.01 ins=21.51 pro=47 1a=False 1b=True 2=True (66.6s)
Sep 12 22:44:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:44:29,628 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:44:29 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 22:44:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:44:37,999 main INFO screen SCRVAN pass=0 dev=0.13 ins=0.0 pro=3 1a=False 1b=False 2=False (55.8s)
Sep 12 22:45:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:45:06,519 main INFO screen 5MORE pass=0 dev=0.43 ins=0.0 pro=5 1a=False 1b=False 2=False (65.9s)
Sep 12 22:45:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:45:08,504 main INFO screen UNDERDOG pass=0 dev=0.0 ins=41.02 pro=9 1a=False 1b=False 2=True (61.8s)
Sep 12 22:45:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:45:45,138 main INFO screen Mindshare pass=1 dev=0.36 ins=10.74 pro=40 1a=False 1b=False 2=False (64.8s)
Sep 12 22:46:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:46:18,248 main INFO screen LAPTOP pass=1 dev=0.88 ins=0.0 pro=16 1a=False 1b=False 2=False (64.9s)
Sep 12 22:47:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:47:48,999 main INFO screen RETARDGPT pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (48.4s)
Sep 12 22:48:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:48:43,162 main INFO screen Underdog pass=1 dev=0.0 ins=12.37 pro=17 1a=False 1b=False 2=False (68.9s)
Sep 12 22:48:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:48:46,150 main INFO screen CUMSEY pass=1 dev=0.0 ins=9.64 pro=63 1a=False 1b=False 2=False (74.3s)
Sep 12 22:48:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:48:54,140 main INFO screen IFONU pass=0 dev=1.2 ins=0.0 pro=2 1a=False 1b=False 2=False (65.1s)
Sep 12 22:49:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:49:33,132 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:49:33 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 22:49:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:49:35,938 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.8s)
Sep 12 22:49:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:49:40,144 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.0s)
Sep 12 22:49:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:49:53,910 main INFO screen GrokPepe pass=0 dev=0.35 ins=59.39 pro=20 1a=False 1b=False 2=True (59.8s)
Sep 12 22:50:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:50:25,632 main INFO screen McDonald's pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.7s)
Sep 12 22:50:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:50:47,676 main INFO screen StonKabra pass=1 dev=0.21 ins=0.0 pro=11 1a=False 1b=False 2=False (67.5s)
Sep 12 22:50:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:50:56,670 main INFO screen 404 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.8s)
Sep 12 22:51:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:51:59,298 main INFO screen Underdog pass=0 dev=0.0 ins=23.29 pro=47 1a=False 1b=False 2=False (61.0s)
Sep 12 22:52:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:52:16,855 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.8s)
Sep 12 22:52:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:52:56,643 main INFO screen Chudette pass=0 dev=0.0 ins=9.74 pro=68 1a=False 1b=False 2=True (70.9s)
Sep 12 22:53:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:53:05,488 main INFO screen Underdog pass=1 dev=0.0 ins=0.0 pro=53 1a=False 1b=False 2=False (66.2s)
Sep 12 22:53:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:53:26,588 main INFO screen BFC pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (56.4s)
Sep 12 22:54:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:54:04,070 main INFO screen VPN pass=0 dev=0.0 ins=38.93 pro=16 1a=False 1b=True 2=True (67.4s)
Sep 12 22:54:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:54:16,854 main INFO screen Underdog pass=0 dev=10.99 ins=22.46 pro=44 1a=False 1b=False 2=False (65.7s)
Sep 12 22:54:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:54:36,958 main INFO screen $HELDON pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (70.4s)
Sep 12 22:54:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:54:37,061 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:54:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 22:55:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:55:01,521 main INFO screen MC pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 12 22:55:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:55:13,300 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.4s)
Sep 12 22:55:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:55:29,059 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (52.1s)
Sep 12 22:56:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:56:05,522 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (60.8s)
Sep 12 22:56:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:56:20,258 main INFO screen DERP pass=0 dev=0.27 ins=0.0 pro=2 1a=False 1b=False 2=False (51.5s)
Sep 12 22:57:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:57:08,126 main INFO screen FONEBATON pass=0 dev=0.0 ins=62.01 pro=22 1a=False 1b=True 2=True (67.7s)
Sep 12 22:57:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:57:20,667 main INFO screen Blaze pass=1 dev=0.03 ins=4.34 pro=55 1a=False 1b=False 2=False (66.6s)
Sep 12 22:57:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:57:22,194 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.9s)
Sep 12 22:58:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:58:01,006 main INFO screen GS pass=0 dev=0.0 ins=19.47 pro=43 1a=False 1b=False 2=True (52.9s)
Sep 12 22:58:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:58:22,825 main INFO screen MC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.2s)
Sep 12 22:58:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:58:55,297 main INFO screen McFly pass=0 dev=0.0 ins=36.03 pro=31 1a=False 1b=False 2=True (66.6s)
Sep 12 22:59:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:59:04,397 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.8s)
Sep 12 22:59:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:59:47,129 main INFO screen $speed pass=0 dev=0.21 ins=0.0 pro=4 1a=False 1b=False 2=False (56.4s)
Sep 12 22:59:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 22:59:54,993 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:22:59:54 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: ad453f090a6d431a85bbf496eb255234
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T21:31:20Z
--- update 2026-09-12T21:36:24Z
--- update 2026-09-12T21:41:26Z
--- update 2026-09-12T21:46:35Z
--- update 2026-09-12T21:51:36Z
--- update 2026-09-12T21:57:01Z
--- update 2026-09-12T22:02:18Z
--- update 2026-09-12T22:07:20Z
--- update 2026-09-12T22:12:36Z
--- update 2026-09-12T22:18:15Z
--- update 2026-09-12T22:23:36Z
--- update 2026-09-12T22:29:00Z
--- update 2026-09-12T22:34:03Z
--- update 2026-09-12T22:39:27Z
--- update 2026-09-12T22:44:28Z
--- update 2026-09-12T22:49:32Z
--- update 2026-09-12T22:54:36Z
--- update 2026-09-12T22:59:54Z
```

## Analyses (laatste 25 regels)
```
inactive
21:35:00   4000 tokens, 469629 trades, 83678 posities (4s)
21:35:03   6000 tokens, 686889 trades, 124260 posities (6s)
21:35:05   8000 tokens, 915934 trades, 161908 posities (8s)
21:35:07   10000 tokens, 1134225 trades, 200519 posities (10s)
21:35:09   12000 tokens, 1348165 trades, 236816 posities (12s)
21:35:11   14000 tokens, 1606497 trades, 285128 posities (14s)
21:35:13   16000 tokens, 1845445 trades, 332302 posities (16s)
21:35:15   18000 tokens, 2069349 trades, 368627 posities (18s)
21:35:17   20000 tokens, 2302073 trades, 408799 posities (20s)
21:35:19   22000 tokens, 2532730 trades, 450683 posities (22s)
21:35:20   24000 tokens, 2749646 trades, 487179 posities (24s)
21:35:23   26000 tokens, 3007294 trades, 538811 posities (26s)
21:35:25   28000 tokens, 3243852 trades, 580513 posities (28s)
21:35:27   30000 tokens, 3459040 trades, 615508 posities (30s)
21:35:29   32000 tokens, 3690377 trades, 657198 posities (32s)
21:35:30   34000 tokens, 3910303 trades, 696922 posities (34s)
21:35:33   36000 tokens, 4150741 trades, 742994 posities (36s)
21:35:35   38000 tokens, 4391159 trades, 788453 posities (38s)
21:35:36   40000 tokens, 4609485 trades, 839321 posities (40s)
21:35:37 posities: 846701 uit 4636829 trades (40s)
21:35:48 177416 wallets gerekend
21:35:48 geluk-toets
21:36:20 persistentie
21:36:22 kopieer-simulatie
21:36:33 klaar in 96s -> /opt/schaduwbot/reports/wallets.md
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
