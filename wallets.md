# Wallet-analyse pump.fun — 2026-09-14 01:25 UTC

## Kort antwoord

- Geluk-toets: 77 van 7587 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=22.4, geluk-grens 5.4).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.9% per positie (alle wallets: -7.9%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.8%, 2 s: -14.8%, 10 s: -16.2%, 60 s: -19.4% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 01:16 UTC → 2026-09-14 01:16 UTC (72.0 uur), helft A/B-grens: 2026-09-12 13:16 UTC
- 6662391 trades, 65825 tokens, 192331 wallets, 2008444 posities (902414 geopend vanaf ≥ $7k, 1106030 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 129864
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8237 | 3023 | +737.11 | +676.72 | +966.20 | 11132.04 | 16718 | +3019.81 |
| dev | 2174 | 5675 | +1959.56 | -287.85 | +1953.47 | 1880.86 | 16069 | +1466.01 |
| bot_hf | 2972 | 211079 | +745.11 | -1215.08 | +6446.65 | 10851.79 | 370851 | +8810.62 |
| swing | 1963 | 22246 | -951.07 | -1252.85 | -161.03 | 61.80 | 15947 | +23.75 |
| incidenteel | 151325 | 173733 | -4189.87 | -8995.56 | +27776.34 | 4348.90 | 259817 | +12371.12 |
| scalper | 25660 | 486658 | -13782.40 | -16885.07 | +20316.68 | 3451.30 | 426628 | +2966.69 |

Wallets met ≥ 10 posities: 16260, waarvan winstgevend: 21%. De top 1% winnaars pakt 39% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -15481.56 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4094 (24) | 61% | +11.54 | +11.39 | +9% | 25.01 | ja | 4 s | +6.11 / +5.42 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6914 (85) | 45% | +40.89 | +39.74 | +1% | 23.99 | ja | 25 s | +23.72 / +17.17 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3049 (61) | 58% | +6.59 | +6.32 | +5% | 23.75 | ja | 4 s | +4.03 / +2.56 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 23 (0) | 87% | +622.20 | +558.76 | +286% | 22.45 | ja | 2 min | +140.38 / +481.82 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6532 (60) | 39% | +6.47 | +5.55 | +0% | 20.84 | ja | 19 s | +4.55 / +1.92 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 27 (0) | 74% | +265.69 | +240.45 | +147% | 15.93 | ja | 3 min | +98.12 / +167.56 |
| 7 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2464 (44) | 47% | +64.50 | +61.28 | +2% | 15.69 | ja | 25 s | +24.07 / +40.44 |
| 8 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2127 (12) | 50% | +18.32 | +17.10 | +1% | 15.47 | ja | 41 s | +8.37 / +9.95 |
| 9 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3276 (44) | 37% | +44.10 | +37.15 | +1% | 14.9 | ja | 30 s | +28.03 / +16.07 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 556 (0) | 64% | +14.89 | +14.22 | +11% | 14.3 | ja | 1 s | +10.43 / +4.45 |
| 11 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.22 | ja | 7 s | +296.22 / +285.29 |
| 12 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1529 (25) | 45% | +4.48 | +4.18 | +3% | 13.89 | ja | 61 s | +3.15 / +1.33 |
| 13 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1791 (8) | 54% | +13.40 | +12.67 | +2% | 13.84 | ja | 40 s | +8.69 / +4.71 |
| 14 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 26 (0) | 77% | +191.87 | +172.01 | +106% | 12.8 | ja | 3 min | +60.22 / +131.64 |
| 15 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1954 (9) | 55% | +2.03 | +1.91 | +2% | 12.21 | ja | 10 s | +1.07 / +0.96 |
| 16 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.66 | ja | 50 s | +2.65 / +14.93 |
| 17 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1449 (3) | 40% | +7.70 | +6.72 | +2% | 11.35 | ja | 26 s | +7.32 / +0.38 |
| 18 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 21 (2) | 81% | +21.18 | +13.34 | +157% | 11.22 | ja | 74 s | +2.58 / +18.59 |
| 19 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2168 (23) | 52% | +3.02 | +2.96 | +8% | 10.82 | ja | 4 s | +2.01 / +1.01 |
| 20 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 534 (0) | 51% | +9.02 | +8.25 | +5% | 10.69 | ja | 1 s | +7.55 / +1.47 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 23 (0) | 87% | +622.20 | +558.76 | +286% | 22.45 | ja | 2 min | +140.38 / +481.82 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.22 | ja | 7 s | +296.22 / +285.29 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.02 | nee | 12 s | +292.21 / +26.80 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 27 (0) | 74% | +265.69 | +240.45 | +147% | 15.93 | ja | 3 min | +98.12 / +167.56 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 26 (0) | 77% | +191.87 | +172.01 | +106% | 12.8 | ja | 3 min | +60.22 / +131.64 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 254 (3) | 65% | +158.95 | +125.00 | +17% | 8.07 | ja | 16 s | +99.47 / +59.48 |
| 7 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +158.23 / +0.00 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.3 | ja | 6 s | +41.58 / +86.93 |
| 9 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 26 (2) | 58% | +85.03 | +71.60 | +47% | 6.21 | ja | 3 min | +10.38 / +74.65 |
| 10 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2464 (44) | 47% | +64.50 | +61.28 | +2% | 15.69 | ja | 25 s | +24.07 / +40.44 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 10 (0) | 90% | +61.28 | +50.48 | +66% | 4.53 | nee | 5 s | +38.05 / +23.23 |
| 12 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 156 (1) | 74% | +58.88 | +55.28 | +15% | 6.7 | ja | 8 s | +35.29 / +23.59 |
| 13 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 75 (0) | 100% | +55.74 | +53.13 | +23% | 6.28 | ja | 20 s | +24.49 / +31.26 |
| 14 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.91 | nee | 8 s | +9.56 / +44.68 |
| 15 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.86 | ja | 5 min | +29.68 / +22.80 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 82 (1) | 83% | +51.77 | +46.78 | +16% | 5.6 | nee | 32 s | +16.35 / +35.42 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.35 | nee | 30 s | +0.00 / +50.13 |
| 18 | [4euy…ndfU](https://solscan.io/account/4euyaqBe45J5dniAcNARERUo7B1wG96riG21sEpNndfU) | dev | 7 (0) | 57% | +48.09 | +29.12 | +57% | 1.83 | nee | 19 s | +16.82 / +31.26 |
| 19 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 20 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3276 (44) | 37% | +44.10 | +37.15 | +1% | 14.9 | ja | 30 s | +28.03 / +16.07 |

## Geluk-toets

Populatie: 7587 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 22.4 | 4.48 | 5.4 |
| #10 | 12.2 | 3.46 | 3.68 |
| #20 | 9.53 | 3.13 | 3.27 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.4): **77**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 17330 | 48% | +4.9% | -0.4% | +574.35 |
| top 20 op winst (A) | 16/20 | 6093 | 45% | +3.3% | -1.2% | +897.26 |
| alle wallets | – | 374645 | 33% | -7.9% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.9% / +0.5% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3622): ρ = 0.535. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 166

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17330 | 30% | -11.8% | -7.8% | -408.33 |
| 2 s | 17330 | 25% | -14.8% | -9.3% | -511.78 |
| 10 s | 17330 | 22% | -16.2% | -9.3% | -562.35 |
| 60 s | 17330 | 19% | -19.4% | -8.0% | -671.16 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 357

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38625 | 29% | -12.4% | -8.5% | -956.46 |
| 2 s | 38625 | 24% | -15.6% | -10.0% | -1202.09 |
| 10 s | 38625 | 22% | -17.1% | -10.0% | -1319.34 |
| 60 s | 38625 | 18% | -20.6% | -9.0% | -1594.54 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 98

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6618 | 32% | -2.2% | -8.2% | -28.82 |
| 2 s | 6618 | 26% | -7.1% | -10.2% | -93.52 |
| 10 s | 6618 | 26% | -7.7% | -8.6% | -101.65 |
| 60 s | 6618 | 24% | -7.1% | -6.1% | -93.68 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
