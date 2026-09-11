# Schaduwbot status

- tijd: 2026-09-11 17:51:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 4 hours, 4 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.7G/38G | geheugen: 877/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 28916, "tokens_in_memory": 7425, "msgs": 3606872, "trades": 864061, "creates": 9284, "decode_fail": 65270, "rpc_calls": 16137, "rpc_errors": 1397, "sol_usd": 101.94782160458446, "open_positions": 103, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 17:49 UTC

Gelogde schaduwtrades: **28037**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 20025 | 2920 | 31 | 2920 | 211 | 5313 | 15682 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 309 | 16% | 1.9% | +42.2% | -16.3% | -6.68% | 99% |
| dip35_V1_gescreend_fail | 2833 | 27% | 3.7% | +46.2% | -25.9% | -6.51% | 100% |
| dip35_V1_alle | 3241 | 26% | 3.8% | +45.5% | -25.2% | -6.75% | 100% |
| dip35_V2_gescreend_pass | 308 | 19% | 2.6% | +45.8% | -21.3% | -8.47% | 100% |
| dip35_V2_gescreend_fail | 2837 | 25% | 4.4% | +56.3% | -28.2% | -7.39% | 100% |
| dip35_V2_alle | 3218 | 24% | 4.4% | +54.9% | -27.8% | -7.91% | 100% |
| dip35_V3_gescreend_pass | 309 | 8% | 2.9% | +121.7% | -22.8% | -11.55% | 100% |
| dip35_V3_gescreend_fail | 2876 | 13% | 6.1% | +104.3% | -29.8% | -11.99% | 100% |
| dip35_V3_alle | 3253 | 13% | 6.0% | +102.8% | -29.3% | -12.30% | 100% |
| dip40_V1_gescreend_pass | 285 | 15% | 1.8% | +47.6% | -15.5% | -6.19% | 99% |
| dip40_V1_gescreend_fail | 2752 | 26% | 3.7% | +48.0% | -25.9% | -6.42% | 100% |
| dip40_V1_alle | 3115 | 26% | 3.7% | +47.7% | -25.1% | -6.54% | 100% |
| dip40_V2_gescreend_pass | 284 | 14% | 2.5% | +52.7% | -19.9% | -9.45% | 100% |
| dip40_V2_gescreend_fail | 2749 | 25% | 4.1% | +55.2% | -28.1% | -7.53% | 100% |
| dip40_V2_alle | 3089 | 24% | 4.2% | +54.8% | -27.5% | -8.10% | 100% |
| dip40_V3_gescreend_pass | 286 | 7% | 2.4% | +100.2% | -21.2% | -13.13% | 100% |
| dip40_V3_gescreend_fail | 2787 | 13% | 5.8% | +91.9% | -29.6% | -13.93% | 100% |
| dip40_V3_alle | 3125 | 12% | 5.7% | +90.9% | -29.0% | -14.17% | 100% |
| dip45_V1_gescreend_pass | 272 | 15% | 1.5% | +53.0% | -15.1% | -4.61% | 98% |
| dip45_V1_gescreend_fail | 2680 | 27% | 3.3% | +49.4% | -25.6% | -5.24% | 100% |
| dip45_V1_alle | 3009 | 26% | 3.3% | +49.4% | -24.8% | -5.40% | 100% |
| dip45_V2_gescreend_pass | 270 | 18% | 2.2% | +50.5% | -19.3% | -6.88% | 99% |
| dip45_V2_gescreend_fail | 2664 | 25% | 3.8% | +58.9% | -27.6% | -6.26% | 100% |
| dip45_V2_alle | 2979 | 24% | 3.8% | +58.1% | -27.0% | -6.68% | 100% |
| dip45_V3_gescreend_pass | 272 | 7% | 2.2% | +155.9% | -20.3% | -7.98% | 100% |
| dip45_V3_gescreend_fail | 2695 | 14% | 5.5% | +105.2% | -29.1% | -10.75% | 100% |
| dip45_V3_alle | 3008 | 13% | 5.4% | +106.2% | -28.5% | -10.79% | 100% |

