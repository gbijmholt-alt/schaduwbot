# Schaduwbot status

- tijd: 2026-09-12 02:42:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 12 hours, 55 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1079/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 25361, "tokens_in_memory": 7816, "msgs": 5124008, "trades": 964648, "creates": 9026, "decode_fail": 52815, "rpc_calls": 32503, "rpc_errors": 1299, "sol_usd": 101.70313958425344, "open_positions": 37, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **39337**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 3089 | 511 | 3 | 510 | 29 | 905 | 2781 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 448 | 17% | 2.2% | +44.4% | -16.9% | -6.46% | 100% |
| dip35_V1_gescreend_fail | 3748 | 27% | 3.7% | +45.6% | -25.9% | -6.79% | 100% |
| dip35_V1_alle | 4548 | 26% | 3.8% | +44.7% | -25.2% | -6.89% | 100% |
| dip35_V2_gescreend_pass | 445 | 22% | 3.1% | +43.5% | -21.4% | -7.14% | 100% |
| dip35_V2_gescreend_fail | 3781 | 25% | 4.3% | +56.5% | -27.9% | -7.17% | 100% |
| dip35_V2_alle | 4516 | 24% | 4.4% | +54.0% | -27.6% | -7.77% | 100% |
| dip35_V3_gescreend_pass | 447 | 8% | 3.6% | +323.1% | -22.7% | +6.69% | 100% |
| dip35_V3_gescreend_fail | 3854 | 13% | 5.9% | +117.5% | -29.6% | -9.99% | 100% |
| dip35_V3_alle | 4560 | 13% | 5.9% | +124.0% | -29.2% | -9.14% | 100% |
| dip40_V1_gescreend_pass | 418 | 15% | 2.4% | +47.1% | -16.2% | -6.64% | 100% |
| dip40_V1_gescreend_fail | 3681 | 26% | 3.8% | +47.5% | -25.8% | -6.60% | 100% |
| dip40_V1_alle | 4370 | 25% | 3.8% | +47.4% | -25.1% | -6.67% | 100% |
| dip40_V2_gescreend_pass | 416 | 18% | 2.9% | +46.1% | -20.1% | -8.33% | 100% |
| dip40_V2_gescreend_fail | 3693 | 25% | 4.3% | +55.5% | -27.9% | -7.24% | 100% |
| dip40_V2_alle | 4332 | 24% | 4.4% | +53.8% | -27.4% | -7.91% | 100% |
| dip40_V3_gescreend_pass | 419 | 7% | 3.1% | +332.9% | -21.3% | +4.87% | 100% |
| dip40_V3_gescreend_fail | 3761 | 13% | 5.8% | +115.7% | -29.4% | -10.49% | 100% |
| dip40_V3_alle | 4378 | 13% | 5.8% | +122.6% | -28.9% | -9.72% | 100% |
| dip45_V1_gescreend_pass | 402 | 16% | 2.2% | +48.7% | -16.1% | -5.78% | 100% |
| dip45_V1_gescreend_fail | 3596 | 27% | 3.3% | +48.4% | -25.5% | -5.29% | 100% |
| dip45_V1_alle | 4223 | 26% | 3.4% | +48.4% | -24.8% | -5.60% | 100% |
| dip45_V2_gescreend_pass | 399 | 19% | 2.8% | +45.1% | -20.0% | -7.43% | 100% |
| dip45_V2_gescreend_fail | 3598 | 25% | 3.9% | +58.0% | -27.5% | -6.06% | 100% |
| dip45_V2_alle | 4185 | 24% | 4.0% | +56.1% | -27.1% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 402 | 7% | 2.7% | +392.1% | -20.7% | +9.12% | 100% |
| dip45_V3_gescreend_fail | 3656 | 14% | 5.5% | +121.3% | -29.0% | -7.99% | 100% |
| dip45_V3_alle | 4225 | 13% | 5.5% | +131.2% | -28.5% | -7.14% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2926 | 13% | 3.6% | -10.08% | 100% |
| zonder_xlink | 870 | 19% | 0.0% | +23.66% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 02:26:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:17,601 main INFO screen Kwit pass=0 dev=1.46 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 02:26:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:20,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:25,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:34,676 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:39,746 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:44,379 main INFO screen ALLDOG pass=0 dev=3.42 ins=75.89 pro=1 1a=False 1b=True 2=True (24.1s)
Sep 12 02:26:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:56,658 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:26:59,462 main INFO screen SBF pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.8s)
Sep 12 02:27:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:01,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:27:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:23,845 main INFO screen TNT pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (27.2s)
Sep 12 02:27:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:34,971 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:27:34 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:27:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:27:51,206 main INFO screen TRUMP pass=0 dev=0.44 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 12 02:28:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:42,777 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:02:28:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 02:28:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:43,135 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:02:28:43 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 02:28:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:49,209 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:28:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:28:54,280 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:13,637 main INFO screen NUT pass=0 dev=6.63 ins=18.32 pro=42 1a=False 1b=False 2=False (5.4s)
Sep 12 02:29:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:15,366 main INFO screen NVDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.2s)
Sep 12 02:29:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:18,394 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:23,483 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:29:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:37,212 main INFO screen catfis pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (6.4s)
Sep 12 02:29:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:41,147 main INFO screen UP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.8s)
Sep 12 02:29:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:29:57,649 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:02,716 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:14,698 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:20,135 main INFO screen LOOM pass=0 dev=7.55 ins=23.35 pro=33 1a=False 1b=False 2=True (22.6s)
Sep 12 02:30:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:27,093 main INFO screen utility pass=0 dev=0.0 ins=19.43 pro=64 1a=False 1b=False 2=True (12.5s)
Sep 12 02:30:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:31,327 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:36,396 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:30:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:30:55,567 main INFO screen utility pass=0 dev=0.0 ins=18.32 pro=42 1a=False 1b=False 2=True (24.3s)
Sep 12 02:31:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:15,611 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:20,681 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:35,003 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:31:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:42,289 main INFO screen Predator pass=0 dev=0.0 ins=42.65 pro=56 1a=False 1b=False 2=True (26.8s)
Sep 12 02:31:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:31:48,347 main INFO screen VOIDHODL pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (13.8s)
Sep 12 02:32:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:32:34,837 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:32:34 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 12 02:34:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:07,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:34:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:12,937 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:34:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:26,232 main INFO screen utility pass=0 dev=0.0 ins=18.32 pro=37 1a=False 1b=False 2=True (18.5s)
Sep 12 02:34:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:40,258 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 12 02:34:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:42,025 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:34:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:46,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:34:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:50,935 main INFO screen VAGINA pass=0 dev=0.0 ins=16.22 pro=33 1a=False 1b=False 2=True (8.9s)
Sep 12 02:34:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:34:51,985 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:06,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:06,872 main INFO screen USWR pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.1s)
Sep 12 02:35:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:11,752 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:17,807 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:22,880 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:26,335 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (19.8s)
Sep 12 02:35:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:29,722 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:34,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:35:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:37,190 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.4s)
Sep 12 02:35:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:41,459 main INFO screen SXSN pass=0 dev=0.73 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 12 02:35:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:47,979 main INFO screen NOTHING pass=0 dev=0.0 ins=65.27 pro=6 1a=False 1b=False 2=True (18.3s)
Sep 12 02:35:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:35:53,854 main INFO screen RAM pass=0 dev=0.0 ins=16.28 pro=57 1a=False 1b=False 2=True (3.4s)
Sep 12 02:36:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:36:45,270 main INFO screen ZEC pass=0 dev=0.0 ins=18.38 pro=24 1a=False 1b=False 2=True (3.9s)
Sep 12 02:37:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:37:06,500 main INFO screen CIPHERCOIN pass=0 dev=0.12 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 12 02:37:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:37:37,174 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:37:37 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
Sep 12 02:37:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:37:52,621 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:38:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:38:00,036 main INFO screen Jarvis pass=0 dev=0.0 ins=0.0 pro=42 1a=False 1b=False 2=True (7.5s)
Sep 12 02:38:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:38:11,747 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:38:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:38:18,669 main INFO screen ZEC pass=0 dev=6.63 ins=19.9 pro=22 1a=False 1b=False 2=False (7.0s)
Sep 12 02:39:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:39:56,705 main INFO screen mortus pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.3s)
Sep 12 02:40:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:40:00,778 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:40:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:40:03,887 main INFO screen COMPCAT pass=0 dev=0.0 ins=28.68 pro=29 1a=False 1b=True 2=False (2.2s)
Sep 12 02:40:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:40:05,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:40:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:40:55,481 main INFO screen fuelcoin pass=0 dev=0.0 ins=18.32 pro=22 1a=False 1b=False 2=True (54.8s)
Sep 12 02:41:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:41:39,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:41:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:41:44,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:41:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:41:59,536 main INFO screen MISSILE pass=0 dev=0.0 ins=18.79 pro=34 1a=False 1b=False 2=True (19.7s)
Sep 12 02:42:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:06,395 main INFO screen Ant pass=0 dev=1.81 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 12 02:42:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:13,602 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:42:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:18,669 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:42:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:26,395 main INFO screen ENGINE pass=1 dev=0.0 ins=0.01 pro=62 1a=False 1b=False 2=False (3.8s)
Sep 12 02:42:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:35,978 main INFO screen VPN pass=1 dev=0.0 ins=5.11 pro=33 1a=False 1b=False 2=False (5.7s)
Sep 12 02:42:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:36,866 main INFO screen wtf pass=0 dev=0.0 ins=16.78 pro=25 1a=False 1b=False 2=True (23.3s)
Sep 12 02:42:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:42,028 main INFO screen mortus pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.1s)
Sep 12 02:42:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:46,686 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 02:42:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 02:42:49,349 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:02:42:49 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T01:16:55Z
--- update 2026-09-12T01:22:03Z
--- update 2026-09-12T01:27:11Z
--- update 2026-09-12T01:32:13Z
--- update 2026-09-12T01:37:15Z
--- update 2026-09-12T01:42:15Z
--- update 2026-09-12T01:47:19Z
--- update 2026-09-12T01:52:21Z
Running as unit: schaduwbot-wallets.service; invocation ID: 39f959b4ea4249ad9802ce16bcd55516
analyses gestart (8746aefc73b4)
--- update 2026-09-12T01:57:21Z
--- update 2026-09-12T02:02:22Z
--- update 2026-09-12T02:07:22Z
--- update 2026-09-12T02:12:26Z
--- update 2026-09-12T02:17:29Z
--- update 2026-09-12T02:22:33Z
--- update 2026-09-12T02:27:33Z
--- update 2026-09-12T02:32:33Z
--- update 2026-09-12T02:37:36Z
--- update 2026-09-12T02:42:48Z
```

## Analyses (laatste 25 regels)
```
inactive
01:52:48 3000 aankopen van gevolgde wallets geëvalueerd
01:53:00 grote spelers: saldo van 1359 wallets opgehaald
01:53:57 herkomst: 40 posities gekoppeld
01:53:58 klaar in 97s -> /opt/schaduwbot/reports/ledger.md
01:54:00   2000 nieuwe tokens doorgerekend
01:54:02 klaar in 4s: 11080 tokens, 2981 nieuw -> /opt/schaduwbot/reports/video_replay.md
01:54:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 01:54 UTC
01:54:02 45856 tokens geladen
01:54:04   2000 tokens, 253102 trades, 54428 posities (2s)
01:54:07   4000 tokens, 520825 trades, 111725 posities (5s)
01:54:09   6000 tokens, 782379 trades, 167557 posities (7s)
01:54:11   8000 tokens, 1054119 trades, 222555 posities (9s)
01:54:13   10000 tokens, 1329211 trades, 281413 posities (11s)
01:54:16   12000 tokens, 1594580 trades, 333921 posities (13s)
01:54:18   14000 tokens, 1836819 trades, 382990 posities (15s)
01:54:20   16000 tokens, 2119459 trades, 446339 posities (18s)
01:54:22   18000 tokens, 2395048 trades, 502642 posities (20s)
01:54:24   20000 tokens, 2629029 trades, 552671 posities (22s)
01:54:27   22000 tokens, 2903307 trades, 608372 posities (24s)
01:54:29 posities: 660394 uit 3108846 trades (26s)
01:54:37 148332 wallets gerekend
01:54:38 geluk-toets
01:55:03 persistentie
01:55:05 kopieer-simulatie
01:55:14 klaar in 72s -> /opt/schaduwbot/reports/wallets.md
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
