# Wallet-analyse pump.fun — 2026-09-13 15:10 UTC

## Kort antwoord

- Geluk-toets: 72 van 8166 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.33, geluk-grens 5.4).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.2% per positie (alle wallets: -8.3%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.7%, 2 s: -16.0%, 10 s: -17.4%, 60 s: -21.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 15:07 UTC → 2026-09-13 15:07 UTC (72.0 uur), helft A/B-grens: 2026-09-12 03:07 UTC
- 6088351 trades, 55562 tokens, 200273 wallets, 1847577 posities (980409 geopend vanaf ≥ $7k, 867168 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 138364
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 10121 | 5520 | +329.68 | +259.07 | +810.70 | 20933.59 | 22578 | +3374.46 |
| dev | 2130 | 6107 | +1465.46 | -861.31 | +1233.81 | 4710.65 | 14814 | +1178.80 |
| swing | 1865 | 21237 | -965.10 | -1298.95 | -386.22 | 87.84 | 11907 | +41.69 |
| bot_hf | 3021 | 218527 | +160.10 | -1948.54 | +6002.16 | 13524.56 | 301549 | +7712.90 |
| incidenteel | 155290 | 200116 | -6351.99 | -12561.25 | +22476.73 | 8307.26 | 194204 | +9525.99 |
| scalper | 27846 | 528902 | -15098.60 | -18619.29 | +20403.08 | 8490.38 | 322116 | +2427.31 |

Wallets met ≥ 10 posities: 17177, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20460.45 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6939 (84) | 45% | +46.17 | +44.95 | +1% | 26.11 | ja | 24 s | +16.44 / +29.74 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4021 (22) | 62% | +12.01 | +11.87 | +9% | 25.58 | ja | 4 s | +6.49 / +5.52 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3059 (64) | 59% | +7.79 | +7.53 | +6% | 23.95 | ja | 4 s | +4.66 / +3.13 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6968 (58) | 38% | +7.41 | +6.40 | +0% | 22.91 | ja | 19 s | +3.77 / +3.63 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2744 (49) | 46% | +45.14 | +43.00 | +1% | 17.0 | ja | 25 s | +13.18 / +31.96 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2171 (15) | 49% | +9.44 | +8.22 | +1% | 16.02 | ja | 39 s | +6.33 / +3.11 |
| 7 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1958 (13) | 51% | +10.69 | +9.96 | +1% | 14.97 | ja | 38 s | +6.44 / +4.25 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1572 (33) | 44% | +4.58 | +4.17 | +3% | 14.95 | ja | 61 s | +2.21 / +2.38 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 557 (1) | 63% | +13.71 | +12.88 | +10% | 14.1 | ja | 1 s | +10.34 / +3.37 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1999 (8) | 55% | +2.29 | +2.18 | +2% | 13.22 | ja | 10 s | +0.77 / +1.51 |
| 11 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.97 | ja | 119 s | +77.01 / +111.56 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2209 (24) | 52% | +3.68 | +3.61 | +10% | 12.82 | ja | 4 s | +2.22 / +1.46 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2617 (2) | 48% | +4.52 | +4.07 | +0% | 12.04 | ja | 7 s | +3.64 / +0.87 |
| 14 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1308 (4) | 41% | +11.07 | +10.03 | +3% | 12.03 | ja | 26 s | +9.13 / +1.94 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 644 (0) | 50% | +9.55 | +8.78 | +4% | 11.76 | ja | 1 s | +8.22 / +1.33 |
| 16 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 78 (1) | 58% | +31.42 | +28.41 | +42% | 11.55 | ja | 51 s | +19.62 / +11.80 |
| 17 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 78 (1) | 56% | +29.27 | +26.08 | +40% | 11.5 | ja | 56 s | +15.63 / +13.63 |
| 18 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +269.26 / +60.38 |
| 19 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1126 (27) | 41% | +1.16 | +0.87 | +1% | 10.73 | ja | 62 s | +0.22 / +0.94 |
| 20 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 744 (5) | 70% | +5.04 | +4.77 | +2% | 10.57 | ja | 10 s | +2.71 / +2.33 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.06 | nee | 101 s | +84.37 / +368.92 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.77 | ja | 8 s | +269.26 / +60.38 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.66 | nee | 12 s | +206.40 / +85.81 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.97 | ja | 119 s | +77.01 / +111.56 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +158.23 / +0.00 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 265 (0) | 64% | +141.53 | +107.58 | +15% | 8.36 | ja | 15 s | +70.21 / +71.32 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.48 | ja | 2 min | +41.57 / +96.42 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.44 | nee | 6 s | +52.09 / +33.97 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 188 (1) | 77% | +68.59 | +64.98 | +14% | 7.88 | ja | 9 s | +45.22 / +23.37 |
| 10 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 175 (9) | 59% | +52.91 | +45.71 | +14% | 7.48 | ja | 115 s | +26.75 / +26.15 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.8 | nee | 9 s | +9.56 / +43.32 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (3) | 96% | +52.68 | +50.06 | +21% | 6.09 | nee | 16 s | +31.62 / +21.06 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 14 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6939 (84) | 45% | +46.17 | +44.95 | +1% | 26.11 | ja | 24 s | +16.44 / +29.74 |
| 15 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 92 (1) | 77% | +46.17 | +41.19 | +13% | 5.59 | nee | 27 s | +24.52 / +21.66 |
| 16 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2744 (49) | 46% | +45.14 | +43.00 | +1% | 17.0 | ja | 25 s | +13.18 / +31.96 |
| 17 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 108 (16) | 54% | +43.53 | +38.73 | +14% | 5.92 | nee | 96 s | +27.84 / +15.70 |
| 18 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 24 (3) | 83% | +43.44 | +36.54 | +77% | 9.27 | ja | 7 min | +19.69 / +23.75 |
| 19 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.15 | nee | 112 s | +3.71 / +38.75 |
| 20 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |

## Geluk-toets

Populatie: 8166 wallets met ≥ 20 posities, 72 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.33 | 4.7 | 5.4 |
| #10 | 10.72 | 3.46 | 3.68 |
| #20 | 8.9 | 3.19 | 3.34 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.4): **72**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 13546 | 49% | +6.2% | -0.1% | +192.42 |
| top 20 op winst (A) | 16/20 | 395 | 69% | +15.7% | +10.3% | +291.00 |
| alle wallets | – | 326701 | 33% | -8.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.9% / +1.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3468): ρ = 0.459. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 134

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13546 | 29% | -12.7% | -7.9% | -343.14 |
| 2 s | 13546 | 23% | -16.0% | -9.6% | -432.23 |
| 10 s | 13546 | 21% | -17.4% | -9.4% | -470.38 |
| 60 s | 13546 | 19% | -21.4% | -8.9% | -578.89 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 364

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40859 | 30% | -11.7% | -7.6% | -953.29 |
| 2 s | 40859 | 24% | -14.7% | -9.1% | -1198.45 |
| 10 s | 40859 | 22% | -15.8% | -8.9% | -1287.99 |
| 60 s | 40859 | 19% | -19.3% | -8.1% | -1578.60 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 163

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10823 | 32% | -2.2% | -5.6% | -47.50 |
| 2 s | 10823 | 28% | -5.5% | -7.0% | -119.32 |
| 10 s | 10823 | 26% | -6.2% | -6.9% | -133.66 |
| 60 s | 10823 | 24% | -6.3% | -5.8% | -135.63 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
