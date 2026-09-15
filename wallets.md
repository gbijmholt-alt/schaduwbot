# Wallet-analyse pump.fun — 2026-09-15 04:45 UTC

## Kort antwoord

- Geluk-toets: 68 van 7551 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=30.25, geluk-grens 5.59).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.9% per positie (alle wallets: -11.0%; 20 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.5%, 2 s: -15.0%, 10 s: -15.9%, 60 s: -18.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 04:33 UTC → 2026-09-15 04:33 UTC (72.0 uur), helft A/B-grens: 2026-09-13 16:33 UTC
- 7257996 trades, 75753 tokens, 208926 wallets, 2232286 posities (894047 geopend vanaf ≥ $7k, 1338239 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124565
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7390 | 3423 | +89.98 | +29.39 | +331.21 | 7651.53 | 18883 | +1944.79 |
| dev | 2207 | 4458 | +1943.61 | -274.43 | +2290.85 | 43.56 | 15828 | +2480.67 |
| bot_hf | 3233 | 218515 | +880.54 | -360.96 | +5284.31 | 8771.52 | 405656 | +6733.60 |
| swing | 1879 | 17848 | -919.86 | -1180.82 | -124.96 | 56.72 | 18681 | +19.06 |
| incidenteel | 168902 | 174834 | -3868.74 | -6804.70 | +34407.89 | 1874.95 | 339006 | +15665.82 |
| scalper | 25315 | 474969 | -12622.97 | -15627.39 | +24672.82 | 1254.70 | 540185 | +3174.72 |

Wallets met ≥ 10 posities: 16178, waarvan winstgevend: 22%. De top 1% winnaars pakt 43% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14497.44 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 50 (1) | 88% | +1461.16 | +1384.99 | +257% | 30.48 | ja | 2 min | +366.88 / +1094.28 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7340 (97) | 46% | +59.98 | +58.85 | +1% | 25.03 | ja | 25 s | +27.40 / +32.58 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3982 (18) | 60% | +8.85 | +8.67 | +7% | 23.14 | ja | 4 s | +5.19 / +3.66 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2842 (57) | 58% | +4.03 | +3.81 | +3% | 22.7 | ja | 4 s | +2.57 / +1.46 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7008 (68) | 40% | +13.23 | +12.24 | +1% | 21.94 | ja | 17 s | +3.64 / +9.59 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 51 (1) | 71% | +502.76 | +470.53 | +125% | 20.03 | ja | 2 min | +112.67 / +390.09 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 428 (76) | 55% | +0.46 | +0.44 | +29% | 19.06 | ja | 23 s | +0.03 / +0.43 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.3 | ja | 8 s | +60.38 / +783.11 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2708 (44) | 48% | +80.54 | +77.31 | +3% | 16.63 | ja | 19 s | +28.70 / +51.84 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 50 (0) | 74% | +356.73 | +336.22 | +97% | 16.11 | ja | 2 min | +94.54 / +262.19 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3562 (59) | 38% | +71.17 | +64.22 | +2% | 15.69 | ja | 27 s | +27.59 / +43.58 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2230 (12) | 49% | +11.70 | +10.28 | +1% | 14.93 | ja | 44 s | +3.20 / +8.50 |
| 13 | [7evu…tqbX](https://solscan.io/account/7evudm7mkommXaFbyrC9AoGNfkqcTdUGZAU25ZTytqbX) | bot_hf | 2292 (7) | 50% | +11.92 | +11.11 | +4% | 14.17 | ja | 30 s | +0.23 / +11.69 |
| 14 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1780 (89) | 44% | +4.79 | +0.88 | +0% | 12.45 | ja | 44 s | +4.00 / +0.78 |
| 15 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1714 (4) | 40% | +7.45 | +5.47 | +1% | 12.41 | ja | 21 s | +0.70 / +6.75 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1440 (28) | 45% | +2.66 | +2.38 | +2% | 12.31 | ja | 57 s | +1.75 / +0.91 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (1) | 86% | +23.34 | +15.51 | +154% | 12.05 | ja | 106 s | +6.87 / +16.47 |
| 18 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2051 (15) | 54% | +2.17 | +2.00 | +2% | 11.21 | ja | 10 s | +1.17 / +1.01 |
| 19 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 22 (1) | 77% | +20.72 | +14.25 | +136% | 10.96 | ja | 99 s | +5.96 / +14.76 |
| 20 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 419 (0) | 61% | +10.03 | +9.52 | +10% | 10.8 | ja | 1 s | +3.57 / +6.45 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 50 (1) | 88% | +1461.16 | +1384.99 | +257% | 30.48 | ja | 2 min | +366.88 / +1094.28 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.3 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 51 (1) | 71% | +502.76 | +470.53 | +125% | 20.03 | ja | 2 min | +112.67 / +390.09 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 50 (0) | 74% | +356.73 | +336.22 | +97% | 16.11 | ja | 2 min | +94.54 / +262.19 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 50 (1) | 60% | +182.54 | +165.61 | +42% | 8.19 | ja | 2 min | +41.26 / +141.28 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 318 (10) | 59% | +146.71 | +112.75 | +12% | 7.59 | ja | 15 s | +93.17 / +53.53 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 10 (1) | 90% | +109.84 | +81.15 | +139% | 9.85 | nee | 4 min | +0.00 / +109.84 |
| 8 | [gVDX…dAkx](https://solscan.io/account/gVDXhoGbePACvSqN7CZBtQXFW9eyJwsgudPEwSydAkx) | dev | 6 (1) | 83% | +100.12 | +73.33 | +86% | 5.85 | nee | 9 s | +12.59 / +87.53 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 66 (0) | 67% | +97.99 | +79.23 | +37% | 7.12 | ja | 11 s | +25.57 / +72.42 |
| 10 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 32 (6) | 72% | +90.39 | +80.47 | +41% | 5.94 | nee | 34 s | +33.97 / +56.42 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 11 (0) | 100% | +88.31 | +55.26 | +124% | 8.61 | nee | 7 s | +44.68 / +43.63 |
| 12 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 9 (2) | 67% | +85.53 | +65.63 | +122% | 4.79 | nee | 7 s | +8.19 / +77.34 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2708 (44) | 48% | +80.54 | +77.31 | +3% | 16.63 | ja | 19 s | +28.70 / +51.84 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | bot_hf | 11 (0) | 100% | +77.17 | +66.36 | +69% | 5.38 | nee | 6 s | +3.37 / +73.80 |
| 15 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 147 (0) | 76% | +75.45 | +70.97 | +21% | 8.88 | ja | 94 s | +28.09 / +47.37 |
| 16 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | bot_hf | 45 (2) | 87% | +72.61 | +64.03 | +27% | 4.99 | nee | 14 s | +16.46 / +56.15 |
| 17 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3562 (59) | 38% | +71.17 | +64.22 | +2% | 15.69 | ja | 27 s | +27.59 / +43.58 |
| 18 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.09 | nee | 33 s | +41.55 / +27.61 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 10 (1) | 80% | +67.21 | +47.91 | +92% | 6.97 | nee | 4 min | +0.00 / +67.21 |
| 20 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 137 (6) | 70% | +66.69 | +62.12 | +23% | 8.63 | ja | 2 min | +26.15 / +40.53 |

## Geluk-toets

Populatie: 7551 wallets met ≥ 20 posities, 79 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 30.25 | 4.48 | 5.59 |
| #10 | 13.9 | 3.46 | 3.62 |
| #20 | 9.03 | 3.16 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.59): **68**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 21056 | 47% | +5.9% | -0.6% | +1982.59 |
| top 20 op winst (A) | 20/20 | 9478 | 47% | +4.9% | -0.6% | +2455.56 |
| alle wallets | – | 559861 | 31% | -11.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.8% / +1.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3309): ρ = 0.498. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 271

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 21056 | 28% | -11.5% | -7.7% | -485.23 |
| 2 s | 21056 | 24% | -15.0% | -9.4% | -630.40 |
| 10 s | 21056 | 22% | -15.9% | -9.0% | -670.83 |
| 60 s | 21056 | 20% | -18.6% | -7.6% | -782.88 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 534

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40067 | 30% | -11.0% | -7.8% | -884.38 |
| 2 s | 40067 | 25% | -14.3% | -9.4% | -1145.86 |
| 10 s | 40067 | 23% | -15.5% | -9.2% | -1243.64 |
| 60 s | 40067 | 20% | -18.3% | -7.8% | -1465.57 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 123

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7366 | 32% | -0.7% | -7.9% | -10.22 |
| 2 s | 7366 | 27% | -6.4% | -9.8% | -94.62 |
| 10 s | 7366 | 27% | -6.5% | -7.9% | -95.93 |
| 60 s | 7366 | 23% | -6.9% | -5.9% | -101.16 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
