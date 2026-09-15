# Schaduwbot status

- tijd: 2026-09-15 17:08:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 5 days, 3 hours, 21 minutes
- bot-service: active
- code-versie: 3840d00
- schijf: 7.4G/38G | geheugen: 2251/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 210869, "tokens_in_memory": 8811, "msgs": 31314006, "trades": 6531531, "creates": 69461, "decode_fail": 556070, "rpc_calls": 189004, "rpc_errors": 15, "sol_usd": 98.7360506229993, "open_positions": 100, "log_all_trades": true, "amm_trades": 0, "amm_skip": 0, "amm_actief": false}
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
Sep 15 16:46:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:46:58,104 main INFO screen BBR pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (50.2s)
Sep 15 16:47:12 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:47:12,128 main INFO screen SKIPPED pass=0 dev=0.0 ins=0.21 pro=6 1a=False 1b=False 2=False (50.2s)
Sep 15 16:47:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:47:32,776 main INFO screen TWINE pass=0 dev=0.0 ins=32.51 pro=73 1a=False 1b=False 2=True (49.2s)
Sep 15 16:48:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:48:06,853 main INFO screen TRUMP pass=0 dev=0.0 ins=21.19 pro=1 1a=False 1b=False 2=False (68.7s)
Sep 15 16:48:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:48:17,125 main INFO screen Potus pass=0 dev=0.0 ins=37.23 pro=88 1a=False 1b=False 2=True (65.0s)
Sep 15 16:48:25 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:48:25,034 main INFO screen SCRIBECAT pass=0 dev=0.0 ins=75.89 pro=0 1a=False 1b=True 2=True (52.3s)
Sep 15 16:48:29 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:48:29,913 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:48:29 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:48:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:48:54,828 main INFO screen TWINE pass=0 dev=0.0 ins=35.69 pro=3 1a=False 1b=False 2=True (48.0s)
Sep 15 16:49:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:49:09,405 main INFO screen QUIBM pass=0 dev=0.0 ins=17.04 pro=62 1a=False 1b=False 2=True (52.3s)
Sep 15 16:49:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:49:20,078 main INFO screen TWINE pass=0 dev=0.0 ins=38.13 pro=5 1a=False 1b=False 2=True (55.0s)
Sep 15 16:49:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:49:46,118 main INFO screen ROBIN pass=0 dev=0.0 ins=0.7 pro=9 1a=False 1b=False 2=False (51.3s)
Sep 15 16:50:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:50:00,173 main INFO screen NER pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (50.8s)
Sep 15 16:50:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:50:09,780 main INFO screen RENZ  pass=0 dev=0.0 ins=0.0 pro=4 1a=False 1b=False 2=False (49.7s)
Sep 15 16:50:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:50:48,486 main INFO screen CATAMARAN pass=0 dev=0.0 ins=11.78 pro=10 1a=False 1b=False 2=False (48.3s)
Sep 15 16:50:49 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:50:49,938 main INFO screen Bill pass=0 dev=0.0 ins=22.06 pro=57 1a=False 1b=False 2=False (63.8s)
Sep 15 16:51:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:51:01,500 main INFO screen PSTR pass=0 dev=0.0 ins=54.5 pro=23 1a=False 1b=False 2=True (51.7s)
Sep 15 16:51:40 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:51:40,196 main INFO screen Banana pass=0 dev=0.0 ins=15.82 pro=14 1a=False 1b=False 2=True (50.3s)
Sep 15 16:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:51:54,315 main INFO screen Bill pass=0 dev=0.0 ins=16.54 pro=20 1a=False 1b=False 2=False (52.8s)
Sep 15 16:51:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:51:54,824 main INFO screen Cuban pass=0 dev=0.0 ins=0.0 pro=51 1a=False 1b=False 2=False (66.3s)
Sep 15 16:52:47 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:52:47,311 main INFO screen MACHETE pass=0 dev=0.0 ins=28.79 pro=15 1a=False 1b=False 2=True (53.0s)
Sep 15 16:52:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:52:53,125 main INFO screen MOONCOIN pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (72.9s)
Sep 15 16:52:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:52:56,014 main INFO screen POTUS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.2s)
Sep 15 16:53:30 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:53:30,427 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:53:30 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 16:53:39 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:53:39,606 main INFO screen Banana pass=0 dev=0.0 ins=37.91 pro=8 1a=False 1b=False 2=True (52.3s)
Sep 15 16:53:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:53:50,714 main INFO screen TIKTOK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (57.6s)
Sep 15 16:53:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:53:54,791 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (58.8s)
Sep 15 16:54:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:02,082 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:02 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:02,326 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:02 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:02,565 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:02 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:02,816 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:02 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:03,079 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:03,323 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:03,563 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:03,811 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:03 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:04,054 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:04 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:04,347 aiohttp.access INFO 212.102.40.218 [15/Sep/2026:16:54:04 +0000] "UNKNOWN / HTTP/1.0" 400 200 "-" "-"
Sep 15 16:54:38 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:38,401 main INFO screen SHELL pass=0 dev=0.0 ins=79.31 pro=0 1a=False 1b=False 2=True (58.8s)
Sep 15 16:54:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:54:57,631 main INFO screen BILL pass=0 dev=0.0 ins=15.33 pro=63 1a=False 1b=False 2=False (66.9s)
Sep 15 16:55:00 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:55:00,103 main INFO screen aicate pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (65.3s)
Sep 15 16:55:33 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:55:33,361 main INFO screen YouTube pass=0 dev=0.0 ins=177.39 pro=1 1a=False 1b=False 2=True (55.0s)
Sep 15 16:56:14 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:56:14,080 main INFO screen LASER pass=0 dev=0.0 ins=55.88 pro=17 1a=False 1b=False 2=True (74.0s)
Sep 15 16:56:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:56:19,740 main INFO screen NICKI pass=0 dev=0.0 ins=0.0 pro=21 1a=False 1b=False 2=False (82.1s)
Sep 15 16:56:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:56:34,937 main INFO screen SPOOK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (61.6s)
Sep 15 16:57:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:57:06,257 main INFO screen STANDARD pass=0 dev=0.0 ins=48.77 pro=7 1a=False 1b=False 2=True (52.2s)
Sep 15 16:57:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:57:16,224 main INFO screen $SATO pass=0 dev=0.1 ins=0.0 pro=3 1a=False 1b=False 2=False (56.5s)
Sep 15 16:57:31 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:57:31,147 main INFO screen LASER pass=0 dev=0.0 ins=45.91 pro=13 1a=True 1b=False 2=True (56.2s)
Sep 15 16:58:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:58:17,712 main INFO screen KITTE pass=0 dev=0.0 ins=26.4 pro=62 1a=False 1b=False 2=True (71.5s)
Sep 15 16:58:23 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:58:23,823 main INFO screen BOOM pass=0 dev=0.01 ins=75.89 pro=0 1a=False 1b=False 2=True (67.6s)
Sep 15 16:58:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:58:32,027 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:16:58:32 +0000] "GET /health HTTP/1.1" 200 509 "-" "Python-urllib/3.14"
Sep 15 16:58:46 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:58:46,519 main INFO screen UNCLEAR pass=0 dev=0.0 ins=5.05 pro=62 1a=False 1b=False 2=True (75.4s)
Sep 15 16:59:32 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:59:32,341 main INFO screen McCannon pass=0 dev=0.0 ins=33.45 pro=68 1a=False 1b=False 2=True (74.6s)
Sep 15 16:59:35 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:59:35,820 main INFO screen Billy pass=0 dev=0.0 ins=19.67 pro=1 1a=False 1b=False 2=False (72.0s)
Sep 15 16:59:48 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 16:59:48,289 main INFO screen DEBUG pass=0 dev=0.0 ins=22.22 pro=58 1a=False 1b=False 2=False (61.8s)
Sep 15 17:00:54 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:00:54,860 main INFO screen MARADONA pass=0 dev=0.0 ins=0.0 pro=18 1a=False 1b=False 2=False (82.5s)
Sep 15 17:00:56 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:00:56,796 main INFO screen DONGLE pass=0 dev=0.0 ins=78.87 pro=3 1a=False 1b=False 2=True (81.0s)
Sep 15 17:00:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:00:58,784 main INFO screen RICK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (70.5s)
Sep 15 17:02:05 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:02:05,513 main INFO screen HOOD pass=0 dev=0.04 ins=0.0 pro=1 1a=False 1b=False 2=True (68.7s)
Sep 15 17:02:07 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:02:07,595 main INFO screen billy pass=0 dev=0.0 ins=25.55 pro=3 1a=False 1b=False 2=True (72.7s)
Sep 15 17:02:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:02:09,927 main INFO screen PRINT pass=0 dev=0.0 ins=19.95 pro=30 1a=False 1b=False 2=True (71.1s)
Sep 15 17:02:58 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:02:58,965 main INFO screen RIPBIDEN pass=0 dev=0.0 ins=75.0 pro=16 1a=False 1b=False 2=True (53.4s)
Sep 15 17:03:19 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:03:19,227 main INFO screen MOONTOKEN pass=0 dev=0.0 ins=0.0 pro=10 1a=False 1b=False 2=False (69.3s)
Sep 15 17:03:20 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:03:20,521 main INFO screen Cloak pass=0 dev=0.0 ins=0.0 pro=48 1a=False 1b=False 2=False (72.9s)
Sep 15 17:03:34 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:03:34,161 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:03:34 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
Sep 15 17:04:04 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:04:04,571 main INFO screen SolCat pass=0 dev=0.0 ins=42.1 pro=68 1a=False 1b=False 2=True (65.6s)
Sep 15 17:04:06 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:04:06,767 main INFO screen SOLCAT pass=0 dev=0.0 ins=8.25 pro=51 1a=False 1b=False 2=True (47.5s)
Sep 15 17:04:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:04:11,405 main INFO screen LASER pass=0 dev=0.0 ins=36.34 pro=18 1a=False 1b=False 2=True (50.9s)
Sep 15 17:05:03 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:05:03,661 main INFO screen cap pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (59.1s)
Sep 15 17:05:16 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:05:16,289 main INFO screen beer pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (64.9s)
Sep 15 17:05:17 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:05:17,949 main INFO screen MESSI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (71.2s)
Sep 15 17:05:57 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:05:57,197 main INFO screen SolCat pass=0 dev=0.0 ins=31.64 pro=10 1a=True 1b=False 2=True (53.5s)
Sep 15 17:06:08 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:06:08,500 main INFO screen SXSN pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (52.2s)
Sep 15 17:06:11 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:06:11,705 main INFO screen LaMisery pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (53.8s)
Sep 15 17:06:50 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:06:50,406 main INFO screen BIGWEEK pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (53.2s)
Sep 15 17:07:02 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:07:02,351 main INFO screen DOOROC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (53.8s)
Sep 15 17:07:09 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:07:09,348 main INFO screen PNL pass=0 dev=0.0 ins=31.55 pro=38 1a=False 1b=False 2=True (57.6s)
Sep 15 17:07:41 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:07:41,496 main INFO screen STAMPEPE pass=0 dev=0.0 ins=0.0 pro=43 1a=False 1b=False 2=False (51.1s)
Sep 15 17:07:53 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:07:53,178 main INFO screen LASER pass=0 dev=0.0 ins=19.33 pro=0 1a=False 1b=False 2=False (50.8s)
Sep 15 17:08:01 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:08:01,629 main INFO screen Dogewheel pass=0 dev=0.0 ins=44.96 pro=21 1a=False 1b=False 2=True (52.3s)
Sep 15 17:08:26 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:08:26,899 main INFO screen DEV pass=0 dev=0.0 ins=48.77 pro=6 1a=False 1b=False 2=True (45.4s)
Sep 15 17:08:37 ubuntu-4gb-fsn1-1 python[86554]: 2026-09-15 17:08:37,234 aiohttp.access INFO 127.0.0.1 [15/Sep/2026:17:08:37 +0000] "GET /health HTTP/1.1" 200 508 "-" "Python-urllib/3.14"
```

## Update-log (laatste 20 regels)
```
--- update 2026-09-15T16:03:18Z
Running as unit: schaduwbot-wallets.service; invocation ID: 1702f0d8babc48c590b11e6b42957c29
analyses gestart (0f687558a2d6)
--- update 2026-09-15T16:08:19Z
--- update 2026-09-15T16:13:20Z
--- update 2026-09-15T16:18:21Z
--- update 2026-09-15T16:23:21Z
--- update 2026-09-15T16:28:23Z
--- update 2026-09-15T16:33:24Z
--- update 2026-09-15T16:38:26Z
--- update 2026-09-15T16:43:26Z
--- update 2026-09-15T16:48:28Z
--- update 2026-09-15T16:53:28Z
nieuwe code: 3840d00
alleen analyses/documentatie gewijzigd: geen herstart
--- update 2026-09-15T16:58:30Z
--- update 2026-09-15T17:03:32Z
Running as unit: schaduwbot-wallets.service; invocation ID: 7c9219c3aae94dd6b36411ad76eddaca
analyses gestart (84579ff37485)
--- update 2026-09-15T17:08:36Z
```

## Analyses (laatste 40 regels)
```
inactive
12:20:45   4500/6807 lopers, 32066 koppelingen
12:21:33   5000/6807 lopers, 35311 koppelingen
12:22:13   5500/6807 lopers, 38244 koppelingen
12:23:33   6000/6807 lopers, 44729 koppelingen
12:24:21   6500/6807 lopers, 48371 koppelingen
12:24:39 uitkomsten uit de trades halen
12:38:25 68882 tokens met een instapkoers
12:38:26 klaar in 2238s: 6807 lopers, 27625 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 12:38:26
--- /opt/schaduwbot/vamp.py 13:01:37
13:01:37 tokens lezen
13:01:41 135941 tokens; lopers zoeken boven 2.054e-07 SOL per token (volledige tradescan)
13:13:51 6879 lopers, 19 niet-onderscheidende woorden
13:14:53   500/6879 lopers, 4294 koppelingen
13:15:46   1000/6879 lopers, 7299 koppelingen
13:16:30   1500/6879 lopers, 11181 koppelingen
13:17:20   2000/6879 lopers, 15724 koppelingen
13:18:02   2500/6879 lopers, 18375 koppelingen
13:18:35   3000/6879 lopers, 21263 koppelingen
13:19:25   3500/6879 lopers, 25366 koppelingen
13:19:59   4000/6879 lopers, 28115 koppelingen
13:20:55   4500/6879 lopers, 31747 koppelingen
13:21:39   5000/6879 lopers, 34889 koppelingen
13:22:16   5500/6879 lopers, 37799 koppelingen
13:23:41   6000/6879 lopers, 44142 koppelingen
13:24:27   6500/6879 lopers, 47629 koppelingen
13:24:50 uitkomsten uit de trades halen
13:38:33 69698 tokens met een instapkoers
13:38:34 klaar in 2217s: 6879 lopers, 27676 afgeleiden -> /opt/schaduwbot/reports/vamp.md
--- /opt/schaduwbot/video_replay.py 13:38:34
--- /opt/schaduwbot/video_replay.py 14:02:16
--- /opt/schaduwbot/video_replay.py 15:02:36
--- /opt/schaduwbot/video_replay.py 16:03:19
--- /opt/schaduwbot/video_replay.py 17:03:33
17:03:38 venster 2026-09-13 05:03 UTC .. nu, 66880 tokens
17:03:59   2000 nieuwe tokens doorgerekend
17:04:09   4000 nieuwe tokens doorgerekend
17:04:21   6000 nieuwe tokens doorgerekend
17:04:38   8000 nieuwe tokens doorgerekend
17:05:13 klaar in 100s: 50231 tokens, 8649 nieuw -> /opt/schaduwbot/reports/video_replay.md
```

## Fouten in de analyses (laatste 30 regels met een fout)
```
Traceback (most recent call last):
sqlite3.OperationalError: no such column: lamports
```

## IJking poolkoers (laatste 12 regels)
```
12:01:27 ijk: +3 van 3 kandidaten (3 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=233 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
12:01:28 ijk-diagnose: nieuwste migratie 2.8 min oud | migraties 15/60/240 min: 3/30/141 | al gemeten: 625
13:02:11 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=234 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
13:02:11 ijk-diagnose: nieuwste migratie 1.4 min oud | migraties 15/60/240 min: 12/50/153 | al gemeten: 631
14:02:52 ijk: +6 van 14 kandidaten (14 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=238 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
14:02:53 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 14/45/160 | al gemeten: 637
15:03:01 ijk: +4 van 4 kandidaten (4 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=240 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
15:03:02 ijk-diagnose: nieuwste migratie 2.0 min oud | migraties 15/60/240 min: 4/34/158 | al gemeten: 641
16:03:54 ijk: +6 van 12 kandidaten (12 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=246 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
16:03:55 ijk-diagnose: nieuwste migratie 0.8 min oud | migraties 15/60/240 min: 12/35/164 | al gemeten: 647
17:04:38 ijk: +6 van 11 kandidaten (11 migraties in het venster, overgeslagen: {'al_gemeten': 0}) | verste bak n=250 -> mediane afwijking 100% boven 25% binnen 5 minuten na de migratie
17:04:40 ijk-diagnose: nieuwste migratie 2.9 min oud | migraties 15/60/240 min: 11/39/153 | al gemeten: 653
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
