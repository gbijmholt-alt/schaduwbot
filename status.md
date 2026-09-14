# Schaduwbot status

- tijd: 2026-09-14 17:02:06 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 3 hours, 15 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.0G/38G | geheugen: 1917/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 124078, "tokens_in_memory": 7106, "msgs": 16070798, "trades": 3456005, "creates": 35402, "decode_fail": 293913, "rpc_calls": 102660, "rpc_errors": 7, "sol_usd": 102.52386554036714, "open_positions": 70, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 16:57:21 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:21,931 main INFO screen Shrek pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.0s)
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,050 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /kmonbaseqtdb5b7567 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,542 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /kmonbasezd04105810 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,568 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.docker/config.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,589 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.htaccess HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,593 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /config/secrets.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,597 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /wp-config.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,638 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /backup.tar.gz HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,642 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /dump.sql HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,689 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.git/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,690 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.kube/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,690 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /laravel.log HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,691 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /config.py HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,708 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /terraform.tfstate HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,710 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /application.properties HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,713 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /web.config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,714 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /config/database.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,715 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /backup.zip HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,740 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /configuration.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,743 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.git/HEAD HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,750 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /airflow.cfg HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,764 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /wp-config.php.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,766 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.git-credentials HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,767 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.env.dist HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,781 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /package.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,799 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /secrets.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,805 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /secrets.py HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,807 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.env.test HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,814 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /docker-compose.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,840 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /config.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,848 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /settings.py HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,854 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /db.sql.gz HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,883 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /db.sql HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,888 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.env.production HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,895 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /backup.sql HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,914 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /config.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,922 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.env.example HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,943 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /www.zip HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,946 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /phpinfo.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,949 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.env.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,975 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /application.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,982 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /.gitlab-ci.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:27,987 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:27 +0000] "GET /Dockerfile HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,004 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /credentials.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,053 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /error.log HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,135 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.development HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,142 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /adminer.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,165 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,167 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /ecosystem.config.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,197 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.staging HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,226 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.htpasswd HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,271 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.ssh/id_rsa HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,338 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /debug.log HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,370 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.npmrc HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,383 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,387 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.aws/credentials HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,424 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.git/logs/HEAD HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,491 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /info.php HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,509 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /Jenkinsfile HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,555 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /config.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,569 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,727 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:28,896 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:28 +0000] "GET /.env.local HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:30,498 aiohttp.access INFO 93.152.209.6 [14/Sep/2026:16:57:30 +0000] "GET /database.sql HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
Sep 14 16:57:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:57:58,323 main INFO screen $BGT pass=0 dev=0.0 ins=0.0 pro=15 1a=False 1b=False 2=False (48.8s)
Sep 14 16:58:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:58:10,182 main WARNING stream verbroken: sent 1002 (protocol error) invalid status code; no close frame received — opnieuw over 1s
Sep 14 16:58:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:58:11,274 main INFO verbonden met wss://api.mainnet-beta.solana.com
Sep 14 16:58:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:58:19,190 main INFO screen GLD pass=0 dev=0.0 ins=20.83 pro=1 1a=False 1b=False 2=False (60.7s)
Sep 14 16:58:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:58:24,878 main INFO screen TWINEGPT pass=0 dev=0.35 ins=77.69 pro=7 1a=False 1b=False 2=True (62.9s)
Sep 14 16:59:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:59:02,202 main INFO screen fone pass=1 dev=0.0 ins=19.45 pro=28 1a=False 1b=False 2=False (63.9s)
Sep 14 16:59:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:59:07,768 main INFO screen LMEOW pass=0 dev=0.12 ins=125.3 pro=1 1a=False 1b=False 2=True (48.6s)
Sep 14 16:59:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:59:15,120 main INFO screen NINA pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (50.2s)
Sep 14 16:59:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 16:59:54,574 main INFO screen AI pass=0 dev=0.0 ins=57.08 pro=39 1a=False 1b=False 2=True (52.4s)
Sep 14 17:00:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:00:16,976 main INFO screen NGLM pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=False (69.2s)
Sep 14 17:00:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:00:18,095 main INFO screen soon pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (63.0s)
Sep 14 17:00:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:00:54,381 main INFO screen CHARLIE pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (59.8s)
Sep 14 17:01:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:01:27,813 main INFO screen Pro-Human pass=0 dev=0.0 ins=31.49 pro=60 1a=False 1b=False 2=True (69.7s)
Sep 14 17:01:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:01:42,532 main INFO screen FARLEY pass=0 dev=18.68 ins=0.0 pro=22 1a=False 1b=False 2=False (85.6s)
Sep 14 17:01:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:01:59,103 main INFO screen GS pass=0 dev=0.0 ins=17.62 pro=35 1a=False 1b=False 2=True (64.7s)
Sep 14 17:02:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:02:06,638 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:02:06 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T15:33:36Z
--- update 2026-09-14T15:38:40Z
--- update 2026-09-14T15:43:41Z
--- update 2026-09-14T15:48:53Z
--- update 2026-09-14T15:54:27Z
Running as unit: schaduwbot-wallets.service; invocation ID: bb9b36ab53964518996f9300eff1d4cf
analyses gestart (61d1b06b5cec)
--- update 2026-09-14T15:59:36Z
--- update 2026-09-14T16:04:41Z
--- update 2026-09-14T16:09:46Z
--- update 2026-09-14T16:14:46Z
--- update 2026-09-14T16:19:50Z
--- update 2026-09-14T16:25:17Z
--- update 2026-09-14T16:30:36Z
--- update 2026-09-14T16:36:15Z
--- update 2026-09-14T16:41:21Z
--- update 2026-09-14T16:46:36Z
--- update 2026-09-14T16:52:04Z
--- update 2026-09-14T16:57:04Z
--- update 2026-09-14T17:02:05Z
```

## Analyses (laatste 25 regels)
```
inactive
16:33:38   34000 tokens, 3432567 trades, 425634 posities (227s)
16:33:53   36000 tokens, 3644007 trades, 450026 posities (242s)
16:34:08   38000 tokens, 3848659 trades, 478377 posities (256s)
16:34:22   40000 tokens, 4046955 trades, 500997 posities (271s)
16:34:35   42000 tokens, 4222952 trades, 519780 posities (283s)
16:34:47   44000 tokens, 4418580 trades, 544143 posities (295s)
16:34:58   46000 tokens, 4610884 trades, 567679 posities (307s)
16:35:10   48000 tokens, 4822586 trades, 593054 posities (319s)
16:35:22   50000 tokens, 5034610 trades, 619442 posities (330s)
16:35:33   52000 tokens, 5213503 trades, 638616 posities (341s)
16:35:45   54000 tokens, 5392064 trades, 660041 posities (353s)
16:35:58   56000 tokens, 5596181 trades, 686230 posities (366s)
16:36:09   58000 tokens, 5774359 trades, 706776 posities (378s)
16:36:23   60000 tokens, 6000078 trades, 737951 posities (392s)
16:36:36   62000 tokens, 6182781 trades, 763126 posities (404s)
16:36:50   64000 tokens, 6399806 trades, 792698 posities (419s)
16:37:03   66000 tokens, 6596383 trades, 817546 posities (432s)
16:37:16   68000 tokens, 6798262 trades, 845064 posities (445s)
16:37:30   70000 tokens, 7001931 trades, 881382 posities (458s)
16:37:40 posities: 900358 uit 7154599 trades (470s)
16:37:52 200540 wallets gerekend
16:37:52 geluk-toets
16:38:27 persistentie
16:38:29 kopieer-simulatie
16:40:34 klaar in 644s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
    led = open_led()
  File "/opt/schaduwbot/pumpswap.py", line 96, in open_led
    db.execute("DELETE FROM amm_prijsijk WHERE wsol IS NULL")
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: database is locked
16:30:37 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:36:18 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:41:25 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:46:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:52:04 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:57:05 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:02:06 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
