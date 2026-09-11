# Schaduwbot status

- tijd: 2026-09-11 08:36:39 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 49 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 561/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3462, "tokens_in_memory": 1232, "msgs": 293719, "trades": 80143, "creates": 1232, "decode_fail": 3535, "rpc_calls": 1621, "rpc_errors": 289, "sol_usd": 99.96597076489164, "open_positions": 77}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 07:38 UTC

Gelogde schaduwtrades: **19043**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 8436 | 1130 | 16 | 1130 | 92 | 2244 | 6688 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 235 | 15% | 1.7% | +41.5% | -16.3% | -7.70% | 98% |
| dip35_V1_gescreend_fail | 1894 | 26% | 3.9% | +45.9% | -26.1% | -7.12% | 100% |
| dip35_V1_alle | 2200 | 25% | 4.0% | +44.7% | -25.4% | -7.59% | 100% |
| dip35_V2_gescreend_pass | 236 | 17% | 2.1% | +40.5% | -21.0% | -10.29% | 100% |
| dip35_V2_gescreend_fail | 1905 | 24% | 4.7% | +54.6% | -28.4% | -8.36% | 100% |
| dip35_V2_alle | 2192 | 23% | 4.7% | +52.7% | -28.0% | -9.05% | 100% |
| dip35_V3_gescreend_pass | 236 | 7% | 2.5% | +141.2% | -23.0% | -11.87% | 100% |
| dip35_V3_gescreend_fail | 1921 | 13% | 6.5% | +115.1% | -30.3% | -11.67% | 100% |
| dip35_V3_alle | 2204 | 12% | 6.4% | +113.4% | -29.8% | -12.17% | 100% |
| dip40_V1_gescreend_pass | 219 | 13% | 1.8% | +44.2% | -15.8% | -8.17% | 98% |
| dip40_V1_gescreend_fail | 1847 | 26% | 3.8% | +47.8% | -26.0% | -6.58% | 100% |
| dip40_V1_alle | 2118 | 25% | 3.9% | +46.8% | -25.2% | -7.07% | 100% |
| dip40_V2_gescreend_pass | 220 | 13% | 1.8% | +50.8% | -19.8% | -10.49% | 100% |
| dip40_V2_gescreend_fail | 1853 | 25% | 4.3% | +55.0% | -28.2% | -7.59% | 100% |
| dip40_V2_alle | 2109 | 23% | 4.3% | +54.3% | -27.6% | -8.37% | 100% |
| dip40_V3_gescreend_pass | 220 | 6% | 2.3% | +116.7% | -21.7% | -13.51% | 100% |
| dip40_V3_gescreend_fail | 1868 | 13% | 6.0% | +104.2% | -30.0% | -12.94% | 100% |
| dip40_V3_alle | 2121 | 12% | 5.9% | +103.3% | -29.3% | -13.44% | 100% |
| dip45_V1_gescreend_pass | 208 | 15% | 1.9% | +50.6% | -15.6% | -5.74% | 95% |
| dip45_V1_gescreend_fail | 1793 | 28% | 3.3% | +49.7% | -25.6% | -4.68% | 100% |
| dip45_V1_alle | 2037 | 26% | 3.4% | +49.4% | -24.7% | -5.11% | 100% |
| dip45_V2_gescreend_pass | 208 | 19% | 2.4% | +51.3% | -19.5% | -6.20% | 97% |
| dip45_V2_gescreend_fail | 1791 | 26% | 3.8% | +59.1% | -27.6% | -5.54% | 100% |
| dip45_V2_alle | 2026 | 25% | 3.9% | +58.1% | -27.0% | -6.00% | 100% |
| dip45_V3_gescreend_pass | 208 | 7% | 2.9% | +198.9% | -20.8% | -6.03% | 99% |
| dip45_V3_gescreend_fail | 1804 | 14% | 5.8% | +113.1% | -29.4% | -10.12% | 100% |
| dip45_V3_alle | 2036 | 13% | 5.7% | +116.5% | -28.7% | -10.08% | 100% |

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
| met_xlink | 1594 | 12% | 2.7% | -9.88% | 100% |
| zonder_xlink | 396 | 14% | 0.0% | -5.28% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 08:26:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:32,494 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:32 +0000] "GET /lib/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:32,569 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:32 +0000] "GET /.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:34 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:34,995 main INFO screen POLYBOSS pass=0 dev=0.0 ins=12.85 pro=25 1a=False 1b=False 2=True (4.8s)
Sep 11 08:26:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:36,993 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:36 +0000] "GET /src/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:37,068 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:37 +0000] "GET /backend/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:37,645 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:37 +0000] "GET /dashboard/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:38,159 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:38 +0000] "GET /test/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:39,251 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:39 +0000] "GET /includes/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:39,835 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:26:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:39,958 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:26:45 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:45,721 main INFO screen as pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 11 08:26:48 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:48,022 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:48 +0000] "GET /build/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:51 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:51,119 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:51 +0000] "GET /dist/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:58,739 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:26:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:58,833 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:26:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:58,982 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:27:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:01,294 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:27:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:01,421 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:27:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:08,401 main INFO screen sdfasafd pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 11 08:27:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:09,742 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:27:09 +0000] "GET /dev/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:27:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:09,816 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:27:09 +0000] "GET /blog/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:27:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:09,890 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:27:09 +0000] "GET /application/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:27:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:23,013 main INFO screen cap pass=0 dev=0.09 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 11 08:27:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:24,654 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:27:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:24,781 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:27:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:28,461 main INFO screen asdasd pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 11 08:27:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:29,199 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:27:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:29,326 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:27:33 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:33,321 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (4.2s)
Sep 11 08:27:51 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:51,171 main INFO screen NEVERFORGET pass=0 dev=7.65 ins=0.0 pro=3 1a=False 1b=False 2=False (2.9s)
Sep 11 08:27:59 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:59,176 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:27:59 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:27:59,263 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:28:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:00,637 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:28:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:00,784 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,782 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:28:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:03,959 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:28:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:05,882 main INFO screen asdcdas pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.8s)
Sep 11 08:28:07 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:28:07,643 main INFO screen Fluf pass=0 dev=0.0 ins=5.35 pro=22 1a=False 1b=False 2=True (7.0s)
Sep 11 08:29:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:41,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:29:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:41,529 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:29:44 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:29:44,961 main INFO screen MIDAS pass=0 dev=0.0 ins=20.9 pro=28 1a=False 1b=False 2=True (3.6s)
Sep 11 08:30:10 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:10,211 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (6.1s)
Sep 11 08:30:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:36,639 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:36,743 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,254 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,380 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:37,559 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:30:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:43,853 main INFO screen WBC pass=0 dev=0.0 ins=79.26 pro=7 1a=False 1b=False 2=True (7.3s)
Sep 11 08:30:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:52,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:30:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:52,517 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:30:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:30:56,213 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 11 08:31:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:31:37,112 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:31:37 +0000] "GET /health HTTP/1.1" 200 421 "-" "Python-urllib/3.14"
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,625 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,695 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:06,891 main INFO screen LCOST pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,320 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,406 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:28,615 main INFO screen BARREL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,778 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:32:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:29,901 main INFO screen BBB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 08:32:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:32:42,943 main INFO screen Aphrodite pass=0 dev=0.26 ins=0.0 pro=6 1a=False 1b=False 2=False (3.1s)
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,210 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,314 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:33:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:33:02,518 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,035 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,146 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:34:15 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:15,324 main INFO screen wind pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:34:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:34:37,327 main INFO screen BBP pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 11 08:35:16 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:16,166 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,097 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,191 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:35:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:35:50,392 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:36:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:05,962 main INFO screen INCOGCAT pass=1 dev=0.0 ins=11.36 pro=24 1a=False 1b=False 2=False (3.5s)
Sep 11 08:36:06 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:06,107 main INFO screen KYC pass=0 dev=0.0 ins=11.25 pro=55 1a=False 1b=False 2=True (4.9s)
Sep 11 08:36:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:37,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:36:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:38,033 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:36:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:38,257 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:36:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:36:39,268 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:36:39 +0000] "GET /health HTTP/1.1" 200 421 "-" "Python-urllib/3.14"
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
