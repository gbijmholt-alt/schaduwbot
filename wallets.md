# Wallet-analyse pump.fun — 2026-09-15 02:43 UTC

## Kort antwoord

- Geluk-toets: 72 van 7484 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=30.98, geluk-grens 5.4).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.4% per positie (alle wallets: -11.2%; 16 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.8%, 2 s: -15.0%, 10 s: -16.0%, 60 s: -18.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 02:31 UTC → 2026-09-15 02:31 UTC (72.0 uur), helft A/B-grens: 2026-09-13 14:31 UTC
- 7226958 trades, 75447 tokens, 209899 wallets, 2223624 posities (888948 geopend vanaf ≥ $7k, 1334676 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124823
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7383 | 3369 | +66.72 | +6.64 | +302.70 | 7803.07 | 19376 | +1969.97 |
| dev | 2216 | 4474 | +1925.15 | -316.14 | +2182.76 | 45.37 | 16488 | +2394.38 |
| bot_hf | 3213 | 216967 | +747.38 | -489.89 | +5078.05 | 8807.40 | 406425 | +6772.11 |
| swing | 1900 | 17968 | -938.09 | -1204.77 | -173.47 | 69.37 | 18943 | +29.14 |
| incidenteel | 170067 | 176282 | -3836.48 | -7415.19 | +34070.01 | 2301.91 | 337783 | +15841.88 |
| scalper | 25120 | 469888 | -12578.78 | -15570.91 | +23695.32 | 1202.13 | 535661 | +2924.61 |

Wallets met ≥ 10 posities: 16027, waarvan winstgevend: 22%. De top 1% winnaars pakt 43% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14614.10 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 50 (1) | 90% | +1404.78 | +1328.61 | +260% | 31.22 | ja | 111 s | +453.29 / +951.50 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7250 (99) | 46% | +57.45 | +56.32 | +1% | 25.17 | ja | 25 s | +31.02 / +26.43 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2861 (59) | 58% | +4.51 | +4.27 | +4% | 23.29 | ja | 4 s | +3.11 / +1.40 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3953 (21) | 60% | +9.04 | +8.89 | +7% | 22.88 | ja | 4 s | +5.55 / +3.49 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6851 (69) | 39% | +11.90 | +10.91 | +1% | 22.02 | ja | 17 s | +2.42 / +9.48 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 51 (1) | 69% | +481.50 | +449.28 | +125% | 19.69 | ja | 117 s | +128.32 / +353.18 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 413 (74) | 54% | +0.41 | +0.39 | +27% | 18.09 | ja | 24 s | +0.03 / +0.38 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.26 | ja | 8 s | +60.38 / +783.11 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2635 (41) | 48% | +80.33 | +77.10 | +3% | 16.6 | ja | 19 s | +31.39 / +48.95 |
| 10 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3450 (52) | 37% | +67.14 | +60.19 | +2% | 15.75 | ja | 28 s | +32.74 / +34.41 |
| 11 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 50 (0) | 68% | +331.67 | +311.16 | +93% | 15.61 | ja | 117 s | +103.45 / +228.22 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2188 (11) | 49% | +9.99 | +8.57 | +1% | 14.86 | ja | 44 s | +3.85 / +6.14 |
| 13 | [7evu…tqbX](https://solscan.io/account/7evudm7mkommXaFbyrC9AoGNfkqcTdUGZAU25ZTytqbX) | bot_hf | 2150 (7) | 50% | +10.17 | +9.68 | +4% | 13.94 | ja | 30 s | +0.04 / +10.14 |
| 14 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1636 (4) | 40% | +9.20 | +7.22 | +2% | 12.87 | ja | 22 s | +2.30 / +6.91 |
| 15 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1426 (24) | 45% | +3.15 | +2.87 | +2% | 12.65 | ja | 57 s | +2.52 / +0.63 |
| 16 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (1) | 86% | +23.34 | +15.51 | +154% | 12.03 | ja | 106 s | +3.35 / +20.00 |
| 17 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1536 (4) | 52% | +4.73 | +4.00 | +1% | 11.76 | ja | 44 s | +4.09 / +0.64 |
| 18 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2045 (13) | 55% | +2.36 | +2.19 | +2% | 11.76 | ja | 10 s | +1.48 / +0.88 |
| 19 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 409 (0) | 62% | +10.47 | +9.96 | +11% | 11.01 | ja | 1 s | +3.75 / +6.72 |
| 20 | [HzMn…qaWF](https://solscan.io/account/HzMnBYTVPr2FKQEsSrSjhnzheCpQE9Z3a5bWPiHsqaWF) | scalper | 22 (1) | 77% | +20.72 | +14.25 | +136% | 10.94 | ja | 99 s | +3.06 / +17.66 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 50 (1) | 90% | +1404.78 | +1328.61 | +260% | 31.22 | ja | 111 s | +453.29 / +951.50 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 76 (0) | 92% | +843.49 | +803.59 | +67% | 17.26 | ja | 8 s | +60.38 / +783.11 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 51 (1) | 69% | +481.50 | +449.28 | +125% | 19.69 | ja | 117 s | +128.32 / +353.18 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 50 (0) | 68% | +331.67 | +311.16 | +93% | 15.61 | ja | 117 s | +103.45 / +228.22 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 50 (1) | 58% | +174.86 | +157.92 | +42% | 8.19 | ja | 2 min | +36.09 / +138.77 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 311 (9) | 58% | +146.11 | +112.15 | +12% | 7.57 | ja | 15 s | +69.90 / +76.21 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 10 (1) | 90% | +109.84 | +81.15 | +139% | 9.83 | nee | 4 min | +0.00 / +109.84 |
| 8 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 67 (0) | 66% | +97.50 | +78.74 | +37% | 6.94 | ja | 11 s | +18.18 / +79.32 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 33 (6) | 73% | +92.42 | +82.50 | +41% | 6.0 | ja | 18 s | +36.00 / +56.42 |
| 10 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 9 (2) | 67% | +85.53 | +65.63 | +122% | 4.78 | nee | 7 s | +8.19 / +77.34 |
| 11 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2635 (41) | 48% | +80.33 | +77.10 | +3% | 16.6 | ja | 19 s | +31.39 / +48.95 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +76.63 | +43.57 | +145% | 8.47 | nee | 7 s | +43.32 / +33.31 |
| 13 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 147 (0) | 76% | +75.45 | +70.97 | +21% | 8.87 | ja | 94 s | +28.09 / +47.37 |
| 14 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 10 (0) | 100% | +69.52 | +58.72 | +69% | 5.14 | nee | 6 s | +3.37 / +66.15 |
| 15 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.08 | nee | 33 s | +16.14 / +53.02 |
| 16 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 10 (1) | 80% | +67.21 | +47.91 | +92% | 6.96 | nee | 4 min | +0.00 / +67.21 |
| 17 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3450 (52) | 37% | +67.14 | +60.19 | +2% | 15.75 | ja | 28 s | +32.74 / +34.41 |
| 18 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 137 (6) | 70% | +66.69 | +62.12 | +23% | 8.61 | ja | 2 min | +26.15 / +40.53 |
| 19 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | scalper | 37 (2) | 86% | +66.39 | +57.81 | +28% | 4.69 | nee | 17 s | +16.46 / +49.93 |
| 20 | [76bg…Rnzh](https://solscan.io/account/76bg6fHvkavukBNggSxTpJX9quDEWTsfmH42VFsRnzh) | bot_hf | 8 (1) | 88% | +64.29 | +47.77 | +130% | 8.62 | nee | 8 s | +2.04 / +62.26 |

## Geluk-toets

Populatie: 7484 wallets met ≥ 20 posities, 80 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 30.98 | 4.5 | 5.4 |
| #10 | 13.94 | 3.45 | 3.66 |
| #20 | 9.01 | 3.15 | 3.34 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.4): **72**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 20941 | 47% | +5.4% | -0.6% | +1686.47 |
| top 20 op winst (A) | 20/20 | 9191 | 46% | +4.7% | -0.6% | +2258.46 |
| alle wallets | – | 557206 | 31% | -11.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.0% / +2.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3314): ρ = 0.519. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 258

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20941 | 29% | -11.8% | -7.7% | -492.89 |
| 2 s | 20941 | 24% | -15.0% | -9.2% | -627.74 |
| 10 s | 20941 | 22% | -16.0% | -8.9% | -670.02 |
| 60 s | 20941 | 20% | -18.6% | -7.5% | -779.15 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 437

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39074 | 30% | -11.1% | -7.7% | -864.58 |
| 2 s | 39074 | 25% | -14.3% | -9.3% | -1120.94 |
| 10 s | 39074 | 23% | -15.7% | -9.2% | -1227.67 |
| 60 s | 39074 | 20% | -18.5% | -7.8% | -1444.80 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 112

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7167 | 32% | -0.6% | -8.0% | -9.02 |
| 2 s | 7167 | 27% | -6.3% | -9.8% | -90.55 |
| 10 s | 7167 | 26% | -6.6% | -8.0% | -94.62 |
| 60 s | 7167 | 24% | -6.9% | -5.9% | -98.56 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
