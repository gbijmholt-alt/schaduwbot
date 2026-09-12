# Wallet-analyse pump.fun — 2026-09-12 01:55 UTC

## Kort antwoord

- Geluk-toets: 48 van 5132 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=13.34, geluk-grens 5.05).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.0% per positie (alle wallets: -14.0%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.5%, 2 s: -14.1%, 10 s: -14.8%, 60 s: -18.7% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 01:54 UTC (36.1 uur), helft A/B-grens: 2026-09-11 07:51 UTC
- 3108846 trades, 23544 tokens, 148332 wallets, 970982 posities (660394 geopend vanaf ≥ $7k, 310588 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 88238
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7804 | 4711 | +20.16 | -26.82 | +405.69 | 19382.37 | 8434 | +1509.52 |
| dev | 1208 | 4075 | +833.54 | -428.15 | +727.99 | 4812.96 | 6504 | +551.52 |
| swing | 916 | 10717 | -373.80 | -528.60 | -176.64 | 42.38 | 3886 | +36.68 |
| bot_hf | 2435 | 145737 | +27.35 | -1149.60 | +4287.07 | 9678.18 | 119554 | +4544.92 |
| incidenteel | 115790 | 168616 | -6185.97 | -11069.38 | +6623.79 | 7860.42 | 83162 | +5329.53 |
| scalper | 20179 | 326538 | -9798.43 | -12134.40 | +10320.32 | 7457.96 | 89048 | +934.75 |

Wallets met ≥ 10 posities: 11501, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15477.16 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2195 (10) | 63% | +6.43 | +6.30 | +10% | 20.18 | ja | 4 s | +2.33 / +4.10 |
| 2 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4311 (31) | 38% | +4.72 | +3.72 | +0% | 20.01 | ja | 19 s | +2.36 / +2.36 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1637 (32) | 59% | +4.63 | +4.36 | +7% | 16.79 | ja | 4 s | +2.10 / +2.53 |
| 4 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1487 (16) | 50% | +2.18 | +1.72 | +0% | 15.56 | ja | 10 s | +1.39 / +0.79 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1851 (39) | 45% | +16.33 | +14.18 | +1% | 14.94 | ja | 24 s | +4.21 / +12.12 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1289 (10) | 48% | +4.64 | +3.42 | +1% | 13.39 | ja | 34 s | +0.39 / +4.25 |
| 7 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 392 (1) | 62% | +9.89 | +9.06 | +10% | 12.43 | ja | 1 s | +2.61 / +7.28 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 972 (26) | 43% | +1.78 | +1.36 | +2% | 12.16 | ja | 61 s | +1.08 / +0.70 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1307 (5) | 55% | +0.73 | +0.64 | +1% | 11.4 | ja | 10 s | +0.04 / +0.69 |
| 10 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1017 (7) | 64% | +1.49 | +1.27 | +0% | 10.99 | ja | 14 s | +0.33 / +1.16 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 788 (5) | 44% | +9.62 | +8.58 | +4% | 10.95 | ja | 32 s | +4.76 / +4.86 |
| 12 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.78 | ja | 60 s | +13.47 / +10.31 |
| 13 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 284 (2) | 60% | +14.75 | +12.78 | +7% | 10.71 | ja | 8 s | +4.22 / +10.54 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 424 (0) | 50% | +7.64 | +6.88 | +5% | 10.45 | ja | 1 s | +0.60 / +7.05 |
| 15 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1290 (15) | 52% | +2.35 | +2.29 | +11% | 10.38 | nee | 4 s | +1.07 / +1.28 |
| 16 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.88 | ja | 64 s | +7.88 / +10.43 |
| 17 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 541 (5) | 69% | +3.19 | +2.94 | +2% | 9.68 | ja | 10 s | +2.59 / +0.59 |
| 18 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1226 (3) | 49% | +3.77 | +3.33 | +1% | 9.53 | nee | 7 s | +0.18 / +3.60 |
| 19 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 277 (15) | 50% | +0.71 | +0.61 | +6% | 9.45 | ja | 8 s | +0.26 / +0.45 |
| 20 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 50 (0) | 56% | +20.69 | +18.64 | +44% | 9.3 | ja | 57 s | +8.92 / +11.77 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 37 (0) | 78% | +269.26 | +244.34 | +79% | 9.76 | ja | 7 s | -0.81 / +270.07 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.15 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.81 | nee | 2 min | +0.00 / +158.23 |
| 4 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 176 (0) | 62% | +70.35 | +64.43 | +12% | 7.45 | ja | 15 s | +28.63 / +41.72 |
| 5 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 15 (3) | 80% | +50.06 | +38.23 | +35% | 4.28 | nee | 6 s | +10.52 / +39.55 |
| 6 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.55 | nee | 2 min | +0.00 / +46.59 |
| 7 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 134 (1) | 76% | +44.23 | +40.62 | +13% | 6.77 | ja | 9 s | +21.93 / +22.29 |
| 8 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 7 (0) | 86% | +35.01 | +26.09 | +64% | 3.22 | nee | 4 s | +0.33 / +34.69 |
| 9 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 56 (3) | 95% | +29.79 | +27.78 | +17% | 4.4 | nee | 15 s | +12.74 / +17.05 |
| 10 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 85 (12) | 51% | +29.11 | +24.30 | +12% | 5.21 | nee | 95 s | +15.32 / +13.79 |
| 11 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 113 (5) | 52% | +28.35 | +21.15 | +11% | 5.51 | nee | 106 s | +31.45 / -3.10 |
| 12 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | vroege_houder | 18 (0) | 72% | +27.08 | +20.06 | +21% | 3.08 | nee | 24 s | +0.80 / +26.29 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 63 (0) | 78% | +25.17 | +22.84 | +11% | 4.81 | nee | 24 s | +13.32 / +11.85 |
| 14 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 11 (0) | 91% | +25.07 | +18.04 | +26% | 3.0 | nee | 61 s | +22.18 / +2.89 |
| 15 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 138 (0) | 60% | +24.87 | +22.03 | +6% | 5.0 | nee | 7 s | +7.62 / +17.25 |
| 16 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 44 (0) | 66% | +24.03 | +20.11 | +12% | 4.0 | nee | 32 s | +13.06 / +10.97 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.78 | ja | 60 s | +13.47 / +10.31 |
| 18 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 21 (1) | 71% | +23.65 | +17.48 | +56% | 7.33 | ja | 80 s | +10.06 / +13.59 |
| 19 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 13 (0) | 62% | +23.15 | +14.79 | +23% | 2.62 | nee | 29 s | -1.00 / +24.15 |
| 20 | [B92U…ApaF](https://solscan.io/account/B92UBzhsvMu8xw4mwnPzuaDEWiy2WoLjwmyj3aUUApaF) | bot_hf | 12 (0) | 75% | +22.42 | +11.43 | +27% | 2.82 | nee | 6 s | +13.13 / +9.29 |

## Geluk-toets

Populatie: 5132 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 13.34 | 4.32 | 5.05 |
| #10 | 8.9 | 3.28 | 3.51 |
| #20 | 7.11 | 2.97 | 3.13 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.05): **48**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 9745 | 49% | +6.0% | -0.2% | +104.26 |
| top 20 op winst (A) | 18/20 | 660 | 58% | +9.4% | +3.4% | +151.92 |
| alle wallets | – | 317298 | 30% | -14.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.8% / +1.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2591): ρ = 0.478. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 95

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 9745 | 29% | -11.5% | -7.7% | -223.26 |
| 2 s | 9745 | 24% | -14.1% | -9.5% | -274.38 |
| 10 s | 9745 | 23% | -14.8% | -9.7% | -287.89 |
| 60 s | 9745 | 20% | -18.7% | -8.4% | -365.09 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 192

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 21438 | 33% | -11.8% | -7.5% | -505.34 |
| 2 s | 21438 | 25% | -15.2% | -9.4% | -651.56 |
| 10 s | 21438 | 23% | -15.8% | -8.9% | -679.35 |
| 60 s | 21438 | 18% | -19.8% | -7.9% | -849.24 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 17

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1029 | 42% | +5.3% | -3.5% | +10.90 |
| 2 s | 1029 | 26% | -10.0% | -10.4% | -20.54 |
| 10 s | 1029 | 25% | -10.9% | -8.7% | -22.53 |
| 60 s | 1029 | 16% | -10.3% | -5.8% | -21.14 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
