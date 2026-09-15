# Wallet-analyse pump.fun — 2026-09-15 08:38 UTC

## Kort antwoord

- Geluk-toets: 76 van 7650 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=31.28, geluk-grens 5.3).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +6.1% per positie (alle wallets: -11.1%; 19 van 20 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -11.9%, 2 s: -15.4%, 10 s: -16.3%, 60 s: -19.2% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-12 08:26 UTC → 2026-09-15 08:26 UTC (72.0 uur), helft A/B-grens: 2026-09-13 20:26 UTC
- 7299848 trades, 75943 tokens, 209933 wallets, 2249889 posities (905040 geopend vanaf ≥ $7k, 1344849 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 124050
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 7310 | 3402 | +133.96 | +79.60 | +349.82 | 7522.22 | 18376 | +1885.65 |
| dev | 2191 | 4505 | +2173.78 | +17.38 | +2650.64 | 41.42 | 16669 | +2363.97 |
| bot_hf | 3232 | 222457 | +807.86 | -346.37 | +5284.61 | 8918.03 | 402659 | +7007.60 |
| swing | 2057 | 19117 | -1055.55 | -1331.65 | -53.92 | 53.18 | 19675 | +19.32 |
| incidenteel | 169732 | 175168 | -3904.85 | -6877.25 | +36172.18 | 1848.34 | 341595 | +15852.88 |
| scalper | 25411 | 480391 | -13070.93 | -16276.88 | +23295.50 | 1170.44 | 545875 | +3309.41 |

Wallets met ≥ 10 posities: 16287, waarvan winstgevend: 22%. De top 1% winnaars pakt 44% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -14915.73 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.44 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [omeg…XAfq](https://solscan.io/account/omegoMAe1AMY5MFKQQr3JwXVy8F4eCvmBAfcpo8XAfq) | bot_hf | 7481 (90) | 46% | +62.59 | +61.46 | +1% | 25.47 | ja | 26 s | +25.83 / +36.76 |
| 3 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 4076 (18) | 60% | +9.24 | +9.06 | +7% | 23.46 | ja | 4 s | +5.68 / +3.56 |
| 4 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 7335 (66) | 40% | +13.90 | +12.91 | +1% | 22.67 | ja | 17 s | +2.85 / +11.05 |
| 5 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 2857 (55) | 58% | +4.20 | +3.98 | +3% | 22.6 | ja | 4 s | +2.68 / +1.52 |
| 6 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.68 | ja | 2 min | +112.67 / +421.81 |
| 7 | [FCQS…woWB](https://solscan.io/account/FCQSYHYnbvgTfVpDineaYZZWfqDYTswNhXNJ9gmTwoWB) | scalper | 450 (76) | 55% | +0.49 | +0.47 | +29% | 19.47 | ja | 23 s | +0.06 / +0.43 |
| 8 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 74 (0) | 92% | +826.24 | +786.34 | +66% | 17.09 | ja | 7 s | +294.19 / +532.05 |
| 9 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2768 (44) | 48% | +83.03 | +79.80 | +3% | 16.97 | ja | 19 s | +28.11 / +54.92 |
| 10 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.12 | ja | 2 min | +94.54 / +274.04 |
| 11 | [ssss…xe7d](https://solscan.io/account/sssssDdMNAWKingjpEojkTNdVuZrBe7FsJLaGtexe7d) | bot_hf | 3725 (56) | 37% | +58.03 | +51.08 | +2% | 15.61 | ja | 28 s | +19.20 / +38.83 |
| 12 | [GVVP…zKVp](https://solscan.io/account/GVVP8N7jnxgr3QdtR461bsuCNNQmuNu4DBW2Ab4tzKVp) | bot_hf | 2326 (9) | 50% | +15.07 | +13.65 | +1% | 15.54 | ja | 46 s | +7.68 / +7.39 |
| 13 | [7evu…tqbX](https://solscan.io/account/7evudm7mkommXaFbyrC9AoGNfkqcTdUGZAU25ZTytqbX) | bot_hf | 2555 (13) | 49% | +11.24 | +10.42 | +3% | 14.4 | ja | 30 s | +0.46 / +10.78 |
| 14 | [SQHK…7TZq](https://solscan.io/account/SQHK48QT8SY1vYN44iXji7wQ6CJek8AjfX6mBp47TZq) | bot_hf | 1933 (89) | 44% | +9.20 | +5.29 | +0% | 13.19 | ja | 42 s | +1.75 / +7.45 |
| 15 | [Esae…VTG2](https://solscan.io/account/EsaeTGMeyipnzTUTWZGpHZGoFh9cFr9YwLjX4kybVTG2) | scalper | 24 (2) | 83% | +27.30 | +19.47 | +166% | 13.03 | ja | 106 s | +10.48 / +16.82 |
| 16 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | bot_hf | 1750 (3) | 40% | +8.70 | +6.71 | +2% | 12.8 | ja | 21 s | +2.27 / +6.42 |
| 17 | [CrAz…MCoj](https://solscan.io/account/CrAzYtsUvb4F1L8uwhGZXkMhRiMSW1P7qp4FA4QFMCoj) | scalper | 798 (158) | 48% | +0.63 | +0.61 | +19% | 12.35 | ja | 30 s | +0.04 / +0.60 |
| 18 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 1459 (26) | 45% | +2.31 | +2.04 | +2% | 12.17 | ja | 58 s | +1.75 / +0.57 |
| 19 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 2111 (15) | 54% | +2.19 | +2.02 | +2% | 11.46 | ja | 10 s | +0.77 / +1.42 |
| 20 | [B8dc…Qc3i](https://solscan.io/account/B8dc6dVcvLyAZr1jFfaVCT4v8vWi6KBCjz5Z6LdQQc3i) | scalper | 23 (2) | 83% | +18.12 | +12.77 | +81% | 11.37 | ja | 74 s | +9.35 / +8.77 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Ecwz…CJwp](https://solscan.io/account/Ecwzx5QjW6zzycpEgDZWehYn738bHsaCJAA73WaZCJwp) | scalper | 53 (1) | 87% | +1542.42 | +1466.25 | +255% | 31.44 | ja | 2 min | +366.88 / +1175.54 |
| 2 | [7qjD…cR3E](https://solscan.io/account/7qjDDvNAp9gdKxQ3ZGBYm4TyU1f7jpxQfK8hZswHcR3E) | bot_hf | 74 (0) | 92% | +826.24 | +786.34 | +66% | 17.09 | ja | 7 s | +294.19 / +532.05 |
| 3 | [CqHA…BhHU](https://solscan.io/account/CqHAAwRg4yfGFy4Qp8WC1wUPCxxYYDAAm4LaBsD5BhHU) | scalper | 54 (1) | 72% | +534.47 | +502.25 | +125% | 20.68 | ja | 2 min | +112.67 / +421.81 |
| 4 | [Epij…Y62C](https://solscan.io/account/Epij2QYgr9xpwaLoMwaNBvLbpgbmc1JrfHTLxHJ3Y62C) | scalper | 53 (0) | 74% | +368.58 | +348.07 | +94% | 16.12 | ja | 2 min | +94.54 / +274.04 |
| 5 | [Cvig…4Y8Z](https://solscan.io/account/CvigqGTgZ837hMSG6vSgE2NnBQEeEXdKQ2p5p4tn4Y8Z) | scalper | 53 (1) | 60% | +188.30 | +171.36 | +40% | 8.4 | ja | 3 min | +41.26 / +147.04 |
| 6 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | scalper | 349 (10) | 57% | +146.17 | +112.22 | +11% | 7.77 | ja | 16 s | +88.37 / +57.80 |
| 7 | [gVDX…dAkx](https://solscan.io/account/gVDXhoGbePACvSqN7CZBtQXFW9eyJwsgudPEwSydAkx) | dev | 9 (1) | 89% | +145.19 | +118.40 | +85% | 6.94 | nee | 9 s | +38.53 / +106.66 |
| 8 | [3aK9…V2Bj](https://solscan.io/account/3aK9HWN81oG56KcsLENEg39E8CoKYBv15vNzXgfiV2Bj) | scalper | 10 (1) | 90% | +109.84 | +81.15 | +139% | 9.86 | nee | 4 min | +0.00 / +109.84 |
| 9 | [26A1…LDtv](https://solscan.io/account/26A17NuKXgV4YfYXdidp7fvo9g4QGFfVDz5QN2aeLDtv) | bot_hf | 66 (0) | 67% | +100.57 | +81.81 | +39% | 7.87 | ja | 11 s | +24.87 / +75.70 |
| 10 | [14W6…CGJp](https://solscan.io/account/14W6L6zVVBbstgTktiR7Qv6z75yPcXij3aS7mqtHCGJp) | dev | 9 (1) | 89% | +92.66 | +64.53 | +20% | 3.14 | nee | 118 s | +0.00 / +92.66 |
| 11 | [5YRg…Uzij](https://solscan.io/account/5YRgrP3mjGzrzirYYN5HAQH19cTYREYwGxW6XRJQUzij) | vroege_houder | 31 (5) | 74% | +90.39 | +80.47 | +42% | 6.0 | ja | 34 s | +84.67 / +5.72 |
| 12 | [6ePb…tHHw](https://solscan.io/account/6ePbEvTDFGPembAtY1vwLF4CWbTWKFisUE2G2k53tHHw) | dev | 11 (0) | 100% | +88.31 | +55.26 | +124% | 8.66 | nee | 7 s | +44.68 / +43.63 |
| 13 | [64hP…4AEz](https://solscan.io/account/64hP97Bwr5PubotcTeGgfhkFrGiLVVxT2kVo9M9b4AEz) | bot_hf | 2768 (44) | 48% | +83.03 | +79.80 | +3% | 16.97 | ja | 19 s | +28.11 / +54.92 |
| 14 | [76bg…Rnzh](https://solscan.io/account/76bg6fHvkavukBNggSxTpJX9quDEWTsfmH42VFsRnzh) | bot_hf | 10 (1) | 90% | +82.81 | +66.29 | +124% | 9.41 | nee | 9 s | +8.25 / +74.56 |
| 15 | [Biue…ctDJ](https://solscan.io/account/Biuetdz3z9Wf6XCajsS3HxdwyipV976KQwFzVsB3ctDJ) | dev | 9 (3) | 56% | +77.34 | +57.44 | +104% | 4.27 | nee | 7 s | +0.00 / +77.34 |
| 16 | [7VsG…iUSX](https://solscan.io/account/7VsGe3TJCjBWzetPVvwmaWZjzDMJNNuQYkjLYmYfiUSX) | scalper | 145 (0) | 77% | +75.69 | +71.21 | +21% | 8.94 | ja | 94 s | +28.33 / +47.37 |
| 17 | [9gpd…2M9L](https://solscan.io/account/9gpdgZTNxvSrbiBcFM8aWdCUBvQrcprQR4TmsJLU2M9L) | bot_hf | 10 (0) | 100% | +73.80 | +62.99 | +73% | 5.39 | nee | 6 s | +10.80 / +62.99 |
| 18 | [76rd…j6SG](https://solscan.io/account/76rdHqaie4ooQ8ErhAgDyeifgVYauG2tBG2ofroNj6SG) | bot_hf | 48 (2) | 85% | +73.17 | +64.58 | +26% | 4.94 | nee | 14 s | +16.02 / +57.14 |
| 19 | [2cBN…XD9k](https://solscan.io/account/2cBNF8Ci1FudMpR3hCCb49B5gDDQETd4kUK4PGUEXD9k) | scalper | 17 (0) | 94% | +69.17 | +46.35 | +38% | 4.09 | nee | 33 s | +50.13 / +19.03 |
| 20 | [4H1N…z2D7](https://solscan.io/account/4H1NVREBvjzbyzqTUrbSgfQbvJm2Cx7mVNXBeBfDz2D7) | scalper | 10 (1) | 80% | +67.21 | +47.91 | +92% | 6.98 | nee | 4 min | +0.00 / +67.21 |

## Geluk-toets

Populatie: 7650 wallets met ≥ 20 posities, 77 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 31.28 | 4.64 | 5.3 |
| #10 | 14.2 | 3.46 | 3.67 |
| #20 | 9.23 | 3.14 | 3.31 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 5.3): **76**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 20/20 | 20225 | 49% | +6.1% | -0.1% | +2583.59 |
| top 20 op winst (A) | 20/20 | 7357 | 49% | +6.2% | +0.0% | +2991.78 |
| alle wallets | – | 544810 | 31% | -11.1% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -5.5% / +1.3% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 3543): ρ = 0.531. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 215

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 20225 | 29% | -11.9% | -7.2% | -482.08 |
| 2 s | 20225 | 24% | -15.4% | -9.0% | -622.47 |
| 10 s | 20225 | 22% | -16.3% | -8.8% | -659.63 |
| 60 s | 20225 | 19% | -19.2% | -7.7% | -775.92 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 679

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 41905 | 29% | -12.5% | -8.1% | -1047.90 |
| 2 s | 41905 | 24% | -15.6% | -9.8% | -1310.10 |
| 10 s | 41905 | 23% | -16.8% | -9.6% | -1408.41 |
| 60 s | 41905 | 19% | -19.6% | -8.1% | -1639.40 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 61

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 3789 | 36% | +2.5% | -5.9% | +18.80 |
| 2 s | 3789 | 30% | -6.1% | -8.2% | -46.38 |
| 10 s | 3789 | 29% | -5.9% | -6.6% | -44.55 |
| 60 s | 3789 | 24% | -6.2% | -5.7% | -46.84 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
