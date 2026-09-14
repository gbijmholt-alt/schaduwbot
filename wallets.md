# Wallet-analyse pump.fun — 2026-09-14 18:48 UTC

## Kort antwoord

- Geluk-toets: 73 van 7734 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=27.41, geluk-grens 5.42).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.1% per positie (alle wallets: -10.0%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -14.1%, 2 s: -17.0%, 10 s: -18.3%, 60 s: -21.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 18:37 UTC → 2026-09-14 18:37 UTC (72.0 uur), helft A/B-grens: 2026-09-13 06:37 UTC
- 7182626 trades, 72395 tokens, 202478 wallets, 2176991 posities (902239 geopend vanaf ≥ $7k, 1274752 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 126478
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7722 | 2480 | +14.96 | -38.12 | +235.34 | 7780.61 | 13239 | +2110.46 |
| dev | 2250 | 5196 | +1980.49 | -334.56 | +1979.69 | 55.30 | 17989 | +2513.41 |
| bot_hf | 3069 | 216428 | +842.19 | -370.53 | +5142.21 | 9022.00 | 409657 | +8250.37 |
| swing | 2071 | 20173 | -1036.99 | -1338.98 | -239.39 | 46.35 | 19636 | +15.77 |
| incidenteel | 161717 | 172967 | -3954.67 | -8326.79 | +31650.22 | 2895.89 | 309333 | +15132.81 |
| scalper | 25649 | 484995 | -13416.91 | -16546.68 | +21179.39 | 1119.84 | 504898 | +3270.06 |

Wallets met ≥ 10 posities: 16454, waarvan winstgevend: 21%. De top 1% winnaars pakt 41% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15570.93 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.62 | ja | 118 s | +140.38 / +984.50 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7234 (89) | 45% | +51.19 | +50.06 | +1% | 24.89 | ja | 26 s | +34.74 / +16.45 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3080 (62) | 58% | +6.26 | +5.99 | +5% | 24.73 | ja | 4 s | +4.89 / +1.37 |
| 4 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4258 (25) | 61% | +11.58 | +11.43 | +8% | 24.61 | ja | 4 s | +7.94 / +3.63 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6687 (53) | 39% | +6.18 | +5.26 | +0% | 20.86 | ja | 18 s | +2.05 / +4.13 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2872 (26) | 50% | +6.65 | +5.73 | +1% | 18.85 | ja | 10 s | +1.01 / +5.64 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.11 | ja | 110 s | +37.88 / +355.13 |
| 8 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 367 (73) | 55% | +0.38 | +0.36 | +31% | 17.67 | ja | 20 s | +0.02 / +0.36 |
| 9 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2240 (9) | 50% | +17.00 | +15.84 | +1% | 16.0 | ja | 44 s | +2.74 / +14.26 |
| 10 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 83 (0) | 92% | +753.47 | +728.55 | +59% | 15.84 | ja | 7 s | +212.53 / +540.94 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3419 (40) | 37% | +61.96 | +55.00 | +2% | 15.54 | ja | 28 s | +39.12 / +22.84 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2536 (40) | 46% | +54.43 | +51.20 | +2% | 15.23 | ja | 22 s | +17.62 / +36.81 |
| 13 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.85 | ja | 110 s | +25.67 / +257.92 |
| 14 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1476 (24) | 45% | +3.87 | +3.58 | +3% | 13.32 | ja | 59 s | +2.58 / +1.30 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1711 (5) | 55% | +11.86 | +11.13 | +2% | 13.32 | ja | 42 s | +7.21 / +4.66 |
| 16 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 473 (0) | 63% | +12.52 | +12.01 | +11% | 12.53 | ja | 1 s | +6.97 / +5.55 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 21 (2) | 81% | +22.69 | +14.86 | +163% | 11.86 | ja | 82 s | +5.50 / +17.19 |
| 18 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1537 (3) | 40% | +6.88 | +5.91 | +1% | 11.82 | ja | 25 s | +5.87 / +1.01 |
| 19 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2040 (13) | 54% | +1.91 | +1.74 | +2% | 11.47 | ja | 10 s | +1.57 / +0.34 |
| 20 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 20 (1) | 85% | +16.95 | +11.59 | +84% | 11.47 | ja | 52 s | +4.82 / +12.13 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 41 (1) | 88% | +1124.88 | +1048.71 | +262% | 27.62 | ja | 118 s | +140.38 / +984.50 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 83 (0) | 92% | +753.47 | +728.55 | +59% | 15.84 | ja | 7 s | +212.53 / +540.94 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 42 (1) | 69% | +393.01 | +360.78 | +128% | 18.11 | ja | 110 s | +37.88 / +355.13 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 41 (0) | 71% | +283.59 | +263.08 | +98% | 14.85 | ja | 110 s | +25.67 / +257.92 |
| 5 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 18 (1) | 94% | +199.73 | +171.04 | +134% | 13.37 | nee | 2 min | +158.23 / +41.50 |
| 6 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 41 (1) | 58% | +170.72 | +153.79 | +53% | 8.5 | ja | 2 min | +4.01 / +166.71 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 273 (7) | 62% | +158.42 | +124.46 | +15% | 7.82 | ja | 15 s | +90.83 / +67.59 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 36 (6) | 81% | +125.29 | +113.45 | +43% | 7.05 | ja | 6 s | +72.33 / +52.96 |
| 9 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 18 (1) | 61% | +77.86 | +52.30 | +55% | 6.27 | nee | 2 min | +46.59 / +31.27 |
| 10 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 64 (0) | 59% | +73.01 | +54.25 | +29% | 5.25 | nee | 11 s | -0.36 / +73.37 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 10 (0) | 100% | +70.66 | +59.86 | +70% | 5.23 | nee | 5 s | +38.62 / +32.04 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 9 (0) | 100% | +70.27 | +37.22 | +133% | 7.56 | nee | 7 s | +47.40 / +22.87 |
| 13 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.06 | nee | 33 s | +0.00 / +69.17 |
| 14 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 162 (0) | 78% | +66.26 | +63.47 | +16% | 7.3 | ja | 9 s | +31.29 / +34.97 |
| 15 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 144 (0) | 74% | +65.98 | +61.50 | +19% | 7.96 | ja | 95 s | +12.93 / +53.05 |
| 16 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3419 (40) | 37% | +61.96 | +55.00 | +2% | 15.54 | ja | 28 s | +39.12 / +22.84 |
| 17 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 5 (0) | 80% | +59.06 | +39.16 | +136% | 5.41 | nee | 7 s | +8.19 / +50.87 |
| 18 | [9RG3…K6S2](https://solscan.io/account/9RG3YAuiQBDdG1esnzSXQ55o265to8nVriQhpwcbK6S2) | dev | 7 (3) | 57% | +56.58 | +32.52 | +87% | 3.66 | nee | 11 s | +10.84 / +45.73 |
| 19 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 82 (1) | 76% | +55.12 | +47.41 | +17% | 5.95 | nee | 30 s | +27.22 / +27.90 |
| 20 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2536 (40) | 46% | +54.43 | +51.20 | +2% | 15.23 | ja | 22 s | +17.62 / +36.81 |

## Geluk-toets

Populatie: 7734 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 27.41 | 4.52 | 5.42 |
| #10 | 13.26 | 3.46 | 3.71 |
| #20 | 9.6 | 3.15 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.42): **73**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 20122 | 48% | +5.1% | -0.5% | +731.15 |
| top 20 op winst (A) | 19/20 | 7423 | 45% | +2.9% | -0.9% | +1007.26 |
| alle wallets | – | 470145 | 32% | -10.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +0.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3689): ρ = 0.552. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 229

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20122 | 28% | -14.1% | -8.4% | -568.75 |
| 2 s | 20122 | 23% | -17.0% | -10.0% | -683.00 |
| 10 s | 20122 | 22% | -18.3% | -10.1% | -735.53 |
| 60 s | 20122 | 19% | -21.4% | -8.6% | -862.29 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 413

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40178 | 30% | -11.4% | -7.6% | -916.54 |
| 2 s | 40178 | 25% | -14.4% | -9.1% | -1158.53 |
| 10 s | 40178 | 23% | -15.8% | -9.0% | -1265.42 |
| 60 s | 40178 | 20% | -18.6% | -7.7% | -1495.13 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 93

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7048 | 32% | -1.5% | -8.2% | -21.34 |
| 2 s | 7048 | 27% | -6.7% | -9.8% | -94.02 |
| 10 s | 7048 | 26% | -7.2% | -8.4% | -101.97 |
| 60 s | 7048 | 24% | -6.8% | -6.0% | -95.65 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
