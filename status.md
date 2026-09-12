# Schaduwbot status

- tijd: 2026-09-12 08:29:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 18 hours, 42 minutes
- bot-service: active
- code-versie: 6d8fae6
- schijf: 3.5G/38G | geheugen: 569/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 2247, "tokens_in_memory": 525, "msgs": 119562, "trades": 40215, "creates": 525, "decode_fail": 1434, "rpc_calls": 1355, "rpc_errors": 75, "sol_usd": 101.6718414936276, "open_positions": 5, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 7618 | 1241 | 6 | 1241 | 93 | 2228 | 6754 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 503 | 16% | 2.0% | +44.1% | -16.6% | -6.93% | 100% |
| dip35_V1_gescreend_fail | 4076 | 27% | 3.8% | +45.6% | -25.9% | -6.60% | 100% |
| dip35_V1_alle | 5003 | 26% | 3.9% | +44.8% | -25.2% | -6.86% | 100% |
| dip35_V2_gescreend_pass | 500 | 21% | 2.8% | +43.1% | -20.9% | -7.42% | 100% |
| dip35_V2_gescreend_fail | 4112 | 25% | 4.3% | +56.2% | -27.9% | -6.90% | 100% |
| dip35_V2_alle | 4969 | 24% | 4.5% | +53.7% | -27.6% | -7.66% | 100% |
| dip35_V3_gescreend_pass | 502 | 8% | 3.2% | +297.3% | -22.3% | +4.45% | 100% |
| dip35_V3_gescreend_fail | 4196 | 13% | 5.9% | +115.1% | -29.6% | -10.11% | 100% |
| dip35_V3_alle | 5016 | 13% | 5.9% | +119.7% | -29.2% | -9.57% | 100% |
| dip40_V1_gescreend_pass | 473 | 14% | 2.1% | +46.7% | -15.9% | -7.07% | 100% |
| dip40_V1_gescreend_fail | 4007 | 26% | 3.7% | +47.2% | -25.7% | -6.48% | 100% |
| dip40_V1_alle | 4808 | 25% | 3.8% | +47.3% | -25.0% | -6.68% | 100% |
| dip40_V2_gescreend_pass | 471 | 17% | 2.5% | +46.2% | -19.8% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 4022 | 25% | 4.2% | +55.8% | -27.8% | -6.95% | 100% |
| dip40_V2_alle | 4769 | 24% | 4.3% | +54.2% | -27.4% | -7.78% | 100% |
| dip40_V3_gescreend_pass | 474 | 8% | 2.7% | +294.2% | -21.1% | +2.87% | 100% |
| dip40_V3_gescreend_fail | 4098 | 13% | 5.6% | +112.1% | -29.4% | -10.69% | 100% |
| dip40_V3_alle | 4817 | 13% | 5.6% | +117.7% | -28.9% | -10.15% | 100% |
| dip45_V1_gescreend_pass | 455 | 15% | 2.0% | +48.7% | -15.8% | -6.28% | 100% |
| dip45_V1_gescreend_fail | 3926 | 28% | 3.3% | +48.4% | -25.4% | -5.15% | 100% |
| dip45_V1_alle | 4655 | 26% | 3.4% | +48.7% | -24.7% | -5.49% | 100% |
| dip45_V2_gescreend_pass | 452 | 19% | 2.4% | +43.3% | -19.8% | -7.90% | 100% |
| dip45_V2_gescreend_fail | 3935 | 25% | 3.8% | +58.5% | -27.4% | -5.69% | 100% |
| dip45_V2_alle | 4617 | 24% | 3.9% | +57.3% | -27.0% | -6.43% | 100% |
| dip45_V3_gescreend_pass | 455 | 7% | 2.4% | +352.6% | -20.5% | +6.56% | 100% |
| dip45_V3_gescreend_fail | 3997 | 14% | 5.4% | +117.1% | -28.9% | -8.58% | 100% |
| dip45_V3_alle | 4656 | 13% | 5.3% | +125.7% | -28.4% | -7.92% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 394 | 15% | 5.6% | -9.69% | -12.8% tot -6.6% | -14.6% | – | 100% |
| per_token_zonder_xlink | 112 | 19% | 0.0% | +20.98% | -14.9% tot +56.8% | -13.3% | 131% | 54% |
| gepoold_met_xlink | 3307 | 13% | 3.2% | -10.31% | -11.7% tot -9.0% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 978 | 18% | 0.0% | +20.19% | +0.2% tot +40.1% | -14.6% | 70% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 08:11:47 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:11:47,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:11:53 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:11:53,881 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:11:54 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:11:54,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:11:59 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:11:59,955 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:12:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:02,628 main INFO screen ELON pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (14.8s)
Sep 12 08:12:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:02,696 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:12:05 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:05,487 main INFO screen TRADER pass=0 dev=0.0 ins=21.16 pro=22 1a=False 1b=False 2=True (12.2s)
Sep 12 08:12:14 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:14,379 main INFO screen AF pass=0 dev=0.18 ins=79.13 pro=9 1a=True 1b=True 2=True (11.8s)
Sep 12 08:12:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:18,295 main INFO screen Lambo pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.3s)
Sep 12 08:12:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:25,028 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:12:40 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:40,144 main INFO screen CASH pass=0 dev=26.03 ins=0.86 pro=42 1a=False 1b=False 2=False (15.2s)
Sep 12 08:12:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:58,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:12:59 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:12:59,870 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:12:59 +0000] "GET /health HTTP/1.1" 200 493 "-" "Python-urllib/3.14"
Sep 12 08:13:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:13:09,793 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (11.3s)
Sep 12 08:13:38 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:13:38,541 main INFO screen Pleb pass=0 dev=0.0 ins=16.41 pro=40 1a=False 1b=False 2=True (10.9s)
Sep 12 08:13:56 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:13:56,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:14:07 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:14:07,266 main INFO screen TRADER pass=0 dev=0.0 ins=15.1 pro=25 1a=False 1b=True 2=True (10.9s)
Sep 12 08:14:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:14:51,150 main INFO screen ~ʚ4° pass=0 dev=0.0 ins=20.21 pro=43 1a=False 1b=True 2=True (5.9s)
Sep 12 08:15:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:15:09,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:15:21 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:15:21,424 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:15:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:15:23,565 main INFO screen GOODBOY pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (14.5s)
Sep 12 08:15:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:15:26,498 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:15:47 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:15:47,492 main INFO screen NICE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.1s)
Sep 12 08:16:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:16:09,396 main INFO screen COIN pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 08:16:45 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:16:45,268 main INFO screen CHAROC pass=0 dev=0.5 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 12 08:17:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:17:02,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:17:17 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:17:17,738 main INFO screen DELULU pass=0 dev=0.0 ins=17.3 pro=26 1a=False 1b=False 2=True (15.4s)
Sep 12 08:17:46 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:17:46,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:17:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:17:51,265 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:18:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:02,880 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.2s)
Sep 12 08:18:14 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:14,522 main INFO screen GOAF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.4s)
Sep 12 08:18:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:18,042 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:18:18 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
Sep 12 08:18:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:35,232 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:18:40 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:40,299 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:18:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:43,839 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:18:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:48,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:18:59 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:18:59,506 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:19:01 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:01,310 main INFO screen foge pass=0 dev=0.0 ins=10.65 pro=48 1a=False 1b=False 2=True (26.2s)
Sep 12 08:19:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:10,681 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.9s)
Sep 12 08:19:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:11,775 main INFO screen foge pass=0 dev=20.34 ins=2.33 pro=41 1a=False 1b=False 2=False (12.3s)
Sep 12 08:19:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:34,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:19:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:39,706 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:19:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:58,535 main INFO screen Dojo pass=0 dev=0.0 ins=20.81 pro=37 1a=False 1b=False 2=False (3.1s)
Sep 12 08:19:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:19:58,538 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:20:01 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:20:01,797 main INFO screen WWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.3s)
Sep 12 08:20:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:20:03,606 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:20:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:20:20,365 main INFO screen MOOGPT pass=0 dev=0.18 ins=77.54 pro=9 1a=False 1b=True 2=True (21.9s)
Sep 12 08:20:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:20:39,622 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:20:44 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:20:44,691 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:21:06 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:06,538 main INFO screen SUPERSTONK pass=0 dev=0.0 ins=17.24 pro=31 1a=False 1b=False 2=True (27.0s)
Sep 12 08:21:21 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:21,622 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:21:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:26,690 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:21:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:37,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:21:49 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:49,072 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (27.6s)
Sep 12 08:21:50 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:50,170 main INFO screen SOLLOVE pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (12.8s)
Sep 12 08:21:55 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:55,172 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:21:55 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:21:55,929 main INFO screen MALLORCA  pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (5.3s)
Sep 12 08:22:00 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:22:00,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:22:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:22:20,435 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.3s)
Sep 12 08:22:33 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:22:33,056 main INFO screen $speed pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (6.3s)
Sep 12 08:22:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:22:58,207 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.2s)
Sep 12 08:23:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:23:37,182 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:23:37 +0000] "GET /health HTTP/1.1" 200 495 "-" "Python-urllib/3.14"
Sep 12 08:24:46 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:24:46,015 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:24:55 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:24:55,965 main INFO screen BTCPRIUS pass=0 dev=0.0 ins=19.96 pro=32 1a=False 1b=False 2=True (10.0s)
Sep 12 08:25:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:20,319 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:25:24 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:24,550 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:25:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:25,393 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:25:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:29,624 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:25:33 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:33,257 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:25:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:43,165 main INFO screen ZNIULAI pass=0 dev=0.14 ins=79.17 pro=8 1a=False 1b=True 2=True (23.0s)
Sep 12 08:25:45 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:45,945 main INFO screen whale pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (12.8s)
Sep 12 08:25:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:25:48,590 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.1s)
Sep 12 08:26:13 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:26:13,495 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:26:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:26:25,390 main INFO screen NIGGA pass=0 dev=2.55 ins=14.37 pro=29 1a=False 1b=False 2=True (12.0s)
Sep 12 08:27:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:27:26,820 main INFO screen TROLL pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.0s)
Sep 12 08:27:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:27:35,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:27:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:27:48,704 main INFO screen ZenoCoin pass=0 dev=0.0 ins=18.61 pro=40 1a=False 1b=False 2=True (13.0s)
Sep 12 08:28:27 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:28:27,915 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:28:42 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:28:42,284 main INFO screen ZenoCoin pass=0 dev=26.91 ins=0.0 pro=32 1a=False 1b=False 2=False (14.5s)
Sep 12 08:29:18 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:29:18,610 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:29:18 +0000] "GET /health HTTP/1.1" 200 494 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T07:41:14Z
nieuwe code: 5e1921e
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 4ef46f4f0356436685dca4ab3e2f1d40
analyses gestart (e6fa7044d08b)
--- update 2026-09-12T07:46:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 2a89401955f64382a4bf605244d564d2
analyses gestart (571ea883d7b8)
--- update 2026-09-12T07:51:47Z
nieuwe code: 6d8fae6
botcode gewijzigd: herstart
install klaar
--- update 2026-09-12T07:56:52Z
--- update 2026-09-12T08:02:05Z
--- update 2026-09-12T08:07:36Z
--- update 2026-09-12T08:12:58Z
--- update 2026-09-12T08:18:16Z
--- update 2026-09-12T08:23:36Z
--- update 2026-09-12T08:29:17Z
```

## Analyses (laatste 25 regels)
```
inactive
07:52:00 probe: 120 transacties ophalen
07:53:00 klaar (551 rpc-calls, 0 fouten)
07:53:02 klaar in 2s: 16508 tokens, 34 nieuw -> /opt/schaduwbot/reports/video_replay.md
07:53:03 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 07:53 UTC
07:53:03 51130 tokens geladen
07:53:06   2000 tokens, 247228 trades, 51459 posities (3s)
07:53:08   4000 tokens, 500285 trades, 104134 posities (6s)
07:53:11   6000 tokens, 746680 trades, 151104 posities (8s)
07:53:13   8000 tokens, 997175 trades, 201671 posities (11s)
07:53:16   10000 tokens, 1260038 trades, 252158 posities (13s)
07:53:19   12000 tokens, 1529500 trades, 309045 posities (16s)
07:53:22   14000 tokens, 1773567 trades, 350771 posities (19s)
07:53:25   16000 tokens, 2034820 trades, 404904 posities (22s)
07:53:28   18000 tokens, 2304063 trades, 461465 posities (25s)
07:53:30   20000 tokens, 2547338 trades, 506874 posities (27s)
07:53:33   22000 tokens, 2801778 trades, 554566 posities (30s)
07:53:35   24000 tokens, 3028677 trades, 599750 posities (32s)
07:53:37   26000 tokens, 3291798 trades, 649697 posities (35s)
07:53:41   28000 tokens, 3560897 trades, 714082 posities (38s)
07:53:41 posities: 733209 uit 3641470 trades (39s)
07:53:52 159725 wallets gerekend
07:53:52 geluk-toets
07:54:30 persistentie
07:54:32 kopieer-simulatie
07:54:44 klaar in 102s -> /opt/schaduwbot/reports/wallets.md
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
