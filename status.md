# Schaduwbot status

- tijd: 2026-09-12 19:33:24 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 5 hours, 46 minutes
- bot-service: active
- code-versie: e364fd9
- schijf: 3.8G/38G | geheugen: 616/3814 MB

## Health
```json
{"ok": false, "last_event_age_s": 7395.4, "uptime_s": 8256, "tokens_in_memory": 434, "msgs": 160742, "trades": 24230, "creates": 434, "decode_fail": 3289, "rpc_calls": 470, "rpc_errors": 15, "sol_usd": 101.60443866598818, "open_positions": 0, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 18266 | 2506 | 14 | 2506 | 182 | 4425 | 13229 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 577 | 16% | 1.7% | +43.6% | -16.1% | -6.24% | 100% |
| dip35_V1_gescreend_fail | 4629 | 27% | 4.0% | +45.3% | -26.1% | -6.74% | 100% |
| dip35_V1_alle | 5756 | 26% | 4.1% | +44.5% | -25.5% | -7.00% | 100% |
| dip35_V2_gescreend_pass | 574 | 22% | 2.4% | +40.8% | -20.3% | -6.69% | 100% |
| dip35_V2_gescreend_fail | 4683 | 25% | 4.4% | +54.8% | -28.1% | -7.07% | 100% |
| dip35_V2_alle | 5716 | 25% | 4.7% | +52.1% | -27.8% | -7.98% | 100% |
| dip35_V3_gescreend_pass | 575 | 9% | 3.0% | +266.5% | -22.1% | +4.01% | 100% |
| dip35_V3_gescreend_fail | 4783 | 14% | 6.1% | +111.0% | -29.9% | -10.81% | 100% |
| dip35_V3_alle | 5768 | 13% | 6.2% | +114.8% | -29.5% | -10.43% | 100% |
| dip40_V1_gescreend_pass | 545 | 14% | 1.8% | +45.4% | -15.6% | -6.94% | 100% |
| dip40_V1_gescreend_fail | 4548 | 27% | 3.9% | +46.8% | -26.0% | -6.62% | 100% |
| dip40_V1_alle | 5529 | 26% | 4.0% | +46.7% | -25.3% | -6.94% | 100% |
| dip40_V2_gescreend_pass | 543 | 17% | 2.2% | +43.6% | -19.5% | -8.53% | 100% |
| dip40_V2_gescreend_fail | 4575 | 25% | 4.3% | +54.6% | -28.1% | -7.09% | 100% |
| dip40_V2_alle | 5483 | 24% | 4.5% | +52.7% | -27.7% | -8.18% | 100% |
| dip40_V3_gescreend_pass | 545 | 8% | 2.6% | +265.1% | -21.0% | +1.58% | 100% |
| dip40_V3_gescreend_fail | 4663 | 13% | 5.9% | +105.8% | -29.6% | -11.83% | 100% |
| dip40_V3_alle | 5536 | 13% | 6.0% | +110.2% | -29.2% | -11.47% | 100% |
| dip45_V1_gescreend_pass | 522 | 15% | 1.7% | +47.5% | -15.4% | -6.22% | 100% |
| dip45_V1_gescreend_fail | 4459 | 28% | 3.6% | +48.2% | -25.8% | -5.46% | 100% |
| dip45_V1_alle | 5347 | 26% | 3.6% | +48.2% | -25.1% | -5.91% | 100% |
| dip45_V2_gescreend_pass | 519 | 18% | 2.1% | +42.7% | -19.5% | -8.11% | 100% |
| dip45_V2_gescreend_fail | 4475 | 25% | 4.1% | +57.4% | -27.8% | -6.17% | 100% |
| dip45_V2_alle | 5303 | 24% | 4.2% | +55.9% | -27.3% | -7.11% | 100% |
| dip45_V3_gescreend_pass | 522 | 8% | 2.1% | +303.1% | -20.3% | +5.08% | 100% |
| dip45_V3_gescreend_fail | 4547 | 14% | 5.6% | +111.2% | -29.2% | -9.97% | 100% |
| dip45_V3_alle | 5347 | 13% | 5.5% | +118.0% | -28.7% | -9.43% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.0%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 451 | 15% | 5.1% | -9.20% | -12.0% tot -6.4% | -14.3% | – | 100% |
| per_token_zonder_xlink | 129 | 21% | 0.0% | +18.56% | -12.6% tot +49.8% | -13.2% | 129% | 54% |
| gepoold_met_xlink | 3803 | 13% | 2.8% | -9.77% | -11.0% tot -8.5% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1119 | 18% | 0.0% | +17.58% | +0.1% tot +35.0% | -14.4% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 12 18:30:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:30:38,095 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:31:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:31:38,173 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:32:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:32:38,271 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:32:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:32:39,171 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:32:39 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:33:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:33:38,356 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:34:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:34:38,447 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:35:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:35:38,541 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:36:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:36:38,623 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:37:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:37:38,701 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:37:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:37:39,524 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:37:39 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:38:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:38:38,770 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:39:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:39:38,852 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:40:00 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:40:00,039 aiohttp.access INFO 16.5.0.236 [12/Sep/2026:18:40:00 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 12 18:40:38 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:40:38,942 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:41:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:41:39,022 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:42:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:42:39,106 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:42:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:42:39,977 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:42:39 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:43:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:43:39,199 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:44:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:44:39,265 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:45:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:45:39,348 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:46:18 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:46:18,104 aiohttp.access INFO 195.182.16.23 [12/Sep/2026:18:46:18 +0000] "GET /SDK/webLanguage HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
Sep 12 18:46:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:46:39,425 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:47:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:47:39,508 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:47:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:47:39,809 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:47:39 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:48:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:48:39,593 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:49:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:49:39,677 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:50:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:50:39,767 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:51:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:51:39,855 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:52:39 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:52:39,942 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:52:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:52:40,359 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:52:40 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:53:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:53:40,041 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:54:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:54:40,250 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:55:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:55:40,342 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:56:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:56:40,409 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:57:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:57:40,482 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:57:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:57:40,760 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:18:57:40 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 18:58:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:58:40,568 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 18:59:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 18:59:40,645 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:00:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:00:40,736 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:01:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:01:40,824 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:02:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:02:40,609 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:02:40 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 19:02:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:02:40,903 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:03:40 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:03:40,998 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:04:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:04:41,089 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:05:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:05:41,173 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:06:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:06:41,258 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:07:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:07:41,065 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:07:41 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 19:07:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:07:41,334 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:08:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:08:41,426 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:09:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:09:41,518 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:10:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:10:41,591 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:11:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:11:41,715 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:12:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:12:41,378 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:12:41 +0000] "GET /health HTTP/1.1" 503 514 "-" "Python-urllib/3.14"
Sep 12 19:12:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:12:41,819 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:13:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:13:41,892 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:14:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:14:41,977 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:15:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:15:42,054 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:16:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:16:42,152 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:17:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:17:41,696 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:17:41 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 19:17:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:17:42,253 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:18:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:18:42,337 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:19:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:19:42,423 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:20:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:20:42,506 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:21:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:21:42,595 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:22:41 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:22:41,989 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:22:41 +0000] "GET /health HTTP/1.1" 503 514 "-" "Python-urllib/3.14"
Sep 12 19:22:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:22:42,677 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:23:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:23:42,775 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:24:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:24:42,853 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:25:16 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:25:16,890 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:19:25:16 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
Sep 12 19:25:17 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:25:17,239 aiohttp.access INFO 150.107.36.82 [12/Sep/2026:19:25:17 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 12 19:25:42 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:25:42,929 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:26:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:26:43,014 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:27:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:27:43,085 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:28:19 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:28:19,575 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:28:19 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
Sep 12 19:28:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:28:43,169 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:29:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:29:43,249 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:30:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:30:43,327 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:31:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:31:43,434 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:32:43 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:32:43,519 main WARNING stream verbroken: server rejected WebSocket connection: HTTP 429 — opnieuw over 60s
Sep 12 19:33:24 ubuntu-4gb-fsn1-1 python[74150]: 2026-09-12 19:33:24,550 aiohttp.access INFO 127.0.0.1 [12/Sep/2026:19:33:24 +0000] "GET /health HTTP/1.1" 503 515 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-12T18:07:16Z
--- update 2026-09-12T18:12:16Z
--- update 2026-09-12T18:17:36Z
--- update 2026-09-12T18:22:38Z
--- update 2026-09-12T18:27:37Z
--- update 2026-09-12T18:32:38Z
--- update 2026-09-12T18:37:38Z
--- update 2026-09-12T18:42:38Z
--- update 2026-09-12T18:47:38Z
--- update 2026-09-12T18:52:39Z
--- update 2026-09-12T18:57:39Z
--- update 2026-09-12T19:02:39Z
--- update 2026-09-12T19:07:40Z
--- update 2026-09-12T19:12:40Z
--- update 2026-09-12T19:17:40Z
--- update 2026-09-12T19:22:40Z
Running as unit: schaduwbot-wallets.service; invocation ID: 868bb1896ee74bf7802de1c47a8100a3
analyses gestart (f08e7b8a0e22)
--- update 2026-09-12T19:28:18Z
--- update 2026-09-12T19:33:23Z
```

