# Wallet-analyse pump.fun — 2026-09-14 12:31 UTC

## Kort antwoord

- Geluk-toets: 75 van 7565 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=26.08, geluk-grens 5.68).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -8.0%; 18 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.7%, 2 s: -15.6%, 10 s: -17.1%, 60 s: -20.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 12:20 UTC → 2026-09-14 12:20 UTC (72.0 uur), helft A/B-grens: 2026-09-13 00:20 UTC
- 7116580 trades, 71365 tokens, 198620 wallets, 2131714 posities (896544 geopend vanaf ≥ $7k, 1235170 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 126759
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8067 | 2628 | +94.33 | +43.40 | +375.93 | 7892.10 | 15233 | +2395.70 |
| dev | 2259 | 5285 | +2262.28 | -41.09 | +2364.57 | 59.10 | 18025 | +1839.91 |
| bot_hf | 2887 | 210809 | +734.17 | -434.86 | +5545.40 | 9304.66 | 405269 | +9310.66 |
| swing | 2099 | 22111 | -1028.85 | -1328.60 | -267.03 | 59.80 | 19496 | +19.76 |
| incidenteel | 157671 | 173398 | -4260.35 | -8536.51 | +29072.01 | 2965.53 | 291220 | +14661.44 |
| scalper | 25637 | 482313 | -12665.70 | -15754.81 | +24383.28 | 1187.10 | 485927 | +3566.19 |

Wallets met ≥ 10 posities: 16285, waarvan winstgevend: 21%. De top 1% winnaars pakt 41% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14864.13 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.23 | ja | 110 s | +140.38 / +838.94 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4303 (25) | 61% | +12.21 | +12.06 | +8% | 24.84 | ja | 4 s | +6.64 / +5.56 |
| 3 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7043 (81) | 45% | +47.10 | +45.95 | +1% | 24.34 | ja | 26 s | +31.22 / +15.88 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3133 (62) | 58% | +6.58 | +6.31 | +5% | 23.72 | ja | 4 s | +5.22 / +1.35 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6474 (50) | 39% | +6.95 | +6.03 | +0% | 20.4 | ja | 18 s | +3.45 / +3.50 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2692 (28) | 51% | +6.37 | +5.45 | +1% | 17.82 | ja | 10 s | +2.34 / +4.03 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.2 | ja | 102 s | +37.88 / +287.78 |
| 8 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2154 (9) | 50% | +21.06 | +19.85 | +1% | 16.02 | ja | 44 s | +5.04 / +16.02 |
| 9 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3288 (38) | 38% | +67.28 | +60.33 | +2% | 15.51 | ja | 29 s | +45.23 / +22.05 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2429 (39) | 47% | +61.72 | +58.49 | +2% | 15.33 | ja | 23 s | +21.76 / +39.96 |
| 11 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 321 (78) | 53% | +0.23 | +0.21 | +22% | 14.55 | ja | 16 s | +0.01 / +0.21 |
| 12 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 543 (0) | 63% | +14.19 | +13.52 | +11% | 14.23 | ja | 1 s | +8.26 / +5.93 |
| 13 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.21 | ja | 7 s | +330.44 / +251.06 |
| 14 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.08 | ja | 108 s | +25.67 / +230.85 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1729 (4) | 54% | +12.80 | +12.08 | +2% | 13.57 | ja | 42 s | +8.72 / +4.08 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1511 (26) | 44% | +3.32 | +3.03 | +2% | 13.12 | ja | 61 s | +2.32 / +1.00 |
| 17 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1990 (12) | 56% | +2.08 | +1.96 | +2% | 12.0 | ja | 10 s | +1.39 / +0.69 |
| 18 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 21 (2) | 81% | +22.69 | +14.86 | +163% | 11.84 | ja | 82 s | +5.24 / +17.45 |
| 19 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 20 (1) | 85% | +16.95 | +11.59 | +84% | 11.46 | ja | 52 s | +5.09 / +11.86 |
| 20 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1507 (1) | 41% | +6.73 | +5.76 | +1% | 11.38 | ja | 26 s | +5.89 / +0.84 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.23 | ja | 110 s | +140.38 / +838.94 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.21 | ja | 7 s | +330.44 / +251.06 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.2 | ja | 102 s | +37.88 / +287.78 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.08 | ja | 108 s | +25.67 / +230.85 |
| 5 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 8 (0) | 100% | +248.57 | +212.23 | +184% | 13.87 | nee | 12 s | +221.77 / +26.80 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 18 (1) | 94% | +199.73 | +171.04 | +134% | 13.36 | nee | 2 min | +158.23 / +41.50 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 250 (4) | 66% | +171.05 | +137.09 | +17% | 7.84 | ja | 16 s | +105.55 / +65.50 |
| 8 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 38 (1) | 58% | +149.84 | +132.90 | +51% | 7.99 | ja | 112 s | +4.01 / +145.83 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.29 | ja | 6 s | +72.89 / +55.61 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 18 (1) | 61% | +77.86 | +52.30 | +55% | 6.26 | nee | 2 min | +46.59 / +31.27 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.9 | nee | 6 s | +38.05 / +32.04 |
| 12 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3288 (38) | 38% | +67.28 | +60.33 | +2% | 15.51 | ja | 29 s | +45.23 / +22.05 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2429 (39) | 47% | +61.72 | +58.49 | +2% | 15.33 | ja | 23 s | +21.76 / +39.96 |
| 14 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 154 (1) | 74% | +58.77 | +55.17 | +15% | 6.76 | nee | 8 s | +31.78 / +26.99 |
| 15 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 14 (0) | 93% | +56.59 | +33.77 | +38% | 3.67 | nee | 31 s | +0.00 / +56.59 |
| 16 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (0) | 96% | +56.27 | +53.65 | +22% | 6.15 | nee | 16 s | +39.17 / +17.09 |
| 17 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.9 | nee | 8 s | +17.33 / +36.92 |
| 18 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 128 (0) | 70% | +54.21 | +49.73 | +18% | 6.77 | ja | 90 s | +12.29 / +41.92 |
| 19 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.85 | ja | 5 min | +36.59 / +15.89 |
| 20 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 80 (1) | 81% | +48.14 | +43.16 | +15% | 5.49 | nee | 34 s | +31.78 / +16.36 |

## Geluk-toets

Populatie: 7565 wallets met ≥ 20 posities, 79 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 26.08 | 4.55 | 5.68 |
| #10 | 12.74 | 3.43 | 3.66 |
| #20 | 9.61 | 3.12 | 3.27 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.68): **75**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 17701 | 48% | +5.0% | -0.3% | +439.90 |
| top 20 op winst (A) | 19/20 | 6625 | 45% | +2.7% | -1.1% | +605.73 |
| alle wallets | – | 393278 | 33% | -8.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.0% / +1.6% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3643): ρ = 0.521. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 175

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17701 | 29% | -12.7% | -8.1% | -449.17 |
| 2 s | 17701 | 24% | -15.6% | -9.5% | -550.61 |
| 10 s | 17701 | 22% | -17.1% | -9.7% | -603.63 |
| 60 s | 17701 | 20% | -20.4% | -8.3% | -721.43 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 405

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39343 | 30% | -11.5% | -7.6% | -906.20 |
| 2 s | 39343 | 25% | -14.5% | -9.2% | -1144.31 |
| 10 s | 39343 | 23% | -15.9% | -9.1% | -1253.29 |
| 60 s | 39343 | 20% | -18.9% | -7.8% | -1488.74 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 87

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6772 | 32% | -1.1% | -7.8% | -15.09 |
| 2 s | 6772 | 27% | -6.5% | -9.9% | -88.54 |
| 10 s | 6772 | 26% | -7.1% | -8.4% | -95.95 |
| 60 s | 6772 | 24% | -6.9% | -6.0% | -93.46 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
