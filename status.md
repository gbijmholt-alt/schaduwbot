# Schaduwbot status

- tijd: 2026-09-12 07:30:52 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 17 hours, 43 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1144/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 42644, "tokens_in_memory": 5490, "msgs": 7434753, "trades": 1391702, "creates": 13219, "decode_fail": 65783, "rpc_calls": 46416, "rpc_errors": 1856, "sol_usd": 101.74493371590636, "open_positions": 35, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **42500**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 6729 | 1110 | 6 | 1110 | 84 | 1962 | 5944 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 491 | 16% | 2.0% | +44.1% | -16.6% | -6.70% | 100% |
| dip35_V1_gescreend_fail | 4011 | 27% | 3.8% | +45.4% | -25.8% | -6.59% | 100% |
| dip35_V1_alle | 4911 | 26% | 3.9% | +44.6% | -25.2% | -6.80% | 100% |
| dip35_V2_gescreend_pass | 487 | 22% | 2.9% | +43.1% | -21.0% | -7.14% | 100% |
| dip35_V2_gescreend_fail | 4050 | 25% | 4.3% | +56.3% | -27.9% | -6.84% | 100% |
| dip35_V2_alle | 4880 | 25% | 4.5% | +53.8% | -27.5% | -7.53% | 100% |
| dip35_V3_gescreend_pass | 489 | 9% | 3.3% | +297.3% | -22.4% | +5.07% | 100% |
| dip35_V3_gescreend_fail | 4127 | 14% | 5.9% | +115.8% | -29.6% | -9.94% | 100% |
| dip35_V3_alle | 4921 | 13% | 5.9% | +120.6% | -29.1% | -9.34% | 100% |
| dip40_V1_gescreend_pass | 461 | 14% | 2.2% | +46.7% | -15.9% | -6.80% | 100% |
| dip40_V1_gescreend_fail | 3942 | 26% | 3.7% | +47.1% | -25.7% | -6.50% | 100% |
| dip40_V1_alle | 4720 | 25% | 3.8% | +47.2% | -25.0% | -6.64% | 100% |
| dip40_V2_gescreend_pass | 458 | 18% | 2.6% | +46.2% | -19.8% | -8.13% | 100% |
| dip40_V2_gescreend_fail | 3960 | 25% | 4.2% | +55.9% | -27.8% | -6.89% | 100% |
| dip40_V2_alle | 4684 | 24% | 4.3% | +54.3% | -27.3% | -7.65% | 100% |
| dip40_V3_gescreend_pass | 461 | 8% | 2.8% | +294.2% | -21.1% | +3.52% | 100% |
| dip40_V3_gescreend_fail | 4031 | 13% | 5.7% | +112.9% | -29.4% | -10.57% | 100% |
| dip40_V3_alle | 4727 | 13% | 5.7% | +118.5% | -28.9% | -9.97% | 100% |
| dip45_V1_gescreend_pass | 443 | 15% | 2.0% | +48.7% | -15.8% | -6.02% | 100% |
| dip45_V1_gescreend_fail | 3858 | 27% | 3.3% | +48.3% | -25.4% | -5.20% | 100% |
| dip45_V1_alle | 4565 | 26% | 3.4% | +48.6% | -24.7% | -5.48% | 100% |
| dip45_V2_gescreend_pass | 439 | 19% | 2.5% | +43.7% | -19.7% | -7.60% | 100% |
| dip45_V2_gescreend_fail | 3867 | 25% | 3.9% | +58.6% | -27.4% | -5.64% | 100% |
| dip45_V2_alle | 4528 | 24% | 4.0% | +57.4% | -27.0% | -6.30% | 100% |
| dip45_V3_gescreend_pass | 442 | 8% | 2.5% | +352.6% | -20.5% | +7.34% | 100% |
| dip45_V3_gescreend_fail | 3926 | 14% | 5.4% | +117.7% | -29.0% | -8.41% | 100% |
| dip45_V3_alle | 4564 | 13% | 5.3% | +126.4% | -28.4% | -7.67% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.2%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 3235 | 13% | 3.3% | -10.11% | 100% |
| zonder_xlink | 936 | 18% | 0.0% | +21.82% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 07:10:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:10:38,696 main INFO screen GTA 6 Coin pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.0s)
Sep 12 07:10:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:10:53,369 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:10:53 +0000] "GET /admin/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:10:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:10:53,412 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:10:53 +0000] "GET /ssi.cgi/Login.htm HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:10,969 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:11:10 +0000] "GET /cgi-bin/authLogin.cgi HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:24,349 aiohttp.access INFO 185.226.197.63 [12/Sep/2026:07:11:24 +0000] "GET /Telerik.Web.UI.WebResource.axd?type=rau HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:34,505 aiohttp.access INFO 185.226.197.64 [12/Sep/2026:07:11:34 +0000] "GET /version HTTP/1.1" 404 174 "-" "kubectl/v1.12.0 (linux/amd64) kubernetes/0ed3388"
Sep 12 07:11:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:34,545 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:11:34 +0000] "GET / HTTP/1.1" 404 174 "-" "kubectl/v1.12.0 (linux/amd64) kubernetes/0ed3388"
Sep 12 07:11:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:34,630 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:11:34 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:43,035 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:11:43 +0000] "GET /console HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:54,190 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:11:54 +0000] "GET /owncloud/status.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:11:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:11:55,843 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:12:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:03,965 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:12:03 +0000] "GET /status.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:09,208 main INFO screen iCoin pass=0 dev=19.75 ins=1.0 pro=43 1a=False 1b=False 2=False (13.5s)
Sep 12 07:12:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:13,264 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:12:13 +0000] "GET /zabbix/favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:28,317 aiohttp.access INFO 185.226.197.64 [12/Sep/2026:07:12:28 +0000] "GET /css/images/PTZOptics_powerby.png HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:28,405 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:12:28 +0000] "GET /api/session/properties HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:28,783 main INFO screen TRANSDAD pass=0 dev=0.22 ins=0.0 pro=3 1a=False 1b=False 2=False (6.9s)
Sep 12 07:12:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:42,524 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:12:42 +0000] "GET /favicon.ico HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:42,556 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:12:42 +0000] "GET /login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:12:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:12:51,907 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:12:51 +0000] "GET /jasperserver/login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:13:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:13:00,199 aiohttp.access INFO 185.226.197.62 [12/Sep/2026:07:13:00 +0000] "GET /jasperserver-pro/login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:13:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:13:12,367 aiohttp.access INFO 185.226.197.65 [12/Sep/2026:07:13:12 +0000] "GET /jasperserverTest/login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:13:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:13:21,623 aiohttp.access INFO 185.226.197.64 [12/Sep/2026:07:13:21 +0000] "GET /partymgr/control/main HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
Sep 12 07:13:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:13:22,363 main INFO screen CASH pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 12 07:13:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:13:24,316 main INFO screen APPLECAT pass=0 dev=0.51 ins=0.0 pro=3 1a=False 1b=False 2=False (7.6s)
Sep 12 07:14:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:07,102 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:14:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:12,173 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:14:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:29,260 main INFO screen shizuku pass=1 dev=0.0 ins=0.0 pro=32 1a=False 1b=False 2=False (6.1s)
Sep 12 07:14:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:35,290 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=True (10.8s)
Sep 12 07:14:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:36,525 main INFO screen Insider pass=0 dev=0.0 ins=39.74 pro=41 1a=False 1b=False 2=True (29.5s)
Sep 12 07:14:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:57,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:14:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:14:58,292 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:14:58 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:15:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:15:02,082 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:15:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:15:20,407 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.5s)
Sep 12 07:15:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:15:26,125 main INFO screen TTerminal pass=1 dev=0.0 ins=11.1 pro=39 1a=False 1b=False 2=False (9.9s)
Sep 12 07:16:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:16:05,529 main INFO screen Pepotamus pass=0 dev=0.71 ins=0.0 pro=4 1a=False 1b=False 2=False (10.1s)
Sep 12 07:16:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:16:25,651 main INFO screen crabcat pass=0 dev=0.0 ins=16.08 pro=27 1a=False 1b=False 2=True (7.3s)
Sep 12 07:16:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:16:49,436 main INFO screen Demunyan pass=0 dev=0.0 ins=16.57 pro=50 1a=False 1b=False 2=True (2.9s)
Sep 12 07:17:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:17:49,866 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:17:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:17:54,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:18:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:18:02,345 main INFO screen S&P pass=0 dev=0.0 ins=25.05 pro=33 1a=False 1b=False 2=True (3.3s)
Sep 12 07:18:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:18:16,216 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (26.4s)
Sep 12 07:18:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:18:33,813 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:18:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:18:38,849 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:18:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:18:57,919 main INFO screen jit pass=0 dev=0.0 ins=47.12 pro=39 1a=False 1b=True 2=True (24.2s)
Sep 12 07:19:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:19:41,869 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:19:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:19:48,462 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:19:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:19:49,517 main INFO screen GOYSLOP pass=0 dev=1.05 ins=17.14 pro=51 1a=False 1b=False 2=True (7.7s)
Sep 12 07:19:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:19:53,481 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:20:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:20:13,650 main INFO screen $Snoop pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.4s)
Sep 12 07:20:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:20:15,017 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:20:15 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 07:21:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:21:25,077 main INFO screen TRANSDAD pass=0 dev=0.1 ins=0.0 pro=2 1a=False 1b=False 2=False (5.8s)
Sep 12 07:21:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:21:42,389 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:07:21:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 07:22:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:22:27,004 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:22:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:22:39,700 main INFO screen Pepegger pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (12.8s)
Sep 12 07:23:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:46,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:23:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:52,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:23:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:23:56,660 main INFO screen TCAT pass=0 dev=1.0 ins=24.36 pro=63 1a=False 1b=False 2=True (3.8s)
Sep 12 07:24:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:09,548 main INFO screen TCAT pass=0 dev=0.0 ins=20.99 pro=25 1a=False 1b=False 2=False (22.7s)
Sep 12 07:24:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:27,519 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:32,607 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:43,817 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:24:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:52,146 main INFO screen GEMEOW pass=0 dev=0.18 ins=79.13 pro=7 1a=False 1b=True 2=True (24.7s)
Sep 12 07:24:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:24:57,413 main INFO screen PUMP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (13.7s)
Sep 12 07:25:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:25:37,153 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:25:37 +0000] "GET /health HTTP/1.1" 200 453 "-" "Python-urllib/3.14"
Sep 12 07:26:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:08,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:26:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:16,323 main INFO screen TCAT pass=0 dev=1.0 ins=17.15 pro=46 1a=False 1b=False 2=True (8.0s)
Sep 12 07:26:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:31,736 main INFO screen GPU pass=0 dev=0.0 ins=13.71 pro=27 1a=False 1b=False 2=True (9.0s)
Sep 12 07:26:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:47,144 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:26:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:26:59,942 main INFO screen MBST pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (12.9s)
Sep 12 07:27:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:27:30,981 main INFO screen OXYGEN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 12 07:28:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:28:58,604 main INFO screen JeJe pass=0 dev=0.24 ins=0.0 pro=3 1a=False 1b=False 2=False (9.0s)
Sep 12 07:29:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:29:24,036 main INFO screen Graduate pass=0 dev=0.25 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 07:30:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:01,971 main INFO screen INU pass=0 dev=0.0 ins=20.21 pro=59 1a=False 1b=False 2=True (3.2s)
Sep 12 07:30:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:33,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,081 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:38,750 main INFO screen PLINE pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (9.0s)
Sep 12 07:30:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:43,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:48,490 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 07:30:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 07:30:52,531 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:07:30:52 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: c28a94468726478892cb2c2291593995
analyses gestart (8746aefc73b4)
--- update 2026-09-12T06:03:40Z
--- update 2026-09-12T06:08:44Z
--- update 2026-09-12T06:13:49Z
--- update 2026-09-12T06:19:09Z
--- update 2026-09-12T06:24:26Z
--- update 2026-09-12T06:29:29Z
--- update 2026-09-12T06:34:34Z
--- update 2026-09-12T06:39:34Z
--- update 2026-09-12T06:44:35Z
--- update 2026-09-12T06:49:36Z
--- update 2026-09-12T06:54:39Z
--- update 2026-09-12T06:59:44Z
--- update 2026-09-12T07:04:47Z
--- update 2026-09-12T07:09:50Z
--- update 2026-09-12T07:14:57Z
--- update 2026-09-12T07:20:13Z
--- update 2026-09-12T07:25:36Z
--- update 2026-09-12T07:30:51Z
```

## Analyses (laatste 25 regels)
```
inactive
06:00:21 herkomst: 40 posities gekoppeld
06:00:24 klaar in 105s -> /opt/schaduwbot/reports/ledger.md
06:00:26   2000 nieuwe tokens doorgerekend
06:00:28 klaar in 4s: 15164 tokens, 2060 nieuw -> /opt/schaduwbot/reports/video_replay.md
06:00:28 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 06:00 UTC
06:00:28 49689 tokens geladen
06:00:31   2000 tokens, 246938 trades, 51841 posities (3s)
06:00:34   4000 tokens, 499800 trades, 105942 posities (5s)
06:00:36   6000 tokens, 751494 trades, 153475 posities (8s)
06:00:39   8000 tokens, 995808 trades, 202157 posities (11s)
06:00:42   10000 tokens, 1288195 trades, 264246 posities (14s)
06:00:44   12000 tokens, 1532978 trades, 311516 posities (16s)
06:00:47   14000 tokens, 1796554 trades, 361411 posities (19s)
06:00:49   16000 tokens, 2038896 trades, 410768 posities (21s)
06:00:53   18000 tokens, 2311003 trades, 467733 posities (25s)
06:00:56   20000 tokens, 2564416 trades, 517269 posities (27s)
06:00:59   22000 tokens, 2805731 trades, 565457 posities (30s)
06:01:01   24000 tokens, 3062477 trades, 617032 posities (33s)
06:01:04   26000 tokens, 3331606 trades, 674482 posities (36s)
06:01:06 posities: 714595 uit 3489207 trades (38s)
06:01:16 156866 wallets gerekend
06:01:17 geluk-toets
06:01:51 persistentie
06:01:53 kopieer-simulatie
06:02:09 klaar in 101s -> /opt/schaduwbot/reports/wallets.md
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
