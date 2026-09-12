# Wallet-analyse pump.fun — 2026-09-12 17:32 UTC

## Kort antwoord

- Geluk-toets: 49 van 6757 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.03, geluk-grens 5.66).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.7% per positie (alle wallets: -11.8%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.1%, 2 s: -14.3%, 10 s: -15.2%, 60 s: -18.5% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 17:30 UTC (51.7 uur), helft A/B-grens: 2026-09-11 15:39 UTC
- 4520254 trades, 38846 tokens, 174384 wallets, 1373752 posities (836053 geopend vanaf ≥ $7k, 537699 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 114731
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9090 | 5293 | +15.31 | -43.51 | +497.96 | 20683.26 | 14896 | +2497.61 |
| dev | 1691 | 5148 | +1159.07 | -658.03 | +902.11 | 4853.87 | 10989 | +837.11 |
| swing | 1473 | 16905 | -713.15 | -988.11 | -339.21 | 62.64 | 6934 | +50.21 |
| bot_hf | 2732 | 184880 | +41.75 | -1803.42 | +4801.41 | 11828.01 | 207582 | +6565.21 |
| incidenteel | 134939 | 188429 | -6564.44 | -12430.54 | +13822.48 | 8524.35 | 123502 | +7674.84 |
| scalper | 24459 | 435398 | -12629.09 | -15485.80 | +14543.25 | 8454.54 | 173796 | +1645.55 |

Wallets met ≥ 10 posities: 14427, waarvan winstgevend: 19%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18690.54 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5629 (73) | 45% | +29.92 | +28.70 | +1% | 24.49 | ja | 23 s | +2.44 / +27.49 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3056 (17) | 62% | +8.20 | +8.06 | +9% | 22.99 | ja | 4 s | +2.69 / +5.50 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5754 (42) | 38% | +6.95 | +5.95 | +1% | 22.15 | ja | 19 s | +3.97 / +2.98 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2323 (45) | 59% | +6.18 | +5.91 | +7% | 21.24 | ja | 4 s | +2.23 / +3.95 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2031 (21) | 51% | +3.76 | +2.84 | +1% | 17.71 | ja | 10 s | +0.95 / +2.81 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2391 (41) | 44% | +25.73 | +23.58 | +1% | 16.3 | ja | 24 s | +7.41 / +18.32 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1743 (13) | 48% | +4.17 | +2.95 | +0% | 15.04 | ja | 38 s | +2.41 / +1.76 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1670 (11) | 51% | +7.95 | +7.21 | +1% | 14.35 | ja | 37 s | +1.45 / +6.50 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1247 (27) | 44% | +3.21 | +2.79 | +3% | 13.92 | ja | 61 s | +1.30 / +1.90 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 485 (1) | 62% | +11.90 | +11.07 | +10% | 13.77 | ja | 1 s | +4.54 / +7.36 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1685 (5) | 55% | +1.20 | +1.11 | +1% | 12.54 | ja | 10 s | +0.48 / +0.72 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1728 (23) | 52% | +2.97 | +2.91 | +10% | 11.85 | ja | 4 s | +1.02 / +1.95 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1069 (4) | 43% | +10.75 | +9.71 | +3% | 11.77 | ja | 30 s | +5.58 / +5.17 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 541 (0) | 49% | +8.21 | +7.44 | +4% | 11.34 | ja | 1 s | +1.58 / +6.62 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1879 (2) | 49% | +5.27 | +4.82 | +1% | 11.17 | nee | 7 s | +2.29 / +2.98 |
| 16 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 335 (3) | 59% | +11.30 | +9.33 | +5% | 10.9 | ja | 8 s | +3.65 / +7.65 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 75 (1) | 57% | +23.08 | +21.07 | +33% | 10.26 | ja | 52 s | +11.36 / +11.72 |
| 18 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 309 (15) | 51% | +0.79 | +0.69 | +6% | 10.19 | ja | 7 s | +0.29 / +0.50 |
| 19 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 75 (1) | 59% | +25.91 | +23.92 | +36% | 10.09 | ja | 48 s | +16.57 / +9.34 |
| 20 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 661 (5) | 68% | +3.24 | +2.99 | +2% | 9.97 | ja | 11 s | +3.10 / +0.14 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 43 (0) | 81% | +326.76 | +301.84 | +78% | 10.89 | ja | 8 s | -0.81 / +327.57 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.65 | nee | 12 s | +135.01 / +157.20 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.93 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 225 (0) | 62% | +127.09 | +93.14 | +15% | 8.26 | ja | 15 s | +44.67 / +82.42 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.2 | nee | 102 s | +60.24 / +37.88 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 20 (5) | 75% | +58.99 | +47.15 | +32% | 4.56 | nee | 6 s | +10.52 / +48.47 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 170 (1) | 77% | +57.40 | +53.79 | +13% | 7.4 | ja | 9 s | +27.43 / +29.97 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 72 (3) | 96% | +44.62 | +42.52 | +20% | 5.58 | nee | 16 s | +15.80 / +28.83 |
| 12 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.6 | nee | 106 s | +31.47 / +10.49 |
| 13 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.94 | ja | 6 min | +8.52 / +30.81 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 97 (14) | 53% | +37.70 | +32.89 | +13% | 5.82 | nee | 89 s | +15.41 / +22.29 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (0) | 78% | +32.82 | +30.50 | +12% | 5.13 | nee | 24 s | +16.31 / +16.52 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5629 (73) | 45% | +29.92 | +28.70 | +1% | 24.49 | ja | 23 s | +2.44 / +27.49 |
| 18 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.19 | ja | 13 s | +18.98 / +8.49 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 10 (0) | 70% | +27.03 | +12.48 | +65% | 4.99 | nee | 12 s | +17.52 / +9.51 |

## Geluk-toets

Populatie: 6757 wallets met ≥ 20 posities, 89 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.03 | 4.46 | 5.66 |
| #10 | 9.69 | 3.37 | 3.71 |
| #20 | 8.09 | 3.07 | 3.23 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.66): **49**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14863 | 49% | +5.7% | -0.3% | +124.83 |
| top 20 op winst (A) | 19/20 | 716 | 57% | +10.4% | +3.9% | +233.96 |
| alle wallets | – | 393018 | 31% | -11.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.3% / +0.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3426): ρ = 0.516. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 128

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14863 | 30% | -11.1% | -7.2% | -331.04 |
| 2 s | 14863 | 24% | -14.3% | -8.9% | -424.00 |
| 10 s | 14863 | 22% | -15.2% | -8.8% | -450.64 |
| 60 s | 14863 | 19% | -18.5% | -8.0% | -550.60 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 312

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 34686 | 31% | -10.9% | -7.1% | -759.52 |
| 2 s | 34686 | 25% | -13.9% | -8.7% | -964.58 |
| 10 s | 34686 | 23% | -14.8% | -8.4% | -1026.03 |
| 60 s | 34686 | 19% | -18.1% | -7.6% | -1254.52 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 96

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6764 | 33% | -1.6% | -5.3% | -22.10 |
| 2 s | 6764 | 27% | -5.4% | -6.8% | -72.69 |
| 10 s | 6764 | 25% | -6.4% | -6.6% | -86.31 |
| 60 s | 6764 | 22% | -6.3% | -5.7% | -85.39 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
