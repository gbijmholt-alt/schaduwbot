# Schaduwbot status

- tijd: 2026-09-13 00:22:48 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 10 hours, 35 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.0G/38G | geheugen: 1133/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 13740, "tokens_in_memory": 5322, "msgs": 1559462, "trades": 478650, "creates": 5322, "decode_fail": 41441, "rpc_calls": 12465, "rpc_errors": 1, "sol_usd": 101.59523617547457, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 22486 | 2931 | 15 | 2911 | 241 | 5242 | 15592 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 590 | 16% | 1.7% | +43.5% | -15.9% | -6.17% | 100% |
| dip35_V1_gescreend_fail | 4663 | 27% | 3.9% | +45.2% | -26.0% | -6.75% | 100% |
| dip35_V1_alle | 6034 | 26% | 4.0% | +44.6% | -25.4% | -6.95% | 100% |
| dip35_V2_gescreend_pass | 587 | 22% | 2.4% | +40.5% | -20.3% | -6.85% | 100% |
| dip35_V2_gescreend_fail | 4720 | 25% | 4.4% | +54.7% | -28.0% | -7.08% | 100% |
| dip35_V2_alle | 5982 | 25% | 4.6% | +52.3% | -27.8% | -7.99% | 100% |
| dip35_V3_gescreend_pass | 592 | 9% | 2.9% | +258.6% | -22.1% | +4.01% | 100% |
| dip35_V3_gescreend_fail | 4836 | 14% | 6.1% | +114.9% | -29.7% | -10.02% | 100% |
| dip35_V3_alle | 6040 | 13% | 6.1% | +115.6% | -29.4% | -10.25% | 100% |
| dip40_V1_gescreend_pass | 560 | 14% | 1.8% | +44.6% | -15.5% | -6.80% | 100% |
| dip40_V1_gescreend_fail | 4582 | 26% | 3.9% | +46.8% | -25.9% | -6.61% | 100% |
| dip40_V1_alle | 5797 | 26% | 3.9% | +46.7% | -25.3% | -6.81% | 100% |
| dip40_V2_gescreend_pass | 558 | 18% | 2.2% | +43.0% | -19.5% | -8.52% | 100% |
| dip40_V2_gescreend_fail | 4613 | 25% | 4.3% | +54.6% | -28.0% | -7.07% | 100% |
| dip40_V2_alle | 5739 | 24% | 4.5% | +52.8% | -27.7% | -8.09% | 100% |
| dip40_V3_gescreend_pass | 563 | 8% | 2.5% | +250.6% | -21.0% | +1.22% | 100% |
| dip40_V3_gescreend_fail | 4719 | 13% | 5.8% | +110.1% | -29.5% | -10.96% | 100% |
| dip40_V3_alle | 5799 | 13% | 5.9% | +110.8% | -29.1% | -11.19% | 100% |
| dip45_V1_gescreend_pass | 538 | 15% | 1.7% | +47.3% | -15.3% | -6.08% | 100% |
| dip45_V1_gescreend_fail | 4498 | 27% | 3.6% | +48.2% | -25.7% | -5.48% | 100% |
| dip45_V1_alle | 5606 | 26% | 3.6% | +48.5% | -25.0% | -5.87% | 100% |
| dip45_V2_gescreend_pass | 535 | 18% | 2.1% | +42.0% | -19.5% | -8.20% | 100% |
| dip45_V2_gescreend_fail | 4522 | 25% | 4.0% | +58.1% | -27.7% | -5.95% | 100% |
| dip45_V2_alle | 5550 | 24% | 4.1% | +56.5% | -27.3% | -6.97% | 100% |
| dip45_V3_gescreend_pass | 541 | 8% | 2.0% | +284.3% | -20.3% | +4.48% | 100% |
| dip45_V3_gescreend_fail | 4612 | 14% | 5.5% | +117.5% | -29.1% | -8.65% | 100% |
| dip45_V3_alle | 5601 | 13% | 5.5% | +120.7% | -28.6% | -8.94% | 100% |

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
| per_token_met_xlink | 464 | 16% | 5.0% | -9.09% | -11.8% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 139 | 22% | 0.0% | +17.08% | -11.9% tot +46.1% | -13.1% | 130% | 58% |
| gepoold_met_xlink | 3900 | 13% | 2.8% | -9.69% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1164 | 18% | 0.0% | +16.67% | -0.1% tot +33.5% | -14.5% | 72% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 23:56:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:56:26,365 main INFO screen Trust pass=1 dev=0.0 ins=0.74 pro=36 1a=False 1b=False 2=False (66.6s)
Sep 12 23:56:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:56:35,859 main INFO screen DOO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.5s)
Sep 12 23:56:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:56:37,712 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:56:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 12 23:57:11 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:57:11,256 main INFO screen binderz pass=0 dev=0.0 ins=48.54 pro=25 1a=False 1b=False 2=True (66.9s)
Sep 12 23:57:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:57:15,045 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (48.7s)
Sep 12 23:57:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:57:27,927 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (52.1s)
Sep 12 23:58:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:58:21,907 main INFO screen Patron pass=1 dev=1.98 ins=0.0 pro=16 1a=False 1b=False 2=False (70.6s)
Sep 12 23:58:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:58:22,382 main INFO screen helpme pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (67.3s)
Sep 12 23:58:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:58:28,490 main INFO screen FATPIG pass=1 dev=0.0 ins=3.46 pro=31 1a=False 1b=False 2=False (60.6s)
Sep 12 23:59:27 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:59:27,879 main INFO screen EMPTY pass=0 dev=0.0 ins=36.0 pro=47 1a=False 1b=False 2=True (65.5s)
Sep 12 23:59:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:59:31,202 main INFO screen FLY pass=1 dev=0.31 ins=0.0 pro=38 1a=False 1b=False 2=False (62.7s)
Sep 12 23:59:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:59:31,561 main INFO screen milo pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.7s)
Sep 13 00:00:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:00:36,783 main INFO screen winston pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (65.6s)
Sep 13 00:00:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:00:39,578 main INFO screen yellow pass=1 dev=0.0 ins=0.74 pro=44 1a=False 1b=False 2=False (71.7s)
Sep 13 00:00:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:00:42,380 main INFO screen pegcoin pass=1 dev=0.0 ins=0.0 pro=24 1a=False 1b=False 2=False (70.8s)
Sep 13 00:01:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:01:41,510 main INFO screen Memestonk pass=0 dev=0.0 ins=0.0 pro=70 1a=False 1b=False 2=True (64.7s)
Sep 13 00:01:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:01:42,756 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:01:42 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:01:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:01:48,184 main INFO screen cat pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (68.6s)
Sep 13 00:01:52 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:01:52,349 main INFO screen wank pass=0 dev=0.17 ins=48.45 pro=50 1a=False 1b=False 2=True (70.0s)
Sep 13 00:02:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:02:34,136 main INFO screen Addidas pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (52.6s)
Sep 13 00:02:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:02:43,567 main INFO screen TripleC pass=0 dev=0.0 ins=78.96 pro=1 1a=True 1b=True 2=True (55.4s)
Sep 13 00:02:45 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:02:45,792 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (53.4s)
Sep 13 00:03:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:03:33,421 main INFO screen cat pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (59.3s)
Sep 13 00:03:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:03:53,638 main INFO screen WOWNEROCHAN pass=0 dev=0.0 ins=16.6 pro=65 1a=False 1b=False 2=True (70.1s)
Sep 13 00:03:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:03:56,811 main INFO screen fat pig pass=0 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=True (71.0s)
Sep 13 00:04:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:04:42,455 main INFO screen jewdog pass=1 dev=0.0 ins=0.0 pro=56 1a=False 1b=False 2=False (69.0s)
Sep 13 00:05:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:05:04,429 main INFO screen BATONANON pass=0 dev=0.0 ins=36.69 pro=18 1a=False 1b=False 2=True (70.8s)
Sep 13 00:05:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:05:07,756 main INFO screen CABAL4 pass=1 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (70.9s)
Sep 13 00:05:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:05:33,896 main INFO screen HOLDWHEEL pass=0 dev=0.0 ins=9.27 pro=30 1a=False 1b=False 2=True (51.4s)
Sep 13 00:05:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:05:57,484 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.1s)
Sep 13 00:06:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:06:13,263 main INFO screen SLINGOOR pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (65.5s)
Sep 13 00:06:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:06:40,225 main INFO screen BATONANON pass=0 dev=0.0 ins=36.65 pro=26 1a=True 1b=True 2=True (66.3s)
Sep 13 00:06:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:06:53,115 main INFO screen TrumpStunk pass=0 dev=0.47 ins=78.96 pro=6 1a=False 1b=True 2=True (55.6s)
Sep 13 00:07:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:07:20,860 main INFO screen INSTANT pass=1 dev=0.49 ins=10.55 pro=53 1a=False 1b=False 2=False (67.6s)
Sep 13 00:07:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:07:35,428 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:07:35 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:07:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:07:53,677 main INFO screen simba pass=1 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (73.5s)
Sep 13 00:08:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:08:29,963 main INFO screen cat pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.0s)
Sep 13 00:08:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:08:34,118 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.7s)
Sep 13 00:08:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:08:48,544 main INFO screen baby  pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (54.9s)
Sep 13 00:09:21 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:09:21,903 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (51.9s)
Sep 13 00:09:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:09:44,157 main INFO screen DERP pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (70.0s)
Sep 13 00:09:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:09:51,534 main INFO screen PMARCA pass=0 dev=79.31 ins=0.0 pro=2 1a=False 1b=False 2=True (63.0s)
Sep 13 00:10:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:10:25,446 main INFO screen S&P pass=0 dev=0.0 ins=17.03 pro=44 1a=False 1b=True 2=True (63.5s)
Sep 13 00:10:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:10:36,339 main INFO screen MINEC$AT pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (52.2s)
Sep 13 00:10:50 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:10:50,911 main INFO screen milo pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (59.4s)
Sep 13 00:11:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:11:23,040 main INFO screen Stonkoor pass=0 dev=0.0 ins=17.07 pro=44 1a=False 1b=False 2=True (57.6s)
Sep 13 00:11:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:11:42,103 main INFO screen Slopcannon pass=0 dev=0.0 ins=7.97 pro=63 1a=False 1b=False 2=True (65.8s)
Sep 13 00:11:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:11:53,635 main INFO screen SATOSHI  pass=0 dev=0.72 ins=0.0 pro=3 1a=False 1b=False 2=False (62.7s)
Sep 13 00:12:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:12:30,799 main INFO screen MPAIR pass=1 dev=0.0 ins=11.96 pro=73 1a=False 1b=False 2=False (67.8s)
Sep 13 00:12:35 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:12:35,934 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:00:12:35 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
Sep 13 00:12:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:12:36,930 main INFO screen PMARCA pass=0 dev=89.83 ins=0.0 pro=1 1a=False 1b=False 2=True (54.8s)
Sep 13 00:13:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:13:07,250 main INFO screen JEWCHAN pass=0 dev=0.0 ins=5.67 pro=58 1a=False 1b=False 2=True (73.6s)
Sep 13 00:13:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 00:13:32,616 main INFO screen solamduck pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (61.8s)
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T22:54:36Z
--- update 2026-09-12T22:59:54Z
--- update 2026-09-12T23:05:16Z
--- update 2026-09-12T23:10:22Z
--- update 2026-09-12T23:15:30Z
--- update 2026-09-12T23:20:36Z
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
