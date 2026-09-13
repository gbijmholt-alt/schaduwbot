# Wallet-analyse pump.fun — 2026-09-13 13:25 UTC

## Kort antwoord

- Geluk-toets: 59 van 8070 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.27, geluk-grens 5.73).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.3% per positie (alle wallets: -8.4%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.9%, 2 s: -16.1%, 10 s: -17.6%, 60 s: -21.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 13:22 UTC (71.6 uur), helft A/B-grens: 2026-09-12 01:35 UTC
- 6008773 trades, 54111 tokens, 201876 wallets, 1822738 posities (981921 geopend vanaf ≥ $7k, 840817 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 137295
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10296 | 5888 | +201.47 | +122.18 | +686.78 | 21674.09 | 22335 | +3204.36 |
| dev | 2141 | 6168 | +1473.75 | -830.98 | +1344.25 | 5008.86 | 14598 | +1175.65 |
| swing | 1825 | 20759 | -943.71 | -1284.70 | -391.08 | 85.47 | 11550 | +34.35 |
| bot_hf | 3073 | 220188 | +76.67 | -2033.02 | +6141.02 | 13802.54 | 294483 | +7737.60 |
| incidenteel | 156770 | 204683 | -6409.51 | -12576.52 | +21521.82 | 8772.26 | 189077 | +9278.49 |
| scalper | 27771 | 524235 | -15373.29 | -18804.37 | +20915.12 | 8847.30 | 308774 | +2296.72 |

Wallets met ≥ 10 posities: 17022, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20974.61 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6868 (89) | 45% | +46.38 | +45.16 | +1% | 26.44 | ja | 24 s | +14.27 / +32.12 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3990 (21) | 62% | +11.86 | +11.72 | +9% | 25.65 | ja | 4 s | +6.26 / +5.60 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3035 (61) | 59% | +7.68 | +7.41 | +6% | 23.91 | ja | 4 s | +4.58 / +3.10 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6904 (58) | 38% | +8.32 | +7.32 | +1% | 23.42 | ja | 19 s | +4.42 / +3.90 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2757 (49) | 45% | +44.16 | +42.01 | +1% | 17.41 | ja | 25 s | +16.75 / +27.41 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2119 (15) | 48% | +10.06 | +8.84 | +1% | 16.11 | ja | 39 s | +4.39 / +5.67 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1551 (33) | 44% | +4.65 | +4.23 | +3% | 15.29 | ja | 61 s | +1.73 / +2.92 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1938 (12) | 51% | +10.14 | +9.40 | +1% | 15.07 | ja | 38 s | +5.67 / +4.47 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 559 (1) | 63% | +13.72 | +12.89 | +10% | 14.25 | ja | 1 s | +9.77 / +3.95 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1998 (8) | 55% | +2.02 | +1.91 | +2% | 13.33 | ja | 10 s | +0.67 / +1.35 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2199 (25) | 52% | +3.73 | +3.66 | +10% | 13.02 | ja | 4 s | +2.26 / +1.47 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1289 (4) | 42% | +12.35 | +11.31 | +3% | 12.38 | ja | 26 s | +9.50 / +2.85 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2595 (2) | 48% | +4.26 | +3.81 | +0% | 11.97 | ja | 7 s | +3.55 / +0.71 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.94 | ja | 53 s | +18.31 / +12.34 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 657 (0) | 49% | +9.33 | +8.56 | +4% | 11.93 | ja | 1 s | +7.51 / +1.82 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.87 | ja | 51 s | +23.78 / +10.46 |
| 17 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.76 | ja | 8 s | +269.26 / +60.38 |
| 18 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 750 (6) | 70% | +5.18 | +4.92 | +2% | 10.74 | ja | 10 s | +2.77 / +2.41 |
| 19 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 794 (5) | 68% | +3.62 | +3.34 | +1% | 10.63 | ja | 11 s | +3.06 / +0.56 |
| 20 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | scalper | 1181 (49) | 44% | +12.43 | +11.09 | +3% | 10.25 | ja | 2 min | +7.96 / +4.47 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 15 (0) | 87% | +372.89 | +321.16 | +281% | 18.03 | nee | 110 s | +0.00 / +372.89 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.76 | ja | 8 s | +269.26 / +60.38 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.65 | nee | 12 s | +206.40 / +85.81 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 19 (0) | 68% | +170.04 | +144.81 | +140% | 12.57 | nee | 2 min | +60.24 / +109.80 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +158.23 / +0.00 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 265 (1) | 63% | +140.10 | +106.15 | +14% | 8.41 | ja | 15 s | +69.36 / +70.75 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 18 (0) | 72% | +116.78 | +97.85 | +98% | 9.93 | nee | 3 min | +34.55 / +82.24 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.44 | nee | 6 s | +50.06 / +36.00 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 188 (2) | 76% | +62.33 | +58.72 | +13% | 7.5 | ja | 9 s | +43.43 / +18.90 |
| 10 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 175 (10) | 59% | +54.69 | +47.49 | +14% | 7.53 | ja | 113 s | +28.35 / +26.34 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.8 | nee | 9 s | +9.56 / +43.32 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.08 | nee | 16 s | +29.32 / +23.25 |
| 13 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 18 (1) | 56% | +52.35 | +39.91 | +45% | 5.04 | nee | 2 min | +6.37 / +45.98 |
| 14 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.68 | nee | 26 s | +25.17 / +21.66 |
| 15 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 16 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6868 (89) | 45% | +46.38 | +45.16 | +1% | 26.44 | ja | 24 s | +14.27 / +32.12 |
| 17 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.02 | nee | 96 s | +29.11 / +15.73 |
| 18 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2757 (49) | 45% | +44.16 | +42.01 | +1% | 17.41 | ja | 25 s | +16.75 / +27.41 |
| 19 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 20 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.93 | ja | 6 min | +20.67 / +18.65 |

## Geluk-toets

Populatie: 8070 wallets met ≥ 20 posities, 73 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.27 | 4.43 | 5.73 |
| #10 | 10.67 | 3.44 | 3.68 |
| #20 | 8.39 | 3.15 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.73): **59**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13441 | 49% | +6.3% | -0.1% | +182.02 |
| top 20 op winst (A) | 16/20 | 420 | 68% | +17.0% | +10.0% | +297.26 |
| alle wallets | – | 324779 | 33% | -8.4% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.8% / +1.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3434): ρ = 0.462. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 134

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13441 | 29% | -12.9% | -7.9% | -347.24 |
| 2 s | 13441 | 23% | -16.1% | -9.6% | -433.97 |
| 10 s | 13441 | 21% | -17.6% | -9.5% | -472.57 |
| 60 s | 13441 | 18% | -21.6% | -9.0% | -581.54 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 387

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41397 | 31% | -11.5% | -7.4% | -952.02 |
| 2 s | 41397 | 25% | -14.5% | -9.0% | -1198.57 |
| 10 s | 41397 | 23% | -15.6% | -8.8% | -1292.62 |
| 60 s | 41397 | 19% | -19.1% | -8.1% | -1581.78 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 168

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10757 | 32% | -2.2% | -5.6% | -48.42 |
| 2 s | 10757 | 28% | -5.5% | -7.0% | -118.09 |
| 10 s | 10757 | 26% | -6.2% | -6.9% | -133.60 |
| 60 s | 10757 | 24% | -6.2% | -5.8% | -134.57 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
