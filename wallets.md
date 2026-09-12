# Wallet-analyse pump.fun — 2026-09-12 12:10 UTC

## Kort antwoord

- Geluk-toets: 54 van 6164 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=14.75, geluk-grens 5.09).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -13.0%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -18.0%, 2 s: -19.2%, 10 s: -20.4%, 60 s: -25.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 12:08 UTC (46.3 uur), helft A/B-grens: 2026-09-11 12:58 UTC
- 3942433 trades, 31963 tokens, 164863 wallets, 1207465 posities (773628 geopend vanaf ≥ $7k, 433837 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 106220
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8349 | 5114 | +116.70 | +61.29 | +523.82 | 20357.68 | 11717 | +2005.92 |
| dev | 1524 | 4760 | +1047.84 | -611.38 | +698.02 | 4835.68 | 9313 | +762.39 |
| swing | 1277 | 14359 | -552.99 | -779.31 | -206.80 | 55.02 | 5605 | +61.73 |
| bot_hf | 2547 | 168403 | +150.82 | -1117.67 | +4562.04 | 11027.55 | 171540 | +6035.08 |
| incidenteel | 127963 | 181642 | -6383.76 | -12095.18 | +10862.20 | 8539.67 | 102942 | +6885.11 |
| scalper | 23203 | 399350 | -11639.79 | -14760.18 | +12806.19 | 8118.84 | 132720 | +1429.78 |

Wallets met ≥ 10 posities: 13412, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -17261.18 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5158 (71) | 45% | +27.66 | +26.44 | +1% | 23.64 | ja | 23 s | +2.71 / +24.95 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2713 (15) | 63% | +7.17 | +7.04 | +9% | 21.72 | ja | 4 s | +2.50 / +4.67 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5313 (41) | 38% | +6.64 | +5.63 | +1% | 21.24 | ja | 18 s | +3.50 / +3.13 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2071 (39) | 59% | +5.10 | +4.83 | +6% | 19.55 | ja | 4 s | +1.84 / +3.25 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1830 (19) | 51% | +4.43 | +3.91 | +1% | 17.17 | ja | 10 s | +0.41 / +4.02 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2259 (40) | 45% | +26.58 | +24.43 | +1% | 16.1 | ja | 24 s | +7.60 / +18.98 |
| 7 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1568 (12) | 51% | +6.21 | +5.48 | +1% | 13.6 | ja | 36 s | +0.22 / +5.99 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1127 (26) | 44% | +2.90 | +2.49 | +3% | 13.32 | ja | 61 s | +1.37 / +1.53 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 449 (1) | 64% | +11.60 | +10.77 | +10% | 13.26 | ja | 1 s | +4.06 / +7.53 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1572 (4) | 55% | +1.28 | +1.19 | +1% | 12.34 | ja | 10 s | +0.22 / +1.05 |
| 11 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1001 (3) | 43% | +11.29 | +10.25 | +3% | 11.51 | ja | 33 s | +5.09 / +6.20 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1551 (19) | 51% | +2.58 | +2.52 | +10% | 10.98 | ja | 4 s | +0.96 / +1.62 |
| 13 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.88 | ja | 8 s | +3.65 / +7.62 |
| 14 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 50 (0) | 66% | +23.78 | +21.79 | +54% | 10.82 | ja | 60 s | +13.47 / +10.31 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1661 (2) | 48% | +5.35 | +4.90 | +1% | 10.71 | nee | 7 s | +1.60 / +3.75 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 489 (0) | 49% | +7.73 | +6.97 | +5% | 10.58 | ja | 1 s | +1.56 / +6.17 |
| 17 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 618 (5) | 69% | +4.03 | +3.78 | +2% | 10.02 | ja | 11 s | +2.65 / +1.37 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 50 (0) | 58% | +18.31 | +16.30 | +41% | 9.93 | ja | 64 s | +7.88 / +10.43 |
| 19 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.91 | ja | 7 s | +0.26 / +0.52 |
| 20 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 725 (7) | 47% | +5.20 | +4.83 | +2% | 9.8 | ja | 70 s | +3.64 / +1.56 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 40 (0) | 80% | +295.41 | +270.49 | +77% | 10.27 | ja | 8 s | -0.81 / +296.22 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 8 (0) | 100% | +262.18 | +225.84 | +210% | 15.29 | nee | 13 s | +70.44 / +191.75 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.86 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 7 (0) | 100% | +132.10 | +86.41 | +240% | 12.14 | nee | 64 s | +0.00 / +132.10 |
| 5 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 10 (0) | 60% | +93.38 | +68.14 | +138% | 9.49 | nee | 3 min | +60.24 / +33.13 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 202 (0) | 62% | +88.16 | +82.24 | +13% | 7.85 | ja | 15 s | +35.40 / +52.76 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 10 (0) | 60% | +58.82 | +41.72 | +93% | 7.68 | nee | 3 min | +34.55 / +24.27 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 161 (1) | 78% | +54.60 | +51.00 | +13% | 7.35 | ja | 9 s | +27.48 / +27.12 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 17 (4) | 76% | +52.09 | +40.25 | +34% | 4.3 | nee | 6 s | +10.52 / +41.58 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 60 (3) | 95% | +32.86 | +30.86 | +18% | 4.64 | nee | 16 s | +12.96 / +19.90 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 129 (7) | 54% | +32.59 | +25.39 | +11% | 5.72 | nee | 99 s | +31.75 / +0.84 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (13) | 51% | +29.14 | +24.34 | +11% | 5.17 | nee | 88 s | +15.32 / +13.82 |
| 15 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 16 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5158 (71) | 45% | +27.66 | +26.44 | +1% | 23.64 | ja | 23 s | +2.71 / +24.95 |
| 17 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.19 | ja | 13 s | +19.21 / +8.25 |
| 18 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 31 (2) | 61% | +26.71 | +20.55 | +43% | 7.16 | ja | 112 s | +10.06 / +16.65 |
| 19 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2259 (40) | 45% | +26.58 | +24.43 | +1% | 16.1 | ja | 24 s | +7.60 / +18.98 |
| 20 | [AQdB…KotY](https://solscan.io/account/AQdBYZNy3BZ1vouGUjA1w9Ay7aq7kH5UQSuh4LQWKotY) | dev | 7 (4) | 29% | +26.44 | -1.08 | +54% | 1.69 | nee | 40 s | -0.83 / +27.27 |

## Geluk-toets

Populatie: 6164 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 14.75 | 4.38 | 5.09 |
| #10 | 9.42 | 3.35 | 3.52 |
| #20 | 7.38 | 3.04 | 3.22 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.09): **54**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 16343 | 51% | +5.0% | +0.2% | -84.90 |
| top 20 op winst (A) | 18/20 | 693 | 57% | +8.8% | +3.3% | +162.49 |
| alle wallets | – | 381269 | 30% | -13.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.7% / +1.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3182): ρ = 0.481. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 246

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 16343 | 24% | -18.0% | -11.7% | -587.08 |
| 2 s | 16343 | 22% | -19.2% | -12.3% | -629.15 |
| 10 s | 16343 | 20% | -20.4% | -12.4% | -668.31 |
| 60 s | 16343 | 16% | -25.6% | -12.5% | -837.70 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 286

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 30821 | 31% | -10.8% | -7.1% | -668.19 |
| 2 s | 30821 | 25% | -13.7% | -8.7% | -846.38 |
| 10 s | 30821 | 23% | -14.7% | -8.4% | -905.53 |
| 60 s | 30821 | 19% | -18.1% | -7.6% | -1116.55 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 133

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 8394 | 32% | -2.5% | -5.7% | -42.74 |
| 2 s | 8394 | 27% | -5.7% | -7.2% | -95.90 |
| 10 s | 8394 | 26% | -6.3% | -7.0% | -105.23 |
| 60 s | 8394 | 24% | -6.1% | -5.8% | -101.94 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
