# Wallet-analyse pump.fun — 2026-09-12 06:02 UTC

## Kort antwoord

- Geluk-toets: 50 van 5621 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.19, geluk-grens 5.12).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.3% per positie (alle wallets: -13.7%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -17.4%, 2 s: -18.9%, 10 s: -19.9%, 60 s: -24.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 06:00 UTC (40.2 uur), helft A/B-grens: 2026-09-11 09:54 UTC
- 3489207 trades, 27273 tokens, 156866 wallets, 1080615 posities (714595 geopend vanaf ≥ $7k, 366020 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 96758
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8072 | 4833 | +58.48 | +9.09 | +470.55 | 19557.67 | 9916 | +1744.14 |
| dev | 1351 | 4318 | +905.52 | -561.64 | +659.79 | 4809.56 | 7514 | +641.03 |
| swing | 1108 | 12426 | -489.89 | -681.06 | -225.58 | 47.57 | 4482 | +56.34 |
| bot_hf | 2502 | 157302 | +109.26 | -1124.28 | +4505.04 | 10483.23 | 141965 | +5320.99 |
| incidenteel | 122112 | 175742 | -6352.30 | -11968.95 | +8222.57 | 8490.81 | 92440 | +6093.93 |
| scalper | 21721 | 359974 | -10499.31 | -13201.89 | +11298.26 | 7837.12 | 109703 | +1167.21 |

Wallets met ≥ 10 posities: 12417, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -16268.24 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 4679 (62) | 45% | +19.27 | +18.04 | +1% | 22.81 | ja | 23 s | +1.54 / +17.73 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2437 (14) | 63% | +6.99 | +6.85 | +10% | 21.2 | ja | 4 s | +2.35 / +4.64 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4828 (36) | 38% | +6.35 | +5.35 | +1% | 20.83 | ja | 18 s | +3.31 / +3.04 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1835 (34) | 59% | +5.17 | +4.91 | +7% | 18.69 | ja | 4 s | +2.04 / +3.13 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1615 (17) | 50% | +2.96 | +2.48 | +1% | 16.39 | ja | 10 s | +1.49 / +1.48 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2071 (40) | 45% | +21.32 | +19.18 | +1% | 15.58 | ja | 25 s | +9.10 / +12.22 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1038 (24) | 44% | +2.72 | +2.30 | +3% | 13.03 | ja | 61 s | +1.27 / +1.45 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 414 (1) | 63% | +10.75 | +9.92 | +10% | 13.02 | ja | 1 s | +3.69 / +7.06 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1461 (4) | 55% | +1.03 | +0.94 | +1% | 12.13 | ja | 10 s | +0.02 / +1.01 |
| 10 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1143 (8) | 63% | +1.51 | +1.29 | +0% | 11.45 | ja | 14 s | +0.93 / +0.58 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 893 (5) | 43% | +9.99 | +8.95 | +3% | 11.34 | ja | 33 s | +5.28 / +4.71 |
| 12 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 329 (2) | 59% | +11.32 | +9.35 | +5% | 10.93 | ja | 8 s | +3.65 / +7.67 |
| 13 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.78 | ja | 60 s | +13.47 / +10.31 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1390 (17) | 52% | +2.42 | +2.36 | +10% | 10.47 | nee | 4 s | +1.03 / +1.39 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 443 (0) | 49% | +7.72 | +6.96 | +5% | 10.43 | ja | 1 s | +0.87 / +6.86 |
| 16 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1518 (4) | 49% | +3.64 | +3.19 | +1% | 10.24 | nee | 7 s | +1.40 / +2.24 |
| 17 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 584 (5) | 69% | +3.42 | +3.18 | +2% | 9.92 | ja | 10 s | +2.81 / +0.61 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.88 | ja | 64 s | +7.88 / +10.43 |
| 19 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.86 | ja | 7 s | +0.26 / +0.52 |
| 20 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 708 (7) | 48% | +5.40 | +5.03 | +2% | 9.79 | ja | 70 s | +3.73 / +1.66 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 37 (0) | 78% | +269.26 | +244.34 | +79% | 9.76 | ja | 7 s | -0.81 / +270.07 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.16 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.81 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 6 (0) | 100% | +86.41 | +53.44 | +198% | 10.09 | nee | 57 s | +0.00 / +86.41 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 188 (0) | 63% | +80.23 | +74.32 | +12% | 7.63 | ja | 15 s | +28.95 / +51.28 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 9 (0) | 56% | +75.90 | +50.66 | +128% | 8.34 | nee | 110 s | +60.24 / +15.66 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.29 | nee | 6 s | +10.52 / +41.58 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 152 (1) | 77% | +50.94 | +47.34 | +13% | 7.19 | ja | 9 s | +23.38 / +27.56 |
| 9 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +0.00 / +46.59 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 9 (0) | 56% | +43.46 | +26.36 | +78% | 6.29 | nee | 110 s | +34.55 / +8.91 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 7 (0) | 86% | +35.01 | +26.09 | +64% | 3.22 | nee | 4 s | +0.33 / +34.69 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 59 (3) | 95% | +32.46 | +30.45 | +18% | 4.59 | nee | 16 s | +12.74 / +19.72 |
| 13 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.14 | nee | 88 s | +15.32 / +13.82 |
| 14 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 113 (5) | 52% | +28.35 | +21.15 | +11% | 5.51 | nee | 106 s | +31.75 / -3.41 |
| 15 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.2 | nee | 28 s | +3.18 / +24.54 |
| 16 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 48 (0) | 69% | +26.33 | +22.41 | +12% | 4.16 | nee | 32 s | +14.90 / +11.44 |
| 17 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 63 (0) | 78% | +25.17 | +22.84 | +11% | 4.82 | nee | 24 s | +13.32 / +11.85 |
| 18 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 11 (0) | 91% | +25.07 | +18.04 | +26% | 3.0 | nee | 61 s | +22.18 / +2.89 |
| 19 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 138 (0) | 60% | +24.87 | +22.03 | +6% | 5.0 | nee | 7 s | +7.62 / +17.25 |
| 20 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.78 | ja | 60 s | +13.47 / +10.31 |

## Geluk-toets

Populatie: 5621 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.19 | 4.34 | 5.12 |
| #10 | 9.04 | 3.3 | 3.51 |
| #20 | 7.13 | 2.99 | 3.14 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.12): **50**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14618 | 52% | +5.3% | +0.6% | -78.62 |
| top 20 op winst (A) | 18/20 | 735 | 55% | +8.8% | +2.6% | +167.57 |
| alle wallets | – | 354030 | 30% | -13.7% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.0% / +2.1% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2891): ρ = 0.488. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 229

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14618 | 25% | -17.4% | -11.6% | -508.33 |
| 2 s | 14618 | 22% | -18.9% | -11.9% | -553.01 |
| 10 s | 14618 | 20% | -19.9% | -12.0% | -581.87 |
| 60 s | 14618 | 16% | -24.9% | -11.8% | -727.85 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 262

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 27772 | 32% | -10.7% | -7.0% | -591.83 |
| 2 s | 27772 | 25% | -13.6% | -8.6% | -756.72 |
| 10 s | 27772 | 23% | -14.4% | -8.3% | -800.99 |
| 60 s | 27772 | 18% | -17.8% | -7.4% | -989.88 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 17

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1051 | 43% | +5.9% | -3.2% | +12.32 |
| 2 s | 1051 | 26% | -10.4% | -9.9% | -21.77 |
| 10 s | 1051 | 25% | -11.5% | -8.3% | -24.19 |
| 60 s | 1051 | 16% | -10.7% | -5.8% | -22.48 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
