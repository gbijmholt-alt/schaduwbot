# Schaduwbot status

- tijd: 2026-09-12 01:22:04 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 11 hours, 35 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.2G/38G | geheugen: 1013/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 20516, "tokens_in_memory": 7520, "msgs": 4472518, "trades": 817930, "creates": 7520, "decode_fail": 46260, "rpc_calls": 27595, "rpc_errors": 1075, "sol_usd": 102.0972269163235, "open_positions": 121, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **37359**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 826 | 131 | 0 | 129 | 11 | 253 | 803 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 430 | 17% | 2.3% | +44.5% | -17.0% | -6.58% | 100% |
| dip35_V1_gescreend_fail | 3585 | 27% | 3.6% | +45.6% | -25.9% | -6.81% | 100% |
| dip35_V1_alle | 4324 | 26% | 3.7% | +44.5% | -25.2% | -6.97% | 100% |
| dip35_V2_gescreend_pass | 427 | 22% | 3.3% | +45.3% | -21.5% | -7.10% | 100% |
| dip35_V2_gescreend_fail | 3606 | 25% | 4.2% | +56.4% | -28.1% | -7.23% | 100% |
| dip35_V2_alle | 4288 | 24% | 4.3% | +54.1% | -27.7% | -7.75% | 100% |
| dip35_V3_gescreend_pass | 428 | 9% | 3.7% | +331.7% | -22.9% | +7.80% | 100% |
| dip35_V3_gescreend_fail | 3682 | 13% | 5.9% | +119.1% | -29.6% | -9.76% | 100% |
| dip35_V3_alle | 4335 | 13% | 5.8% | +126.6% | -29.2% | -8.79% | 100% |
| dip40_V1_gescreend_pass | 400 | 15% | 2.5% | +47.3% | -16.3% | -6.96% | 100% |
| dip40_V1_gescreend_fail | 3515 | 26% | 3.7% | +47.4% | -25.9% | -6.70% | 100% |
| dip40_V1_alle | 4151 | 25% | 3.7% | +47.0% | -25.1% | -6.82% | 100% |
| dip40_V2_gescreend_pass | 398 | 17% | 3.0% | +49.4% | -20.2% | -8.46% | 100% |
| dip40_V2_gescreend_fail | 3516 | 25% | 4.2% | +55.4% | -28.0% | -7.49% | 100% |
| dip40_V2_alle | 4108 | 24% | 4.3% | +54.0% | -27.5% | -8.06% | 100% |
| dip40_V3_gescreend_pass | 401 | 8% | 3.2% | +343.8% | -21.4% | +5.91% | 100% |
| dip40_V3_gescreend_fail | 3591 | 13% | 5.8% | +116.6% | -29.5% | -10.50% | 100% |
| dip40_V3_alle | 4162 | 13% | 5.7% | +124.6% | -28.9% | -9.57% | 100% |
| dip45_V1_gescreend_pass | 385 | 16% | 2.3% | +48.8% | -16.2% | -5.91% | 100% |
| dip45_V1_gescreend_fail | 3431 | 27% | 3.2% | +47.9% | -25.6% | -5.51% | 100% |
| dip45_V1_alle | 4011 | 26% | 3.3% | +47.7% | -24.9% | -5.83% | 100% |
| dip45_V2_gescreend_pass | 381 | 19% | 2.9% | +47.6% | -20.1% | -7.27% | 100% |
| dip45_V2_gescreend_fail | 3421 | 25% | 3.8% | +57.4% | -27.6% | -6.46% | 100% |
| dip45_V2_alle | 3965 | 24% | 3.9% | +55.8% | -27.1% | -7.07% | 100% |
| dip45_V3_gescreend_pass | 385 | 8% | 2.9% | +392.1% | -20.7% | +10.38% | 100% |
| dip45_V3_gescreend_fail | 3487 | 14% | 5.3% | +123.3% | -28.9% | -7.77% | 100% |
| dip45_V3_alle | 4015 | 13% | 5.3% | +134.0% | -28.4% | -6.74% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.4%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2772 | 13% | 3.8% | -10.06% | 100% |
| zonder_xlink | 863 | 18% | 0.0% | +23.78% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 01:13:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:08,258 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:13:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:13,328 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:13:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:28,605 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.4s)
Sep 12 01:13:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:30,952 main INFO screen OLD pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (9.8s)
Sep 12 01:13:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:33,057 main INFO screen kittylick pass=0 dev=1.07 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 12 01:13:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:33,263 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:13:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:38,368 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:13:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:38,488 main INFO screen TOKEN pass=0 dev=0.0 ins=9.94 pro=66 1a=False 1b=False 2=True (3.4s)
Sep 12 01:13:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:53,889 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:13:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:57,434 main INFO screen dwog pass=0 dev=3.73 ins=18.32 pro=35 1a=False 1b=False 2=True (24.2s)
Sep 12 01:13:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:13:58,960 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:14:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:06,634 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:14:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:12,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:14:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:13,780 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (20.0s)
Sep 12 01:14:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:25,884 main INFO screen SAVEME pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (19.3s)
Sep 12 01:14:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:30,986 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:14:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:36,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:14:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:53,295 main INFO screen SAVEME pass=0 dev=24.17 ins=0.0 pro=3 1a=False 1b=False 2=False (22.4s)
Sep 12 01:14:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:54,909 main INFO screen Meme pass=0 dev=0.0 ins=20.36 pro=33 1a=False 1b=False 2=True (8.0s)
Sep 12 01:14:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:14:58,109 main INFO screen NUT pass=0 dev=0.0 ins=11.54 pro=47 1a=False 1b=False 2=True (9.6s)
Sep 12 01:15:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:15,044 main INFO screen 6 pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 12 01:15:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:46,308 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:15:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:46,532 main INFO screen SCRVAN pass=0 dev=1.68 ins=0.0 pro=3 1a=False 1b=False 2=False (9.3s)
Sep 12 01:15:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:52,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:15:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:56,374 main INFO screen POO pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=True (10.1s)
Sep 12 01:15:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:15:57,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:16:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:16:02,575 main INFO screen skipoo pass=0 dev=0.88 ins=0.0 pro=4 1a=False 1b=False 2=False (7.9s)
Sep 12 01:16:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:16:07,023 aiohttp.access INFO 4.148.1.139 [12/Sep/2026:01:16:07 +0000] "GET /actuator/health HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 12 01:16:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:16:11,434 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (19.5s)
Sep 12 01:16:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:16:56,203 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:16:56 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 01:17:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:24,084 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:17:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:29,110 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:17:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:42,677 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:17:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:45,379 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (21.4s)
Sep 12 01:17:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:47,704 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:17:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:52,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:17:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:57,417 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:01:17:57 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 01:17:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:17:57,919 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:01,368 main INFO screen SAVEME pass=0 dev=0.12 ins=0.0 pro=2 1a=False 1b=False 2=False (19.2s)
Sep 12 01:18:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:02,055 main INFO screen TvsF pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 12 01:18:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:05,627 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:10,956 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:12,186 main INFO screen SAVEME pass=0 dev=22.37 ins=0.0 pro=2 1a=False 1b=False 2=False (19.4s)
Sep 12 01:18:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:28,628 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:33,281 main INFO screen fuckyou pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (27.7s)
Sep 12 01:18:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:33,707 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:41,307 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:46,884 main INFO screen fuckyou pass=0 dev=0.89 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 12 01:18:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:46,900 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:18:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:51,517 main INFO screen XBT pass=0 dev=0.0 ins=26.42 pro=70 1a=False 1b=False 2=True (23.0s)
Sep 12 01:18:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:18:57,317 main INFO screen SXSN pass=0 dev=0.08 ins=0.0 pro=1 1a=False 1b=False 2=False (5.7s)
Sep 12 01:19:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:01,477 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (20.2s)
Sep 12 01:19:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:10,165 main INFO screen FKBBY pass=0 dev=1.32 ins=0.0 pro=1 1a=False 1b=False 2=False (10.8s)
Sep 12 01:19:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:36,312 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:19:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:41,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:19:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:51,822 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:19:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:56,869 main INFO screen WOFI pass=0 dev=2.69 ins=79.31 pro=1 1a=False 1b=False 2=True (20.7s)
Sep 12 01:19:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:19:56,888 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:18,107 main INFO screen fuckyou pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (26.4s)
Sep 12 01:20:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:20,129 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:23,624 main INFO screen fuckyou pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (9.3s)
Sep 12 01:20:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:24,666 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:25,197 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:31,279 main INFO screen SAVEME pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 01:20:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:40,017 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:43,743 main INFO screen MEME pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.7s)
Sep 12 01:20:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:45,184 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:20:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:47,422 main INFO screen skipoo pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (7.8s)
Sep 12 01:20:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:53,641 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (9.9s)
Sep 12 01:20:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:20:55,995 main INFO screen NODE pass=0 dev=0.77 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 12 01:21:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:04,387 main INFO screen CUCUMBER pass=0 dev=0.18 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 01:21:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:04,568 main INFO screen WOTF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.9s)
Sep 12 01:21:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:19,297 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 01:21:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:23,445 main INFO screen SAVEME pass=0 dev=26.17 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 12 01:21:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:24,284 main INFO screen rats pass=1 dev=1.26 ins=17.43 pro=38 1a=False 1b=False 2=False (4.7s)
Sep 12 01:21:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:34,382 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (15.2s)
Sep 12 01:21:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:39,934 main INFO screen Eme pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (5.6s)
Sep 12 01:21:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:57,176 main WARNING stream verbroken: no close frame received or sent — opnieuw over 1s
Sep 12 01:21:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:21:58,297 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 12 01:22:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 01:22:04,611 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:01:22:04 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: b162cdb09d844c599f2691bd2f42382f
analyses gestart (8746aefc73b4)
--- update 2026-09-11T23:52:35Z
--- update 2026-09-11T23:57:36Z
--- update 2026-09-12T00:02:54Z
--- update 2026-09-12T00:08:05Z
--- update 2026-09-12T00:13:36Z
--- update 2026-09-12T00:18:41Z
--- update 2026-09-12T00:24:13Z
--- update 2026-09-12T00:29:13Z
--- update 2026-09-12T00:34:36Z
--- update 2026-09-12T00:39:59Z
--- update 2026-09-12T00:45:13Z
--- update 2026-09-12T00:50:17Z
--- update 2026-09-12T00:55:36Z
--- update 2026-09-12T01:00:52Z
--- update 2026-09-12T01:06:31Z
--- update 2026-09-12T01:11:36Z
--- update 2026-09-12T01:16:55Z
--- update 2026-09-12T01:22:03Z
```

## Analyses (laatste 25 regels)
```
inactive
23:47:43 ingelezen: 322040 nieuwe trades, 322040 bruikbaar (7s)
23:48:00 2429 aankopen van gevolgde wallets geëvalueerd
23:48:06 grote spelers: saldo van 404 wallets opgehaald
23:49:10 herkomst: 40 posities gekoppeld
23:49:11 klaar in 95s -> /opt/schaduwbot/reports/ledger.md
23:49:13   2000 nieuwe tokens doorgerekend
23:49:14 klaar in 4s: 8512 tokens, 2651 nieuw -> /opt/schaduwbot/reports/video_replay.md
23:49:15 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 23:49 UTC
23:49:15 43238 tokens geladen
23:49:17   2000 tokens, 267586 trades, 60734 posities (3s)
23:49:20   4000 tokens, 532423 trades, 117776 posities (5s)
23:49:22   6000 tokens, 799668 trades, 174921 posities (7s)
23:49:24   8000 tokens, 1110246 trades, 245252 posities (10s)
23:49:26   10000 tokens, 1366401 trades, 294918 posities (12s)
23:49:29   12000 tokens, 1641516 trades, 355008 posities (14s)
23:49:31   14000 tokens, 1922876 trades, 417966 posities (16s)
23:49:34   16000 tokens, 2201914 trades, 478052 posities (19s)
23:49:36   18000 tokens, 2446968 trades, 532110 posities (22s)
23:49:39   20000 tokens, 2731719 trades, 594313 posities (24s)
23:49:40 posities: 627709 uit 2860518 trades (26s)
23:49:48 141754 wallets gerekend
23:49:49 geluk-toets
23:50:14 persistentie
23:50:15 kopieer-simulatie
23:50:24 klaar in 70s -> /opt/schaduwbot/reports/wallets.md
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
