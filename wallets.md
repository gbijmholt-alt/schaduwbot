# Wallet-analyse pump.fun — 2026-09-14 21:39 UTC

## Kort antwoord

- Geluk-toets: 77 van 7599 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.35, geluk-grens 5.46).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.6% per positie (alle wallets: -10.8%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.0%, 2 s: -14.8%, 10 s: -15.9%, 60 s: -18.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 21:27 UTC → 2026-09-14 21:27 UTC (72.0 uur), helft A/B-grens: 2026-09-13 09:27 UTC
- 7239579 trades, 74481 tokens, 209406 wallets, 2210556 posities (902419 geopend vanaf ≥ $7k, 1308137 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 125767
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8036 | 2558 | +103.36 | +42.19 | +379.27 | 8030.34 | 18291 | +1819.41 |
| dev | 2271 | 4756 | +1921.51 | -379.30 | +2079.86 | 67.60 | 17052 | +2549.14 |
| bot_hf | 3154 | 217112 | +658.41 | -528.68 | +4948.09 | 8921.46 | 407633 | +7840.28 |
| swing | 2076 | 19891 | -1076.31 | -1358.53 | -291.01 | 78.94 | 19625 | -13.31 |
| incidenteel | 168242 | 176361 | -3837.07 | -8204.95 | +32052.98 | 3014.43 | 322857 | +15341.13 |
| scalper | 25627 | 481741 | -13116.52 | -16260.53 | +22519.84 | 1429.89 | 522679 | +2864.45 |

Wallets met ≥ 10 posities: 16463, waarvan winstgevend: 21%. De top 1% winnaars pakt 42% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15346.62 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.6 | ja | 118 s | +140.38 / +984.50 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7432 (88) | 45% | +48.45 | +47.32 | +1% | 25.29 | ja | 26 s | +32.04 / +16.41 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2990 (60) | 58% | +5.42 | +5.15 | +4% | 23.58 | ja | 4 s | +4.28 / +1.14 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4085 (23) | 61% | +10.21 | +10.06 | +7% | 23.54 | ja | 4 s | +7.02 / +3.19 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7013 (59) | 39% | +10.34 | +9.42 | +1% | 22.06 | ja | 17 s | +2.68 / +7.66 |
| 6 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 379 (78) | 55% | +0.42 | +0.40 | +33% | 18.22 | ja | 19 s | +0.04 / +0.38 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.1 | ja | 110 s | +37.88 / +355.13 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.17 | ja | 8 s | +60.38 / +783.11 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2553 (39) | 47% | +67.88 | +64.65 | +2% | 16.01 | ja | 22 s | +20.12 / +47.76 |
| 10 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3498 (48) | 38% | +67.88 | +60.92 | +2% | 15.89 | ja | 28 s | +38.37 / +29.51 |
| 11 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.84 | ja | 110 s | +25.67 / +257.92 |
| 12 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 21 (2) | 90% | +228.97 | +200.28 | +132% | 14.0 | ja | 2 min | +119.13 / +109.84 |
| 13 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1690 (4) | 54% | +10.59 | +9.87 | +1% | 13.28 | ja | 43 s | +5.63 / +4.96 |
| 14 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 24 (2) | 83% | +25.50 | +17.67 | +159% | 13.1 | ja | 106 s | +5.50 / +20.00 |
| 15 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1465 (24) | 44% | +3.25 | +2.97 | +2% | 12.75 | ja | 59 s | +2.46 / +0.79 |
| 16 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 453 (0) | 64% | +13.76 | +13.25 | +13% | 12.63 | ja | 1 s | +7.47 / +6.29 |
| 17 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 24 (2) | 75% | +23.16 | +16.70 | +144% | 12.06 | ja | 103 s | +5.51 / +17.66 |
| 18 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1597 (3) | 40% | +5.90 | +4.92 | +1% | 11.98 | ja | 26 s | +3.94 / +1.96 |
| 19 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2038 (13) | 55% | +2.46 | +2.29 | +2% | 11.95 | ja | 10 s | +1.47 / +0.99 |
| 20 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 22 (1) | 86% | +18.23 | +12.87 | +84% | 11.82 | ja | 74 s | +4.82 / +13.40 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.6 | ja | 118 s | +140.38 / +984.50 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.17 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.1 | ja | 110 s | +37.88 / +355.13 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.84 | ja | 110 s | +25.67 / +257.92 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 21 (2) | 90% | +228.97 | +200.28 | +132% | 14.0 | ja | 2 min | +119.13 / +109.84 |
| 6 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.49 | ja | 2 min | +4.01 / +166.71 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 267 (7) | 62% | +155.00 | +121.05 | +15% | 7.48 | ja | 15 s | +83.76 / +71.24 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 42 (7) | 76% | +128.76 | +116.92 | +41% | 6.9 | ja | 18 s | +72.33 / +56.42 |
| 9 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 21 (2) | 62% | +104.55 | +78.99 | +64% | 7.71 | ja | 2 min | +37.34 / +67.21 |
| 10 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 67 (0) | 61% | +91.85 | +73.09 | +34% | 6.37 | ja | 11 s | -4.97 / +96.82 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +76.63 | +43.57 | +145% | 8.43 | nee | 7 s | +43.32 / +33.31 |
| 12 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 144 (0) | 76% | +74.58 | +70.09 | +21% | 8.8 | ja | 94 s | +21.79 / +52.79 |
| 13 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.06 | nee | 33 s | +1.20 / +67.97 |
| 14 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3498 (48) | 38% | +67.88 | +60.92 | +2% | 15.89 | ja | 28 s | +38.37 / +29.51 |
| 15 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2553 (39) | 47% | +67.88 | +64.65 | +2% | 16.01 | ja | 22 s | +20.12 / +47.76 |
| 16 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 162 (0) | 79% | +64.81 | +62.02 | +16% | 7.19 | ja | 9 s | +25.12 / +39.69 |
| 17 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 134 (6) | 69% | +64.03 | +59.47 | +22% | 8.38 | ja | 2 min | +18.96 / +45.07 |
| 18 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 9 (0) | 100% | +62.27 | +51.47 | +68% | 4.73 | nee | 6 s | +11.24 / +51.03 |
| 19 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 5 (0) | 80% | +59.06 | +39.16 | +136% | 5.4 | nee | 7 s | +8.19 / +50.87 |
| 20 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 84 (1) | 75% | +56.99 | +49.28 | +17% | 5.87 | nee | 31 s | +24.07 / +32.91 |

## Geluk-toets

Populatie: 7599 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.35 | 4.52 | 5.46 |
| #10 | 13.91 | 3.44 | 3.66 |
| #20 | 9.47 | 3.14 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.46): **77**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 20770 | 47% | +4.6% | -0.6% | +261.38 |
| top 20 op winst (A) | 20/20 | 8538 | 46% | +3.2% | -0.8% | +705.43 |
| alle wallets | – | 519743 | 32% | -10.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +2.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3520): ρ = 0.517. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 248

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20770 | 29% | -12.0% | -7.6% | -497.69 |
| 2 s | 20770 | 24% | -14.8% | -9.1% | -612.88 |
| 10 s | 20770 | 22% | -15.9% | -9.1% | -661.03 |
| 60 s | 20770 | 20% | -18.4% | -7.6% | -765.50 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 402

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 35484 | 29% | -12.2% | -8.2% | -865.91 |
| 2 s | 35484 | 24% | -15.5% | -9.8% | -1100.81 |
| 10 s | 35484 | 22% | -17.0% | -9.8% | -1205.15 |
| 60 s | 35484 | 19% | -20.1% | -8.3% | -1425.61 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 103

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7274 | 32% | -0.8% | -8.0% | -11.99 |
| 2 s | 7274 | 27% | -6.3% | -9.8% | -91.44 |
| 10 s | 7274 | 26% | -6.8% | -8.3% | -99.52 |
| 60 s | 7274 | 24% | -6.7% | -6.0% | -97.85 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
