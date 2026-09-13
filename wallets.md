# Wallet-analyse pump.fun — 2026-09-13 11:46 UTC

## Kort antwoord

- Geluk-toets: 65 van 7919 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=17.91, geluk-grens 5.26).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.4% per positie (alle wallets: -8.6%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.4%, 2 s: -16.6%, 10 s: -18.0%, 60 s: -22.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 11:43 UTC (69.9 uur), helft A/B-grens: 2026-09-12 00:45 UTC
- 5870637 trades, 52732 tokens, 199603 wallets, 1778391 posities (963682 geopend vanaf ≥ $7k, 814709 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 134458
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10203 | 5828 | -2.44 | -79.56 | +481.40 | 21391.16 | 21315 | +3152.10 |
| dev | 2099 | 6120 | +1456.16 | -807.76 | +1344.27 | 5009.39 | 14389 | +1092.85 |
| swing | 1780 | 20218 | -931.95 | -1273.98 | -398.74 | 79.68 | 11000 | +48.10 |
| bot_hf | 3015 | 216019 | +93.57 | -1970.23 | +5168.94 | 13746.14 | 287483 | +7562.08 |
| incidenteel | 155116 | 203096 | -6370.39 | -12578.68 | +20289.86 | 8756.21 | 184810 | +8880.94 |
| scalper | 27390 | 512401 | -14938.58 | -18300.99 | +21339.84 | 8812.76 | 295712 | +2198.19 |

Wallets met ≥ 10 posities: 16675, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20693.63 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6691 (85) | 45% | +45.87 | +44.64 | +1% | 26.26 | ja | 24 s | +14.08 / +31.78 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3933 (20) | 62% | +11.78 | +11.64 | +9% | 25.37 | ja | 4 s | +5.97 / +5.81 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2996 (60) | 59% | +7.76 | +7.49 | +6% | 23.86 | ja | 4 s | +3.80 / +3.96 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6736 (56) | 38% | +7.59 | +6.58 | +0% | 23.14 | ja | 19 s | +4.51 / +3.08 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2707 (48) | 45% | +38.44 | +36.30 | +1% | 17.12 | ja | 25 s | +15.58 / +22.86 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2068 (14) | 48% | +7.07 | +5.85 | +0% | 15.72 | ja | 39 s | +4.51 / +2.56 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1510 (32) | 44% | +4.52 | +4.10 | +3% | 15.13 | ja | 61 s | +1.56 / +2.95 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1895 (12) | 51% | +8.32 | +7.58 | +1% | 14.74 | ja | 38 s | +5.14 / +3.17 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 557 (1) | 63% | +13.50 | +12.67 | +10% | 14.25 | ja | 1 s | +9.53 / +3.97 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1956 (8) | 55% | +1.88 | +1.77 | +2% | 13.17 | ja | 10 s | +0.72 / +1.16 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2178 (25) | 52% | +3.68 | +3.61 | +10% | 12.87 | ja | 4 s | +2.21 / +1.47 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1249 (4) | 42% | +12.51 | +11.46 | +3% | 12.34 | ja | 26 s | +9.42 / +3.09 |
| 13 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 649 (0) | 49% | +9.29 | +8.53 | +4% | 11.99 | ja | 1 s | +7.35 / +1.94 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.92 | ja | 53 s | +18.31 / +12.34 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.86 | ja | 51 s | +23.78 / +10.46 |
| 16 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1272 (7) | 63% | +1.06 | +0.84 | +0% | 11.8 | ja | 15 s | +1.00 / +0.06 |
| 17 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2506 (2) | 48% | +4.57 | +4.12 | +0% | 11.8 | ja | 7 s | +2.73 / +1.85 |
| 18 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 783 (5) | 68% | +4.48 | +4.20 | +2% | 10.85 | ja | 10 s | +2.60 / +1.88 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.75 | ja | 8 s | +269.26 / +60.38 |
| 20 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 742 (6) | 70% | +5.21 | +4.94 | +2% | 10.68 | ja | 10 s | +2.57 / +2.64 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.75 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.63 | nee | 12 s | +206.40 / +85.81 |
| 3 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 11 (0) | 82% | +181.66 | +135.96 | +233% | 12.45 | nee | 64 s | +0.00 / +181.66 |
| 4 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +158.23 / +0.00 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 262 (0) | 63% | +139.12 | +105.17 | +15% | 8.39 | ja | 15 s | +69.36 / +69.77 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 14 (0) | 64% | +113.18 | +87.94 | +129% | 9.77 | nee | 102 s | +60.24 / +52.93 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.43 | nee | 6 s | +50.06 / +36.00 |
| 8 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 14 (0) | 71% | +74.42 | +57.33 | +90% | 8.07 | nee | 108 s | +34.55 / +39.88 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 187 (1) | 76% | +62.33 | +58.72 | +13% | 7.52 | ja | 9 s | +42.62 / +19.71 |
| 10 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 165 (9) | 59% | +53.16 | +45.95 | +15% | 7.41 | ja | 113 s | +28.35 / +24.81 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.79 | nee | 9 s | +9.56 / +43.32 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.08 | nee | 16 s | +29.18 / +23.39 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.67 | nee | 26 s | +25.17 / +21.66 |
| 14 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 15 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6691 (85) | 45% | +45.87 | +44.64 | +1% | 26.26 | ja | 24 s | +14.08 / +31.78 |
| 16 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.02 | nee | 96 s | +29.11 / +15.73 |
| 17 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 18 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.92 | ja | 6 min | +20.67 / +18.65 |
| 19 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2707 (48) | 45% | +38.44 | +36.30 | +1% | 17.12 | ja | 25 s | +15.58 / +22.86 |
| 20 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |

## Geluk-toets

Populatie: 7919 wallets met ≥ 20 posities, 74 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 17.91 | 4.33 | 5.26 |
| #10 | 10.49 | 3.41 | 3.65 |
| #20 | 8.36 | 3.11 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.26): **65**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13190 | 49% | +6.4% | -0.1% | +171.01 |
| top 20 op winst (A) | 16/20 | 467 | 66% | +16.8% | +9.1% | +306.67 |
| alle wallets | – | 317320 | 33% | -8.6% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.4% / +2.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3367): ρ = 0.468. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 125

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13190 | 29% | -13.4% | -8.2% | -353.24 |
| 2 s | 13190 | 23% | -16.6% | -9.8% | -437.26 |
| 10 s | 13190 | 21% | -18.0% | -9.8% | -475.61 |
| 60 s | 13190 | 18% | -22.4% | -9.3% | -589.79 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 340

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40641 | 32% | -11.6% | -7.3% | -944.83 |
| 2 s | 40641 | 25% | -14.6% | -8.9% | -1187.73 |
| 10 s | 40641 | 23% | -15.6% | -8.7% | -1269.97 |
| 60 s | 40641 | 18% | -19.1% | -7.9% | -1554.61 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 161

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10493 | 32% | -2.5% | -5.7% | -51.84 |
| 2 s | 10493 | 27% | -5.6% | -7.1% | -116.96 |
| 10 s | 10493 | 26% | -6.2% | -6.9% | -130.01 |
| 60 s | 10493 | 23% | -6.3% | -5.8% | -131.42 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
