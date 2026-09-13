# Wallet-analyse pump.fun — 2026-09-13 20:34 UTC

## Kort antwoord

- Geluk-toets: 82 van 7837 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.34, geluk-grens 5.17).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.4% per positie (alle wallets: -8.3%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.1%, 2 s: -15.2%, 10 s: -16.5%, 60 s: -19.8% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 20:27 UTC → 2026-09-13 20:27 UTC (72.0 uur), helft A/B-grens: 2026-09-12 08:27 UTC
- 6399772 trades, 60887 tokens, 200202 wallets, 1938083 posities (944626 geopend vanaf ≥ $7k, 993457 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 135287
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9695 | 4201 | +440.40 | +377.12 | +835.10 | 16201.63 | 19210 | +3607.66 |
| dev | 2189 | 5930 | +1813.43 | -449.19 | +1714.14 | 2994.68 | 15142 | +1098.95 |
| swing | 1898 | 21783 | -908.05 | -1194.66 | -261.91 | 79.41 | 14359 | +34.20 |
| bot_hf | 3026 | 216195 | +563.95 | -1397.96 | +6345.78 | 11650.92 | 340601 | +8413.92 |
| incidenteel | 156960 | 190708 | -5245.07 | -11184.60 | +25866.27 | 6761.43 | 229550 | +10983.97 |
| scalper | 26434 | 505809 | -14765.31 | -18142.64 | +20214.27 | 5932.22 | 374595 | +2837.36 |

Wallets met ≥ 10 posities: 16740, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18100.65 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6856 (80) | 45% | +43.72 | +42.58 | +1% | 25.14 | ja | 25 s | +18.04 / +25.68 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3960 (24) | 61% | +11.91 | +11.76 | +9% | 24.78 | ja | 4 s | +6.23 / +5.68 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3011 (64) | 59% | +7.29 | +7.02 | +6% | 23.36 | ja | 4 s | +4.60 / +2.68 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6691 (60) | 38% | +5.85 | +4.93 | +0% | 21.76 | ja | 19 s | +3.04 / +2.81 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2568 (48) | 46% | +41.86 | +39.71 | +1% | 15.75 | ja | 25 s | +13.76 / +28.11 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2121 (12) | 49% | +12.67 | +11.45 | +1% | 15.7 | ja | 40 s | +5.08 / +7.59 |
| 7 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3396 (52) | 36% | +28.95 | +22.00 | +1% | 15.01 | ja | 30 s | +10.41 / +18.54 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1580 (32) | 44% | +4.57 | +4.27 | +3% | 14.66 | ja | 61 s | +2.89 / +1.68 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 553 (0) | 64% | +14.55 | +13.89 | +11% | 14.41 | ja | 1 s | +9.97 / +4.59 |
| 10 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1835 (11) | 52% | +12.12 | +11.39 | +1% | 14.28 | ja | 40 s | +5.48 / +6.64 |
| 11 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.18 | ja | 7 s | +287.31 / +294.19 |
| 12 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 13 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1987 (8) | 55% | +1.62 | +1.51 | +1% | 12.33 | ja | 10 s | +0.84 / +0.77 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2156 (22) | 53% | +3.38 | +3.32 | +9% | 12.04 | ja | 4 s | +1.99 / +1.40 |
| 15 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1422 (5) | 41% | +9.20 | +8.16 | +2% | 11.65 | ja | 26 s | +6.89 / +2.31 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 589 (0) | 50% | +9.15 | +8.38 | +5% | 11.34 | ja | 1 s | +7.71 / +1.44 |
| 17 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1299 (32) | 40% | +0.84 | +0.55 | +1% | 11.0 | ja | 62 s | +0.73 / +0.11 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 81 (1) | 57% | +31.52 | +28.50 | +39% | 10.92 | ja | 45 s | +16.81 / +14.71 |
| 19 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 81 (1) | 57% | +29.49 | +26.30 | +37% | 10.8 | ja | 53 s | +13.51 / +15.98 |
| 20 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1057 (7) | 63% | +1.33 | +1.11 | +0% | 10.75 | ja | 14 s | +1.33 / +0.01 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.18 | ja | 7 s | +287.31 / +294.19 |
| 2 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.03 | nee | 101 s | +86.41 / +366.88 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 15.97 | nee | 12 s | +206.40 / +112.61 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +158.23 / +0.00 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 260 (1) | 64% | +155.71 | +121.75 | +16% | 8.3 | ja | 16 s | +67.34 / +88.37 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.46 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 40 (8) | 78% | +133.90 | +122.06 | +40% | 7.36 | ja | 6 s | +49.23 / +84.67 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 158 (1) | 75% | +59.59 | +55.99 | +15% | 7.06 | ja | 9 s | +41.34 / +18.25 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 79 (2) | 98% | +57.98 | +55.37 | +23% | 6.35 | ja | 27 s | +24.95 / +33.03 |
| 11 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 93 (1) | 81% | +56.65 | +51.66 | +16% | 5.97 | nee | 30 s | +20.80 / +35.85 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.89 | nee | 8 s | +9.56 / +44.68 |
| 13 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.83 | ja | 5 min | +20.16 / +32.32 |
| 14 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.34 | nee | 30 s | +0.00 / +50.13 |
| 15 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +48.86 | +38.05 | +67% | 4.02 | nee | 4 s | +38.05 / +10.80 |
| 16 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6856 (80) | 45% | +43.72 | +42.58 | +1% | 25.14 | ja | 25 s | +18.04 / +25.68 |
| 18 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.14 | nee | 112 s | +1.20 / +41.26 |
| 19 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2568 (48) | 46% | +41.86 | +39.71 | +1% | 15.75 | ja | 25 s | +13.76 / +28.11 |
| 20 | [9Yrc…ax2G](https://solscan.io/account/9YrcswPY5NhbhUUStRCHzF3n2oF8NCZbQtrHHeUMax2G) | bot_hf | 51 (0) | 59% | +41.30 | +31.32 | +20% | 3.35 | nee | 7 s | +0.54 / +40.76 |

## Geluk-toets

Populatie: 7837 wallets met ≥ 20 posities, 75 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.34 | 4.44 | 5.17 |
| #10 | 10.57 | 3.43 | 3.64 |
| #20 | 9.14 | 3.13 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.17): **82**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 15519 | 48% | +5.4% | -0.5% | +433.23 |
| top 20 op winst (A) | 16/20 | 3340 | 49% | +4.6% | -0.1% | +654.25 |
| alle wallets | – | 355553 | 33% | -8.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.4% / +1.1% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3637): ρ = 0.533. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 158

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 15519 | 29% | -12.1% | -8.0% | -375.67 |
| 2 s | 15519 | 24% | -15.2% | -9.6% | -472.86 |
| 10 s | 15519 | 21% | -16.5% | -9.4% | -512.85 |
| 60 s | 15519 | 19% | -19.8% | -8.3% | -615.24 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 410

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41335 | 30% | -11.8% | -8.3% | -975.38 |
| 2 s | 41335 | 24% | -14.8% | -9.8% | -1227.06 |
| 10 s | 41335 | 22% | -16.0% | -9.6% | -1320.29 |
| 60 s | 41335 | 19% | -19.3% | -8.5% | -1593.80 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 137

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10349 | 32% | -2.4% | -5.6% | -49.60 |
| 2 s | 10349 | 28% | -5.5% | -6.9% | -114.34 |
| 10 s | 10349 | 26% | -6.2% | -6.8% | -127.38 |
| 60 s | 10349 | 24% | -6.1% | -5.8% | -126.81 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
