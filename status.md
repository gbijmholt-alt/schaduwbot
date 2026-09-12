# Schaduwbot status

- tijd: 2026-09-12 05:38:34 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 15 hours, 51 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.4G/38G | geheugen: 1102/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 35906, "tokens_in_memory": 6410, "msgs": 6738225, "trades": 1225469, "creates": 11785, "decode_fail": 60098, "rpc_calls": 41460, "rpc_errors": 1677, "sol_usd": 101.63141152545394, "open_positions": 28, "log_all_trades": true}
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
Sep 12 05:30:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:14,808 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:19,955 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:19 +0000] "GET /jsp/index.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:20,521 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (6.9s)
Sep 12 05:30:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:22,017 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:26,389 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:26 +0000] "GET /login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:27,253 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:29,605 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:32,910 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:32 +0000] "GET /login.action HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:33,936 main INFO screen FOMO pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.5s)
Sep 12 05:30:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:34,675 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:39,091 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:39 +0000] "GET /login.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:45,305 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:45 +0000] "GET /login.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:46,369 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:50,118 main INFO screen Anthropic pass=0 dev=98.3 ins=0.0 pro=1 1a=False 1b=False 2=True (28.2s)
Sep 12 05:30:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:51,437 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:30:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:51,850 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:51 +0000] "GET /logon/LogonPoint/custom.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:30:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:52,326 main INFO screen Benz pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (22.8s)
Sep 12 05:30:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:30:58,072 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:30:58 +0000] "GET /logon/LogonPoint/index.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:05 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:05,338 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:05 +0000] "GET /logon/LogonPoint/tmindex.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:06,633 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:06,942 main INFO screen Will pass=0 dev=0.0 ins=11.16 pro=66 1a=False 1b=False 2=True (20.6s)
Sep 12 05:31:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:11,660 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:11,668 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:11 +0000] "GET /mftp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:14 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:14,737 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:18,228 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:18 +0000] "GET /mifs/login.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:23,583 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:24,623 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:24 +0000] "GET /mifs/user/login.jsp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:27,940 main INFO screen CARROT pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (13.2s)
Sep 12 05:31:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:29,115 main INFO screen KEYCAT pass=0 dev=36.15 ins=21.39 pro=5 1a=True 1b=True 2=False (22.9s)
Sep 12 05:31:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:29,253 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:31,235 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:31 +0000] "GET /owa/auth/logon.aspx HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:31,337 main INFO screen ASSOL pass=1 dev=0.0 ins=3.16 pro=42 1a=False 1b=False 2=False (3.2s)
Sep 12 05:31:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:37,428 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:37 +0000] "GET /php/login.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:43,616 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:43 +0000] "GET /php/ztp_gate.php/.js.map HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:46 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:46,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:50,042 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:50 +0000] "GET /portal/webclient/index.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:31:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:50,658 main INFO screen WHEEL pass=0 dev=3.82 ins=21.37 pro=61 1a=False 1b=False 2=True (27.1s)
Sep 12 05:31:51 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:51,139 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:31:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:31:56,430 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:31:56 +0000] "GET /rdweb HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:03,549 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:03 +0000] "GET /remote HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:10,386 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:10 +0000] "GET /remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:11,094 main INFO screen TITCOIN pass=0 dev=0.11 ins=0.0 pro=1 1a=False 1b=False 2=False (25.0s)
Sep 12 05:32:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:17,001 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:17 +0000] "GET /remote/login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:23,863 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:23 +0000] "GET /secure/Dashboard.jspa HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:28,997 main INFO screen SFL pass=0 dev=1.24 ins=23.08 pro=48 1a=False 1b=False 2=True (9.3s)
Sep 12 05:32:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:30,375 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:30 +0000] "GET /showLogin.cc HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:36,513 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:36 +0000] "GET /sonicui/7/login/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:43,195 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:43 +0000] "GET /sonicui/7/sslvpn-portal/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:49,909 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:49 +0000] "GET /sslvpn/Login/Login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:32:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:32:56,788 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:32:56 +0000] "GET /users/sign_in HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:01,589 main INFO screen . pass=0 dev=0.18 ins=0.0 pro=4 1a=False 1b=False 2=False (2.4s)
Sep 12 05:33:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:04,073 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:04 +0000] "GET /vpn/index.html HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:10,193 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:10 +0000] "GET /web/login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:16,694 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:16 +0000] "GET /webapps/login HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:21,719 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (2.0s)
Sep 12 05:33:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:23,472 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:23 +0000] "GET /webclient/Login.xhtml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:29,668 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:29 +0000] "GET /webconsole HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:30,250 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:33:30 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 05:33:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:36,263 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:36 +0000] "GET /webui/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:33:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:39,588 main INFO screen ROO pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 12 05:33:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:33:43,166 aiohttp.access INFO 64.225.35.230 [12/Sep/2026:05:33:43 +0000] "GET /wsman HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
Sep 12 05:34:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:34:20,797 main INFO screen assol pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (3.1s)
Sep 12 05:34:23 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:34:23,225 main INFO screen BUTTCOIN pass=0 dev=0.49 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 12 05:35:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:35:33,155 main INFO screen TITS pass=1 dev=0.0 ins=0.45 pro=43 1a=False 1b=False 2=False (2.8s)
Sep 12 05:35:37 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:35:37,992 main INFO screen Bricko pass=0 dev=0.08 ins=0.0 pro=2 1a=False 1b=False 2=False (2.5s)
Sep 12 05:36:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:36:17,881 main INFO screen LOL pass=1 dev=0.0 ins=5.21 pro=40 1a=False 1b=False 2=False (2.8s)
Sep 12 05:36:34 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:36:34,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:36:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:36:39,087 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:36:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:36:55,180 main INFO screen BREASTS pass=0 dev=0.0 ins=36.47 pro=42 1a=False 1b=False 2=True (21.3s)
Sep 12 05:37:28 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:28,898 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:37:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:30,280 aiohttp.access INFO 3.130.168.2 [12/Sep/2026:05:37:30 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 12 05:37:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:33,668 aiohttp.access INFO 3.130.168.2 [12/Sep/2026:05:37:33 +0000] "GET / HTTP/1.1" 404 174 "-" "visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36"
Sep 12 05:37:33 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:33,965 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:37:48 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:48,899 main INFO screen Butthole pass=0 dev=0.0 ins=19.43 pro=44 1a=False 1b=False 2=True (20.1s)
Sep 12 05:37:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:37:54,939 main INFO screen TJR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.2s)
Sep 12 05:38:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:38:16,248 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:38:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:38:17,881 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:38:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:38:21,314 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 05:38:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:38:25,671 main INFO screen titcoin pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (7.9s)
Sep 12 05:38:35 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 05:38:35,023 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:05:38:35 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-12T05:33:29Z
--- update 2026-09-12T05:38:34Z
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
