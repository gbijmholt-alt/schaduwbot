# Wallet-analyse pump.fun — 2026-09-13 18:29 UTC

## Kort antwoord

- Geluk-toets: 68 van 8001 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.17, geluk-grens 5.46).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.3% per positie (alle wallets: -8.4%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.1%, 2 s: -15.2%, 10 s: -16.4%, 60 s: -19.8% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 18:22 UTC → 2026-09-13 18:22 UTC (72.0 uur), helft A/B-grens: 2026-09-12 06:22 UTC
- 6293738 trades, 58654 tokens, 201693 wallets, 1908649 posities (967684 geopend vanaf ≥ $7k, 940965 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 138214
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9676 | 5109 | +434.19 | +364.80 | +872.87 | 18509.41 | 21844 | +3650.84 |
| dev | 2175 | 6073 | +1768.26 | -488.02 | +1610.66 | 3591.73 | 14821 | +1050.43 |
| swing | 1917 | 21724 | -911.91 | -1228.94 | -275.07 | 91.39 | 13460 | +64.03 |
| bot_hf | 3047 | 218531 | +457.05 | -1556.72 | +6273.73 | 12466.59 | 325863 | +8020.28 |
| incidenteel | 157491 | 196867 | -6033.56 | -12178.97 | +23652.94 | 7647.52 | 213066 | +10706.01 |
| scalper | 27387 | 519380 | -15333.79 | -18793.77 | +20045.77 | 6925.22 | 351911 | +2555.45 |

Wallets met ≥ 10 posities: 17032, waarvan winstgevend: 20%. De top 1% winnaars pakt 38% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -19619.76 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6840 (80) | 45% | +42.75 | +41.60 | +1% | 25.37 | ja | 24 s | +17.37 / +25.38 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3978 (23) | 62% | +11.87 | +11.73 | +9% | 25.1 | ja | 4 s | +6.53 / +5.34 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3043 (63) | 59% | +7.65 | +7.38 | +6% | 23.51 | ja | 4 s | +4.87 / +2.78 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6809 (63) | 38% | +5.84 | +4.92 | +0% | 22.3 | ja | 19 s | +3.05 / +2.79 |
| 5 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2652 (52) | 46% | +45.43 | +43.28 | +1% | 16.53 | ja | 25 s | +17.49 / +27.94 |
| 6 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3463 (57) | 36% | +35.20 | +28.25 | +1% | 15.62 | ja | 30 s | +13.45 / +21.76 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2138 (13) | 49% | +10.03 | +8.81 | +1% | 15.59 | ja | 40 s | +4.93 / +5.10 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1587 (32) | 44% | +4.21 | +3.91 | +3% | 14.71 | ja | 60 s | +2.59 / +1.61 |
| 9 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1887 (11) | 52% | +11.24 | +10.50 | +1% | 14.48 | ja | 39 s | +4.64 / +6.60 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 553 (0) | 64% | +13.62 | +12.96 | +10% | 14.29 | ja | 1 s | +10.28 / +3.35 |
| 11 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 55 (0) | 86% | +454.17 | +429.25 | +77% | 13.21 | ja | 7 s | +269.36 / +184.82 |
| 12 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2023 (8) | 56% | +1.99 | +1.88 | +2% | 13.05 | ja | 10 s | +1.07 / +0.92 |
| 13 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2177 (22) | 53% | +3.63 | +3.57 | +10% | 12.66 | ja | 4 s | +2.18 / +1.45 |
| 15 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2902 (2) | 48% | +5.47 | +5.02 | +0% | 12.6 | ja | 7 s | +4.00 / +1.47 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 625 (0) | 50% | +9.57 | +8.80 | +5% | 11.75 | ja | 1 s | +8.01 / +1.55 |
| 17 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1381 (4) | 41% | +9.07 | +8.03 | +2% | 11.66 | ja | 25 s | +8.01 / +1.06 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 78 (1) | 58% | +30.68 | +27.67 | +40% | 10.87 | ja | 43 s | +16.81 / +13.88 |
| 19 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 766 (5) | 71% | +6.33 | +6.07 | +3% | 10.85 | ja | 10 s | +2.81 / +3.52 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1235 (31) | 40% | +0.77 | +0.48 | +1% | 10.85 | ja | 62 s | +0.70 / +0.07 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 55 (0) | 86% | +454.17 | +429.25 | +77% | 13.21 | ja | 7 s | +269.36 / +184.82 |
| 2 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.02 | nee | 101 s | +86.41 / +366.88 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 15.97 | nee | 12 s | +206.40 / +112.61 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 269 (1) | 64% | +161.40 | +127.44 | +16% | 8.53 | ja | 15 s | +69.69 / +91.71 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +158.23 / +0.00 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.46 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 40 (8) | 78% | +131.74 | +119.90 | +40% | 7.25 | ja | 6 s | +52.09 / +79.65 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 169 (1) | 78% | +64.83 | +61.22 | +15% | 7.63 | ja | 9 s | +44.82 / +20.01 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 84 (3) | 96% | +56.24 | +53.62 | +21% | 6.32 | nee | 16 s | +28.78 / +27.46 |
| 11 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 92 (1) | 78% | +54.62 | +49.64 | +15% | 5.81 | nee | 30 s | +20.63 / +33.99 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.89 | nee | 8 s | +9.56 / +44.68 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 155 (9) | 60% | +49.63 | +42.43 | +15% | 7.26 | ja | 113 s | +23.48 / +26.15 |
| 14 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 10 (0) | 90% | +49.33 | +26.52 | +41% | 3.49 | nee | 31 s | +0.00 / +49.33 |
| 15 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +48.86 | +38.05 | +67% | 4.02 | nee | 4 s | +34.69 / +14.17 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (5) | 78% | +48.08 | +41.18 | +69% | 9.04 | ja | 6 min | +17.93 / +30.14 |
| 17 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 18 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2652 (52) | 46% | +45.43 | +43.28 | +1% | 16.53 | ja | 25 s | +17.49 / +27.94 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6840 (80) | 45% | +42.75 | +41.60 | +1% | 25.37 | ja | 24 s | +17.37 / +25.38 |
| 20 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.14 | nee | 112 s | +1.20 / +41.26 |

## Geluk-toets

Populatie: 8001 wallets met ≥ 20 posities, 73 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.17 | 4.47 | 5.46 |
| #10 | 10.43 | 3.45 | 3.64 |
| #20 | 9.05 | 3.15 | 3.28 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.46): **68**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 15127 | 48% | +5.3% | -0.6% | +320.35 |
| top 20 op winst (A) | 16/20 | 1376 | 55% | +9.1% | +2.3% | +578.66 |
| alle wallets | – | 344307 | 33% | -8.4% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.6% / +2.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3554): ρ = 0.522. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 159

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 15127 | 29% | -12.1% | -8.0% | -365.73 |
| 2 s | 15127 | 23% | -15.2% | -9.7% | -460.04 |
| 10 s | 15127 | 21% | -16.4% | -9.3% | -495.98 |
| 60 s | 15127 | 19% | -19.8% | -8.3% | -598.59 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 419

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 44214 | 30% | -11.3% | -7.8% | -996.97 |
| 2 s | 44214 | 24% | -14.1% | -9.2% | -1249.81 |
| 10 s | 44214 | 22% | -15.2% | -8.9% | -1346.13 |
| 60 s | 44214 | 19% | -18.4% | -7.9% | -1626.94 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 146

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10529 | 32% | -2.2% | -5.6% | -46.64 |
| 2 s | 10529 | 28% | -5.3% | -7.0% | -112.15 |
| 10 s | 10529 | 26% | -5.9% | -6.8% | -124.67 |
| 60 s | 10529 | 24% | -6.1% | -5.8% | -129.07 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
