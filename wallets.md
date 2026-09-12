# Wallet-analyse pump.fun — 2026-09-12 09:55 UTC

## Kort antwoord

- Geluk-toets: 59 van 5918 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.99, geluk-grens 4.95).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -13.7%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -18.6%, 2 s: -19.8%, 10 s: -20.9%, 60 s: -26.0% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 09:53 UTC (44.1 uur), helft A/B-grens: 2026-09-11 11:51 UTC
- 3769235 trades, 30245 tokens, 161540 wallets, 1155824 posities (745944 geopend vanaf ≥ $7k, 409880 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 100754
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8215 | 4962 | +54.89 | +0.77 | +462.32 | 19791.45 | 11172 | +1864.30 |
| dev | 1458 | 4580 | +928.08 | -663.33 | +610.58 | 4819.13 | 8621 | +740.59 |
| swing | 1206 | 13607 | -529.01 | -749.71 | -239.42 | 51.75 | 5268 | +50.15 |
| bot_hf | 2510 | 162956 | +137.43 | -1121.72 | +4472.99 | 10901.13 | 160395 | +5831.18 |
| incidenteel | 125687 | 178969 | -6460.85 | -12124.60 | +9616.51 | 8521.15 | 99868 | +6628.33 |
| scalper | 22464 | 380870 | -11391.32 | -14254.58 | +11647.21 | 8010.28 | 124556 | +1318.75 |

Wallets met ≥ 10 posities: 12938, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -17260.78 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 4921 (64) | 45% | +21.29 | +20.07 | +1% | 23.27 | ja | 23 s | +2.97 / +18.32 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2539 (14) | 63% | +7.04 | +6.90 | +10% | 21.89 | ja | 4 s | +2.21 / +4.82 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5096 (39) | 38% | +5.32 | +4.31 | +0% | 21.09 | ja | 18 s | +3.31 / +2.01 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1967 (39) | 59% | +5.17 | +4.90 | +7% | 19.12 | ja | 4 s | +1.90 / +3.27 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1698 (18) | 50% | +2.80 | +2.32 | +1% | 16.83 | ja | 10 s | +0.86 / +1.94 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2150 (39) | 45% | +20.55 | +18.40 | +1% | 15.78 | ja | 25 s | +7.74 / +12.81 |
| 7 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1505 (11) | 50% | +5.49 | +4.75 | +1% | 13.5 | ja | 35 s | +0.42 / +5.07 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1075 (26) | 44% | +2.74 | +2.32 | +3% | 13.24 | ja | 61 s | +1.11 / +1.63 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 421 (1) | 63% | +10.90 | +10.07 | +10% | 13.24 | ja | 1 s | +3.99 / +6.91 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1511 (4) | 55% | +1.21 | +1.12 | +1% | 12.42 | ja | 10 s | +0.21 / +1.00 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 946 (3) | 43% | +9.37 | +8.33 | +3% | 11.33 | ja | 34 s | +5.09 / +4.27 |
| 12 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.87 | ja | 8 s | +3.65 / +7.62 |
| 13 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.81 | ja | 60 s | +13.47 / +10.31 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1468 (19) | 51% | +2.46 | +2.40 | +10% | 10.74 | ja | 4 s | +0.91 / +1.55 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 462 (0) | 50% | +7.89 | +7.13 | +5% | 10.7 | ja | 1 s | +1.48 / +6.41 |
| 16 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1641 (2) | 48% | +4.74 | +4.29 | +1% | 10.65 | nee | 7 s | +1.11 / +3.63 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.92 | ja | 64 s | +7.88 / +10.43 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.9 | ja | 7 s | +0.26 / +0.52 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 593 (5) | 68% | +3.20 | +2.96 | +2% | 9.89 | ja | 11 s | +2.59 / +0.61 |
| 20 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 725 (7) | 47% | +5.20 | +4.83 | +2% | 9.79 | ja | 70 s | +3.56 / +1.64 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 40 (0) | 80% | +295.41 | +270.49 | +77% | 10.26 | ja | 8 s | -0.81 / +296.22 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.2 | nee | 13 s | +35.46 / +170.94 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 6 (0) | 100% | +86.41 | +53.44 | +198% | 10.12 | nee | 57 s | +0.00 / +86.41 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 193 (0) | 63% | +84.28 | +78.37 | +13% | 7.77 | ja | 15 s | +30.55 / +53.73 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 9 (0) | 56% | +75.90 | +50.66 | +128% | 8.37 | nee | 110 s | +60.24 / +15.66 |
| 7 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 157 (1) | 78% | +53.20 | +49.59 | +13% | 7.33 | ja | 9 s | +27.48 / +25.72 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.3 | nee | 6 s | +10.52 / +41.58 |
| 9 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +0.00 / +46.59 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 9 (0) | 56% | +43.46 | +26.36 | +78% | 6.31 | nee | 110 s | +34.55 / +8.91 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 59 (3) | 95% | +32.46 | +30.45 | +18% | 4.6 | nee | 16 s | +12.74 / +19.72 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 117 (7) | 52% | +30.06 | +22.86 | +12% | 5.69 | nee | 112 s | +31.75 / -1.69 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.16 | nee | 88 s | +15.32 / +13.82 |
| 15 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.21 | nee | 28 s | +7.11 / +20.61 |
| 16 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 147 (0) | 60% | +26.35 | +23.51 | +6% | 5.1 | nee | 7 s | +7.62 / +18.73 |
| 17 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 51 (0) | 67% | +26.00 | +22.07 | +11% | 4.13 | nee | 31 s | +15.17 / +10.83 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 63 (0) | 78% | +25.17 | +22.84 | +11% | 4.84 | nee | 24 s | +13.58 / +11.59 |
| 19 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 11 (0) | 91% | +25.07 | +18.04 | +26% | 3.01 | nee | 61 s | +22.18 / +2.89 |
| 20 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 144 (0) | 48% | +25.04 | +21.32 | +14% | 6.88 | ja | 12 s | +18.90 / +6.14 |

## Geluk-toets

Populatie: 5918 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.99 | 4.3 | 4.95 |
| #10 | 9.26 | 3.31 | 3.51 |
| #20 | 7.18 | 3.0 | 3.14 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 4.95): **59**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 15063 | 51% | +5.1% | +0.5% | -91.16 |
| top 20 op winst (A) | 18/20 | 661 | 56% | +8.7% | +3.5% | +158.05 |
| alle wallets | – | 367408 | 30% | -13.7% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.1% / +0.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3055): ρ = 0.472. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 233

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 15063 | 24% | -18.6% | -12.3% | -561.79 |
| 2 s | 15063 | 22% | -19.8% | -12.7% | -595.40 |
| 10 s | 15063 | 20% | -20.9% | -12.8% | -628.63 |
| 60 s | 15063 | 16% | -26.0% | -12.8% | -784.50 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 273

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 29434 | 31% | -10.8% | -7.1% | -637.37 |
| 2 s | 29434 | 25% | -13.7% | -8.7% | -807.68 |
| 10 s | 29434 | 23% | -14.6% | -8.4% | -860.72 |
| 60 s | 29434 | 19% | -17.9% | -7.6% | -1055.58 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 18

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1175 | 42% | +4.0% | -3.9% | +9.52 |
| 2 s | 1175 | 27% | -9.2% | -9.6% | -21.52 |
| 10 s | 1175 | 25% | -10.3% | -7.4% | -24.13 |
| 60 s | 1175 | 17% | -9.6% | -5.8% | -22.46 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
