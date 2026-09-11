# Wallet-analyse pump.fun — 2026-09-11 09:55 UTC

## Kort antwoord

- Geluk-toets: 15 van 2542 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=9.61, geluk-grens 5.16).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.6% per positie (alle wallets: -10.2%; 12 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.8%, 2 s: -15.9%, 10 s: -17.0%, 60 s: -19.7% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 09:54 UTC (20.1 uur), helft A/B-grens: 2026-09-10 23:51 UTC
- 1104943 trades, 4495 tokens, 80901 wallets, 370164 posities (358484 geopend vanaf ≥ $7k, 11680 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 49079
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6039 | 3989 | -44.04 | -67.51 | +277.00 | 20788.87 | 538 | +29.60 |
| swing | 416 | 3745 | -178.26 | -240.09 | -123.30 | 30.81 | 206 | -0.35 |
| dev | 607 | 2124 | -131.50 | -827.25 | -380.23 | 3643.87 | 252 | -10.23 |
| bot_hf | 1661 | 80327 | -161.08 | -1049.07 | +1437.18 | 5840.52 | 4173 | +158.45 |
| scalper | 11719 | 168025 | -4791.25 | -5982.02 | +4320.30 | 5984.43 | 3151 | -18.17 |
| incidenteel | 60459 | 100274 | -4076.01 | -7450.56 | +3124.90 | 6304.32 | 3360 | +140.10 |

Wallets met ≥ 10 posities: 6514, waarvan winstgevend: 24%. De top 1% winnaars pakt 30% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -9382.14 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 2669 (23) | 38% | +3.31 | +2.31 | +1% | 15.41 | ja | 18 s | +2.45 / +0.87 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1109 (5) | 65% | +2.35 | +2.30 | +8% | 15.06 | ja | 4 s | +1.24 / +1.11 |
| 3 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1188 (27) | 44% | +9.10 | +7.22 | +1% | 11.96 | ja | 24 s | +2.42 / +6.68 |
| 4 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 833 (7) | 48% | +1.49 | +1.02 | +1% | 11.78 | ja | 10 s | +1.26 / +0.23 |
| 5 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 841 (19) | 58% | +2.04 | +1.89 | +6% | 11.43 | ja | 4 s | +1.10 / +0.94 |
| 6 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 533 (15) | 43% | +1.27 | +0.85 | +2% | 9.25 | ja | 57 s | +0.01 / +1.26 |
| 7 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.17 | ja | 71 s | +6.97 / +6.49 |
| 8 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.4 | ja | 20 s | +8.93 / +4.58 |
| 9 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 1605 (13) | 63% | +0.24 | +0.22 | +2% | 7.91 | nee | 4 s | +0.14 / +0.10 |
| 10 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 327 (5) | 69% | +2.81 | +2.57 | +3% | 7.72 | nee | 12 s | +1.33 / +1.48 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 331 (3) | 44% | +5.28 | +4.24 | +5% | 7.7 | nee | 26 s | +3.63 / +1.65 |
| 12 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 313 (6) | 71% | +3.29 | +3.02 | +3% | 7.68 | nee | 11 s | +1.65 / +1.64 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 609 (9) | 49% | +1.03 | +0.99 | +10% | 7.66 | nee | 4 s | +0.64 / +0.39 |
| 14 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 481 (15) | 46% | +7.46 | +6.12 | +4% | 7.44 | nee | 2 min | +5.59 / +1.87 |
| 15 | [8KUY…hCQF](https://solscan.io/account/8KUYGivN8zgRfKiLTeHBxpk9houRUxJb82NRwUBkhCQF) | bot_hf | 303 (1) | 39% | +0.03 | +0.02 | +1% | 7.1 | nee | 10 s | +0.03 / +0.00 |
| 16 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 166 (1) | 61% | +3.69 | +2.86 | +9% | 7.0 | nee | 1 s | +1.11 / +2.58 |
| 17 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 258 (2) | 57% | +0.95 | +0.88 | +5% | 6.42 | nee | 60 s | +0.79 / +0.16 |
| 18 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 20 (0) | 55% | +8.92 | +6.87 | +47% | 6.38 | ja | 63 s | +6.69 / +2.23 |
| 19 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 21 (0) | 67% | +7.88 | +6.30 | +41% | 6.31 | ja | 68 s | +4.81 / +3.08 |
| 20 | [4WxE…dzhP](https://solscan.io/account/4WxE3GAiFG6EofdSF4N3DWXg5na9V3BQJJN5LuE5dzhP) | scalper | 320 (0) | 50% | +4.02 | +3.53 | +2% | 6.04 | nee | 18 s | +3.25 / +0.77 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 79 (4) | 56% | +31.75 | +24.55 | +18% | 5.59 | nee | 94 s | +31.17 / +0.58 |
| 2 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 95 (0) | 59% | +28.95 | +23.59 | +9% | 4.95 | nee | 15 s | +16.20 / +12.75 |
| 3 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 76 (0) | 82% | +23.38 | +21.63 | +13% | 5.06 | nee | 10 s | +17.74 / +5.64 |
| 4 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | vroege_houder | 6 (0) | 100% | +22.18 | +15.15 | +40% | 2.99 | nee | 67 s | +10.46 / +11.72 |
| 5 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.26 | nee | 8 min | -1.24 / +22.08 |
| 6 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.13 | nee | 13 s | +1.05 / +16.46 |
| 7 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.96 | nee | 25 s | +17.30 / +0.00 |
| 8 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |
| 9 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 34 (1) | 68% | +16.52 | +13.81 | +15% | 3.84 | nee | 21 s | +12.08 / +4.44 |
| 10 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 56 (8) | 46% | +15.32 | +10.52 | +10% | 3.54 | nee | 116 s | +17.20 / -1.88 |
| 11 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 58 (0) | 47% | +15.21 | +11.96 | +21% | 5.45 | nee | 19 s | +11.90 / +3.32 |
| 12 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 26 (0) | 65% | +14.90 | +10.97 | +13% | 2.97 | nee | 38 s | +1.93 / +12.97 |
| 13 | [2KP9…PURD](https://solscan.io/account/2KP9miexioqgNbjPwysggcbi3sKqhH8JsPaDmFxRPURD) | bot_hf | 14 (0) | 71% | +14.56 | +9.46 | +23% | 3.32 | nee | 9 s | +13.97 / +0.59 |
| 14 | [H8UK…FzHm](https://solscan.io/account/H8UKNvUeaqpVT7DZ8TXJVreSQEXDjTA7fEv8hjD3FzHm) | bot_hf | 10 (0) | 80% | +14.56 | +6.88 | +32% | 2.95 | nee | 15 s | +0.04 / +14.52 |
| 15 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.4 | ja | 20 s | +8.93 / +4.58 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 21 (0) | 81% | +13.47 | +11.49 | +79% | 9.17 | ja | 71 s | +6.97 / +6.49 |
| 17 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 35 (0) | 71% | +13.32 | +10.99 | +11% | 3.36 | nee | 22 s | +6.83 / +6.49 |
| 18 | [69Vp…gAjS](https://solscan.io/account/69Vppxj63mAGdt8fMhgEK9MimbboXn5meMPrLWEegAjS) | scalper | 15 (0) | 67% | +13.29 | +8.73 | +22% | 2.53 | nee | 44 s | +13.29 / +0.00 |
| 19 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 6 (0) | 83% | +13.13 | +2.14 | +31% | 1.63 | nee | 6 s | +13.13 / +0.00 |
| 20 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 29 (3) | 90% | +12.74 | +11.53 | +14% | 2.97 | nee | 16 s | +11.00 / +1.74 |

## Geluk-toets

Populatie: 2542 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 9.61 | 4.14 | 5.16 |
| #10 | 5.89 | 2.99 | 3.19 |
| #20 | 4.76 | 2.66 | 2.84 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.16): **15**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 4335 | 49% | +4.6% | -0.1% | +25.54 |
| top 20 op winst (A) | 16/20 | 289 | 45% | +4.5% | -2.4% | +16.83 |
| alle wallets | – | 119675 | 32% | -10.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.5% / +3.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1017): ρ = 0.45. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 53

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 4335 | 29% | -12.8% | -7.8% | -111.11 |
| 2 s | 4335 | 24% | -15.9% | -10.1% | -137.79 |
| 10 s | 4335 | 22% | -17.0% | -10.0% | -146.98 |
| 60 s | 4335 | 20% | -19.7% | -8.6% | -170.57 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 133

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 11989 | 29% | -15.9% | -10.2% | -380.97 |
| 2 s | 11989 | 23% | -19.4% | -13.4% | -464.82 |
| 10 s | 11989 | 21% | -21.1% | -13.1% | -506.14 |
| 60 s | 11989 | 17% | -26.6% | -13.4% | -636.50 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 10

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 635 | 39% | +5.8% | -4.5% | +7.36 |
| 2 s | 635 | 27% | -6.6% | -11.0% | -8.39 |
| 10 s | 635 | 25% | -9.3% | -9.8% | -11.85 |
| 60 s | 635 | 20% | -9.9% | -6.8% | -12.54 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
