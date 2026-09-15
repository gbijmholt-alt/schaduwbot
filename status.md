# Schaduwbot status

- tijd: 2026-09-15 07:43:53 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 17 hours, 56 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2273/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 176985, "tokens_in_memory": 6521, "msgs": 26389541, "trades": 5342754, "creates": 56988, "decode_fail": 451180, "rpc_calls": 155008, "rpc_errors": 13, "sol_usd": 100.65057939741787, "open_positions": 37, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,713 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.4; robots.txt; +https://openai.com/searchbot)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,735 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user) Chrome/118.0.7917.205 Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,736 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,736 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; LinkedInBot/1.0; +http://www.linkedin.com)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,737 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Amzn-SearchBot/1.0; +https://developer.amazon.com/support/amazonbot)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,737 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Discordbot/2.0; +https://discordapp.com"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,738 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.4; robots.txt; +https://openai.com/searchbot) Chrome/133.0.5795.112 Mobile Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,738 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.599.233 Safari/537.36 Edg/134.0.599.233; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,739 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,740 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.5385.189 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,740 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,740 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,740 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.597.168 Safari/537.36; compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,741 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,742 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Twitterbot/1.0) Chrome/148.0.7528.149 Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,742 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot) Chrome/126.0.5168.195 Mobile Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,742 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; meta-externalagent/1.1; +https://developers.facebook.com/docs/sharing/webmasters/crawler)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,743 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /application.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.4; +https://openai.com/gptbot) Chrome/136.0.4829.72 Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,743 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0) Chrome/148.0.3253.63 Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,744 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,919 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Discordbot/2.0; +https://discordapp.com) Chrome/85.0.263.71 Mobile Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,943 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,944 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,945 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /docker-compose.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,275 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,277 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /docker-compose.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,278 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,279 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,280 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /docker-compose.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,281 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /docker-compose.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6234.202 Mobile Safari/537.36; compatible; Google-Extended/1.0; +http://www.google.com/bot.html"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,282 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; LinkedInBot/1.0; +http://www.linkedin.com)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,282 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /docker-compose.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; WhatsApp/10.0.2.1)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,283 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.3064.35 Safari/537.36; compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,284 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Applebot/0.1; +http://www.apple.com/go/applebot)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,285 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; TelegramBot/1.0"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,285 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots) Chrome/133.0.5673.107 Mobile Safari/537.36"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,285 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots)"
Sep 15 07:33:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:19,286 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:19 +0000] "GET /serverless.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; GPTBot/1.2; +https://openai.com/gptbot)"
Sep 15 07:33:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:29,967 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:33:29 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:33:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:32,158 main INFO screen All-In pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=False (67.5s)
Sep 15 07:33:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:33,285 main INFO screen SNOOPDOGE pass=0 dev=0.0 ins=0.0 pro=61 1a=False 1b=False 2=False (73.9s)
Sep 15 07:33:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:35,244 main INFO screen HashFly pass=0 dev=0.0 ins=38.06 pro=1 1a=False 1b=False 2=True (54.9s)
Sep 15 07:34:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:34:31,488 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (56.2s)
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:35:35,322 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 15 07:35:35 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 15 07:35:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:35:36,406 main INFO screen BMW pass=0 dev=0.0 ins=162.21 pro=0 1a=False 1b=False 2=True (123.1s)
Sep 15 07:35:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:35:40,950 main INFO screen Bulljak pass=0 dev=0.0 ins=77.57 pro=2 1a=False 1b=False 2=True (128.8s)
Sep 15 07:36:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:36:43,046 main INFO screen BOOBA pass=0 dev=0.0 ins=15.41 pro=53 1a=False 1b=False 2=True (131.6s)
Sep 15 07:36:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:36:50,829 main INFO screen $TORQ pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (74.4s)
Sep 15 07:36:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:36:51,418 main INFO screen power pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (70.5s)
Sep 15 07:37:52 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:37:52,254 main INFO screen NORA pass=0 dev=0.0 ins=32.73 pro=66 1a=False 1b=False 2=True (69.2s)
Sep 15 07:37:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:37:57,426 main INFO screen CUBA pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (66.6s)
Sep 15 07:38:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:38:00,034 main INFO screen $CATHOOD pass=0 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (68.6s)
Sep 15 07:38:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:38:37,365 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:38:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 07:38:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:38:45,625 main INFO screen NVDA pass=0 dev=0.0 ins=79.31 pro=1 1a=False 1b=False 2=True (53.4s)
Sep 15 07:39:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:39:02,982 main INFO screen Normie pass=0 dev=0.0 ins=0.16 pro=44 1a=False 1b=False 2=False (62.9s)
Sep 15 07:39:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:39:05,739 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (68.3s)
Sep 15 07:39:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:39:46,588 main INFO screen MOSQUITO pass=0 dev=0.0 ins=21.16 pro=60 1a=False 1b=False 2=True (61.0s)
Sep 15 07:40:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:00,861 main INFO screen biketrump pass=0 dev=0.0 ins=77.42 pro=3 1a=False 1b=True 2=True (57.9s)
Sep 15 07:40:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:02,859 main INFO screen $KOR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.1s)
Sep 15 07:40:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:44,171 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (57.6s)
Sep 15 07:40:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:54,121 main INFO screen att pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (51.3s)
Sep 15 07:40:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:40:56,757 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.9s)
Sep 15 07:41:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:41:41,577 main INFO screen mentality pass=0 dev=0.0 ins=7.28 pro=32 1a=False 1b=False 2=False (57.4s)
Sep 15 07:42:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:04,108 main INFO screen Og pass=0 dev=0.0 ins=0.0 pro=38 1a=False 1b=False 2=False (67.4s)
Sep 15 07:42:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:05,570 main INFO screen CharlieDurk pass=0 dev=0.0 ins=28.03 pro=61 1a=False 1b=False 2=True (71.4s)
Sep 15 07:42:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:42:39,645 main INFO screen BIKESHIBA pass=0 dev=0.0 ins=79.24 pro=8 1a=False 1b=True 2=True (58.1s)
Sep 15 07:43:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:08,783 main INFO screen sol pass=0 dev=0.0 ins=0.88 pro=2 1a=False 1b=False 2=True (64.7s)
Sep 15 07:43:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:11,698 main INFO screen MOSQUITO pass=0 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (66.1s)
Sep 15 07:43:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:30,930 main INFO screen UP COIN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.3s)
Sep 15 07:43:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:43:53,475 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:07:43:53 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T06:15:38Z
--- update 2026-09-15T06:20:58Z
--- update 2026-09-15T06:26:02Z
--- update 2026-09-15T06:31:06Z
--- update 2026-09-15T06:36:14Z
--- update 2026-09-15T06:41:14Z
--- update 2026-09-15T06:46:16Z
--- update 2026-09-15T06:51:34Z
--- update 2026-09-15T06:56:36Z
--- update 2026-09-15T07:01:46Z
--- update 2026-09-15T07:07:17Z
--- update 2026-09-15T07:12:19Z
--- update 2026-09-15T07:17:36Z
--- update 2026-09-15T07:23:10Z
--- update 2026-09-15T07:28:19Z
--- update 2026-09-15T07:33:28Z
--- update 2026-09-15T07:38:36Z
--- update 2026-09-15T07:43:52Z
Running as unit: schaduwbot-wallets.service; invocation ID: 490b6a2e509d44eea38db760fa673dd3
analyses gestart (ef01904db983)
```

## Analyses (laatste 25 regels)
```
active
06:28:28   38000 tokens, 3681003 trades, 443940 posities (248s)
06:28:42   40000 tokens, 3878402 trades, 468824 posities (262s)
06:28:55   42000 tokens, 4065280 trades, 492092 posities (275s)
06:29:07   44000 tokens, 4243961 trades, 512326 posities (287s)
06:29:19   46000 tokens, 4422263 trades, 532650 posities (299s)
06:29:33   48000 tokens, 4597419 trades, 553807 posities (312s)
06:29:46   50000 tokens, 4788806 trades, 577841 posities (326s)
06:30:00   52000 tokens, 4999896 trades, 603952 posities (339s)
06:30:12   54000 tokens, 5196535 trades, 629071 posities (352s)
06:30:26   56000 tokens, 5386638 trades, 656411 posities (366s)
06:30:39   58000 tokens, 5556442 trades, 675632 posities (379s)
06:30:53   60000 tokens, 5747120 trades, 700684 posities (393s)
06:31:08   62000 tokens, 5938035 trades, 722696 posities (407s)
06:31:20   64000 tokens, 6133797 trades, 751257 posities (420s)
06:31:32   66000 tokens, 6333181 trades, 775959 posities (431s)
06:31:44   68000 tokens, 6522980 trades, 801090 posities (443s)
06:31:56   70000 tokens, 6699942 trades, 821373 posities (456s)
06:32:08   72000 tokens, 6901917 trades, 845358 posities (467s)
06:32:21   74000 tokens, 7110225 trades, 878785 posities (480s)
06:32:31 posities: 896682 uit 7257573 trades (496s)
06:32:47 209065 wallets gerekend
06:32:47 geluk-toets
06:33:30 persistentie
06:33:34 kopieer-simulatie
06:35:45 klaar in 690s -> /opt/schaduwbot/reports/wallets.md
```

## IJking poolkoers (laatste 12 regels)
```
07:12:32 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=202 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:12:33 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 10/42/163 | al gemeten: 554
07:17:48 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=205 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:17:48 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 11/42/161 | al gemeten: 558
07:23:19 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=208 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:23:19 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/40/161 | al gemeten: 561
07:28:25 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=210 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:28:25 ijk-diagnose: nieuwste migratie 3.4 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 563
07:33:31 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=211 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:33:31 ijk-diagnose: nieuwste migratie 4.8 min oud | migraties 15/60/240 min: 6/37/159 | al gemeten: 564
07:38:45 ijk: +3 van 3 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=214 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:38:45 ijk-diagnose: nieuwste migratie 0.3 min oud | migraties 15/60/240 min: 6/33/158 | al gemeten: 567
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
