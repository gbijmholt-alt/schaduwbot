# Wallet-analyse pump.fun — 2026-09-15 00:37 UTC

## Kort antwoord

- Geluk-toets: 62 van 7431 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.44, geluk-grens 5.59).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -11.1%; 16 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.8%, 2 s: -15.6%, 10 s: -16.7%, 60 s: -19.5% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 00:25 UTC → 2026-09-15 00:25 UTC (72.0 uur), helft A/B-grens: 2026-09-13 12:25 UTC
- 7196469 trades, 74915 tokens, 211069 wallets, 2203746 posities (885811 geopend vanaf ≥ $7k, 1317935 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124523
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7750 | 2550 | +71.58 | +7.56 | +339.21 | 7886.06 | 16881 | +1998.93 |
| dev | 2217 | 4578 | +1812.21 | -446.89 | +2080.30 | 57.54 | 17149 | +2601.14 |
| bot_hf | 3178 | 216023 | +754.75 | -504.75 | +5063.21 | 9128.44 | 407611 | +7234.15 |
| swing | 1965 | 18751 | -992.10 | -1265.39 | -191.14 | 85.64 | 19281 | +25.12 |
| incidenteel | 170929 | 176718 | -3772.97 | -7775.22 | +33264.40 | 2751.66 | 332209 | +15626.30 |
| scalper | 25030 | 467191 | -12580.79 | -15531.56 | +23424.91 | 1235.26 | 524804 | +2800.51 |

Wallets met ≥ 10 posities: 16019, waarvan winstgevend: 22%. De top 1% winnaars pakt 42% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14707.31 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.69 | ja | 118 s | +181.66 / +943.22 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7128 (91) | 46% | +53.30 | +52.17 | +1% | 25.04 | ja | 25 s | +32.05 / +21.24 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2965 (59) | 59% | +5.71 | +5.44 | +4% | 24.34 | ja | 4 s | +3.83 / +1.88 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4037 (22) | 61% | +9.49 | +9.34 | +7% | 23.15 | ja | 4 s | +5.86 / +3.63 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6793 (63) | 39% | +12.10 | +11.11 | +1% | 21.84 | ja | 17 s | +3.27 / +8.84 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.16 | ja | 110 s | +52.93 / +340.07 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 405 (78) | 54% | +0.40 | +0.38 | +26% | 17.88 | ja | 23 s | +0.03 / +0.37 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.23 | ja | 8 s | +60.38 / +783.11 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2591 (42) | 48% | +82.42 | +79.20 | +3% | 16.63 | ja | 20 s | +24.00 / +58.42 |
| 10 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3427 (50) | 38% | +68.38 | +61.42 | +2% | 15.71 | ja | 28 s | +40.18 / +28.20 |
| 11 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2166 (7) | 50% | +16.39 | +14.97 | +1% | 15.5 | ja | 44 s | +3.07 / +13.31 |
| 12 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.89 | ja | 110 s | +39.88 / +243.71 |
| 13 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1424 (24) | 45% | +3.42 | +3.14 | +2% | 12.8 | ja | 58 s | +2.91 / +0.51 |
| 14 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1547 (2) | 40% | +6.71 | +5.75 | +1% | 12.43 | ja | 24 s | +2.77 / +3.93 |
| 15 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1626 (87) | 44% | +10.96 | +7.05 | +1% | 12.29 | ja | 49 s | +7.84 / +3.12 |
| 16 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1540 (2) | 54% | +7.65 | +6.92 | +1% | 12.28 | ja | 44 s | +3.48 / +4.17 |
| 17 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2023 (13) | 54% | +2.33 | +2.15 | +2% | 11.86 | ja | 10 s | +1.23 / +1.10 |
| 18 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 23 (2) | 83% | +23.34 | +15.51 | +151% | 11.75 | ja | 106 s | +3.35 / +20.00 |
| 19 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 421 (0) | 63% | +11.56 | +11.06 | +12% | 11.55 | ja | 1 s | +5.00 / +6.57 |
| 20 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 23 (2) | 74% | +20.72 | +14.25 | +133% | 10.69 | ja | 99 s | +3.06 / +17.66 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.69 | ja | 118 s | +181.66 / +943.22 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.23 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.16 | ja | 110 s | +52.93 / +340.07 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.89 | ja | 110 s | +39.88 / +243.71 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.52 | ja | 2 min | +10.53 / +160.20 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 306 (9) | 58% | +141.60 | +107.65 | +12% | 7.55 | ja | 15 s | +71.29 / +70.32 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 11 (2) | 82% | +107.71 | +79.02 | +125% | 9.14 | nee | 4 min | -2.13 / +109.84 |
| 8 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 66 (0) | 65% | +95.18 | +76.42 | +36% | 6.82 | ja | 11 s | -1.69 / +96.87 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 33 (6) | 73% | +92.42 | +82.50 | +41% | 5.99 | nee | 18 s | +36.00 / +56.42 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2591 (42) | 48% | +82.42 | +79.20 | +3% | 16.63 | ja | 20 s | +24.00 / +58.42 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +76.63 | +43.57 | +145% | 8.46 | nee | 7 s | +43.32 / +33.31 |
| 12 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 147 (0) | 76% | +75.45 | +70.97 | +21% | 8.85 | ja | 94 s | +22.32 / +53.13 |
| 13 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 7 (1) | 71% | +69.78 | +49.88 | +125% | 4.83 | nee | 7 s | +8.19 / +61.59 |
| 14 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.07 | nee | 33 s | +1.20 / +67.97 |
| 15 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3427 (50) | 38% | +68.38 | +61.42 | +2% | 15.71 | ja | 28 s | +40.18 / +28.20 |
| 16 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 137 (6) | 70% | +66.69 | +62.12 | +23% | 8.6 | ja | 2 min | +25.33 / +41.36 |
| 17 | [AoGe…cMFe](https://solscan.io/account/AoGefnxF5CbZvbd2cvxv4Ex1E5j86dqEjehazRuMcMFe) | scalper | 32 (12) | 31% | +66.07 | +46.02 | +39% | 2.12 | nee | 62 s | -0.21 / +66.27 |
| 18 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 11 (2) | 73% | +64.18 | +44.89 | +81% | 6.27 | nee | 4 min | -3.02 / +67.21 |
| 19 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | scalper | 34 (2) | 85% | +63.67 | +55.08 | +28% | 4.45 | nee | 18 s | +16.46 / +47.20 |
| 20 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 9 (0) | 100% | +62.51 | +51.70 | +69% | 4.89 | nee | 6 s | +3.37 / +59.14 |

## Geluk-toets

Populatie: 7431 wallets met ≥ 20 posities, 80 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.44 | 4.59 | 5.59 |
| #10 | 13.75 | 3.44 | 3.72 |
| #20 | 8.97 | 3.14 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.59): **62**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 23075 | 47% | +5.0% | -0.6% | +1105.00 |
| top 20 op winst (A) | 19/20 | 9036 | 46% | +4.4% | -0.7% | +2045.46 |
| alle wallets | – | 552435 | 31% | -11.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.7% / +1.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3270): ρ = 0.511. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 280

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 23075 | 29% | -12.8% | -7.9% | -588.23 |
| 2 s | 23075 | 24% | -15.6% | -9.4% | -720.93 |
| 10 s | 23075 | 22% | -16.7% | -9.3% | -771.20 |
| 60 s | 23075 | 20% | -19.5% | -8.0% | -899.45 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 500

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38339 | 29% | -11.7% | -8.0% | -897.70 |
| 2 s | 38339 | 24% | -14.8% | -9.5% | -1131.84 |
| 10 s | 38339 | 23% | -16.1% | -9.4% | -1232.25 |
| 60 s | 38339 | 20% | -19.0% | -8.1% | -1456.73 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 124

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7078 | 32% | -1.0% | -8.0% | -13.98 |
| 2 s | 7078 | 27% | -6.2% | -9.8% | -87.81 |
| 10 s | 7078 | 26% | -6.6% | -8.2% | -92.99 |
| 60 s | 7078 | 24% | -6.7% | -6.0% | -95.30 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
