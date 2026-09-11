# Wallet-analyse pump.fun — 2026-09-11 12:00 UTC

## Kort antwoord

- Geluk-toets: 18 van 2753 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=9.91, geluk-grens 5.1).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.3% per positie (alle wallets: -9.6%; 11 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.1%, 2 s: -16.1%, 10 s: -17.0%, 60 s: -19.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 11:59 UTC (22.2 uur), helft A/B-grens: 2026-09-11 00:53 UTC
- 1255975 trades, 6348 tokens, 84645 wallets, 413620 posities (377872 geopend vanaf ≥ $7k, 35748 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 52037
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6152 | 4093 | -49.10 | -75.28 | +268.78 | 20662.08 | 1747 | +187.99 |
| swing | 433 | 4404 | -183.90 | -252.74 | -131.84 | 30.18 | 474 | -0.24 |
| dev | 651 | 2253 | -112.89 | -830.90 | -307.97 | 3789.85 | 779 | +28.98 |
| bot_hf | 1735 | 84966 | -160.41 | -1083.25 | +1539.80 | 6293.05 | 13434 | +243.31 |
| scalper | 12282 | 179240 | -5160.11 | -6502.06 | +5105.77 | 6100.55 | 9931 | -54.81 |
| incidenteel | 63392 | 102916 | -4052.83 | -7458.69 | +4327.38 | 6414.23 | 9383 | +326.94 |

Wallets met ≥ 10 posities: 6913, waarvan winstgevend: 24%. De top 1% winnaars pakt 31% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -9719.24 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 2833 (24) | 38% | +3.23 | +2.23 | +0% | 15.85 | ja | 18 s | +2.10 / +1.13 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1186 (6) | 64% | +2.46 | +2.38 | +8% | 15.34 | ja | 4 s | +1.36 / +1.09 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 872 (20) | 58% | +1.77 | +1.62 | +5% | 11.62 | ja | 4 s | +1.42 / +0.35 |
| 4 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.22 | ja | 71 s | +9.88 / +3.59 |
| 5 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.44 | ja | 20 s | +9.44 / +4.07 |
| 6 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 1684 (13) | 63% | +0.25 | +0.23 | +2% | 8.28 | nee | 4 s | +0.15 / +0.10 |
| 7 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 370 (3) | 44% | +5.06 | +4.02 | +4% | 7.82 | nee | 28 s | +3.63 / +1.43 |
| 8 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 320 (6) | 71% | +3.23 | +2.97 | +3% | 7.72 | nee | 11 s | +2.02 / +1.21 |
| 9 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 337 (5) | 68% | +2.59 | +2.35 | +3% | 7.7 | nee | 12 s | +1.20 / +1.39 |
| 10 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 394 (1) | 49% | +3.54 | +3.18 | +3% | 7.63 | nee | 70 s | +3.19 / +0.36 |
| 11 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 499 (17) | 46% | +7.32 | +5.99 | +4% | 7.48 | nee | 2 min | +5.34 / +1.98 |
| 12 | [8KUY…hCQF](https://solscan.io/account/8KUYGivN8zgRfKiLTeHBxpk9houRUxJb82NRwUBkhCQF) | bot_hf | 328 (1) | 39% | +0.04 | +0.02 | +1% | 7.42 | nee | 9 s | +0.03 / +0.01 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 643 (9) | 49% | +0.95 | +0.90 | +9% | 7.18 | nee | 4 s | +0.77 / +0.18 |
| 14 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 175 (1) | 59% | +3.96 | +3.13 | +8% | 6.8 | nee | 1 s | +1.29 / +2.66 |
| 15 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 269 (2) | 57% | +0.98 | +0.92 | +5% | 6.57 | nee | 60 s | +0.82 / +0.16 |
| 16 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 20 (0) | 55% | +8.92 | +6.87 | +47% | 6.41 | ja | 63 s | +8.20 / +0.72 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 21 (0) | 67% | +7.88 | +6.30 | +41% | 6.34 | ja | 68 s | +6.21 / +1.68 |
| 18 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 62 (0) | 48% | +18.90 | +15.64 | +24% | 6.31 | ja | 19 s | +12.35 / +6.55 |
| 19 | [F6XJ…Youk](https://solscan.io/account/F6XJTh93VGFcbnf2FJmyR6f3y2HZsav25EeEaZosYouk) | scalper | 311 (0) | 49% | +2.99 | +2.40 | +2% | 6.07 | nee | 18 s | +1.74 / +1.25 |
| 20 | [4WxE…dzhP](https://solscan.io/account/4WxE3GAiFG6EofdSF4N3DWXg5na9V3BQJJN5LuE5dzhP) | scalper | 324 (0) | 50% | +4.01 | +3.52 | +2% | 6.06 | nee | 18 s | +3.53 / +0.48 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 79 (4) | 56% | +31.75 | +24.55 | +18% | 5.62 | nee | 94 s | +31.17 / +0.58 |
| 2 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 101 (0) | 59% | +30.55 | +25.19 | +9% | 5.04 | nee | 15 s | +19.71 / +10.84 |
| 3 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 81 (0) | 83% | +27.48 | +25.34 | +14% | 5.45 | nee | 10 s | +19.48 / +8.00 |
| 4 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | vroege_houder | 6 (0) | 100% | +22.18 | +15.15 | +40% | 3.0 | nee | 67 s | +13.52 / +8.65 |
| 5 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.27 | nee | 8 min | +21.53 / -0.69 |
| 6 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 62 (0) | 48% | +18.90 | +15.64 | +24% | 6.31 | ja | 19 s | +12.35 / +6.55 |
| 7 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 39 (1) | 64% | +17.90 | +15.19 | +14% | 3.88 | nee | 20 s | +12.08 / +5.82 |
| 8 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.15 | nee | 13 s | +1.05 / +16.46 |
| 9 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.97 | nee | 25 s | +17.30 / +0.00 |
| 10 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |
| 11 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 30 (0) | 67% | +16.97 | +13.05 | +12% | 3.11 | nee | 38 s | +1.93 / +15.04 |
| 12 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 56 (8) | 46% | +15.32 | +10.52 | +10% | 3.56 | nee | 116 s | +17.20 / -1.88 |
| 13 | [2KP9…PURD](https://solscan.io/account/2KP9miexioqgNbjPwysggcbi3sKqhH8JsPaDmFxRPURD) | bot_hf | 14 (0) | 71% | +14.56 | +9.46 | +23% | 3.33 | nee | 9 s | +13.97 / +0.59 |
| 14 | [H8UK…FzHm](https://solscan.io/account/H8UKNvUeaqpVT7DZ8TXJVreSQEXDjTA7fEv8hjD3FzHm) | bot_hf | 10 (0) | 80% | +14.56 | +6.88 | +32% | 2.97 | nee | 15 s | +10.23 / +4.33 |
| 15 | [3PwX…pdvA](https://solscan.io/account/3PwXa9BRA2sUdjtcGxs4bVLBau2dHTuZwtb6CbpTpdvA) | scalper | 29 (1) | 55% | +14.02 | +9.42 | +42% | 4.68 | nee | 116 s | +11.19 / +2.83 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 37 (0) | 73% | +13.94 | +11.61 | +11% | 3.4 | nee | 18 s | +9.42 / +4.51 |
| 17 | [5L7a…aBUD](https://solscan.io/account/5L7aqweEkQWzogyyqi1xs2oU2ePseSXQnpnxYrg2aBUD) | bot_hf | 14 (0) | 64% | +13.55 | +8.90 | +22% | 2.8 | nee | 15 s | +3.34 / +10.21 |
| 18 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.44 | ja | 20 s | +9.44 / +4.07 |
| 19 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.22 | ja | 71 s | +9.88 / +3.59 |
| 20 | [69Vp…gAjS](https://solscan.io/account/69Vppxj63mAGdt8fMhgEK9MimbboXn5meMPrLWEegAjS) | scalper | 15 (0) | 67% | +13.29 | +8.73 | +22% | 2.54 | nee | 44 s | +13.29 / +0.00 |

## Geluk-toets

Populatie: 2753 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 9.91 | 4.06 | 5.1 |
| #10 | 5.93 | 3.01 | 3.17 |
| #20 | 4.88 | 2.67 | 2.82 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.1): **18**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 4217 | 48% | +4.3% | -0.4% | +21.19 |
| top 20 op winst (A) | 17/20 | 293 | 50% | +10.3% | +0.0% | +40.21 |
| alle wallets | – | 120346 | 33% | -9.6% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -3.8% / +4.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1068): ρ = 0.457. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 50

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 4217 | 28% | -13.1% | -8.0% | -110.23 |
| 2 s | 4217 | 23% | -16.1% | -10.2% | -135.99 |
| 10 s | 4217 | 22% | -17.0% | -9.9% | -143.37 |
| 60 s | 4217 | 20% | -19.9% | -8.5% | -167.75 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 88

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10710 | 29% | -18.0% | -11.7% | -385.09 |
| 2 s | 10710 | 23% | -21.7% | -15.3% | -463.87 |
| 10 s | 10710 | 19% | -23.9% | -16.2% | -510.98 |
| 60 s | 10710 | 15% | -30.4% | -16.5% | -650.32 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 11

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 669 | 40% | +7.1% | -4.2% | +9.53 |
| 2 s | 669 | 28% | -5.4% | -10.9% | -7.23 |
| 10 s | 669 | 25% | -8.8% | -9.8% | -11.73 |
| 60 s | 669 | 21% | -9.0% | -6.8% | -12.10 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
