# Wallet-analyse pump.fun — 2026-09-13 23:19 UTC

## Kort antwoord

- Geluk-toets: 77 van 7700 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=18.59, geluk-grens 5.28).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.0% per positie (alle wallets: -8.0%; 15 van 18 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.6%, 2 s: -14.7%, 10 s: -16.0%, 60 s: -19.1% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 23:10 UTC → 2026-09-13 23:10 UTC (72.0 uur), helft A/B-grens: 2026-09-12 11:10 UTC
- 6542295 trades, 63843 tokens, 192830 wallets, 1974539 posities (913444 geopend vanaf ≥ $7k, 1061095 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 132588
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8460 | 3415 | +571.31 | +505.74 | +827.35 | 12777.66 | 17436 | +3227.05 |
| dev | 2188 | 5823 | +1867.79 | -369.28 | +1870.82 | 2265.04 | 15590 | +1283.75 |
| swing | 1932 | 21953 | -942.69 | -1234.66 | -226.67 | 69.07 | 15400 | +14.23 |
| bot_hf | 3011 | 214045 | +627.33 | -1377.12 | +6530.96 | 11285.68 | 359730 | +8601.70 |
| incidenteel | 151425 | 176257 | -4218.82 | -9700.48 | +27726.20 | 4998.26 | 247646 | +11771.96 |
| scalper | 25814 | 491951 | -13906.35 | -17141.45 | +19610.90 | 4549.60 | 405293 | +2919.31 |

Wallets met ≥ 10 posities: 16429, waarvan winstgevend: 21%. De top 1% winnaars pakt 38% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -16001.44 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3995 (24) | 61% | +11.93 | +11.78 | +9% | 24.55 | ja | 4 s | +6.06 / +5.87 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6936 (83) | 45% | +40.49 | +39.34 | +1% | 24.15 | ja | 25 s | +21.61 / +18.88 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 3017 (63) | 59% | +6.79 | +6.52 | +5% | 23.62 | ja | 4 s | +4.08 / +2.71 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6653 (61) | 39% | +5.33 | +4.41 | +0% | 20.91 | ja | 19 s | +3.20 / +2.13 |
| 5 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2155 (14) | 50% | +19.38 | +18.16 | +1% | 15.79 | ja | 41 s | +10.38 / +8.99 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2527 (44) | 46% | +51.65 | +49.50 | +2% | 15.37 | ja | 25 s | +21.25 / +30.39 |
| 7 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3364 (48) | 36% | +41.42 | +34.47 | +1% | 14.94 | ja | 30 s | +20.70 / +20.72 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 551 (0) | 64% | +14.74 | +14.07 | +11% | 14.35 | ja | 1 s | +10.66 / +4.08 |
| 9 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1828 (10) | 54% | +15.74 | +15.01 | +2% | 14.26 | ja | 40 s | +8.85 / +6.88 |
| 10 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.22 | ja | 7 s | +296.22 / +285.29 |
| 11 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1553 (25) | 45% | +4.76 | +4.46 | +3% | 14.16 | ja | 61 s | +3.09 / +1.67 |
| 12 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.98 | ja | 119 s | +75.90 / +112.67 |
| 13 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1971 (8) | 55% | +1.99 | +1.86 | +2% | 12.29 | ja | 10 s | +1.03 / +0.96 |
| 14 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1443 (3) | 41% | +7.95 | +6.98 | +2% | 11.48 | ja | 26 s | +7.20 / +0.75 |
| 15 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2134 (21) | 53% | +3.17 | +3.11 | +9% | 11.32 | ja | 4 s | +1.80 / +1.38 |
| 16 | [DMmR…72kt](https://solscan.io/account/DMmR6s5fQuvUAF93H2WYVDs6n54j6yT5dZZoz7EK72kt) | bot_hf | 1360 (30) | 41% | +0.87 | +0.58 | +1% | 11.17 | ja | 61 s | +0.80 / +0.07 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 81 (1) | 57% | +31.52 | +28.50 | +39% | 10.95 | ja | 45 s | +16.81 / +14.71 |
| 18 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 81 (1) | 57% | +29.49 | +26.30 | +37% | 10.83 | ja | 53 s | +13.51 / +15.98 |
| 19 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 554 (0) | 50% | +8.80 | +8.03 | +5% | 10.73 | ja | 1 s | +7.38 / +1.42 |
| 20 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.5 | ja | 2 min | +43.46 / +94.54 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 70 (0) | 87% | +581.50 | +556.58 | +69% | 14.22 | ja | 7 s | +296.22 / +285.29 |
| 2 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 18 (0) | 89% | +453.29 | +389.85 | +272% | 19.09 | nee | 101 s | +86.41 / +366.88 |
| 3 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 10 (0) | 100% | +319.01 | +282.67 | +193% | 16.02 | nee | 12 s | +237.55 / +81.46 |
| 4 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 22 (0) | 68% | +188.57 | +163.33 | +133% | 12.98 | ja | 119 s | +75.90 / +112.67 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 256 (2) | 66% | +162.77 | +128.81 | +17% | 8.37 | ja | 16 s | +72.21 / +90.56 |
| 6 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +158.23 / +0.00 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 21 (0) | 71% | +138.00 | +118.14 | +96% | 10.5 | ja | 2 min | +43.46 / +94.54 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 39 (8) | 77% | +128.50 | +116.67 | +40% | 7.24 | ja | 6 s | +41.58 / +86.93 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 153 (1) | 75% | +57.99 | +54.38 | +15% | 6.63 | ja | 9 s | +36.80 / +21.18 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 78 (2) | 97% | +55.90 | +53.28 | +23% | 6.24 | ja | 21 s | +21.86 / +34.03 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 9 (0) | 89% | +55.22 | +44.41 | +67% | 4.27 | nee | 4 s | +38.05 / +17.16 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (0) | 100% | +54.25 | +21.19 | +155% | 6.91 | nee | 8 s | +9.56 / +44.68 |
| 13 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 86 (1) | 81% | +53.90 | +48.91 | +16% | 5.77 | nee | 32 s | +18.05 / +35.85 |
| 14 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 27 (4) | 82% | +52.48 | +45.59 | +77% | 9.86 | ja | 5 min | +22.18 / +30.30 |
| 15 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2527 (44) | 46% | +51.65 | +49.50 | +2% | 15.37 | ja | 25 s | +21.25 / +30.39 |
| 16 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 11 (0) | 91% | +50.13 | +27.32 | +40% | 3.35 | nee | 30 s | +0.00 / +50.13 |
| 17 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +46.59 / +0.00 |
| 18 | [9Yrc…ax2G](https://solscan.io/account/9YrcswPY5NhbhUUStRCHzF3n2oF8NCZbQtrHHeUMax2G) | bot_hf | 53 (0) | 58% | +42.88 | +32.90 | +20% | 3.43 | nee | 7 s | -1.13 / +44.02 |
| 19 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 92 (15) | 59% | +42.74 | +39.03 | +15% | 5.49 | nee | 66 s | +11.94 / +30.80 |
| 20 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 21 (2) | 48% | +42.46 | +30.01 | +30% | 4.16 | nee | 112 s | +1.20 / +41.26 |

## Geluk-toets

Populatie: 7700 wallets met ≥ 20 posities, 77 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 18.59 | 4.56 | 5.28 |
| #10 | 11.36 | 3.49 | 3.71 |
| #20 | 9.41 | 3.14 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.28): **77**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 18/20 | 17050 | 48% | +5.0% | -0.4% | +421.81 |
| top 20 op winst (A) | 16/20 | 6049 | 45% | +2.8% | -1.2% | +664.03 |
| alle wallets | – | 374115 | 33% | -8.0% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.2% / +1.7% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3644): ρ = 0.529. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 168

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 17050 | 30% | -11.6% | -7.8% | -395.36 |
| 2 s | 17050 | 25% | -14.7% | -9.4% | -499.82 |
| 10 s | 17050 | 22% | -16.0% | -9.3% | -544.17 |
| 60 s | 17050 | 19% | -19.1% | -8.1% | -649.78 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 389

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 40316 | 29% | -11.9% | -8.4% | -959.70 |
| 2 s | 40316 | 24% | -15.0% | -9.9% | -1207.52 |
| 10 s | 40316 | 22% | -16.3% | -9.8% | -1314.05 |
| 60 s | 40316 | 19% | -19.7% | -8.7% | -1587.84 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 68

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 3529 | 36% | -0.4% | -5.7% | -2.55 |
| 2 s | 3529 | 28% | -7.8% | -9.0% | -54.78 |
| 10 s | 3529 | 28% | -7.9% | -7.8% | -55.51 |
| 60 s | 3529 | 25% | -7.0% | -6.0% | -49.06 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
