# Schaduwbot status

- tijd: 2026-09-12 17:15:48 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 3 hours, 28 minutes
- bot-service: active
- code-versie: e364fd9
- schijf: 3.8G/38G | geheugen: 1156/3814 MB

## Health
```json
(niet bereikbaar: <urlopen error [Errno 111] Connection refused>)
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 16945 | 2396 | 14 | 2395 | 178 | 4220 | 12642 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 574 | 17% | 1.7% | +43.6% | -16.1% | -6.22% | 100% |
| dip35_V1_gescreend_fail | 4584 | 27% | 3.9% | +45.4% | -26.1% | -6.60% | 100% |
| dip35_V1_alle | 5690 | 26% | 4.1% | +44.7% | -25.4% | -6.85% | 100% |
| dip35_V2_gescreend_pass | 570 | 22% | 2.5% | +40.8% | -20.4% | -6.62% | 100% |
| dip35_V2_gescreend_fail | 4633 | 25% | 4.4% | +55.0% | -28.1% | -6.97% | 100% |
| dip35_V2_alle | 5648 | 25% | 4.6% | +52.3% | -27.8% | -7.83% | 100% |
| dip35_V3_gescreend_pass | 571 | 9% | 2.8% | +266.5% | -22.0% | +4.28% | 100% |
| dip35_V3_gescreend_fail | 4734 | 14% | 6.1% | +110.9% | -29.8% | -10.71% | 100% |
| dip35_V3_alle | 5701 | 13% | 6.1% | +114.9% | -29.4% | -10.27% | 100% |
| dip40_V1_gescreend_pass | 542 | 14% | 1.8% | +46.0% | -15.6% | -6.93% | 100% |
| dip40_V1_gescreend_fail | 4504 | 27% | 3.9% | +46.9% | -25.9% | -6.55% | 100% |
| dip40_V1_alle | 5464 | 26% | 4.0% | +46.8% | -25.2% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 539 | 17% | 2.2% | +43.6% | -19.5% | -8.49% | 100% |
| dip40_V2_gescreend_fail | 4529 | 25% | 4.3% | +54.8% | -28.1% | -7.02% | 100% |
| dip40_V2_alle | 5419 | 24% | 4.5% | +52.8% | -27.6% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 541 | 8% | 2.4% | +265.1% | -20.9% | +1.84% | 100% |
| dip40_V3_gescreend_fail | 4614 | 13% | 5.9% | +105.9% | -29.6% | -11.74% | 100% |
| dip40_V3_alle | 5469 | 13% | 5.9% | +110.5% | -29.1% | -11.31% | 100% |
| dip45_V1_gescreend_pass | 520 | 15% | 1.7% | +47.5% | -15.4% | -6.19% | 100% |
| dip45_V1_gescreend_fail | 4415 | 28% | 3.6% | +48.3% | -25.7% | -5.37% | 100% |
| dip45_V1_alle | 5285 | 26% | 3.6% | +48.3% | -25.0% | -5.80% | 100% |
| dip45_V2_gescreend_pass | 516 | 18% | 2.1% | +42.7% | -19.5% | -8.04% | 100% |
| dip45_V2_gescreend_fail | 4428 | 25% | 4.1% | +57.5% | -27.7% | -6.11% | 100% |
| dip45_V2_alle | 5240 | 24% | 4.1% | +55.9% | -27.3% | -6.99% | 100% |
| dip45_V3_gescreend_pass | 519 | 8% | 2.1% | +303.1% | -20.3% | +5.22% | 100% |
| dip45_V3_gescreend_fail | 4498 | 14% | 5.5% | +111.2% | -29.2% | -9.84% | 100% |
| dip45_V3_alle | 5282 | 13% | 5.5% | +118.1% | -28.6% | -9.26% | 100% |

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
| per_token_met_xlink | 448 | 15% | 4.9% | -9.04% | -11.8% tot -6.2% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3773 | 13% | 2.8% | -9.69% | -10.9% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 17:08:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:23,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:24,667 main INFO screen HODL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.5s)
Sep 12 17:08:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:29,387 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:34,492 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:08:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:37,644 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.9s)
Sep 12 17:08:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:39,893 main INFO screen rewardog pass=0 dev=0.0 ins=53.23 pro=45 1a=False 1b=False 2=True (26.3s)
Sep 12 17:08:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:50,545 main INFO screen DOGE  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (6.4s)
Sep 12 17:08:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:52,103 main INFO screen GEMI pass=0 dev=0.35 ins=78.96 pro=1 1a=False 1b=True 2=True (22.8s)
Sep 12 17:08:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:08:55,524 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:00,604 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:05,295 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:10,364 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:09:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:22,841 main INFO screen TOMB pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (9.4s)
Sep 12 17:09:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:23,125 main INFO screen RTW pass=0 dev=3.43 ins=0.0 pro=2 1a=False 1b=False 2=False (27.6s)
Sep 12 17:09:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:09:23,992 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.8s)
Sep 12 17:10:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:06,412 main INFO screen OpenAI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.6s)
Sep 12 17:10:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:35,061 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:10:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:38,911 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:17:10:38 +0000] "GET /health HTTP/1.1" 200 504 "-" "Python-urllib/3.14"
Sep 12 17:10:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:40,147 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:10:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:49,225 main INFO screen KC pass=0 dev=0.08 ins=0.0 pro=4 1a=False 1b=False 2=False (8.2s)
Sep 12 17:10:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:56,272 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (21.3s)
Sep 12 17:10:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:56,901 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:10:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:10:59,949 main INFO screen STC pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (4.7s)
Sep 12 17:11:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:01,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:17,873 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (21.1s)
Sep 12 17:11:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:18,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:23,510 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:32,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:34 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:34,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:37,402 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.0s)
Sep 12 17:11:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:37,470 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:37,913 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:39,823 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:42,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:11:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:11:54,935 main INFO screen CASHBACK pass=0 dev=0.0 ins=26.58 pro=4 1a=False 1b=False 2=True (22.1s)
Sep 12 17:12:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:03,612 main INFO screen MHWA pass=0 dev=0.0 ins=1.93 pro=34 1a=False 1b=False 2=True (28.9s)
Sep 12 17:12:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:07,534 main INFO screen MHWA pass=0 dev=0.0 ins=37.47 pro=23 1a=False 1b=False 2=True (30.1s)
Sep 12 17:12:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:12,247 main INFO screen MHWA pass=0 dev=0.0 ins=26.69 pro=19 1a=False 1b=False 2=True (17.3s)
Sep 12 17:12:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:16,473 main INFO screen godcha pass=0 dev=6.35 ins=28.12 pro=19 1a=False 1b=False 2=False (12.9s)
Sep 12 17:12:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:22,505 main INFO screen MHWA pass=0 dev=0.0 ins=36.86 pro=11 1a=False 1b=False 2=True (15.0s)
Sep 12 17:12:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:22,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:12:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:29,695 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (17.4s)
Sep 12 17:12:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:30,816 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (8.3s)
Sep 12 17:12:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:32,088 main INFO screen BOOBA pass=0 dev=0.0 ins=17.35 pro=37 1a=False 1b=False 2=True (15.6s)
Sep 12 17:12:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:55,881 main INFO screen CAJUN pass=0 dev=0.5 ins=0.0 pro=3 1a=False 1b=False 2=False (10.5s)
Sep 12 17:12:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:59,173 main INFO screen PINKE pass=0 dev=6.64 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 12 17:12:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:12:59,653 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:04,726 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:17,785 main INFO screen VRINU pass=0 dev=34.89 ins=0.16 pro=9 1a=False 1b=False 2=False (6.8s)
Sep 12 17:13:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:18,521 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.9s)
Sep 12 17:13:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:28,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:29,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:33,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:40,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:42,903 main INFO screen $WHOOPS pass=0 dev=0.06 ins=0.0 pro=1 1a=False 1b=False 2=False (13.4s)
Sep 12 17:13:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:45,183 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:48,521 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:53,555 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:13:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:13:55,642 main INFO screen MINI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.2s)
Sep 12 17:14:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:01,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:06,517 main INFO screen lovenowar pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (26.4s)
Sep 12 17:14:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:06,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:07,818 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.4s)
Sep 12 17:14:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:20,579 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.5s)
Sep 12 17:14:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:30,391 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:35,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:40,643 main INFO screen BALL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 17:14:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:43,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:48,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:14:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:53,010 main INFO screen Apple pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.7s)
Sep 12 17:14:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:14:55,131 main INFO screen BPCATE pass=0 dev=0.47 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 12 17:15:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:15:09,772 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (26.5s)
Sep 12 17:15:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:15:12,987 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:15:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:15:18,071 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 17:15:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 17:15:37,529 main INFO screen COMMUNISM pass=0 dev=0.0 ins=21.0 pro=44 1a=False 1b=False 2=True (24.6s)
Sep 12 17:15:48 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 17:15:48 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 17:15:48 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 17:15:48 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 39min 26.321s CPU time over 7h 23min 27.989s wall clock time, 678.8M memory peak.
Sep 12 17:15:48 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T16:23:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 734fe7fd71e047c5827569b33cc14ab3
analyses gestart (02faa7a55c91)
--- update 2026-09-12T16:28:48Z
--- update 2026-09-12T16:34:00Z
--- update 2026-09-12T16:39:17Z
--- update 2026-09-12T16:44:36Z
--- update 2026-09-12T16:50:10Z
--- update 2026-09-12T16:55:17Z
--- update 2026-09-12T17:00:34Z
--- update 2026-09-12T17:05:36Z
nieuwe code: 8d4b88e
alleen analyses/documentatie gewijzigd: geen herstart
Running as unit: schaduwbot-wallets.service; invocation ID: 4382a0e1c14a4f7986ac753e7d367fa4
analyses gestart (4ee13da033ab)
--- update 2026-09-12T17:10:37Z
--- update 2026-09-12T17:15:43Z
nieuwe code: e364fd9
botcode gewijzigd: herstart
install klaar
```

