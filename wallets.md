# Wallet-analyse pump.fun — 2026-09-13 05:51 UTC

## Kort antwoord

- Geluk-toets: 68 van 7536 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.95, geluk-grens 5.2).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.0% per positie (alle wallets: -9.6%; 16 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.3%, 2 s: -15.5%, 10 s: -16.6%, 60 s: -20.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 05:47 UTC (64.0 uur), helft A/B-grens: 2026-09-11 21:48 UTC
- 5497133 trades, 48666 tokens, 193401 wallets, 1667496 posities (923066 geopend vanaf ≥ $7k, 744430 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 126346
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9911 | 5694 | -45.58 | -120.43 | +424.96 | 21128.86 | 19345 | +2790.84 |
| dev | 1951 | 5806 | +1382.65 | -728.31 | +1156.07 | 5008.79 | 13337 | +1034.30 |
| swing | 1640 | 18696 | -842.94 | -1149.27 | -421.71 | 70.09 | 9740 | +47.93 |
| bot_hf | 2961 | 207111 | +82.31 | -1861.00 | +5207.94 | 12869.01 | 266390 | +7469.85 |
| incidenteel | 150521 | 198989 | -6430.44 | -12549.63 | +17571.98 | 8726.79 | 172744 | +8672.58 |
| scalper | 26417 | 486770 | -14463.96 | -17643.72 | +17300.23 | 8728.12 | 262874 | +1963.68 |

Wallets met ≥ 10 posities: 15974, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20317.96 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6400 (78) | 45% | +37.18 | +35.95 | +1% | 25.73 | ja | 23 s | +11.57 / +25.61 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3644 (20) | 62% | +10.80 | +10.66 | +9% | 24.24 | ja | 4 s | +4.98 / +5.81 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2803 (58) | 60% | +7.72 | +7.46 | +7% | 23.37 | ja | 4 s | +3.56 / +4.16 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6392 (50) | 38% | +6.92 | +5.92 | +0% | 22.71 | ja | 19 s | +3.64 / +3.28 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2417 (24) | 50% | +1.64 | +0.72 | +0% | 18.44 | ja | 10 s | +0.87 / +0.77 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2593 (45) | 45% | +33.55 | +31.41 | +1% | 16.86 | ja | 24 s | +13.18 / +20.37 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1435 (29) | 44% | +4.04 | +3.62 | +3% | 14.88 | ja | 61 s | +1.87 / +2.17 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1805 (12) | 50% | +7.96 | +7.23 | +1% | 14.6 | ja | 37 s | +2.49 / +5.47 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 543 (1) | 62% | +12.26 | +11.43 | +9% | 13.99 | ja | 1 s | +6.22 / +6.04 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1877 (6) | 55% | +1.88 | +1.77 | +2% | 13.18 | ja | 10 s | +0.52 / +1.36 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2076 (24) | 53% | +3.65 | +3.58 | +10% | 13.12 | ja | 4 s | +1.90 / +1.75 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1190 (4) | 42% | +11.95 | +10.90 | +3% | 12.23 | ja | 26 s | +7.49 / +4.46 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2340 (2) | 48% | +5.16 | +4.71 | +1% | 11.94 | ja | 7 s | +3.05 / +2.11 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.9 | ja | 53 s | +12.80 / +17.86 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.83 | ja | 51 s | +18.91 / +15.33 |
| 16 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.78 | ja | 15 s | +0.97 / +0.09 |
| 17 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 617 (0) | 48% | +7.38 | +6.61 | +4% | 11.52 | ja | 1 s | +5.91 / +1.46 |
| 18 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.88 | ja | 8 s | +3.54 / +7.77 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 20 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 763 (5) | 68% | +4.08 | +3.79 | +2% | 10.71 | ja | 10 s | +3.18 / +0.90 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.6 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.83 | nee | 2 min | +67.53 / +90.70 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.89 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 255 (0) | 64% | +138.64 | +104.69 | +15% | 8.4 | ja | 15 s | +58.93 / +79.71 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.17 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.42 | nee | 6 s | +13.73 / +72.33 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 184 (1) | 76% | +62.10 | +58.49 | +13% | 7.5 | ja | 9 s | +39.35 / +22.75 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.3 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.78 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.06 | nee | 16 s | +24.66 / +27.91 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.83 / +24.00 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +27.39 / +19.20 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 109 (16) | 54% | +42.55 | +37.75 | +13% | 5.86 | nee | 95 s | +28.58 / +13.97 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.58 | nee | 106 s | +28.35 / +13.62 |
| 16 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 17 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +19.76 / +19.56 |
| 18 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6400 (78) | 45% | +37.18 | +35.95 | +1% | 25.73 | ja | 23 s | +11.57 / +25.61 |
| 20 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.83 | ja | 51 s | +18.91 / +15.33 |

## Geluk-toets

Populatie: 7536 wallets met ≥ 20 posities, 79 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.95 | 4.48 | 5.2 |
| #10 | 10.22 | 3.44 | 3.63 |
| #20 | 8.32 | 3.14 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.2): **68**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14190 | 48% | +6.0% | -0.3% | +191.52 |
| top 20 op winst (A) | 18/20 | 496 | 66% | +16.7% | +8.1% | +309.16 |
| alle wallets | – | 342629 | 33% | -9.6% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.9% / +1.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3471): ρ = 0.493. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 112

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14190 | 28% | -12.3% | -7.8% | -348.60 |
| 2 s | 14190 | 23% | -15.5% | -9.6% | -441.09 |
| 10 s | 14190 | 21% | -16.6% | -9.3% | -471.91 |
| 60 s | 14190 | 18% | -20.6% | -8.9% | -584.67 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 324

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38732 | 32% | -11.4% | -7.2% | -883.63 |
| 2 s | 38732 | 25% | -14.4% | -8.7% | -1117.15 |
| 10 s | 38732 | 22% | -15.4% | -8.4% | -1190.18 |
| 60 s | 38732 | 18% | -18.9% | -7.6% | -1464.67 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 107

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7547 | 33% | -1.4% | -5.2% | -21.00 |
| 2 s | 7547 | 27% | -5.4% | -6.7% | -81.70 |
| 10 s | 7547 | 24% | -6.4% | -6.7% | -96.33 |
| 60 s | 7547 | 22% | -6.5% | -5.8% | -98.28 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
