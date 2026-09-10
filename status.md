# Schaduwbot status

- tijd: 2026-09-10 21:27:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 7 hours, 40 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 635/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 27560, "tokens_in_memory": 1582, "msgs": 5591647, "trades": 1016000, "creates": 11302, "decode_fail": 79422, "rpc_calls": 16914, "rpc_errors": 1721, "sol_usd": 99.94706803009828, "open_positions": 90}
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
Sep 10 21:18:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:32,136 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:18:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:32,382 main INFO screen GORK pass=0 dev=0.0 ins=25.24 pro=31 1a=False 1b=False 2=True (6.6s)
Sep 10 21:18:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:38,162 main INFO screen CUM pass=0 dev=0.27 ins=0.0 pro=4 1a=False 1b=False 2=False (7.7s)
Sep 10 21:18:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:39,157 main INFO screen MEME pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (8.2s)
Sep 10 21:18:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:55,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:18:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:18:55,183 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:00,135 main INFO screen FUD pass=0 dev=0.0 ins=20.84 pro=5 1a=False 1b=False 2=True (5.2s)
Sep 10 21:19:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:01,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:19:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:02,094 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:06,129 main INFO screen $NOT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.2s)
Sep 10 21:19:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:15,978 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:19:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:16,220 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:16,520 main INFO screen PUMPZI  pass=0 dev=0.0 ins=4.45 pro=32 1a=False 1b=False 2=True (0.8s)
Sep 10 21:19:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:21,616 main INFO screen x10 pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (8.2s)
Sep 10 21:19:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:22,339 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:19:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:22,456 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:27,906 main INFO screen SPNE pass=0 dev=0.0 ins=16.78 pro=4 1a=False 1b=False 2=True (5.6s)
Sep 10 21:19:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:34,713 main INFO screen HOLYCAT pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (9.1s)
Sep 10 21:19:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:52,754 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 10 21:19:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:54,268 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:19:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:54,430 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:54,590 main INFO screen Pumpzi pass=0 dev=0.0 ins=23.97 pro=11 1a=False 1b=False 2=True (0.4s)
Sep 10 21:19:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:55,062 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:19:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:55,816 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:19:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:19:59,992 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:20:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:00,102 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:20:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:00,200 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 10 21:20:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:02,499 main INFO screen MIGOS pass=1 dev=0.0 ins=19.41 pro=19 1a=False 1b=False 2=False (7.9s)
Sep 10 21:20:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:04,205 main INFO screen RST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 21:20:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:16,310 main INFO screen wifpump pass=0 dev=0.0 ins=23.58 pro=67 1a=False 1b=False 2=True (4.0s)
Sep 10 21:20:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:19,085 main INFO screen Pumpcat pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.5s)
Sep 10 21:20:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:33,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:20:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:33,884 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:20:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:38,891 main INFO screen $CAJUN pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 10 21:20:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:40,948 main INFO screen Bob pass=0 dev=0.0 ins=19.99 pro=5 1a=False 1b=False 2=True (7.3s)
Sep 10 21:20:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:57,974 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:20:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:20:58,031 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:21:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:01,519 main INFO screen ats pass=0 dev=0.0 ins=42.04 pro=11 1a=False 1b=False 2=True (3.6s)
Sep 10 21:21:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:07,527 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:21:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:07,651 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:21:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:11,215 main INFO screen MOONBOI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.8s)
Sep 10 21:21:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:27,773 main INFO screen X10 pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (10.2s)
Sep 10 21:21:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:21:36,848 main INFO screen MSFT pass=0 dev=3.01 ins=19.95 pro=38 1a=False 1b=False 2=True (8.8s)
Sep 10 21:22:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:22:26,694 main INFO screen $DEMP pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (6.4s)
Sep 10 21:22:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:22:27,024 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:22:27 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 21:23:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:13,859 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:23:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:13,957 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:23:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:18,051 main INFO screen SOLFROG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 21:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:19,640 main INFO screen att pass=0 dev=3.39 ins=0.0 pro=2 1a=False 1b=False 2=False (4.9s)
Sep 10 21:23:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:31,218 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:23:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:31,284 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:23:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:31,601 main INFO screen AIO pass=0 dev=0.0 ins=16.05 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 10 21:23:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:42,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:23:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:23:43,033 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
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