## Analyses (laatste 25 regels)
```
active
17:14:35 klaar in 2s: 20774 tokens, 876 nieuw -> /opt/schaduwbot/reports/video_replay.md
17:14:35 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 17:14 UTC
17:14:35 61285 tokens geladen
17:14:38   2000 tokens, 237689 trades, 43891 posities (2s)
17:14:40   4000 tokens, 474403 trades, 87041 posities (4s)
17:14:42   6000 tokens, 691913 trades, 128039 posities (6s)
17:14:44   8000 tokens, 916484 trades, 166582 posities (9s)
17:14:46   10000 tokens, 1143626 trades, 209905 posities (11s)
17:14:48   12000 tokens, 1370692 trades, 245797 posities (13s)
17:14:50   14000 tokens, 1639320 trades, 300827 posities (15s)
17:14:53   16000 tokens, 1871697 trades, 343694 posities (17s)
17:14:55   18000 tokens, 2084337 trades, 377696 posities (19s)
17:14:57   20000 tokens, 2345121 trades, 425249 posities (22s)
17:14:59   22000 tokens, 2568183 trades, 464829 posities (24s)
17:15:01   24000 tokens, 2818670 trades, 514732 posities (26s)
17:15:04   26000 tokens, 3048800 trades, 556135 posities (28s)
17:15:06   28000 tokens, 3278743 trades, 595657 posities (31s)
17:15:08   30000 tokens, 3524870 trades, 641622 posities (33s)
17:15:10   32000 tokens, 3728331 trades, 676970 posities (35s)
17:15:13   34000 tokens, 3964569 trades, 721009 posities (37s)
17:15:15   36000 tokens, 4211806 trades, 769532 posities (40s)
17:15:17   38000 tokens, 4438241 trades, 820930 posities (42s)
17:15:18 posities: 835223 uit 4494178 trades (43s)
17:15:29 174024 wallets gerekend
17:15:29 geluk-toets
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
