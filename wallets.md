# Wallet-analyse pump.fun — 2026-09-12 03:58 UTC

## Kort antwoord

- Geluk-toets: 50 van 5370 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=13.82, geluk-grens 5.04).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.6% per positie (alle wallets: -13.9%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.4%, 2 s: -13.8%, 10 s: -14.5%, 60 s: -18.3% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 03:57 UTC (38.1 uur), helft A/B-grens: 2026-09-11 08:52 UTC
- 3308619 trades, 25535 tokens, 153508 wallets, 1029407 posities (689428 geopend vanaf ≥ $7k, 339979 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 93160
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7866 | 4710 | +100.27 | +56.66 | +486.92 | 19333.85 | 9284 | +1664.99 |
| dev | 1273 | 4158 | +860.68 | -501.13 | +686.12 | 4806.44 | 6870 | +591.06 |
| swing | 1018 | 11538 | -416.43 | -583.99 | -188.17 | 43.05 | 4215 | +52.40 |
| bot_hf | 2489 | 151787 | +107.38 | -1118.90 | +4489.34 | 10184.50 | 130507 | +5127.27 |
| incidenteel | 119833 | 172776 | -6265.16 | -11649.95 | +7837.80 | 8395.98 | 88871 | +5792.11 |
| scalper | 21029 | 344459 | -10209.38 | -12768.76 | +10689.98 | 7710.65 | 100232 | +1014.56 |

Wallets met ≥ 10 posities: 11983, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15822.64 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 4476 (58) | 45% | +18.08 | +16.86 | +1% | 22.38 | ja | 22 s | +0.34 / +17.74 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2307 (12) | 63% | +6.82 | +6.68 | +10% | 20.74 | ja | 4 s | +2.25 / +4.57 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 4565 (34) | 38% | +5.18 | +4.18 | +0% | 20.33 | ja | 19 s | +2.87 / +2.31 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1739 (33) | 59% | +4.86 | +4.59 | +7% | 17.43 | ja | 4 s | +2.08 / +2.78 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1567 (18) | 50% | +2.73 | +2.27 | +1% | 16.02 | ja | 10 s | +1.51 / +1.22 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 1963 (37) | 45% | +17.23 | +15.08 | +1% | 15.03 | ja | 24 s | +8.51 / +8.72 |
| 7 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 405 (1) | 63% | +10.44 | +9.61 | +10% | 12.66 | ja | 1 s | +3.30 / +7.15 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1003 (25) | 43% | +2.35 | +1.94 | +2% | 12.63 | ja | 61 s | +1.23 / +1.12 |
| 9 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1397 (5) | 55% | +0.75 | +0.66 | +1% | 11.86 | ja | 10 s | +0.01 / +0.74 |
| 10 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 844 (3) | 44% | +10.88 | +9.84 | +4% | 11.41 | ja | 34 s | +4.81 / +6.07 |
| 11 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 296 (3) | 60% | +15.27 | +13.30 | +8% | 11.2 | ja | 8 s | +3.69 / +11.58 |
| 12 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1069 (7) | 63% | +1.18 | +0.96 | +0% | 11.04 | ja | 14 s | +1.10 / +0.08 |
| 13 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.77 | ja | 60 s | +13.47 / +10.31 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1336 (17) | 51% | +2.42 | +2.36 | +11% | 10.62 | ja | 4 s | +0.99 / +1.43 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 432 (0) | 50% | +8.13 | +7.36 | +5% | 10.56 | ja | 1 s | +0.75 / +7.38 |
| 16 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.87 | ja | 64 s | +7.88 / +10.43 |
| 17 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 564 (5) | 68% | +3.15 | +2.90 | +2% | 9.67 | ja | 10 s | +2.77 / +0.38 |
| 18 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1388 (2) | 48% | +3.09 | +2.64 | +1% | 9.65 | nee | 7 s | +1.01 / +2.08 |
| 19 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 663 (7) | 47% | +4.73 | +4.36 | +2% | 9.45 | ja | 70 s | +3.82 / +0.91 |
| 20 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 277 (15) | 50% | +0.71 | +0.61 | +6% | 9.44 | ja | 8 s | +0.26 / +0.45 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 37 (0) | 78% | +269.26 | +244.34 | +79% | 9.75 | ja | 7 s | -0.81 / +270.07 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 6 (0) | 100% | +206.40 | +170.06 | +229% | 14.14 | nee | 13 s | +0.00 / +206.40 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.8 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 6 (0) | 100% | +86.41 | +53.44 | +198% | 10.11 | nee | 57 s | +0.00 / +86.41 |
| 5 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 9 (0) | 56% | +75.90 | +50.66 | +128% | 8.36 | nee | 110 s | +60.24 / +15.66 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 180 (0) | 62% | +73.57 | +67.65 | +12% | 7.51 | ja | 15 s | +31.18 / +42.39 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 16 (3) | 81% | +52.09 | +40.25 | +35% | 4.35 | nee | 6 s | +10.52 / +41.58 |
| 8 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.55 | nee | 2 min | +0.00 / +46.59 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 141 (1) | 76% | +46.52 | +42.92 | +13% | 6.91 | ja | 9 s | +22.89 / +23.64 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 9 (0) | 56% | +43.46 | +26.36 | +78% | 6.28 | nee | 110 s | +34.55 / +8.91 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 7 (0) | 86% | +35.01 | +26.09 | +64% | 3.22 | nee | 4 s | +0.33 / +34.69 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 59 (3) | 95% | +32.46 | +30.45 | +18% | 4.58 | nee | 16 s | +12.74 / +19.72 |
| 13 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.15 | nee | 88 s | +15.32 / +13.82 |
| 14 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 113 (5) | 52% | +28.35 | +21.15 | +11% | 5.5 | nee | 106 s | +31.75 / -3.41 |
| 15 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | vroege_houder | 18 (0) | 72% | +27.08 | +20.06 | +21% | 3.08 | nee | 24 s | +2.02 / +25.06 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 63 (0) | 78% | +25.17 | +22.84 | +11% | 4.81 | nee | 24 s | +13.32 / +11.85 |
| 17 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 11 (0) | 91% | +25.07 | +18.04 | +26% | 3.0 | nee | 61 s | +22.18 / +2.89 |
| 18 | [9NgH…w6pz](https://solscan.io/account/9NgHs3A8F2cnM2w6kWsMp8AGAeyQyJckQ2unJvmiw6pz) | bot_hf | 138 (0) | 60% | +24.87 | +22.03 | +6% | 5.0 | nee | 7 s | +7.62 / +17.25 |
| 19 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 46 (0) | 67% | +24.38 | +20.46 | +11% | 4.03 | nee | 32 s | +15.03 / +9.36 |
| 20 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.77 | ja | 60 s | +13.47 / +10.31 |

## Geluk-toets

Populatie: 5370 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 13.82 | 4.34 | 5.04 |
| #10 | 8.95 | 3.28 | 3.5 |
| #20 | 7.15 | 2.97 | 3.13 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.04): **50**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 10646 | 49% | +5.6% | +0.0% | +108.72 |
| top 20 op winst (A) | 18/20 | 704 | 55% | +8.2% | +2.1% | +148.73 |
| alle wallets | – | 334466 | 30% | -13.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.4% / +1.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 2726): ρ = 0.488. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 98

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10646 | 30% | -11.4% | -7.4% | -243.02 |
| 2 s | 10646 | 25% | -13.8% | -9.2% | -294.52 |
| 10 s | 10646 | 23% | -14.5% | -9.2% | -308.33 |
| 60 s | 10646 | 20% | -18.3% | -8.1% | -389.95 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 251

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 26391 | 32% | -10.7% | -7.0% | -562.48 |
| 2 s | 26391 | 25% | -13.6% | -8.6% | -718.90 |
| 10 s | 26391 | 23% | -14.4% | -8.3% | -758.02 |
| 60 s | 26391 | 18% | -17.8% | -7.4% | -939.06 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 16

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 1028 | 43% | +5.9% | -3.3% | +12.20 |
| 2 s | 1028 | 26% | -10.5% | -10.2% | -21.50 |
| 10 s | 1028 | 25% | -11.6% | -8.4% | -23.92 |
| 60 s | 1028 | 16% | -10.7% | -5.8% | -22.05 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
