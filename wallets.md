# Wallet-analyse pump.fun — 2026-09-14 20:52 UTC

## Kort antwoord

- Geluk-toets: 79 van 7716 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.36, geluk-grens 5.38).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.8% per positie (alle wallets: -10.7%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.3%, 2 s: -15.0%, 10 s: -16.3%, 60 s: -18.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 20:41 UTC → 2026-09-14 20:41 UTC (72.0 uur), helft A/B-grens: 2026-09-13 08:41 UTC
- 7229176 trades, 73802 tokens, 206737 wallets, 2204627 posities (901948 geopend vanaf ≥ $7k, 1302679 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 125891
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7904 | 2390 | -1.88 | -60.32 | +229.50 | 7958.62 | 18344 | +1878.85 |
| dev | 2289 | 4798 | +1943.01 | -364.65 | +2075.69 | 76.57 | 17059 | +2521.39 |
| bot_hf | 3128 | 216750 | +796.29 | -388.77 | +5184.36 | 8817.29 | 407738 | +7876.05 |
| swing | 2095 | 20202 | -1083.15 | -1374.07 | -257.34 | 68.62 | 20053 | +15.00 |
| incidenteel | 165726 | 175148 | -3893.74 | -8275.48 | +31724.96 | 3000.89 | 320305 | +15331.75 |
| scalper | 25595 | 482660 | -13325.69 | -16493.88 | +22141.98 | 1180.49 | 519180 | +3054.33 |

Wallets met ≥ 10 posities: 16442, waarvan winstgevend: 20%. De top 1% winnaars pakt 42% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15565.16 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.63 | ja | 118 s | +140.38 / +984.50 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7473 (90) | 45% | +52.32 | +51.19 | +1% | 25.62 | ja | 26 s | +34.82 / +17.50 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3015 (61) | 59% | +6.01 | +5.75 | +5% | 23.93 | ja | 4 s | +4.55 / +1.47 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4120 (23) | 61% | +10.46 | +10.31 | +7% | 23.76 | ja | 4 s | +6.93 / +3.53 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7024 (57) | 39% | +9.15 | +8.23 | +1% | 22.18 | ja | 17 s | +2.75 / +6.40 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2945 (24) | 50% | +5.53 | +4.61 | +0% | 19.11 | ja | 10 s | +0.14 / +5.38 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.12 | ja | 110 s | +37.88 / +355.13 |
| 8 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 374 (76) | 55% | +0.40 | +0.38 | +32% | 17.98 | ja | 20 s | +0.04 / +0.36 |
| 9 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.19 | ja | 8 s | +60.38 / +783.11 |
| 10 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3483 (43) | 37% | +66.96 | +60.01 | +2% | 16.11 | ja | 28 s | +39.64 / +27.33 |
| 11 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2241 (8) | 49% | +16.16 | +14.74 | +1% | 15.97 | ja | 44 s | +0.30 / +15.86 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2535 (39) | 47% | +64.59 | +61.36 | +2% | 15.89 | ja | 22 s | +19.48 / +45.11 |
| 13 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.86 | ja | 110 s | +25.67 / +257.92 |
| 14 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 22 (2) | 91% | +229.88 | +201.19 | +128% | 13.88 | ja | 3 min | +153.66 / +76.23 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1709 (4) | 54% | +11.21 | +10.49 | +1% | 13.31 | ja | 43 s | +6.03 / +5.19 |
| 16 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 24 (2) | 83% | +25.50 | +17.67 | +159% | 13.12 | ja | 106 s | +5.50 / +20.00 |
| 17 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1481 (25) | 45% | +3.46 | +3.18 | +2% | 12.96 | ja | 59 s | +2.59 / +0.87 |
| 18 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 467 (0) | 64% | +13.64 | +13.13 | +12% | 12.94 | ja | 1 s | +7.28 / +6.36 |
| 19 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1610 (4) | 40% | +8.02 | +7.04 | +2% | 12.42 | ja | 26 s | +5.63 / +2.39 |
| 20 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 24 (2) | 75% | +23.16 | +16.70 | +144% | 12.08 | ja | 103 s | +5.51 / +17.66 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.63 | ja | 118 s | +140.38 / +984.50 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.19 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.12 | ja | 110 s | +37.88 / +355.13 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.86 | ja | 110 s | +25.67 / +257.92 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 22 (2) | 91% | +229.88 | +201.19 | +128% | 13.88 | ja | 3 min | +153.66 / +76.23 |
| 6 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.5 | ja | 2 min | +4.01 / +166.71 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 276 (7) | 62% | +159.85 | +125.89 | +15% | 7.77 | ja | 15 s | +90.18 / +69.67 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 42 (11) | 71% | +127.67 | +115.83 | +41% | 6.46 | ja | 6 s | +72.33 / +55.34 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 67 (0) | 61% | +91.85 | +73.09 | +34% | 6.39 | ja | 11 s | -4.97 / +96.82 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 22 (2) | 59% | +89.41 | +63.85 | +53% | 6.59 | ja | 3 min | +44.35 / +45.06 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +76.63 | +43.57 | +145% | 8.44 | nee | 7 s | +43.32 / +33.31 |
| 12 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 142 (1) | 75% | +69.45 | +64.97 | +20% | 8.38 | ja | 96 s | +19.96 / +49.49 |
| 13 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.06 | nee | 33 s | -1.33 / +70.50 |
| 14 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3483 (43) | 37% | +66.96 | +60.01 | +2% | 16.11 | ja | 28 s | +39.64 / +27.33 |
| 15 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2535 (39) | 47% | +64.59 | +61.36 | +2% | 15.89 | ja | 22 s | +19.48 / +45.11 |
| 16 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 161 (0) | 79% | +63.60 | +60.80 | +16% | 7.18 | ja | 9 s | +25.52 / +38.07 |
| 17 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 131 (6) | 68% | +60.21 | +55.64 | +22% | 8.13 | ja | 3 min | +15.55 / +44.66 |
| 18 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 5 (0) | 80% | +59.06 | +39.16 | +136% | 5.41 | nee | 7 s | +8.19 / +50.87 |
| 19 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 84 (1) | 75% | +56.99 | +49.28 | +17% | 5.89 | nee | 31 s | +24.07 / +32.91 |
| 20 | [9RG3…K6S2](https://solscan.io/account/9RG3YAuiQBDdG1esnzSXQ55o265to8nVriQhpwcbK6S2) | dev | 7 (3) | 57% | +56.58 | +32.52 | +87% | 3.66 | nee | 11 s | +17.63 / +38.95 |

## Geluk-toets

Populatie: 7716 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.36 | 4.44 | 5.38 |
| #10 | 13.95 | 3.43 | 3.61 |
| #20 | 9.48 | 3.15 | 3.27 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.38): **79**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 20446 | 47% | +4.8% | -0.6% | +243.36 |
| top 20 op winst (A) | 20/20 | 8245 | 45% | +2.9% | -0.9% | +611.19 |
| alle wallets | – | 505717 | 32% | -10.7% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.2% / +0.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3524): ρ = 0.512. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 234

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20446 | 29% | -12.3% | -7.7% | -501.28 |
| 2 s | 20446 | 24% | -15.0% | -9.2% | -615.13 |
| 10 s | 20446 | 22% | -16.3% | -9.2% | -665.26 |
| 60 s | 20446 | 20% | -18.9% | -7.8% | -774.16 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 410

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38747 | 29% | -11.6% | -7.7% | -897.29 |
| 2 s | 38747 | 24% | -14.7% | -9.3% | -1141.74 |
| 10 s | 38747 | 22% | -16.0% | -9.2% | -1242.73 |
| 60 s | 38747 | 20% | -18.9% | -8.0% | -1460.99 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 106

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7244 | 32% | -1.0% | -8.1% | -14.19 |
| 2 s | 7244 | 27% | -6.3% | -9.8% | -92.01 |
| 10 s | 7244 | 26% | -7.0% | -8.4% | -101.09 |
| 60 s | 7244 | 24% | -6.8% | -6.0% | -99.00 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
