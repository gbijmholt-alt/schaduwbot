# Schaduwbot status

- tijd: 2026-09-12 06:03:41 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 16 hours, 16 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1122/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 37412, "tokens_in_memory": 6153, "msgs": 6907221, "trades": 1268806, "creates": 12130, "decode_fail": 61199, "rpc_calls": 43049, "rpc_errors": 1737, "sol_usd": 101.59078114957315, "open_positions": 27, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **41671**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 5902 | 963 | 4 | 963 | 68 | 1678 | 5115 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 483 | 17% | 2.1% | +44.1% | -16.7% | -6.63% | 100% |
| dip35_V1_gescreend_fail | 3934 | 27% | 3.8% | +45.7% | -25.9% | -6.57% | 100% |
| dip35_V1_alle | 4815 | 26% | 3.9% | +44.9% | -25.2% | -6.73% | 100% |
| dip35_V2_gescreend_pass | 480 | 22% | 2.9% | +43.1% | -21.1% | -7.03% | 100% |
| dip35_V2_gescreend_fail | 3972 | 25% | 4.4% | +56.7% | -27.9% | -6.77% | 100% |
| dip35_V2_alle | 4785 | 25% | 4.5% | +54.2% | -27.6% | -7.44% | 100% |
| dip35_V3_gescreend_pass | 482 | 9% | 3.3% | +297.3% | -22.4% | +5.42% | 100% |
| dip35_V3_gescreend_fail | 4051 | 14% | 5.9% | +115.7% | -29.6% | -9.89% | 100% |
| dip35_V3_alle | 4829 | 13% | 6.0% | +120.8% | -29.2% | -9.23% | 100% |
| dip40_V1_gescreend_pass | 452 | 15% | 2.2% | +46.7% | -16.0% | -6.72% | 100% |
| dip40_V1_gescreend_fail | 3866 | 26% | 3.8% | +47.3% | -25.7% | -6.44% | 100% |
| dip40_V1_alle | 4627 | 26% | 3.8% | +47.4% | -25.0% | -6.53% | 100% |
| dip40_V2_gescreend_pass | 450 | 18% | 2.7% | +46.2% | -19.9% | -8.01% | 100% |
| dip40_V2_gescreend_fail | 3882 | 25% | 4.2% | +56.5% | -27.8% | -6.77% | 100% |
| dip40_V2_alle | 4591 | 24% | 4.4% | +54.8% | -27.3% | -7.50% | 100% |
| dip40_V3_gescreend_pass | 453 | 8% | 2.9% | +294.2% | -21.2% | +3.88% | 100% |
| dip40_V3_gescreend_fail | 3956 | 13% | 5.7% | +113.3% | -29.4% | -10.41% | 100% |
| dip40_V3_alle | 4637 | 13% | 5.7% | +119.2% | -28.9% | -9.77% | 100% |
| dip45_V1_gescreend_pass | 434 | 15% | 2.1% | +48.7% | -15.9% | -5.91% | 100% |
| dip45_V1_gescreend_fail | 3782 | 27% | 3.3% | +48.4% | -25.4% | -5.15% | 100% |
| dip45_V1_alle | 4473 | 26% | 3.4% | +48.6% | -24.7% | -5.46% | 100% |
| dip45_V2_gescreend_pass | 431 | 20% | 2.6% | +43.7% | -19.8% | -7.41% | 100% |
| dip45_V2_gescreend_fail | 3791 | 25% | 3.9% | +58.9% | -27.4% | -5.55% | 100% |
| dip45_V2_alle | 4438 | 24% | 4.0% | +56.9% | -27.0% | -6.40% | 100% |
| dip45_V3_gescreend_pass | 433 | 8% | 2.5% | +352.6% | -20.5% | +7.92% | 100% |
| dip45_V3_gescreend_fail | 3852 | 14% | 5.4% | +118.8% | -28.9% | -8.11% | 100% |
| dip45_V3_alle | 4476 | 14% | 5.4% | +127.6% | -28.4% | -7.35% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 3183 | 13% | 3.3% | -10.01% | 100% |
| zonder_xlink | 915 | 19% | 0.0% | +22.62% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 05:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:36,304 main INFO screen BEAST pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (21.4s)
Sep 12 05:51:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:36,999 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.7s)
Sep 12 05:51:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:43,838 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:47,430 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:48,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:51:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:51:52,503 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:52:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:03,413 main INFO screen USGR pass=0 dev=42.92 ins=0.0 pro=2 1a=False 1b=False 2=True (19.6s)
Sep 12 05:52:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:06,639 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.3s)
Sep 12 05:52:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:52:46,755 main INFO screen NOTBAD pass=0 dev=0.27 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 12 05:53:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:21,937 main INFO screen Cashback pass=1 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (6.0s)
Sep 12 05:53:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:23,497 main INFO screen REVDOG pass=1 dev=2.75 ins=4.71 pro=39 1a=False 1b=False 2=False (4.0s)
Sep 12 05:53:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:26,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:53:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:32,051 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:53:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:36,132 main INFO screen MSTRbate pass=0 dev=0.0 ins=18.77 pro=29 1a=False 1b=False 2=True (3.6s)
Sep 12 05:53:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:39,489 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:53:39 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:53:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:53:46,714 main INFO screen UP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.8s)
Sep 12 05:54:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:08,584 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:54:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:13,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:54:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:17,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:54:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:22,451 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:54:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:28,484 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 05:54:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:54:36,492 main INFO screen KILLER pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.2s)
Sep 12 05:55:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:00,506 main INFO screen CHBU pass=0 dev=1.41 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 05:55:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:05,023 main INFO screen NOTBAD pass=0 dev=0.26 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 12 05:55:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:16,070 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:55:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:24,292 main INFO screen GOLD pass=0 dev=0.0 ins=12.3 pro=41 1a=False 1b=False 2=True (8.3s)
Sep 12 05:55:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:27,732 main INFO screen ASS pass=1 dev=0.0 ins=8.05 pro=34 1a=False 1b=False 2=False (3.4s)
Sep 12 05:55:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:55:42,489 main INFO screen REVCAT pass=0 dev=0.51 ins=0.0 pro=4 1a=False 1b=False 2=False (2.9s)
Sep 12 05:56:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:00,121 main INFO screen Bricko pass=0 dev=0.08 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 12 05:56:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:15,039 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:56:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:20,115 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:56:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:34,662 main INFO screen PILLY pass=1 dev=0.0 ins=15.14 pro=33 1a=False 1b=False 2=False (19.7s)
Sep 12 05:56:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:42,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:56:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:45,846 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:05:56:45 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "-"
Sep 12 05:56:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:45,870 aiohttp.access INFO 204.76.203.49 [12/Sep/2026:05:56:45 +0000] "UNKNOWN / HTTP/1.0" 400 214 "-" "-"
Sep 12 05:56:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:56:51,309 main INFO screen AMD pass=0 dev=0.0 ins=13.45 pro=60 1a=False 1b=False 2=True (8.5s)
Sep 12 05:57:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:57:41,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:57:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:57:46,456 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:57:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:57:59,730 main INFO screen TURBOFLY pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (18.4s)
Sep 12 05:58:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:10,340 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 05:58:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:39,988 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:58:39 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:58:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:41,665 main INFO screen SHIB pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 12 05:58:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:42,522 main INFO screen Peperdle pass=0 dev=1.91 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 12 05:58:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:51,205 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:58:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:54,231 main INFO screen tung pass=0 dev=3.42 ins=0.0 pro=2 1a=False 1b=False 2=True (2.7s)
Sep 12 05:58:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:58:56,232 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:59:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:59:11,517 main INFO screen MARKOV pass=0 dev=10.0 ins=21.94 pro=27 1a=False 1b=True 2=True (20.4s)
Sep 12 05:59:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:59:23,252 main INFO screen Peperdle pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 12 05:59:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:59:24,830 main INFO screen drill pass=0 dev=1.0 ins=21.85 pro=58 1a=False 1b=False 2=True (3.8s)
Sep 12 05:59:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:59:38,221 main INFO screen FGP pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 12 06:00:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:04,435 rpc WARNING rpc getTokenAccountsByOwner exc 500, message='Attempt to decode JSON with unexpected mimetype: ', url='https://mainnet.helius-rpc.com/?api-key=***'
Sep 12 06:00:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:05,215 main INFO screen ChatGPT pass=0 dev=0.0 ins=25.1 pro=68 1a=False 1b=False 2=True (4.4s)
Sep 12 06:00:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:17,101 main INFO screen ChatGPT pass=1 dev=0.0 ins=6.29 pro=20 1a=False 1b=False 2=False (3.3s)
Sep 12 06:00:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:18,482 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:00:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:24,435 main INFO screen ChatGPT pass=1 dev=0.0 ins=0.0 pro=26 1a=False 1b=False 2=False (4.8s)
Sep 12 06:00:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:27,310 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:00:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:29,020 main INFO screen REVCAT pass=0 dev=0.42 ins=0.0 pro=2 1a=False 1b=False 2=False (10.6s)
Sep 12 06:00:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:32,389 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:00:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:48,818 main INFO screen ORALCLE pass=0 dev=0.0 ins=15.03 pro=31 1a=False 1b=True 2=False (3.2s)
Sep 12 06:00:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:49,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:00:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:53,109 main INFO screen America250 pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (25.9s)
Sep 12 06:00:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:00:54,657 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:01:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:01:01,600 main INFO screen NOTBAD pass=0 dev=0.09 ins=0.0 pro=3 1a=False 1b=False 2=False (6.3s)
Sep 12 06:01:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:01:13,884 main INFO screen PURRPLEX pass=0 dev=0.18 ins=77.54 pro=9 1a=False 1b=True 2=True (24.3s)
Sep 12 06:01:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:01:20,536 main INFO screen ChatGPT pass=0 dev=0.03 ins=12.36 pro=36 1a=False 1b=False 2=True (3.2s)
Sep 12 06:01:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:01:36,783 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:01:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:01:41,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:02:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:03,103 main INFO screen FTFS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.4s)
Sep 12 06:02:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:16,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:02:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:22,577 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:02:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:28,400 main INFO screen DEREK pass=0 dev=3.56 ins=14.22 pro=47 1a=False 1b=False 2=True (6.9s)
Sep 12 06:02:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:45,314 main INFO screen McDonald's pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (28.5s)
Sep 12 06:02:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:46,530 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=True (7.3s)
Sep 12 06:02:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:54,830 main INFO screen REVDOG pass=1 dev=0.0 ins=11.4 pro=33 1a=False 1b=False 2=False (5.9s)
Sep 12 06:02:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:02:58,387 main INFO screen FERSPE pass=0 dev=1.35 ins=0.0 pro=2 1a=False 1b=False 2=False (10.2s)
Sep 12 06:03:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:00,821 main INFO screen SDS pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 12 06:03:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:15,433 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:03:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:20,502 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 06:03:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:40,215 main INFO screen Gatto pass=0 dev=15.17 ins=0.0 pro=22 1a=False 1b=True 2=False (5.5s)
Sep 12 06:03:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 06:03:41,135 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:06:03:41 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T04:36:20Z
--- update 2026-09-12T04:41:36Z
--- update 2026-09-12T04:46:50Z
--- update 2026-09-12T04:52:05Z
--- update 2026-09-12T04:57:05Z
--- update 2026-09-12T05:02:29Z
--- update 2026-09-12T05:07:36Z
--- update 2026-09-12T05:12:53Z
--- update 2026-09-12T05:18:21Z
--- update 2026-09-12T05:23:25Z
--- update 2026-09-12T05:28:27Z
--- update 2026-09-12T05:33:29Z
--- update 2026-09-12T05:38:34Z
--- update 2026-09-12T05:43:36Z
--- update 2026-09-12T05:48:37Z
--- update 2026-09-12T05:53:38Z
--- update 2026-09-12T05:58:38Z
Running as unit: schaduwbot-wallets.service; invocation ID: c28a94468726478892cb2c2291593995
analyses gestart (8746aefc73b4)
--- update 2026-09-12T06:03:40Z
```

## Analyses (laatste 25 regels)
```
inactive
06:00:21 herkomst: 40 posities gekoppeld
06:00:24 klaar in 105s -> /opt/schaduwbot/reports/ledger.md
06:00:26   2000 nieuwe tokens doorgerekend
06:00:28 klaar in 4s: 15164 tokens, 2060 nieuw -> /opt/schaduwbot/reports/video_replay.md
06:00:28 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 06:00 UTC
06:00:28 49689 tokens geladen
06:00:31   2000 tokens, 246938 trades, 51841 posities (3s)
06:00:34   4000 tokens, 499800 trades, 105942 posities (5s)
06:00:36   6000 tokens, 751494 trades, 153475 posities (8s)
06:00:39   8000 tokens, 995808 trades, 202157 posities (11s)
06:00:42   10000 tokens, 1288195 trades, 264246 posities (14s)
06:00:44   12000 tokens, 1532978 trades, 311516 posities (16s)
06:00:47   14000 tokens, 1796554 trades, 361411 posities (19s)
06:00:49   16000 tokens, 2038896 trades, 410768 posities (21s)
06:00:53   18000 tokens, 2311003 trades, 467733 posities (25s)
06:00:56   20000 tokens, 2564416 trades, 517269 posities (27s)
06:00:59   22000 tokens, 2805731 trades, 565457 posities (30s)
06:01:01   24000 tokens, 3062477 trades, 617032 posities (33s)
06:01:04   26000 tokens, 3331606 trades, 674482 posities (36s)
06:01:06 posities: 714595 uit 3489207 trades (38s)
06:01:16 156866 wallets gerekend
06:01:17 geluk-toets
06:01:51 persistentie
06:01:53 kopieer-simulatie
06:02:09 klaar in 101s -> /opt/schaduwbot/reports/wallets.md
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
