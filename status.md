# Schaduwbot status

- tijd: 2026-09-11 16:08:55 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 2 hours, 21 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.6G/38G | geheugen: 779/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 22751, "tokens_in_memory": 6422, "msgs": 2597068, "trades": 596223, "creates": 6699, "decode_fail": 47412, "rpc_calls": 10517, "rpc_errors": 1004, "sol_usd": 102.09042113451937, "open_positions": 77, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 15:49 UTC

Gelogde schaduwtrades: **25464**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 17033 | 2392 | 26 | 2392 | 164 | 4446 | 13109 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 286 | 16% | 1.7% | +41.5% | -16.2% | -7.10% | 99% |
| dip35_V1_gescreend_fail | 2573 | 26% | 3.8% | +45.5% | -25.9% | -7.06% | 100% |
| dip35_V1_alle | 2946 | 26% | 3.9% | +44.5% | -25.2% | -7.35% | 100% |
| dip35_V2_gescreend_pass | 283 | 18% | 2.5% | +41.9% | -21.2% | -9.84% | 100% |
| dip35_V2_gescreend_fail | 2575 | 24% | 4.5% | +55.4% | -28.3% | -7.79% | 100% |
| dip35_V2_alle | 2922 | 24% | 4.6% | +53.8% | -27.9% | -8.42% | 100% |
| dip35_V3_gescreend_pass | 286 | 7% | 2.4% | +133.4% | -22.6% | -11.70% | 100% |
| dip35_V3_gescreend_fail | 2612 | 13% | 6.2% | +107.3% | -29.9% | -11.70% | 100% |
| dip35_V3_alle | 2957 | 13% | 6.1% | +106.0% | -29.4% | -12.12% | 100% |
| dip40_V1_gescreend_pass | 262 | 14% | 1.5% | +42.7% | -15.4% | -7.46% | 99% |
| dip40_V1_gescreend_fail | 2502 | 26% | 3.8% | +47.9% | -25.9% | -6.60% | 100% |
| dip40_V1_alle | 2829 | 25% | 3.8% | +47.1% | -25.1% | -6.93% | 100% |
| dip40_V2_gescreend_pass | 260 | 14% | 2.3% | +50.8% | -20.0% | -10.47% | 100% |
| dip40_V2_gescreend_fail | 2497 | 25% | 4.2% | +55.0% | -28.1% | -7.64% | 100% |
| dip40_V2_alle | 2804 | 24% | 4.3% | +54.4% | -27.6% | -8.31% | 100% |
| dip40_V3_gescreend_pass | 263 | 6% | 2.3% | +112.1% | -21.4% | -13.74% | 100% |
| dip40_V3_gescreend_fail | 2534 | 13% | 5.8% | +96.5% | -29.6% | -13.33% | 100% |
| dip40_V3_alle | 2840 | 12% | 5.7% | +95.7% | -29.0% | -13.74% | 100% |
| dip45_V1_gescreend_pass | 251 | 14% | 1.6% | +48.9% | -15.4% | -6.18% | 98% |
| dip45_V1_gescreend_fail | 2431 | 27% | 3.3% | +49.6% | -25.5% | -5.06% | 100% |
| dip45_V1_alle | 2730 | 26% | 3.4% | +49.2% | -24.7% | -5.44% | 100% |
| dip45_V2_gescreend_pass | 248 | 18% | 2.4% | +50.0% | -19.7% | -7.32% | 99% |
| dip45_V2_gescreend_fail | 2416 | 25% | 3.7% | +58.7% | -27.6% | -6.05% | 100% |
| dip45_V2_alle | 2702 | 24% | 3.8% | +57.8% | -27.1% | -6.54% | 100% |
| dip45_V3_gescreend_pass | 251 | 6% | 2.4% | +180.2% | -20.6% | -7.80% | 100% |
| dip45_V3_gescreend_fail | 2449 | 14% | 5.5% | +109.6% | -29.2% | -10.05% | 100% |
| dip45_V3_alle | 2734 | 13% | 5.4% | +111.4% | -28.5% | -10.19% | 100% |

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
| met_xlink | 1931 | 12% | 2.6% | -9.83% | 100% |
| zonder_xlink | 459 | 13% | 0.0% | -6.08% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 16:03:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:08,713 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (10.1s)
Sep 11 16:03:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:09,411 main INFO screen FERSPE pass=0 dev=5.17 ins=0.0 pro=2 1a=False 1b=False 2=False (8.4s)
Sep 11 16:03:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:31,046 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:03:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:31,095 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:03:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:37,299 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:03:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 16:03:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:38,445 main INFO screen Enteras pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.5s)
Sep 11 16:03:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:43,755 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:03:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:43,879 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:03:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:47,558 main INFO screen PONEMBER pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (3.9s)
Sep 11 16:03:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:54,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:03:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:03:55,561 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:04:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:00,106 main INFO screen leptonyx pass=0 dev=0.0 ins=7.62 pro=17 1a=False 1b=False 2=True (5.9s)
Sep 11 16:04:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:03,903 main INFO screen SCRVAN pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (10.5s)
Sep 11 16:04:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:12,779 main INFO screen leptonyx pass=0 dev=0.0 ins=20.62 pro=18 1a=False 1b=False 2=True (5.4s)
Sep 11 16:04:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:31,340 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:04:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:31,433 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:04:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:38,512 main INFO screen TNT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.3s)
Sep 11 16:04:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:40,019 main INFO screen DOOROC pass=0 dev=0.53 ins=0.0 pro=6 1a=False 1b=False 2=False (8.3s)
Sep 11 16:04:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:04:47,975 main INFO screen wing pass=0 dev=0.0 ins=13.28 pro=34 1a=False 1b=False 2=True (3.4s)
Sep 11 16:05:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:05,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:05:05 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:05,221 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:05:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:08,183 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:05:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:08,265 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:05:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:09,890 main INFO screen fihdih pass=0 dev=0.0 ins=20.11 pro=7 1a=False 1b=False 2=True (4.9s)
Sep 11 16:05:10 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:10,997 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:05:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:11,161 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:05:11 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:11,463 main INFO screen WHITEHORSE pass=0 dev=0.0 ins=24.12 pro=35 1a=False 1b=False 2=True (0.5s)
Sep 11 16:05:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:12,254 main INFO screen BLabs pass=1 dev=0.0 ins=3.19 pro=27 1a=False 1b=False 2=False (4.1s)
Sep 11 16:05:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:22,118 main INFO screen ASSwich pass=0 dev=1.74 ins=0.0 pro=4 1a=False 1b=False 2=False (7.3s)
Sep 11 16:05:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:44,968 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:05:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:45,042 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:05:49 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:49,950 main INFO screen stocklana pass=0 dev=0.0 ins=0.35 pro=2 1a=False 1b=False 2=False (5.1s)
Sep 11 16:05:53 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:05:53,705 main INFO screen SCAMTYOU pass=1 dev=0.53 ins=9.09 pro=35 1a=False 1b=False 2=False (3.4s)
Sep 11 16:06:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:01,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:06:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:01,413 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:06:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:01,565 main INFO screen Honohon pass=0 dev=0.0 ins=21.32 pro=18 1a=False 1b=False 2=True (0.3s)
Sep 11 16:06:19 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:19,111 main INFO screen SCAMTYOU pass=1 dev=3.9 ins=0.93 pro=54 1a=False 1b=False 2=False (7.3s)
Sep 11 16:06:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:20,776 main INFO screen kittylick pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.6s)
Sep 11 16:06:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:31,732 main INFO screen tst pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (3.6s)
Sep 11 16:06:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:40,453 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:06:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:40,577 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:06:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:06:44,300 main INFO screen Coca Cola pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.9s)
Sep 11 16:07:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:04,740 main INFO screen Honohon pass=0 dev=0.0 ins=20.03 pro=22 1a=False 1b=False 2=False (1.8s)
Sep 11 16:07:14 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:14,027 main INFO screen stocklana pass=0 dev=0.46 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 11 16:07:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:16,185 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:16,689 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:23,156 main INFO screen $CAJUN pass=0 dev=0.86 ins=0.35 pro=1 1a=False 1b=False 2=False (7.4s)
Sep 11 16:07:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:24,016 main INFO screen 99cBUTTS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (8.1s)
Sep 11 16:07:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:26,944 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:27,167 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:30,993 main INFO screen Olaf pass=0 dev=0.0 ins=4.45 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 11 16:07:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:31,964 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.8s)
Sep 11 16:07:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:34,206 main INFO screen BBC pass=0 dev=15.36 ins=3.06 pro=56 1a=False 1b=False 2=False (11.4s)
Sep 11 16:07:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:40,732 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:40 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:40,866 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:41 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:41,025 main INFO screen baton pass=0 dev=0.0 ins=23.06 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 16:07:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:42,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:42,137 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:43,013 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:43 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:43,150 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:46,273 main INFO screen BAH pass=0 dev=0.0 ins=13.21 pro=4 1a=False 1b=False 2=True (3.3s)
Sep 11 16:07:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:47,365 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:07:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:47,492 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:07:47 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:47,775 main INFO screen HOLD pass=0 dev=0.0 ins=26.6 pro=11 1a=False 1b=False 2=True (0.5s)
Sep 11 16:07:48 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:07:48,987 main INFO screen BBC pass=0 dev=0.0 ins=1.39 pro=12 1a=False 1b=False 2=True (7.0s)
Sep 11 16:08:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:08,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:08:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:08,868 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:08:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:16,044 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:08:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:16,201 main INFO screen baton pass=0 dev=0.0 ins=8.91 pro=3 1a=False 1b=False 2=True (7.5s)
Sep 11 16:08:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:16,211 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:08:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:16,620 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:08:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:16,743 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:08:21 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:21,574 main INFO screen SNP500 pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=True (5.0s)
Sep 11 16:08:22 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:22,078 main INFO screen TRANSDAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.1s)
Sep 11 16:08:24 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:24,951 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:08:25 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:25,081 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:08:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:30,306 main INFO screen MoanikaL pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (5.4s)
Sep 11 16:08:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:50,912 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 16:08:50 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:50,999 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 16:08:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 16:08:55,643 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:16:08:55 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T14:39:34Z
--- update 2026-09-11T14:44:36Z
--- update 2026-09-11T14:49:38Z
--- update 2026-09-11T14:54:48Z
--- update 2026-09-11T15:00:22Z
--- update 2026-09-11T15:05:25Z
--- update 2026-09-11T15:10:36Z
--- update 2026-09-11T15:15:48Z
--- update 2026-09-11T15:21:20Z
--- update 2026-09-11T15:26:33Z
--- update 2026-09-11T15:31:36Z
--- update 2026-09-11T15:37:24Z
--- update 2026-09-11T15:42:36Z
--- update 2026-09-11T15:48:24Z
--- update 2026-09-11T15:53:29Z
--- update 2026-09-11T15:58:34Z
--- update 2026-09-11T16:03:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: bf2f0fbff9834af3ad8812a9ec61480b
analyses gestart (8213ec5e675e)
--- update 2026-09-11T16:08:54Z
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
