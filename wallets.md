# Wallet-analyse pump.fun — 2026-09-12 23:37 UTC

## Kort antwoord

- Geluk-toets: 56 van 7118 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=16.6, geluk-grens 5.45).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.2% per positie (alle wallets: -10.5%; 19 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.2%, 2 s: -14.5%, 10 s: -15.5%, 60 s: -19.3% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 23:35 UTC (57.8 uur), helft A/B-grens: 2026-09-11 18:41 UTC
- 4907398 trades, 42762 tokens, 183439 wallets, 1494748 posities (876726 geopend vanaf ≥ $7k, 618022 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 120982
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9423 | 5461 | -11.64 | -76.16 | +505.38 | 20993.64 | 16757 | +2457.62 |
| dev | 1776 | 5422 | +1268.28 | -661.95 | +919.06 | 4904.29 | 12038 | +924.34 |
| swing | 1564 | 17930 | -765.09 | -1060.13 | -372.97 | 68.67 | 7949 | +51.87 |
| bot_hf | 2845 | 193976 | +157.17 | -1743.77 | +5062.64 | 12278.52 | 230934 | +7135.00 |
| incidenteel | 142340 | 193505 | -6275.06 | -12320.99 | +14865.51 | 8690.52 | 143616 | +8039.35 |
| scalper | 25491 | 460432 | -13123.73 | -16186.56 | +15511.93 | 8592.53 | 206728 | +1800.12 |

Wallets met ≥ 10 posities: 15193, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18750.07 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5969 (77) | 45% | +32.19 | +30.97 | +1% | 24.84 | ja | 23 s | +3.83 / +28.35 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3271 (17) | 62% | +9.04 | +8.90 | +9% | 23.76 | ja | 4 s | +3.20 / +5.84 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6025 (43) | 38% | +7.27 | +6.26 | +1% | 22.33 | ja | 19 s | +4.49 / +2.78 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2482 (48) | 60% | +6.94 | +6.67 | +7% | 22.09 | ja | 4 s | +2.60 / +4.34 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2168 (21) | 50% | +2.54 | +1.62 | +0% | 17.71 | ja | 10 s | +0.62 / +1.92 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2483 (44) | 44% | +28.45 | +26.30 | +1% | 16.53 | ja | 25 s | +14.98 / +13.47 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1876 (13) | 48% | +4.93 | +3.71 | +0% | 15.3 | ja | 37 s | +2.48 / +2.45 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1751 (11) | 51% | +9.13 | +8.39 | +1% | 14.59 | ja | 37 s | +0.90 / +8.23 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1331 (27) | 44% | +3.70 | +3.28 | +3% | 14.23 | ja | 61 s | +1.42 / +2.28 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 507 (1) | 63% | +12.22 | +11.39 | +10% | 13.85 | ja | 1 s | +6.11 / +6.11 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1772 (6) | 55% | +1.64 | +1.53 | +2% | 12.74 | ja | 10 s | +0.42 / +1.21 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1097 (4) | 42% | +10.89 | +9.85 | +3% | 11.88 | ja | 28 s | +6.08 / +4.81 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1834 (23) | 52% | +3.07 | +3.02 | +10% | 11.78 | ja | 4 s | +1.43 / +1.65 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2083 (2) | 48% | +5.33 | +4.88 | +1% | 11.39 | nee | 7 s | +3.02 / +2.31 |
| 15 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 82 (1) | 56% | +27.83 | +25.60 | +37% | 11.39 | ja | 53 s | +12.80 / +15.03 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 575 (0) | 48% | +7.71 | +6.94 | +4% | 11.37 | ja | 1 s | +5.54 / +2.17 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 82 (1) | 58% | +32.61 | +29.59 | +42% | 11.16 | ja | 51 s | +18.91 / +13.70 |
| 18 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 339 (3) | 59% | +11.30 | +9.32 | +5% | 10.85 | ja | 8 s | +3.65 / +7.65 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.75 | ja | 8 s | +124.83 / +204.81 |
| 20 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 725 (5) | 67% | +3.16 | +2.92 | +1% | 10.07 | ja | 11 s | +2.39 / +0.77 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.75 | ja | 8 s | +124.83 / +204.81 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.63 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.85 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.91 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 245 (0) | 63% | +133.88 | +99.93 | +15% | 8.34 | ja | 15 s | +48.76 / +85.12 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.19 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 28 (6) | 75% | +83.41 | +71.57 | +35% | 5.43 | nee | 6 s | +13.73 / +69.68 |
| 8 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.32 | nee | 108 s | +34.55 / +25.67 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 177 (1) | 77% | +58.94 | +55.34 | +13% | 7.4 | ja | 9 s | +31.04 / +27.90 |
| 10 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 78 (4) | 95% | +51.13 | +48.51 | +21% | 5.97 | nee | 16 s | +22.00 / +29.13 |
| 11 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.57 | nee | 2 min | +0.00 / +46.59 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 90 (0) | 78% | +44.16 | +39.17 | +13% | 5.39 | nee | 25 s | +19.61 / +24.55 |
| 13 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 102 (14) | 55% | +43.01 | +38.21 | +15% | 6.09 | nee | 88 s | +21.00 / +22.01 |
| 14 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 150 (8) | 57% | +41.96 | +34.76 | +13% | 6.59 | nee | 106 s | +31.47 / +10.49 |
| 15 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.92 | ja | 6 min | +9.85 / +29.47 |
| 16 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | -0.24 / +38.62 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 82 (1) | 58% | +32.61 | +29.59 | +42% | 11.16 | ja | 51 s | +18.91 / +13.70 |
| 18 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5969 (77) | 45% | +32.19 | +30.97 | +1% | 24.84 | ja | 23 s | +3.83 / +28.35 |
| 19 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2483 (44) | 44% | +28.45 | +26.30 | +1% | 16.53 | ja | 25 s | +14.98 / +13.47 |
| 20 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 154 (0) | 48% | +28.45 | +24.72 | +15% | 7.23 | ja | 13 s | +16.94 / +11.51 |

## Geluk-toets

Populatie: 7118 wallets met ≥ 20 posities, 84 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 16.6 | 4.54 | 5.45 |
| #10 | 10.15 | 3.4 | 3.72 |
| #20 | 7.82 | 3.1 | 3.29 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.45): **56**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 14398 | 49% | +6.2% | -0.2% | +134.71 |
| top 20 op winst (A) | 18/20 | 1697 | 52% | +6.5% | +1.0% | +469.22 |
| alle wallets | – | 374009 | 32% | -10.5% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.0% / +1.2% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3531): ρ = 0.534. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 118

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14398 | 30% | -11.2% | -7.4% | -324.04 |
| 2 s | 14398 | 24% | -14.5% | -9.0% | -417.93 |
| 10 s | 14398 | 22% | -15.5% | -8.9% | -447.37 |
| 60 s | 14398 | 18% | -19.3% | -8.2% | -555.70 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 310

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 36497 | 31% | -11.1% | -7.1% | -806.93 |
| 2 s | 36497 | 25% | -14.0% | -8.7% | -1023.24 |
| 10 s | 36497 | 23% | -14.9% | -8.4% | -1090.10 |
| 60 s | 36497 | 18% | -18.2% | -7.6% | -1330.51 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 146

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 9706 | 32% | -2.3% | -5.7% | -44.62 |
| 2 s | 9706 | 27% | -5.8% | -7.2% | -112.73 |
| 10 s | 9706 | 26% | -6.3% | -7.0% | -123.07 |
| 60 s | 9706 | 23% | -6.3% | -5.8% | -122.20 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
