# Schaduwbot status

- tijd: 2026-09-10 20:24:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 6 hours, 37 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 627/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 23780, "tokens_in_memory": 1574, "msgs": 4782742, "trades": 859547, "creates": 9620, "decode_fail": 65999, "rpc_calls": 14404, "rpc_errors": 1489, "sol_usd": 100.05537697582231, "open_positions": 132}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 19:48 UTC

Gelogde schaduwtrades: **6731**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 8656 | 1215 | 26 | 1215 | 123 | 2270 | 6731 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 101 | 13% | 1.0% | +34.6% | -15.7% | -9.22% | 86% |
| dip35_V1_gescreend_fail | 654 | 26% | 4.1% | +45.1% | -26.2% | -7.75% | 100% |
| dip35_V1_alle | 784 | 24% | 4.0% | +43.3% | -25.2% | -8.48% | 100% |
| dip35_V2_gescreend_pass | 100 | 15% | 1.0% | +31.0% | -20.6% | -12.85% | 94% |
| dip35_V2_gescreend_fail | 652 | 24% | 4.8% | +55.6% | -28.0% | -8.37% | 100% |
| dip35_V2_alle | 775 | 22% | 4.5% | +52.3% | -27.4% | -9.61% | 100% |
| dip35_V3_gescreend_pass | 101 | 5% | 1.0% | +75.2% | -22.2% | -17.36% | 98% |
| dip35_V3_gescreend_fail | 664 | 13% | 5.7% | +91.4% | -29.4% | -14.14% | 100% |
| dip35_V3_alle | 786 | 12% | 5.3% | +87.0% | -28.8% | -15.12% | 100% |
| dip40_V1_gescreend_pass | 92 | 15% | 1.1% | +43.2% | -14.3% | -5.54% | 73% |
| dip40_V1_gescreend_fail | 642 | 25% | 4.7% | +49.0% | -26.4% | -7.41% | 100% |
| dip40_V1_alle | 755 | 24% | 4.2% | +47.5% | -25.2% | -7.45% | 100% |
| dip40_V2_gescreend_pass | 91 | 13% | 1.1% | +54.4% | -19.6% | -9.88% | 88% |
| dip40_V2_gescreend_fail | 639 | 24% | 5.0% | +58.5% | -28.6% | -7.64% | 100% |
| dip40_V2_alle | 745 | 23% | 4.6% | +57.2% | -27.7% | -8.32% | 100% |
| dip40_V3_gescreend_pass | 92 | 8% | 1.1% | +57.1% | -21.1% | -15.15% | 95% |
| dip40_V3_gescreend_fail | 651 | 13% | 6.1% | +89.9% | -30.2% | -14.66% | 100% |
| dip40_V3_alle | 756 | 12% | 5.6% | +84.9% | -29.3% | -15.06% | 100% |
| dip45_V1_gescreend_pass | 82 | 15% | 2.4% | +44.4% | -14.8% | -6.12% | 76% |
| dip45_V1_gescreend_fail | 615 | 26% | 4.2% | +51.2% | -26.3% | -5.98% | 100% |
| dip45_V1_alle | 714 | 25% | 4.1% | +50.2% | -25.1% | -6.34% | 100% |
| dip45_V2_gescreend_pass | 81 | 18% | 2.5% | +42.8% | -18.6% | -7.27% | 79% |
| dip45_V2_gescreend_fail | 611 | 25% | 4.6% | +66.5% | -28.2% | -4.61% | 100% |
| dip45_V2_alle | 705 | 24% | 4.4% | +63.6% | -27.3% | -5.36% | 100% |
| dip45_V3_gescreend_pass | 82 | 7% | 2.4% | +108.1% | -19.8% | -10.41% | 91% |
| dip45_V3_gescreend_fail | 618 | 14% | 5.7% | +118.4% | -29.5% | -8.94% | 100% |
| dip45_V3_alle | 711 | 13% | 5.3% | +115.4% | -28.6% | -9.53% | 100% |

