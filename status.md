# Schaduwbot status

- tijd: 2026-09-11 08:04:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 17 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 537/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 1540, "tokens_in_memory": 535, "msgs": 107314, "trades": 33743, "creates": 535, "decode_fail": 1132, "rpc_calls": 688, "rpc_errors": 130, "sol_usd": 99.61875424137722, "open_positions": 53}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 07:38 UTC

Gelogde schaduwtrades: **19043**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 8436 | 1130 | 16 | 1130 | 92 | 2244 | 6688 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 235 | 15% | 1.7% | +41.5% | -16.3% | -7.70% | 98% |
| dip35_V1_gescreend_fail | 1894 | 26% | 3.9% | +45.9% | -26.1% | -7.12% | 100% |
| dip35_V1_alle | 2200 | 25% | 4.0% | +44.7% | -25.4% | -7.59% | 100% |
| dip35_V2_gescreend_pass | 236 | 17% | 2.1% | +40.5% | -21.0% | -10.29% | 100% |
| dip35_V2_gescreend_fail | 1905 | 24% | 4.7% | +54.6% | -28.4% | -8.36% | 100% |
| dip35_V2_alle | 2192 | 23% | 4.7% | +52.7% | -28.0% | -9.05% | 100% |
| dip35_V3_gescreend_pass | 236 | 7% | 2.5% | +141.2% | -23.0% | -11.87% | 100% |
| dip35_V3_gescreend_fail | 1921 | 13% | 6.5% | +115.1% | -30.3% | -11.67% | 100% |
| dip35_V3_alle | 2204 | 12% | 6.4% | +113.4% | -29.8% | -12.17% | 100% |
| dip40_V1_gescreend_pass | 219 | 13% | 1.8% | +44.2% | -15.8% | -8.17% | 98% |
| dip40_V1_gescreend_fail | 1847 | 26% | 3.8% | +47.8% | -26.0% | -6.58% | 100% |
| dip40_V1_alle | 2118 | 25% | 3.9% | +46.8% | -25.2% | -7.07% | 100% |
| dip40_V2_gescreend_pass | 220 | 13% | 1.8% | +50.8% | -19.8% | -10.49% | 100% |
| dip40_V2_gescreend_fail | 1853 | 25% | 4.3% | +55.0% | -28.2% | -7.59% | 100% |
| dip40_V2_alle | 2109 | 23% | 4.3% | +54.3% | -27.6% | -8.37% | 100% |
| dip40_V3_gescreend_pass | 220 | 6% | 2.3% | +116.7% | -21.7% | -13.51% | 100% |
| dip40_V3_gescreend_fail | 1868 | 13% | 6.0% | +104.2% | -30.0% | -12.94% | 100% |
| dip40_V3_alle | 2121 | 12% | 5.9% | +103.3% | -29.3% | -13.44% | 100% |
| dip45_V1_gescreend_pass | 208 | 15% | 1.9% | +50.6% | -15.6% | -5.74% | 95% |
| dip45_V1_gescreend_fail | 1793 | 28% | 3.3% | +49.7% | -25.6% | -4.68% | 100% |
| dip45_V1_alle | 2037 | 26% | 3.4% | +49.4% | -24.7% | -5.11% | 100% |
| dip45_V2_gescreend_pass | 208 | 19% | 2.4% | +51.3% | -19.5% | -6.20% | 97% |
| dip45_V2_gescreend_fail | 1791 | 26% | 3.8% | +59.1% | -27.6% | -5.54% | 100% |
| dip45_V2_alle | 2026 | 25% | 3.9% | +58.1% | -27.0% | -6.00% | 100% |
| dip45_V3_gescreend_pass | 208 | 7% | 2.9% | +198.9% | -20.8% | -6.03% | 99% |
| dip45_V3_gescreend_fail | 1804 | 14% | 5.8% | +113.1% | -29.4% | -10.12% | 100% |
| dip45_V3_alle | 2036 | 13% | 5.7% | +116.5% | -28.7% | -10.08% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 1594 | 12% | 2.7% | -9.88% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 07:55:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:55:52,815 main INFO screen $AURA pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 07:56:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:56:47,332 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:56:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:56:47,478 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:56:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:56:47,661 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (0.4s)
Sep 11 07:56:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:56:52,722 main INFO screen aa pass=0 dev=3.42 ins=0.0 pro=8 1a=False 1b=False 2=False (3.3s)
Sep 11 07:58:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:03,067 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:58:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:03,137 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:58:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:03,320 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:58:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:47,276 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:58:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:47,408 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:58:47 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:58:47,596 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:59:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:05,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:59:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:05,236 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:59:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:05,580 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 07:59:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:06,428 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:59:06 +0000] "GET /health HTTP/1.1" 200 415 "-" "Python-urllib/3.14"
Sep 11 07:59:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:15,323 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:59:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:15,447 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:59:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:15,606 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 07:59:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:43,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:59:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:43,414 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:59:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:59:43,609 main INFO screen jsjhsh pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 08:00:13 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:13,759 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:00:13 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:13,892 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:00:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:19,860 main INFO screen RODENT pass=0 dev=0.0 ins=17.72 pro=12 1a=False 1b=False 2=True (6.2s)
Sep 11 08:00:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:22,027 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:00:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:22,155 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:00:26 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:26,003 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (4.0s)
Sep 11 08:00:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:39,789 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:00:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:39,882 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:00:40 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:40,357 main INFO screen a real man pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 11 08:00:57 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:57,845 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:00:57 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:00:57,973 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:01:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:00,298 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:01:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:00,419 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:01:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:00,827 main INFO screen a real man pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.6s)
Sep 11 08:01:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:01,809 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 08:01:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:02,480 main INFO screen GRADELESS pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 11 08:01:31 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:31,766 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:01:31 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:31,896 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:01:35 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:35,160 main INFO screen 2 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 11 08:01:35 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:35,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:01:35 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:35,317 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:01:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:36,231 main INFO screen KlShE pass=0 dev=9.37 ins=0.0 pro=1 1a=False 1b=False 2=False (8.7s)
Sep 11 08:01:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:38,255 main INFO screen RISE pass=0 dev=39.77 ins=0.0 pro=8 1a=False 1b=False 2=False (8.5s)
Sep 11 08:01:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:39,728 main INFO screen XCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 11 08:01:49 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:49,282 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:01:49 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:49,412 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:01:49 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:01:49,546 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:02:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:05,118 main INFO screen LMAO pass=0 dev=0.97 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 11 08:02:14 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:14,269 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:02:14 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:14,406 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:02:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:20,788 main INFO screen 911 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.6s)
Sep 11 08:02:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:28,947 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:02:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:29,241 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:02:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:29,525 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 11 08:02:33 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:33,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:02:33 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:33,743 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:02:35 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:35,794 main INFO screen LMAO pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 11 08:02:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:38,309 main INFO screen assasa pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.8s)
Sep 11 08:02:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:39,063 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:02:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:39,197 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:02:45 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:45,814 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.8s)
Sep 11 08:02:53 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:53,038 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:02:53 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:02:53,165 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:03:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:00,281 main INFO screen FPOOP pass=0 dev=0.0 ins=79.27 pro=8 1a=False 1b=False 2=True (7.3s)
Sep 11 08:03:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:05,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:03:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:05,998 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:03:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:10,387 main INFO screen sasasa pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.6s)
Sep 11 08:03:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:15,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:03:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:15,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:03:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:19,384 main INFO screen FLYBRAIN pass=0 dev=0.0 ins=76.71 pro=6 1a=False 1b=False 2=True (3.8s)
Sep 11 08:03:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:21,135 main INFO screen registry pass=0 dev=3.98 ins=18.2 pro=68 1a=False 1b=True 2=False (6.9s)
Sep 11 08:03:31 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:31,524 main INFO screen LCN pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 08:03:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:32,785 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:03:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:32,909 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:03:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:39,701 main INFO screen gamble pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.0s)
Sep 11 08:03:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:54,286 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:03:54 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:03:54,388 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:04:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:04:00,743 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 11 08:04:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:04:37,068 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:04:37 +0000] "GET /health HTTP/1.1" 200 418 "-" "Python-urllib/3.14"
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
