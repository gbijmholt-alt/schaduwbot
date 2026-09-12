# Wallet-analyse pump.fun — 2026-09-12 07:54 UTC

## Kort antwoord

- Geluk-toets: 44 van 5813 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.42, geluk-grens 5.5).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -13.6%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -17.8%, 2 s: -19.0%, 10 s: -20.1%, 60 s: -25.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 07:53 UTC (42.1 uur), helft A/B-grens: 2026-09-11 10:50 UTC
- 3641470 trades, 28673 tokens, 159725 wallets, 1122081 posities (733209 geopend vanaf ≥ $7k, 388872 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 98884
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8177 | 4917 | +49.16 | -4.94 | +457.12 | 19606.87 | 10652 | +1793.76 |
| dev | 1405 | 4465 | +919.45 | -601.72 | +665.40 | 4819.70 | 8043 | +684.15 |
| swing | 1183 | 13279 | -524.37 | -737.03 | -258.93 | 51.39 | 5056 | +50.98 |
| bot_hf | 2505 | 160490 | +133.43 | -1128.43 | +4483.79 | 10701.32 | 151132 | +5502.96 |
| incidenteel | 124247 | 177566 | -6407.51 | -12032.36 | +8518.70 | 8487.07 | 96134 | +6317.29 |
| scalper | 22208 | 372492 | -10952.64 | -13715.17 | +11774.75 | 7966.57 | 117855 | +1195.71 |

Wallets met ≥ 10 posities: 12760, waarvan winstgevend: 20%. De top 1% winnaars pakt 35% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -16782.49 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 4902 (62) | 45% | +20.72 | +19.50 | +1% | 23.2 | ja | 23 s | +0.78 / +19.95 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2454 (14) | 63% | +6.98 | +6.84 | +10% | 21.31 | ja | 4 s | +2.27 / +4.71 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4995 (37) | 38% | +5.83 | +4.83 | +1% | 21.07 | ja | 18 s | +3.07 / +2.76 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1909 (36) | 59% | +5.18 | +4.92 | +7% | 19.01 | ja | 4 s | +1.92 / +3.26 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1654 (18) | 49% | +2.94 | +2.46 | +1% | 16.51 | ja | 10 s | +1.25 / +1.69 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2122 (38) | 45% | +20.06 | +17.91 | +1% | 15.65 | ja | 25 s | +8.43 / +11.63 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1062 (25) | 44% | +2.77 | +2.36 | +3% | 13.16 | ja | 61 s | +1.19 / +1.58 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 415 (1) | 63% | +10.79 | +9.96 | +10% | 13.08 | ja | 1 s | +3.58 / +7.20 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1492 (4) | 55% | +1.09 | +1.00 | +1% | 12.24 | ja | 10 s | +0.15 / +0.94 |
| 10 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1162 (7) | 63% | +1.11 | +0.89 | +0% | 11.51 | ja | 14 s | +0.88 / +0.24 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 942 (3) | 43% | +9.61 | +8.57 | +3% | 11.39 | ja | 34 s | +4.78 / +4.83 |
| 12 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 329 (2) | 59% | +11.32 | +9.35 | +5% | 10.96 | ja | 8 s | +3.65 / +7.67 |
| 13 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.81 | ja | 60 s | +13.47 / +10.31 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 451 (0) | 49% | +7.86 | +7.09 | +5% | 10.6 | ja | 1 s | +0.79 / +7.07 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1602 (2) | 48% | +4.47 | +4.02 | +1% | 10.52 | nee | 7 s | +1.15 / +3.32 |
| 16 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1442 (17) | 51% | +2.40 | +2.35 | +10% | 10.46 | nee | 4 s | +0.95 / +1.45 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.91 | ja | 64 s | +7.88 / +10.43 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.89 | ja | 7 s | +0.26 / +0.52 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 590 (5) | 68% | +3.20 | +2.96 | +2% | 9.86 | ja | 10 s | +2.68 / +0.52 |
| 20 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 725 (7) | 47% | +5.20 | +4.83 | +2% | 9.78 | ja | 70 s | +3.84 / +1.36 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 39 (0) | 80% | +286.51 | +261.58 | +79% | 10.2 | ja | 7 s | -0.81 / +287.31 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.19 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.84 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 6 (0) | 100% | +86.41 | +53.44 | +198% | 10.11 | nee | 57 s | +0.00 / +86.41 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 189 (0) | 64% | +80.78 | +74.86 | +12% | 7.67 | ja | 15 s | +29.34 / +51.44 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 9 (0) | 56% | +75.90 | +50.66 | +128% | 8.36 | nee | 110 s | +60.24 / +15.66 |
| 7 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 156 (1) | 78% | +53.02 | +49.42 | +13% | 7.33 | ja | 9 s | +25.34 / +27.69 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.3 | nee | 6 s | +10.52 / +41.58 |
| 9 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +0.00 / +46.59 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 9 (0) | 56% | +43.46 | +26.36 | +78% | 6.3 | nee | 110 s | +34.55 / +8.91 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 59 (3) | 95% | +32.46 | +30.45 | +18% | 4.6 | nee | 16 s | +12.74 / +19.72 |
| 13 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.16 | nee | 88 s | +15.32 / +13.82 |
| 14 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 114 (5) | 53% | +28.41 | +21.20 | +11% | 5.51 | nee | 112 s | +31.75 / -3.35 |
| 15 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.21 | nee | 28 s | +7.11 / +20.61 |
| 16 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 143 (0) | 60% | +26.36 | +23.52 | +6% | 5.06 | nee | 7 s | +7.62 / +18.74 |
| 17 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 51 (0) | 67% | +26.00 | +22.07 | +11% | 4.12 | nee | 31 s | +13.85 / +12.14 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 63 (0) | 78% | +25.17 | +22.84 | +11% | 4.83 | nee | 24 s | +13.32 / +11.85 |
| 19 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 11 (0) | 91% | +25.07 | +18.04 | +26% | 3.01 | nee | 61 s | +22.18 / +2.89 |
| 20 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 143 (0) | 48% | +24.65 | +20.93 | +14% | 6.84 | nee | 12 s | +17.70 / +6.95 |

## Geluk-toets

Populatie: 5813 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.42 | 4.43 | 5.5 |
| #10 | 9.18 | 3.35 | 3.55 |
| #20 | 7.16 | 3.03 | 3.18 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.5): **44**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 14923 | 51% | +5.1% | +0.5% | -82.23 |
| top 20 op winst (A) | 19/20 | 749 | 56% | +8.5% | +3.2% | +170.55 |
| alle wallets | – | 365848 | 30% | -13.6% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.7% / +2.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2979): ρ = 0.484. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 229

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14923 | 24% | -17.8% | -11.8% | -530.40 |
| 2 s | 14923 | 22% | -19.0% | -12.3% | -568.25 |
| 10 s | 14923 | 20% | -20.1% | -12.4% | -598.55 |
| 60 s | 14923 | 16% | -25.1% | -12.2% | -748.07 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 259

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 28634 | 32% | -10.7% | -7.1% | -612.98 |
| 2 s | 28634 | 25% | -13.7% | -8.6% | -781.77 |
| 10 s | 28634 | 23% | -14.4% | -8.3% | -826.88 |
| 60 s | 28634 | 18% | -17.8% | -7.4% | -1020.48 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 17

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1161 | 42% | +4.0% | -4.0% | +9.38 |
| 2 s | 1161 | 27% | -9.3% | -9.6% | -21.54 |
| 10 s | 1161 | 25% | -10.4% | -7.4% | -24.10 |
| 60 s | 1161 | 17% | -9.5% | -5.8% | -22.08 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
