# Schaduwbot status

- tijd: 2026-09-10 21:32:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 7 hours, 45 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 635/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 27872, "tokens_in_memory": 1572, "msgs": 5642733, "trades": 1028520, "creates": 11421, "decode_fail": 80780, "rpc_calls": 17157, "rpc_errors": 1747, "sol_usd": 99.93548687563872, "open_positions": 88}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 20:48 UTC

Gelogde schaduwtrades: **8017**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 10222 | 1462 | 27 | 1462 | 144 | 2707 | 8017 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 115 | 14% | 2.6% | +35.7% | -17.2% | -9.86% | 91% |
| dip35_V1_gescreend_fail | 790 | 26% | 4.4% | +46.2% | -26.1% | -6.97% | 100% |
| dip35_V1_alle | 936 | 25% | 4.4% | +44.5% | -25.3% | -7.78% | 100% |
| dip35_V2_gescreend_pass | 113 | 16% | 2.7% | +30.1% | -21.8% | -13.56% | 96% |
| dip35_V2_gescreend_fail | 789 | 24% | 5.2% | +53.7% | -28.3% | -8.52% | 100% |
| dip35_V2_alle | 925 | 23% | 5.1% | +50.8% | -27.8% | -9.69% | 100% |
| dip35_V3_gescreend_pass | 113 | 4% | 2.7% | +75.2% | -23.2% | -18.83% | 99% |
| dip35_V3_gescreend_fail | 803 | 12% | 6.2% | +112.2% | -29.8% | -12.66% | 100% |
| dip35_V3_alle | 937 | 11% | 6.0% | +106.5% | -29.3% | -13.91% | 100% |
| dip40_V1_gescreend_pass | 105 | 15% | 2.9% | +42.9% | -16.1% | -7.08% | 84% |
| dip40_V1_gescreend_fail | 767 | 26% | 4.8% | +50.5% | -26.3% | -6.59% | 100% |
| dip40_V1_alle | 896 | 25% | 4.6% | +48.9% | -25.2% | -6.87% | 100% |
| dip40_V2_gescreend_pass | 103 | 14% | 2.9% | +48.7% | -21.1% | -11.57% | 94% |
| dip40_V2_gescreend_fail | 768 | 25% | 5.3% | +55.6% | -28.6% | -7.91% | 100% |
| dip40_V2_alle | 886 | 23% | 5.1% | +54.4% | -27.9% | -8.67% | 100% |
| dip40_V3_gescreend_pass | 104 | 7% | 2.9% | +57.1% | -22.3% | -17.00% | 98% |
| dip40_V3_gescreend_fail | 783 | 12% | 6.5% | +94.2% | -30.0% | -15.28% | 100% |
| dip40_V3_alle | 900 | 11% | 6.1% | +89.2% | -29.3% | -15.76% | 100% |
| dip45_V1_gescreend_pass | 94 | 13% | 4.3% | +44.4% | -16.2% | -8.50% | 87% |
| dip45_V1_gescreend_fail | 735 | 27% | 4.2% | +52.6% | -25.7% | -4.52% | 100% |
| dip45_V1_alle | 848 | 26% | 4.2% | +51.7% | -24.8% | -5.29% | 100% |
| dip45_V2_gescreend_pass | 92 | 16% | 4.3% | +42.8% | -20.2% | -9.91% | 89% |
| dip45_V2_gescreend_fail | 732 | 25% | 4.8% | +65.2% | -27.9% | -4.63% | 100% |
| dip45_V2_alle | 837 | 24% | 4.8% | +62.9% | -27.2% | -5.58% | 100% |
| dip45_V3_gescreend_pass | 93 | 6% | 4.3% | +108.1% | -21.1% | -12.77% | 96% |
| dip45_V3_gescreend_fail | 748 | 13% | 6.1% | +120.1% | -29.4% | -10.17% | 100% |
| dip45_V3_alle | 852 | 12% | 6.0% | +117.3% | -28.6% | -10.80% | 100% |

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
Sep 10 21:23:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:48,855 main INFO screen OpenAI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 10 21:23:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:56,793 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (7.3s)
Sep 10 21:24:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:24:18,422 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:21:24:18 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 10 21:24:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:24:18,767 aiohttp.access INFO 150.107.36.82 [10/Sep/2026:21:24:18 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 10 21:24:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:24:24,636 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:24:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:24:24,738 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:24:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:24:30,208 main INFO screen MAYEM pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.7s)
Sep 10 21:25:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:20,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:25:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:20,899 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:25:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:26,388 main INFO screen Coca Cola pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.8s)
Sep 10 21:25:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:28,421 main INFO screen $WOLFGIGI pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.8s)
Sep 10 21:25:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:33,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:25:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:33,590 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:25:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:38,839 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 10 21:25:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:43,562 main INFO screen MAYEM pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.5s)
Sep 10 21:25:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:48,695 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:25:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:48,821 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:25:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:25:53,440 main INFO screen CHILLGUY pass=0 dev=0.0 ins=78.48 pro=5 1a=False 1b=False 2=True (4.8s)
Sep 10 21:26:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:26:01,235 aiohttp.access INFO 198.235.24.36 [10/Sep/2026:21:26:01 +0000] "GET / HTTP/1.0" 404 174 "-" "Hello from Palo Alto Networks, find out more about our scans in https://docs-cortex.paloaltonetworks.com/r/1/Cortex-Xpanse/Scanning-activity"
Sep 10 21:26:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:26:14,260 main INFO screen PORNHUB pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 10 21:27:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:11,998 main INFO screen Nono pass=0 dev=0.0 ins=17.95 pro=16 1a=False 1b=False 2=True (6.9s)
Sep 10 21:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:17,388 main INFO screen FERSPE pass=0 dev=6.94 ins=0.0 pro=4 1a=False 1b=False 2=False (7.4s)
Sep 10 21:27:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:19,716 main INFO screen TRUST pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.3s)
Sep 10 21:27:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:25,857 main INFO screen GodCat pass=0 dev=1.74 ins=0.0 pro=6 1a=False 1b=False 2=False (8.2s)
Sep 10 21:27:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:32,374 main INFO screen Lit pass=0 dev=0.0 ins=15.61 pro=60 1a=False 1b=False 2=True (9.3s)
Sep 10 21:27:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:37,116 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:27:37 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 21:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:41,508 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:27:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:41,646 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:27:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:45,586 main INFO screen BR1 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 21:27:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:27:54,840 aiohttp.access INFO 185.180.141.24 [10/Sep/2026:21:27:54 +0000] "GET /swagger.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 10 21:28:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:06,556 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:28:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:06,684 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:28:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:06,703 main INFO screen BROOCO pass=0 dev=6.35 ins=0.0 pro=6 1a=False 1b=False 2=False (2.9s)
Sep 10 21:28:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:06,865 main INFO screen BATon pass=0 dev=0.0 ins=11.25 pro=33 1a=False 1b=False 2=True (0.4s)
Sep 10 21:28:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:21,603 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:21:28:21 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 21:28:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:31,568 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:28:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:31,628 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:28:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:31,866 main INFO screen BUDDY pass=0 dev=0.0 ins=20.07 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 10 21:28:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:33,410 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:28:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:34,132 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:28:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:34,657 main INFO screen TONTON pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (1.6s)
Sep 10 21:28:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:28:35,304 main INFO screen TOAD pass=0 dev=6.94 ins=0.0 pro=3 1a=False 1b=False 2=False (3.0s)
Sep 10 21:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:19,365 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:19,504 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:19,713 main INFO screen chud pass=0 dev=0.0 ins=25.04 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 10 21:29:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:28,811 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:29:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:28,940 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:29:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:29,089 main INFO screen PSL500 pass=0 dev=0.0 ins=9.15 pro=26 1a=False 1b=False 2=True (0.3s)
Sep 10 21:29:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:35,538 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:29:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:35,697 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:29:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:35,830 main INFO screen PSL500 pass=0 dev=0.0 ins=11.48 pro=25 1a=False 1b=False 2=True (0.3s)
Sep 10 21:29:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:43,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:29:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:43,911 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:29:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:29:44,038 main INFO screen Up! pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 21:30:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:30:35,173 main INFO screen adv pass=0 dev=0.63 ins=0.0 pro=1 1a=False 1b=False 2=False (1.6s)
Sep 10 21:31:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:12,765 main INFO screen Broco pass=0 dev=3.35 ins=0.0 pro=3 1a=False 1b=False 2=False (3.5s)
Sep 10 21:31:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:13,875 main INFO screen PUMPZI pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 10 21:31:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:14,662 main INFO screen wind pass=0 dev=6.56 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 21:31:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:18,173 main INFO screen Eclipse  pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 10 21:31:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:26,039 main INFO screen WOZNIAK pass=0 dev=1.74 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 21:31:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:26,326 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:31:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:26,417 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:31:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:26,959 main INFO screen WOJUGG pass=0 dev=0.0 ins=78.96 pro=6 1a=False 1b=False 2=True (0.7s)
Sep 10 21:31:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:31:28,901 main INFO screen KALDIRMAK pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=True (1.7s)
Sep 10 21:32:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:12,703 main INFO screen AIO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.1s)
Sep 10 21:32:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:14,664 main INFO screen Sloth pass=0 dev=0.0 ins=35.0 pro=17 1a=False 1b=False 2=True (2.6s)
Sep 10 21:32:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:17,664 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:32:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:17,780 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:32:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:17,905 main INFO screen PUMPZI pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:32:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:32,252 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:32:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:32,373 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:32:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:32,671 main INFO screen ZODL pass=0 dev=0.0 ins=25.57 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 21:32:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:33,613 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:32:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:33,737 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:32:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:33,896 main INFO screen ZODL pass=0 dev=0.0 ins=20.42 pro=15 1a=False 1b=False 2=True (0.3s)
Sep 10 21:32:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:46,597 main INFO screen ZODL pass=0 dev=0.0 ins=21.01 pro=11 1a=False 1b=False 2=False (1.5s)
Sep 10 21:32:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:47,948 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:32:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:48,046 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:32:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:48,184 main INFO screen Singularity pass=0 dev=0.0 ins=12.18 pro=32 1a=False 1b=False 2=True (0.3s)
Sep 10 21:32:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:32:49,289 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:32:49 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
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
