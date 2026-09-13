# Wallet-analyse pump.fun — 2026-09-13 21:04 UTC

## Kort antwoord

- Geluk-toets: 77 van 7825 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.29, geluk-grens 5.27).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.6% per positie (alle wallets: -8.1%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.2%, 2 s: -15.3%, 10 s: -16.8%, 60 s: -20.5% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 20:56 UTC → 2026-09-13 20:56 UTC (72.0 uur), helft A/B-grens: 2026-09-12 08:56 UTC
- 6436124 trades, 61435 tokens, 199194 wallets, 1947974 posities (941185 geopend vanaf ≥ $7k, 1006789 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 135314
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9543 | 4141 | +434.97 | +372.66 | +779.20 | 15467.61 | 19351 | +3542.58 |
| dev | 2193 | 5948 | +1820.01 | -431.41 | +1767.46 | 2901.47 | 15330 | +1177.59 |
| swing | 1898 | 21806 | -914.04 | -1200.62 | -273.55 | 79.77 | 14533 | +26.81 |
| bot_hf | 3036 | 216451 | +607.73 | -1353.67 | +6557.48 | 11606.14 | 344067 | +8449.85 |
| incidenteel | 156230 | 188885 | -5182.65 | -10946.50 | +26341.68 | 6518.45 | 232668 | +11148.85 |
| scalper | 26294 | 503954 | -14484.00 | -17867.71 | +20248.18 | 5692.71 | 380840 | +2839.56 |

Wallets met ≥ 10 posities: 16707, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -17717.98 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6875 (84) | 45% | +45.43 | +44.29 | +1% | 25.02 | ja | 25 s | +18.83 / +26.61 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4003 (25) | 61% | +11.97 | +11.82 | +9% | 24.68 | ja | 4 s | +6.12 / +5.85 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3033 (65) | 59% | +7.11 | +6.84 | +6% | 23.49 | ja | 4 s | +4.59 / +2.52 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6686 (60) | 38% | +6.55 | +5.62 | +0% | 21.65 | ja | 19 s | +3.13 / +3.42 |
| 5 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2141 (13) | 49% | +13.49 | +12.28 | +1% | 15.7 | ja | 41 s | +5.86 / +7.63 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2563 (49) | 46% | +44.01 | +41.86 | +1% | 15.64 | ja | 25 s | +13.12 / +30.88 |
| 7 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3395 (51) | 36% | +28.17 | +21.21 | +1% | 14.84 | ja | 30 s | +8.36 / +19.81 |
| 8 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1583 (30) | 44% | +4.62 | +4.32 | +3% | 14.48 | ja | 60 s | +2.85 / +1.77 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 552 (0) | 64% | +14.54 | +13.88 | +11% | 14.41 | ja | 1 s | +10.04 / +4.50 |
| 10 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1844 (11) | 52% | +12.32 | +11.60 | +2% | 14.21 | ja | 40 s | +6.01 / +6.32 |
| 11 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +296.22 / +285.29 |
| 12 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 13 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1980 (8) | 55% | +1.72 | +1.61 | +1% | 12.35 | ja | 10 s | +0.89 / +0.83 |
| 14 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2154 (22) | 53% | +3.35 | +3.29 | +9% | 11.88 | ja | 4 s | +1.93 / +1.42 |
| 15 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1432 (3) | 41% | +9.22 | +8.18 | +2% | 11.6 | ja | 26 s | +6.88 / +2.34 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 584 (0) | 50% | +8.99 | +8.23 | +5% | 11.22 | ja | 1 s | +7.53 / +1.47 |
| 17 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1319 (31) | 41% | +0.88 | +0.59 | +1% | 11.05 | ja | 62 s | +0.73 / +0.15 |
| 18 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 81 (1) | 57% | +31.52 | +28.50 | +39% | 10.92 | ja | 45 s | +16.81 / +14.71 |
| 19 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 81 (1) | 57% | +29.49 | +26.30 | +37% | 10.8 | ja | 53 s | +13.51 / +15.98 |
| 20 | [9wZK…twgU](https://solscan.io/account/9wZKBHJhuo2ytDxAX6ZMRojcdKYXx5BAfC8JJwDLtwgU) | bot_hf | 1047 (7) | 63% | +1.36 | +1.14 | +0% | 10.71 | ja | 14 s | +1.18 / +0.18 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.19 | ja | 7 s | +296.22 / +285.29 |
| 2 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.03 | nee | 101 s | +86.41 / +366.88 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 15.97 | nee | 12 s | +206.40 / +112.61 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.94 | ja | 119 s | +75.90 / +112.67 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 264 (1) | 65% | +159.39 | +125.43 | +17% | 8.39 | ja | 16 s | +67.34 / +92.05 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +158.23 / +0.00 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.47 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 40 (8) | 78% | +133.90 | +122.06 | +40% | 7.35 | ja | 6 s | +49.23 / +84.67 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 157 (1) | 75% | +60.16 | +56.56 | +15% | 7.01 | ja | 9 s | +40.77 / +19.39 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 79 (2) | 98% | +57.46 | +54.84 | +23% | 6.3 | ja | 23 s | +23.94 / +33.52 |
| 11 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 92 (1) | 82% | +56.86 | +51.87 | +16% | 5.95 | nee | 30 s | +21.01 / +35.85 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.89 | nee | 8 s | +9.56 / +44.68 |
| 13 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.83 | ja | 5 min | +19.72 / +32.76 |
| 14 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.34 | nee | 30 s | +0.00 / +50.13 |
| 15 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +48.86 | +38.05 | +67% | 4.02 | nee | 4 s | +38.05 / +10.80 |
| 16 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +46.59 / +0.00 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6875 (84) | 45% | +45.43 | +44.29 | +1% | 25.02 | ja | 25 s | +18.83 / +26.61 |
| 18 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2563 (49) | 46% | +44.01 | +41.86 | +1% | 15.64 | ja | 25 s | +13.12 / +30.88 |
| 19 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.15 | nee | 112 s | +1.20 / +41.26 |
| 20 | [9Yrc…ax2G](https://solscan.io/account/9YrcswPY5NhbhUUStRCHzF3n2oF8NCZbQtrHHeUMax2G) | bot_hf | 51 (0) | 59% | +41.30 | +31.32 | +20% | 3.35 | nee | 7 s | +0.54 / +40.76 |

## Geluk-toets

Populatie: 7825 wallets met ≥ 20 posities, 75 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.29 | 4.42 | 5.27 |
| #10 | 10.98 | 3.44 | 3.65 |
| #20 | 9.19 | 3.15 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.27): **77**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 15194 | 49% | +5.6% | +0.0% | +411.08 |
| top 20 op winst (A) | 15/20 | 3377 | 48% | +4.7% | -0.2% | +636.45 |
| alle wallets | – | 361357 | 33% | -8.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.6% / +1.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3655): ρ = 0.531. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 145

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 15194 | 30% | -12.2% | -7.5% | -371.06 |
| 2 s | 15194 | 25% | -15.3% | -9.0% | -464.50 |
| 10 s | 15194 | 22% | -16.8% | -9.1% | -509.22 |
| 60 s | 15194 | 19% | -20.5% | -8.2% | -622.73 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 411

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41445 | 30% | -11.8% | -8.3% | -979.88 |
| 2 s | 41445 | 24% | -14.9% | -9.8% | -1232.53 |
| 10 s | 41445 | 22% | -16.1% | -9.6% | -1331.72 |
| 60 s | 41445 | 19% | -19.4% | -8.5% | -1606.23 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 142

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 10365 | 32% | -2.4% | -5.5% | -48.93 |
| 2 s | 10365 | 28% | -5.5% | -6.8% | -113.40 |
| 10 s | 10365 | 26% | -6.1% | -6.8% | -127.33 |
| 60 s | 10365 | 24% | -6.1% | -5.8% | -126.37 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
