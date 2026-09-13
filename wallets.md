# Wallet-analyse pump.fun — 2026-09-13 12:39 UTC

## Kort antwoord

- Geluk-toets: 66 van 7984 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.12, geluk-grens 5.31).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.5% per positie (alle wallets: -8.4%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.2%, 2 s: -16.5%, 10 s: -17.9%, 60 s: -22.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 12:36 UTC (70.8 uur), helft A/B-grens: 2026-09-12 01:12 UTC
- 5945197 trades, 53436 tokens, 200885 wallets, 1802216 posities (971417 geopend vanaf ≥ $7k, 830799 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 135420
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10253 | 5859 | +54.97 | -23.00 | +536.95 | 21493.44 | 22024 | +3166.52 |
| dev | 2127 | 6174 | +1463.24 | -829.10 | +1342.83 | 5009.39 | 14522 | +1117.40 |
| swing | 1796 | 20449 | -936.60 | -1272.99 | -417.58 | 83.45 | 11284 | +40.53 |
| bot_hf | 3045 | 217319 | +93.48 | -1990.02 | +6042.53 | 13787.96 | 291325 | +7733.47 |
| incidenteel | 156089 | 203859 | -6454.57 | -12638.30 | +20886.11 | 8770.29 | 187917 | +9138.31 |
| scalper | 27575 | 517757 | -15171.76 | -18583.89 | +20536.17 | 8827.95 | 303727 | +2254.45 |

Wallets met ≥ 10 posities: 16799, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20951.23 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6774 (87) | 45% | +46.44 | +45.22 | +1% | 26.4 | ja | 24 s | +13.80 / +32.64 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3945 (20) | 62% | +11.78 | +11.64 | +9% | 25.55 | ja | 4 s | +5.95 / +5.83 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3010 (61) | 59% | +7.64 | +7.37 | +6% | 23.81 | ja | 4 s | +3.95 / +3.68 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6785 (56) | 38% | +7.77 | +6.76 | +0% | 23.24 | ja | 19 s | +4.11 / +3.66 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2722 (48) | 45% | +39.69 | +37.54 | +1% | 17.19 | ja | 25 s | +15.28 / +24.41 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2092 (14) | 48% | +7.83 | +6.62 | +1% | 15.94 | ja | 39 s | +4.23 / +3.60 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1526 (32) | 44% | +4.62 | +4.20 | +3% | 15.26 | ja | 61 s | +1.55 / +3.07 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1916 (12) | 51% | +8.79 | +8.06 | +1% | 14.87 | ja | 38 s | +5.52 / +3.27 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 558 (1) | 63% | +13.76 | +12.93 | +10% | 14.29 | ja | 1 s | +9.62 / +4.14 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1974 (8) | 55% | +1.89 | +1.79 | +2% | 13.22 | ja | 10 s | +0.61 / +1.29 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2184 (25) | 52% | +3.69 | +3.63 | +10% | 12.96 | ja | 4 s | +2.19 / +1.51 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1274 (4) | 42% | +12.57 | +11.53 | +3% | 12.4 | ja | 26 s | +9.49 / +3.08 |
| 13 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 652 (0) | 49% | +9.35 | +8.59 | +4% | 12.0 | ja | 1 s | +7.44 / +1.91 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2541 (2) | 48% | +4.84 | +4.39 | +0% | 11.93 | ja | 7 s | +2.88 / +1.96 |
| 15 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.93 | ja | 53 s | +18.31 / +12.34 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.86 | ja | 51 s | +23.78 / +10.46 |
| 17 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.81 | ja | 15 s | +0.83 / +0.23 |
| 18 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.76 | ja | 8 s | +269.26 / +60.38 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 786 (5) | 68% | +4.08 | +3.80 | +2% | 10.75 | ja | 10 s | +2.61 / +1.48 |
| 20 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 742 (6) | 70% | +5.21 | +4.94 | +2% | 10.69 | ja | 10 s | +2.67 / +2.54 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.76 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.64 | nee | 12 s | +206.40 / +85.81 |
| 3 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 12 (0) | 83% | +233.39 | +181.66 | +245% | 14.06 | nee | 79 s | +0.00 / +233.39 |
| 4 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.86 | nee | 2 min | +158.23 / +0.00 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 262 (0) | 63% | +139.12 | +105.17 | +15% | 8.4 | ja | 15 s | +69.36 / +69.77 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 16 (0) | 62% | +131.10 | +105.86 | +134% | 10.51 | nee | 102 s | +60.24 / +70.86 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 15 (0) | 73% | +89.39 | +72.29 | +98% | 8.91 | nee | 110 s | +34.55 / +54.84 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.43 | nee | 6 s | +50.06 / +36.00 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 187 (1) | 76% | +62.33 | +58.72 | +13% | 7.52 | ja | 9 s | +42.62 / +19.71 |
| 10 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 170 (9) | 59% | +53.78 | +46.58 | +14% | 7.49 | ja | 113 s | +28.35 / +25.43 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.8 | nee | 9 s | +9.56 / +43.32 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.08 | nee | 16 s | +29.18 / +23.39 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.67 | nee | 26 s | +25.17 / +21.66 |
| 14 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 15 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6774 (87) | 45% | +46.44 | +45.22 | +1% | 26.4 | ja | 24 s | +13.80 / +32.64 |
| 16 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.02 | nee | 96 s | +29.11 / +15.73 |
| 17 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2722 (48) | 45% | +39.69 | +37.54 | +1% | 17.19 | ja | 25 s | +15.28 / +24.41 |
| 18 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 19 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.93 | ja | 6 min | +20.67 / +18.65 |
| 20 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +35.01 / +3.37 |

## Geluk-toets

Populatie: 7984 wallets met ≥ 20 posities, 74 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.12 | 4.47 | 5.31 |
| #10 | 10.63 | 3.45 | 3.71 |
| #20 | 8.37 | 3.16 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.31): **66**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13258 | 49% | +6.5% | -0.0% | +176.54 |
| top 20 op winst (A) | 16/20 | 475 | 66% | +16.8% | +9.3% | +308.51 |
| alle wallets | – | 319589 | 33% | -8.4% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.9% / +1.6% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3414): ρ = 0.47. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 129

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13258 | 29% | -13.2% | -8.1% | -351.28 |
| 2 s | 13258 | 23% | -16.5% | -9.8% | -436.42 |
| 10 s | 13258 | 21% | -17.9% | -9.8% | -476.06 |
| 60 s | 13258 | 18% | -22.1% | -9.3% | -587.36 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 343

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40966 | 32% | -11.6% | -7.3% | -949.76 |
| 2 s | 40966 | 25% | -14.6% | -8.9% | -1194.43 |
| 10 s | 40966 | 23% | -15.6% | -8.7% | -1277.30 |
| 60 s | 40966 | 18% | -19.1% | -7.9% | -1562.81 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 163

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10600 | 32% | -2.4% | -5.6% | -51.46 |
| 2 s | 10600 | 27% | -5.5% | -7.1% | -117.65 |
| 10 s | 10600 | 26% | -6.2% | -6.9% | -131.22 |
| 60 s | 10600 | 23% | -6.3% | -5.8% | -132.69 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
