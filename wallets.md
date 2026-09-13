# Wallet-analyse pump.fun — 2026-09-13 08:27 UTC

## Kort antwoord

- Geluk-toets: 65 van 7688 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=17.47, geluk-grens 5.31).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.5% per positie (alle wallets: -9.2%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -16.5%, 10 s: -17.8%, 60 s: -21.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 08:25 UTC (66.6 uur), helft A/B-grens: 2026-09-11 23:06 UTC
- 5660548 trades, 50687 tokens, 195681 wallets, 1713947 posities (939120 geopend vanaf ≥ $7k, 774827 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 129438
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10016 | 5806 | -46.88 | -121.19 | +431.99 | 21219.32 | 20278 | +2896.73 |
| dev | 2016 | 5953 | +1434.19 | -741.27 | +1245.85 | 5008.97 | 13906 | +1057.37 |
| swing | 1691 | 19229 | -865.40 | -1181.86 | -408.74 | 74.69 | 10184 | +45.32 |
| bot_hf | 2983 | 211011 | +98.37 | -1938.50 | +5172.43 | 13411.39 | 277520 | +7581.37 |
| incidenteel | 152204 | 200458 | -6460.02 | -12583.03 | +18674.30 | 8741.97 | 177527 | +8842.82 |
| scalper | 26771 | 496663 | -14765.01 | -18002.04 | +19186.42 | 8751.95 | 275412 | +1888.12 |

Wallets met ≥ 10 posities: 16222, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20604.74 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6473 (82) | 45% | +39.50 | +38.28 | +1% | 25.89 | ja | 23 s | +12.71 / +26.79 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3767 (21) | 62% | +11.36 | +11.23 | +9% | 24.89 | ja | 4 s | +5.08 / +6.29 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2884 (58) | 59% | +7.60 | +7.34 | +7% | 23.37 | ja | 4 s | +3.65 / +3.96 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6532 (53) | 38% | +6.53 | +5.53 | +0% | 22.89 | ja | 19 s | +4.42 / +2.11 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2436 (24) | 50% | +0.94 | +0.02 | +0% | 18.34 | ja | 10 s | +0.04 / +0.90 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2643 (46) | 45% | +34.56 | +32.42 | +1% | 16.96 | ja | 24 s | +16.61 / +17.95 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1455 (30) | 44% | +4.34 | +3.92 | +3% | 15.04 | ja | 61 s | +1.74 / +2.60 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1836 (11) | 51% | +8.36 | +7.62 | +1% | 14.72 | ja | 38 s | +3.80 / +4.55 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 553 (1) | 63% | +13.38 | +12.55 | +10% | 14.16 | ja | 1 s | +7.45 / +5.93 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1906 (6) | 55% | +2.00 | +1.89 | +2% | 13.22 | ja | 10 s | +0.66 / +1.33 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2134 (25) | 53% | +3.72 | +3.65 | +10% | 13.09 | ja | 4 s | +1.95 / +1.77 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1212 (4) | 42% | +12.20 | +11.16 | +3% | 12.3 | ja | 26 s | +8.06 / +4.14 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2400 (2) | 48% | +5.46 | +5.02 | +1% | 11.94 | ja | 7 s | +3.07 / +2.40 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.9 | ja | 53 s | +17.89 / +12.76 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 640 (0) | 49% | +8.55 | +7.79 | +4% | 11.88 | ja | 1 s | +6.61 / +1.94 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +21.38 / +12.85 |
| 17 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.89 | ja | 8 s | +3.52 / +7.79 |
| 18 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 771 (5) | 68% | +4.39 | +4.11 | +2% | 10.8 | ja | 10 s | +2.85 / +1.55 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 973 (23) | 42% | +1.39 | +1.10 | +1% | 10.69 | ja | 62 s | +0.02 / +1.37 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.6 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.83 | nee | 2 min | +91.06 / +67.17 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.89 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 258 (0) | 64% | +140.16 | +106.21 | +15% | 8.48 | ja | 15 s | +69.27 / +70.89 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.42 | nee | 6 s | +24.74 / +61.32 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 186 (1) | 76% | +62.37 | +58.77 | +13% | 7.5 | ja | 9 s | +40.84 / +21.54 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.31 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.78 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.07 | nee | 16 s | +24.66 / +27.91 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.83 / +24.00 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +50.28 / -3.69 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.01 | nee | 96 s | +29.11 / +15.73 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 154 (8) | 58% | +43.35 | +36.15 | +13% | 6.67 | nee | 112 s | +28.35 / +15.00 |
| 16 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6473 (82) | 45% | +39.50 | +38.28 | +1% | 25.89 | ja | 23 s | +12.71 / +26.79 |
| 17 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 18 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +20.67 / +18.65 |
| 19 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 13 (0) | 69% | +34.82 | +20.27 | +67% | 5.35 | nee | 12 s | +21.18 / +13.64 |

## Geluk-toets

Populatie: 7688 wallets met ≥ 20 posities, 77 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 17.47 | 4.56 | 5.31 |
| #10 | 10.42 | 3.49 | 3.68 |
| #20 | 8.42 | 3.14 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.31): **65**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13318 | 49% | +6.5% | -0.0% | +179.81 |
| top 20 op winst (A) | 19/20 | 534 | 64% | +16.0% | +7.3% | +296.36 |
| alle wallets | – | 324448 | 33% | -9.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.1% / +0.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3325): ρ = 0.472. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 114

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13318 | 29% | -13.0% | -8.0% | -346.94 |
| 2 s | 13318 | 23% | -16.5% | -9.8% | -439.48 |
| 10 s | 13318 | 20% | -17.8% | -9.6% | -473.33 |
| 60 s | 13318 | 18% | -21.9% | -9.2% | -584.14 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 349

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39180 | 31% | -11.5% | -7.3% | -900.13 |
| 2 s | 39180 | 24% | -14.5% | -8.9% | -1136.65 |
| 10 s | 39180 | 22% | -15.5% | -8.6% | -1215.09 |
| 60 s | 39180 | 18% | -19.2% | -7.8% | -1504.83 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 110

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7559 | 33% | -1.7% | -5.2% | -25.88 |
| 2 s | 7559 | 27% | -5.3% | -6.7% | -80.04 |
| 10 s | 7559 | 24% | -6.4% | -6.6% | -96.72 |
| 60 s | 7559 | 22% | -6.5% | -5.8% | -97.74 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
