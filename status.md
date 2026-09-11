# Schaduwbot status

- tijd: 2026-09-11 11:59:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 22 hours, 12 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.4G/38G | geheugen: 631/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 7792, "tokens_in_memory": 1955, "msgs": 603509, "trades": 153461, "creates": 1955, "decode_fail": 6908, "rpc_calls": 2359, "rpc_errors": 281, "sol_usd": 99.47322315892453, "open_positions": 62, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 11:49 UTC

Gelogde schaduwtrades: **22005**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 12621 | 1705 | 23 | 1705 | 109 | 3291 | 9650 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 250 | 15% | 1.6% | +41.0% | -16.2% | -7.54% | 98% |
| dip35_V1_gescreend_fail | 2212 | 26% | 3.8% | +46.2% | -26.0% | -6.99% | 100% |
| dip35_V1_alle | 2542 | 26% | 3.9% | +45.0% | -25.4% | -7.36% | 100% |
| dip35_V2_gescreend_pass | 249 | 18% | 2.0% | +39.4% | -21.1% | -10.15% | 100% |
| dip35_V2_gescreend_fail | 2217 | 24% | 4.5% | +56.6% | -28.4% | -7.67% | 100% |
| dip35_V2_alle | 2524 | 24% | 4.6% | +54.6% | -28.0% | -8.37% | 100% |
| dip35_V3_gescreend_pass | 251 | 7% | 2.4% | +137.5% | -22.9% | -12.01% | 100% |
| dip35_V3_gescreend_fail | 2255 | 13% | 6.3% | +117.5% | -30.1% | -10.72% | 100% |
| dip35_V3_alle | 2559 | 13% | 6.2% | +115.1% | -29.6% | -11.31% | 100% |
| dip40_V1_gescreend_pass | 232 | 14% | 1.7% | +43.1% | -15.7% | -7.57% | 98% |
| dip40_V1_gescreend_fail | 2153 | 26% | 3.7% | +48.1% | -26.0% | -6.52% | 100% |
| dip40_V1_alle | 2445 | 25% | 3.8% | +47.1% | -25.2% | -6.91% | 100% |
| dip40_V2_gescreend_pass | 231 | 14% | 2.2% | +49.8% | -20.1% | -10.41% | 100% |
| dip40_V2_gescreend_fail | 2149 | 25% | 4.1% | +56.0% | -28.3% | -7.41% | 100% |
| dip40_V2_alle | 2423 | 24% | 4.3% | +55.2% | -27.7% | -8.14% | 100% |
| dip40_V3_gescreend_pass | 233 | 6% | 2.6% | +114.0% | -21.9% | -13.69% | 100% |
| dip40_V3_gescreend_fail | 2189 | 13% | 5.8% | +105.0% | -29.8% | -12.25% | 100% |
| dip40_V3_alle | 2461 | 12% | 5.8% | +103.6% | -29.3% | -12.82% | 100% |
| dip45_V1_gescreend_pass | 221 | 14% | 1.8% | +50.1% | -15.6% | -6.09% | 97% |
| dip45_V1_gescreend_fail | 2093 | 27% | 3.3% | +49.6% | -25.6% | -4.99% | 100% |
| dip45_V1_alle | 2358 | 26% | 3.4% | +49.3% | -24.8% | -5.37% | 100% |
| dip45_V2_gescreend_pass | 218 | 19% | 2.3% | +49.7% | -19.7% | -6.64% | 98% |
| dip45_V2_gescreend_fail | 2078 | 25% | 3.8% | +59.1% | -27.7% | -5.74% | 100% |
| dip45_V2_alle | 2330 | 25% | 3.9% | +58.0% | -27.2% | -6.24% | 100% |
| dip45_V3_gescreend_pass | 221 | 7% | 2.7% | +186.5% | -21.0% | -6.88% | 99% |
| dip45_V3_gescreend_fail | 2112 | 14% | 5.6% | +111.6% | -29.3% | -9.73% | 100% |
| dip45_V3_alle | 2363 | 13% | 5.6% | +113.5% | -28.8% | -9.85% | 100% |

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
| met_xlink | 1710 | 12% | 2.6% | -9.94% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 11:38:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:41,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:38:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:41,984 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:38:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:38:42,216 main INFO screen PEPENOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:39:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:46,867 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:39:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:47,009 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:39:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:47,208 main INFO screen Nikki pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,357 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,442 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:39:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:39:55,606 main INFO screen THUG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,710 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,835 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:40:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:01,960 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 11:40:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:31,017 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 11:40:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:40:45,144 main INFO screen Animalio pass=0 dev=0.07 ins=27.64 pro=12 1a=False 1b=False 2=False (3.8s)
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,494 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,669 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:41:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:41:17,908 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.5s)
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,559 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,659 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:42:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:16,849 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,219 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,345 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:42:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:27,469 main INFO screen BULLSTER pass=0 dev=0.0 ins=37.77 pro=15 1a=False 1b=False 2=True (0.3s)
Sep 11 11:42:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:42:59,027 main INFO screen BUFF pass=0 dev=1.23 ins=0.0 pro=1 1a=False 1b=False 2=False (2.0s)
Sep 11 11:43:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:43:39,363 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:43:39 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:44:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:44:16,275 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:44:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:44:16,364 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:44:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:44:16,573 main INFO screen TRIPLET pass=0 dev=0.0 ins=79.12 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 11:45:15 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:45:15,813 main INFO screen MEMES pass=0 dev=0.0 ins=15.04 pro=62 1a=False 1b=False 2=True (3.5s)
Sep 11 11:45:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:45:58,389 main INFO screen BPCATE pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 11:46:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:46:41,038 main INFO screen 34% pass=0 dev=0.64 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 11 11:48:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:48:37,978 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:48:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:48:38,108 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:48:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:48:38,315 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:49:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:49:04,795 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:49:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:49:04,895 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:49:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:49:05,088 main INFO screen Doge  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:49:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:49:08,942 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:49:08 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:50:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:50:33,714 main INFO screen TRANS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 11:50:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:50:44,626 main INFO screen PUP pass=0 dev=0.35 ins=37.77 pro=19 1a=False 1b=False 2=True (3.3s)
Sep 11 11:52:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:52:28,256 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:52:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:52:28,390 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:52:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:52:28,611 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 11:53:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:12,141 main INFO screen power pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 11:53:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:20,916 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:53:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:21,061 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:53:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:21,200 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 11:53:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:51,671 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:53:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:51,775 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:53:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:53:51,951 main INFO screen PHANCAT pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:54:18 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:18,503 main INFO screen ⬆️ pass=0 dev=0.34 ins=0.0 pro=4 1a=False 1b=False 2=False (3.5s)
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,333 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,460 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:54:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:22,602 main INFO screen WATER pass=0 dev=0.0 ins=25.62 pro=21 1a=False 1b=False 2=True (0.3s)
Sep 11 11:54:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:34,133 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:54:34 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
Sep 11 11:54:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:35,800 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:35,926 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:54:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:36,144 main INFO screen Launchcat pass=0 dev=0.0 ins=30.95 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 11:54:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:59,136 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:54:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:54:59,241 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:55:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:01,475 main INFO screen 🚀 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (2.4s)
Sep 11 11:55:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:29,914 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:55:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:30,013 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:55:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:55:30,234 main INFO screen JPPEPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:56:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:44,776 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:56:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:44,875 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:56:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:56:45,082 main INFO screen PRAWN pass=0 dev=0.0 ins=51.51 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 11:57:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:36,807 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:57:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:36,904 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:57:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:57:37,094 main INFO screen TRANS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 11:58:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:07,411 main INFO screen BUSTER pass=0 dev=0.35 ins=37.77 pro=16 1a=False 1b=False 2=True (3.9s)
Sep 11 11:58:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:31,367 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.5s)
Sep 11 11:58:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:35,054 main INFO screen RISE pass=0 dev=42.48 ins=0.0 pro=6 1a=False 1b=False 2=True (3.5s)
Sep 11 11:58:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:50,893 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:58:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:50,991 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:58:51 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:58:51,189 main INFO screen PHAN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,079 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,176 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 11:59:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:10,360 main INFO screen Wolf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 11:59:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 11:59:37,161 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:11:59:37 +0000] "GET /health HTTP/1.1" 200 446 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T10:31:36Z
--- update 2026-09-11T10:36:47Z
--- update 2026-09-11T10:41:47Z
--- update 2026-09-11T10:47:06Z
--- update 2026-09-11T10:52:18Z
--- update 2026-09-11T10:57:35Z
--- update 2026-09-11T11:02:35Z
--- update 2026-09-11T11:08:05Z
--- update 2026-09-11T11:13:36Z
--- update 2026-09-11T11:18:37Z
--- update 2026-09-11T11:23:37Z
--- update 2026-09-11T11:28:37Z
--- update 2026-09-11T11:33:37Z
--- update 2026-09-11T11:38:38Z
--- update 2026-09-11T11:43:38Z
--- update 2026-09-11T11:49:07Z
--- update 2026-09-11T11:54:33Z
--- update 2026-09-11T11:59:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 91d89b5fe55047b9bdf833a434bfc1f0
analyses gestart (8213ec5e675e)
```

## Analyses (laatste 25 regels)
```
active
08:52:53 geluk-toets
08:53:06 persistentie
08:53:07 kopieer-simulatie
08:53:11 klaar in 34s -> /opt/schaduwbot/reports/wallets.md
09:54:51 1006 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
09:54:53   ingelezen tot rowid 200000 (200000 rijen, 0 bruikbaar)
09:54:54   ingelezen tot rowid 400000 (400000 rijen, 0 bruikbaar)
09:54:55   ingelezen tot rowid 600000 (600000 rijen, 0 bruikbaar)
09:54:56   ingelezen tot rowid 800000 (800000 rijen, 0 bruikbaar)
09:54:57   ingelezen tot rowid 1000000 (1000000 rijen, 0 bruikbaar)
09:54:58   ingelezen tot rowid 1104902 (1104902 rijen, 62330 bruikbaar)
09:54:58 ingelezen: 1104902 nieuwe trades, 62330 bruikbaar (7s)
09:54:59 klaar in 7s -> /opt/schaduwbot/reports/ledger.md
09:54:59 klaar in 0s: 0 tokens, 0 nieuw -> /opt/schaduwbot/reports/video_replay.md
09:54:59 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 09:54 UTC
09:54:59 25844 tokens geladen
09:55:05   2000 tokens, 492920 trades, 158174 posities (6s)
09:55:11   4000 tokens, 1003526 trades, 323887 posities (12s)
09:55:12 posities: 358484 uit 1104943 trades (13s)
09:55:19 80901 wallets gerekend
09:55:19 geluk-toets
09:55:33 persistentie
09:55:34 kopieer-simulatie
09:55:39 klaar in 40s -> /opt/schaduwbot/reports/wallets.md
11:59:36 2892 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
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
