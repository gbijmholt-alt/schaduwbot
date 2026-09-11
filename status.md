# Schaduwbot status

- tijd: 2026-09-11 08:26:05 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 18 hours, 39 minutes
- bot-service: active
- code-versie: c32fe95
- schijf: 2.3G/38G | geheugen: 551/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2828, "tokens_in_memory": 1033, "msgs": 245638, "trades": 66952, "creates": 1033, "decode_fail": 2615, "rpc_calls": 1388, "rpc_errors": 247, "sol_usd": 99.88487128807265, "open_positions": 101}
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
Sep 11 08:25:50 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:50,397 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:50 +0000] "GET /cms/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:51 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:51,410 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:51 +0000] "GET /prod/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:51 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:51,505 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:51 +0000] "GET /media../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:51 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:51,582 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:51 +0000] "GET /static../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:52,110 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:52 +0000] "GET /web/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:52 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:52,494 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:52 +0000] "GET /app/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:53 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:53,198 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:53 +0000] "GET /client/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:53 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:53,273 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:53 +0000] "GET /prod/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:55 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:55,598 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:55 +0000] "GET /backup/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:55 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:55,673 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:55 +0000] "GET /cms/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:55 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:55,749 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:55 +0000] "GET /media../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:55 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:55,824 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:55 +0000] "GET /static../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,367 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /app/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,503 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /media../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,578 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /static../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,656 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /admin/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,730 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /media/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,805 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /site/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,881 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /legacy/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:56 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:56,960 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:56 +0000] "GET /lib/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,064 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,139 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /server/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,219 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /dashboard/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,294 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /code/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,369 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /old/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,443 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /build/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:25:58 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:25:58,927 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:25:58 +0000] "GET /admin/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,014 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /media/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,088 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /site/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,163 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /legacy/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,237 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /lib/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,316 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,390 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /server/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,465 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /dashboard/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:00 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:00,540 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:00 +0000] "GET /code/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,442 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /cms/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,517 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /media../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,550 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /dist/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,624 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /plugins/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,650 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /old/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,664 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /site/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,699 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /core/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,724 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /build/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,738 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /legacy/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,773 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /project/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,800 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /dist/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,817 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /lib/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,854 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /dev/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,874 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /plugins/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,901 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,929 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /blog/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,949 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /core/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:01 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:01,976 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:01 +0000] "GET /server/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,003 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /application/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,024 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /project/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,054 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /dashboard/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,078 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /v2/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,129 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /code/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,154 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /release/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,534 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,609 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /static../.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,609 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "UNKNOWN / HTTP/1.0" 400 208 "-" "-"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,687 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /admin/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,689 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET / HTTP/1.1" 404 193 "-" "l9tcpid/v1.1.0"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,765 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /media/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,779 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /v2/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,844 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /site/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,857 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /release/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:02 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:02,933 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:02 +0000] "GET /deploy/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,008 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /public/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,084 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /www/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,158 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /portal/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,232 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /v1/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,250 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /deploy/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,308 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /staging/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,339 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /public/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,383 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /vendor/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,413 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /www/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:03 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:03,458 aiohttp.access INFO 193.32.204.199 [11/Sep/2026:08:26:03 +0000] "GET /modules/.git/config HTTP/1.1" 404 193 "-" "l9explore/1.2.2"
Sep 11 08:26:05 ubuntu-4gb-fsn1-1 python[28325]: 2026-09-11 08:26:05,102 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:08:26:05 +0000] "GET /health HTTP/1.1" 200 422 "-" "Python-urllib/3.14"
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
