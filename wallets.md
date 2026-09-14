# Wallet-analyse pump.fun — 2026-09-14 05:31 UTC

## Kort antwoord

- Geluk-toets: 75 van 7573 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=23.98, geluk-grens 5.51).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.2% per positie (alle wallets: -7.9%; 16 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -15.7%, 10 s: -17.2%, 60 s: -20.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 05:21 UTC → 2026-09-14 05:21 UTC (72.0 uur), helft A/B-grens: 2026-09-12 17:21 UTC
- 6928702 trades, 69397 tokens, 194290 wallets, 2085327 posities (898489 geopend vanaf ≥ $7k, 1186838 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 129044
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8026 | 2772 | +122.56 | +63.99 | +409.76 | 9359.90 | 15261 | +2813.96 |
| dev | 2193 | 5580 | +1974.68 | -268.71 | +2131.23 | 1467.07 | 17168 | +1706.55 |
| bot_hf | 2966 | 211709 | +860.87 | -1008.43 | +6416.49 | 10200.19 | 394912 | +9098.31 |
| swing | 2026 | 22694 | -927.28 | -1218.78 | -92.72 | 53.73 | 17576 | +39.34 |
| incidenteel | 153558 | 172280 | -4344.81 | -8573.31 | +28420.77 | 3231.13 | 280192 | +13701.94 |
| scalper | 25521 | 483454 | -12858.27 | -15786.42 | +23852.70 | 1919.49 | 461729 | +3047.21 |

Wallets met ≥ 10 posities: 16246, waarvan winstgevend: 21%. De top 1% winnaars pakt 40% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15172.24 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4169 (23) | 61% | +11.66 | +11.52 | +8% | 24.69 | ja | 4 s | +6.15 / +5.52 |
| 2 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3097 (62) | 58% | +6.75 | +6.48 | +5% | 24.17 | ja | 4 s | +4.27 / +2.48 |
| 3 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.1 | ja | 110 s | +140.38 / +658.24 |
| 4 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6940 (89) | 45% | +44.17 | +43.02 | +1% | 23.86 | ja | 25 s | +28.52 / +15.65 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6590 (58) | 39% | +8.40 | +7.48 | +1% | 20.73 | ja | 19 s | +4.77 / +3.64 |
| 6 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2148 (11) | 50% | +19.92 | +18.71 | +1% | 15.4 | ja | 42 s | +5.33 / +14.60 |
| 7 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2448 (43) | 47% | +62.52 | +59.30 | +2% | 15.32 | ja | 24 s | +26.26 / +36.26 |
| 8 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 275 (66) | 55% | +0.21 | +0.20 | +27% | 15.26 | ja | 15 s | +0.02 / +0.20 |
| 9 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3313 (46) | 38% | +56.92 | +49.96 | +2% | 15.24 | ja | 29 s | +39.76 / +17.16 |
| 10 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.67 | ja | 110 s | +53.26 / +222.65 |
| 11 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 559 (0) | 63% | +14.96 | +14.29 | +11% | 14.3 | ja | 1 s | +9.85 / +5.11 |
| 12 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.23 | ja | 7 s | +327.57 / +253.93 |
| 13 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1770 (8) | 54% | +13.13 | +12.40 | +2% | 13.32 | ja | 40 s | +9.26 / +3.87 |
| 14 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1528 (30) | 44% | +3.46 | +3.17 | +2% | 13.16 | ja | 61 s | +2.38 / +1.09 |
| 15 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.42 | ja | 110 s | +29.11 / +183.15 |
| 16 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1969 (12) | 55% | +2.21 | +2.09 | +2% | 12.2 | ja | 10 s | +1.14 / +1.08 |
| 17 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (2) | 82% | +23.12 | +15.29 | +159% | 11.9 | ja | 78 s | +3.30 / +19.82 |
| 18 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.67 | ja | 50 s | +3.38 / +14.20 |
| 19 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1385 (32) | 41% | +0.75 | +0.47 | +1% | 11.2 | ja | 61 s | +0.69 / +0.07 |
| 20 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1445 (3) | 41% | +6.91 | +5.94 | +1% | 11.12 | ja | 28 s | +5.98 / +0.93 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 32 (1) | 84% | +798.62 | +735.18 | +247% | 24.1 | ja | 110 s | +140.38 / +658.24 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.23 | ja | 7 s | +327.57 / +253.93 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.03 | nee | 12 s | +292.21 / +26.80 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 34 (1) | 68% | +275.91 | +251.14 | +116% | 14.67 | ja | 110 s | +53.26 / +222.65 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 33 (0) | 73% | +212.26 | +192.40 | +92% | 12.42 | ja | 110 s | +29.11 / +183.15 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.89 | nee | 2 min | +158.23 / +0.00 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 252 (3) | 66% | +156.65 | +122.70 | +17% | 7.94 | ja | 15 s | +100.33 / +56.32 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.3 | ja | 6 s | +48.47 / +80.03 |
| 9 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 33 (1) | 58% | +116.66 | +100.06 | +48% | 6.97 | ja | 2 min | +1.04 / +115.62 |
| 10 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.91 | nee | 6 s | +38.05 / +32.04 |
| 11 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 163 (1) | 75% | +63.84 | +60.24 | +15% | 6.98 | ja | 8 s | +36.01 / +27.84 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2448 (43) | 47% | +62.52 | +59.30 | +2% | 15.32 | ja | 24 s | +26.26 / +36.26 |
| 13 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3313 (46) | 38% | +56.92 | +49.96 | +2% | 15.24 | ja | 29 s | +39.76 / +17.16 |
| 14 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (0) | 96% | +55.37 | +52.75 | +21% | 6.09 | nee | 16 s | +31.89 / +23.48 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.92 | nee | 8 s | +9.56 / +44.68 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.87 | ja | 5 min | +36.59 / +15.89 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.35 | nee | 30 s | +0.00 / +50.13 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (1) | 82% | +47.87 | +42.88 | +16% | 5.4 | nee | 35 s | +19.50 / +28.37 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.59 | nee | 2 min | +46.59 / +0.00 |
| 20 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 89 (16) | 61% | +45.07 | +41.36 | +16% | 5.72 | nee | 64 s | +22.29 / +22.78 |

## Geluk-toets

Populatie: 7573 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 23.98 | 4.44 | 5.51 |
| #10 | 12.22 | 3.44 | 3.71 |
| #20 | 9.53 | 3.14 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.51): **75**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 18021 | 48% | +5.2% | -0.4% | +387.37 |
| top 20 op winst (A) | 17/20 | 6369 | 45% | +3.4% | -1.0% | +1005.91 |
| alle wallets | – | 377476 | 33% | -7.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.7% / +1.4% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3539): ρ = 0.53. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 230

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 18021 | 30% | -13.0% | -8.1% | -467.56 |
| 2 s | 18021 | 24% | -15.7% | -9.4% | -563.97 |
| 10 s | 18021 | 22% | -17.2% | -9.6% | -620.46 |
| 60 s | 18021 | 19% | -20.4% | -8.2% | -734.48 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 440

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 37848 | 30% | -11.5% | -8.0% | -869.14 |
| 2 s | 37848 | 24% | -14.5% | -9.6% | -1097.64 |
| 10 s | 37848 | 23% | -15.8% | -9.5% | -1199.64 |
| 60 s | 37848 | 20% | -18.9% | -8.2% | -1431.31 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 113

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6757 | 32% | -1.7% | -7.9% | -22.46 |
| 2 s | 6757 | 26% | -7.3% | -10.2% | -98.80 |
| 10 s | 6757 | 26% | -7.7% | -8.7% | -104.59 |
| 60 s | 6757 | 24% | -7.1% | -6.0% | -95.70 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
