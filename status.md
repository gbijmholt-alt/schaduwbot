# Schaduwbot status

- tijd: 2026-09-12 07:56:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 18 hours, 9 minutes
- bot-service: active
- code-versie: 6d8fae6
- schijf: 3.5G/38G | geheugen: 549/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 302, "tokens_in_memory": 59, "msgs": 14247, "trades": 3700, "creates": 59, "decode_fail": 181, "rpc_calls": 85, "rpc_errors": 8, "sol_usd": 101.62920277116288, "open_positions": 1, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 12 07:35:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:35:59,638 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:05,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:10,486 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:13,717 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:36:13 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:36:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:14,421 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.9s)
Sep 12 07:36:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:23,677 main INFO screen FLYPAIN pass=0 dev=0.04 ins=79.27 pro=6 1a=False 1b=True 2=True (18.3s)
Sep 12 07:36:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:49,194 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:36:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:36:54,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:37:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:07,826 main INFO screen RUFUS pass=0 dev=0.0 ins=21.88 pro=30 1a=False 1b=True 2=True (18.7s)
Sep 12 07:37:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:37:10,248 main INFO screen $speed pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 12 07:39:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:05,811 main INFO screen HORACE pass=0 dev=0.0 ins=18.12 pro=24 1a=False 1b=False 2=True (2.1s)
Sep 12 07:39:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:39:10,050 main INFO screen Fox pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 12 07:40:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:40:02,878 main INFO screen GYROS pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.7s)
Sep 12 07:41:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:14,093 main INFO screen WOTF pass=0 dev=98.49 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 12 07:41:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:41:15,023 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (5.7s)
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 1h 22min 30.038s CPU time over 12h 1min 10.049s wall clock time, 1.1G memory peak.
Sep 12 07:41:18 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,143 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 07:41:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:41:19,167 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:41:19 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 12 07:42:54 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:42:54,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:42:59 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:42:59,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:43:14 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:43:14,171 main INFO screen UP pass=0 dev=0.0 ins=35.87 pro=40 1a=True 1b=False 2=True (20.1s)
Sep 12 07:44:23 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:44:23,814 main INFO screen DOOYET pass=0 dev=1.72 ins=0.0 pro=1 1a=False 1b=False 2=True (1.4s)
Sep 12 07:44:51 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:44:51,213 main INFO screen moneyCAT pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.8s)
Sep 12 07:45:15 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:15,182 main INFO screen XeXe pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (5.4s)
Sep 12 07:45:15 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:15,379 main INFO screen chickjock pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.6s)
Sep 12 07:45:56 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:45:56,541 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:00 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:00,403 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:01 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:01,610 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:05 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:05,472 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:06 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:06,756 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:11 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:11,827 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:46:16 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:16,687 main INFO screen MEGACAT pass=0 dev=0.0 ins=15.14 pro=65 1a=False 1b=False 2=True (20.2s)
Sep 12 07:46:19 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:19,941 main INFO screen HolyGuac pass=0 dev=0.89 ins=0.0 pro=5 1a=False 1b=False 2=False (19.6s)
Sep 12 07:46:25 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:25,973 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.3s)
Sep 12 07:46:37 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:46:37,155 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:46:37 +0000] "GET /health HTTP/1.1" 200 487 "-" "Python-urllib/3.14"
Sep 12 07:48:11 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:11,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:48:16 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:16,629 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:48:25 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:25,854 main INFO screen trollcat pass=0 dev=0.0 ins=21.78 pro=29 1a=False 1b=False 2=True (1.9s)
Sep 12 07:48:29 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:29,827 main INFO screen 公牛 pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (18.4s)
Sep 12 07:48:38 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:38,171 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:07:48:38 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 07:48:38 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:38,532 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:07:48:38 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 07:48:40 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:40,932 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:48:42 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:42,623 main INFO screen iCoin pass=0 dev=28.21 ins=0.0 pro=25 1a=False 1b=False 2=False (3.4s)
Sep 12 07:48:46 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:46,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:48:59 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:48:59,886 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.5s)
Sep 12 07:49:45 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:49:45,883 main INFO screen . pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (4.3s)
Sep 12 07:49:55 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:49:55,193 main INFO screen vrl pass=0 dev=0.69 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 12 07:50:07 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:50:07,647 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:50:12 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:50:12,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:50:27 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:50:27,241 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (19.7s)
Sep 12 07:50:34 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:50:34,725 main INFO screen FISHTT pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (1.6s)
Sep 12 07:50:58 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:50:58,412 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:51:03 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:51:03,481 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:51:18 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:51:18,499 main INFO screen PUMP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 12 07:51:48 ubuntu-4gb-fsn1-1 python[65177]: 2026-09-12 07:51:48,917 main INFO screen RAGE pass=0 dev=1.51 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 1min 20.246s CPU time over 10min 32.864s wall clock time, 109.3M memory peak.
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:51:51,863 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:51:51 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 12 07:51:51 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:51:51,913 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 07:52:53 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:52:53,463 main INFO screen KILL pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 12 07:53:06 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:06,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:53:08 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:08,616 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:53:11 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:11,542 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:53:13 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:13,645 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:53:27 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:27,929 main INFO screen Frankie pass=0 dev=0.0 ins=23.51 pro=46 1a=False 1b=False 2=True (21.6s)
Sep 12 07:53:28 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:53:28,006 main INFO screen NASP pass=0 dev=0.19 ins=79.12 pro=8 1a=True 1b=True 2=True (19.5s)
Sep 12 07:54:41 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:54:41,653 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:54:46 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:54:46,727 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:54:59 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:54:59,996 main INFO screen CATWIZARD pass=0 dev=0.04 ins=78.03 pro=8 1a=False 1b=True 2=True (18.4s)
Sep 12 07:56:07 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:56:07,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:56:12 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:56:12,221 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:56:25 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:56:25,637 main INFO screen LIT pass=0 dev=0.0 ins=21.37 pro=32 1a=False 1b=False 2=True (18.6s)
Sep 12 07:56:53 ubuntu-4gb-fsn1-1 python[65502]: 2026-09-12 07:56:53,466 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:56:53 +0000] "GET /health HTTP/1.1" 200 486 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T07:09:50Z
--- update 2026-09-12T07:14:57Z
--- update 2026-09-12T07:20:13Z
--- update 2026-09-12T07:25:36Z
--- update 2026-09-12T07:30:51Z
--- update 2026-09-12T07:36:12Z
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
