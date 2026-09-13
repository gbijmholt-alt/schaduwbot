# Wallet-analyse pump.fun — 2026-09-13 09:44 UTC

## Kort antwoord

- Geluk-toets: 63 van 7767 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=17.82, geluk-grens 5.45).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.3% per positie (alle wallets: -8.8%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.2%, 2 s: -16.4%, 10 s: -17.7%, 60 s: -22.0% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 09:41 UTC (67.9 uur), helft A/B-grens: 2026-09-11 23:45 UTC
- 5734887 trades, 51327 tokens, 197038 wallets, 1736080 posities (948585 geopend vanaf ≥ $7k, 787495 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 131210
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10066 | 5807 | -44.18 | -118.80 | +436.26 | 21261.55 | 20288 | +2907.64 |
| dev | 2049 | 6032 | +1453.25 | -754.35 | +1346.70 | 5008.97 | 14048 | +1076.19 |
| swing | 1709 | 19462 | -877.48 | -1204.64 | -390.10 | 80.16 | 10376 | +51.02 |
| bot_hf | 2998 | 213354 | +68.91 | -1974.09 | +5139.85 | 13451.48 | 281145 | +7607.55 |
| incidenteel | 153205 | 201392 | -6467.15 | -12598.77 | +19288.57 | 8756.63 | 179396 | +8906.82 |
| scalper | 27011 | 502538 | -14815.64 | -18087.47 | +19894.14 | 8762.91 | 282242 | +2013.41 |

Wallets met ≥ 10 posities: 16379, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20682.28 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6552 (84) | 45% | +43.14 | +41.91 | +1% | 26.1 | ja | 23 s | +13.66 / +29.47 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3894 (21) | 62% | +11.77 | +11.63 | +9% | 25.31 | ja | 4 s | +5.63 / +6.13 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2962 (60) | 59% | +7.76 | +7.49 | +6% | 23.58 | ja | 4 s | +3.81 / +3.95 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6574 (55) | 38% | +6.70 | +5.70 | +0% | 22.95 | ja | 19 s | +4.34 / +2.36 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2663 (47) | 45% | +34.54 | +32.39 | +1% | 16.99 | ja | 24 s | +15.65 / +18.89 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2024 (13) | 48% | +5.96 | +4.74 | +0% | 15.66 | ja | 39 s | +5.41 / +0.55 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1476 (30) | 44% | +4.20 | +3.78 | +3% | 14.94 | ja | 61 s | +1.70 / +2.50 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1858 (11) | 51% | +8.42 | +7.69 | +1% | 14.75 | ja | 38 s | +5.29 / +3.14 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 555 (1) | 63% | +13.47 | +12.64 | +10% | 14.21 | ja | 1 s | +7.54 / +5.92 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1926 (7) | 55% | +1.88 | +1.77 | +2% | 13.19 | ja | 10 s | +0.74 / +1.14 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2161 (25) | 52% | +3.68 | +3.62 | +10% | 12.89 | ja | 4 s | +2.12 / +1.56 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1236 (4) | 42% | +12.59 | +11.55 | +3% | 12.33 | ja | 25 s | +8.87 / +3.72 |
| 13 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 646 (0) | 49% | +9.30 | +8.53 | +4% | 12.04 | ja | 1 s | +6.75 / +2.55 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.91 | ja | 53 s | +16.46 / +14.20 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2435 (2) | 48% | +4.93 | +4.48 | +0% | 11.85 | ja | 7 s | +1.83 / +3.10 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +22.12 / +12.11 |
| 17 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.79 | ja | 15 s | +0.77 / +0.29 |
| 18 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.89 | ja | 8 s | +5.91 / +5.40 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 775 (5) | 68% | +4.24 | +3.96 | +2% | 10.78 | ja | 10 s | +2.56 / +1.69 |
| 20 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.61 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.84 | nee | 2 min | +144.35 / +13.88 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.9 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 258 (0) | 64% | +140.16 | +106.21 | +15% | 8.49 | ja | 15 s | +69.27 / +70.89 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.42 | nee | 6 s | +39.67 / +46.39 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 187 (1) | 76% | +62.33 | +58.72 | +13% | 7.5 | ja | 9 s | +42.33 / +20.00 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.31 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.79 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.07 | nee | 16 s | +25.37 / +27.20 |
| 12 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 159 (10) | 58% | +47.31 | +40.11 | +14% | 6.99 | ja | 113 s | +28.35 / +18.96 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.06 / +24.76 |
| 14 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +53.77 / -7.18 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.01 | nee | 96 s | +29.11 / +15.73 |
| 16 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6552 (84) | 45% | +43.14 | +41.91 | +1% | 26.1 | ja | 23 s | +13.66 / +29.47 |
| 17 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 18 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +20.67 / +18.65 |
| 19 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |
| 20 | [1mGR…f5Hp](https://solscan.io/account/1mGRiNd5QgddUpASfGRftpQRKMB2peE5hj1gMF6f5Hp) | bot_hf | 27 (0) | 93% | +34.68 | +31.07 | +32% | 5.14 | nee | 7 s | +17.18 / +17.50 |

## Geluk-toets

Populatie: 7767 wallets met ≥ 20 posities, 76 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 17.82 | 4.35 | 5.45 |
| #10 | 10.31 | 3.46 | 3.63 |
| #20 | 8.34 | 3.16 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.45): **63**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 13669 | 49% | +6.3% | -0.2% | +192.46 |
| top 20 op winst (A) | 19/20 | 487 | 66% | +16.8% | +8.6% | +320.67 |
| alle wallets | – | 320518 | 33% | -8.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.8% / +1.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3329): ρ = 0.479. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 122

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13669 | 28% | -13.2% | -8.0% | -359.87 |
| 2 s | 13669 | 23% | -16.4% | -9.7% | -447.72 |
| 10 s | 13669 | 21% | -17.7% | -9.5% | -484.56 |
| 60 s | 13669 | 18% | -22.0% | -9.1% | -601.29 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 330

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39574 | 31% | -11.8% | -7.5% | -932.94 |
| 2 s | 39574 | 25% | -14.8% | -9.1% | -1171.99 |
| 10 s | 39574 | 22% | -15.8% | -8.9% | -1253.01 |
| 60 s | 39574 | 18% | -19.5% | -8.1% | -1540.86 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 113

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7658 | 33% | -1.6% | -5.2% | -24.50 |
| 2 s | 7658 | 27% | -5.2% | -6.6% | -79.43 |
| 10 s | 7658 | 25% | -6.2% | -6.6% | -95.67 |
| 60 s | 7658 | 22% | -6.4% | -5.7% | -97.47 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
