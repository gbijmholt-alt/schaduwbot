# Wallet-analyse pump.fun — 2026-09-13 13:44 UTC

## Kort antwoord

- Geluk-toets: 62 van 8111 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.4, geluk-grens 5.54).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.3% per positie (alle wallets: -8.4%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -16.1%, 10 s: -17.7%, 60 s: -21.7% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 13:40 UTC (71.9 uur), helft A/B-grens: 2026-09-12 01:44 UTC
- 6042752 trades, 54404 tokens, 202358 wallets, 1833894 posities (986877 geopend vanaf ≥ $7k, 847017 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 137809
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10315 | 5908 | +203.45 | +123.82 | +689.50 | 21757.61 | 22535 | +3237.00 |
| dev | 2147 | 6192 | +1474.35 | -836.65 | +1348.73 | 5008.86 | 14630 | +1150.14 |
| swing | 1825 | 20795 | -942.14 | -1281.55 | -410.55 | 85.49 | 11623 | +33.99 |
| bot_hf | 3088 | 221574 | +47.66 | -2083.30 | +6021.44 | 13819.73 | 296133 | +7750.56 |
| incidenteel | 157095 | 205054 | -6392.13 | -12582.05 | +21858.35 | 8776.32 | 190099 | +9346.02 |
| scalper | 27888 | 527354 | -15539.20 | -19005.54 | +20806.51 | 8856.80 | 311997 | +2325.98 |

Wallets met ≥ 10 posities: 17131, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -21148.02 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6926 (87) | 45% | +47.42 | +46.20 | +1% | 26.54 | ja | 24 s | +15.08 / +32.34 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4031 (21) | 62% | +12.16 | +12.02 | +9% | 25.79 | ja | 4 s | +6.30 / +5.86 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3054 (64) | 59% | +7.96 | +7.70 | +6% | 23.95 | ja | 4 s | +4.63 / +3.33 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6949 (58) | 38% | +7.97 | +6.97 | +0% | 23.38 | ja | 19 s | +4.80 / +3.17 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2771 (49) | 45% | +45.36 | +43.21 | +1% | 17.49 | ja | 24 s | +16.11 / +29.24 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2129 (14) | 49% | +9.63 | +8.42 | +1% | 16.13 | ja | 38 s | +4.56 / +5.07 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1563 (33) | 44% | +4.63 | +4.21 | +3% | 15.33 | ja | 61 s | +1.75 / +2.88 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1944 (13) | 51% | +10.20 | +9.47 | +1% | 15.08 | ja | 38 s | +5.54 / +4.66 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 565 (1) | 62% | +13.65 | +12.82 | +10% | 14.26 | ja | 1 s | +9.77 / +3.88 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2010 (9) | 55% | +2.11 | +2.00 | +2% | 13.39 | ja | 10 s | +0.72 / +1.38 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2211 (26) | 52% | +3.74 | +3.68 | +10% | 12.99 | ja | 4 s | +2.35 / +1.39 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1296 (5) | 42% | +12.77 | +11.73 | +3% | 12.43 | ja | 26 s | +9.55 / +3.22 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2617 (2) | 48% | +4.52 | +4.07 | +0% | 12.05 | ja | 7 s | +3.58 / +0.94 |
| 14 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 657 (0) | 49% | +9.33 | +8.56 | +4% | 11.95 | ja | 1 s | +7.51 / +1.82 |
| 15 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.94 | ja | 53 s | +18.31 / +12.34 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.87 | ja | 51 s | +23.78 / +10.46 |
| 17 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 754 (6) | 70% | +5.32 | +5.05 | +2% | 10.8 | ja | 10 s | +2.89 / +2.43 |
| 18 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +269.26 / +60.38 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 795 (5) | 67% | +3.58 | +3.29 | +1% | 10.63 | ja | 11 s | +3.15 / +0.43 |
| 20 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | scalper | 1183 (48) | 44% | +12.38 | +11.04 | +3% | 10.25 | ja | 2 min | +7.71 / +4.66 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 15 (0) | 87% | +372.89 | +321.16 | +281% | 18.08 | nee | 110 s | +0.00 / +372.89 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +269.26 / +60.38 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.65 | nee | 12 s | +206.40 / +85.81 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 19 (0) | 68% | +170.04 | +144.81 | +140% | 12.6 | nee | 2 min | +60.24 / +109.80 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +158.23 / +0.00 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 266 (0) | 63% | +140.01 | +106.06 | +14% | 8.4 | ja | 15 s | +69.66 / +70.35 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 18 (0) | 72% | +116.78 | +97.85 | +98% | 9.96 | nee | 3 min | +34.55 / +82.24 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.44 | nee | 6 s | +50.06 / +36.00 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 189 (1) | 76% | +64.94 | +61.33 | +14% | 7.67 | ja | 9 s | +43.96 / +20.98 |
| 10 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 179 (10) | 60% | +55.65 | +48.45 | +14% | 7.55 | ja | 113 s | +28.35 / +27.30 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.8 | nee | 9 s | +9.56 / +43.32 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.08 | nee | 16 s | +29.79 / +22.78 |
| 13 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 18 (1) | 56% | +52.35 | +39.91 | +45% | 5.08 | nee | 2 min | +6.37 / +45.98 |
| 14 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6926 (87) | 45% | +47.42 | +46.20 | +1% | 26.54 | ja | 24 s | +15.08 / +32.34 |
| 15 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.68 | nee | 26 s | +25.17 / +21.66 |
| 16 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 17 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2771 (49) | 45% | +45.36 | +43.21 | +1% | 17.49 | ja | 24 s | +16.11 / +29.24 |
| 18 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.02 | nee | 96 s | +29.11 / +15.73 |
| 19 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 20 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 24 (4) | 79% | +39.32 | +32.43 | +72% | 8.72 | ja | 6 min | +20.67 / +18.65 |

## Geluk-toets

Populatie: 8111 wallets met ≥ 20 posities, 72 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.4 | 4.51 | 5.54 |
| #10 | 10.71 | 3.46 | 3.68 |
| #20 | 8.36 | 3.17 | 3.33 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.54): **62**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13564 | 49% | +6.3% | -0.1% | +182.61 |
| top 20 op winst (A) | 16/20 | 419 | 68% | +17.2% | +10.1% | +298.38 |
| alle wallets | – | 327101 | 33% | -8.4% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.4% / +2.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3439): ρ = 0.461. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 135

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13564 | 29% | -13.0% | -8.0% | -351.67 |
| 2 s | 13564 | 23% | -16.1% | -9.6% | -437.93 |
| 10 s | 13564 | 21% | -17.7% | -9.6% | -478.96 |
| 60 s | 13564 | 18% | -21.7% | -9.1% | -588.80 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 390

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41668 | 31% | -11.5% | -7.4% | -958.70 |
| 2 s | 41668 | 25% | -14.5% | -9.0% | -1205.73 |
| 10 s | 41668 | 23% | -15.6% | -8.8% | -1301.86 |
| 60 s | 41668 | 19% | -19.1% | -8.1% | -1594.27 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 167

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10836 | 32% | -2.2% | -5.6% | -48.60 |
| 2 s | 10836 | 28% | -5.5% | -7.0% | -118.51 |
| 10 s | 10836 | 26% | -6.2% | -6.9% | -134.17 |
| 60 s | 10836 | 24% | -6.2% | -5.8% | -135.41 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
