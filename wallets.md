# Wallet-analyse pump.fun — 2026-09-14 22:30 UTC

## Kort antwoord

- Geluk-toets: 80 van 7467 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.34, geluk-grens 5.31).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.9% per positie (alle wallets: -11.2%; 17 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.5%, 2 s: -15.4%, 10 s: -16.6%, 60 s: -19.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 22:18 UTC → 2026-09-14 22:18 UTC (72.0 uur), helft A/B-grens: 2026-09-13 10:18 UTC
- 7198322 trades, 74683 tokens, 209874 wallets, 2197702 posities (891065 geopend vanaf ≥ $7k, 1306637 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 123830
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8076 | 2555 | +138.63 | +76.99 | +406.20 | 8052.41 | 14915 | +1903.62 |
| dev | 2260 | 4661 | +1892.83 | -400.71 | +2084.04 | 63.02 | 16798 | +2540.10 |
| bot_hf | 3133 | 215727 | +637.19 | -527.41 | +5113.82 | 8958.24 | 407433 | +7655.58 |
| swing | 2025 | 19278 | -1007.43 | -1292.20 | -240.59 | 84.75 | 19243 | +3.35 |
| incidenteel | 169205 | 177420 | -3809.40 | -8230.60 | +32472.74 | 3144.32 | 325628 | +15463.93 |
| scalper | 25175 | 471424 | -12898.01 | -15965.52 | +22057.22 | 1362.35 | 522620 | +2787.50 |

Wallets met ≥ 10 posities: 16060, waarvan winstgevend: 21%. De top 1% winnaars pakt 42% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15046.19 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.6 | ja | 118 s | +182.45 / +942.43 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7300 (86) | 45% | +52.23 | +51.10 | +1% | 25.36 | ja | 26 s | +33.56 / +18.67 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2956 (60) | 59% | +5.43 | +5.17 | +4% | 23.65 | ja | 4 s | +4.22 / +1.22 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4039 (23) | 61% | +10.03 | +9.88 | +7% | 23.24 | ja | 4 s | +6.74 / +3.30 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6883 (57) | 39% | +10.43 | +9.51 | +1% | 22.06 | ja | 17 s | +4.14 / +6.29 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2946 (23) | 50% | +7.21 | +6.29 | +1% | 19.33 | ja | 10 s | +0.10 / +7.11 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 387 (81) | 55% | +0.43 | +0.41 | +33% | 18.47 | ja | 18 s | +0.03 / +0.40 |
| 8 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.1 | ja | 110 s | +53.41 / +339.60 |
| 9 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.18 | ja | 8 s | +60.38 / +783.11 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2520 (37) | 47% | +70.83 | +67.61 | +2% | 16.27 | ja | 22 s | +23.87 / +46.97 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3458 (47) | 38% | +70.90 | +63.94 | +2% | 16.03 | ja | 28 s | +42.98 / +27.92 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2206 (6) | 49% | +15.70 | +14.28 | +1% | 15.86 | ja | 44 s | +1.10 / +14.59 |
| 13 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.84 | ja | 110 s | +39.70 / +243.88 |
| 14 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1622 (1) | 54% | +10.52 | +9.79 | +1% | 13.03 | ja | 44 s | +4.77 / +5.74 |
| 15 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1454 (24) | 45% | +3.40 | +3.13 | +2% | 12.86 | ja | 59 s | +2.78 / +0.62 |
| 16 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 25 (3) | 80% | +25.50 | +17.67 | +153% | 12.83 | ja | 106 s | +5.50 / +20.00 |
| 17 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1581 (3) | 40% | +8.00 | +7.02 | +2% | 12.48 | ja | 26 s | +4.79 / +3.20 |
| 18 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1588 (84) | 43% | +7.84 | +3.93 | +0% | 12.27 | ja | 53 s | +4.60 / +3.25 |
| 19 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 439 (0) | 63% | +12.96 | +12.45 | +12% | 12.25 | ja | 1 s | +6.27 / +6.69 |
| 20 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2015 (13) | 55% | +2.37 | +2.19 | +2% | 12.01 | ja | 10 s | +1.31 / +1.05 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.6 | ja | 118 s | +182.45 / +942.43 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.18 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.1 | ja | 110 s | +53.41 / +339.60 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.84 | ja | 110 s | +39.70 / +243.88 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 19 (2) | 90% | +200.54 | +171.85 | +126% | 12.68 | nee | 2 min | +90.70 / +109.84 |
| 6 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.49 | ja | 2 min | +10.36 / +160.36 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 260 (8) | 62% | +146.14 | +112.19 | +14% | 7.32 | ja | 15 s | +75.56 / +70.58 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 40 (7) | 75% | +120.90 | +109.06 | +41% | 6.77 | ja | 21 s | +64.48 / +56.42 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 69 (0) | 62% | +92.82 | +74.06 | +34% | 6.45 | ja | 11 s | -5.63 / +98.45 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 19 (2) | 63% | +86.41 | +60.85 | +58% | 6.67 | nee | 2 min | +19.20 / +67.21 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +76.63 | +43.57 | +145% | 8.43 | nee | 7 s | +43.32 / +33.31 |
| 12 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 145 (0) | 76% | +74.82 | +70.33 | +21% | 8.81 | ja | 94 s | +21.79 / +53.03 |
| 13 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3458 (47) | 38% | +70.90 | +63.94 | +2% | 16.03 | ja | 28 s | +42.98 / +27.92 |
| 14 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2520 (37) | 47% | +70.83 | +67.61 | +2% | 16.27 | ja | 22 s | +23.87 / +46.97 |
| 15 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.06 | nee | 33 s | +1.20 / +67.97 |
| 16 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 135 (6) | 70% | +64.40 | +59.83 | +22% | 8.4 | ja | 2 min | +23.59 / +40.81 |
| 17 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 161 (1) | 78% | +63.10 | +60.30 | +15% | 7.1 | ja | 10 s | +22.98 / +40.12 |
| 18 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 5 (0) | 80% | +59.06 | +39.16 | +136% | 5.4 | nee | 7 s | +8.19 / +50.87 |
| 19 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 85 (1) | 74% | +56.87 | +49.16 | +17% | 5.77 | nee | 32 s | +24.00 / +32.87 |
| 20 | [9RG3…K6S2](https://solscan.io/account/9RG3YAuiQBDdG1esnzSXQ55o265to8nVriQhpwcbK6S2) | dev | 7 (3) | 57% | +56.58 | +32.52 | +87% | 3.66 | nee | 11 s | +17.63 / +38.95 |

## Geluk-toets

Populatie: 7467 wallets met ≥ 20 posities, 80 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.34 | 4.45 | 5.31 |
| #10 | 14.0 | 3.44 | 3.66 |
| #20 | 9.27 | 3.13 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.31): **80**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 22205 | 47% | +4.9% | -0.6% | +1095.19 |
| top 20 op winst (A) | 20/20 | 8603 | 46% | +4.5% | -0.8% | +2030.95 |
| alle wallets | – | 526623 | 31% | -11.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.8% / +2.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3455): ρ = 0.519. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 255

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 22205 | 29% | -12.5% | -7.9% | -555.49 |
| 2 s | 22205 | 24% | -15.4% | -9.4% | -685.46 |
| 10 s | 22205 | 22% | -16.6% | -9.4% | -736.09 |
| 60 s | 22205 | 20% | -19.4% | -8.0% | -862.67 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 497

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41619 | 30% | -11.0% | -7.4% | -917.44 |
| 2 s | 41619 | 25% | -14.0% | -9.0% | -1161.38 |
| 10 s | 41619 | 23% | -15.2% | -8.8% | -1268.05 |
| 60 s | 41619 | 20% | -17.9% | -7.6% | -1487.78 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 104

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7190 | 32% | -0.7% | -8.0% | -10.58 |
| 2 s | 7190 | 27% | -6.2% | -9.8% | -89.40 |
| 10 s | 7190 | 26% | -6.7% | -8.2% | -96.68 |
| 60 s | 7190 | 24% | -6.7% | -6.0% | -96.69 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
