# Schaduwbot status

- tijd: 2026-09-12 05:28:28 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 15 hours, 41 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1104/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 35300, "tokens_in_memory": 6514, "msgs": 6686275, "trades": 1209236, "creates": 11663, "decode_fail": 59588, "rpc_calls": 40871, "rpc_errors": 1655, "sol_usd": 101.50545049032655, "open_positions": 32, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **40946**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 5003 | 828 | 3 | 826 | 53 | 1440 | 4390 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 470 | 17% | 2.1% | +44.4% | -16.7% | -6.46% | 100% |
| dip35_V1_gescreend_fail | 3879 | 27% | 3.8% | +45.7% | -25.9% | -6.65% | 100% |
| dip35_V1_alle | 4734 | 26% | 3.9% | +45.0% | -25.2% | -6.77% | 100% |
| dip35_V2_gescreend_pass | 467 | 22% | 3.0% | +43.5% | -21.2% | -6.83% | 100% |
| dip35_V2_gescreend_fail | 3916 | 25% | 4.3% | +56.0% | -27.9% | -7.07% | 100% |
| dip35_V2_alle | 4703 | 24% | 4.5% | +53.6% | -27.6% | -7.67% | 100% |
| dip35_V3_gescreend_pass | 468 | 9% | 3.4% | +304.4% | -22.6% | +6.08% | 100% |
| dip35_V3_gescreend_fail | 3993 | 14% | 5.9% | +116.4% | -29.6% | -9.90% | 100% |
| dip35_V3_alle | 4746 | 13% | 5.9% | +122.0% | -29.2% | -9.15% | 100% |
| dip40_V1_gescreend_pass | 438 | 15% | 2.3% | +47.2% | -16.0% | -6.52% | 100% |
| dip40_V1_gescreend_fail | 3808 | 26% | 3.8% | +47.5% | -25.7% | -6.52% | 100% |
| dip40_V1_alle | 4545 | 25% | 3.8% | +47.6% | -25.0% | -6.54% | 100% |
| dip40_V2_gescreend_pass | 435 | 18% | 2.8% | +45.9% | -20.0% | -8.04% | 100% |
| dip40_V2_gescreend_fail | 3825 | 25% | 4.2% | +55.7% | -27.8% | -7.09% | 100% |
| dip40_V2_alle | 4508 | 24% | 4.4% | +54.1% | -27.3% | -7.74% | 100% |
| dip40_V3_gescreend_pass | 438 | 8% | 3.0% | +309.4% | -21.3% | +4.39% | 100% |
| dip40_V3_gescreend_fail | 3898 | 13% | 5.7% | +114.3% | -29.4% | -10.46% | 100% |
| dip40_V3_alle | 4555 | 13% | 5.7% | +120.5% | -28.9% | -9.74% | 100% |
| dip45_V1_gescreend_pass | 421 | 16% | 2.1% | +48.6% | -16.0% | -5.86% | 100% |
| dip45_V1_gescreend_fail | 3726 | 27% | 3.3% | +48.5% | -25.4% | -5.22% | 100% |
| dip45_V1_alle | 4396 | 26% | 3.4% | +48.7% | -24.8% | -5.51% | 100% |
| dip45_V2_gescreend_pass | 417 | 19% | 2.6% | +44.2% | -19.9% | -7.60% | 100% |
| dip45_V2_gescreend_fail | 3736 | 25% | 3.9% | +58.0% | -27.4% | -5.90% | 100% |
| dip45_V2_alle | 4360 | 24% | 4.0% | +56.2% | -27.0% | -6.73% | 100% |
| dip45_V3_gescreend_pass | 420 | 7% | 2.6% | +373.1% | -20.6% | +8.45% | 100% |
| dip45_V3_gescreend_fail | 3795 | 14% | 5.4% | +119.5% | -28.9% | -8.11% | 100% |
| dip45_V3_alle | 4399 | 13% | 5.4% | +129.0% | -28.4% | -7.32% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.8%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 3059 | 13% | 3.5% | -10.00% | 100% |
| zonder_xlink | 915 | 19% | 0.0% | +22.62% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 05:20:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:20:47,260 main INFO screen LOOP pass=0 dev=96.37 ins=0.0 pro=1 1a=False 1b=False 2=True (24.7s)
Sep 12 05:20:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:20:57,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:21:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:21:03,006 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:21:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:21:22,460 main INFO screen FLYALON pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (24.6s)
Sep 12 05:22:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:07,152 main INFO screen cat pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.3s)
Sep 12 05:22:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:12,098 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:22:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:17,115 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:22:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:28,715 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (9.4s)
Sep 12 05:22:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:36,169 main INFO screen ROBIN pass=0 dev=98.16 ins=0.0 pro=1 1a=False 1b=False 2=True (24.1s)
Sep 12 05:22:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:22:52,568 main INFO screen CRISPE pass=0 dev=0.46 ins=0.0 pro=1 1a=False 1b=False 2=False (9.3s)
Sep 12 05:23:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:23:25,549 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:23:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:23:26,905 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:23:26 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:23:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:23:30,576 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:23:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:23:51,034 main INFO screen Cat pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (25.6s)
Sep 12 05:24:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:04,420 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:04 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:06,202 main INFO screen NOTBAD pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 12 05:24:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:08,718 aiohttp.access INFO 45.56.109.80 [12/Sep/2026:05:24:08 +0000] "GET /vpn/js/rdx/core/lang/rdx_en.json.gz HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:11,149 main INFO screen chulo pass=0 dev=0.88 ins=0.0 pro=2 1a=False 1b=False 2=False (9.8s)
Sep 12 05:24:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:15,469 aiohttp.access INFO 104.248.223.122 [12/Sep/2026:05:24:15 +0000] "POST /v1/statement HTTP/1.1" 404 174 "-" "python-urllib3/2.7.0"
Sep 12 05:24:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:19,819 aiohttp.access INFO 192.53.123.53 [12/Sep/2026:05:24:19 +0000] "UNKNOWN / HTTP/1.0" 400 352 "-" "-"
Sep 12 05:24:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:29,091 aiohttp.access INFO 45.56.100.247 [12/Sep/2026:05:24:29 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:29,273 aiohttp.access INFO 45.56.100.247 [12/Sep/2026:05:24:29 +0000] "GET /_layouts/15/error.aspx HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:36,275 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:36 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:36,526 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:36 +0000] "GET /auth.html HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:36,781 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:36 +0000] "GET /auth1.html HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:37,037 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:37 +0000] "GET /sslvpnLogin.html HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:37,286 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:37 +0000] "GET /api/sonicos/auth HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:37,534 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:37 +0000] "GET /api/sonicos/tfa HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:37,783 aiohttp.access INFO 72.14.187.229 [12/Sep/2026:05:24:37 +0000] "GET /sonicui/7/sslvpn-portal/ HTTP/1.1" 404 193 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
Sep 12 05:24:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:38,999 main INFO screen ray pass=1 dev=0.0 ins=5.21 pro=40 1a=False 1b=False 2=False (9.4s)
Sep 12 05:24:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:44,453 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:24:44 +0000] "GET /robots.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:24:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:45,781 aiohttp.access INFO 178.128.71.140 [12/Sep/2026:05:24:45 +0000] "GET / HTTP/1.0" 404 174 "-" "-"
Sep 12 05:24:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:24:48,305 main INFO screen skipoo pass=0 dev=1.48 ins=0.0 pro=1 1a=False 1b=False 2=False (5.5s)
Sep 12 05:25:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:13,710 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:13 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:24,355 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:24 +0000] "GET /+CSCOE+/logon.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:31,777 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:31 +0000] "GET /+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2BCSCOE%2B/portal_inc.lua HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:39,177 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:39 +0000] "GET /.env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:46,458 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:46 +0000] "GET /.ftpconfig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:52,838 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:52 +0000] "GET /.git/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:25:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:25:59,787 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:25:59 +0000] "GET /.idea/WebServers.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:00,352 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:26:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:05,420 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:26:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:06,288 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:06 +0000] "GET /.remote-sync.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:12,468 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:12 +0000] "GET /.vscode/ftp-sync.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:18,556 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:18 +0000] "GET /.vscode/sftp.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:23,119 main INFO screen DERP pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (22.9s)
Sep 12 05:26:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:24,761 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:24 +0000] "GET /AHT/AHT_UI/public/js/app.min.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:31,286 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:31 +0000] "GET /CACHE/sdesktop/install/start.htm HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:37,874 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:37 +0000] "GET /EndUserPortal.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:44,214 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:26:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:44,518 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:44 +0000] "GET /Guest.aspx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:49,283 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:26:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:50,992 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:50 +0000] "GET /Login.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:26:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:26:57,630 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:26:57 +0000] "GET /Login/Login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:04,284 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:04 +0000] "GET /Orion/Login.aspx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:07,567 main INFO screen revolve  pass=0 dev=0.0 ins=39.75 pro=28 1a=True 1b=False 2=True (23.5s)
Sep 12 05:27:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:10,507 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:10 +0000] "GET /RASHTML5Gateway/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:11,543 main INFO screen $THRAX pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.2s)
Sep 12 05:27:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:16,990 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:16 +0000] "GET /WebInterface/login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:24,074 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:24 +0000] "GET /_layouts/15/error.aspx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:30,258 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:30 +0000] "GET /admin HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:36,778 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:27:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:36,943 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:36 +0000] "GET /admin_login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:43,209 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:43 +0000] "GET /api/v2/cmdb/system/admin HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:47,765 main INFO screen LILC pass=0 dev=1.4 ins=0.0 pro=2 1a=False 1b=False 2=False (11.1s)
Sep 12 05:27:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:49,565 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:49 +0000] "GET /api/v2/cmdb/system/admin/admin HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:56,225 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:27:56 +0000] "GET /appliance HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:27:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:27:58,105 main INFO screen CULTEPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (8.0s)
Sep 12 05:28:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:03,415 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:28:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:03,483 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:28:03 +0000] "GET /auth HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:28:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:07,386 main INFO screen NOVONORDICKS pass=1 dev=1.05 ins=9.75 pro=39 1a=False 1b=False 2=False (3.0s)
Sep 12 05:28:08 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:08,474 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:28:09 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:09,803 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:28:09 +0000] "GET /auth.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:28:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:16,416 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:28:16 +0000] "GET /auth/admin HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:28:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:17,292 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:28:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:20,820 main INFO screen MEME1921 pass=0 dev=18.5 ins=0.0 pro=7 1a=False 1b=False 2=False (9.0s)
Sep 12 05:28:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:22,334 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:28:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:23,168 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:28:23 +0000] "GET /auth/admin/master/console/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:28:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:28,471 main INFO screen ASSDAQ pass=0 dev=3.39 ins=75.89 pro=2 1a=False 1b=True 2=True (25.1s)
Sep 12 05:28:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:28:28,579 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:28:28 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
Running as unit: schaduwbot-wallets.service; invocation ID: 65c97d0888f44ae1a8047aba8afd8a37
analyses gestart (8746aefc73b4)
--- update 2026-09-12T04:00:11Z
--- update 2026-09-12T04:05:13Z
--- update 2026-09-12T04:10:36Z
--- update 2026-09-12T04:15:47Z
--- update 2026-09-12T04:20:53Z
--- update 2026-09-12T04:25:56Z
--- update 2026-09-12T04:31:17Z
--- update 2026-09-12T04:36:20Z
--- update 2026-09-12T04:41:36Z
--- update 2026-09-12T04:46:50Z
--- update 2026-09-12T04:52:05Z
--- update 2026-09-12T04:57:05Z
--- update 2026-09-12T05:02:29Z
--- update 2026-09-12T05:07:36Z
--- update 2026-09-12T05:12:53Z
--- update 2026-09-12T05:18:21Z
--- update 2026-09-12T05:23:25Z
--- update 2026-09-12T05:28:27Z
```

## Analyses (laatste 25 regels)
```
inactive
03:55:46 grote spelers: saldo van 418 wallets opgehaald
03:56:54 herkomst: 40 posities gekoppeld
03:56:57 klaar in 108s -> /opt/schaduwbot/reports/ledger.md
03:56:59   2000 nieuwe tokens doorgerekend
03:57:01 klaar in 4s: 13363 tokens, 2580 nieuw -> /opt/schaduwbot/reports/video_replay.md
03:57:01 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-09 03:57 UTC
03:57:01 47900 tokens geladen
03:57:04   2000 tokens, 246053 trades, 52081 posities (3s)
03:57:07   4000 tokens, 503264 trades, 107812 posities (6s)
03:57:09   6000 tokens, 764215 trades, 157570 posities (8s)
03:57:12   8000 tokens, 1014522 trades, 208740 posities (11s)
03:57:15   10000 tokens, 1313518 trades, 277037 posities (14s)
03:57:17   12000 tokens, 1549954 trades, 317998 posities (16s)
03:57:20   14000 tokens, 1819922 trades, 373769 posities (19s)
03:57:23   16000 tokens, 2091269 trades, 432443 posities (22s)
03:57:25   18000 tokens, 2350661 trades, 485256 posities (24s)
03:57:28   20000 tokens, 2609433 trades, 537071 posities (27s)
03:57:30   22000 tokens, 2847285 trades, 586776 posities (29s)
03:57:32   24000 tokens, 3117299 trades, 640240 posities (31s)
03:57:34 posities: 689428 uit 3308619 trades (33s)
03:57:43 153508 wallets gerekend
03:57:44 geluk-toets
03:58:14 persistentie
03:58:16 kopieer-simulatie
03:58:26 klaar in 85s -> /opt/schaduwbot/reports/wallets.md
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
