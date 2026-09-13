# Wallet-analyse pump.fun — 2026-09-13 17:56 UTC

## Kort antwoord

- Geluk-toets: 67 van 8048 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.45, geluk-grens 5.47).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.5% per positie (alle wallets: -8.3%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.2%, 2 s: -15.2%, 10 s: -16.6%, 60 s: -20.3% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 17:51 UTC → 2026-09-13 17:51 UTC (72.0 uur), helft A/B-grens: 2026-09-12 05:51 UTC
- 6254391 trades, 58050 tokens, 201010 wallets, 1897900 posities (969836 geopend vanaf ≥ $7k, 928064 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 138508
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9724 | 5182 | +384.50 | +317.91 | +823.12 | 19029.37 | 21647 | +3645.79 |
| dev | 2156 | 6073 | +1737.75 | -508.59 | +1585.47 | 3918.41 | 14718 | +1064.95 |
| swing | 1905 | 21660 | -912.71 | -1238.61 | -308.68 | 94.17 | 13171 | +51.41 |
| bot_hf | 3090 | 217024 | +315.44 | -1718.44 | +6140.94 | 12647.46 | 320875 | +7851.63 |
| incidenteel | 156702 | 196582 | -5984.46 | -12167.52 | +23351.74 | 7686.72 | 208976 | +10467.99 |
| scalper | 27433 | 523315 | -15296.56 | -18803.00 | +19932.61 | 7147.62 | 348677 | +2639.29 |

Wallets met ≥ 10 posities: 17096, waarvan winstgevend: 20%. De top 1% winnaars pakt 38% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -19756.04 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3993 (23) | 62% | +12.14 | +12.01 | +9% | 25.48 | ja | 4 s | +6.81 / +5.33 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6825 (80) | 45% | +42.66 | +41.52 | +1% | 25.38 | ja | 24 s | +16.36 / +26.31 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3053 (63) | 59% | +7.63 | +7.37 | +6% | 23.55 | ja | 4 s | +5.15 / +2.49 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6856 (63) | 38% | +6.79 | +5.79 | +0% | 22.4 | ja | 19 s | +4.63 / +2.16 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2663 (51) | 46% | +46.55 | +44.40 | +2% | 16.64 | ja | 25 s | +20.43 / +26.12 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2148 (15) | 49% | +8.55 | +7.33 | +1% | 15.67 | ja | 40 s | +3.20 / +5.35 |
| 7 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3481 (54) | 36% | +32.70 | +25.75 | +1% | 15.56 | ja | 31 s | +10.22 / +22.49 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1561 (30) | 44% | +4.34 | +4.04 | +3% | 14.7 | ja | 60 s | +2.76 / +1.58 |
| 9 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1894 (11) | 52% | +10.61 | +9.88 | +1% | 14.45 | ja | 39 s | +3.97 / +6.64 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 559 (1) | 63% | +13.15 | +12.48 | +10% | 14.25 | ja | 1 s | +9.93 / +3.21 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2016 (8) | 56% | +2.14 | +2.04 | +2% | 13.07 | ja | 10 s | +1.09 / +1.05 |
| 12 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2190 (23) | 53% | +3.62 | +3.56 | +10% | 12.62 | ja | 4 s | +2.25 / +1.38 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2851 (2) | 48% | +4.88 | +4.43 | +0% | 12.37 | ja | 7 s | +3.77 / +1.11 |
| 15 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 50 (0) | 84% | +392.65 | +367.73 | +79% | 12.26 | ja | 7 s | +269.09 / +123.56 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 632 (0) | 50% | +9.34 | +8.57 | +4% | 11.82 | ja | 1 s | +7.74 / +1.60 |
| 17 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1371 (4) | 41% | +9.40 | +8.36 | +2% | 11.72 | ja | 25 s | +8.41 / +0.99 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 77 (1) | 58% | +31.43 | +28.41 | +42% | 11.03 | ja | 47 s | +16.81 / +14.62 |
| 19 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 77 (1) | 57% | +29.31 | +26.12 | +39% | 10.85 | ja | 58 s | +13.51 / +15.80 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1203 (28) | 40% | +0.93 | +0.64 | +1% | 10.8 | ja | 62 s | +0.77 / +0.15 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.03 | nee | 101 s | +86.41 / +366.88 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 50 (0) | 84% | +392.65 | +367.73 | +79% | 12.26 | ja | 7 s | +269.09 / +123.56 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 15.97 | nee | 12 s | +206.40 / +112.61 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 272 (1) | 65% | +163.70 | +129.75 | +16% | 8.52 | ja | 15 s | +70.94 / +92.76 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +158.23 / +0.00 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.46 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (9) | 74% | +112.93 | +101.09 | +36% | 6.12 | ja | 6 s | +52.09 / +60.84 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 173 (1) | 78% | +66.42 | +62.82 | +15% | 7.7 | ja | 9 s | +46.89 / +19.54 |
| 10 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 92 (1) | 79% | +54.91 | +49.93 | +15% | 5.81 | nee | 30 s | +20.88 / +34.04 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 7 (1) | 86% | +54.25 | +21.19 | +153% | 6.43 | nee | 8 s | +9.56 / +44.68 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 83 (4) | 95% | +53.56 | +50.95 | +21% | 6.1 | nee | 16 s | +28.78 / +24.78 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 155 (9) | 60% | +49.63 | +42.43 | +15% | 7.26 | ja | 113 s | +23.48 / +26.15 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +48.86 | +38.05 | +67% | 4.01 | nee | 4 s | +34.69 / +14.17 |
| 15 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 9 (0) | 89% | +47.16 | +24.35 | +42% | 3.47 | nee | 33 s | +0.00 / +47.16 |
| 16 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 17 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 26 (5) | 77% | +46.58 | +39.69 | +71% | 9.02 | ja | 6 min | +17.93 / +28.65 |
| 18 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2663 (51) | 46% | +46.55 | +44.40 | +2% | 16.64 | ja | 25 s | +20.43 / +26.12 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6825 (80) | 45% | +42.66 | +41.52 | +1% | 25.38 | ja | 24 s | +16.36 / +26.31 |
| 20 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.14 | nee | 112 s | +1.20 / +41.26 |

## Geluk-toets

Populatie: 8048 wallets met ≥ 20 posities, 73 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.45 | 4.56 | 5.47 |
| #10 | 10.44 | 3.47 | 3.67 |
| #20 | 8.93 | 3.16 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.47): **67**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 14389 | 49% | +5.5% | -0.1% | +239.60 |
| top 20 op winst (A) | 16/20 | 1375 | 54% | +8.0% | +1.9% | +463.39 |
| alle wallets | – | 341048 | 33% | -8.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.4% / +2.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3564): ρ = 0.51. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 142

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14389 | 30% | -12.2% | -7.5% | -350.59 |
| 2 s | 14389 | 24% | -15.2% | -9.1% | -438.95 |
| 10 s | 14389 | 22% | -16.6% | -9.0% | -477.28 |
| 60 s | 14389 | 18% | -20.3% | -8.2% | -584.38 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 409

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 43522 | 29% | -11.4% | -7.9% | -990.30 |
| 2 s | 43522 | 24% | -14.3% | -9.4% | -1249.02 |
| 10 s | 43522 | 22% | -15.4% | -9.1% | -1342.91 |
| 60 s | 43522 | 19% | -18.6% | -8.1% | -1620.95 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 146

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10523 | 32% | -2.2% | -5.6% | -46.43 |
| 2 s | 10523 | 28% | -5.3% | -6.9% | -111.85 |
| 10 s | 10523 | 26% | -5.9% | -6.8% | -124.50 |
| 60 s | 10523 | 24% | -6.1% | -5.8% | -128.75 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
