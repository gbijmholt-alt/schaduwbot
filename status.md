# Schaduwbot status

- tijd: 2026-09-15 07:33:29 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 17 hours, 46 minutes
- bot-service: active
- code-versie: 8878e1e
- schijf: 6.9G/38G | geheugen: 2237/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.5, "uptime_s": 176362, "tokens_in_memory": 6620, "msgs": 26347496, "trades": 5326598, "creates": 56801, "decode_fail": 450384, "rpc_calls": 154453, "rpc_errors": 13, "sol_usd": 100.71488867026392, "open_positions": 42, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,723 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /_ignition/health-check HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Twitterbot/1.0) Chrome/136.0.2631.110 Safari/537.36"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,723 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /gradle.properties HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.5) Gecko/20100101 Firefox/133.5; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,724 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /.sentryclirc HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.6753.102 Safari/537.36; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,724 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /app.log HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5320.187 Safari/537.36; compatible; TelegramBot/1.0"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,725 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /appsettings.Development.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,725 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /sftp-config.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7707.35 Safari/537.36; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,726 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /buildspec.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Bytespider; +https://zhanzhang.toutiao.com/)"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,726 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /.streamlit/secrets.toml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7536.114 Safari/537.36; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,727 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /buildspec.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.7531.71 Mobile Safari/537.36; compatible; Twitterbot/1.0"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,727 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /api/v1/status/flags HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user)"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,728 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /api/v1/status/config HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.1) Gecko/20100101 Firefox/149.1; compatible; Twitterbot/1.0"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,729 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /appspec.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"
Sep 15 07:33:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:17,730 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:17 +0000] "GET /appspec.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.7) Gecko/20100101 Firefox/127.7; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,009 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /app/config/pimcore/google-api-private-key.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1177.212 Safari/537.36; compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,013 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /pimcore/app/config/pimcore/google-api-private-key.json HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,014 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /ecosystem.config.js HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.2177.52 Safari/537.36 Edg/133.0.2177.52; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,015 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /ecosystem.config.cjs HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Bytespider; +https://zhanzhang.toutiao.com/)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,201 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /compose.yml HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,205 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /compose.yaml HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Slackbot-LinkExpanding/1.0; +https://api.slack.com/robots) Chrome/130.0.2748.56 Safari/537.36 Edg/130.0.2748.56"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,206 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.env.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4219.90 Safari/537.36; compatible; TelegramBot/1.0"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,207 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.env.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.9) Gecko/20100101 Firefox/128.9; compatible; TelegramBot/1.0"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,209 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.backup HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,209 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.11) Gecko/20100101 Firefox/78.11; compatible; TelegramBot/1.0"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,210 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/19.6 Mobile/15E148 Safari/604.1; compatible; Applebot/0.1; +http://www.apple.com/go/applebot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,210 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3432.53 Safari/537.36; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,211 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.env.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,211 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.6) Gecko/20100101 Firefox/105.6; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,212 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,212 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.3453.51 Mobile Safari/537.36; compatible; GPTBot/1.4; +https://openai.com/gptbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,213 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 (compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,213 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /.aws/credentials.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,214 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.save HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 15; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko; compatible; facebookexternalhit/1.1; +http://www.facebook.com/externalhit_uatext.php) Chrome/128.0.4511.115 Mobile Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,214 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate~ HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,215 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.copy HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8202.193 Safari/537.36; compatible; GrokBot/1.0; +https://x.ai/grokbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,215 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.4; robots.txt; +https://openai.com/searchbot) Chrome/148.0.5514.220 Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,216 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.orig HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,216 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.swp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Windows NT 10.0; rv:105.0) Gecko/20100101 Firefox/105.0; compatible; Discordbot/2.0; +https://discordapp.com"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,442 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.tmp HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com) Chrome/124.0.5023.213 Mobile Safari/537.36"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,454 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /terraform.tfstate.1 HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; meta-externalagent/1.1; +https://developers.facebook.com/docs/sharing/webmasters/crawler)"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,457 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.bak HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.2; +https://openai.com/gptbot"
Sep 15 07:33:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 07:33:18,462 aiohttp.access INFO 136.70.127.6 [15/Sep/2026:07:33:18 +0000] "GET /config.json.old HTTP/1.1" 404 174 "-" "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; Claude-User/1.0; +https://www.anthropic.com/claude-user"
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
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T05:55:30Z
--- update 2026-09-15T06:00:31Z
--- update 2026-09-15T06:05:31Z
--- update 2026-09-15T06:10:36Z
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
```

## Analyses (laatste 25 regels)
```
inactive
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
07:01:49 ijk: +1 van 1 kandidaten (6 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=195 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:01:49 ijk-diagnose: nieuwste migratie 1.7 min oud | migraties 15/60/240 min: 6/41/164 | al gemeten: 546
07:07:30 ijk: +4 van 4 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 3}) | verste bak n=198 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:07:30 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 7/41/161 | al gemeten: 550
07:12:32 ijk: +4 van 4 kandidaten (9 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=202 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:12:33 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 10/42/163 | al gemeten: 554
07:17:48 ijk: +4 van 4 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 7}) | verste bak n=205 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:17:48 ijk-diagnose: nieuwste migratie 1.1 min oud | migraties 15/60/240 min: 11/42/161 | al gemeten: 558
07:23:19 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=208 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:23:19 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/40/161 | al gemeten: 561
07:28:25 ijk: +2 van 2 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=210 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
07:28:25 ijk-diagnose: nieuwste migratie 3.4 min oud | migraties 15/60/240 min: 8/40/160 | al gemeten: 563
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
