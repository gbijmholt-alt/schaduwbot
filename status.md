# Schaduwbot status

- tijd: 2026-09-12 09:10:28 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 19 hours, 23 minutes
- bot-service: active
- code-versie: 6d8fae6
- schijf: 3.5G/38G | geheugen: 591/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 4716, "tokens_in_memory": 1086, "msgs": 222772, "trades": 82529, "creates": 1087, "decode_fail": 3153, "rpc_calls": 2608, "rpc_errors": 134, "sol_usd": 101.86968122510584, "open_positions": 43, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 8436 | 1351 | 6 | 1351 | 93 | 2391 | 7209 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 503 | 16% | 2.0% | +44.1% | -16.6% | -6.93% | 100% |
| dip35_V1_gescreend_fail | 4124 | 27% | 3.8% | +45.5% | -25.8% | -6.62% | 100% |
| dip35_V1_alle | 5058 | 26% | 3.9% | +44.8% | -25.2% | -6.88% | 100% |
| dip35_V2_gescreend_pass | 500 | 21% | 2.8% | +43.1% | -20.9% | -7.42% | 100% |
| dip35_V2_gescreend_fail | 4159 | 25% | 4.3% | +56.0% | -27.9% | -6.92% | 100% |
| dip35_V2_alle | 5021 | 24% | 4.5% | +53.6% | -27.6% | -7.71% | 100% |
| dip35_V3_gescreend_pass | 502 | 8% | 3.2% | +297.3% | -22.3% | +4.45% | 100% |
| dip35_V3_gescreend_fail | 4247 | 13% | 5.8% | +114.4% | -29.5% | -10.28% | 100% |
| dip35_V3_alle | 5072 | 13% | 5.9% | +119.1% | -29.1% | -9.75% | 100% |
| dip40_V1_gescreend_pass | 473 | 14% | 2.1% | +46.7% | -15.9% | -7.07% | 100% |
| dip40_V1_gescreend_fail | 4051 | 26% | 3.7% | +47.1% | -25.6% | -6.54% | 100% |
| dip40_V1_alle | 4858 | 25% | 3.7% | +47.3% | -25.0% | -6.72% | 100% |
| dip40_V2_gescreend_pass | 471 | 17% | 2.5% | +46.2% | -19.8% | -8.44% | 100% |
| dip40_V2_gescreend_fail | 4063 | 25% | 4.1% | +55.5% | -27.8% | -7.01% | 100% |
| dip40_V2_alle | 4815 | 24% | 4.3% | +54.0% | -27.4% | -7.85% | 100% |
| dip40_V3_gescreend_pass | 474 | 8% | 2.7% | +294.2% | -21.1% | +2.87% | 100% |
| dip40_V3_gescreend_fail | 4144 | 13% | 5.6% | +111.2% | -29.3% | -10.80% | 100% |
| dip40_V3_alle | 4868 | 13% | 5.6% | +116.8% | -28.8% | -10.28% | 100% |
| dip45_V1_gescreend_pass | 455 | 15% | 2.0% | +48.7% | -15.8% | -6.28% | 100% |
| dip45_V1_gescreend_fail | 3969 | 27% | 3.3% | +48.3% | -25.4% | -5.22% | 100% |
| dip45_V1_alle | 4704 | 26% | 3.3% | +48.7% | -24.7% | -5.55% | 100% |
| dip45_V2_gescreend_pass | 452 | 19% | 2.4% | +43.3% | -19.8% | -7.90% | 100% |
| dip45_V2_gescreend_fail | 3976 | 25% | 3.8% | +58.3% | -27.4% | -5.75% | 100% |
| dip45_V2_alle | 4663 | 24% | 3.9% | +57.1% | -27.0% | -6.50% | 100% |
| dip45_V3_gescreend_pass | 455 | 7% | 2.4% | +352.6% | -20.5% | +6.56% | 100% |
| dip45_V3_gescreend_fail | 4042 | 14% | 5.3% | +116.3% | -28.9% | -8.70% | 100% |
| dip45_V3_alle | 4706 | 13% | 5.3% | +124.9% | -28.3% | -8.05% | 100% |

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
Sep 12 08:41:21 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:41:21,650 main INFO screen ELOGE pass=0 dev=0.0 ins=6.71 pro=67 1a=False 1b=False 2=True (3.7s)
Sep 12 08:41:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:41:25,009 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:41:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:41:39,057 main INFO screen GROK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (19.7s)
Sep 12 08:43:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:43:03,694 main INFO screen LaMisery pass=0 dev=0.52 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 12 08:43:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:43:25,242 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:43:30 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:43:30,311 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:43:44 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:43:44,843 main INFO screen Pokémon pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 08:44:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:44:37,091 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:44:37 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 08:46:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:46:22,336 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:46:27 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:46:27,407 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:46:36 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:46:36,932 main INFO screen BITBANK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 12 08:46:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:46:43,155 main INFO screen MC pass=0 dev=0.0 ins=23.52 pro=52 1a=False 1b=False 2=True (20.9s)
Sep 12 08:47:19 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:47:19,349 main INFO screen $GOML pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 12 08:47:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:47:23,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:47:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:47:29,708 main INFO screen MEOW  pass=0 dev=0.0 ins=19.7 pro=26 1a=False 1b=False 2=True (6.3s)
Sep 12 08:48:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:48:15,442 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:48:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:48:20,542 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:48:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:48:23,293 main INFO screen CHBU pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=True (3.7s)
Sep 12 08:48:35 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:48:34,999 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.7s)
Sep 12 08:49:37 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:49:37,184 main INFO screen CHAROC pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 12 08:49:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:49:43,750 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:49:43 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 08:50:01 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:50:01,922 main INFO screen PIKACOQ pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 12 08:51:20 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:51:20,304 main INFO screen uptard pass=0 dev=1.0 ins=21.59 pro=54 1a=False 1b=False 2=True (2.3s)
Sep 12 08:51:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:51:39,947 main INFO screen NinjaCat pass=0 dev=0.0 ins=21.75 pro=59 1a=False 1b=False 2=True (2.3s)
Sep 12 08:52:50 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:52:50,371 main INFO screen FLYCOIN pass=0 dev=0.04 ins=79.27 pro=9 1a=False 1b=True 2=True (3.2s)
Sep 12 08:52:50 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:52:50,762 main INFO screen TROLL pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 12 08:52:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:52:51,065 main INFO screen USMS pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (4.0s)
Sep 12 08:53:08 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:53:08,640 main INFO screen kittylick pass=0 dev=0.87 ins=0.0 pro=1 1a=False 1b=False 2=False (3.7s)
Sep 12 08:53:23 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:53:23,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:53:30 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:53:30,800 main INFO screen liq  pass=0 dev=0.12 ins=0.0 pro=1 1a=False 1b=False 2=False (7.6s)
Sep 12 08:54:03 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:54:03,370 main INFO screen MANMEME pass=0 dev=35.83 ins=0.0 pro=6 1a=False 1b=False 2=True (2.2s)
Sep 12 08:54:04 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:54:04,272 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:54:09 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:54:09,346 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:54:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:54:22,621 main INFO screen FlyGuy pass=0 dev=0.26 ins=79.05 pro=9 1a=False 1b=True 2=True (18.4s)
Sep 12 08:54:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:54:48,618 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:54:48 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 08:56:05 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:56:05,733 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:56:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:56:10,806 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:56:22 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:56:22,514 main INFO screen vrl pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.9s)
Sep 12 08:56:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:56:26,754 main INFO screen DAVIDE pass=0 dev=3.5 ins=16.37 pro=33 1a=False 1b=False 2=True (21.1s)
Sep 12 08:56:41 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:56:41,543 main INFO screen $GOAT pass=0 dev=1.07 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 12 08:57:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:57:34,392 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:57:39 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:57:39,461 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:57:54 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:57:54,762 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.5s)
Sep 12 08:58:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:58:43,325 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 08:58:49 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:58:49,801 main INFO screen DERP pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 12 08:59:48 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 08:59:48,850 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:08:59:48 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 09:01:05 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:05,431 main INFO screen CHAROC pass=0 dev=2.16 ins=0.0 pro=4 1a=False 1b=False 2=False (7.9s)
Sep 12 09:01:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:10,148 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:01:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:11,855 main INFO screen HALH pass=0 dev=0.19 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 12 09:01:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:15,215 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:01:31 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:31,809 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:01:36 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:36,022 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:01:36 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:36,096 main INFO screen RUN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (26.0s)
Sep 12 09:01:41 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:41,095 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:01:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:01:43,871 main INFO screen HALH pass=0 dev=1.0 ins=0.0 pro=2 1a=False 1b=False 2=False (12.1s)
Sep 12 09:02:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:02:02,163 main INFO screen PONSBRAIN pass=0 dev=0.07 ins=79.24 pro=7 1a=False 1b=True 2=True (26.2s)
Sep 12 09:02:31 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:02:31,232 main INFO screen HODL pass=0 dev=32.2 ins=0.9 pro=14 1a=False 1b=False 2=True (9.1s)
Sep 12 09:03:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:10,061 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:03:15 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:15,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:03:29 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:29,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:03:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:34,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:03:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:34,643 main INFO screen SHROOMS pass=0 dev=0.7 ins=54.55 pro=8 1a=True 1b=False 2=True (24.7s)
Sep 12 09:03:54 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:03:54,401 main INFO screen MAGIC pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (25.7s)
Sep 12 09:04:06 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:04:06,671 main INFO screen SAVPIR pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 12 09:04:49 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:04:49,091 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:04:49 +0000] "GET /health HTTP/1.1" 200 497 "-" "Python-urllib/3.14"
Sep 12 09:06:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:06:11,964 main INFO screen stonk pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.1s)
Sep 12 09:06:14 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:06:14,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:06:26 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:06:26,045 main INFO screen DOGE pass=0 dev=0.0 ins=13.82 pro=27 1a=False 1b=False 2=True (11.7s)
Sep 12 09:06:58 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:06:58,873 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:07:02 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:02,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:07:07 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:07,204 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:07:10 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:10,336 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (11.6s)
Sep 12 09:07:21 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:21,984 main INFO screen STAMPIES pass=0 dev=7.66 ins=0.0 pro=2 1a=False 1b=False 2=False (19.9s)
Sep 12 09:07:38 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:38,002 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:07:43 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:07:43,083 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:08:04 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:08:04,288 main INFO screen Ed pass=0 dev=0.0 ins=11.19 pro=51 1a=False 1b=False 2=True (26.4s)
Sep 12 09:09:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:09:11,844 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:09:16 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:09:16,912 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 09:09:34 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:09:34,316 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (22.6s)
Sep 12 09:10:28 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 09:10:28,133 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:09:10:28 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T08:34:23Z
--- update 2026-09-12T08:39:30Z
--- update 2026-09-12T08:44:36Z
--- update 2026-09-12T08:49:42Z
--- update 2026-09-12T08:54:47Z
--- update 2026-09-12T08:59:47Z
--- update 2026-09-12T09:04:48Z
--- update 2026-09-12T09:10:27Z
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
