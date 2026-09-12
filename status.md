# Schaduwbot status

- tijd: 2026-09-12 12:25:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 22 hours, 38 minutes
- bot-service: active
- code-versie: 49e15c7
- schijf: 3.6G/38G | geheugen: 610/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 9196, "tokens_in_memory": 2012, "msgs": 706238, "trades": 197241, "creates": 2012, "decode_fail": 7479, "rpc_calls": 6019, "rpc_errors": 272, "sol_usd": 102.2176087288364, "open_positions": 53, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 12:10:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:10:22,313 main INFO screen FoMo pass=1 dev=3.62 ins=2.61 pro=36 1a=False 1b=False 2=False (6.9s)
Sep 12 12:10:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:10:32,763 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:10:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:10:35,023 main INFO screen $CAJUN pass=0 dev=1.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 12 12:10:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:10:45,143 main INFO screen FoMo pass=1 dev=0.0 ins=7.1 pro=46 1a=False 1b=False 2=False (8.4s)
Sep 12 12:10:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:10:46,755 main INFO screen $TUCCI pass=0 dev=0.33 ins=0.0 pro=1 1a=False 1b=False 2=True (14.0s)
Sep 12 12:11:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:11:05,981 main INFO screen SXSN pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 12 12:11:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:11:14,522 main INFO screen CumCoin pass=1 dev=0.0 ins=13.3 pro=25 1a=False 1b=False 2=False (3.3s)
Sep 12 12:11:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:11:20,132 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:11:33 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:11:33,777 main INFO screen stocklana pass=0 dev=0.36 ins=0.0 pro=4 1a=False 1b=False 2=False (13.7s)
Sep 12 12:11:58 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:11:58,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:12:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:12:03,547 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:12:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:12:25,152 main INFO screen fagcat pass=0 dev=0.0 ins=43.95 pro=17 1a=False 1b=False 2=True (26.8s)
Sep 12 12:12:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:12:37,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:12:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:12:42,179 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:12:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:12:46,278 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (9.2s)
Sep 12 12:13:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:02,704 main INFO screen GTA6 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.6s)
Sep 12 12:13:31 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:31,768 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:13:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:36,837 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:13:41 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:41,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:13:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:46,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:13:59 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:13:59,538 main INFO screen fagcat pass=0 dev=0.77 ins=44.03 pro=14 1a=False 1b=False 2=True (27.8s)
Sep 12 12:14:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:03,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:14:08 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:08,058 main INFO screen Hoodtard pass=0 dev=0.0 ins=20.48 pro=51 1a=False 1b=False 2=True (26.3s)
Sep 12 12:14:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:14,180 main INFO screen Awnım pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (10.9s)
Sep 12 12:14:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:37,092 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:14:37 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 12:14:39 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:39,023 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:14:44 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:14:44,092 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:15:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:15:05,901 main INFO screen BPCATE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (26.9s)
Sep 12 12:15:10 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:15:10,631 main INFO screen LVL pass=0 dev=3.42 ins=0.0 pro=3 1a=False 1b=False 2=False (6.7s)
Sep 12 12:15:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:15:22,720 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:15:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:15:27,820 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:15:53 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:15:53,470 main INFO screen Macrofly pass=1 dev=0.0 ins=14.21 pro=39 1a=False 1b=False 2=False (30.8s)
Sep 12 12:16:36 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:16:36,579 main INFO screen aircoin pass=1 dev=0.0 ins=0.46 pro=30 1a=False 1b=False 2=False (3.2s)
Sep 12 12:16:40 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:16:40,500 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:16:45 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:16:45,564 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:16:49 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:16:49,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:16:54 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:16:54,904 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:17:04 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:17:04,187 main INFO screen $1 pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.7s)
Sep 12 12:17:14 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:17:14,643 main INFO screen NEKO pass=0 dev=6.63 ins=72.68 pro=1 1a=False 1b=True 2=True (24.9s)
Sep 12 12:17:15 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:17:15,388 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:17:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:17:20,456 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:17:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:17:42,529 main INFO screen FOMO APP pass=0 dev=67.51 ins=0.05 pro=11 1a=False 1b=False 2=False (27.2s)
Sep 12 12:18:09 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:18:09,716 main INFO screen PPF pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 12 12:18:11 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:18:11,786 main INFO screen DERP pass=0 dev=0.53 ins=0.0 pro=2 1a=False 1b=False 2=False (6.2s)
Sep 12 12:18:24 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:18:24,782 aiohttp.access INFO 195.182.16.23 [12/Sep/2026:12:18:24 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 12:18:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:18:38,520 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:18:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:18:43,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:19:02 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:19:02,657 main INFO screen BRAINFROG pass=0 dev=0.35 ins=78.96 pro=7 1a=False 1b=True 2=True (24.2s)
Sep 12 12:19:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:19:22,318 main INFO screen ROGUE pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.5s)
Sep 12 12:20:12 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:20:12,908 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:20:12 +0000] "GET /health HTTP/1.1" 200 500 "-" "Python-urllib/3.14"
Sep 12 12:20:18 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:20:18,028 main INFO screen . pass=0 dev=0.52 ins=0.0 pro=3 1a=False 1b=False 2=False (6.5s)
Sep 12 12:20:22 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:20:22,632 main INFO screen USMS pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 12 12:22:23 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:23,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:22:28 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:28,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:22:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:30,382 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:22:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:35,409 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:22:46 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:46,614 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (23.6s)
Sep 12 12:22:56 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:22:56,186 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.9s)
Sep 12 12:23:00 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:23:00,990 aiohttp.access INFO 45.135.193.198 [12/Sep/2026:12:23:00 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 12:23:01 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:23:01,011 aiohttp.access INFO 45.135.193.198 [12/Sep/2026:12:23:01 +0000] "GET / HTTP/1.0" 404 174 "-" "0day"
Sep 12 12:23:38 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:23:38,714 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:23:42 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:23:42,851 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.3s)
Sep 12 12:23:43 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:23:43,782 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:24:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:03,316 main INFO screen . pass=0 dev=0.52 ins=0.0 pro=3 1a=False 1b=False 2=False (8.8s)
Sep 12 12:24:05 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:05,163 main INFO screen Vmaxsolana pass=0 dev=0.0 ins=77.99 pro=6 1a=False 1b=True 2=True (26.5s)
Sep 12 12:24:21 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:21,431 main INFO screen rnr pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 12:24:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:25,485 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:24:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:30,544 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 12 12:24:30 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:30,555 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:24:47 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:24:47,171 main INFO screen CATON pass=0 dev=0.07 ins=79.24 pro=9 1a=False 1b=True 2=True (21.8s)
Sep 12 12:25:03 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:03,090 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:07 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:07,266 main INFO screen INVICTUS pass=0 dev=8.0 ins=24.39 pro=21 1a=False 1b=True 2=True (7.9s)
Sep 12 12:25:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:13,579 main INFO screen RICK pass=0 dev=3.24 ins=0.0 pro=1 1a=False 1b=False 2=False (6.2s)
Sep 12 12:25:13 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:13,787 main INFO screen $GOAT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (10.8s)
Sep 12 12:25:20 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:20,879 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:25 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:25,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:27 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:27,494 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:32 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:32,563 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:35 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:35,384 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 12:25:37 ubuntu-4gb-fsn1-1 python[67492]: 2026-09-12 12:25:37,112 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:12:25:37 +0000] "GET /health HTTP/1.1" 200 499 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T10:55:36Z
--- update 2026-09-12T11:01:03Z
--- update 2026-09-12T11:06:18Z
--- update 2026-09-12T11:11:18Z
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