## Beste variant: dip45_V1_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2058 | 13% | 2.8% | -9.55% | 100% |
| zonder_xlink | 537 | 16% | 0.0% | -3.85% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 17:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:27,671 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:27,906 main INFO screen Flybook pass=0 dev=0.0 ins=25.0 pro=5 1a=False 1b=False 2=True (0.4s)
Sep 11 17:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:33,631 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:42:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:33,815 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:42:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:35,891 main INFO screen PAYBOX pass=1 dev=0.0 ins=2.86 pro=38 1a=False 1b=False 2=False (2.3s)
Sep 11 17:42:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:39,048 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:42:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:39,178 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:42:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:40,736 main INFO screen mnky pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (1.8s)
Sep 11 17:42:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:42:55,922 aiohttp.access INFO 189.18.97.61 [11/Sep/2026:17:42:55 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 11 17:43:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:00,841 main INFO screen RAYCAT pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.8s)
Sep 11 17:43:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:34,871 main INFO screen Milestones pass=0 dev=4.79 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 17:43:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:42,631 main INFO screen stocklana pass=0 dev=0.71 ins=0.0 pro=2 1a=False 1b=False 2=False (2.9s)
Sep 11 17:43:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:57,372 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:43:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:57,432 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:43:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:43:58,452 main INFO screen FLYWHALE pass=0 dev=0.0 ins=79.13 pro=9 1a=False 1b=False 2=True (2.2s)
Sep 11 17:44:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:10,385 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:44:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:10,524 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:44:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:10,671 main INFO screen stocklana pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 17:44:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:29,422 main INFO screen ペペ pass=1 dev=3.28 ins=0.79 pro=40 1a=False 1b=False 2=False (3.3s)
Sep 11 17:44:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:31,009 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:44:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:31,198 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:44:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:31,630 main INFO screen NINJACAT pass=0 dev=0.0 ins=4.45 pro=0 1a=False 1b=False 2=True (0.6s)
Sep 11 17:44:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:41,744 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:44:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:41,984 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:44:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:42,120 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 11 17:44:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:45,445 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.7s)
Sep 11 17:44:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:50,505 main INFO screen RI pass=0 dev=0.31 ins=0.0 pro=1 1a=False 1b=False 2=False (4.3s)
Sep 11 17:44:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:51,466 main INFO screen Liquididdy pass=1 dev=2.62 ins=0.0 pro=51 1a=False 1b=False 2=False (3.9s)
Sep 11 17:44:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:57,540 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:44:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:57,717 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:44:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:44:57,825 main INFO screen Memer pass=0 dev=0.0 ins=40.89 pro=13 1a=False 1b=False 2=True (0.3s)
Sep 11 17:45:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:45:35,222 main INFO screen Liquididdy pass=1 dev=0.0 ins=5.19 pro=52 1a=False 1b=False 2=False (3.4s)
Sep 11 17:45:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:45:44,091 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:45:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:45:44,222 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:45:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:45:44,383 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 17:46:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:08,127 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:46:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:08,221 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:46:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:08,413 main INFO screen Amazoon pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 17:46:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:11,656 main INFO screen HEDGIE pass=0 dev=0.0 ins=15.54 pro=20 1a=False 1b=True 2=True (1.2s)
Sep 11 17:46:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:14,999 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:46:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:15,127 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:46:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:15,276 main INFO screen Grok 4.7 pass=0 dev=0.0 ins=0.1 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 17:46:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:24,264 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:46:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:24,350 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:46:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:24,525 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 17:46:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:38,893 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:46:38 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 17:46:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:55,582 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:46:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:55,680 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:46:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:46:56,611 main INFO screen PEEDY pass=0 dev=0.0 ins=43.65 pro=1 1a=False 1b=False 2=True (1.1s)
Sep 11 17:47:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:09,190 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.5s)
Sep 11 17:47:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:33,491 main INFO screen CHEDDAR pass=0 dev=0.18 ins=0.0 pro=6 1a=False 1b=False 2=False (2.4s)
Sep 11 17:47:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:38,155 main INFO screen SUNSTRIKE pass=0 dev=3.42 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 11 17:47:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:43,586 main INFO screen DOOB pass=0 dev=0.15 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 17:47:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:46,632 main INFO screen 34% pass=0 dev=3.64 ins=0.0 pro=4 1a=False 1b=False 2=False (3.6s)
Sep 11 17:47:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:47:49,231 main INFO screen ROI pass=0 dev=0.0 ins=24.97 pro=17 1a=False 1b=False 2=True (1.4s)
Sep 11 17:48:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:48:27,200 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:48:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:48:27,288 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:48:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:48:27,487 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 17:49:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:09,104 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:49:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:09,355 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:49:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:09,552 main INFO screen 911 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 17:49:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:09,632 main INFO screen CHEDDAR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.7s)
Sep 11 17:49:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:22,976 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:49:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:23,099 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:49:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:49:23,232 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (0.3s)
Sep 11 17:50:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:43,487 main INFO screen BRAINROT pass=0 dev=0.0 ins=77.42 pro=8 1a=False 1b=True 2=True (3.7s)
Sep 11 17:50:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:44,273 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.9s)
Sep 11 17:50:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:45,029 main INFO screen 100 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 11 17:50:52 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:52,533 main INFO screen doge pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 11 17:50:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:55,661 main INFO screen Minecraft pass=0 dev=93.76 ins=0.0 pro=1 1a=False 1b=False 2=True (11.4s)
Sep 11 17:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:57,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:57,698 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:50:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:57,867 main INFO screen CAT pass=0 dev=0.0 ins=19.12 pro=12 1a=False 1b=False 2=True (2.2s)
Sep 11 17:50:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:59,603 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (14.6s)
Sep 11 17:50:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:50:59,796 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.3s)
Sep 11 17:51:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:51:10,518 main INFO screen $TRUMPX pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (10.7s)
Sep 11 17:51:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:51:11,007 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 11 17:51:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:51:12,393 main INFO screen ROI pass=1 dev=0.0 ins=4.99 pro=61 1a=False 1b=False 2=False (10.9s)
Sep 11 17:51:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:51:17,387 main INFO screen $CAT pass=0 dev=6.59 ins=0.0 pro=6 1a=False 1b=False 2=False (3.1s)
Sep 11 17:51:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:51:40,939 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:51:40 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T16:14:06Z
--- update 2026-09-11T16:19:29Z
--- update 2026-09-11T16:24:36Z
--- update 2026-09-11T16:29:47Z
--- update 2026-09-11T16:34:50Z
--- update 2026-09-11T16:40:09Z
--- update 2026-09-11T16:45:19Z
--- update 2026-09-11T16:50:30Z
--- update 2026-09-11T16:55:36Z
--- update 2026-09-11T17:00:58Z
--- update 2026-09-11T17:06:10Z
--- update 2026-09-11T17:11:21Z
--- update 2026-09-11T17:16:23Z
--- update 2026-09-11T17:21:29Z
--- update 2026-09-11T17:26:32Z
--- update 2026-09-11T17:31:32Z
--- update 2026-09-11T17:36:36Z
--- update 2026-09-11T17:41:37Z
--- update 2026-09-11T17:46:37Z
--- update 2026-09-11T17:51:39Z
```

## Analyses (laatste 25 regels)
```
inactive
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
16:03:36 7475 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
16:03:40   ingelezen tot rowid 1652718 (200000 rijen, 200000 bruikbaar)
16:03:41   ingelezen tot rowid 1684078 (231360 rijen, 231360 bruikbaar)
16:03:41 ingelezen: 231360 nieuwe trades, 231360 bruikbaar (4s)
16:03:46 klaar in 10s -> /opt/schaduwbot/reports/ledger.md
16:03:48   2000 nieuwe tokens doorgerekend
16:03:48 klaar in 2s: 3448 tokens, 2089 nieuw -> /opt/schaduwbot/reports/video_replay.md
16:03:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 16:03 UTC
16:03:48 32317 tokens geladen
16:03:51   2000 tokens, 318886 trades, 83589 posities (3s)
16:03:54   4000 tokens, 653328 trades, 170937 posities (6s)
16:03:57   6000 tokens, 953319 trades, 248089 posities (9s)
16:04:01   8000 tokens, 1282543 trades, 335538 posities (13s)
16:04:05   10000 tokens, 1602875 trades, 422034 posities (16s)
16:04:06 posities: 447031 uit 1684507 trades (17s)
16:04:12 104760 wallets gerekend
16:04:12 geluk-toets
16:04:29 persistentie
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
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
