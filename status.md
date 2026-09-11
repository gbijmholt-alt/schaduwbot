# Schaduwbot status

- tijd: 2026-09-11 06:31:15 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 16 hours, 44 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.3G/38G | geheugen: 646/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 60178, "tokens_in_memory": 998, "msgs": 10234956, "trades": 1988541, "creates": 22147, "decode_fail": 129294, "rpc_calls": 33616, "rpc_errors": 3215, "sol_usd": 99.66000193007997, "open_positions": 58}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 05:48 UTC

Gelogde schaduwtrades: **17399**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 6416 | 838 | 7 | 838 | 85 | 1679 | 5044 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 230 | 15% | 1.7% | +41.5% | -16.4% | -7.62% | 98% |
| dip35_V1_gescreend_fail | 1725 | 27% | 3.9% | +45.5% | -25.8% | -6.70% | 100% |
| dip35_V1_alle | 2015 | 26% | 4.0% | +44.4% | -25.0% | -7.17% | 100% |
| dip35_V2_gescreend_pass | 231 | 17% | 2.2% | +41.5% | -21.2% | -10.31% | 100% |
| dip35_V2_gescreend_fail | 1738 | 25% | 4.7% | +55.3% | -28.1% | -7.45% | 100% |
| dip35_V2_alle | 2010 | 24% | 4.6% | +53.5% | -27.6% | -8.26% | 100% |
| dip35_V3_gescreend_pass | 231 | 7% | 2.6% | +141.2% | -23.2% | -11.79% | 100% |
| dip35_V3_gescreend_fail | 1743 | 13% | 6.2% | +112.8% | -30.0% | -11.71% | 100% |
| dip35_V3_alle | 2013 | 12% | 6.0% | +111.9% | -29.4% | -12.15% | 100% |
| dip40_V1_gescreend_pass | 214 | 13% | 1.9% | +43.7% | -15.9% | -8.36% | 98% |
| dip40_V1_gescreend_fail | 1676 | 26% | 3.9% | +48.1% | -25.7% | -6.40% | 100% |
| dip40_V1_alle | 1935 | 25% | 3.8% | +47.0% | -24.8% | -6.85% | 100% |
| dip40_V2_gescreend_pass | 214 | 13% | 1.9% | +48.9% | -19.9% | -10.92% | 100% |
| dip40_V2_gescreend_fail | 1685 | 25% | 4.3% | +56.5% | -27.9% | -6.79% | 100% |
| dip40_V2_alle | 1928 | 24% | 4.2% | +55.5% | -27.1% | -7.67% | 100% |
| dip40_V3_gescreend_pass | 214 | 6% | 2.3% | +116.7% | -21.8% | -13.42% | 100% |
| dip40_V3_gescreend_fail | 1691 | 13% | 5.7% | +103.3% | -29.7% | -12.67% | 100% |
| dip40_V3_alle | 1932 | 12% | 5.5% | +102.4% | -29.0% | -13.11% | 100% |
| dip45_V1_gescreend_pass | 203 | 15% | 2.0% | +52.2% | -15.7% | -5.63% | 95% |
| dip45_V1_gescreend_fail | 1625 | 28% | 3.4% | +49.5% | -25.3% | -4.46% | 100% |
| dip45_V1_alle | 1858 | 26% | 3.4% | +49.4% | -24.3% | -4.83% | 100% |
| dip45_V2_gescreend_pass | 202 | 19% | 2.5% | +52.0% | -19.6% | -6.16% | 97% |
| dip45_V2_gescreend_fail | 1629 | 26% | 3.8% | +60.4% | -27.2% | -4.66% | 100% |
| dip45_V2_alle | 1852 | 25% | 3.8% | +59.4% | -26.5% | -5.16% | 100% |
| dip45_V3_gescreend_pass | 202 | 7% | 3.0% | +198.9% | -20.9% | -5.68% | 99% |
| dip45_V3_gescreend_fail | 1635 | 14% | 5.4% | +112.0% | -29.0% | -9.59% | 100% |
| dip45_V3_alle | 1856 | 13% | 5.3% | +115.7% | -28.3% | -9.48% | 100% |

