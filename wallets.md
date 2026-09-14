# Wallet-analyse pump.fun — 2026-09-14 03:28 UTC

## Kort antwoord

- Geluk-toets: 78 van 7652 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=23.98, geluk-grens 5.44).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -7.8%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.8%, 2 s: -15.6%, 10 s: -17.0%, 60 s: -20.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 03:18 UTC → 2026-09-14 03:18 UTC (72.0 uur), helft A/B-grens: 2026-09-12 15:18 UTC
- 6836758 trades, 68063 tokens, 194054 wallets, 2060898 posities (907715 geopend vanaf ≥ $7k, 1153183 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 129901
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8137 | 2885 | +140.96 | +78.50 | +377.65 | 9865.60 | 16491 | +2932.34 |
| dev | 2195 | 5690 | +1935.51 | -312.65 | +1983.72 | 1703.90 | 16759 | +1617.50 |
| bot_hf | 2974 | 213369 | +826.72 | -1095.27 | +6469.67 | 10549.73 | 385137 | +9080.73 |
| swing | 2021 | 22762 | -928.76 | -1224.80 | -97.11 | 57.24 | 17044 | +76.45 |
| incidenteel | 152925 | 173849 | -4227.38 | -8855.82 | +27691.73 | 3926.77 | 270730 | +13045.02 |
| scalper | 25802 | 489160 | -12955.57 | -16005.08 | +22802.62 | 2712.53 | 447022 | +3006.28 |

Wallets met ≥ 10 posities: 16356, waarvan winstgevend: 21%. De top 1% winnaars pakt 39% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15208.51 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4170 (23) | 62% | +11.67 | +11.52 | +8% | 25.05 | ja | 4 s | +6.03 / +5.64 |
| 2 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3092 (62) | 59% | +6.67 | +6.40 | +5% | 24.06 | ja | 4 s | +4.41 / +2.26 |
| 3 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.05 | ja | 110 s | +140.38 / +658.24 |
| 4 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6992 (87) | 45% | +39.12 | +37.97 | +1% | 23.68 | ja | 25 s | +25.09 / +14.04 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6653 (60) | 39% | +7.22 | +6.30 | +0% | 20.64 | ja | 19 s | +4.67 / +2.55 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2480 (42) | 47% | +63.87 | +60.64 | +2% | 15.53 | ja | 25 s | +26.69 / +37.18 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2170 (13) | 50% | +21.28 | +20.06 | +1% | 15.51 | ja | 41 s | +8.44 / +12.84 |
| 8 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3325 (45) | 38% | +56.18 | +49.23 | +2% | 15.24 | ja | 30 s | +38.96 / +17.22 |
| 9 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.65 | ja | 110 s | +53.26 / +222.65 |
| 10 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 254 (56) | 56% | +0.17 | +0.16 | +25% | 14.42 | ja | 16 s | +0.01 / +0.16 |
| 11 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 565 (0) | 64% | +15.18 | +14.51 | +11% | 14.38 | ja | 1 s | +10.36 / +4.81 |
| 12 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.21 | ja | 7 s | +327.57 / +253.93 |
| 13 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1540 (28) | 45% | +4.04 | +3.74 | +3% | 13.49 | ja | 61 s | +2.76 / +1.28 |
| 14 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1805 (9) | 54% | +13.73 | +13.01 | +2% | 13.49 | ja | 40 s | +10.06 / +3.67 |
| 15 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.41 | ja | 110 s | +29.11 / +183.15 |
| 16 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1985 (10) | 55% | +2.07 | +1.95 | +2% | 12.18 | ja | 10 s | +1.16 / +0.92 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (2) | 82% | +23.12 | +15.29 | +159% | 11.88 | ja | 78 s | +2.58 / +20.54 |
| 18 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.65 | ja | 50 s | +2.65 / +14.93 |
| 19 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1475 (3) | 40% | +7.09 | +6.12 | +1% | 11.29 | ja | 26 s | +6.42 / +0.67 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1385 (32) | 41% | +0.75 | +0.47 | +1% | 11.18 | ja | 61 s | +0.69 / +0.06 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.05 | ja | 110 s | +140.38 / +658.24 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.21 | ja | 7 s | +327.57 / +253.93 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.0 | nee | 12 s | +292.21 / +26.80 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.65 | ja | 110 s | +53.26 / +222.65 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.41 | ja | 110 s | +29.11 / +183.15 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 243 (3) | 67% | +161.90 | +127.95 | +18% | 8.08 | ja | 15 s | +102.35 / +59.55 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.87 | nee | 2 min | +158.23 / +0.00 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.29 | ja | 6 s | +48.47 / +80.03 |
| 9 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 33 (1) | 58% | +116.66 | +100.06 | +48% | 7.01 | ja | 2 min | +1.04 / +115.62 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2480 (42) | 47% | +63.87 | +60.64 | +2% | 15.53 | ja | 25 s | +26.69 / +37.18 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 10 (0) | 90% | +61.28 | +50.48 | +66% | 4.45 | nee | 5 s | +38.05 / +23.23 |
| 12 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 158 (1) | 75% | +60.57 | +56.97 | +15% | 6.66 | ja | 8 s | +38.10 / +22.47 |
| 13 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (0) | 98% | +57.61 | +54.99 | +22% | 6.28 | ja | 16 s | +30.12 / +27.48 |
| 14 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3325 (45) | 38% | +56.18 | +49.23 | +2% | 15.24 | ja | 30 s | +38.96 / +17.22 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.91 | nee | 8 s | +9.56 / +44.68 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.85 | ja | 5 min | +36.59 / +15.89 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.35 | nee | 30 s | +0.00 / +50.13 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (1) | 82% | +47.87 | +42.88 | +16% | 5.39 | nee | 35 s | +17.86 / +30.01 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 20 | [4euy…ndfU](https://solscan.io/account/4euyaqBe45J5dniAcNARERUo7B1wG96riG21sEpNndfU) | scalper | 6 (0) | 50% | +44.30 | +25.34 | +69% | 1.74 | nee | 54 s | +13.04 / +31.26 |

## Geluk-toets

Populatie: 7652 wallets met ≥ 20 posities, 77 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 23.98 | 4.45 | 5.44 |
| #10 | 12.24 | 3.46 | 3.68 |
| #20 | 9.54 | 3.13 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.44): **78**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 18122 | 48% | +5.0% | -0.3% | +366.84 |
| top 20 op winst (A) | 16/20 | 6293 | 45% | +3.2% | -1.1% | +963.30 |
| alle wallets | – | 378492 | 33% | -7.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.3% / +0.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3599): ρ = 0.518. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 228

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 18122 | 30% | -12.8% | -8.0% | -464.59 |
| 2 s | 18122 | 25% | -15.6% | -9.4% | -564.68 |
| 10 s | 18122 | 22% | -17.0% | -9.5% | -616.96 |
| 60 s | 18122 | 19% | -20.1% | -8.1% | -729.15 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 428

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38103 | 29% | -11.4% | -8.0% | -869.78 |
| 2 s | 38103 | 25% | -14.4% | -9.6% | -1098.97 |
| 10 s | 38103 | 23% | -15.8% | -9.5% | -1205.53 |
| 60 s | 38103 | 20% | -18.8% | -8.2% | -1429.55 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 96

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6704 | 32% | -1.8% | -8.1% | -24.16 |
| 2 s | 6704 | 26% | -7.0% | -10.1% | -93.97 |
| 10 s | 6704 | 26% | -7.4% | -8.6% | -99.39 |
| 60 s | 6704 | 24% | -6.9% | -6.0% | -92.36 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
