# Wallet-analyse pump.fun — 2026-09-11 16:04 UTC

## Kort antwoord

- Geluk-toets: 26 van 3282 wallets scoren beter dan de beste wallet in een wereld van puur geluk (echte #1 t=9.87, geluk-grens 4.91).
- Persistentie: de top 20 uit helft A haalde in helft B gemiddeld +4.3% per positie (alle wallets: -12.5%; 12 van 19 actieve toppers bleven winstgevend).
- Kopiëren buiten de steekproef, EV per trade na onze kosten: 0 s: -14.3%, 2 s: -16.8%, 10 s: -17.9%, 60 s: -21.0% (drempel uit het bouwplan: +3%).

## Dekking van de data

- Periode: 2026-09-10 13:48 UTC → 2026-09-11 16:03 UTC (26.3 uur), helft A/B-grens: 2026-09-11 02:56 UTC
- 1684507 trades, 10552 tokens, 104760 wallets, 547229 posities (447031 geopend vanaf ≥ $7k, 100198 eerder)
- Posities zonder verkoop binnen de data (gewaardeerd op laatste curveprijs): 60123
- Alle trades (ook onder $7k) gelogd sinds: 2026-09-11 08:47 UTC

## Wie wint het geld (posities vanaf ≥ $7k)

| type | wallets | posities | winst gesloten (SOL) | + verlies op onverkochte (SOL) | incl. papieren winst (SOL) | verkoop oude voorraad (SOL) | posities < $7k | winst < $7k (SOL) |
|---|---|---|---|---|---|---|---|---|
| vroege_houder | 6396 | 4480 | -24.53 | -55.00 | +307.29 | 20625.91 | 3376 | +412.07 |
| swing | 550 | 5871 | -233.43 | -315.96 | -141.95 | 29.46 | 1097 | -2.14 |
| dev | 785 | 2599 | +220.36 | -591.81 | +150.77 | 4008.82 | 2080 | +131.71 |
| bot_hf | 1870 | 96366 | -232.36 | -1182.38 | +1508.01 | 6848.65 | 35390 | +785.26 |
| scalper | 14495 | 213687 | -6169.26 | -7747.07 | +7454.96 | 6508.85 | 24756 | +130.97 |
| incidenteel | 80664 | 124028 | -4798.81 | -8326.18 | +5671.69 | 6508.74 | 33499 | +1455.17 |

Wallets met ≥ 10 posities: 7942, waarvan winstgevend: 23%. De top 1% winnaars pakt 34% van alle winst op gesloten posities. Som over alle gesloten posities (na pump-fee): -11238.03 SOL.

Types: dev = handelt vooral eigen tokens; bot_hf = mediane houdtijd < 15 s of ≥ 20 posities per actief uur; vroege_houder = verkoopt vooral voorraad die vóór $7k gekocht is (snipers/bundlers); scalper = houdtijd 15 s–10 min; swing = ≥ 10 min; incidenteel = minder dan 5 posities. Papieren winst = posities zonder verkoop gewaardeerd op de laatste curveprijs; dat overschat, want niet iedereen kan tegelijk tegen die prijs verkopen. Alle ranglijsten en toetsen gebruiken daarom de voorzichtige winst.

## Top 20 beste traders (streng gefilterd)

Filters: ≥ 20 posities, geen dev, winst in beide helften, nog winst zonder beste trade. Gerangschikt op t: hoeveel standaardfouten hun posities beter zijn dan vergelijkbare posities (zelfde uur, tokenleeftijd en marketcap bij instap). Rendement afgekapt op -100%/+300%, zodat één moonshot niet domineert. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [ssss…Q57E](https://solscan.io/account/ssssswdk4RR8HqkE3uwUWzDbd6mXFTTPjcXBKNzQ57E) | bot_hf | 3189 (26) | 38% | +3.45 | +2.44 | +0% | 17.2 | ja | 19 s | +2.29 / +1.16 |
| 2 | [Bd8N…SpTF](https://solscan.io/account/Bd8Nqy2c28HnJJdifqg6Ea7gCAdPkg5H7f4HXzFdSpTF) | bot_hf | 1396 (5) | 63% | +2.68 | +2.61 | +7% | 15.86 | ja | 4 s | +1.62 / +1.06 |
| 3 | [Hx44…R9GJ](https://solscan.io/account/Hx44ecKZzK2UqZfVSxBp6B46jLBc2KGUwp4x9bLoR9GJ) | bot_hf | 1024 (19) | 58% | +2.08 | +1.94 | +5% | 12.0 | ja | 4 s | +1.38 / +0.70 |
| 4 | [GjKj…EB1c](https://solscan.io/account/GjKjTmzuoAMdxmKHJpQp9PTJLNuvN1SBXAEARr4GEB1c) | bot_hf | 666 (18) | 42% | +1.40 | +0.98 | +2% | 10.28 | ja | 60 s | +0.23 / +1.17 |
| 5 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 29 (0) | 72% | +16.57 | +14.60 | +67% | 9.68 | ja | 71 s | +13.47 / +3.11 |
| 6 | [8NsB…c5TJ](https://solscan.io/account/8NsBPSP4p4i3QcUgscLd1Y1PJqC7aobbQsZCU7Xrc5TJ) | bot_hf | 2023 (14) | 63% | +0.32 | +0.30 | +3% | 9.1 | nee | 4 s | +0.17 / +0.15 |
| 7 | [5Eu4…HAX3](https://solscan.io/account/5Eu4myQ55U5EN1KFEzp1xdQeRLXwU6iDNkCMAo7THAX3) | bot_hf | 867 (4) | 53% | +0.47 | +0.38 | +1% | 8.79 | nee | 10 s | +0.15 / +0.32 |
| 8 | [B7Sc…zjL2](https://solscan.io/account/B7ScStbz4Ru9SRtDirori9DjjJe43UWGpfYmTEhwzjL2) | bot_hf | 221 (1) | 60% | +4.46 | +3.63 | +8% | 8.59 | ja | 1 s | +1.39 / +3.07 |
| 9 | [FSz6…4BZX](https://solscan.io/account/FSz6mptAxKrjDjaJYQiGiCGGwsxL4WgWjsh9sGhw4BZX) | scalper | 449 (4) | 44% | +5.60 | +4.56 | +4% | 8.55 | ja | 31 s | +4.01 / +1.58 |
| 10 | [7boc…doWL](https://solscan.io/account/7bocByUyoecXdt1WTc2Sw5ZihWzap6Ho6JzS3ZnCdoWL) | scalper | 41 (0) | 54% | +13.51 | +9.89 | +49% | 8.42 | ja | 20 s | +11.34 / +2.17 |
| 11 | [Cxkx…VjV8](https://solscan.io/account/CxkxCQYLWVRStkWwdCcsAX6BWcPnMeKGQ3zm2m6jVjV8) | bot_hf | 563 (19) | 46% | +7.13 | +5.80 | +3% | 8.23 | nee | 2 min | +4.96 / +2.18 |
| 12 | [ceBa…e8nj](https://solscan.io/account/ceBaMgQ76Vc7eUYt6fgG6Lh2TGcbAe5PjfcDrHve8nj) | scalper | 439 (1) | 48% | +3.79 | +3.42 | +3% | 8.22 | nee | 70 s | +3.02 / +0.77 |
| 13 | [4RMb…2tvb](https://solscan.io/account/4RMb8vyjiFXZ6WGrggNkVt721Ybd1FLKsTA35Hic2tvb) | bot_hf | 371 (5) | 69% | +3.03 | +2.78 | +3% | 8.05 | ja | 12 s | +1.71 / +1.32 |
| 14 | [8fSt…Dcud](https://solscan.io/account/8fStGV461vNqwhmQkvYvTFEYkxT4dKqNsyepgtFFDcud) | bot_hf | 348 (6) | 71% | +3.47 | +3.21 | +3% | 7.92 | ja | 11 s | +2.74 / +0.73 |
| 15 | [9qto…deWh](https://solscan.io/account/9qtoxCHwfjwKy2uLus3vtehGE7Xiybpf8mkM5gykdeWh) | bot_hf | 720 (9) | 50% | +1.11 | +1.07 | +9% | 7.84 | nee | 4 s | +0.80 / +0.31 |
| 16 | [ADgm…7cug](https://solscan.io/account/ADgmHHFYmqTHm8n6EBWMBniiKJKj7g86jCXSabBs7cug) | scalper | 29 (0) | 66% | +11.36 | +9.35 | +44% | 7.6 | ja | 68 s | +7.88 / +3.48 |
| 17 | [3H7x…Reso](https://solscan.io/account/3H7xDiUm8MEb144KuUvRVaTL43LJVHwLAZTqLL5jReso) | scalper | 28 (0) | 54% | +11.37 | +9.32 | +43% | 7.35 | ja | 63 s | +8.92 / +2.45 |
| 18 | [5mbo…nJdJ](https://solscan.io/account/5mbo1CogP1VEyHExZCkaegSwXwdrbdomQJSZTEHSnJdJ) | bot_hf | 171 (1) | 58% | +3.65 | +2.13 | +4% | 7.29 | ja | 9 s | +0.16 / +3.48 |
| 19 | [4wbr…gpVq](https://solscan.io/account/4wbrLxXe4pwZe1u4g56BcKBN8uWi8xNoqwwN5tktgpVq) | scalper | 306 (2) | 57% | +1.11 | +1.04 | +5% | 7.2 | nee | 60 s | +0.72 / +0.39 |
| 20 | [BRHa…bgTo](https://solscan.io/account/BRHacVMrBcYBvBscAu571q94bwkUKugPFp4nYPWVbgTo) | scalper | 28 (0) | 57% | +11.10 | +9.02 | +41% | 7.07 | ja | 62 s | +7.43 / +3.67 |

## Top 20 op winst (zonder filters, ter vergelijking)

Zo werken de meeste 'smart money'-lijsten. Winst is voorzichtig gerekend: bij posities zonder verkoop telt verlies mee, papieren winst niet.

| # | wallet | type | pos. (open) | winkans | winst SOL | zonder beste | ROI | t | boven geluk | med. houdtijd | winst A / B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [7ufm…VsmL](https://solscan.io/account/7ufmve7ZSFCzuNcKRunYrGtyb2Ka1MXzkWwf7jZhVsmL) | dev | 5 (0) | 100% | +170.06 | +134.60 | +227% | 12.82 | nee | 12 s | +0.00 / +170.06 |
| 2 | [2CQg…ctFG](https://solscan.io/account/2CQgjcdNEo7WtbQLpJTAVcC3Ga61pNvRDTgP5grzctFG) | vroege_houder | 118 (0) | 64% | +45.29 | +39.93 | +11% | 5.87 | nee | 15 s | +21.91 / +23.39 |
| 3 | [Fqam…zrve](https://solscan.io/account/FqamE7xrahg7FEWoByrx1o8SeyHt44rpmE6ZQfT7zrve) | scalper | 102 (5) | 54% | +31.78 | +24.58 | +14% | 5.86 | nee | 94 s | +31.17 / +0.61 |
| 4 | [57st…4DyZ](https://solscan.io/account/57stAMFvwctAjkBS76RXGoK4QKyS1QoxbGMbzFFe4DyZ) | bot_hf | 89 (1) | 79% | +27.86 | +25.71 | +13% | 5.53 | nee | 9 s | +19.98 / +7.87 |
| 5 | [FKdm…kemf](https://solscan.io/account/FKdmT4MqPVTbDw2B3nncXhBjrUgmUE2vhQGMzb7fkemf) | vroege_houder | 12 (0) | 58% | +22.59 | +14.23 | +25% | 2.56 | nee | 31 s | -4.42 / +27.01 |
| 6 | [68DY…qkaX](https://solscan.io/account/68DYn5Xfo3ZneMg6pdVpu3eNzL1M7K4dDHACKaBmqkaX) | scalper | 7 (0) | 86% | +20.96 | +13.93 | +32% | 2.78 | nee | 73 s | +13.89 / +7.06 |
| 7 | [FM1Y…Jgke](https://solscan.io/account/FM1YCKED2KaqB8Uat8aB1nsffR1vezr7s6FAEieXJgke) | dev | 5 (0) | 20% | +20.83 | -3.01 | +63% | -0.27 | nee | 8 min | +21.46 / -0.62 |
| 8 | [Dd2n…KanL](https://solscan.io/account/Dd2nB2vD1XvDsdKqhtmCuh1q6tzWckkqLq3JubznKanL) | vroege_houder | 45 (2) | 60% | +19.07 | +16.36 | +13% | 4.14 | nee | 19 s | +11.96 / +7.11 |
| 9 | [CAvv…z8vT](https://solscan.io/account/CAvvAFNRfXDWTTDqwgxb9qSyYT8fTuTXWSFwL7Jsz8vT) | scalper | 65 (0) | 49% | +18.98 | +15.72 | +23% | 6.28 | ja | 16 s | +12.42 / +6.55 |
| 10 | [2CHr…NE71](https://solscan.io/account/2CHrnc2LyagAbMaMFgthiDWh7ZZ9zT9TF8WEJf7MNE71) | scalper | 12 (0) | 75% | +17.78 | +14.91 | +42% | 3.57 | nee | 18 s | +6.80 / +10.98 |
| 11 | [66Jy…xuzm](https://solscan.io/account/66JyEVRCx4uYnwwzcqmW6Ji2cygp6ubBhEciSqnkxuzm) | scalper | 32 (0) | 66% | +17.72 | +13.79 | +12% | 3.18 | nee | 33 s | +7.76 / +9.96 |
| 12 | [D4py…thqu](https://solscan.io/account/D4pycXUXjs7FEWES39RMwfrs2E5LsbxGm5asCX6Tthqu) | scalper | 43 (0) | 77% | +17.68 | +15.35 | +12% | 3.94 | nee | 24 s | +13.32 / +4.36 |
| 13 | [D4vx…BdY2](https://solscan.io/account/D4vxtAbxz2F6i7KW5pAPoiatYszvXPJuZgEikE3yBdY2) | bot_hf | 7 (0) | 57% | +17.52 | +2.96 | +72% | 4.14 | nee | 13 s | +1.05 / +16.46 |
| 14 | [7kDp…Y1sC](https://solscan.io/account/7kDpxMJDNvPXhdd4XSQfgmYPGo5asd9eHf2gLGDZY1sC) | scalper | 11 (0) | 73% | +17.30 | +12.58 | +20% | 2.97 | nee | 25 s | +17.30 / +0.00 |
| 15 | [4vw5…9Ud9](https://solscan.io/account/4vw54BmAogeRV3vPKWyFet5yf8DTLcREzdSzx4rw9Ud9) | scalper | 65 (9) | 48% | +17.05 | +12.25 | +9% | 3.87 | nee | 111 s | +17.18 / -0.13 |
| 16 | [75Hc…g74J](https://solscan.io/account/75Hc8hVYZuCnSEN4kNbK4BbWi3kogjirBfjTWgKMg74J) | dev | 11 (0) | 27% | +17.01 | -69.58 | +7% | -0.07 | nee | 20 s | +0.00 / +17.01 |
| 17 | [BbjK…aX8s](https://solscan.io/account/BbjK3rdn3rJeK2DxpbUDAKaXQ3JgJ27qNtyfNuesaX8s) | scalper | 29 (0) | 72% | +16.57 | +14.60 | +67% | 9.68 | ja | 71 s | +13.47 / +3.11 |
| 18 | [4Ddr…9nNh](https://solscan.io/account/4DdrfiDHpmx55i4SPssxVzS9ZaKLb8qr45NKY9Er9nNh) | vroege_houder | 33 (3) | 91% | +15.80 | +14.42 | +16% | 3.35 | nee | 16 s | +11.15 / +4.65 |
| 19 | [2KP9…PURD](https://solscan.io/account/2KP9miexioqgNbjPwysggcbi3sKqhH8JsPaDmFxRPURD) | bot_hf | 15 (0) | 73% | +15.04 | +9.93 | +21% | 3.33 | nee | 10 s | +15.01 / +0.03 |
| 20 | [Cv5G…bbVL](https://solscan.io/account/Cv5GgkpXvtXcsrMcKCJvx46BpMjiM61mpPU1j8RbbbVL) | scalper | 60 (2) | 45% | +14.99 | +11.67 | +16% | 5.36 | nee | 80 s | +11.92 / +3.08 |

## Geluk-toets

Populatie: 3282 wallets met ≥ 20 posities, 100 husselrondes.

| rang | echte t | geluk mediaan | geluk 95% |
|---|---|---|---|
| #1 | 9.87 | 4.04 | 4.91 |
| #10 | 6.77 | 3.1 | 3.33 |
| #20 | 5.14 | 2.77 | 2.94 |

Wallets boven de 95%-grens van de beste 'geluks-wallet' (t > 4.91): **26**. Let op: deze toets is nodig maar niet voldoende. Husselen negeert dat wallets op dezelfde tokens zitten en dat hun eigen aankopen de prijs bewegen; hij valt dus eerder te gunstig uit. De beslissende toets is de kopieer-simulatie buiten de steekproef.

## Persistentie: gekozen op helft A, gemeten op helft B

| groep | actief in B | posities | winkans | gem. rend. | med. rend. | winst SOL |
|---|---|---|---|---|---|---|
| top 20 op t (A) | 19/20 | 4781 | 49% | +4.3% | -0.3% | +26.16 |
| top 20 op winst (A) | 18/20 | 382 | 52% | +5.1% | +0.6% | +64.48 |
| alle wallets | – | 160889 | 31% | -12.5% | – | – |
| willekeurige 20 (mediaan / p95) | – | – | – | -4.9% / +2.9% | – | – |

Rangcorrelatie rendement A vs B (wallets met ≥ 10 posities in beide helften: 1259): ρ = 0.42. Rond 0 betekent: goed in A zegt niets over B.

## Kopieer-simulatie (0,2 SOL, PumpPortal-fees, verkopen als de wallet ≥ 50% verkoopt)

**buiten steekproef: top 20 uit A, gekopieerd in B** — posities zonder verkoopsignaal binnen de data: 56

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 4781 | 28% | -14.3% | -8.1% | -136.45 |
| 2 s | 4781 | 23% | -16.8% | -9.8% | -160.56 |
| 10 s | 4781 | 22% | -17.9% | -10.1% | -170.88 |
| 60 s | 4781 | 19% | -21.0% | -8.9% | -200.66 |

**binnen steekproef: top 20 beste traders, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 115

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 12908 | 30% | -18.0% | -12.1% | -463.68 |
| 2 s | 12908 | 24% | -21.6% | -15.7% | -557.49 |
| 10 s | 12908 | 21% | -23.7% | -16.4% | -612.92 |
| 60 s | 12908 | 16% | -30.3% | -16.5% | -781.50 |

**binnen steekproef: top 20 op winst, hele periode (optimistisch)** — posities zonder verkoopsignaal binnen de data: 14

| vertraging | n | winkans | EV per trade | mediaan | winst SOL |
|---|---|---|---|---|---|
| 0 s | 766 | 40% | +4.9% | -4.6% | +7.57 |
| 2 s | 766 | 26% | -7.3% | -11.3% | -11.18 |
| 10 s | 766 | 25% | -8.0% | -8.8% | -12.17 |
| 60 s | 766 | 22% | -8.1% | -6.1% | -12.34 |

## Beperkingen

- Trades worden gelogd voor tokens die de bot zag ontstaan, tot ongeveer 1 uur na creatie en tot migratie naar PumpSwap. Wat daarna gebeurt is onzichtbaar; open posities zijn gewaardeerd op de laatste curveprijs.
- Tot de uitbreiding van de logging zijn alleen trades vanaf het moment dat een token ≥ $7k marketcap haalde bewaard. Aankopen daarvóór (snipers, bundlers) zijn dan niet als positie te zien, alleen hun latere verkopen ('vroege_houder').
- Na een herstart van de bot stopt het volgen van tokens die al bestonden; die posities lijken open en zijn gewaardeerd op de laatst geziene prijs.
- Winst per wallet is na pump-fee (1,25% per kant), maar zonder hun terminal- en prioriteitskosten. Voor hoogfrequente bots is de werkelijke winst dus lager.
- Eén wallet is niet één persoon: slimme handelaren verspreiden over veel wallets en wisselen vaak. Een wallet die verdwijnt, is niet te volgen.
- De kopieer-simulatie negeert mislukte transacties, MEV en het koerseffect van andere kopieerders; de echte uitkomst is eerder slechter.
