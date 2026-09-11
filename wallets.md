# Wallet-analyse pump.fun — 2026-09-11 18:07 UTC

## Kort antwoord

- Geluk-toets: 26 van 3669 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=10.1, geluk-grens 5.11).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -13.7%; 13 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -14.4%, 2 s: -17.1%, 10 s: -17.9%, 60 s: -21.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 18:07 UTC (28.3 uur), helft A/B-grens: 2026-09-11 03:57 UTC
- 1996386 trades, 13476 tokens, 115882 wallets, 637569 posities (488514 geopend vanaf ≥ $7k, 149055 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 65165
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6758 | 4557 | -7.95 | -40.83 | +399.28 | 20298.45 | 4645 | +587.25 |
| swing | 608 | 6577 | -257.47 | -351.22 | -151.94 | 30.93 | 2009 | -3.43 |
| dev | 885 | 2885 | +403.48 | -509.76 | +422.89 | 4092.75 | 3051 | +232.82 |
| bot_hf | 1931 | 104218 | -145.65 | -1116.33 | +1744.04 | 7533.20 | 51438 | +2261.90 |
| scalper | 15482 | 234461 | -6884.17 | -8561.04 | +9505.98 | 6626.72 | 40045 | +264.82 |
| incidenteel | 90218 | 135816 | -5260.43 | -8813.26 | +6044.06 | 6656.81 | 47867 | +2562.33 |

Wallets met ≥ 10 posities: 8538, waarvan winstgevend: 22%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -12152.19 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 2835 (36) | 44% | +3.83 | +2.61 | +0% | 18.2 | ja | 21 s | +1.58 / +2.25 |
| 2 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 3331 (27) | 38% | +4.48 | +3.47 | +1% | 17.71 | ja | 19 s | +2.16 / +2.32 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1546 (6) | 63% | +3.07 | +2.98 | +7% | 16.28 | ja | 4 s | +1.66 / +1.41 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1135 (23) | 59% | +2.42 | +2.27 | +6% | 12.69 | ja | 4 s | +1.50 / +0.92 |
| 5 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 730 (21) | 43% | +1.34 | +0.92 | +2% | 10.54 | ja | 60 s | +0.94 / +0.40 |
| 6 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 981 (5) | 54% | +0.40 | +0.31 | +1% | 9.7 | nee | 10 s | +0.11 / +0.29 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 262 (1) | 61% | +5.78 | +4.95 | +8% | 9.63 | ja | 1 s | +2.04 / +3.74 |
| 9 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 45 (0) | 53% | +13.76 | +10.14 | +49% | 9.45 | ja | 20 s | +13.02 / +0.75 |
| 10 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2040 (15) | 63% | +0.33 | +0.31 | +3% | 9.17 | nee | 4 s | +0.17 / +0.17 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 492 (4) | 44% | +6.23 | +5.19 | +4% | 8.94 | ja | 31 s | +4.40 / +1.83 |
| 12 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | scalper | 590 (23) | 46% | +7.08 | +5.74 | +3% | 8.53 | nee | 2 min | +5.13 / +1.95 |
| 13 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 462 (3) | 48% | +3.67 | +3.30 | +2% | 8.3 | nee | 70 s | +3.28 / +0.39 |
| 14 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 403 (5) | 69% | +2.38 | +2.13 | +2% | 8.24 | nee | 11 s | +1.66 / +0.72 |
| 15 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 30 (0) | 57% | +12.95 | +10.90 | +47% | 8.09 | ja | 67 s | +8.92 / +4.03 |
| 16 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 31 (0) | 64% | +12.80 | +10.79 | +46% | 8.07 | ja | 70 s | +7.88 / +4.92 |
| 17 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 827 (9) | 51% | +1.27 | +1.22 | +9% | 7.89 | nee | 4 s | +0.85 / +0.42 |
| 18 | [6rH3…try1](https://solscan.io/account/6rH3c2DLQvd8CSNVF4geb6GLWYPBSeTqepALSfKbtry1) | bot_hf | 263 (2) | 56% | +2.27 | +2.08 | +4% | 7.54 | nee | 3 s | +1.48 / +0.79 |
| 19 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.34 | ja | 80 s | +10.06 / +13.59 |
| 20 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 320 (2) | 57% | +1.16 | +1.09 | +5% | 7.32 | nee | 60 s | +0.84 / +0.32 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.19 | nee | 13 s | +0.00 / +206.40 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 15 (0) | 73% | +88.89 | +73.39 | +79% | 5.87 | nee | 9 s | -0.81 / +89.69 |
| 3 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 126 (0) | 64% | +50.13 | +44.77 | +12% | 6.15 | nee | 15 s | +23.75 / +26.38 |
| 4 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 102 (5) | 54% | +31.52 | +24.32 | +14% | 5.82 | nee | 94 s | +31.17 / +0.35 |
| 5 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 96 (1) | 76% | +30.98 | +27.37 | +13% | 5.72 | nee | 9 s | +20.22 / +10.76 |
| 6 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.34 | ja | 80 s | +10.06 / +13.59 |
| 7 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.62 | nee | 29 s | -4.42 / +27.57 |
| 8 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 13 (0) | 77% | +22.10 | +17.78 | +47% | 4.17 | nee | 18 s | +6.80 / +15.30 |
| 9 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 68 (9) | 50% | +21.36 | +16.56 | +11% | 4.27 | nee | 108 s | +17.75 / +3.61 |
| 10 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 7 (0) | 86% | +20.96 | +13.93 | +32% | 2.76 | nee | 73 s | +13.89 / +7.06 |
| 11 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.26 | nee | 8 min | +21.46 / -0.62 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 41 (4) | 90% | +20.49 | +18.49 | +16% | 3.58 | nee | 16 s | +12.61 / +7.88 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 49 (0) | 78% | +19.61 | +17.28 | +12% | 4.06 | nee | 24 s | +13.32 / +6.29 |
| 14 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 45 (2) | 60% | +19.07 | +16.36 | +13% | 4.12 | nee | 19 s | +11.84 / +7.24 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 31 (0) | 74% | +18.91 | +16.93 | +70% | 10.38 | ja | 77 s | +13.47 / +5.44 |
| 16 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 33 (0) | 67% | +18.60 | +14.68 | +12% | 3.28 | nee | 37 s | +8.90 / +9.70 |
| 17 | [K6Eh…KHnR](https://solscan.io/account/K6Eh9fwKkrhVNq6SpRtJn7F4Myi3HUst5QP8x5BKHnR) | dev | 166 (6) | 40% | +17.90 | +9.86 | +5% | 4.88 | nee | 15 s | -0.35 / +18.25 |
| 18 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.11 | nee | 13 s | +1.05 / +16.46 |
| 19 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.94 | nee | 25 s | +17.30 / +0.00 |
| 20 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 70 (0) | 46% | +17.16 | +13.90 | +20% | 5.8 | nee | 17 s | +13.04 / +4.11 |

## Geluk-toets

Populatie: 3669 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 10.1 | 4.24 | 5.11 |
| #10 | 7.32 | 3.12 | 3.36 |
| #20 | 5.72 | 2.82 | 2.96 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.11): **26**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 5328 | 48% | +5.1% | -0.3% | +38.96 |
| top 20 op winst (A) | 18/20 | 357 | 58% | +12.7% | +3.6% | +96.79 |
| alle wallets | – | 187133 | 30% | -13.7% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.0% / +2.4% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1503): ρ = 0.447. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 63

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 5328 | 28% | -14.4% | -8.5% | -153.16 |
| 2 s | 5328 | 23% | -17.1% | -10.2% | -182.16 |
| 10 s | 5328 | 22% | -17.9% | -10.4% | -191.26 |
| 60 s | 5328 | 20% | -21.4% | -9.2% | -228.49 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 162

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 16375 | 29% | -15.8% | -9.9% | -515.71 |
| 2 s | 16375 | 24% | -19.0% | -12.3% | -622.56 |
| 10 s | 16375 | 21% | -20.8% | -12.5% | -682.18 |
| 60 s | 16375 | 17% | -26.2% | -12.2% | -856.73 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 17

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 925 | 40% | +5.4% | -5.0% | +9.95 |
| 2 s | 925 | 26% | -7.2% | -11.0% | -13.30 |
| 10 s | 925 | 25% | -7.3% | -8.5% | -13.42 |
| 60 s | 925 | 19% | -8.6% | -6.0% | -15.91 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
