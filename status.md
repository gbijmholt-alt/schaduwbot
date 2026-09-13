# Schaduwbot status

- tijd: 2026-09-13 06:39:08 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 2 days, 16 hours, 52 minutes
- bot-service: active
- code-versie: e5a2860
- schijf: 4.3G/38G | geheugen: 558/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 300, "tokens_in_memory": 59, "msgs": 30277, "trades": 3123, "creates": 59, "decode_fail": 897, "rpc_calls": 141, "rpc_errors": 0, "sol_usd": 101.3435395612293, "open_positions": 9, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 13 06:13:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:13:44,255 main INFO screen 2 pass=0 dev=0.0 ins=0.35 pro=2 1a=False 1b=False 2=False (57.9s)
Sep 13 06:13:44 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:13:44,764 main INFO screen Mayhem pass=1 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=False (69.1s)
Sep 13 06:13:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:13:49,914 main INFO screen WOFI pass=0 dev=3.97 ins=0.0 pro=1 1a=False 1b=False 2=True (52.7s)
Sep 13 06:14:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:14:14,083 aiohttp.access INFO 178.128.184.235 [13/Sep/2026:06:14:14 +0000] "CONNECT  HTTP/1.1" 404 174 "-" "Mozilla/5.0 zgrab/0.x"
Sep 13 06:14:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:14:39,133 main INFO screen FHALES pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.9s)
Sep 13 06:14:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:14:40,202 main INFO screen Rolex pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (55.4s)
Sep 13 06:14:46 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:14:46,262 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.3s)
Sep 13 06:15:49 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:15:49,511 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (69.3s)
Sep 13 06:15:55 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:15:55,334 main INFO screen Kermit pass=1 dev=0.21 ins=0.0 pro=11 1a=False 1b=False 2=False (76.2s)
Sep 13 06:15:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:15:57,879 main INFO screen $MWIN pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (71.6s)
Sep 13 06:16:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:16:58,716 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=True (63.4s)
Sep 13 06:17:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:17:00,176 main INFO screen stick pass=0 dev=0.0 ins=20.52 pro=63 1a=False 1b=False 2=True (70.7s)
Sep 13 06:17:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:17:09,293 main INFO screen Journey pass=0 dev=0.0 ins=17.05 pro=52 1a=False 1b=False 2=True (71.4s)
Sep 13 06:17:38 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:17:38,238 aiohttp.access INFO 16.5.0.236 [13/Sep/2026:06:17:38 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 13 06:18:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:18:08,760 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (68.6s)
Sep 13 06:18:14 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:18:14,573 main INFO screen savemeeee pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (65.3s)
Sep 13 06:18:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:18:16,214 main INFO screen $PUPH pass=1 dev=0.0 ins=3.43 pro=76 1a=False 1b=False 2=False (77.5s)
Sep 13 06:18:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:18:37,161 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:18:37 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 06:18:59 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:18:59,212 aiohttp.access INFO 189.18.97.61 [13/Sep/2026:06:18:59 +0000] "GET /hachk.php HTTP/1.1" 404 193 "-" "proxy-prefilter/1"
Sep 13 06:19:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:19:06,572 main INFO screen Goblin pass=0 dev=0.0 ins=17.82 pro=43 1a=False 1b=False 2=True (57.8s)
Sep 13 06:19:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:19:23,617 main INFO screen savemeeee pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (69.0s)
Sep 13 06:19:25 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:19:25,556 main INFO screen CATGIRL pass=0 dev=3.42 ins=75.89 pro=3 1a=False 1b=False 2=True (69.3s)
Sep 13 06:20:00 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:20:00,378 main INFO screen savemeeee pass=0 dev=0.2 ins=0.0 pro=2 1a=False 1b=False 2=True (53.8s)
Sep 13 06:20:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:20:37,771 main INFO screen BBP pass=1 dev=0.39 ins=0.0 pro=10 1a=False 1b=False 2=False (72.2s)
Sep 13 06:20:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:20:37,979 main INFO screen $GAMBLE pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (74.4s)
Sep 13 06:21:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:21:12,317 main INFO screen BEAST pass=0 dev=0.0 ins=94.57 pro=1 1a=False 1b=False 2=True (71.9s)
Sep 13 06:21:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:21:36,612 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (58.6s)
Sep 13 06:21:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:21:39,721 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (61.9s)
Sep 13 06:22:08 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:22:08,096 main INFO screen Mayhem pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (55.8s)
Sep 13 06:22:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:22:39,449 main INFO screen BPCATE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (62.8s)
Sep 13 06:22:42 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:22:42,467 main INFO screen SOLAMA pass=0 dev=0.0 ins=27.39 pro=57 1a=False 1b=False 2=True (62.7s)
Sep 13 06:23:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:23:16,931 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=6 1a=False 1b=False 2=False (68.8s)
Sep 13 06:23:36 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:23:36,627 main INFO screen USDE pass=0 dev=0.04 ins=79.27 pro=7 1a=False 1b=True 2=True (56.1s)
Sep 13 06:23:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:23:37,843 main INFO screen WOFI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (52.4s)
Sep 13 06:23:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:23:40,264 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:23:40 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 06:24:37 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:24:37,529 main INFO screen PIGEM pass=0 dev=0.11 ins=77.39 pro=7 1a=False 1b=True 2=True (61.2s)
Sep 13 06:25:15 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:25:15,904 main INFO screen ASTRO pass=0 dev=0.0 ins=17.35 pro=59 1a=False 1b=False 2=True (65.2s)
Sep 13 06:25:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:25:39,052 main INFO screen OpenAI pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.9s)
Sep 13 06:26:05 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:26:05,318 main INFO screen plottwist pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (58.9s)
Sep 13 06:27:40 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:27:40,899 main INFO screen PUMPDOG! pass=1 dev=0.0 ins=0.0 pro=22 1a=False 1b=False 2=False (68.3s)
Sep 13 06:27:57 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:27:57,515 main INFO screen RizzMky pass=1 dev=0.3 ins=0.0 pro=10 1a=False 1b=False 2=False (68.7s)
Sep 13 06:28:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:28:34,059 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (74.0s)
Sep 13 06:28:58 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:28:58,690 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:28:58 +0000] "GET /health HTTP/1.1" 200 505 "-" "Python-urllib/3.14"
Sep 13 06:29:09 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:29:09,708 main INFO screen ALLSTATE pass=0 dev=0.48 ins=0.0 pro=6 1a=False 1b=False 2=False (71.9s)
Sep 13 06:29:16 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:29:16,660 main INFO screen SIGMA pass=0 dev=0.25 ins=0.0 pro=3 1a=False 1b=False 2=False (70.0s)
Sep 13 06:30:06 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:30:06,458 main INFO screen PSYCHO pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.3s)
Sep 13 06:30:07 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:30:07,662 main INFO screen JotGPT pass=0 dev=0.18 ins=79.13 pro=8 1a=False 1b=True 2=True (56.9s)
Sep 13 06:30:10 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:30:10,386 main INFO screen NTDA pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 13 06:31:12 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:31:12,448 main INFO screen IPO pass=0 dev=0.0 ins=9.9 pro=60 1a=False 1b=False 2=True (61.2s)
Sep 13 06:31:34 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:31:34,873 main INFO screen DOOB pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.2s)
Sep 13 06:32:23 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:32:23,696 main INFO screen CATGIRL pass=0 dev=3.42 ins=75.89 pro=2 1a=False 1b=True 2=True (57.2s)
Sep 13 06:32:39 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:32:39,907 main INFO screen AstroDog pass=0 dev=0.07 ins=79.2 pro=6 1a=False 1b=True 2=True (51.9s)
Sep 13 06:33:26 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:33:26,318 main INFO screen PAD pass=0 dev=0.0 ins=20.06 pro=69 1a=False 1b=False 2=True (74.0s)
Sep 13 06:33:33 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:33:33,359 main INFO screen BAGS pass=1 dev=0.0 ins=0.2 pro=52 1a=False 1b=False 2=False (69.7s)
Sep 13 06:33:48 ubuntu-4gb-fsn1-1 python[77259]: 2026-09-13 06:33:48,491 main INFO screen SAVPIR pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (67.4s)
Sep 13 06:34:07 ubuntu-4gb-fsn1-1 systemd[1]: Stopping schaduwbot.service - Schaduwbot (fase 1, geen echte trades)...
Sep 13 06:34:07 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Deactivated successfully.
Sep 13 06:34:07 ubuntu-4gb-fsn1-1 systemd[1]: Stopped schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 13 06:34:07 ubuntu-4gb-fsn1-1 systemd[1]: schaduwbot.service: Consumed 48min 48.208s CPU time over 10h 19.534s wall clock time, 1.2G memory peak.
Sep 13 06:34:07 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 13 06:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:34:08,288 main INFO verbonden met wss://api.mainnet-beta.solana.com
Sep 13 06:34:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:34:08,290 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:34:08 +0000] "GET /health HTTP/1.1" 503 249 "-" "Python-urllib/3.14"
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:35:06,778 main ERROR rapport mislukt: string indices must be integers, not 'str'
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]: Traceback (most recent call last):
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/main.py", line 200, in ticker
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     try: report_mod.write(self.store); self.store.set_meta("last_report", now)
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 170, in write
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     rep = build(store); day = time.strftime("%Y-%m-%d", time.gmtime())
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:   File "/opt/schaduwbot/report.py", line 90, in build
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:     rep["drempels"] = {"n>=500": bool(best and best[1]["n"] >= 500), "winkans>=0.50": bool(best and best[1]["winkans"] >= 0.5),
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]:                                                ~~~~~~~^^^^^
Sep 13 06:35:06 ubuntu-4gb-fsn1-1 python[86554]: TypeError: string indices must be integers, not 'str'
Sep 13 06:36:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:08,028 main INFO screen cco pass=0 dev=0.21 ins=0.0 pro=6 1a=False 1b=False 2=False (61.0s)
Sep 13 06:36:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:09,430 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (62.3s)
Sep 13 06:36:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:36:29,831 main INFO screen batonwif pass=0 dev=3.11 ins=75.89 pro=1 1a=True 1b=True 2=True (57.3s)
Sep 13 06:37:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:37:06,478 main INFO screen OpenClaw pass=0 dev=79.31 ins=0.0 pro=1 1a=False 1b=False 2=True (47.4s)
Sep 13 06:37:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:37:30,597 main INFO screen CHAROC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (48.7s)
Sep 13 06:38:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:38:26,924 main INFO screen PNUT pass=0 dev=0.0 ins=25.45 pro=46 1a=False 1b=False 2=True (70.2s)
Sep 13 06:39:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-13 06:39:08,069 aiohttp.access INFO 127.0.0.1 [13/Sep/2026:06:39:08 +0000] "GET /health HTTP/1.1" 200 486 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-13T05:36:56Z
Running as unit: schaduwbot-wallets.service; invocation ID: 8bfe45551dd4468d8f62fa306c9c7338
analyses gestart (f08e7b8a0e22)
--- update 2026-09-13T05:42:11Z
--- update 2026-09-13T05:47:36Z
--- update 2026-09-13T05:52:49Z
--- update 2026-09-13T05:57:55Z
--- update 2026-09-13T06:03:08Z
--- update 2026-09-13T06:08:19Z
--- update 2026-09-13T06:13:23Z
--- update 2026-09-13T06:18:36Z
--- update 2026-09-13T06:23:39Z
--- update 2026-09-13T06:28:57Z
--- update 2026-09-13T06:34:02Z
nieuwe code: e5a2860
botcode gewijzigd: herstart
install klaar
Running as unit: schaduwbot-wallets.service; invocation ID: a7e508db89c149a5bfe6a64d43f3bf81
analyses gestart (53ca44e52d90)
--- update 2026-09-13T06:39:07Z
```

## Analyses (laatste 25 regels)
```
active
05:48:55   34000 tokens, 3848204 trades, 630517 posities (70s)
05:49:02   36000 tokens, 4062597 trades, 663700 posities (78s)
05:49:09   38000 tokens, 4302243 trades, 705695 posities (85s)
05:49:15   40000 tokens, 4501664 trades, 737577 posities (90s)
05:49:19   42000 tokens, 4725136 trades, 777320 posities (95s)
05:49:24   44000 tokens, 4962765 trades, 815814 posities (99s)
05:49:29   46000 tokens, 5209556 trades, 859079 posities (105s)
05:49:33   48000 tokens, 5418709 trades, 905742 posities (109s)
05:49:34 posities: 923066 uit 5497133 trades (110s)
05:49:46 193401 wallets gerekend
05:49:47 geluk-toets
05:50:19 persistentie
05:50:21 kopieer-simulatie
05:51:13 klaar in 208s -> /opt/schaduwbot/reports/wallets.md
06:34:08 48372 tokens sinds start volledige logging, waarvan 12041 met een gat door herstart
06:34:15   ingelezen tot rowid 5565853 (84640 rijen, 84640 bruikbaar)
06:34:15 ingelezen: 84640 nieuwe trades, 84640 bruikbaar (8s)
06:35:18 1476 aankopen van gevolgde wallets geëvalueerd
06:35:31 vroege kopers: 159 voldoen nu, register 255, 93 tokens beoordeeld
06:35:45 grote spelers: saldo van 41 wallets opgehaald
06:36:11 herkomst: 40 posities gekoppeld
06:36:17 klaar in 129s -> /opt/schaduwbot/reports/ledger.md
06:37:24 S1: gezakt — toets n=4289, verkennend n=14656
06:37:24 klaar in 66s -> /opt/schaduwbot/reports/hypotheses.md
06:37:24 na-migratie: 400 paren te checken
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
