# Schaduwbot status

- tijd: 2026-09-12 12:47:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 23 hours, 0 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.6G/38G | geheugen: 616/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 10486, "tokens_in_memory": 2318, "msgs": 832569, "trades": 228224, "creates": 2318, "decode_fail": 9623, "rpc_calls": 6886, "rpc_errors": 324, "sol_usd": 102.22148217796085, "open_positions": 40, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 10828 | 1662 | 8 | 1662 | 115 | 2907 | 8717 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 520 | 16% | 1.9% | +43.9% | -16.5% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 4248 | 27% | 3.8% | +45.8% | -25.8% | -6.54% | 100% |
| dip35_V1_alle | 5232 | 26% | 4.0% | +45.1% | -25.2% | -6.77% | 100% |
| dip35_V2_gescreend_pass | 516 | 22% | 2.7% | +42.6% | -20.9% | -6.75% | 100% |
| dip35_V2_gescreend_fail | 4289 | 25% | 4.3% | +56.0% | -27.9% | -6.81% | 100% |
| dip35_V2_alle | 5191 | 25% | 4.6% | +53.4% | -27.7% | -7.62% | 100% |
| dip35_V3_gescreend_pass | 517 | 9% | 3.1% | +273.0% | -22.2% | +4.59% | 100% |
| dip35_V3_gescreend_fail | 4385 | 14% | 6.0% | +115.0% | -29.6% | -10.03% | 100% |
| dip35_V3_alle | 5245 | 13% | 6.1% | +119.0% | -29.2% | -9.61% | 100% |
| dip40_V1_gescreend_pass | 488 | 14% | 2.0% | +46.1% | -15.8% | -6.83% | 100% |
| dip40_V1_gescreend_fail | 4181 | 26% | 3.7% | +47.3% | -25.7% | -6.42% | 100% |
| dip40_V1_alle | 5029 | 25% | 3.9% | +47.4% | -25.0% | -6.64% | 100% |
| dip40_V2_gescreend_pass | 486 | 18% | 2.5% | +45.4% | -19.9% | -8.18% | 100% |
| dip40_V2_gescreend_fail | 4198 | 25% | 4.2% | +55.5% | -27.9% | -6.91% | 100% |
| dip40_V2_alle | 4984 | 24% | 4.4% | +53.8% | -27.5% | -7.81% | 100% |
| dip40_V3_gescreend_pass | 488 | 8% | 2.7% | +275.2% | -21.1% | +3.17% | 100% |
| dip40_V3_gescreend_fail | 4282 | 13% | 5.8% | +109.1% | -29.4% | -11.07% | 100% |
| dip40_V3_alle | 5037 | 13% | 5.8% | +114.5% | -29.0% | -10.55% | 100% |
| dip45_V1_gescreend_pass | 469 | 15% | 1.9% | +47.8% | -15.7% | -6.20% | 100% |
| dip45_V1_gescreend_fail | 4096 | 27% | 3.3% | +48.5% | -25.4% | -5.17% | 100% |
| dip45_V1_alle | 4866 | 26% | 3.4% | +48.8% | -24.7% | -5.54% | 100% |
| dip45_V2_gescreend_pass | 465 | 19% | 2.4% | +43.0% | -19.8% | -7.78% | 100% |
| dip45_V2_gescreend_fail | 4104 | 25% | 3.8% | +58.2% | -27.5% | -5.72% | 100% |
| dip45_V2_alle | 4822 | 24% | 4.0% | +56.9% | -27.1% | -6.52% | 100% |
| dip45_V3_gescreend_pass | 469 | 8% | 2.3% | +317.5% | -20.5% | +6.85% | 100% |
| dip45_V3_gescreend_fail | 4173 | 14% | 5.4% | +113.9% | -28.9% | -8.90% | 100% |
| dip45_V3_alle | 4867 | 13% | 5.3% | +122.0% | -28.4% | -8.25% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 99.9%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 406 | 15% | 5.4% | -9.25% | -12.3% tot -6.2% | -14.6% | – | 100% |
| per_token_zonder_xlink | 117 | 20% | 0.0% | +20.37% | -14.0% tot +54.7% | -13.2% | 130% | 54% |
| gepoold_met_xlink | 3404 | 13% | 3.1% | -9.91% | -11.2% tot -8.6% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1014 | 19% | 0.0% | +19.84% | +0.6% tot +39.1% | -14.3% | 69% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 12:29:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:29:59,836 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:01,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:04,906 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:06,265 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:08,645 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:13,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:26,730 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.6s)
Sep 12 12:30:26 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:26,882 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (27.1s)
Sep 12 12:30:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:28,700 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:30:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:31,581 main INFO screen PepeGPT pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (23.0s)
Sep 12 12:30:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:30:41,822 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (13.2s)
Sep 12 12:31:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:31:17,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:31:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:31:19,027 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:31:19 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 12:31:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:31:22,764 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:31:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:31:43,051 main INFO screen 4D pass=0 dev=9.0 ins=29.92 pro=8 1a=False 1b=True 2=True (25.5s)
Sep 12 12:31:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:31:49,842 main INFO screen CATBRAIN pass=1 dev=0.0 ins=11.06 pro=23 1a=False 1b=False 2=False (5.1s)
Sep 12 12:32:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:32:36,231 main INFO screen Cinema pass=0 dev=0.0 ins=21.08 pro=30 1a=False 1b=False 2=True (7.6s)
Sep 12 12:32:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:32:36,697 main INFO screen FoMo pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (9.5s)
Sep 12 12:33:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:33:12,359 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:33:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:33:17,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:33:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:33:31,709 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.5s)
Sep 12 12:33:50 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:33:50,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:33:55 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:33:55,498 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:34:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:34:09,850 main INFO screen PAD pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.5s)
Sep 12 12:34:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:34:32,956 main INFO screen Dad pass=1 dev=0.01 ins=0.0 pro=38 1a=False 1b=False 2=False (2.0s)
Sep 12 12:34:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:34:42,650 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:34:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:34:47,724 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:34:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:34:56,233 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:35:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:35:01,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:35:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:35:02,558 main INFO screen VAGINA pass=0 dev=0.0 ins=17.86 pro=28 1a=False 1b=False 2=True (19.9s)
Sep 12 12:35:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:35:09,032 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:35:16 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:35:16,978 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.8s)
Sep 12 12:35:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:35:17,633 main INFO screen sol shark  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 12 12:36:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:23,999 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:36:23 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 12:36:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:38,599 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:36:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:40,581 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=6 1a=False 1b=False 2=False (3.4s)
Sep 12 12:36:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:43,666 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:36:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:48,997 main INFO screen RIPTRUMP pass=1 dev=0.96 ins=5.26 pro=44 1a=False 1b=False 2=False (3.2s)
Sep 12 12:36:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:53,697 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:36:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:58,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:36:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:36:58,751 main INFO screen MrBeast pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.8s)
Sep 12 12:37:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:02,107 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:37:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:07,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:37:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:13,248 main INFO screen bundloor pass=0 dev=0.0 ins=16.24 pro=31 1a=False 1b=False 2=True (19.6s)
Sep 12 12:37:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:23,066 main INFO screen VOID pass=0 dev=39.08 ins=0.0 pro=3 1a=False 1b=False 2=True (21.0s)
Sep 12 12:37:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:25,923 main INFO screen king pass=0 dev=1.01 ins=0.0 pro=3 1a=False 1b=False 2=False (3.6s)
Sep 12 12:37:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:36,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:37:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:41,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:37:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:54,530 main INFO screen ONLYDEVS pass=0 dev=10.0 ins=33.83 pro=12 1a=False 1b=True 2=True (18.3s)
Sep 12 12:37:57 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:37:57,992 main INFO screen CHBU pass=0 dev=1.72 ins=0.0 pro=1 1a=False 1b=False 2=True (2.6s)
Sep 12 12:38:51 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:38:51,997 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 12 12:39:48 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:39:48,119 main INFO screen . pass=0 dev=0.46 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 12 12:40:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:40:58,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:41:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:03,665 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:41:17 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:17,308 main INFO screen CBRAIN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (18.8s)
Sep 12 12:41:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:37,103 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:41:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
Sep 12 12:41:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:41:49,483 main INFO screen SOL pass=0 dev=0.14 ins=0.0 pro=4 1a=False 1b=False 2=False (3.0s)
Sep 12 12:42:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:46,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:42:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:49,318 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:42:52 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:52,995 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.5s)
Sep 12 12:42:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:42:54,348 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:07,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:07,674 main INFO screen SHIBAGO pass=0 dev=0.35 ins=78.96 pro=6 1a=False 1b=True 2=True (18.4s)
Sep 12 12:43:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:12,532 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:43:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:25,795 main INFO screen bulesh pass=0 dev=0.07 ins=79.24 pro=8 1a=False 1b=True 2=True (19.1s)
Sep 12 12:43:29 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:43:29,585 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 12:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:01,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:01,334 main INFO screen MONOPOLY pass=0 dev=0.0 ins=10.94 pro=34 1a=False 1b=False 2=True (3.7s)
Sep 12 12:44:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:06,344 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:19,775 main INFO screen FERSPE pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (18.6s)
Sep 12 12:44:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:40,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:44:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:44:45,612 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:45:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:45:13,148 main INFO screen LARPTOP pass=0 dev=0.0 ins=71.67 pro=67 1a=False 1b=False 2=True (32.7s)
Sep 12 12:45:19 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:45:19,431 aiohttp.access INFO 94.154.43.223 [12/Sep/2026:12:45:19 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 12 12:46:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:30,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:46:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:39,115 main INFO screen DEGENFLY pass=1 dev=0.0 ins=7.86 pro=57 1a=False 1b=False 2=False (9.2s)
Sep 12 12:46:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:46:56,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:47:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:01,182 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:47:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:05,154 main INFO screen TAL pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (3.8s)
Sep 12 12:47:06 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:47:06,661 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:47:06 +0000] "GET /health HTTP/1.1" 200 501 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T11:16:36Z
--- update 2026-09-12T11:21:57Z
--- update 2026-09-12T11:27:19Z
--- update 2026-09-12T11:32:19Z
--- update 2026-09-12T11:37:36Z
--- update 2026-09-12T11:43:20Z
--- update 2026-09-12T11:48:20Z
--- update 2026-09-12T11:53:36Z
--- update 2026-09-12T11:59:05Z
Running as unit: schaduwbot-wallets.service; invocation ID: 67d32d30228c414781697fb76280fa59
analyses gestart (cb883cffd7a1)
--- update 2026-09-12T12:04:33Z
--- update 2026-09-12T12:09:34Z
--- update 2026-09-12T12:14:36Z
--- update 2026-09-12T12:20:11Z
--- update 2026-09-12T12:25:36Z
--- update 2026-09-12T12:31:17Z
--- update 2026-09-12T12:36:23Z
--- update 2026-09-12T12:41:36Z
--- update 2026-09-12T12:47:05Z
```

## Analyses (laatste 25 regels)
```
inactive
12:08:37 klaar (851 rpc-calls, 13 fouten)
12:08:39 klaar in 2s: 16626 tokens, 144 nieuw -> /opt/schaduwbot/reports/video_replay.md
12:08:39 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 12:08 UTC
12:08:40 54535 tokens geladen
12:08:42   2000 tokens, 250045 trades, 51008 posities (2s)
12:08:44   4000 tokens, 496319 trades, 99458 posities (5s)
12:08:47   6000 tokens, 732039 trades, 144482 posities (7s)
12:08:49   8000 tokens, 966346 trades, 188464 posities (9s)
12:08:51   10000 tokens, 1209956 trades, 232898 posities (12s)
12:08:54   12000 tokens, 1492659 trades, 295155 posities (14s)
12:08:56   14000 tokens, 1728094 trades, 337299 posities (17s)
12:08:59   16000 tokens, 1980589 trades, 384171 posities (19s)
12:09:02   18000 tokens, 2223133 trades, 430721 posities (22s)
12:09:04   20000 tokens, 2484878 trades, 484120 posities (25s)
12:09:07   22000 tokens, 2725661 trades, 529712 posities (27s)
12:09:09   24000 tokens, 2971988 trades, 575609 posities (29s)
12:09:11   26000 tokens, 3193304 trades, 615760 posities (31s)
12:09:13   28000 tokens, 3442466 trades, 664641 posities (33s)
12:09:16   30000 tokens, 3709953 trades, 717663 posities (36s)
12:09:18 posities: 773628 uit 3942433 trades (39s)
12:09:29 164863 wallets gerekend
12:09:29 geluk-toets
12:10:06 persistentie
12:10:08 kopieer-simulatie
12:10:21 klaar in 102s -> /opt/schaduwbot/reports/wallets.md
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
