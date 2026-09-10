# Schaduwbot status

- tijd: 2026-09-10 21:48:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 8 hours, 1 minute
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 641/3814 MB

## Health
```json
(niet bereikbaar: timed out)
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
Sep 10 21:40:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:23,548 main INFO screen NUT pass=0 dev=0.0 ins=20.12 pro=70 1a=False 1b=False 2=True (3.3s)
Sep 10 21:40:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:47,622 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:40:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:47,680 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:40:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:47,906 main INFO screen Charlie pass=0 dev=0.0 ins=21.54 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 10 21:40:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:47,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:40:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:48,093 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:40:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:48,211 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 21:40:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:53,719 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:40:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:53,850 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:40:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:40:54,015 main INFO screen UPS pass=0 dev=0.0 ins=12.0 pro=26 1a=False 1b=False 2=True (0.3s)
Sep 10 21:41:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:41:33,631 main INFO screen monkdog pass=0 dev=1.64 ins=0.0 pro=2 1a=False 1b=False 2=False (3.8s)
Sep 10 21:41:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:41:35,079 main INFO screen INVESTOR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.3s)
Sep 10 21:42:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:01,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:42:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:01,734 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:42:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:01,963 main INFO screen MARIO pass=0 dev=0.0 ins=23.14 pro=24 1a=False 1b=False 2=True (0.4s)
Sep 10 21:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:16,023 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:16,150 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:42:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:16,328 main INFO screen MoonPepe pass=0 dev=0.0 ins=19.82 pro=10 1a=False 1b=False 2=True (0.3s)
Sep 10 21:42:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:23,498 main INFO screen $CAJUN pass=0 dev=0.55 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 21:42:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:41,361 main INFO screen drillcock pass=1 dev=0.0 ins=16.96 pro=22 1a=False 1b=False 2=False (1.7s)
Sep 10 21:42:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:46,973 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:42:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:47,098 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:42:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:47,221 main INFO screen Hirono pass=0 dev=0.0 ins=19.73 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 21:42:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:57,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:42:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:57,342 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:42:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:42:57,646 main INFO screen baton pass=0 dev=0.0 ins=13.08 pro=13 1a=False 1b=False 2=True (0.5s)
Sep 10 21:43:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:00,038 main INFO screen 5000 pass=0 dev=0.0 ins=0.18 pro=6 1a=True 1b=False 2=False (1.2s)
Sep 10 21:43:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:04,954 main INFO screen SELF pass=0 dev=0.87 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 21:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:12,404 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:12,498 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:43:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:12,680 main INFO screen SOLANAFROG pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 21:43:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:14,204 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:43:14 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 21:43:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:27,384 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:43:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:27,507 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:43:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:27,895 main INFO screen Dihvidends pass=0 dev=0.0 ins=12.8 pro=5 1a=False 1b=False 2=True (0.6s)
Sep 10 21:43:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:31,202 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (3.4s)
Sep 10 21:43:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:32,141 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:43:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:32,227 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:43:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:32,382 main INFO screen basket pass=0 dev=0.0 ins=12.5 pro=27 1a=False 1b=False 2=True (0.3s)
Sep 10 21:43:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:37,042 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:43:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:37,164 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:43:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:37,281 main INFO screen Joe pass=0 dev=0.0 ins=19.8 pro=8 1a=False 1b=False 2=True (0.3s)
Sep 10 21:43:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:49,401 main INFO screen $KITTY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.4s)
Sep 10 21:43:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:54,788 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:43:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:54,897 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:43:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:43:55,034 main INFO screen GOTHAM pass=1 dev=0.0 ins=6.17 pro=25 1a=False 1b=False 2=False (0.3s)
Sep 10 21:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:15,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:15,123 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:44:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:15,310 main INFO screen JUGJAK pass=0 dev=0.0 ins=79.17 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 21:44:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:26,329 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:44:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:26,457 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:44:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:26,579 main INFO screen SHIBANAUT pass=0 dev=0.0 ins=78.96 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 21:44:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:44:57,175 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 10 21:45:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:03,736 main INFO screen BULL pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 21:45:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:06,932 main INFO screen niga coin pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 10 21:45:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:27,907 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:28,036 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:28,225 main INFO screen DOCAT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 21:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:28,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:28,458 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:45:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:45:28,583 main INFO screen Callr pass=0 dev=0.0 ins=53.54 pro=13 1a=False 1b=False 2=True (0.3s)
Sep 10 21:46:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:04,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:46:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:04,431 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:46:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:04,623 main INFO screen SPSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 21:46:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:20,582 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:46:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:20,672 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:46:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:20,858 main INFO screen $PNK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 21:46:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:26,496 main INFO screen fraudster pass=0 dev=8.57 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 10 21:46:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:46:56,598 main INFO screen Moderatoor pass=0 dev=0.0 ins=16.14 pro=42 1a=False 1b=False 2=True (1.5s)
Sep 10 21:47:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:47:08,301 main INFO screen TOAD pass=0 dev=7.86 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 10 21:47:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:47:10,868 main INFO screen LEGS pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.4s)
Sep 10 21:47:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:47:29,278 main INFO screen AARON pass=0 dev=1.12 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 10 21:47:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:47:33,192 main INFO screen CADOG pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.0s)
Sep 10 21:47:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:47:53,992 main INFO screen 1 Meme pass=1 dev=0.0 ins=11.73 pro=22 1a=False 1b=False 2=False (1.5s)
Sep 10 21:48:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:00,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:48:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:00,749 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:48:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:01,080 main INFO screen IRA pass=1 dev=0.0 ins=15.54 pro=15 1a=False 1b=False 2=False (0.5s)
Sep 10 21:48:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:10,170 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:48:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:10,312 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:48:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:10,457 main INFO screen SOL pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
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
