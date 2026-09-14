# Wallet-analyse pump.fun — 2026-09-14 14:33 UTC

## Kort antwoord

- Geluk-toets: 82 van 7623 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=25.99, geluk-grens 5.51).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.4% per positie (alle wallets: -8.8%; 18 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.8%, 2 s: -16.6%, 10 s: -18.1%, 60 s: -21.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 14:23 UTC → 2026-09-14 14:23 UTC (72.0 uur), helft A/B-grens: 2026-09-13 02:23 UTC
- 7156509 trades, 71545 tokens, 201106 wallets, 2146901 posities (898781 geopend vanaf ≥ $7k, 1248120 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 126992
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9039 | 2663 | +81.73 | +28.84 | +352.11 | 8019.95 | 15371 | +2549.74 |
| dev | 2265 | 5380 | +2142.86 | -178.23 | +2218.94 | 56.26 | 18255 | +1810.97 |
| bot_hf | 2866 | 212252 | +847.62 | -324.65 | +5438.15 | 9166.00 | 405968 | +9225.13 |
| swing | 2085 | 21368 | -1037.42 | -1340.17 | -300.19 | 65.69 | 19255 | +13.59 |
| incidenteel | 159399 | 173004 | -3893.98 | -8211.75 | +29749.45 | 3066.52 | 295528 | +14866.14 |
| scalper | 25452 | 484114 | -13253.72 | -16346.22 | +23445.94 | 1247.89 | 493743 | +3475.55 |

Wallets met ≥ 10 posities: 16297, waarvan winstgevend: 21%. De top 1% winnaars pakt 41% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15112.92 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.19 | ja | 110 s | +140.38 / +838.94 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4310 (25) | 61% | +12.13 | +11.98 | +8% | 24.73 | ja | 4 s | +7.25 / +4.88 |
| 3 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7070 (83) | 45% | +48.71 | +47.56 | +1% | 24.53 | ja | 26 s | +33.02 / +15.69 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3129 (63) | 58% | +5.92 | +5.66 | +4% | 23.68 | ja | 4 s | +5.14 / +0.79 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6487 (52) | 39% | +6.36 | +5.44 | +0% | 20.34 | ja | 18 s | +2.48 / +3.88 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2753 (27) | 50% | +6.11 | +5.20 | +1% | 18.31 | ja | 10 s | +1.13 / +4.98 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 338 (82) | 54% | +0.31 | +0.29 | +28% | 16.35 | ja | 16 s | +0.02 / +0.29 |
| 8 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.17 | ja | 102 s | +37.88 / +287.78 |
| 9 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2170 (11) | 50% | +19.38 | +18.16 | +1% | 15.93 | ja | 44 s | +3.70 / +15.68 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2460 (39) | 47% | +64.47 | +61.25 | +2% | 15.51 | ja | 23 s | +20.10 / +44.37 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3315 (40) | 38% | +63.09 | +56.14 | +2% | 15.31 | ja | 29 s | +42.01 / +21.08 |
| 12 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +330.44 / +251.06 |
| 13 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.06 | ja | 108 s | +25.67 / +230.85 |
| 14 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 525 (0) | 63% | +13.86 | +13.19 | +11% | 13.5 | ja | 1 s | +7.99 / +5.87 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1715 (6) | 54% | +12.23 | +11.50 | +2% | 13.43 | ja | 42 s | +7.63 / +4.61 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1502 (27) | 44% | +3.20 | +2.91 | +2% | 13.08 | ja | 60 s | +2.37 / +0.83 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 21 (2) | 81% | +22.69 | +14.86 | +163% | 11.83 | ja | 82 s | +5.50 / +17.19 |
| 18 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2025 (13) | 56% | +2.04 | +1.91 | +2% | 11.66 | ja | 10 s | +1.35 / +0.69 |
| 19 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1499 (1) | 41% | +6.99 | +6.02 | +1% | 11.51 | ja | 25 s | +6.77 / +0.22 |
| 20 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 20 (1) | 85% | +16.95 | +11.59 | +84% | 11.44 | ja | 52 s | +4.82 / +12.13 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.19 | ja | 110 s | +140.38 / +838.94 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +330.44 / +251.06 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.17 | ja | 102 s | +37.88 / +287.78 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.06 | ja | 108 s | +25.67 / +230.85 |
| 5 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 7 (0) | 100% | +216.81 | +180.47 | +181% | 12.64 | nee | 11 s | +190.01 / +26.80 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 18 (1) | 94% | +199.73 | +171.04 | +134% | 13.34 | nee | 2 min | +158.23 / +41.50 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 251 (4) | 65% | +163.89 | +129.93 | +17% | 7.65 | ja | 16 s | +98.47 / +65.41 |
| 8 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 38 (1) | 58% | +149.84 | +132.90 | +51% | 7.98 | ja | 112 s | +4.01 / +145.83 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.28 | ja | 6 s | +72.89 / +55.61 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 18 (1) | 61% | +77.86 | +52.30 | +55% | 6.25 | nee | 2 min | +46.59 / +31.27 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.89 | nee | 6 s | +38.05 / +32.04 |
| 12 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 16 (0) | 94% | +64.64 | +41.83 | +38% | 3.99 | nee | 31 s | +0.00 / +64.64 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2460 (39) | 47% | +64.47 | +61.25 | +2% | 15.51 | ja | 23 s | +20.10 / +44.37 |
| 14 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3315 (40) | 38% | +63.09 | +56.14 | +2% | 15.31 | ja | 29 s | +42.01 / +21.08 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 7 (0) | 100% | +59.62 | +26.57 | +149% | 7.33 | nee | 8 s | +50.39 / +9.23 |
| 16 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 155 (0) | 76% | +59.53 | +55.92 | +15% | 6.84 | ja | 9 s | +30.38 / +29.14 |
| 17 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 82 (0) | 96% | +56.52 | +53.91 | +21% | 6.17 | nee | 16 s | +37.79 / +18.73 |
| 18 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 130 (0) | 71% | +55.91 | +51.42 | +18% | 6.95 | ja | 88 s | +12.61 / +43.30 |
| 19 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 61 (0) | 54% | +53.47 | +34.71 | +22% | 3.83 | nee | 10 s | -3.98 / +57.45 |
| 20 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 78% | +52.38 | +45.49 | +80% | 9.93 | ja | 3 min | +31.79 / +20.59 |

## Geluk-toets

Populatie: 7623 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 25.99 | 4.49 | 5.51 |
| #10 | 12.67 | 3.45 | 3.67 |
| #20 | 9.58 | 3.16 | 3.3 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.51): **82**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 17983 | 48% | +5.4% | -0.3% | +451.40 |
| top 20 op winst (A) | 19/20 | 5496 | 44% | +2.7% | -1.3% | +594.82 |
| alle wallets | – | 412463 | 33% | -8.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.0% / +0.4% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3692): ρ = 0.544. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 252

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17983 | 29% | -13.8% | -8.2% | -497.60 |
| 2 s | 17983 | 24% | -16.6% | -9.8% | -598.08 |
| 10 s | 17983 | 22% | -18.1% | -10.0% | -651.00 |
| 60 s | 17983 | 20% | -21.2% | -8.5% | -763.86 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 420

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39524 | 30% | -11.6% | -7.6% | -912.78 |
| 2 s | 39524 | 25% | -14.6% | -9.2% | -1151.65 |
| 10 s | 39524 | 22% | -16.0% | -9.1% | -1261.49 |
| 60 s | 39524 | 20% | -18.9% | -7.8% | -1494.14 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 89

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6819 | 32% | -1.2% | -8.0% | -16.91 |
| 2 s | 6819 | 27% | -6.7% | -10.1% | -91.84 |
| 10 s | 6819 | 26% | -7.2% | -8.4% | -97.84 |
| 60 s | 6819 | 24% | -6.9% | -6.0% | -94.46 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
