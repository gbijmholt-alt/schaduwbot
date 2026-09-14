# Wallet-analyse pump.fun — 2026-09-14 08:20 UTC

## Kort antwoord

- Geluk-toets: 86 van 7521 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=25.24, geluk-grens 5.28).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.3% per positie (alle wallets: -7.8%; 17 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -13.0%, 2 s: -15.7%, 10 s: -17.3%, 60 s: -20.6% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-11 08:11 UTC → 2026-09-14 08:11 UTC (72.0 uur), helft A/B-grens: 2026-09-12 20:11 UTC
- 7039798 trades, 70721 tokens, 196188 wallets, 2110304 posities (893588 geopend vanaf ≥ $7k, 1216716 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 127083
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8032 | 2582 | +106.99 | +55.54 | +394.77 | 8379.53 | 15084 | +2778.12 |
| dev | 2211 | 5220 | +2160.46 | -102.73 | +2327.19 | 349.81 | 17002 | +1778.72 |
| bot_hf | 2919 | 209952 | +806.93 | -637.68 | +6022.33 | 9342.36 | 405569 | +9311.65 |
| swing | 2069 | 22820 | -997.13 | -1297.18 | -166.12 | 58.22 | 19057 | +15.91 |
| incidenteel | 155466 | 172815 | -4450.39 | -8693.19 | +27881.31 | 3022.80 | 286564 | +14042.22 |
| scalper | 25491 | 480199 | -12417.92 | -15386.57 | +24943.31 | 1408.30 | 473440 | +3261.75 |

Wallets met ≥ 10 posities: 16210, waarvan winstgevend: 22%. De top 1% winnaars pakt 40% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14791.06 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 36 (1) | 86% | +918.87 | +855.43 | +247% | 25.41 | ja | 110 s | +140.38 / +778.48 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4224 (24) | 61% | +11.88 | +11.73 | +8% | 24.9 | ja | 4 s | +5.79 / +6.09 |
| 3 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6961 (87) | 45% | +47.75 | +46.60 | +1% | 24.19 | ja | 26 s | +30.44 / +17.30 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3072 (62) | 58% | +6.66 | +6.39 | +5% | 23.87 | ja | 4 s | +3.99 / +2.67 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6576 (52) | 39% | +7.52 | +6.60 | +0% | 20.72 | ja | 19 s | +4.12 / +3.40 |
| 6 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2750 (30) | 51% | +3.60 | +2.69 | +0% | 17.52 | ja | 11 s | +2.31 / +1.30 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2173 (11) | 50% | +18.36 | +17.15 | +1% | 15.62 | ja | 43 s | +3.83 / +14.53 |
| 8 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 37 (1) | 68% | +307.44 | +281.79 | +117% | 15.61 | ja | 102 s | +37.88 / +269.57 |
| 9 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 289 (57) | 55% | +0.23 | +0.21 | +27% | 15.53 | ja | 18 s | +0.02 / +0.21 |
| 10 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3327 (41) | 38% | +64.96 | +58.01 | +2% | 15.52 | ja | 30 s | +46.90 / +18.07 |
| 11 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2411 (39) | 47% | +59.23 | +56.00 | +2% | 15.28 | ja | 24 s | +19.73 / +39.50 |
| 12 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 552 (0) | 63% | +14.86 | +14.19 | +11% | 14.26 | ja | 1 s | +9.31 / +5.55 |
| 13 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.23 | ja | 7 s | +327.57 / +253.93 |
| 14 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 36 (0) | 72% | +242.62 | +222.11 | +96% | 13.61 | ja | 108 s | +25.67 / +216.95 |
| 15 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1766 (7) | 54% | +12.24 | +11.51 | +2% | 13.46 | ja | 41 s | +8.32 / +3.92 |
| 16 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1545 (27) | 44% | +3.10 | +2.81 | +2% | 13.02 | ja | 60 s | +1.96 / +1.14 |
| 17 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1980 (12) | 55% | +2.12 | +2.00 | +2% | 12.09 | ja | 10 s | +1.18 / +0.94 |
| 18 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 22 (2) | 82% | +23.12 | +15.29 | +159% | 11.9 | ja | 78 s | +3.30 / +19.82 |
| 19 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 21 (1) | 86% | +17.58 | +12.23 | +84% | 11.67 | ja | 50 s | +3.38 / +14.20 |
| 20 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1361 (29) | 41% | +0.80 | +0.51 | +1% | 11.21 | ja | 61 s | +0.73 / +0.07 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 36 (1) | 86% | +918.87 | +855.43 | +247% | 25.41 | ja | 110 s | +140.38 / +778.48 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.23 | ja | 7 s | +327.57 / +253.93 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.03 | nee | 12 s | +292.21 / +26.80 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 37 (1) | 68% | +307.44 | +281.79 | +117% | 15.61 | ja | 102 s | +37.88 / +269.57 |
| 5 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 36 (0) | 72% | +242.62 | +222.11 | +96% | 13.61 | ja | 108 s | +25.67 / +216.95 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.89 | nee | 2 min | +158.23 / +0.00 |
| 7 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 250 (3) | 66% | +154.72 | +120.76 | +17% | 7.81 | ja | 15 s | +97.68 / +57.03 |
| 8 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 36 (1) | 58% | +141.31 | +124.38 | +51% | 7.68 | ja | 112 s | +4.01 / +137.30 |
| 9 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 38 (7) | 79% | +128.50 | +116.67 | +41% | 7.3 | ja | 6 s | +48.47 / +80.03 |
| 10 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 11 (0) | 91% | +70.10 | +59.29 | +68% | 4.91 | nee | 6 s | +38.05 / +32.04 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3327 (41) | 38% | +64.96 | +58.01 | +2% | 15.52 | ja | 30 s | +46.90 / +18.07 |
| 12 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 159 (1) | 76% | +63.56 | +59.96 | +15% | 7.07 | ja | 8 s | +35.29 / +28.27 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2411 (39) | 47% | +59.23 | +56.00 | +2% | 15.28 | ja | 24 s | +19.73 / +39.50 |
| 14 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (0) | 96% | +55.37 | +52.75 | +21% | 6.09 | ja | 16 s | +31.89 / +23.48 |
| 15 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.92 | nee | 8 s | +9.56 / +44.68 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.87 | ja | 5 min | +36.59 / +15.89 |
| 17 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 12 (0) | 92% | +50.88 | +28.07 | +39% | 3.36 | nee | 27 s | +0.00 / +50.88 |
| 18 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 77 (1) | 82% | +47.87 | +42.88 | +16% | 5.4 | nee | 35 s | +19.50 / +28.37 |
| 19 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6961 (87) | 45% | +47.75 | +46.60 | +1% | 24.19 | ja | 26 s | +30.44 / +17.30 |
| 20 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.59 | nee | 2 min | +46.59 / +0.00 |

## Geluk-toets

Populatie: 7521 wallets met ≥ 20 posities, 79 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 25.24 | 4.43 | 5.28 |
| #10 | 12.59 | 3.45 | 3.66 |
| #20 | 9.52 | 3.16 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.28): **86**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 19221 | 48% | +5.3% | -0.3% | +396.06 |
| top 20 op winst (A) | 17/20 | 6684 | 45% | +2.6% | -1.0% | +606.96 |
| alle wallets | – | 399595 | 34% | -7.8% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +1.8% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3564): ρ = 0.527. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 233

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 19221 | 30% | -13.0% | -8.0% | -500.44 |
| 2 s | 19221 | 24% | -15.7% | -9.5% | -604.29 |
| 10 s | 19221 | 22% | -17.3% | -9.6% | -664.38 |
| 60 s | 19221 | 19% | -20.6% | -8.3% | -790.39 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 432

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 39209 | 30% | -11.3% | -7.7% | -883.15 |
| 2 s | 39209 | 25% | -14.2% | -9.2% | -1117.38 |
| 10 s | 39209 | 23% | -15.6% | -9.1% | -1223.95 |
| 60 s | 39209 | 20% | -18.6% | -7.8% | -1456.29 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 176

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13614 | 32% | -2.4% | -6.5% | -64.05 |
| 2 s | 13614 | 27% | -5.7% | -7.7% | -154.64 |
| 10 s | 13614 | 25% | -6.4% | -7.3% | -173.41 |
| 60 s | 13614 | 24% | -6.2% | -5.8% | -170.15 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
