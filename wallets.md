# Wallet-analyse pump.fun — 2026-09-13 07:39 UTC

## Kort antwoord

- Geluk-toets: 65 van 7658 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=17.36, geluk-grens 5.35).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.1% per positie (alle wallets: -9.3%; 16 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.4%, 2 s: -15.7%, 10 s: -17.1%, 60 s: -21.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 07:37 UTC (65.8 uur), helft A/B-grens: 2026-09-11 22:42 UTC
- 5621803 trades, 50162 tokens, 194983 wallets, 1703316 posities (935651 geopend vanaf ≥ $7k, 767665 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 128436
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9992 | 5785 | -47.06 | -121.34 | +431.96 | 21201.14 | 20115 | +2866.21 |
| dev | 2000 | 5896 | +1404.82 | -753.54 | +1202.94 | 5008.79 | 13791 | +1022.91 |
| swing | 1665 | 18997 | -861.44 | -1170.85 | -414.46 | 73.41 | 9949 | +47.85 |
| bot_hf | 2978 | 210424 | +93.09 | -1942.76 | +5153.28 | 13373.34 | 275484 | +7547.97 |
| incidenteel | 151644 | 199987 | -6446.23 | -12574.06 | +18142.12 | 8737.69 | 176024 | +8830.03 |
| scalper | 26704 | 494562 | -14744.06 | -17974.38 | +18578.61 | 8750.42 | 272302 | +1922.72 |

Wallets met ≥ 10 posities: 16177, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20600.89 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6457 (79) | 45% | +38.14 | +36.92 | +1% | 25.82 | ja | 23 s | +12.34 / +25.80 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3727 (20) | 62% | +11.15 | +11.02 | +9% | 24.74 | ja | 4 s | +5.10 / +6.05 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2849 (57) | 59% | +7.29 | +7.02 | +6% | 23.2 | ja | 4 s | +3.64 / +3.65 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6515 (53) | 38% | +6.54 | +5.53 | +0% | 22.85 | ja | 19 s | +3.87 / +2.67 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2637 (46) | 45% | +32.97 | +30.82 | +1% | 16.91 | ja | 24 s | +16.26 / +16.71 |
| 6 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1451 (30) | 44% | +4.17 | +3.75 | +3% | 14.97 | ja | 61 s | +1.75 / +2.42 |
| 7 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1827 (11) | 51% | +8.17 | +7.43 | +1% | 14.67 | ja | 38 s | +4.31 / +3.86 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 550 (1) | 62% | +13.18 | +12.35 | +10% | 14.11 | ja | 1 s | +7.30 / +5.88 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1901 (6) | 55% | +2.00 | +1.90 | +2% | 13.24 | ja | 10 s | +0.65 / +1.35 |
| 10 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2118 (25) | 53% | +3.60 | +3.53 | +10% | 12.86 | ja | 4 s | +1.99 / +1.60 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1209 (4) | 42% | +12.18 | +11.14 | +3% | 12.3 | ja | 25 s | +8.39 / +3.79 |
| 12 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2390 (2) | 48% | +5.46 | +5.01 | +1% | 12.0 | ja | 7 s | +3.70 / +1.77 |
| 13 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.9 | ja | 53 s | +13.38 / +17.27 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 635 (0) | 49% | +8.57 | +7.81 | +4% | 11.89 | ja | 1 s | +6.62 / +1.95 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +18.14 / +16.10 |
| 16 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.89 | ja | 8 s | +3.40 / +7.91 |
| 17 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 769 (5) | 68% | +4.34 | +4.05 | +2% | 10.82 | ja | 10 s | +2.92 / +1.41 |
| 18 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |
| 19 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 729 (6) | 70% | +5.22 | +4.95 | +2% | 10.69 | ja | 10 s | +2.77 / +2.44 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 969 (23) | 42% | +1.23 | +0.94 | +1% | 10.61 | ja | 62 s | +0.02 / +1.21 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.61 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.83 | nee | 2 min | +91.06 / +67.17 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.9 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 257 (0) | 64% | +139.59 | +105.63 | +15% | 8.47 | ja | 15 s | +69.18 / +70.41 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.42 | nee | 6 s | +24.74 / +61.32 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 186 (1) | 76% | +62.37 | +58.77 | +13% | 7.51 | ja | 9 s | +40.84 / +21.53 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.31 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.78 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.07 | nee | 16 s | +24.66 / +27.91 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.83 / +24.00 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +50.28 / -3.69 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.01 | nee | 96 s | +29.11 / +15.73 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 154 (9) | 57% | +42.63 | +35.43 | +13% | 6.57 | nee | 112 s | +28.35 / +14.28 |
| 16 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 17 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +20.67 / +18.65 |
| 18 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6457 (79) | 45% | +38.14 | +36.92 | +1% | 25.82 | ja | 23 s | +12.34 / +25.80 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 13 (0) | 69% | +34.82 | +20.27 | +67% | 5.35 | nee | 12 s | +21.18 / +13.64 |

## Geluk-toets

Populatie: 7658 wallets met ≥ 20 posities, 77 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 17.36 | 4.45 | 5.35 |
| #10 | 10.35 | 3.47 | 3.64 |
| #20 | 8.33 | 3.16 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.35): **65**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 13959 | 48% | +6.1% | -0.3% | +184.41 |
| top 20 op winst (A) | 19/20 | 501 | 66% | +14.4% | +7.2% | +286.48 |
| alle wallets | – | 329216 | 33% | -9.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.8% / +1.4% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3344): ρ = 0.478. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 109

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13959 | 29% | -12.4% | -7.8% | -347.37 |
| 2 s | 13959 | 23% | -15.7% | -9.5% | -439.18 |
| 10 s | 13959 | 21% | -17.1% | -9.3% | -475.92 |
| 60 s | 13959 | 18% | -21.1% | -8.9% | -587.59 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 328

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 37298 | 31% | -11.8% | -7.6% | -880.17 |
| 2 s | 37298 | 24% | -14.8% | -9.2% | -1108.07 |
| 10 s | 37298 | 22% | -15.9% | -8.9% | -1188.40 |
| 60 s | 37298 | 18% | -19.8% | -8.1% | -1475.36 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 108

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7542 | 33% | -1.7% | -5.2% | -26.25 |
| 2 s | 7542 | 27% | -5.3% | -6.7% | -80.36 |
| 10 s | 7542 | 24% | -6.4% | -6.7% | -96.76 |
| 60 s | 7542 | 22% | -6.5% | -5.8% | -97.64 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
