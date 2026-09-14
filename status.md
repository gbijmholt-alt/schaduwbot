# Schaduwbot status

- tijd: 2026-09-14 10:57:14 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 3 days, 21 hours, 10 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 5.6G/38G | geheugen: 1924/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 102186, "tokens_in_memory": 4470, "msgs": 12272627, "trades": 2714904, "creates": 28237, "decode_fail": 227701, "rpc_calls": 80991, "rpc_errors": 7, "sol_usd": 101.75616108018512, "open_positions": 73, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
```

## Laatste rapport
```
| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 28511 | 4468 | 41 | 4467 | 369 | 8202 | 24201 |
| 2026-09-12 | 23127 | 2999 | 15 | 2987 | 255 | 5350 | 15953 |
| 2026-09-13 | 5572 | 625 | 10 | 635 | 107 | 1125 | 3395 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 617 | 17% | 1.6% | +43.2% | -15.9% | -5.99% | 100% |
| dip35_V1_gescreend_fail | 4728 | 27% | 4.0% | +45.1% | -25.9% | -6.78% | 100% |
| dip35_V1_alle | 6456 | 26% | 4.0% | +44.4% | -25.5% | -7.05% | 100% |
| dip35_V2_gescreend_pass | 616 | 23% | 2.3% | +40.7% | -20.1% | -6.31% | 100% |
| dip35_V2_gescreend_fail | 4810 | 25% | 4.4% | +54.6% | -27.9% | -7.05% | 100% |
| dip35_V2_alle | 6416 | 25% | 4.5% | +52.3% | -27.8% | -7.95% | 100% |
| dip35_V3_gescreend_pass | 625 | 9% | 3.2% | +253.7% | -21.9% | +3.65% | 100% |
| dip35_V3_gescreend_fail | 4943 | 14% | 6.1% | +119.4% | -29.6% | -9.19% | 100% |
| dip35_V3_alle | 6472 | 13% | 6.1% | +116.5% | -29.4% | -10.33% | 100% |
| dip40_V1_gescreend_pass | 588 | 15% | 1.7% | +43.7% | -15.4% | -6.70% | 100% |
| dip40_V1_gescreend_fail | 4653 | 26% | 3.9% | +46.6% | -25.7% | -6.64% | 100% |
| dip40_V1_alle | 6210 | 26% | 3.9% | +46.4% | -25.3% | -6.98% | 100% |
| dip40_V2_gescreend_pass | 589 | 18% | 2.0% | +43.0% | -19.4% | -7.95% | 100% |
| dip40_V2_gescreend_fail | 4712 | 25% | 4.3% | +54.6% | -27.8% | -6.97% | 100% |
| dip40_V2_alle | 6164 | 24% | 4.4% | +53.3% | -27.6% | -7.94% | 100% |
| dip40_V3_gescreend_pass | 598 | 8% | 2.8% | +251.7% | -21.0% | +1.83% | 100% |
| dip40_V3_gescreend_fail | 4828 | 13% | 5.8% | +115.5% | -29.3% | -9.97% | 100% |
| dip40_V3_alle | 6220 | 13% | 5.9% | +113.2% | -29.1% | -11.05% | 100% |
| dip45_V1_gescreend_pass | 568 | 15% | 1.6% | +46.7% | -15.1% | -5.90% | 100% |
| dip45_V1_gescreend_fail | 4570 | 27% | 3.6% | +48.0% | -25.5% | -5.53% | 100% |
| dip45_V1_alle | 6003 | 26% | 3.6% | +48.1% | -25.1% | -6.06% | 100% |
| dip45_V2_gescreend_pass | 567 | 19% | 1.9% | +42.4% | -19.4% | -7.86% | 100% |
| dip45_V2_gescreend_fail | 4621 | 25% | 4.0% | +58.3% | -27.5% | -5.83% | 100% |
| dip45_V2_alle | 5957 | 24% | 4.1% | +56.9% | -27.3% | -6.83% | 100% |
| dip45_V3_gescreend_pass | 578 | 8% | 2.4% | +276.6% | -20.3% | +3.82% | 100% |
| dip45_V3_gescreend_fail | 4723 | 14% | 5.4% | +121.9% | -28.9% | -7.66% | 100% |
| dip45_V3_alle | 6006 | 13% | 5.5% | +121.6% | -28.7% | -8.97% | 100% |

## Beste variant: dip45_V3_gescreend_pass

- n>=500: ✅
- winkans>=0.50: ❌
- rug<=0.05: ✅
- ev>=+0.03: ✅
- maxdd20<=0.40: ❌
- Monte Carlo (20% inzet): kans 10.000× 0.1%, kans ruïne 100.0%

## Community-proxy (regel 3, niet als filter — alleen X-link aanwezig ja/nee)

