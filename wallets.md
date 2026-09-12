# Wallet-analyse pump.fun — 2026-09-12 14:15 UTC

## Kort antwoord

- Geluk-toets: 48 van 6399 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=15.16, geluk-grens 5.56).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.4% per positie (alle wallets: -12.3%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -10.9%, 2 s: -13.7%, 10 s: -14.6%, 60 s: -18.0% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 14:13 UTC (48.4 uur), helft A/B-grens: 2026-09-11 14:01 UTC
- 4144083 trades, 33857 tokens, 168023 wallets, 1263478 posities (802052 geopend vanaf ≥ $7k, 461426 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 110003
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8525 | 4993 | +30.77 | -25.73 | +453.61 | 20314.99 | 11884 | +2036.43 |
| dev | 1586 | 4946 | +1136.57 | -570.02 | +820.90 | 4827.95 | 10023 | +782.87 |
| swing | 1373 | 15456 | -618.68 | -870.11 | -237.87 | 61.16 | 6021 | +62.83 |
| bot_hf | 2587 | 175114 | +139.67 | -1150.60 | +4587.58 | 11267.64 | 184119 | +6250.28 |
| incidenteel | 130110 | 185100 | -6554.24 | -12309.85 | +12165.31 | 8524.72 | 105995 | +7248.54 |
| scalper | 23842 | 416443 | -12106.31 | -15372.34 | +13753.36 | 8399.83 | 143384 | +1622.25 |

Wallets met ≥ 10 posities: 13894, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -17972.23 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5394 (72) | 45% | +28.32 | +27.09 | +1% | 24.08 | ja | 23 s | +2.13 / +26.19 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2875 (16) | 62% | +7.56 | +7.42 | +9% | 22.21 | ja | 4 s | +2.57 / +4.99 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5568 (42) | 38% | +6.98 | +5.97 | +1% | 21.7 | ja | 19 s | +4.10 / +2.88 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2176 (42) | 59% | +5.63 | +5.37 | +7% | 20.48 | ja | 4 s | +2.10 / +3.53 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1913 (19) | 51% | +4.99 | +4.47 | +1% | 17.52 | ja | 10 s | +0.99 / +3.99 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2307 (41) | 45% | +24.72 | +22.57 | +1% | 16.27 | ja | 24 s | +8.16 / +16.56 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1670 (15) | 48% | +5.92 | +4.70 | +1% | 14.84 | ja | 37 s | +1.50 / +4.42 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1621 (13) | 51% | +7.71 | +6.97 | +1% | 14.07 | ja | 36 s | +0.93 / +6.78 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1187 (28) | 44% | +3.12 | +2.70 | +3% | 13.7 | ja | 61 s | +1.41 / +1.70 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 459 (1) | 63% | +11.88 | +11.04 | +10% | 13.62 | ja | 1 s | +4.34 / +7.53 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1615 (4) | 55% | +1.24 | +1.15 | +1% | 12.4 | ja | 10 s | +0.26 / +0.98 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1041 (3) | 43% | +11.06 | +10.02 | +3% | 11.77 | ja | 31 s | +5.53 / +5.53 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1611 (19) | 52% | +2.79 | +2.73 | +10% | 11.53 | ja | 4 s | +0.97 / +1.82 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1770 (2) | 49% | +5.68 | +5.24 | +1% | 11.11 | nee | 7 s | +1.39 / +4.30 |
| 15 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 510 (0) | 49% | +7.95 | +7.19 | +5% | 10.97 | ja | 1 s | +1.65 / +6.30 |
| 16 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.89 | ja | 8 s | +3.65 / +7.62 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 61 (0) | 64% | +25.39 | +23.39 | +46% | 10.38 | ja | 54 s | +13.47 / +11.92 |
| 18 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 644 (5) | 68% | +3.73 | +3.48 | +2% | 10.08 | ja | 11 s | +2.68 / +1.05 |
| 19 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 740 (7) | 48% | +5.60 | +5.23 | +2% | 9.93 | ja | 70 s | +3.65 / +1.94 |
| 20 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 931 (35) | 45% | +8.19 | +6.85 | +2% | 9.92 | ja | 2 min | +7.35 / +0.84 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 40 (0) | 80% | +295.41 | +270.49 | +77% | 10.28 | ja | 8 s | -0.81 / +296.22 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.67 | nee | 12 s | +102.20 / +190.01 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.94 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 212 (0) | 61% | +120.64 | +86.68 | +16% | 7.97 | ja | 15 s | +38.70 / +81.94 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.21 | nee | 102 s | +60.24 / +37.88 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 20 (5) | 75% | +58.99 | +47.15 | +32% | 4.57 | nee | 6 s | +10.52 / +48.47 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 167 (1) | 77% | +55.09 | +51.48 | +13% | 7.39 | ja | 9 s | +27.70 / +27.39 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 64 (3) | 95% | +37.60 | +35.49 | +19% | 5.03 | nee | 16 s | +14.34 / +23.26 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 140 (8) | 56% | +37.26 | +30.06 | +12% | 6.13 | nee | 112 s | +31.64 / +5.62 |
| 14 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 22 (4) | 77% | +32.42 | +25.52 | +64% | 7.73 | ja | 6 min | +5.84 / +26.58 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 90 (14) | 50% | +29.14 | +24.34 | +11% | 5.16 | nee | 88 s | +15.32 / +13.82 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 70 (0) | 77% | +28.43 | +26.10 | +11% | 4.86 | nee | 24 s | +14.67 / +13.76 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5394 (72) | 45% | +28.32 | +27.09 | +1% | 24.08 | ja | 23 s | +2.13 / +26.19 |
| 18 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.2 | ja | 13 s | +18.76 / +8.71 |
| 20 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 31 (2) | 61% | +26.71 | +20.55 | +43% | 7.17 | ja | 112 s | +10.06 / +16.65 |

## Geluk-toets

Populatie: 6399 wallets met ≥ 20 posities, 95 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 15.16 | 4.41 | 5.56 |
| #10 | 9.53 | 3.34 | 3.58 |
| #20 | 7.46 | 3.04 | 3.2 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.56): **48**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 14947 | 49% | +5.4% | -0.2% | +131.79 |
| top 20 op winst (A) | 19/20 | 853 | 57% | +8.8% | +2.7% | +219.82 |
| alle wallets | – | 390763 | 31% | -12.3% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.6% / +1.2% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3322): ρ = 0.499. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 127

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 14947 | 30% | -10.9% | -7.0% | -325.22 |
| 2 s | 14947 | 25% | -13.7% | -8.6% | -409.02 |
| 10 s | 14947 | 22% | -14.6% | -8.6% | -438.10 |
| 60 s | 14947 | 19% | -18.0% | -7.8% | -536.87 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 328

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 34423 | 32% | -10.5% | -7.0% | -720.84 |
| 2 s | 34423 | 26% | -13.2% | -8.5% | -908.72 |
| 10 s | 34423 | 23% | -14.2% | -8.3% | -980.82 |
| 60 s | 34423 | 20% | -17.3% | -7.5% | -1191.75 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 97

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6498 | 32% | -1.5% | -5.2% | -19.05 |
| 2 s | 6498 | 27% | -5.3% | -6.8% | -68.48 |
| 10 s | 6498 | 25% | -6.3% | -6.7% | -81.86 |
| 60 s | 6498 | 22% | -6.2% | -5.8% | -81.14 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
