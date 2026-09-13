# Wallet-analyse pump.fun — 2026-09-13 03:49 UTC

## Kort antwoord

- Geluk-toets: 59 van 7405 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.89, geluk-grens 5.51).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.2% per positie (alle wallets: -10.0%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.9%, 2 s: -15.2%, 10 s: -16.3%, 60 s: -20.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 03:46 UTC (62.0 uur), helft A/B-grens: 2026-09-11 20:47 UTC
- 5314228 trades, 46984 tokens, 190892 wallets, 1614838 posities (909801 geopend vanaf ≥ $7k, 705037 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124423
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9804 | 5542 | -40.47 | -111.25 | +426.19 | 21017.79 | 18287 | +2723.96 |
| dev | 1903 | 5690 | +1364.69 | -698.39 | +1136.30 | 5010.62 | 13312 | +1019.67 |
| swing | 1615 | 18409 | -815.78 | -1116.90 | -415.83 | 69.06 | 9149 | +50.03 |
| bot_hf | 2953 | 203883 | +58.70 | -1877.49 | +5149.88 | 12718.11 | 255401 | +7321.85 |
| incidenteel | 148506 | 197857 | -6455.99 | -12557.17 | +16040.78 | 8699.88 | 164439 | +8203.74 |
| scalper | 26111 | 478420 | -14030.36 | -17176.26 | +16952.85 | 8703.02 | 244449 | +1969.41 |

Wallets met ≥ 10 posities: 15735, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -19919.20 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6262 (78) | 45% | +34.48 | +33.26 | +1% | 25.49 | ja | 23 s | +6.01 / +28.47 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3539 (20) | 62% | +10.45 | +10.31 | +9% | 24.08 | ja | 4 s | +4.45 / +6.00 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2691 (53) | 60% | +7.54 | +7.27 | +7% | 23.23 | ja | 4 s | +3.27 / +4.26 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6322 (47) | 38% | +6.19 | +5.18 | +0% | 22.58 | ja | 19 s | +3.69 / +2.50 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2357 (23) | 50% | +1.09 | +0.18 | +0% | 18.37 | ja | 10 s | +0.45 / +0.64 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2557 (45) | 44% | +29.56 | +27.41 | +1% | 16.68 | ja | 24 s | +14.64 / +14.91 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1911 (13) | 48% | +3.96 | +2.74 | +0% | 15.26 | ja | 37 s | +3.91 / +0.04 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1405 (30) | 44% | +3.98 | +3.56 | +3% | 14.77 | ja | 61 s | +1.74 / +2.24 |
| 9 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1781 (12) | 50% | +8.21 | +7.48 | +1% | 14.55 | ja | 37 s | +2.29 / +5.92 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 540 (1) | 62% | +12.19 | +11.36 | +9% | 14.0 | ja | 1 s | +6.23 / +5.96 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1846 (6) | 55% | +1.71 | +1.61 | +2% | 12.95 | ja | 10 s | +0.45 / +1.26 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2012 (25) | 52% | +3.48 | +3.41 | +10% | 12.7 | ja | 4 s | +1.69 / +1.79 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1140 (5) | 42% | +12.09 | +11.05 | +3% | 12.2 | ja | 26 s | +6.56 / +5.53 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.9 | ja | 53 s | +12.80 / +17.86 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2258 (2) | 48% | +5.48 | +5.03 | +1% | 11.87 | ja | 7 s | +3.82 / +1.66 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +18.91 / +15.33 |
| 17 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.79 | ja | 15 s | +1.04 / +0.01 |
| 18 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 611 (0) | 48% | +7.39 | +6.62 | +4% | 11.56 | ja | 1 s | +5.99 / +1.41 |
| 19 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.88 | ja | 8 s | +3.60 / +7.71 |
| 20 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.61 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.83 | nee | 2 min | +11.47 / +146.76 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.9 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 251 (0) | 63% | +137.49 | +103.53 | +15% | 8.43 | ja | 15 s | +51.08 / +86.40 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.44 | nee | 6 s | +13.73 / +72.33 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 182 (1) | 76% | +60.87 | +57.26 | +13% | 7.43 | ja | 9 s | +36.89 / +23.97 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.31 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.77 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.07 | nee | 16 s | +24.51 / +28.07 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.75 / +24.07 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +8.74 / +37.84 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 107 (16) | 54% | +44.00 | +39.20 | +14% | 6.03 | nee | 89 s | +25.16 / +18.84 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.58 | nee | 106 s | +29.55 / +12.41 |
| 16 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 2.08 | nee | 97 s | +0.00 / +39.35 |
| 17 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +15.64 / +23.68 |
| 18 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +19.93 / +18.45 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6262 (78) | 45% | +34.48 | +33.26 | +1% | 25.49 | ja | 23 s | +6.01 / +28.47 |
| 20 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +18.91 / +15.33 |

## Geluk-toets

Populatie: 7405 wallets met ≥ 20 posities, 80 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.89 | 4.41 | 5.51 |
| #10 | 10.17 | 3.41 | 3.66 |
| #20 | 8.31 | 3.12 | 3.28 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.51): **59**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14187 | 48% | +6.2% | -0.3% | +197.24 |
| top 20 op winst (A) | 18/20 | 517 | 65% | +14.9% | +7.4% | +305.69 |
| alle wallets | – | 357159 | 32% | -10.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.8% / +1.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3522): ρ = 0.5. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 118

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14187 | 29% | -11.9% | -7.7% | -337.25 |
| 2 s | 14187 | 23% | -15.2% | -9.6% | -431.94 |
| 10 s | 14187 | 21% | -16.3% | -9.3% | -463.10 |
| 60 s | 14187 | 18% | -20.2% | -8.7% | -573.74 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 331

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39069 | 31% | -11.1% | -7.2% | -869.91 |
| 2 s | 39069 | 25% | -14.1% | -8.7% | -1101.22 |
| 10 s | 39069 | 22% | -15.0% | -8.5% | -1173.46 |
| 60 s | 39069 | 18% | -18.4% | -7.6% | -1435.10 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 107

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7401 | 33% | -1.4% | -5.2% | -20.59 |
| 2 s | 7401 | 27% | -5.4% | -6.7% | -80.58 |
| 10 s | 7401 | 24% | -6.5% | -6.7% | -95.40 |
| 60 s | 7401 | 21% | -6.5% | -5.8% | -96.83 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