Proxy voor regel 3 uit het bouwplan (community-check): alleen X-link aanwezig ja/nee, niet de daadwerkelijke activiteit. Inzet 0,2 SOL / PumpPortal-fees, alleen gescreend_pass. Let op: 'gepoold' telt elk token één keer per dip%/exit-variant, dus die n is geen aantal onafhankelijke waarnemingen. 'per_token' telt elk token één keer (gemiddelde over zijn varianten) en is de eerlijke steekproefgrootte. Niets hiervan is vooraf vastgelegd.

| groep | n | winkans | rug% | EV/trade | 95%-marge | mediaan | top-3 aandeel van de winst | maxDD@20% |
|---|---|---|---|---|---|---|---|---|
| per_token_met_xlink | 488 | 16% | 5.3% | -8.21% | -11.3% tot -5.1% | -14.3% | – | 100% |
| per_token_zonder_xlink | 154 | 23% | 0.0% | +18.49% | -8.6% tot +45.6% | -13.1% | 119% | 58% |
| gepoold_met_xlink | 4066 | 14% | 2.9% | -9.32% | -10.5% tot -8.1% | -15.2% | – | 100% |
| gepoold_zonder_xlink | 1280 | 18% | 0.0% | +15.22% | -0.1% tot +30.5% | -14.3% | 71% | 100% |

