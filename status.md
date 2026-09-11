# Schaduwbot status

- tijd: 2026-09-11 07:48:58 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 2 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 523/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 602, "tokens_in_memory": 194, "msgs": 49060, "trades": 10836, "creates": 194, "decode_fail": 407, "rpc_calls": 217, "rpc_errors": 52, "sol_usd": 99.76899359037812, "open_positions": 31}
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
Sep 11 07:40:57 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:40:57,908 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:40:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:40:58,033 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:40:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:40:58,617 main INFO screen 1000X pass=1 dev=0.0 ins=15.61 pro=41 1a=False 1b=False 2=False (0.8s)
Sep 11 07:41:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:42,818 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:41:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:42,915 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:41:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:43,111 main INFO screen 150k scrip pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.4s)
Sep 11 07:41:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:58,763 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:41:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:58,822 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:41:59 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:41:59,042 main INFO screen computer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:42:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:42:22,189 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:42:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:42:22,288 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:42:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:42:22,479 main INFO screen HEDGIE pass=0 dev=0.0 ins=9.18 pro=6 1a=False 1b=False 2=True (0.4s)
Sep 11 07:43:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:21,405 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:43:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:21,464 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:43:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:21,881 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 11 07:43:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:22,552 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:43:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:22,677 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:43:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:22,830 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 07:43:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:29,297 aiohttp.access INFO 16.5.0.236 [11/Sep/2026:07:43:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 11 07:43:33 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:33,816 main INFO screen DIDI2 pass=0 dev=20.3 ins=0.0 pro=11 1a=False 1b=False 2=False (3.9s)
Sep 11 07:43:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:43:58,831 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:43:58 +0000] "GET /health HTTP/1.1" 200 409 "-" "Python-urllib/3.14"
Sep 11 07:44:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:11,024 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:11,122 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:11 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:11,387 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 11 07:44:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:23,174 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:23,299 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:23,422 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 07:44:25 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:25,024 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:25 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:25,152 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:25 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:25,302 main INFO screen KIRKLADEN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 07:44:34 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:34,138 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:34 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:34,259 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:34 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:34,504 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:44:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:38,350 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:38,473 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:38 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:38,808 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.5s)
Sep 11 07:44:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:43,544 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:44:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:43,675 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:44:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:43,842 main INFO screen ZBULLISH pass=0 dev=0.0 ins=79.26 pro=8 1a=False 1b=False 2=True (0.4s)
Sep 11 07:44:48 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:44:48,741 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (3.1s)
Sep 11 07:45:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:03,852 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:45:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:03,994 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:45:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:04,180 main INFO screen KIRKLADEN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (0.4s)
Sep 11 07:45:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:23,261 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:45:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:23,363 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:45:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:23,564 main INFO screen Athena pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:45:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:29,572 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:45:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:29,669 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:45:29 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:29,798 main INFO screen KIRKLADEN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.3s)
Sep 11 07:45:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:45:36,865 main INFO screen FTK pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (2.3s)
Sep 11 07:46:12 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:46:12,689 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:46:12 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:46:12,943 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:46:13 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:46:13,641 main INFO screen ASD pass=0 dev=9.64 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 11 07:46:14 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:46:14,521 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.0s)
Sep 11 07:47:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:08,064 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:47:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:08,115 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:47:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:08,347 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 07:47:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:21,803 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:47:21 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:21,890 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:47:22 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:22,071 main INFO screen ass pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 11 07:47:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:41,870 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:47:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:41,930 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:47:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:47:42,158 main INFO screen ch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.4s)
Sep 11 07:48:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:02,714 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:48:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:02,774 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:48:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:03,004 main INFO screen JPM pass=0 dev=0.0 ins=21.86 pro=12 1a=False 1b=False 2=True (0.4s)
Sep 11 07:48:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:09,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:48:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:09,253 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:48:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:09,620 main INFO screen matsu pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 11 07:48:12 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:12,245 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:48:12 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:12,370 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:48:12 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:12,490 main INFO screen GINA NYC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 11 07:48:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:19,126 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:48:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:19,253 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:48:19 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:19,420 main INFO screen $1 pass=0 dev=0.0 ins=49.61 pro=18 1a=False 1b=False 2=True (0.3s)
Sep 11 07:48:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:24,186 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 07:48:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:24,313 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 07:48:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:24,464 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (0.3s)
Sep 11 07:48:26 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:26,563 main INFO screen matsu pass=0 dev=0.88 ins=0.0 pro=3 1a=False 1b=False 2=False (2.2s)
Sep 11 07:48:59 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 07:48:59,032 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:07:48:59 +0000] "GET /health HTTP/1.1" 200 414 "-" "Python-urllib/3.14"
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
