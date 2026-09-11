# Wallet-analyse pump.fun — 2026-09-11 23:50 UTC

## Kort antwoord

- Geluk-toets: 46 van 4837 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=12.66, geluk-grens 4.98).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.6% per positie (alle wallets: -14.0%; 15 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.1%, 2 s: -13.8%, 10 s: -14.4%, 60 s: -18.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 23:49 UTC (34.0 uur), helft A/B-grens: 2026-09-11 06:48 UTC
- 2860518 trades, 20970 tokens, 141754 wallets, 900061 posities (627709 geopend vanaf ≥ $7k, 272352 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 83242
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7289 | 4571 | +22.94 | -24.30 | +402.64 | 19287.55 | 7227 | +1160.87 |
| dev | 1139 | 3854 | +764.10 | -420.13 | +654.10 | 4640.54 | 5671 | +499.11 |
| swing | 801 | 9687 | -339.86 | -483.43 | -206.74 | 40.02 | 3477 | +40.72 |
| bot_hf | 2355 | 137232 | -18.56 | -1136.00 | +4021.82 | 9113.61 | 101995 | +3916.30 |
| incidenteel | 110814 | 163640 | -6002.08 | -10274.67 | +7065.27 | 7415.52 | 76999 | +4921.08 |
| scalper | 19356 | 308725 | -9268.09 | -11397.08 | +9505.60 | 7238.16 | 76983 | +790.59 |

Wallets met ≥ 10 posities: 10876, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14841.57 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4090 (29) | 38% | +4.50 | +3.50 | +0% | 19.57 | ja | 19 s | +2.70 / +1.80 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2043 (9) | 63% | +5.63 | +5.51 | +9% | 19.33 | ja | 4 s | +2.16 / +3.47 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1491 (32) | 59% | +3.81 | +3.61 | +7% | 15.59 | ja | 4 s | +2.01 / +1.80 |
| 4 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1778 (37) | 45% | +15.65 | +13.50 | +1% | 14.76 | ja | 24 s | +0.82 / +14.82 |
| 5 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1221 (10) | 48% | +5.23 | +4.02 | +1% | 13.21 | ja | 33 s | +0.15 / +5.08 |
| 6 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 916 (24) | 43% | +1.71 | +1.29 | +2% | 11.95 | ja | 61 s | +1.22 / +0.48 |
| 7 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 359 (1) | 61% | +7.54 | +6.71 | +8% | 11.38 | ja | 1 s | +2.61 / +4.93 |
| 8 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1231 (4) | 55% | +0.73 | +0.64 | +1% | 11.14 | ja | 10 s | +0.08 / +0.65 |
| 9 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.91 | ja | 60 s | +13.47 / +10.31 |
| 10 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 722 (4) | 45% | +8.85 | +7.81 | +4% | 10.64 | ja | 30 s | +4.77 / +4.08 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1197 (13) | 52% | +2.12 | +2.06 | +10% | 9.9 | nee | 4 s | +1.04 / +1.08 |
| 12 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 401 (0) | 49% | +6.75 | +5.98 | +5% | 9.84 | ja | 1 s | +1.00 / +5.74 |
| 13 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 264 (15) | 52% | +0.89 | +0.79 | +9% | 9.63 | ja | 7 s | +0.26 / +0.63 |
| 14 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 50 (0) | 56% | +20.69 | +18.64 | +44% | 9.42 | ja | 57 s | +8.92 / +11.77 |
| 15 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 507 (5) | 68% | +2.58 | +2.34 | +2% | 9.3 | ja | 10 s | +2.02 / +0.56 |
| 16 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 737 (28) | 46% | +7.47 | +6.13 | +3% | 9.16 | ja | 2 min | +6.38 / +1.08 |
| 17 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2040 (15) | 63% | +0.33 | +0.31 | +3% | 9.16 | nee | 4 s | +0.21 / +0.12 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (1) | 56% | +16.46 | +14.45 | +37% | 9.01 | ja | 61 s | +7.88 / +8.57 |
| 19 | [HTbm…VpFX](https://solscan.io/account/HTbmNcdJZeMxfRdzw7BGYAC5FbeCapxqyPrRWkEFVpFX) | scalper | 282 (6) | 58% | +1.75 | +1.48 | +3% | 8.99 | ja | 29 s | +0.63 / +1.11 |
| 20 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 390 (1) | 56% | +2.94 | +2.75 | +4% | 8.96 | ja | 3 s | +1.66 / +1.28 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 37 (0) | 78% | +269.26 | +244.34 | +79% | 9.77 | ja | 7 s | -0.81 / +270.07 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.16 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 13 (0) | 100% | +144.35 | +125.89 | +135% | 11.76 | nee | 119 s | +0.00 / +144.35 |
| 4 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 168 (0) | 62% | +69.32 | +63.40 | +12% | 7.3 | ja | 15 s | +26.36 / +42.96 |
| 5 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 13 (0) | 62% | +53.77 | +28.22 | +54% | 5.47 | nee | 119 s | +0.00 / +53.77 |
| 6 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 126 (1) | 76% | +42.33 | +38.73 | +14% | 6.66 | ja | 9 s | +21.85 / +20.48 |
| 7 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 7 (0) | 86% | +35.01 | +26.09 | +64% | 3.23 | nee | 4 s | +0.33 / +34.69 |
| 8 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 85 (12) | 51% | +29.11 | +24.30 | +12% | 5.21 | nee | 95 s | +15.32 / +13.79 |
| 9 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 113 (5) | 52% | +28.35 | +21.15 | +11% | 5.51 | nee | 106 s | +31.17 / -2.82 |
| 10 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | vroege_houder | 17 (0) | 76% | +27.09 | +20.07 | +22% | 3.1 | nee | 21 s | +0.80 / +26.30 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | bot_hf | 50 (3) | 94% | +25.37 | +23.36 | +16% | 3.95 | nee | 15 s | +12.74 / +12.63 |
| 12 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 13 (5) | 62% | +25.34 | +19.57 | +20% | 2.78 | nee | 6 s | +10.52 / +14.83 |
| 13 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 138 (0) | 60% | +24.87 | +22.03 | +6% | 5.01 | nee | 7 s | +7.62 / +17.25 |
| 14 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 39 (0) | 67% | +23.90 | +19.98 | +13% | 3.8 | nee | 31 s | +10.08 / +13.82 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.91 | ja | 60 s | +13.47 / +10.31 |
| 16 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.33 | ja | 80 s | +10.06 / +13.59 |
| 17 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 10 (0) | 90% | +23.51 | +16.48 | +26% | 2.85 | nee | 66 s | +22.18 / +1.33 |
| 18 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.63 | nee | 29 s | -1.00 / +24.15 |
| 19 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 12 (0) | 75% | +22.42 | +11.43 | +27% | 2.84 | nee | 6 s | +13.13 / +9.29 |
| 20 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 13 (0) | 77% | +22.10 | +17.78 | +47% | 4.16 | nee | 18 s | +6.80 / +15.30 |

## Geluk-toets

Populatie: 4837 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 12.66 | 4.23 | 4.98 |
| #10 | 8.71 | 3.22 | 3.42 |
| #20 | 6.93 | 2.91 | 3.08 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 4.98): **46**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 9100 | 49% | +5.6% | -0.2% | +90.91 |
| top 20 op winst (A) | 18/20 | 682 | 56% | +8.5% | +2.9% | +147.16 |
| alle wallets | – | 296229 | 30% | -14.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.7% / +1.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2281): ρ = 0.481. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 105

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 9100 | 30% | -11.1% | -7.4% | -201.85 |
| 2 s | 9100 | 25% | -13.8% | -9.4% | -251.30 |
| 10 s | 9100 | 23% | -14.4% | -9.4% | -261.77 |
| 60 s | 9100 | 20% | -18.2% | -8.3% | -330.63 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 200

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 19819 | 30% | -15.5% | -10.4% | -614.56 |
| 2 s | 19819 | 24% | -19.1% | -13.1% | -756.45 |
| 10 s | 19819 | 21% | -20.4% | -12.8% | -808.10 |
| 60 s | 19819 | 17% | -25.8% | -12.1% | -1020.95 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 16

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 944 | 42% | +5.9% | -3.6% | +11.13 |
| 2 s | 944 | 25% | -10.9% | -11.4% | -20.62 |
| 10 s | 944 | 24% | -11.4% | -9.2% | -21.56 |
| 60 s | 944 | 16% | -10.4% | -5.8% | -19.61 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
