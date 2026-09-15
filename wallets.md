# Wallet-analyse pump.fun — 2026-09-15 06:35 UTC

## Kort antwoord

- Geluk-toets: 71 van 7582 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=31.22, geluk-grens 5.53).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.3% per positie (alle wallets: -10.9%; 19 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.9%, 2 s: -15.4%, 10 s: -16.4%, 60 s: -19.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 06:24 UTC → 2026-09-15 06:24 UTC (72.0 uur), helft A/B-grens: 2026-09-13 18:24 UTC
- 7257573 trades, 75808 tokens, 209065 wallets, 2234943 posities (896682 geopend vanaf ≥ $7k, 1338261 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124472
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7307 | 3387 | +106.00 | +45.79 | +335.64 | 7573.95 | 20224 | +1844.61 |
| dev | 2200 | 4457 | +2077.11 | -105.17 | +2469.60 | 38.34 | 15988 | +2393.32 |
| bot_hf | 3216 | 220497 | +912.00 | -358.06 | +5293.34 | 8800.63 | 402955 | +6821.17 |
| swing | 1904 | 18138 | -977.28 | -1255.12 | -178.99 | 52.27 | 18905 | +10.18 |
| incidenteel | 169117 | 174794 | -3831.73 | -6812.70 | +35018.40 | 1887.75 | 339306 | +15804.09 |
| scalper | 25321 | 475409 | -12833.37 | -15875.23 | +24633.55 | 1229.41 | 540883 | +3308.37 |

Wallets met ≥ 10 posities: 16176, waarvan winstgevend: 22%. De top 1% winnaars pakt 44% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14547.27 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.43 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7388 (94) | 46% | +63.29 | +62.16 | +1% | 25.35 | ja | 25 s | +25.52 / +37.77 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3975 (18) | 60% | +9.13 | +8.94 | +7% | 22.96 | ja | 4 s | +5.30 / +3.82 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2817 (55) | 58% | +4.00 | +3.78 | +3% | 22.42 | ja | 4 s | +2.83 / +1.17 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7092 (67) | 40% | +13.54 | +12.55 | +1% | 22.16 | ja | 17 s | +2.90 / +10.64 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.67 | ja | 2 min | +112.67 / +421.81 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 440 (81) | 55% | +0.48 | +0.46 | +29% | 19.47 | ja | 22 s | +0.03 / +0.45 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.32 | ja | 8 s | +184.82 / +658.67 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2718 (44) | 48% | +82.67 | +79.44 | +3% | 16.72 | ja | 19 s | +27.86 / +54.81 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.11 | ja | 2 min | +94.54 / +274.04 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3622 (56) | 37% | +61.91 | +54.96 | +2% | 15.49 | ja | 28 s | +21.38 / +40.53 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2278 (11) | 50% | +13.20 | +11.79 | +1% | 15.17 | ja | 45 s | +5.10 / +8.11 |
| 13 | [7evu…tqbX](https://solscan.io/account/7evudm7mkommXaFbyrC9AoGNfkqcTdUGZAU25ZTytqbX) | bot_hf | 2411 (8) | 49% | +11.95 | +11.13 | +3% | 14.24 | ja | 30 s | +0.33 / +11.61 |
| 14 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1848 (89) | 44% | +5.24 | +1.33 | +0% | 12.72 | ja | 43 s | +2.50 / +2.74 |
| 15 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1726 (3) | 40% | +8.48 | +6.50 | +2% | 12.65 | ja | 22 s | +1.22 / +7.26 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1447 (27) | 45% | +2.53 | +2.25 | +2% | 12.26 | ja | 58 s | +1.61 / +0.92 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (1) | 86% | +23.34 | +15.51 | +154% | 12.06 | ja | 106 s | +6.87 / +16.47 |
| 18 | [CrAz…MCoj](https://solscan.io/account/CrAzYtsUvb4F1L8uwhGZXkMhRiMSW1P7qp4FA4QFMCoj) | scalper | 767 (167) | 48% | +0.55 | +0.53 | +19% | 11.73 | ja | 30 s | +0.00 / +0.55 |
| 19 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2051 (15) | 54% | +2.07 | +1.90 | +2% | 11.22 | ja | 10 s | +0.93 / +1.14 |
| 20 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 22 (1) | 77% | +20.72 | +14.25 | +136% | 10.97 | ja | 99 s | +5.96 / +14.76 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.43 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.32 | ja | 8 s | +184.82 / +658.67 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.67 | ja | 2 min | +112.67 / +421.81 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.11 | ja | 2 min | +94.54 / +274.04 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 53 (1) | 60% | +188.30 | +171.36 | +40% | 8.4 | ja | 3 min | +41.26 / +147.04 |
| 6 | [gVDX…dAkx](https://solscan.io/account/gVDXhoGbePACvSqN7CZBtQXFW9eyJwsgudPEwSydAkx) | dev | 9 (1) | 89% | +145.19 | +118.40 | +85% | 6.98 | nee | 9 s | +12.59 / +132.59 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 338 (10) | 56% | +144.57 | +110.62 | +11% | 7.61 | ja | 16 s | +91.71 / +52.86 |
| 8 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 10 (1) | 90% | +109.84 | +81.15 | +139% | 9.86 | nee | 4 min | +0.00 / +109.84 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 68 (0) | 66% | +100.79 | +82.03 | +37% | 7.9 | ja | 11 s | +22.56 / +78.23 |
| 10 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 31 (5) | 74% | +90.39 | +80.47 | +42% | 6.0 | ja | 34 s | +79.65 / +10.74 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 11 (0) | 100% | +88.31 | +55.26 | +124% | 8.65 | nee | 7 s | +44.68 / +43.63 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2718 (44) | 48% | +82.67 | +79.44 | +3% | 16.72 | ja | 19 s | +27.86 / +54.81 |
| 13 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 9 (3) | 56% | +77.34 | +57.44 | +104% | 4.27 | nee | 7 s | +0.00 / +77.34 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | bot_hf | 11 (0) | 100% | +77.17 | +66.36 | +69% | 5.37 | nee | 6 s | +14.17 / +62.99 |
| 15 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 147 (0) | 76% | +75.45 | +70.97 | +21% | 8.89 | ja | 94 s | +28.09 / +47.37 |
| 16 | [76bg…Rnzh](https://solscan.io/account/76bg6fHvkavukBNggSxTpJX9quDEWTsfmH42VFsRnzh) | bot_hf | 9 (1) | 89% | +73.25 | +56.73 | +129% | 9.13 | nee | 8 s | +8.25 / +65.00 |
| 17 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | bot_hf | 46 (2) | 85% | +72.47 | +63.88 | +27% | 4.95 | nee | 14 s | +15.53 / +56.93 |
| 18 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.09 | nee | 33 s | +49.33 / +19.84 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 10 (1) | 80% | +67.21 | +47.91 | +92% | 6.98 | nee | 4 min | +0.00 / +67.21 |
| 20 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 137 (6) | 70% | +66.69 | +62.12 | +23% | 8.64 | ja | 2 min | +26.15 / +40.53 |

## Geluk-toets

Populatie: 7582 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 31.22 | 4.47 | 5.53 |
| #10 | 14.09 | 3.42 | 3.69 |
| #20 | 9.06 | 3.14 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.53): **71**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 19869 | 49% | +6.3% | -0.1% | +2715.69 |
| top 20 op winst (A) | 20/20 | 7271 | 49% | +6.2% | +0.0% | +3067.87 |
| alle wallets | – | 547392 | 31% | -10.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +0.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3448): ρ = 0.52. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 225

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 19869 | 29% | -11.9% | -7.3% | -474.29 |
| 2 s | 19869 | 24% | -15.4% | -9.0% | -612.63 |
| 10 s | 19869 | 22% | -16.4% | -8.9% | -653.72 |
| 60 s | 19869 | 20% | -19.2% | -7.6% | -765.05 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 694

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40860 | 29% | -12.5% | -8.1% | -1018.58 |
| 2 s | 40860 | 24% | -15.6% | -9.8% | -1276.26 |
| 10 s | 40860 | 23% | -16.8% | -9.6% | -1374.30 |
| 60 s | 40860 | 20% | -19.6% | -8.1% | -1597.43 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 63

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 3860 | 36% | +3.2% | -5.8% | +24.54 |
| 2 s | 3860 | 31% | -5.6% | -8.3% | -43.22 |
| 10 s | 3860 | 29% | -5.4% | -6.7% | -41.79 |
| 60 s | 3860 | 24% | -6.1% | -5.7% | -47.18 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
