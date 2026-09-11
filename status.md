# Schaduwbot status

- tijd: 2026-09-11 18:38:18 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 4 hours, 51 minutes
- bot-service: active
- code-versie: a16a395
- schijf: 2.8G/38G | geheugen: 584/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 0}
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
Sep 11 18:30:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:26,558 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:30:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:28,741 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:30:28 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:28,862 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:30:31 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:31,372 main INFO screen MSBD pass=0 dev=0.0 ins=19.86 pro=5 1a=False 1b=False 2=False (5.0s)
Sep 11 18:30:33 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:33,148 main INFO screen emberjak pass=0 dev=0.0 ins=79.27 pro=7 1a=False 1b=False 2=True (7.6s)
Sep 11 18:30:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:35,777 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.1s)
Sep 11 18:30:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:56,333 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:30:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:56,435 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:30:59 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:30:59,929 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:31:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:31:00,053 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:31:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:31:00,616 main INFO screen aninfly pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 11 18:31:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:31:02,113 main INFO screen Crypto pass=0 dev=0.0 ins=46.87 pro=14 1a=False 1b=False 2=True (2.3s)
Sep 11 18:31:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:31:04,567 main INFO screen BPCATE pass=0 dev=1.52 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 18:31:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:31:45,042 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 11 18:32:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:12,721 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:32:12 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:12,860 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:32:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:13,076 main INFO screen QUFIB pass=0 dev=0.0 ins=15.86 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 18:32:26 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:26,817 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 18:32:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:34,586 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 11 18:32:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:37,249 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:32:37 +0000] "GET /health HTTP/1.1" 200 451 "-" "Python-urllib/3.14"
Sep 11 18:32:37 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:37,780 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:32:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:38,027 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:32:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:38,293 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.7s)
Sep 11 18:32:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:39,643 main INFO screen att pass=0 dev=0.2 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 18:32:46 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:46,803 main INFO screen $CAJUN pass=0 dev=0.85 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 18:32:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:32:54,636 main INFO screen TME pass=0 dev=1.05 ins=0.0 pro=1 1a=False 1b=False 2=False (2.3s)
Sep 11 18:33:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:04,043 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:33:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:04,208 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:33:04 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:04,416 main INFO screen QUFIB pass=0 dev=0.0 ins=0.66 pro=20 1a=False 1b=False 2=True (0.4s)
Sep 11 18:33:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:08,185 main INFO screen emberj pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (3.1s)
Sep 11 18:33:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:16,212 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:33:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:16,375 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:33:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:16,541 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 18:33:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:23,195 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:33:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:23,326 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:33:23 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:23,469 main INFO screen GTA 6 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 18:33:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:29,582 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:33:29 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:29,710 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:33:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:33:35,393 main INFO screen gooner pass=0 dev=0.0 ins=48.08 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 18:34:27 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:27,983 main INFO screen Black pass=0 dev=0.47 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 18:34:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:35,479 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:34:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:35,972 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:34:36 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:36,490 main INFO screen $1 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (1.2s)
Sep 11 18:34:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:38,360 main INFO screen beer pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (4.0s)
Sep 11 18:34:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:38,642 main INFO screen ONCHAIN pass=0 dev=0.0 ins=24.09 pro=22 1a=False 1b=False 2=False (2.4s)
Sep 11 18:34:42 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:42,406 main INFO screen MINECAT pass=0 dev=0.22 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 11 18:34:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:45,875 main INFO screen STOCKLESS pass=1 dev=0.0 ins=18.65 pro=17 1a=False 1b=False 2=False (1.8s)
Sep 11 18:34:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:56,624 main INFO screen 9112001 pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (4.1s)
Sep 11 18:34:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:57,416 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:34:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:57,663 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:58,061 main INFO screen GROKER pass=0 dev=0.0 ins=46.41 pro=7 1a=False 1b=False 2=True (0.9s)
Sep 11 18:34:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:34:58,471 main INFO screen Bricko pass=0 dev=0.27 ins=0.0 pro=3 1a=False 1b=False 2=False (4.1s)
Sep 11 18:35:30 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:35:30,821 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (2.7s)
Sep 11 18:35:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:35:45,714 main INFO screen DPA⁠ pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (2.9s)
Sep 11 18:35:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:35:54,590 main INFO screen $REGRET pass=0 dev=3.42 ins=0.0 pro=2 1a=False 1b=False 2=False (2.2s)
Sep 11 18:36:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:36:39,616 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:36:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:36:39,708 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:36:39 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:36:39,907 main INFO screen BEPE pass=0 dev=0.0 ins=29.11 pro=16 1a=False 1b=False 2=True (0.4s)
Sep 11 18:36:44 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:36:44,138 main INFO screen MICROFLY pass=0 dev=0.0 ins=20.13 pro=14 1a=False 1b=False 2=False (1.6s)
Sep 11 18:37:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:09,535 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:37:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:09,637 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:37:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:09,833 main INFO screen APPLECAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 18:37:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:17,120 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:37:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:17,250 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:37:17 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:17,406 main INFO screen Macintosh pass=0 dev=0.0 ins=24.57 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 11 18:37:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:34,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:37:34 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:34,882 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:37:35 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:35,712 main INFO screen B pass=0 dev=0.0 ins=44.61 pro=2 1a=False 1b=False 2=True (1.0s)
Sep 11 18:37:45 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:37:45,128 main INFO screen SIXSEVEN pass=0 dev=0.91 ins=0.0 pro=3 1a=False 1b=False 2=False (2.6s)
Sep 11 18:38:00 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:38:00,922 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 18:38:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:38:01,015 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 18:38:01 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:38:01,427 main INFO screen NW pass=0 dev=0.0 ins=16.26 pro=29 1a=False 1b=False 2=True (0.6s)
Sep 11 18:38:13 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 18:38:13,556 main INFO screen $GOAT10 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.7s)
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 48min 5.317s CPU time over 8h 48min 33.144s wall clock time, 732.6M memory peak.
Sep 11 18:38:17 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 11 18:38:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:38:18,233 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 11 18:38:18 ubuntu-4gb-fsn1-1 python[41396]: 2026-09-11 18:38:18,343 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:18:38:18 +0000] "GET /health HTTP/1.1" 200 230 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-11T17:31:32Z
--- update 2026-09-11T17:36:36Z
--- update 2026-09-11T17:41:37Z
--- update 2026-09-11T17:46:37Z
--- update 2026-09-11T17:51:39Z
--- update 2026-09-11T17:56:40Z
--- update 2026-09-11T18:01:40Z
--- update 2026-09-11T18:06:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: f4240d03c1404a3aa0fe2959269b0656
analyses gestart (8213ec5e675e)
--- update 2026-09-11T18:11:40Z
--- update 2026-09-11T18:17:20Z
--- update 2026-09-11T18:22:26Z
--- update 2026-09-11T18:27:35Z
--- update 2026-09-11T18:32:36Z
--- update 2026-09-11T18:38:13Z
nieuwe code: a16a395
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: 1322d8308bda44ab89e4732e0436b52e
analyses gestart (ed3e144883fd)
```

## Analyses (laatste 25 regels)
```
active
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
18:06:41 10533 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
18:06:45   ingelezen tot rowid 1884078 (200000 rijen, 200000 bruikbaar)
18:06:47   ingelezen tot rowid 1995665 (311587 rijen, 311587 bruikbaar)
18:06:47 ingelezen: 311587 nieuwe trades, 311587 bruikbaar (6s)
18:06:58 820 aankopen van groeiers geëvalueerd
18:06:59 klaar in 18s -> /opt/schaduwbot/reports/ledger.md
18:07:01   2000 nieuwe tokens doorgerekend
18:07:02 klaar in 3s: 5471 tokens, 2456 nieuw -> /opt/schaduwbot/reports/video_replay.md
18:07:02 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 18:07 UTC
18:07:02 35379 tokens geladen
18:07:05   2000 tokens, 288862 trades, 71888 posities (3s)
18:07:08   4000 tokens, 576736 trades, 138871 posities (6s)
18:07:12   6000 tokens, 890562 trades, 213603 posities (9s)
18:07:14   8000 tokens, 1176630 trades, 283011 posities (12s)
18:07:18   10000 tokens, 1485942 trades, 359232 posities (16s)
18:07:21   12000 tokens, 1771256 trades, 428551 posities (19s)
18:07:24 posities: 488514 uit 1996386 trades (22s)
18:07:31 115882 wallets gerekend
18:07:31 geluk-toets
18:07:51 persistentie
18:07:53 kopieer-simulatie
18:08:00 klaar in 58s -> /opt/schaduwbot/reports/wallets.md
18:38:17 11258 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
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
