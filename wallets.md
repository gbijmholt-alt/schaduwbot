# Wallet-analyse pump.fun — 2026-09-13 06:47 UTC

## Kort antwoord

- Geluk-toets: 62 van 7605 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=17.22, geluk-grens 5.46).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.3% per positie (alle wallets: -9.4%; 16 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -12.5%, 2 s: -15.9%, 10 s: -17.2%, 60 s: -21.3% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-13 06:45 UTC (65.0 uur), helft A/B-grens: 2026-09-11 22:17 UTC
- 5575165 trades, 49601 tokens, 194340 wallets, 1689425 posities (930082 geopend vanaf ≥ $7k, 759343 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 127631
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 9954 | 5744 | -42.96 | -116.88 | +436.12 | 21145.97 | 19775 | +2839.60 |
| dev | 1981 | 5871 | +1378.56 | -762.43 | +1183.16 | 5008.79 | 13684 | +1060.52 |
| swing | 1652 | 18820 | -846.34 | -1154.68 | -400.39 | 72.28 | 9842 | +47.52 |
| bot_hf | 2976 | 209145 | +85.50 | -1949.04 | +5141.61 | 13268.81 | 271759 | +7472.10 |
| incidenteel | 151192 | 199580 | -6427.08 | -12538.52 | +18292.00 | 8739.04 | 174956 | +8762.56 |
| scalper | 26585 | 490922 | -14594.49 | -17795.47 | +17709.37 | 8740.69 | 269327 | +1941.26 |

Wallets met ≥ 10 posities: 16090, waarvan winstgevend: 20%. De top 1% winnaars pakt 36% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -20446.81 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6434 (79) | 45% | +38.58 | +37.35 | +1% | 25.83 | ja | 23 s | +11.34 / +27.24 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 3697 (20) | 62% | +11.21 | +11.08 | +9% | 24.62 | ja | 4 s | +4.99 / +6.23 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2823 (57) | 59% | +7.46 | +7.19 | +7% | 23.21 | ja | 4 s | +3.49 / +3.97 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 6455 (53) | 38% | +6.59 | +5.58 | +0% | 22.73 | ja | 19 s | +3.98 / +2.60 |
| 5 | [9gPK…9sfB](https://solscan.io/account/9gPKLV4DdUupHDXowMVYgA7kBKsU1GEdE35KWEjZ9sfB) | bot_hf | 2418 (24) | 50% | +1.63 | +0.71 | +0% | 18.4 | ja | 10 s | +0.24 / +1.39 |
| 6 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2619 (46) | 45% | +32.75 | +30.61 | +1% | 16.86 | ja | 24 s | +13.82 / +18.93 |
| 7 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1444 (30) | 44% | +4.01 | +3.59 | +3% | 14.84 | ja | 61 s | +1.74 / +2.27 |
| 8 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1816 (11) | 51% | +8.31 | +7.57 | +1% | 14.66 | ja | 37 s | +3.66 / +4.65 |
| 9 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 549 (1) | 62% | +13.15 | +12.32 | +10% | 14.09 | ja | 1 s | +7.20 / +5.95 |
| 10 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 1893 (6) | 55% | +2.03 | +1.93 | +2% | 13.27 | ja | 10 s | +0.59 / +1.44 |
| 11 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 2100 (25) | 53% | +3.63 | +3.56 | +10% | 12.98 | ja | 4 s | +1.97 / +1.66 |
| 12 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 1202 (4) | 41% | +11.95 | +10.91 | +3% | 12.24 | ja | 25 s | +7.61 / +4.35 |
| 13 | [2WJT…fwMo](https://solscan.io/account/2WJTQ6q91HBZLqHuVuRLgsiGQV8yCgVKtzaLX4HBfwMo) | bot_hf | 2371 (2) | 48% | +5.39 | +4.95 | +1% | 11.94 | ja | 7 s | +3.91 / +1.49 |
| 14 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 84 (1) | 56% | +30.66 | +27.47 | +39% | 11.9 | ja | 53 s | +13.38 / +17.27 |
| 15 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 84 (1) | 58% | +34.24 | +31.22 | +43% | 11.84 | ja | 51 s | +18.14 / +16.10 |
| 16 | [3dtd…FmPk](https://solscan.io/account/3dtdzzPYR1EbAr8AqHsgB53Seqe3Jefo4fqVznMbFmPk) | bot_hf | 632 (0) | 49% | +8.41 | +7.64 | +4% | 11.81 | ja | 1 s | +6.59 / +1.81 |
| 17 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 352 (3) | 58% | +11.31 | +9.34 | +5% | 10.89 | ja | 8 s | +3.40 / +7.91 |
| 18 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 767 (5) | 68% | +4.25 | +3.97 | +2% | 10.79 | ja | 10 s | +3.13 / +1.12 |
| 19 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 20 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 727 (6) | 70% | +5.13 | +4.87 | +2% | 10.66 | ja | 10 s | +3.07 / +2.07 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 45 (0) | 82% | +329.64 | +304.71 | +76% | 10.73 | ja | 8 s | +269.26 / +60.38 |
| 2 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 9 (0) | 100% | +292.21 | +255.86 | +202% | 15.6 | nee | 12 s | +206.40 / +85.81 |
| 3 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 15 (1) | 93% | +158.23 | +139.77 | +128% | 11.83 | nee | 2 min | +67.53 / +90.70 |
| 4 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | vroege_houder | 9 (0) | 89% | +140.38 | +94.69 | +214% | 11.89 | nee | 64 s | +0.00 / +140.38 |
| 5 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 257 (0) | 64% | +139.59 | +105.63 | +15% | 8.47 | ja | 15 s | +65.73 / +73.86 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 12 (0) | 67% | +98.12 | +72.89 | +123% | 9.18 | nee | 102 s | +60.24 / +37.88 |
| 7 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | bot_hf | 30 (7) | 73% | +86.06 | +74.22 | +34% | 5.42 | nee | 6 s | +21.58 / +64.48 |
| 8 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 185 (1) | 76% | +62.33 | +58.72 | +13% | 7.52 | ja | 9 s | +39.35 / +22.98 |
| 9 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 12 (0) | 67% | +60.22 | +43.13 | +82% | 7.3 | nee | 108 s | +34.55 / +25.67 |
| 10 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 6 (1) | 83% | +52.88 | +19.83 | +174% | 6.78 | nee | 9 s | +9.56 / +43.32 |
| 11 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | scalper | 81 (3) | 96% | +52.57 | +49.96 | +21% | 6.07 | nee | 16 s | +24.66 / +27.91 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 94 (1) | 78% | +46.83 | +41.84 | +13% | 5.66 | nee | 26 s | +22.83 / +24.00 |
| 13 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 15 (1) | 53% | +46.59 | +21.03 | +40% | 4.56 | nee | 2 min | +27.39 / +19.20 |
| 14 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 110 (16) | 55% | +44.84 | +40.03 | +14% | 6.0 | nee | 96 s | +28.72 / +16.12 |
| 15 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 151 (9) | 56% | +41.96 | +34.76 | +13% | 6.55 | nee | 106 s | +28.35 / +13.62 |
| 16 | [BRoG…nmB6](https://solscan.io/account/BRoGEZL1gfFQUC5Jb6BYhPeANoDqzMz3MHBZ7SPXnmB6) | scalper | 6 (1) | 67% | +39.35 | +6.18 | +52% | 1.96 | nee | 97 s | +0.00 / +39.35 |
| 17 | [6yVb…JBqm](https://solscan.io/account/6yVb4pxNwDfr6rovwNnBg3SyKSvDcHGD4WdFPN1JJBqm) | scalper | 23 (3) | 83% | +39.32 | +32.43 | +75% | 8.91 | ja | 6 min | +20.67 / +18.65 |
| 18 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 6434 (79) | 45% | +38.58 | +37.35 | +1% | 25.83 | ja | 23 s | +11.34 / +27.24 |
| 19 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | dev | 8 (0) | 88% | +38.38 | +29.46 | +59% | 3.31 | nee | 4 s | +35.01 / +3.37 |
| 20 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 13 (0) | 69% | +34.82 | +20.27 | +67% | 5.31 | nee | 12 s | +21.18 / +13.64 |

## Geluk-toets

Populatie: 7605 wallets met ≥ 20 posities, 78 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 17.22 | 4.47 | 5.46 |
| #10 | 10.19 | 3.42 | 3.64 |
| #20 | 8.32 | 3.15 | 3.28 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.46): **62**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 13655 | 49% | +6.3% | -0.1% | +189.91 |
| top 20 op winst (A) | 19/20 | 555 | 64% | +16.4% | +7.2% | +308.16 |
| alle wallets | – | 335470 | 33% | -9.4% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -6.7% / +2.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3397): ρ = 0.49. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 108

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 13655 | 29% | -12.5% | -7.9% | -342.02 |
| 2 s | 13655 | 23% | -15.9% | -9.6% | -433.91 |
| 10 s | 13655 | 21% | -17.2% | -9.4% | -470.23 |
| 60 s | 13655 | 18% | -21.3% | -9.1% | -580.89 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 328

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 38512 | 31% | -11.5% | -7.2% | -884.25 |
| 2 s | 38512 | 25% | -14.5% | -8.8% | -1116.46 |
| 10 s | 38512 | 22% | -15.5% | -8.5% | -1196.40 |
| 60 s | 38512 | 18% | -19.2% | -7.7% | -1477.51 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 108

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 7515 | 33% | -1.7% | -5.2% | -25.82 |
| 2 s | 7515 | 27% | -5.3% | -6.7% | -79.82 |
| 10 s | 7515 | 24% | -6.4% | -6.7% | -96.23 |
| 60 s | 7515 | 22% | -6.5% | -5.8% | -97.18 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
