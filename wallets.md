# Wallet-analyse pump.fun — 2026-09-12 07:45 UTC

## Kort antwoord

- Geluk-toets: 53 van 5802 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.42, geluk-grens 5.19).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -13.5%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -17.8%, 2 s: -19.1%, 10 s: -20.1%, 60 s: -25.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 07:43 UTC (41.9 uur), helft A/B-grens: 2026-09-11 10:45 UTC
- 3631910 trades, 28541 tokens, 159638 wallets, 1119866 posities (732216 geopend vanaf ≥ $7k, 387650 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 98755
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8170 | 4914 | +49.53 | -4.58 | +457.33 | 19589.12 | 10577 | +1786.56 |
| dev | 1401 | 4447 | +920.04 | -596.82 | +669.53 | 4819.70 | 7982 | +681.18 |
| swing | 1184 | 13275 | -524.46 | -736.43 | -258.23 | 51.39 | 5048 | +50.93 |
| bot_hf | 2502 | 160199 | +140.01 | -1120.57 | +4485.65 | 10689.44 | 150525 | +5503.21 |
| incidenteel | 124204 | 177537 | -6408.34 | -12030.85 | +8521.02 | 8501.73 | 96046 | +6297.73 |
| scalper | 22177 | 371844 | -10928.78 | -13687.44 | +11721.15 | 7959.54 | 117472 | +1196.43 |

Wallets met ≥ 10 posities: 12738, waarvan winstgevend: 20%. De top 1% winnaars pakt 35% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -16752.00 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 4902 (62) | 45% | +20.72 | +19.50 | +1% | 23.18 | ja | 23 s | +0.66 / +20.07 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2445 (14) | 63% | +6.99 | +6.86 | +10% | 21.3 | ja | 4 s | +2.32 / +4.67 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4984 (37) | 38% | +5.90 | +4.89 | +1% | 21.02 | ja | 18 s | +3.20 / +2.70 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1906 (35) | 59% | +5.22 | +4.95 | +7% | 18.98 | ja | 4 s | +1.96 / +3.26 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1653 (18) | 49% | +2.79 | +2.31 | +1% | 16.48 | ja | 10 s | +1.22 / +1.57 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2116 (38) | 45% | +19.37 | +17.23 | +1% | 15.59 | ja | 24 s | +8.63 / +10.74 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1059 (25) | 44% | +2.80 | +2.38 | +3% | 13.17 | ja | 61 s | +1.19 / +1.60 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 414 (1) | 63% | +10.75 | +9.92 | +10% | 13.06 | ja | 1 s | +3.58 / +7.17 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1492 (4) | 55% | +1.09 | +1.00 | +1% | 12.24 | ja | 10 s | +0.14 / +0.95 |
| 10 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1161 (7) | 63% | +1.19 | +0.97 | +0% | 11.52 | ja | 14 s | +0.85 / +0.34 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 942 (3) | 43% | +9.61 | +8.57 | +3% | 11.39 | ja | 34 s | +4.78 / +4.83 |
| 12 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 329 (2) | 59% | +11.32 | +9.35 | +5% | 10.96 | ja | 8 s | +3.65 / +7.67 |
| 13 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.8 | ja | 60 s | +13.47 / +10.31 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 450 (0) | 49% | +7.83 | +7.07 | +5% | 10.58 | ja | 1 s | +0.79 / +7.04 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1598 (2) | 48% | +4.48 | +4.03 | +1% | 10.51 | nee | 7 s | +1.15 / +3.33 |
| 16 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1442 (17) | 51% | +2.40 | +2.35 | +10% | 10.46 | nee | 4 s | +0.95 / +1.45 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.91 | ja | 64 s | +7.88 / +10.43 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.89 | ja | 7 s | +0.26 / +0.52 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 590 (5) | 68% | +3.20 | +2.96 | +2% | 9.86 | ja | 10 s | +2.68 / +0.52 |
| 20 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 725 (7) | 47% | +5.20 | +4.83 | +2% | 9.78 | ja | 70 s | +3.84 / +1.36 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 39 (0) | 80% | +286.51 | +261.58 | +79% | 10.21 | ja | 7 s | -0.81 / +287.31 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.19 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.84 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 6 (0) | 100% | +86.41 | +53.44 | +198% | 10.11 | nee | 57 s | +0.00 / +86.41 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 189 (0) | 64% | +80.78 | +74.86 | +12% | 7.67 | ja | 15 s | +29.34 / +51.44 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 9 (0) | 56% | +75.90 | +50.66 | +128% | 8.36 | nee | 110 s | +60.24 / +15.66 |
| 7 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 156 (1) | 78% | +53.02 | +49.42 | +13% | 7.32 | ja | 9 s | +25.34 / +27.69 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.29 | nee | 6 s | +10.52 / +41.58 |
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
| 20 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 143 (1) | 48% | +24.83 | +21.11 | +14% | 6.86 | ja | 12 s | +17.70 / +7.13 |

## Geluk-toets

Populatie: 5802 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.42 | 4.31 | 5.19 |
| #10 | 9.17 | 3.31 | 3.51 |
| #20 | 7.16 | 3.02 | 3.14 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.19): **53**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 14910 | 51% | +5.0% | +0.5% | -82.94 |
| top 20 op winst (A) | 18/20 | 740 | 56% | +8.6% | +3.2% | +168.94 |
| alle wallets | – | 365848 | 30% | -13.5% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.0% / +1.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2969): ρ = 0.489. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 231

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14910 | 24% | -17.8% | -11.8% | -530.54 |
| 2 s | 14910 | 22% | -19.1% | -12.2% | -568.32 |
| 10 s | 14910 | 20% | -20.1% | -12.4% | -597.87 |
| 60 s | 14910 | 16% | -25.1% | -12.2% | -747.31 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 259

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 28594 | 32% | -10.7% | -7.1% | -611.90 |
| 2 s | 28594 | 25% | -13.6% | -8.6% | -780.28 |
| 10 s | 28594 | 23% | -14.4% | -8.3% | -824.89 |
| 60 s | 28594 | 18% | -17.8% | -7.4% | -1018.60 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 18

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1161 | 42% | +4.1% | -3.9% | +9.43 |
| 2 s | 1161 | 27% | -9.3% | -9.5% | -21.51 |
| 10 s | 1161 | 25% | -10.4% | -7.4% | -24.12 |
| 60 s | 1161 | 17% | -9.5% | -5.8% | -22.07 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