## Analyses (laatste 25 regels)
```
inactive
19:28:33   2000 tokens, 234531 trades, 43728 posities (2s)
19:28:35   4000 tokens, 469930 trades, 86030 posities (4s)
19:28:37   6000 tokens, 686745 trades, 126162 posities (6s)
19:28:39   8000 tokens, 912039 trades, 165110 posities (8s)
19:28:41   10000 tokens, 1134949 trades, 207013 posities (10s)
19:28:43   12000 tokens, 1363173 trades, 244092 posities (11s)
19:28:45   14000 tokens, 1629244 trades, 297867 posities (14s)
19:28:47   16000 tokens, 1861152 trades, 340904 posities (16s)
19:28:48   18000 tokens, 2080015 trades, 376103 posities (17s)
19:28:51   20000 tokens, 2329827 trades, 420414 posities (19s)
19:28:52   22000 tokens, 2553211 trades, 460401 posities (21s)
19:28:55   24000 tokens, 2796749 trades, 506835 posities (23s)
19:28:57   26000 tokens, 3030508 trades, 549163 posities (25s)
19:28:59   28000 tokens, 3260600 trades, 588722 posities (27s)
19:29:01   30000 tokens, 3497390 trades, 631312 posities (29s)
19:29:03   32000 tokens, 3708145 trades, 669692 posities (31s)
19:29:05   34000 tokens, 3939276 trades, 712847 posities (34s)
19:29:07   36000 tokens, 4195644 trades, 763072 posities (36s)
19:29:10   38000 tokens, 4428707 trades, 815767 posities (38s)
19:29:10 posities: 836053 uit 4520254 trades (39s)
19:29:21 174384 wallets gerekend
19:29:21 geluk-toets
19:29:55 persistentie
19:29:57 kopieer-simulatie
19:30:09 klaar in 98s -> /opt/schaduwbot/reports/wallets.md
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