## Beste variant: dip45_V2_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 10 20:14:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:14:29,672 main INFO screen $Shit pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (3.9s)
Sep 10 20:14:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:14:50,289 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:14:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:14:50,386 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:14:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:14:54,380 main INFO screen BBM pass=0 dev=0.0 ins=22.48 pro=40 1a=False 1b=False 2=True (4.2s)
Sep 10 20:15:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:15:26,024 main INFO screen SCRVAN pass=0 dev=0.05 ins=0.0 pro=3 1a=False 1b=False 2=False (7.2s)
Sep 10 20:15:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:15:34,376 main INFO screen TEST pass=1 dev=0.0 ins=6.75 pro=34 1a=False 1b=False 2=False (7.8s)
Sep 10 20:15:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:15:59,547 main INFO screen BALD pass=0 dev=0.5 ins=0.0 pro=3 1a=False 1b=False 2=False (8.6s)
Sep 10 20:16:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:27,208 main INFO screen $CAT pass=0 dev=2.63 ins=0.0 pro=4 1a=False 1b=False 2=False (8.3s)
Sep 10 20:16:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:28,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:16:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:28,156 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:16:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:34,945 main INFO screen PAIR pass=0 dev=0.0 ins=33.15 pro=7 1a=False 1b=False 2=True (7.0s)
Sep 10 20:16:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:41,168 main INFO screen NVIDIA pass=1 dev=0.0 ins=0.4 pro=34 1a=False 1b=False 2=False (6.9s)
Sep 10 20:16:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:52,918 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:16:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:53,060 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:16:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:16:56,639 main INFO screen MUSKRAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 10 20:17:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:17:38,267 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:17:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:17:38,352 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:17:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:17:43,582 main INFO screen EGG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.4s)
Sep 10 20:18:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:01,707 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:18:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:05,001 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:18:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:05,122 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:18:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:07,084 main INFO screen TKIRK pass=0 dev=2.32 ins=0.0 pro=3 1a=False 1b=True 2=False (6.5s)
Sep 10 20:18:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:07,942 main INFO screen nirvana pass=0 dev=6.63 ins=17.68 pro=21 1a=False 1b=False 2=True (6.7s)
Sep 10 20:18:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:09,694 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.8s)
Sep 10 20:18:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:21,069 main INFO screen mycoin pass=0 dev=6.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.7s)
Sep 10 20:18:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:36,556 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 10 20:18:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:42,548 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:18:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:42,674 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:18:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:43,069 main INFO screen DIHVIDENDS pass=0 dev=0.0 ins=15.68 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 20:18:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:18:52,183 main INFO screen 00Marley  pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 10 20:19:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:19:36,594 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:19:36 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 20:19:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:19:39,220 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:19:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:19:39,383 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:19:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:19:42,020 main INFO screen FLOWERS pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.8s)
Sep 10 20:19:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:19:43,342 main INFO screen CryptoKitties pass=0 dev=0.0 ins=20.22 pro=12 1a=False 1b=False 2=True (4.2s)
Sep 10 20:20:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:30,345 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:20:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:30,446 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:20:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:30,858 main INFO screen NINJACAT pass=0 dev=0.0 ins=23.23 pro=9 1a=False 1b=False 2=True (0.6s)
Sep 10 20:20:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:50,958 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:20:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:51,625 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:20:58,176 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (10.3s)
Sep 10 20:21:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:05,117 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:21:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:05,201 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:21:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:10,497 main INFO screen STOCKDOG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 10 20:21:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:16,240 main INFO screen sol pass=0 dev=0.92 ins=0.0 pro=3 1a=False 1b=False 2=False (9.3s)
Sep 10 20:21:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:20,178 aiohttp.access INFO 189.18.97.61 [10/Sep/2026:20:21:20 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 10 20:21:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:33,895 main INFO screen HALH pass=0 dev=6.56 ins=0.0 pro=5 1a=False 1b=False 2=False (8.5s)
Sep 10 20:21:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:46,841 main INFO screen EGG pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 10 20:21:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:48,267 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:21:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:48,427 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:21:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:21:54,480 main INFO screen NASDUCK pass=0 dev=0.0 ins=6.75 pro=20 1a=False 1b=False 2=True (6.2s)
Sep 10 20:22:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:02,649 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:22:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:02,810 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:22:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:09,483 main INFO screen CATEPULT pass=0 dev=0.0 ins=38.38 pro=6 1a=False 1b=False 2=True (6.9s)
Sep 10 20:22:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:27,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:22:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:27,351 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:22:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:34,572 main INFO screen MOVEMENT pass=0 dev=0.0 ins=11.44 pro=14 1a=False 1b=False 2=True (7.4s)
Sep 10 20:22:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:37,859 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:22:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:37,984 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:22:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:44,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:22:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:44,925 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:22:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:45,060 main INFO screen CZBULL pass=0 dev=0.0 ins=78.49 pro=7 1a=False 1b=False 2=True (7.3s)
Sep 10 20:22:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:49,944 main INFO screen MOVEMENT pass=0 dev=0.0 ins=36.23 pro=8 1a=False 1b=False 2=True (5.2s)
Sep 10 20:22:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:22:58,927 main INFO screen $GOAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (8.9s)
Sep 10 20:23:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:10,394 main INFO screen MADS pass=0 dev=3.79 ins=0.0 pro=1 1a=False 1b=False 2=False (5.1s)
Sep 10 20:23:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:23,332 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:23:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:23,424 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:23:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:30,501 main INFO screen CATEPULT pass=0 dev=0.0 ins=38.23 pro=5 1a=False 1b=False 2=True (7.3s)
Sep 10 20:23:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:30,577 main INFO screen DIVIDEND pass=0 dev=6.63 ins=18.36 pro=26 1a=False 1b=False 2=True (5.3s)
Sep 10 20:23:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:32,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:23:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:33,142 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:23:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:23:39,939 main INFO screen BATON pass=0 dev=0.0 ins=25.12 pro=15 1a=False 1b=False 2=True (7.0s)
Sep 10 20:24:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:01,979 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:24:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:02,070 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:24:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:02,477 main INFO screen WAYLON pass=0 dev=0.0 ins=6.48 pro=13 1a=False 1b=False 2=True (0.6s)
Sep 10 20:24:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:11,847 main INFO screen SOLDOG pass=0 dev=0.24 ins=0.0 pro=3 1a=False 1b=False 2=False (6.6s)
Sep 10 20:24:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:27,780 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 20:24:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:27,865 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 20:24:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:32,085 main INFO screen WAYLON pass=0 dev=0.0 ins=35.98 pro=7 1a=False 1b=False 2=True (4.4s)
Sep 10 20:24:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 20:24:37,101 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:20:24:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
