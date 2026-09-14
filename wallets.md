# Wallet-analyse pump.fun — 2026-09-14 06:17 UTC

## Kort antwoord

- Geluk-toets: 71 van 7558 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=24.01, geluk-grens 5.65).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.2% per positie (alle wallets: -7.8%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -15.7%, 10 s: -17.2%, 60 s: -20.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 06:06 UTC → 2026-09-14 06:06 UTC (72.0 uur), helft A/B-grens: 2026-09-12 18:06 UTC
- 6953211 trades, 69734 tokens, 194532 wallets, 2091809 posities (897901 geopend vanaf ≥ $7k, 1193908 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 129087
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7977 | 2646 | +139.68 | +81.13 | +423.75 | 9218.98 | 15163 | +2789.78 |
| dev | 2197 | 5485 | +1984.28 | -273.55 | +2207.17 | 1105.64 | 16940 | +1719.25 |
| bot_hf | 2952 | 211549 | +842.61 | -956.76 | +6259.05 | 10085.80 | 397871 | +9124.02 |
| swing | 2037 | 22902 | -962.49 | -1254.66 | -137.30 | 51.82 | 18356 | +27.69 |
| incidenteel | 153845 | 172170 | -4304.92 | -8526.80 | +28413.46 | 3133.49 | 281631 | +13779.12 |
| scalper | 25524 | 483149 | -12797.14 | -15726.63 | +24093.75 | 1726.16 | 463947 | +3121.30 |

Wallets met ≥ 10 posities: 16248, waarvan winstgevend: 21%. De top 1% winnaars pakt 40% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15097.98 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4153 (24) | 61% | +11.39 | +11.25 | +8% | 24.53 | ja | 4 s | +6.06 / +5.33 |
| 2 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3073 (62) | 58% | +6.78 | +6.51 | +5% | 24.14 | ja | 4 s | +4.28 / +2.50 |
| 3 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.12 | ja | 110 s | +140.38 / +658.24 |
| 4 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6966 (91) | 45% | +46.29 | +45.14 | +1% | 24.0 | ja | 25 s | +29.81 / +16.48 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6591 (57) | 39% | +8.22 | +7.30 | +1% | 20.69 | ja | 19 s | +4.46 / +3.76 |
| 6 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | bot_hf | 283 (69) | 56% | +0.23 | +0.21 | +28% | 15.67 | ja | 14 s | +0.02 / +0.21 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2146 (12) | 50% | +20.63 | +19.41 | +1% | 15.5 | ja | 42 s | +4.46 / +16.16 |
| 8 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2437 (42) | 47% | +62.77 | +59.54 | +2% | 15.31 | ja | 24 s | +24.64 / +38.13 |
| 9 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3304 (43) | 38% | +59.09 | +52.13 | +2% | 15.3 | ja | 30 s | +42.38 / +16.71 |
| 10 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.68 | ja | 110 s | +53.26 / +222.65 |
| 11 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.24 | ja | 7 s | +327.57 / +253.93 |
| 12 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 555 (0) | 63% | +14.56 | +13.89 | +11% | 14.16 | ja | 1 s | +9.32 / +5.24 |
| 13 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1762 (8) | 54% | +13.15 | +12.42 | +2% | 13.39 | ja | 40 s | +8.90 / +4.25 |
| 14 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1527 (31) | 44% | +3.38 | +3.08 | +2% | 13.09 | ja | 61 s | +2.30 / +1.07 |
| 15 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.43 | ja | 110 s | +29.11 / +183.15 |
| 16 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1978 (12) | 55% | +2.17 | +2.05 | +2% | 12.2 | ja | 10 s | +1.17 / +1.00 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (2) | 82% | +23.12 | +15.29 | +159% | 11.91 | ja | 78 s | +3.30 / +19.82 |
| 18 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.68 | ja | 50 s | +3.38 / +14.20 |
| 19 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1385 (32) | 41% | +0.75 | +0.47 | +1% | 11.21 | ja | 61 s | +0.69 / +0.07 |
| 20 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1446 (4) | 41% | +7.36 | +6.38 | +2% | 11.16 | ja | 28 s | +6.01 / +1.35 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.12 | ja | 110 s | +140.38 / +658.24 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.24 | ja | 7 s | +327.57 / +253.93 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.04 | nee | 12 s | +292.21 / +26.80 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.68 | ja | 110 s | +53.26 / +222.65 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.43 | ja | 110 s | +29.11 / +183.15 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.9 | nee | 2 min | +158.23 / +0.00 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 254 (3) | 66% | +157.68 | +123.72 | +17% | 7.92 | ja | 15 s | +100.61 / +57.07 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.31 | ja | 6 s | +48.47 / +80.03 |
| 9 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 33 (1) | 58% | +116.66 | +100.06 | +48% | 6.98 | ja | 2 min | +1.04 / +115.62 |
| 10 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.91 | nee | 6 s | +38.05 / +32.04 |
| 11 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 163 (1) | 75% | +63.82 | +60.21 | +15% | 7.0 | ja | 8 s | +35.55 / +28.27 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2437 (42) | 47% | +62.77 | +59.54 | +2% | 15.31 | ja | 24 s | +24.64 / +38.13 |
| 13 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3304 (43) | 38% | +59.09 | +52.13 | +2% | 15.3 | ja | 30 s | +42.38 / +16.71 |
| 14 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (0) | 96% | +55.37 | +52.75 | +21% | 6.1 | nee | 16 s | +31.89 / +23.48 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.92 | nee | 8 s | +9.56 / +44.68 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.88 | ja | 5 min | +36.59 / +15.89 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 12 (0) | 92% | +50.88 | +28.07 | +39% | 3.36 | nee | 27 s | +0.00 / +50.88 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (1) | 82% | +47.87 | +42.88 | +16% | 5.41 | nee | 35 s | +19.50 / +28.37 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.59 | nee | 2 min | +46.59 / +0.00 |
| 20 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6966 (91) | 45% | +46.29 | +45.14 | +1% | 24.0 | ja | 25 s | +29.81 / +16.48 |

## Geluk-toets

Populatie: 7558 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 24.01 | 4.48 | 5.65 |
| #10 | 12.1 | 3.45 | 3.64 |
| #20 | 9.55 | 3.14 | 3.28 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.65): **71**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 18257 | 48% | +5.2% | -0.3% | +391.98 |
| top 20 op winst (A) | 17/20 | 6446 | 45% | +3.4% | -1.0% | +1009.34 |
| alle wallets | – | 381536 | 33% | -7.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.6% / +2.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3544): ρ = 0.528. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 239

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 18257 | 30% | -13.0% | -8.0% | -474.93 |
| 2 s | 18257 | 24% | -15.7% | -9.4% | -573.38 |
| 10 s | 18257 | 22% | -17.2% | -9.6% | -627.06 |
| 60 s | 18257 | 19% | -20.4% | -8.2% | -745.25 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 444

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 37818 | 30% | -11.5% | -8.0% | -866.61 |
| 2 s | 37818 | 24% | -14.5% | -9.6% | -1094.89 |
| 10 s | 37818 | 23% | -15.8% | -9.4% | -1195.64 |
| 60 s | 37818 | 20% | -18.9% | -8.2% | -1427.69 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 185

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13617 | 32% | -2.5% | -6.5% | -67.53 |
| 2 s | 13617 | 27% | -5.7% | -7.7% | -156.21 |
| 10 s | 13617 | 25% | -6.4% | -7.3% | -175.00 |
| 60 s | 13617 | 24% | -6.2% | -5.8% | -169.54 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
