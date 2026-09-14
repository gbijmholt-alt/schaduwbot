# Wallet-analyse pump.fun — 2026-09-14 10:24 UTC

## Kort antwoord

- Geluk-toets: 88 van 7529 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=26.06, geluk-grens 5.21).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.3% per positie (alle wallets: -7.9%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -15.7%, 10 s: -17.2%, 60 s: -20.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 10:13 UTC → 2026-09-14 10:13 UTC (72.0 uur), helft A/B-grens: 2026-09-12 22:13 UTC
- 7089253 trades, 71129 tokens, 197310 wallets, 2123367 posities (893845 geopend vanaf ≥ $7k, 1229522 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 126099
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7956 | 2631 | +94.80 | +38.56 | +364.53 | 8219.45 | 14155 | +2339.00 |
| dev | 2235 | 5233 | +2210.90 | -73.69 | +2390.23 | 84.85 | 17662 | +1941.37 |
| bot_hf | 2916 | 210104 | +731.97 | -599.99 | +5828.24 | 9250.54 | 408906 | +9281.27 |
| swing | 2062 | 22361 | -1002.14 | -1295.45 | -189.99 | 57.38 | 19409 | +18.23 |
| incidenteel | 156604 | 173192 | -4252.88 | -8552.21 | +28598.62 | 2897.84 | 291512 | +14404.97 |
| scalper | 25537 | 480324 | -12409.40 | -15385.67 | +24837.47 | 1055.63 | 477878 | +3398.88 |

Wallets met ≥ 10 posities: 16217, waarvan winstgevend: 22%. De top 1% winnaars pakt 41% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14626.76 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.2 | ja | 110 s | +140.38 / +838.94 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4294 (25) | 62% | +12.18 | +12.04 | +8% | 24.79 | ja | 4 s | +6.52 / +5.66 |
| 3 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6985 (85) | 45% | +48.68 | +47.53 | +1% | 24.25 | ja | 26 s | +29.70 / +18.98 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3088 (61) | 59% | +6.90 | +6.63 | +5% | 23.95 | ja | 4 s | +4.64 / +2.27 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6496 (50) | 39% | +7.88 | +6.96 | +1% | 20.56 | ja | 18 s | +4.40 / +3.49 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2761 (29) | 51% | +4.49 | +3.57 | +0% | 17.61 | ja | 11 s | +1.99 / +2.50 |
| 7 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.19 | ja | 102 s | +37.88 / +287.78 |
| 8 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2155 (9) | 50% | +20.72 | +19.50 | +1% | 15.77 | ja | 43 s | +6.00 / +14.72 |
| 9 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3292 (39) | 38% | +66.50 | +59.54 | +2% | 15.43 | ja | 29 s | +46.30 / +20.20 |
| 10 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 298 (62) | 55% | +0.23 | +0.22 | +26% | 15.3 | ja | 17 s | +0.01 / +0.22 |
| 11 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2414 (39) | 47% | +60.89 | +57.66 | +2% | 15.24 | ja | 24 s | +15.58 / +45.31 |
| 12 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +330.44 / +251.06 |
| 13 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.07 | ja | 108 s | +25.67 / +230.85 |
| 14 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 539 (0) | 63% | +14.04 | +13.37 | +11% | 14.05 | ja | 1 s | +8.14 / +5.91 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1739 (4) | 54% | +12.85 | +12.13 | +2% | 13.45 | ja | 42 s | +9.28 / +3.57 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1523 (27) | 44% | +3.33 | +3.04 | +2% | 13.04 | ja | 60 s | +2.30 / +1.03 |
| 17 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1986 (12) | 55% | +2.21 | +2.08 | +2% | 12.19 | ja | 10 s | +1.45 / +0.76 |
| 18 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (2) | 82% | +23.12 | +15.29 | +159% | 11.87 | ja | 78 s | +3.30 / +19.82 |
| 19 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.64 | ja | 50 s | +3.38 / +14.20 |
| 20 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1490 (1) | 40% | +6.95 | +5.97 | +1% | 11.24 | ja | 27 s | +5.89 / +1.06 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 38 (1) | 87% | +979.33 | +915.89 | +248% | 26.2 | ja | 110 s | +140.38 / +838.94 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +330.44 / +251.06 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 39 (1) | 67% | +325.66 | +300.00 | +117% | 16.19 | ja | 102 s | +37.88 / +287.78 |
| 4 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 15.99 | nee | 12 s | +292.21 / +26.80 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 38 (0) | 71% | +256.52 | +236.01 | +96% | 14.07 | ja | 108 s | +25.67 / +230.85 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 248 (4) | 66% | +167.83 | +133.88 | +18% | 7.83 | ja | 15 s | +102.43 / +65.40 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.86 | nee | 2 min | +158.23 / +0.00 |
| 8 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 38 (1) | 58% | +149.84 | +132.90 | +51% | 7.99 | ja | 112 s | +4.01 / +145.83 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.28 | ja | 6 s | +63.41 / +65.09 |
| 10 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.89 | nee | 6 s | +38.05 / +32.04 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3292 (39) | 38% | +66.50 | +59.54 | +2% | 15.43 | ja | 29 s | +46.30 / +20.20 |
| 12 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 157 (1) | 75% | +62.64 | +59.04 | +15% | 6.96 | ja | 9 s | +35.59 / +27.05 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2414 (39) | 47% | +60.89 | +57.66 | +2% | 15.24 | ja | 24 s | +15.58 / +45.31 |
| 14 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (0) | 96% | +55.37 | +52.75 | +21% | 6.08 | ja | 16 s | +31.89 / +23.48 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.9 | nee | 8 s | +9.56 / +44.68 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.84 | ja | 5 min | +36.59 / +15.89 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 13 (0) | 92% | +52.26 | +29.45 | +37% | 3.36 | nee | 30 s | +0.00 / +52.26 |
| 18 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 120 (0) | 69% | +49.20 | +44.71 | +18% | 6.41 | ja | 88 s | +12.29 / +36.91 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6985 (85) | 45% | +48.68 | +47.53 | +1% | 24.25 | ja | 26 s | +29.70 / +18.98 |
| 20 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (1) | 82% | +47.87 | +42.88 | +16% | 5.39 | nee | 35 s | +20.97 / +26.90 |

## Geluk-toets

Populatie: 7529 wallets met ≥ 20 posities, 79 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 26.06 | 4.42 | 5.21 |
| #10 | 12.66 | 3.44 | 3.68 |
| #20 | 9.5 | 3.13 | 3.3 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.21): **88**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 19132 | 48% | +5.3% | -0.3% | +403.44 |
| top 20 op winst (A) | 17/20 | 6710 | 45% | +2.7% | -1.0% | +602.27 |
| alle wallets | – | 396811 | 33% | -7.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.6% / +1.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3629): ρ = 0.531. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 236

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 19132 | 30% | -13.0% | -8.0% | -496.81 |
| 2 s | 19132 | 24% | -15.7% | -9.4% | -598.92 |
| 10 s | 19132 | 22% | -17.2% | -9.5% | -658.40 |
| 60 s | 19132 | 20% | -20.4% | -8.2% | -782.10 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 397

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39288 | 30% | -11.3% | -7.6% | -891.34 |
| 2 s | 39288 | 25% | -14.4% | -9.2% | -1129.14 |
| 10 s | 39288 | 23% | -15.7% | -9.0% | -1236.06 |
| 60 s | 39288 | 20% | -18.7% | -7.8% | -1470.06 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 172

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13716 | 32% | -2.2% | -6.4% | -60.59 |
| 2 s | 13716 | 27% | -5.5% | -7.6% | -150.70 |
| 10 s | 13716 | 26% | -6.2% | -7.2% | -169.86 |
| 60 s | 13716 | 24% | -6.2% | -5.8% | -169.72 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
