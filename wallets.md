# Wallet-analyse pump.fun — 2026-09-12 21:36 UTC

## Kort antwoord

- Geluk-toets: 50 van 6863 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.16, geluk-grens 5.53).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.7% per positie (alle wallets: -11.0%; 19 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -10.8%, 2 s: -14.1%, 10 s: -15.0%, 60 s: -18.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 21:34 UTC (55.8 uur), helft A/B-grens: 2026-09-11 17:41 UTC
- 4636829 trades, 40195 tokens, 177416 wallets, 1409623 posities (846701 geopend vanaf ≥ $7k, 562922 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 116868
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9150 | 5337 | +5.50 | -56.52 | +519.26 | 20731.98 | 15546 | +2416.01 |
| dev | 1728 | 5259 | +1175.58 | -674.93 | +912.10 | 4892.43 | 11379 | +930.81 |
| swing | 1483 | 16998 | -719.53 | -998.14 | -344.89 | 62.68 | 7205 | +44.26 |
| bot_hf | 2790 | 187110 | +12.17 | -1842.81 | +4888.82 | 11928.09 | 214306 | +6921.00 |
| incidenteel | 137573 | 190024 | -6362.13 | -12313.24 | +14530.17 | 8560.57 | 130578 | +7763.56 |
| scalper | 24692 | 441973 | -12671.56 | -15573.55 | +14764.78 | 8562.91 | 183908 | +1691.52 |

Wallets met ≥ 10 posities: 14624, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18559.98 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5720 (75) | 45% | +29.72 | +28.50 | +1% | 24.56 | ja | 23 s | +3.35 / +26.36 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3148 (17) | 62% | +8.55 | +8.41 | +9% | 23.22 | ja | 4 s | +3.04 / +5.51 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5830 (44) | 38% | +7.01 | +6.00 | +1% | 22.21 | ja | 19 s | +4.31 / +2.70 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2374 (47) | 59% | +6.43 | +6.16 | +7% | 21.63 | ja | 4 s | +2.33 / +4.10 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2085 (21) | 51% | +3.46 | +2.54 | +0% | 17.64 | ja | 10 s | +0.15 / +3.31 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2414 (44) | 44% | +23.48 | +21.33 | +1% | 16.31 | ja | 24 s | +13.40 / +10.08 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1765 (13) | 48% | +3.49 | +2.28 | +0% | 15.04 | ja | 38 s | +2.21 / +1.29 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1679 (11) | 51% | +7.90 | +7.17 | +1% | 14.34 | ja | 37 s | +1.13 / +6.77 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1271 (27) | 44% | +3.44 | +3.02 | +3% | 14.07 | ja | 61 s | +1.36 / +2.08 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 496 (1) | 62% | +11.70 | +10.87 | +10% | 13.67 | ja | 1 s | +5.66 / +6.04 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1710 (6) | 55% | +1.50 | +1.40 | +1% | 12.75 | ja | 10 s | +0.39 / +1.11 |
| 12 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.82 | ja | 15 s | +0.99 / +0.07 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1083 (4) | 42% | +10.79 | +9.75 | +3% | 11.82 | ja | 28 s | +5.57 / +5.23 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1760 (23) | 52% | +3.00 | +2.94 | +10% | 11.82 | ja | 4 s | +1.30 / +1.70 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 558 (0) | 49% | +7.90 | +7.13 | +4% | 11.33 | ja | 1 s | +4.78 / +3.12 |
| 16 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1916 (2) | 49% | +5.54 | +5.09 | +1% | 11.22 | nee | 7 s | +2.59 / +2.95 |
| 17 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 337 (3) | 59% | +11.24 | +9.27 | +5% | 10.84 | ja | 8 s | +3.65 / +7.59 |
| 18 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +78.03 / +251.61 |
| 19 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 75 (1) | 57% | +23.08 | +21.07 | +33% | 10.26 | ja | 52 s | +12.80 / +10.28 |
| 20 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 75 (1) | 59% | +25.91 | +23.92 | +36% | 10.09 | ja | 48 s | +18.91 / +7.00 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +78.03 / +251.61 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.65 | nee | 12 s | +170.06 / +122.15 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.93 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 229 (0) | 62% | +128.65 | +94.69 | +15% | 8.29 | ja | 15 s | +50.13 / +78.52 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.21 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 21 (5) | 76% | +60.81 | +48.97 | +31% | 4.54 | nee | 6 s | +13.73 / +47.08 |
| 8 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 172 (1) | 77% | +58.95 | +55.34 | +14% | 7.48 | ja | 9 s | +30.98 / +27.97 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 72 (3) | 96% | +44.62 | +42.52 | +20% | 5.58 | nee | 16 s | +19.71 / +24.91 |
| 12 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.6 | nee | 106 s | +31.47 / +10.49 |
| 13 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.94 | ja | 6 min | +9.85 / +29.47 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | -0.24 / +38.62 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 97 (14) | 53% | +37.70 | +32.89 | +13% | 5.82 | nee | 89 s | +21.36 / +16.33 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 80 (0) | 76% | +32.90 | +30.57 | +12% | 5.17 | nee | 24 s | +19.45 / +13.46 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5720 (75) | 45% | +29.72 | +28.50 | +1% | 24.56 | ja | 23 s | +3.35 / +26.36 |
| 18 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 151 (0) | 48% | +27.69 | +23.97 | +15% | 7.18 | ja | 13 s | +17.71 / +9.98 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 10 (0) | 70% | +27.03 | +12.48 | +65% | 4.99 | nee | 12 s | +17.52 / +9.51 |

## Geluk-toets

Populatie: 6863 wallets met ≥ 20 posities, 88 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.16 | 4.42 | 5.53 |
| #10 | 9.67 | 3.38 | 3.65 |
| #20 | 7.7 | 3.07 | 3.19 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.53): **50**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 14380 | 48% | +5.7% | -0.3% | +113.62 |
| top 20 op winst (A) | 18/20 | 744 | 62% | +12.5% | +5.1% | +478.93 |
| alle wallets | – | 361940 | 32% | -11.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.8% / +2.2% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3433): ρ = 0.527. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 128

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14380 | 30% | -10.8% | -7.2% | -311.64 |
| 2 s | 14380 | 24% | -14.1% | -8.7% | -406.29 |
| 10 s | 14380 | 22% | -15.0% | -8.5% | -431.88 |
| 60 s | 14380 | 19% | -18.4% | -7.8% | -529.62 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 310

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 35613 | 31% | -10.9% | -7.1% | -779.75 |
| 2 s | 35613 | 25% | -13.9% | -8.6% | -992.45 |
| 10 s | 35613 | 23% | -14.8% | -8.4% | -1052.62 |
| 60 s | 35613 | 19% | -17.9% | -7.4% | -1278.15 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 98

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6869 | 32% | -1.7% | -5.3% | -23.00 |
| 2 s | 6869 | 27% | -5.4% | -6.8% | -74.09 |
| 10 s | 6869 | 25% | -6.4% | -6.7% | -87.81 |
| 60 s | 6869 | 22% | -6.3% | -5.7% | -86.90 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
