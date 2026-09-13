# Wallet-analyse pump.fun — 2026-09-13 15:40 UTC

## Kort antwoord

- Geluk-toets: 65 van 8150 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.31, geluk-grens 5.48).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.9% per positie (alle wallets: -8.3%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.5%, 2 s: -15.6%, 10 s: -17.0%, 60 s: -20.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 15:36 UTC → 2026-09-13 15:36 UTC (72.0 uur), helft A/B-grens: 2026-09-12 03:36 UTC
- 6110942 trades, 55891 tokens, 199901 wallets, 1854348 posities (976402 geopend vanaf ≥ $7k, 877946 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 138098
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9984 | 5518 | +333.45 | +259.09 | +818.07 | 20617.97 | 22216 | +3441.88 |
| dev | 2133 | 6127 | +1521.65 | -813.70 | +1297.42 | 4574.01 | 14983 | +1193.40 |
| swing | 1870 | 21297 | -961.45 | -1291.85 | -380.07 | 87.58 | 12139 | +39.18 |
| bot_hf | 3030 | 218129 | +115.46 | -1964.98 | +6010.53 | 13473.54 | 304442 | +7733.10 |
| incidenteel | 155172 | 198956 | -6311.77 | -12521.81 | +22548.95 | 8156.61 | 196974 | +9628.66 |
| scalper | 27712 | 526375 | -15129.90 | -18639.03 | +20242.04 | 8214.36 | 327192 | +2393.83 |

Wallets met ≥ 10 posities: 17162, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20432.55 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6975 (83) | 45% | +46.95 | +45.73 | +1% | 26.28 | ja | 24 s | +16.70 / +30.25 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4015 (22) | 62% | +11.97 | +11.84 | +9% | 25.5 | ja | 4 s | +6.52 / +5.45 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3066 (65) | 59% | +7.63 | +7.36 | +6% | 23.81 | ja | 4 s | +4.51 / +3.12 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6942 (57) | 38% | +6.85 | +5.84 | +0% | 22.79 | ja | 19 s | +3.54 / +3.31 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2724 (49) | 46% | +45.42 | +43.27 | +1% | 16.98 | ja | 25 s | +12.32 / +33.10 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2162 (14) | 49% | +9.42 | +8.21 | +1% | 15.94 | ja | 39 s | +6.32 / +3.10 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1577 (32) | 44% | +4.58 | +4.16 | +3% | 14.98 | ja | 60 s | +2.46 / +2.12 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1946 (11) | 52% | +11.25 | +10.52 | +1% | 14.96 | ja | 39 s | +6.71 / +4.54 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 566 (1) | 63% | +13.12 | +12.46 | +10% | 14.37 | ja | 1 s | +9.51 / +3.62 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1993 (8) | 55% | +2.28 | +2.17 | +2% | 13.3 | ja | 10 s | +0.70 / +1.58 |
| 11 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.98 | ja | 119 s | +75.90 / +112.67 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2208 (24) | 52% | +3.71 | +3.64 | +10% | 12.94 | ja | 4 s | +2.29 / +1.41 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1325 (4) | 41% | +11.38 | +10.34 | +3% | 12.18 | ja | 26 s | +9.98 / +1.40 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2631 (2) | 48% | +4.91 | +4.46 | +0% | 12.13 | ja | 7 s | +3.65 / +1.26 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 643 (0) | 50% | +8.86 | +8.09 | +4% | 11.72 | ja | 1 s | +7.53 / +1.33 |
| 16 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.78 | ja | 8 s | +269.26 / +60.38 |
| 17 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1139 (26) | 41% | +1.07 | +0.78 | +1% | 10.77 | ja | 62 s | +0.40 / +0.67 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 73 (1) | 56% | +27.14 | +23.95 | +39% | 10.58 | ja | 53 s | +13.51 / +13.63 |
| 19 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 73 (1) | 56% | +28.61 | +25.59 | +40% | 10.51 | ja | 41 s | +16.81 / +11.80 |
| 20 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 740 (5) | 70% | +4.99 | +4.73 | +2% | 10.49 | ja | 10 s | +2.59 / +2.40 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.08 | nee | 101 s | +86.41 / +366.88 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.78 | ja | 8 s | +269.26 / +60.38 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.03 | nee | 12 s | +206.40 / +112.61 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.98 | ja | 119 s | +75.90 / +112.67 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +158.23 / +0.00 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 265 (0) | 64% | +141.53 | +107.58 | +15% | 8.4 | ja | 15 s | +73.64 / +67.89 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.49 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.45 | nee | 6 s | +52.09 / +33.97 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 187 (1) | 76% | +67.81 | +64.21 | +14% | 7.83 | ja | 9 s | +44.40 / +23.41 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 84 (3) | 96% | +54.63 | +52.01 | +21% | 6.21 | nee | 16 s | +31.62 / +23.00 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.81 | nee | 9 s | +9.56 / +43.32 |
| 12 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 171 (9) | 59% | +49.95 | +42.75 | +14% | 7.35 | ja | 113 s | +23.80 / +26.15 |
| 13 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6975 (83) | 45% | +46.95 | +45.73 | +1% | 26.28 | ja | 24 s | +16.70 / +30.25 |
| 14 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 15 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2724 (49) | 46% | +45.42 | +43.27 | +1% | 16.98 | ja | 25 s | +12.32 / +33.10 |
| 16 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 105 (16) | 54% | +44.77 | +39.96 | +15% | 6.1 | nee | 89 s | +27.31 / +17.46 |
| 17 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 91 (1) | 77% | +44.45 | +39.46 | +13% | 5.54 | nee | 26 s | +22.79 / +21.66 |
| 18 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 24 (3) | 83% | +43.44 | +36.54 | +77% | 9.28 | ja | 7 min | +19.69 / +23.75 |
| 19 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.16 | nee | 112 s | +1.20 / +41.26 |
| 20 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.97 | nee | 97 s | +0.00 / +39.35 |

## Geluk-toets

Populatie: 8150 wallets met ≥ 20 posities, 73 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.31 | 4.55 | 5.48 |
| #10 | 10.45 | 3.46 | 3.65 |
| #20 | 8.88 | 3.18 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.48): **65**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 14136 | 48% | +5.9% | -0.3% | +179.84 |
| top 20 op winst (A) | 16/20 | 440 | 69% | +15.7% | +10.3% | +298.32 |
| alle wallets | – | 327137 | 33% | -8.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.8% / +1.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3459): ρ = 0.476. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 131

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14136 | 29% | -12.5% | -7.7% | -352.76 |
| 2 s | 14136 | 23% | -15.6% | -9.3% | -440.54 |
| 10 s | 14136 | 21% | -17.0% | -9.2% | -480.59 |
| 60 s | 14136 | 19% | -20.9% | -8.7% | -591.28 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 357

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40865 | 30% | -11.7% | -7.5% | -956.62 |
| 2 s | 40865 | 24% | -14.7% | -9.1% | -1199.78 |
| 10 s | 40865 | 22% | -15.8% | -8.9% | -1289.92 |
| 60 s | 40865 | 19% | -19.4% | -8.1% | -1582.00 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 162

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10835 | 32% | -2.2% | -5.6% | -47.44 |
| 2 s | 10835 | 27% | -5.5% | -7.0% | -119.39 |
| 10 s | 10835 | 26% | -6.1% | -6.9% | -132.93 |
| 60 s | 10835 | 24% | -6.3% | -5.8% | -136.16 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
