# Schaduwbot status

- tijd: 2026-09-14 17:22:49 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 4 days, 3 hours, 35 minutes
- bot-service: active
- code-versie: 7a1ec62
- schijf: 6.0G/38G | geheugen: 1920/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 125321, "tokens_in_memory": 7455, "msgs": 16371555, "trades": 3501544, "creates": 36017, "decode_fail": 300228, "rpc_calls": 103947, "rpc_errors": 7, "sol_usd": 102.8413245834934, "open_positions": 54, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 14 17:02:36 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:02:36,345 main INFO screen NIGGABUTT pass=0 dev=0.0 ins=24.74 pro=77 1a=False 1b=False 2=True (68.5s)
Sep 14 17:02:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:02:51,696 main INFO screen SOL pass=0 dev=0.0 ins=39.53 pro=61 1a=False 1b=False 2=True (52.6s)
Sep 14 17:02:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:02:54,641 main INFO screen Neil pass=1 dev=0.0 ins=0.0 pro=59 1a=False 1b=False 2=False (72.1s)
Sep 14 17:03:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:03:33,203 main INFO screen vorcaro pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (56.9s)
Sep 14 17:03:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:03:54,056 main INFO screen Pepe pass=0 dev=0.0 ins=24.94 pro=64 1a=False 1b=False 2=False (62.4s)
Sep 14 17:04:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:04:02,240 main INFO screen 奶龙 pass=0 dev=0.04 ins=85.51 pro=1 1a=False 1b=False 2=True (67.6s)
Sep 14 17:04:27 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:04:27,755 main INFO screen FC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.6s)
Sep 14 17:04:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:04:51,472 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=8 1a=False 1b=False 2=False (57.4s)
Sep 14 17:05:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:05:03,684 main INFO screen Amish pass=0 dev=0.0 ins=18.23 pro=65 1a=False 1b=False 2=True (61.4s)
Sep 14 17:05:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:05:25,050 main INFO screen florklate pass=0 dev=28.82 ins=0.0 pro=14 1a=False 1b=False 2=False (57.3s)
Sep 14 17:05:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:05:48,149 main INFO screen Perplexity pass=0 dev=0.01 ins=0.0 pro=1 1a=False 1b=False 2=True (56.7s)
Sep 14 17:06:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:06:03,587 main INFO screen SOLANA pass=0 dev=0.0 ins=19.66 pro=4 1a=False 1b=False 2=True (59.9s)
Sep 14 17:06:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:06:20,337 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (55.3s)
Sep 14 17:06:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:06:56,822 main INFO screen Apu  pass=1 dev=3.73 ins=15.42 pro=47 1a=False 1b=False 2=False (68.7s)
Sep 14 17:07:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:07:03,920 main INFO screen Amish pass=0 dev=0.0 ins=27.88 pro=56 1a=False 1b=False 2=True (60.3s)
Sep 14 17:07:22 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:07:22,052 main INFO screen NEBUS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (61.7s)
Sep 14 17:07:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:07:35,083 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:07:35 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:07:51 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:07:51,591 main INFO screen BEANS pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.8s)
Sep 14 17:08:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:08:07,303 main INFO screen Peg pass=0 dev=0.1 ins=47.14 pro=72 1a=False 1b=False 2=True (63.4s)
Sep 14 17:08:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:08:19,540 main INFO screen HTML pass=0 dev=0.0 ins=18.98 pro=43 1a=False 1b=False 2=True (57.5s)
Sep 14 17:09:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:09:06,927 main INFO screen SOUP pass=1 dev=0.0 ins=15.83 pro=74 1a=False 1b=False 2=False (75.3s)
Sep 14 17:09:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:09:09,773 main INFO screen master pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (62.5s)
Sep 14 17:09:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:09:14,490 main INFO screen TRUMPEDO pass=0 dev=0.0 ins=49.19 pro=44 1a=False 1b=False 2=True (54.9s)
Sep 14 17:10:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:10:04,914 main INFO screen BILL pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (58.0s)
Sep 14 17:10:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:10:14,755 main INFO screen biketyson pass=0 dev=0.04 ins=6.42 pro=67 1a=False 1b=False 2=True (65.0s)
Sep 14 17:10:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:10:24,861 main INFO screen TLC pass=0 dev=0.0 ins=0.21 pro=7 1a=False 1b=False 2=False (70.4s)
Sep 14 17:11:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:11:01,496 main INFO screen GOLDGOOSE pass=0 dev=0.0 ins=78.96 pro=0 1a=True 1b=True 2=True (56.6s)
Sep 14 17:11:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:11:11,828 main INFO screen punch pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.1s)
Sep 14 17:11:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:11:23,116 main INFO screen mogg pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.3s)
Sep 14 17:11:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:11:59,915 main INFO screen BONKONFONE pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (58.4s)
Sep 14 17:12:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:12:18,034 main INFO screen MOCHI pass=0 dev=0.0 ins=20.86 pro=2 1a=False 1b=False 2=False (66.2s)
Sep 14 17:12:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:12:24,363 main INFO screen VCC pass=0 dev=0.0 ins=57.08 pro=34 1a=False 1b=False 2=True (61.2s)
Sep 14 17:12:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:12:37,274 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:12:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:12:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:12:54,970 main INFO screen HOOD pass=0 dev=0.0 ins=99.17 pro=1 1a=False 1b=False 2=True (55.1s)
Sep 14 17:13:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:13:16,857 main INFO screen lm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (58.8s)
Sep 14 17:13:18 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:13:18,541 main INFO screen Keylist pass=0 dev=0.0 ins=48.82 pro=61 1a=False 1b=False 2=True (54.2s)
Sep 14 17:13:42 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:13:42,903 main INFO screen XSTOCKS pass=0 dev=0.0 ins=0.36 pro=2 1a=False 1b=False 2=False (47.9s)
Sep 14 17:14:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:14:08,279 main INFO screen NINA pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (51.4s)
Sep 14 17:14:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:14:14,871 main INFO screen tolyet pass=0 dev=0.0 ins=50.19 pro=38 1a=False 1b=False 2=True (56.3s)
Sep 14 17:14:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:14:37,219 main INFO screen Jackie pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (54.3s)
Sep 14 17:14:59 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:14:59,157 main INFO screen HALH pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.9s)
Sep 14 17:15:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:15:11,618 main INFO screen m&m pass=0 dev=0.0 ins=30.14 pro=45 1a=False 1b=False 2=True (56.7s)
Sep 14 17:15:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:15:30,685 main INFO screen OpenAI pass=0 dev=0.0 ins=144.09 pro=1 1a=False 1b=False 2=True (53.5s)
Sep 14 17:16:10 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:16:10,691 main INFO screen tolyet pass=0 dev=0.0 ins=21.18 pro=3 1a=False 1b=False 2=False (71.5s)
Sep 14 17:16:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:16:19,265 main INFO screen APOCAL pass=0 dev=0.0 ins=30.36 pro=60 1a=False 1b=False 2=True (67.6s)
Sep 14 17:16:24 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:16:24,174 main INFO screen FROE pass=0 dev=0.0 ins=0.36 pro=1 1a=False 1b=False 2=False (53.5s)
Sep 14 17:17:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:17:02,078 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (51.4s)
Sep 14 17:17:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:17:09,535 main INFO screen Sidelined pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.3s)
Sep 14 17:17:15 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:17:15,531 main INFO screen vcoin pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (51.4s)
Sep 14 17:17:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:17:40,948 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:17:40 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 14 17:17:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:17:53,110 main INFO screen RETARD pass=0 dev=0.0 ins=31.61 pro=61 1a=False 1b=False 2=True (51.0s)
Sep 14 17:18:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:18:03,848 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (54.3s)
Sep 14 17:18:13 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:18:13,366 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.8s)
Sep 14 17:18:45 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:18:45,947 main INFO screen RETARD pass=0 dev=0.0 ins=38.02 pro=62 1a=False 1b=False 2=True (52.8s)
Sep 14 17:18:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:18:58,700 main INFO screen SCRVAN pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (54.9s)
Sep 14 17:19:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:19:19,433 main INFO screen mm pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (66.1s)
Sep 14 17:19:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:19:46,104 main INFO screen Shibabull pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.2s)
Sep 14 17:19:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:19:53,383 main INFO screen BIKETYSON pass=0 dev=0.0 ins=78.12 pro=2 1a=False 1b=True 2=True (54.7s)
Sep 14 17:20:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:20:20,215 main INFO screen pope pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (60.8s)
Sep 14 17:20:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:20:46,644 main INFO screen DONALD  pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (60.5s)
Sep 14 17:20:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:20:57,729 main INFO screen MEMEBASKET pass=0 dev=0.0 ins=28.67 pro=65 1a=False 1b=False 2=True (64.3s)
Sep 14 17:21:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:21:29,404 main INFO screen MEMEBASKET pass=0 dev=0.0 ins=17.35 pro=68 1a=False 1b=False 2=True (69.2s)
Sep 14 17:21:43 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:21:43,925 main INFO screen MIKEBISON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (57.3s)
Sep 14 17:21:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:21:56,839 main INFO screen MEMEBASKET pass=1 dev=0.0 ins=15.28 pro=64 1a=False 1b=False 2=False (59.1s)
Sep 14 17:22:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:22:39,631 main INFO screen MEMEBASKET pass=0 dev=0.0 ins=9.03 pro=86 1a=False 1b=False 2=True (70.2s)
Sep 14 17:22:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:22:47,830 main INFO screen AI pass=1 dev=0.0 ins=0.0 pro=78 1a=False 1b=False 2=False (63.9s)
Sep 14 17:22:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-14 17:22:49,084 aiohttp.access INFO 127.0.0.1 [14/Sep/2026:17:22:49 +0000] "GET /health HTTP/1.1" 200 507 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
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
--- update 2026-09-14T17:07:34Z
--- update 2026-09-14T17:12:36Z
--- update 2026-09-14T17:17:39Z
--- update 2026-09-14T17:22:47Z
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
sqlite3.OperationalError: database is locked
16:30:37 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:36:18 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:41:25 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:46:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:52:04 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
16:57:05 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:02:06 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:07:34 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:12:36 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:17:40 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
17:22:48 ijk: +0 | verste bak n=2 -> nog 13 metingen binnen 5 minuten na de migratie te gaan
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
