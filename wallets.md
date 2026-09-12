# Wallet-analyse pump.fun — 2026-09-12 14:32 UTC

## Kort antwoord

- Geluk-toets: 55 van 6434 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=15.38, geluk-grens 5.15).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +5.5% per positie (alle wallets: -12.2%; 18 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -10.8%, 2 s: -13.7%, 10 s: -14.6%, 60 s: -17.9% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-12 14:30 UTC (48.7 uur), helft A/B-grens: 2026-09-11 14:09 UTC
- 4173971 trades, 34220 tokens, 168398 wallets, 1272407 posities (805880 geopend vanaf ≥ $7k, 466527 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 110278
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 8554 | 5004 | +28.80 | -27.74 | +449.07 | 20339.15 | 11987 | +2059.24 |
| dev | 1599 | 4987 | +1137.13 | -584.42 | +809.29 | 4828.16 | 10134 | +774.31 |
| swing | 1379 | 15532 | -622.19 | -875.05 | -249.36 | 61.18 | 6045 | +63.15 |
| bot_hf | 2592 | 176251 | +139.72 | -1151.02 | +4578.59 | 11306.63 | 186244 | +6204.23 |
| incidenteel | 130340 | 185268 | -6559.88 | -12322.79 | +11906.66 | 8517.86 | 106786 | +7282.18 |
| scalper | 23934 | 418838 | -12184.10 | -15471.64 | +14227.35 | 8421.22 | 145331 | +1643.57 |

Wallets met ≥ 10 posities: 13952, waarvan winstgevend: 20%. De top 1% winnaars pakt 37% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -18060.51 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5413 (73) | 45% | +28.99 | +27.77 | +1% | 24.18 | ja | 23 s | +1.51 / +27.48 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 2894 (18) | 62% | +7.63 | +7.50 | +9% | 22.43 | ja | 4 s | +2.63 / +5.01 |
| 3 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 5599 (41) | 38% | +7.05 | +6.04 | +1% | 21.82 | ja | 19 s | +4.10 / +2.95 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2192 (43) | 59% | +5.55 | +5.29 | +7% | 20.54 | ja | 4 s | +2.10 / +3.45 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 1929 (19) | 51% | +5.42 | +4.90 | +1% | 17.62 | ja | 10 s | +1.17 / +4.25 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2319 (42) | 45% | +23.57 | +21.42 | +1% | 16.2 | ja | 24 s | +7.58 / +15.98 |
| 7 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 1680 (13) | 48% | +6.14 | +4.93 | +1% | 14.94 | ja | 37 s | +1.00 / +5.14 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1629 (14) | 51% | +7.72 | +6.99 | +1% | 14.12 | ja | 36 s | +0.77 / +6.95 |
| 9 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1194 (27) | 44% | +3.10 | +2.68 | +3% | 13.71 | ja | 61 s | +1.41 / +1.69 |
| 10 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 462 (1) | 63% | +11.70 | +10.86 | +10% | 13.65 | ja | 1 s | +4.35 / +7.34 |
| 11 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1623 (5) | 55% | +1.24 | +1.15 | +1% | 12.43 | ja | 10 s | +0.33 / +0.91 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1042 (3) | 43% | +11.02 | +9.98 | +3% | 11.77 | ja | 31 s | +5.34 / +5.69 |
| 13 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 1623 (20) | 52% | +2.85 | +2.79 | +10% | 11.76 | ja | 4 s | +0.95 / +1.90 |
| 14 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 1785 (2) | 49% | +5.31 | +4.86 | +1% | 11.11 | ja | 7 s | +1.55 / +3.76 |
| 15 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 330 (2) | 58% | +11.27 | +9.29 | +5% | 10.89 | ja | 8 s | +3.65 / +7.62 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 511 (0) | 49% | +7.94 | +7.18 | +4% | 10.89 | ja | 1 s | +1.65 / +6.29 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 63 (1) | 62% | +24.75 | +22.76 | +43% | 10.12 | ja | 54 s | +13.47 / +11.29 |
| 18 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 644 (5) | 68% | +3.73 | +3.48 | +2% | 10.1 | ja | 11 s | +2.68 / +1.05 |
| 19 | [qBv7…NnQp](https://solscan.io/account/qBv7hMi5EeBopV9QpgLvCzjHFFgYeypkrEBuYQ2NnQp) | bot_hf | 286 (15) | 50% | +0.78 | +0.68 | +7% | 9.92 | ja | 7 s | +0.26 / +0.52 |
| 20 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 940 (39) | 45% | +7.43 | +6.09 | +2% | 9.88 | ja | 2 min | +7.29 / +0.14 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 40 (0) | 80% | +295.41 | +270.49 | +77% | 10.29 | ja | 8 s | -0.81 / +296.22 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.67 | nee | 12 s | +102.20 / +190.01 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.88 | nee | 2 min | +0.00 / +158.23 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.94 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 212 (0) | 61% | +120.64 | +86.68 | +16% | 7.98 | ja | 15 s | +38.70 / +81.94 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.21 | nee | 102 s | +60.24 / +37.88 |
| 7 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.33 | nee | 108 s | +34.55 / +25.67 |
| 8 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 20 (5) | 75% | +58.99 | +47.15 | +32% | 4.56 | nee | 6 s | +10.52 / +48.47 |
| 9 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 167 (1) | 77% | +55.09 | +51.48 | +13% | 7.4 | ja | 9 s | +27.36 / +27.73 |
| 10 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.58 | nee | 2 min | +0.00 / +46.59 |
| 11 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.32 | nee | 4 s | +0.33 / +38.05 |
| 12 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 64 (3) | 95% | +37.60 | +35.49 | +19% | 5.03 | nee | 16 s | +14.34 / +23.26 |
| 13 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 144 (9) | 56% | +36.95 | +29.75 | +12% | 6.04 | nee | 101 s | +31.59 / +5.36 |
| 14 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 22 (3) | 82% | +35.79 | +28.90 | +71% | 8.26 | ja | 7 min | +5.84 / +29.95 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 90 (13) | 51% | +29.70 | +24.89 | +12% | 5.2 | nee | 89 s | +15.43 / +14.27 |
| 16 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 71 (0) | 78% | +29.27 | +26.94 | +11% | 4.93 | nee | 24 s | +14.67 / +14.60 |
| 17 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 5413 (73) | 45% | +28.99 | +27.77 | +1% | 24.18 | ja | 23 s | +1.51 / +27.48 |
| 18 | [HvSe…J8jE](https://solscan.io/account/HvSezmMEnEQiUoBuHvm5YnbWFPVZM5Svg6D4PrA2J8jE) | scalper | 19 (0) | 74% | +27.72 | +20.69 | +21% | 3.22 | nee | 28 s | +6.71 / +21.01 |
| 19 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | bot_hf | 149 (0) | 48% | +27.47 | +23.75 | +15% | 7.2 | ja | 13 s | +18.76 / +8.71 |
| 20 | [93kk…2uT9](https://solscan.io/account/93kk52HkrH5pHEPyb2KM62mP4cWA1N5DaSgBgDzA2uT9) | scalper | 31 (2) | 61% | +26.71 | +20.55 | +43% | 7.17 | ja | 112 s | +10.06 / +16.65 |

## Geluk-toets

Populatie: 6434 wallets met ≥ 20 posities, 94 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 15.38 | 4.34 | 5.15 |
| #10 | 9.48 | 3.34 | 3.54 |
| #20 | 7.48 | 3.03 | 3.21 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.15): **55**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 15001 | 49% | +5.5% | -0.2% | +132.48 |
| top 20 op winst (A) | 18/20 | 849 | 57% | +8.6% | +2.5% | +212.38 |
| alle wallets | – | 392086 | 31% | -12.2% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -7.1% / +1.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3337): ρ = 0.496. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 131

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 15001 | 30% | -10.8% | -7.0% | -325.29 |
| 2 s | 15001 | 25% | -13.7% | -8.6% | -410.24 |
| 10 s | 15001 | 23% | -14.6% | -8.6% | -438.38 |
| 60 s | 15001 | 19% | -17.9% | -7.8% | -537.49 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 340

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 34158 | 31% | -10.6% | -7.0% | -726.70 |
| 2 s | 34158 | 25% | -13.4% | -8.5% | -917.19 |
| 10 s | 34158 | 23% | -14.4% | -8.4% | -985.10 |
| 60 s | 34158 | 19% | -17.6% | -7.6% | -1202.18 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 97

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 6522 | 32% | -1.5% | -5.2% | -18.89 |
| 2 s | 6522 | 27% | -5.3% | -6.8% | -68.85 |
| 10 s | 6522 | 25% | -6.3% | -6.7% | -82.31 |
| 60 s | 6522 | 22% | -6.2% | -5.8% | -81.56 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
