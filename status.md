# Schaduwbot status

- tijd: 2026-09-12 04:36:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 14 hours, 49 minutes
- bot-service: active
- code-versie: 1cefa36
- schijf: 3.3G/38G | geheugen: 1104/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 32173, "tokens_in_memory": 6882, "msgs": 6267811, "trades": 1138318, "creates": 10847, "decode_fail": 57885, "rpc_calls": 38682, "rpc_errors": 1569, "sol_usd": 101.78483749723375, "open_positions": 36, "log_all_trades": true}
```

## Laatste rapport
```

Gelogde schaduwtrades: **40074**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 4122 | 672 | 3 | 672 | 43 | 1150 | 3518 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 459 | 17% | 2.2% | +44.4% | -16.8% | -6.63% | 100% |
| dip35_V1_gescreend_fail | 3803 | 27% | 3.8% | +45.8% | -25.9% | -6.72% | 100% |
| dip35_V1_alle | 4636 | 26% | 3.9% | +45.0% | -25.2% | -6.81% | 100% |
| dip35_V2_gescreend_pass | 456 | 22% | 3.1% | +42.9% | -21.3% | -7.23% | 100% |
| dip35_V2_gescreend_fail | 3838 | 25% | 4.4% | +56.6% | -28.0% | -7.07% | 100% |
| dip35_V2_alle | 4603 | 24% | 4.5% | +54.0% | -27.6% | -7.68% | 100% |
| dip35_V3_gescreend_pass | 458 | 8% | 3.5% | +315.4% | -22.6% | +6.18% | 100% |
| dip35_V3_gescreend_fail | 3914 | 13% | 6.0% | +117.7% | -29.6% | -9.92% | 100% |
| dip35_V3_alle | 4648 | 13% | 6.0% | +123.4% | -29.2% | -9.13% | 100% |
| dip40_V1_gescreend_pass | 428 | 15% | 2.3% | +47.1% | -16.1% | -6.79% | 100% |
| dip40_V1_gescreend_fail | 3731 | 26% | 3.8% | +47.6% | -25.7% | -6.53% | 100% |
| dip40_V1_alle | 4448 | 25% | 3.8% | +47.7% | -25.0% | -6.56% | 100% |
| dip40_V2_gescreend_pass | 426 | 18% | 2.8% | +45.2% | -20.1% | -8.41% | 100% |
| dip40_V2_gescreend_fail | 3746 | 25% | 4.3% | +56.2% | -27.9% | -7.04% | 100% |
| dip40_V2_alle | 4410 | 24% | 4.4% | +54.4% | -27.4% | -7.73% | 100% |
| dip40_V3_gescreend_pass | 429 | 8% | 3.0% | +323.1% | -21.3% | +4.39% | 100% |
| dip40_V3_gescreend_fail | 3819 | 13% | 5.8% | +115.9% | -29.4% | -10.42% | 100% |
| dip40_V3_alle | 4459 | 13% | 5.8% | +122.2% | -28.9% | -9.69% | 100% |
| dip45_V1_gescreend_pass | 411 | 16% | 2.2% | +48.7% | -16.0% | -5.95% | 100% |
| dip45_V1_gescreend_fail | 3652 | 27% | 3.3% | +48.6% | -25.4% | -5.19% | 100% |
| dip45_V1_alle | 4302 | 26% | 3.4% | +48.8% | -24.8% | -5.49% | 100% |
| dip45_V2_gescreend_pass | 408 | 19% | 2.7% | +44.3% | -19.9% | -7.48% | 100% |
| dip45_V2_gescreend_fail | 3659 | 25% | 3.9% | +58.6% | -27.4% | -5.79% | 100% |
| dip45_V2_alle | 4264 | 24% | 4.0% | +56.6% | -27.0% | -6.61% | 100% |
| dip45_V3_gescreend_pass | 411 | 7% | 2.7% | +379.8% | -20.6% | +8.62% | 100% |
| dip45_V3_gescreend_fail | 3717 | 14% | 5.5% | +121.2% | -29.0% | -7.96% | 100% |
| dip45_V3_alle | 4304 | 13% | 5.5% | +130.6% | -28.4% | -7.15% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ❌
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.3%, kans ruïne 99.7%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Gepoold over alle dip%/exit-varianten, gescreend_pass, 0,2 SOL/PumpPortal.

