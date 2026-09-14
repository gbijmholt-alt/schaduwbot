# Wallet-analyse pump.fun — 2026-09-14 16:40 UTC

## Kort antwoord

- Geluk-toets: 81 van 7651 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.32, geluk-grens 5.32).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.7% per positie (alle wallets: -9.3%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.5%, 2 s: -15.3%, 10 s: -16.7%, 60 s: -19.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 16:29 UTC → 2026-09-14 16:29 UTC (72.0 uur), helft A/B-grens: 2026-09-13 04:29 UTC
- 7154599 trades, 71759 tokens, 200540 wallets, 2151001 posities (900358 geopend vanaf ≥ $7k, 1250643 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 127157
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9408 | 2676 | +95.02 | +41.94 | +333.76 | 8156.76 | 15735 | +2424.89 |
| bot_hf | 2952 | 213586 | +928.02 | -232.26 | +5241.50 | 9107.09 | 401699 | +9088.20 |
| dev | 2259 | 5351 | +2005.20 | -322.66 | +1980.02 | 61.00 | 17781 | +1763.75 |
| swing | 2066 | 20169 | -1016.89 | -1317.98 | -239.49 | 59.47 | 19581 | +16.69 |
| incidenteel | 158294 | 172121 | -4035.61 | -8352.05 | +30992.66 | 3094.99 | 296320 | +15148.68 |
| scalper | 25561 | 486455 | -13138.11 | -16250.47 | +22473.63 | 1259.83 | 499527 | +3233.78 |

Wallets met ≥ 10 posities: 16363, waarvan winstgevend: 21%. De top 1% winnaars pakt 41% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15162.38 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.51 | ja | 118 s | +140.38 / +984.50 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4326 (25) | 62% | +12.05 | +11.90 | +8% | 24.88 | ja | 4 s | +7.97 / +4.08 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3145 (66) | 58% | +6.34 | +6.07 | +5% | 24.45 | ja | 4 s | +5.46 / +0.87 |
| 4 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7134 (93) | 45% | +46.83 | +45.70 | +1% | 24.33 | ja | 26 s | +31.34 / +15.49 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6570 (54) | 39% | +7.54 | +6.61 | +0% | 20.3 | ja | 18 s | +3.65 / +3.89 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2842 (28) | 50% | +7.86 | +6.94 | +1% | 18.7 | ja | 10 s | +1.36 / +6.49 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.04 | ja | 110 s | +37.88 / +355.13 |
| 8 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 352 (68) | 54% | +0.33 | +0.31 | +29% | 16.61 | ja | 22 s | +0.02 / +0.32 |
| 9 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2219 (12) | 50% | +18.70 | +17.55 | +1% | 15.91 | ja | 44 s | +1.25 / +17.46 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2551 (40) | 47% | +63.10 | +59.88 | +2% | 15.65 | ja | 22 s | +22.38 / +40.73 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3357 (40) | 38% | +66.26 | +59.30 | +2% | 15.22 | ja | 29 s | +44.81 / +21.45 |
| 12 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.79 | ja | 110 s | +25.67 / +257.92 |
| 13 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 88% | +624.04 | +599.12 | +63% | 14.19 | ja | 7 s | +306.16 / +317.88 |
| 14 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1715 (5) | 54% | +12.00 | +11.27 | +2% | 13.2 | ja | 42 s | +7.21 / +4.79 |
| 15 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1497 (26) | 45% | +3.74 | +3.44 | +2% | 13.16 | ja | 60 s | +2.73 / +1.00 |
| 16 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 506 (0) | 63% | +13.66 | +12.99 | +11% | 13.0 | ja | 1 s | +7.62 / +6.04 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 21 (2) | 81% | +22.69 | +14.86 | +163% | 11.81 | ja | 82 s | +5.50 / +17.19 |
| 18 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1492 (1) | 41% | +7.41 | +6.43 | +2% | 11.46 | ja | 26 s | +6.86 / +0.55 |
| 19 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 20 (1) | 85% | +16.95 | +11.59 | +84% | 11.42 | ja | 52 s | +4.82 / +12.13 |
| 20 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2035 (14) | 55% | +1.74 | +1.62 | +1% | 11.36 | ja | 10 s | +1.38 / +0.36 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.51 | ja | 118 s | +140.38 / +984.50 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 88% | +624.04 | +599.12 | +63% | 14.19 | ja | 7 s | +306.16 / +317.88 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.04 | ja | 110 s | +37.88 / +355.13 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.79 | ja | 110 s | +25.67 / +257.92 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 18 (1) | 94% | +199.73 | +171.04 | +134% | 13.32 | nee | 2 min | +158.23 / +41.50 |
| 6 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.47 | ja | 2 min | +4.01 / +166.71 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 259 (4) | 63% | +155.35 | +121.39 | +15% | 7.25 | ja | 15 s | +89.19 / +66.15 |
| 8 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 5 (0) | 100% | +148.95 | +112.61 | +166% | 9.82 | nee | 11 s | +122.15 / +26.80 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 37 (7) | 78% | +125.29 | +113.45 | +41% | 7.04 | ja | 6 s | +72.33 / +52.96 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 18 (1) | 61% | +77.86 | +52.30 | +55% | 6.24 | nee | 2 min | +46.59 / +31.27 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.88 | nee | 6 s | +38.05 / +32.04 |
| 12 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.04 | nee | 33 s | +0.00 / +69.17 |
| 13 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 158 (0) | 78% | +67.30 | +63.70 | +16% | 7.07 | ja | 9 s | +34.32 / +32.98 |
| 14 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3357 (40) | 38% | +66.26 | +59.30 | +2% | 15.22 | ja | 29 s | +44.81 / +21.45 |
| 15 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2551 (40) | 47% | +63.10 | +59.88 | +2% | 15.65 | ja | 22 s | +22.38 / +40.73 |
| 16 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 139 (0) | 73% | +63.05 | +58.56 | +18% | 7.72 | ja | 89 s | +12.93 / +50.11 |
| 17 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 60 (0) | 57% | +58.45 | +39.69 | +25% | 4.08 | nee | 11 s | -0.36 / +58.82 |
| 18 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 7 (0) | 100% | +56.81 | +23.76 | +142% | 6.91 | nee | 7 s | +47.40 / +9.42 |
| 19 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 78 (1) | 95% | +54.32 | +51.70 | +22% | 6.08 | nee | 20 s | +35.40 / +18.92 |
| 20 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 25 (5) | 76% | +53.51 | +46.62 | +80% | 10.21 | ja | 3 min | +29.47 / +24.04 |

## Geluk-toets

Populatie: 7651 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.32 | 4.5 | 5.32 |
| #10 | 12.65 | 3.45 | 3.64 |
| #20 | 9.57 | 3.15 | 3.28 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.32): **81**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 18337 | 48% | +4.7% | -0.5% | +523.17 |
| top 20 op winst (A) | 19/20 | 7009 | 45% | +2.9% | -1.0% | +740.45 |
| alle wallets | – | 437531 | 33% | -9.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.6% / +3.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3692): ρ = 0.553. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 188

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 18337 | 29% | -12.5% | -7.9% | -458.38 |
| 2 s | 18337 | 24% | -15.3% | -9.4% | -560.20 |
| 10 s | 18337 | 22% | -16.7% | -9.5% | -611.15 |
| 60 s | 18337 | 20% | -19.6% | -8.0% | -719.01 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 421

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39982 | 30% | -11.5% | -7.6% | -916.76 |
| 2 s | 39982 | 25% | -14.5% | -9.2% | -1159.37 |
| 10 s | 39982 | 23% | -15.9% | -9.0% | -1268.08 |
| 60 s | 39982 | 20% | -18.8% | -7.8% | -1500.62 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 90

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6981 | 32% | -1.1% | -8.0% | -15.27 |
| 2 s | 6981 | 27% | -6.6% | -10.0% | -92.38 |
| 10 s | 6981 | 26% | -7.0% | -8.4% | -98.35 |
| 60 s | 6981 | 24% | -6.8% | -6.0% | -94.87 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
