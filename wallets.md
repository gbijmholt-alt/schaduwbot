# Wallet-analyse pump.fun — 2026-09-11 08:53 UTC

## Kort antwoord

- Geluk-toets: 15 van 2481 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=9.22, geluk-grens 5.18).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +3.1% per positie (alle wallets: -10.1%; 10 van 17 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -10.0%, 2 s: -12.8%, 10 s: -13.5%, 60 s: -15.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 08:52 UTC (19.1 uur), helft A/B-grens: 2026-09-10 23:20 UTC
- 1045578 trades, 3575 tokens, 79415 wallets, 353579 posities (352960 geopend vanaf ≥ $7k, 619 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 48153
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6031 | 3927 | -74.49 | -97.91 | +246.35 | 20693.24 | 18 | -0.28 |
| swing | 406 | 3510 | -170.57 | -226.79 | -119.50 | 25.45 | 1 | -0.00 |
| dev | 582 | 2076 | -133.23 | -813.26 | -403.59 | 3653.92 | 16 | -5.99 |
| bot_hf | 1653 | 79078 | -145.26 | -1035.04 | +1443.32 | 5955.62 | 310 | +12.45 |
| scalper | 11548 | 164896 | -4675.59 | -5836.76 | +3980.53 | 5921.69 | 97 | -0.97 |
| incidenteel | 59195 | 99473 | -4055.36 | -7421.96 | +2068.81 | 6205.61 | 177 | +9.40 |

Wallets met ≥ 10 posities: 6418, waarvan winstgevend: 24%. De top 1% winnaars pakt 30% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -9254.51 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1084 (5) | 65% | +2.25 | +2.20 | +8% | 14.71 | ja | 4 s | +1.24 / +1.00 |
| 2 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1169 (27) | 44% | +8.51 | +6.63 | +1% | 11.87 | ja | 24 s | +2.81 / +5.70 |
| 3 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 820 (6) | 48% | +1.51 | +1.05 | +1% | 11.72 | ja | 10 s | +1.08 / +0.43 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 831 (18) | 58% | +2.08 | +1.93 | +7% | 11.37 | ja | 4 s | +1.06 / +1.02 |
| 5 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.16 | ja | 71 s | +6.97 / +6.49 |
| 6 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.38 | ja | 20 s | +8.93 / +4.58 |
| 7 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 1583 (13) | 63% | +0.24 | +0.22 | +2% | 7.82 | nee | 4 s | +0.14 / +0.10 |
| 8 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 322 (5) | 69% | +2.77 | +2.53 | +3% | 7.69 | nee | 12 s | +1.22 / +1.55 |
| 9 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 310 (6) | 71% | +3.31 | +3.05 | +3% | 7.67 | nee | 11 s | +1.63 / +1.68 |
| 10 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 373 (1) | 48% | +3.82 | +3.46 | +3% | 7.66 | nee | 70 s | +3.62 / +0.21 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 601 (9) | 49% | +0.99 | +0.95 | +10% | 7.48 | nee | 4 s | +0.65 / +0.35 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 311 (3) | 44% | +4.81 | +3.77 | +5% | 7.41 | nee | 28 s | +2.71 / +2.10 |
| 13 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 470 (15) | 46% | +7.10 | +5.76 | +4% | 7.3 | nee | 2 min | +5.17 / +1.93 |
| 14 | [8KUY…hCQF](https://solscan.io/account/8KUYGivN8zgRfKiLTeHBxpk9houRUxJb82NRwUBkhCQF) | bot_hf | 243 (1) | 39% | +0.04 | +0.02 | +1% | 6.99 | nee | 11 s | +0.03 / +0.00 |
| 15 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 149 (1) | 60% | +3.30 | +2.47 | +9% | 6.52 | nee | 1 s | +0.77 / +2.53 |
| 16 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 255 (2) | 57% | +0.96 | +0.90 | +5% | 6.48 | nee | 60 s | +0.71 / +0.25 |
| 17 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 20 (0) | 55% | +8.92 | +6.87 | +47% | 6.37 | ja | 63 s | +6.69 / +2.23 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 21 (0) | 67% | +7.88 | +6.30 | +41% | 6.3 | ja | 68 s | +4.81 / +3.08 |
| 19 | [4WxE…dzhP](https://solscan.io/account/4WxE3GAiFG6EofdSF4N3DWXg5na9V3BQJJN5LuE5dzhP) | scalper | 313 (0) | 50% | +3.82 | +3.33 | +2% | 5.96 | nee | 18 s | +3.34 / +0.48 |
| 20 | [F6XJ…Youk](https://solscan.io/account/F6XJTh93VGFcbnf2FJmyR6f3y2HZsav25EeEaZosYouk) | scalper | 295 (0) | 50% | +2.98 | +2.38 | +2% | 5.89 | nee | 18 s | +1.37 / +1.61 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 79 (4) | 56% | +31.75 | +24.55 | +18% | 5.59 | nee | 94 s | +27.82 / +3.93 |
| 2 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | bot_hf | 93 (0) | 59% | +31.18 | +25.81 | +10% | 4.99 | nee | 14 s | +16.13 / +15.05 |
| 3 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 74 (0) | 81% | +22.89 | +21.14 | +13% | 5.02 | nee | 10 s | +17.74 / +5.15 |
| 4 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | vroege_houder | 6 (0) | 100% | +22.18 | +15.15 | +40% | 2.98 | nee | 67 s | +10.46 / +11.72 |
| 5 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.26 | nee | 8 min | +0.00 / +20.83 |
| 6 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.12 | nee | 13 s | +1.05 / +16.46 |
| 7 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.95 | nee | 25 s | +17.30 / +0.00 |
| 8 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |
| 9 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 33 (1) | 70% | +16.74 | +14.02 | +15% | 3.9 | nee | 21 s | +11.77 / +4.97 |
| 10 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 56 (8) | 46% | +15.32 | +10.52 | +10% | 3.53 | nee | 116 s | +17.20 / -1.88 |
| 11 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 58 (0) | 47% | +15.21 | +11.96 | +21% | 5.44 | nee | 19 s | +12.13 / +3.08 |
| 12 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 25 (0) | 68% | +15.03 | +11.10 | +13% | 2.95 | nee | 39 s | +1.93 / +13.10 |
| 13 | [2KP9…PURD](https://solscan.io/account/2KP9miexioqgNbjPwysggcbi3sKqhH8JsPaDmFxRPURD) | bot_hf | 14 (0) | 71% | +14.56 | +9.46 | +23% | 3.31 | nee | 9 s | +12.02 / +2.54 |
| 14 | [H8UK…FzHm](https://solscan.io/account/H8UKNvUeaqpVT7DZ8TXJVreSQEXDjTA7fEv8hjD3FzHm) | bot_hf | 10 (0) | 80% | +14.56 | +6.88 | +32% | 2.95 | nee | 15 s | +0.04 / +14.52 |
| 15 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.38 | ja | 20 s | +8.93 / +4.58 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.16 | ja | 71 s | +6.97 / +6.49 |
| 17 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 35 (0) | 71% | +13.32 | +10.99 | +11% | 3.36 | nee | 22 s | +7.12 / +6.20 |
| 18 | [69Vp…gAjS](https://solscan.io/account/69Vppxj63mAGdt8fMhgEK9MimbboXn5meMPrLWEegAjS) | scalper | 15 (0) | 67% | +13.29 | +8.73 | +22% | 2.52 | nee | 44 s | +13.29 / +0.00 |
| 19 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 6 (0) | 83% | +13.13 | +2.14 | +31% | 1.63 | nee | 6 s | +13.13 / +0.00 |
| 20 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 29 (3) | 90% | +12.74 | +11.53 | +14% | 2.96 | nee | 16 s | +11.00 / +1.74 |

## Geluk-toets

Populatie: 2481 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 9.22 | 4.19 | 5.18 |
| #10 | 5.86 | 2.97 | 3.18 |
| #20 | 4.72 | 2.65 | 2.8 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.18): **15**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 17/20 | 3852 | 46% | +3.1% | -1.1% | +22.58 |
| top 20 op winst (A) | 15/20 | 270 | 48% | +9.1% | +0.0% | +36.54 |
| alle wallets | – | 123411 | 32% | -10.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -3.9% / +4.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1026): ρ = 0.481. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 71

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 3852 | 30% | -10.0% | -7.2% | -76.69 |
| 2 s | 3852 | 25% | -12.8% | -9.1% | -98.49 |
| 10 s | 3852 | 23% | -13.5% | -8.5% | -104.33 |
| 60 s | 3852 | 21% | -15.6% | -7.1% | -120.52 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 95

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 9232 | 29% | -19.6% | -13.1% | -362.18 |
| 2 s | 9232 | 23% | -23.2% | -17.7% | -427.84 |
| 10 s | 9232 | 19% | -25.6% | -18.4% | -473.22 |
| 60 s | 9232 | 14% | -32.4% | -20.3% | -598.90 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 10

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 629 | 40% | +6.0% | -4.4% | +7.55 |
| 2 s | 629 | 28% | -6.5% | -10.9% | -8.18 |
| 10 s | 629 | 25% | -9.3% | -9.8% | -11.76 |
| 60 s | 629 | 20% | -10.0% | -6.8% | -12.53 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
