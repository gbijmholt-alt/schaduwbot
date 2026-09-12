# Schaduwbot status

- tijd: 2026-09-12 21:15:16 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 7 hours, 28 minutes
- bot-service: active
- code-versie: b458321
- schijf: 3.8G/38G | geheugen: 665/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 2488, "tokens_in_memory": 1036, "msgs": 262814, "trades": 76392, "creates": 1036, "decode_fail": 7373, "rpc_calls": 2273, "rpc_errors": 1, "sol_usd": 101.46597171192265, "open_positions": 31, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 20:48:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:48:35,036 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.7s)
Sep 12 20:48:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:48:48,659 main INFO screen MRNA pass=0 dev=0.17 ins=48.95 pro=30 1a=False 1b=False 2=True (53.8s)
Sep 12 20:49:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:49:10,670 main INFO screen cantwin pass=1 dev=0.3 ins=0.03 pro=51 1a=False 1b=False 2=False (66.7s)
Sep 12 20:49:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:49:16,789 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:20:49:16 +0000] "GET /health HTTP/1.1" 200 492 "-" "Python-urllib/3.14"
Sep 12 20:49:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:49:46,304 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (71.3s)
Sep 12 20:49:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:49:52,925 aiohttp.access INFO 198.235.24.233 [12/Sep/2026:20:49:52 +0000] "GET / HTTP/1.0" 404 174 "-" "Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity"
Sep 12 20:50:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:50:15,253 main INFO screen SBP pass=0 dev=0.02 ins=0.0 pro=1 1a=False 1b=False 2=False (86.6s)
Sep 12 20:50:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:50:15,324 main INFO screen watch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.7s)
Sep 12 20:50:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:50:45,594 main INFO screen PADON pass=0 dev=0.0 ins=37.48 pro=17 1a=True 1b=True 2=True (59.3s)
Sep 12 20:50:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:50:54,191 rpc WARNING rpc getTokenLargestAccounts exc Server disconnected
Sep 12 20:51:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:51:10,804 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (55.6s)
Sep 12 20:51:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:51:22,541 main INFO screen ai bs  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.2s)
Sep 12 20:51:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:51:36,270 main INFO screen RWA pass=0 dev=0.0 ins=43.65 pro=11 1a=False 1b=False 2=True (50.7s)
Sep 12 20:51:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:51:39,439 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:20:51:39 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 20:51:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:51:39,463 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:20:51:39 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 12 20:52:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:52:08,307 main INFO screen Token pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.5s)
Sep 12 20:52:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:52:18,902 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (56.4s)
Sep 12 20:52:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:52:33,912 main INFO screen TRUMP pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (57.6s)
Sep 12 20:53:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:53:05,371 main INFO screen PVE pass=0 dev=0.0 ins=41.09 pro=16 1a=False 1b=False 2=True (57.1s)
Sep 12 20:53:17 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:53:17,015 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.1s)
Sep 12 20:53:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:53:45,761 main INFO screen UNITY pass=1 dev=0.0 ins=9.59 pro=73 1a=False 1b=False 2=False (71.8s)
Sep 12 20:54:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:54:06,661 main INFO screen TripleB pass=0 dev=0.35 ins=78.96 pro=5 1a=False 1b=True 2=True (61.3s)
Sep 12 20:54:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:54:28,434 main INFO screen kemo pass=0 dev=0.0 ins=27.71 pro=80 1a=False 1b=False 2=True (71.4s)
Sep 12 20:54:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:54:29,346 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:20:54:29 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 12 20:55:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:55:02,414 main INFO screen UNITY pass=0 dev=0.0 ins=63.95 pro=33 1a=False 1b=False 2=True (76.7s)
Sep 12 20:55:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:55:20,479 main INFO screen ETHFNc pass=0 dev=9.88 ins=0.0 pro=19 1a=False 1b=False 2=False (73.8s)
Sep 12 20:55:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:55:42,620 main INFO screen TeTe pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (74.2s)
Sep 12 20:56:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:56:15,923 main INFO screen Pikachu pass=1 dev=3.49 ins=10.83 pro=49 1a=False 1b=False 2=False (73.5s)
Sep 12 20:56:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:56:18,340 main INFO screen Token pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.9s)
Sep 12 20:56:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:56:35,089 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.5s)
Sep 12 20:57:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:57:25,518 aiohttp.access INFO 85.217.149.4 [12/Sep/2026:20:57:25 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 20:57:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:57:28,255 main INFO screen PUMP pass=0 dev=0.0 ins=29.67 pro=55 1a=False 1b=False 2=False (69.9s)
Sep 12 20:57:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:57:31,275 main INFO screen ALPHA pass=0 dev=0.0 ins=60.3 pro=80 1a=False 1b=False 2=True (75.4s)
Sep 12 20:57:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:57:31,675 main INFO screen NIGGABUTT pass=0 dev=0.0 ins=1.82 pro=28 1a=False 1b=False 2=True (56.6s)
Sep 12 20:58:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:58:14,669 main INFO screen Niggabutt pass=0 dev=0.0 ins=0.95 pro=61 1a=False 1b=False 2=True (46.4s)
Sep 12 20:58:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:58:41,038 main INFO screen assol pass=1 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (69.4s)
Sep 12 20:58:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:58:43,994 main INFO screen DERP pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (72.7s)
Sep 12 20:59:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:59:15,904 main INFO screen Cat pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 12 20:59:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:59:33,288 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.2s)
Sep 12 20:59:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 20:59:34,498 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:20:59:34 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T19:53:42Z
--- update 2026-09-12T19:58:42Z
--- update 2026-09-12T20:03:42Z
--- update 2026-09-12T20:08:43Z
--- update 2026-09-12T20:13:43Z
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
```

## Analyses (laatste 25 regels)
```
inactive
19:28:33   2000 tokens, 234531 trades, 43728 posities (2s)
19:28:35   4000 tokens, 469930 trades, 86030 posities (4s)
19:28:37   6000 tokens, 686745 trades, 126162 posities (6s)
19:28:39   8000 tokens, 912039 trades, 165110 posities (8s)
19:28:41   10000 tokens, 1134949 trades, 207013 posities (10s)
19:28:43   12000 tokens, 1363173 trades, 244092 posities (11s)
19:28:45   14000 tokens, 1629244 trades, 297867 posities (14s)
19:28:47   16000 tokens, 1861152 trades, 340904 posities (16s)
19:28:48   18000 tokens, 2080015 trades, 376103 posities (17s)
19:28:51   20000 tokens, 2329827 trades, 420414 posities (19s)
19:28:52   22000 tokens, 2553211 trades, 460401 posities (21s)
19:28:55   24000 tokens, 2796749 trades, 506835 posities (23s)
19:28:57   26000 tokens, 3030508 trades, 549163 posities (25s)
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
