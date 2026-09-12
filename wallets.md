# Wallet-analyse pump.fun — 2026-09-12 16:34 UTC

## Kort antwoord

- Geluk-toets: 56 van 6632 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=15.65, geluk-grens 5.24).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.5% per positie (alle wallets: -12.0%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -10.9%, 2 s: -14.0%, 10 s: -14.9%, 60 s: -18.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 16:32 UTC (50.7 uur), helft A/B-grens: 2026-09-11 15:10 UTC
- 4407533 trades, 37292 tokens, 172443 wallets, 1340853 posities (829213 geopend vanaf ≥ $7k, 511640 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 113296
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8903 | 5238 | -5.47 | -63.91 | +455.74 | 20553.14 | 13842 | +2379.88 |
| dev | 1664 | 5092 | +1163.47 | -633.24 | +875.06 | 4851.16 | 10687 | +841.04 |
| swing | 1449 | 16178 | -696.78 | -958.30 | -315.32 | 62.72 | 6512 | +51.68 |
| bot_hf | 2684 | 182994 | +129.94 | -1684.30 | +4825.43 | 11608.43 | 200488 | +6533.43 |
| incidenteel | 133387 | 187532 | -6556.99 | -12347.23 | +13419.58 | 8540.03 | 116563 | +7510.72 |
| scalper | 24356 | 432179 | -12516.32 | -15353.88 | +14586.96 | 8451.96 | 163548 | +1661.03 |

Wallets met ≥ 10 posities: 14347, waarvan winstgevend: 19%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18482.15 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5609 (74) | 45% | +29.19 | +27.97 | +1% | 24.35 | ja | 23 s | +0.90 / +28.29 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3012 (17) | 62% | +7.88 | +7.75 | +9% | 22.72 | ja | 4 s | +2.68 / +5.20 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5723 (43) | 38% | +7.35 | +6.35 | +1% | 22.06 | ja | 19 s | +3.58 / +3.78 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2281 (44) | 59% | +6.05 | +5.78 | +7% | 21.04 | ja | 4 s | +2.25 / +3.80 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2008 (22) | 51% | +3.27 | +2.75 | +0% | 17.58 | ja | 10 s | +1.08 / +2.19 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2367 (42) | 45% | +27.37 | +25.23 | +1% | 16.31 | ja | 24 s | +8.26 / +19.12 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1730 (12) | 48% | +4.37 | +3.15 | +0% | 14.95 | ja | 38 s | +1.64 / +2.72 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1662 (11) | 51% | +8.14 | +7.41 | +1% | 14.32 | ja | 37 s | +1.30 / +6.84 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1240 (27) | 44% | +3.11 | +2.69 | +3% | 13.84 | ja | 61 s | +1.24 / +1.87 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 481 (1) | 63% | +11.95 | +11.12 | +10% | 13.68 | ja | 1 s | +4.50 / +7.44 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1665 (4) | 55% | +1.29 | +1.20 | +1% | 12.56 | ja | 10 s | +0.39 / +0.90 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1703 (24) | 52% | +2.99 | +2.93 | +10% | 11.94 | ja | 4 s | +1.01 / +1.98 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1067 (4) | 42% | +10.86 | +9.82 | +3% | 11.81 | ja | 30 s | +5.56 / +5.31 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 531 (0) | 49% | +8.22 | +7.45 | +5% | 11.17 | ja | 1 s | +1.64 / +6.58 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1858 (2) | 49% | +5.05 | +4.60 | +1% | 11.07 | ja | 7 s | +2.01 / +3.04 |
| 16 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.89 | ja | 8 s | +3.65 / +7.62 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 75 (1) | 57% | +23.08 | +21.07 | +33% | 10.26 | ja | 52 s | +11.36 / +11.72 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 303 (15) | 52% | +0.82 | +0.72 | +7% | 10.26 | ja | 7 s | +0.26 / +0.56 |
| 19 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 75 (1) | 59% | +25.91 | +23.92 | +36% | 10.1 | ja | 48 s | +16.57 / +9.34 |
| 20 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 656 (5) | 68% | +3.41 | +3.16 | +2% | 9.97 | ja | 11 s | +2.83 / +0.57 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 43 (0) | 81% | +326.76 | +301.84 | +78% | 10.9 | ja | 8 s | -0.81 / +327.57 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.66 | nee | 12 s | +135.01 / +157.20 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.94 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 220 (0) | 61% | +126.61 | +92.65 | +16% | 8.11 | ja | 15 s | +43.36 / +83.25 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.21 | nee | 102 s | +60.24 / +37.88 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 20 (5) | 75% | +58.99 | +47.15 | +32% | 4.56 | nee | 6 s | +10.52 / +48.47 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 169 (1) | 78% | +58.09 | +54.48 | +14% | 7.48 | ja | 9 s | +28.01 / +30.08 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 71 (3) | 96% | +44.05 | +41.95 | +20% | 5.5 | nee | 19 s | +15.52 / +28.53 |
| 12 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.58 | nee | 106 s | +31.59 / +10.38 |
| 13 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.94 | ja | 6 min | +8.52 / +30.81 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 97 (14) | 53% | +37.70 | +32.89 | +13% | 5.79 | nee | 89 s | +16.15 / +21.55 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 76 (0) | 78% | +31.30 | +28.97 | +11% | 5.02 | nee | 24 s | +16.31 / +15.00 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5609 (74) | 45% | +29.19 | +27.97 | +1% | 24.35 | ja | 23 s | +0.90 / +28.29 |
| 18 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.2 | ja | 13 s | +18.76 / +8.71 |
| 20 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2367 (42) | 45% | +27.37 | +25.23 | +1% | 16.31 | ja | 24 s | +8.26 / +19.12 |

## Geluk-toets

Populatie: 6632 wallets met ≥ 20 posities, 91 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 15.65 | 4.35 | 5.24 |
| #10 | 9.52 | 3.36 | 3.64 |
| #20 | 7.59 | 3.05 | 3.26 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.24): **56**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14974 | 48% | +5.5% | -0.3% | +127.13 |
| top 20 op winst (A) | 19/20 | 784 | 57% | +9.4% | +3.2% | +226.23 |
| alle wallets | – | 399312 | 31% | -12.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.0% / +3.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3449): ρ = 0.507. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 132

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14974 | 30% | -10.9% | -7.1% | -327.75 |
| 2 s | 14974 | 24% | -14.0% | -8.8% | -420.53 |
| 10 s | 14974 | 22% | -14.9% | -8.6% | -447.60 |
| 60 s | 14974 | 19% | -18.2% | -7.9% | -545.62 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 314

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 34376 | 31% | -10.9% | -7.1% | -748.68 |
| 2 s | 34376 | 25% | -13.9% | -8.6% | -951.95 |
| 10 s | 34376 | 23% | -14.7% | -8.4% | -1012.75 |
| 60 s | 34376 | 19% | -18.0% | -7.5% | -1238.33 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 139

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 9093 | 32% | -2.6% | -5.7% | -47.53 |
| 2 s | 9093 | 27% | -5.8% | -7.2% | -106.07 |
| 10 s | 9093 | 26% | -6.3% | -6.9% | -115.06 |
| 60 s | 9093 | 24% | -6.2% | -5.8% | -113.09 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
