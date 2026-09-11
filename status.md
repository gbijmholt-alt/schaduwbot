# Schaduwbot status

- tijd: 2026-09-11 09:44:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 19 hours, 57 minutes
- bot-service: active
- code-versie: 3e65967
- schijf: 2.4G/38G | geheugen: 558/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.2, "uptime_s": 3418, "tokens_in_memory": 853, "msgs": 175790, "trades": 54146, "creates": 854, "decode_fail": 4635, "rpc_calls": 1278, "rpc_errors": 108, "sol_usd": 99.05043300364545, "open_positions": 41, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 08:47 UTC

Gelogde schaduwtrades: **20217**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 9843 | 1366 | 18 | 1366 | 99 | 2655 | 7862 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 241 | 15% | 1.7% | +40.4% | -16.5% | -7.74% | 98% |
| dip35_V1_gescreend_fail | 2021 | 26% | 4.0% | +46.0% | -26.4% | -7.46% | 100% |
| dip35_V1_alle | 2338 | 25% | 4.1% | +44.7% | -25.7% | -7.82% | 100% |
| dip35_V2_gescreend_pass | 242 | 18% | 2.1% | +39.3% | -21.1% | -10.35% | 100% |
| dip35_V2_gescreend_fail | 2029 | 24% | 4.6% | +55.0% | -28.7% | -8.72% | 100% |
| dip35_V2_alle | 2326 | 23% | 4.7% | +53.1% | -28.2% | -9.33% | 100% |
| dip35_V3_gescreend_pass | 242 | 7% | 2.5% | +141.2% | -23.1% | -12.22% | 100% |
| dip35_V3_gescreend_fail | 2057 | 13% | 6.5% | +111.6% | -30.4% | -12.26% | 100% |
| dip35_V3_alle | 2349 | 12% | 6.3% | +110.0% | -29.9% | -12.70% | 100% |
| dip40_V1_gescreend_pass | 223 | 13% | 1.8% | +42.7% | -15.9% | -8.26% | 98% |
| dip40_V1_gescreend_fail | 1966 | 26% | 3.9% | +47.9% | -26.3% | -6.87% | 100% |
| dip40_V1_alle | 2246 | 25% | 3.9% | +46.9% | -25.5% | -7.27% | 100% |
| dip40_V2_gescreend_pass | 224 | 13% | 1.8% | +49.8% | -19.8% | -10.50% | 100% |
| dip40_V2_gescreend_fail | 1967 | 24% | 4.3% | +55.9% | -28.5% | -7.90% | 100% |
| dip40_V2_alle | 2231 | 23% | 4.3% | +55.1% | -27.8% | -8.60% | 100% |
| dip40_V3_gescreend_pass | 224 | 6% | 2.2% | +116.7% | -21.7% | -13.64% | 100% |
| dip40_V3_gescreend_fail | 1995 | 13% | 6.1% | +103.3% | -30.2% | -13.11% | 100% |
| dip40_V3_alle | 2255 | 12% | 5.9% | +102.1% | -29.5% | -13.59% | 100% |
| dip45_V1_gescreend_pass | 212 | 15% | 1.9% | +50.6% | -15.7% | -6.02% | 96% |
| dip45_V1_gescreend_fail | 1909 | 28% | 3.4% | +49.9% | -25.9% | -5.06% | 100% |
| dip45_V1_alle | 2162 | 26% | 3.5% | +49.5% | -25.0% | -5.42% | 100% |
| dip45_V2_gescreend_pass | 212 | 19% | 2.4% | +50.3% | -19.5% | -6.37% | 97% |
| dip45_V2_gescreend_fail | 1902 | 25% | 3.8% | +59.8% | -27.9% | -5.97% | 100% |
| dip45_V2_alle | 2145 | 24% | 3.9% | +58.7% | -27.3% | -6.42% | 100% |
| dip45_V3_gescreend_pass | 212 | 7% | 2.8% | +186.5% | -20.9% | -6.20% | 99% |
| dip45_V3_gescreend_fail | 1926 | 14% | 5.9% | +111.7% | -29.6% | -10.29% | 100% |
| dip45_V3_alle | 2165 | 13% | 5.8% | +114.2% | -28.9% | -10.27% | 100% |

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
| met_xlink | 1636 | 12% | 2.6% | -10.04% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 09:26:37 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:26:37,605 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:26:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:26:42,021 main INFO screen pumpfly pass=0 dev=0.0 ins=9.64 pro=49 1a=False 1b=False 2=True (5.9s)
Sep 11 09:26:42 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:26:42,541 main INFO screen NUT pass=0 dev=0.0 ins=17.25 pro=13 1a=False 1b=False 2=True (5.5s)
Sep 11 09:26:49 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:26:49,808 main INFO screen WHALE pass=0 dev=4.38 ins=0.0 pro=2 1a=False 1b=False 2=False (8.3s)
Sep 11 09:26:54 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:26:54,614 main INFO screen CUTE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.9s)
Sep 11 09:27:24 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:27:24,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:27:24 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:27:24,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:27:30 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:27:30,311 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.3s)
Sep 11 09:28:32 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:32,194 main INFO screen Jose pass=1 dev=0.0 ins=19.88 pro=20 1a=False 1b=False 2=False (5.0s)
Sep 11 09:28:33 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:33,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:28:33 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:33,595 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:28:39 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:39,315 main INFO screen WBATON pass=0 dev=0.0 ins=77.91 pro=6 1a=False 1b=False 2=True (5.9s)
Sep 11 09:28:53 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:53,579 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:28:53 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:53,644 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:28:56 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:28:56,921 main INFO screen DAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.4s)
Sep 11 09:29:12 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:29:12,000 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:29:11 +0000] "GET /health HTTP/1.1" 200 440 "-" "Python-urllib/3.14"
Sep 11 09:29:34 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:29:34,436 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:29:34 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:29:34,570 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:29:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:29:35,452 main INFO screen $KVN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 11 09:29:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:29:41,684 main INFO screen CHUNGUS pass=0 dev=0.0 ins=16.79 pro=11 1a=False 1b=False 2=True (7.3s)
Sep 11 09:31:25 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:25,476 main INFO screen BetOnBlak pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.6s)
Sep 11 09:31:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:35,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:31:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:35,305 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:31:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:35,440 main INFO screen FLYCHAD pass=0 dev=0.0 ins=78.58 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 11 09:31:49 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:49,537 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:31:49 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:49,709 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:31:49 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:31:49,811 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 11 09:32:01 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:32:01,279 aiohttp.access INFO 94.154.43.70 [11/Sep/2026:09:32:01 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 11 09:32:40 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:32:40,853 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:32:40 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:32:40,938 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:32:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:32:41,307 main INFO screen fine pass=0 dev=0.0 ins=18.25 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 11 09:33:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:09,319 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:33:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:09,379 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:33:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:09,629 main INFO screen Microsoft pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 09:33:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:35,659 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:33:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:35,766 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:33:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:33:35,956 main INFO screen brainjack pass=0 dev=0.0 ins=79.31 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 09:34:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:34:23,394 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:34:23 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 09:34:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:34:23,434 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:34:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:34:23,526 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:34:23 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:34:23,715 main INFO screen NBATON pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 11 09:34:37 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:34:37,396 main INFO screen NUTS pass=0 dev=0.0 ins=16.69 pro=63 1a=False 1b=False 2=True (3.4s)
Sep 11 09:35:36 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:36,109 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:35:36 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:36,206 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:35:36 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:36,480 main INFO screen PUMPFLY pass=0 dev=0.0 ins=77.78 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 11 09:35:59 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:59,137 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:35:59 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:59,633 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:35:59 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:35:59,982 main INFO screen 100D pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.3s)
Sep 11 09:36:00 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:00,816 main INFO screen yoda coin pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 09:36:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:35,202 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:36:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:35,302 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:36:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:35,481 main INFO screen HONDA pass=0 dev=0.0 ins=16.63 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 09:36:40 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:40,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:36:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:41,062 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:36:41 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:36:41,191 main INFO screen ! pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 09:37:09 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:37:09,209 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 11 09:38:28 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:38:28,938 main INFO screen HALAL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.9s)
Sep 11 09:39:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:39:35,493 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:39:35 +0000] "GET /health HTTP/1.1" 200 442 "-" "Python-urllib/3.14"
Sep 11 09:39:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:39:46,828 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:39:46 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:39:46,937 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:39:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:39:47,104 main INFO screen ! pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 09:40:13 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:40:13,752 main INFO screen LMAO pass=0 dev=1.03 ins=0.0 pro=1 1a=False 1b=False 2=False (2.8s)
Sep 11 09:41:07 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:07,442 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:41:07 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:07,542 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:41:07 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:07,734 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 09:41:13 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:13,380 main INFO screen ! pass=0 dev=0.32 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 11 09:41:20 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:20,283 main INFO screen Wolf pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.4s)
Sep 11 09:41:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:35,423 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:41:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:35,501 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:41:35 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:41:35,719 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 09:42:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:42:43,717 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:42:43 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:42:43,821 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:42:44 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:42:44,009 main INFO screen VON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 11 09:43:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:43:47,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 09:43:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:43:47,740 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 09:43:47 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:43:47,971 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 11 09:43:50 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:43:50,502 main INFO screen Uhhh pass=0 dev=0.42 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 09:43:58 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:43:58,836 main INFO screen ch pass=0 dev=2.16 ins=0.0 pro=3 1a=False 1b=False 2=False (2.3s)
Sep 11 09:44:19 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:44:19,334 main INFO screen cap pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 09:44:37 ubuntu-4gb-fsn1-1 python[29210]: 2026-09-11 09:44:37,153 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:09:44:37 +0000] "GET /health HTTP/1.1" 200 443 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T08:26:04Z
--- update 2026-09-11T08:31:36Z
--- update 2026-09-11T08:36:38Z
--- update 2026-09-11T08:42:29Z
--- update 2026-09-11T08:47:35Z
nieuwe code: 3e65967
install klaar
--- update 2026-09-11T08:52:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 277361cb46e7428ca1de36d4214ea43b
wallet-analyse gestart (e04fe8bd5728)
--- update 2026-09-11T08:57:39Z
--- update 2026-09-11T09:02:40Z
--- update 2026-09-11T09:07:58Z
--- update 2026-09-11T09:13:03Z
--- update 2026-09-11T09:18:36Z
--- update 2026-09-11T09:23:40Z
--- update 2026-09-11T09:29:10Z
--- update 2026-09-11T09:34:22Z
--- update 2026-09-11T09:39:34Z
--- update 2026-09-11T09:44:36Z
```

## Wallet-analyse (laatste 15 regels)
```
inactive
08:52:36 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 08:52 UTC
08:52:36 24905 tokens geladen
08:52:43   2000 tokens, 587636 trades, 196383 posities (6s)
08:52:47 posities: 352960 uit 1045578 trades (11s)
08:52:52 79415 wallets gerekend
08:52:53 geluk-toets
08:53:06 persistentie
08:53:07 kopieer-simulatie
08:53:11 klaar in 34s -> /opt/schaduwbot/reports/wallets.md
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
