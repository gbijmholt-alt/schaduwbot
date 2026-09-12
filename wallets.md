# Wallet-analyse pump.fun — 2026-09-12 13:14 UTC

## Kort antwoord

- Geluk-toets: 51 van 6265 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.97, geluk-grens 5.33).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -12.6%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -17.6%, 2 s: -19.3%, 10 s: -20.5%, 60 s: -25.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 13:12 UTC (47.4 uur), helft A/B-grens: 2026-09-11 13:30 UTC
- 4042689 trades, 32888 tokens, 166368 wallets, 1236474 posities (788267 geopend vanaf ≥ $7k, 448207 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 108346
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8467 | 4990 | +28.79 | -26.80 | +435.74 | 20205.21 | 11688 | +2008.93 |
| dev | 1559 | 4874 | +1087.16 | -598.17 | +755.36 | 4837.22 | 9687 | +774.93 |
| swing | 1322 | 14872 | -589.56 | -837.31 | -224.51 | 56.35 | 5830 | +65.98 |
| bot_hf | 2568 | 172147 | +130.52 | -1153.38 | +4528.87 | 11132.53 | 177689 | +6095.70 |
| incidenteel | 128908 | 183670 | -6554.42 | -12301.69 | +11443.80 | 8524.17 | 104715 | +7169.05 |
| scalper | 23544 | 407714 | -11877.01 | -15080.38 | +13362.04 | 8378.55 | 138598 | +1560.75 |

Wallets met ≥ 10 posities: 13663, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -17774.50 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5297 (70) | 45% | +27.17 | +25.95 | +1% | 23.84 | ja | 23 s | +2.49 / +24.68 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2824 (17) | 62% | +7.52 | +7.38 | +9% | 22.06 | ja | 4 s | +2.54 / +4.98 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5427 (40) | 38% | +6.62 | +5.61 | +1% | 21.49 | ja | 19 s | +3.48 / +3.14 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2138 (41) | 59% | +5.43 | +5.16 | +7% | 20.25 | ja | 4 s | +2.08 / +3.35 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1855 (20) | 50% | +4.89 | +4.38 | +1% | 17.4 | ja | 10 s | +0.57 / +4.32 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2283 (41) | 45% | +23.98 | +21.83 | +1% | 16.18 | ja | 24 s | +6.81 / +17.17 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1640 (13) | 48% | +5.62 | +4.41 | +0% | 14.62 | ja | 37 s | +0.62 / +5.00 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1597 (11) | 51% | +7.00 | +6.26 | +1% | 13.83 | ja | 36 s | +0.61 / +6.39 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 455 (1) | 63% | +11.79 | +10.96 | +10% | 13.59 | ja | 1 s | +4.23 / +7.56 |
| 10 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1160 (28) | 44% | +3.04 | +2.62 | +3% | 13.54 | ja | 61 s | +1.18 / +1.86 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1600 (4) | 55% | +1.25 | +1.16 | +1% | 12.44 | ja | 10 s | +0.21 / +1.04 |
| 12 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1247 (7) | 63% | +1.36 | +1.14 | +0% | 11.79 | ja | 15 s | +1.24 / +0.12 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1027 (3) | 43% | +10.97 | +9.93 | +3% | 11.67 | ja | 32 s | +5.07 / +5.90 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1588 (19) | 52% | +2.78 | +2.72 | +10% | 11.5 | ja | 4 s | +0.96 / +1.81 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1718 (2) | 49% | +5.57 | +5.12 | +1% | 10.91 | nee | 7 s | +1.39 / +4.18 |
| 16 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.88 | ja | 8 s | +3.65 / +7.62 |
| 17 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 499 (0) | 49% | +7.86 | +7.10 | +5% | 10.87 | ja | 1 s | +1.72 / +6.15 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 58 (1) | 64% | +23.95 | +21.96 | +46% | 10.44 | ja | 59 s | +13.47 / +10.49 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 629 (5) | 69% | +3.90 | +3.66 | +2% | 10.11 | ja | 11 s | +2.54 / +1.36 |
| 20 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 59 (1) | 58% | +19.90 | +17.89 | +38% | 10.02 | ja | 64 s | +7.88 / +12.01 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 40 (0) | 80% | +295.41 | +270.49 | +77% | 10.27 | ja | 8 s | -0.81 / +296.22 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.73 | nee | 12 s | +102.20 / +190.01 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.93 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 207 (0) | 61% | +120.36 | +86.40 | +16% | 7.97 | ja | 15 s | +35.40 / +84.96 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.2 | nee | 102 s | +60.24 / +37.88 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 165 (1) | 78% | +54.81 | +51.20 | +13% | 7.41 | ja | 9 s | +27.48 / +27.33 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.3 | nee | 6 s | +10.52 / +41.58 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 62 (3) | 95% | +35.64 | +33.53 | +19% | 4.89 | nee | 16 s | +12.96 / +22.68 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 132 (9) | 54% | +32.92 | +25.72 | +11% | 5.76 | nee | 101 s | +31.38 / +1.54 |
| 14 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 21 (3) | 81% | +32.42 | +25.52 | +69% | 7.88 | ja | 6 min | +2.74 / +29.68 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.17 | nee | 88 s | +15.32 / +13.82 |
| 16 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 17 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.19 | ja | 13 s | +18.76 / +8.71 |
| 18 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5297 (70) | 45% | +27.17 | +25.95 | +1% | 23.84 | ja | 23 s | +2.49 / +24.68 |
| 19 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 31 (2) | 61% | +26.71 | +20.55 | +43% | 7.16 | ja | 112 s | +10.06 / +16.65 |
| 20 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 147 (0) | 60% | +26.35 | +23.51 | +6% | 5.11 | nee | 7 s | +7.62 / +18.73 |

## Geluk-toets

Populatie: 6265 wallets met ≥ 20 posities, 97 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.97 | 4.37 | 5.33 |
| #10 | 9.45 | 3.36 | 3.56 |
| #20 | 7.51 | 3.05 | 3.2 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.33): **51**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 17355 | 51% | +5.1% | +0.3% | -83.86 |
| top 20 op winst (A) | 19/20 | 815 | 57% | +8.9% | +3.2% | +218.14 |
| alle wallets | – | 383258 | 31% | -12.6% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.3% / +3.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3262): ρ = 0.49. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 257

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17355 | 25% | -17.6% | -11.2% | -611.24 |
| 2 s | 17355 | 22% | -19.3% | -11.7% | -668.88 |
| 10 s | 17355 | 20% | -20.5% | -11.9% | -710.31 |
| 60 s | 17355 | 16% | -25.6% | -11.8% | -889.86 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 293

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 33431 | 32% | -10.6% | -6.9% | -707.93 |
| 2 s | 33431 | 25% | -13.5% | -8.4% | -900.18 |
| 10 s | 33431 | 23% | -14.3% | -8.2% | -959.16 |
| 60 s | 33431 | 19% | -17.4% | -7.3% | -1162.85 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 94

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6456 | 33% | -1.4% | -5.2% | -18.03 |
| 2 s | 6456 | 27% | -5.5% | -6.8% | -70.46 |
| 10 s | 6456 | 25% | -6.5% | -6.7% | -83.71 |
| 60 s | 6456 | 22% | -6.3% | -5.7% | -81.57 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
