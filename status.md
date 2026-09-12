# Schaduwbot status

- tijd: 2026-09-12 21:31:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 7 hours, 44 minutes
- bot-service: active
- code-versie: b458321
- schijf: 3.9G/38G | geheugen: 716/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 3453, "tokens_in_memory": 1480, "msgs": 355138, "trades": 109213, "creates": 1480, "decode_fail": 9959, "rpc_calls": 3088, "rpc_errors": 1, "sol_usd": 101.46737481165076, "open_positions": 83, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 18267 | 2506 | 14 | 2506 | 182 | 4425 | 13229 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 577 | 16% | 1.7% | +43.6% | -16.1% | -6.24% | 100% |
| dip35_V1_gescreend_fail | 4629 | 27% | 4.0% | +45.3% | -26.1% | -6.74% | 100% |
| dip35_V1_alle | 5756 | 26% | 4.1% | +44.5% | -25.5% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 574 | 22% | 2.4% | +40.8% | -20.3% | -6.69% | 100% |
| dip35_V2_gescreend_fail | 4683 | 25% | 4.4% | +54.8% | -28.1% | -7.07% | 100% |
| dip35_V2_alle | 5716 | 25% | 4.7% | +52.1% | -27.8% | -7.98% | 100% |
| dip35_V3_gescreend_pass | 575 | 9% | 3.0% | +266.5% | -22.1% | +4.01% | 100% |
| dip35_V3_gescreend_fail | 4783 | 14% | 6.1% | +111.0% | -29.9% | -10.81% | 100% |
| dip35_V3_alle | 5768 | 13% | 6.2% | +114.8% | -29.5% | -10.43% | 100% |
| dip40_V1_gescreend_pass | 545 | 14% | 1.8% | +45.4% | -15.6% | -6.94% | 100% |
| dip40_V1_gescreend_fail | 4548 | 27% | 3.9% | +46.8% | -26.0% | -6.62% | 100% |
| dip40_V1_alle | 5529 | 26% | 4.0% | +46.7% | -25.3% | -6.94% | 100% |
| dip40_V2_gescreend_pass | 543 | 17% | 2.2% | +43.6% | -19.5% | -8.53% | 100% |
| dip40_V2_gescreend_fail | 4575 | 25% | 4.3% | +54.6% | -28.1% | -7.09% | 100% |
| dip40_V2_alle | 5483 | 24% | 4.5% | +52.7% | -27.7% | -8.18% | 100% |
| dip40_V3_gescreend_pass | 545 | 8% | 2.6% | +265.1% | -21.0% | +1.58% | 100% |
| dip40_V3_gescreend_fail | 4663 | 13% | 5.9% | +105.8% | -29.6% | -11.83% | 100% |
| dip40_V3_alle | 5536 | 13% | 6.0% | +110.2% | -29.2% | -11.47% | 100% |
| dip45_V1_gescreend_pass | 522 | 15% | 1.7% | +47.5% | -15.4% | -6.22% | 100% |
| dip45_V1_gescreend_fail | 4459 | 28% | 3.6% | +48.2% | -25.8% | -5.46% | 100% |
| dip45_V1_alle | 5347 | 26% | 3.6% | +48.2% | -25.1% | -5.91% | 100% |
| dip45_V2_gescreend_pass | 519 | 18% | 2.1% | +42.7% | -19.5% | -8.11% | 100% |
| dip45_V2_gescreend_fail | 4475 | 25% | 4.1% | +57.4% | -27.8% | -6.17% | 100% |
| dip45_V2_alle | 5303 | 24% | 4.2% | +55.9% | -27.3% | -7.11% | 100% |
| dip45_V3_gescreend_pass | 522 | 8% | 2.1% | +303.1% | -20.3% | +5.08% | 100% |
| dip45_V3_gescreend_fail | 4547 | 14% | 5.6% | +111.2% | -29.2% | -9.97% | 100% |
| dip45_V3_alle | 5347 | 13% | 5.5% | +118.0% | -28.7% | -9.43% | 100% |

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
| per_token_met_xlink | 451 | 15% | 5.1% | -9.20% | -12.0% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3803 | 13% | 2.8% | -9.77% | -11.0% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 20:59:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:59:42,173 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.2s)
Sep 12 21:00:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:00:11,937 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.0s)
Sep 12 21:00:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:00:46,070 main INFO screen RISE pass=0 dev=43.16 ins=0.0 pro=6 1a=False 1b=False 2=False (72.8s)
Sep 12 21:00:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:00:48,422 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.2s)
Sep 12 21:01:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:01:05,500 main INFO screen Benz pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 12 21:01:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:01:41,708 main INFO screen asshol pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (55.6s)
Sep 12 21:01:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:01:56,671 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (59.0s)
Sep 12 21:02:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:02:37,294 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:21:02:37 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 21:03:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:03:16,809 main INFO screen NIGGABUTT pass=0 dev=41.09 ins=20.0 pro=50 1a=False 1b=False 2=True (66.3s)
Sep 12 21:03:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:03:19,472 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (63.5s)
Sep 12 21:03:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:03:47,354 main INFO screen Apple pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.6s)
Sep 12 21:04:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:04:08,292 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.5s)
Sep 12 21:04:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:04:37,230 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:04:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 12 21:04:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:04:59,833 main INFO screen CMAX pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.0s)
Sep 12 21:05:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:05:10,640 main INFO screen Rge pass=0 dev=3.29 ins=0.0 pro=1 1a=False 1b=False 2=False (69.6s)
Sep 12 21:05:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:05:22,609 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (69.4s)
Sep 12 21:06:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:06:25,676 main INFO screen Loom pass=0 dev=0.0 ins=30.81 pro=10 1a=False 1b=False 2=True (73.2s)
Sep 12 21:06:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:06:30,977 main INFO screen NIGGABUTT pass=0 dev=0.0 ins=49.22 pro=71 1a=False 1b=False 2=True (69.6s)
Sep 12 21:06:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:06:39,013 main INFO screen ChatGPT pass=0 dev=95.38 ins=0.0 pro=1 1a=False 1b=False 2=True (51.7s)
Sep 12 21:07:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:07:30,337 main INFO screen NIGGABUTT pass=0 dev=0.0 ins=28.72 pro=6 1a=False 1b=False 2=False (59.4s)
Sep 12 21:07:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:07:33,895 main INFO screen RIPTRUMP  pass=1 dev=0.0 ins=5.91 pro=40 1a=False 1b=False 2=False (68.2s)
Sep 12 21:07:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:07:44,226 main INFO screen DOGESAURUS pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (65.2s)
Sep 12 21:08:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:08:37,588 main INFO screen HOODCAT pass=0 dev=0.0 ins=6.35 pro=29 1a=False 1b=False 2=True (63.7s)
Sep 12 21:08:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:08:40,147 main INFO screen wind pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (69.8s)
Sep 12 21:08:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:08:47,475 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (63.2s)
Sep 12 21:09:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:09:29,454 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.9s)
Sep 12 21:09:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:09:46,677 main INFO screen LordVerity pass=0 dev=0.0 ins=26.08 pro=75 1a=False 1b=False 2=True (66.5s)
Sep 12 21:09:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:09:58,232 main INFO screen TEST pass=0 dev=0.0 ins=36.62 pro=21 1a=False 1b=False 2=True (70.8s)
Sep 12 21:10:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:10:11,428 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:10:11 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 12 21:10:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:10:45,355 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (75.9s)
Sep 12 21:10:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:10:57,368 main INFO screen att pass=0 dev=0.01 ins=0.0 pro=5 1a=False 1b=False 2=False (70.7s)
Sep 12 21:11:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:11:04,414 main INFO screen DOGESAUR pass=0 dev=5.3 ins=0.0 pro=2 1a=False 1b=False 2=False (66.2s)
Sep 12 21:11:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:11:56,850 main INFO screen MPGA pass=0 dev=0.0 ins=32.95 pro=61 1a=False 1b=False 2=True (71.5s)
Sep 12 21:11:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:11:58,481 main INFO screen ALL pass=0 dev=79.31 ins=22.49 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 12 21:11:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:11:59,912 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (62.5s)
Sep 12 21:13:01 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:13:01,921 main INFO screen SPIDER pass=0 dev=0.0 ins=12.87 pro=61 1a=False 1b=False 2=True (63.4s)
Sep 12 21:13:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:13:03,823 main INFO screen ROTATOOR pass=1 dev=3.42 ins=1.52 pro=69 1a=False 1b=False 2=False (67.0s)
Sep 12 21:13:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:13:19,836 main INFO screen SPIDER pass=0 dev=0.0 ins=30.61 pro=20 1a=False 1b=False 2=True (66.9s)
Sep 12 21:14:24 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:14:24,141 main INFO screen TANGLE pass=0 dev=0.0 ins=41.8 pro=55 1a=False 1b=False 2=True (50.4s)
Sep 12 21:15:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:15:16,062 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:15:16 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 21:15:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:15:35,103 main INFO screen RAY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.7s)
Sep 12 21:16:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:16:12,650 main INFO screen Quack pass=1 dev=0.0 ins=1.9 pro=48 1a=False 1b=False 2=False (69.9s)
Sep 12 21:16:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:16:41,625 main INFO screen Giga pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (68.2s)
Sep 12 21:16:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:16:57,312 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (54.1s)
Sep 12 21:17:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:17:55,703 main INFO screen bullpump pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.4s)
Sep 12 21:18:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:18:48,703 main INFO screen watch pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (71.0s)
Sep 12 21:19:03 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:19:03,322 main INFO screen dula pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (63.0s)
Sep 12 21:19:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:19:26,670 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 12 21:20:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:20:04,509 main INFO screen vrl pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (65.5s)
Sep 12 21:20:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:20:15,836 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:20:15 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 21:20:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:20:35,272 main INFO screen SCoin pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (56.9s)
Sep 12 21:21:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:21:06,164 main INFO screen HVAC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.0s)
Sep 12 21:21:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:21:09,527 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.0s)
Sep 12 21:21:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:21:43,533 main INFO screen QQQ pass=1 dev=0.0 ins=4.76 pro=39 1a=False 1b=False 2=False (68.3s)
Sep 12 21:22:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:22:07,082 main INFO screen SAFEMOON pass=0 dev=0.0 ins=25.34 pro=52 1a=True 1b=False 2=False (60.9s)
Sep 12 21:22:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:22:14,422 main INFO screen Credit pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.9s)
Sep 12 21:23:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:23:02,176 main INFO screen HOOD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (49.7s)
Sep 12 21:23:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:23:28,145 main INFO screen SGM pass=1 dev=2.42 ins=0.0 pro=56 1a=False 1b=False 2=False (68.4s)
Sep 12 21:24:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:24:29,706 main INFO screen KEMO pass=0 dev=3.43 ins=18.27 pro=61 1a=False 1b=False 2=True (70.8s)
Sep 12 21:24:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:24:30,402 main INFO screen VOID  pass=0 dev=39.93 ins=0.0 pro=4 1a=False 1b=False 2=False (72.1s)
Sep 12 21:24:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:24:38,568 main INFO screen BATON pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (70.4s)
Sep 12 21:25:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:15,739 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:21:25:15 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 21:25:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:16,095 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:21:25:16 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 21:25:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:37,472 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:25:37 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 21:25:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:45,653 main INFO screen Holder pass=0 dev=0.0 ins=50.54 pro=76 1a=False 1b=False 2=True (75.9s)
Sep 12 21:25:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:46,545 main INFO screen Bot pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (76.1s)
Sep 12 21:25:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:25:47,196 main INFO screen BURP pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.6s)
Sep 12 21:26:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:50,105 main INFO screen $CHILL pass=0 dev=0.06 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 12 21:26:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:50,384 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (63.2s)
Sep 12 21:26:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:26:53,575 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.9s)
Sep 12 21:28:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:09,599 main INFO screen USMS pass=0 dev=0.01 ins=0.0 pro=8 1a=False 1b=False 2=False (79.2s)
Sep 12 21:28:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:10,926 main INFO screen ZEC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (77.3s)
Sep 12 21:28:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:28:11,543 main INFO screen HOODLANA pass=0 dev=0.0 ins=39.65 pro=61 1a=False 1b=False 2=True (81.4s)
Sep 12 21:29:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:18,182 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (68.6s)
Sep 12 21:29:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:28,642 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (77.7s)
Sep 12 21:29:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:29:30,776 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (79.2s)
Sep 12 21:30:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:30,924 main INFO screen BS pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (72.7s)
Sep 12 21:30:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:41,461 main INFO screen REVOLUT pass=1 dev=0.21 ins=0.0 pro=14 1a=False 1b=False 2=False (72.8s)
Sep 12 21:30:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:30:49,313 main INFO screen PUPPY pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (78.5s)
Sep 12 21:31:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 21:31:21,348 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:21:31:21 +0000] "GET /health HTTP/1.1" 200 498 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T20:18:43Z
--- update 2026-09-12T20:23:43Z
--- update 2026-09-12T20:28:44Z
--- update 2026-09-12T20:33:44Z
nieuwe code: b458321
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T20:38:58Z
--- update 2026-09-12T20:44:07Z
--- update 2026-09-12T20:49:15Z
--- update 2026-09-12T20:54:28Z
--- update 2026-09-12T20:59:33Z
--- update 2026-09-12T21:04:36Z
--- update 2026-09-12T21:10:10Z
--- update 2026-09-12T21:15:15Z
--- update 2026-09-12T21:20:14Z
--- update 2026-09-12T21:25:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: ad453f090a6d431a85bbf496eb255234
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T21:31:20Z
```

## Analyses (laatste 25 regels)
```
active
19:28:59   28000 tokens, 3260600 trades, 588722 posities (27s)
19:29:01   30000 tokens, 3497390 trades, 631312 posities (29s)
19:29:03   32000 tokens, 3708145 trades, 669692 posities (31s)
19:29:05   34000 tokens, 3939276 trades, 712847 posities (34s)
19:29:07   36000 tokens, 4195644 trades, 763072 posities (36s)
19:29:10   38000 tokens, 4428707 trades, 815767 posities (38s)
19:29:10 posities: 836053 uit 4520254 trades (39s)
19:29:21 174384 wallets gerekend
19:29:21 geluk-toets
19:29:55 persistentie
19:29:57 kopieer-simulatie
19:30:09 klaar in 98s -> /opt/schaduwbot/reports/wallets.md
21:25:37 38271 tokens sinds start volledige logging, waarvan 12041 met een gat door herstart
21:25:40   ingelezen tot rowid 4616991 (96737 rijen, 96737 bruikbaar)
21:25:40 ingelezen: 96737 nieuwe trades, 96737 bruikbaar (4s)
21:26:13 543 aankopen van gevolgde wallets geëvalueerd
21:26:22 vroege kopers: 149 voldoen nu, register 224, 0 tokens beoordeeld
21:26:32 grote spelers: saldo van 381 wallets opgehaald
21:26:54 herkomst: 40 posities gekoppeld
21:26:57 klaar in 81s -> /opt/schaduwbot/reports/ledger.md
21:27:34 S1: gezakt — toets n=573, verkennend n=14656
21:27:34 klaar in 36s -> /opt/schaduwbot/reports/hypotheses.md
21:27:34 na-migratie: 400 paren te checken
21:31:14 na-migratie: 10 paren, 40 prijzen
21:31:15 probe: 400 transacties ophalen
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
