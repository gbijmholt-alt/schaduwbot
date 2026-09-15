# Wallet-analyse pump.fun — 2026-09-15 09:52 UTC

## Kort antwoord

- Geluk-toets: 75 van 7717 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=31.27, geluk-grens 5.34).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.1% per positie (alle wallets: -11.1%; 20 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.5%, 2 s: -15.0%, 10 s: -15.8%, 60 s: -18.7% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 09:39 UTC → 2026-09-15 09:40 UTC (72.0 uur), helft A/B-grens: 2026-09-13 21:39 UTC
- 7325165 trades, 76140 tokens, 210371 wallets, 2260379 posities (913473 geopend vanaf ≥ $7k, 1346906 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 125414
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7356 | 3206 | +148.32 | +92.41 | +389.28 | 7503.98 | 17991 | +1872.52 |
| dev | 2198 | 4549 | +2199.11 | +48.00 | +2796.20 | 40.23 | 16750 | +2411.75 |
| bot_hf | 3222 | 224121 | +882.70 | -286.16 | +5351.80 | 9040.11 | 401785 | +6946.81 |
| swing | 2099 | 19616 | -1061.38 | -1327.98 | -27.47 | 47.63 | 19845 | +31.43 |
| incidenteel | 169925 | 175725 | -3944.34 | -6910.55 | +36785.51 | 1877.93 | 340862 | +15880.75 |
| scalper | 25571 | 486256 | -13023.91 | -16267.52 | +23551.98 | 1162.35 | 549673 | +3306.20 |

Wallets met ≥ 10 posities: 16402, waarvan winstgevend: 22%. De top 1% winnaars pakt 44% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14799.50 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.44 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7689 (99) | 46% | +66.52 | +65.39 | +2% | 25.65 | ja | 26 s | +25.89 / +40.62 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4132 (19) | 61% | +9.85 | +9.58 | +7% | 23.7 | ja | 4 s | +5.87 / +3.98 |
| 4 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2881 (55) | 58% | +4.56 | +4.34 | +4% | 22.71 | ja | 4 s | +2.68 / +1.88 |
| 5 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7443 (67) | 40% | +14.26 | +13.26 | +1% | 22.65 | ja | 18 s | +4.05 / +10.20 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.68 | ja | 2 min | +112.67 / +421.81 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 452 (78) | 55% | +0.48 | +0.46 | +28% | 19.25 | ja | 23 s | +0.11 / +0.38 |
| 8 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2825 (44) | 49% | +88.83 | +85.60 | +3% | 17.18 | ja | 19 s | +31.35 / +57.48 |
| 9 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 73 (0) | 92% | +817.34 | +777.44 | +67% | 17.05 | ja | 7 s | +285.29 / +532.05 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.12 | ja | 2 min | +94.54 / +274.04 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3791 (60) | 37% | +58.79 | +51.83 | +2% | 15.59 | ja | 29 s | +18.52 / +40.27 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2377 (14) | 50% | +12.94 | +11.53 | +1% | 15.31 | ja | 46 s | +7.72 / +5.22 |
| 13 | [7evu…tqbX](https://solscan.io/account/7evudm7mkommXaFbyrC9AoGNfkqcTdUGZAU25ZTytqbX) | bot_hf | 2623 (15) | 49% | +12.96 | +12.14 | +3% | 14.41 | ja | 30 s | +0.71 / +12.25 |
| 14 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1984 (89) | 45% | +10.52 | +6.61 | +0% | 13.23 | ja | 42 s | +0.52 / +9.99 |
| 15 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 24 (2) | 83% | +27.30 | +19.47 | +166% | 13.03 | ja | 106 s | +10.48 / +16.82 |
| 16 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1825 (9) | 40% | +11.43 | +9.44 | +2% | 13.01 | ja | 21 s | +2.44 / +8.98 |
| 17 | [CrAz…MCoj](https://solscan.io/account/CrAzYtsUvb4F1L8uwhGZXkMhRiMSW1P7qp4FA4QFMCoj) | scalper | 800 (159) | 48% | +0.62 | +0.60 | +19% | 12.37 | ja | 30 s | +0.05 / +0.57 |
| 18 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1479 (27) | 44% | +2.42 | +2.15 | +2% | 12.15 | ja | 58 s | +1.83 / +0.59 |
| 19 | [2k2j…UJf9](https://solscan.io/account/2k2jJVet1SeAKvVSbvd8pZbqpaLcbMgRmYx8EhNTUJf9) | bot_hf | 1630 (3) | 52% | +6.09 | +5.37 | +1% | 12.08 | ja | 47 s | +6.08 / +0.01 |
| 20 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 23 (2) | 83% | +18.12 | +12.77 | +81% | 11.37 | ja | 74 s | +9.35 / +8.77 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.44 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 73 (0) | 92% | +817.34 | +777.44 | +67% | 17.05 | ja | 7 s | +285.29 / +532.05 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.68 | ja | 2 min | +112.67 / +421.81 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.12 | ja | 2 min | +94.54 / +274.04 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 53 (1) | 60% | +188.30 | +171.36 | +40% | 8.4 | ja | 3 min | +41.26 / +147.04 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 350 (10) | 57% | +146.04 | +112.08 | +11% | 7.72 | ja | 16 s | +92.04 / +53.99 |
| 7 | [gVDX…dAkx](https://solscan.io/account/gVDXhoGbePACvSqN7CZBtQXFW9eyJwsgudPEwSydAkx) | dev | 9 (1) | 89% | +145.19 | +118.40 | +85% | 6.94 | nee | 9 s | +38.53 / +106.66 |
| 8 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 10 (1) | 90% | +109.84 | +81.15 | +139% | 9.86 | nee | 4 min | +0.00 / +109.84 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 69 (0) | 68% | +106.20 | +87.44 | +39% | 8.07 | ja | 11 s | +29.16 / +77.04 |
| 10 | [14W6…CGJp](https://solscan.io/account/14W6L6zVVBbstgTktiR7Qv6z75yPcXij3aS7mqtHCGJp) | dev | 10 (2) | 80% | +92.66 | +64.53 | +18% | 2.96 | nee | 118 s | +0.00 / +92.66 |
| 11 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 31 (5) | 74% | +90.39 | +80.47 | +42% | 6.0 | ja | 34 s | +84.67 / +5.72 |
| 12 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2825 (44) | 49% | +88.83 | +85.60 | +3% | 17.18 | ja | 19 s | +31.35 / +57.48 |
| 13 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 11 (0) | 100% | +88.31 | +55.26 | +124% | 8.66 | nee | 7 s | +44.68 / +43.63 |
| 14 | [76bg…Rnzh](https://solscan.io/account/76bg6fHvkavukBNggSxTpJX9quDEWTsfmH42VFsRnzh) | bot_hf | 10 (1) | 90% | +82.81 | +66.29 | +124% | 9.41 | nee | 9 s | +8.25 / +74.56 |
| 15 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 9 (3) | 56% | +77.34 | +57.44 | +104% | 4.27 | nee | 7 s | +14.46 / +62.87 |
| 16 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | bot_hf | 10 (0) | 100% | +73.80 | +62.99 | +73% | 5.39 | nee | 6 s | +10.80 / +62.99 |
| 17 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | bot_hf | 48 (2) | 85% | +73.17 | +64.58 | +26% | 4.92 | nee | 14 s | +16.02 / +57.14 |
| 18 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 145 (0) | 76% | +73.11 | +68.63 | +20% | 8.78 | ja | 91 s | +31.78 / +41.34 |
| 19 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.09 | nee | 33 s | +50.13 / +19.03 |
| 20 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 160 (1) | 77% | +68.62 | +65.68 | +16% | 7.43 | ja | 9 s | +19.36 / +49.26 |

## Geluk-toets

Populatie: 7717 wallets met ≥ 20 posities, 76 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 31.27 | 4.52 | 5.34 |
| #10 | 14.07 | 3.48 | 3.75 |
| #20 | 9.23 | 3.17 | 3.32 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.34): **75**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 20241 | 48% | +6.1% | -0.2% | +2589.30 |
| top 20 op winst (A) | 20/20 | 7429 | 49% | +6.2% | +0.0% | +2979.99 |
| alle wallets | – | 542249 | 31% | -11.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +2.0% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3601): ρ = 0.522. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 228

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20241 | 29% | -11.5% | -7.1% | -466.53 |
| 2 s | 20241 | 24% | -15.0% | -8.9% | -605.67 |
| 10 s | 20241 | 23% | -15.8% | -8.7% | -640.39 |
| 60 s | 20241 | 20% | -18.7% | -7.6% | -756.53 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 697

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 42211 | 28% | -12.5% | -8.2% | -1057.89 |
| 2 s | 42211 | 24% | -15.7% | -10.0% | -1327.14 |
| 10 s | 42211 | 22% | -16.8% | -9.8% | -1420.27 |
| 60 s | 42211 | 20% | -19.5% | -8.5% | -1648.67 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 62

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 4000 | 36% | +2.5% | -5.6% | +19.60 |
| 2 s | 4000 | 30% | -6.0% | -8.2% | -47.93 |
| 10 s | 4000 | 29% | -5.8% | -6.5% | -46.24 |
| 60 s | 4000 | 24% | -6.0% | -5.7% | -48.31 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
