# Wallet-analyse pump.fun — 2026-09-13 01:40 UTC

## Kort antwoord

- Geluk-toets: 63 van 7262 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.47, geluk-grens 5.33).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.2% per positie (alle wallets: -10.2%; 17 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.6%, 2 s: -14.9%, 10 s: -16.0%, 60 s: -19.8% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 01:38 UTC (59.8 uur), helft A/B-grens: 2026-09-11 19:43 UTC
- 5124941 trades, 45028 tokens, 187794 wallets, 1560645 posities (893712 geopend vanaf ≥ $7k, 666933 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 122565
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9730 | 5572 | -30.28 | -102.01 | +443.71 | 21075.90 | 17800 | +2577.12 |
| dev | 1829 | 5549 | +1329.17 | -661.76 | +980.94 | 4925.95 | 12708 | +983.23 |
| swing | 1585 | 18152 | -786.90 | -1084.75 | -405.53 | 69.31 | 8577 | +45.59 |
| bot_hf | 2893 | 197900 | +140.82 | -1768.83 | +5169.96 | 12497.30 | 242991 | +7224.27 |
| incidenteel | 145942 | 195915 | -6320.87 | -12424.47 | +15443.74 | 8709.86 | 156188 | +8119.77 |
| scalper | 25815 | 470624 | -13684.01 | -16812.09 | +15966.41 | 8628.74 | 228669 | +1894.55 |

Wallets met ≥ 10 posities: 15507, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -19352.07 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6134 (77) | 45% | +35.11 | +33.88 | +1% | 25.31 | ja | 23 s | +4.35 / +30.75 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3387 (19) | 62% | +9.37 | +9.23 | +9% | 23.72 | ja | 4 s | +3.68 / +5.69 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2557 (51) | 60% | +7.14 | +6.87 | +7% | 22.45 | ja | 4 s | +2.71 / +4.43 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6186 (44) | 38% | +6.81 | +5.81 | +0% | 22.44 | ja | 19 s | +3.98 / +2.83 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2257 (23) | 50% | +2.77 | +1.85 | +0% | 18.01 | ja | 11 s | +0.46 / +2.31 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2524 (43) | 45% | +28.88 | +26.73 | +1% | 16.59 | ja | 24 s | +15.70 / +13.18 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1891 (13) | 48% | +4.75 | +3.54 | +0% | 15.31 | ja | 37 s | +4.06 / +0.70 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1764 (11) | 51% | +8.97 | +8.23 | +1% | 14.62 | ja | 37 s | +1.91 / +7.06 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1374 (29) | 44% | +3.83 | +3.41 | +3% | 14.5 | ja | 61 s | +1.70 / +2.13 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 532 (1) | 62% | +12.37 | +11.54 | +10% | 13.93 | ja | 1 s | +6.26 / +6.11 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1806 (6) | 55% | +1.64 | +1.54 | +2% | 12.82 | ja | 10 s | +0.54 / +1.11 |
| 12 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1888 (24) | 52% | +3.27 | +3.21 | +10% | 12.42 | ja | 4 s | +1.55 / +1.72 |
| 13 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1119 (5) | 42% | +10.85 | +9.81 | +3% | 11.98 | ja | 27 s | +6.87 / +3.98 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.91 | ja | 53 s | +12.80 / +17.86 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.85 | ja | 51 s | +18.91 / +15.33 |
| 16 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2176 (2) | 48% | +5.21 | +4.76 | +1% | 11.6 | ja | 7 s | +3.05 / +2.16 |
| 17 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 596 (0) | 48% | +7.58 | +6.82 | +4% | 11.51 | ja | 1 s | +6.21 / +1.37 |
| 18 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.85 | ja | 8 s | +3.65 / +7.66 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +203.49 / +126.15 |
| 20 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 744 (6) | 68% | +3.33 | +3.08 | +1% | 10.26 | ja | 11 s | +2.55 / +0.78 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.74 | ja | 8 s | +203.49 / +126.15 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.62 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.84 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.9 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 250 (0) | 63% | +137.17 | +103.22 | +15% | 8.43 | ja | 15 s | +49.82 / +87.35 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 29 (7) | 72% | +83.41 | +71.57 | +34% | 5.4 | nee | 6 s | +13.73 / +69.68 |
| 8 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.31 | nee | 108 s | +34.55 / +25.67 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 181 (1) | 76% | +58.71 | +55.11 | +13% | 7.35 | ja | 9 s | +35.32 / +23.39 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 80 (3) | 96% | +52.13 | +49.52 | +21% | 6.06 | nee | 16 s | +22.00 / +30.14 |
| 11 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 5 (1) | 80% | +50.39 | +17.33 | +199% | 6.98 | nee | 11 s | +5.49 / +44.90 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +20.76 / +26.07 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +0.00 / +46.59 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 103 (14) | 55% | +43.15 | +38.35 | +14% | 6.1 | nee | 89 s | +20.21 / +22.94 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.58 | nee | 106 s | +31.47 / +10.49 |
| 16 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.92 | ja | 6 min | +9.85 / +29.47 |
| 17 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +4.91 / +33.47 |
| 18 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6134 (77) | 45% | +35.11 | +33.88 | +1% | 25.31 | ja | 23 s | +4.35 / +30.75 |
| 19 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.85 | ja | 51 s | +18.91 / +15.33 |
| 20 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.91 | ja | 53 s | +12.80 / +17.86 |

## Geluk-toets

Populatie: 7262 wallets met ≥ 20 posities, 82 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.47 | 4.4 | 5.33 |
| #10 | 10.18 | 3.4 | 3.72 |
| #20 | 8.32 | 3.1 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.33): **63**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14305 | 49% | +6.2% | -0.3% | +261.05 |
| top 20 op winst (A) | 18/20 | 1635 | 52% | +6.5% | +1.0% | +394.86 |
| alle wallets | – | 367054 | 32% | -10.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.7% / +1.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3515): ρ = 0.513. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 113

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14305 | 29% | -11.6% | -7.5% | -331.88 |
| 2 s | 14305 | 24% | -14.9% | -9.3% | -425.56 |
| 10 s | 14305 | 22% | -16.0% | -9.2% | -457.13 |
| 60 s | 14305 | 18% | -19.8% | -8.5% | -565.88 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 318

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 37500 | 31% | -11.1% | -7.1% | -831.14 |
| 2 s | 37500 | 25% | -14.0% | -8.7% | -1052.83 |
| 10 s | 37500 | 22% | -15.0% | -8.4% | -1123.85 |
| 60 s | 37500 | 18% | -18.3% | -7.6% | -1374.54 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 105

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7342 | 33% | -0.9% | -5.2% | -12.77 |
| 2 s | 7342 | 27% | -5.5% | -6.8% | -81.55 |
| 10 s | 7342 | 24% | -6.5% | -6.7% | -95.18 |
| 60 s | 7342 | 21% | -6.6% | -5.8% | -96.65 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