## Beste variant: dip45_V1_gescreend_fail

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ❌
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%
```

## Bot-log (laatste 80 regels)
```
Sep 11 06:19:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:01,821 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:19:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:05,316 main INFO screen WEINERS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.7s)
Sep 11 06:19:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:12,460 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:19:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:12,600 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:19:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:16,378 main INFO screen asdfsasdf pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.0s)
Sep 11 06:19:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:19:32,046 aiohttp.access INFO 123.160.223.72 [11/Sep/2026:06:19:32 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
Sep 11 06:20:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:03,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:20:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:03,270 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:20:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:07,652 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.6s)
Sep 11 06:20:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:29,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:20:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:29,325 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:20:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:29,429 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:20:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:29,702 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:20:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:33,910 main INFO screen GG pass=0 dev=0.0 ins=22.19 pro=33 1a=False 1b=False 2=True (4.8s)
Sep 11 06:20:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:35,220 main INFO screen trash pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.9s)
Sep 11 06:20:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:48,841 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:20:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:48,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:20:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:50,024 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:20:50 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:20:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:20:53,246 main INFO screen sdfsdf pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.5s)
Sep 11 06:21:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:21:15,668 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:21:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:21:15,729 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:21:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:21:22,519 main INFO screen dsfggfsd pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.9s)
Sep 11 06:21:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:21:30,376 main INFO screen WEINERS pass=0 dev=1.49 ins=0.0 pro=2 1a=False 1b=False 2=False (7.3s)
Sep 11 06:21:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:21:36,646 main INFO screen EvilGrok pass=0 dev=23.02 ins=0.0 pro=48 1a=False 1b=False 2=False (7.7s)
Sep 11 06:22:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:22:13,288 main INFO screen trash pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (5.4s)
Sep 11 06:22:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:22:43,731 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:22:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:22:43,819 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:22:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:22:51,015 main INFO screen sdfsfd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.4s)
Sep 11 06:23:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:14,853 main INFO screen TOAD pass=0 dev=2.39 ins=0.0 pro=4 1a=False 1b=False 2=False (6.5s)
Sep 11 06:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:19,687 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:19,825 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:23:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:25,269 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.6s)
Sep 11 06:23:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:32,738 main INFO screen cumcoin pass=0 dev=0.0 ins=17.19 pro=70 1a=False 1b=False 2=True (7.2s)
Sep 11 06:23:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:42,278 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:23:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:42,460 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:23:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:23:46,582 main INFO screen $AURA pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.3s)
Sep 11 06:24:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:24:03,003 main INFO screen WEINERS pass=0 dev=1.34 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 11 06:24:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:24:24,433 main INFO screen trash pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 11 06:25:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:05,476 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:25:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:05,580 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:25:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:09,274 main INFO screen MONKEINU pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 11 06:25:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:20,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:25:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:21,082 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:25:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:22,618 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:25:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:22,817 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:25:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:27,027 main INFO screen NVIDOG pass=0 dev=0.0 ins=75.89 pro=1 1a=False 1b=False 2=True (6.1s)
Sep 11 06:25:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:28,426 main INFO screen EYE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.8s)
Sep 11 06:25:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:57,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:25:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:57,268 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:25:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:25:58,706 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:25:58 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
Sep 11 06:26:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:00,068 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:26:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:00,193 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:26:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:02,778 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.7s)
Sep 11 06:26:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:04,600 main INFO screen White pass=0 dev=0.0 ins=16.22 pro=10 1a=False 1b=False 2=True (4.6s)
Sep 11 06:26:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:17,179 main INFO screen sdfsdf pass=0 dev=33.04 ins=0.0 pro=9 1a=False 1b=False 2=False (8.5s)
Sep 11 06:26:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:26:42,036 main INFO screen BUTTERFLY pass=0 dev=0.0 ins=0.0 pro=64 1a=False 1b=False 2=True (2.6s)
Sep 11 06:27:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:27:43,635 main INFO screen LaMisery pass=0 dev=1.05 ins=0.0 pro=2 1a=False 1b=False 2=False (6.9s)
Sep 11 06:28:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:28:36,482 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:28:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:28:36,586 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:28:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:28:41,383 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=9 1a=False 1b=False 2=False (5.0s)
Sep 11 06:29:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:21,142 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:29:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:21,247 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:29:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:28,194 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.1s)
Sep 11 06:29:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:29,463 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:29:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:29,591 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:29:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:36,783 main INFO screen dsfgdsfg pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 11 06:29:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:59,501 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:29:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:29:59,563 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:30:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:04,508 main INFO screen sdfgsdfg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.1s)
Sep 11 06:30:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:23,834 main INFO screen SCRVAN pass=0 dev=0.28 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 11 06:30:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:35,178 main INFO screen HALH pass=0 dev=5.59 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 11 06:30:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:43,896 main INFO screen Fruitfly pass=0 dev=0.0 ins=23.69 pro=61 1a=False 1b=False 2=True (3.2s)
Sep 11 06:30:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:44,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:30:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:44,451 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:30:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:49,419 main INFO screen CMNY pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (5.2s)
Sep 11 06:30:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:56,934 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 06:30:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:30:57,264 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 06:31:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:31:02,335 main INFO screen CYBERLEEK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.6s)
Sep 11 06:31:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:31:05,173 main INFO screen ALICE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.3s)
Sep 11 06:31:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-11 06:31:15,161 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:06:31:15 +0000] "GET /health HTTP/1.1" 200 430 "-" "Python-urllib/3.14"
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