Een EV die grotendeels uit drie trades komt, en een 95%-marge die door nul loopt, zijn geen bewijs van een verschil. Als dit blijft staan, moet het vooraf vastgelegd en op nieuwe tokens getoetst worden.
```

## Bot-log (laatste 80 regels)
```
Sep 14 10:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:30,974 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:30 +0000] "GET /config.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:30,986 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:30 +0000] "GET /runtime-config.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:30,999 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:30 +0000] "GET /config.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,043 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /config.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,230 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /config.php.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,286 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /phpinfo.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,297 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /config.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,331 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.git/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,550 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.git-credentials HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,583 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.pypirc HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,677 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.npmrc HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,678 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.aws/credentials HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,923 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /.docker/config.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,929 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /appsettings.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,949 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /application.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,957 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /application.properties HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:31,959 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:31 +0000] "GET /appsettings.Production.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,261 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /server.key HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,269 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /application.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,277 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /config/secrets.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,279 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /conf/tomcat-users.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,281 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /.kube/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,574 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /actuator/configprops HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,587 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /actuator/env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,590 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /robots.txt HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,603 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /sitemap.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,630 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /sitemap_index.xml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,842 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /api/ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,879 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /openapi.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,934 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /openapi.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:32,942 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:32 +0000] "GET /openapi.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,014 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /swagger.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,176 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /swagger/v1/swagger.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,187 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /v2/api-docs HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,224 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /v3/api-docs HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,247 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /api-docs HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,329 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /api/openapi.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,492 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /package.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,497 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /debug HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,500 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /composer.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,539 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /_profiler HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,616 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /telescope HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:33,778 aiohttp.access INFO 134.185.94.184 [14/Sep/2026:10:45:33 +0000] "GET /docs HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
Sep 14 10:45:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:45,186 main INFO screen DeepSeek pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 14 10:45:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:45:56,310 main INFO screen ElonCoin pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.0s)
Sep 14 10:46:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:46:12,692 main INFO screen wifkayak pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.3s)
Sep 14 10:46:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:46:37,238 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:10:46:37 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 10:47:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:47:07,295 main INFO screen VOID pass=0 dev=42.6 ins=0.0 pro=6 1a=False 1b=False 2=False (65.2s)
Sep 14 10:47:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:47:16,514 main INFO screen Spawn pass=1 dev=0.0 ins=11.38 pro=48 1a=False 1b=False 2=False (64.3s)
Sep 14 10:47:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:47:27,302 main INFO screen shaggy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (55.2s)
Sep 14 10:48:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:48:15,227 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (67.9s)
Sep 14 10:48:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:48:23,033 main INFO screen . pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (66.5s)
Sep 14 10:48:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:48:31,522 main INFO screen VOID pass=1 dev=0.0 ins=0.0 pro=80 1a=False 1b=False 2=False (64.2s)
Sep 14 10:49:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:49:21,286 main INFO screen PUMPBURN pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (66.1s)
Sep 14 10:49:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:49:23,731 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 14 10:49:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:49:29,234 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (57.7s)
Sep 14 10:50:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:50:17,731 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.4s)
Sep 14 10:50:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:50:30,518 main INFO screen Gill pass=0 dev=0.0 ins=51.09 pro=71 1a=False 1b=False 2=True (66.8s)
Sep 14 10:50:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:50:34,020 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.8s)
Sep 14 10:51:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:51:26,063 main INFO screen Gill pass=1 dev=0.0 ins=15.66 pro=68 1a=False 1b=False 2=False (68.3s)
Sep 14 10:51:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:51:30,632 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.1s)
Sep 14 10:51:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:51:34,059 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.0s)
Sep 14 10:52:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:52:04,288 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:10:52:04 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
Sep 14 10:52:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:52:22,281 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (56.2s)
Sep 14 10:52:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:52:32,555 main INFO screen Toeken pass=0 dev=0.0 ins=23.22 pro=19 1a=False 1b=False 2=True (61.9s)
Sep 14 10:52:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:52:34,025 main INFO screen . pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 14 10:53:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:53:12,275 main INFO screen ROBIN pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (50.0s)
Sep 14 10:53:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:53:24,245 main INFO screen Google pass=0 dev=3.57 ins=0.0 pro=1 1a=False 1b=False 2=True (50.2s)
Sep 14 10:53:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:53:26,201 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.6s)
Sep 14 10:54:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:54:01,986 main INFO screen TrumpC47 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (49.7s)
Sep 14 10:54:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:54:27,831 main INFO screen wifkayak pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.6s)
Sep 14 10:54:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:54:29,103 main INFO screen DOOB pass=0 dev=0.17 ins=0.0 pro=2 1a=False 1b=False 2=False (62.9s)
Sep 14 10:54:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:54:49,798 main INFO screen FROGGY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (47.8s)
Sep 14 10:55:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:55:31,678 main INFO screen wifkayak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (63.8s)
Sep 14 10:55:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:55:32,919 main INFO screen billy pass=1 dev=0.43 ins=0.0 pro=15 1a=False 1b=False 2=False (63.8s)
Sep 14 10:55:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:55:44,438 main INFO screen FrogCat pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.6s)
Sep 14 10:56:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:56:35,839 main INFO screen wifkayak pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (64.2s)
Sep 14 10:56:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:56:38,145 main INFO screen . pass=0 dev=0.07 ins=0.0 pro=2 1a=False 1b=False 2=False (65.2s)
Sep 14 10:56:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:56:43,630 main INFO screen UCG pass=0 dev=0.03 ins=0.0 pro=1 1a=False 1b=False 2=False (59.2s)
Sep 14 10:57:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 10:57:14,247 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:10:57:14 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T09:28:56Z
--- update 2026-09-14T09:34:27Z
--- update 2026-09-14T09:39:33Z
--- update 2026-09-14T09:44:36Z
Running as unit: schaduwbot-wallets.service; invocation ID: 980b8aeb5eca48cf8ad4d8ca2b0c2103
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T09:49:36Z
--- update 2026-09-14T09:54:37Z
--- update 2026-09-14T09:59:41Z
--- update 2026-09-14T10:05:20Z
--- update 2026-09-14T10:10:36Z
--- update 2026-09-14T10:15:50Z
--- update 2026-09-14T10:20:56Z
--- update 2026-09-14T10:26:04Z
--- update 2026-09-14T10:31:04Z
--- update 2026-09-14T10:36:11Z
--- update 2026-09-14T10:41:17Z
--- update 2026-09-14T10:46:36Z
--- update 2026-09-14T10:52:03Z
--- update 2026-09-14T10:57:13Z
```

## Analyses (laatste 25 regels)
```
inactive
10:17:17   34000 tokens, 3445797 trades, 426946 posities (228s)
10:17:31   36000 tokens, 3663031 trades, 454723 posities (243s)
10:17:46   38000 tokens, 3863147 trades, 480598 posities (258s)
10:18:00   40000 tokens, 4059696 trades, 501889 posities (272s)
10:18:13   42000 tokens, 4235861 trades, 522161 posities (284s)
10:18:26   44000 tokens, 4436601 trades, 546540 posities (298s)
10:18:37   46000 tokens, 4625596 trades, 570049 posities (308s)
10:18:49   48000 tokens, 4836921 trades, 596160 posities (320s)
10:18:59   50000 tokens, 5034151 trades, 618091 posities (331s)
10:19:10   52000 tokens, 5217058 trades, 639850 posities (341s)
10:19:21   54000 tokens, 5400605 trades, 660082 posities (353s)
10:19:32   56000 tokens, 5595459 trades, 686652 posities (364s)
10:19:43   58000 tokens, 5779455 trades, 707835 posities (374s)
10:19:55   60000 tokens, 5978226 trades, 735178 posities (386s)
10:20:06   62000 tokens, 6177793 trades, 763023 posities (398s)
10:20:19   64000 tokens, 6387196 trades, 789703 posities (410s)
10:20:31   66000 tokens, 6583185 trades, 815152 posities (422s)
10:20:42   68000 tokens, 6781231 trades, 844581 posities (434s)
10:20:55   70000 tokens, 6994817 trades, 881795 posities (446s)
10:21:01 posities: 893845 uit 7089253 trades (456s)
10:21:15 197310 wallets gerekend
10:21:15 geluk-toets
10:21:55 persistentie
10:21:58 kopieer-simulatie
10:24:01 klaar in 636s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
sqlite3.OperationalError: database is locked
10:05:21 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:10:39 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:15:54 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:20:59 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:26:08 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:31:05 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:36:12 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:41:18 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:46:36 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:52:03 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
10:57:13 ijk: +0 | verste bak n=0 -> nog 15 metingen binnen 5 minuten na de migratie te gaan
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
