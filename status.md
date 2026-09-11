# Schaduwbot status

- tijd: 2026-09-11 08:15:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 28 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 544/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2200, "tokens_in_memory": 799, "msgs": 187920, "trades": 49925, "creates": 799, "decode_fail": 1803, "rpc_calls": 1092, "rpc_errors": 186, "sol_usd": 99.49119339587753, "open_positions": 64}
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
Sep 11 08:07:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:04,096 main INFO screen Kirk11 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (4.5s)
Sep 11 08:07:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:04,130 main INFO screen gamble pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (3.6s)
Sep 11 08:07:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:32,113 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:07:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:32,169 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:07:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:37,735 main INFO screen gamble pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.7s)
Sep 11 08:07:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:39,301 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:07:39 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:39,388 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:07:43 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:07:43,806 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.6s)
Sep 11 08:08:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:08:03,950 main INFO screen gamble pass=0 dev=0.52 ins=0.0 pro=2 1a=False 1b=False 2=False (6.5s)
Sep 11 08:09:18 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:18,790 main INFO screen aa pass=0 dev=4.88 ins=0.0 pro=7 1a=False 1b=False 2=False (10.3s)
Sep 11 08:09:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:23,655 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:09:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:23,774 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:09:27 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:27,697 main INFO screen bulltober pass=0 dev=0.0 ins=12.85 pro=29 1a=False 1b=False 2=True (4.1s)
Sep 11 08:09:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:30,586 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:09:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:30,746 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:32,891 aiohttp.server ERROR Error handling request from 185.189.182.234
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]: Traceback (most recent call last):
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:   File "/opt/schaduwbot/.venv/lib/python3.14/site-packages/aiohttp/web_protocol.py", line 433, in data_received
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:     messages, upgraded, tail = self._parser.feed_data(data)
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:                                ~~~~~~~~~~~~~~~~~~~~~~^^^^^^
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:   File "aiohttp/_http_parser.pyx", line 687, in aiohttp._http_parser.HttpParser.feed_data
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:   File "aiohttp/_http_parser.pyx", line 879, in aiohttp._http_parser.cb_on_headers_complete
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:     pyparser._on_headers_complete()
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:   File "aiohttp/_http_parser.pyx", line 491, in aiohttp._http_parser.HttpParser._on_headers_complete
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:     raise BadHttpMessage("Missing 'Host' header in request.")
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]: aiohttp.http_exceptions.BadHttpMessage: 400, message:
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]:   Missing 'Host' header in request.
Sep 11 08:09:32 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:32,896 aiohttp.access INFO 185.189.182.234 [11/Sep/2026:08:09:32 +0000] "UNKNOWN / HTTP/1.0" 400 195 "-" "-"
Sep 11 08:09:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:09:36,419 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.9s)
Sep 11 08:10:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:00,082 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:10:00 +0000] "GET /health HTTP/1.1" 200 418 "-" "Python-urllib/3.14"
Sep 11 08:10:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:08,935 main INFO screen assa pass=0 dev=4.67 ins=0.0 pro=4 1a=False 1b=False 2=False (6.5s)
Sep 11 08:10:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:20,223 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:10:20 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:20,327 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:10:25 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:25,479 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.3s)
Sep 11 08:10:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:28,362 main INFO screen ASD pass=0 dev=11.24 ins=0.0 pro=2 1a=False 1b=False 2=False (2.6s)
Sep 11 08:10:31 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:31,207 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:10:31 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:31,333 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:10:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:10:37,861 main INFO screen fg pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (6.7s)
Sep 11 08:11:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:02,210 main INFO screen U23 pass=1 dev=0.0 ins=8.7 pro=33 1a=False 1b=False 2=False (3.7s)
Sep 11 08:11:17 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:17,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:11:17 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:17,942 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:11:25 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:25,121 main INFO screen OCTN pass=0 dev=0.0 ins=17.19 pro=9 1a=False 1b=False 2=True (7.4s)
Sep 11 08:11:48 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:48,248 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:11:48 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:48,345 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:11:48 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:11:48,526 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 11 08:12:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:04,777 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:12:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:04,920 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:12:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:09,540 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:12:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:09,668 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:12:09 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:09,928 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (5.2s)
Sep 11 08:12:14 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:14,206 main INFO screen CHILLTOWERS pass=0 dev=0.0 ins=30.52 pro=14 1a=False 1b=False 2=True (4.7s)
Sep 11 08:12:17 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:17,158 main INFO screen blackrock pass=0 dev=0.0 ins=21.27 pro=59 1a=False 1b=False 2=True (3.0s)
Sep 11 08:12:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:28,481 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:12:28 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:28,568 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:12:34 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:12:34,249 main INFO screen 22 pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (5.8s)
Sep 11 08:13:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:03,168 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:13:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:03,222 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:13:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:03,441 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (0.4s)
Sep 11 08:13:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:08,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:13:08 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:08,278 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:13:13 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:13,721 main INFO screen saas pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (5.6s)
Sep 11 08:13:23 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:23,763 main INFO screen GRADELESS pass=0 dev=0.05 ins=0.0 pro=2 1a=False 1b=False 2=False (5.9s)
Sep 11 08:13:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:36,322 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:13:36 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:36,427 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:13:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:13:42,136 main INFO screen 34% pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (5.9s)
Sep 11 08:14:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:03,594 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:14:03 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 11 08:14:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:03,941 aiohttp.access INFO 150.107.36.82 [11/Sep/2026:08:14:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 08:14:07 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:07,217 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:14:07 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:07,276 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:14:14 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:14,742 main INFO screen sddsds pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (7.6s)
Sep 11 08:14:35 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:35,002 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.4s)
Sep 11 08:14:41 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:41,086 main INFO screen LEPRECHAUN pass=0 dev=0.78 ins=0.0 pro=1 1a=False 1b=False 2=False (6.5s)
Sep 11 08:14:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:42,010 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:14:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:42,130 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:14:42 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:14:42,268 main INFO screen ASD pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (0.3s)
Sep 11 08:15:04 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:15:04,300 main INFO screen as pass=0 dev=22.73 ins=0.0 pro=3 1a=False 1b=False 2=False (10.2s)
Sep 11 08:15:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:15:24,597 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 08:15:24 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:15:24,694 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 08:15:30 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:15:30,216 main INFO screen RACCO pass=0 dev=0.0 ins=79.27 pro=8 1a=False 1b=False 2=True (5.7s)
Sep 11 08:15:37 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:15:37,079 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:15:37 +0000] "GET /health HTTP/1.1" 200 419 "-" "Python-urllib/3.14"
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
