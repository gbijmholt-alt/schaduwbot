# Schaduwbot status

- tijd: 2026-09-11 17:41:38 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 day, 3 hours, 54 minutes
- bot-service: active
- code-versie: 84f1f27
- schijf: 2.7G/38G | geheugen: 868/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 28314, "tokens_in_memory": 7324, "msgs": 3515359, "trades": 838813, "creates": 9062, "decode_fail": 64596, "rpc_calls": 15471, "rpc_errors": 1363, "sol_usd": 101.97964499404722, "open_positions": 89, "log_all_trades": true}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-11 16:49 UTC

Gelogde schaduwtrades: **26758**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|
| 2026-09-10 | 14993 | 2145 | 28 | 2144 | 188 | 4138 | 12355 |
| 2026-09-11 | 18692 | 2655 | 28 | 2655 | 187 | 4886 | 14403 |

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|
| dip35_V1_gescreend_pass | 297 | 16% | 2.0% | +41.4% | -16.3% | -7.13% | 99% |
| dip35_V1_gescreend_fail | 2703 | 26% | 3.8% | +46.1% | -25.9% | -6.85% | 100% |
| dip35_V1_alle | 3094 | 26% | 3.9% | +45.3% | -25.2% | -7.09% | 100% |
| dip35_V2_gescreend_pass | 293 | 18% | 2.7% | +44.3% | -21.3% | -9.23% | 100% |
| dip35_V2_gescreend_fail | 2706 | 25% | 4.5% | +56.3% | -28.3% | -7.48% | 100% |
| dip35_V2_alle | 3068 | 24% | 4.6% | +54.9% | -27.9% | -8.06% | 100% |
| dip35_V3_gescreend_pass | 298 | 7% | 2.7% | +128.8% | -22.5% | -11.36% | 100% |
| dip35_V3_gescreend_fail | 2742 | 13% | 6.1% | +107.7% | -29.8% | -11.73% | 100% |
| dip35_V3_alle | 3104 | 13% | 6.0% | +106.3% | -29.3% | -12.08% | 100% |
| dip40_V1_gescreend_pass | 275 | 14% | 1.5% | +42.3% | -15.2% | -7.24% | 99% |
| dip40_V1_gescreend_fail | 2628 | 26% | 3.8% | +48.1% | -25.8% | -6.58% | 100% |
| dip40_V1_alle | 2975 | 25% | 3.8% | +47.4% | -25.0% | -6.79% | 100% |
| dip40_V2_gescreend_pass | 271 | 14% | 2.2% | +51.1% | -19.8% | -9.82% | 100% |
| dip40_V2_gescreend_fail | 2621 | 25% | 4.2% | +55.3% | -28.1% | -7.52% | 100% |
| dip40_V2_alle | 2944 | 24% | 4.3% | +54.7% | -27.5% | -8.12% | 100% |
| dip40_V3_gescreend_pass | 276 | 6% | 2.2% | +108.3% | -21.0% | -13.02% | 100% |
| dip40_V3_gescreend_fail | 2659 | 13% | 5.9% | +95.0% | -29.6% | -13.73% | 100% |
| dip40_V3_alle | 2983 | 12% | 5.8% | +94.1% | -29.0% | -14.00% | 100% |
| dip45_V1_gescreend_pass | 263 | 14% | 1.5% | +48.6% | -15.1% | -6.13% | 98% |
| dip45_V1_gescreend_fail | 2558 | 27% | 3.4% | +49.4% | -25.5% | -5.33% | 100% |
| dip45_V1_alle | 2875 | 26% | 3.4% | +49.3% | -24.7% | -5.61% | 100% |
| dip45_V2_gescreend_pass | 258 | 17% | 2.3% | +49.1% | -19.4% | -7.46% | 99% |
| dip45_V2_gescreend_fail | 2540 | 25% | 3.8% | +59.2% | -27.6% | -6.16% | 100% |
| dip45_V2_alle | 2841 | 24% | 3.8% | +58.2% | -27.0% | -6.64% | 100% |
| dip45_V3_gescreend_pass | 263 | 6% | 2.3% | +170.5% | -20.3% | -7.93% | 100% |
| dip45_V3_gescreend_fail | 2572 | 14% | 5.6% | +108.1% | -29.1% | -10.63% | 100% |
| dip45_V3_alle | 2874 | 13% | 5.4% | +109.5% | -28.5% | -10.71% | 100% |

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
| met_xlink | 2017 | 12% | 2.7% | -9.45% | 100% |
| zonder_xlink | 477 | 13% | 0.0% | -6.31% | 100% |
```

## Bot-log (laatste 80 regels)
```
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,050 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /ecosystem.config.cjs HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko; compatible; Twitterbot/1.0) Version/16.5 Mobile/15E148 Safari/604.1"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,294 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.env.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1456.90 Safari/537.36; compatible; Twitterbot/1.0"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,300 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3150.71 Safari/537.36 Edg/122.0.3150.71; compatible; LinkedInBot/1.0; +http://www.linkedin.com"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,301 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GrokBot/1.0; +https://x.ai/grokbot)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,302 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,303 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.4; +https://openai.com/gptbot)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,303 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.env.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,304 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:128.9) Gecko/20100101 Firefox/128.9; compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,304 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4001.32 Mobile Safari/537.36; compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,305 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,305 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Twitterbot/1.0)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,305 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,306 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.aws/credentials.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GrokBot/1.0; +https://x.ai/grokbot)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,306 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot) Chrome/85.0.7119.83 Safari/537.36"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,307 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1; compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,308 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Twitterbot/1.0)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,308 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_0) AppleWebKit/605.1.15 (KHTML, like Gecko; compatible; Bytespider; +https://zhanzhang.toutiao.com/) Version/16.6 Safari/605.1.15"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,308 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; OAI-SearchBot/1.4; robots.txt; +https://openai.com/searchbot)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,309 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6670.150 Mobile Safari/537.36; compatible; GPTBot/1.4; +https://openai.com/gptbot"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,309 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /terraform.tfstate.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.1972.97 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,310 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /config.json.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/1.0; +https://developer.amazon.com/support/amazonbot)"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,310 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /config.json.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.15) Gecko/20100101 Firefox/128.15; compatible; GPTBot/1.4; +https://openai.com/gptbot"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,310 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /config.json.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,311 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /config.json.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Google-Extended/1.0; +http://www.google.com/bot.html) Chrome/147.0.487.83 Mobile Safari/537.36"
Sep 11 17:40:02 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:02,311 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:02 +0000] "GET /.env.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Claude-SearchBot/1.0; +https://www.anthropic.com/claude-searchbot)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,032 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,097 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.6189.148 Mobile Safari/537.36; compatible; GPTBot/1.4; +https://openai.com/gptbot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,149 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,164 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,164 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,165 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; +https://www.anthropic.com/claude-searchbot)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,165 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 15; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6694.30 Mobile Safari/537.36; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,166 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; LinkedInBot/1.0; +http://www.linkedin.com"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,166 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.6162.188 Safari/537.36; compatible; TelegramBot/1.0"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,166 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,167 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,167 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /config.json.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,167 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user) Chrome/126.0.8957.72 Safari/537.36 Edg/126.0.8957.72"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,167 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0) Chrome/151.0.2000.7 Safari/537.36"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,168 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,169 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.3280.136 Safari/537.36; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,169 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,169 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1400.130 Mobile Safari/537.36; compatible; WhatsApp/10.0.2.1"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,170 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Twitterbot/1.0)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,170 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.8773.141 Safari/537.36; compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,170 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; Applebot/0.1; +http://www.apple.com/go/applebot)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,171 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /application.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.2705.39 Safari/537.36; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,171 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.8432.167 Mobile Safari/537.36; compatible; ChatGPT-User/1.0; +https://openai.com/bot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,171 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GrokBot/1.0; +https://x.ai/grokbot)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,172 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; WhatsApp/10.0.2.1)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,172 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,279 main INFO screen NATHANS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,549 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Bytespider; +https://zhanzhang.toutiao.com/)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,618 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /docker-compose.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,619 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.4; robots.txt; +https://openai.com/searchbot)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,619 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; meta-externalagent/1.1; +https://developers.facebook.com/docs/sharing/webmasters/crawler)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,619 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ClaudeBot/1.0; +claudebot@anthropic.com"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,620 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:127.6) Gecko/20100101 Firefox/127.6; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,620 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; LinkedInBot/1.0; +http://www.linkedin.com) Chrome/109.0.2612.73 Safari/537.36"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,621 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.7932.178 Safari/537.36; compatible; OAI-SearchBot/1.3; +https://openai.com/searchbot"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,621 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; TelegramBot/1.0)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,621 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; TelegramBot/1.0)"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,622 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; meta-externalagent/1.1; +https://developers.facebook.com/docs/sharing/webmasters/crawler"
Sep 11 17:40:03 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:03,622 aiohttp.access INFO 34.16.142.140 [11/Sep/2026:17:40:03 +0000] "GET /serverless.yml.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6432.75 Mobile Safari/537.36; compatible; WhatsApp/10.0.2.1"
Sep 11 17:40:16 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:16,897 main INFO screen DERP pass=0 dev=0.35 ins=0.0 pro=4 1a=False 1b=False 2=False (2.8s)
Sep 11 17:40:54 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:54,842 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:40:55 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:55,483 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:40:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:56,377 main INFO screen PONSCANDLE pass=0 dev=0.0 ins=79.27 pro=8 1a=False 1b=False 2=True (2.2s)
Sep 11 17:40:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:56,468 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:40:56 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:56,736 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:40:57 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:57,135 main INFO screen stocklana pass=0 dev=0.54 ins=0.0 pro=2 1a=False 1b=False 2=False (3.4s)
Sep 11 17:40:58 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:40:58,571 main INFO screen ELON pass=0 dev=0.0 ins=79.14 pro=1 1a=False 1b=False 2=True (2.2s)
Sep 11 17:41:07 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:07,439 main INFO screen Memelord pass=0 dev=0.0 ins=0.17 pro=3 1a=False 1b=False 2=False (6.3s)
Sep 11 17:41:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:08,060 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 11 17:41:08 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:08,576 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 11 17:41:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:09,077 main INFO screen Oil pass=1 dev=0.0 ins=0.0 pro=25 1a=False 1b=False 2=False (1.6s)
Sep 11 17:41:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:09,188 main INFO screen SAVPIR pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.8s)
Sep 11 17:41:09 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:09,450 main INFO screen IMPOSTER pass=0 dev=0.32 ins=0.0 pro=4 1a=False 1b=False 2=False (7.7s)
Sep 11 17:41:20 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:20,735 main INFO screen HOLD pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (4.9s)
Sep 11 17:41:38 ubuntu-4gb-fsn1-1 python[31338]: 2026-09-11 17:41:38,406 aiohttp.access INFO 127.0.0.1 [11/Sep/2026:17:41:38 +0000] "GET /health HTTP/1.1" 200 452 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
analyses gestart (8213ec5e675e)
--- update 2026-09-11T16:08:54Z
--- update 2026-09-11T16:14:06Z
--- update 2026-09-11T16:19:29Z
--- update 2026-09-11T16:24:36Z
--- update 2026-09-11T16:29:47Z
--- update 2026-09-11T16:34:50Z
--- update 2026-09-11T16:40:09Z
--- update 2026-09-11T16:45:19Z
--- update 2026-09-11T16:50:30Z
--- update 2026-09-11T16:55:36Z
--- update 2026-09-11T17:00:58Z
--- update 2026-09-11T17:06:10Z
--- update 2026-09-11T17:11:21Z
--- update 2026-09-11T17:16:23Z
--- update 2026-09-11T17:21:29Z
--- update 2026-09-11T17:26:32Z
--- update 2026-09-11T17:31:32Z
--- update 2026-09-11T17:36:36Z
--- update 2026-09-11T17:41:37Z
```

## Analyses (laatste 25 regels)
```
inactive
14:03:22 94951 wallets gerekend
14:03:22 geluk-toets
14:03:38 persistentie
14:03:39 kopieer-simulatie
14:03:44 klaar in 43s -> /opt/schaduwbot/reports/wallets.md
16:03:36 7475 tokens sinds start volledige logging, waarvan 937 met een gat door herstart
16:03:40   ingelezen tot rowid 1652718 (200000 rijen, 200000 bruikbaar)
16:03:41   ingelezen tot rowid 1684078 (231360 rijen, 231360 bruikbaar)
16:03:41 ingelezen: 231360 nieuwe trades, 231360 bruikbaar (4s)
16:03:46 klaar in 10s -> /opt/schaduwbot/reports/ledger.md
16:03:48   2000 nieuwe tokens doorgerekend
16:03:48 klaar in 2s: 3448 tokens, 2089 nieuw -> /opt/schaduwbot/reports/video_replay.md
16:03:48 wallet-analyse start /opt/schaduwbot/data/schaduwbot.sqlite since 2026-09-08 16:03 UTC
16:03:48 32317 tokens geladen
16:03:51   2000 tokens, 318886 trades, 83589 posities (3s)
16:03:54   4000 tokens, 653328 trades, 170937 posities (6s)
16:03:57   6000 tokens, 953319 trades, 248089 posities (9s)
16:04:01   8000 tokens, 1282543 trades, 335538 posities (13s)
16:04:05   10000 tokens, 1602875 trades, 422034 posities (16s)
16:04:06 posities: 447031 uit 1684507 trades (17s)
16:04:12 104760 wallets gerekend
16:04:12 geluk-toets
16:04:29 persistentie
16:04:30 kopieer-simulatie
16:04:35 klaar in 47s -> /opt/schaduwbot/reports/wallets.md
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