| groep | n | winkans | rug% | EV/trade | maxDD@20% |
|---|---|---|---|---|---|
| met_xlink | 2998 | 13% | 3.5% | -10.11% | 100% |
| zonder_xlink | 888 | 18% | 0.0% | +22.78% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 12 04:18:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:18:50,054 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:19:04 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:04,338 main INFO screen NICE pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (19.5s)
Sep 12 04:19:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:18,524 main INFO screen TOAD pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 04:19:40 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:40,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:19:45 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:19:45,977 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:00,863 main INFO screen PUMP pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.0s)
Sep 12 04:20:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:32,936 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:38,149 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:20:44 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:44,395 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 12 04:20:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:53,598 main INFO screen Dellphin pass=0 dev=0.0 ins=10.39 pro=64 1a=False 1b=False 2=True (20.8s)
Sep 12 04:20:54 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:20:54,697 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:20:54 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:22:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:02,318 main INFO screen US pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.3s)
Sep 12 04:22:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:11,096 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:22:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:16,164 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:22:36 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:36,834 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (25.8s)
Sep 12 04:22:41 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:41,135 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:04:22:41 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 04:22:49 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:49,381 main INFO screen chigga pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (2.8s)
Sep 12 04:22:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:22:50,421 main INFO screen skipoo pass=0 dev=1.74 ins=0.0 pro=1 1a=False 1b=False 2=False (9.1s)
Sep 12 04:23:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:23:19,344 main INFO screen kjk pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (6.8s)
Sep 12 04:23:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:23:22,820 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:23:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:23:27,882 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:23:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:23:47,008 main INFO screen USWS pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (24.2s)
Sep 12 04:23:53 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:23:53,823 aiohttp.access INFO 193.124.20.229 [12/Sep/2026:04:23:53 +0000] "GET /zc?action=getInfo HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,638 aiohttp.access INFO 194.88.98.91 [12/Sep/2026:04:24:01 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,662 aiohttp.access INFO 194.88.98.89 [12/Sep/2026:04:24:01 +0000] "GET /favicon.ico HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,674 aiohttp.access INFO 69.5.169.2 [12/Sep/2026:04:24:01 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,675 aiohttp.access INFO 69.5.169.46 [12/Sep/2026:04:24:01 +0000] "GET /mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,676 aiohttp.access INFO 194.88.98.87 [12/Sep/2026:04:24:01 +0000] "GET /api/mcp HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,677 aiohttp.access INFO 194.88.98.100 [12/Sep/2026:04:24:01 +0000] "GET /mcp/ HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:01 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:01,692 aiohttp.access INFO 193.124.20.227 [12/Sep/2026:04:24:01 +0000] "GET /sse HTTP/1.1" 404 193 "-" "Mozilla/5.0 (compatible; Infrawatch/1.0; +https://infrawat.ch/)"
Sep 12 04:24:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:24:20,501 aiohttp.access INFO 94.154.43.223 [12/Sep/2026:04:24:20 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 12 04:25:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:17,814 main INFO screen Dih pass=0 dev=8.11 ins=0.0 pro=27 1a=False 1b=False 2=False (6.8s)
Sep 12 04:25:38 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:38,262 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:25:43 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:43,331 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:25:47 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:47,584 main INFO screen BPCATE pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (9.2s)
Sep 12 04:25:52 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:52,720 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:25:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:57,746 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:25:57 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:25:57 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:25:57,808 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:26:00 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:26:00,488 main INFO screen LASTGPT pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (22.3s)
Sep 12 04:26:10 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:26:10,253 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:26:15 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:26:15,681 main INFO screen BMW pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (23.0s)
Sep 12 04:26:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:26:25,223 main INFO screen DELLPHIN pass=0 dev=0.21 ins=0.0 pro=3 1a=False 1b=False 2=False (15.2s)
Sep 12 04:27:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:27:12,154 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:27:26 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:27:26,802 main INFO screen kittylick pass=0 dev=0.34 ins=0.0 pro=1 1a=False 1b=False 2=False (14.7s)
Sep 12 04:28:11 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:28:11,529 main INFO screen LASERGAT pass=0 dev=33.84 ins=0.0 pro=7 1a=False 1b=False 2=True (6.3s)
Sep 12 04:28:29 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:28:29,993 main INFO screen skipoo pass=0 dev=2.08 ins=0.0 pro=2 1a=False 1b=False 2=True (8.3s)
Sep 12 04:28:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:28:42,733 main INFO screen DERP pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=True (5.2s)
Sep 12 04:28:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:28:56,611 main INFO screen salfetka pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (7.5s)
Sep 12 04:29:06 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:29:06,440 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:29:19 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:29:19,977 main INFO screen FRC pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (13.6s)
Sep 12 04:29:31 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:29:31,435 main INFO screen AI pass=1 dev=0.01 ins=0.0 pro=44 1a=False 1b=False 2=False (3.7s)
Sep 12 04:30:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:30:13,477 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:30:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:30:18,546 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:30:39 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:30:39,960 main INFO screen Liquider pass=0 dev=0.0 ins=49.87 pro=13 1a=False 1b=False 2=True (26.6s)
Sep 12 04:31:02 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:31:02,213 main INFO screen DARK pass=0 dev=15.18 ins=17.13 pro=50 1a=False 1b=False 2=True (9.8s)
Sep 12 04:31:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:31:07,712 main INFO screen . pass=0 dev=0.35 ins=0.0 pro=1 1a=False 1b=False 2=False (8.9s)
Sep 12 04:31:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:31:18,741 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:31:18 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
Sep 12 04:31:24 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:31:24,867 main INFO screen ROCKET pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (11.4s)
Sep 12 04:31:50 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:31:50,369 main INFO screen skipoo pass=0 dev=1.52 ins=0.0 pro=4 1a=False 1b=False 2=False (7.3s)
Sep 12 04:32:20 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:32:20,800 main INFO screen DARK pass=1 dev=0.0 ins=16.26 pro=42 1a=False 1b=False 2=False (3.1s)
Sep 12 04:32:58 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:32:58,146 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:33:03 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:03,234 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:33:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:12,660 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:33:16 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:16,498 main INFO screen ZPOOP pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (18.5s)
Sep 12 04:33:17 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:17,730 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:33:30 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:30,009 main INFO screen API pass=1 dev=0.0 ins=9.35 pro=30 1a=False 1b=False 2=False (2.7s)
Sep 12 04:33:32 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:33:32,308 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=True 2=True (19.7s)
Sep 12 04:34:22 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:22,878 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:34:25 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:25,718 main INFO screen skipoo pass=0 dev=1.82 ins=0.0 pro=5 1a=False 1b=False 2=False (3.9s)
Sep 12 04:34:27 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:27,938 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:34:42 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:42,583 main INFO screen BEAST pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (20.2s)
Sep 12 04:34:55 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:55,564 main INFO screen SSD pass=0 dev=0.0 ins=23.82 pro=59 1a=False 1b=False 2=True (3.4s)
Sep 12 04:34:59 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:34:59,336 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:35:07 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:35:07,426 main INFO screen CHONK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 12 04:35:56 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:35:56,826 main INFO screen skipoo pass=0 dev=2.32 ins=0.0 pro=2 1a=False 1b=False 2=False (1.9s)
Sep 12 04:36:12 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:12,489 main INFO screen Gatto pass=0 dev=15.17 ins=0.78 pro=19 1a=False 1b=True 2=False (4.2s)
Sep 12 04:36:13 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:13,592 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:36:18 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:18,659 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:36:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:21,296 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 12 04:36:21 ubuntu-4gb-fsn1-1 python[43210]: 2026-09-12 04:36:21,973 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:04:36:21 +0000] "GET /health HTTP/1.1" 200 454 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T03:08:04Z
--- update 2026-09-12T03:13:08Z
--- update 2026-09-12T03:18:29Z
--- update 2026-09-12T03:23:36Z
--- update 2026-09-12T03:28:37Z
--- update 2026-09-12T03:33:53Z
--- update 2026-09-12T03:39:36Z
--- update 2026-09-12T03:44:43Z
--- update 2026-09-12T03:49:57Z
--- update 2026-09-12T03:55:08Z
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
