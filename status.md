# Schaduwbot status

- tijd: 2026-09-15 00:17:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 10 hours, 30 minutes
- bot-service: active
- code-versie: 2a95007
- schijf: 6.6G/38G | geheugen: 2327/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.3, "uptime_s": 150209, "tokens_in_memory": 10332, "msgs": 22359204, "trades": 4558619, "creates": 48373, "decode_fail": 398368, "rpc_calls": 128540, "rpc_errors": 13, "sol_usd": 102.4861893708951, "open_positions": 45, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 23:52:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:52:45,473 main INFO screen agrer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (66.4s)
Sep 14 23:53:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:53:08,667 main INFO screen HAZE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (56.3s)
Sep 14 23:53:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:53:19,144 main INFO screen FTR pass=0 dev=0.0 ins=11.16 pro=10 1a=False 1b=False 2=False (46.7s)
Sep 14 23:53:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:53:51,212 main INFO screen bag pass=0 dev=0.0 ins=22.88 pro=42 1a=False 1b=False 2=False (65.7s)
Sep 14 23:53:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:53:58,286 main INFO screen Loom pass=0 dev=0.0 ins=39.45 pro=2 1a=False 1b=False 2=True (49.6s)
Sep 14 23:54:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:54:13,887 main INFO screen Indian pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.7s)
Sep 14 23:54:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:54:41,417 main INFO screen Loom pass=0 dev=0.0 ins=40.58 pro=14 1a=True 1b=False 2=False (50.2s)
Sep 14 23:55:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:55:00,169 main INFO screen Alawn pass=0 dev=0.0 ins=10.11 pro=1 1a=False 1b=False 2=False (61.9s)
Sep 14 23:55:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:55:06,663 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.8s)
Sep 14 23:55:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:55:41,915 main INFO screen PillCrew pass=0 dev=6.74 ins=2.58 pro=66 1a=False 1b=False 2=False (60.5s)
Sep 14 23:55:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:55:56,485 main INFO screen DAISIE pass=0 dev=0.0 ins=40.05 pro=2 1a=False 1b=False 2=True (56.3s)
Sep 14 23:56:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:00,606 main INFO screen GTA 6 Coin pass=0 dev=0.0 ins=0.0 pro=0 1a=False 1b=False 2=True (53.9s)
Sep 14 23:56:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:37,406 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:23:56:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 14 23:56:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:42,941 aiohttp.access INFO 16.5.0.236 [14/Sep/2026:23:56:42 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 14 23:56:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:53,154 main INFO screen SPORTS pass=0 dev=0.0 ins=8.19 pro=70 1a=False 1b=False 2=False (71.2s)
Sep 14 23:56:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:53,178 main INFO screen VEST pass=0 dev=0.0 ins=23.58 pro=14 1a=True 1b=False 2=True (56.7s)
Sep 14 23:56:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:56:57,773 main INFO screen STANKS pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (57.2s)
Sep 14 23:57:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:57:59,118 main INFO screen TRUMBOT pass=0 dev=0.0 ins=11.38 pro=7 1a=False 1b=False 2=False (65.9s)
Sep 14 23:58:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:58:00,593 main INFO screen mmrich pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (67.4s)
Sep 14 23:58:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:58:01,082 main INFO screen DARK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.3s)
Sep 14 23:59:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:59:00,005 aiohttp.access INFO 45.79.149.61 [14/Sep/2026:23:59:00 +0000] "GET / HTTP/1.1" 404 174 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
Sep 14 23:59:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:59:04,524 main INFO screen Sidequest pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (63.4s)
Sep 14 23:59:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:59:05,750 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=17 1a=False 1b=False 2=False (66.6s)
Sep 14 23:59:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 23:59:06,803 main INFO screen QUAKEIII pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (66.2s)
Sep 15 00:00:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:00:20,754 main INFO screen BUFFETT pass=0 dev=0.0 ins=21.32 pro=3 1a=False 1b=False 2=True (75.0s)
Sep 15 00:00:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:00:22,212 main INFO screen FlySwarm pass=0 dev=0.0 ins=11.38 pro=48 1a=False 1b=False 2=False (77.7s)
Sep 15 00:00:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:00:24,679 main INFO screen SOLBANK pass=0 dev=0.0 ins=36.92 pro=59 1a=False 1b=False 2=True (77.9s)
Sep 15 00:01:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:01:16,791 main INFO screen Fartcoin3 pass=0 dev=0.0 ins=5.12 pro=40 1a=False 1b=False 2=False (56.0s)
Sep 15 00:01:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:01:20,387 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (58.2s)
Sep 15 00:01:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:01:25,003 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.3s)
Sep 15 00:01:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:01:53,718 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:01:53 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:02:28 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:02:28,676 main INFO screen $GOLD pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (71.9s)
Sep 15 00:02:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:02:29,838 main INFO screen weave pass=0 dev=0.0 ins=34.11 pro=61 1a=False 1b=False 2=True (69.4s)
Sep 15 00:02:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:02:34,966 main INFO screen Spawn pass=0 dev=0.0 ins=17.49 pro=9 1a=False 1b=False 2=True (70.0s)
Sep 15 00:03:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:03:31,571 main INFO screen bag pass=0 dev=0.0 ins=25.69 pro=53 1a=False 1b=False 2=True (61.7s)
Sep 15 00:03:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:03:37,036 main INFO screen PHANTASM pass=0 dev=0.0 ins=0.0 pro=14 1a=False 1b=False 2=False (68.4s)
Sep 15 00:03:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:03:38,764 main INFO screen troll9 pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (63.8s)
Sep 15 00:04:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:04:25,176 main INFO screen TRUTH pass=0 dev=0.0 ins=19.47 pro=1 1a=False 1b=False 2=True (53.6s)
Sep 15 00:04:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:04:42,845 main INFO screen PF pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (65.8s)
Sep 15 00:04:44 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:04:44,509 main INFO screen FOMO pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (65.7s)
Sep 15 00:05:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:05:02,937 aiohttp.access INFO 94.154.43.254 [15/Sep/2026:00:05:02 +0000] "GET /login HTTP/1.1" 404 174 "-" "Go-http-client/1.1"
Sep 15 00:05:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:05:18,362 main INFO screen CocaCola pass=0 dev=0.0 ins=156.91 pro=1 1a=False 1b=False 2=True (53.2s)
Sep 15 00:05:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:05:35,662 main INFO screen Benz pass=0 dev=0.0 ins=142.37 pro=0 1a=False 1b=False 2=True (52.8s)
Sep 15 00:05:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:05:36,151 main INFO screen STRATEGY pass=0 dev=0.0 ins=117.82 pro=1 1a=False 1b=False 2=True (51.6s)
Sep 15 00:06:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:06:15,870 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.5s)
Sep 15 00:06:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:06:30,574 main INFO screen WASIB pass=0 dev=0.0 ins=36.63 pro=24 1a=True 1b=False 2=True (54.4s)
Sep 15 00:06:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:06:48,754 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (73.1s)
Sep 15 00:07:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:07:17,038 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 15 00:07:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:07:24,989 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:07:24 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:07:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:07:29,499 main INFO screen Sidequest pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (58.9s)
Sep 15 00:07:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:07:46,974 main INFO screen kittylick pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (58.2s)
Sep 15 00:08:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:08:10,753 main INFO screen  JetsetRM pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.7s)
Sep 15 00:08:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:08:32,131 main INFO screen S&B pass=0 dev=0.0 ins=17.18 pro=3 1a=False 1b=False 2=False (62.6s)
Sep 15 00:08:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:08:45,597 main INFO screen ZENCAT pass=0 dev=0.0 ins=0.0 pro=28 1a=False 1b=False 2=False (58.6s)
Sep 15 00:09:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:09:04,477 main INFO screen DOG pass=0 dev=0.0 ins=20.06 pro=9 1a=False 1b=False 2=True (53.7s)
Sep 15 00:09:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:09:32,919 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (60.8s)
Sep 15 00:09:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:09:58,466 main INFO screen Pink Bull pass=0 dev=0.0 ins=0.0 pro=20 1a=False 1b=False 2=False (72.9s)
Sep 15 00:10:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:10:07,415 main INFO screen brain pass=0 dev=0.0 ins=19.86 pro=0 1a=False 1b=False 2=False (62.9s)
Sep 15 00:10:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:10:53,744 main INFO screen Slingoor pass=0 dev=0.0 ins=42.6 pro=69 1a=False 1b=False 2=True (80.8s)
Sep 15 00:11:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:11:09,187 main INFO screen Molly pass=0 dev=0.0 ins=28.7 pro=22 1a=False 1b=False 2=True (70.7s)
Sep 15 00:11:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:11:23,077 main INFO screen SOLBANK pass=0 dev=0.0 ins=35.12 pro=56 1a=True 1b=True 2=True (75.7s)
Sep 15 00:11:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:11:59,200 main INFO screen Ponso pass=0 dev=0.0 ins=20.62 pro=5 1a=False 1b=False 2=True (65.5s)
Sep 15 00:12:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:12:13,403 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (64.2s)
Sep 15 00:12:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:12:26,600 main INFO screen WOTF pass=0 dev=79.31 ins=125.76 pro=1 1a=False 1b=False 2=True (63.5s)
Sep 15 00:12:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:12:35,768 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:12:35 +0000] "GET /health HTTP/1.1" 200 510 "-" "Python-urllib/3.14"
Sep 15 00:13:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:13:05,647 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.4s)
Sep 15 00:13:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:13:07,133 main INFO screen USDF pass=0 dev=0.0 ins=128.27 pro=1 1a=False 1b=False 2=True (53.7s)
Sep 15 00:13:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:13:23,866 main INFO screen brain pass=0 dev=0.0 ins=22.99 pro=54 1a=False 1b=False 2=True (57.3s)
Sep 15 00:14:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:14:00,229 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (54.6s)
Sep 15 00:14:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:14:14,876 main INFO screen sadface pass=0 dev=0.0 ins=0.0 pro=5 1a=False 1b=False 2=False (67.7s)
Sep 15 00:14:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:14:17,668 main INFO screen shabbalon pass=0 dev=0.0 ins=26.4 pro=42 1a=False 1b=False 2=True (53.8s)
Sep 15 00:15:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:03,089 main INFO screen Johy pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (62.9s)
Sep 15 00:15:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:13,823 main INFO screen sol pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.9s)
Sep 15 00:15:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:15:24,488 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=7 1a=False 1b=False 2=False (66.8s)
Sep 15 00:16:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:18,797 main INFO screen CATLLM pass=0 dev=0.0 ins=18.94 pro=3 1a=False 1b=False 2=False (75.7s)
Sep 15 00:16:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:25,766 main INFO screen MILKSWEENE pass=0 dev=7.44 ins=0.11 pro=21 1a=False 1b=False 2=False (71.9s)
Sep 15 00:16:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:16:31,068 main INFO screen coniswork pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (66.6s)
Sep 15 00:17:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:13,737 main INFO screen memelord pass=0 dev=0.0 ins=20.54 pro=6 1a=False 1b=False 2=True (54.9s)
Sep 15 00:17:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:22,206 main INFO screen PADAI pass=0 dev=0.0 ins=68.18 pro=20 1a=True 1b=False 2=True (56.4s)
Sep 15 00:17:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 00:17:37,307 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:00:17:37 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-14T22:48:36Z
--- update 2026-09-14T22:53:43Z
--- update 2026-09-14T22:59:05Z
--- update 2026-09-14T23:04:17Z
--- update 2026-09-14T23:09:27Z
--- update 2026-09-14T23:14:36Z
--- update 2026-09-14T23:19:55Z
--- update 2026-09-14T23:24:58Z
--- update 2026-09-14T23:30:00Z
--- update 2026-09-14T23:35:20Z
--- update 2026-09-14T23:40:36Z
--- update 2026-09-14T23:46:20Z
Running as unit: schaduwbot-wallets.service; invocation ID: dc6a5a650126498b923bda7a46c6b0de
analyses gestart (96a46d7e3c26)
--- update 2026-09-14T23:51:32Z
--- update 2026-09-14T23:56:36Z
--- update 2026-09-15T00:01:52Z
--- update 2026-09-15T00:07:23Z
--- update 2026-09-15T00:12:34Z
--- update 2026-09-15T00:17:36Z
```

## Analyses (laatste 25 regels)
```
active
22:26:56 posities: 891065 uit 7198322 trades (512s)
22:27:09 209874 wallets gerekend
22:27:10 geluk-toets
22:27:44 persistentie
22:27:47 kopieer-simulatie
22:30:19 klaar in 715s -> /opt/schaduwbot/reports/wallets.md
23:46:21 96170 tokens sinds start volledige logging, waarvan 13929 met een gat door herstart
23:46:46   ingelezen tot rowid 9966626 (200000 rijen, 200000 bruikbaar)
23:46:52   ingelezen tot rowid 10060007 (293381 rijen, 293381 bruikbaar)
23:46:54 ingelezen: 293381 nieuwe trades, 293381 bruikbaar (34s)
23:49:47 3000 aankopen van gevolgde wallets geëvalueerd
23:50:45 vroege kopers: 261 voldoen nu, register 468, 445 tokens beoordeeld
23:51:22 grote spelers: saldo van 1158 wallets opgehaald
23:51:51 herkomst: 40 posities gekoppeld
23:52:03 klaar in 342s -> /opt/schaduwbot/reports/ledger.md
00:05:45 S1: gezakt — toets n=27615, verkennend n=14656
00:05:45 klaar in 822s -> /opt/schaduwbot/reports/hypotheses.md
00:05:46 probe: 150 transacties ophalen
00:09:05 poolveld: 12 pools bekeken, 0 te gaan -> vastgesteld @43
00:10:17 poollookup: 25/25 dezelfde pool als in de transactie -> klopt
00:10:17 prijsijk: n=50 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
00:10:18 na-migratie: 100 paren te checken
00:12:16 na-migratie: 40 paren, 19 prijzen
00:15:43 gemigreerde koersen: 62 gedaan, 1588 te gaan
00:15:45 klaar (596 rpc-calls, 140 fouten)
```

## IJking poolkoers (laatste 12 regels)
```
23:20:02 ijk: +3 van 3 kandidaten (7 migraties in het venster, overgeslagen: {'al_gemeten': 4}) | verste bak n=32 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:20:02 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 7/41/171 | al gemeten: 301
23:25:07 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=35 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:25:07 ijk-diagnose: nieuwste migratie 2.4 min oud | migraties 15/60/240 min: 8/39/166 | al gemeten: 304
23:30:16 ijk: +5 van 5 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 6}) | verste bak n=39 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:30:16 ijk-diagnose: nieuwste migratie 2.3 min oud | migraties 15/60/240 min: 11/39/170 | al gemeten: 309
23:35:28 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=42 -> mediane afwijking 99% boven 25% binnen 5 minuten na de migratie
23:35:29 ijk-diagnose: nieuwste migratie -0.0 min oud | migraties 15/60/240 min: 12/42/171 | al gemeten: 312
23:40:44 ijk: +3 van 3 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 8}) | verste bak n=44 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:40:45 ijk-diagnose: nieuwste migratie 0.1 min oud | migraties 15/60/240 min: 11/38/168 | al gemeten: 315
23:46:54 ijk: +3 van 3 kandidaten (8 migraties in het venster, overgeslagen: {'al_gemeten': 5}) | verste bak n=46 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
23:46:55 ijk-diagnose: nieuwste migratie -0.1 min oud | migraties 15/60/240 min: 9/38/167 | al gemeten: 318
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
