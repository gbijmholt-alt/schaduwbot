# Schaduwbot status

- tijd: 2026-09-12 23:46:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 9 hours, 59 minutes
- bot-service: active
- code-versie: b458321
- schijf: 4.0G/38G | geheugen: 1043/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 11569, "tokens_in_memory": 4521, "msgs": 1256186, "trades": 407839, "creates": 4521, "decode_fail": 34901, "rpc_calls": 10197, "rpc_errors": 1, "sol_usd": 101.78112469895733, "open_positions": 55, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 23:19:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:19:12,029 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.4s)
Sep 12 23:20:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:02,003 main INFO screen SINGLE pass=0 dev=0.0 ins=21.8 pro=57 1a=False 1b=False 2=True (64.2s)
Sep 12 23:20:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:07,574 main INFO screen NOVA pass=0 dev=0.22 ins=0.0 pro=4 1a=False 1b=False 2=False (72.5s)
Sep 12 23:20:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:15,896 aiohttp.access INFO 89.42.231.200 [12/Sep/2026:23:20:15 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 23:20:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:28,879 main INFO screen vrl pass=0 dev=18.08 ins=0.0 pro=1 1a=False 1b=False 2=False (76.9s)
Sep 12 23:20:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:20:37,099 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:20:37 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:21:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:06,301 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (64.3s)
Sep 12 23:21:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:10,110 main INFO screen MIND pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.5s)
Sep 12 23:21:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:21:26,322 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.03 pro=23 1a=False 1b=False 2=True (57.4s)
Sep 12 23:22:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:10,948 main INFO screen 400 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 12 23:22:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:15,033 main INFO screen Cagefight pass=1 dev=3.76 ins=0.0 pro=65 1a=False 1b=False 2=False (68.7s)
Sep 12 23:22:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:22:32,534 main INFO screen DUVAL pass=0 dev=0.0 ins=21.49 pro=52 1a=False 1b=False 2=True (66.2s)
Sep 12 23:23:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:22,112 main INFO screen duluth pass=0 dev=0.0 ins=0.03 pro=3 1a=False 1b=False 2=False (67.1s)
Sep 12 23:23:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:23,462 main INFO screen $speed pass=1 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (72.5s)
Sep 12 23:23:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:23:28,620 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.03 pro=20 1a=False 1b=False 2=True (56.1s)
Sep 12 23:24:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:36,696 main INFO screen $speed pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (74.6s)
Sep 12 23:24:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:37,025 main INFO screen MEMPOOLS pass=0 dev=0.0 ins=48.5 pro=22 1a=False 1b=False 2=True (73.6s)
Sep 12 23:24:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:24:40,061 main INFO screen catsey pass=1 dev=1.25 ins=5.37 pro=45 1a=False 1b=False 2=False (71.4s)
Sep 12 23:25:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:41,205 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:25:41 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:25:54 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:54,645 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (77.9s)
Sep 12 23:25:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:55,827 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (75.8s)
Sep 12 23:25:56 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:25:56,565 main INFO screen LaMisery pass=0 dev=1.56 ins=0.0 pro=1 1a=False 1b=False 2=False (79.5s)
Sep 12 23:27:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:09,769 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (73.2s)
Sep 12 23:27:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:12,271 main INFO screen SOR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (76.4s)
Sep 12 23:27:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:27:12,906 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.62 pro=31 1a=False 1b=False 2=True (78.3s)
Sep 12 23:28:43 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:43,957 main INFO screen PRIMETIME pass=0 dev=0.0 ins=19.97 pro=36 1a=False 1b=False 2=True (91.1s)
Sep 12 23:28:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:46,013 main INFO screen pray pass=0 dev=8.79 ins=0.0 pro=52 1a=False 1b=False 2=False (93.7s)
Sep 12 23:28:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:28:48,533 main INFO screen SOLCHAN pass=0 dev=0.0 ins=9.55 pro=62 1a=False 1b=False 2=True (98.8s)
Sep 12 23:30:04 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:04,191 main INFO screen Desk pass=1 dev=0.0 ins=12.37 pro=21 1a=False 1b=False 2=False (78.2s)
Sep 12 23:30:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:09,197 main INFO screen $GOAT pass=1 dev=0.35 ins=0.0 pro=10 1a=False 1b=False 2=False (85.2s)
Sep 12 23:30:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:30:10,901 main INFO screen Duluth pass=1 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (82.4s)
Sep 12 23:31:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:31:07,702 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:31:07 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:31:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:31:12,145 main INFO screen SOR GUMMY pass=0 dev=0.9 ins=0.0 pro=9 1a=False 1b=False 2=False (68.0s)
Sep 12 23:31:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:31:19,981 main INFO screen ONE pass=0 dev=0.0 ins=20.3 pro=76 1a=False 1b=False 2=True (70.8s)
Sep 12 23:31:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:31:29,025 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.72 pro=7 1a=False 1b=False 2=True (78.1s)
Sep 12 23:32:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:32:25,733 main INFO screen 💎BALLS pass=0 dev=19.03 ins=0.0 pro=12 1a=False 1b=False 2=False (73.6s)
Sep 12 23:32:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:32:29,300 main INFO screen ANONRUNNER pass=0 dev=0.0 ins=36.47 pro=29 1a=True 1b=False 2=True (69.3s)
Sep 12 23:32:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:32:40,388 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (71.4s)
Sep 12 23:33:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:33:28,373 main INFO screen HORACE pass=0 dev=0.0 ins=22.71 pro=22 1a=False 1b=False 2=True (48.0s)
Sep 12 23:33:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:33:30,221 main INFO screen Duluth pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.9s)
Sep 12 23:33:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:33:30,731 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (65.0s)
Sep 12 23:35:13 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:35:13,769 main INFO screen triple t pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (103.5s)
Sep 12 23:35:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:35:15,284 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (106.9s)
Sep 12 23:35:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:35:16,715 main INFO screen Duluth pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (106.0s)
Sep 12 23:36:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:36:10,211 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:36:10 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:36:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:36:19,013 main INFO screen HOOD pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (62.3s)
Sep 12 23:36:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:36:20,133 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (64.8s)
Sep 12 23:36:20 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:36:20,480 main INFO screen BetOnBlak pass=1 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (66.7s)
Sep 12 23:37:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:37:14,335 main INFO screen batonmusk pass=0 dev=0.0 ins=78.6 pro=4 1a=False 1b=True 2=True (55.3s)
Sep 12 23:37:30 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:37:30,310 main INFO screen ETHERPUMP pass=1 dev=3.58 ins=6.71 pro=58 1a=False 1b=False 2=False (69.8s)
Sep 12 23:37:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:37:34,122 main INFO screen DELULU pass=0 dev=0.0 ins=18.97 pro=72 1a=False 1b=False 2=True (74.0s)
Sep 12 23:38:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:38:16,109 main INFO screen SIA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.8s)
Sep 12 23:38:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:38:25,815 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (55.5s)
Sep 12 23:38:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:38:34,887 main INFO screen 🌟  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.8s)
Sep 12 23:39:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:39:14,664 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (58.6s)
Sep 12 23:39:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:39:28,695 main INFO screen DOOROC pass=0 dev=0.03 ins=0.0 pro=3 1a=False 1b=False 2=False (62.9s)
Sep 12 23:39:51 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:39:51,475 main INFO screen TRANSCEND pass=0 dev=0.0 ins=48.55 pro=31 1a=False 1b=False 2=True (76.6s)
Sep 12 23:40:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:40:32,080 main INFO screen openai pass=1 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (77.4s)
Sep 12 23:40:41 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:40:41,936 main INFO screen CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.2s)
Sep 12 23:40:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:40:53,752 main INFO screen 🌟  pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (62.3s)
Sep 12 23:41:31 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:41:31,203 main INFO screen triple t pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (59.1s)
Sep 12 23:41:32 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:41:32,435 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:41:32 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
Sep 12 23:41:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:41:42,632 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.7s)
Sep 12 23:42:02 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:42:02,996 main INFO screen Quest pass=0 dev=0.0 ins=12.64 pro=70 1a=False 1b=False 2=True (69.2s)
Sep 12 23:42:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:42:25,574 main INFO screen WHALEGPT pass=0 dev=0.43 ins=78.96 pro=7 1a=False 1b=True 2=True (54.4s)
Sep 12 23:42:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:42:37,064 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.4s)
Sep 12 23:42:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:42:55,783 main INFO screen CAT pass=0 dev=0.9 ins=0.0 pro=3 1a=False 1b=False 2=False (52.8s)
Sep 12 23:43:19 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:43:19,481 main INFO screen duluth pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (53.9s)
Sep 12 23:43:29 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:43:29,483 main INFO screen triple t pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (52.4s)
Sep 12 23:43:47 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:43:47,733 main INFO screen triple t pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.9s)
Sep 12 23:44:22 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:44:22,395 main INFO screen Illiquid pass=0 dev=0.0 ins=48.6 pro=23 1a=False 1b=False 2=True (62.9s)
Sep 12 23:44:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:44:34,654 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (65.2s)
Sep 12 23:44:53 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:44:53,727 main INFO screen FLYPAD pass=1 dev=0.26 ins=2.56 pro=61 1a=False 1b=False 2=False (66.0s)
Sep 12 23:45:18 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:45:18,862 main INFO screen triple t pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 12 23:45:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:45:26,566 main INFO screen FL pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.9s)
Sep 12 23:45:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:45:40,714 main INFO screen WOFI pass=0 dev=0.27 ins=0.0 pro=1 1a=False 1b=False 2=True (47.0s)
Sep 12 23:46:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:46:06,483 main INFO screen BONK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (47.6s)
Sep 12 23:46:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:46:15,946 main INFO screen CATFLIGHT pass=0 dev=0.0 ins=78.26 pro=0 1a=False 1b=True 2=True (49.4s)
Sep 12 23:46:28 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:46:28,378 main INFO screen OpenClaw pass=0 dev=0.39 ins=0.0 pro=1 1a=False 1b=False 2=True (47.7s)
Sep 12 23:46:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-12 23:46:37,124 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:23:46:37 +0000] "GET /health HTTP/1.1" 200 502 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T22:18:15Z
--- update 2026-09-12T22:23:36Z
--- update 2026-09-12T22:29:00Z
--- update 2026-09-12T22:34:03Z
--- update 2026-09-12T22:39:27Z
--- update 2026-09-12T22:44:28Z
--- update 2026-09-12T22:49:32Z
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
