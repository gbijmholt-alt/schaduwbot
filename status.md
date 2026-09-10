# Schaduwbot status

- tijd: 2026-09-10 21:54:01 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 8 hours, 7 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 2.1G/38G | geheugen: 627/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 29144, "tokens_in_memory": 1646, "msgs": 5910134, "trades": 1089249, "creates": 12023, "decode_fail": 85138, "rpc_calls": 18141, "rpc_errors": 1835, "sol_usd": 99.8384261943561, "open_positions": 86}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 21:48 UTC

Gelogde schaduwtrades: **9333**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 11848 | 1695 | 28 | 1695 | 157 | 3131 | 9333 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 124 | 16% | 2.4% | +37.8% | -17.5% | -8.56% | 92% |
| dip35_V1_gescreend_fail | 929 | 27% | 4.5% | +46.5% | -26.2% | -6.89% | 100% |
| dip35_V1_alle | 1088 | 26% | 4.5% | +45.0% | -25.5% | -7.57% | 100% |
| dip35_V2_gescreend_pass | 123 | 18% | 3.3% | +30.6% | -22.5% | -13.03% | 97% |
| dip35_V2_gescreend_fail | 930 | 24% | 5.2% | +55.3% | -28.2% | -8.04% | 100% |
| dip35_V2_alle | 1080 | 23% | 5.2% | +52.3% | -27.9% | -9.20% | 100% |
| dip35_V3_gescreend_pass | 123 | 6% | 3.3% | +155.3% | -23.6% | -13.44% | 99% |
| dip35_V3_gescreend_fail | 940 | 12% | 6.6% | +133.0% | -30.0% | -10.61% | 100% |
| dip35_V3_alle | 1088 | 11% | 6.4% | +130.2% | -29.6% | -11.50% | 100% |
| dip40_V1_gescreend_pass | 112 | 15% | 2.7% | +43.8% | -16.4% | -7.26% | 87% |
| dip40_V1_gescreend_fail | 898 | 26% | 4.6% | +50.4% | -26.1% | -6.55% | 100% |
| dip40_V1_alle | 1038 | 25% | 4.4% | +49.1% | -25.2% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 111 | 14% | 2.7% | +47.2% | -21.1% | -11.23% | 94% |
| dip40_V2_gescreend_fail | 902 | 24% | 5.0% | +57.2% | -28.2% | -7.29% | 100% |
| dip40_V2_alle | 1032 | 23% | 4.8% | +55.8% | -27.6% | -8.12% | 100% |
| dip40_V3_gescreend_pass | 112 | 7% | 2.7% | +130.9% | -22.2% | -11.30% | 98% |
| dip40_V3_gescreend_fail | 915 | 12% | 6.3% | +116.0% | -29.8% | -12.74% | 100% |
| dip40_V3_alle | 1044 | 11% | 6.0% | +114.3% | -29.2% | -12.95% | 100% |
| dip45_V1_gescreend_pass | 101 | 13% | 4.0% | +45.5% | -16.6% | -8.60% | 90% |
| dip45_V1_gescreend_fail | 867 | 27% | 3.9% | +52.9% | -25.4% | -4.20% | 100% |
| dip45_V1_alle | 989 | 26% | 4.0% | +52.0% | -24.6% | -5.02% | 100% |
| dip45_V2_gescreend_pass | 100 | 17% | 4.0% | +42.1% | -20.3% | -9.67% | 90% |
| dip45_V2_gescreend_fail | 866 | 25% | 4.4% | +65.1% | -27.5% | -4.05% | 100% |
| dip45_V2_alle | 981 | 24% | 4.5% | +62.9% | -26.9% | -5.03% | 100% |
| dip45_V3_gescreend_pass | 101 | 7% | 4.0% | +185.1% | -21.1% | -6.79% | 96% |
| dip45_V3_gescreend_fail | 879 | 12% | 6.0% | +139.9% | -29.2% | -8.07% | 100% |
| dip45_V3_alle | 993 | 12% | 5.9% | +140.4% | -28.6% | -8.33% | 100% |

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
Sep 10 21:48:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:48:57,997 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:48:57 +0000] "GET /health HTTP/1.1" 200 429 "-" "Python-urllib/3.14"
Sep 10 21:49:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:03,867 main INFO screen MOONBOI pass=0 dev=0.01 ins=0.0 pro=3 1a=False 1b=False 2=False (5.9s)
Sep 10 21:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:04,045 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.8s)
Sep 10 21:49:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:04,304 main INFO screen vox pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (5.8s)
Sep 10 21:49:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:09,072 main INFO screen IRA pass=0 dev=0.0 ins=13.61 pro=53 1a=False 1b=False 2=True (5.2s)
Sep 10 21:49:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:39,461 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:49:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:39,532 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:49:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:39,957 main INFO screen RADIO pass=0 dev=0.0 ins=3.9 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 10 21:49:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:52,703 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:49:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:52,870 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:49:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:49:53,012 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:50:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:18,728 main INFO screen mmrich pass=0 dev=6.56 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 10 21:50:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:24,303 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:50:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:24,437 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:50:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:24,563 main INFO screen GME pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.3s)
Sep 10 21:50:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:46,152 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:50:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:46,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:50:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:50:46,450 main INFO screen Scratcher pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 21:51:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:15,245 main INFO screen MANA pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 10 21:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:22,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:51:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:22,970 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:51:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:23,108 main INFO screen FN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 21:51:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:25,535 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:51:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:25,693 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:51:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:25,876 main INFO screen Doogle pass=0 dev=0.0 ins=41.17 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 10 21:51:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:33,243 main INFO screen GTA6Coin pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 21:51:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:51:59,783 main INFO screen MEMEFACTORY pass=0 dev=0.39 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 21:52:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:05,972 main INFO screen CATE pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (1.8s)
Sep 10 21:52:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:10,815 main INFO screen BULLISH pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (3.5s)
Sep 10 21:52:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:26,631 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:26,890 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:27,089 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 10 21:52:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:27,486 main INFO screen anorchia pass=0 dev=0.0 ins=19.99 pro=57 1a=False 1b=False 2=True (3.2s)
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,260 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,348 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,513 main INFO screen HAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,682 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,824 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:39,931 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:43,228 main INFO screen DERP pass=0 dev=9.55 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 10 21:52:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:52,921 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:53,088 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:53,215 main INFO screen MEMEFACTORY pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,830 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 21:52:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:52:56,943 main INFO screen ELON pass=0 dev=0.0 ins=20.69 pro=7 1a=False 1b=False 2=True (0.3s)
Sep 10 21:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:11,602 main INFO screen BROKE pass=0 dev=0.3 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 10 21:53:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:28,262 main INFO screen DGCOIN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 10 21:53:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:29,586 main INFO screen Orlando pass=0 dev=0.0 ins=17.3 pro=13 1a=False 1b=False 2=True (2.1s)
Sep 10 21:53:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:53:39,162 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 21:54:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 21:54:01,098 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:21:54:01 +0000] "GET /health HTTP/1.1" 200 428 "-" "Python-urllib/3.14"
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
