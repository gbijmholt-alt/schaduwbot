# Wallet-analyse pump.fun — 2026-09-11 21:45 UTC

## Kort antwoord

- Geluk-toets: 34 van 4395 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=11.98, geluk-grens 5.34).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.7% per positie (alle wallets: -13.9%; 14 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.2%, 2 s: -14.5%, 10 s: -15.2%, 60 s: -19.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 21:43 UTC (31.9 uur), helft A/B-grens: 2026-09-11 05:46 UTC
- 2537772 trades, 18147 tokens, 132608 wallets, 802237 posities (576157 geopend vanaf ≥ $7k, 226080 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 76788
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6997 | 4544 | +11.88 | -32.18 | +397.41 | 19516.04 | 6085 | +1018.07 |
| swing | 693 | 8508 | -290.23 | -410.09 | -177.02 | 34.64 | 3119 | +3.56 |
| dev | 1041 | 3565 | +648.74 | -446.67 | +556.45 | 4638.63 | 4632 | +408.22 |
| bot_hf | 2219 | 124792 | -21.60 | -1077.36 | +4027.56 | 8667.62 | 83110 | +3469.95 |
| incidenteel | 103710 | 154097 | -5927.70 | -9661.95 | +6549.00 | 6743.40 | 67585 | +4137.17 |
| scalper | 17948 | 280651 | -8294.88 | -10230.68 | +8974.83 | 6941.53 | 61549 | +624.13 |

Wallets met ≥ 10 posities: 10013, waarvan winstgevend: 21%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -13873.79 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 3367 (51) | 45% | +10.93 | +9.71 | +1% | 20.09 | ja | 21 s | +0.12 / +10.82 |
| 2 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 3663 (34) | 38% | +3.79 | +2.79 | +0% | 18.71 | ja | 19 s | +2.37 / +1.43 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1877 (7) | 63% | +4.98 | +4.88 | +9% | 18.47 | ja | 4 s | +2.04 / +2.95 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1369 (28) | 59% | +3.58 | +3.37 | +7% | 15.01 | ja | 4 s | +1.88 / +1.69 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1647 (36) | 45% | +13.36 | +11.22 | +1% | 14.18 | ja | 24 s | +1.19 / +12.18 |
| 6 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 851 (23) | 43% | +1.87 | +1.45 | +2% | 11.81 | ja | 61 s | +0.92 / +0.95 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1119 (4) | 55% | +0.52 | +0.43 | +1% | 10.74 | ja | 10 s | +0.03 / +0.49 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 330 (1) | 60% | +6.22 | +5.39 | +7% | 10.57 | ja | 1 s | +2.19 / +4.03 |
| 9 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.43 | ja | 77 s | +13.47 / +5.44 |
| 10 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 630 (4) | 43% | +7.51 | +6.47 | +4% | 10.12 | ja | 28 s | +4.74 / +2.77 |
| 11 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 257 (13) | 52% | +0.91 | +0.81 | +9% | 9.69 | ja | 7 s | +0.27 / +0.64 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1099 (14) | 51% | +1.91 | +1.85 | +10% | 9.32 | nee | 4 s | +0.91 / +1.00 |
| 13 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 382 (0) | 49% | +5.91 | +5.15 | +4% | 9.29 | ja | 1 s | +0.11 / +5.81 |
| 14 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2040 (15) | 63% | +0.33 | +0.31 | +3% | 9.21 | nee | 4 s | +0.19 / +0.15 |
| 15 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 465 (5) | 70% | +3.18 | +2.93 | +2% | 9.16 | ja | 11 s | +1.64 / +1.53 |
| 16 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 49 (1) | 51% | +14.58 | +10.96 | +43% | 9.0 | ja | 23 s | +13.53 / +1.05 |
| 17 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 359 (1) | 56% | +2.95 | +2.75 | +4% | 8.98 | ja | 3 s | +1.76 / +1.19 |
| 18 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 675 (25) | 46% | +5.82 | +4.49 | +2% | 8.65 | nee | 2 min | +5.54 / +0.28 |
| 19 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 436 (6) | 71% | +3.00 | +2.73 | +2% | 8.63 | ja | 10 s | +2.38 / +0.61 |
| 20 | [5Vox…UA6U](https://solscan.io/account/5Voxqwa8y9KRJNY71mrKHHs5MEVwuVVdySCJExrrUA6U) | bot_hf | 132 (4) | 55% | +3.09 | +0.98 | +6% | 8.54 | ja | 15 s | +0.11 / +2.98 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 37 (0) | 78% | +269.26 | +244.34 | +79% | 9.83 | ja | 7 s | -0.81 / +270.07 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.25 | nee | 13 s | +0.00 / +206.40 |
| 3 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 157 (0) | 62% | +56.68 | +51.32 | +11% | 6.91 | nee | 15 s | +26.76 / +29.93 |
| 4 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 6 (1) | 83% | +49.07 | +30.87 | +111% | 6.45 | nee | 4 min | +0.00 / +49.07 |
| 5 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 115 (1) | 76% | +37.51 | +33.91 | +13% | 6.41 | nee | 9 s | +21.85 / +15.66 |
| 6 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 7 (0) | 86% | +35.01 | +26.09 | +64% | 3.22 | nee | 4 s | +0.33 / +34.69 |
| 7 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 113 (5) | 52% | +28.35 | +21.15 | +11% | 5.53 | nee | 106 s | +31.17 / -2.82 |
| 8 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 80 (11) | 50% | +28.10 | +23.30 | +12% | 5.08 | nee | 100 s | +15.32 / +12.78 |
| 9 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | vroege_houder | 17 (0) | 76% | +27.09 | +20.07 | +22% | 3.11 | nee | 21 s | +0.69 / +26.40 |
| 10 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 138 (0) | 60% | +24.87 | +22.03 | +6% | 5.03 | nee | 7 s | +7.62 / +17.25 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | bot_hf | 48 (3) | 94% | +24.66 | +22.66 | +17% | 4.0 | nee | 14 s | +12.74 / +11.93 |
| 12 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.37 | ja | 80 s | +10.06 / +13.59 |
| 13 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.64 | nee | 29 s | -3.26 / +26.41 |
| 14 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 54 (0) | 80% | +22.83 | +20.50 | +12% | 4.5 | nee | 24 s | +13.32 / +9.50 |
| 15 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 8 (0) | 88% | +22.48 | +15.45 | +30% | 2.91 | nee | 67 s | +20.58 / +1.90 |
| 16 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 13 (0) | 77% | +22.10 | +17.78 | +47% | 4.19 | nee | 18 s | +6.80 / +15.30 |
| 17 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 8 (0) | 62% | +21.18 | +6.62 | +69% | 4.55 | nee | 13 s | +17.52 / +3.66 |
| 18 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | scalper | 9 (1) | 22% | +20.18 | -3.66 | +50% | -0.25 | nee | 90 s | +20.83 / -0.66 |
| 19 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 11 (0) | 73% | +20.13 | +9.14 | +28% | 2.73 | nee | 5 s | +13.13 / +7.00 |
| 20 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 15 (3) | 80% | +19.76 | +16.18 | +61% | 5.93 | nee | 7 min | +2.74 / +17.02 |

## Geluk-toets

Populatie: 4395 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 11.98 | 4.26 | 5.34 |
| #10 | 8.0 | 3.19 | 3.39 |
| #20 | 6.58 | 2.88 | 3.03 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.34): **34**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 7256 | 49% | +5.7% | -0.1% | +58.95 |
| top 20 op winst (A) | 18/20 | 620 | 55% | +5.9% | +2.4% | +100.35 |
| alle wallets | – | 254149 | 30% | -13.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.0% / +1.4% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1965): ρ = 0.48. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 111

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7256 | 29% | -12.2% | -7.7% | -176.33 |
| 2 s | 7256 | 25% | -14.5% | -9.6% | -210.62 |
| 10 s | 7256 | 23% | -15.2% | -9.7% | -220.71 |
| 60 s | 7256 | 20% | -19.4% | -8.5% | -281.34 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 241

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20778 | 30% | -14.5% | -9.3% | -601.19 |
| 2 s | 20778 | 24% | -17.4% | -11.2% | -724.31 |
| 10 s | 20778 | 21% | -18.8% | -11.2% | -780.70 |
| 60 s | 20778 | 17% | -23.8% | -10.5% | -990.69 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 17

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 876 | 41% | +4.2% | -3.6% | +7.42 |
| 2 s | 876 | 26% | -10.0% | -10.7% | -17.45 |
| 10 s | 876 | 24% | -10.5% | -8.5% | -18.34 |
| 60 s | 876 | 16% | -10.0% | -5.9% | -17.58 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
